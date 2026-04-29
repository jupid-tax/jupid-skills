# Example: Consultant with $250,000 Schedule C Net Profit (Wage Base Cap)

A walkthrough showing how the Social Security wage base caps the SS portion of SE tax, while Medicare keeps applying. Also demonstrates when Form 8959 (Additional Medicare Tax) becomes required.

## The filer

- **Name**: Priya Sharma
- **Business**: Independent management consultant (mid-market private equity advisory)
- **Entity**: Single-member LLC, disregarded entity
- **Tax year**: 2025 (filing in 2026)
- **W-2 wages this year**: None (Priya left her last W-2 job in 2023)
- **Filing status**: Single
- **Prior-year SE income**: $220K in 2024 (regularly self-employed)

## Inputs gathered

### SE income source

| Source | Amount |
|--------|--------|
| Schedule C Line 31 net profit | $250,000 |
| Schedule F | $0 |
| K-1 Box 14 Code A | $0 |
| Church employee income | $0 |

### W-2 wages

None — Priya is fully self-employed.

### Optional method

Not relevant — earnings are far above any optional method threshold.

## Step-by-step computation

### Line 1a, 1b, 2 — SE income sources

```
Line 1a (farm):             $0
Line 1b (CRP):              $0
Line 2 (non-farm):          $250,000
```

### Line 3 — Sum

```
Line 3 = $250,000
```

### Line 4a — Apply 0.9235 factor

```
Line 4a = $250,000 × 0.9235 = $230,875
```

### Line 4b, 4c — Optional method

```
Line 4b = $0
Line 4c = $230,875
```

### Line 5a, 5b — Church employee income

```
Line 5a = $0
Line 5b = $0
```

### Line 6 — Net earnings from SE

```
Line 6 = $230,875
```

### Line 7 — SS wage base (2025)

```
Line 7 = $176,100
```

### Line 8 — W-2 wage offset

```
Line 8a = $0
Line 8b = $0
Line 8c = $0
Line 8d = $0
```

### Line 9 — Remaining SS wage base

```
Line 9 = $176,100 − $0 = $176,100
```

### Line 10 — SS portion (CAPPED)

```
Line 10 = min(Line 6, Line 9) × 0.124
        = min($230,875, $176,100) × 0.124
        = $176,100 × 0.124
        = $21,836.40
```

Round to $21,836.

**This is the maximum SS portion of SE tax for tax year 2025.** Priya's Line 6 exceeds the wage base by $54,775 — that excess only owes Medicare, not SS.

### Line 11 — Medicare portion (NO CAP)

```
Line 11 = $230,875 × 0.029 = $6,695.38
```

Round to $6,695.

Note: Medicare keeps applying past the wage base.

### Line 12 — Total SE tax

```
Line 12 = $21,836 + $6,695 = $28,531
```

### Line 13 — Deductible half

```
Line 13 = $28,531 × 0.5 = $14,266  (rounded; exact: $14,265.50)
```

### Form 8959 — Additional Medicare Tax (REQUIRED)

Because Priya's wages + SE earnings exceed $200,000 (single threshold), she owes an additional 0.9% Medicare tax on the excess.

Per Form 8959:
- Line 4 (SE earnings × 0.9235) = $230,875 (matches Schedule SE Line 6)
- Line 5 (Medicare threshold for single filer) = $200,000
- Line 6 (excess) = $230,875 − $200,000 = $30,875
- Line 7 (Additional Medicare Tax) = $30,875 × 0.009 = $277.88 → $278

Form 8959 is a **separate form**, not part of Schedule SE. Flag for the user.

## The completed Schedule SE draft

```markdown
# Schedule SE — DRAFT for tax year 2025

## Header
Name of person with self-employment income: Priya Sharma
Social security number: XXX-XX-XXXX

## Part I — Self-Employment Tax
1a. Net farm profit (Schedule F Line 34):        $0
1b. CRP payments excluded:                       $0
2.  Net non-farm profit (Schedule C Line 31):    $250,000
3.  Combine 1a, 1b, 2:                           $250,000
4a. Line 3 × 0.9235:                             $230,875
4b. Optional method amount:                      $0
4c. Combine 4a + 4b:                             $230,875
5a. Church employee income:                      $0
5b. Line 5a × 0.9235:                            $0
6.  Net earnings from SE (4c + 5b):              $230,875

7.  SS wage base for 2025:                       $176,100
8a. Total W-2 SS wages (Box 3):                  $0
8b. Unreported tip income:                       $0
8c. Wages from Form 8919:                        $0
8d. Sum 8a + 8b + 8c:                            $0
9.  Line 7 − Line 8d:                            $176,100

10. SS portion: min(Line 6, Line 9) × 0.124:     $21,836  (CAPPED at wage base)
11. Medicare portion: Line 6 × 0.029:            $6,695
12. Total SE tax (10 + 11):                      $28,531
13. Deductible half (12 × 0.5):                  $14,266

## Part II — Optional Methods
Section A — Farm Optional Method:                Not elected
Section B — Non-Farm Optional Method:            Not elected

## Required attachments
- [x] Schedule C (Line 2 source)
- [x] Form 8959 — REQUIRED (combined wages + SE > $200K single threshold)

## Form 8959 quick computation (separate form, not part of Schedule SE)
Line 4 (SE × 0.9235):                            $230,875
Line 5 (single threshold):                       $200,000
Line 6 (excess):                                 $30,875
Line 7 (Additional Medicare Tax 0.9%):           $278

Form 8959 Line 18 ($278) flows to Schedule 2 Line 11.

## Validation summary
- Math: all checks passed
- Sanity:
  - Line 10 capped at SS wage base × 0.124 = $21,836 (the maximum for 2025) ✓
  - Line 6 ($230,875) > Line 7 ($176,100) → expected; SS cap engaged ✓
  - Combined wages + SE > $200K → Form 8959 required ✓
- Next steps:
  - Schedule 2 Line 4: $28,531 (SE tax)
  - Schedule 2 Line 11: $278 (Additional Medicare Tax from Form 8959)
  - Schedule 1 Line 15: $14,266 (deductible half of SE tax)
  - Form 1040-ES quarterly estimates: SE tax + income tax + Add'l Medicare = significant; calculate carefully

## Sources cited in this draft
- IRS Schedule SE (Form 1040), Rev. 2025
- IRS Instructions for Schedule SE, Rev. 2025
- IRC §1401(a) (12.4% SS), §1401(b) (2.9% Medicare), §1402(a)(12) (0.9235 factor), §164(f) (deductible half)
- IRC §1401(b)(2) — Additional Medicare Tax (Form 8959)
- SSA Contribution and Benefit Base 2025: $176,100
- Form 8959 Instructions (Additional Medicare Tax thresholds)
```

## Why each non-obvious choice

**Why does Line 10 cap at $21,836 even though Priya's earnings are $230,875?** The Social Security wage base is the maximum income subject to the 12.4% SS portion. Once Line 6 exceeds Line 9 ($176,100 in 2025), the SS portion stops accruing. Priya pays SS tax on the first $176,100 of SE earnings only.

**Why doesn't Medicare have a cap?** IRC §1401(b) imposes the 2.9% rate on "all" SE earnings — there's no wage base. The Affordable Care Act of 2010 added the 0.9% Additional Medicare Tax (Form 8959) on high earners, also uncapped.

**Why is Form 8959 separate from Schedule SE?** Schedule SE handles the original 2.9% Medicare. Form 8959 handles the ACA's additional 0.9% with its own threshold computations and treatment of W-2 wages, RRTA wages, and SE income separately. The IRS chose not to fold Form 8959 into Schedule SE because the threshold logic differs by income type.

**What's Priya's effective SE tax rate?** $28,531 / $250,000 = 11.4%. Compare to Daniel's 14.13% in the $50K example. The cap on the SS portion makes the marginal rate above $176,100 only 2.9% (Medicare) + 0.9% (Add'l Medicare) = 3.8% — much lower than the headline 15.3%.

**Should Priya consider an S-corp election?** This is a common consulting decision. With $250K SE earnings, electing S-corp status (Form 2553) and taking a "reasonable salary" of, say, $100K W-2 + $150K K-1 distribution could save SE tax on the $150K distribution portion. The reasonable salary requirement (IRC §3121(d)) is enforced by the IRS, and the S-corp adds its own compliance burden (Form 1120-S, Form 941 quarterly, payroll). **This is a tax-planning decision out of scope for Schedule SE** — surface to the user as a "consider with a CPA" item.

## Audit defense

If the IRS questioned the Schedule SE:
1. Schedule C Line 31 = $250,000, supported by invoices, bank deposits, and 1099-NECs/1099-Ks
2. Line 4a math: $250,000 × 0.9235 = $230,875 (verifiable)
3. Line 10 cap math: min($230,875, $176,100) × 0.124 = $21,836 — the cap is intentional, not an error
4. Form 8959 attached for Additional Medicare Tax on the excess above $200K
5. No W-2 wages → Line 8a = $0 (cross-checked against IRS W-2 records)
