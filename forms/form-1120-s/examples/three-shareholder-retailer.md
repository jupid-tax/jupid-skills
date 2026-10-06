# Example: Three-Shareholder Specialty Food Retailer With a Mid-Year Share Sale (2025 Form 1120-S)

Accrual method, inventory, two officer-shareholders and one non-officer shareholder-employee, a share sale on April 30, and total receipts above $500,000. Shows: Form 1125-A and Form 1125-E, the line 7 / line 8 / line 18 split for health insurance, section 179 and charitable contributions moved to Schedule K, Schedules L and M-1 because question 11 is "No", the AAA, day-weighted item G percentages, distributions reported to the actual recipients, and Statement A. Every figure below was recomputed in Python before writing; amounts are whole dollars.

---

## Scenario

- **Corporation:** Copper Kettle Provisions, Inc., an Ohio corporation, EIN 31-•••0587; S corporation since incorporation on June 1, 2016 (never a C corporation)
- **Activity:** online and in-store retail of specialty foods; code 445298 (All Other Specialty Food Retailers; nonstore retailers select by primary product)
- **Method:** accrual; inventory at cost (FIFO)
- **Shares:** 1,000 outstanding all year
  - Dana Okafor, president: 500 shares all year
  - Luis Ferreira, vice president: 300 shares; sold 150 shares to Priya on April 30, 2025
  - Priya Natarajan, fulfillment manager (not an officer): 200 shares; 350 after the purchase
- **Distributions:** $40 per share on March 31 ($40,000) and $60 per share on October 31 ($60,000)

## Questions the agent asked, and the answers

| Question | Answer |
|---|---|
| "Did any shareholder buy, sell, gift or redeem shares during the year? Date and shares?" | Luis sold 150 shares to Priya on April 30, 2025 |
| "Did the corporation and all affected shareholders agree to any closing-of-the-books election?" | No. (Luis kept 150 shares, so §1377(a)(2) is not available; 150 shares is 15% of outstanding stock, below the 20% qualifying-disposition threshold.) |
| "Who are the officers, and what W-2 amounts did each receive?" | Dana: box 1 $105,840 (includes $9,840 health premiums), box 5 $96,000. Luis: box 1 and box 5 $38,500 (no premiums; he is on a spouse's plan) |
| "Is Priya an officer? Her W-2?" | Not an officer. Box 1 $58,212 (includes $6,212 premiums), box 5 $52,000 |
| "Other employees' wages and benefits?" | Three staff: $121,850 wages; group health premiums $14,736 |
| "Do the four Forms 941 agree with W-2 box 5 totals?" | Yes, $308,350 |
| "Section 179 elections this year?" | Yes: a $22,600 packing machine placed in service in August, fully expensed under §179 |
| "Charitable contributions?" | $2,750 cash to a food bank (written acknowledgment on file) |
| "Interest income source?" | $1,083 from a business money-market account (portfolio) |
| "Beginning AAA from the 2024 return?" | $63,418 |
| "Loans to or from shareholders?" | Dana lent the corporation $25,000 in 2023; balance unchanged all year. Interest-free (recorded as an open question for the CPA under §7872) |
| "Foreign activity?" | None |

---

## Cost of goods sold (Form 1125-A summary)

```
Beginning inventory               84,210
Purchases                        612,644
Cost of labor                          0
Other costs (freight-in, packaging) 23,918
Ending inventory                 (91,377)
Cost of goods sold (line 8)      629,395  → Form 1120-S line 2
```

## Page 1

```
1a Gross receipts or sales                    1,386,214
1b Returns and allowances                        18,947
1c Balance                                    1,367,267
2  Cost of goods sold (Form 1125-A)             629,395
3  Gross profit                                 737,872
4  Net gain (loss) from Form 4797                     0
5  Other income (loss)                                0
6  Total income                                 737,872

7  Compensation of officers (Form 1125-E, line 4)  144,340
8  Salaries and wages                           180,062
9  Repairs and maintenance                        3,416
10 Bad debts                                      2,108
11 Rents (warehouse)                             47,520
12 Taxes and licenses                            27,990
13 Interest (line of credit)                      4,672
14 Depreciation (Form 4562; no §179 here)        18,355
15 Depletion                                          0
16 Advertising                                   61,288
17 Pension, profit-sharing, etc., plans               0
18 Employee benefit programs                     14,736
19 Energy efficient commercial buildings deduction    0
20 Other deductions (statement)                 113,096
21 Total deductions                             617,583
22 Ordinary business income                     120,289

23a, 23b, 23c                                         0  (never a C corporation; screen clean)
24a–24z                                               0
25, 26, 27, 28a, 28b                                  0
```

**Line 7 (Form 1125-E):** Dana $105,840 ($96,000 + $9,840 premiums; 100% of time; 50% common stock at year end); Luis $38,500 (40% of time; 15% common stock at year end). Line 2 $144,340; line 3 $0; line 4 $144,340.

**Line 8:** staff $121,850 + Priya $58,212 ($52,000 + $6,212 premiums; more-than-2% shareholder who is not an officer, so her premiums go on line 8, not line 18) = $180,062.

**Line 12:** employer social security and Medicare $23,589 (7.65% × $308,350 box 5 wages); FUTA $252; state unemployment $2,964; licenses and permits $1,185. Total $27,990.

**Line 13:** small business taxpayer (average gross receipts far below $31 million), so no §163(j) limit and no Form 8990; Schedule B, question 10 "No".

**Line 20 statement:** merchant and payment processing $33,842; outbound shipping $41,219; e-commerce software $12,604; insurance $6,918; legal and professional $8,350; meals $1,127 (50% of $2,254); utilities and office $9,036. Total $113,096.

**Moved off page 1:** section 179 $22,600 → Schedule K, line 11; charitable $2,750 → Schedule K, line 12a; interest $1,083 → Schedule K, line 4; nondeductible meals $1,127 → Schedule K, line 16c.

---

## Schedule B highlights

1 Accrual. 2 Specialty food retail / packaged specialty foods. 3 No. 4a/4b No. 9 No. 10 No. **11 No** (total receipts $1,387,297 = line 1a $1,386,214 + K line 4 $1,083). 12 No. 13 No. 14a Yes (Forms 1099-NEC to two freelance product photographers paid in 2025; their fees are in line 16); 14b Yes. 16 No.

Because question 11 is "No", Schedules L and M-1 are required. Total assets are below $10 million, so Schedule M-1 (not M-3). Total receipts are $500,000 or more, so Form 1125-E is attached.

---

## Schedule K

```
1   Ordinary business income                 120,289
4   Interest income                            1,083
11  Section 179 deduction                     22,600
12a Cash charitable contributions              2,750
16c Nondeductible expenses                     1,127
16d Distributions                            100,000
17a Investment income                          1,083
17d Code V* STMT; code AC not needed (no shareholder request)
18  Reconciliation: 120,289 + 1,083 − 22,600 − 2,750 = 96,022
All other lines                                    0
```

## Schedule L (per books)

```
                                   Beginning (b)        End (d)
1   Cash                               58,214            52,560
2a  Trade receivables                  21,906            26,481
3   Inventories                        84,210            91,377
10a Depreciable assets                146,830           169,430
10b Less accumulated depreciation     (61,442)          (81,411)
14  Other assets (deposits)             6,000             6,000
15  Total assets                      255,718           264,437   → item F
16  Accounts payable                   38,615            41,980
17  Notes payable < 1 year (line of credit) 42,000       30,000
18  Other current liabilities          12,733            14,206
19  Loans from shareholders            25,000            25,000   = sum of K-1 item I
22  Capital stock                       1,000             1,000
23  Additional paid-in capital         49,000            49,000
24  Retained earnings                  87,370           103,251
27  Total liabilities and equity      255,718           264,437
```

Book depreciation: $18,355 on existing assets (same as tax) plus $1,614 on the packing machine (7-year straight line, half year: $22,600 ÷ 7 × 0.5). Accumulated depreciation: $61,442 + $18,355 + $1,614 = $81,411. Retained earnings: $87,370 + book net income $115,881 − distributions $100,000 = $103,251.

## Schedule M-1

```
1  Net income per books                       115,881
2  Income on K not on books                         0
3b Travel and entertainment (nondeductible meals) 1,127
4  Add lines 1–3                              117,008
6a Depreciation (tax §179 22,600 − book 1,614)  20,986
7  Add lines 5 and 6                           20,986
8  Income (loss), Schedule K line 18           96,022   ✓ equals K line 18
```

## Schedule M-2

```
                                   (a) AAA
1 Beginning balance                  63,418
2 Ordinary income (line 22)         120,289
3 Other additions (K line 4)          1,083
4 Loss                                    0
5 Other reductions (§179 22,600 + charity 2,750 + nondeductible 1,127)  (26,477)
6 Combine                           158,313
7 Distributions                     100,000
8 Ending balance                     58,313
Columns (b), (c), (d): 0
```

---

## Item G and the K-1 allocation

Days: January 1–April 30 = 120 days (Luis is the shareholder on April 30, the day of the sale); May 1–December 31 = 245 days; total 365.

```
Dana  : 50% × 365 ÷ 365                              = 50.0000%
Luis  : (30% × 120 + 15% × 245) ÷ 365 = 72.75 ÷ 365   = 19.9315%
Priya : (20% × 120 + 35% × 245) ÷ 365 = 109.75 ÷ 365  = 30.0685%
Total                                                  100.0000%
```

Allocated amounts (each rounded to the dollar; a $1 rounding difference on line 1 was assigned to Dana so the K-1s sum to Schedule K):

| Schedule K line → K-1 box | Total | Dana | Luis | Priya |
|---|---|---|---|---|
| 1 → box 1 | 120,289 | 60,145 | 23,975 | 36,169 |
| 4 → box 4 | 1,083 | 541 | 216 | 326 |
| 11 → box 11 | 22,600 | 11,300 | 4,505 | 6,795 |
| 12a → box 12, code A | 2,750 | 1,375 | 548 | 827 |
| 16c → box 16, code C | 1,127 | 563 | 225 | 339 |
| 17a → box 17, code A | 1,083 | 541 | 216 | 326 |
| 16d → box 16, code D (actual receipts) | 100,000 | 50,000 | 21,000 | 29,000 |

Distributions are reported as actually received, not by item G: Luis received $40 × 300 = $12,000 on March 31 and $60 × 150 = $9,000 on October 31; Priya $40 × 200 = $8,000 and $60 × 350 = $21,000. The per-share amount was the same for every share on each date ($40, then $60), so the one-class-of-stock sanity check passes.

Items H and I: Dana 500/500 shares, loan $25,000/$25,000; Luis 300/150, loan 0/0; Priya 200/350, loan 0/0. Item D: 1,000/1,000.

**Statement A (one trade or business, non-SSTB as reported by the corporation):** QBI items by box (box 1 income, box 11 §179 deduction) as allocated above; W-2 wages $308,350 (unmodified box method: lesser of box 1 total $324,402 and box 5 total $308,350, Rev. Proc. 2019-11, §5.01) allocated Dana $154,175, Luis $61,459, Priya $92,716; UBIA of qualified property $158,940 per the fixed-asset register, allocated Dana $79,470, Luis $31,679, Priya $47,791.

**Form 7203 handoff:** all three received non-dividend distributions, so each generally files Form 7203. Each also has a section 179 deduction that their own limits apply to (Form 4562 at shareholder level). Luis sold stock, so his Form 7203 also covers the disposition; his gain on the sale is his own computation from his basis in the 150 shares.

---

## Validation summary

- **Math:** 1c, 3, 6, 21, 22 pass; Form 1125-A line 8 = line 2; Form 1125-E line 4 = line 7; line 20 = statement; K line 18 = 96,022 = M-1 line 8; Schedule L totals balance (255,718 and 264,437) and line 15(d) = item F; M-2 (a) line 6 = 158,313, line 8 = 58,313; item G sums to 100%; each K-1 column sums to Schedule K; box 16D sums to 100,000.
- **Payroll tie-out:** line 7 + line 8 = $324,402 = W-2 box 1 total; box 5 total $308,350 = Forms 941.
- **Sanity:** officer wages present; distributions pro rata per share on each date; §179 and charity off page 1.
- **Boundary flags:** none (never a C corporation; no foreign activity; assets under $10 million).
- **Open questions for the CPA:** interest-free $25,000 shareholder loan from Dana (§7872 below-market loan rules); no other items.

## Filing notes

- Due March 16, 2026; K-1s to all three shareholders by the same date.
- E-file required: during calendar 2025 the corporation was required to file the 2024 Form 1120-S, four Forms 941, Form 940, six Forms W-2 and two Forms 1099-NEC for 2024 (the same six employees and two photographers worked in 2024), 14 returns, which is 10 or more (Reg. §301.6037-2(d)(5)).
- If paper were ever permitted: Ohio, total assets under $10 million, no Schedule M-3 → Kansas City, MO 64999-0013.

## Sources

2025 Form 1120-S and Instructions (lines 2, 7, 8, 12, 13, 14, 18, 20; Question 11; Schedules K, L, M-1, M-2; item G; line 16d); Form 1125-E (Rev. October 2016) and Instructions (Rev. October 2018); IRC §1377(a); Reg. §§1.1377-1(b), 1.1368-1(g)(2), 1.1361-1(l), 301.6037-2; Rev. Proc. 2019-11; Instructions for Form 7203; IRS page "S Corporation Compensation and Medical Insurance Issues".
