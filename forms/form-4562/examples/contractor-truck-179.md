# Example: Contractor Buys $80,000 Truck — §179 vs. MACRS

A complete walkthrough of Form 4562 for a sole-proprietor contractor who bought a heavy-duty pickup for the business. Includes a side-by-side comparison of full §179 expensing vs. 5-year MACRS, with vehicle GVWR mattering.

## The filer

- **Name**: Daniel Reyes
- **Business**: Reyes Plumbing & Heating (sole prop, Schedule C)
- **Tax year**: 2025 (filing in 2026)
- **Other income**: none (full-time sole prop)
- **Net Schedule C profit before §179/depreciation**: $112,000

## The asset

- **Vehicle**: 2025 Ford F-250 SuperDuty crew cab, 8-foot bed
- **Purchase date**: March 15, 2025
- **Placed in service for business**: March 18, 2025
- **Cost**: $80,000 (cash purchase, no trade-in)
- **GVWR**: 11,000 lbs (>6,000 lbs — heavy SUV / pickup category)
- **Bed length**: 8 feet (>6 feet — exempts from heavy-SUV §179 cap; full §179 dollar limit applies)
- **Business use**: 95% (5% personal — driving to grocery store, family weekends)
- **Adjusted basis for depreciation**: $80,000 × 95% = $76,000

Daniel kept a contemporaneous mileage log via the Jupid app. Year 2025 totals: 24,000 total miles, 22,800 business, 1,200 personal, 0 commuting (he goes from home directly to job sites — no fixed business location).

## Why this truck escapes the heavy-SUV §179 cap

The $31,300 heavy-SUV §179 cap (IRC §179(b)(5), Rev. Proc. 2024-40) applies to vehicles >6,000 lbs and ≤14,000 lbs GVWR with cargo bed length ≤6 feet. The F-250 has an 8-foot bed, so it's NOT subject to the SUV cap. It IS still listed property (>50% business use required) and follows the general §179 dollar limit ($1,250,000 for 2025) and §280F caps... but the §280F luxury auto caps don't apply because the F-250 is a truck >6,000 lbs GVWR.

So Daniel can §179 the full $76,000 (the business-use-adjusted basis), subject only to:
- The $1.25M dollar limit (well under)
- His business income limit ($112,000 — covers it)
- The >50% business use test (95% — passes)

## Path A: Full §179 election

Daniel elects §179 on the full $76,000.

### Form 4562 Part I

```
1.  Maximum amount:                              $1,250,000
2.  Total cost of §179 property placed in service:  $76,000
3.  Threshold cost:                              $3,130,000
4.  Reduction in limit:                          $0
5.  Dollar limit (Line 1 − Line 4):              $1,250,000
6.  (a) F-250 truck / (b) $76,000 / (c) $76,000
7.  Listed property §179 (from Line 29):         $0  (truck handled in Part V Line 26 below; see note)
8.  Total elected:                               $76,000
9.  Tentative deduction:                         $76,000
10. Carryover from 2024:                         $0
11. Business income limit:                       $112,000
12. §179 deduction:                              $76,000
13. Carryover to 2026:                           $0
```

### Form 4562 Part V (because vehicle is listed property)

```
24a. Have evidence to support business use:      Yes
24b. Is the evidence written:                    Yes (Jupid app log)

26. Property used >50% in qualified business use:
   (a) Description: 2025 Ford F-250
   (b) Date placed in service: 03/18/2025
   (c) Business %: 95%
   (d) Cost or basis: $80,000
   (e) Basis for depreciation (= b×c): $76,000
   (f) Recovery period: 5 years
   (g) Method/Convention: 200DB / HY
   (h) Depreciation: $0 (fully expensed via §179)
   (i) Elected §179: $76,000

28. Total (Lines 25+26+27, column h) → Line 21:  $0
29. Total §179 (column i, Line 26) → Line 7:     $76,000

Vehicle 1 — F-250 (Section B):
30a. Total business miles:    22,800
30b. Total commuting miles:   0
30c. Total other personal:    1,200
30d. Total miles:             24,000
31. Available for personal use during off-duty hours:  Yes
32. Used primarily by >5%-owner or related person:     Yes (Daniel himself)
33. Another vehicle available for personal use:        Yes (Daniel's wife has a sedan)
```

**Note on Line 7 vs. Line 6**: because the truck is listed property, its §179 election goes through Part V Line 26 column (i), then aggregates on Line 29, then carries to Part I Line 7. Line 6 (Part I) does NOT separately list the truck — that would double-count. Line 8 = Line 6 (column c sum) + Line 7. So Line 6 column (c) = $0 here; Line 7 = $76,000; Line 8 = $76,000.

(I showed Line 6 with the truck above for narrative clarity, but the IRS form puts listed property §179 only in Part V; Line 6 lists non-listed-property §179 only.)

### Form 4562 Part IV

```
21. Listed property (from Line 28):              $0
22. Total (Lines 12+14+15+16+17+19+20+21):       $76,000
23. §263A capitalization:                         $0
```

Line 22 = $76,000 → flows to **Schedule C Line 13**.

### Year 1 tax effect

```
Schedule C Line 7 (Gross income):       (assume) $185,000
Schedule C expenses Lines 8-27a:                  $73,000  (other operating expenses)
Schedule C Line 13 (Form 4562):                   $76,000
Schedule C Line 28 (Total expenses):             $149,000
Schedule C Line 29 / 31 (Net profit):             $36,000

Federal tax (rough):                              $36,000 × ~22% = $7,920
Self-employment tax:                              $36,000 × 0.9235 × 15.3% = $5,089
                                                  Less ½ SE tax adjustment

Net income tax + SE tax this year:                ~$10,469
```

## Path B: 5-year MACRS (no §179, no bonus)

Daniel opts out of §179 and bonus to spread the deduction.

### Form 4562 Part III Section A

```
19b 5-year:
   (b) Month/year placed in service: 03/2025
   (c) Basis for depreciation: $76,000
   (d) Recovery period: 5 yrs
   (e) Convention: HY
   (f) Method: 200DB
   (g) Depreciation: $76,000 × 20% = $15,200
```

### Form 4562 Part V

```
24a/24b: Yes/Yes (same as Path A)
26. Same row, but column (i) = $0 (no §179 elected); column (h) = $15,200
28. Total → Line 21: $15,200
29. Total §179 → Line 7: $0
```

### Form 4562 Part IV

```
21. Listed property:                  $15,200
22. Total:                            $15,200  (flows to Schedule C Line 13)
```

### Year-by-year MACRS schedule

| Year | % | Deduction |
|------|---|-----------|
| 2025 | 20.00% | $15,200 |
| 2026 | 32.00% | $24,320 |
| 2027 | 19.20% | $14,592 |
| 2028 | 11.52% | $8,755 |
| 2029 | 11.52% | $8,755 |
| 2030 | 5.76% | $4,378 |
| **Total** | **100%** | **$76,000** |

Note: assumes HY convention. If Daniel placed the truck in service in October-December and the MQ test triggered (>40% of total annual personal-property cost in Q4), MQ would apply with a different schedule.

## Path C: §179 partial + bonus on remainder

A middle path: §179 enough to use the income, bonus on the rest.

```
§179 elected:                        $50,000  (chosen to leave $26K for bonus, but income limit is binding)
Adjusted basis after §179:           $26,000
Bonus depreciation (100%, post-Jan 19): $26,000
MACRS year 1:                        $0
Total year 1:                        $76,000
```

Same total as Path A. Why pick this? Almost no reason for Daniel — Path A and Path C give identical year 1 deductions and same future-year depreciation ($0 for both). The only theoretical difference is the §179 carryforward path: if Daniel's income later drops, §179 carryforward applies; bonus doesn't carry over.

## Decision: which path?

For Daniel:
- Path A (full §179): $76,000 year 1 deduction
- Path B (full MACRS): $15,200 year 1 deduction, balance over years 2-6
- Path C (partial §179 + bonus): $76,000 year 1 deduction, same as Path A

**Path A is the right choice** because:
1. Daniel's $112,000 net profit before §179 covers the full $76,000 deduction (income limit not binding)
2. Time value of money — getting the full deduction at his current 22% bracket gives ~$16,720 in immediate tax + SE tax savings vs. ~$3,344 in year 1 under MACRS
3. No carryforward complexity to track
4. Bonus alternative (Path C) is functionally identical for Daniel's situation

Path B might make sense if:
- Daniel expected his income to spike to a 32% bracket in year 2 — saving the deduction for the higher bracket year is worth it
- Daniel is approaching the §199A QBI deduction phase-out and a smaller current-year deduction keeps him under it
- State-conformity issues (e.g., the user's state doesn't conform to bonus depreciation) make MACRS more state-tax-efficient

For most solo filers buying tools they need this year, **Path A is the default**.

## Risk: business use must stay >50%

Daniel §179'd $76,000 based on 95% business use. If business use drops to ≤50% in years 2-5 of the recovery period, IRC §280F(b)(2) recapture triggers. Recapture amount = §179 + bonus + accelerated MACRS taken − ADS SL that would have been allowable.

Year-2 hypothetical drop to 40% business use:
- Allowed §179 + bonus + MACRS through year 2 (under original elections): $76,000 (year 1) + $0 (year 2 — already fully depreciated) = $76,000
- ADS SL that would have been allowable: ADS for vehicles is 5-year SL, half-year convention. Year 1 = 10%, Year 2 = 20% → through year 2 = 30% × $76,000 = $22,800
- Recapture in year 2: $76,000 − $22,800 = $53,200 ordinary income on Form 4797 Part IV → flows to Form 1040 Line 8 (via Schedule 1 Line 4)

Daniel needs to project forward: is 95% business use sustainable? If he's selling the plumbing business in 2 years and may use the truck for personal moving/family, §179 is risky. Better to use MACRS or ADS to avoid recapture.

## What Daniel files

- Form 1040 with Schedule C, Schedule SE
- **Form 4562** (Path A): Part I §179 + Part IV summary + Part V listed property
- Mileage log retained but not attached
- Receipt for $80,000 truck purchase retained

## Audit defense

If audited:
1. Mileage log substantiates 95% business use claim
2. Truck title shows 11,000 lbs GVWR (escapes §280F luxury cap)
3. Business income ($112,000) substantiates §179 income limit
4. Form 8594 not required (truck purchase, not business acquisition)
5. Daniel's business has plausible need for an F-250 (plumbing/heating contractor — moving heavy equipment)

## Sources cited in this draft

- IRS Form 4562, Rev. 2025
- IRS Instructions for Form 4562, Rev. 2025
- IRC §179, §168(k), §280F
- IRC §179(b)(5) — heavy SUV cap (not applicable here due to 8-ft bed exemption)
- Rev. Proc. 2024-40 (2025 §179 limit $1.25M, phase-out $3.13M, heavy SUV cap $31,300)
- IRS Pub. 946 (MACRS tables, vehicle treatment)
- IRS Pub. 463 (vehicle substantiation)
