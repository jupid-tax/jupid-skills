# Example: Freelancer with $50,000 Schedule C Net Profit

A complete walkthrough of Schedule SE for the canonical solo freelancer pattern: one income source, no W-2 wages, no optional method, no quirks.

## The filer

- **Name**: Daniel Park
- **Business**: Freelance copywriter (B2B content)
- **Entity**: Sole proprietor (no LLC)
- **Tax year**: 2025 (filing in 2026)
- **W-2 wages this year**: None
- **Filing status**: Single
- **Prior-year SE income**: $42K in 2024, $38K in 2023 (regularly self-employed)

## Inputs gathered (Step 2 of workflow)

### SE income source

| Source | Amount |
|--------|--------|
| Schedule C Line 31 net profit | $50,000 |
| Schedule F | $0 |
| K-1 Box 14 Code A | $0 |
| Church employee income | $0 |

### W-2 wages

None — Daniel has no employer W-2 in 2025.

### Optional method

Daniel does NOT need to elect an optional method. His net SE earnings are well above $400, and his actual earnings ($50K) generate full 4 SS credits for the year (2025: 4 credits = $7,240 in covered earnings; Daniel's $50K × 0.9235 = $46,175, far above).

## Step-by-step computation

### Line 1a, 1b, 2 — SE income sources

```
Line 1a (farm):             $0
Line 1b (CRP):              $0
Line 2 (non-farm):          $50,000  (Schedule C Line 31)
```

### Line 3 — Sum

```
Line 3 = $0 + $0 + $50,000 = $50,000
```

### Line 4a — Apply 0.9235 factor

```
Line 4a = $50,000 × 0.9235 = $46,175
```

Line 4a > $400, so SE tax is owed. Continue.

### Line 4b, 4c — Optional method

```
Line 4b = $0  (no optional method)
Line 4c = $46,175 + $0 = $46,175
```

### Line 5a, 5b — Church employee income

```
Line 5a = $0
Line 5b = $0
```

### Line 6 — Net earnings from SE

```
Line 6 = $46,175 + $0 = $46,175
```

### Line 7 — SS wage base (2025)

```
Line 7 = $176,100  (per 2025 Schedule SE form)
```

### Line 8a, 8b, 8c, 8d — W-2 wage offset

```
Line 8a = $0   (no W-2)
Line 8b = $0
Line 8c = $0
Line 8d = $0
```

### Line 9 — Remaining SS wage base

```
Line 9 = $176,100 − $0 = $176,100
```

### Line 10 — SS portion

```
Line 10 = min($46,175, $176,100) × 0.124 = $46,175 × 0.124 = $5,725.70
```

Round to $5,726.

### Line 11 — Medicare portion

```
Line 11 = $46,175 × 0.029 = $1,339.08
```

Round to $1,339.

### Line 12 — Total SE tax

```
Line 12 = $5,726 + $1,339 = $7,065
```

### Line 13 — Deductible half

```
Line 13 = $7,065 × 0.5 = $3,533  (rounded; exact: $3,532.50)
```

## The completed Schedule SE draft

```markdown
# Schedule SE — DRAFT for tax year 2025

## Header
Name of person with self-employment income: Daniel Park
Social security number: XXX-XX-XXXX

## Part I — Self-Employment Tax
1a. Net farm profit (Schedule F Line 34):        $0
1b. CRP payments excluded:                       $0
2.  Net non-farm profit (Schedule C Line 31):    $50,000
3.  Combine 1a, 1b, 2:                           $50,000
4a. Line 3 × 0.9235:                             $46,175
4b. Optional method amount:                      $0
4c. Combine 4a + 4b:                             $46,175
5a. Church employee income:                      $0
5b. Line 5a × 0.9235:                            $0
6.  Net earnings from SE (4c + 5b):              $46,175

7.  SS wage base for 2025:                       $176,100
8a. Total W-2 SS wages (Box 3):                  $0
8b. Unreported tip income:                       $0
8c. Wages from Form 8919:                        $0
8d. Sum 8a + 8b + 8c:                            $0
9.  Line 7 − Line 8d:                            $176,100

10. SS portion: min(Line 6, Line 9) × 0.124:     $5,726
11. Medicare portion: Line 6 × 0.029:            $1,339
12. Total SE tax (10 + 11):                      $7,065
13. Deductible half (12 × 0.5):                  $3,533

## Part II — Optional Methods
Section A — Farm Optional Method:                Not elected
Section B — Non-Farm Optional Method:            Not elected

## Required attachments
- [x] Schedule C (Line 2 source)
- [ ] Schedule F — N/A
- [ ] Form 8959 — N/A (Daniel's combined wages + SE = $46,175, below $200K threshold)

## Validation summary
- Math: all checks passed
- Sanity: none flagged
  - Line 4a = $46,175 ≥ $400 (SE tax required) ✓
  - W-2 wages $0 → no Line 9 reduction ✓
  - Combined wages + SE ($46,175) < $200K → no Form 8959 needed ✓
- Next steps:
  - Schedule 2 Line 4: $7,065 (SE tax flows to Form 1040 Line 23)
  - Schedule 1 Line 15: $3,533 (deductible half reduces AGI)
  - Form 1040-ES quarterly estimates for 2026: ~($7,065 / 4) = $1,766/quarter for SE component, plus income tax estimate

## Sources cited in this draft
- IRS Schedule SE (Form 1040), Rev. 2025
- IRS Instructions for Schedule SE, Rev. 2025
- IRC §1401(a) (12.4% SS rate), §1401(b) (2.9% Medicare rate), §1402(a)(12) (0.9235 factor), §164(f) (deductible half)
- SSA Contribution and Benefit Base 2025: $176,100
```

## Why each non-obvious choice

**Why not elect the non-farm optional method?** Daniel's earnings already generate the maximum 4 SS credits for the year (the 2025 threshold is $1,810 per credit × 4 = $7,240, and Daniel's $46,175 is far above). The optional method would only INCREASE his SE tax with zero credit benefit. Skip.

**Why no Form 8959?** Additional Medicare Tax kicks in only when wages + SE earnings exceed $200K (single). Daniel's combined total is $46,175 — well below.

**Why is the deductible half ($3,533) so important?** At Daniel's marginal income tax rate (likely 22% federal in 2025 for $46K AGI), the §164(f) deduction saves him $3,533 × 0.22 = $777 in income tax. Skipping it would be an unforced error.

**What's Daniel's effective SE tax rate?** $7,065 / $50,000 = 14.13%. That's the canonical SE tax rate net of the 0.9235 factor: 0.9235 × 0.153 = 0.1413 = 14.13%. This applies to any pure-SE filer below the wage base with no W-2 wages.

**What if Daniel had a Roth IRA or solo 401(k)?** Retirement contributions don't affect SE tax (SE is computed before retirement deductions). They affect income tax via Schedule 1 Line 16. Out of scope for Schedule SE.

**What about state SE tax?** California, Daniel's state, has no separate state SE tax — the SE income is taxed via regular state income tax on his California return. New York City residents would owe additional UBT; out of scope here.

## Audit defense

If the IRS questioned the Schedule SE:
1. Schedule C Line 31 = $50,000, supported by invoices, bank deposits, and 1099-NECs received
2. Line 4a math: $50,000 × 0.9235 = $46,175 (verifiable)
3. Line 8a = $0, supported by absence of W-2 (the IRS already knows from W-2 cross-matching)
4. Line 12 = $7,065 matches Schedule 2 Line 4 and contributes to Form 1040 Line 23
5. Line 13 = $3,533 matches Schedule 1 Line 15 deduction
