# Example: California Caregiver, State Contributions Paid Late (Tax Year 2025)

A retiree in California employs a full-time caregiver, pays the 2025 California unemployment contributions after April 15, 2026, and files his 2025 return on extension. Two adjustments stack: the 90% limit for late contributions (Worksheet 1) and California's 2025 credit reduction (Worksheet 2). Line map: 2025 Schedule H (Created 4/15/25) and 2025 Instructions for Schedule H (ISH25), Section B and Worksheets 1 and 2.

## The household

- **Employer:** Harold Bennett, 78, single, Sacramento, California. Income: Social Security benefits and a pension with federal income tax withholding. Files Form 1040 on extension (due October 15, 2026). EIN on file since he hired a caregiver in 2023.
- **Employee:** Marisol Reyes, unrelated adult, provides personal care in Harold's home on a schedule he sets. Paid $1,140 every Friday; 52 Fridays in 2025 = $59,280 ($14,820 per quarter). Harold withholds her share ($70.68 Social Security and $16.53 Medicare per week). She did not request income tax withholding.
- **California:** Harold's state account shows a 3.4% assigned rate for 2025 (user document). California's 2025 taxable wage base is $7,000 (DOL, Significant Provisions of State UI Laws, July 2025), so the unemployment contribution is $7,000 × 3.4% = $238.00. Harold paid it on **May 4, 2026**. Amounts the state withheld from Marisol's pay for state disability insurance, and any line other than the unemployment contribution, are not contributions (ISH25, Part II: payments deducted from employees' pay are excluded).
- **Credit reduction:** California 0.012 for 2025 (ISH25, Worksheet 2).

"Late" for Schedule H means paid after the due date of Form 1040 not including extensions, which was April 15, 2026 (ISH25, line 23). Harold's extension does not move that date.

## Tests and routing

- **Line A:** $59,280 ≥ $2,800 → Yes.
- **Line 9:** $14,820 per quarter → Yes.
- **Line 10:** California is a credit reduction state → **No**.
- **Line 11:** contributions paid May 4, 2026, after April 15, 2026 → **No**.
- **Line 12:** California taxed the same wages → Yes.
- Any No → **Section B**, Worksheet 1 (late), then Worksheet 2 (credit reduction).

## Section B computation

Line 17 (one row; one rate for the whole year):

| (a) State | (b) Taxable wages | (c) Rate period | (d) Rate | (e) (b) × 0.054 | (f) (b) × (d) | (g) (e) − (f) | (h) Paid by Apr 15, 2026 |
|---|---:|---|---:|---:|---:|---:|---:|
| CA | 7,000.00 | 01/01/2025–12/31/2025 | .034 | 378.00 | 238.00 | 140.00 | 0.00 |

Line 18: (g) 140.00; (h) 0.00. Line 19: 140.00. Line 20: 7,000.00. Line 21: 7,000 × 0.06 = 420.00. Line 22: 7,000 × 0.054 = 378.00.

Worksheet 1 (Credit for Late Contributions):

| Line | Computation | Amount |
|---|---|---:|
| 1 | Schedule H line 22 | 378.00 |
| 2 | Schedule H line 19 | 140.00 |
| 3 | 378.00 − 140.00 | 238.00 |
| 4 | Contributions paid after the Form 1040 due date | 238.00 |
| 5 | Smaller of 3 or 4 | 238.00 |
| 6 | 238.00 × 0.90 | 214.20 |
| 7 | 140.00 + 214.20 | 354.20 |
| 8 | Smaller of line 1 or line 7 | 354.20 |
| 9 | Credit reduction state? Yes → Worksheet 2, line 1 | |

Worksheet 2 (Credit Reduction State):

| Line | Computation | Amount |
|---|---|---:|
| 1 | Worksheet 1, line 8 | 354.20 |
| 2 | Schedule H line 20 | 7,000.00 |
| 3 | CA: 7,000.00 × 0.012 (X in CA box only) | 84.00 |
| 4 | Total credit reduction | 84.00 |
| 5 | 354.20 − 84.00 → Schedule H line 23 | 270.20 |

Line 23: 270.20 (box checked). Line 24: 420.00 − 270.20 = **149.80**.

Comparison: paid by April 15, 2026 → line 23 = 378.00 − 84.00 = 294.00 and line 24 = 126.00. Paying late cost $23.80, which is 10% of the $238.00 credit. Outside a credit reduction state and on time, FUTA would have been $42.00.

## The completed draft

```markdown
# Schedule H (Form 1040) — DRAFT for tax year 2025

Form revision used: Schedule H (2025), Created 4/15/25

## Header
Name of employer: Harold Bennett
SSN: XXX-XX-XXXX (masked)
EIN: 6X-XXXXXXX (masked)

## Filing questions
A. Yes ($59,280 to Marisol Reyes)

## Part I
1. Cash wages subject to social security tax:        59,280.00
2. Social security tax (× 0.124):                      7,350.72
3. Cash wages subject to Medicare tax:                59,280.00
4. Medicare tax (× 0.029):                             1,719.12
5. Cash wages subject to Additional Medicare:              0.00
6. Additional Medicare Tax withholding:                    0.00
7. Federal income tax withheld:                            0.00
8. Total (2 + 4 + 6 + 7):                              9,069.84
9. Yes

## Part II
10. No (credit reduction state)   11. No (paid May 4, 2026)   12. Yes
Section B
17. CA | 7,000.00 | 01/01/2025–12/31/2025 | .034 | 378.00 | 238.00 | 140.00 | 0.00
18. (g) 140.00   (h) 0.00
19. 140.00
20. 7,000.00
21. 420.00
22. 378.00
23. 270.20  [X] late contributions / credit reduction state (Worksheets 1 and 2 kept)
24. FUTA tax: 149.80

## Part III
25. 9,069.84
26. Total household employment taxes:                  9,219.64
27. Yes → Schedule 2 (Form 1040) 2025, line 9: 9,219.64

## Form W-2 for Marisol Reyes (was due Feb 2, 2026)
Box 1 59,280.00 | Box 2 0.00 | Box 3 59,280.00 | Box 4 3,675.36 | Box 5 59,280.00 | Box 6 859.56
Form W-3: "Hshld. emp." checked

## Validation summary
- 59,280 × 0.124 = 7,350.72 ✓; × 0.029 = 1,719.12 ✓; line 8 = 9,069.84 ✓
- (e) 378.00, (f) 238.00, (g) 140.00 ✓; line 19 = 140.00 ✓
- Worksheet 1 line 8 = 354.20 ✓; Worksheet 2 line 5 = 270.20 ✓
- Line 24 = 420.00 − 270.20 = 149.80 ✓; line 26 = 149.80 + 9,069.84 = 9,219.64 ✓
- Weekly 70.68 × 52 = 3,675.36 = box 4 ✓; 16.53 × 52 = 859.56 = box 6 ✓
```

## Paying the tax

Harold has federal withholding on his pension, so the IRC §3510(b)(2) exception does not apply and line 26 counts for the estimated tax penalty (IRC §3510(b)(1)). For 2025 he paid $2,400 with each Form 1040-ES installment (April 15, June 16, September 15, 2025, and January 15, 2026; ISH25 caution), $9,600 in total, which covers $9,219.64 of household tax. For 2026 the agent offered extra pension withholding on Form W-4P instead, since withholding counts as paid evenly through the year (IRC §6654(g)(1); Pub. 926 (2026), "Asking for more federal income tax withholding"). Penalty review: [`../../form-2210/SKILL.md`](../../form-2210/SKILL.md).

## Why each non-obvious choice

**Column (h) is 0.00.** It holds only contributions paid by April 15, 2026. The May 4 payment enters through Worksheet 1, line 4.

**Worksheet 1 before Worksheet 2.** The instructions require Worksheet 1 first when both apply (ISH25, line 23 TIP).

**FUTA taxable wages for Worksheet 2 = $7,000.** Only the first $7,000 of Marisol's wages are FUTA wages, all paid in California.

**No Additional Medicare.** Wages are under $200,000.

## Handoffs

- Schedule 2 line 9 for 2025: [`../../schedule-2/SKILL.md`](../../schedule-2/SKILL.md).
- If Harold had filed before paying California and later paid, he would correct with Form 1040-X and a corrected Schedule H ([`../../form-1040-x/SKILL.md`](../../form-1040-x/SKILL.md)).
- For 2026, California's rate is pending; the 2026 draft Worksheet 2 shows "0.0XX". Do not reuse 0.012.
