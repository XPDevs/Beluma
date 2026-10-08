# §02 Writing System — Beluma Language Standard v1.0

Status: **Normative.** Beluma is written with a 23-letter Latin alphabet. One
script, one spelling, one set of punctuation conventions, in print and on screens.

## 2.1 The alphabet

The canonical alphabet, in canonical order:

```
a  b  d  e  f  g  h  i  j  k  l  m  n  o  p  r  s  t  u  v  w  z  x
```

- 23 letters: 5 vowels (`a e i o u`), 18 consonants.
- **There is no `c`, `q`, or `y`.** A `c` in text is an error (write `k` or `s`
  per §1.3); loanwords are respelled (§15.6).
- The **acute accent** (`á é í ó ú`) is a stress mark (§1.5), **not a letter**.
  The alphabet has 23 letters in uppercase and lowercase alike.
- Letter names (§1.9.6): vowels are named by themselves; consonants as `C+a`
  (`ba`, `da`, `fa`, `ga`, `ha`, `ja`, `ka`, `la`, `ma`, `na`, `pa`, `ra`,
  `sa`, `ta`, `va`, `wa`, `za`); `x` is named `ksa`.

## 2.2 Capitalisation

1. The first word of a sentence starts with a capital letter.
2. Proper nouns start with a capital letter: personal names, place names, names of
   languages and peoples, months, and weekdays (`Méra-Tava`, `Beluma`, `Soma`).
3. The language name `Beluma` and the adjective `beluma` (about the language) are
   capitalised when they name the language: `Mi parla Beluma.` / `beluma sova`
   ("a Beluma sentence" — lowercase when used attributively inside a phrase
   describing components, e.g. `beluma nira`).
4. Nothing else is capitalised — including the pronoun `mi` and the word `I` equivalent.
5. Acronyms are written in capitals without points: `UN` (not `U.N.`), pronounced
   letter by letter using §2.1 letter names, or as a word if a reading is registered
   in the dictionary.

## 2.3 Punctuation

| Glyph | Beluma name | Usage |
| --- | --- | --- |
| `.` | `dota` | end of declarative sentence; decimal point (§13) |
| `,` | `kama` | clause separation, listing |
| `?` | `kwamorka` | end of question (§07) |
| `!` | `fimorka` | end of exclamative; never doubled |
| `:` | `tuo-dota` | introduction of a list or explanation |
| `;` | `dota-kama` | separation of closely related clauses |
| `"` `"` | `sa-morka` | quotation (speech-mark) |
| `'` | `morka-nira` | apostrophe in elisions of informal speech (§23); never in possessives (possession is `-la`, §05) |
| `-` | `linya-nira` | inside compounds; never at line end |
| `–` `—` | `linya-sula` | parenthetical break (en dash/em dash); never doubled |
| `...` | `dota-tro` | ellipsis; replaces the final `dota` of the sentence |
| `(...)` | `parentesa` | parenthetical aside (loanword, respelled) |
| `/` | `linya-ora` | alternation ("and/or") |
| `@` | `na-morka` | at-address (electronic addresses) |
| `#` | `linya-dis` | number/cross mark (labels) |
| `%` | `porsenta-morka` | percent; also written `porsenta` after a number |

Rules:

- **One space** between words; **one space** after `,` `:` `;` and before `?` `!`
  is not used (the marks attach to the preceding word: `suna?`, never `suna ?`).
- Quotation: the opening `"` sits outside the following punctuation; full stop
  goes inside when the quote is a full sentence.
- A compound is written as one word (§15.1); the hyphen `-` is reserved for
  deliberate disambiguation and for compounds written open in the dictionary
  (`tuma-pira`, `diza-é-sita`). Dictionary spelling is authoritative: if the
  dictionary writes a compound closed, write it closed.

## 2.4 Numerals

- Prose and general writing use **number words**: `tro diva`, `kvín cénta`.
- Technical, scientific, and financial writing MAY use Arabic numerals
  `0 1 2 3 4 5 6 7 8 9` in the ASCII forms. Group thousands with a **space**
  (`3 000`), decimals with `dota` (`3.5`), read digit by digit after the point
  (§13).
- Ordinals in numerals take `-ji` (`1.-ji` = first) — preferred form remains the
  word `onaji`.

## 2.5 The acute accent in text

- Encoding: NFC precomposed characters — `á` is U+00E1, not `a` + U+0301 (§2.8).
- Mandatory: accent-pair entries (§1.5.4).
- Recommended: dictionaries, textbooks, poetry, any text for learners.
- Optional: everyday prose and informal registers (§23).
- The accent never carries meaning beyond stress marking or accent-pair identity.

## 2.6 Compound spelling

1. Dictionary compounds are written as recorded in §20 — closed (`kora` + `jula` →
   `kora-jula` when the dictionary hyphenates, `beluma` closed when it does not).
2. The general rule is **closed, no space**; a hyphen appears when the dictionary
   shows one or when disambiguation requires it (`diza-é-sita` "seventeen" vs a
   hypothetical `dizaésita`).
3. A compound keeps its internal spelling unchanged — no assimilation, no vowel
   harmony, no truncation.

## 2.7 Line breaking

- Break lines **after** a compound hyphen, never before one.
- Never split a single word: Beluma syllables are short enough that hyphenation
  within a word is unnecessary in ordinary text; where a layout engine must
  hyphenate, it MAY break after any syllable boundary (§1.4), preserving one
  hyphen at line end.
- Never break between a number and its unit (`kvín porsenta` stays together).

## 2.8 Digital encoding

- **UTF-8** is the required encoding for all files and transports.
- Text MUST be normalised to **NFC** (canonical composition): `á` = U+00E1.
  Decomposed input (`a` + U+0301) MUST be composed on ingestion.
- The complete Beluma character inventory is:

```
lowercase:  a b d e f g h i j k l m n o p r s t u v w z x
            á é í ó ú
uppercase:  A B D E F G H I J K L M N O P R S T U V W Z X
            Á É Í Ó Ú
digits:     0 1 2 3 4 5 6 7 8 9
punctuation: . , ? ! : ; " ' - – — ... ( ) / @ # %
space, tab, newline
```

- Text containing `c`, `q`, `y`, or any other character outside this inventory is
  non-conformant (quoted foreign material excepted and marked).

## 2.9 Keyboarding

On a US-QWERTY keyboard with a US-International or compose configuration:

| Beluma | US-International | Compose | Notes |
| --- | --- | --- | --- |
| `á é í ó ú` | `'a 'e 'i 'o 'u` | `Compose ' a` | acute (dead key) |
| `Á É Í Ó Ú` | `'A 'E 'I 'O 'U` | `Compose ' A` | |
| `? ! : ; "` | direct | direct | |
| `– —` | `Ctrl+-` / `Ctrl+Shift+-` | `Compose - -` / `Compose - - -` | |
| `...` | `.` `.` `.` | `Compose . .` | |

Accented letters may be omitted only where §1.5 allows it. A conformant text MUST
be recoverable to its dictionary spelling — writers of informal unaccented text
MUST still distinguish accent-pair words (write `ra` and `rá` distinctly).

## 2.10 Handwriting (informative)

Print and cursive forms follow the same shapes as the Latin models:
single-storey `a`, open-tailed `g`, uncrossed `t` with a short bar; `l` and `I`
(capital i) are never confusable because capital `I` occurs only at sentence
start and in names. The acute is a single stroke rising to the right above the
vowel. Speed conventions (looping `e`, merged `in`/`im`) are permitted provided
the letter identities remain recoverable — legibility, not style, is the constraint.

## 2.11 Historical note: the radical script (out of scope)

Earlier drafts of this project described a stroke-based "radical" writing system.
It was never implemented, has no font, no keyboard, and no corpus. **It is not part
of Beluma v1.0.** The Latin alphabet of this section is the one and only Beluma
script. Any future script proposal requires a major version of this Standard.
