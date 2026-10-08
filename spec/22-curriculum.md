# §22 Curriculum and Translation Guide — Beluma Language Standard v1.0

Status: **Normative** for the teaching sequence; **Informative** for method.

## 22.1 The learning path

The curriculum lives in `course/`. It teaches Standard Beluma first (§23.1),
then the three other registers. Six levels, each with reading, writing,
listening, and speaking goals:

| Level | Beluma | Can-do |
| --- | --- | --- |
| A1 | `baza-onaji` | sounds, alphabet, 200 heads, present tense, greetings |
| A2 | `baza-tuji` | full noun/verb morphology, questions, negation, 500 heads |
| B1 | `mi-onaji` | all tenses/aspects, modals, relative clauses, 1,200 heads |
| B2 | `mi-tuji` | derivation (§15), compounds, formal/informal switching |
| C1 | `sula-onaji` | Technical and Formal registers, domain texts, 2,000+ heads |
| C2 | `sula-tuji` | translation, corpus study, conformance work (§24) |

## 22.2 Order of instruction

1. **§01–§02** sounds and writing — read every legal cluster aloud.
2. **§03–§04** grammar core and pronouns — build SVO sentences.
3. **§05–§08** nouns, verbs, questions, negation.
4. **§09–§14** adjectives, adverbs, prepositions, conjunctions, numbers, time.
5. **§15** word formation — the productivity engine; teach before vocabulary
   drilling, so learners coin words instead of memorizing.
6. **§16–§19** domains, register-appropriate.
7. **§20–§26** reference and rules.

## 22.3 Assessment

Each level ends with a conformance sample (§24.2). A B2 pass means the learner
can derive new words on demand; a C1 pass means they can write a conformant
domain text at the right register.

## 22.4 Translation principles

### 22.4.1 Direction

- **Into Beluma:** translate **sense**, not words. Prefer a built word (§15)
  over a calque; admit a short international loan only if none fits.
- **Out of Beluma:** give the plain sense; render register (a Formal text
  becomes formal English, an Informal text casual English).

### 22.4.2 The four steps

1. **Segment** the source into clauses.
2. **Strip** register-neutral content; identify actors, actions,
   times, and conditions.
3. **Re-map** onto Beluma's pipeline (§03.2): topic `ia`, subject, tense
   `un (né|wé|wés)`, aspect/modal, verb, object, PP, manner.
4. **Re-derive** any missing concept via §15 and register it (§20.10).

### 22.4.3 Lexical gaps

When a concept has no head: (a) look for a §15 derivation; (b) if it is
international and short, respell as a loan (§15.10); (c) only then propose a new
root through the Academy (§25).

### 22.4.4 Register mapping

| Source register | Beluma register |
| --- | --- |
| legal / diplomatic | Formal (§23.2) |
| scientific / technical | Technical (§23.3) |
| news / reference | Standard |
| chat / fiction dialogue | Informal |
| poetry / oratory | Literary Standard (§23.4) |

### 22.4.5 Names and numbers

Proper names are respelled to Beluma phonology (§15.10) and kept as bare nouns:
`Londona`, `Shangai`, `Mila`. Numbers are spelled out in Standard and Formal,
digit-form in Technical (§13.2). Dates follow §14.6.

## 22.5 Worked example

Source (English): *"The government must protect citizens' data."*

1. Actors: government (`registaro`), data (`datumaro`), citizens
   (`sivitanos` → `lé sivitanos`).
2. Modal: `gida` *must*; verb: protect (`garda`).
3. Register: legal → **Formal**, passive preferred.

Formal output:

> `Lé datumaro gida s gardi-ké li lé registaro pro lé sivitanos.`
> *Data must be protected by the government for the citizens.*

Standard output:

> `Lé registaro gida garda lé datumaro de lé sivitanos.`

## 22.6 Exercises (informative)

- Derive `X-sienko` for *biology*, *geology*, *psychology* (§15.8).
- Convert §21.2 Informal dialogue to Standard (§23.1).
- Translate five lines of a treaty into Formal and justify each register
  choice (§18.1).

## 22.7 Tools for learners

| Tool | Use |
| --- | --- |
| `site/dictionary.html` | search the lexicon |
| `tools/validate_dict.py` | check a new word |
| `tools/grow.py` | see licensed derivations |
| `course/` | the graded lessons |
| `library/` | reference articles |
