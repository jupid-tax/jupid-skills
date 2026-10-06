# Example: Licensed Family Daycare, Started Mid-Year, Owner, First-Year Depreciation

A daycare that uses rooms regularly but not exclusively, began in March 2025 (part-year: line 5 is prorated, expenses cover only the business period), and an owned home first used for business in 2025 (month percentage and Form 4562 line 19j). Tax year 2025 (filed in 2026) on the 2025 Form 8829. All math checked in Python; percentages to two decimals, line 6 to four decimals, dollars to whole dollars.

## The filer

- **Name**: Lucía Ferreira, sole proprietor, licensed family child care home (state license issued February 2025, in effect all year)
- **Home**: owned, 2,080 sq ft, bought in 2016
- **Daycare area**: living room, playroom, nap room, kitchen and a half bath: 1,245 sq ft, used for daycare every operating day; the family uses the same rooms evenings and weekends
- **Opened**: Monday, March 3, 2025; open through December 31
- **Schedule C line 29**: $38,615 (food for the children and daycare liability insurance are already on Schedule C, not on Form 8829)
- **Standard deduction** filer
- No prior Form 8829

## Questions asked and answers

| Question | Answer | Consequence |
|---|---|---|
| License, certification, or registration status? | Licensed, in effect | Daycare exception to exclusive use applies |
| Any room used only for daycare? | No | Part I lines 1–7 (no special three-step computation) |
| Hours and days? | 11 hours a day on 208 weekdays; 6 hours on 9 Saturdays | Line 4 = 2,288 + 54 = 2,342 |
| When did daycare start? | March 3, 2025 | Line 5 = 24 × days available, not 8,760 |
| Expense amounts for which period? | Gave amounts for March 3–December 31 only | Part-year rule satisfied |
| Purchase price, improvements, FMV, land? | See below | Part III |

Days available: March 3–31 (29) + April (30) + May (31) + June (30) + July (31) + August (31) + September (30) + October (31) + November (30) + December (31) = 304. Line 5 = 304 × 24 = 7,296.

## Expenses for March 3–December 31, 2025

| Expense | Amount | Column |
|---|---|---|
| Mortgage interest (acquisition debt) | $9,684 | Line 16(b) (standard deduction) |
| Real estate taxes | $3,217 | Line 17(b) (standard deduction) |
| Homeowner's insurance (portion for the period) | $1,358 | Line 18(b) |
| Repainting the playroom (daycare area, not exclusive) | $624 × line 6 (0.3210) = $200 | Line 20(a) |
| Plumbing repair (whole home) | $380 | Line 20(b) |
| Utilities | $2,946 | Line 21(b) |
| Pest control (whole home) | $290 | Line 22(b) |

## Home basis facts

| Item | Amount |
|---|---|
| Purchase price 2016 | $318,400 |
| Improvements before March 2025 (roof 2020) | $12,600 |
| Adjusted basis including land | $331,000 |
| FMV in March 2025 | $455,000 |
| Land (cost basis, below March 2025 land FMV) | $74,900 |

## Completed Form 8829 (2025)

```
Part I
 1  Area used regularly for daycare                            1,245
 2  Total area of home                                         2,080
 3  Line 1 ÷ line 2                                            59.86%
 4  Days used × hours per day                                  2,342 hr.
 5  24 × 304 days available (started March 3)                  7,296 hr.
 6  Line 4 ÷ line 5                                            .3210
 7  Business percentage (line 6 × line 3)                      19.22%

Part II                                       (a) Direct   (b) Indirect
 8  Schedule C line 29 ± home-use gains/losses                 $38,615
 9  Casualty losses                            $0           $0
10  Deductible mortgage interest               $0           $0
11  Real estate taxes                          $0           $0
12  Add lines 9–11                             $0           $0
13  Line 12(b) × line 7                                        $0
14  Line 12(a) + line 13                                       $0
15  Line 8 − line 14                                           $38,615
16  Excess mortgage interest                   $0           $9,684
17  Excess real estate taxes                   $0           $3,217
18  Insurance                                  $0           $1,358
19  Rent                                       $0           $0
20  Repairs and maintenance                    $200         $380
21  Utilities                                  $0           $2,946
22  Other expenses (pest control)              $0           $290
23  Add lines 16–22                            $200         $17,875
24  Line 23(b) × line 7                                        $3,436
25  Prior-year operating carryover                             $0
26  Line 23(a) + line 24 + line 25                             $3,636
27  Smaller of line 15 or line 26                              $3,636
28  Line 15 − line 27                                          $34,979
29  Excess casualty losses                                     $0
30  Depreciation (line 42)                                     $1,001
31  Prior-year excess casualty/depreciation carryover          $0
32  Add lines 29–31                                            $1,001
33  Smaller of line 28 or line 32                              $1,001
34  Add lines 14, 27, 33                                       $4,637
35  Casualty loss portion → Form 4684                          $0
36  Allowable expenses → Schedule C line 30                    $4,637

Part III
37  Smaller of adjusted basis ($331,000) or FMV ($455,000)     $331,000
38  Land                                                       $74,900
39  Building basis                                             $256,100
40  Business basis (line 39 × 19.22%)                          $49,222
41  Depreciation percentage (first used March 2025)            2.033%
42  Depreciation allowable                                     $1,001

Part IV
43  Operating expense carryover to 2026                        $0
44  Excess casualty/depreciation carryover to 2026             $0
```

Arithmetic: 1,245 ÷ 2,080 = 0.598558 → 59.86%. 2,342 ÷ 7,296 = 0.320998 → .3210. Line 7 = 0.3210 × 59.86% = 19.215% → 19.22%. Line 20(a) = $624 × 0.3210 = $200.30 → $200. Line 23(b) = $9,684 + $3,217 + $1,358 + $380 + $2,946 + $290 = $17,875. Line 24 = $17,875 × 19.22% = $3,435.58 → $3,436. Line 40 = $256,100 × 19.22% = $49,222.42 → $49,222. Line 42 = $49,222 × 2.033% = $1,000.68 → $1,001.

## Form 4562 (first business use in 2025)

```
Line 19j  Nonresidential real property
  (b) Month and year placed in service     03/2025
  (c) Basis for depreciation               $49,222   (= Form 8829 line 40)
  (d) Recovery period                      39 yrs.
  (e) Convention                           MM
  (f) Method                               S/L
  (g) Depreciation deduction               $1,001    (= Form 8829 line 42)
```

Not included on Schedule C line 13; it reaches Schedule C only through line 30. Hand the row to the form-4562 skill.

## Notes in the draft

- The simplified method could not exceed $1,500 (300 sq ft × $5), and for a part-time daycare area the rate would also be reduced by the time fraction and the area averaged by month; $1,500 < $4,637, so the comparison table states the cap rather than computing the exact simplified figure.
- Mortgage interest and real estate taxes went on lines 16 and 17 because Lucía takes the standard deduction; the remaining 80.78% of them is not deductible for her this year.
- Food and the daycare's own liability insurance stay on Schedule C. The Pub. 587 standard meal and snack rates are an option for eligible children; ask before using them.
- Sale sentence included: depreciation claimed after May 6, 1997 is not excludable under §121 when the home is sold.

## Validation

- License status confirmed; daycare exception applies ✔
- Line 5 prorated (24 × 304), not 8,760 ✔; line 6 = 2,342 ÷ 7,296 ✔; line 7 = line 6 × line 3 ✔
- Direct expense multiplied by line 6 before entry in column (a) ✔
- Expenses limited to March 3–December 31 ✔
- Line 27 ≤ line 15 ✔; line 33 ≤ line 28 ✔; line 36 = $3,636 + $1,001 = $4,637 ✔
- Line 41 = March 2025 percentage 2.033% ✔; Form 4562 line 19j filled; Schedule C line 13 excludes it ✔

## Sources cited in this draft

- 2025 Form 8829 (Created 10/2/25); 2025 Instructions for Form 8829 (Mar 4, 2026): Daycare Facilities; Line 4; Line 5; Columns (a) and (b); Lines 16, 17; Line 41; Line 42 (Form 4562 line 19j)
- Pub. 587 (2025): Daycare Facility (Examples 1 and 3), Part-year use, Table 2 (39-year percentages), Meals
- 2025 Form 4562, line 19j
- IRC §280A(c)(4)
