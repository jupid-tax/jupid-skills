# Example: Late 2025 Return, a Disregarded-Entity Member, and a Lost Question 4 Exception

A three-member LLC that missed the March 16, 2026 deadline without Form 7004 and is preparing its 2025 return in October 2026. The lateness changes three things: Schedule B, question 4 becomes "No" (so page 6 and K-1 item L are required even though the business is small), the partnership cannot elect out of the centralized audit regime (and one member is a disregarded entity anyway), and the section 6698 penalty has to be estimated. All arithmetic was checked in Python.

## The partnership

- **Name**: Lattice Home Inspections LLC, Savannah, Georgia
- **Entity**: domestic LLC, three members, no Form 8832 or Form 2553, so a partnership
- **Tax year**: calendar 2025; due March 16, 2026; no Form 7004 filed
- **Today**: October 6, 2026; the members plan to file on October 20, 2026
- **Accounting method**: cash
- **Members all year** (profit, loss, and capital by the operating agreement, which liquidates by percentage interests):
  - Priya Raman, individual, 40%, managing member, full-time inspector
  - Coastal Ridge Holdings LLC, 30%, a single-member LLC disregarded for tax purposes, owned by Marcus Bell (individual); investor, does no work
  - Theo Vance, individual, 30%, full-time inspector, not a manager

## Questions the agent asked (and the answers)

| Question | Answer |
|----------|--------|
| Was Form 7004 filed by March 16, 2026? | No |
| When were (or will) the K-1s be furnished? | With the return, October 20, 2026 |
| Payments to members? | Priya: $2,500 per month for managing = $30,000 guaranteed payment for services. Draws: Priya $36,000, Coastal Ridge $27,000, Theo $27,500 |
| Self-employment treatment (per their CPA)? | Priya and Theo: general-partner treatment (both work in the business). Marcus Bell (through Coastal Ridge): limited-partner treatment (no services, no management rights) |
| Tax type of each member? | Coastal Ridge Holdings LLC is a single-member LLC with no election; its owner is Marcus Bell |
| Equipment placed in service in 2025? | Thermal camera and drone, $6,900 total, depreciated (no section 179) |
| Liabilities (per CPA)? | Only a business credit card in the LLC's name, no personal guarantee: nonrecourse, shared by profit percentages |
| Returns required during calendar 2025? | Only the 2024 Form 1065 (no employees, no contractors): paper filing is allowed |
| Have the members filed their own 2025 returns? | Priya and Theo filed extended returns on October 15, 2026 using the bookkeeper's draft figures; Marcus has not filed |

## Page 1

```
1a Gross receipts or sales                 214,380
1b Returns and allowances                        0
1c Balance                                 214,380
2  Cost of goods sold                            0
3  Gross profit                            214,380
4-7                                              0
8  Total income                            214,380
9  Salaries and wages                            0
10 Guaranteed payments to partners          30,000
11 Repairs and maintenance                   1,265
12 Bad debts                                     0
13 Rent                                     14,400
14 Taxes and licenses                        3,970
15 Interest                                      0
16a Depreciation (Form 4562)                 7,418
16b                                              0
16c                                          7,418
17-20                                            0
21 Other deductions (statement)             31,457
22 Total deductions                         88,510
23 Ordinary business income                125,870
24-32                                            0
```

Line 21 statement: errors and omissions insurance 9,860; vehicle fuel 8,215; inspection reporting software 4,790; continuing education 2,155; advertising 6,027; meals 410 (50% of 820). Total 31,457.

## Schedule B, question 4

```
(a) Total receipts: 214,380 + Schedule K line 5 140 = 214,520      < 250,000   pass
(b) Total assets at year end: 117,915                               < 1,000,000 pass
(c) K-1s furnished on or before the due date (March 16, 2026)?      no          FAIL
(d) Schedule M-3 required?                                          no          pass
Answer: No
```

Because of (c), Schedules L, M-1, M-2, item F, and item L on every K-1 are required. The K-2/K-3 small partnership exception is also unavailable; the domestic filing exception still applies (no foreign activity; direct partners are two U.S. citizens and a single-member LLC owned by a U.S. citizen), so line 16b is checked and the members get the K-3 notice.

## Schedule B, questions 2 and 33

- 2a: No. Coastal Ridge is a disregarded entity, not a corporation, partnership, or trust. 2b: No. The largest individual holding is 40% (Priya); Marcus holds 30% through his LLC; the members confirmed no family relationships.
- 33: **No**, for two independent reasons: the return is not timely, and a disregarded entity is not an eligible partner (Instructions pp. 30-31). Partnership representative: Priya Raman, U.S. street address and U.S. phone number supplied by Priya.

## Schedule K

```
1   Ordinary business income                125,870
4a  Guaranteed payments, services            30,000
4c  Total guaranteed payments                30,000
5   Interest income                             140
14a Net earnings from self-employment       118,109   (worksheet: 3a 125,870; 3b 37,761 Coastal; 3c 88,109; 4c 30,000)
14c Gross nonfarm income                    159,066   (Priya 103,752 + Theo 55,314)
16b Exception to filing Schedule K-2        checked
18c Nondeductible expenses                      410
19a Cash distributions                       90,500   (F 36,000 + A 27,000 + F 27,500)
20a Investment income                           140
20c Code Z (Statement A)
All other lines                                   0
```

## Analysis of Net Income (Loss) per Return

```
1  125,870 + 30,000 + 140 = 156,010
2b Limited partners (LLC members), (ii) Individual (active):  118,207   Priya 80,404 + Theo 37,803
2b Limited partners (LLC members), (iii) Individual (passive): 37,803   Marcus Bell (through Coastal Ridge)
```

## Schedule L (cash method; books on the tax basis)

```
                                       Beginning      End
1   Cash                                  46,165     81,453
9a  Depreciable assets                    48,650     55,550
9b  Less accumulated depreciation        (12,870)   (20,288)
13  Other assets (deposit)                 1,200      1,200
14  Total assets                          83,145    117,915
17  Other current liabilities (card)       4,310      3,980
21  Partners' capital accounts            78,835    113,935
22  Total liabilities and capital         83,145    117,915
```

Item F = 117,915.

## Schedule M-1 and M-2

```
M-1  1  Net income per books           125,600   (125,870 + 140 − 410)
     3  Guaranteed payments             30,000
     4b Travel and entertainment           410
     5                                 156,010
     8                                       0
     9  Income per return              156,010   = Analysis line 1

M-2  1  Beginning balance               78,835
     2  Contributions                        0
     3  Net income (Analysis line 1)   156,010
     4  Other increases                      0
     5                                 234,845
     6a Cash distributions              90,500
     7  Other decreases                 30,410   (guaranteed payments 30,000; nondeductible meals 410)
     8                                 120,910
     9  Ending balance                 113,935   = Schedule L line 21
```

## Schedule K-1s

| Item / box | Priya Raman | Coastal Ridge Holdings LLC (Marcus Bell) | Theo Vance |
|------------|-------------|------------------------------------------|------------|
| E | Priya's SSN | **Marcus Bell's SSN** (beneficial owner) | Theo's SSN |
| F | Priya, Savannah, GA | **Marcus Bell's** name and address | Theo, Savannah, GA |
| G | LLC member-manager | Other LLC member | Other LLC member |
| H2 | | **Checked: DE TIN = Coastal Ridge's EIN; name Coastal Ridge Holdings LLC** | |
| I1 | Individual | **Individual** (beneficial owner's type) | Individual |
| J (beg and end) | 40% / 40% / 40% | 30% / 30% / 30% | 30% / 30% / 30% |
| K1 nonrecourse (beg / end) | 1,724 / 1,592 | 1,293 / 1,194 | 1,293 / 1,194 |
| L beginning | 31,240 | 24,615 | 22,980 |
| L current year net income | 50,240 | 37,680 | 37,680 |
| L withdrawals and distributions | (36,000) | (27,000) | (27,500) |
| L ending | 45,480 | 35,295 | 33,160 |
| 1 Ordinary business income | 50,348 | 37,761 | 37,761 |
| 4a / 4c | 30,000 / 30,000 | 0 / 0 | 0 / 0 |
| 5 Interest income | 56 | 42 | 42 |
| 14 A Net SE earnings | 80,348 | blank (limited-partner treatment) | 37,761 |
| 14 C Gross nonfarm income | 103,752 | blank | 55,314 |
| 18 C Nondeductible expenses | 164 | 123 | 123 |
| 19 Distributions | F 36,000 | A 27,000 | F 27,500 |
| 20 A Investment income | 56 | 42 | 42 |
| 20 Z* Statement A | QBI 50,348 | QBI 37,761 | QBI 37,761 |

Item L current year net income = share of (125,870 + 140 − 410) = share of 125,600. Ending total 45,480 + 35,295 + 33,160 = 113,935 = M-2 line 9.

Theo's item G box ("Other LLC member") and his box 14 entry (general-partner treatment) are independent: item G reports management status, box 14 follows the self-employment answer the members' CPA gave.

## Penalty estimate (IRC §6698; Instructions p. 7)

```
Due date: March 16, 2026 (no extension)
Planned filing: October 20, 2026 → 7 full months + part of an 8th = 8 months
Persons who were partners at any time in 2025: 3
Penalty: $255 × 3 × 8 = $6,120
If filed on or before October 16, 2026: $255 × 3 × 7 = $5,355
Each additional month: $255 × 3 = $765; cap at 12 months = $9,180
Late K-1s (IRC §6722): up to $340 × 3 = $1,020
```

Had a member sold their interest during 2025, the buyer and the seller would both count, and the multiplier would be 4.

Rev. Proc. 84-35 screen (IRM 20.1.2.4.3.1):

| Criterion | Status |
|-----------|--------|
| 10 or fewer partners | Met (3) |
| Each partner an individual (not a nonresident alien) or a deceased partner's estate | Uncertain: one member is a single-member LLC; refer to CPA |
| All items allocated in the same proportion | Met (no special allocations) |
| Each partner reported their share on a timely filed return | Not met yet: Marcus has not filed |

Conclusion for the user: relief is not presumed on these facts. Do not attach an explanation to the return; if a penalty notice arrives, the CPA can request reasonable-cause relief.

## Filing

Paper is allowed (one return required in calendar 2025). Georgia, total assets under $10 million, no Schedule M-3: Department of the Treasury, Internal Revenue Service Center, Kansas City, MO 64999-0011. E-filing through an authorized provider is also allowed. A Form 7004 filed now would be invalid (it must be filed by the original due date), so do not file one. Signed by a member.

## Validation summary

- Page 1 totals recomputed; every K-1 box sums to Schedule K
- Worksheet line 5 (118,109) = box 14 A total (80,348 + 37,761)
- Analysis line 1 = M-1 line 9 = 156,010; line 2 entries total 156,010
- Schedule L balances; L line 21 = M-2 line 9 = sum of item L = 113,935
- Coastal Ridge K-1 uses Marcus Bell's TIN in item E and the DE's TIN in item H2
- Question 33 "No" with a complete PR designation

## Why each non-obvious choice

**Why is question 4 "No" for a $214,380 business?** Condition (c) requires the K-1s to be furnished by the due date including extensions. Without Form 7004 the due date was March 16, 2026.

**Why can't the members elect out of the audit regime?** The election can be made only on a timely filed return, and a disregarded entity is an ineligible partner. Either reason alone blocks it.

**Why does Coastal Ridge's K-1 show Marcus Bell's SSN?** Item E takes the beneficial owner's TIN for a disregarded-entity partner; the DE's own TIN goes in item H2, and item I1 shows the beneficial owner's entity type.

**Why is the penalty multiplier 3 and the month count 8?** The penalty runs for each month or part of a month, times the number of persons who were partners at any time during the year.
