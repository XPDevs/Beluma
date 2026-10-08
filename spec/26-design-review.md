# §26 Design Review and Known Issues — Beluma Language Standard v1.0

Status: **Informative.** This section records the reasoning behind the design,
the known blemishes, and the accent-pair registry. It is normative only where it
registers an exception (§26.4).

## 26.1 Why Beluma

Beluma is engineered for five goals: (1) **regular** — one rule, one form;
(2) **producible** — new words come from rules, not memorization; (3) **legible**
— short, unambiguous shapes; (4) **scalable** — capacity beyond 250,000 words;
(5) **speakable** — every legal word is easy for a world speaker to say.

## 26.2 Design principles accepted

| Principle | Choice |
| --- | --- |
| Alphabet | Latin, a–z minus `c q y` (§01.2) |
| Stress | absolute penult (§01.5) |
| Word order | SVO, head-first (§03) |
| Formation | root + affix + compound (§15) |
| Registers | Standard, Formal, Informal, Technical (§23) |
| Spelling | regular; accents mark penult stress only |

## 26.3 Known blemishes

1. **Synonym surplus.** Early seeding imported loans that duplicate native
   roots (`sango` vs `gúndo` *blood*; `luno` was dropped because `miso` already
   meant *cat*). Policy: the Academy demotes the weaker form to `{colloq}` or
   removes it at the next MAJOR bump.
2. **Seed transliteration.** Early seeds used Esperanto/international forms and
   were respelled by the sanitizer. Some glosses were historically mangled; the
   seed tool now sanitizes **keys only** (`tools/seed_vocab.py:clean`).
3. **Coiner tool.** References to a `tools/coiner.js` were removed; the
   authoritative validator is `tools/validate_dict.py`. No Node.js dependency.
4. **Non-Latin script.** The 31-radicals script is illustrative only; all
   normative text is Latin (§02).
5. **Number forms.** Cardinal 11–19 and digit-forms coexist; the Academy fixed
   the cardinals (`unésa … séza`) and the Technical digit-forms
   (`zer éne di tri …`), removing the seed duplicates (`tremado`, `kvardeko`…).

## 26.4 Accent-pair registry

Because stress is fixed at the penult, two short words may share letters but
differ only by an accent (`mása` vs `masa`). These are permitted and listed
here. The validator treats them as **warnings**, never errors.

| Pair | Meaning A | Meaning B |
| --- | --- | --- |
| `mása` / `masa` | mass (physical) | crowd |
| `síta` / `sita` | quote | seven |
| `nóra` / `nora` | north | (name-like root) |
| `póra` / `pora` | carry | for |
| `kóva` / `kova` | cover | — |

(Run `tools/validate_dict.py` to print the live list; the table above is
illustrative.)

## 26.5 Trade-offs reconsidered

- **Penult stress + accent pairs.** Chosen over free stress for learnability;
  the cost is a small collision class (§26.4), accepted as warnings.
- **Expanded clusters (v4.0).** Onsets `st sk sl kl gl bl fl vl ps sf ts ks dn
  rn nj` and coda `m` were added to admit modern loans (`stato`, `klubo`,
  `métra`, `njutona`). This slightly departs from the original CV ideal; the
  Academy accepted it to protect productivity.
- **Digit-forms.** Kept for the Technical register because reading long numbers
  is otherwise slow.

## 26.6 Open questions (for future rulings)

1. Whether to fold synonym surplus automatically or case-by-case.
2. Whether to standardize a second stress rule for learned compounds.
3. Whether to extend the coda inventory further (`-ns`, `-nt`).
4. Numbering harmonization of §25 vs the §24/§26 gap in early drafts.

## 26.7 Conclusion

Beluma meets its goals: regular, productive, scalable past 250,000 words,
register-aware, and validated by open tools. Remaining issues are catalogued
here for the Academy (§25) to resolve in future VTXT releases.
