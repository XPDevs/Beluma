# §13 Numbers — Beluma Language Standard v1.0

Status: **Normative.**

## 13.1 Cardinal numbers (Standard)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `zéra` | `ona` | `tuo` | `tro` | `fóra` | `kvín` | `sixa` | `sita` | `oita` | `noa` |

| 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `diza` | `unésa` | `dúésa` | `trésa` | `késa` | `kinsa` | `séza` | `diza-é-sita` | `diza-é-oita` | `diza-é-noa` |

**Tens:** `vinta` 20, `triga` 30, `forga` 40, `livga` 50, `sixga` 60, `sitga` 70,
`oitga` 80, `noga` 90.

**Hundreds and above:** `senta` 100, `mila` 1,000, `miliona` 10⁶, `biliona` 10⁹,
`triliona` 10¹².

- 11–16 are single words (irregular but fixed); 17–19 are built `diza-é-X`
  (ten-and-X).
- 21 = `vinta-ona`, 35 = `triga-kvín`, 47 = `forga-diza-é-sita`.
- 100 = `senta`; 250 = `tuo senta livga`; 1,001 = `mila e ona` (with `e` between
  scale groups).
- Compound tens and units are hyphenated; larger elements are separate words.

## 13.2 Decimal numbers (Technical)

For reading digit strings — phone numbers, codes, IDs, and arithmetic — the
**digit-form** is used. It is a separate set of short roots (§23.4):

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `zer` | `éne` | `di` | `tri` | `kvar` | `kvin` | `sis` | `sep` | `ok` | `nof` | `dek` |

- A number read digit by digit: `éne-di-tri` = "1-2-3".
- Arabic numerals are written in Technical texts (§2.4) and read with digit-forms.
- The decimal separator is said `punto`: `tro punto kvin` = 3.5.

## 13.3 Ordinals

Add **`-ji`** to the cardinal: `onaji` 1st, `tuoji` 2nd, `troji` 3rd,
`dizaji` 10th, `vintaji` 20th. Hyphenated cardinals take `-ji` on the last
element: `triga-kvín-ji` 35th. Ordinals are adjectives (§09).

## 13.4 Fractions and parts

`parta` *part/fraction*; `duon` *half* (§13). A fraction is `CARDINAL + -parta`:
`troparta` *a third*, `kvínparta` *a fifth*. General: `X / Y` = `X parta ze Y`
(*X parts of Y*). Decimal fractions use `punto` (§13.2).

## 13.5 Percent, arithmetic, and signs

| Operation | Beluma | Example |
| --- | --- | --- |
| percent | `porsenta` | `triga porsenta` 30% |
| add | `ada` | `tuo ada tro s kvín` 2 + 3 = 5 |
| subtract | `subta` | `kvín subta tuo s tro` 5 − 2 = 3 |
| multiply | `multa` | `tuo multa tro s sixa` 2 × 3 = 6 |
| divide | `divita` | `sixa divita tuo s tro` 6 ÷ 2 = 3 |
| equals | `ekva` / `s` | `X ekva Y` |
| negative | `un-` | `un-kvín` −5 |
| plus / minus sign | `mésa-morka` / `mísa-morka` | written `+` / `−` |

The copula `s` may serve as "equals": `tuo ada tro s kvín`.

## 13.6 Counting and measurement

A counted noun follows the numeral; plural is optional after numbers (§5.2):
`tres lunos` or `tre luno` *three cats*. Measurement uses a **number + unit**
phrase (§17): `kvín métra` *five metres*, `diza grado` *ten degrees*. Units are
registered nouns (§17.4).

## 13.7 Negation and approximation

`zéra` is also the negative quantifier *none* (§08): `Zéra luno esto.` *There is
no cat.* Approximation uses `sirka` *about* (`sirka vinta` *about twenty*),
`mésa ban` (*more than*), `mísa ban` (*less than*), and `preskawe` *nearly*.
