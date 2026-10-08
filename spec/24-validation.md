# §24 Validation, Conformance, and Change Control — Beluma Language Standard v1.0

Status: **Normative.**

## 24.1 Purpose

This section defines what it means for a text, dictionary, or tool to
**conform** to Beluma Standard v1.0, and how the standard changes.

## 24.2 Conformance levels

| Level | Requirement |
| --- | --- |
| **C0 — Phonological** | Text uses only legal letters (§01.2) and legal onset/coda clusters (§01.4). |
| **C1 — Morphological** | Every word parses by §15 derivation/compounding rules. |
| **C2 — Grammatical** | Sentences follow §03–§14 clause and phrase structure. |
| **C3 — Lexical** | Every head is in `h.txt` at the declared VTXT. |
| **C4 — Stylistic** | Register is consistent and appropriate (§23.1). |

A **Standard-conformant** text is C0–C4. A **Technical/Formal** text adds the
rules of §23.2/§23.3.

## 24.3 Normative vs informative status

Each section header states its status. **Normative** material defines the
language; **Informative** material illustrates or lists vocabulary. Where a
word list and a rule conflict, the rule wins and the list is corrected.

## 24.4 Automated checks

| Check | Tool | Gate |
| --- | --- | --- |
| dictionary format/alphabet/phonotactics | `tools/validate_dict.py` | 0 errors |
| spec tokens exist | `tools/check_spec_words.py` | 0 unknown |
| internal links resolve | `tools/check_links.py` | 0 broken |
| example texts conform | `tools/check_text.py` | 0 unknown |
| derivation capacity | `tools/grow.py` | ≥ 250,000 |

All gates must pass before a standard release is tagged.

## 24.5 Versioning (VTXT)

The version format is `MAJOR.MINOR`:

- **MAJOR** — breaking change (alphabet, phonotactics, core grammar, removing a
  head used normatively).
- **MINOR** — additive change (new heads, new optional patterns).

Ahead-of-release changes live in `canon/` as dated notes; the released standard
lives in `spec/Beluma-Standard-v1.0.md`.

## 24.6 Change control

1. **Propose** — write the change and rationale under `canon/`.
2. **Analyze** — list affected heads, texts, and tools; run all §24.4 checks.
3. **Trial** — apply to a branch of the dictionary; re-run checks.
4. **Ratify** — the Language Academy (§25) approves by simple majority.
5. **Release** — bump VTXT, update `spec/`, rebuild artifacts (§20.8).

## 24.7 Compatibility

- Adding heads: backward-compatible (MINOR).
- Changing a normative rule or deleting a head: requires migration notes and a
  MAJOR bump.
- Accent-pair spellings (§26.4) are stable; removing one is a MINOR change.

## 24.8 Error taxonomy

| Code | Meaning | Example |
| --- | --- | --- |
| E-ALPHA | illegal letter | `c`, `q`, `y` |
| E-CLUS | illegal onset/coda | `-ld`, `nj-` (before v4.0) |
| E-ACCENT | wrong stress position | stress off the penult |
| E-DUP | duplicate head | `vata` twice |
| E-SYNTAX | malformed line | missing ` = ` |

Errors block release; warnings (§26.4) do not.
