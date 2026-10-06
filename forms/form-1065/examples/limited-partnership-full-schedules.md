# Example: Limited Partnership With Full Page 6, an S Corporation Partner, and an Election Out

A limited partnership above the Schedule B, question 4 thresholds, so Schedules L, M-1, M-2, item F, and K-1 item L are required. It has a general partner with a guaranteed payment for services, a limited partner with a guaranteed payment for capital, an S corporation limited partner, separately stated section 179 and charitable items, and it elects out of the centralized audit regime with Schedule B-2. All arithmetic was checked in Python.

## The partnership

- **Name**: Northgate Coffee Roasters LP, Chicago, Illinois
- **Entity**: domestic limited partnership (state LP certificate)
- **Tax year**: calendar 2025 (2025 Form 1065, due March 16, 2026)
- **Accounting method**: accrual; inventory of green and roasted coffee; books kept on the tax basis
- **Partners** (profit and loss percentages fixed by the LP agreement):
  - Ava Brennan, general partner, individual, 40%
  - Daniel Okafor, limited partner, individual, 35%
  - Ridgeway Holdings, Inc., limited partner, S corporation, 25% (shareholders: Laura Chen, Victor Chen, Chen 2019 Family Trust)
- **Liquidation clause**: liquidating distributions follow positive capital account balances
- **Employees**: 11 W-2 employees (roasting, packing, cafe staff)

## Questions the agent asked (and the answers)

| Question | Answer |
|----------|--------|
| Changes in partners or percentages in 2025? | None |
| Payments to partners, by type? | Ava: $6,000 per month for managing the business = $72,000 (services). Daniel: 6% per year on his $150,000 capital contribution = $9,000 (use of capital). Draws: Ava $52,000; Daniel $41,000; Ridgeway $30,000 |
| Does Daniel or anyone at Ridgeway perform services for the partnership? | No |
| Partner health insurance or retirement contributions? | None for partners. Employee SIMPLE IRA match $6,437 |
| Section 179 election? | Yes, $24,800 on a new roaster afterburner placed in service in 2025 |
| Charitable contributions? | $2,500 cash to a local food bank (public charity) |
| Liability allocation (per CPA)? | Ava, as general partner, bears the economic risk of loss on all liabilities and personally guaranteed the bank note: all recourse to Ava |
| Returns required during calendar 2025? | Well over 10 (11 Forms W-2, 4 Forms 941, Form 940, Forms 1099, the 2024 Form 1065): e-file is mandatory |
| Election out of the audit regime? | Yes, after review with their CPA |
| Ridgeway's shareholders (names, TINs, types)? | Laura Chen (individual), Victor Chen (individual), Chen 2019 Family Trust (trust) |
| Section 199A W-2 wages and UBIA? | W-2 wages $238,420 (includes $23,860 of roasting labor in Form 1125-A); UBIA $412,600 |
| Preparer's basis for line 14c? | Page 1, line 8; general partner only |

## Page 1

```
1a Gross receipts or sales                          1,184,370
1b Returns and allowances                               6,215
1c Balance                                          1,178,155
2  Cost of goods sold (Form 1125-A, line 8)           512,835
3  Gross profit                                       665,320
4-7                                                         0
8  Total income                                       665,320
9  Salaries and wages (other than to partners)        214,560
10 Guaranteed payments to partners                     81,000   (Ava 72,000 services; Daniel 9,000 capital)
11 Repairs and maintenance                              8,743
12 Bad debts                                            1,920
13 Rent                                                54,600
14 Taxes and licenses                                  24,318
15 Interest                                             6,412
16a Depreciation (Form 4562)                           38,950
16b Less depreciation elsewhere                             0
16c                                                    38,950
17 Depletion                                                0
18 Retirement plans (employee SIMPLE match)             6,437
19 Employee benefit programs                           12,960
20 Energy efficient commercial buildings                    0
21 Other deductions (statement)                        61,860
22 Total deductions                                   511,760
23 Ordinary business income                           153,560
24-32                                                       0
```

Line 21 statement: insurance 14,230; utilities 18,964; legal and professional fees 9,850; advertising 11,206; software 4,390; meals 3,220 (50% of 6,440). Total 61,860.

Not on page 1: bank interest $1,340 (Schedule K, line 5), section 179 $24,800 (line 12), charitable contribution $2,500 (line 13a), nondeductible half of meals $3,220 (line 18c).

## Schedule B (key answers)

- 1: b (domestic limited partnership)
- 2a: No (Ridgeway owns 25%); 2b: No (largest individual is 40%; no family holdings per the partners)
- 4: **No** (total receipts 1,184,370 + 1,340 = 1,185,710, above $250,000)
- 16a: Yes; 16b: Yes
- 24: No (prior 3-year average gross receipts far below $31 million; no losses allocated, so not a syndicate)
- 30: No
- 33: **Yes**, Schedule B-2 total 6
- All other questions: No, or 0 where a count is asked

Schedule B-2: Part I: Ava Brennan (I), Daniel Okafor (I), Ridgeway Holdings, Inc. (S). Part II for Ridgeway: Laura Chen (I), Victor Chen (I), Chen 2019 Family Trust (T). Part III: line 1 = 3, line 2 = 3, line 3 = 6. The trust shareholder does not disqualify the election: an S corporation is an eligible partner regardless of its shareholders, but its shareholders are counted (Regulations section 301.6221(b)-1(b)(2)(ii), (b)(3)(i)). Notify all three partners of the election within 30 days (section 301.6221(b)-1(c)(3)). No PR designation.

## Self-employment worksheet

```
1a / 1e / 3a  Ordinary business income                     153,560
3b  Allocated to limited partners and corporations (60%)    92,136
3c  General partner share (40%)                             61,424
4a  Guaranteed payments (Schedule K, line 4c)               81,000
4b  To limited partners for other than services              9,000   (Daniel's return on capital)
4c                                                          72,000
5   Net earnings from self-employment (K line 14a)         133,424
```

## Schedule K

```
1   Ordinary business income                 153,560
4a  Guaranteed payments, services             72,000
4b  Guaranteed payments, capital               9,000
4c  Total                                     81,000
5   Interest income                            1,340
12  Section 179 deduction                     24,800
13a Cash contributions                         2,500
14a Net earnings from self-employment        133,424
14c Gross nonfarm income                     305,728   (72,000 + 40% × (665,320 − 81,000))
16b Exception to filing Schedule K-2          checked
18c Nondeductible expenses                     3,220
19a Distributions of cash                    123,000   (code F 52,000 + code A 41,000 + 30,000)
20a Investment income                          1,340
20c Code Z (Statement A)
All other lines                                    0
```

Domestic filing exception for K-2/K-3: no foreign activity; direct partners are two U.S. citizens and an S corporation (criterion 2 allows S corporations); notice attached to each K-1; no K-3 request by the 1-month date. A C corporation partner would have failed criterion 2.

## Analysis of Net Income (Loss) per Return

```
1  153,560 + 81,000 + 1,340 − 24,800 − 2,500 = 208,600
2a General partners, (ii) Individual (active):   123,040   Ava
2b Limited partners, (i) Corporate:               31,900   Ridgeway
2b Limited partners, (iii) Individual (passive):  53,660   Daniel
   Total                                          208,600
```

Per partner: 40%, 35%, 25% of (153,560 + 1,340 − 24,800 − 2,500) = 127,600, plus each partner's guaranteed payments.

## Schedule L (books on the tax basis)

```
                                         Beginning            End
1   Cash                                    84,215          36,038
2a  Trade notes and accounts receivable     61,340          70,115
2b  Less allowance                               0               0
3   Inventories                             47,980          52,406
9a  Buildings and depreciable assets       286,400         372,500
9b  Less accumulated depreciation         (118,650)       (182,400)
13  Other assets (deposits)                  9,100           9,100
14  Total assets                           370,385         357,759
15  Accounts payable                        38,760          41,207
16  Notes payable < 1 year                  18,000          18,000
17  Other current liabilities               12,415          13,962
19b Notes payable 1 year or more            96,000          78,000
21  Partners' capital accounts             205,210         206,590
22  Total liabilities and capital          370,385         357,759
```

Item F = 357,759. Additions to 9a: 24,800 (section 179 property) + 61,300 (other equipment). 9b increase: 38,950 depreciation + 24,800 section 179 expensed.

## Schedule M-1

```
1  Net income per books                     124,380   (153,560 + 1,340 − 24,800 − 2,500 − 3,220)
2  Income on K not on books                       0
3  Guaranteed payments (other than health)   81,000
4a Depreciation                                   0
4b Travel and entertainment                   3,220   (nondeductible half of meals)
5  Add lines 1 through 4                    208,600
6a Tax-exempt interest                            0
7a Depreciation                                   0
8  Add lines 6 and 7                              0
9  Income per return                        208,600   = Analysis line 1
```

## Schedule M-2 and item L

```
M-2  1  Beginning balance                   205,210
     2a Cash contributed                          0
     2b Property contributed                      0
     3  Net income (Analysis line 1)        208,600
     4  Other increases                           0
     5  Add lines 1 through 4               413,810
     6a Cash distributions                  123,000
     6b Property distributions                    0
     7  Other decreases                      84,220   (guaranteed payments 81,000; nondeductible meals 3,220)
     8  Add lines 6 and 7                   207,220
     9  Ending balance                      206,590
```

| Item L | Ava | Daniel | Ridgeway | Total |
|--------|-----|--------|----------|-------|
| Beginning capital account | 79,540 | 78,150 | 47,520 | 205,210 |
| Capital contributed | 0 | 0 | 0 | 0 |
| Current year net income (loss) | 49,752 | 43,533 | 31,095 | 124,380 |
| Other increase (decrease) | 0 | 0 | 0 | 0 |
| Withdrawals and distributions | (52,000) | (41,000) | (30,000) | (123,000) |
| Ending capital account | 77,292 | 80,683 | 48,615 | 206,590 |

Current year net income = share of (153,560 + 1,340 − 24,800 − 2,500 − 3,220) = share of 124,380. Guaranteed payments are not in item L. Ending total 206,590 = M-2 line 9 = Schedule L line 21.

## Schedule K-1s

| Item / box | Ava Brennan | Daniel Okafor | Ridgeway Holdings, Inc. |
|------------|-------------|---------------|-------------------------|
| G | General partner | Limited partner | Limited partner |
| I1 | Individual | Individual | Corporation (S corporation) |
| J profit / loss (beg and end) | 40% | 35% | 25% |
| J capital, beginning | 38.7603% | 38.0829% | 23.1568% |
| J capital, ending | 37.4132% | 39.0547% | 23.5321% |
| K1 recourse (beg / end) | 165,175 / 151,169 | 0 / 0 | 0 / 0 |
| K3 | checked | | |
| L (see table above) | 77,292 ending | 80,683 ending | 48,615 ending |
| 1 Ordinary business income | 61,424 | 53,746 | 38,390 |
| 4a / 4b / 4c | 72,000 / 0 / 72,000 | 0 / 9,000 / 9,000 | 0 / 0 / 0 |
| 5 Interest income | 536 | 469 | 335 |
| 12 Section 179 deduction | 9,920 | 8,680 | 6,200 |
| 13 A Cash contributions (60%) | 1,000 | 875 | 625 |
| 14 A Net SE earnings | 133,424 | blank | blank (corporation) |
| 14 C Gross nonfarm income | 305,728 | blank | blank |
| 18 C Nondeductible expenses | 1,288 | 1,127 | 805 |
| 19 Distributions | F 52,000 | A 41,000 | A 30,000 |
| 20 A Investment income | 536 | 469 | 335 |
| 20 Z* Statement A | QBI 61,424; sec. 179 (9,920); W-2 wages 95,368; UBIA 165,040 | QBI 53,746; sec. 179 (8,680); W-2 wages 83,447; UBIA 144,410 | QBI 38,390; sec. 179 (6,200); W-2 wages 59,605; UBIA 103,150 |

Capital percentages follow the liquidation clause (ending capital ÷ total capital, to four decimals). The ending figures round to 99.9999%; the 0.0001 residual went to Daniel so the column totals 100%.

## Validation summary

- Page 1: 1c, 3, 8, 16c, 22, 23 recomputed
- Every K-1 box sums to its Schedule K line (box 1: 61,424 + 53,746 + 38,390 = 153,560)
- Worksheet line 5 = 133,424 = Ava's box 14 A
- Analysis line 1 (208,600) = M-1 line 9 = sum of line 2 entries
- Schedule L balances at both dates; line 14(d) = item F
- M-2 line 1 = sum of beginning item L; line 9 = sum of ending item L = Schedule L line 21
- Schedule B-2 line 3 = 6 (≤ 100); no ineligible partner; return filed on time
- Sanity: no partner payments on line 9; section 179 and contributions only on Schedule K; Daniel's guaranteed payment kept out of box 14

## Filing

E-file through an authorized e-file provider (mandatory: 10 or more returns in calendar 2025). Ava signs Form 8879-PE. Item C on each K-1: "e-file". Due March 16, 2026. Attach Form 1125-A, Form 4562, line 21 statement, Schedule B-2, Statement A, and the K-3 notice; send the 30-day election-out notice to all three partners.

## Why each non-obvious choice

**Why is Daniel's $9,000 not self-employment income?** It is a guaranteed payment for use of capital to a limited partner, so it goes on worksheet line 4b and is excluded from line 4c.

**Why is Ridgeway's box 14 blank?** Box 14 is not completed for a corporation partner, including an S corporation.

**Why is M-2 line 7 $84,220?** Analysis line 1 contains the $81,000 of guaranteed payments, which are not part of the partners' tax-basis capital, and it does not subtract the $3,220 of nondeductible meals, which do reduce capital. Line 7 removes both.

**Why code F for Ava but code A for Daniel and Ridgeway?** Ava performs services, receives income allocations, and took her draw as a distribution: code F. The limited partners perform no services: code A.

**Why can this partnership elect out?** All three partners are eligible types (two individuals and an S corporation) for the whole year, the count including Ridgeway's three shareholders is 6, and the return is timely.
