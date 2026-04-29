# Example: Low-Income Freelancer with Full-Year Coverage — PTC Refund

A complete walkthrough of Form 8962 for a single freelancer with full-year marketplace coverage whose actual income ended up *lower* than estimated. Result: Premium Tax Credit > APTC received, producing a refundable Net PTC on Schedule 3 Line 9.

## The filer

- **Name**: Sara Watanabe
- **Filing status**: Single
- **Occupation**: Freelance illustrator
- **Tax year**: 2025 (filing in 2026)
- **State**: Oregon (48 contiguous + DC group)
- **Coverage**: Self-only Silver plan via healthcare.gov, full year

## Inputs gathered

### Income

When Sara enrolled in November 2024, she estimated 2025 income of **$38,000**. Based on that estimate, the marketplace computed APTC of **$245/month** ($2,940/year).

Sara's actual 2025 income (slow year):

- Schedule C gross receipts: $36,200
- Schedule C expenses: $7,800
- Schedule C net profit: $28,400
- Bank interest: $50
- Half-of-SE-tax adjustment: $2,008 (from Schedule SE)
- AGI = $28,400 + $50 − $2,008 = **$26,442**
- Tax-exempt interest: $0
- Non-taxable SS: $0
- MAGI for PTC = AGI = **$26,442**

### Tax family

- Family size: 1 (single, no dependents)
- 2024 FPL (48+DC, family of 1) = **$15,060**

### % of FPL

- Line 5 = ($26,442 / $15,060) × 100 = 175.6% → rounded down to **175%**

### Form 1095-A data

Same plan all 12 months (no mid-year change):

- Column A (Monthly enrollment premium): $396
- Column B (Monthly applicable SLCSP): $384
- Column C (Monthly APTC): $245

Annual totals:
- Column A annual: $4,752
- Column B annual: $4,608
- Column C annual (APTC): $2,940

### Method decision

- Family size constant: yes
- Same eligibility all year: yes
- Same SLCSP: yes
- Not a shared policy: yes
- Coverage all 12 months: yes

→ **Annual method (Line 10 = Yes)**.

## Form 8962 computation

### Part I

| Line | Value | Computation |
|------|-------|-------------|
| 1 | 1 | Tax family size |
| 2a | $26,442 | Sara's MAGI |
| 2b | $0 | No dependents |
| 3 | $26,442 | Line 2a + Line 2b |
| 4 | $15,060 | 2024 FPL, 48+DC, family size 1 |
| 5 | 175% | (26,442 / 15,060) × 100 = 175.6%, rounded down |

### Line 7 — Applicable figure (2025 IRA table, 175% FPL)

Band: 150% – 200%, initial 0.00, final 0.02.

```
applicable_figure = 0.00 + (175 − 150) / (200 − 150) × (0.02 − 0.00)
                  = (25 / 50) × 0.02
                  = 0.0100
```

→ Line 7 = **0.0100**

### Part I continued

| Line | Value | Computation |
|------|-------|-------------|
| 8a | $264 | $26,442 × 0.0100 (rounded) |
| 8b | $22 | $264 / 12 |

### Part II — Annual calculation (Line 11)

| Column | Value | Source |
|--------|-------|--------|
| 11a — Annual premium | $4,752 | 1095-A Column A annual |
| 11b — Annual SLCSP | $4,608 | 1095-A Column B annual |
| 11c — Annual contribution | $264 | = Line 8a |
| 11d — Annual maximum premium assistance | $4,344 | max(0, 4,608 − 264) |
| 11e — Annual PTC allowed | $4,344 | min(4,752, 4,344) |
| 11f — Annual APTC | $2,940 | 1095-A Column C annual |

### Reconciliation

| Line | Value | Computation |
|------|-------|-------------|
| 24 | $4,344 | Total PTC = Line 11e |
| 25 | $2,940 | Total APTC = Line 11f |
| 26 | $1,404 | Line 24 − Line 25 (Net PTC, refundable) |
| 27 | — | (skip; Line 24 ≥ Line 25) |
| 28 | — | (skip) |
| 29 | — | (skip) |

→ **Schedule 3 Line 9 = $1,404** (refundable Net Premium Tax Credit)

## The completed Form 8962 draft

```markdown
# Form 8962 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Sara Watanabe
Your social security number: XXX-XX-XXXX

## Part I — Annual and Monthly Contribution Amount
1.  Tax family size:                                      1
2a. Modified AGI of taxpayer:                             $26,442
2b. Dependents' modified AGI:                             $0
3.  Household income:                                     $26,442
4.  Federal poverty line (FPL) for family size:           $15,060
5.  Household income as % of FPL (rounded down):          175 %
6.  (Reserved):                                           —
7.  Applicable figure:                                    0.0100
8a. Annual contribution amount:                           $264
8b. Monthly contribution amount:                          $22

## Part II — Premium Tax Credit Claim and Reconciliation of APTC
9.  Did you allocate policy amounts? Yes / No:            No
10. Annual calculation? Yes / No:                         Yes

11. Annual calculation:
    a. Annual enrollment premiums:                        $4,752
    b. Annual applicable SLCSP premium:                   $4,608
    c. Annual contribution amount (= Line 8a):            $264
    d. Annual maximum premium assistance (b − c, ≥ 0):    $4,344
    e. Annual Premium Tax Credit (lesser of a or d):      $4,344
    f. Annual advance payment of PTC:                     $2,940

12-23. Monthly calculation:                               (skip; Line 10 = Yes)

24. Total Premium Tax Credit:                             $4,344
25. Advance payment of PTC:                               $2,940
26. Net Premium Tax Credit (Line 24 − Line 25):           $1,404
    → enter on Schedule 3 Line 9

27. Excess APTC:                                          (skip)
28. Repayment limitation:                                 (skip)
29. Excess APTC repayment:                                (skip)

## Part IV — Allocation                                   (not applicable)
## Part V — Year of marriage                              (not applicable)

## Routing
- Line 26 → Schedule 3 Line 9 (refundable PTC):           $1,404
- Line 29 → Schedule 2 Line 2:                            $0

## Required attachments
- [x] Form 8962 attached to Form 1040
- [x] Form 1095-A retained in records (not attached)

## Validation summary
- Math:
  - Line 3 = $26,442 + $0 = $26,442 ✓
  - Line 5 = (26,442 / 15,060) × 100 = 175.6% → 175% ✓ (rounded down)
  - Line 7 = 0.00 + (25/50) × 0.02 = 0.0100 ✓
  - Line 8a = 26,442 × 0.0100 = $264.42 → $264 (rounded) ✓
  - Line 11d = max(0, 4,608 − 264) = $4,344 ✓
  - Line 11e = min(4,752, 4,344) = $4,344 ✓
  - Line 24 = $4,344 ✓
  - Line 25 = $2,940 ✓
  - Line 26 = $4,344 − $2,940 = $1,404 ✓
- Inputs:
  - 2024 HHS FPL used (correct for 2025 return)
  - 48+DC table used (Oregon)
  - Family size 1 matches Form 1040 (no dependents)
  - MAGI $26,442 = AGI (no tax-exempt interest, no SS, no foreign income)
- Sanity:
  - Line 5 = 175% within expected range (above Medicaid threshold for non-expansion situations; eligible for PTC)
  - Net PTC $1,404 makes sense — Sara's actual income was $11,558 lower than estimate, so APTC was under-paid
  - Annual method correct (no changes during year)

## Sources cited in this draft
- IRS Form 8962, Rev. 2025
- IRS Instructions for Form 8962, Rev. 2025
- IRS Pub 974 (Premium Tax Credit), 2025 edition, Table 1 and Table 2
- HHS 2024 Poverty Guidelines (used for 2025-tax-year PTC)
- IRC §36B (PTC)
- IRC §36B(b)(3)(A) (applicable figure)
- IRC §36B(d)(3)(C) (FPL determination date — prior-year HHS guidelines)
- IRC §36B(c)(1) (eligibility)
- IRA 2022 Section 12001 (extension of ARPA modification through 2025)
```

## Why each non-obvious choice

**Why is the Net PTC refundable?** PTC is a refundable credit under IRC §36B(d)(2) — even if the filer has $0 income tax liability, they receive the credit as a refund. This is unlike many other tax credits that only reduce tax owed (non-refundable).

**Why doesn't Sara owe Schedule 2 Line 2?** Lines 26 and 29 are mutually exclusive. When PTC > APTC (entitled to more than received), Line 26 is positive and Line 29 is zero. When APTC > PTC (received more than entitled), Line 27 is positive and Line 29 may be capped repayment.

**Why use annual method?** All four conditions for annual were met: same family size, same SLCSP, same eligibility, single tax family, full-year coverage. Annual is simpler and produces the same result.

**Why is MAGI = AGI here?** Sara has no tax-exempt municipal bond interest, no Social Security benefits, and no foreign earned income exclusion. So MAGI = AGI without adjustments.

**Why didn't Sara's $50 in bank interest matter?** It's already in AGI (Schedule B / Form 1040 Line 2b for taxable interest). MAGI doesn't add it again — only tax-exempt interest from §103 (muni bonds) is added back.

**What if Sara had reported her income change to the marketplace mid-year?** She could have requested an APTC increase, which would have reduced her end-of-year PTC reconciliation (less Net PTC because more APTC was received). Either way, the total PTC ($4,344) is the same; only the timing differs.

## What if Sara were audited?

Her audit defense would be:

1. Form 1095-A from healthcare.gov showing actual monthly APTC of $245
2. Schedule C documentation supporting net profit of $28,400
3. Form 8962 worksheet showing FPL calculation with 2024 HHS table
4. Pub 974 Table 2 reference for 2025 applicable figure at 175% FPL
5. AGI reconciliation: Schedule C profit + interest − half-SE-tax adjustment
6. Bank statements for the year showing income deposits matching Schedule C
