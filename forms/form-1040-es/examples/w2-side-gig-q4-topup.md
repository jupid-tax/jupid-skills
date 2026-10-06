# Example: W-2 Employee with Side Gig — Q4 Top-Up

A common pattern: filer is fully W-2-employed, has a small side income, realizes in November they're under-withheld, and fixes it late in the year rather than restructuring the whole year. All figures use the 2026 Form 1040-ES (2026 Tax Rate Schedules, $16,100 standard deduction, $184,500 Social Security wage base).

## The filer

- **Name**: Marcus Chen
- **Day job**: Senior software engineer, $180,000 W-2 salary (no pretax deductions)
- **Side gig**: Freelance technical writing, $25,000 net profit (Schedule C)
- **Filing status**: Single
- **State**: Washington (no state income tax — federal only)
- **Tax year being projected**: 2026
- **Prior tax year (2025)**: AGI $192,000, total tax $42,800 (figured per the 2026 Form 1040-ES line 12b instructions)
- **Payroll**: semi-monthly (15th and last day of the month)

## The situation

Marcus's day job withholds federal tax on his $180K W-2 as if the wages were his only income. His pay stubs project about **$31,900** of 2026 withholding. He has made no estimated payments through Q3. In November 2026 he runs the full worksheet.

## The full 2026 worksheet

| Worksheet line | Amount | How computed |
|----------------|--------|--------------|
| SE tax (SE worksheet) | $1,228 | $25,000 × 92.35% = $23,088; SS: 12.4% × min($23,088, $184,500 − $180,000 = $4,500) = $558; Medicare: 2.9% × $23,088 = $670 |
| Half of SE tax | $614 | SE worksheet line 11 |
| **1. AGI** | **$204,386** | $180,000 + $25,000 − $614 |
| 2a. Standard deduction | $16,100 | 2026 single |
| 2b. QBI | $4,877 | 20% × ($25,000 − $614); taxable income before QBI ($188,286) is under the $201,750 threshold |
| 2c. Schedule 1-A | $0 | |
| 2d. | $20,977 | |
| **3. Taxable income** | **$183,409** | |
| 4. Tax (Schedule X) | $36,616 | $17,966 + 24% × ($183,409 − $105,700) |
| 5–8. AMT, credits | $0 | |
| 9. SE tax | $1,228 | |
| 10. Other taxes | $28 | Additional Medicare Tax: SE earnings $23,088 − ($200,000 − $180,000 wages) = $3,088 × 0.9% |
| **11c. Total 2026 estimated tax** | **$37,872** | |
| 12a. 90% × 11c | $34,085 | |
| 12b. Prior year × 110% | $47,080 | 2025 AGI $192,000 > $150,000 |
| **12c. Required annual payment** | **$34,085** | smaller of 12a, 12b |
| 13. Expected withholding | $31,900 | |
| 14a. 12c − 13 | $2,185 | more than zero |
| 14b. 11c − 13 | $5,972 | $1,000 or more → estimates required |

Note the Social Security wage base: his $180,000 of wages already uses all but $4,500 of the $184,500 base, so only $4,500 of SE earnings bear the 12.4% part. Multiplying $25,000 × 92.35% × 15.3% ($3,533) would overstate his SE tax by about $2,300.

## What §6654 says

Required annual payment: $34,085 → $8,521.25 per installment. Withholding is treated as paid evenly ($31,900 / 4 = $7,975 per installment, IRC §6654(g)), so each of Q1–Q3 is $546.25 short and he must make up $2,185 in total.

## Two paths Marcus considers

### Path A — Single Q4 1040-ES payment of $2,185 (by January 15, 2027)

- One transaction, but an estimated payment counts only from the date it is paid
- Q1, Q2, and Q3 stay underpaid by $546.25 each until January 15, 2027
- Approximate §6654 penalty: about $63 (2026 underpayment rates 6% for Q2 and 7% for Q3–Q4, https://www.irs.gov/payments/quarterly-interest-rates; the January 2027 rate is announced in late 2026 — 7% assumed)

### Path B — Increase W-2 withholding via Form W-4 Step 4(c) for the remaining paychecks

Under IRC §6654(g), withholding is treated as paid in equal amounts on the four due dates, no matter when it is withheld. With four paychecks left (Nov 15, Nov 30, Dec 15, Dec 31), Marcus asks for $547 extra on each → $2,188, bringing withholding to $34,088 ≥ $34,085. **No penalty for any quarter.**

### What the agent recommends

**Path B**, because:

1. It removes the §6654 penalty entirely (Path A leaves the Q1–Q3 shortfall)
2. Marcus has W-2 wages left to absorb the extra withholding
3. One Form W-4 update, no IRS payment to manage

**Path A is the fallback** if Marcus can't update his W-4 in time (no paychecks left, or between jobs). The 12a figure relies on the projection being right; if Marcus wants certainty against a surprise in December, the prior-year route (12b, $47,080) would need $15,180 more withholding, which is far more than he needs on these facts.

---

## The deliverable (Path B — primary recommendation)

```markdown
# Form 1040-ES — Estimated Tax Plan for tax year 2026

## Filer
- Name: Marcus Chen
- SSN: ***-**-**** (placeholder)
- Filing status: Single
- State (for voucher mailing): WA (federal only — no state income tax)

## Prior-year baseline (tax year 2025)
- Prior-year AGI: $192,000
- Prior-year total tax (line 12b definition): $42,800
- 110% safe harbor applies: Yes (AGI $192,000 > $150,000)
- Prior-year safe harbor amount: $42,800 × 1.10 = $47,080

## Current-year projection (tax year 2026)
| Worksheet line | Amount |
|----------------|--------|
| 1.  Estimated AGI | $204,386 |
| 2a. Standard deduction | $16,100 |
| 2b. QBI deduction | $4,877 |
| 2c. Schedule 1-A deductions | $0 |
| 2d. Total deductions | $20,977 |
| 3.  Taxable income | $183,409 |
| 4.  Tax (2026 Schedule X) | $36,616 |
| 5.  AMT | $0 |
| 6.  Subtotal | $36,616 |
| 7.  Credits | $0 |
| 8.  Subtotal | $36,616 |
| 9.  Self-employment tax | $1,228 |
| 10. Other taxes (Additional Medicare Tax) | $28 |
| 11a. Total tax | $37,872 |
| 11b. Refundable credits | $0 |
| 11c. Net total tax | $37,872 |
| 12a. 90% × Line 11c | $34,085 |
| 12b. Prior-year × 110% | $47,080 |
| 12c. Required annual payment (smaller) | $34,085 |
| 13. Expected withholding (W-2, before the change) | $31,900 |
| 14a. Line 12c − Line 13 | $2,185 |
| 14b. Line 11c − Line 13 ($1,000 test) | $5,972 |

## Plan
| Action | Amount | Timing |
|--------|--------|--------|
| Form W-4 Step 4(c) extra withholding | $547 per paycheck × 4 = $2,188 | Paychecks Nov 15 – Dec 31, 2026 |
| 1040-ES vouchers | $0 | Not needed once withholding reaches $34,085 |

## Method
- [ ] Equal installments
- [ ] Annualized income
- [x] Q4 top-up via Form W-4 Step 4(c) (withholding counts as paid evenly, §6654(g))
- [ ] Fallback: single Q4 1040-ES payment of $2,185 by Jan 15, 2027 (≈ $63 penalty for Q1–Q3)

## Validation summary
- Math: all checks passed
- Sanity:
  - SS wage base shared with W-2 wages: only $4,500 of SE earnings taxed at 12.4%
  - Additional Medicare Tax $28: SE earnings above the $200,000 threshold after his $180,000 of wages; the employer withholds 0.9% only on wages over $200,000, so none was withheld
  - Withholding after the change ($34,088) ≥ required annual payment ($34,085)
- Year-aware notes:
  - 2026 Tax Rate Schedules, $16,100 standard deduction, $184,500 wage base — 2026 Form 1040-ES
  - QBI under the 2026 $201,750 threshold (Rev. Proc. 2025-32 §4.26)

## Sources cited in this draft
- IRS Form 1040-ES (2026)
- IRC §6654(d)(1)(B), (C), (g)
- IRC §1402 (SE tax)
- IRC §3101(b)(2) (Additional Medicare Tax); Form 8959 Part II
- IRC §199A (QBI)
- Rev. Proc. 2025-32 (2026 figures)
- IRS Pub. 505
```

---

## Why each non-obvious choice

**Why does W-2 withholding count "evenly" across the year?**
IRC §6654(g): withholding is deemed paid in equal amounts on each installment due date unless the taxpayer elects actual dates. This statutory rule lets late-year withholding cure early-year underpayment.

**Why does estimated tax NOT get the same treatment?**
An estimated payment is credited on the date paid. A January 15 payment cannot retroactively cover Q1, Q2, Q3 — only withholding can.

**Why does the 110% rule apply here, yet not control?**
Prior-year AGI $192,000 > $150,000 (single), so the prior-year safe harbor is 110% of 2025 tax ($47,080). The 90% current-year figure ($34,085) is lower, so it controls — as long as the 2026 projection holds.

**Why is the Additional Medicare Tax only $28?**
On Form 8959, the $200,000 threshold is reduced by wages ($180,000) before it is applied to SE income, leaving $20,000; SE earnings of $23,088 exceed that by $3,088, and 0.9% of $3,088 is $28. His employer withheld none because his wages are under $200,000.

**What if Marcus changes jobs mid-year?**
W-2 withholding from both employers counts toward the safe harbor. Each employer withholds as if it were the only one, so withholding and Additional Medicare Tax withholding can both fall short; the agent re-runs the projection with combined wages.
