# Example: Landscaping Company with 14 Employees in Texas (Tax Year 2026)

A single-state employer with full-time, seasonal, and part-time staff, employer health and 401(k) contributions, and FUTA liability that crosses $500 in the second quarter. Line numbers follow the 2026 draft Form 940 (identical to the 2025 form); confirm against the final 2026 form before filing.

## The filer

- **Name:** Bluebonnet Grounds LLC (single-member LLC, disregarded for income tax; files employment returns under its own name and EIN per the Instructions for Form 940, "Disregarded entities")
- **EIN:** 8X-XXXXXXX (user supplied; masked here)
- **Owner:** Rafael Ortega. His draws are not wages and are not on Form 940.
- **State unemployment:** Texas only. Texas taxable wage base for 2026 is $9,000 (DOL, Significant Provisions of State UI Laws, July 2026). The user confirmed every quarterly Texas payment was made by its due date and that Texas taxed all employees' wages. Texas is not on the DOL potential 2026 credit reduction list (California and U.S. Virgin Islands only); re-check the final 2026 Schedule A.
- **Deposits:** EFTPS, user's confirmation numbers on file.

## Inputs gathered

Exempt payments: employer health plan premiums of $6,180 per covered employee (E01–E05), box 4a; employer 3% safe harbor 401(k) contributions for full-time staff, box 4c. Employees' own 401(k) deferrals are inside "Wages" and stay FUTA wages.

| Emp | Role | Q1 | Q2 | Q3 | Q4 | Wages | Health (4a) | ER 401(k) (4c) | Line 3 payments | Line 5 excess |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| E01 | Office manager | 12,480 | 12,480 | 12,480 | 12,480 | 49,920.00 | 6,180.00 | 1,497.60 | 57,597.60 | 42,920.00 |
| E02 | Crew lead | 13,650 | 13,650 | 13,650 | 13,650 | 54,600.00 | 6,180.00 | 1,638.00 | 62,418.00 | 47,600.00 |
| E03 | Crew lead | 12,870 | 12,870 | 12,870 | 12,870 | 51,480.00 | 6,180.00 | 1,544.40 | 59,204.40 | 44,480.00 |
| E04 | Equipment tech | 11,830 | 11,830 | 11,830 | 11,830 | 47,320.00 | 6,180.00 | 1,419.60 | 54,919.60 | 40,320.00 |
| E05 | Crew | 9,672 | 9,672 | 9,672 | 9,672 | 38,688.00 | 6,180.00 | 1,160.64 | 46,028.64 | 31,688.00 |
| E06 | Crew | 9,230 | 9,230 | 9,230 | 9,230 | 36,920.00 | 0.00 | 1,107.60 | 38,027.60 | 29,920.00 |
| E07 | Crew | 6,695 | 6,695 | 6,695 | 6,695 | 26,780.00 | 0.00 | 803.40 | 27,583.40 | 19,780.00 |
| E08 | Crew | 6,850 | 6,850 | 6,850 | 6,850 | 27,400.00 | 0.00 | 822.00 | 28,222.00 | 20,400.00 |
| E09 | Seasonal | 0 | 5,940 | 6,210 | 1,890 | 14,040.00 | 0.00 | 0.00 | 14,040.00 | 7,040.00 |
| E10 | Seasonal | 0 | 5,615 | 5,832 | 1,728 | 13,175.00 | 0.00 | 0.00 | 13,175.00 | 6,175.00 |
| E11 | Seasonal (left Sept) | 0 | 4,968 | 5,184 | 0 | 10,152.00 | 0.00 | 0.00 | 10,152.00 | 3,152.00 |
| E12 | Seasonal (hired June) | 0 | 3,240 | 5,508 | 1,566 | 10,314.00 | 0.00 | 0.00 | 10,314.00 | 3,314.00 |
| E13 | Part-time office | 3,159 | 3,159 | 3,159 | 3,159 | 12,636.00 | 0.00 | 0.00 | 12,636.00 | 5,636.00 |
| E14 | Summer helper (19) | 0 | 1,946 | 2,918 | 0 | 4,864.00 | 0.00 | 0.00 | 4,864.00 | 0.00 |
| | **Totals** | | | | | | **30,900.00** | **9,993.24** | **439,182.24** | **302,425.00** |

FUTA wages by quarter (first $7,000 per employee, in payment order):

| Emp | Q1 | Q2 | Q3 | Q4 |
|---|---:|---:|---:|---:|
| E01–E06 | 7,000 each = 42,000 | 0 | 0 | 0 |
| E07 | 6,695 | 305 | 0 | 0 |
| E08 | 6,850 | 150 | 0 | 0 |
| E09 | 0 | 5,940 | 1,060 | 0 |
| E10 | 0 | 5,615 | 1,385 | 0 |
| E11 | 0 | 4,968 | 2,032 | 0 |
| E12 | 0 | 3,240 | 3,760 | 0 |
| E13 | 3,159 | 3,159 | 682 | 0 |
| E14 | 0 | 1,946 | 2,918 | 0 |
| **Total** | **58,704** | **25,323** | **11,837** | **0** |
| Liability × 0.006 | **352.22** | **151.94** | **71.02** | **0.00** |

Deposit test (Instructions for Form 940, "When Must You Deposit Your FUTA Tax?"):

| Quarter | Liability | Cumulative undeposited | Action |
|---|---:|---:|---|
| Q1 | 352.22 | 352.22 | ≤ $500, carry |
| Q2 | 151.94 | 504.16 | > $500, deposit $504.16 by Fri Jul 31, 2026. Deposited Jul 24, 2026 |
| Q3 | 71.02 | 71.02 | ≤ $500, carry (Nov 2, 2026 deadline not triggered) |
| Q4 | 0.00 | 71.02 | ≤ $500 at year end: deposit or pay with return by Feb 1, 2027. User deposited $71.02 on Jan 21, 2027 |

## The completed draft

```markdown
# Form 940 — DRAFT for tax year 2026

Form revision used: 2026 draft Form 940 (Created 3/25/26); re-check final

## Header
EIN: 8X-XXXXXXX
Name: Bluebonnet Grounds LLC
Trade name: blank
Address: <user's address>, Austin, TX
Type of return: none checked
Aggregate Return Filers Only: blank

## Part 1
1a. TX
1b. blank
2.  blank

## Part 2
3. Total payments to all employees:            439,182.24
4. Payments exempt from FUTA tax:               40,893.24   [X]4a [ ]4b [X]4c [ ]4d [ ]4e
5. Payments in excess of $7,000:               302,425.00
6. Subtotal (4 + 5):                           343,318.24
7. Total taxable FUTA wages (3 − 6):            95,864.00
8. FUTA tax before adjustments (7 × 0.006):        575.18

## Part 3
9.  blank
10. blank
11. blank

## Part 4
12. Total FUTA tax after adjustments:              575.18
13. FUTA tax deposited for the year:               575.18
14. Balance due:                                   blank
15a. Overpayment:                                  blank

## Part 5
16a. Q1:  352.22
16b. Q2:  151.94
16c. Q3:   71.02
16d. Q4:  blank (575.18 − 352.22 − 151.94 − 71.02 = 0)
17.  Total: 575.18 (= line 12)

## Part 6 — No designee
## Part 7 — Rafael Ortega, Owner; phone <user>; date <at signing>

## Validation summary
- Line 4 = 30,900.00 + 9,993.24 = 40,893.24 ✓ (both amounts inside line 3)
- Line 7 recomputed: 13 employees × 7,000 + 4,864 = 95,864.00 ✓
- Line 8 = 95,864 × 0.006 = 575.184 → 575.18 ✓
- Quarterly FUTA wages 58,704 + 25,323 + 11,837 = 95,864 = line 7 ✓
- 16a + 16b + 16c = 575.18 = line 12 ✓
- Deposits: Q2 deposit due Jul 31, 2026, made Jul 24 ✓; year-end $71.02 deposited before Feb 1, 2027 ✓
- Sanity: line 8 ≤ 14 × $42 = $588 ✓

## Filing
- Due Feb 1, 2027 (Jan 31 is a Sunday); because every deposit was made when due, the return may be filed by Feb 10, 2027
- E-file through a 94x provider, or paper without a payment to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0046 (Texas group; 2025 table and 2026 draft both)
```

## Why each non-obvious choice

**Health premiums and employer 401(k) on line 3 and line 4.** Line 3 includes employer contributions to a 401(k) and section 125 and health benefits, and line 4 may only hold amounts that are on line 3 (Instructions for Form 940, lines 3 and 4). Box 4a covers accident or health plan contributions; box 4c covers employer qualified-plan contributions.

**Employees' own deferrals stay in.** Box 4c excludes "elective salary reduction contributions" (Instructions for Form 940, line 4), so the wages column is gross of deferrals.

**The 19-year-old summer helper is FUTA-taxable.** No student or age exemption applies to a business employer's non-family employee. He is the only employee under $7,000, so his full $4,864 is FUTA wages.

**Line 16d blank.** The instructions compute 16d as line 17 minus 16a–16c. That is zero here because all FUTA wages were paid by September and no credit reduction applies. A zero quarter is left blank.

**Why the year-end $71.02 was deposited instead of paid with the return.** Either is allowed at $500 or less. Depositing it keeps the "deposited all your FUTA tax when it was due" condition clearly met for the February 10 filing date.

**Line 10 blank.** Texas taxed all FUTA wages and every Texas payment was made before the Form 940 due date. The Texas wage base ($9,000) exceeds $7,000, so state wages are not a constraint.

## Handoffs

- Forms W-2 and W-3 for 2026 and Q4 2026 Form 941 (see [`../../form-941/SKILL.md`](../../form-941/SKILL.md)).
- Texas quarterly wage reports are state filings, out of scope.
- If the final 2026 Schedule A adds Texas (not expected from the DOL January list), rebuild with Schedule A and line 11 before filing.
