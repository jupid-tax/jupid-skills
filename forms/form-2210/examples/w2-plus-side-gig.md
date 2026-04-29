# Example: W-2 Employee with Under-Withheld Side-Gig Income (Modest Penalty)

A complete walkthrough of Form 2210 for a filer with steady W-2 wages and a Schedule C side gig that wasn't subject to withholding. Walks through both safe harbors and produces a small penalty using the regular method.

## The filer

- **Name**: Marcus Chen
- **Filing status**: Single
- **Income**:
  - W-2 from MarketingCo: $95,000 (Box 1) / $24,000 federal income tax withheld (Box 2)
  - Schedule C consulting: $32,000 net profit
- **Tax year**: 2025 (filing in 2026)
- **Prior year**: similar mix, prior-year total tax = $19,500, prior-year AGI = $108,000

## Inputs gathered

```
Current-year:
  Form 1040 Line 22 (total tax):    $26,400
    (income tax + SE tax + Add'l Medicare Tax)
  Withholding:                      $24,000  (W-2 Box 2 only)
  Estimated tax payments:           $0
  (Marcus thought withholding was enough)

Prior-year:
  Form 1040 Line 22:                $19,500
  AGI:                              $108,000
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis:
  Unpaid balance = $26,400 − $24,000 = $2,400
  $2,400 > $1,000 → de minimis fails
  Continue.

Test 2 — First-year exception:
  Prior-year tax = $19,500 ≠ $0 → fails
  Continue.

Test 3 — 90% current-year safe harbor:
  Required: $26,400 × 90% = $23,760
  Paid: $24,000 (withholding alone)
  $24,000 > $23,760 → safe harbor MET ✓

No penalty owed. No Form 2210 required.
```

Wait — let's double-check by computing both safe harbors:

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
Required quarterly installments (cumulative):
  Q1: $23,760 × 25% = $5,940
  Q2: $23,760 × 50% = $11,880
  Q3: $23,760 × 75% = $17,820
  Q4: $23,760 × 100% = $23,760

Withholding allocated evenly: $22,000 ÷ 4 = $5,500 per quarter
  (cumulative: $5,500 / $11,000 / $16,500 / $22,000)

Underpayment per quarter:
  Q1: $5,940 − $5,500 = $440
  Q2: $11,880 − $11,000 = $880  (incremental: $440)
  Q3: $17,820 − $16,500 = $1,320  (incremental: $440)
  Q4: $23,760 − $22,000 = $1,760  (incremental: $440)

Penalty (assume 8% annual rate, days from quarter due to next-year 4/15):
  Q1 underpayment $440 outstanding 365 days × 8% = $35.20
  Q2 underpayment +$440 outstanding 304 days × 8% = $29.32
  Q3 underpayment +$440 outstanding 213 days × 8% = $20.54
  Q4 underpayment +$440 outstanding 90 days × 8% = $8.68
  Total ≈ $93.74
```

Penalty ≈ $94. Marcus could let the IRS compute it (simpler) or file Form 2210 (no waiver claim, no Schedule AI needed).

## The completed Form 2210 draft (under the modified scenario)

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] No Form 2210 — let IRS compute penalty and bill (~$94 expected)
  (Filing decision: regular method gives the only available answer; Schedule AI doesn't help with even-income mix; no waiver basis. IRS will compute and issue CP14 notice.)

## Header
Name(s) shown on return:    Marcus Chen
Your SSN:                   XXX-XX-XXXX
Filing status:              Single
Prior-year AGI:             $108,000  → safe-harbor multiplier: 100%

## Part I — Required Annual Payment
1. Current-year total tax:                          $26,400
2. (Other taxes already in Line 1 per worksheet):   $0
3. (Refundable credits):                            $0
4. Subtotal:                                        $26,400
5. Line 4 × 90%:                                    $23,760
6. Current-year withholding:                        $22,000
7. Line 5 − Line 6:                                 $1,760  (> $1,000 → not de minimis)
8. Prior-year tax × 100%:                           $24,000
9. Required annual payment (smaller of 5 or 8):     $23,760

## Part II — Waivers (none claimed)
- [ ] Box A
- [ ] Box B
- [ ] Box C
- [x] No waiver

## Part III — Quarterly Underpayment Computation (Regular Method)

| Quarter | Due date | Cumulative req'd installment | Cumulative withholding | Cumulative paid | Underpayment |
|---------|----------|------------------------------|----------------------|----------------|--------------|
| Q1      | 4/15/2025 | $5,940                       | $5,500               | $5,500         | $440         |
| Q2      | 6/16/2025 | $11,880                      | $11,000              | $11,000        | $880         |
| Q3      | 9/15/2025 | $17,820                      | $16,500              | $16,500        | $1,320       |
| Q4      | 1/15/2026 | $23,760                      | $22,000              | $22,000        | $1,760       |

(Withholding allocated evenly per IRC §6654(g)(1) default.)

## Penalty computation per quarter (illustrative — verify rates against current Form 2210 instructions)

| Quarter | Incremental underpayment | Days (due to next 4/15) | Rate | Penalty |
|---------|--------------------------|--------------------------|------|---------|
| Q1      | $440                     | 365                      | 8%   | $35.20  |
| Q2      | $440                     | 304                      | 8%   | $29.32  |
| Q3      | $440                     | 213                      | 8%   | $20.54  |
| Q4      | $440                     | 90                       | 8%   | $8.68   |
| **Total** |                       |                          |      | **$93.74** |

## Validation summary
- Math: all checks passed (using illustrative 8% rate)
- Sanity:
  - Penalty < $100: filer should let IRS compute and bill rather than file Form 2210
  - Income was even across the year: Schedule AI does not help
  - For 2026 planning: update Form W-4 to add ~$8/biweekly extra federal withholding to lock into prior-year safe harbor next year
- Filing decision: let IRS compute (no Form 2210 attached)
- Penalty: ~$94 (IRS-computed, expected on CP14 notice 4-8 weeks post-acceptance)
- Next steps:
  - Form 1040 Line 38: leave blank (IRS computes)
  - For 2026: increase W-4 Step 4(c) by $8 biweekly to add ~$200/year of withholding, putting Marcus over both safe harbors

## Sources cited in this draft
- IRS Form 2210, Rev. 2025
- IRS Instructions for Form 2210, Rev. 2025
- IRC §6654(d)(1)(A) — $1,000 de minimis
- IRC §6654(d)(1)(B) — 100% prior-year safe harbor
- IRC §6654(g)(1) — Withholding allocated evenly across quarters
- IRC §6621 — Penalty rate (verify current rate against Form 2210 instructions)
- Form 1040 Line 38
```

## Why each non-obvious choice

**Why does the SKILL recommend "let IRS compute" instead of filing Form 2210?** Two reasons. First, the regular method is the only method that fits this filer (income was even, no waiver basis). The IRS computes regular method automatically. Second, the penalty is small (~$94) — the analytical and form-filing effort exceeds the cost of just letting IRS bill it.

**Why does Marcus pass the safe harbor in the original scenario but fail in the modified one?** The original had withholding of $24,000 against current-year tax of $26,400. 90% current = $23,760, and $24,000 > $23,760 → safe harbor met. The modified scenario dropped withholding to $22,000, falling under both 90% current ($23,760) and 100% prior ($24,000).

**Why is the prior-year safe harbor 100% and not 110%?** Marcus's prior-year AGI was $108,000. The 110% threshold under IRC §6654(d)(1)(C) only kicks in if prior-year AGI > $150,000.

**Why won't Schedule AI help here?** Marcus's income was roughly even across the year (W-2 paid biweekly, Schedule C work spread across the year). Schedule AI annualizes income through each quarter-end and applies cumulative percentages — for steady income, the cumulative annualization closely matches the regular method's 25% per quarter, and Schedule AI doesn't reduce the required installments. It only helps when income is back-loaded.

**What should Marcus do for 2026?** Either increase W-4 Step 4(c) by ~$8 per biweekly paycheck (adds $208/year of withholding), or file quarterly estimates of $50/quarter. Either approach lifts him above 100% of prior-year tax (which is the easier safe harbor to lock into prospectively). The W-4 approach is simpler — one form change with the employer, no quarterly tracking.

**What audit defense does Marcus have?** His W-2 Box 2 matches his pay summary; Schedule C income is documented; SE tax computes through Schedule SE; Form 8959 documents any Additional Medicare Tax (likely zero at this income level). The IRS-computed penalty of ~$94 will appear on the CP14 notice and Marcus pays it within 21 days to close the case.
