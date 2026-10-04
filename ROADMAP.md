# Lía Beluma — Master Roadmap (Canon Build)

Lead Architect checkpoint document. Version the roadmap with the dictionary: every new
dict version number in `h.txt` (`VTXT=` line) corresponds to a roadmap checkpoint.

---

## PHASE 0 — AUDIT (completed)

### What exists (verified against the files in this repo)

| Area | Status | Files |
| --- | --- | --- |
| Phonology & script | Complete (23 letters, stress-accent, open-syllable bias) | `index.html`, `grammar.html`, `lessons.html` |
| Basic SVO syntax | Yes | `grammar.html` §2 |
| Basic pronouns | Partial (person forms + `-la` possessives) | `h.txt` lines 8–27, `grammar.html` §4 |
| Tense marking | Yes (`né` past, `wé` future, zero present) | `grammar.html` §5 |
| Negation & imperatives | Yes (`un`, `du`) | `grammar.html` §10 |
| Yes/no + wh- questions | Partial (`kvo`, wh- set) | `grammar.html` §10 |
| Relative clauses | Basic (`ka`, `ta`, `ka-la`) | `grammar.html` §13 |
| Article system | Minimal (`lé`, `o`) | `grammar.html` §2 |
| Derivation/compounding | Strong (head-first, productive) | `grammar.html` §7 |
| Two number systems | Yes (classic + digit) | `grammar.html` §9 |
| Formal vs colloquial register | Inventive (fusions, suppletion, discourse markers) | `grammar.html` §12 |
| Idioms | Small starter set | `h.txt` "IDIOMS" block |
| Dictionary | 742 entries | `h.txt` |

### What is MISSING (against the master roadmap)

1. **Core grammar systems absent:** passive voice, aspect system, complete
   conditionals (real/irrealis/counterfactual), complete modal stack with
   tense interactions, full definiteness rules, correlative pronoun system,
   clusivity, formal address rules, reflexive/reciprocal standardization.
2. **Dictionary:** 742 words vs 50,000 minimum target (0.15%). No
   domain coverage in science/philosophy/law/medicine/politics/engineering.
3. **Literature:** zero works. Only example sentences.
4. **Native speakers:** no plan, no child-raising toolkit.
5. **Media:** zero. One translator page only.
6. **Utility/games:** zero game or platform assets.
7. **Education:** one 20-minute course, one grammar page. No textbook,
   no exams, no certification, no teacher program, no university syllabus.

### Conflicts flagged (existing material disagrees with itself)

| # | Conflict | Source A | Source B | Proposed resolution |
| --- | --- | --- | --- | --- |
| C1 | `wés` meaning | `h.txt`: "will not / won't" | `grammar.html` §5: "about to" | **RESOLVED (Phase 2):** canonical = *about to / imminent*. `will not` = `un wé`. `h.txt` edited; `beluma.js` renders `wés` as subject-aware "am/is/are about to". Old FUT-NEG branch retired. |
| C2 | First-person object | `h.txt`: `mu = me (object)` + `mi = I / me` | `grammar.html` §4: `mi = I / me`; example "Siva leva mi" | Canonical: **`mu` = object/oblique 1sg**, `mi` = subject 1sg. `Siva leva mu.` = She loves me (SVO keeps subjects first). `mi` as post-verb object allowed only in poetry/lax speech. |
| C3 | Reflexive | `h.txt`: `hasa = self/oneself` | `grammar.html` §4: "repeat pronoun — mi-la mi (myself)" | Canonical: reflexive = **pronoun + `hasa`** (`mi hasa` = myself). `mi-la mi` is *emphatic* ("I myself"), not reflexive. |
| C4 | Homophonous `niva` | `h.txt`: `niva = swim / grow`; `níva = sing` | accent marks stress only → both pronounce `/niva/` | Flag as accepted homonym (compare `koro` bear/really?). `níva` retains accent in learner texts; translators show both senses. |
| C5 | "Language" word | `beluma.js` hardcodes `lingua = language` | no dictionary entry | **RESOLVED (Phase 3):** coined `sova-nela` (speech-stream) = language, `sova-nela-nira` = dialect, `beluma` = the language itself. Hardcode removed from `beluma.js` (FIXED_EN + beToEn fallback). |
| C6 | Duplicate finance terms | `riva-gava = bank / treasury`, `banka = bank`, `gava = money`, `mone = money` | — | **RESOLVED (Phase 3):** `banka`/`mone` relabeled `(loanword)`; `riva-gava`/`gava` remain everyday roots. |
| C7 | Number compounding | index: `vinta-é-kvín` = 25 | grammar: `vinta-kvín` = 25; h.txt uses `-é-` for 17–19 | Canonical: **`-é-` "and" connector only for 17–19** (established forms); plain stacking for other tens (25 = `vinta-kvín`). Document in canon/numbers. |
| C8 | Stray artifacts | `beluma.js` VERB_ROOTS & FIXED_EN contain `hasenge`, `sijan`, `dali`, `morwa`; `h.txt` has `coah` | no glosses | **RESOLVED (Phase 3):** removed all four from `beluma.js` VERB_ROOTS and removed `coah` from `h.txt` (duplicate of `kosa`). |
| C9 | `kva` question word | grammar §10: `kva = which/what` | grammar §13 note: question word is "a separate, older root" | Both true: `kva` = interrogative selector; `ka` = relative. Keep distinct. |

### Design principles locked in (Assumption, labeled — override me if wrong)

The Codex is `h.txt` + `grammar.html` + `beluma.js`. I treat `grammar.html` as the
human-readable spec, `h.txt` as the machine lexicon, `beluma.js` as the reference
analyzer. New canon docs under `canon/` are additions, never rewrites of the phonology,
number systems, or compounding rules.

---

## 7-PHASE DEVELOPMENT ROADMAP

### Phase 1 — Core syntax foundation (NOW)
Pronouns (complete), sentence word order, question formation, possession, definiteness.
Artifacts: `canon/02-pronouns.md`, `canon/03-word-order.md`, `canon/01-articles.md`,
`h.txt` pronoun/correlative batch, this roadmap. → establishes the syntactic spine every
later phase builds on.

### Phase 2 — Verb system (DONE — see checkpoint below)
Aspect (progressive/habitual/perfect/inchoative), passive & voice, full modal stack with
tense composition, conditionals (real/irrealis/counterfactual), relative/adverbial clauses
completed. Also resolves conflict C1 (`wés`). Artifacts: `canon/04-verbs.md`,
`canon/05-clauses.md`, verb dictionary batch, `beluma.js` aspect/voice support.

### Phase 3 — Dictionary machine (0 → 50,000)
- A **coining framework** (`canon/06-lexicography.md`): semantic-field taxonomies,
  head-first compounding spec, affix registry, loanword policy, domain terminology templates.
- Semantic-field **batch generator** (script `tools/coiner.js`) producing words per domain:
  astronomy, biology, chemistry, mathematics, physics, computing, economics, law, military,
  medicine, politics, engineering, emotion, religion/philosophy, slang, everyday-life
  core (~2,000 lemmas per batch), each tagged and validated against `beluma.js`.
- Phased counts: end of P3a 10,000 → P3b 25,000 → P3c 50,000. Longer term 100,000+ is a
  compounding-by-product of the system (any two roots legitimately coin).
- Cleanup list from audit (C5, C6, C8) executed here.

### Phase 4 — Literature & media (thought-tools)
- **Poetry**: define meter & verse from phonology (CV structure + stress), produce
  original poems + songs with glosses.
- **Fiction**: short-story cycle first (a shared town of speakers), then a serialized
  novel, children's books, a newspaper template (`Sova-Néla` "The Language/Stream"),
  a comic script, encyclopedia stub explaining the world in Beluma.
- **Style guides**: `canon/07-style.md` — formal, colloquial, literary, legal-scientific.

### Phase 5 — Education
- Course expansion to 40 lessons (A1→B1), textbook format, drill/answer keys.
- **Certification**: Lía Beluma exams (A1–C2) with papers, listening, oral.
- Teacher program and university syllabus design; integration with translator.

### Phase 6 — Native speakers & community
- Family toolkit (parenting in Beluma), newborn-naming culture, kids curriculum.
- Events: weekly voice nights, writing circles, sports-commentary hands-on.
- Immersion residency plan; target N speakers born per year modeled from media uptake.

### Phase 7 — Utility ecosystem
- **Flagship game** in Beluma (interactive fiction/RPG using the compounding engine as
  its magic system), localization framework for software, YouTube/podcast content plan,
  online community infrastructure, franchise plan.
- Economic moat: the dictionary + analyzer is the "engine"; every word added by the
  community is versioned, credited, and playable.

### Cross-cutting policy (all phases)
- Every phase ends with a **checkpoint**: completed work, artifacts, open questions, next actions.
- **Dictionary versioning:** bump `VTXT=` in `h.txt` per phase; roadmap tracks it.
- **No English-mode prose** in canon docs where the gloss exists — Beluma first, gloss second.

---

## PHASE 1 — DETAILED WORK

### 1.1 Pronoun system (complete)
See `canon/02-pronouns.md`. Summary of decisions:
- Persons 1/2/3 × singular/plural. No grammatical gender (already fixed).
- **Clusivity** added via transparent compounds `mis-vél-tu` (we-with-you, incl.) and `mis-dé-tu` (we-from-you, excl.); `mis` covers both in writing.
- **Epicene 3sg** `miro` (gender-neutral singular "they"); nivo/siva/ét unchanged.
- **Impersonal/generic** `zava` (one); avoids a homonym with `ména` (moon).
- **Formal 2nd person** = `tur` (already the pl.; re-allocated as V-form); familiar = `tu`.
- **Correlative series** built transparently on quantifiers: `ona-`, `zera-`, `ala-`,
  `véta-` + `-misi` (person) / `-bira` (thing) → someone/anyone/everyone, nothing/anything/everything.
- **Reflexive** = pronoun + `hasa`. **Reciprocal** = `ona-ona`.
- Demonstratives: `eka` (this), `oka` (that-near-you), `ta` (that/distant, existing).
- Object/oblique 1sg `mu` canonicalized (resolves C2).

### 1.2 Sentence word order
See `canon/03-word-order.md`. Locked rules:
1. SVO; **topic-first with `ya`** for emphasis (formalizes existing colloquial rule).
2. Particles pipeline (subject precedence):
   `[topic ya] SUBJ (time-word) (un/neg) (TENSE né/wé) (MODAL) VERB [OBJ] ([PP])`.
3. Manner adverbs + `-lé` sit after the verb (or after object); time words before the
   verb by default, clause-final when emphasized.
4. Imperative: verb-initial; 2sg implicit, `tur` explicit for plural/polite.
5. Yes/no `kvo` front; wh-words front, no inversion after them.
6. Subordinators (`kausa`, `da`, `béza`, …) begin their clause; relative clauses are
   postnominal. No movement.
7. Ditransitives: `V [recipient] [theme]` or `V [theme] po [recipient]`; `mu` fills the
   recipient slot. Documented with examples.

### 1.3 Vocabulary batch delivered with this phase
~40 new canon entries appended to `h.txt` (pronouns, correlatives, reflexive/emphatic
phrases, demonstratives, `sova-néla` family, epicene + clusivity + impersonal pronouns).

### 1.4 Files produced
- `ROADMAP.md` (this file)
- `canon/00-directory.md` — canon index, numbering, and versioning rules
- `canon/02-pronouns.md` — the complete pronoun system
- `canon/03-word-order.md` — sentence structure rules
- `h.txt` — Phase 1 vocabulary batch appended (VTXT=3.2)

---

## PHASE 1 — CHECKPOINT

**Completed:** audit of all 6 repo files; conflict register C1–C9 with resolutions;
7-phase roadmap; complete pronoun system; sentence order rules; first testable vocab batch.

**Artifacts:** ROADMAP.md, canon/00-directory.md, canon/02-pronouns.md,
canon/03-word-order.md, h.txt (VTXT 3.1 → 3.2).

**Open questions (for you):**
1. Confirm clusivity (`mis-vél-tu`/`mis-dé-tu`) is wanted in everyday Beluma, or keep `mis` neutral only?
2. Confirm `tur` doubles as formal-address pronoun (vs coining a separate `tusa`).
3. Approve `zava` as "one/impersonal" root (not `mena`, which homonyms with the moon).
4. Adopt the C1 resolution (`wés` = about-to; `will not` = `un wé`)? This changes translator behavior in Phase 2.
5. `sova-néla` for "language" — acceptable, or do you prefer a plain root (e.g. `linua` was hardcoded)?

**Next actions:** (a) your sign-off on labels; (b) begin Phase 2 — verb system doc draft.
Continue from checkpoint when asked, or reply "Continue" to advance to Phase 2.

---

## PHASE 2 — CHECKPOINT (completed)

**Completed:** verb system complete — aspect (progressive via `s`+V-`-va`; perfect via
`vóta`+V; inchoative `jála`+V; habitual `véta`+V; iterative `ré-`), voice (passive via
`li` + `s`+V-`-ké`, with the new generative past-participle suffix `-ké`), full modal
stack with tense composition and negation semantics, conditionals (open / hypothetical /
counterfactual, carried by tense+modal), full clause system (relative incl. oblique,
complement `ta`, embedded questions, adverbial introducers, purpose/result/concession),
existential verb `esto`, temporal reference rules. Conflict C1 resolved (see table).

**Artifacts:** `canon/04-verbs.md`, `canon/05-clauses.md`; `h.txt` VTXT 3.3 (+7 entries:
`vento`, `duna`, `esto`, `fema-ke`, `gai-ke`, `dora-ke`, `gida-nira`; retagged `wés`,
`da-va`); `beluma.js`: imminent marker `wés` (normalized, subject-aware), suffix `-ke`
support, `esto` verb root, `TENSE_MARKERS` accent-normalized lookup.
`canon/00-directory.md`, `canon/03-word-order.md` cross-referenced.

**Engine verification (local `h.txt`, node):**
- `Mi wés gai.` → *I am about to go*
- `Lé fura s féma-ké li lé bino.` → active/passive parse correct
- `Lé fura né s féma-ké li lé bino.` → *the fruit was eaten by the boy*
- `Mi s gai-va.` → *I am going*; `Esto o loma ra lé nésa.` → *There is a tree near the house*

**Open questions (Phase 2):**
1. Approve the `-ké` suffix form (vs alternatives `-tá`, `-nés`)? `-ké` normalized to `ke`
   is collision-free in the dict.
2. Approve coinages `vento` (maybe), `duna` (while/during), `esto` (exist)?
3. Confirm conditional formula resting on tense+modal (no dedicated irrealis particle)?
4. Approve canonical `-ké` on adjectives = "has become" (`s nula-ké` = has turned cold)?

**Next actions:** Phase 3 — the dictionary machine: coining framework (`canon/06`),
semantic-field batch generator (`tools/coiner.js`), domain vocab (astronomy→slang),
cleanup of audit items C5/C6/C8, target 10,000 entries. Reply "Continue" to proceed.

---

## Phase 3 CHECKPOINT — Dictionary Machine ✓

**Completed:** the coining framework canon (`canon/06-lexicography.md`) and a real,
reusable dictionary machine:

- `tools/domain-data.js` — seed corpus: **174 entries across 13 semantic fields**
  (astronomy, mathematics, chemistry & physics, computing, economics & money,
  law & government, military, medicine & body, emotion & mind, music & arts,
  sports & games, everyday life, slang & colloquial).
- `tools/coiner.js` — Canon 06 validation engine, fully re-runnable:
  - **V1** duplicate detection (normalized: lowercase, accents stripped, `-`/space removed);
  - **V2** morpheme resolution (every compound segment must match an existing root/
    corpus segment/affix `un ni re s os an or et va ke`, or a root coined in the same batch);
  - **V3** allows dedicated single-token roots;
  - **V4** flags international loans that lack the mandatory `(loanword)` gloss tag
    (slang loans use `(slang loanword)`);
  - **V5** phonotactic audit (bans `c/q/y`, checks onset clusters `pr tr kr br gr dr fr vr
    sr / pl tl kl bl gl fl vl sl / kv st`, final codas `s n r m l k x`, requires a vowel).
  - Dry run (`node tools/coiner.js`) writes `out/phase3-report.txt`; commit
    (`--commit`) merges accepted entries under a `# VTXT 3.4 · Phase 3` section and
    bumps the `VTXT=` line. Commit is idempotent (re-runs skip already-merged keys).
- **Results:** 174/174 accepted, **0 hard rejections**; 30 soft V5 warnings — all on
  deliberate `(loanword)` borrowings, which canon 06 explicitly allows to bend native
  phonotactics (that is why they are tagged).
- **Audit cleanup executed:** C5 **RESOLVED** — `lingua` hardcode removed from
  `beluma.js` (`FIXED_EN` line + `beToEn['lingua']` fallback); C6 **RESOLVED** —
  `banka`/`mone` relabeled `(loanword)`; C8 **RESOLVED** — `hasenge`, `sijan`, `dali`,
  `morwa` removed from VERB_ROOTS, `coah` removed from `h.txt`.

**Artifacts:** `canon/06-lexicography.md` (Rev 1); `tools/domain-data.js`,
`tools/coiner.js` (new); `h.txt` VTXT 3.4 (+174 entries); `beluma.js` cleanup;
`canon/00-directory.md` + `grammar.html` canon list updated.

**Engine verification (node, local `h.txt`, incl. Phase 1/2 regressions):**
- Phase 1/2 regressions green — incl. `Mi wés gai.` → *I am about to go*,
  `Mi un wé gai.` → *I will not go* (C1), passive `Lé fura né s féma-ké li lé bino.`,
  existential `Esto o loma ra lé nésa.`
- New lexicon spot-checks: `saro-kéma` → *astronomy*, `zanva-meda` → *vaccine*,
  `léva-níva` → *love song*, `hula-gai-or` → *astronaut*, `misés-jura` → *human rights*,
  `koda-fala` → *bug*, `gavi` → *cash*; en→be: `hospital` → *Eza-nesa*,
  `vaccine` → *Zanva-meda*, plural `keys` → *Kelas*.

**Open questions (Phase 3):**
1. Approve the seed corpora / loanword style (transparent compounds + tagged loans)?
   The next batches should extend fields toward ~1,000 native roots, not just loans.
2. `sova-nela` is recorded unaccented (matches `h.txt:907`); canon note uses `sova-néla`.
   Keep unaccented spelling — accents remain stress-only?
3. Word-count target: canon 06 plan says 10,000 by Phase 3 end — realistically this
   machine produces hundreds per batch. Approve shifting bulk volume to Phase 4
   (literature-driven coining) or scale generators now?

**Next actions:** Phase 4 — literature & native fluency: story bank + dialogue corpus +
idioms + canonical translations. Also: (a) extend `tools/domain-data.js` with fields
for Phase 4 flows (foods, fauna, weather, crafts, family-role vocabulary, numbers in
use); (b) convert `canon/*.md` → `*.html` under `canon/` for the site nav (grammar.html
already links them). Reply "Continue" to proceed.

---

## Phase 4 CHECKPOINT — Literature, Media & Style ✓

**Completed:** the style canon and the launch of the Sova-Nésa literature corpus.

**Vocabulary (VTXT 3.5, +69 entries, 0 hard rejections):**
- `canon/07-style.md` — four registers (formal `tur` + full particles; colloquial
  `dus`-affirmation + clips + slang; literary stress/meter + metaphor + archaism;
  legal-scientific `-ké` passives + `ta` complements + loanword spacers).
- **Idiom batch (15)** as multi-word `(idiom)` keys — e.g. `su lé kúna` = exactly right,
  `gava-néla` = worthless, `dora kéla` = breakthrough, `vira-soma` = a busy week.
- **Functional word fields:** food & cooking, fauna & flora, weather & seasons,
  crafts & tools, family & kinship, time & daily cycle (+69).
- `tools/coiner.js` upgraded in the field: fixed an empty-`errs` vacuous-truth bug that
  skipped clean entries; commit now refuses to write when the batch is empty (this also
  killed the stale duplicate-header artifact); coining teams caught **4 real collisions**
  with existing corpus (`luma kúna` *dizzy*, `loma-fura` *stomach*, `loma-nira` *bush*,
  `féra-pira` *knife*) and removed them — the machine earned its keep.

**Literature dossier (`literature/`):**
- `poetry/README.md` — native meter (5·7·5 `nira-sóva`, 8·8 `róla-níva`), two poems.
- `story/episode-01-le-kela.md` — "The Key": the Sova-Nésa cycle launch (town myth:
  *the river gives the morning*), colloquial register, interlinear glosses.
- `sova-nela/` — the weekly paper template + Issue 1 front page (formal register).
- `childrens/ona-tuo-tro.md` — counting book (numbers 1–10 + animals).
- `encyclopedia/sova-nesa.md` — in-universe stub (population, geography, lore).

**Engine verification (node, local `h.txt`):**
- Phase 1/2/3 regressions green. New-batch: 16/16 spot-checks pass incl. multi-word
  idioms `su lé kúna`, `nula kúna`, `gava-néla`, `dora kéla`; en→be still resolves
  `hospital`→`Eza-nesa`, `vaccine`→`Zanva-meda`, `soup`→`Zupa`.

**Artifacts:** `canon/07-style.md`; `literature/` dossier (6 files); `h.txt` VTXT 3.5;
`tools/{coiner,domain-data}.js`; `canon/00-directory.md` + `grammar.html` updated.

**Open questions (Phase 4):**
1. Canon of the town: approve **Sova-Nésa** (Speech-Home) as the shared setting, the
   **Véné** river, the **Kémenta** bridge, the **Méra-Tava** market, and the myth
   "the river gives the morning"?
2. Meter names `nira-sóva`/`róla-níva` and the `-vá` literary progressive variant —
   keep both as literary devices (canon 07 §3)?
3. Idiom keys are recognized by the engine when the full phrase occurs; single-word
   idioms (`vira-soma`) gloss fully. Approve `(idiom)` tagging in the lexicon as
   permanent, and add per-idiom `(register)` marks going forward?

**Next actions:** Phase 5 — education: expand lessons to 40 (A1→B1), textbook + drill
format, exam papers (A1–C2). Also: convert `canon/*.md` → `canon/*.html` for the site
nav; add a dialogue-bank file under `literature/` to feed the drills. Reply "Continue"
to proceed.

---

## Phase 5 CHECKPOINT — Education, Certification & the Site ✓

**Completed:** the full course, the exam program, the teacher/university plan, the
dialogue bank, and the Markdown→HTML site builder.

**Vocabulary (VTXT 3.6 → 3.7, +19 entries, 0 rejections):**
- **Education field (12):** `kéma-nésa` school, `livo` lesson, `léro` learn, `léro-misi`
  learner, `kéma-kiva` study, `kémor-sula` professor, `sak-sula` exam, `móra-kéma` grade,
  `kéma-tésa` diploma, `livo-tiva` classroom, `léro-nira` beginner, `vésa-sova` essay.
- **Examination field (7):** `lóva` read, `lóva-sova` reading, `sova-kéma` grammar,
  `dis` across, `dis-sova` translation, `héna-sova` listening, `sova-tiva` oral.
- **Corpus audit caught real leaks:** I drafted exam/listening/dialogue text that used
  invented words (`tita` = live, `nésa-sula` = town, `péza`, `rédi`, `huta`, `véra` as
  break, `héna-néna` = believe) and **pulled all of them** — the fabricated `tita` was
  even in the A1 listening script. Every line of the dialogue bank and every model answer
  is now dictionary-locked. Also corrected a real mis-gloss in my drafts: `saro-liso` is
  *asteroid*, not *telescope* (`teleskopa` is the loanword), and `éza-nésa` is *hospital*
  (`túsa-nésa` = kitchen!). all now match h.txt.

**The course (`lessons/`):**
- `README.md` — 40-lesson A1→B1 map, books 1–4 by level, the D1–D5 drill system.
- `book-01` (A1: alphabet→numbers→first conversation) through `book-03` (B1: relatives,
  conditionals, passive, speech reports, reading the paper) and `book-04` (B1+ reading:
  register shifts, retelling Episode 1, meter, dialogues, letters, exam workshop,
  project). Every drill = question + hidden answer key, both with glosses.

**Certification (`exams/`):**
- `README.md` — six levels A1–C2, the six-section blueprint (25/25/20/15/10/5), marking
  rules, session delivery, and the **dictionary lock** (a paper never runs ahead of `h.txt`).
- `A1-paper.md` — full sample paper: reading/grammar/translation/listening/writing/speaking
  with the examiner's answer key and the listening script.
- Codified in `canon/08-education.md` (Rev 1), marked current in the index.

**Wrap-around:**
- `teacher/README.md` — teacher certificate (three units), four-semester university
  syllabus, translator-integrated classroom patterns (self-correction, discovery,
  coining-lab feedback loop).
- `literature/dialogues.md` — six dictionary-locked dialogues (market, family, phone,
  doctor, formal letter, counting book) for role-play and listening scripts.
- `tools/md2html.js` — the site builder: renders every `.md` under canon/, lessons/,
  exams/, teacher/, literature/ to styled HTML (24 pages), fixing the previously-broken
  grammar.html canon links. `lessons.html` now links the course, exams, and dialogue bank.

**Engine verification (node, local `h.txt`):** 13/14 term spot-checks pass (the one
"fail" was a test artifact — the engine returns only the primary gloss, "speaking test",
which is correct). Phase 1–4 regressions untouched. Coiner re-run idempotent, 0 rejections.

**Artifacts:** `canon/08-education.md`; `lessons/` (5 files); `exams/` (2); `teacher/` (1);
`literature/dialogues.md`; `tools/md2html.js`; `h.txt` VTXT 3.7; `canon/00-directory.md`;
`lessons.html`; 24 generated HTML pages.

**Decisions (Phase 5) — approved 2026-09-17, all four open questions resolved:**
1. **Exam blueprint approved as-is**: 25/25/20/15/10/5 weights, pass ≥60% overall and
   ≥50% per section; fixed form for A1–C2 papers; A2/B1 sample papers authorized to be
   printed using it.
2. **Dictionary lock is standing policy**: papers are printed against a VTXT snapshot;
   materials never run ahead of `h.txt`; a learner's canon-06-clean coin is never marked
   wrong.
3. **`lóva` and `dis` are permanent roots** (feed `lóva-sova`, `dis-sova`, and others).
4. **Folk dating confirmed**: `sofavi, 12 séli 1247 suso` stays as the paper-header style;
   calendar math is not tested.

**Next actions:** Phase 6 — native speakers & society: canon 09 (politeness, registers in
the wild, regional variation), a native-speaker corpus (fluent monologues/dialogues beyond
the classroom), and the first "good-enough-to-exist" reading fluency bar: the Sova-Néla
front page should be readable unaided at B1+. Also: ship the site builder output in a
`site/` preview and integrate the translator embed into book pages. Reply "Continue"
to proceed.