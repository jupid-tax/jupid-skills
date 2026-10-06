# Example: Full-Time Nanny with Income Tax Withholding (Tax Year 2025)

A married couple employs one unrelated nanny all year, withholds her Social Security, Medicare, and requested income tax, pays Illinois unemployment contributions on time, and covers the Schedule H bill through extra wage withholding. Line map: 2025 Schedule H (Created 4/15/25) and 2025 Instructions for Schedule H (ISH25).

## The household

- **Employer:** Daniel Okafor (EIN 3X-XXXXXXX, masked), filing Form 1040 jointly with Priya Okafor. Daniel is the employer of record, so one Schedule H is attached under his name; a joint return may carry at most two (ISH25, "Name of employer").
- **Location:** Evanston, Illinois.
- **Employee:** Rosa Delgado, 34, unrelated, cares for the children in the Okafors' home on their schedule and with their supplies. Household employee under the control test (ISH25, "Did you have a household employee?").
- **Pay:** $860 every Friday. 2025 had 52 Fridays, 13 in each quarter: $11,180 per quarter, $44,720 for the year. No meals, lodging, or transit benefits.
- **Withholding:** Rosa gave a Form W-4 asking for income tax withholding; per Pub. 15-T it came to $58 a week ($3,016 for the year). The Okafors also withhold her 7.65%.
- **Prior year:** Rosa was paid more than $1,000 in every 2024 quarter.
- **Illinois:** registered with the state unemployment agency. Illinois' 2025 taxable wage base is $13,916 (DOL, Significant Provisions of State UI Laws, July 2025). The account statement shows a 3.1% assigned rate and 2025 contributions of $346.58 (Q1, on $11,180) and $84.82 (Q2, on the remaining $2,736), total $431.40, all paid by January 2026. Rate and amounts are the user's documents, not a statement of Illinois law for every household.

## Weekly paycheck

| Item | Amount | Basis |
|---|---:|---|
| Gross | 860.00 | |
| Social Security withheld | 53.32 | 860 × 6.2% |
| Medicare withheld | 12.47 | 860 × 1.45% |
| Federal income tax withheld | 58.00 | W-4 and Pub. 15-T |
| Net pay | 736.21 | |

A weekly wage that is a multiple of $20 makes 6.2% and 1.45% come out to whole cents, so 52 paychecks sum exactly to the annual amounts (53.32 × 52 = 2,772.64; 12.47 × 52 = 648.44).

## Tests

- **Line A:** $44,720 ≥ $2,800 → Yes; go to line 1.
- **Line 9:** $11,180 in each 2025 quarter (and more than $1,000 in 2024) → Yes; go to line 10.
- **Lines 10–12:** one state, Illinois, not a credit reduction state for 2025 (ISH25 Worksheet 2 rate 0.000); all contributions paid by April 15, 2026; Illinois taxes the same wages → Yes, Yes, Yes → Section A.

## The completed draft

```markdown
# Schedule H (Form 1040) — DRAFT for tax year 2025

Form revision used: Schedule H (2025), Created 4/15/25

## Header
Name of employer: Daniel Okafor
SSN: XXX-XX-XXXX (masked)
EIN: 3X-XXXXXXX

## Filing questions
A. Yes ($44,720 to Rosa Delgado)
B. (skipped)
C. (skipped)

## Part I
1. Cash wages subject to social security tax:        44,720.00
2. Social security tax (× 0.124):                      5,545.28
3. Cash wages subject to Medicare tax:                44,720.00
4. Medicare tax (× 0.029):                             1,296.88
5. Cash wages subject to Additional Medicare:              0.00
6. Additional Medicare Tax withholding:                    0.00
7. Federal income tax withheld:                        3,016.00
8. Total (2 + 4 + 6 + 7):                              9,858.16
9. $1,000 in any quarter of 2024 or 2025: Yes

## Part II
10. Yes   11. Yes   12. Yes
Section A
13. IL
14. Contributions paid to state fund:                    431.40
15. Cash wages subject to FUTA:                        7,000.00
16. FUTA tax (× 0.006):                                   42.00

## Part III
25. 9,858.16
26. Total household employment taxes:                  9,900.16
27. Yes → Schedule 2 (Form 1040) 2025, line 9: 9,900.16

## Form W-2 for Rosa Delgado (due Feb 2, 2026)
Box 1  Wages, tips, other comp.:     44,720.00
Box 2  Federal income tax withheld:   3,016.00
Box 3  Social security wages:        44,720.00
Box 4  Social security tax withheld:  2,772.64
Box 5  Medicare wages:               44,720.00
Box 6  Medicare tax withheld:           648.44
Form W-3: box b "Hshld. emp." checked; Copy A + W-3 to SSA by Feb 2, 2026

## Validation summary
- 44,720 × 0.124 = 5,545.28 ✓; × 0.029 = 1,296.88 ✓
- Line 8 = 5,545.28 + 1,296.88 + 0 + 3,016.00 = 9,858.16 ✓
- Line 26 = 42.00 + 9,858.16 = 9,900.16 ✓
- W-2 box 3 = line 1; box 5 = line 3; box 2 = line 7 ✓
- Box 4 + box 6 = 2,772.64 + 648.44 = 3,421.08 = (line 2 + line 4) ÷ 2 = 6,842.16 ÷ 2 ✓
- Year check: $2,800 test, $176,100 base, Schedule 2 line 9 are 2025 values ✓
```

## Who pays what inside line 26

| Part | Amount | Paid by |
|---|---:|---|
| Employer Social Security (6.2%) + Medicare (1.45%) | 3,421.08 | Okafors |
| FUTA | 42.00 | Okafors |
| Employee Social Security + Medicare withheld | 3,421.08 | Rosa (withheld) |
| Income tax withheld | 3,016.00 | Rosa (withheld) |
| **Line 26** | **9,900.16** | |

Lines 2 + 4 = 6,842.16 = 2 × 3,421.08. The Okafors' own cost beyond wages: 3,421.08 + 42.00 + 431.40 Illinois = 3,894.48.

## Paying during the year

Household employment taxes are paid with the Form 1040 and count as income tax for the estimated tax penalty (IRC §3510(a)–(b)). In January 2025 Daniel gave his employer a new Form W-4 with an extra $415 per biweekly paycheck. Twenty-four paychecks remained in 2025: 24 × $415 = $9,960, which covers $9,900.16. Withholding is treated as paid in equal parts on each installment date regardless of when it was withheld (IRC §6654(g)(1)), so no Form 1040-ES payments were needed for the household tax. See [`../../form-w4/SKILL.md`](../../form-w4/SKILL.md) and [`../../form-2210/SKILL.md`](../../form-2210/SKILL.md).

## Why each non-obvious choice

**All $44,720 on line 1.** The test is passed, so every cash dollar counts, including the first $2,800 (ISH25, "$2,800 test"). The $176,100 cap does not bind.

**Line 7 is Rosa's money, not the Okafors'.** It is income tax withheld at her request and turned over through the Okafors' return (ISH25 line 7).

**Line 14 is informational.** Section A computes FUTA from line 15 alone; line 14 records the contributions. Only the first $7,000 of Rosa's wages is FUTA wages even though Illinois taxed $13,916.

**No Additional Medicare.** Rosa's wages are under $200,000.

## Handoffs

- Schedule 2 assembly: [`../../schedule-2/SKILL.md`](../../schedule-2/SKILL.md) (line 9 for 2025).
- Return: [`../../form-1040/SKILL.md`](../../form-1040/SKILL.md).
- For 2026 wages, the test is $3,000, the wage base $184,500, and the 2026 draft routes line 26 to Schedule 2 line 17a.
