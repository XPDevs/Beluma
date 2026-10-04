"use strict";
/* md2html.js — Phase 5: renders the site's Markdown into styled HTML so that the
   canon/, lessons/, exams/, teacher/ and literature/ pages are served by the nav.
   Usage: node tools/md2html.js [dir...]   (defaults to all five dirs)
   Idempotent: overwrites <basename>.html beside each .md. */

const FS = require("fs");
const PATH = require("path");

const root = PATH.join(__dirname, "..");
const DIRS = process.argv.slice(2).length
  ? process.argv.slice(2).map((d) => PATH.join(root, d))
  : ["canon", "lessons", "exams", "teacher", "literature"].map(
      (d) => PATH.join(root, d)
    );

const esc = (s) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function inline(s) {
  let out = esc(s);
  out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
  out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  out = out.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, t, u) => {
    const href = u.startsWith("http") ? u : u.replace(/\.md(#[^)]*)?$/, ".html$1");
    return `<a href="${href}">${t}</a>`;
  });
  return out;
}

function isTableRow(line) {
  const body = line.trim().replace(/^\||\|$/g, "");
  return body.includes("|");
}
function isTableSep(line) {
  return /^\s*\|?[\s:|-]+\|?$/.test(line) && line.trim().includes("-");
}

function md2html(md, title) {
  const lines = md.split("\n");
  const out = [];
  let i = 0;
  let list = null; // {type:"ul"|"ol", items:[]}
  let table = null; // {head:[], rows:[[]]}
  let fence = false;

  const flushList = () => {
    if (!list) return;
    const tag = list.type;
    out.push(`<${tag}>`);
    for (const it of list.items) out.push(`  <li>${it}</li>`);
    out.push(`</${tag}>`);
    list = null;
  };
  const flushTable = () => {
    if (!table) return;
    out.push("<table>");
    if (table.head.length)
      out.push(
        "<thead><tr>" +
          table.head.map((c) => `<th>${inline(c)}</th>`).join("") +
          "</tr></thead>"
      );
    out.push("<tbody>");
    for (const row of table.rows)
      out.push(
        "<tr>" + row.map((c) => `<td>${inline(c)}</td>`).join("") + "</tr>"
      );
    out.push("</tbody></table>");
    table = null;
  };

  while (i < lines.length) {
    const line = lines[i];
    if (fence) {
      if (/^\s*```/.test(line)) {
        out.push("</code></pre>");
        fence = false;
      } else out.push(esc(line));
      i++;
      continue;
    }
    if (/^\s*```/.test(line)) {
      flushList();
      flushTable();
      out.push("<pre><code>");
      fence = true;
      i++;
      continue;
    }
    const t = line.trim();
    if (t === "") {
      flushList();
      flushTable();
      i++;
      continue;
    }
    if (/^---+$/.test(t)) {
      flushList();
      flushTable();
      out.push("<hr>");
      i++;
      continue;
    }
    const h = t.match(/^(#{1,4})\s+(.*)$/);
    if (h) {
      flushList();
      flushTable();
      const lvl = h[1].length;
      out.push(`<h${lvl}>${inline(h[2])}</h${lvl}>`);
      i++;
      continue;
    }
    if (t.startsWith("> ")) {
      flushList();
      flushTable();
      out.push(`<blockquote>${inline(t.slice(2))}</blockquote>`);
      i++;
      continue;
    }
    if (isTableSep(line) && table) {
      table.sepSeen = true;
      i++;
      continue;
    }
    if (isTableRow(line)) {
      flushList();
      const cells = t.replace(/^\|/, "").replace(/\|$/, "").split("|").map((c)=>c.trim());
      if (!table) {
        table = { head: cells, rows: [], sepSeen: false };
      } else if (table.sepSeen) {
        table.rows.push(cells);
      }
      i++;
      continue;
    }
    if (/^\s{2,}\S/.test(line) && !isTableRow(line)) {
      // hard-wrapped continuation of the previous bullet/paragraph
      const cont = t.trim();
      if (list && list.items.length) {
        list.items[list.items.length - 1] += " " + inline(cont);
      } else if (out.length && /^<p>/.test(out[out.length - 1])) {
        out[out.length - 1] = out[out.length - 1].replace(
          /<\/p>$/,
          " " + inline(cont) + "</p>"
        );
      } else {
        out.push(`<p>${inline(cont)}</p>`);
      }
      i++;
      continue;
    }
    if (/^[-*]\s+/.test(t)) {
      flushTable();
      if (!list || list.type !== "ul") {
        flushList();
        list = { type: "ul", items: [] };
      }
      list.items.push(inline(t.replace(/^[-*]\s+/, "")));
      i++;
      continue;
    }
    if (/^\d+[.)]\s+/.test(t)) {
      flushTable();
      if (!list || list.type !== "ol") {
        flushList();
        list = { type: "ol", items: [] };
      }
      list.items.push(inline(t.replace(/^\d+[.)]\s+/, "")));
      i++;
      continue;
    }
    flushList();
    flushTable();
    out.push(`<p>${inline(t)}</p>`);
    i++;
  }
  flushList();
  flushTable();
  if (fence) out.push("</code></pre>");
  return `<h1>${esc(title)}</h1>\n` + out.join("\n");
}

const TEMPLATE = (t, body) => `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${t} | Lía Beluma</title>
<style>
:root{--accent:#9b59b6;--dark:#22142b;--text:#333;--border:#e6dceb}
*{box-sizing:border-box}
body{font-family:'Segoe UI',Roboto,sans-serif;margin:0;background:#faf7fc;color:var(--text);line-height:1.8}
header{background:var(--dark);color:#fff;padding:16px 5%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap}
header .t{font-weight:800}
header a{color:#e6d7ef;text-decoration:none;margin-left:16px;font-weight:600}
main{max-width:900px;margin:30px auto;padding:0 18px 60px}
h1{color:var(--dark);border-bottom:4px solid var(--accent);padding-bottom:10px}
h2{color:var(--accent);text-transform:uppercase;letter-spacing:1px;font-size:1rem;margin-top:42px}
h3{color:var(--dark)}
table{border-collapse:collapse;width:100%;margin:14px 0}
th,td{border:1px solid var(--border);padding:8px 12px;text-align:left;vertical-align:top}
th{background:#f3edf8;color:var(--dark)}
code{background:#f0e9f4;padding:2px 7px;border-radius:6px;color:#7a3da1}
pre{background:#22142b;color:#e6d7ef;padding:14px 18px;border-radius:12px;overflow-x:auto}
pre code{background:none;color:inherit;padding:0}
blockquote{border-left:5px solid var(--accent);background:#f3edf8;padding:8px 16px;border-radius:0 10px 10px 0;margin:14px 0}
a{color:var(--accent)}
li{margin:4px 0}
.navhome{font-size:.85rem;color:#b8a6c4}
</style>
</head>
<body>
<header>
  <span class="t">${t}</span>
  <span><a href="../index.html">Overview</a><a href="../grammar.html">Grammar</a><a href="../lessons.html">Course</a><a href="../translator.html">Translator</a></span>
</header>
<main>
${body}
<p class="navhome">Generated from Markdown by <code>tools/md2html.js</code> · Dictionary VTXT 3.7</p>
</main>
</body>
</html>`;

let built = 0;
const walk = (dir) => {
  for (const f of FS.readdirSync(dir)) {
    const full = PATH.join(dir, f);
    if (FS.statSync(full).isDirectory()) {
      if (!f.startsWith(".")) walk(full);
      continue;
    }
    if (!f.endsWith(".md")) continue;
    const md = FS.readFileSync(full, "utf8");
    const titleMatch = md.match(/^#\s+(.+)$/m);
    const title = titleMatch ? titleMatch[1].trim() : f.replace(/\.md$/, "");
    const body = md2html(md, title);
    const outPath = full.replace(/\.md$/, ".html");
    FS.writeFileSync(outPath, TEMPLATE(title, body));
    console.log(`✓ ${PATH.relative(root, outPath)}`);
    built++;
  }
};
for (const dir of DIRS) {
  if (FS.existsSync(dir)) walk(dir);
}
console.log(`\nBuilt ${built} pages.`);