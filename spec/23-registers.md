# §23 Registers — Beluma Language Standard v1.0

Status: **Normative.** Beluma has four registers. Every conformant text is written
in one of them; mixing is allowed only where §23.3 permits it.

## 23.1 The four registers

| Register | Domain | Morphology | Syntax & lexicon |
| --- | --- | --- | --- |
| **Standard** | general writing, media, teaching | full forms: `mi-la nésa`, regular tenses (`né`, never `rá`) | complete SVO sentences; accents optional (§1.5); articles normal |
| **Formal** | law, diplomacy, academia, ceremonies | Standard morphology, **no** fusions, no ellipsis | accents **required** on penults; articles always explicit; passive preferred (§6.5); no discourse markers; no tag questions |
| **Informal** | speech, friends, family, messages | fusions (`mila` my, `nésana` at home, `wégai` will go), irregular pasts (`rá` was, `dá` did, `víra` went) | topic `ya`, dropped subjects/articles, ellipsis, discourse markers (`evi`, `koro`, `maka`), idioms |
| **Technical** | science, IT, engineering | Standard morphology + digit-style numbers (`zer` … `dek`), respelled loans (§15.5) | definitional sentences, Arabic numerals allowed (§2.4), precise cross-references |

## 23.2 How the registers differ

**Morphology.**

| Feature | Standard / Formal | Informal |
| --- | --- | --- |
| possession | `mi-la nésa` | `mila nésa` (fused entry) |
| location phrase | `nésa na` | `nésana` (fused entry) |
| future | `mi wé gai` | `mi wégai` (fused entry) |
| past of `s` | `mi né s` | `mi rá` |
| past of `diva` | `mi né diva` | `mi dá` |
| past of `gai` | `mi né gai` | `mi víra` |

- Fused and irregular forms exist as dictionary entries tagged `colloquial`.
  They are **Informal only**: Standard, Formal, and Technical texts MUST NOT use
  them (except where a fusion is the dictionary's sole spelling — the dictionary
  tag decides, and §26 lists the transitional cases).
- Formal additionally requires accents on every penultimate syllable; Standard
  makes them optional; Informal usually drops them except on accent-pair words
  (§1.5.4, which are never droppable).

**Syntax.**

- Topic `ya` fronting (§0.3): Informal default, Standard permitted, Formal avoided.
- Subject and article dropping: Informal only (§4.5).
- Ellipsis (`dota-tro`): Informal only.
- Passive: Formal/Standard; Informal prefers active or generic `zava` (§6.5).

**Lexicon.**

- Discourse markers — Informal only: `evi` *well…/um*, `koro` *really?/I'm
  listening*, `maka` *actually/in fact*.
- Idioms — mostly Informal, fixed and non-compositional: `méra-nako` *thanks very
  much* (sea-of-thanks), `luma-kúna` *dizzy* (light-head), `nula-vosa`
  *goosebumps* (cold-flesh), `tuma-sulo` *courage* (heart-great).
- Technical loans and digit-style numbers: Technical register only (loans are also
  fine in Standard once registered — §15.8).

## 23.3 Mixing rules

1. **One register per text.** Texts, exam answers, and corpus entries carry a
   register tag: `[standard]`, `[formal]`, `[informal]`, `[technical]`.
2. Quoted speech inside a Formal text may stay Informal if the quotation is
   marked with `sa-morka`.
3. A Technical text MAY use Standard sentence furniture but MUST keep digit-style
   numbers and loan spellings internally consistent.
4. Formal MUST NOT contain any Informal item; a Formal text with `mila`, `rá`,
   `ya`, or `evi` is non-conformant.
5. Titles, dictionary headwords, and examples in this Standard are **Standard**
   unless labelled otherwise.

## 23.4 Literary style

Literary prose and poetry are written in Standard or Formal — never Informal —
and may use the full expressive machinery of those registers: fronting for rhythm,
relative-clause chains, `-lé` manner tails, and the poetic license of moving a
stressed word to clause end (§1.8). Rhyme and meter conventions live with the
corpus (`library/poetry/`); nothing in §03–§15 is relaxed for verse.

## 23.5 Register change over time

An Informal form enters Standard only by:

1. general attestation in the corpus, and
2. a VTXT bump that re-tags the entry from `colloquial` to `standard`, and
3. passing §24 validation.

Until all three hold, the old tag governs. This is the language's change process:
**usage proposes, the dictionary disposes.**

## 23.6 Register of this corpus (informative)

| Material | Register |
| --- | --- |
| `course/` lessons, `site/` documentation | Standard (examples) / Formal (reference prose) |
| `library/corpus/` dialogues | tagged per text; square-market dialogues are `[informal]` |
| `library/poetry/`, `library/story/` | Standard/Formal |
| `exams/` | answers MUST match the question's register tag |
| `canon/` | archived pre-1.0 drafts — not register-governed, not normative |
