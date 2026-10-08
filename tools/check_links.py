#!/usr/bin/env python3
"""check_links.py — verifies every local href/src in the repo resolves to a file.

Usage:  python tools/check_links.py [root]
Exit 1 when broken links are found. External (http/https/mailto) and
pure-anchor (#x) targets are ignored.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

ATTR = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
MDLINK = re.compile(r"""\[[^\]]*\]\(([^)\s]+)\)""")

SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".woff", ".woff2", ".ttf"}


def targets(path: Path):
    if path.suffix.lower() in SKIP_EXT:
        return
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    if path.suffix.lower() in (".html", ".htm", ".md"):
        for m in ATTR.finditer(text):
            yield m.group(1), text.count("\n", 0, m.start()) + 1
    if path.suffix.lower() == ".md":
        for m in MDLINK.finditer(text):
            yield m.group(1), text.count("\n", 0, m.start()) + 1


def main():
    broken, checked = [], 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        for raw, line in targets(path):
            t = raw.strip()
            if not t or t.startswith(("http://", "https://", "mailto:", "javascript:", "data:")):
                continue
            if t.startswith("#"):
                continue
            t = t.split("#", 1)[0].split("?", 1)[0]
            if not t:
                continue
            checked += 1
            dest = (path.parent / t).resolve()
            if not dest.exists():
                broken.append(f"{path.relative_to(ROOT)}:{line} -> {raw}")
    print(f"checked {checked} local links in {ROOT}")
    if broken:
        print(f"BROKEN ({len(broken)}):")
        for b in broken:
            print("  " + b)
        return 1
    print("OK: no broken links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
