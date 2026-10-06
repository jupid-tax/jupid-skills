# Example: Missed Form 1099-NEC on a 2024 Return (Additional Tax Owed)

A W-2 employee filed her 2024 return in March 2025 and, in September 2026, found a 2024 Form 1099-NEC for freelance work that never made it onto the return. The amendment adds Schedule C, Schedule SE, and a QBI deduction, and results in additional tax. All 2024 figures come from the 2024 Instructions for Form 1040, 2024 Schedule SE, and 2024 Form 8995 (prior-year PDFs at https://www.irs.gov/pub/irs-prior/). Math checked in Python (see notes file).

## The filer

- **Name**: Dana Okafor (single), Georgia resident
- **Tax year amended**: 2024 (amendment prepared October 2026)
- **Original return**: e-filed March 3, 2025 with software; accepted; refund of $591 received
- **IRS contact so far**: none (agent asked: no CP2000, no math-error notice, no prior amendment)

## Inputs gathered

### From the filed 2024 return (column A)

| Item | Amount |
|---|---|
| W-2 wages (box 1), Brightline Logistics | $68,412 |
| W-2 Social Security wages (box 3) | $68,412 |
| Federal income tax withheld (box 2) | $7,486 |
| AGI (2024 Form 1040, line 11) | $68,412 |
| Standard deduction, single (2024 Instructions for Form 1040) | $14,600 |
| Taxable income (line 15) | $53,812 |
| Tax (line 16), 2024 Tax Table row $53,800–$53,850, Single | $6,895 |
| Total tax (line 24) | $6,895 |
| Overpayment (line 34) | $591 |

### The new information

- 2024 Form 1099-NEC from Harbor Lane Studio LLC, box 1: **$9,640** (UX research, September–November 2024).
- Business expenses Dana can document for that work: software subscriptions $612 (Schedule C line 27a, itemized in Part V) and a portable monitor $571 (line 18, under the de minimis safe harbor).
- Agent asked: any other 2024 changes? None. Any other 1099s? None.

## Step 1 — Should this be an amendment?

Yes. Unreported income changes income and tax liability (row 13 of [`../references/when-not-to-amend.md`](../references/when-not-to-amend.md)). The IRS has not contacted Dana, so this is a voluntary amendment, not a CP2000 response.

## Step 2 — Deadline check

The amendment **increases** tax, so there is no §6511 claim deadline to meet. Interest on the extra tax runs from April 15, 2025, the 2024 due date (2024 Instructions for Form 1040). The agent tells Dana to file and pay now and not to include interest on the form; the IRS will bill it.

## Step 3 — Rebuild the affected 2024 schedules

**Schedule C (2024)**

| Line | Amount |
|---|---|
| 1 Gross receipts | $9,640 |
| 7 Gross income | $9,640 |
| 18 Office expense | $571 |
| 27a Other expenses (Part V: software subscriptions) | $612 |
| 28 Total expenses | $1,183 |
| 31 Net profit | **$8,457** |

**Schedule SE (2024)**

| Line | Computation | Amount |
|---|---|---|
| 2 | Schedule C line 31 | $8,457 |
| 3 | | $8,457 |
| 4a | $8,457 × 92.35% = $7,810.04 | $7,810 |
| 4c / 6 | | $7,810 |
| 7 | 2024 maximum (printed on form) | $168,600 |
| 8a / 8d | W-2 box 3 | $68,412 |
| 9 | $168,600 − $68,412 | $100,188 |
| 10 | smaller of line 6 or 9 × 12.4% = $968.44 | $968 |
| 11 | $7,810 × 2.9% = $226.49 | $226 |
| 12 | SE tax → Schedule 2, line 4 | **$1,194** |
| 13 | 50% → Schedule 1, line 15 | **$597** |

**Schedule 1 / Schedule 2**: Schedule 1 line 3 = $8,457, line 10 = $8,457, line 15 = $597, line 26 = $597. Schedule 2 line 4 = $1,194, line 21 = $1,194.

**AGI**: $68,412 + $8,457 − $597 = **$76,272**.

**Form 8995 (2024)** — taxable income before QBI ($76,272 − $14,600 = $61,672) is below the 2024 threshold of $191,950 printed on the 2024 Form 8995, so the simplified form applies. QBI is reduced by the deductible part of SE tax (2024 Instructions for Form 8995):

| Line | Computation | Amount |
|---|---|---|
| 1(c) / 2 / 4 | $8,457 − $597 | $7,860 |
| 5 | 20% | $1,572 |
| 10 | | $1,572 |
| 11 | | $61,672 |
| 13 | (no net capital gain) | $61,672 |
| 14 | 20% | $12,334 |
| 15 | smaller of 10 or 14 → Form 1040 line 13 | **$1,572** |

**Taxable income**: $61,672 − $1,572 = **$60,100**. **Tax**: 2024 Tax Table row $60,100–$60,150, Single = **$8,281**.

## The completed Form 1040-X draft

```markdown
# Form 1040-X — DRAFT amending tax year 2024
Form revision used: Form 1040-X (Rev. December 2025)

## Header
Tax year amended: 2024
Name / SSN: Dana Okafor / XXX-XX-XXXX
Current address: <current address>
Presidential Election Campaign: no change
Amended return filing status: Single (original: Single)

## Lines 1–23
| Line | Description | A | B | C |
|---|---|---:|---:|---:|
| 1 | Adjusted gross income | 68,412 | 7,860 | 76,272 |
| 2 | Standard deduction | 14,600 | 0 | 14,600 |
| 3 | Line 1 − line 2 | 53,812 | 7,860 | 61,672 |
| 4a | QBI deduction | 0 | 1,572 | 1,572 |
| 4b | Schedule 1-A deductions (not available for 2024) | 0 | 0 | 0 |
| 5 | Taxable income | 53,812 | 6,288 | 60,100 |
| 6 | Tax (method: Table) | 6,895 | 1,386 | 8,281 |
| 7 | Nonrefundable credits | 0 | 0 | 0 |
| 8 | Line 6 − line 7 | 6,895 | 1,386 | 8,281 |
| 9 | Reserved | — | — | — |
| 10 | Other taxes (self-employment tax) | 0 | 1,194 | 1,194 |
| 11 | Total tax | 6,895 | 2,580 | 9,475 |
| 12 | Withholding | 7,486 | 0 | 7,486 |
| 13 | Estimated tax payments | 0 | 0 | 0 |
| 14 | Earned income credit | 0 | 0 | 0 |
| 15 | Refundable credits | 0 | 0 | 0 |
| 16 | Paid with extension/original/after filing | | | 0 |
| 17 | Total payments | | | 7,486 |
| 18 | Overpayment on original | | | 591 |
| 19 | Line 17 − line 18 | | | 6,895 |
| 20 | Amount you owe | | | 2,580 |
| 21 | Overpayment on this return | | | 0 |
| 22 | Refunded to you | | | 0 |
| 23 | Applied to estimated tax | | | 0 |

## Part I — Dependents
No change.

## Part II — Explanation of changes
After filing, I located a 2024 Form 1099-NEC from Harbor Lane Studio LLC reporting
$9,640 of nonemployee compensation that was omitted from my original return. I added
Schedule C showing $9,640 of gross receipts, $571 of office expense, and $612 of
software subscriptions, for a net profit of $8,457. Schedule SE adds $1,194 of
self-employment tax (line 10) and a $597 deduction for half of it, increasing AGI by
$7,860 (line 1). Form 8995 adds a $1,572 qualified business income deduction
(line 4a). Tax on the corrected taxable income of $60,100 is $8,281 from the 2024
Tax Table (line 6). Attached: corrected 2024 Form 1040, Schedules 1, 2, C, and SE,
and Form 8995.

## Statute check
Not a refund claim (tax increases). Interest accrues from 04/15/2025; not entered on
the form.

## Attachments
- Complete corrected 2024 Form 1040 with Schedule 1, Schedule 2, Schedule C,
  Schedule SE, Form 8995 (e-file: software includes all forms)
- No new W-2 or 1099-R with withholding

## Filing channel
E-file through tax software: 2024 is within the current or two prior tax periods
during 2026, and the original was e-filed in 2025 (not on paper in the current
processing year). Pay $2,580 by direct debit with the e-filed 1040-X or IRS Direct Pay.

## Validation summary
- Math: all checks passed (each C = A + B; line 20 = 9,475 − 6,895 = 2,580;
  change in total tax 2,580 = 1,386 + 1,194)
- Sanity: 2024 amounts used throughout; QBI reduced by half of SE tax; SE tax uses
  2024 wage base; line 16 has no interest or penalty
- Next steps: Georgia amended return may be required (contact the Georgia
  Department of Revenue); IRS may bill interest and an estimated tax penalty
  separately; track at Where's My Amended Return about 3 weeks after acceptance

## Sources cited in this draft
- Form 1040-X (Rev. December 2025) and Instructions (Rev. December 2025)
- 2024 Instructions for Form 1040 (standard deduction $14,600; Tax Table; due date
  April 15, 2025)
- 2024 Schedule SE (92.35%, 12.4%, 2.9%, $168,600)
- 2024 Form 8995 and Instructions ($191,950 threshold; QBI reduced by deductible
  part of SE tax)
- irs.gov Amended return FAQs (e-file scope)
```

## Why each non-obvious choice

**Why does column B on line 1 show $7,860, not $8,457?** AGI rises by the Schedule C profit minus the deductible half of SE tax ($8,457 − $597). Line 1 carries the net change in AGI, not the gross 1099 amount.

**Why is line 10 used for SE tax instead of line 6?** Line 6 is income tax on taxable income. SE tax is an "other tax" from Schedule 2, which the instructions route to line 10.

**Why is line 18 $591 when Dana already received that refund?** Line 18 holds the original overpayment so the reconciliation does not treat the $591 as still available. Without it, line 19 would be $7,486 and the amount owed would be understated by $591.

**Why e-file rather than paper?** The IRS amended return FAQ allows e-filing for the current or two prior tax periods; in 2026 that includes 2024. The paper-only exception (a prior-year return originally filed on paper during the current processing year) does not apply.

**What if Dana had received a CP2000 first?** If the CP2000 matched this exact change and she had nothing else, she would follow the notice and not amend. Because she also has expenses to claim, she would file this Form 1040-X marked "CP2000" with the notice response, at the notice's address (see [`../references/when-not-to-amend.md`](../references/when-not-to-amend.md)).
