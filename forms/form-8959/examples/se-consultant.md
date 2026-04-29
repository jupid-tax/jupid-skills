# Example: Solo Consultant with $350K Schedule C Net Earnings (No Wages, No Withholding)

A complete walkthrough of Form 8959 for a self-employed consultant with high Schedule C net profit, no W-2 wages, and no employer-side withholding mechanism. The full Additional Medicare Tax obligation lands at filing.

## The filer

- **Name**: Sasha Volkov
- **Filing status**: Single
- **Income**: Solo consulting practice (Schedule C); no W-2 employment, no RRTA
- **Tax year**: 2025 (filing in 2026)
- **Pays quarterly estimates**: Yes, but underestimated for 2025

## Inputs gathered

| Source | Field | Amount |
|--------|-------|--------|
| Schedule C | Line 31 (net profit) | $350,000 |
| Schedule SE | Line 4a (Line 31 × 92.35%) | $323,225 |
| Schedule SE | Line 6 (net earnings, used on Form 8959 Line 8) | **$323,225** |
| W-2 (any) | Box 5 | $0 |
| W-2 (any) | Box 6 | $0 |
| RRTA | compensation | $0 |
| Form 4137 / 8919 | unreported tips / misclassified worker | $0 |

Schedule SE Line 6 = $323,225 (the figure after the 92.35% multiplier per IRC §1402(a)(12)).

Note: For Schedule SE Part I, the 12.4% Social Security portion only applies to the first $176,100 (2025 SS wage base; verify for tax year). The 2.9% Medicare portion applies to all $323,225. The Additional Medicare Tax via Form 8959 is on top of the 2.9%, computed via Form 8959 itself.

## The completed Form 8959 draft

```markdown
# Form 8959 — DRAFT for tax year 2025

## Header
Name(s) shown on return:    Sasha Volkov
Your social security number: XXX-XX-XXXX
Filing status:               Single
Threshold (Line 5):          $200,000

## Part I — Additional Medicare Tax on Medicare Wages
 1. Medicare wages (W-2 Box 5 total):              $0
 2. Unreported tips (Form 4137 Line 6):            $0
 3. Wages from Form 8919 Line 6:                   $0
 4. Add Lines 1, 2, 3:                             $0
 5. Threshold for filing status:                   $200,000
 6. Subtract Line 5 from Line 4 (floor zero):      $0
 7. Additional Medicare Tax on wages (Line 6 × 0.9%): $0

## Part II — Additional Medicare Tax on Self-Employment Income
 8. Self-employment income (Schedule SE Line 6):   $323,225
 9. Threshold for filing status:                   $200,000
10. Wages from Part I Line 4:                      $0
11. Subtract Line 10 from Line 9 (floor zero):     $200,000
12. Subtract Line 11 from Line 8 (floor zero):     $123,225
13. Additional Medicare Tax on SE income (Line 12 × 0.9%): $1,109

## Part III — RRTA Compensation
14. RRTA compensation:                             $0
15–17. (all zero)

## Part IV — Total Additional Medicare Tax
18. Total Additional Medicare Tax (7 + 13 + 17):   $1,109
    → flows to Schedule 2 Line 11 → Form 1040 Line 23

## Part V — Withholding Reconciliation
19. Medicare tax withheld (W-2 Box 6 total):       $0
20. Regular 1.45% Medicare on Line 1 ($0 × 1.45%): $0
21. Additional Medicare Tax withheld (19 − 20, floor zero): $0
22. (Same as Line 21):                             $0
23. RRTA Additional Medicare Tax withheld:         $0
24. Total Additional Medicare Tax withheld:        $0
    → flows to Form 1040 Line 25c

## Validation summary
- Math: all checks passed
- Sanity:
  - Pure SE filer with no wages → no employer withholding mechanism per IRC §3102(f)
  - Schedule SE Line 6 ($323,225) confirmed = Schedule C net profit ($350,000) × 92.35% per IRC §1402(a)(12)
  - Threshold fully available to absorb SE income (Line 11 = full $200K because Line 10 wages = $0)
  - SE surtax base: $323,225 − $200,000 = $123,225; surtax = $1,109
  - Net at filing: Line 18 − Line 24 = $1,109 owed (in addition to regular Schedule SE tax of 15.3% × $323,225 = $49,453)
- Next steps:
  - Schedule 2 Line 11 = $1,109
  - Form 1040 Line 25c does NOT include any Form 8959 amount
  - Sasha owes the full $1,109 at filing if her 2025 quarterly estimates didn't include it
  - For 2026: include the projected Additional Medicare Tax in Form 1040-ES quarterly estimates. If 2026 SE earnings are similar, ~$280 per quarter covers it.
  - Sasha should also evaluate whether she should be paying via Form 1040-ES quarterly or whether 2210 underpayment penalty applies (separate form, separate skill)

## Sources cited in this draft
- IRS Form 8959, Rev. 2025
- IRS Instructions for Form 8959, Rev. 2025
- IRC §1401(b)(2) — 0.9% Additional Medicare Tax on self-employment income
- IRC §1402(a)(12) — 92.35% multiplier for SE earnings
- IRS Schedule SE (Form 1040), Rev. 2025
- IRS Schedule 2 (Form 1040), Rev. 2025
- IRS Form 1040-ES — Estimated Tax for Individuals
```

## Why each non-obvious choice

**Why is Line 8 = $323,225 instead of $350,000 (Schedule C net profit)?** Form 8959 Line 8 takes Schedule SE Part I Line 6 — the figure after the 92.35% multiplier. The multiplier exists because self-employed filers don't get to deduct the employer-side share of SS/Medicare tax (which a W-2 employee gets implicitly, since the employer pays half and that half is not the employee's wage). The 92.35% effectively grants SE filers the same deduction. Form 8959 inherits this.

The numerical effect: at $350K Schedule C net, the surtax base is $123,225 and the surtax is $1,109. If the form used raw Schedule C net, the surtax base would be $150,000 ($350K − $200K) and the surtax would be $1,350. The difference ($241) is the multiplier benefit on the Form 8959 line.

**Why does Sasha owe the full $1,109 at filing?** Self-employment income has no withholding mechanism. Employers withhold; SE income flows through Schedule SE which computes the regular SS + Medicare tax (15.3%, paid through the SE tax line on Form 1040 via Schedule 2 Line 4) but does NOT pre-pay the Additional Medicare Tax. Form 8959 Part V reconciliation shows zero withheld because zero was withheld. The gross is owed.

**What's the total federal tax bite on Sasha's $350K SE earnings?**

```
Schedule SE tax (regular SS + Medicare):
  SS:       12.4% × min($323,225, $176,100) = $21,836  (capped at SS wage base)
  Medicare: 2.9% × $323,225               = $9,374
  Subtotal Schedule SE:                     $31,210

Form 8959 Additional Medicare Tax:
  0.9% × $123,225 = $1,109

Federal income tax (single, ~$350K - $7,003 SE deduction adjustment - $15,000 standard deduction
  = ~$328,000 taxable income, marginal rate 32% / 35%):
  Approx. $79,000 federal income tax (bracket-by-bracket calc; exact figure depends on
  all other income, deductions, credits)

Total federal tax: ~$111,300 on $350,000 gross. ~32% effective federal rate.
```

The Form 8959 surtax is ~1% of total federal tax — small in dollar terms but easy to miss. Without Form 8959, the IRS would issue a CP2000 notice 12-24 months after filing.

**Why is the planning recommendation "include in quarterly estimates" rather than "increase W-4"?** Sasha has no W-2 employer to set a W-4 with. Her only federal pre-payment mechanism is Form 1040-ES quarterly estimates. The Form 1040-ES worksheet has a line for the Additional Medicare Tax that should be included in her quarterly computation.

**What about Form 2210 underpayment penalty?** If Sasha's total 2025 federal tax (income + SE + Form 8959 surtax) exceeds her 2025 quarterly estimates by more than $1,000 AND her estimates weren't at least 90% of current-year tax or 100% of prior-year tax (110% if prior AGI > $150K), Form 2210 may apply. See the form-2210 skill for the safe harbor analysis.

**What audit defense does Sasha have?** Schedule C with full receipt-and-expense documentation; Schedule SE flowing correctly to Line 6; Form 8959 correctly applying Lines 8–13 with the threshold reduction by zero wages; no W-2 reconciliation needed because zero W-2 income. Clean trail.
