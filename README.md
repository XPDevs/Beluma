# Lía Beluma — Language Standard v1.0

**Beluma** is a complete, engineered constructed language: a regular
phonology, Latin orthography (a–z minus `c q y`), a fully regular grammar, a
productive word-formation system, and a validated lexicon of ~2,200 heads that
licenses **more than 250,000 words**.

The normative reference is
**[spec/Beluma-Standard-v1.0.md](spec/Beluma-Standard-v1.0.md)** (HTML:
[`spec/Beluma-Standard-v1.0.html`](spec/Beluma-Standard-v1.0.html)), assembled
from the numbered sections in `spec/` by `tools/build_standard.py`.

## Repository map

| Path | Contents |
| --- | --- |
| `spec/` | The Standard — sections `00`–`26`, plus the assembled `Beluma-Standard-v1.0.md/.html` |
| `lexicon/h.txt` | The dictionary (single source of truth, VTXT 4.0) |
| `engine/beluma.js` | Reference engine: dictionary load, word analysis, EN↔BE glossing |
| `site/` | Web app: `index.html`, `grammar.html`, `dictionary.html`, `lessons.html`, `translator.html` |
| `course/` | Graded lessons (A1→C2, see §22) |
| `library/` | Reference articles, corpus, interactive fiction |
| `exams/` | Certification papers (A1–C2) |
| `teacher/` | Teaching materials |
| `canon/` | Pre-1.0 source notes and Academy rulings (§25) |
| `tools/` | Builders and validators (Python) |

## The Standard at a glance

- **§01** phonology — 23 letters, fixed penult stress, legal onset/coda clusters.
- **§03–§14** grammar — SVO, `un (né|wé|wés)` tense, aspects, modals, pronouns,
  nouns, adjectives, adverbs, prepositions, conjunctions, numbers, time.
- **§15** word formation — the productivity engine (prefixes, suffixes,
  compounding, loan respelling).
- **§16–§19** domains — technology, science/measurement, government/law,
  education/culture.
- **§20** dictionary format · **§21** example texts · **§22** curriculum and
  translation guide · **§23** registers · **§24** validation · **§25** the
  Language Academy · **§26** design review.

## Try it

```sh
python -m http.server 8080
# open http://localhost:8080/site/translator.html
```

| English | Beluma |
| --- | --- |
| I am happy | `mi s réva` |
| I ate fruit | `mi un né fura` |
| Do you go home? | `kvo tu gava po nésa?` |
| Don't go | `un gava` |
| Knowledge alone frees. | `Kéma sola libera.` |

## Build and validate

```sh
python tools\validate_dict.py     # dictionary: format, alphabet, phonotactics, accents
python tools\check_spec_words.py  # every word used in spec/ exists in h.txt
python tools\check_links.py       # no broken internal links
python tools\grow.py              # word-formation capacity report
python tools\seed_vocab.py        # add domain vocabulary (keys sanitized)
python tools\build_vocab.py       # rebuild site/dictionary.html + library/lexicon.html
python tools\build_standard.py    # reassemble spec/Beluma-Standard-v1.0.md + .html
python tools\md2html.py           # render spec/canon/course/... Markdown to HTML
```

All checks currently pass: **0 dictionary errors, 0 unknown spec words, 0 broken
links**.

## Extending the language

1. Add a **head** (not a derived form) to `lexicon/h.txt` in the right block:
   `head = gloss / gloss [class] {register} # note`.
2. Run `tools\validate_dict.py` (must be 0 errors) and, if used in `spec/`,
   `tools\check_spec_words.py`.
3. Derive, don't memorize — most words come from §15 rules, and the parser
   (`engine/beluma.js`, `tools/grow.py`) generates them on the fly.
4. Breaking changes are ratified by the Language Academy and bump the VTXT
   version (§24).

## Status

Constructed language project. All content is dictionary-locked to **VTXT 4.0**
and works entirely in the browser or from the command line.
