# Example: MFJ Couple, Two W-2 Earners Each Under $200K (Owes at Filing)

A complete walkthrough of Form 8959 for a married couple filing jointly where each spouse has a W-2 under the $200,000 employer-trigger but combined household wages exceed the $250,000 MFJ filing threshold. This is the canonical "MFJ surprise" pattern that catches couples who didn't plan for it.

## The filers

- **Names**: Priya Mehta and Jordan Park
- **Filing status**: Married Filing Jointly
- **Income**: Two W-2s; no self-employment, no RRTA, no investment income above material thresholds
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered

| Source | Field | Amount |
|--------|-------|--------|
| W-2 Spouse 1 (Priya — BankCo) | Box 1 (federal taxable wages) | $172,000 |
| W-2 Spouse 1 (Priya — BankCo) | Box 5 (Medicare wages) | $186,500 |
| W-2 Spouse 1 (Priya — BankCo) | Box 6 (Medicare tax withheld) | $2,704 |
| W-2 Spouse 2 (Jordan — University) | Box 1 (federal taxable wages) | $94,000 |
| W-2 Spouse 2 (Jordan — University) | Box 5 (Medicare wages) | $98,300 |
| W-2 Spouse 2 (Jordan — University) | Box 6 (Medicare tax withheld) | $1,425 |
| Schedule C / SE | net earnings | $0 |
| RRTA | compensation | $0 |
| Form 4137 / 8919 | unreported tips / misclassified worker | $0 |

### Verify each Box 6 against the IRC §3102(f) formula

```
Priya:  Expected Box 6 = 1.45% × $186,500 = $2,704.25  →  $2,704 actual ✓
Jordan: Expected Box 6 = 1.45% × $98,300  = $1,425.35  →  $1,425 actual ✓
```

Neither employer withheld any additional 0.9% — neither saw wages over $200K from its own payroll. Combined household Medicare wages = $284,800.

## The completed Form 8959 draft

```markdown
# Form 8959 — DRAFT for tax year 2025

## Header
Name(s) shown on return:    Priya Mehta and Jordan Park
Your social security number: XXX-XX-XXXX  (Priya, the first-listed filer)
Filing status:               Married Filing Jointly
Threshold (Line 5):          $250,000

## Part I — Additional Medicare Tax on Medicare Wages
 1. Medicare wages (W-2 Box 5 total, both spouses):  $284,800
 2. Unreported tips (Form 4137 Line 6):              $0
 3. Wages from Form 8919 Line 6:                     $0
 4. Add Lines 1, 2, 3:                               $284,800
 5. Threshold for filing status:                     $250,000
 6. Subtract Line 5 from Line 4 (floor zero):        $34,800
 7. Additional Medicare Tax on wages (Line 6 × 0.9%): $313

## Part II — Additional Medicare Tax on Self-Employment Income
 8. Self-employment income (Schedule SE Line 6):     $0
 9. Threshold for filing status:                     $250,000
10. Wages from Part I Line 4:                        $284,800
11. Subtract Line 10 from Line 9 (floor zero):       $0
12. Subtract Line 11 from Line 8 (floor zero):       $0
13. Additional Medicare Tax on SE income:            $0

## Part III — RRTA Compensation
14. RRTA compensation:                               $0
15. Threshold:                                       $250,000
16. Subtract Line 15 from Line 14 (floor zero):      $0
17. Additional Medicare Tax on RRTA:                 $0

## Part IV — Total Additional Medicare Tax
18. Total Additional Medicare Tax (7 + 13 + 17):     $313
    → flows to Schedule 2 Line 11 → Form 1040 Line 23

## Part V — Withholding Reconciliation
19. Medicare tax withheld (W-2 Box 6 total):         $4,129
20. Regular 1.45% Medicare on Line 1 ($284,800 × 1.45%): $4,130
21. Additional Medicare Tax withheld (19 − 20, floor zero): $0
22. (Same as Line 21):                               $0
23. RRTA Additional Medicare Tax withheld:           $0
24. Total Additional Medicare Tax withheld:          $0
    → flows to Form 1040 Line 25c

## Validation summary
- Math: all checks passed
- Sanity:
  - MFJ couple with two W-2 earners, neither over $200K from a single employer per IRC §3102(f) → no employer withholding for Additional Medicare Tax
  - Combined wages $284,800 > MFJ threshold $250,000 → $34,800 surtax base × 0.9% = $313 owed
  - Net at filing: Line 18 − Line 24 = $313 owed
  - Line 19 = $4,129 vs. Line 20 = $4,130: $1 rounding variance across paychecks; consistent with no additional 0.9% withholding by either employer
- Next steps:
  - Schedule 2 Line 11 = $313
  - Form 1040 Line 25c does NOT include any Form 8959 amount (Line 24 = $0)
  - For 2026 planning: have one spouse update Form W-4 Step 4(c) to add ~$13/biweekly extra federal withholding to absorb the next year's expected surtax (assumes similar income trajectory; recompute in Q1 2026)
  - Alternative: file Form 1040-ES quarterly to pay $80/quarter to cover next year's expected $313 surtax

## Sources cited in this draft
- IRS Form 8959, Rev. 2025
- IRS Instructions for Form 8959, Rev. 2025
- IRC §3101(b)(2) — 0.9% Additional Medicare Tax on wages, $250K MFJ threshold
- IRC §3102(f) — Employer withholding obligation: $200K trigger per single employer regardless of filing status
- IRS Schedule 2 (Form 1040), Rev. 2025
- IRS Publication 505 — Tax Withholding and Estimated Tax (chapter on Additional Medicare Tax planning)
```

## Why each non-obvious choice

**Why does this couple owe at filing when neither made over $200K individually?** IRC §3102(f) only triggers employer withholding when *a single employer* pays *a single employee* more than $200,000 in a calendar year. The MFJ filing threshold is $250,000 of combined household wages. The gap is $50,000 of "unprotected wages" before the household triggers — meaning a couple at $250K combined owes $0 surtax, but at $284,800 combined they owe $313, with no employer-side cushion.

**Why is the planning recommendation "extra W-4 withholding" rather than "ask the employer to start withholding the 0.9%"?** Employers cannot legally withhold the additional 0.9% unless their own payroll to the employee crosses $200K. The W-4 Step 4(c) extra withholding is the lawful workaround — the employee asks the employer for additional flat-dollar federal income tax withholding, which appears in W-2 Box 2 and ultimately settles all federal tax (including the Form 8959 surtax) at filing.

**Why does Schedule 2 Line 11 show $313 if Line 21 is $0?** Schedule 2 Line 11 is the *gross* Additional Medicare Tax owed (Form 8959 Line 18). The withholding credit (Form 8959 Line 24) flows separately to Form 1040 Line 25c. The two figures meet at Form 1040 totals — Schedule 2 increases tax, Line 25c decreases tax — and the net effect is what the filer pays. In this couple's case: +$313 (Schedule 2 Line 11), $0 (Form 1040 Line 25c from 8959), so net additional tax owed is $313.

**What if the couple had filed MFS?** Each spouse would use $125K threshold. Priya at $186,500 wages owes $186,500 − $125,000 = $61,500 × 0.9% = $554. Jordan at $98,300 wages owes $0 (under $125K). Combined MFS surtax = $554, which is *higher* than MFJ's $313. MFS is rarely beneficial for this couple, but tax software should compute both filing statuses to confirm.

**What if next year Priya gets a raise to $210K (still under MFJ $250K with Jordan's $98K)?** Now Priya's employer is required to withhold 0.9% on the $10K above $200K — an extra $90 from her paycheck. The combined household wages ($308,300) are $58,300 above the MFJ threshold; surtax owed = $525. Employer withheld $90 of the $525. Net at filing: $435 owed. The W-4 extra withholding plan should be revisited.

**What audit defense do they have?** Both W-2 Box 5 figures match their year-end pay summaries. Both Box 6 figures match the IRC §3102(f) formula (1.45% only, since neither was over $200K from one employer). The Form 8959 reconciliation correctly identifies the gap. The $313 is paid through Form 1040 totals.
