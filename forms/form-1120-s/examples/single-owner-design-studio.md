# Example: Single-Shareholder Design Studio (2025 Form 1120-S)

One shareholder who is also the only officer, cash method, no inventory, total receipts and assets under $250,000. Shows: officer wages plus more-than-2% shareholder health insurance on line 7, bank interest moved to Schedule K, bonus depreciation on line 14, the question 11 test, the AAA roll-forward that question 11 does not excuse, the K-1, the Statement A W-2 wage figure, and the Form 7203 handoff. All amounts were checked with a Python script before writing; figures are whole dollars.

---

## Scenario

- **Corporation:** Halvorsen Studio, Inc., a Colorado corporation, EIN 84-•••6142, principal office in Denver
- **Incorporated and S election effective:** January 4, 2022 (Form 2553 accepted; the corporation was never a C corporation)
- **Activity:** brand identity and graphic design; code 541400 (Specialized Design Services, including graphic design)
- **Shareholder:** Mara Halvorsen, 1,000 of 1,000 shares all year; president
- **Tax year:** calendar 2025; cash method; books follow the tax return

## Questions the agent asked, and the answers

| Question | Answer |
|---|---|
| "Do you have the IRS letter accepting Form 2553, and what effective date does it show?" | Yes; January 4, 2022 |
| "Was the corporation ever a C corporation or did it acquire assets from one?" | No |
| "Which shareholders are officers, and what W-2 box 1, 3 and 5 amounts did each receive?" | Mara, president. Box 1 $85,428; boxes 3 and 5 $78,000 |
| "Did the corporation pay health insurance for any more-than-2% shareholder, and is it in box 1?" | Yes, $7,428 of premiums, included in box 1, not in boxes 3/5 |
| "Do the four Forms 941 agree?" | Yes, line 5c totals $78,000 |
| "How was the $78,000 decided?" | Board resolution of December 2024 citing her own survey of design-director pay. The agent records this; it does not evaluate it |
| "Was the $312 of interest from customer invoices or from the bank?" | Business savings account |
| "Any asset over your capitalization policy bought this year? Section 179 or not?" | A $3,890 workstation placed in service April 2025; no section 179 election |
| "Distributions: dates and amounts?" | Eight transfers totaling $52,500, all to Mara |
| "Beginning AAA from the 2024 return?" | $18,240 (2024 Schedule M-2, line 8, column (a)) |
| "Any foreign taxes, foreign accounts or foreign entities?" | No |
| "Any payments that required Forms 1099 in 2025?" | No |

---

## Page 1

```
1a Gross receipts or sales                                   187,460
1b Returns and allowances (refunds to two clients)              1,250
1c Balance (1a − 1b)                                          186,210
2  Cost of goods sold                                               0
3  Gross profit (1c − 2)                                      186,210
4  Net gain (loss) from Form 4797                                   0
5  Other income (loss)                                              0
6  Total income (3 + 4 + 5)                                   186,210

7  Compensation of officers (78,000 wages + 7,428 health)      85,428
8  Salaries and wages                                               0
9  Repairs and maintenance                                        640
10 Bad debts                                                        0
11 Rents (studio)                                              14,760
12 Taxes and licenses                                           6,637
13 Interest                                                         0
14 Depreciation (Form 4562; 100% special allowance)             3,890
15 Depletion                                                        0
16 Advertising                                                  2,315
17 Pension, profit-sharing, etc., plans                             0
18 Employee benefit programs                                        0
19 Energy efficient commercial buildings deduction                  0
20 Other deductions (statement)                                11,873
21 Total deductions (7 through 20)                            125,543
22 Ordinary business income (6 − 21)                           60,667

23a Excess net passive income or LIFO recapture tax                 0
23b Tax from Schedule D (Form 1120-S)                               0
23c Add 23a and 23b                                                 0
24a Estimated tax payments                                          0
24b Tax deposited with Form 7004                                    0
24c Form 4136 credit                                                0
24d Elective payment election amount                                0
24z Total payments                                                  0
25 Estimated tax penalty                                            0
26 Amount owed                                                      0
27 Overpayment                                                      0
28a Credited to 2026 estimated tax                                  0
28b Refunded                                                        0
```

**Line 12 detail:** employer social security and Medicare $5,967 (7.65% × $78,000, IRC §3111(a),(b)); FUTA $42 (Form 940); state unemployment $378; state and city license and report fees $250. Total $6,637.

**Line 20 statement:** software subscriptions $4,188; business insurance $1,870; CPA fees $2,400; payroll service $684; meals $673 (50% of $1,346); business share of phone and internet $1,140; supplies $918. Total $11,873.

**Reasoning notes**
- Line 7 includes the $7,428 of premiums because Mara owns more than 2% and is an officer (Instr., lines 7, 8 and 18). Line 18 stays at zero.
- The $312 of savings interest is portfolio income: it goes to Schedule K, line 4, not line 5.
- The workstation is depreciated on line 14 through Form 4562. Had she elected section 179, the amount would go to Schedule K, line 11 instead.
- The nondeductible half of meals ($673) is a Schedule K, line 16c item.
- History screen clean (never a C corporation): lines 23a–23c are zero.

---

## Schedule B (answers)

1 Cash. 2 Graphic design / brand identity design. 3 No. 4a No. 4b No. 5a No. 5b No. 6 No. 7 Not checked. 8 Not applicable (blank). 9 No. 10 No. 11 **Yes** (test below). 12 No. 13 No. 14a No. 15 No. 16 No.

### Question 11 test

```
Line 1a gross receipts                         187,460
Lines 4 + 5                                          0
Schedule K 3a, 4, 5a, 6 (interest)                 312
Schedule K 7, 8a, 9, 10                              0
Form 8825                                            0
Total receipts                                 187,772   < 250,000  Y
Year-end total assets (item F)                  31,406   < 250,000  Y
Question 11                                        Yes
```

Schedules L and M-1 are not required. Total receipts are under $500,000, so Form 1125-E is not required. Schedules K-2 and K-3 are not required (small S corporation filing exception, 2025 K-2/K-3 Instructions). Item F still shows $31,406 (cash; the workstation is fully depreciated on the books).

---

## Schedule K

```
1   Ordinary business income                    60,667
2–3c                                                 0
4   Interest income                                312
5a–10                                                0
11  Section 179 deduction                            0
12a–12e                                              0
13a–13g                                              0
14a / 14b                                   not checked
15a–15f                                              0
16a, 16b                                             0
16c Nondeductible expenses                         673
16d Distributions                               52,500
16e, 16f                                             0
17a Investment income                              312
17b, 17c                                             0
17d Code V*  STMT (Statement A)
18  Income (loss) reconciliation (60,667 + 312)  60,979
```

## Schedule M-2 (completed although question 11 is "Yes")

```
                                   (a) AAA    (b) PTEP  (c) AE&P  (d) OAA
1 Balance at beginning of year      18,240        0         0        0
2 Ordinary income, line 22          60,667
3 Other additions (K line 4)           312                           0
4 Loss from line 22                      0
5 Other reductions (K line 16c)      (673)                           0
6 Combine lines 1–5                 78,546        0         0        0
7 Distributions                     52,500        0         0        0
8 Balance at end of year            26,046        0         0        0
```

---

## Schedule K-1 — Mara Halvorsen

```
A 84-•••6142   B Halvorsen Studio, Inc., Denver, CO   C e-file or "Ogden" if paper   D Shares 1,000 / 1,000
E •••-••-4417  F1 Mara Halvorsen   F2 n/a   F3 Individual
G Current year allocation percentage 100%   H Shares 1,000 / 1,000   I Loans from shareholder 0 / 0
Box 1   Ordinary business income        60,667
Box 4   Interest income                    312
Box 16  C  Nondeductible expenses          673
Box 16  D  Distributions                52,500
Box 17  A  Investment income               312
Box 17  V* STMT (Statement A)
```

**Statement A (one trade or business, not an SSTB as reported by the corporation):** QBI $60,667; W-2 wages $78,000 (unmodified box method: the lesser of box 1 total $85,428 and box 5 total $78,000, Rev. Proc. 2019-11, §5.01); UBIA of qualified property $9,615 (the 2025 workstation $3,890 plus $5,725 of 2023 equipment, per the asset list Mara provided).

**Form 7203 handoff (shareholder level, not part of Form 1120-S):** Mara received a non-dividend distribution, so she generally files Form 7203 with her Form 1040 (Instructions for Form 7203, Who Must File). Illustration from her stated beginning stock basis of $21,740: plus income $60,667 and $312 = $82,719; minus distributions $52,500 = $30,219; minus nondeductible expenses $673 = $29,546. The distribution did not exceed basis. Her K-1 box 1 income is not subject to self-employment tax (Shareholder's Instructions for Schedule K-1 (Form 1120-S)).

---

## Validation summary

- **Math:** 1c, 3, 6, 21, 22, 23c, 24z pass; K line 1 = line 22; K line 18 = 60,667 + 312 = 60,979; M-2 line 6 = 18,240 + 60,667 + 312 − 673 = 78,546; line 8 = 26,046; K-1 = Schedule K (100%).
- **Payroll tie-out:** line 7 $85,428 = W-2 box 1; W-2 box 5 $78,000 = Forms 941 line 5c totals.
- **Sanity:** distributions ($52,500) are below line 22 income and AAA; officer wages present. No warnings.
- **Boundary flags:** none.
- **Open questions:** none.

## Filing notes

- Due March 16, 2026 for the calendar 2025 return (Instr., When To File).
- E-file count for calendar 2025: the 2024 Form 1120-S, four Forms 941, one Form 940 and one Form W-2 = 7 returns, under 10, so paper is permitted (Reg. §301.6037-2(d)(5)). Colorado, any asset size → Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0013.
- Penalty exposure if filed three months late without an extension: 1 shareholder × 3 months × $255 = $765 (§6699; 2025 Instr.).

## Sources

2025 Form 1120-S and Instructions (Income caution; lines 7, 8, 12, 14, 18, 20, 22; Question 11; Schedule M-2; Where To File); 2025 Schedule K-1 (Form 1120-S) and Shareholder's Instructions; 2025 S Corporation Instructions for Schedules K-2 and K-3 (Small S Corporation Filing Exception); Instructions for Form 7203; Rev. Proc. 2019-11; IRC §§1366, 1367, 1368, 3111, 6699; Reg. §301.6037-2.
