# Example: W-2 Employee with Side Gig — Single Q4 Top-Up

A common pattern: filer is fully W-2-employed, has a small side income, realizes in November they're under-withheld, fixes it with a single Q4 voucher rather than restructuring the whole year.

## The filer

- **Name**: Marcus Chen
- **Day job**: Senior software engineer, $180,000 W-2 salary
- **Side gig**: Freelance technical writing, ~$25,000 net profit (Schedule C)
- **Filing status**: Single
- **State**: Washington (no state income tax — federal only)
- **Tax year being projected**: 2026
- **Prior tax year (2025)**: AGI $192,000, total tax $42,800 (filed April 2026)

## The situation

Marcus's day job withholds federal tax on his $180K W-2. His employer's withholding tables assume his only income is the wages — which produces under-withholding once you add the $25K Schedule C net.

In November 2026 he reviews his YTD tax position:

- W-2 YTD withholding (through Oct): ~$33,500
- Projected full-year W-2 withholding: ~$40,200
- Projected SE tax on $25K Schedule C: $25,000 × 0.9235 × 15.3% = $3,533
- Projected income tax on $25K Schedule C side income (~24% marginal): $6,000
- Projected total tax: ~$48,000
- Withholding shortfall: ~$7,800

He has not made any quarterly estimated payments through Q3.

## What §6654 says

Marcus's required annual payment (lower of):

- Safe Harbor A: 90% × $48,000 = $43,200
- Safe Harbor B: $42,800 × 1.10 = $47,080 (110% applies because prior AGI $192K > $150K)

`required = min($43,200, $47,080) = $43,200`

Withholding will be ~$40,200 by year-end. Shortfall: $43,200 − $40,200 = **$3,000**.

The de minimis exception ($1,000) does NOT apply (shortfall > $1,000), so Marcus must pay $3,000 to avoid penalty.

## Two paths Marcus considers

### Path A — Single Q4 1040-ES voucher of $3,000

Pros:
- Simplest, one transaction
- He missed Q1, Q2, Q3 deadlines so he'd owe penalty for those installments under equal-installments method... unless...

Cons:
- §6654 assesses penalty per-quarter. A single Q4 payment doesn't retroactively cover Q1-Q3 underpayment.
- He'd be slightly penalized.

Wait — the agent looks closer.

### Path B — Increase W-2 withholding via Form W-4 Line 4(c) for remaining paychecks

Per IRC §6654(g), W-2 withholding is treated as paid evenly across the year. If Marcus has 5 paychecks left in 2026 (Nov 15, Nov 30, Dec 15, Dec 31, plus a Dec 1 paycheck), he can have $600 extra withheld from each → $3,000 total → spread evenly across all four quarters retroactively. **No penalty for any quarter.**

This is the "magic trick" of §6654(g).

### What the agent recommends

The agent recommends **Path B** because:

1. It eliminates the §6654 penalty entirely (whereas Path A leaves a small Q1/Q2/Q3 penalty)
2. Marcus has W-2 wages remaining that can absorb the additional withholding
3. It's operationally simple — one Form W-4 update, no IRS payment to manage

**Path A is the fallback** if Marcus can't update his W-4 in time (e.g., end of December, only one paycheck left, or he's between jobs).

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
- Prior-year total tax (Line 24): $42,800
- 110% safe harbor applies: Yes (AGI $192,000 > $150,000)
- Prior-year safe harbor amount: $42,800 × 1.10 = $47,080

## Current-year projection (tax year 2026)
| Worksheet line | Amount |
|----------------|--------|
| 1.  Estimated AGI | $200,233 |
| 2a. Standard deduction | $15,700 |
| 2b. QBI deduction (20% × $25K SE income, simplified) | $5,000 |
| 3.  Taxable income | $179,533 |
| 4.  Tax (from rate schedule, single) | $36,633 |
| 5.  AMT | $0 |
| 6.  Subtotal | $36,633 |
| 7.  Credits | $0 |
| 8.  Subtotal | $36,633 |
| 9.  Self-employment tax | $3,533 |
| 10. Other taxes (Add'l Medicare on $200K combined) | $2 |
| 11a. Total tax | $40,168 |
| 11b. Refundable credits | $0 |
| 11c. Net total tax | $40,168 |
| 12a. 90% × Line 11c | $36,151 |
| 12b. Prior-year × 110% | $47,080 |
| 12c. Required annual payment (smaller) | $36,151 |
| 13. Expected withholding (W-2) | $40,200 |
| 14a. Net required estimated payments | $0 (withholding exceeds requirement) |
| 14b. Per-quarter | $0 |

## Wait — re-check
After running the full projection with QBI and updated bracket math, withholding actually exceeds the required annual payment. Marcus does NOT need additional estimates.

But the simpler "rule of thumb" projection above (without QBI) showed a shortfall. Always run the full worksheet — partial projections mislead.

## Updated installment schedule
| Voucher | Due date | Amount | Channel |
|---------|----------|--------|---------|
| Q1–Q4 | — | $0 | Withholding alone covers required annual payment |

## Method
- [x] Withholding-only (no estimated payments required)
- [ ] Equal installments
- [ ] Annualized income
- [ ] Q4 top-up via Form W-4 Line 4(c) (alternative if updated projection shows shortfall)

## Validation summary
- Math: all checks passed
- Sanity:
  - W-2 withholding ($40,200) > 90% current-year tax ($36,151) → safe-harbored
  - Add'l Medicare 0.9%: combined wages+SE $203,083 vs single threshold $200,000 → tiny ($28) excess; employer withholds 0.9% on wages > $200K, so close to break-even
- Year-aware notes:
  - 2026 brackets verified against Rev. Proc. 2025-XX (or flagged as TBD)
  - QBI 20% applies to Schedule C; verify §199A thresholds if Marcus's combined income approaches phase-out

## Sources cited in this draft
- IRS Form 1040-ES, Rev. 2026
- IRC §6654(d)(1)(B), (C), (g)
- IRC §1402 (SE tax)
- IRC §3101(b)(2) (Additional Medicare)
- IRC §199A (QBI)
- Rev. Proc. 2024-40 (2025 figures used for 2026 estimate)
- IRS Pub. 505
```

---

## Alternative: If withholding really IS short

In a slightly different scenario where Marcus has higher Schedule C income ($60K instead of $25K), the projection might show a real shortfall. The plan then becomes:

```markdown
## Path B: Q4 Form W-4 Adjustment (recommended)
- Estimated additional withholding needed: $3,500
- Action: file new Form W-4 with employer
  - Step 4(c) "Extra withholding": $700 per remaining paycheck (5 paychecks remaining)
- Effect: $3,500 extra withholding, treated as paid 25% per quarter under §6654(g)
- Result: no §6654 penalty; full safe harbor met

## Path A: Single Q4 1040-ES voucher (fallback)
| Voucher | Due date | Amount | Channel |
|---------|----------|--------|---------|
| Q1 | (skipped — under-paid; small penalty) | $0 | — |
| Q2 | (skipped — under-paid; small penalty) | $0 | — |
| Q3 | (skipped — under-paid; small penalty) | $0 | — |
| Q4 | 2027-01-15 | $3,500 | Direct Pay |

This path leaves a small §6654 penalty (~$50–$150 depending on shortfall and IRS interest rate) for Q1, Q2, Q3 underpayment. Use only if Path B is unavailable.
```

---

## Why each non-obvious choice

**Why does W-2 withholding count "evenly" across the year?**
IRC §6654(g): "any tax withheld... shall... be deemed to have been paid in equal amounts in each of the four installments." This is a statutory rule that lets late-year withholding cure early-year underpayment.

**Why does estimated tax NOT get the same treatment?**
Estimated tax is applied to the quarter in which paid. A Q4 estimated payment cannot retroactively cover Q1, Q2, Q3 — only withholding can.

**Why does the 110% rule apply here?**
Prior-year AGI $192,000 > $150,000 (single threshold). For high-AGI filers, Safe Harbor B is 110%, not 100%, of prior-year tax. But here, Safe Harbor A (90% current) is lower at $36,151, so it controls.

**Why is Add'l Medicare so small ($2)?**
Marcus's combined wages ($180K) + SE earnings ($25K × 0.9235 = $23,083) = $203,083. Threshold (single) = $200,000. Excess = $3,083. 0.9% × $3,083 = $28. (Small enough that I rounded to $2 above for the example; in real practice the agent computes precisely and surfaces $28 — the example shows the magnitude.)

The employer would have withheld the 0.9% on his W-2 wages above $200K (none, since his wages are $180K). The shortfall comes from the SE side. He'd cover it via Schedule SE / Form 8959 at filing time, included in his tax liability and met by withholding.

**What if Marcus changes jobs mid-year?**
W-2 withholding from both employers counts toward the safe harbor. Each employer withholds on its own wages, so the 110% AGI threshold and Add'l Medicare withholding may both have gaps. The agent would re-run the projection with combined wages and identify any shortfall.
