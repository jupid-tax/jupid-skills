# Example: W-2 Employee with Under-Withheld Side-Gig Income (Modest Penalty)

A complete walkthrough of Form 2210 for a filer with steady W-2 wages and a Schedule C side gig that wasn't subject to withholding. Walks through both safe harbors and produces a small penalty using the regular method.

## The filer

- **Name**: Marcus Chen
- **Filing status**: Single
- **Income**:
  - W-2 from MarketingCo: $112,925 (Box 1) / $24,000 federal income tax withheld (Box 2)
  - Schedule C consulting: $32,000 net profit
- **Tax year**: 2025 (filing in 2026)
- **Prior year**: similar mix, prior-year total tax = $19,500, prior-year AGI = $108,000

## Inputs gathered

```
Current-year (2025):
  Form 1040 line 22 (income tax):   $21,879
    (AGI $142,664 − $15,750 standard deduction − $5,948 QBI deduction
     = $120,966 taxable income; 2025 Tax Rate Schedule X)
  Schedule 2 line 4 (SE tax):       $4,521   ($32,000 × 92.35% × 15.3%)
  Current-year tax (2210 line 4):   $26,400
    (no Additional Medicare Tax: wages + SE earnings $142,477 < $200,000)
  Withholding:                      $24,000  (W-2 Box 2 only)
  Estimated tax payments:           $0
  (Marcus thought withholding was enough)

Prior-year (2024):
  Tax per Form 2210 line 8 rules:   $19,500
  AGI:                              $108,000
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis:
  Unpaid balance = $26,400 − $24,000 = $2,400
  $2,400 > $1,000 → de minimis fails
  Continue.

Test 2 — No prior-year liability (IRC §6654(e)(2)):
  Prior-year tax = $19,500 ≠ $0 → fails
  Continue.

Test 3 — 90% current-year safe harbor:
  Required: $26,400 × 90% = $23,760
  Paid: $24,000 (withholding alone)
  $24,000 > $23,760 → safe harbor MET ✓

No penalty owed. No Form 2210 required.
```

Check both safe harbors:

```
Test 3 — 90% current-year:
  Required = $23,760. Paid = $24,000. Met. ✓

Test 4 — 100% prior-year (AGI ≤ $150K so 100% applies):
  Required = $19,500. Paid = $24,000. Met. ✓
```

Both safe harbors met. Marcus's W-2 withholding alone covers him. No penalty, no Form 2210.

## What if Marcus's withholding had been lower?

Suppose Marcus's W-2 withholding was $22,000 instead of $24,000 (under-withheld due to a W-4 mistake). Re-run:

```
Test 1 — De minimis:
  Unpaid balance = $26,400 − $22,000 = $4,400 > $1,000. Fails.

Test 3 — 90% current:
  Required: $23,760. Paid: $22,000. Fails.

Test 4 — 100% prior:
  Required: $19,500. Paid: $22,000. Met. ✓
```

Even with lower withholding, the prior-year safe harbor saves Marcus. No penalty.

## What if Marcus's prior-year tax had been higher?

Suppose Marcus's prior-year tax was $24,000 (similar income but no side gig) and current-year withholding was $22,000:

```
Test 3 — 90% current ($26,400 tax):
  Required: $23,760. Paid: $22,000. Fails.

Test 4 — 100% prior ($24,000 tax):
  Required: $24,000. Paid: $22,000. Fails.

Required annual payment = smaller of $23,760 or $24,000 = $23,760
Penalty: yes, owed.
```

Compute the regular method penalty:

```
Part III, Section A (regular method):
  Line 10, each column: $23,760 × 25% = $5,940
  Line 11, each column: withholding $22,000 ÷ 4 = $5,500 (no estimated payments)

  Column (a) 4/15/25: line 15 $5,500 → line 17 underpayment $440
  Column (b) 6/15/25: the $5,500 pays the $440 first (line 14) → line 15 $5,060 → line 17 $880
  Column (c) 9/15/25: the $5,500 pays the $880 first → line 15 $4,620 → line 17 $1,320
  Column (d) 1/15/26: the $5,500 pays the $1,320 first → line 15 $4,180 → line 17 $1,760
  The $1,760 is paid with the return on April 15, 2026.

Section B penalty worksheet (2025 rate: 0.07 in every rate period):
  (a) $440 from 4/15/25 to 6/15/25 (61 days):     $440 × 0.07 × 61/365   = $5.15
  (b) $880 from 6/15/25 to 9/15/25 (92 days):     $880 × 0.07 × 92/365   = $15.53
  (c) $1,320 from 9/15/25 to 1/15/26 (122 days):  $1,320 × 0.07 × 122/365 = $30.88
  (d) $1,760 from 1/15/26 to 4/15/26 (90 days):   $1,760 × 0.07 × 90/365  = $30.38
  Total (line 19) ≈ $81.94
```

Penalty ≈ $82. (Same total as treating each $440 shortfall as unpaid from its own due date to April 15, 2026: the balance outstanding over time is identical.) Marcus could let the IRS compute it (simpler) or file Form 2210 (no waiver claim, no Schedule AI needed).

## The completed Form 2210 draft (under the modified scenario)

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] No Form 2210 — let IRS compute penalty and bill (~$82 expected)
  (Filing decision: no Part II box applies; Schedule AI doesn't help with even-income mix; no waiver basis. IRS will compute and send a CP30 notice.)

## Header
Name(s) shown on return:    Marcus Chen
Your SSN:                   XXX-XX-XXXX
Filing status:              Single
Prior-year AGI:             $108,000  → safe-harbor multiplier: 100%

## Part I — Required Annual Payment
1. Form 1040 line 22:                               $21,879
2. Other taxes (Schedule 2 line 4, SE tax):         $4,521
3. (Refundable credits):                            $0
4. Current-year tax:                                $26,400
5. Line 4 × 90%:                                    $23,760
6. Withholding:                                     $22,000
7. Line 4 − Line 6:                                 $4,400  (not less than $1,000 → continue)
8. Prior-year tax × 100%:                           $24,000
9. Required annual payment (smaller of 5 or 8):     $23,760

## Part II — Reasons for Filing
- [ ] Box A
- [ ] Box B
- [ ] Box C
- [ ] Box D
- [ ] Box E
- [x] None (don't file Form 2210)

## Part III, Section A — Underpayment per column (worksheet only; not filed)

| Line | (a) 4/15/25 | (b) 6/15/25 | (c) 9/15/25 | (d) 1/15/26 |
|------|-------------|-------------|-------------|-------------|
| 10 Required installment | $5,940 | $5,940 | $5,940 | $5,940 |
| 11 Tax withheld | $5,500 | $5,500 | $5,500 | $5,500 |
| 14 Earlier underpayment | — | $440 | $880 | $1,320 |
| 15 Line 13 − 14 | $5,500 | $5,060 | $4,620 | $4,180 |
| 17 Underpayment | $440 | $880 | $1,320 | $1,760 |

(Withholding allocated evenly per IRC §6654(g)(1) default.)

## Part III, Section B — Penalty worksheet (2025 rate 7% in every rate period)

| Column | Underpayment | Paid on | Days | Rate | Penalty |
|--------|--------------|---------|------|------|---------|
| (a)    | $440         | 6/15/25 | 61   | 7%   | $5.15   |
| (b)    | $880         | 9/15/25 | 92   | 7%   | $15.53  |
| (c)    | $1,320       | 1/15/26 | 122  | 7%   | $30.88  |
| (d)    | $1,760       | 4/15/26 | 90   | 7%   | $30.38  |
| **Total** |           |         |      |      | **$81.94** |

## Validation summary
- Math: all checks passed (2025 worksheet rate 0.07)
- Sanity:
  - Penalty < $100: filer should let IRS compute and bill rather than file Form 2210
  - Income was even across the year: Schedule AI does not help
  - For 2026 planning: the 2026 prior-year safe harbor is 100% of 2025 tax ($26,400; 2025 AGI $142,664 ≤ $150,000), $4,400 more than 2025 withholding
- Filing decision: let IRS compute (no Form 2210 attached)
- Penalty: ~$82 (IRS-computed, sent on a CP30 notice)
- Next steps:
  - Form 1040 line 38: leave blank (IRS computes)
  - For 2026: increase W-4 Step 4(c) by about $170 per biweekly paycheck ($4,420/year), or pay $1,100 per quarter on Form 1040-ES, so payments reach 100% of 2025 tax

## Sources cited in this draft
- IRS Form 2210, Rev. 2025
- IRS Instructions for Form 2210, Rev. 2025
- IRC §6654(e)(1) — $1,000 de minimis
- IRC §6654(d)(1)(B) — 90% current-year / 100% prior-year required annual payment
- IRC §6654(b)(3) — Payments applied to the earliest underpayment
- IRC §6654(g)(1) — Withholding allocated evenly across quarters
- IRC §6621 — Penalty rate (7% for all 2025 rate periods, 2025 Form 2210 worksheet)
- Form 1040 Line 38
```

## Why each non-obvious choice

**Why does the SKILL recommend "let IRS compute" instead of filing Form 2210?** Two reasons. First, the regular method is the only method that fits this filer (income was even, no waiver basis). The IRS computes regular method automatically. Second, the penalty is small (~$82) — the analytical and form-filing effort exceeds the cost of just letting IRS bill it.

**Why does Marcus pass the safe harbor in the original scenario but fail in the modified one?** The original had withholding of $24,000 against current-year tax of $26,400. 90% current = $23,760, and $24,000 > $23,760 → safe harbor met. The modified scenario dropped withholding to $22,000, falling under both 90% current ($23,760) and 100% prior ($24,000).

**Why is the prior-year safe harbor 100% and not 110%?** Marcus's prior-year AGI was $108,000. The 110% threshold under IRC §6654(d)(1)(C) only kicks in if prior-year AGI > $150,000.

**Why won't Schedule AI help here?** Marcus's income was roughly even across the year (W-2 paid biweekly, Schedule C work spread across the year). Schedule AI annualizes income through each quarter-end and applies cumulative percentages — for steady income, the cumulative annualization closely matches the regular method's 25% per quarter, and Schedule AI doesn't reduce the required installments. It only helps when income is back-loaded.

**What should Marcus do for 2026?** For 2026 the prior-year safe harbor is 100% of his 2025 tax, $26,400 (2025 AGI $142,664, under $150,000). At $22,000 of withholding he is $4,400 short. Either increase W-4 Step 4(c) by about $170 per biweekly paycheck (26 × $170 = $4,420), or pay $1,100 per quarter on Form 1040-ES. Either approach lifts him to 100% of prior-year tax (the easier safe harbor to lock into prospectively). The W-4 approach is simpler — one form change with the employer, no quarterly tracking, and withholding counts as paid evenly even if the change starts mid-year.

**What audit defense does Marcus have?** His W-2 Box 2 matches his pay summary; Schedule C income is documented; SE tax computes through Schedule SE; no Form 8959 is needed (wages plus SE earnings are under $200,000). The IRS-computed penalty of ~$82 arrives on a CP30 notice; Marcus pays it by the date on the notice (no interest on the penalty if paid by then, per the Form 1040 line 38 instructions).
