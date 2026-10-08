# §25 The Language Academy — Beluma Language Standard v1.0

Status: **Normative** for composition and procedure; **Informative** for
historical framing.

## 25.1 Mandate

The **Beluma Language Academy** (`Beluma Kéma-Kosa`, BKK) is the sole
authority for the Beluma language. It:

- maintains `lexicon/h.txt` and the VTXT version;
- ratifies changes (§24.6);
- interprets this standard where ambiguous;
- publishes the dictionary, curriculum, and periodic rulings;
- promotes the language and supports its worldwide learners.

## 25.2 Bodies

| Body | Beluma | Function |
| --- | --- | --- |
| Assembly | `Kosa` | ratifies changes by majority |
| Lexicon Council | `Kéma-Konsilio` | admits heads, curates glosses |
| Grammar Council | `Livo-Konsilio` | rules on structure and usage |
| Standards Board | `Tésa-Konsilio` | maintains tools, versions, releases |
| Registrar | `Kosa-Kivor` | keeps records and the canon |

Each council has 5–9 members serving five-year terms; the Assembly has 50
members elected by registered speakers.

## 25.3 Decisions

- Ordinary changes: simple majority of the Assembly, on council recommendation.
- Breaking changes (§24.5 MAJOR): two-thirds of the Assembly and a one-month
  public comment period.
- Emergencies (security, legal need): the Standards Board may issue a
  provisional ruling valid 90 days, then submitted for ratification.

## 25.4 Rulings

A **ruling** is a dated document under `canon/` that records a decision with its
rationale and examples. Rulings are numbered `BKK-YYYY-NNN` and cited like
precedent. Two examples:

- `BKK-2026-001` — topic marker respelled `ya` → `ia` (letter `y` banned).
- `BKK-2026-002` — stress fixed at the penult; accents in `h.txt` corrected.

## 25.5 Style and purity

The Academy judges purity by **producibility**: a word is Beluma if it parses by
§15, regardless of source. Loans are admitted when international and short, and
respelled to Beluma phonology (`telefona`, `kafe`, `susi`). Calques are
discouraged where a built word exists.

## 25.6 Regional and functional variation

The Academy recognizes no regional dialects; registers (§23) are functional
varieties, not regional ones. Pedagogical materials must teach Standard first,
then registers per §22.

## 25.7 Records and transparency

- The dictionary is a plain-text file under version control (§20).
- Every ruling is public and dated.
- Tool source (`tools/*.py`) is open, so any speaker can verify conformance.

## 25.8 Motto

`Kéma sola libera.` — *Knowledge alone frees.*
