# Example: MFJ Couple with Q4 Income Spike — Excess APTC Repayment

A complete walkthrough of Form 8962 for a married couple filing jointly whose Q4 income spike (one spouse landed a large consulting contract) pushed their actual income well above their enrollment estimate. Result: APTC > PTC, owing excess APTC repayment on Schedule 2 Line 1a. Tax year 2025 rules; the cap shown here does not exist for 2026 returns (P.L. 119-21 §71305).

## The filers

- **Names**: Carlos and Elena Mendoza
- **Filing status**: MFJ
- **Tax year**: 2025 (filing in 2026)
- **State**: Texas (48 contiguous + DC group)
- **Coverage**: Family Silver plan (Carlos + Elena + their 8-year-old son, Mateo) via healthcare.gov, full year

## Inputs gathered

### Income — estimate vs. actual

When they enrolled in November 2024, they estimated 2025 household income of **$58,000** (Carlos's W-2 wages, Elena freelancing modestly). Based on that estimate, the marketplace computed APTC of **$1,180/month** ($14,160/year).

Actual 2025 income:
- Carlos W-2 wages (Box 1): $52,400
- Elena Schedule C net profit: $44,800 (Q4 surge — landed an enterprise consulting deal in October)
- Bank interest: $230
- Half-of-SE-tax adjustment (from Elena's Schedule SE): $3,165 ($44,800 × 0.9235 × 15.3% = $6,330.04; × 50% = $3,165.02, rounded)
- AGI = $52,400 + $44,800 + $230 − $3,165 = **$94,265**
- Tax-exempt interest: $0
- Non-taxable SS: $0
- MAGI for PTC = AGI = **$94,265**

### Tax family

- Family size: 3 (Carlos + Elena + dependent son Mateo)
- 2024 FPL (48+DC, family of 3) = **$25,820**

### % of FPL

- Line 5 = ($94,265 / $25,820) × 100 = 365.1% → **365%**

### Form 1095-A data

Same plan all 12 months (no mid-year change):

- Column A (Monthly enrollment premium): $1,420 (family policy)
- Column B (Monthly applicable SLCSP): $1,365 (family of 3 SLCSP)
- Column C (Monthly APTC): $1,180

Annual totals:
- Column A annual: $17,040
- Column B annual: $16,380
- Column C annual (APTC): $14,160

### Method decision

- Family size constant: yes
- Same SLCSP: yes
- Same eligibility: yes
- Single tax family (Mateo is dependent on this return): yes
- Full year: yes

→ **Annual method (Line 10 = Yes)**.

## Form 8962 computation

### Part I

| Line | Value | Computation |
|------|-------|-------------|
| 1 | 3 | Tax family size |
| 2a | $94,265 | Carlos + Elena MAGI |
| 2b | $0 | Mateo not required to file (no income) |
| 3 | $94,265 | Line 2a + Line 2b |
| 4 | $25,820 | 2024 FPL, 48+DC, family size 3 |
| 5 | 365% | (94,265 / 25,820) × 100 = 365.1%, rounded down |

### Line 7 — Applicable figure (2025 IRA table, 365% FPL)

Band: 300% – 400%, initial 0.06, final 0.085.

```
applicable_figure = 0.06 + (365 − 300) / (400 − 300) × (0.085 − 0.06)
                  = 0.06 + (65 / 100) × 0.025
                  = 0.06 + 0.01625
                  = 0.07625
```

→ Line 7 = **0.0763** (2025 instructions Table 2 at 365)

### Part I continued

| Line | Value | Computation |
|------|-------|-------------|
| 8a | $7,192 | $94,265 × 0.0763 = $7,192.42, rounded to nearest dollar |
| 8b | $599 | $7,192 / 12 = $599.33, rounded |

### Part II — Annual calculation (Line 11)

| Column | Value | Source |
|--------|-------|--------|
| 11a — Annual premium | $17,040 | 1095-A Column A annual |
| 11b — Annual SLCSP | $16,380 | 1095-A Column B annual |
| 11c — Annual contribution | $7,192 | = Line 8a |
| 11d — Annual maximum premium assistance | $9,188 | max(0, 16,380 − 7,192) |
| 11e — Annual PTC allowed | $9,188 | min(17,040, 9,188) |
| 11f — Annual APTC | $14,160 | 1095-A Column C annual |

### Reconciliation

| Line | Value | Computation |
|------|-------|-------------|
| 24 | $9,188 | Total PTC = Line 11e |
| 25 | $14,160 | Total APTC = Line 11f |
| 26 | — | (skip; Line 25 > Line 24) |
| 27 | $4,972 | Line 25 − Line 24 (raw excess) |
| 28 | $3,250 | 2025 instructions Table 5: 365% FPL, MFJ ("any other filing status") row 300–<400 = $3,250 |
| 29 | $3,250 | lesser of $4,972 or $3,250 |

→ **Schedule 2 Line 1a = $3,250** (excess APTC repayment, capped)

The $1,722 of excess that exceeds the cap ($4,972 − $3,250) is **not collected** under IRC §36B(f)(2)(B) (2025). The Mendozas keep the windfall. On a 2026 return the same facts would mean repaying the full $4,972.

## The completed Form 8962 draft

```markdown
# Form 8962 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Carlos and Elena Mendoza
Your social security number: XXX-XX-XXXX (Carlos, primary filer)

## Part I — Annual and Monthly Contribution Amount
1.  Tax family size:                                      3
2a. Modified AGI of taxpayer (and spouse):                $94,265
2b. Dependents' modified AGI:                             $0
3.  Household income:                                     $94,265
4.  Federal poverty line (FPL) for family size:           $25,820
5.  Household income as % of FPL (rounded down):          365 %
6.  (Reserved):                                           —
7.  Applicable figure:                                    0.0763
8a. Annual contribution amount:                           $7,192
8b. Monthly contribution amount:                          $599

## Part II — Premium Tax Credit Claim and Reconciliation of APTC
9.  Allocating policy amounts or using Part V? Yes / No:  No
10. Annual calculation? Yes / No:                         Yes

11. Annual calculation:
    a. Annual enrollment premiums:                        $17,040
    b. Annual applicable SLCSP premium:                   $16,380
    c. Annual contribution amount (= Line 8a):            $7,192
    d. Annual maximum premium assistance (b − c, ≥ 0):    $9,188
    e. Annual Premium Tax Credit (lesser of a or d):      $9,188
    f. Annual advance payment of PTC:                     $14,160

12-23. Monthly calculation:                               (skip; Line 10 = Yes)

24. Total Premium Tax Credit:                             $9,188
25. Advance payment of PTC:                               $14,160
26. Net Premium Tax Credit:                               (blank; Line 25 > Line 24)
27. Excess APTC (Line 25 − Line 24):                      $4,972
28. Repayment limitation (2025 instructions Table 5,
    MFJ at 365% FPL → 300–<400 "other" row):              $3,250
29. Excess APTC repayment (lesser of 27 or 28):           $3,250
    → enter on Schedule 2 Line 1a

## Part IV — Allocation                                   (not applicable)
## Part V — Year of marriage                              (not applicable)

## Routing
- Line 26 → Schedule 3 Line 9:                            $0
- Line 29 → Schedule 2 Line 1a (excess APTC repayment):   $3,250

## Required attachments
- [x] Form 8962 attached to Form 1040
- [x] Form 1095-A retained in records (not attached)

## Validation summary
- Math:
  - Line 3 = $94,265 + $0 = $94,265 ✓
  - Line 5 = (94,265 / 25,820) × 100 = 365.09% → 365% ✓
  - Line 7 = 0.06 + (65/100) × 0.025 = 0.07625 → 0.0763 (Table 2) ✓
  - Line 8a = 94,265 × 0.0763 = $7,192.42 → $7,192 (rounded) ✓
  - Line 8b = 7,192 / 12 = $599.33 → $599 ✓
  - Line 11d = max(0, 16,380 − 7,192) = $9,188 ✓
  - Line 11e = min(17,040, 9,188) = $9,188 ✓
  - Line 24 = $9,188 ✓
  - Line 25 = $14,160 ✓
  - Line 27 = $14,160 − $9,188 = $4,972 ✓
  - Line 28 = $3,250 (2025 instructions Table 5 lookup) ✓
  - Line 29 = min($4,972, $3,250) = $3,250 ✓
- Inputs:
  - 2024 HHS FPL (correct for 2025 return)
  - 48+DC table (Texas)
  - Family size 3 matches Form 1040 (Carlos + Elena + dependent Mateo)
  - MAGI $94,265 = AGI (no §103 interest, no SS, no foreign income)
- Sanity:
  - Line 5 = 365% — below 400%, so the 2025 Table 5 cap applies
  - Repayment cap saved $1,722 of excess from being repaid
  - Lines 26 and 29 mutually exclusive (Line 26 blank, Line 29 = $3,250) ✓
  - Q4 income spike from Elena's consulting consistent with $44,800 net profit on Schedule C

## Sources cited in this draft
- IRS Form 8962, Rev. 2025
- IRS Instructions for Form 8962, Rev. 2025
- IRS Pub 974, 2025 edition
- Form 8962 instructions (2025), Table 1-1 (FPL), Table 2 (applicable figure), Table 5 (repayment limitation)
- HHS 2024 Poverty Guidelines (used for 2025-tax-year PTC)
- IRC §36B (PTC), §36B(b)(3)(A) (applicable figure), §36B(d)(3)(B) (FPL determination), §36B(f)(2)(B) (repayment limitation, tax years before 2026)
- IRA 2022 Section 12001 (ARPA modification extended through 2025)
```

## Why each non-obvious choice

**Why does the cap save the Mendozas money?** Without the cap, they'd repay $4,972 (the full excess). With the cap at $3,250, the additional $1,722 is forgiven by statute. This is a deliberate policy choice in IRC §36B(f)(2)(B) to protect filers below 400% FPL from punitive repayments when their income lands higher than estimated.

**Why MFJ uses the "other" column of Table 5?** The cap table in the Form 8962 instructions has two columns: "Single" and "any other filing status". MFJ falls in "other" (along with HoH, MFS, QSS). The MFJ cap is double the single cap.

**Why didn't the Mendozas trigger a higher cap with $94,265 income?** The cap is based on **% FPL**, not absolute income. At 365% FPL (within 300%–400% band), the MFJ cap is $3,250. If they were at 410% FPL on a 2025 return, Line 28 would be blank (no cap) and they would repay the full excess; on a 2026 return there is no cap at any income and no PTC above 400% FPL. Income of $94,265 with family size 3 happens to land in the 300-400% band.

**Why isn't Mateo's MAGI on Line 2b?** Mateo is 8 years old and has no income. Even if he had a tiny amount of unearned income (e.g., $200 in dividend income from a custodial account), it would be below the dependent filing requirement and wouldn't be on Line 2b.

**What if Elena had reported her Q4 income increase to the marketplace?** They could have reduced their APTC mid-year, which would have lowered Line 25 and reduced excess APTC. But the total PTC entitled ($9,188) would be the same — only the reconciliation differential changes. There's no penalty for not reporting; it's just smoother cash flow.

**Could the Mendozas have avoided this entirely?** Yes, by paying full marketplace premium with no APTC and claiming PTC at filing. But they'd have to front $14,160 of premiums during the year. The APTC mechanism trades end-of-year reconciliation risk for in-year cash flow relief.

## What if the Mendozas were audited?

Their audit defense would be:

1. Form 1095-A from healthcare.gov showing actual monthly APTC of $1,180
2. Carlos's W-2 supporting $52,400 wages
3. Elena's Schedule C with bank-statement-traced consulting receipts
4. Schedule SE supporting half-of-SE-tax adjustment
5. Form 8962 worksheet with 2024 FPL table and 0.0763 applicable figure
6. 2025 Form 8962 instructions Table 5 reference for the $3,250 cap
7. Mateo's birth certificate (or other dependent qualification documentation) supporting family size 3
