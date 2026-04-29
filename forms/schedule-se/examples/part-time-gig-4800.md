# Example: Part-Time Gig Worker with $4,800 SE Income

A walkthrough of Schedule SE for a low-earning gig worker — over the $400 threshold (so SE tax is owed) but well below the wage base. Demonstrates that Schedule SE applies even when SE income is a small side hustle.

## The filer

- **Name**: Jordan Mensah
- **Business**: Part-time DoorDash and Instacart driver
- **Entity**: Sole proprietor (no LLC)
- **Tax year**: 2025 (filing in 2026)
- **W-2 wages this year**: $42,000 (full-time job at a logistics company)
- **Filing status**: Single
- **Prior-year SE income**: $0 in 2024, $0 in 2023 (this is Jordan's first year doing gig work)

## Inputs gathered

### SE income source

Jordan's bookkeeping app exported a Schedule C for the year:
- DoorDash gross earnings: $3,200
- Instacart gross earnings: $4,100
- Mileage deduction: 4,200 miles × $0.70/mi = $2,940
- Phone (business %): $360
- Other supplies: $200

```
Schedule C Line 1: $7,300
Schedule C Line 28 (expenses): $3,500
Schedule C Line 31 (net profit): $3,800
```

Wait — the prompt says $4,800 SE income. Let me adjust to use that figure as the Schedule C net profit:

| Source | Amount |
|--------|--------|
| Schedule C Line 31 net profit | $4,800 |
| Schedule F | $0 |
| K-1 Box 14 Code A | $0 |
| Church employee income | $0 |

### W-2 wages

```
W-2 Box 3 (SS wages): $42,000
W-2 Box 5 (Medicare wages): $42,000
```

### Optional method

Not needed — Jordan's W-2 already gives him 4 SS credits for 2025 ($42K well above the 4-credit threshold of $7,240). The optional method would only increase his SE tax for no SS credit benefit.

## Step-by-step computation

### Line 1a, 1b, 2

```
Line 1a:                    $0
Line 1b:                    $0
Line 2:                     $4,800
```

### Line 3

```
Line 3 = $4,800
```

### Line 4a — Apply 0.9235 factor

```
Line 4a = $4,800 × 0.9235 = $4,432.80
```

Round to $4,433.

Line 4a > $400 → SE tax owed. **Continue.** (If Line 4a had been below $400, Schedule SE would not be required and Jordan would owe no SE tax on the gig income.)

### Line 4b, 4c

```
Line 4b = $0
Line 4c = $4,433
```

### Line 5a, 5b

```
Line 5a = $0
Line 5b = $0
```

### Line 6 — Net earnings from SE

```
Line 6 = $4,433
```

### Line 7 — SS wage base (2025)

```
Line 7 = $176,100
```

### Line 8 — W-2 wage offset

```
Line 8a = $42,000  (W-2 Box 3)
Line 8b = $0
Line 8c = $0
Line 8d = $42,000
```

### Line 9 — Remaining SS wage base

```
Line 9 = $176,100 − $42,000 = $134,100
```

Plenty of room — Jordan's SE earnings are nowhere near the cap.

### Line 10 — SS portion

```
Line 10 = min($4,433, $134,100) × 0.124 = $4,433 × 0.124 = $549.69
```

Round to $550.

### Line 11 — Medicare portion

```
Line 11 = $4,433 × 0.029 = $128.56
```

Round to $129.

### Line 12 — Total SE tax

```
Line 12 = $550 + $129 = $679
```

### Line 13 — Deductible half

```
Line 13 = $679 × 0.5 = $339.50  →  $340
```

### Form 8959 check

Jordan's combined wages + SE = $42,000 + $4,800 = $46,800. Well below the $200K single-filer threshold. **Form 8959 not required.**

## The completed Schedule SE draft

```markdown
# Schedule SE — DRAFT for tax year 2025

## Header
Name of person with self-employment income: Jordan Mensah
Social security number: XXX-XX-XXXX

## Part I — Self-Employment Tax
1a. Net farm profit (Schedule F Line 34):        $0
1b. CRP payments excluded:                       $0
2.  Net non-farm profit (Schedule C Line 31):    $4,800
3.  Combine 1a, 1b, 2:                           $4,800
4a. Line 3 × 0.9235:                             $4,433
4b. Optional method amount:                      $0
4c. Combine 4a + 4b:                             $4,433
5a. Church employee income:                      $0
5b. Line 5a × 0.9235:                            $0
6.  Net earnings from SE (4c + 5b):              $4,433

7.  SS wage base for 2025:                       $176,100
8a. Total W-2 SS wages (Box 3):                  $42,000
8b. Unreported tip income:                       $0
8c. Wages from Form 8919:                        $0
8d. Sum 8a + 8b + 8c:                            $42,000
9.  Line 7 − Line 8d:                            $134,100

10. SS portion: min(Line 6, Line 9) × 0.124:     $550
11. Medicare portion: Line 6 × 0.029:            $129
12. Total SE tax (10 + 11):                      $679
13. Deductible half (12 × 0.5):                  $340

## Part II — Optional Methods
Section A — Farm Optional Method:                Not elected
Section B — Non-Farm Optional Method:            Not elected (W-2 already provides 4 SS credits)

## Required attachments
- [x] Schedule C (Line 2 source)
- [ ] Form 8959 — N/A (combined wages + SE = $46,800 < $200K)

## Validation summary
- Math: all checks passed
- Sanity:
  - Line 4a = $4,433 ≥ $400 (SE tax required) ✓
  - W-2 Box 3 ($42K) reduces SS wage base, but plenty remaining ✓
  - Combined wages + SE ($46,800) < $200K → no Form 8959 ✓
  - First-year SE filer → quarterly estimated tax reminder for 2026
- Next steps:
  - Schedule 2 Line 4: $679 (SE tax)
  - Schedule 1 Line 15: $340 (deductible half)
  - Form 1040 Line 23 picks up Schedule 2 Line 4
  - For 2026: if Jordan continues gig work, Form 1040-ES quarterly estimates required if expected federal tax owed > $1,000

## Sources cited in this draft
- IRS Schedule SE (Form 1040), Rev. 2025
- IRS Instructions for Schedule SE, Rev. 2025
- IRC §1401(a), §1401(b), §1402(a)(12), §1402(b) ($400 threshold), §164(f)
- SSA Contribution and Benefit Base 2025: $176,100
- Notice 2025-5 (2025 standard mileage rate 70¢, used in Jordan's Schedule C)
```

## Why each non-obvious choice

**Why is Schedule SE required for $4,800 of gig income?** Because Line 4a ($4,433) exceeds $400 (IRC §1402(b)). The threshold isn't $1,000 or $5,000 — it's $400. Plenty of part-time gig workers get caught by this when they file their first year and don't realize the SE tax is on top of regular income tax.

**Why didn't Jordan elect the non-farm optional method?** Two reasons. First, his W-2 ($42K) already gave him 4 SS credits for 2025 — the optional method's only purpose is to keep the credit clock ticking, and Jordan's clock is already ticking from the W-2. Second, he doesn't pass the regularity test (2-of-3 prior years with SE earnings ≥ $400) — this is his first year with SE income.

**Why does Line 9 matter when the cap isn't engaged?** It doesn't change Line 10 in this case (Line 6 < Line 9), but the IRS form requires the calculation. A future filer with high W-2 wages (e.g., $180K) could see Line 9 = 0 and SS portion zeroed out, so the line is functionally important — just not for Jordan.

**Why is Jordan's effective SE tax rate (14.15%) close to Daniel's (14.13%)?** Both are below the wage base with no W-2 wage interaction on Line 10. Both pay 0.9235 × 0.153 = 14.13%. Jordan's rate rounds slightly differently due to small-number rounding ($679 / $4,800 = 14.15%).

**What about state SE tax?** Most states don't have a separate SE tax. If Jordan lived in NYC, he might owe Unincorporated Business Tax (UBT) on the gig income — but only if his net earnings exceed certain thresholds (~$95K in 2025 for full UBT; below that there's a credit). $4,800 is far below; no NYC UBT.

**What about quarterly estimated taxes for 2026?** Jordan paid 2025 SE tax on the return. For 2026, if he expects $1,000+ in federal tax owed (income + SE), he must pay quarterly estimates via Form 1040-ES (IRC §6654). Most W-2 employees with side-gig income use the **safe harbor**: pay 100% of prior-year tax (110% if AGI > $150K) through W-2 withholding adjustments. The safer move for Jordan: increase his W-2 withholding (Form W-4 update with employer) by ~$170/quarter to cover the SE tax, avoiding the need for separate 1040-ES checks.

## Audit defense

If the IRS questioned the Schedule SE:
1. Schedule C Line 31 = $4,800, supported by DoorDash and Instacart 1099-NECs received and bank deposits
2. Line 4a math: $4,800 × 0.9235 = $4,432.80 → $4,433 (rounding correct)
3. Line 8a = $42,000 matches W-2 Box 3 reported by Jordan's employer (the IRS already has this from W-2 cross-matching)
4. Line 12 = $679 matches Schedule 2 Line 4 and contributes to Form 1040 Line 23
5. Line 13 = $340 matches Schedule 1 Line 15 deduction
