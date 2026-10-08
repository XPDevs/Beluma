#!/usr/bin/env python3
"""md2html.py — renders the repo's Markdown into the styled HTML pages.

Canonical port of tools/md2html.js (kept for Node users). Walks the given
directories (default: spec, canon, course, exams, teacher, library),
converts every .md beside it into .html with the site chrome.

Header nav links are computed relative to each page's own depth, so pages
nested two levels deep no longer break (the original template bug).

Usage: python tools/md2html.py [dir ...]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = sys.argv[1:] or ["spec", "canon", "course", "exams", "teacher", "library"]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Lía Beluma</title>
<style>
:root{{--accent:#9b59b6;--dark:#22142b;--text:#333;--border:#e6dceb}}
*{{box-sizing:border-box}}
body{{font-family:'Segoe UI',Roboto,sans-serif;margin:0;background:#faf7fc;color:var(--text);line-height:1.8}}
header{{background:var(--dark);color:#fff;padding:16px 5%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap}}
header .t{{font-weight:800}}
header a{{color:#e6d7ef;text-decoration:none;margin-left:16px;font-weight:600}}
main{{max-width:900px;margin:30px auto;padding:0 18px 60px}}
h1{{color:var(--dark);border-bottom:4px solid var(--accent);padding-bottom:10px}}
h2{{color:var(--accent);text-transform:uppercase;letter-spacing:1px;font-size:1rem;margin-top:42px}}
h3{{color:var(--dark)}}
table{{border-collapse:collapse;width:100%;margin:14px 0}}
th,td{{border:1px solid var(--border);padding:8px 12px;text-align:left;vertical-align:top}}
th{{background:#f3edf8;color:var(--dark)}}
code{{background:#f0e9f4;padding:2px 7px;border-radius:6px;color:#7a3da1}}
pre{{background:#22142b;color:#e6d7ef;padding:14px 18px;border-radius:12px;overflow-x:auto}}
pre code{{background:none;color:inherit;padding:0}}
blockquote{{border-left:5px solid var(--accent);background:#f3edf8;padding:8px 16px;border-radius:0 10px 10px 0;margin:14px 0}}
a{{color:var(--accent)}}
li{{margin:4px 0}}
.navhome{{font-size:.85rem;color:#b8a6c4}}
</style>
</head>
<body>
<header>
  <span class="t">{title}</span>
  <span>{nav}</span>
</header>
<main>
{body}
<p class="navhome">Generated from Markdown by <code>tools/md2html.py</code> · Beluma Language Standard v1.0</p>
</main>
</body>
</html>
"""


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(s: str) -> str:
    out = esc(s)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)

    def link(m):
        text, url = m.group(1), m.group(2)
        if not url.startswith("http"):
            url = re.sub(r"\.md(#[^)]*)?$", r".html\1", url)
        return f'<a href="{url}">{text}</a>'

    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, out)
    return out


def is_table_row(line: str) -> bool:
    body = line.strip().removeprefix("|").removesuffix("|")
    return "|" in body


def is_table_sep(line: str) -> bool:
    t = line.strip()
    return bool(re.match(r"^\|?[\s:|-]+\|?$", t)) and "-" in t


def md2html(md: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    lst = None          # (type, items)
    table = None        # {"head": [...], "rows": [...], "sep": bool}
    fence = False

    def flush_list():
        nonlocal lst
        if not lst:
            return
        out.append(f"<{lst[0]}>")
        out.extend(f"  <li>{it}</li>" for it in lst[1])
        out.append(f"</{lst[0]}>")
        lst = None

    def flush_table():
        nonlocal table
        if not table:
            return
        out.append("<table>")
        if table["head"]:
            out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in table["head"]) + "</tr></thead>")
        out.append("<tbody>")
        for row in table["rows"]:
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
        out.append("</tbody></table>")
        table = None

    def split_cells(t: str):
        t = t.strip()
        t = re.sub(r"^\|", "", t)
        t = re.sub(r"\|$", "", t)
        return [c.strip() for c in t.split("|")]

    while i < len(lines):
        line = lines[i]
        if fence:
            if re.match(r"^\s*```", line):
                out.append("</code></pre>")
                fence = False
            else:
                out.append(esc(line))
            i += 1
            continue
        if re.match(r"^\s*```", line):
            flush_list()
            flush_table()
            out.append("<pre><code>")
            fence = True
            i += 1
            continue
        t = line.strip()
        if t == "":
            flush_list()
            flush_table()
            i += 1
            continue
        if re.match(r"^---+$", t):
            flush_list()
            flush_table()
            out.append("<hr>")
            i += 1
            continue
        h = re.match(r"^(#{1,4})\s+(.*)$", t)
        if h:
            flush_list()
            flush_table()
            out.append(f"<h{len(h.group(1))}>{inline(h.group(2))}</h{len(h.group(1))}>")
            i += 1
            continue
        if t.startswith("> "):
            flush_list()
            flush_table()
            out.append(f"<blockquote>{inline(t[2:])}</blockquote>")
            i += 1
            continue
        if table is not None and is_table_sep(line):
            table["sep"] = True
            i += 1
            continue
        if is_table_row(line):
            flush_list()
            cells = split_cells(t)
            if table is None:
                table = {"head": cells, "rows": [], "sep": False}
            elif table["sep"]:
                table["rows"].append(cells)
            i += 1
            continue
        if re.match(r"^\s{2,}\S", line) and not is_table_row(line):
            cont = t
            if lst and lst[1]:
                lst[1][-1] += " " + inline(cont)
            elif out and out[-1].startswith("<p>") and out[-1].endswith("</p>"):
                out[-1] = out[-1][:-4] + " " + inline(cont) + "</p>"
            else:
                out.append(f"<p>{inline(cont)}</p>")
            i += 1
            continue
        m = re.match(r"^[-*]\s+(.*)$", t)
        if m:
            flush_table()
            if not lst or lst[0] != "ul":
                flush_list()
                lst = ("ul", [])
            lst[1].append(inline(m.group(1)))
            i += 1
            continue
        m = re.match(r"^\d+[.)]\s+(.*)$", t)
        if m:
            flush_table()
            if not lst or lst[0] != "ol":
                flush_list()
                lst = ("ol", [])
            lst[1].append(inline(m.group(1)))
            i += 1
            continue
        flush_list()
        flush_table()
        out.append(f"<p>{inline(t)}</p>")
        i += 1
    flush_list()
    flush_table()
    if fence:
        out.append("</code></pre>")
    return "\n".join(out)


def nav_for(page: Path) -> str:
    import os
    def rel(target):
        return os.path.relpath(ROOT / target, page.parent).replace("\\", "/")
    items = [("Overview", "site/index.html"), ("Grammar", "site/grammar.html"),
             ("Course", "site/lessons.html"), ("Standard", "spec/Beluma-Standard-v1.0.html"),
             ("Translator", "site/translator.html")]
    return "".join(f'<a href="{rel(t)}">{label}</a>' for label, t in items)


def build(md_path: Path) -> Path:
    md = md_path.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+)$", md, re.M)
    title = m.group(1).strip() if m else md_path.stem
    body = md2html(md)
    html = TEMPLATE.format(title=esc(title), nav=nav_for(md_path), body=body)
    out = md_path.with_suffix(".html")
    out.write_text(html, encoding="utf-8")
    return out


def main():
    built = 0
    for d in DIRS:
        root = ROOT / d
        if not root.exists():
            continue
        for md in sorted(root.rglob("*.md")):
            rel = md.relative_to(ROOT)
            print(f"build {rel.with_suffix('.html')}")
            build(md)
            built += 1
    print(f"\nBuilt {built} pages.")


if __name__ == "__main__":
    main()
