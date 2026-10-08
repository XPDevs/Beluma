# Lía Beluma

**A complete, learnable constructed language.** Real phonology, a real writing system (Latin letters), regular grammar, and a growing lexicon. Read it. Write it. Speak it.

## What this repo is

Beluma used to be a word-for-word substitution cipher of English. That version is retired.
This version is structured like a real human language:

- **Sounds** — 23 letters, always pronounced the same way (see `grammar.html` / `index.html`).
- **Grammar** — SVO word order, analytic tense markers, head-first compounds, a small set of regular suffixes.
- **One script** — the 23 Latin letters `a b d e f g h i j k l m n o p r s t u v w z x`. The acute accent marks stress only.
- **A machine translation engine** — beluma.js is a morphological, two-way gloss translator powered by the dictionary in `h.txt`.

| File | What it is |
| --- | --- |
| `h.txt` | The dictionary — every Beluma word with its English gloss. Source of truth. |
| `beluma.js` | The language engine: dictionary loading, word analysis, EN↔BE translation. |
| `index.html` | Documentation homepage (phonology, writing system, grammar, numbers). |
| `grammar.html` | Full grammar reference. |
| `lessons.html` | 20-minute beginner course. |
| `translator.html` | Interactive two-way translator with word analysis. |

## Run it

The pages load `h.txt` and `beluma.js` by name, so serve this folder:

```sh
python3 -m http.server 8080
# then open http://localhost:8080/translator.html
```

Or just open `index.html` from the file system — the grammar/lesson pages work offline.

## Try it right now

Past these into the translator (English → Beluma):

| English | Beluma |
| --- | --- |
| I am happy | `mi s réva` |
| I ate fruit | `mi né féma fura` |
| The bird will fly in the sky | `le fira wé hura na le hula` |
| Do you go home? | `kvo tu gai po nésa?` |
| Don't go | `du gai` |

And back (Beluma → English):

| Beluma | English |
| --- | --- |
| `mi-la nésa s sulo` | My home is strong |
| `mi un kéma ta` | I do not know that |
| `siva s béla` | She is beautiful |

## How the language works (60 seconds)

- Sentence order: **Subject – Verb – Object** (like English).
- Time is a marker word before the verb: no marker = now, `né` = past, `wé` = future.
- Negation: `un` = not, `du` = don't. Questions: put `kvo` in front.
- Plurals add `-s`; possession adds `-la`; adjectives come before the noun.
- New words are head-first compounds: `néla` (water) + `sula` (great) = `nela-sula` (ocean).
- The acute accent marks stress only (`béla`, `nésa`). It never changes the meaning.

## Honest limitation

The translator is a *morphological glosser*, not a neural machine like DeepL. It handles
dictionary words, affixes, plurals, possessives and common phrases well; it does *not*
compose idiomatic English at the speed of a professional translator. Unknown words are
passed through and underlined. It is a teaching tool that grows with the dictionary.

## Extending the dictionary

`h.txt` is line-based and simple:

```
beluma-word = English gloss / another gloss
```

- Lines starting with `#` are comments. `VTXT=3.1` records the dictionary version.
- The machine form is written without accents (they are stripped on load); the accent-marked
  spelling is kept alongside for learners.
- Adding a line is enough: open the translator (reload) and the new word is live.
- Derived words (compounds and `-suffix` forms) are analysed automatically even when they
  aren't listed: `fema-pira` (eat + tool) = spoon works even though only the rule is taught.

## License / status

Constructed by James Turner (XPDevs). This is a learning project — fork it and teach Beluma
however you like.
## Learn the language directly in your browser

You can learn Beluma without downloading anything. Start here:

- **[index.html](site/index.html)** — Overview of Beluma (what it is, why)
- **[grammar.html](site/grammar.html)** — Complete grammar reference
- **[lessons.html](site/lessons.html)** — Quick 8-lesson taster (read and practice)
- **[lessons/README.html](course/README.html)** — Full 40-lesson A1→B1 course (books 01–04) with drills and keys
- **[translator.html](site/translator.html)** — Interactive translator (Beluma ↔ English) with word analysis
- **[exams/README.html](exams/README.html)** — Certification (A1–C2) and sample papers
- **[literature/corpus/README.html](library/corpus/README.html)** — Native-speaker corpus (B1+ reading band)
- **[literature/if/if-01-the-key.html](library/if/if-01-the-key.html)** — Interactive fiction (dictionary-locked)

All content is dictionary-locked to VTXT 3.9 and works entirely in the browser. Just open `index.html` in any modern browser to get started.
