#!/usr/bin/env python3
"""build_vocab.py — builds the searchable dictionary artifacts from lexicon/h.txt.

Generates:
  site/dictionary.html   searchable, client-side filter
  library/lexicon.html   static browsable list grouped by block
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "lexicon" / "h.txt"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Lía Beluma</title>
<style>
:root{{--accent:#9b59b6;--dark:#22142b;--border:#e6dceb}}
*{{box-sizing:border-box}}
body{{font-family:'Segoe UI',Roboto,sans-serif;margin:0;background:#faf7fc;color:#333;line-height:1.6}}
header{{background:var(--dark);color:#fff;padding:16px 5%;display:flex;justify-content:space-between;flex-wrap:wrap;align-items:center}}
header a{{color:#e6d7ef;text-decoration:none;margin-left:14px;font-weight:600}}
main{{max-width:1000px;margin:26px auto;padding:0 18px 60px}}
h1{{color:var(--dark);border-bottom:4px solid var(--accent);padding-bottom:8px}}
h2{{color:var(--accent);text-transform:uppercase;letter-spacing:1px;font-size:.95rem;margin-top:34px}}
input{{width:100%;padding:11px 14px;border:2px solid var(--border);border-radius:10px;font-size:1rem;margin:10px 0 20px}}
table{{border-collapse:collapse;width:100%}}
td,th{{border-bottom:1px solid var(--border);padding:7px 10px;text-align:left;vertical-align:top}}
th{{background:#f3edf8;color:var(--dark);position:sticky;top:0}}
.k{{font-weight:700;color:#7a3da1;white-space:nowrap}}
.note{{color:#888;font-size:.85rem}}
.navhome{{font-size:.85rem;color:#b8a6c4;margin-top:40px}}
</style>
</head>
<body>
<header><span style="font-weight:800">{title}</span><span>{nav}</span></header>
<main>
{content}
<p class="navhome">Generated from <code>lexicon/h.txt</code> by <code>tools/build_vocab.py</code></p>
</main>
</body>
</html>
"""

NAV = ('<a href="index.html">Overview</a>'
       '<a href="grammar.html">Grammar</a>'
       '<a href="dictionary.html">Dictionary</a>'
       '<a href="lessons.html">Course</a>')


def parse():
    entries = []
    block = "core"
    for ln in SRC.read_text(encoding="utf-8").splitlines():
        s = ln.strip()
        if not s:
            continue
        if s.startswith("#"):
            m = re.match(r"#\s*---\s*(.+?)\s*---", s)
            if m:
                block = m.group(1)
            continue
        if "=" not in s:
            continue
        head, rest = s.split("=", 1)
        head = head.strip()
        rest = rest.strip()
        cls = ""
        reg = ""
        cm = re.search(r"\[([^\]]+)\]", rest)
        if cm:
            cls = cm.group(1)
            rest = rest.replace(cm.group(0), "").strip()
        rm = re.search(r"\{([^}]+)\}", rest)
        if rm:
            reg = rm.group(1)
            rest = rest.replace(rm.group(0), "").strip()
        note = ""
        if "#" in rest:
            rest, note = rest.split("#", 1)
        entries.append((head, rest.strip(), cls, reg, note.strip(), block))
    return entries


def search_page(entries):
    rows = "\n".join(
        f'<tr><td class="k">{html.escape(h)}</td><td>{html.escape(g)}</td>'
        f'<td class="note">{html.escape(c)} {html.escape("{"+r+"}" if r else "")}</td></tr>'
        for (h, g, c, r, n, b) in entries)
    script = """<input id="q" placeholder="Search Beluma or English...">
<script>
const q=document.getElementById('q');
const rows=[...document.querySelectorAll('tbody tr')];
q.addEventListener('input',()=>{const v=q.value.toLowerCase();
 rows.forEach(t=>t.style.display=t.textContent.toLowerCase().includes(v)?'':'none');});
</script>"""
    content = (f"<h1>Beluma Dictionary</h1>"
               f"<p>{len(entries)} heads · VTXT 4.0</p>{script}"
               f"<table><thead><tr><th>Beluma</th><th>English</th><th>class</th></tr></thead>"
               f"<tbody>{rows}</tbody></table>")
    return HEAD.format(title="Dictionary", nav=NAV, content=content)


def browse_page(entries):
    blocks = {}
    for e in entries:
        blocks.setdefault(e[5], []).append(e)
    out = ["<h1>Lexicon</h1>", f"<p>{len(entries)} heads grouped by block.</p>"]
    for b in sorted(blocks):
        out.append(f"<h2>{html.escape(b)} ({len(blocks[b])})</h2><table><tbody>")
        for (h, g, c, r, n, _) in blocks[b]:
            out.append(f'<tr><td class="k">{html.escape(h)}</td><td>{html.escape(g)}</td>'
                       f'<td class="note">{html.escape(c)}</td></tr>')
        out.append("</tbody></table>")
    nav = ('<a href="../site/index.html">Overview</a>'
           '<a href="../site/grammar.html">Grammar</a>'
           '<a href="../site/dictionary.html">Dictionary</a>')
    return HEAD.format(title="Lexicon", nav=nav, content="\n".join(out))


def main():
    entries = parse()
    dest_html = ROOT / "site" / "dictionary.html"
    dest_lib = ROOT / "library" / "lexicon.html"
    dest_html.write_text(search_page(entries), encoding="utf-8")
    dest_lib.write_text(browse_page(entries), encoding="utf-8")
    print(f"{len(entries)} heads -> {dest_html.relative_to(ROOT)}, {dest_lib.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
