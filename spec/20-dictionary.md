# §20 Dictionary Structure — Beluma Language Standard v1.0

Status: **Normative.** The dictionary is a single plain-text file,
`lexicon/h.txt`. This section defines its format, fields, tags, and versioning.

## 20.1 File format

The dictionary is UTF-8, one entry per line, fields separated by ` = `:

```
kéma = know / know-how [noun] {standard} # teaches
```

Formal grammar: `head = glosses [class] {register} # notes`.

- **head** — the citation form, lowercase, alphabet-legal (§01), one word.
- **glosses** — English senses, separated by ` / `.
- **`[class]`** — grammatical class tag (optional but recommended).
- **`{register}`** — register tag (optional; default Standard).
- **`# notes`** — usage note, example, or inflection (optional).

## 20.2 Class tags

| Tag | Meaning | Tag | Meaning |
| --- | --- | --- | --- |
| `[noun]` | substantive | `[adj]` | adjective |
| `[verb]` | verb | `[adv]` | adverb |
| `[pron]` | pronoun | `[prep]` | preposition |
| `[conj]` | conjunction | `[num]` | numeral |
| `[part]` | particle | `[interj]` | interjection |
| `[affix]` | bound morpheme | `[name]` | proper noun |

## 20.3 Register tags

`{standard}` (default), `{formal}`, `{informal}`, `{technical}`, `{literary}`,
`{colloq}`, `{archaic}`. A definition may carry more than one, e.g.
`{standard,technical}`. See §23.1.

## 20.4 Field blocks

Sections are introduced by `# --- name ---` comments:

| Block | Content |
| --- | --- |
| core | function words, pronouns, particles |
| core-added | regular derivations and number words |
| domain: … | 24 domain sets (§15.13) |
| units/science | §17 |
| gov/law | §18 |
| education/culture | §19 |
| notation | meta-linguistic and punctuation names |

Block comments are documentation only; the loader ignores them.

## 20.5 Derived forms and the head principle

Only **heads** are listed. Regular derivations (`-la -ji -lé -os -an -s -as
-é`…) and compounds are **not** listed; the parser and `tools/grow.py` generate
them from §15 rules. This keeps the file at ~2,200 heads while licensing
hundreds of thousands of words. A derived form is listed **only** if its
meaning is idiomatic, not compositional (e.g. `kéma` *know*, but `kémor`
*teacher* is listed because the agent sense is conventionalized).

## 20.6 Required metadata header

The first lines of `h.txt` are:

```
# Beluma Lexicon
# VTXT 4.0
# format: head = glosses [class] {register} # notes
```

The **VTXT** line is the dictionary version and MUST match §15.12. Tools read
it to detect breaking changes.

## 20.7 Validation rules

Every submission is checked by `tools/validate_dict.py`, which enforces:

1. alphabet legality (§01.2);
2. onset/coda phonotactics (§01.4);
3. accent placement = penult (§01.5), except registered accent pairs;
4. no exact duplicate heads;
5. well-formed line syntax.

Accent-pair spelling collisions are downgraded to **warnings** and recorded in
the registry (§26.4). Any **error** blocks a VTXT release.

## 20.8 Derived artifacts

The dictionary generates:

- `site/dictionary.html` — searchable web list;
- `library/lexicon.html` — browsable reference;
- `spec/20-dictionary.md` statistics (head count, blocks, tag counts);
- engine word-data for `engine/beluma.js`.

None of these are hand-edited; all are rebuilt by `tools/build_vocab.py`.

## 20.9 Current statistics

| Metric | Value |
| --- | --- |
| Heads | ~2,191 |
| Blocks | core, core-added, 24 domains, units/science, gov/law, education/culture, notation |
| VTXT | 4.0 |
| Rebuild tool | `tools/build_vocab.py` (to be run on every release) |

## 20.10 Adding an entry

1. Confirm the word is a **head** (§20.5), alphabet-legal, and not a duplicate.
2. Write the line in `h.txt` in the right block.
3. Run `tools/validate_dict.py` — must be 0 errors.
4. Run `tools/check_spec_words.py` if the entry is used in `spec/`.
5. Bump VTXT if the change is breaking (§15.12); note it in `canon/`.
