# §00 Preface — Beluma Language Standard v1.0

**Beluma Language Standard v1.0** — the complete, normative definition of the Beluma
language: sounds, writing, grammar, word formation, lexicon, and usage. This document
is the single authority for what is and is not correct Beluma.

Beluma is an analytic constructed language: SVO word order, tense carried by particles
rather than inflection, head-first compounding, a 23-letter Latin orthography, and a
dictionary that is the source of truth for every word.

## 0.1 Scope

This Standard is organised as follows.

| Sections | Content | Status |
| --- | --- | --- |
| §01–§02 | Phonology and writing system | Normative |
| §03–§15 | Grammar core: sentence structure, pronouns, nouns, verbs, questions, negation, modifiers, adverbs, prepositions, conjunctions, numbers, time, word formation | Normative |
| §16–§19 | Domain vocabulary: technology, science, government and law, education | Normative vocabulary |
| §20 | Full vocabulary (generated from the dictionary) | Normative |
| §21 | Example texts | Informative (conformant) |
| §22 | Learning guide | Informative |
| §23 | Registers | Normative |
| §24 | Validation suite | Normative (test definitions) |
| §26 | Design review and known issues | Informative |

The following are **not** part of this Standard:

- `canon/` — archived pre-1.0 drafts, retained for history only. Where canon and this
  Standard disagree, **this Standard wins**.
- `course/`, `library/`, `exams/`, `teacher/` — teaching and reading material. Texts
  marked *conformant* are written to this Standard; anything else is clearly marked.
- `engine/`, `tools/` — reference implementations (informative). The dictionary they
  operate on (§20) is normative; the algorithms are not.

## 0.2 Conformance language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT,
RECOMMENDED, MAY, and OPTIONAL are to be interpreted as in RFC 2119.

- A text is **conformant Beluma** if every word is a dictionary entry (§20) or a
  derivative formed by the rules of §15, and every sentence follows the rules of
  §03–§15 and the register rules of §23.
- A dictionary entry is **valid** if it obeys the phonotactics of §1.9, the
  orthography of §2, and the collision rules of §15.

## 0.3 Document structure

This Standard exists as:

1. Per-section Markdown files (`00-preface.md` … `26-design-review.md`) — the
   working source.
2. One combined document, **`Beluma-Standard-v1.0.html`**, generated from the
   section files by `tools/build_standard.py`. The combined document is the
   published form; in case of conflict between a rendered page and this source,
   the Markdown source governs.

## 0.4 The dictionary lock

`lexicon/h.txt` is the source of truth for the vocabulary. Its header carries a
`VTXT=` version line; this Standard is published against **VTXT 4.0**.

- A word is **in the language** if and only if it appears as an entry key in the
  dictionary at the published VTXT version.
- A word is **a valid derived form** if it is built from dictionary roots by the
  rules of §15 (affixes, compounding, reduplication), even when not listed as its
  own entry.
- Changing the dictionary requires bumping VTXT and revalidating (§24).

## 0.5 Reference implementations

- `engine/beluma.js` — two-way gloss translator and morphological analyser
  (informative). Behaviour described in §24 is normative; implementation detail is not.
- `tools/check_links.py`, `tools/validate_dict.py`, `tools/check_text.py`,
  `tools/build_standard.py` — the validation suite of §24.

## 0.6 Versioning and changes

- **Language version (this document):** `v1.0`. Additive changes (new words, new
  example texts) increment the minor version (`v1.1`); grammar changes increment the
  major version.
- **Dictionary version (`VTXT`):** increments on every accepted dictionary change,
  independently of the language version. The VTXT that a text was written against is
  recorded with it (§24).

## 0.7 How to read this Standard

- **New to Beluma?** §22 (learning guide) → `site/lessons.html` (course) → §03 (grammar core).
- **Writing in Beluma?** §01–§15 are your reference; §20 is your word list; §23 tells
  you which register to use.
- **Checking a text?** Run the §24 validation suite.
- **Curious about the trade-offs?** §26 explains what was deliberately left out and
  what is known to be weak.
