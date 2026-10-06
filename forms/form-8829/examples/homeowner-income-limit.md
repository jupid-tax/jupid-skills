# Example: Homeowner Who Itemizes, Weak Year, Income Limit and Carryovers

An owner-occupied home, itemized deductions with the Line 11 Worksheet, prior-year carryovers coming in, and the gross income limit cutting off depreciation. The pattern for owners in a low-profit year. Tax year 2025 (filed in 2026) on the 2025 Form 8829. All math checked in Python; percentages rounded to two decimals, dollars to whole dollars.

## The filer

- **Name**: Hannah Brecht, single, freelance technical writer (Schedule C)
- **Home**: owned house, 2,240 sq ft, bought in 2017
- **Office**: converted back bedroom, 252 sq ft, used only for writing and client calls since September 2021
- **2025**: lost her largest client in February; Schedule C line 29 (tentative profit) = **$3,947**
- **Itemizes** on Schedule A (mortgage interest and state taxes exceed her standard deduction)
- **2024 Form 8829**: line 43 = $312, line 44 = $517

## Facts gathered

| Item | Amount | Source the user gave |
|---|---|---|
| Purchase price 2017 | $386,500 | Closing statement |
| Improvements before Sept 2021 (new windows 2019) | $18,700 | Invoices |
| FMV in Sept 2021 | $512,000 | Appraisal for a 2021 refinance |
| Land: assessor's land value at purchase (lower than 2021 land FMV) | $97,300 | County assessment |
| Mortgage interest 2025 (Form 1098; acquisition debt under the Pub. 936 limit) | $14,862 | Form 1098 |
| Real estate taxes paid on the home 2025 | $7,420 | County receipts |
| State income tax (personal) | $9,850 | State estimated payments and prior-year balance due |
| Personal property tax (car) | $310 | DMV |
| Homeowner's insurance (2025 coverage) | $1,986 | Policy |
| Furnace repair (whole home) | $642 | Invoice |
| Utilities (electric, gas, water, trash) | $3,418 | Bills |
| Alarm monitoring (whole home) | $396 | Contract |
| Other business income locations | None | |
| Casualty losses | None | |

## Line 11 Worksheet (total SALT > $10,000, so Step 2 applies)

```
1   State and local income taxes (personal)                    $9,850
2   Real estate taxes on the home with the office              $7,420
3   Other personal real estate taxes                           $0
4   Personal property taxes                                    $310
5   Add lines 1–4                                              $17,580
6   Line 2 × Form 8829 line 7 (11.25%)                         $835
7a  Line 5 − line 6                                            $16,745
7b  Line 5 ≤ $10,000?                                          No
7c  Line 7a ≥ $40,000?                                         No
7d  MAGI ≤ $500,000 with $40,000 on line 8?                    Yes (MAGI well under)
8   Overall SALT limit                                         $40,000
9   Line 8 − line 7a                                           $23,255
10  Smaller of line 6 or line 9 → Form 8829 line 11, col (a)   $835
11  Line 6 − line 10 → Form 8829 line 17, col (a)              $0
```

## Completed Form 8829 (2025)

```
Part I
 1  Area used regularly and exclusively for business           252
 2  Total area of home                                         2,240
 3  Line 1 ÷ line 2                                            11.25%
 4–6 Daycare                                                   N/A
 7  Business percentage                                        11.25%

Part II                                       (a) Direct   (b) Indirect
 8  Schedule C line 29 ± home-use gains/losses                 $3,947
 9  Casualty losses                            $0           $0
10  Deductible mortgage interest               $0           $14,862
11  Real estate taxes (Line 11 Worksheet)      $835         $0
12  Add lines 9–11                             $835         $14,862
13  Line 12(b) × line 7                                        $1,672
14  Line 12(a) + line 13                                       $2,507
15  Line 8 − line 14                                           $1,440
16  Excess mortgage interest                   $0           $0
17  Excess real estate taxes                   $0           $0
18  Insurance                                  $0           $1,986
19  Rent                                       $0           $0
20  Repairs and maintenance                    $0           $642
21  Utilities                                  $0           $3,418
22  Other expenses (alarm monitoring)          $0           $396
23  Add lines 16–22                            $0           $6,442
24  Line 23(b) × line 7                                        $725
25  Prior-year operating carryover (2024 line 43)              $312
26  Line 23(a) + line 24 + line 25                             $1,037
27  Smaller of line 15 or line 26                              $1,037
28  Line 15 − line 27                                          $403
29  Excess casualty losses                                     $0
30  Depreciation (line 42)                                     $888
31  Prior-year excess casualty/depreciation (2024 line 44)     $517
32  Add lines 29–31                                            $1,405
33  Smaller of line 28 or line 32                              $403
34  Add lines 14, 27, 33                                       $3,947
35  Casualty loss portion → Form 4684                          $0
36  Allowable expenses → Schedule C line 30                    $3,947

Part III
37  Smaller of adjusted basis ($405,200) or FMV ($512,000)     $405,200
38  Land                                                       $97,300
39  Building basis                                             $307,900
40  Business basis (line 39 × 11.25%)                          $34,639
41  Depreciation percentage (first used Sept 2021)             2.564%
42  Depreciation allowable (line 40 × line 41)                 $888

Part IV
43  Operating expense carryover to 2026 (1,037 − 1,037)        $0
44  Excess casualty/depreciation carryover to 2026 (1,405 − 403) $1,002
```

Arithmetic: 252 ÷ 2,240 = 0.1125. Line 13 = $14,862 × 11.25% = $1,671.98 → $1,672. Line 23(b) = $1,986 + $642 + $3,418 + $396 = $6,442; line 24 = $724.73 → $725. Line 37 = $386,500 + $18,700 = $405,200 (below FMV). Line 40 = $307,900 × 11.25% = $34,638.75 → $34,639. Line 42 = $34,639 × 2.564% = $888.14 → $888.

## Reading the result

- Schedule C line 30 = $3,947, so Schedule C line 31 = $0. Tiers 2 and 3 were capped at line 15 ($1,440); they did not create a loss.
- Order of absorption: Tier 1 ($2,507) first, then all operating expenses including the 2024 carryover ($1,037), then only $403 of the $1,405 depreciation pool. $1,002 carries to 2026 line 31.
- Schedule A gets the personal remainder: mortgage interest $14,862 − $1,672 = $13,190; real estate taxes on line 5b $7,420 − $835 = $6,585. Hand these to the schedule-a skill.
- No Form 4562: first business use was 2021 and no improvements were placed in service in 2025.
- The $1,002 depreciation carryover is recorded for 2026 line 31. How depreciation that is carried over (and possibly never used) affects basis at a later sale is not answered by the form instructions; the draft flags it for the CPA. The general sale sentence (post-May 6, 1997 depreciation is not excludable under §121) is included.

## Method comparison shown to the user

| | Simplified | Form 8829 |
|---|---|---|
| Worksheet line 1 (gross income limitation) | $3,947 | n/a |
| 252 sq ft × $5 | $1,260 | n/a |
| Schedule C line 30 | $1,260 | $3,947 |
| Business share of interest and taxes ($2,507) | Stays on Schedule A | On Schedule C |
| 2024 carryovers ($312, $517) | Frozen (Simplified Method Worksheet lines 6a, 6b) | Partly used; $1,002 carries |

Hannah's draft presents both and leaves the choice to her and her CPA; the agent does not pick.

## Validation

- Line 7 = 252 ÷ 2,240 ✔
- Line 11 Worksheet routed to column (a) because Step 1 failed (SALT $17,580 > $10,000) ✔
- Line 15 = $3,947 − $2,507 = $1,440 ✔; line 27 ≤ line 15 ✔; line 28 = $403 ✔; line 33 ≤ line 28 ✔
- Line 34 = $2,507 + $1,037 + $403 = $3,947 = line 8 (the limit binds exactly) ✔
- Line 43 = $0 and line 44 = $1,002 recorded for 2026 lines 25 and 31 ✔
- Line 37 ≤ FMV, land excluded ✔; 2.564% for pre-2025 first use ✔
- No double counting on Schedule A ✔

## Sources cited in this draft

- 2025 Form 8829 (Created 10/2/25); 2025 Instructions for Form 8829 (Mar 4, 2026): Lines 9, 10, and 11; Line 11 Worksheet; Lines 25, 31; Lines 37 Through 40; Line 41; Part IV
- Pub. 587 (2025): Deduction Limit, Carryover of unallowed expenses, Depreciating Your Home, Sale or Exchange of Your Home
- Pub. 936 (home mortgage interest limits, applied to line 10 Step 1)
- 2025 Instructions for Schedule C, Simplified Method Worksheet (lines 1, 5, 6a, 6b)
- IRC §280A(c)(5); 2025 SALT limit ($40,000 / $10,000 floor) as stated in the 2025 Instructions for Form 8829, What's New
