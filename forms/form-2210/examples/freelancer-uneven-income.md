# Example: Freelancer with Uneven Q4-Heavy Income (Schedule AI Lowers the Penalty)

A complete walkthrough of Form 2210 for a freelance editor with no Q1 income, modest Q2/Q3 income, and a large Q4 payday from a delivered project. Schedule AI lowers the penalty compared to the regular method. The saving is modest here because the low prior-year safe harbor already keeps the regular installments small.

All figures use the 2025 Form 2210 and its instructions (2025 returns filed in 2026), the 2025 Form 1040 standard deduction ($15,750 single), and the 2025 Tax Table. Amounts are rounded to whole dollars except installments and penalties.

## The filer

- **Name**: Riley Andersen
- **Filing status**: Single
- **Income**: 100% Schedule C (freelance video editor)
- **Tax year**: 2025 (filing in 2026)
- **Prior year (2024)**: $25,000 of Schedule C net profit. 2024 tax for Form 2210 line 8: $4,225 (2024 Form 1040 line 22 $693 + SE tax $3,532). 2024 AGI $23,234.

Riley had tax in 2024, so the no-prior-year-liability exception (IRC §6654(e)(2)) does not apply.

## Inputs gathered

```
Current-year Schedule C net profit by period:
  Jan–Mar:    $0
  Apr–May:    $5,000
  Jun–Aug:    $15,000
  Sep–Dec:    $80,000
  Annual:     $100,000

Schedule SE: $100,000 × 92.35% = $92,350 net earnings
  SS 12.4% × $92,350 = $11,451 (under the $176,100 wage base); Medicare 2.9% = $2,678
  SE tax = $14,130; deductible half = $7,065

Federal income tax:
  AGI $100,000 − $7,065 = $92,935
  − $15,750 standard deduction = $77,185
  − $15,437 QBI deduction (20% × $77,185, the taxable-income limit)
  = $61,748 taxable income → $8,494 (2025 Tax Table)

Form 1040 line 22: $8,494; Schedule 2 line 4 (SE tax): $14,130
Current-year tax (Form 2210 line 4): $22,624

Withholding:                        $0
Estimated tax payments:             $0
  (Riley underestimated his Q4 windfall and paid no quarterlies)

Prior-year tax:                     $4,225
Prior-year AGI:                     $23,234  → 100% safe harbor multiplier
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis (line 7 = line 4 − withholding):
  $22,624 − $0 = $22,624, not less than $1,000. Fails.

Test 2 — No prior-year liability:
  Prior-year tax = $4,225 ≠ $0. Fails.

Test 3 — 90% current:
  Required: $22,624 × 90% = $20,362. Paid: $0. Fails.

Test 4 — 100% prior:
  Required: $4,225. Paid: $0. Fails.

Penalty owed. Required annual payment (line 9) = smaller of $20,362 or $4,225 = $4,225.
```

The prior-year safe harbor is the binding constraint at $4,225.

## Regular method penalty computation

```
Line 10, each column: $4,225 × 25% = $1,056.25
Line 11, each column: $0

No payments, so each column's line 17 underpayment is $1,056.25, and each stays
unpaid until the balance is paid with the return on April 15, 2026.

Penalty (2025 worksheet rate 0.07 in every rate period):
  (a) $1,056.25 × 0.07 × 365/365 = $73.94   (4/15/25 → 4/15/26)
  (b) $1,056.25 × 0.07 × 304/365 = $61.58   (6/15/25 → 4/15/26)
  (c) $1,056.25 × 0.07 × 212/365 = $42.94   (9/15/25 → 4/15/26)
  (d) $1,056.25 × 0.07 × 90/365  = $18.23   (1/15/26 → 4/15/26)
  Total ≈ $196.69
```

Regular method penalty: ~$197.

## Schedule AI computation

Riley's income was concentrated in Q4. Schedule AI should reduce the early-quarter required installments. Each column uses income from January 1 through the column's end date; the standard deduction is the full $15,750 in every column (line 7, not prorated); SE tax is annualized in Part II and the deductible half of each period's SE tax reduces that period's AGI.

### Column (a) — January 1 through March 31, 2025

```
Line 28 net SE earnings: $0 → line 36 SE tax: $0
Line 1 AGI: $0;  line 3 annualized (× 4): $0
Line 13 taxable income: $0;  line 14 tax: $0
Line 17 total tax: $0
Line 21: $0 × 22.5% = $0
Line 23: $0;  line 26: $1,056.25 (regular installment)
Line 27 = smaller of 23 or 26 = $0
```

### Column (b) — January 1 through May 31, 2025

```
Line 28: $5,000 × 92.35% = $4,618
Line 33: 0.2976 × $4,618 = $1,374;  line 35: 0.0696 × $4,618 = $321
Line 36 annualized SE tax: $1,695
Line 1 AGI: $5,000 − ($1,695 ÷ 2.4 ÷ 2 = $353) = $4,647
Line 3 annualized (× 2.4): $11,153
Line 13 taxable income: $11,153 − $15,750 → $0;  line 14 tax: $0
Line 17 total tax: $0 + $1,695 = $1,695
Line 21: $1,695 × 45% = $762.75
Line 22: $0;  line 23: $762.75
Line 25: $1,056.25 − $0 = $1,056.25 carried;  line 26: $1,056.25 + $1,056.25 = $2,112.50
Line 27 = $762.75
```

### Column (c) — January 1 through August 31, 2025

```
Line 28: $20,000 × 92.35% = $18,470
Line 33: 0.186 × $18,470 = $3,435;  line 35: 0.0435 × $18,470 = $803
Line 36 annualized SE tax: $4,238
Line 1 AGI: $20,000 − ($4,238 ÷ 1.5 ÷ 2 = $1,413) = $18,587
Line 3 annualized (× 1.5): $27,881
Line 8 standard deduction: $15,750;  line 9 QBI: 20% × $12,131 = $2,426
Line 13 taxable income: $9,705;  line 14 tax: $973
Line 17 total tax: $973 + $4,238 = $5,211
Line 21: $5,211 × 67.5% = $3,517.43
Line 22: $762.75;  line 23: $2,754.68
Line 25: $2,112.50 − $762.75 = $1,349.75;  line 26: $1,056.25 + $1,349.75 = $2,406.00
Line 27 = smaller of $2,754.68 or $2,406.00 = $2,406.00
```

### Column (d) — January 1 through December 31, 2025

```
Line 28: $92,350;  line 33: 0.124 × $92,350 = $11,451;  line 35: 0.029 × $92,350 = $2,678
Line 36 annualized SE tax: $14,129
Line 1 AGI: $92,935;  line 3: $92,935
Line 9 QBI: $15,437;  line 13 taxable income: $61,748;  line 14 tax: $8,494
Line 17 total tax: $22,623
Line 21: $22,623 × 90% = $20,360.70
Line 22: $762.75 + $2,406.00 = $3,168.75;  line 23: $17,191.95
Line 25: $2,406.00 − $2,406.00 = $0;  line 26: $1,056.25
Line 27 = $1,056.25
```

Column (d) shows the gotcha: line 21 is 90% of the current-year tax ($20,360.70), far above the regular installments that the $4,225 prior-year safe harbor sets. Line 27 takes the smaller amount, so the column (d) installment stays $1,056.25.

| Column | Line 23 (annualized) | Line 26 (regular + carried) | Line 27 (used) |
|--------|----------------------|-----------------------------|----------------|
| (a) | $0 | $1,056.25 | **$0** |
| (b) | $762.75 | $2,112.50 | **$762.75** |
| (c) | $2,754.68 | $2,406.00 | **$2,406.00** |
| (d) | $17,191.95 | $1,056.25 | **$1,056.25** |

The four installments total $4,225, the same as line 9. Schedule AI moves part of the requirement to later due dates; it does not lower the annual total.

## Penalty under Schedule AI

```
Part III line 10 (from Schedule AI line 27): $0 / $762.75 / $2,406.00 / $1,056.25
Line 11: $0 in every column, so line 17 equals line 10 in each column.

Penalty (0.07, each underpayment unpaid until April 15, 2026):
  (a) $0
  (b) $762.75 × 0.07 × 304/365   = $44.47
  (c) $2,406.00 × 0.07 × 212/365 = $97.82
  (d) $1,056.25 × 0.07 × 90/365  = $18.23
  Total ≈ $160.52
```

**Schedule AI penalty: ~$161** vs. **regular method: ~$197**. Schedule AI saves ~$36.

## The completed Form 2210 draft

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] File Form 2210 with Schedule AI (annualized income installment method)
  Reason: Q4-concentrated income; Schedule AI saves ~$36 vs. regular method.

## Header
Name(s) shown on return:    Riley Andersen
Identifying number:         XXX-XX-XXXX
Filing status:              Single
Prior-year AGI:             $23,234  → safe-harbor multiplier: 100%

## Part I — Required Annual Payment
1. Form 1040 line 22:                               $8,494
2. Other taxes (Schedule 2 line 4, SE tax):         $14,130
3. (Refundable credits):                            $0
4. Current-year tax:                                $22,624
5. Line 4 × 90%:                                    $20,362
6. Withholding:                                     $0
7. Line 4 − Line 6:                                 $22,624  (not less than $1,000)
8. Prior-year tax × 100%:                           $4,225
9. Required annual payment (smaller of 5 or 8):     $4,225

## Part II — Reasons for Filing
- [x] Box C: annualized income installment method
- [ ] Boxes A, B, D, E

## Schedule AI — Annualized Income Installment Method (Part I summary)

| Line | (a) | (b) | (c) | (d) |
|------|-----|-----|-----|-----|
| 1 AGI for the period | $0 | $4,647 | $18,587 | $92,935 |
| 3 Annualized income | $0 | $11,153 | $27,881 | $92,935 |
| 8 Standard deduction | $15,750 | $15,750 | $15,750 | $15,750 |
| 9 QBI deduction | $0 | $0 | $2,426 | $15,437 |
| 13 Taxable income | $0 | $0 | $9,705 | $61,748 |
| 14 Tax | $0 | $0 | $973 | $8,494 |
| 15 SE tax (Part II line 36) | $0 | $1,695 | $4,238 | $14,129 |
| 17 Total tax | $0 | $1,695 | $5,211 | $22,623 |
| 21 × 22.5% / 45% / 67.5% / 90% | $0 | $762.75 | $3,517.43 | $20,360.70 |
| 23 | $0 | $762.75 | $2,754.68 | $17,191.95 |
| 26 | $1,056.25 | $2,112.50 | $2,406.00 | $1,056.25 |
| 27 → Part III line 10 | $0 | $762.75 | $2,406.00 | $1,056.25 |

## Part III — Underpayment and penalty

| Column | Line 10 | Line 11 | Line 17 | Paid on | Days | Rate | Penalty |
|--------|---------|---------|---------|---------|------|------|---------|
| (a) 4/15/25 | $0 | $0 | $0 | — | — | 7% | $0 |
| (b) 6/15/25 | $762.75 | $0 | $762.75 | 4/15/26 | 304 | 7% | $44.47 |
| (c) 9/15/25 | $2,406.00 | $0 | $2,406.00 | 4/15/26 | 212 | 7% | $97.82 |
| (d) 1/15/26 | $1,056.25 | $0 | $1,056.25 | 4/15/26 | 90 | 7% | $18.23 |
| **Line 19** | | | | | | | **$160.52** |

## Validation summary
- Math: all checks passed (2025 worksheet rate 0.07 in every rate period)
- Sanity:
  - Income materially back-loaded: Schedule AI is appropriate (Sep–Dec = 80% of annual income)
  - Column (d) line 21 ($20,360.70) exceeds line 26 ($1,056.25), so line 27 keeps the regular amount
  - Penalty ~$161 with Schedule AI vs. ~$197 with regular method (savings ~$36)
- Filing decision: file Form 2210 with Schedule AI (box C)
- Penalty: ~$161
- Next steps:
  - Form 1040 line 38: $161 (rounded to whole dollar), added to the balance due on line 37
  - For 2026: 100% of 2025 tax ($22,624; 2025 AGI $92,935 ≤ $150,000) = $5,656 per quarter on Form 1040-ES locks in the prior-year safe harbor. If 2026 income will be lower, figure 90% of projected 2026 tax on the 2026 Form 1040-ES worksheet instead.

## Sources cited in this draft
- IRS Form 2210 (2025), including Schedule AI
- IRS Instructions for Form 2210 (2025, Feb 17, 2026), penalty worksheet and Table 2
- IRC §6654(d)(2) — Annualized income installment method
- IRC §6654(d)(1)(B) — 100% prior-year safe harbor (applied because prior AGI ≤ $150K)
- IRC §6621 — Penalty rate (7% for all 2025 rate periods)
- IRC §6654(g)(1) — Withholding allocated equally across quarters (not relevant here; withholding = $0)
- 2025 Form 1040 (standard deduction), 2025 Schedule SE
```

## Why each non-obvious choice

**Why does Schedule AI's column (d) show $20,360.70 on line 21 but the actual column (d) installment is only $1,056.25?** Line 21 is the annualized tax × 90% for the whole year. But the filer's required *annual* payment (Form 2210 line 9) was capped at $4,225 by the prior-year safe harbor, and line 24 puts 25% of that ($1,056.25) into each column's regular installment. Line 27 takes the smaller of the annualized amount (line 23) and the regular amount plus carried savings (line 26), so for column (d) the regular amount controls.

**Why does Schedule AI help here?** Riley earned $0 in Q1, so Schedule AI's column (a) installment is $0 (vs. regular method's $1,056.25). Columns (a) and (b) push $1,349.75 of the requirement to the September 15 column, where it accrues for 212 days instead of 365 or 304. The saving is limited because the regular installments are small to begin with.

**Why doesn't the prior-year safe harbor save Riley entirely?** The prior-year safe harbor only saves the filer if they actually pre-paid the required annual amount. Riley paid $0 in withholding and $0 in estimates. So even though the required annual payment is only $4,225, Riley owes penalty on the unpaid installments.

**What about the no-prior-year-liability exception?** Doesn't apply because Riley had $4,225 of prior-year tax. The exception requires literally zero.

**What's the planning recommendation for 2026?** Riley should pay quarterly Form 1040-ES estimates of $5,656 each (100% of 2025's tax, locking in the prior-year safe harbor). If 2026 income drops back down, he can reduce mid-year using the 90% current-year figure, at the cost of certainty. The key is getting *something* paid in each quarter to avoid the same penalty pattern.

**What audit defense does Riley have?** Schedule C with full income/expense documentation (invoices, bank statements showing the Q4 deposit, etc.); Schedule SE flowing correctly; Schedule AI requires income documentation for each period, which Riley has from his accounting records. The $161 penalty appears on Form 1040 line 38; Riley pays it with the return.
