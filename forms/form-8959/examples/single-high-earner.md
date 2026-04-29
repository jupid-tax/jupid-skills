# Example: Single High-Earner with One W-2 (Employer Withholding Correctly Above $200K)

A complete walkthrough of Form 8959 for a single filer with W-2 wages above $200,000 from a single employer that withheld correctly. This is the canonical "no surprise at filing" pattern.

## The filer

- **Name**: Daniel Reyes
- **Filing status**: Single
- **Income**: One W-2 from a tech company; no self-employment, no RRTA
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered

| Source | Field | Amount |
|--------|-------|--------|
| W-2 (TechCo Inc.) | Box 1 (federal taxable wages) | $238,500 |
| W-2 (TechCo Inc.) | Box 3 (SS wages, capped at $176,100) | $176,100 |
| W-2 (TechCo Inc.) | Box 5 (Medicare wages) | **$262,400** |
| W-2 (TechCo Inc.) | Box 6 (Medicare tax withheld) | **$4,366** |
| Schedule C / SE | net earnings | $0 (no SE income) |
| RRTA | compensation | $0 |
| Form 4137 / 8919 | unreported tips / misclassified worker | $0 |

The Box 5 figure exceeds Box 1 because Daniel deferred $23,500 to a 401(k) (Box 1 reduced; Box 5 not reduced). Box 5 also includes ESPP discount and HSA wages added back.

### Verify Box 6 against the IRC §3102(f) formula

```
Expected Box 6 = (1.45% × $262,400) + (0.9% × ($262,400 − $200,000))
              = $3,805 + $562
              = $4,367
```

Actual Box 6 = $4,366. Difference of $1 due to per-paycheck rounding. Within tolerance. The employer correctly withheld the additional 0.9% on the $62,400 of wages above $200K.

## The completed Form 8959 draft

```markdown
# Form 8959 — DRAFT for tax year 2025

## Header
Name(s) shown on return:    Daniel Reyes
Your social security number: XXX-XX-XXXX
Filing status:               Single
Threshold (Line 5):          $200,000

## Part I — Additional Medicare Tax on Medicare Wages
 1. Medicare wages (W-2 Box 5 total):              $262,400
 2. Unreported tips (Form 4137 Line 6):            $0
 3. Wages from Form 8919 Line 6:                   $0
 4. Add Lines 1, 2, 3:                             $262,400
 5. Threshold for filing status:                   $200,000
 6. Subtract Line 5 from Line 4 (floor zero):      $62,400
 7. Additional Medicare Tax on wages (Line 6 × 0.9%): $562

## Part II — Additional Medicare Tax on Self-Employment Income
 8. Self-employment income (Schedule SE Line 6):   $0
 9. Threshold for filing status:                   $200,000
10. Wages from Part I Line 4:                      $262,400
11. Subtract Line 10 from Line 9 (floor zero):     $0
12. Subtract Line 11 from Line 8 (floor zero):     $0
13. Additional Medicare Tax on SE income (Line 12 × 0.9%): $0

## Part III — RRTA Compensation
14. RRTA compensation:                             $0
15. Threshold:                                     $200,000
16. Subtract Line 15 from Line 14 (floor zero):    $0
17. Additional Medicare Tax on RRTA:               $0

## Part IV — Total Additional Medicare Tax
18. Total Additional Medicare Tax (7 + 13 + 17):   $562
    → flows to Schedule 2 Line 11 → Form 1040 Line 23

## Part V — Withholding Reconciliation
19. Medicare tax withheld (W-2 Box 6 total):       $4,366
20. Regular 1.45% Medicare on Line 1 ($262,400 × 1.45%): $3,805
21. Additional Medicare Tax withheld (19 − 20, floor zero): $561
22. (Same as Line 21 — no railroad reconciliation): $561
23. RRTA Additional Medicare Tax withheld:         $0
24. Total Additional Medicare Tax withheld (22 + 23): $561
    → flows to Form 1040 Line 25c (federal income tax withheld)

## Validation summary
- Math: all checks passed
- Sanity:
  - Line 19 ($4,366) > Line 20 ($3,805): employer withheld additional Medicare tax (consistent with $262K > $200K from a single employer per IRC §3102(f))
  - Line 18 ($562) ≈ Line 24 ($561): per-paycheck rounding accounts for the $1 difference; Daniel will owe $1 at filing through normal Form 1040 totals
  - Net at filing: Line 18 − Line 24 = $1 owed (effectively zero — captured in Form 1040 totals)
- Next steps:
  - Schedule 2 Line 11 = $562
  - Form 1040 Line 25c includes $561 from Form 8959 Line 24 (in addition to $XX,XXX from W-2 Box 2 federal income tax)
  - No quarterly estimated tax adjustment needed for 2026 — employer withholding will continue to absorb the surtax as long as Daniel stays at TechCo

## Sources cited in this draft
- IRS Form 8959, Rev. 2025
- IRS Instructions for Form 8959, Rev. 2025
- IRC §3101(b)(2) — 0.9% Additional Medicare Tax on wages
- IRC §3102(f) — Employer withholding obligation at $200K wage threshold
- IRS Schedule 2 (Form 1040), Rev. 2025
- IRS Form 1040 Instructions, Line 25c
```

## Why each non-obvious choice

**Why Box 5 is $262,400 even though Box 1 is $238,500?** Box 1 (federal taxable wages) excludes 401(k) elective deferrals. Box 5 (Medicare wages) includes them. Daniel deferred $23,500 to his 401(k); the difference also reflects ESPP discount and HSA contributions handled through payroll. Always use Box 5 for Form 8959, not Box 1.

**Why the $1 rounding gap?** Payroll systems compute the additional 0.9% withholding on each paycheck once year-to-date wages cross $200K. Per-paycheck rounding to whole cents accumulates a small variance across the year. The IRS expects this and accepts it; the filer settles the variance through Form 1040 totals.

**Why doesn't Daniel need to file Form 1040-ES quarterly estimates next year?** His employer absorbs the surtax through payroll. As long as he stays at the same employer at a similar income level, withholding will continue to cover the surtax. If he changes jobs mid-year and his new employer doesn't see year-to-date wages over $200K from its own payroll, he should reassess.

**What if Daniel had a Roth IRA conversion in Q4?** Roth conversions are not earned income for Form 8959 purposes — they are ordinary income flowing to Form 1040 Line 4b but not Medicare wages. The conversion would NOT change Form 8959 figures. (It might trigger Form 8960 NIIT exposure if it pushes investment income up — but that's a different surtax.)

**What audit defense does Daniel have?** His W-2 Box 5 matches his year-end pay summary from TechCo. His Box 6 matches the IRC §3102(f) formula within $1. The Form 8959 reconciliation produces $562 owed and $561 withheld — the IRS sees a clean trail.
