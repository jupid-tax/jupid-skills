# Schedule 2 Line 17 Sub-Items

Line 17 is a catchall for additional taxes that don't have their own dedicated line. The form labels sub-items 17a through 17z. Most filers leave these blank; only specific recapture or non-qualified distribution events trigger them.

The exact list of sub-letters and labels can shift between revisions. Always cross-check against the current-year `f1040s2.pdf` and `i1040gi.pdf` before producing a final draft. The list below reflects the recent stable set.

## Sub-item table

### 17a — Recapture of other credits

| Field | Detail |
|-------|--------|
| Trigger | Filer claimed a non-refundable credit in a prior year that requires recapture due to a triggering event |
| Common examples | Investment Tax Credit (Form 4255), New Markets Credit, Indian Employment Credit, recapture of EV credit, recapture of residential energy credit if property disposed of |
| Format | Filer must list the credit type on the dotted line and enter the amount |
| Source | The form for the original credit usually has a recapture worksheet |

### 17b — Recapture of federal mortgage subsidy

| Field | Detail |
|-------|--------|
| IRC | §143(m) |
| Trigger | Filer received a federally subsidized mortgage and disposed of the home within 9 years; recapture is the lesser of 50% of gain or 6.25% of original loan × ratable holding period factor |
| Form | Form 8828 |

### 17c — Additional tax on HSA distributions

| Field | Detail |
|-------|--------|
| IRC | §223(f)(4) |
| Rate | 20% additional tax on non-qualified HSA distributions (in addition to ordinary income inclusion) |
| Source | Form 8889 Line 17b |
| Exception | No additional tax if account holder is age 65+, disabled, or deceased |

### 17d — Additional tax on Archer MSA distributions

| Field | Detail |
|-------|--------|
| IRC | §220(f)(4) |
| Rate | 20% on non-qualified MSA distributions |
| Source | Form 8853 Part I |
| Note | Archer MSAs are largely closed to new contributions; rare for new filers |

### 17e — Additional tax on Medicare Advantage MSA distributions

| Field | Detail |
|-------|--------|
| IRC | §138(c)(2) |
| Rate | 50% on non-qualified Medicare Advantage MSA distributions |
| Source | Form 8853 Part III |

### 17f — Recapture of charitable contribution deduction (fractional interest in tangible personal property)

| Field | Detail |
|-------|--------|
| IRC | §170(o)(3) |
| Trigger | Filer claimed a charitable deduction for a fractional interest in tangible personal property and the donation rules were violated within 10 years |

### 17g — Income from look-back interest, IRC §167(g)

| Field | Detail |
|-------|--------|
| IRC | §167(g)(2) |
| Trigger | Filer used income forecast method depreciation; actual results differed from forecast and look-back interest is owed/owed-to-filer |
| Source | Form 8866 |

### 17h — Look-back interest under §460(b)

| Field | Detail |
|-------|--------|
| IRC | §460(b) |
| Trigger | Long-term contract using percentage-of-completion method; look-back applies in the year a contract is completed |
| Source | Form 8697 |

### 17i — §72(p) loan deemed distribution

| Field | Detail |
|-------|--------|
| IRC | §72(p) |
| Trigger | Filer took a loan from a qualified retirement plan that violated the §72(p) rules (e.g., exceeded $50,000 limit, repayment schedule not met). The loan becomes a deemed distribution and the additional 10% tax under §72(t) applies if filer < 59½. |
| Source | Form 5329 Part I, but report the §72(p) deemed distribution portion here on Line 17i |

### 17j — Section 72(m)(5) excess benefits tax

| Field | Detail |
|-------|--------|
| IRC | §72(m)(5) |
| Trigger | 5% owner of an employer received qualified plan distributions in excess of allowable amount |

### 17k — Additional tax on ABLE account distributions

| Field | Detail |
|-------|--------|
| IRC | §529A(c)(3) |
| Rate | 10% on non-qualified ABLE distributions |

### 17l — Recapture of qualified plug-in EV credit

| Field | Detail |
|-------|--------|
| IRC | §30D / §25E |
| Trigger | Vehicle ceases to qualify (placed in business use abroad, etc.) within recapture period |
| Note | OBBBA 2025 changes to EV credit recapture provisions — verify current rules |

### 17m — Form 8889 HSA additional 20% (alternative reporting)

| Field | Detail |
|-------|--------|
| Note | Some recent form revisions consolidate HSA additional tax under either 17c or 17m. Verify against current-year Form 8889 instructions. |

### 17n — Recapture of Indian employment credit

| Field | Detail |
|-------|--------|
| IRC | §45A |
| Source | Form 8845 |

### 17o — Recapture of new markets credit

| Field | Detail |
|-------|--------|
| IRC | §45D |
| Source | Form 8874 |

### 17p — Recapture of employer-provided childcare facilities and services credit

| Field | Detail |
|-------|--------|
| IRC | §45F |
| Source | Form 8882 |

### 17q — Recapture of alternative motor vehicle credit / refueling property credit

| Field | Detail |
|-------|--------|
| IRC | §30B / §30C |
| Source | Form 8910 / Form 8911 |

### 17r — Excise tax on insider stock compensation in inversion (§4985)

| Field | Detail |
|-------|--------|
| IRC | §4985 |
| Trigger | Insider of a corporation that underwent an inversion received stock-based compensation. Very rare for individual filers. |

### 17s — Income from non-qualified deferred compensation that fails §409A

| Field | Detail |
|-------|--------|
| IRC | §409A |
| Trigger | NQDC plan failed §409A operational or documentary requirements; filer owes 20% additional tax + premium interest. The income amount is reported on Form 1040 Line 1h; the 20% additional tax goes here. |

### 17t — Section 457A failure

| Field | Detail |
|-------|--------|
| IRC | §457A |
| Trigger | Compensation from a nonqualified entity (foreign / tax-exempt / partnership with mostly tax-indifferent partners) that fails §457A |

### 17u — Tax on accumulated distribution of trusts

| Field | Detail |
|-------|--------|
| IRC | §667 |
| Source | Form 4970 |

### 17v — Reserved (varies by year)

Some recent years use 17v for additional Medicare tax on RRTA compensation that didn't flow through Form 8959. Verify against current-year form.

### 17w – 17z — Reserved or per current-year instructions

The IRS reserves several sub-letters for new items. Check the current-year Schedule 2 instructions before assigning.

## Line 18 — Total of 17a–17z

Sum of every populated 17x line. Routes into Line 21 total.

## Citation discipline

When populating a Line 17 sub-item, the agent must:

1. Identify the **specific IRC section** that imposes the additional tax
2. Identify the **upstream form** that computed the amount (Form 8889, 8853, 8866, 8697, 4970, 8845, 8874, 8882, 8910, 8911, etc.)
3. Verify the **dotted-line description** uses standard IRS terminology from the current-year instructions

Do not populate a Line 17 sub-item from "I think I owe this" without an upstream computation. Many of these items are rare enough that misclassification is more likely than legitimate liability.
