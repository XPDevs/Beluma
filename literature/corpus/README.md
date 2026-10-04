# Téva-Krosa: Native-Speaker Corpus (canon 09 §6)

**What this is.** The corpus is the "beyond the classroom" reading shelf of Lía Beluma —
fluent texts by (resident) native speakers doing ordinary things: trade, town meetings,
letters, signs, news, celebrations, and neighbours' talk. It is the B1+ **reading-fluency
band**: a learner who can follow these unaided has the standing of a `krosa` (friend) of
the town's speech.

Every line is **dictionary-locked** to the VTXT snapshot printed on the page (`VTXT 3.9`),
which is exactly the same lock the exams, lessons, and the paper use (canon 08 §4, canon 09
§5). `tools/check-corpus.js` re-verifies the whole corpus on every change.

## The fluency bar

The bar is prose that has moved past the classroom register:

- uses the four folk registers as the town actually does (canon 09 §1: the paper's
  official speech, the square's colloquial speech, the court's legal speech, the
  poem-voice);
- runs compounds and touches the city-civility vocabulary (`kíra-sova` polite speech,
  `nako-sula` great thanks, `gavo-gai` welcome, `nésa-krosa` neighbour, the market
  fair `tava-marketa`, the festival `réva-sumés`);
- reads smoothly *on the page* — a mid-issue item or a market-day letter should be
  readable in one sitting without a translator.

## Contents

| File | Register | Setting |
| --- | --- | --- |
| `01-market-day.md` | colloquial (market) | a market day at Méra-Tava |
| `02-town-meeting.md` | formal (town meeting) | the town assembly |
| `03-the-letter.md` | formal letter | a letter to the paper / to family |
| `04-regional-accents.md` | colloquial + regional variants | the same lines with accents |
| `05-signs.md` | legal-notice register | signs of the town |
| `06-the-fair.md` | folk/literary | the celebration fair (`réva-sumés`) |

## How to use

- **B1 students:** read `01`–`04` as the semester's "you can read this now" bar; keep the
  glosses folded until you've tried.
- **Pos grad (exam author, canon 08 §4):** every corpus word already exists in h.txt at
  `VTXT 3.9`; never print a paper that runs ahead of it.
- **Translator tests:** each file's Beluma fences are stable test inputs for the
  matching/compounding engine (see `beluma.js` `checkCorpus()`).
