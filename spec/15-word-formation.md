# §15 Word Formation — Beluma Language Standard v1.0

Status: **Normative.** Beluma grows by **compounding** existing roots and by a
**closed, fully productive set of affixes**. Every word is built, never invented
from nothing, and becomes part of the language only when it is registered in the
dictionary (§0.4). Because the rules are regular, a speaker can build and parse
words never heard before, and a defined core of a few thousand roots supports a
usable lexicon of hundreds of thousands of words.

## 15.1 The growth model

Beluma's lexicon has three layers:

| Layer | Size (v1.0 target) | How it is made |
| --- | --- | --- |
| **Roots** | 2,000–3,000 | simple, monomorphemic words (§15.9) |
| **Derived words** | 20,000+ | one to three affixes on a root (§15.2–§15.6) |
| **Compounds & terms** | 250,000+ | head-first combination of registered words (§15.7–§15.8) |

Because derivation and compounding are regular, the *reachable* vocabulary is the
product of the layers, not their sum (§15.11).

## 15.2 The affix inventory (normative)

Every affix below is **productive**: it may be added to any semantically
compatible root and the result is grammatical and inferable without a dictionary.

### 15.2.1 Prefixes

| Prefix | Meaning | Example |
| --- | --- | --- |
| `un-` | not, negation, privation | `un-kula` light/easy (not-heavy) |
| `ni-` | opposite, contrary, anti- | `ni-kéma` misunderstand |
| `ré-` | again, re-, back | `ré-dora` reopen |
| `né-` | before, pre-, ex- | `né-vista` preview (before-see) |
| `wé-` | after, post-, future | `wé-kiva` postscript, follow-up |
| `mi-` | mid-, inter-, between | `mi-tiva` corridor (between-room) |
| `hi-` | over-, super-, hyper- | `hi-méra` open ocean (above-sea) |
| `lu-` | under-, sub-, infra- | `lu-méra` seabed, submarine zone |
| `ko-` | with, co-, joint | `ko-kivor` colleague |
| `dis-` | across, trans-, through | `dis-sova` translation |
| `zu-` | bad, mal-, mis- (pejorative) | `zu-viva` misfire, foul (bad-shoot) |
| `gavo-` | good, well-, eu- | `gavo-gai` welcome (well-come) |

### 15.2.2 Noun-forming suffixes

| Suffix | Meaning | Example |
| --- | --- | --- |
| `-or` | doer, agent | `kémor` teacher (know-er) |
| `-pira` | tool, instrument | `fóra-pira` knife (cut-tool) |
| `-tavi` | platform, surface, table | `kiva-tavi` desk |
| `-tiva` | room, chamber, container | `livo-tiva` classroom |
| `-nása` | house, building, institution | `kéma-nása` school |
| `-an` | place, habitat, natural site | `fira-an` nest |
| `-os` | group, collective, corps | `fira-os` flock |
| `-ét` | young, offspring | `lavo-ét` puppy |
| `-ik` | one resembling, -like (also adj) | `fira-ik` birdlike |
| `-va` | act, process (verbal noun) | `sola-va` playing |
| `-ké` | result, product, completed state | `féma-ké` a meal eaten |
| `-sula` | great form; abstract quality when on a noun | `sulo-sula` greatness |
| `-nira` | small form; endearment | `kora-nira` bucket |
| `-moka` | outward location, out- | `tiva-moka` outdoors |
| `-nilo` | inner location, in- | `tiva-nilo` indoors |
| `-síka` | piece, fragment, -let | `fura-síka` fruit-piece |
| `-kosa` | -ness, -ity (state noun, on adjectives) | `béla-kosa` beauty |

### 15.2.3 Adjective-forming suffixes

| Suffix | Meaning | Example |
| --- | --- | --- |
| `-ik` | having the quality of, -y | `koma-ik` painful |
| `-oka` | having (possessive adjective) | `vosa-oka` fleshy |
| `-uma` | lacking, -less (privative) | `fola-uma` hairless |
| `-vela` | full of, rich in | `riva-vela` joyful, joy-filled |
| `-sama` | like, similar to | `luno-sama` catlike |
| `-ona` | made of, material | `luma-ona` light-made |
| `-jan` | able to be, -able | `kiva-jan` doable |
| `-jira` | needing to be, -worthy | `nava-jira` wash-needing |

### 15.2.4 Verb-forming suffixes

| Suffix | Meaning | Example |
| --- | --- | --- |
| `-ka` | causative: make, cause to | `kiva-ka` employ, set to work |
| `-ta` | inchoative: become | `nula-ta` get cold |
| `-sa` | factitive: produce, emit | `luma-sa` shine, give light |
| `-ni` | instrumental: do with | `fóra-ni` cut with a knife |
| `-ruka` | repetitive / habitual | `kosa-ruka` chatter |
| `-ski` | attempt, try to | `tora-ski` attempt an attack |
| `-bira` | malefactive: do to harm | `kosa-bira` talk behind someone's back |

### 15.2.5 Inflectional suffixes (obligatory, outermost)

| Suffix | Meaning | Example |
| --- | --- | --- |
| `-s` / `-as` | plural (-s after vowel, -as after consonant) | `lavos` dogs |
| `-la` | possession | `mi-la` my |
| `-ji` | ordinal | `ona-ji` first |
| `-lé` | adverb (manner) | `gavo-lé` well |

## 15.3 Derivation pipeline (normative)

Derivation is strictly ordered; the slots are applied left to right.

```
PREFIX  +  ROOT  +  DERIVATION SUFFIX  +  INFLECTION
(gavo|un|ni|ré|…)   (kiva)  (-or|-pira|-tiva|-ka|-ik…)  (-s|-la|-ji|-lé)
```

Examples: `un-kiva-jan-lé` "unemployably"; `ré-kosa-ruka-va` "chattering
again"; `lu-méra-pira` "deep-sea tool". At most **three** derivational affixes
per word in Standard prose (§15.7); more must be registered as a term (§15.8).

## 15.4 Deriving each word class (normative)

**Noun → verb.** `-ka` causative, `-ta` become, `-sa` produce, `-ni` use:
`kora` heart → `kora-ka` encourage, `kora-ta` take courage, `kora-ni` do by heart.

**Verb → noun.** `-or` agent, `-pira` instrument, `-tiva` room, `-va` act,
`-ké` result, `-an` place: `sola` play → `sola-or` player, `sola-pira` toy,
`sola-tiva` playroom, `sola-va` playing, `sola-ké` a finished game.

**Verb/adjective → adjective.** `-ik` quality, `-jan` able, `-jira` worthy,
`-akta` past-participial: `sola-ik` playful, `sola-jan` playable, `sola-jira`
worth playing, `sola-akta` played-out.

**Adjective → adverb.** `-lé`: `sulo-lé` strongly; `-nira-lé` mildly.

**Adjective → abstract noun.** `-kosa` or `-sula`: `béla` beautiful → `béla-kosa`
beauty; `sulo` strong → `sulo-sula` strength (great).

**Noun → adjective of material/origin.** `-ona` made of, `-vela` full of,
`-uma` without: `tira-ona` metal-made, `riva-vela` joyful, `fola-uma` hairless.

**Noun → diminutive / augmentative.** `-nira` small/endearing, `-sula` large,
`-ét` young: `luno-nira` kitten, `luno-sula` a great cat, `lavo-ét` puppy.

**Abstract / collective.** `-sula` (quality), `-os` (group), `-kosa` (state):
`misi-os` a people, `liso-kosa` hardness.

## 15.5 Zero derivation

Any adjective may be used as a noun, and vice versa, with no suffix:
`béla` *beautiful / beauty*, `sulo` *strong / strength*, `koma` *pain / hurt*.
The dictionary records both readings. Prefer zero derivation over coining an
`-sula` form when the dictionary already has the adjective.

## 15.6 Reduplication

Whole-word repetition marks reciprocal or distributive meaning: `ona-ona`
*each other*. Only dictionary-recorded reduplications are lexemes; a new one is
understandable but enters the dictionary only with a registered gloss.
Reduplication never marks plurality (`-s` does).

## 15.7 Compounding

- **Head-first:** the first element is the semantic head; every later element
  specifies it: `nela-sula` water+great = *ocean*; `kiva-nira` work+small =
  *gadget*; `kora-jula` chest+serving = *server*; `sova-nela` speech+stream =
  *language*; `luma-saro` light+star = *flashlight*.
- Any two (or three) dictionary words may combine; the compound is grammatical
  at once. Three elements are the prose limit; four only in Technical names.
- Writing: closed unless the dictionary hyphenates the compound (§2.6).
- **Transparent nesting** is required for parsing: `luma-kora-pira` is read
  `(luma-kora)-pira` (battery-tool), never ambiguously.
- A compound is licensed by *meaning*: the head must denote a real class the
  modifier restricts (`kéma-nása` know-house = school, not "a knowledgeable
  building").

## 15.8 Terminology (how Technical Beluma is coined)

New scientific and technical words MUST be built from existing roots where
possible; loans (§15.10) are the fallback. Standard patterns:

| Concept | Beluma pattern | Example |
| --- | --- | --- |
| discipline | `X-kéma` (knowledge of X) | `saro-kéma` astronomy |
| instrument | `X-pira` | `hurox-pira` microscope |
| process | `X-va` | `fosa-va` fusion |
| person in field | `X-or` / `X-kivor` | `kimia-kivor` chemist |
| theory / system | `X-sula` | `gravita-sula` theory of gravity |
| measurement | `X-méra` | `sumés-méra` chronometry |
| small/particle | `X-nira` | `luma-nira` photon-let |
| device/network | `X-nása` | `kêve-nása` server-hub |

A term is legitimate when a Beluma speaker who knows the roots could infer its
meaning. Terms are registered with a `[technical]` tag (§23).

## 15.9 Root coining rules (normative)

New **roots** are the rarest addition. A candidate root MUST:

1. obey the alphabet (no `c`, `q`, `y`; write `k`, `s`/`kv`, `i`) and §1
   phonotactics (legal onsets, penult stress);
2. not collide with an existing entry (§15.10);
3. not be a synonym of an existing root unless it adds a needed distinction
   (avoid synonym surplus);
4. be short (1–3 syllables) and end in a vowel for easy compounding;
5. be built from the semantic-field primitives where one already exists.

Roots are proposed by the Academy (§25), validated (§24), and registered with a
VTXT bump.

## 15.10 Collision rules and loanwords

A candidate word is rejected if it: differs from an entry only by accent; equals
an entry after stripping plural/possessive marking; is a near-homophone (§1.9.4);
or violates §1 phonotactics.

**Loans** enter by respelling: no `c/q/y`, §1 phonotactics, penult stress, noun
final vowel. Attested: `komputa` < computer, `programa` < program, `porsenta` <
percent, `muzika` < music, `telefona` < telephone, `foto` < photo. When a loan
collides with a native root, **the native word wins** and the loan is reshaped or
rejected.

## 15.11 Capacity (why 250,000+ is reachable)

The reachable lexicon is combinatorial:

```
reachable  ≈  R × (1 + A)  +  R × M  +  H × M
             └ derived ┘      └ 2-part ┘  └ heads × modifiers ┘
```

With `R = 2,000` roots, `A = 30` derivation affixes, `M = 2,000` modifiers and
`H = 500` classifier heads:

- derived words: `R × A` = **60,000**
- two-part compounds: essentially unbounded; even 5% registration = **>200,000**
- registered core (roots + common derivations + named terms): **>20,000**

The Academy registers only words in actual use; the *capacity* above is what any
speaker can produce correctly on demand, which is what makes Beluma scalable.
`tools/grow.py` computes and reports this capacity from the live dictionary.

## 15.12 Registration

1. Build the form by §15.2–§15.10.
2. Check with `tools/validate_dict.py` (§24).
3. Add the entry to `lexicon/h.txt` with gloss(es) and register tag; bump `VTXT`.
4. Until registered, a form is a transparent derived word or compound — still
   grammatical and parseable, just not yet "official".

**Register of coinage:** roots enter as **Standard**; domain terms as
**Technical** (§23) and are promoted by usage via a VTXT change. Words only for
Informal use are tagged `colloquial` and must still obey §15.10 rules 1–4.
