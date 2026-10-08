# §03 Grammar: Sentence Structure — Beluma Language Standard v1.0

Status: **Normative.** Beluma is analytic and SVO: order carries the grammar,
inflection carries nothing.

## 3.1 Clause structure

The canonical clause is the slot pipeline below. Slots are written in fixed order;
a slot that is empty is simply absent — no filler words appear.

| # | Slot | Filled by | Notes |
| --- | --- | --- | --- |
| 0 | Topic | noun phrase + `ya` | optional, §3.3 |
| 1 | Subject | noun phrase / pronoun | required in Formal, droppable §04 |
| 2 | Time adverb | time word or PP | `safa`, `na túo vora` |
| 3 | Negation | `un` | §08 |
| 4 | Tense | (none) / `né` / `wé` / `wés` | §06 |
| 5 | Aspect / modal | `vóta` `jála` `véta` / `kima` `gida` … | §06 |
| 6 | Verb | bare verb | never inflected |
| 7 | Object | noun phrase | |
| 8 | Prepositional phrases | PPs in time > place order | §11 |
| 9 | Manner | adjective + `-lé` | §10 |

```
[ya TOPIC] SUBJECT (TIME) un (né|wé|wés) (ASPECT|MODAL) VERB (OBJECT) (PP …) (MANNER-lé)
```

Examples:

- `Mi né féra fura.` — *I cut the fruit.*
- `Mi un né féra fura.` — *I did not cut the fruit.* (`un` before `né`)
- `Siva wé gai po nésa.` — *She will go home.* (time > place)
- `Lé fira hura vévlo gavo-lé.` — *The bird flies very well.*

## 3.2 The noun phrase

Internal order, outermost first:

```
DEMONSTRATIVE  POSS(-la)  NUMERAL  ADJECTIVE  NOUN  (RELATIVE CLAUSE)
```

- Demonstratives: `eka` this (near speaker), `oka` that (near listener), `ta`
  that (far); `ta` doubles as relative "that" (§3.5).
- Articles `lé` (definite) and `o` (indefinite) sit **before** the demonstrative
  when both appear: `lé eka loma` *this tree (known)*; `o eka loma` *this tree (first
  mention)*. Articles are optional but normal in Standard and Formal.
- Order examples:
  - `mi-la túo béla loma` — *my two beautiful trees*
  - `oka nira fira` — *that small bird*
  - `o susa sulo keran` — *a strongest man* (attic: `susa` + noun = "the strongest
    of the group" when definite: `lé susa sulo keran`).

## 3.3 Topic fronting

`ya` fronting moves the most important information to slot 0 and is followed by a
comma. It is normal in Informal and permitted in Standard; Formal prefers plain SVO.

- Standard: `Mi né féra fura.` — *I cut the fruit.*
- Informal: `Fura ya, mi né féra.` — *The fruit, I cut it.*

Only one `ya` topic per clause. The rest of the pipeline is unchanged.

## 3.4 Coordination

- `unas` *and*, `ora` *or*, `néka` *but* join words, phrases, and clauses at the
  same level; they sit between the elements, never sentence-initially in Formal
  (use `néka` clause-initially only in Standard/Informal; Formal starts a new
  sentence or uses `tamen`, §12).
- Before the last element of a list of three or more: `a, b unas c`.
- Coordinated subjects take a singular predicate if the items form one unit:
  `Méra unas nela s nula.` — *Sea and water are cold* (one body of water).

## 3.5 Relative clauses

A relative clause is placed **directly after its noun**, and keeps perfectly normal
SVO order — nothing moves to the front.

| Word | Role | Example |
| --- | --- | --- |
| `ka` | subject relative (*who/which*) | `lé misi ka s unréva` — *the person who is sad* |
| `ta` | object relative (*whom/that*) | `lé fura ta mi né féra` — *the fruit that I cut* |
| `ka-la` | possessive (*whose*) | `lé keran ka-la lavo` — *the man whose dog* |

- Non-restrictive relatives are set off with commas: `Siva, ka mi léva, s nira.`
  — *Siva, whom I love, is small.*
- Nesting is allowed but a Formal text SHOULD keep to one level: a second relative
  may instead start a new sentence.
- The relative `ka` is a different word from the question word `kvasi` (§07) —
  English uses *who* for both; Beluma keeps them apart.
- `ta` is also the demonstrative *that*; the noun it attaches to decides the reading.

## 3.6 Sentence types

| Type | Marking | Example |
| --- | --- | --- |
| Declarative | statement, final `dota` | `Mi gai po nésa.` |
| Interrogative | fronted `kvo` or wh-word, `kwamorka` | §07 |
| Imperative | bare verb, (exclamative) | `Gai!` *Go!* — negative: `du gai!` §08 |
| Exclamative | statement + `fimorka` | `Tu s vévlo gavo!` — *You are very good!* |

## 3.7 Word order variation (informative)

Focus commonly lands clause-final (slot 9's position or the object's) — a focused
object may move after the PPs, and contrastive topics use `ya` (§3.3). Questions
never invert subject and verb (§07). Passive reorders to `s + V-ké` with the agent
in a `li` PP (§06).
