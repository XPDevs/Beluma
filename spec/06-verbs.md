# §06 Verbs and Tense — Beluma Language Standard v1.0

Status: **Normative.** Verbs never conjugate. Person, number, and gender never
touch the verb; tense, aspect, mood, and voice are carried by pre-verbal particles,
auxiliaries, and two participle suffixes.

## 6.1 The bare verb

- The unmarked verb is present tense, any person, any number:
  `Mi gai.` *I go.* — `Misu gai.` *They go.*
- The verb form is the dictionary form; there is no infinitive marker. A verb used
  as a noun takes `-va` (§6.8): `lé sola-va` *the playing*.

## 6.2 Tense particles

| Particle | Meaning | Example | Gloss |
| --- | --- | --- | --- |
| (none) | present | `Mi gai.` | I go / I am going |
| `né` | past | `Mi né gai.` | I went |
| `wé` | future | `Mi wé gai.` | I will go |
| `wés` | imminent (*about to*) | `Mi wés gai.` | I am about to go |

Position rules:

1. The tense particle sits after the subject (and any time adverb), after `un`
   when negated, before aspect and modals:
   `Mi un né gai.` — *I did not go.* (`un` precedes `né`)
2. `wés` is **not** a negative future: *will not* is `un wé`
   (`Mi un wé gai.` — *I will not go.*). The retired reading *won't* for `wés`
   is obsolete; texts using it are non-conformant.
3. Only one tense particle per clause.

## 6.3 Aspect

Aspect reuses two items every speaker already has — the copula `s` and the
suffixes `-va` (-ing) and `-ké` (-ed) — plus three auxiliary verbs.

| Aspect | Construction | Example | Gloss |
| --- | --- | --- | --- |
| progressive | `s` + V-`va` | `Mi s gai-va.` | I am going |
| past progressive | `né s` + V-`va` | `Mi né s gai-va.` | I was going |
| perfect | `vóta` + V | `Mi vóta gai.` | I have gone |
| past perfect | `né vóta` + V | `Mi né vóta gai.` | I had gone |
| future perfect | `wé vóta` + V | `Mi wé vóta gai.` | I will have gone |
| inchoative | `jála` + V | `Mi jála gai.` | I begin to go |
| habitual | `véta` + V | `Mi véta gai vavi.` | I usually go in the morning |
| iterative | `ré-` + V | `Mi ré-gai.` | I go again |

- The aspect words are ordinary words: `vóta` = *finish*, `jála` = *begin*,
  `véta` = *every* — the aspect word owns the clause and the main verb is its
  object (head-first, §15).
- `véta` before a verb = *usually/each time*; before a noun = *every*: `véta misi`
  *every person*. No ambiguity in practice.
- Stacking: tense > aspect > modal. At most **one** aspect word and **one** modal
  per clause: `Mi né vóta gida kiva.` — *I had to finish work.* (lit. I past
  finish must work). More deeply layered meanings use two clauses.
- `ré-` is the only bound aspect; it attaches directly to the verb, hyphenated:
  `ré-gai`, `ré-féma`.

## 6.4 The participles

| Form | Meaning | Uses |
| --- | --- | --- |
| V-`va` | -ing, ongoing | progressive with `s`; verbal noun |
| V-`ké` | -ed/-en, completed state | passive with `s`; *become ADJ* |

- `-ké` on an adjective phrases *have become*: `Lé néla s nula-ké.` — *The water
  has become cold.* `Mi s ésa-ké.` — *I have become tired.*
- The verbal noun: `Lé sola-va s réva.` — *The playing is fun.*

## 6.5 Voice — active and passive

- Active: ordinary SVO. `Lé bino né féma lé fura.` — *The boy ate the fruit.*
- Passive: front the object as subject, verb = `s` + V-`ké`, doer with `li`:

| Active | Passive |
| --- | --- |
| `Lé bino né féma lé fura.` | `Lé fura né s féma-ké li lé bino.` |
| *The boy ate the fruit.* | *The fruit was eaten by the boy.* |

- Agentless passive: omit the `li` phrase: `Lé tura s dora-ké.` — *The door is opened.*
- Perfect passive: `vóta s` + V-`ké`: `Lé fura vóta s féma-ké.` — *The fruit has
  been eaten.*
- Register: passive is Formal/Standard (law, news, academic); Informal prefers
  active or the generic agent `zava` (*one*): `Zava né féma lé fura.`

## 6.6 Modals

All modals take a bare verb; tense composes to their left.

| Modal | Meaning | Example |
| --- | --- | --- |
| `kima` | can, be able | `Mi kima gai.` — I can go |
| `unkima` | cannot | `Mi unkima gai.` — I cannot go |
| `néma` | may (permission) | `Tu néma gai.` — You may go |
| `gida` | must, have to | `Mis gida gai.` — We must go |
| `gida-nira` | ought to (mild) | `Tu gida-nira soma.` — You ought to sleep |
| `sud` | should (advice) | `Tu sud gai.` — You should go |
| `unsud` | shouldn't | `Tu unsud gai.` — You shouldn't go |
| `da-va` | would, could, might | `Mi da-va gai.` — I would go |
| `vento` | maybe (likelihood adverb, verb-final scope) | `Vento nivo gai.` — Maybe he goes |

Negation of modals — use the modal's own form or `un`, with these fixed readings:

| Reading | Beluma |
| --- | --- |
| don't have to | `un gida` |
| must not / not allowed | `du` (command) or `un néma` |
| cannot | `unkima` (or `un kima`) |
| shouldn't | `unsud` (or `un sud`) |
| won't have to | `un wé gida` |

Tense + modal examples: `Mi né kima gai.` — *I could go.* — `Mi wé gida gai.` —
*I will have to go.* — `Mi un wé gida gai.` — *I won't have to go.*

## 6.7 Conditionals

- Open/likely condition: `da` clause + main clause: `Da tu suda, mi wé gai.` —
  *If you call, I will go.* (verify `suda` = call; else rephrase in your text)
- Hypothetical/counterfactual: `da` clause + `da-va` main clause:
  `Da mi né suda, mi da-va gai.` — *If I had called, I would have gone.*
- `né da-va` + verb = *would have*: `Mi né da-va gai.` — *I would have gone.*
- `da` always opens the condition clause; the result clause follows in normal
  order. Conjunction cross-reference: §12.

## 6.8 Imperatives

- Affirmative: bare verb, subject omitted: `Gai!` *Go!* — `Féra lé fura!`
  *Cut the fruit!*
- Subject emphasis (rare, Standard): `Tu gai!` — *You go!*
- Negative: `du` + verb: `Du gai!` — *Don't go!* — `Du féra lé fura!`
  *Don't cut the fruit!* (`du` replaces `un`; §08)
- Politeness: sentence-initial `téva` (*please*): `Téva gai po ra.` — *Please
  come near.* — or the idiom `téva-gavo` style requests per §23.
- There is no imperative inflection and no vocative requirement.

## 6.9 The copula `s`

- Equational: `Mi s misi.` — *I am a person.*
- Locative: `Mi s na nésa.` — *I am in the house.*
- With adjectives (no *-ly* verb needed): `La loma s béla.` — *The tree is beautiful.*
- Tense applies to `s`: `Mi né s na nésa.` — *I was in the house.* — `Mi wé s.` —
  *I will be.*
- Negation: `un` before `s`: `Mi un s esa.` — *I am not tired.*
- 3 sg subjects use `s` unchanged: `Nivo s koma.` — *He is in pain.*
- Tag questions: Informal uses `koro?` (`Siva s gavo, koro?`); Formal states a
  short declarative with `kvo`: `Siva s gavo. Kvo un?` — or simply no tag.
  Formal writing SHOULD avoid tags entirely.

## 6.10 Existential `esto`

`esto` = *there is / there are* (from `esera` = being):

- `Esto o loma ra lé nésa.` — *There is a tree near the house.*
- `Un esto o misi na lé tiva.` — *There is no one in the room.*
- `Esto misu na lé méra.` — *There are people at the sea.* (plural is on the
  subject noun, never on `esto`)
- Negation is `un esto`, never `zéra esto`.

## 6.11 Informal irregular forms

Informal speech memorises high-frequency pasts as whole chunks, bypassing `né`:

| Standard | Informal | Gloss |
| --- | --- | --- |
| `Mi né s.` | `Mi rá.` | I was |
| `Mi né diva.` | `Mi dá.` | I did |
| `Mi né gai.` | `Mi víra.` | I went |

- These forms are **Informal register only** (§23). Standard, Formal, and
  Technical texts MUST use `né`.
- They compose with aspect: `Mi rá s gai-va.` — *I was going.* —
  `Mis dá jála lérn.` — *We began to learn.*
- `rá`, `dá` are accent-pair words (§1.5.4): `ra` *near* vs `rá` *was*,
  `da` *if* vs `dá` *did*; spelling MUST be exact.
- Dictionary note: `víra` carries both the irregular-past gloss and the
  unrelated lexical senses *green / life* (§26.4 homographs).

## 6.12 Verb inventory notes (informative)

Light and support verbs keep their literal meanings: `diva` *do/make*, `gai` *go*,
`vóta` *finish*, `jála` *begin*. A verb used with a borrowed noun (`programa diva`)
is still `diva` — no support-verb inflection differences exist.
