# Example: Two-Member Service LLC That Qualifies for the Schedule B, Question 4 Exception

A two-member LLC with a guaranteed payment, parts inventory, a financed van, no employees, and no foreign activity. It answers Schedule B, question 4 "Yes", so Schedules L, M-1, M-2, item F, and K-1 item L are left blank, and it qualifies for the K-2/K-3 exceptions. The members choose not to elect out of the centralized audit regime, so the return designates a partnership representative. All arithmetic below was checked in Python.

## The partnership

- **Name**: Kestrel Mobile Bike Repair LLC, Austin, Texas
- **Entity**: domestic LLC, two members, no Form 8832 or Form 2553 on file, so a partnership
- **Tax year**: calendar 2025 (2025 Form 1065, due March 16, 2026)
- **Accounting method**: cash; average annual gross receipts far below $31 million; no C corporation partner
- **Members**: Maya Ortiz 55% and Jonah Feld 45% of profit, loss, and capital; the operating agreement allocates every item by those percentages and liquidates by them
- **Business started**: April 3, 2023

## Questions the agent asked (and the answers)

| Question | Answer |
|----------|--------|
| Did anyone join, leave, or change percentage in 2025? | No |
| Payments to members, by type? | Jonah: $2,200 per month fixed for running the workshop schedule = $26,400 (guaranteed payment for services). Maya: none fixed. Draws of profit: Maya $38,000, Jonah $31,500 |
| Self-employment treatment of each member (per their CPA)? | Both work full time in the business and manage it; treat both like general partners for box 14 |
| Health insurance or retirement contributions for members? | None |
| Employees? Contractors? | No employees. Two contractors paid $4,950 in total; Forms 1099-NEC filed for both |
| Returns the LLC was required to file during calendar 2025? | Its 2024 Form 1065 and two 2024 Forms 1099-NEC: 3 returns, so e-filing is not mandatory |
| Foreign accounts, foreign partners, crypto? | None |
| Elect out of the centralized audit regime? | No; designate Maya as partnership representative |
| Preparer's basis for line 14c? | Page 1, line 8, allocated as guaranteed payments plus share of (line 8 minus all guaranteed payments) |
| Van loan: who bears the risk? (per their CPA) | Both members personally guaranteed it in proportion to their percentages: recourse, 55/45 |
| Section 199A W-2 wages and UBIA | W-2 wages $0; UBIA $46,180 (the van, placed in service 2024) |

## Inputs (from the books)

| Item | Amount |
|------|--------|
| Gross receipts (repairs and parts sales) | $187,640 |
| Refunds to customers | $1,215 |
| Cost of goods sold (Form 1125-A, line 8, parts) | $41,305 |
| Interest on the business savings account | $220 |
| Van repairs | $2,964 |
| Shop rent | $10,800 |
| Licenses and vehicle registration | $1,382 |
| Van loan interest | $1,147 |
| Depreciation (Form 4562; the van is listed property) | $9,236 |
| Insurance | $3,876 |
| Contractors | $4,950 |
| Fuel | $6,355 |
| Phone and software | $1,644 |
| Advertising | $2,215 |
| Card processing and bank fees | $3,091 |
| Client and travel meals (total $600) | 50% deductible = $300; 50% nondeductible = $300 |
| Total assets at December 31, 2025 (books) | $96,410 |

## Schedule B, question 4 test

```
Total receipts = line 1a 187,640 + lines 4-7 0 + Schedule K line 5 220 = 187,860   (< 250,000)
Total assets at year end                                               = 96,410   (< 1,000,000)
K-1s filed with the return and furnished by March 16, 2026                         (yes)
Schedule M-3 required?                                                             (no)
Answer: Yes
```

## Self-employment worksheet

```
1a Ordinary business income (Schedule K, line 1)        70,760
1b-1d                                                        0
1e                                                      70,760
2  Net gain from Form 4797 included on 1a                    0
3a                                                      70,760
3b Allocated to limited partners, corporations, etc.         0
3c                                                      70,760
4a Guaranteed payments (Schedule K, line 4c)            26,400
4b Limited partners (other than services), entities          0
4c                                                      26,400
5  Net earnings from self-employment (K line 14a)       97,160
```

## The completed draft

```markdown
# Form 1065 — DRAFT for tax year 2025
Kestrel Mobile Bike Repair LLC   EIN 88-XXXXXXX   Austin, TX

## Header
A. Principal business activity: Repair and maintenance
B. Principal product or service: Bicycle repair
C. Business code: 811490 (Other personal and household goods repair and maintenance)  [user confirmed from the code list]
D. EIN: 88-XXXXXXX
E. Date business started: 04/03/2023
F. Total assets: blank (Schedule B, question 4 = Yes)
G. Boxes: none
H. Accounting method: (1) Cash
I. Number of Schedules K-1: 2
J. Schedules C and M-3: not attached
K. Aggregation/grouping: none

## Income
1a. Gross receipts or sales:                 187,640
1b. Returns and allowances:                    1,215
1c. Balance:                                 186,425
2.  Cost of goods sold (Form 1125-A):         41,305
3.  Gross profit:                            145,120
4.  Ordinary income from other entities:           0
5.  Net farm profit:                               0
6.  Net gain from Form 4797:                       0
7.  Other income:                                  0
8.  Total income:                            145,120

## Deductions
9.  Salaries and wages:                            0
10. Guaranteed payments to partners:          26,400
11. Repairs and maintenance:                   2,964
12. Bad debts:                                     0
13. Rent:                                     10,800
14. Taxes and licenses:                        1,382
15. Interest:                                  1,147
16a. Depreciation:                             9,236
16b. Less depreciation elsewhere:                  0
16c. Net:                                      9,236
17. Depletion:                                     0
18. Retirement plans:                              0
19. Employee benefit programs:                     0
20. Energy efficient commercial buildings:         0
21. Other deductions (statement):             22,431
22. Total deductions:                         74,360
23. Ordinary business income:                 70,760

## Tax and payment
24-28: 0    29: 0    30: 0    31: 0    32a: 0

Line 21 statement: insurance 3,876; contract labor 4,950; fuel 6,355; phone and software 1,644;
advertising 2,215; card processing and bank fees 3,091; meals (50% of 600) 300. Total 22,431.

## Schedule B
1 c (Domestic LLC) | 2a No | 2b Yes (Schedule B-1, Part II: Maya Ortiz, SSN, United States, 55%)
3a No | 3b No | 4 Yes | 5 No | 6 No | 7 No | 8 No | 9 No | 10a No | 10b No | 10c No | 10d No
11 unchecked | 12 No | 13a 0 | 14 No | 15 0 | 16a Yes | 16b Yes | 17 0 | 18 0 | 19 No | 20 No
21 No | 22 No | 23 No | 24 No | 25 No | 26 0 | 27 No | 28 No | 29a No | 29b No | 30 No
32 unchecked | 33 No
Partnership representative: Maya Ortiz, 2417 Larkwood Dr, Austin, TX 78723, (512) 555-0148
(no designated individual; the PR is an individual)

## Schedule K
1.  Ordinary business income:                 70,760
2-3c. Rental:                                      0
4a. Guaranteed payments, services:            26,400
4b. Guaranteed payments, capital:                  0
4c. Total guaranteed payments:                26,400
5.  Interest income:                             220
6a-11:                                             0
12-13e:                                            0
14a. Net earnings from self-employment:       97,160
14b. Gross farming or fishing income:              0
14c. Gross nonfarm income:                   145,120
15a-15f:                                           0
16a. K-2 attached: unchecked   16b. Exception: checked
17a-17f:                                           0
18a-18b:                                           0
18c. Nondeductible expenses:                     300
19a. Cash distributions:                      69,500   (code F 38,000 + 31,500)
19b. Property distributions:                       0
20a. Investment income:                          220
20b. Investment expenses:                          0
20c. Other: code Z, section 199A information (Statement A)
21. Foreign taxes:                                 0

## Analysis of Net Income (Loss) per Return
1. 70,760 + 26,400 + 220 - 0 = 97,380
2. Row b (limited partners; LLC members), column (ii) Individual (active): 97,380

## Schedules L, M-1, M-2: not required (Schedule B, question 4 = Yes)

## Schedule K-1s
| Item / box                     | Maya Ortiz          | Jonah Feld          |
|--------------------------------|---------------------|---------------------|
| E / F                          | SSN / Austin, TX    | SSN / Austin, TX    |
| G                              | LLC member-manager  | LLC member-manager  |
| H1 / I1                        | Domestic / Individual | Domestic / Individual |
| J profit, loss, capital (beg/end) | 55% / 55%       | 45% / 45%           |
| K1 recourse (beg / end)        | 13,376 / 9,878      | 10,944 / 8,082      |
| K3 (guarantee)                 | checked             | checked             |
| L capital account              | not required        | not required        |
| M / N                          | No / blank          | No / blank          |
| 1 Ordinary business income     | 38,918              | 31,842              |
| 4a / 4c Guaranteed payments    | 0 / 0               | 26,400 / 26,400     |
| 5 Interest income              | 121                 | 99                  |
| 14 A Net SE earnings           | 38,918              | 58,242              |
| 14 C Gross nonfarm income      | 65,296              | 79,824              |
| 18 C Nondeductible expenses    | 165                 | 135                 |
| 19 F Cash distributions        | 38,000              | 31,500              |
| 20 A Investment income         | 121                 | 99                  |
| 20 Z* Statement A              | QBI 38,918; W-2 wages 0; UBIA 25,399 | QBI 31,842; W-2 wages 0; UBIA 20,781 |
Item C on each K-1: Ogden (paper filing).

## Required attachments
- [x] Form 1125-A
- [x] Form 4562 (van is listed property)
- [x] Line 21 statement
- [x] Schedule B-1, Part II
- [x] Schedules K-1 (2) with Statement A
- [x] K-3 notice to both members: "You will not receive Schedule K-3 unless you request it"
- [ ] Schedule B-2 (not electing out)

## Validation summary
- Math: 1c, 3, 8, 16c, 22, 23 recomputed; K-1 boxes sum to Schedule K on every line; worksheet line 5 = sum of box 14 A
- Question 4: receipts 187,860 < 250,000; assets 96,410 < 1,000,000; K-1s on time; no M-3
- Sanity: no partner payments on line 9; no portfolio income on page 1; meals split 300/300
- Penalty exposure if filed after March 16, 2026 without Form 7004: $255 × 2 partners per month

## Filing
Paper allowed (3 returns in calendar 2025). Texas, any total assets: Department of the Treasury,
Internal Revenue Service Center, Ogden, UT 84201-0011. Due March 16, 2026. Signed by a member.
```

## Check of the K-1 splits

```
Box 1:    70,760 × 55% = 38,918    70,760 × 45% = 31,842    sum 70,760
Box 5:       220 × 55% =    121       220 × 45% =     99    sum    220
Box 14A:  38,918 + 0  = 38,918     31,842 + 26,400 = 58,242 sum 97,160 = K 14a
Box 14C:  0 + 55% × (145,120 − 26,400) = 65,296
          26,400 + 45% × (145,120 − 26,400) = 79,824          sum 145,120 = K 14c
Box 18C:     300 × 55% =    165       300 × 45% =    135    sum    300
K1 begin: 24,320 × 55% = 13,376    24,320 × 45% = 10,944
K1 end:   17,960 × 55% =  9,878    17,960 × 45% =  8,082
UBIA:     46,180 × 55% = 25,399    46,180 × 45% = 20,781
```

## Why each non-obvious choice

**Why is Jonah's $26,400 on line 10 and not a wage?** Line 9 excludes payments to partners. A fixed monthly amount for work is a guaranteed payment for services (line 10, Schedule K, line 4a, box 4a).

**Why is the $220 of interest not on page 1?** Interest on a bank deposit is portfolio income (Schedule K, line 5, and investment income on line 20a). It still counts toward the question 4 total receipts.

**Why code F and not code A in box 19?** Both members performed services, received allocations of income, and took the cash as distributions, which is the three-part test for code F in the 2025 instructions. Code A is for partners not providing services.

**Why answer 2b "Yes"?** Maya owns 55% of profit, loss, and capital at year end, which is 50% or more; Schedule B-1, Part II lists her.

**Why does the Analysis of Net Income use the limited partners row?** The instructions say to report all amounts for LLC members on the line for limited partners. The active column reflects the members' answer that both materially participate.

**Why no Schedule K-2?** Question 4 is "Yes" (small partnership exception) and both members are U.S. citizens with no foreign activity (domestic filing exception). The members get the written notice with their K-1s, and line 16b is checked.

**What would change if the return were filed late?** Condition (c) of question 4 would fail. Schedules L, M-1, M-2, item F, and item L would become required, and the penalty would run at $255 × 2 members for each month or part of a month (Instructions p. 7).
