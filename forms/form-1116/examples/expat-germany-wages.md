# Example: US Expat Working in Germany — Full Form 1116 General Basket

A US citizen working as an employee in Germany for a German employer. German tax (about 33% of her wages here) is well above her US tax, so she chooses FTC over FEIE; this walkthrough produces the full Form 1116 (general basket) and shows the §904 limitation math. Line numbers follow the 2025 Form 1116.

## The filer

- **Name**: Sarah Chen
- **Status**: US citizen, single, lives in Munich since 2021
- **Profession**: software engineer at SAP (W-2 equivalent — German Lohnsteuer)
- **US-source income**: $1,200 of interest only (Sarah works exclusively for her German employer)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Foreign income

| Source | Currency | Amount | USD (yearly avg) |
|--------|----------|--------|------------------|
| SAP gross salary 2025 | EUR | €110,000 | $124,153 |
| Year-end bonus | EUR | €10,000 | $11,287 |
| **Line 1a (general basket)** | | **€120,000** | **$135,440** |

Income is translated at the IRS 2025 yearly average rate for the euro, 0.886 euros per dollar: divide the euro amount by 0.886 (€120,000 ÷ 0.886 = $135,440). Source: https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates (the IRS accepts any posted rate used consistently).

### Foreign tax (German Lohnsteuer + Solidaritätszuschlag)

Sarah claims taxes on the paid basis, so each payroll withholding is translated at the rate on the day it was withheld, not the yearly average (2025 i1116, "Foreign Currency Conversion"). Her employer withheld €3,000 Lohnsteuer and €165 Soli each month, and €5,000 / €275 in December with the bonus. Rates: ECB euro reference rate (US dollars per euro) on each payday.

| Payday 2025 | USD per EUR | Lohnsteuer EUR | USD | Soli EUR | USD |
|-------------|-------------|----------------|-----|----------|-----|
| Jan 31 | 1.0393 | €3,000 | $3,118 | €165 | $171 |
| Feb 28 | 1.0411 | €3,000 | $3,123 | €165 | $172 |
| Mar 31 | 1.0815 | €3,000 | $3,244 | €165 | $178 |
| Apr 30 | 1.1373 | €3,000 | $3,412 | €165 | $188 |
| May 30 | 1.1339 | €3,000 | $3,402 | €165 | $187 |
| Jun 30 | 1.1720 | €3,000 | $3,516 | €165 | $193 |
| Jul 31 | 1.1446 | €3,000 | $3,434 | €165 | $189 |
| Aug 29 | 1.1658 | €3,000 | $3,497 | €165 | $192 |
| Sep 30 | 1.1741 | €3,000 | $3,522 | €165 | $194 |
| Oct 31 | 1.1554 | €3,000 | $3,466 | €165 | $191 |
| Nov 28 | 1.1566 | €3,000 | $3,470 | €165 | $191 |
| Dec 31 | 1.1750 | €5,000 | $5,875 | €275 | $323 |
| **Total** | | **€38,000** | **$43,079** | **€2,090** | **$2,369** |

| Tax type | EUR | USD |
|----------|-----|-----|
| Lohnsteuer (income tax withheld) | €38,000 | $43,079 |
| Solidaritätszuschlag (solidarity surcharge) | €2,090 | $2,369 |
| Kirchensteuer (church tax) | €0 | $0 (Sarah opted out) |
| **Total foreign tax (Line 8)** | **€40,090** | **$45,448** |

(Note: German social security contributions — Rentenversicherung, Krankenversicherung, etc. — are left off Form 1116. No credit or deduction is allowed for social security taxes paid to a country that has a social security agreement with the US, and Germany has one (Pub. 514; agreement list in the 2025 Schedule SE instructions). Contributions outside the agreement's coverage would need a separate creditability review; see [`non-creditable-taxes.md`](../references/non-creditable-taxes.md).)

### Tax election

- Sarah elects "Paid" (cash basis) — most common for individuals
- Method binding implications for accrual not relevant

### Sarah's other facts

- No US-source wages (lived/worked in Germany all year)
- $1,200 US-source interest from Schwab money market (USD)
- Standard deduction 2025 single: $15,750 (2025 Form 1040; P.L. 119-21)
- Bona fide resident of Germany since 2021 — qualifies for FEIE if she elected, but FEIE is suboptimal at her income level (see Why FTC over FEIE below)

### FEIE coordination check

Sarah considered FEIE (Form 2555) but rejected it:

- Foreign earned income $135,440 vs. FEIE cap $130,000 (2025) — FEIE would exclude $130,000 and leave $5,440 of wages taxable
- Her German tax is $45,448 — much more than her US tax on the same income ($21,861 at 2025 single rates)
- With FTC, the credit wipes out US tax on the German wages ($21,669); $192 of US tax on the US-source interest remains, and $23,779 of unused German tax carries over
- With FEIE, AGI drops to $6,640 (below the standard deduction), so US income tax is $0, but the German tax allocable to the excluded wages ($45,448 × 130,000 / 135,440 = $43,623) can never be credited or carried, and the excluded wages don't count as IRA compensation
- Final choice: **FTC (Form 1116) general basket**: $192 more US tax this year in exchange for the carryover and IRA eligibility

See [`coordination-with-2555.md`](../references/coordination-with-2555.md).

## Step-by-step Form 1116

### Part I — Foreign-source taxable income (general basket)

| Line | Calculation | USD |
|------|------------|-----|
| h | Resident of | Germany |
| i (Country A) | Germany | |
| 1a (Country A: Germany) | Gross wages | $135,440 |
| 1b | Checkbox: not checked (compensation under $250,000; time basis) | — |
| 2 | Definitely related deductions (none) | $0 |
| 3a | Standard deduction | $15,750 |
| 3b | Other deductions (none) | $0 |
| 3c | 3a + 3b | $15,750 |
| 3d | Foreign general-basket gross income | $135,440 |
| 3e | Gross income from all sources | $136,640 ($135,440 + $1,200 US interest) |
| 3f | 3d / 3e, at least 4 decimals | 0.9912 |
| 3g | 3c × 3f | $15,611 |
| 4a | Home mortgage interest | $0 (Sarah rents) |
| 4b | Other interest expense | $0 |
| 5 | Foreign losses | $0 |
| 6 | 2 + 3g + 4a + 4b + 5 | $15,611 |
| **7** | **1a − 6 (foreign-source taxable income)** | **$119,829** |

### Part II — Foreign taxes paid

Box (j) Paid. Country A (Germany), one line; column (l) "Various 2025 paydays (statement attached)" with the payday table above as the conversion explanation:

| Column | EUR | USD |
|--------|-----|-----|
| (p) / (t) Other foreign taxes paid: Lohnsteuer + Soli | €40,090 | $45,448 |
| (u) Total | | $45,448 |
| **Line 8 — Total** | | **$45,448** |

### Part III — Figuring the credit (§904 limitation)

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $45,448 |
| 10 | Carryover / carryback (none) | $0 |
| 11 | 9 + 10 | $45,448 |
| 12 | Reduction in foreign taxes (no Form 2555, no other reduction) | $0 |
| 13 | High tax kickout (general category; n/a) | $0 |
| 14 | 11 + 12 + 13 | $45,448 |
| 15 | = Line 7 | $119,829 |
| 16 | Adjustments (no losses) | $0 |
| 17 | 15 + 16 | $119,829 |
| 18 | Form 1040 line 11b − line 14 + Schedule 1-A line 37 | $120,890 ($136,640 − $15,750 + $0) |
| 19 | 17 / 18 | 0.9912 |
| 20 | Form 1040 line 16 + Schedule 2 line 1z | $21,861 (see calc below) |
| 21 | 20 × 19 | $21,669 |
| 22 | §960(c) increase | $0 |
| 23 | 21 + 22 | $21,669 |
| **24** | **Smaller of 14 or 23** | **$21,669** |

#### Computing Line 20

Sarah's Form 1040 line 16 tax at 2025 single rates (Rev. Proc. 2024-40 Table 3; taxable income is $100,000 or more, so the Tax Computation Worksheet applies, not the Tax Table):

Calculation on taxable income $120,890:
- 10% on first $11,925 = $1,192.50
- 12% on next $36,550 ($11,925-$48,475) = $4,386.00
- 22% on next $54,875 ($48,475-$103,350) = $12,072.50
- 24% on remaining $17,540 ($103,350-$120,890) = $4,209.60
- **Form 1040 line 16 = $21,860.60 → $21,861**; Schedule 2 line 1z = $0

- Line 21 = $21,861 × 0.9912 = **$21,669**
- Line 24 = smaller of $45,448 or $21,669 = **$21,669**

#### Part IV (required for 2025 even with one Form 1116)

| Line | Calculation | USD |
|------|------------|-----|
| 28 | General category credit (line 24) | $21,669 |
| 25-27, 29-31 | Other categories | $0 |
| 32 | Add lines 25 through 31 | $21,669 |
| 33 | Smaller of line 20 ($21,861) or line 32 | $21,669 |
| 34 | Boycott reduction | $0 |
| **35** | **Foreign tax credit → Schedule 3 line 1** | **$21,669** |

US income tax after the credit: $21,861 − $21,669 = $192 (the US tax on the US-source interest, which the limitation keeps out of reach).

### Unused foreign tax

Line 14 ($45,448) − Line 24 ($21,669) = **$23,779 unused** (Schedule B (Form 1116) attached for the general category)

This carries:
- Back 1 year (Sarah could amend her 2024 return if 2024 had limitation room — likely not, since she had similar facts)
- Forward 10 years (until 2035)

## The completed Form 1116 draft

```markdown
# Form 1116 — DRAFT for tax year 2025 (Category: General — Box d)

## Header
Filer name: Sarah Chen
SSN/ITIN: XXX-XX-XXXX
Category (a-g): (d) General category income
h. Resident of: Germany

## Part I — Foreign-source taxable income
i. Country column A: Germany
1a. Gross foreign-source income:
    Germany: $135,440
    Total: $135,440
1b. Alternative-basis compensation box:        not checked
2.  Definitely-related deductions:            $0
3a. Standard deduction:                       $15,750
3b. Other deductions:                         $0
3c. 3a + 3b:                                  $15,750
3d. Foreign-source gross income:              $135,440
3e. Gross income from all sources:            $136,640
3f. 3d ÷ 3e:                                  0.9912
3g. 3c × 3f:                                  $15,611
4a. Home mortgage interest:                   $0
4b. Other interest expense:                   $0
5.  Losses from foreign sources:              $0
6.  2 + 3g + 4a + 4b + 5:                     $15,611
7.  1a − 6:                                   $119,829

## Part II — Foreign taxes paid ((j) Paid)
| Line | Country | (l) Date paid | (p) Other foreign taxes, EUR | (t) USD | (u) Total USD |
|------|---------|---------------|------------------------------|---------|---------------|
| A    | Germany | Various 2025 paydays (statement attached) | €40,090 | $45,448 | $45,448 |
8. Total foreign tax (USD):                   $45,448

## Part III — Figuring the credit
9.  = Line 8:                                 $45,448
10. Carryover (Schedule B) + carrybacks:      $0
11. 9 + 10:                                   $45,448
12. Reduction in foreign taxes:               $0
13. High tax kickout reclassification:        $0
14. 11 + 12 + 13:                             $45,448
15. = Line 7:                                 $119,829
16. Adjustments to line 15:                   $0
17. 15 + 16:                                  $119,829
18. Taxable income (1040 11b − 14 + 1-A 37):  $120,890
19. 17 ÷ 18:                                  0.9912
20. 1040 line 16 + Sch. 2 line 1z:            $21,861
21. 20 × 19:                                  $21,669
22. §960(c) increase:                         $0
23. 21 + 22:                                  $21,669
24. Smaller of 14 or 23:                      $21,669

## Part IV (required for 2025 even with one Form 1116)
28. General category credit:                  $21,669
32. Add lines 25 through 31:                  $21,669
33. Smaller of line 20 or line 32:            $21,669
34. Boycott reduction:                        $0
35. Foreign tax credit (Schedule 3 line 1):   $21,669

## Carryover tracking
Unused foreign tax this year (Line 14 − Line 24), general basket: $45,448 − $21,669 = $23,779
  - Carryback to 2024: consider amending if 2024 had limitation room
  - Carryforward to 2026 onwards (through 2035 max)
  - Schedule B (Form 1116) attached for the general category

## Required attachments
- [x] Form 1116 (general basket, this draft), Part IV completed
- [x] Schedule B (Form 1116), general category (new carryover generated)
- [x] Statement: currency conversion (payday table with ECB reference rates; IRS 2025 yearly average 0.886 for wages)
- [ ] Form 8938 if foreign financial assets exceed reporting threshold ($200K end of year / $300K any time, unmarried living abroad)
- [ ] FBAR / FinCEN 114 if German bank account aggregate > $10,000 at any point in year (separate filing, not attached to 1040)

## Validation summary
- Math: all checks passed
  - Line 3f = $135,440 / $136,640 = 0.9912; Line 3g = $15,750 × 0.9912 = $15,611 ✓
  - Line 6 = $0 + $15,611 + $0 + $0 + $0 = $15,611 ✓
  - Line 7 = $135,440 − $15,611 = $119,829 ✓
  - Line 19 = $119,829 / $120,890 = 0.9912 ✓
  - Line 21 = $21,861 × 0.9912 = $21,669; Line 24 = smaller of $45,448 or $21,669 = $21,669 ✓
  - Line 35 $21,669 ≤ Line 20 $21,861 ✓
- Sanity:
  - Foreign tax / foreign income = $45,448 / $135,440 = 33.6% (33.4% in euros) — plausible German rate at this income
  - Unused foreign tax $23,779 — significant; track carryforward
  - Sarah passes bona fide residence test → could elect FEIE; chose FTC instead based on tax-rate analysis
- Next steps:
  - File 2025 return with Form 1116 attached
  - Track carryforward schedule by basket
  - Confirm Form 8938 / FBAR thresholds
  - Re-evaluate FEIE vs. FTC each year if circumstances change

## Sources cited in this draft
- IRS Form 1116 (2025), created 9/16/25
- IRS Instructions for Form 1116 (2025), Dec 23, 2025 ("Foreign Currency Conversion", Part II, Part III, Part IV)
- IRC §901, §904(a)-(c), §905
- Pub. 514 — Foreign Tax Credit for Individuals
- Pub. 54 — US Citizens and Resident Aliens Abroad
- Rev. Proc. 2024-40 (2025 tax rates); 2025 Form 1040 (standard deduction $15,750)
- IRS Yearly Average Currency Exchange Rates (2025 EUR 0.886); ECB euro reference rates (payday rates)
- US-Germany Tax Treaty (1989, as amended)
- US-Germany Totalization Agreement (1979, for SS-equivalent treatment)
```

## Why each non-obvious choice

**Why general basket (d), not passive (c)?** Wages are general-category income under IRC §904(d). Passive is for dividends, interest, royalties. Sarah's salary goes in general regardless of country.

**Why "Paid" not "Accrued"?** Sarah pays German tax via withholding throughout the year — cash basis matches her actual cash flow. "Accrued" would be appropriate if she had a year-end true-up that lands in the next year, but her German employer withholds full liability monthly.

**Why no Line 4 home mortgage allocation?** Sarah rents her Munich apartment. Renters have no mortgage interest, so Line 4a/4b = $0. If she owned her German apartment, there would be additional allocation work.

**Why FEIE wasn't chosen.** Sarah's German tax of $45,448 vastly exceeds her US tax on the same income ($21,861). FEIE would exclude $130,000 of the wages and bring US income tax to $0, but the $43,623 of German tax allocable to the excluded wages could never be credited or carried. FTC costs $192 more this year (US tax on the US-source interest) and preserves $23,779 as a carryforward (10-year window), which has value only if she later has unused limitation in the general category. FEIE also blocks IRA contributions based on the excluded wages (excluded income isn't compensation for IRA purposes; Pub. 590-A); FTC preserves that option.

**Why no QD/LTCG adjustment (lines 1a and 18 unadjusted)?** Sarah has no qualified dividends or capital gains, foreign or US — only wages and interest. The line 1a and line 18 adjustments apply only when the return includes preferential-rate items. See [`qualified-dividend-adjustment.md`](../references/qualified-dividend-adjustment.md).

**What if Sarah's situation included $5,000 of US-source wages (e.g., a side gig she did while visiting the US)?** US-source income reduces Line 19 (it stays in the denominator at full rate, but doesn't add to the numerator). Limitation goes down slightly, FTC may be slightly lower; carryforward increases. The mechanics are the same.

## What Sarah should remember

- Track the $23,779 carryforward in a running schedule (year, basket, original amount, used amount, remaining) and on Schedule B (Form 1116)
- File Form 8938 if German bank/brokerage assets exceed $200K end-of-year or $300K any time during 2025 (unmarried living abroad threshold; 2025 Instructions for Form 8938)
- File FBAR (FinCEN 114) separately if any foreign account aggregate exceeds $10,000 — separate from tax return, due April 15 with an automatic extension to October 15 (IRS FBAR page)
- Each year, re-evaluate: if Sarah moves to a low-tax country (Singapore, UAE), FEIE may then be better (subject to 5-year revocation lock-out only if she had previously elected and revoked)
