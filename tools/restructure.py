#!/usr/bin/env python3
"""restructure.py — one-shot migration to the v1.0 repository layout.

Moves files/directories to their new homes and rewrites every local
href/src in .html/.md files by *recomputing* the relative path from the
file's new location to its target's new location. Idempotent: running it
twice leaves links untouched (old and new resolution then coincide).

Layout produced:
    site/      web pages (index, grammar, lessons, translator)
    spec/      Beluma Language Standard 1.0
    lexicon/   h.txt
    engine/    beluma.js
    course/    (was lessons/)
    library/   (was literature/)
    canon/ exams/ teacher/ tools/   unchanged
"""
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# old path (relative to ROOT) -> new path (relative to ROOT)
MOVES = {
    "index.html": "site/index.html",
    "grammar.html": "site/grammar.html",
    "lessons.html": "site/lessons.html",
    "translator.html": "site/translator.html",
    "h.txt": "lexicon/h.txt",
    "beluma.js": "engine/beluma.js",
    "lessons": "course",
    "literature": "library",
}

# logical asset remapping used when resolving link targets
ASSET_MAP = {
    "index.html": "site/index.html",
    "grammar.html": "site/grammar.html",
    "lessons.html": "site/lessons.html",
    "translator.html": "site/translator.html",
    "h.txt": "lexicon/h.txt",
    "beluma.js": "engine/beluma.js",
    "lessons/": "course/",
    "literature/": "library/",
    # dead reference fixed during migration
    "ROADMAP.md": "spec/Beluma-Standard-v1.0.html",
}

LINK = re.compile(r"""((?:href|src)\s*=\s*["'])([^"']+)(["'])""", re.I)
MDLINK = re.compile(r"""\(([^()\s]+(?:\.[A-Za-z0-9]+)?(?:#[^()\s]*)?)\)""")
TOUCH_EXT = {".html", ".htm", ".md"}


def mapped(rel: str) -> str:
    """Apply the asset map to a ROOT-relative path."""
    rel = rel.replace("\\", "/")
    if rel in ASSET_MAP:
        return ASSET_MAP[rel]
    for old, new in ASSET_MAP.items():
        if rel.startswith(old):
            return new + rel[len(old):]
    return rel


def norm(path: Path) -> str:
    return Path(os.path.normpath(str(path))).as_posix()


def relocate():
    """Move files/dirs according to MOVES (dirs first are fine: all top-level)."""
    for old, new in MOVES.items():
        src, dst = ROOT / old, ROOT / new
        if src.exists() and not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"moved {old} -> {new}")


def new_location_of(old_rel: str) -> Path:
    """Where a file that *was* at old_rel lives now (before its own content rewrite)."""
    p = norm(Path(old_rel))
    if p in MOVES:
        return ROOT / MOVES[p]
    for old, new in MOVES.items():
        if p.startswith(old + "/"):
            return ROOT / new / p[len(old) + 1:]
    return ROOT / p


def rewrite_file(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0
    ext = path.suffix.lower()
    if ext not in TOUCH_EXT:
        return 0

    # logical old location of THIS file (to resolve its links the old way)
    rel = path.relative_to(ROOT).as_posix()
    # invert MOVES to find where the file came from
    old_rel = rel
    for old, new in MOVES.items():
        if rel == new:
            old_rel = old
            break
        if rel.startswith(new + "/"):
            old_rel = old + rel[len(new):]
            break
    old_dir = (ROOT / old_rel).parent
    changed = 0

    def fix(target: str) -> str:
        nonlocal changed
        t = target.strip()
        if not t or t.startswith(("http://", "https://", "mailto:", "javascript:", "data:")):
            return target
        if t.startswith("#"):
            return target
        frag = ""
        if "#" in t:
            t, frag = t.split("#", 1)
            frag = "#" + frag
        if not t:
            return target
        # resolve the way it would have resolved BEFORE the move
        old_abs = norm((old_dir / t))
        if old_abs.startswith(".."):        # escapes the repo: leave alone
            return target
        # make it ROOT-relative if inside the repo
        try:
            old_root_rel = os.path.relpath(old_abs, norm(ROOT)).replace("\\", "/")
        except ValueError:
            return target
        new_root_rel = mapped(old_root_rel)
        new_abs = norm(ROOT / new_root_rel)
        rel_new = os.path.relpath(new_abs, norm(path.parent)).replace("\\", "/")
        if rel_new == t and not frag:
            return target
        changed += 1
        return rel_new + frag

    if ext in (".html", ".htm"):
        out = LINK.sub(lambda m: m.group(1) + fix(m.group(2)) + m.group(3), text)
    else:
        def md_sub(m):
            return "(" + fix(m.group(1)) + ")"
        out = MDLINK.sub(md_sub, text)

    if out != text:
        path.write_text(out, encoding="utf-8")
    return changed


# The md2html template hard-codes ../index.html etc., which is wrong for
# pages nested two levels deep. Repair the header nav by label so every
# page points at the real site pages from wherever it lives.
NAV = {
    "Overview": "site/index.html",
    "Grammar": "site/grammar.html",
    "Course": "site/lessons.html",
    "Translator": "site/translator.html",
}
NAV_RE = re.compile(r'<a href="[^"]*">(Overview|Grammar|Course|Translator)</a>')


def repair_nav(path: Path) -> int:
    if path.suffix.lower() not in (".html", ".htm"):
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    fixed = 0

    def sub(m):
        nonlocal fixed
        want = os.path.relpath(
            norm(ROOT / NAV[m.group(1)]), norm(path.parent)
        ).replace("\\", "/")
        if m.group(0) == f'<a href="{want}">{m.group(1)}</a>':
            return m.group(0)
        fixed += 1
        return f'<a href="{want}">{m.group(1)}</a>'

    out = NAV_RE.sub(sub, text)
    if out != text:
        path.write_text(out, encoding="utf-8")
    return fixed


def write_root_redirect():
    p = ROOT / "index.html"
    if p.exists() and 'site/index.html' not in p.read_text(encoding="utf-8", errors="replace")[:400]:
        return
    p.write_text(
        """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url=site/index.html">
<title>Lía Beluma</title>
</head>
<body>
<p style="font-family:sans-serif;padding:2em">Lía Beluma moved to <a href="site/index.html">site/index.html</a>.</p>
</body>
</html>
""",
        encoding="utf-8",
    )
    print("wrote index.html redirect -> site/index.html")


def main():
    relocate()
    total = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        total += rewrite_file(path)
    print(f"rewrote {total} link targets")
    nav = 0
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and ".git" not in path.parts:
            nav += repair_nav(path)
    print(f"repaired {nav} nav links")
    write_root_redirect()


if __name__ == "__main__":
    main()
