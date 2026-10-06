# Example: Former C Corporation With AE&P and a Built-In Gain Sale (2025 Form 1120-S, boundary flags)

A surveying firm that was a C corporation until December 31, 2022 sold a piece of equipment it held on the conversion date. Shows how the agent drafts everything it can, runs the entity-level tax screens, computes the screen arithmetic, and stops lines 23a–23c (and everything that depends on them) at "PENDING — CPA". It does not compute the built-in gains tax. Figures were checked in Python before writing; amounts are whole dollars.

---

## Scenario

- **Corporation:** Ridgeline Surveying, Inc., a Washington corporation, EIN 91-•••3308; C corporation 2011–2022; S election effective January 1, 2023
- **Activity:** land surveying; code 541370 (Surveying & Mapping (except Geophysical) Services)
- **Shareholders (all year):** Glen Arvidson, president, 600 of 1,000 shares; Ana Arvidson, vice president, 400 shares
- **Method:** accrual; no inventory; never used LIFO
- **Carryover from C years:** accumulated earnings and profits (AE&P) of $41,300 on Schedule M-2, column (c)
- **Conversion appraisal (January 1, 2023):** net unrealized built-in gain (NUBIG) $57,900; no built-in gain recognized in 2023 or 2024

## Questions the agent asked, and the answers

| Question | Answer |
|---|---|
| "Was the corporation ever a C corporation?" | Yes, through December 31, 2022 |
| "Did it sell or dispose of any asset this year that it held on January 1, 2023? FMV and adjusted basis on that date?" | Yes: a robotic total station. FMV $18,500 and adjusted basis $6,200 on January 1, 2023. Original cost $41,900. Sold March 2025 for $16,750; adjusted basis at sale $2,480, so the whole $14,270 gain is §1245 depreciation recapture (ordinary) |
| "What is the net unrealized built-in gain from the conversion, and how much was recognized in prior years?" | $57,900 per the 2023 appraisal; $0 recognized in 2023–2024 |
| "Does the corporation have accumulated E&P from C years? Balance?" | Yes, $41,300 |
| "Passive investment income this year (interest, dividends, rents, royalties, annuities)?" | Interest $3,906; dividends $1,214 (all qualified) |
| "Officer wages and health premiums?" | Glen box 1 $129,268 (includes $11,268 premiums), box 5 $118,000; Ana box 1 and box 5 $84,500 |
| "Beginning AAA?" | $74,615 |
| "Distributions?" | $68,000, paid 60/40 ($40,800 Glen, $27,200 Ana) on the same dates |
| "Any LIFO, investment credit recapture, or prior built-in gain carryforwards?" | None known |

---

## What the agent computed

### Page 1 (provisional until line 23b is final)

```
1a Gross receipts or sales                       642,815
1b Returns and allowances                              0
1c Balance                                       642,815
2  Cost of goods sold                                  0
3  Gross profit                                  642,815
4  Net gain from Form 4797, Part II, line 17      14,270   (16,750 − 2,480; ordinary §1245 recapture)
5  Other income                                        0
6  Total income                                  657,085

7  Compensation of officers (Form 1125-E)        213,768   (Glen 129,268 + Ana 84,500)
8  Salaries and wages (field crew)               196,430
9  Repairs and maintenance                         7,812
10 Bad debts                                           0
11 Rents                                          29,160
12 Taxes and licenses (PROVISIONAL)               36,261
13 Interest (equipment loan)                       2,945
14 Depreciation                                   21,604
15 Depletion                                           0
16 Advertising                                     3,180
17 Pension, profit-sharing, etc., plans                0
18 Employee benefit programs (crew health)        22,416
19 Energy efficient commercial buildings               0
20 Other deductions (statement)                   62,984
21 Total deductions (PROVISIONAL)                596,560
22 Ordinary business income (PROVISIONAL)         60,525
```

Line 12 = employer social security and Medicare $30,518 (7.65% × $398,930 box 5 wages) + FUTA $294 + state unemployment $4,107 + licenses $1,342 = $36,261, before any built-in gains tax. Line 20 = vehicles $18,733 + insurance $14,092 + software $6,155 + professional fees $9,600 + supplies $8,474 + meals $612 (50% of $1,224) + utilities and phone $5,318 = $62,984.

Total receipts (Form 1125-E and question 11): $642,815 + $14,270 + $3,906 + $1,214 = $662,205. Question 11 is "No"; Form 1125-E is required.

### Screen 1 — excess net passive income tax (line 23a)

```
Worksheet line 1  Gross receipts (§1362(d)(3)(B)): at least 642,815 (line 1a alone)
Worksheet line 2  Passive investment income: 3,906 + 1,214 = 5,120
Worksheet line 3  Line 1 × 25%: at least 160,704 (642,815 × 25% = 160,703.75)
Line 2 is less than line 3 → stop. No excess net passive income tax for 2025.
```

The exact gross receipts figure (how the equipment sale counts under §1362(d)(3)(B)) does not change the answer, because line 1a alone already puts the 25% threshold far above $5,120. Record: "AE&P exists; passive income test passed for 2025; re-test every year while AE&P remains."

### Screen 2 — built-in gains tax (line 23b): FAILED → stop

- The total station was held on January 1, 2023 and sold in March 2025, inside the 5-year recognition period that began January 1, 2023 (Instructions for Schedule D (Form 1120-S), Part III).
- Built-in gain on the conversion date: $18,500 − $6,200 = $12,300. Gain recognized on the sale: $14,270. Recognized built-in gain for this asset is limited to the $12,300 built-in at conversion.
- Schedule B, item 8: $57,900 − $0 = **$57,900**.
- Upper bound for information only: 21% × $12,300 = $2,583 (Schedule D (Form 1120-S), line 21 rate), before the line 17 taxable-income limit, the line 18 smallest-of test, any §1374(b)(2) deduction, and line 22 credit carryforwards. **Not entered on the return.**

### Screen 3 — LIFO recapture: not applicable (never used LIFO).

---

## What the agent marked PENDING — CPA, and why

| Line | Status | Reason |
|---|---|---|
| 23a | 0 (screen passed) | ENPI test passed; no LIFO |
| 23b | PENDING — CPA | Built-in gains tax requires Schedule D (Form 1120-S), Part III, lines 16–23, including a taxable-income computation (line 17) |
| 23c | PENDING — CPA | Depends on 23b |
| 12, 21, 22 | PROVISIONAL | The part of the built-in gains tax allocable to ordinary income is deductible on line 12 (2025 Instr., line 12); this gain is ordinary §1245 recapture |
| Schedule K line 1, line 18; M-2; every K-1 box 1 | PROVISIONAL | Follow line 22 |
| 24a / 25 | PENDING — CPA | Estimated tax was required if the entity-level taxes are $500 or more (Instr., Estimated Tax Payments); the upper bound is $2,583, so ask whether any 2025 estimates were paid and expect Form 2220 |

---

## Draft Schedule K, M-2 and K-1s (provisional)

```
Schedule K: 1 = 60,525 (prov.)  4 = 3,906  5a = 1,214  5b = 1,214  16c = 612  16d = 68,000
            17a = 5,120  17c = 0  17d V* STMT  18 = 65,645 (prov.)
```

Schedule M-2 (provisional):

```
                         (a) AAA     (c) AE&P
1 Beginning               74,615      41,300
2 Ordinary income         60,525
3 Other additions          5,120              (interest 3,906 + dividends 1,214)
5 Other reductions          (612)
6 Combine                139,648      41,300
7 Distributions           68,000           0
8 Ending                  71,648      41,300
```

Distributions of $68,000 are within the AAA, so no part is a dividend from AE&P: Schedule K line 17c is $0 and no Form 1099-DIV is needed.

| K-1 box | Glen (60%) | Ana (40%) |
|---|---|---|
| 1 Ordinary business income (prov.) | 36,315 | 24,210 |
| 4 Interest | 2,344 | 1,562 |
| 5a / 5b Dividends | 728 / 728 | 486 / 486 |
| 16 C Nondeductible expenses | 367 | 245 |
| 16 D Distributions | 40,800 | 27,200 |
| 17 A Investment income | 3,072 | 2,048 |

(Interest and dividends split $2,343.6/$1,562.4 and $728.4/$485.6 before rounding; each pair sums to the Schedule K total.)

---

## Validation summary

- **Math:** 1c, 3, 6, 21, 22 computed; K line 18 = 60,525 + 3,906 + 1,214 = 65,645; M-2 line 6 = 74,615 + 60,525 + 5,120 − 612 = 139,648; line 8 = 71,648; K-1s sum to Schedule K.
- **Boundary flags (open):** built-in gains tax on the 2025 sale (lines 23b/23c; Schedule D (Form 1120-S), Part III); estimated tax for the entity-level tax (Form 2220); AE&P present (re-run the passive income test every year; three consecutive failing years would terminate the election under §1362(d)(3)).
- **Status:** draft not ready to file. Hand to a CPA with the conversion appraisal, the asset-level built-in gain schedule, and this draft.

## Sources

2025 Form 1120-S and Instructions (Schedule B item 8; lines 4, 12, 22, 23a–23c; Excess Net Passive Income Tax Worksheet; Estimated Tax Payments; Schedule M-2 columns (a) and (c); Distributions); 2025 Instructions for Schedule D (Form 1120-S), Part III; Form 1125-E; IRC §§1362(d)(3), 1366(f), 1368, 1374, 1375.
