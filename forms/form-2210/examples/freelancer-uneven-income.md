# Example: Freelancer with Uneven Q4-Heavy Income (Schedule AI Saves Significant Penalty)

A complete walkthrough of Form 2210 for a freelance editor with no Q1 income, modest Q2/Q3 income, and a large Q4 payday from a delivered project. Schedule AI dramatically reduces the penalty compared to the regular method.

## The filer

- **Name**: Riley Andersen
- **Filing status**: Single
- **Income**: 100% Schedule C (freelance video editor)
- **Tax year**: 2025 (filing in 2026)
- **Prior year**: $0 income (Riley was in graduate school full-time)

Wait — that triggers the first-year exception. Let me modify.

- **Prior year**: $25,000 of Schedule C income, prior-year tax $4,200, prior AGI $25,000

## Inputs gathered

```
Current-year Schedule C net profit by quarter:
  Q1 (Jan–Mar):    $0
  Q2 (Apr–May):    $5,000
  Q3 (Jun–Aug):    $15,000
  Q4 (Sep–Dec):    $80,000
  Annual:          $100,000

Schedule SE Line 6 = $100,000 × 92.35% = $92,350
SE tax = $92,350 × 15.3% = $14,130 (assuming under SS wage base; rough — exact computation has the SS / Medicare split)

Federal income tax (single, $100K - $7,065 SE deduction adjustment - $15,000 standard
                    deduction = $77,935 taxable income):
  ≈ $11,950 (10/12/22% brackets; exact figure depends on year)

Total tax (Line 22): ~$26,080

Withholding:                        $0
Estimated tax payments:             $0
  (Riley underestimated his Q4 windfall and paid no quarterlies)

Prior-year tax:                     $4,200
Prior-year AGI:                     $25,000  → 100% safe harbor multiplier
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis:
  Unpaid balance = $26,080 − $0 = $26,080 > $1,000. Fails.

Test 2 — First-year exception:
  Prior-year tax = $4,200 ≠ $0. Fails.

Test 3 — 90% current:
  Required: $26,080 × 90% = $23,472. Paid: $0. Fails.

Test 4 — 100% prior:
  Required: $4,200. Paid: $0. Fails.

Penalty owed. Required annual payment = smaller of $23,472 or $4,200 = $4,200.
```

The prior-year safe harbor is the binding constraint at $4,200.

## Regular method penalty computation

```
Required quarterly installments (cumulative):
  Q1: $4,200 × 25% = $1,050
  Q2: $4,200 × 50% = $2,100
  Q3: $4,200 × 75% = $3,150
  Q4: $4,200 × 100% = $4,200

Cumulative paid (withholding + estimates):
  Q1: $0
  Q2: $0
  Q3: $0
  Q4: $0

Underpayment per quarter (incremental):
  Q1: $1,050 (outstanding from 4/15/2025)
  Q2: $1,050 (outstanding from 6/16/2025)
  Q3: $1,050 (outstanding from 9/15/2025)
  Q4: $1,050 (outstanding from 1/15/2026)

Penalty (assume 8% annual rate, days from quarter due to next-year 4/15):
  Q1: $1,050 × 8% × (365/365) = $84
  Q2: $1,050 × 8% × (304/365) = $70
  Q3: $1,050 × 8% × (213/365) = $49
  Q4: $1,050 × 8% × (90/365) = $21
  Total ≈ $224
```

Regular method penalty: ~$224.

## Schedule AI computation

Riley's income was concentrated in Q4. Schedule AI should reduce the early-quarter required installments.

```
Standard deduction: $15,000 (full year, not prorated)
Self-employment tax: computed inside each column
```

### Column (a) — Cumulative through 3/31/2025

```
Cumulative AGI: $0
Annualized: $0 × 4 = $0
Annualized deductions: $15,000 standard
Annualized taxable income: max($0 − $15,000, 0) = $0
Annualized income tax: $0
Annualized SE tax: $0 (no SE income to date)
Annualized total tax: $0
De-annualized tax: $0 / 4 = $0
Q1 required cumulative installment: $0 × 22.5% = $0
```

Compared to regular method's $1,050 → Schedule AI saves $1,050 of Q1 required installment.

### Column (b) — Cumulative through 5/31/2025

```
Cumulative AGI (Q1 + Q2 partial): $5,000
Annualized: $5,000 × 2.4 = $12,000
Annualized AGI: $12,000
Annualized deductions: $15,000 standard
Annualized taxable income: max($12,000 − $15,000, 0) = $0
Annualized income tax: $0
Annualized SE tax: $5,000 × 92.35% × 2.4 × 15.3% ≈ $1,696 (annualized)
                  (the annualized SE-equivalent earnings of $11,082 × 15.3%)
De-annualized SE tax: $1,696 / 2.4 = $707
Annualized total tax: $0 income + $1,696 SE tax = $1,696 (annualized)
De-annualized total tax: $1,696 / 2.4 = $707
Q2 required cumulative installment: $707 × 45% = $318
```

Compared to regular method's $2,100 → Schedule AI saves $1,782 of Q2 cumulative required installment.

### Column (c) — Cumulative through 8/31/2025

```
Cumulative AGI: $20,000
Annualized: $20,000 × 1.5 = $30,000
Annualized deductions: $15,000
Annualized taxable income: $30,000 − $15,000 = $15,000

Annualized income tax (single, $15,000 taxable): ~$1,538 (10% bracket)
Annualized SE tax: $20,000 × 92.35% × 1.5 × 15.3% ≈ $4,239
                  (annualized SE earnings $27,705 × 15.3%)

But SE deduction reduces AGI: $4,239 / 2 = $2,120 deduction
Recompute annualized AGI: $30,000 − $2,120 = $27,880
Annualized taxable income: $27,880 − $15,000 = $12,880
Annualized income tax: ~$1,288

Annualized total tax: $1,288 + $4,239 = $5,527
De-annualized: $5,527 / 1.5 = $3,685
Q3 required cumulative installment: $3,685 × 67.5% = $2,487
```

Compared to regular method's $3,150 → Schedule AI saves $663 of Q3 cumulative required installment.

### Column (d) — Cumulative through 12/31/2025

```
Cumulative AGI: $100,000 (full year)
Annualized: $100,000 × 1 = $100,000
SE tax deduction: ~$7,065
AGI after SE deduction: $92,935
Annualized taxable income: $92,935 − $15,000 = $77,935
Annualized income tax: ~$11,950
SE tax: ~$14,130
Annualized total tax: $26,080
De-annualized: $26,080 / 1 = $26,080
Q4 required cumulative installment: $26,080 × 90% = $23,472
```

Compare to regular method's $4,200 (which used the smaller prior-year safe harbor).

This is the gotcha: Schedule AI uses 90% × current-year tax for column (d), NOT the prior-year safe harbor. Schedule AI's column (d) installment is $23,472, much higher than the regular method's $4,200.

For the per-quarter comparison, the filer uses the lower of:
- Schedule AI per-column installment, OR
- Regular method's per-quarter installment (using $4,200 required annual payment)

| Quarter | Schedule AI cumulative | Regular method cumulative | Smaller (used) |
|---------|------------------------|----------------------------|----------------|
| Q1 | $0 | $1,050 | **$0** |
| Q2 | $318 | $2,100 | **$318** |
| Q3 | $2,487 | $3,150 | **$2,487** |
| Q4 | $23,472 | $4,200 | **$4,200** |

## Penalty under Schedule AI (mixed quarters)

```
Q1 underpayment = max($0 − $0, 0) = $0
Q2 underpayment = max($318 − $0, 0) = $318
Q3 underpayment = max($2,487 − $0, 0) = $2,487  (but the relevant figure is incremental: $2,487 − $318 = $2,169)
Q4 underpayment = max($4,200 − $0, 0) = $4,200  (incremental: $4,200 − $2,487 = $1,713)

Penalty (assume 8% annual rate):
  Q1: $0
  Q2: $318 × 8% × (304/365) = $21
  Q3: $2,169 × 8% × (213/365) = $101  (incremental Q3 underpayment of $2,169)
       [Note: cumulative Q3 underpayment is $2,487, of which $318 was already accruing
        from Q2; only the incremental $2,169 starts accruing from Q3]
  Q4: $1,713 × 8% × (90/365) = $34
  Total ≈ $156
```

But wait — the cumulative-vs-incremental distinction matters here. Form 2210's actual worksheet computes the penalty on the *cumulative* underpayment outstanding from each due date, with payments allocated forward. Let me redo:

```
Q1: cumulative underpayment $0 outstanding 365 days → $0 penalty
Q2: cumulative underpayment $318 outstanding 304 days × 8% = $21
Q3: cumulative underpayment $2,487 outstanding 213 days × 8% = $116
    But $318 of that was already accruing from Q2. So:
    - Q2 portion ($318) continues from Q2; total days from 6/15 to 4/15 = 304 days, $21
    - New Q3 portion ($2,169) accrues from 9/15: 213 days × 8% = $101
Q4: cumulative underpayment $4,200 outstanding 90 days
    - Q2 portion ($318) continues; from 6/15 to 4/15 = 304 days = $21
    - Q3 portion ($2,169) continues; from 9/15 to 4/15 = 213 days = $101
    - New Q4 portion ($1,713) accrues from 1/15: 90 days × 8% = $34

Total penalty ≈ $21 + $101 + $34 = $156
```

(The exact math depends on the worksheet structure in the current Form 2210 instructions; this is illustrative. Verify with actual current-year worksheet.)

**Schedule AI penalty: ~$156** vs. **regular method: ~$224**. Schedule AI saves ~$68.

## The completed Form 2210 draft

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] File Form 2210 with Schedule AI (annualized income installment method)
  Reason: Q4-concentrated income; Schedule AI saves ~$68 vs. regular method.

## Header
Name(s) shown on return:    Riley Andersen
Your SSN:                   XXX-XX-XXXX
Filing status:              Single
Prior-year AGI:             $25,000  → safe-harbor multiplier: 100%

## Part I — Required Annual Payment
1. Current-year total tax:                          $26,080
4. Subtotal (after worksheet):                      $26,080
5. Line 4 × 90%:                                    $23,472
6. Current-year withholding:                        $0
7. Line 5 − Line 6:                                 $23,472  (> $1,000)
8. Prior-year tax × 100%:                           $4,200
9. Required annual payment (smaller of 5 or 8):     $4,200

## Part II — Waivers
- [x] No waiver
(Box for Schedule AI checked separately per Part III instructions)

## Schedule AI — Annualized Income Installment Method

| Quarter | Cumulative AGI | Factor | Annualized AGI | Annualized total tax | De-annualized | Cumulative % | Required cumulative installment |
|---------|----------------|--------|----------------|---------------------|---------------|--------------|-------------------------------|
| (a) Q1  | $0             | 4      | $0             | $0                  | $0            | 22.5%        | $0                            |
| (b) Q2  | $5,000         | 2.4    | $12,000        | $1,696              | $707          | 45%          | $318                          |
| (c) Q3  | $20,000        | 1.5    | $30,000        | $5,527              | $3,685        | 67.5%        | $2,487                        |
| (d) Q4  | $100,000       | 1      | $100,000       | $26,080             | $26,080       | 90%          | $23,472                       |

## Comparison: Schedule AI vs. Regular method (smaller per quarter applies)

| Quarter | Schedule AI | Regular method | Smaller (applied) | Underpayment |
|---------|-------------|----------------|-------------------|--------------|
| Q1      | $0          | $1,050         | $0                | $0           |
| Q2      | $318        | $2,100         | $318              | $318         |
| Q3      | $2,487      | $3,150         | $2,487            | $2,487       |
| Q4      | $23,472     | $4,200         | $4,200            | $4,200       |

## Penalty computation

| Underpayment portion | Source | Days outstanding | Rate | Penalty |
|----------------------|--------|------------------|------|---------|
| $318 (Q2)            | new Q2 | 304 (6/15→4/15)  | 8%   | $21     |
| $2,169 (Q3 incremental) | new Q3 | 213 (9/15→4/15) | 8%   | $101    |
| $1,713 (Q4 incremental) | new Q4 | 90 (1/15→4/15)  | 8%   | $34     |
| **Total**            |        |                  |      | **~$156** |

(Exact penalty depends on current-year rate table; verify against Form 2210 instructions.)

## Validation summary
- Math: all checks passed (using illustrative 8% rate; verify against current Form 2210 rate table)
- Sanity:
  - Income materially back-loaded: Schedule AI is appropriate (Q4 = 80% of annual income)
  - Prior-year safe harbor $4,200 caps Q4 cumulative requirement at $4,200 — Schedule AI's column (d) of $23,472 doesn't apply because the regular method's $4,200 is smaller
  - Penalty ~$156 with Schedule AI vs. ~$224 with regular method (savings ~$68)
- Filing decision: file Form 2210 with Schedule AI
- Penalty: ~$156
- Next steps:
  - Form 1040 Line 38: $156 (rounded to whole dollar)
  - For 2026: file quarterly estimates. With prior-year tax now $26,080, prior-year safe harbor next year requires either $26,080 × 100% (assuming AGI ≤ $150K) = $26,080 across four quarters or $6,520/quarter. Recommend Riley start Form 1040-ES quarterly payments at $6,520 each.
  - Alternative if Riley expects 2026 income similar to 2025: 90% × $26,080 = $23,472 / 4 = $5,868 per quarter

## Sources cited in this draft
- IRS Form 2210, Rev. 2025
- IRS Instructions for Form 2210, Rev. 2025
- IRC §6654(d)(2) — Annualized income installment method
- IRC §6654(d)(1)(B) — 100% prior-year safe harbor (applied because prior AGI ≤ $150K)
- IRC §6621 — Penalty rate (8% used illustratively; verify against current Form 2210 rate table)
- IRC §6654(g)(1) — Withholding allocated equally across quarters (not relevant here; withholding = $0)
- Schedule AI worksheet, current-year Form 2210 instructions
```

## Why each non-obvious choice

**Why does Schedule AI's column (d) show $23,472 but the actual Q4 required installment is only $4,200?** Schedule AI computes the *cumulative* required installment for each column based on annualized current-year tax × cumulative percentage. Column (d) uses 90% × current-year total tax = $23,472. But the filer's required *annual* payment (Form 2210 Line 9) was capped at $4,200 by the prior-year safe harbor. The per-quarter rule is "smaller of Schedule AI cumulative or regular method cumulative" — so for Q4, the regular method's $4,200 caps the requirement.

**Why does Schedule AI help here?** Riley earned $0 in Q1, so Schedule AI's Q1 required installment is $0 (vs. regular method's $1,050). The savings from Q1 dwarfed by Q2/Q3 savings. The cumulative effect: Schedule AI removes the early-quarter penalty accrual that would otherwise apply against the $1,050 Q1 installment that Riley couldn't have paid (had no income to pay from).

**Why doesn't the prior-year safe harbor save Riley entirely?** The prior-year safe harbor only saves the filer if they actually pre-paid the required annual amount. Riley paid $0 in withholding and $0 in estimates. So even though the required annual payment is only $4,200, Riley owes penalty on the unpaid quarterly installments.

**What about the first-year exception?** Doesn't apply because Riley had $4,200 of prior-year tax. The exception requires literally zero.

**What's the planning recommendation for 2026?** Riley should file quarterly Form 1040-ES estimates of $6,520 each (covering 100% of 2025's tax, locking in the prior-year safe harbor). If 2026 income drops back down, he can reduce mid-year. The key is getting *something* paid in each quarter to avoid the same penalty pattern.

**What audit defense does Riley have?** Schedule C with full income/expense documentation (invoices, bank statements showing the Q4 deposit, etc.); Schedule SE flowing correctly; Schedule AI requires quarter-by-quarter income documentation, which Riley has from his accounting records. The $156 penalty appears on Form 1040 Line 38; Riley pays it with the return.
