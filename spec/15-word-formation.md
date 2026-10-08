# §15 Word Formation — Beluma Language Standard v1.0

Status: **Normative.** Beluma grows by compounding existing roots and by a small,
closed set of affixes. Every new word is built, never invented from nothing — and
becomes part of the language only when it is registered in the dictionary (§0.4).

## 15.1 Compounding

- **Head-first:** the first element is the head — the class the word belongs to —
  and every following element specifies it:
  `nela-sula` water+great = *ocean* (a great water),
  `kiva-nira` work+small = *gadget* (small work-thing),
  `fira-os` bird+group = *flock*,
  `kora-jula` chest+serving = *server*,
  `sova-nela` speech+stream = *language*,
  `luma-saro` light+star = *flashlight*.
- Any two dictionary roots may be combined; a compound is grammatical the moment
  its parts are (§0.1 conformance).
- Writing: closed unless the dictionary hyphenates (§2.6); internal spelling is
  never altered.
- Stacking limit: three roots in normal prose (`kiva-siva-nira` *phone* =
  work-voice-small); four only in technical names. Beyond that, register a new
  compound instead (§15.7).

## 15.2 The affix inventory (normative)

| Affix | Position | Meaning | Example |
| --- | --- | --- | --- |
| `-s` / `-as` | final | plural (-s after vowel, -as after consonant) | `lavos` dogs |
| `-la` | final | possession | `mi-la` my |
| `-nira` | final | small, mild, young | `luma-nira` idea (light-small) |
| `-sula` | final | great, abstract quality | `nela-sula` ocean |
| `-ét` | final | young of | `lavoét` puppy |
| `-os` | final | group, herd | `fira-os` flock |
| `-an` | final | place, habitat | `fira-an` nest |
| `-or` | final | doer of (drops a final `-a`: `kéma` know → `kémor` knower/teacher) | `kémor` teacher |
| `-pira` | final | tool for | `féma-pira` spoon |
| `-tavi` | final | platform for | `kiva-tavi` desk |
| `-ik` | final | like, resembling | `fira-ik` birdlike |
| `-nélo` | final | flowing/running (of a substance) | `siva-nélo` speech-stream |
| `-lé` | final | adverb | `gavo-lé` well |
| `-va` | final | -ing / verbal noun | `sola-va` playing |
| `-ké` | final | -ed / completed state | `féma-ké` eaten |
| `-ji` | final | ordinal | `onaji` first |
| `un-` | initial | not, lack of | `un-kula` easy |
| `ni-` | initial | opposite, anti, mis- | `ni-kéma` misunderstand |
| `ré-` | initial | again, re- | `ré-dora` re-open |

- **Suffix stacking order** (outermost last): a category suffix, then inflection:
  `root + (-nira|-sula|-pira …) + (-va|-ké) + (-s|-la|-lé|-ji)`. Example:
  `luma-nira-va s` — "is being a little-light". Adverbial `-lé` is last before
  inflection: `gavo-nira-lé`.
- `-or` and `-pira` are **open** (any root); `-nélo`, `-ét`, `-os`, `-an` are
  semi-closed (productive but lexicalised in most existing words); everything
  else is fully productive.
- Prefix order if stacked (rare): `ni-` then `un-` is forbidden — use one.

## 15.3 Zero derivation

Any adjective may be used as a noun without a suffix, and vice versa:
`béla` *beautiful / beauty*, `sulo` *strong / strength*, `koma` *pain / hurt*.
Context decides; the dictionary glosses both readings. This is the preferred way
to abstract — do not coin `-sula` versions of existing adjectives unless the
dictionary already has them.

## 15.4 Reduplication

- Wholesale repetition of a word marks **reciprocal/distributive** meaning:
  `ona-ona` *each other* (one-one), `sumés sumés` style repetition in poetry.
- Only lexicalised reduplications are dictionary entries; a new reduplication is
  understandable but enters the dictionary only with a registered gloss.
- Reduplication never changes number: `loma lomas` is not plural marking (plural
  is `-s` only).

## 15.5 Loanwords

International vocabulary enters by **respelling** — a loan MUST:

1. contain no `c`, `q`, `y` (write `k`, `s`/`kv`, `i`);
2. fit §1 phonotactics (open syllables, legal onsets, penult stress);
3. be head-compatible: nouns end in a vowel when they enter a compound.

Examples (dictionary-attested): `komputa` < computer, `programa` < program,
`eksporta` < export, `porsenta` < percent, `parentesa` < parenthesis, `téléfona`
if attested. If a loan collides with a native root, **the native word wins** —
the loan is reshaped or rejected (§15.6).

## 15.6 Collision rules (normative — registration MUST fail otherwise)

A candidate word is rejected if:

1. it differs from an existing entry **only by accent** (§1.9.3 — the accent-pair
   defect of v1.0 is closed to new entries);
2. it equals an existing entry after stripping plural/possessive marking;
3. it is a near-homophone of an existing entry (§1.9.4);
4. it violates §1.9 phonotactics in any way;
5. its gloss is already carried by a single existing word (synonym surplus) —
   prefer compounding over a new root for a meaning an existing root can express.

## 15.7 Registration — how a word becomes a word

1. Build the form by §15.1–§15.5.
2. Run the validation suite (§24): `tools/validate_dict.py` checks 1–4 above and
   the dictionary format.
3. Add the entry to `lexicon/h.txt` with glosses and register tag; bump `VTXT`.
4. Only then may texts use the word as a dictionary word (before that it is a
   transparent compound, still parseable by the engine).

Note: the historical `tools/coiner.js` referenced by archived canon does not exist
in this repository; `tools/validate_dict.py` is the normative gate (§24).

## 15.8 Register of coinage

New roots enter as **Standard** by default. Words intended only for Informal use
(tagged `colloquial` in the dictionary) may bypass collision rule 5 but never
rules 1–4. Domain vocabulary (§16–§19) enters as **Technical** and is promoted to
Standard by usage, via a VTXT change.
