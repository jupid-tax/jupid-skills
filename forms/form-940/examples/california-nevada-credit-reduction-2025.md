# Example: Multi-State Employer with a California Credit Reduction (Tax Year 2025)

A partnership with employees in California and Nevada, one employee who transferred between the two states, an employer health contribution, Schedule A (Form 940) with California's 2025 credit reduction, and a fourth-quarter deposit triggered by the reduction. Line map: 2025 Form 940 (Created 6/2/25) and 2025 Schedule A (Created 11/12/25).

## The filer

- **Name:** Arroyo Clay Works LLC, a two-member LLC taxed as a partnership (EIN 9X-XXXXXXX, masked)
- **Partners:** two members who receive guaranteed payments. Partners are not employees; their payments are not on Form 940 and partners are not counted for the 20-week test (Instructions for Form 940, "Who Must File Form 940?"; Pub. 15 (2026), section 15 table).
- **States:** studio in Los Angeles, California; warehouse in Reno, Nevada. The user holds unemployment accounts in both states and paid every 2025 contribution before February 2, 2026. California's 2025 taxable wage base is $7,000 (DOL, Significant Provisions of State UI Laws, July 2025), so California taxed the same wages FUTA taxes for California employees. No wages were excluded from either state's unemployment tax (user confirmed).
- **Credit reduction:** California 0.012 for 2025; Nevada 0.000 (Schedule A (Form 940) 2025, page 2).

## Inputs gathered

| Emp | State and timing | Q1 | Q2 | Q3 | Q4 | Total wages | Exempt (4a health) | Line 3 | Line 5 excess |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ana | CA, studio manager | 13,104 | 13,104 | 13,104 | 13,104 | 52,416 | 0 | 52,416 | 45,416 |
| Ben | CA, production tech | 9,945 | 9,945 | 9,945 | 9,945 | 39,780 | 3,960 | 43,740 | 32,780 |
| Cora | CA, part-time | 2,808 | 2,808 | 2,808 | 2,808 | 11,232 | 0 | 11,232 | 4,232 |
| Dev | CA Jan–Mar, NV from Apr 1 | 5,850 (CA) | 9,100 (NV) | 9,100 (NV) | 9,100 (NV) | 33,150 | 0 | 33,150 | 26,150 |
| Eli | NV, hired July | 0 | 0 | 7,020 | 7,020 | 14,040 | 0 | 14,040 | 7,040 |
| Faye | CA, holiday helper | 0 | 0 | 0 | 3,276 | 3,276 | 0 | 3,276 | 0 |
| **Totals** | | | | | | | **3,960** | **157,854** | **115,618** |

FUTA wages by quarter and state (first $7,000 per employee, in payment order, across states):

| Emp | Q1 | Q2 | Q3 | Q4 | CA FUTA wages | NV FUTA wages |
|---|---:|---:|---:|---:|---:|---:|
| Ana | 7,000 | 0 | 0 | 0 | 7,000 | 0 |
| Ben | 7,000 | 0 | 0 | 0 | 7,000 | 0 |
| Cora | 2,808 | 2,808 | 1,384 | 0 | 7,000 | 0 |
| Dev | 5,850 | 1,150 | 0 | 0 | 5,850 | 1,150 |
| Eli | 0 | 0 | 7,000 | 0 | 0 | 7,000 |
| Faye | 0 | 0 | 0 | 3,276 | 3,276 | 0 |
| **Total** | **22,658** | **3,958** | **8,384** | **3,276** | **30,126** | **8,150** |
| × 0.006 | 135.95 | 23.75 | 50.30 | 19.66 | | |

Dev's FUTA wage base is shared across states: $5,850 in California leaves $1,150 for Nevada, the same method as Example 2 in the Schedule A instructions.

## Schedule A (Form 940) for 2025

| State | Box checked | FUTA taxable wages | Reduction rate | Credit reduction |
|---|---|---:|---:|---:|
| CA | X | 30,126.00 | 0.012 | 361.51 |
| NV | X | (none entered; rate 0.000) | | |
| **Total credit reduction → Form 940 line 11** | | | | **361.51** |

30,126 × 0.012 = 361.512 → 361.51.

## Deposit test

| Quarter | Liability | Cumulative undeposited | Action |
|---|---:|---:|---|
| Q1 | 135.95 | 135.95 | carry |
| Q2 | 23.75 | 159.70 | carry |
| Q3 | 50.30 | 210.00 | carry |
| Q4 | 19.66 + 361.51 credit reduction = 381.17 | 591.17 | > $500: deposit the entire $591.17 by Mon Feb 2, 2026 (Jan 31, 2026 was a Saturday). Deposited by EFTPS on Jan 27, 2026 |

Without the credit reduction the year would have ended at $229.66 and could have been paid with the return. The reduction is fourth-quarter liability and pushed the cumulative total past $500 (Instructions for Form 940, "Fourth quarter liabilities" and line 16 Tip).

## The completed draft

```markdown
# Form 940 — DRAFT for tax year 2025

Form revision used: Form 940 (2025), Created 6/2/25; Schedule A (Form 940) 2025, Created 11/12/25

## Header
EIN: 9X-XXXXXXX
Name: Arroyo Clay Works LLC
Type of return: none checked

## Part 1
1a. blank (multi-state)
1b. [X] multi-state employer — Schedule A attached
2.  [X] wages paid in a credit reduction state — Schedule A attached

## Part 2
3. Total payments to all employees:            157,854.00
4. Payments exempt from FUTA tax:                3,960.00   [X]4a
5. Payments in excess of $7,000:               115,618.00
6. Subtotal (4 + 5):                           119,578.00
7. Total taxable FUTA wages (3 − 6):            38,276.00
8. FUTA tax before adjustments (7 × 0.006):        229.66

## Part 3
9.  blank
10. blank
11. Credit reduction (Schedule A):                 361.51

## Part 4
12. Total FUTA tax after adjustments:              591.17
13. FUTA tax deposited for the year:               591.17
14. Balance due:                                   blank
15a. Overpayment:                                  blank

## Part 5
16a. Q1: 135.95
16b. Q2:  23.75
16c. Q3:  50.30
16d. Q4: 381.17   (591.17 − 135.95 − 23.75 − 50.30)
17.  Total: 591.17 (= line 12)

## Part 6 — No designee
## Part 7 — <partner name>, Managing member; phone; date

## Validation summary
- Line 5: 45,416 + 32,780 + 4,232 + 26,150 + 7,040 + 0 = 115,618 ✓
- Line 7 recomputed: 5 × 7,000 + 3,276 = 38,276 ✓; equals CA 30,126 + NV 8,150 ✓
- Line 8: 38,276 × 0.006 = 229.656 → 229.66 ✓
- Schedule A CA: 30,126 × 0.012 = 361.51 ✓; ≤ 5 CA-paid employees × 7,000 ✓
- Line 12 = 229.66 + 361.51 = 591.17 ✓; line 17 = line 12 ✓
- Deposit made before Feb 2, 2026 ✓ → filing date may be Feb 10, 2026
```

## Why each non-obvious choice

**Line 1a blank, 1b checked.** Line 1a is only for a single state. A multi-state employer checks 1b and lists every state on Schedule A, including Nevada with a zero rate (Schedule A instructions, Step 1).

**Ben's health contribution.** Included on line 3 and exempted on line 4 (box 4a), following the IRS example on line 4 of the instructions. His excess is $43,740 − $3,960 − $7,000 = $32,780.

**Dev's split.** The $7,000 base is per employee per employer across all states. Only the $5,850 paid while he worked in California is California FUTA taxable wages for Schedule A.

**Faye's wages.** Her $3,276 is below $7,000, all FUTA wages, all in Q4, all in California, so all subject to the credit reduction.

**16d includes the credit reduction.** The instructions compute 16d as line 17 minus the first three quarters, and record credit reduction liability in the fourth quarter.

## What changes for tax year 2026

DOL's potential 2026 list (Jan 15, 2026) shows California at a 0.015 base reduction with an estimated 0.038 BCR add-on, and the 2026 draft Schedule A leaves the rate as "0.0XX". Do not reuse 0.012. Wait for the final 2026 Schedule A, then recompute line 11, 16d, and the fourth-quarter deposit, which is due February 1, 2027.

## Handoffs

- Forms 941 for each 2025 quarter and Forms W-2/W-3 (see [`../../form-941/SKILL.md`](../../form-941/SKILL.md)).
- California and Nevada quarterly wage reports are state filings, out of scope.
- Paper filing address for a California-based filer without a payment: Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0046 (Instructions for Form 940 (2025), "Where Do You File?"). See [`../filing.md`](../filing.md).
