# Example: Renter, Freelance Consultant, Full-Year Office

A renter with one dedicated room, no depreciation, no income limit pressure. The pattern for most renters. Tax year 2025 (filed in 2026) on the 2025 Form 8829. All math checked in Python; percentages rounded to two decimals, dollars to whole dollars.

## The filer

- **Name**: Nadia Karim, sole proprietor, UX research consulting (Schedule C)
- **Home**: rented apartment, 1,140 sq ft; rent $2,385 a month all of 2025
- **Office**: second bedroom, 12 ft × 14 ft = 168 sq ft, desk, shelves, a printer; nothing else in the room
- **Use**: every workday; client calls and all billing and bookkeeping happen there; no other office
- **Prior Form 8829**: none (used the simplified method in 2024; no carryovers ever)
- **Schedule C line 29** (tentative profit before line 30): $71,486

## Questions asked and answers

| Question | Answer | Consequence |
|---|---|---|
| Does anyone use the room for anything personal? | No. Guests sleep on the living room sofa bed | Exclusive use met |
| Where do you do billing, scheduling, bookkeeping? | Only in that room | Principal place of business (admin test, no other fixed location) |
| Employee of anyone? | No | Form 8829 allowed |
| Any other business location? | No; client workshops happen at client offices | Line 8 = Schedule C line 29; no allocation |
| Itemize or standard deduction? | Standard deduction | Irrelevant here: no mortgage or real estate taxes |
| Expenses that benefit only the office? | Repainted the office in March, $412 | Line 20, column (a) |
| Renter's insurance, utilities? | Insurance $264; electric $1,317; gas $486 | Lines 18 and 21, column (b) |
| Internet? | Handled separately on Schedule C | Not on Form 8829 in this draft; confirm it is not also in utilities |

## Completed Form 8829 (2025)

```
Part I
 1  Area used regularly and exclusively for business           168
 2  Total area of home                                         1,140
 3  Line 1 ÷ line 2                                            14.74%
 4  Daycare hours                                              N/A
 5  Daycare hours available                                    N/A
 6  Line 4 ÷ line 5                                            N/A
 7  Business percentage                                        14.74%

Part II                                       (a) Direct   (b) Indirect
 8  Schedule C line 29 ± home-use gains/losses                 $71,486
 9  Casualty losses                            $0           $0
10  Deductible mortgage interest               $0           $0
11  Real estate taxes                          $0           $0
12  Add lines 9–11                             $0           $0
13  Line 12(b) × line 7                                        $0
14  Line 12(a) + line 13                                       $0
15  Line 8 − line 14                                           $71,486
16  Excess mortgage interest                   $0           $0
17  Excess real estate taxes                   $0           $0
18  Insurance                                  $0           $264
19  Rent                                       $0           $28,620
20  Repairs and maintenance                    $412         $0
21  Utilities                                  $0           $1,803
22  Other expenses                             $0           $0
23  Add lines 16–22                            $412         $30,687
24  Line 23(b) × line 7                                        $4,523
25  Prior-year operating carryover                             $0
26  Line 23(a) + line 24 + line 25                             $4,935
27  Smaller of line 15 or line 26                              $4,935
28  Line 15 − line 27                                          $66,551
29  Excess casualty losses                                     $0
30  Depreciation (line 42)                                     $0
31  Prior-year excess casualty/depreciation carryover          $0
32  Add lines 29–31                                            $0
33  Smaller of line 28 or line 32                              $0
34  Add lines 14, 27, 33                                       $4,935
35  Casualty loss portion → Form 4684                          $0
36  Allowable expenses → Schedule C line 30                    $4,935

Part III  (renter: not applicable)
37–42                                                          N/A

Part IV
43  Operating expense carryover to 2026                        $0
44  Excess casualty/depreciation carryover to 2026             $0
```

Arithmetic: 168 ÷ 1,140 = 0.147368 → 14.74%. Rent $2,385 × 12 = $28,620. Utilities $1,317 + $486 = $1,803. Line 23(b) = $264 + $28,620 + $1,803 = $30,687. Line 24 = $30,687 × 14.74% = $4,523.26 → $4,523. Line 26 = $412 + $4,523 = $4,935.

## Method comparison shown to the user

| | Simplified | Form 8829 |
|---|---|---|
| Computation | 168 sq ft × $5 | Line 36 |
| Schedule C line 30 | $840 | $4,935 |
| Schedule C line 31 | $70,646 | $66,551 |

Nadia chose Form 8829. No depreciation is involved, so there is no sale consequence for a renter.

## Validation

- Line 3 = 168 ÷ 1,140 ✔; line 7 = line 3 (no daycare) ✔
- Line 12–14 zero (no Tier 1 items) ✔; line 15 = line 8 ✔
- Line 23 columns sum lines 16–22 ✔; line 24 = $30,687 × 14.74% ✔
- Line 27 ≤ line 15 ✔; line 33 = 0 ✔; line 36 = line 34 − line 35 ✔
- Lines 43/44 zero, so nothing to record for 2026 ✔
- Sanity: rent dominates column (b), as expected for a renter; the direct-expense painting is in column (a), not multiplied twice ✔

## Sources cited in this draft

- 2025 Form 8829 (Created 10/2/25); 2025 Instructions for Form 8829 (Mar 4, 2026): Lines 1 and 2, Columns (a) and (b), Line 19
- Pub. 587 (2025): Exclusive Use, Principal Place of Business, Rent, Utilities and services
- 2025 Instructions for Schedule C, Line 30 (simplified method, $5 per sq ft, 300 sq ft cap)
- IRC §280A(c)(1)
