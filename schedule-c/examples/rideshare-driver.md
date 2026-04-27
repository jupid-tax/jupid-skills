# Example: Rideshare Driver (Heavy Vehicle, Multiple Platforms)

A complete walkthrough for a part-time rideshare driver who drives for both Uber and DoorDash, has very high vehicle expenses, and modest other costs. This is the canonical "gig economy with a vehicle" pattern.

## The filer

- **Name**: Carlos Mendoza
- **Business**: Rideshare driving (Uber) + delivery (DoorDash) on the same vehicle
- **Entity**: Sole proprietor (no LLC)
- **First Schedule C year**: No (second year)
- **Tax year**: 2025

## Inputs gathered

### Income

Gig platforms send multiple forms. Carlos collected:

| Source | Type | Amount |
|--------|------|--------|
| Uber 1099-NEC (rider fares) | 1099-NEC | $9,200 |
| Uber 1099-K (rider fare card payments routed through Uber) | 1099-K | $14,800 |
| DoorDash 1099-NEC | 1099-NEC | $7,400 |
| Tips received in cash and not on any 1099 | cash | $1,150 |
| **Line 1 Gross receipts** | | **$32,550** |

Note on rideshare 1099s: platforms issue different forms based on the type of payment. Uber typically sends 1099-K for rider payments and 1099-NEC for tips and incentives. The user must report the gross of both. **Do not reduce gross receipts by platform commissions** — those go on Line 10 separately.

### Expenses

Carlos drove a 2019 Honda Civic with 47,200 total miles for the year:

- 38,400 business miles (logged via Hurdlr)
- 4,200 commuting (none, since he goes directly from home to first ride)
- 4,600 personal

Business-use percentage: 38,400 / 47,200 = **81.4%**

He compares standard mileage vs. actual:

#### Standard mileage method

```
38,400 miles × $0.70 = $26,880
+ Tolls (logged):                $420
+ Parking (logged):              $180
+ Vehicle loan interest (Line 16b separately): $260 × 81.4% = $212

Total Line 9 if standard: $27,480
Plus Line 16b: $212
```

#### Actual expense method

```
Gas:               $4,800
Insurance:         $2,100
Repairs:             $980
Registration:        $290
Tires:               $620
Depreciation:      $4,200   (MACRS year 2 of 5-year property)
Total vehicle:    $12,990

Line 9 actual: $12,990 × 81.4% = $10,574
Tolls + parking: $600 → still deductible separately, $600 × 81.4% = $488
Vehicle loan interest (Line 16b): $260 × 81.4% = $212

Total Line 9 if actual: $11,062
Plus Line 16b: $212
```

**Carlos picks standard mileage** — it's $16,418 better than actual. He documents the comparison in his records.

### Other expenses

| Original transaction | Mapped to | Amount |
|---------------------|-----------|--------|
| Uber commission (~25% of fares; reported gross on 1099, deducted here) | Line 10 (Commissions/fees) | $5,950 |
| DoorDash commission (~10%) | Line 10 (Commissions/fees) | $740 |
| Roadside assistance (AAA) | Line 15 (Insurance) | $96 |
| Cell phone × 70% business use | Line 25 (Utilities — phone) or Line 27a | $560 |
| Snacks and water for passengers | Line 27a (Other) | $185 |
| Rideshare-required dashcam ($120, expensed under de minimis) | Line 27a (Other) | $120 |
| Phone mount and charger | Line 22 (Supplies) | $48 |
| Car washes (business portion 81.4%) | Line 9 (already inside standard mileage) | $0 separately |

Note: Carlos uses standard mileage, so gas/repairs/insurance/depreciation are inside the rate. His vehicle insurance is *not* on Line 15 — it's bundled into the per-mile rate. Roadside assistance is a separate non-vehicle policy, so it's Line 15 (or Line 27a; either is defensible).

### No home office

Carlos doesn't have a qualifying home office. He uses a corner of his bedroom for app management — fails the exclusive-use test. **Line 30 = $0**.

## The completed Schedule C draft

```markdown
# Schedule C — DRAFT for tax year 2025

## Header
A. Principal business: Rideshare and delivery driving
B. Business code: 485300 (Taxi & limousine service — covers rideshare)
C. Business name: (blank — using personal name)
D. EIN: (blank — using SSN)
E. Address: Same as Form 1040
F. Accounting method: Cash
G. Material participation: Yes
H. Started this year: No
I. Paid any individual $600+: No
J. (skipped)

## Part I — Income
1.  Gross receipts:                $32,550
2.  Returns and allowances:        $0
3.  Subtract line 2 from 1:        $32,550
4.  Cost of goods sold:            $0
5.  Gross profit:                  $32,550
6.  Other income:                  $0
7.  Gross income:                  $32,550

## Part II — Expenses
 8. Advertising:                   $0
 9. Car and truck:                 $27,480   (38,400 mi × $0.70 + $420 tolls + $180 parking; standard mileage)
10. Commissions and fees:          $6,690    (Uber + DoorDash platform fees)
11. Contract labor:                $0
12. Depletion:                     $0
13. Depreciation + §179:           $0        (using standard mileage; depreciation inside Line 9)
14. Employee benefit programs:     $0
15. Insurance (other than health): $96       (AAA roadside; not vehicle insurance — that's inside Line 9)
16a. Mortgage interest:            $0
16b. Other interest:               $212      (vehicle loan × 81.4% business)
17. Legal and professional:        $0
18. Office expense:                $0
19. Pension/profit-sharing:        $0
20a. Rent (vehicles, machinery):   $0
20b. Rent (other):                 $0
21. Repairs and maintenance:       $0        (inside Line 9 standard mileage)
22. Supplies:                      $48       (phone mount/charger)
23. Taxes and licenses:            $0
24a. Travel:                       $0        (driving locally is not "travel away from home")
24b. Deductible meals (50%):       $0
25. Utilities:                     $560      (cell phone × 70% business)
26. Wages:                         $0
27a. Other expenses (Part V):      $305
28. Total expenses:                $35,391

## Part II totals
29. Tentative profit/loss:         ($2,841)  [a loss — see notes]
30. Home office:                   $0
31. Net loss:                      ($2,841)
32. At-risk:                       32a (all investment is at risk)

## Part III — COGS
   N/A

## Part IV — Vehicle
43. Date placed in service:        01/01/2025  (full-year use)
44a. Business miles:               38,400
44b. Commuting miles:              4,200
44c. Other miles:                  4,600
45. Available for personal use:    Yes
46. Another vehicle available:     No
47a. Have evidence:                Yes (Hurdlr app + receipts)
47b. Written:                      Yes (digital log)

## Part V — Other Expenses (detail of Line 27a)
| Description                          | Amount |
|---------------------------------------|--------|
| Passenger snacks and water            | $185   |
| Dashcam (under de minimis $2,500)     | $120   |
| **Total (Line 48 = Line 27a)**        | $305   |

## Required attachments
- [ ] Form 4562 — Not required (no §179 or depreciation; standard mileage)
- [ ] Form 8829 — Not required (no home office)
- [ ] Schedule SE — Not required because Line 31 < $400 (this is a loss; no SE tax owed)

## Validation summary
- Math: all checks passed
- Sanity:
  - Net loss of $2,841 — first year showing a loss; not yet a hobby-loss pattern
  - Vehicle business-use 81.4% — high but plausible for a serious rideshare driver with separate personal vehicle... wait, Carlos has only this vehicle. Flag for review.
  - Commission ratio 20.5% — typical for Uber-heavy mix
  - Cell phone 70% business → flagged: high; user should be ready to substantiate
  - Loss of $2,841 will reduce other 2025 income on Form 1040
- Next steps:
  - This loss reduces Carlos's W-2 income on Form 1040
  - No quarterly estimated tax adjustment needed for 2026 unless income pattern changes
  - Carlos should track 2026 closely — two consecutive losses isn't a hobby trigger but three of five is

## Sources cited in this draft
- IRS Form 1040 Schedule C, Rev. 2025
- IRC §162; §183 (hobby loss); §280F (luxury auto)
- Notice 2025-5 (2025 standard mileage rate 70¢)
- Pub 463 (Travel, Gift, and Car Expenses)
```

## Why each non-obvious choice

**Why not deduct gas and repairs separately?** Carlos chose standard mileage. Gas, repairs, insurance, depreciation, and oil are inside the 70¢/mile rate. Deducting them again would be double-dipping.

**Why is vehicle insurance on Line 15 ($96) but not the regular auto insurance ($2,100)?** Auto insurance is bundled into standard mileage. AAA roadside is a separate optional service Carlos buys outside of his auto policy — so it's a legitimate Line 15 (or Line 27a) item.

**Why isn't Line 24a (Travel) used?** Carlos drives in his local metro area. He's not "away from home" overnight. Local driving is Line 9, not Line 24a.

**Why didn't Carlos take the home office?** The bedroom corner with his phone and laptop fails the exclusive-use test. Honest assessment beats a $300 deduction that wouldn't survive audit.

**Should Carlos consider switching to actual expenses next year?** Run the comparison. If the vehicle is paid off and depreciation runs out, actual expenses drop sharply and standard mileage usually wins. If he buys a new car, actual + bonus depreciation could win in year one.

**What about the loss?** A first-year or second-year loss is unremarkable — many rideshare drivers post small losses while ramping up. Three losses in five years would shift the burden onto Carlos to prove profit motive (IRC §183). At this stage, no concern.

**Why is Schedule SE not required?** Schedule SE is required only when net profit > $400. A loss means no SE tax. Schedule SE itself is not filed.

**What if Carlos had multiple gig platforms with overlapping miles?** All business miles count toward Line 9 regardless of platform — Uber and DoorDash miles are both business. The split between platforms only matters for understanding the income source, not for the deduction.
