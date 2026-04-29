# Example: US Expat Working in Germany — Full Form 1116 General Basket

A US citizen working as an employee in Germany for a German employer. High German tax rates (~38% effective) make FTC the correct choice over FEIE; this walkthrough produces the full Form 1116 (general basket) and shows the §904 limitation math.

## The filer

- **Name**: Sarah Chen
- **Status**: US citizen, single, lives in Munich since 2021
- **Profession**: software engineer at SAP (W-2 equivalent — German Lohnsteuer)
- **US-source income**: $0 (Sarah works exclusively for German employer)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Foreign income

| Source | Currency | Amount | USD (yearly avg) |
|--------|----------|--------|------------------|
| SAP gross salary 2025 | EUR | €110,000 | $119,020 |
| Year-end bonus | EUR | €10,000 | $10,820 |
| **Line 1a (general basket)** | | **€120,000** | **$129,840** |

Yearly average rate (illustrative; verify on https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates for 2025): 1 EUR = $1.082 USD.

### Foreign tax (German Lohnsteuer + Solidaritätszuschlag)

| Tax type | EUR | USD |
|----------|-----|-----|
| Lohnsteuer (income tax withheld) | €38,000 | $41,116 |
| Solidaritätszuschlag (solidarity surcharge) | €2,090 | $2,261 |
| Kirchensteuer (church tax) | €0 | $0 (Sarah opted out) |
| **Total foreign tax (Line 8)** | **€40,090** | **$43,377** |

(Note: German social security tax — Rentenversicherung, Krankenversicherung, etc. — is NOT creditable. Germany has a US Totalization Agreement, so Sarah's SS-equivalent contribution shifts under that framework, not via Form 1116.)

### Tax election

- Sarah elects "Paid" (cash basis) — most common for individuals
- Method binding implications for accrual not relevant

### Sarah's other facts

- No US-source wages (lived/worked in Germany all year)
- $1,200 US-source interest from Schwab money market (USD)
- Standard deduction 2025 single: $15,000 (verify with IRS Rev. Proc.; using illustrative figure)
- Bona fide resident of Germany since 2021 — qualifies for FEIE if she elected, but FEIE is suboptimal at her income level (see Why FTC over FEIE below)

### FEIE coordination check

Sarah considered FEIE (Form 2555) but rejected it:

- Foreign earned income $129,840 vs. FEIE cap $130,000 (2025) — she's right at the cap; FEIE would exclude essentially all wages
- However, her German tax is $43,377 — much more than her US tax would be on the same income (~$24K at single rates)
- With FTC, she fully credits the $43,377 against US tax, generating a large unused carryforward
- With FEIE alone, she'd waste the German tax (no US tax to offset; the $43,377 is gone)
- Final choice: **FTC (Form 1116) general basket**

See [`coordination-with-2555.md`](../references/coordination-with-2555.md).

## Step-by-step Form 1116

### Part I — Foreign-source taxable income (general basket)

| Line | Calculation | USD |
|------|------------|-----|
| 1a (Country A: Germany) | Gross wages | $129,840 |
| 1b | Compensation for services performed abroad | $129,840 |
| 2 | Definitely related deductions (none) | $0 |
| 3a | Standard deduction | $15,000 |
| 3b | Other pro-rata deductions | $0 |
| 3c | 3a + 3b | $15,000 |
| 3d | Foreign general-basket gross income | $129,840 |
| 3e | Total gross income (worldwide) | $131,040 ($129,840 + $1,200 US interest) |
| 3f | 3d / 3e | 0.990842 |
| 3g | 3c × 3f | $14,863 |
| 4a | Home mortgage interest | $0 (Sarah rents) |
| 4b | Allocated to foreign | $0 |
| 5 | Foreign losses | $0 |
| 6 | 2 + 3g + 4b + 5 | $14,863 |
| **7** | **1a − 6 (foreign-source taxable income)** | **$114,977** |

### Part II — Foreign taxes paid

Country A (Germany), Paid (cash basis):

| Type | EUR | Conversion rate | USD |
|------|-----|-----------------|-----|
| Income tax withheld at source on wages | €38,000 | 1.082 | $41,116 |
| Solidaritätszuschlag (income surtax) | €2,090 | 1.082 | $2,261 |
| **Line 8 — Total** | | | **$43,377** |

### Part III — §904 limitation

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $43,377 |
| 10 | Carryover from prior years (none) | $0 |
| 11 | 9 + 10 | $43,377 |
| 12 | Boycott reduction | $0 |
| 13 | 11 − 12 | $43,377 |
| 14 | = Line 7 | $114,977 |
| 15 | QD/LTCG adjustment (no QD/LTCG in foreign income) | $0 |
| 17 | 14 − 15 | $114,977 |
| 18 | Total taxable income (Form 1040 Line 15) | $116,040 ($131,040 − $15,000 std deduction) |
| 19 | 17 / 18 | 0.990840 |
| 20 | Line 19 × Form 1040 tax before credits | (see calc below) |
| **21** | **Lesser of 13 or 20** | **(see calc)** |

#### Computing Line 20

Sarah's Form 1040 tax before credits at 2025 single rates (using illustrative 2025 brackets — verify Rev. Proc. before filing):

Approximate calculation on taxable income $116,040:
- 10% on first $11,925 = $1,193
- 12% on next $36,550 ($11,925-$48,475) = $4,386
- 22% on next $54,400 ($48,475-$102,875) = $11,968
- 24% on remaining $13,165 ($102,875-$116,040) = $3,160
- **Form 1040 tax before credits ≈ $20,706**

Verify exact bracket schedule from 2025 Tax Tables (IRS).

- Line 20 = 0.990840 × $20,706 = **$20,517**
- Line 21 = lesser of $43,377 or $20,517 = **$20,517**

### Unused FTC

Line 13 ($43,377) − Line 21 ($20,517) = **$22,860 unused**

This carries:
- Back 1 year (Sarah could amend her 2024 return if 2024 had limitation room — likely not, since she had similar facts)
- Forward 10 years (until 2035)

## The completed Form 1116 draft

```markdown
# Form 1116 — DRAFT for tax year 2025 (Category: General — Box d)

## Header
Filer name: Sarah Chen
SSN/ITIN: XXX-XX-XXXX
Resident country (Line i): Germany (DE)
Category: (d) General category income
Paid or accrued (h): Paid

## Part I — Foreign-source taxable income
Country column A: Germany (DE)
1a. Gross foreign-source income:
    Germany: $129,840
    Total: $129,840
1b. Compensation for services abroad:        $129,840
2.  Definitely-related deductions:            $0
3a. Pro-rata: standard deduction:             $15,000
3b. Pro-rata: other deductions:               $0
3c. 3a + 3b:                                  $15,000
3d. Foreign-source gross income:              $129,840
3e. Gross income from all sources:            $131,040
3f. 3d ÷ 3e:                                  0.990842
3g. 3c × 3f:                                  $14,863
4a. Home mortgage interest:                   $0
4b. Allocated to foreign:                     $0
5.  Losses from foreign sources:              $0
6.  Total deductions (2+3g+4b+5):             $14,863
7.  Foreign-source taxable income (1a−6):     $114,977

## Part II — Foreign taxes paid (cash basis)
| Country | Foreign currency | USD amount | Date paid |
|---------|------------------|-----------|-----------|
| Germany (A) — income tax withheld | €38,000 | $41,116 | Various 2025 paychecks |
| Germany (A) — Solidaritätszuschlag | €2,090 | $2,261 | Various 2025 paychecks |
8. Total foreign tax (USD):                   $43,377

## Part III — §904 limitation
9.  = Line 8:                                 $43,377
10. Prior-year carryover:                     $0
11. 9 + 10:                                   $43,377
12. Boycott reduction:                        $0
13. 11 − 12:                                  $43,377
14. = Line 7:                                 $114,977
15. QD/LTCG adjustment:                       $0 (no foreign QD/LTCG)
17. 14 − 15:                                  $114,977
18. Total taxable income (Form 1040 Line 15): $116,040
19. 17 ÷ 18:                                  0.990840
20. Line 19 × US tax before credits:          $20,517
21. Lesser of 13 or 20 (FTC, general basket): $20,517

## Part IV (this is the only basket, so summary on this 1116)
22. Credit from this 1116 Part III Line 21:   $20,517
33. Total credit:                             $20,517
35. Final FTC (Schedule 3 Line 1):            $20,517

## Carryover tracking
Unused FTC this year (general basket): $43,377 − $20,517 = $22,860
  - Carryback to 2024: consider amending if 2024 had limitation room
  - Carryforward to 2026 onwards (through 2035 max)

## Required attachments
- [x] Form 1116 (general basket, this draft)
- [ ] Form 8938 if foreign financial assets exceed reporting threshold ($200K end of year / $300K any time, single living abroad)
- [ ] FBAR / FinCEN 114 if German bank account aggregate > $10,000 at any point in year (separate filing, not attached to 1040)

## Validation summary
- Math: all checks passed
  - Line 6 = $0 + $14,863 + $0 + $0 = $14,863 ✓
  - Line 7 = $129,840 − $14,863 = $114,977 ✓
  - Line 19 = $114,977 / $116,040 = 0.990840 ✓
  - Line 21 = lesser of $43,377 or $20,517 = $20,517 ✓
- Sanity:
  - Foreign tax / foreign income = $43,377 / $129,840 = 33.4% — typical German effective rate; plausible
  - Unused FTC $22,860 — significant; track carryforward
  - Sarah passes bona fide residence test → could elect FEIE; chose FTC instead based on tax-rate analysis
- Next steps:
  - File 2025 return with Form 1116 attached
  - Track carryforward schedule by basket
  - Confirm Form 8938 / FBAR thresholds
  - Re-evaluate FEIE vs. FTC each year if circumstances change

## Sources cited in this draft
- IRS Form 1116, Rev. 2025
- IRS Instructions for Form 1116, Rev. 2025
- IRC §901, §904(a)-(c), §905
- Pub. 514 — Foreign Tax Credit for Individuals
- Pub. 54 — US Citizens and Resident Aliens Abroad
- IRS Yearly Average Currency Exchange Rates (2025 EUR rate)
- US-Germany Tax Treaty (1989, as amended)
- US-Germany Totalization Agreement (1979, for SS-equivalent treatment)
```

## Why each non-obvious choice

**Why general basket (d), not passive (c)?** Wages are general-category income under IRC §904(d). Passive is for dividends, interest, royalties. Sarah's salary goes in general regardless of country.

**Why "Paid" not "Accrued"?** Sarah pays German tax via withholding throughout the year — cash basis matches her actual cash flow. "Accrued" would be appropriate if she had a year-end true-up that lands in the next year, but her German employer withholds full liability monthly.

**Why no Line 4 home mortgage allocation?** Sarah rents her Munich apartment. Renters have no mortgage interest, so Line 4a/4b = $0. If she owned her German apartment, there would be additional allocation work.

**Why FEIE wasn't chosen.** Sarah's German tax of $43,377 vastly exceeds her US tax on the same income (~$20,706). FEIE would zero out US tax on the wages but waste $22,860 of "extra" German tax. FTC captures the same current-year tax result AND preserves the $22,860 as a carryforward asset (10-year window). FEIE also blocks IRA contribution (excluded income isn't compensation for IRA purposes); FTC preserves that option.

**Why no QD/LTCG adjustment (Line 15 = $0)?** Sarah has no foreign-source qualified dividends or LTCG — only wages. The Line 15 adjustment only applies when foreign income includes preferential-rate items. See [`qualified-dividend-adjustment.md`](../references/qualified-dividend-adjustment.md).

**What if Sarah's situation included $5,000 of US-source wages (e.g., a side gig she did while visiting the US)?** US-source income reduces Line 19 (it stays in the denominator at full rate, but doesn't add to the numerator). Limitation goes down slightly, FTC may be slightly lower; carryforward increases. The mechanics are the same.

## What Sarah should remember

- Track the $22,860 carryforward in a running schedule (year, basket, original amount, used amount, remaining)
- File Form 8938 if German bank/brokerage assets exceed $200K end-of-year or $300K any time during 2025 (single living abroad threshold)
- File FBAR (FinCEN 114) separately if any foreign account aggregate exceeds $10,000 — separate from tax return, June 30 deadline (auto-extended to October)
- Each year, re-evaluate: if Sarah moves to a low-tax country (Singapore, UAE), FEIE may then be better (subject to 5-year revocation lock-out only if she had previously elected and revoked)
