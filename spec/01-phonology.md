# §01 Phonology — Beluma Language Standard v1.0

Status: **Normative.** Beluma has a one-to-one orthography: every letter represents
exactly one sound, and every sound is written with exactly one letter. There are no
silent letters, no alternative spellings, and no spelling pronunciations.

## 1.1 Overview

- 23 letters, 23 phonemes: 5 vowels and 18 consonants (§1.2, §1.3).
- Every word is pronounced as written; every word is written as pronounced, up to
  the acute accent (§1.5).
- Stress is fixed by rule — it never distinguishes words (§1.5).

## 1.2 Vowels

| Letter | IPA | Notes |
| --- | --- | --- |
| `a` | /a/ | open central, never reduced |
| `e` | /e/ | mid front |
| `i` | /i/ | close front |
| `o` | /o/ | mid back |
| `u` | /u/ | close back |

- No vowel length: `mala` /ma-la/ — both vowels short.
- No diphthongs: adjacent vowels in different syllables (hiatus), e.g. `spira`
  /spi-ra/, `huroxan` /hu-ro-xan/. In rapid informal speech an off-glide [j] or [w]
  may appear between adjacent vowels (`spira` ≈ [spjra]) — this is **informative**,
  not required, and never changes the spelling.
- No schwa and no unstressed reduction: every vowel is full in every register.

## 1.3 Consonants

| Letter | IPA | Notes |
| --- | --- | --- |
| `b` | /b/ | |
| `d` | /d/ | |
| `f` | /f/ | |
| `g` | /ɡ/ | always hard; never /dʒ/ |
| `h` | /h/ | always pronounced, never silent |
| `j` | /j/ | as English *y* in *yes*; never /dʒ/ |
| `k` | /k/ | always hard |
| `l` | /l/ | |
| `m` | /m/ | |
| `n` | /n/ | |
| `p` | /p/ | |
| `r` | /r/ | alveolar trill; a tap [ɾ] in rapid speech is acceptable |
| `s` | /s/ | always voiceless; never /z/ |
| `t` | /t/ | |
| `v` | /v/ | |
| `w` | /w/ | |
| `z` | /z/ | |
| `x` | /ks/ | always /ks/, in every position (`hurox` /hu-roks/) |

- There is no `c`, `q`, or `y` in the alphabet (§2.1). Sounds /k/ and /ɡ/ before
  front vowels are still written `k` and `g`; the approximant is written `j`.
- The letters `c`, `q`, `y` may appear only inside quoted English or in loanwords,
  which MUST be respelled on entry (§15.6).

## 1.4 Syllable structure

Beluma syllables have the shape **(C)V(C)**: an optional single consonant onset, a
mandatory vowel nucleus, an optional single consonant coda.

**Onsets.** A syllable may begin with a single consonant or with one of these
attested clusters:

> `pr tr br dr fr kr gr pl sp kv kw`

- New coinages SHOULD use only `pr br tr dr fr kr gr pl kv kw` (`sp` occurs in
  established words such as `spira` and is otherwise reserved for loans).
- Clusters such as `bl gl fl sl st sm sn` do not occur and MUST NOT be created.

**Codas.** A syllable may end with a single consonant. Attested codas, by frequency:

> `s n r l k t f d p x`

- The productive codas in native words are **`s`** (plural, §05), **`n r l k`**,
  and **`t`** as realised by the suffix `-ét` (§15.5).
- Codas `f d p x` occur only in established roots and digit roots (`af`, `nof`,
  `rip`, `hurox`, `sep`, `nof`). New coinages MUST NOT end in `f d p x`.
- The preferred shape of a new root is open: `CV`, `CVV`, or `CVCV`.

**Word shapes.** Approximately 85% of dictionary entries end in a vowel. Closed
monosyllables (`un`, `du`, `s`, `ét`, `af`) are overwhelmingly function words.

## 1.5 Stress and the acute accent

1. **Stress falls on the penultimate syllable of the whole word**, counting across
   compound hyphens: `beluma` /be-LU-ma/, `tuma-pira` /tu-ma-PI-ra/,
   `kora-vésa` /ko-ra-VÉ-sa/. Monosyllables are stressed on their only syllable.
2. Stress is completely predictable: **it never distinguishes words**. Two entries
   that differ only in accent (§26.4) are homophones in speech; the accent is a
   spelling distinction only.
3. The **acute accent** (`á é í ó ú`) marks the stressed (penultimate) syllable:
   `méra`, `kvín`, `fóra`.
4. Writing the accent is **OPTIONAL** in all registers except:
   - **Accent-pair words** (§26.4): where two dictionary entries differ only by an
     accent, both entries MUST be written exactly as the dictionary spells them
     (`loma` = tree, `lóma` = look; `ra` = near, `rá` = was). Dropping or adding an
     accent on such a word produces a different word.
   - The dictionary, teaching materials, and poetry SHOULD mark all penultimate syllables.
5. The accent is written on a monosyllable only in accent-pair entries (`rá`, `dá`).
6. There is no other use of diacritics: no cedillas, tildes, diaereses, or
   circumflexes exist in Beluma.

**Transitional rule:** at VTXT 4.0 the accent-pair registry (§26.4) is being reduced
by respelling; until a pair is respelled, rule 4 applies to it.

## 1.6 Phoneme inventory summary

```
Vowels:     a  e  i  o  u                          (5)
Consonants: b  d  f  g  h  j  k  l  m  n  p  r  s  t  v  w  z  x   (18)
Total:      23 phonemes / 23 letters
```

## 1.7 Connected speech (informative)

- Hiatus glides (§1.2) appear in fast speech.
- A final nasal may assimilate before a following consonant in rapid speech; the
  spelling never changes.
- Function words (`s`, `un`, `né`, `wé`) are unstressed but retain their full vowel.

## 1.8 Prosody (informative)

- Declaratives fall at the end; yes/no questions (`kvo`) rise; content questions
  fall, as in most languages.
- Contrastive focus is marked by moving the focused element to clause end or by
  contrastive stress on the penult — never by a spelling change.

## 1.9 Phonotactics for new words (normative)

A coinage (§15) MUST satisfy all of the following:

1. Every syllable is (C)V(C) with an onset from §1.4.
2. Stress falls on the penult; if that is impossible with the intended morphology,
   the morphology is wrong — change the word, do not add an exceptional accent.
3. The word does not differ from an existing entry only by accent, only by plural
   marking, or by reduplication that collides with an existing reduplicated form
   (§15.7).
4. The word is not a near-homophone of an existing entry (same syllable count,
   same stress, ≥2 of 3 phonemes in common in the same positions) unless it is a
   deliberate transparent compound.
5. Vowel sequences respect vowel harmony avoidance: no more than two different
   adjacent unaccented vowels in a row beyond what existing loans show.
6. Letter names are a meta-linguistic exception: consonants are named `C+a`
   (`ba da fa …`), vowels are named by themselves, and `x` is named `ksa` — the
   only word-initial `ks` in the language, permitted because letter names are
   cited in isolation.
