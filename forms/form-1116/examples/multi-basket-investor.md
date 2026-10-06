# Example: Investor with Passive + General Baskets — Two Form 1116s

A US-resident filer who has both foreign passive income (international index fund dividends) and foreign general-basket income (consulting work performed abroad). Demonstrates the two-1116 setup with Part IV completed on one of them. Line numbers follow the 2025 Form 1116.

## The filer

- **Name**: Marcus Wright
- **Status**: US citizen, single, lives in Austin TX
- **Profession**: independent management consultant (Schedule C)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered

### Foreign income

**Passive basket (1099-DIV Box 7)**:

| Source | USD dividends | USD foreign tax (Box 7) |
|--------|---------------|------------------------|
| Vanguard VXUS (international developed) | $5,200 | $390 |
| Schwab SCHF (developed ex-US) | $2,100 | $158 |
| iShares EEMV (emerging markets low vol) | $1,200 | $90 |
| **Passive total** | **$8,500** | **$638** |

**General basket (foreign consulting performed in Spain)**:

Marcus did a 5-week consulting engagement in Madrid for a Spanish client in October 2025. He performed services on-site in Spain, working from an office in Madrid that the client keeps regularly available to him for his recurring engagements (Marcus confirmed this). That office is a fixed base, so Spain may tax the income attributable to it (US-Spain income tax treaty, Art. 15(1)). Without a fixed base, Article 15 makes this income taxable only in the US; the Spanish tax would then be refundable from Spain and not creditable (2025 i1116, "Foreign Taxes Not Eligible for a Credit"). The agent must ask before entering foreign tax on services income.

| Item | EUR | USD (ECB rate Oct 31, 2025: 1.1554 USD per EUR) |
|------|-----|----------------------|
| Consulting fees received | €40,000 | $46,216 |
| Spanish income tax withheld at source | €9,600 | $11,092 |

The fee and the withholding are dated October 31, 2025. Marcus claims taxes paid, so the tax uses the exchange rate on the day it was withheld (2025 i1116, "Foreign Currency Conversion"); the fee uses the same day's rate. The agent confirms the €9,600 is his final Spanish liability on that income, not over-withholding he could reclaim.

Marcus paid $1,200 of project-related expenses (flights, hotel, meals at 50%, local transport — all on Schedule C as definitely-related to the Spain engagement).

### Other income

- US-source consulting fees on Schedule C (other clients): $115,000 (gross)
- US-source consulting expenses on Schedule C: $18,000
- US bank interest: $400
- US dividends (Vanguard VTI, US-source): $3,200
- All $11,700 of dividends ($8,500 foreign + $3,200 US) are qualified dividends (Box 1b) — persona assumption

### Tax election

- "Paid" (cash basis) — the Spanish withholding occurred October 31, 2025; the funds' foreign tax is reported in USD on the 1099-DIVs ("1099 taxes")
- Standard deduction 2025 single: $15,750 (2025 Form 1040; P.L. 119-21)

### Return-level figures (2025, single)

| Item | Amount | Source / computation |
|------|--------|----------------------|
| Schedule C net profit | $142,016 | $115,000 + $46,216 − $18,000 − $1,200 |
| SE tax | $20,066 | $142,016 × 92.35% = $131,152; × 12.4% (under the $176,100 wage base) = $16,263; × 2.9% = $3,803 |
| Deductible part of SE tax (Schedule 1 Part II) | $10,033 | half of SE tax |
| AGI (Form 1040 line 11a/11b) | $144,083 | $142,016 + $11,700 + $400 − $10,033 |
| QBI deduction (Form 8995; line 13a) | $18,029 | 20% × QBI of $90,147 (US consulting only: $97,000 − $6,853 share of the SE deduction). The Spain fees aren't effectively connected with a US trade or business, so they aren't QBI (IRC §199A(c)(3)(A)(i)). Taxable income before QBI is under the $197,300 threshold, so the specified-service limits don't apply. Income limit 20% × ($128,333 − $11,700) = $23,327 is higher |
| Form 1040 line 14 | $33,779 | $15,750 + $18,029 |
| Taxable income (line 15) | $110,304 | $144,083 − $33,779 |
| Income tax (line 16) | $18,367 | Qualified Dividends and Capital Gain Tax Worksheet: line 5 = $98,604, Tax Table $16,612 + 15% × $11,700 = $1,755 (regular tax on $110,304 would be $19,320) |

### De-minimis check (Step 1)

Total foreign tax = $638 (passive) + $11,092 (Spain) = $11,730.

- Total > $300 single → **fails the de-minimis test**
- Also, general-basket income from Spain → fails "all passive" criterion

So full Form 1116 required, one per basket.

### Adjustment exception (qualified dividends)

Qualified Dividends and Capital Gain Tax Worksheet line 5 = $98,604 (≤ $197,300) and foreign qualified dividends = $8,500 (< $20,000), so Marcus qualifies for the adjustment exception and elects it: foreign qualified dividends go on line 1a without adjustment, and line 18 is not adjusted (2025 i1116, "Adjustment exception").

## Step-by-step — Passive Basket Form 1116

### Part I (passive)

| Line | Calculation | USD |
|------|------------|-----|
| i | "RIC" (mutual-fund pass-through, one column) | |
| 1a | Foreign-source dividends | $8,500 |
| 2 | Definitely-related (none) | $0 |
| 3a | Standard deduction | $15,750 |
| 3b | Other deductions: deductible part of SE tax (Schedule 1 Part II) | $10,033 |
| 3c | 3a + 3b | $25,783 |
| 3d | Foreign passive gross income | $8,500 |
| 3e | Gross income from all sources | $173,316 (see breakdown below) |
| 3f | 3d / 3e | 0.0490 |
| 3g | 3c × 3f | $1,263 |
| 4a/4b | Mortgage interest (Marcus rents); no other interest expense | $0 |
| 5 | Foreign losses | $0 |
| 6 | 2 + 3g + 4a + 4b + 5 | $1,263 |
| **7** | **Foreign-source taxable income (passive)** | **$7,237** |

**Gross income from all sources (Line 3e)** breakdown:
- US-source Schedule C gross receipts: $115,000
- US-source dividends: $3,200
- US-source interest: $400
- Foreign passive (dividends): $8,500
- Foreign general (Spain consulting gross fees): $46,216
- **Total**: $173,316

The instructions name Schedule 1 Part II adjustments as an example for line 3b, so the deductible part of SE tax is apportioned there; a reviewer who treats it as definitely related to the consulting income would instead apportion it between the US and Spain fees on line 2 of the general form.

### Part II (passive)

RIC pass-through amounts go on one line labeled "RIC" (2025 i1116, "Regulated investment company (RIC) pass-through amounts"):

| Line | Country | (l) Date | (q) Dividends, USD | (u) Total |
|------|---------|----------|--------------------|-----------|
| A | RIC | 1099 taxes | $638 | $638 |
| **8** | | | | **$638** |

### Part III (passive)

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $638 |
| 10 | Carryover (none) | $0 |
| 11 | 9 + 10 | $638 |
| 12 | Reduction in foreign taxes | $0 |
| 13 | High tax kickout (passive taxed well below US rates) | $0 |
| 14 | 11 + 12 + 13 | $638 |
| 15 | = Line 7 | $7,237 |
| 16 | Adjustments | $0 |
| 17 | 15 + 16 | $7,237 |
| 18 | Form 1040 line 11b − line 14 + Schedule 1-A line 37 | $110,304 |
| 19 | 17 / 18 | 0.0656 |
| 20 | Form 1040 line 16 + Schedule 2 line 1z | $18,367 |
| 21 | 20 × 19 | $1,205 |
| 22 | §960(c) increase | $0 |
| 23 | 21 + 22 | $1,205 |
| **24** | **Smaller of 14 or 23** | **$638** (full credit) |

## Step-by-step — General Basket Form 1116

### Part I (general)

| Line | Calculation | USD |
|------|------------|-----|
| i (Country A) | Spain | |
| 1a | Gross consulting fees | $46,216 |
| 1b | Checkbox: not checked (not employee compensation) | — |
| 2 | Definitely-related (Spain project expenses) | $1,200 |
| 3a | Standard deduction | $15,750 |
| 3b | Other deductions (deductible part of SE tax) | $10,033 |
| 3c | 3a + 3b | $25,783 |
| 3d | Foreign general gross income | $46,216 |
| 3e | Gross income from all sources | $173,316 |
| 3f | 3d / 3e | 0.2667 |
| 3g | 3c × 3f | $6,876 |
| 4a/4b | Mortgage (rents); no other interest expense | $0 |
| 5 | Foreign losses | $0 |
| 6 | 2 + 3g + 4a + 4b + 5 | $8,076 |
| **7** | **Foreign-source taxable income (general)** | **$38,140** |

### Part II (general)

| Line | Country | (l) Date paid | (p) Other foreign taxes, EUR | (t) USD | (u) Total |
|------|---------|---------------|------------------------------|---------|-----------|
| A | Spain | 10/31/2025 | €9,600 | $11,092 | $11,092 |
| **8** | | | | | **$11,092** |

### Part III (general)

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $11,092 |
| 10 | Carryover | $0 |
| 11 | 9 + 10 | $11,092 |
| 12 | Reduction in foreign taxes | $0 |
| 13 | High tax kickout | $0 |
| 14 | 11 + 12 + 13 | $11,092 |
| 15 | = Line 7 | $38,140 |
| 16 | Adjustments | $0 |
| 17 | 15 + 16 | $38,140 |
| 18 | Form 1040 line 11b − line 14 + Schedule 1-A line 37 | $110,304 |
| 19 | 17 / 18 | 0.3458 |
| 20 | Form 1040 line 16 + Schedule 2 line 1z | $18,367 |
| 21 | 20 × 19 | $6,351 |
| 22 | §960(c) increase | $0 |
| 23 | 21 + 22 | $6,351 |
| **24** | **Smaller of 14 or 23** | **$6,351** |

**Unused foreign tax, general basket**: $11,092 − $6,351 = **$4,741** (carries back 1 year, forward 10 years; Schedule B (Form 1116) for the general category).

## Part IV — Summary of separate credits

Part IV is completed on the Form 1116 with the largest line 24: the general form ($6,351). The passive form is attached behind it (2025 i1116, Part IV).

| Line | Description | USD |
|------|------------|-----|
| 27 | Passive category credit (passive line 24) | $638 |
| 28 | General category credit (general line 24) | $6,351 |
| 32 | Add lines 25 through 31 | $6,989 |
| 33 | Smaller of line 20 ($18,367) or line 32 | $6,989 |
| 34 | Boycott reduction | $0 |
| 35 | Foreign tax credit (Schedule 3 Line 1) | $6,989 |

## The completed deliverable

```markdown
# Form 1116 — DRAFT for tax year 2025 (Multi-basket: Passive + General)

## Filer
Name: Marcus Wright
SSN: XXX-XX-XXXX
h. Resident of: United States

## Form 1116 #1 — Passive category (Box c)

### Part I
i.  Column A:                                 RIC
1a. Foreign-source gross income:              $8,500
2.  Definitely-related deductions:            $0
3a. Standard deduction:                       $15,750
3b. Other deductions (SE tax deduction):      $10,033
3c. Sum:                                      $25,783
3d. Foreign passive gross:                    $8,500
3e. Total gross income:                       $173,316
3f. Ratio:                                    0.0490
3g. Pro-rata foreign share:                   $1,263
4a/4b. Interest expense:                      $0
5.  Losses:                                   $0
6.  2 + 3g + 4a + 4b + 5:                     $1,263
7.  Foreign-source taxable income:            $7,237

### Part II ((j) Paid)
A.  RIC, (l) 1099 taxes, (q) $638, (u) $638
8.  Total foreign tax (passive):              $638

### Part III
9-11.   Total available:                      $638
12-13.  Reductions / HTKO:                    $0
14.     11 + 12 + 13:                         $638
15.     = Line 7:                             $7,237
16.     Adjustments:                          $0
17.     15 + 16:                              $7,237
18.     1040 line 11b − line 14 + 1-A 37:     $110,304
19.     17 ÷ 18:                              0.0656
20.     1040 line 16 + Sch. 2 line 1z:        $18,367
21.     20 × 19:                              $1,205
22-23.  §960(c) / 21 + 22:                    $0 / $1,205
24.     Smaller of 14 or 23:                  $638

## Form 1116 #2 — General category (Box d)

### Part I
i.  Column A:                                  Spain
1a. Foreign-source gross income (Spain):      $46,216
1b. Alternative-basis compensation box:        not checked
2.  Definitely-related (Spain expenses):       $1,200
3a. Standard deduction:                        $15,750
3b. Other deductions (SE tax deduction):       $10,033
3c. Sum:                                       $25,783
3d. Foreign general gross:                     $46,216
3e. Total gross income:                        $173,316
3f. Ratio:                                     0.2667
3g. Pro-rata foreign share:                    $6,876
4a/4b. Interest expense:                       $0
5.  Losses:                                    $0
6.  2 + 3g + 4a + 4b + 5:                      $8,076
7.  Foreign-source taxable income:             $38,140

### Part II ((j) Paid)
A.  Spain, (l) 10/31/2025, (p) €9,600, (t) $11,092, (u) $11,092
8.  Total foreign tax (general — Spain):       $11,092

### Part III
9-11.   Total available:                       $11,092
12-13.  Reductions / HTKO:                     $0
14.     11 + 12 + 13:                          $11,092
15.     = Line 7:                              $38,140
16.     Adjustments:                           $0
17.     15 + 16:                               $38,140
18.     1040 line 11b − line 14 + 1-A 37:      $110,304
19.     17 ÷ 18:                               0.3458
20.     1040 line 16 + Sch. 2 line 1z:         $18,367
21.     20 × 19:                               $6,351
22-23.  §960(c) / 21 + 22:                     $0 / $6,351
24.     Smaller of 14 or 23:                   $6,351

## Part IV — Summary (on the General 1116, the larger line 24)
27. Passive category credit:                  $638
28. General category credit:                  $6,351
32. Add lines 25 through 31:                  $6,989
33. Smaller of line 20 or line 32:            $6,989
34. Boycott reduction:                        $0
35. Foreign tax credit (Schedule 3 Line 1):   $6,989

## Carryover tracking (per basket)
- Passive: Line 14 $638 − Line 24 $638 = $0 unused (full credit; no carryover)
- General: Line 14 $11,092 − Line 24 $6,351 = $4,741 unused
  - Carryback to 2024 (consider amending if room exists)
  - Carryforward through 2035
  - Schedule B (Form 1116) attached for the general category

## Required attachments
- [x] Two Form 1116s (one passive, one general), Part IV on the general form
- [x] Schedule B (Form 1116), general category
- [x] Statements: line 2 expense list, line 3b list (SE tax deduction), currency conversion (ECB rate for Oct 31, 2025)
- [x] Schedule C reflecting Spain consulting income (with $1,200 expenses) and US consulting
- [x] Schedule SE on combined SE earnings (Spain SE income subject to US SE tax — see note below)
- [x] Form 8995 (QBI deduction, US consulting only)
- [ ] Form 8938 if foreign financial assets exceed threshold (unmarried, living in the US: more than $50,000 on the last day of the year or $75,000 at any time)

## Validation summary
- Math: all passes
  - Passive: 3f = $8,500 / $173,316 = 0.0490; 3g = $25,783 × 0.0490 = $1,263; line 7 = $7,237; line 19 = 0.0656; line 21 = $1,205; line 24 = $638
  - General: 3f = $46,216 / $173,316 = 0.2667; 3g = $6,876; line 6 = $1,200 + $6,876 = $8,076; line 7 = $38,140; line 19 = 0.3458; line 21 = $6,351; line 24 = $6,351
  - Line 35 $6,989 ≤ Line 20 $18,367
- Sanity:
  - Spanish tax / fees = $11,092 / $46,216 = 24.0% — confirm against Marcus's Spanish withholding statement
  - General basket has unused foreign tax $4,741 — track carryforward
  - Passive basket fully credited (small amount, well under limitation)
  - $173,316 gross income, $110,304 taxable income → $18,367 income tax → $6,989 FTC → $11,378 income tax after the credit (SE tax of $20,066 is separate and not reduced by the FTC)
- Next steps:
  - SE tax on Spain SE income: Marcus resides in the US, so the US-Spain social security agreement assigns his self-employment to US coverage only: US SE tax applies to all his net SE earnings, including the Spain portion, and Spain should not levy social security on it. A US certificate of coverage documents this for Spain; CPA review if Spain assesses its social security anyway
  - Track $4,741 general-basket carryforward
  - Re-verify Spain consulting was bona fide foreign-source (services performed IN Spain, not remote work for Spain client from Austin) and that the Madrid office is a fixed base

## Sources cited in this draft
- IRS Form 1116 (2025), created 9/16/25
- IRS Instructions for Form 1116 (2025), Dec 23, 2025 (RIC pass-through amounts, "1099 taxes", adjustment exception, lines 3b, 18, 20, Part IV)
- IRC §901, §904(a)-(d), §905; IRC §199A(c)(3)(A)(i)
- Pub. 514
- Rev. Proc. 2024-40 (2025 rates, $197,300 threshold); 2025 Form 1040 (standard deduction $15,750); 2025 Schedule SE ($176,100 wage base)
- ECB euro reference rate, Oct 31, 2025 (1.1554 USD per EUR)
- US-Spain Tax Treaty (1990, as amended), Art. 15
- US-Spain Totalization Agreement (1988) — re SE tax / Spanish SS coordination (SSA, "Totalization Agreement with Spain")
```

## Why each non-obvious choice

**Why two separate 1116s?** Passive and general baskets have different §904 limitations. They cannot be combined; each must compute its limitation independently. Part IV, completed on the form with the largest line 24, sums the credits.

**Why the line 3 deductions allocate differently across baskets.** Each basket's allocation ratio uses that basket's gross income / total gross income. So the standard deduction plus the SE tax deduction ($25,783 on line 3c) "shares" with each basket proportionally:
- Passive: $1,263 (small share, 4.90%)
- General: $6,876 (larger share, 26.67%)
- Remaining: $17,644 stays with US-source income (68.43%)
- Sum: $1,263 + $6,876 + $17,644 = $25,783 ✓

**Why Marcus's Spain expenses ($1,200) are definitely-related (Line 2), not pro-rata.** They were incurred specifically for the Spain engagement (project travel, project expenses). Definitely related = full allocation to that basket. This advantage compounds: it lowers Line 7 in the general basket but doesn't dilute the standard deduction.

**Why there is no QD/LTCG adjustment.** Marcus's foreign-source dividends are qualified, but he meets both tests of the adjustment exception: line 5 of the Qualified Dividends and Capital Gain Tax Worksheet is $98,604 (not more than $197,300) and his foreign qualified dividends are $8,500 (less than $20,000). He elects it by not adjusting, so line 1a carries the full $8,500 and line 18 is unadjusted (2025 i1116, "Adjustment exception").

**Why Marcus didn't use FEIE for the Spain income.** Two reasons:
1. He doesn't qualify — he was in Spain only 5 weeks (35 days), well short of the 330-day physical presence test
2. Even if he had qualified, FEIE requires being a tax home abroad for the whole period of qualification; Marcus's tax home is Austin (where his US business is)

**Why the Schedule C / SE coordination is tricky.** Marcus's Spain consulting is SE income subject to US SE tax (12.4% on net SE earnings up to the $176,100 2025 wage base plus 2.9% on all of them). Under the US-Spain social security agreement, a self-employed person who resides in the US is covered only by the US system, so Spain should not collect social security on this work; a certificate of coverage from SSA documents that. If Spain assesses its social security anyway, that is a coordination issue separate from Form 1116 — escalate to CPA if material.

## What Marcus should remember

- File the FBAR / FinCEN 114 separately if his Spain bank account (if any) ever exceeded $10,000
- Track the $4,741 general-basket foreign tax carryforward (Schedule B (Form 1116))
- Keep documentation: Spain contract, payment receipts, Spanish withholding statements, travel records (showing services performed IN Spain — not remote), and evidence of the Madrid office arrangement
- Consider obtaining Certificate of Coverage from SSA if he plans more Spain work (avoids Spanish social security)
- Each year, the basket assignment is per income source, not historical — same passive 1099-DIV mix as last year goes to passive again
