# Example: Investor with Passive + General Baskets — Two Form 1116s

A US-resident filer who has both foreign passive income (international index fund dividends) and foreign general-basket income (consulting work performed abroad). Demonstrates the two-1116 setup with Part IV summary.

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

Marcus did a 5-week consulting engagement in Madrid for a Spanish client in October 2025. He performed services on-site in Spain.

| Item | EUR | USD (yearly avg 1.082) |
|------|-----|----------------------|
| Consulting fees received | €40,000 | $43,280 |
| Spanish income tax withheld at source (24% non-resident rate) | €9,600 | $10,387 |

Marcus paid $1,200 of project-related expenses (flights, hotel, meals at 50%, local transport — all on Schedule C as definitely-related to the Spain engagement).

### Other income

- US-source consulting fees on Schedule C (other clients): $115,000 (gross)
- US-source consulting expenses on Schedule C: $18,000
- US bank interest: $400
- US dividends (Vanguard VTI, US-source): $3,200

### Tax election

- "Paid" (cash basis) — withholding for Spain occurred in October; Spanish brokerage already paid the dividend foreign tax through 2025
- Standard deduction 2025 single: $15,000 (verify Rev. Proc.)

### De-minimis check (Step 1)

Total foreign tax = $638 (passive) + $10,387 (Spain) = $11,025.

- Total > $300 single → **fails the de-minimis test**
- Also, general-basket income from Spain → fails "all passive" criterion

So full Form 1116 required, one per basket.

## Step-by-step — Passive Basket Form 1116

### Part I (passive)

| Line | Calculation | USD |
|------|------------|-----|
| 1a | Foreign-source dividends | $8,500 |
| 2 | Definitely-related (none) | $0 |
| 3a | Standard deduction | $15,000 |
| 3b | Other pro-rata | $0 |
| 3c | 3a + 3b | $15,000 |
| 3d | Foreign passive gross income | $8,500 |
| 3e | Total gross income (worldwide) | $170,380 (see breakdown below) |
| 3f | 3d / 3e | 0.049890 |
| 3g | 3c × 3f | $748 |
| 4a/4b | Mortgage interest (Marcus rents) | $0 |
| 5 | Foreign losses | $0 |
| 6 | Total deductions | $748 |
| **7** | **Foreign-source taxable income (passive)** | **$7,752** |

**Gross income from all sources (Line 3e)** breakdown:
- US-source wages/SE: $115,000
- US-source dividends: $3,200
- US-source interest: $400
- Foreign passive (dividends): $8,500
- Foreign general (Spain consulting): $43,280
- **Total**: $170,380

### Part II (passive)

Multiple countries (treated as aggregated per IRS instructions for retail 1099-DIV without specific country breakdown):

| Country | USD foreign tax (paid) |
|---------|----------------------|
| Various (per 1099-DIV Box 8 country code) | $638 |
| **Line 8** | **$638** |

### Part III (passive)

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $638 |
| 10 | Carryover (none) | $0 |
| 11 | 9 + 10 | $638 |
| 13 | 11 − 12 | $638 |
| 14 | = Line 7 | $7,752 |
| 15 | QD/LTCG adjustment | $0 (within de-minimis exemption — foreign QD/LTCG well under $20K) |
| 17 | 14 − 15 | $7,752 |
| 18 | Total taxable income (see below) | $137,580 |
| 19 | 17 / 18 | 0.056346 |
| 20 | 19 × US tax before credits | (see below) |
| **21** | **Lesser of 13 or 20** | **(see below)** |

**Total taxable income (Line 18)**: $170,380 gross − $15,000 std deduction − $18,000 US Schedule C expenses − $1,200 Spain Schedule C expenses − $1,600 deductible portion of SE tax = $134,580. (Approximate; actual depends on full Schedule SE calc.)

For simplicity in this example, assume Form 1040 Line 15 = $134,580.

**Form 1040 tax before credits** at 2025 single rates on $134,580:
- ~$26,000 (using 2025 brackets — verify)

- Line 20 = 0.057580 × $26,000 ≈ $1,497
  
  Wait, recompute: Line 19 = 7,752 / 134,580 = 0.057602. Line 20 = 0.057602 × $26,000 = **$1,498**.

- Line 21 (passive) = lesser of $638 or $1,498 = **$638** (full credit)

## Step-by-step — General Basket Form 1116

### Part I (general)

| Line | Calculation | USD |
|------|------------|-----|
| 1a (Country A: Spain) | Gross consulting fees | $43,280 |
| 1b | Compensation for services abroad | $43,280 |
| 2 | Definitely-related (Spain project expenses) | $1,200 |
| 3a | Standard deduction | $15,000 |
| 3b | Other pro-rata | $0 |
| 3c | 3a + 3b | $15,000 |
| 3d | Foreign general gross income | $43,280 |
| 3e | Total gross income | $170,380 |
| 3f | 3d / 3e | 0.254080 |
| 3g | 3c × 3f | $3,811 |
| 4a/4b | Mortgage (rents) | $0 |
| 5 | Foreign losses | $0 |
| 6 | Total deductions | $5,011 |
| **7** | **Foreign-source taxable income (general)** | **$38,269** |

### Part II (general)

| Country | USD foreign tax (paid) | Date |
|---------|----------------------|------|
| Spain (Country A) — non-resident income tax | $10,387 | October 2025 |
| **Line 8** | **$10,387** | |

### Part III (general)

| Line | Calculation | USD |
|------|------------|-----|
| 9 | = Line 8 | $10,387 |
| 10 | Carryover | $0 |
| 11 | 9 + 10 | $10,387 |
| 13 | 11 − 12 | $10,387 |
| 14 | = Line 7 | $38,269 |
| 15 | QD/LTCG (no foreign QD in general basket) | $0 |
| 17 | 14 − 15 | $38,269 |
| 18 | Total taxable income | $134,580 |
| 19 | 17 / 18 | 0.284324 |
| 20 | 19 × US tax before credits ($26,000) | $7,392 |
| **21** | **Lesser of 13 or 20** | **$7,392** |

**Unused FTC general basket**: $10,387 − $7,392 = **$2,995** (carries back 1 year, forward 10 years).

## Summary 1116 — Part IV

The passive 1116 is designated as the summary 1116 (or general; doesn't matter which — IRS just requires one to consolidate).

| Line | Description | USD |
|------|------------|-----|
| 22 | Passive basket Line 21 | $638 |
| 23 | General basket Line 21 | $7,392 |
| 33 | Total credit | $8,030 |
| 35 | Final FTC (Schedule 3 Line 1) | $8,030 |

## The completed deliverable

```markdown
# Form 1116 — DRAFT for tax year 2025 (Multi-basket: Passive + General)

## Filer
Name: Marcus Wright
SSN: XXX-XX-XXXX
Resident country: United States (US)

## Form 1116 #1 — Passive category (Box c)

### Part I
1a. Foreign-source gross income:              $8,500
2.  Definitely-related deductions:            $0
3a. Standard deduction:                       $15,000
3c. Sum:                                      $15,000
3d. Foreign passive gross:                    $8,500
3e. Total gross income:                       $170,380
3f. Ratio:                                    0.049890
3g. Pro-rata foreign share:                   $748
6.  Total deductions:                         $748
7.  Foreign-source taxable income:            $7,752

### Part II (Paid)
8.  Total foreign tax (passive):              $638

### Part III
9-11.   Total available:                      $638
13.     11 − 12:                              $638
14.     = Line 7:                             $7,752
15.     QD/LTCG adjustment:                   $0
17.     14 − 15:                              $7,752
18.     Total taxable income:                 $134,580
19.     17 ÷ 18:                              0.057602
20.     19 × US tax before credits:           $1,498
21.     Lesser of 13 or 20:                   $638

## Form 1116 #2 — General category (Box d)

### Part I
1a. Foreign-source gross income (Spain):      $43,280
1b. Compensation for services abroad:          $43,280
2.  Definitely-related (Spain expenses):       $1,200
3a. Standard deduction:                        $15,000
3c. Sum:                                       $15,000
3d. Foreign general gross:                     $43,280
3e. Total gross income:                        $170,380
3f. Ratio:                                     0.254080
3g. Pro-rata foreign share:                    $3,811
6.  Total deductions:                          $5,011
7.  Foreign-source taxable income:             $38,269

### Part II (Paid)
8.  Total foreign tax (general — Spain):       $10,387

### Part III
9-11.   Total available:                       $10,387
13.     11 − 12:                               $10,387
14.     = Line 7:                              $38,269
15.     QD/LTCG adjustment:                    $0
17.     14 − 15:                               $38,269
18.     Total taxable income:                  $134,580
19.     17 ÷ 18:                               0.284324
20.     19 × US tax before credits:            $7,392
21.     Lesser of 13 or 20:                    $7,392

## Part IV — Summary (consolidated on the General 1116)
22. Passive basket Line 21:                   $638
23. General basket Line 21:                   $7,392
33. Total credit:                             $8,030
35. Final FTC (Schedule 3 Line 1):            $8,030

## Carryover tracking (per basket)
- Passive: Line 13 $638 − Line 21 $638 = $0 unused (full credit; no carryover)
- General: Line 13 $10,387 − Line 21 $7,392 = $2,995 unused
  - Carryback to 2024 (consider amending if room exists)
  - Carryforward through 2035

## Required attachments
- [x] Two Form 1116s (one passive, one general)
- [x] Schedule C reflecting Spain consulting income (with $1,200 expenses) and US consulting
- [x] Schedule SE on combined SE earnings (Spain SE income subject to US SE tax — see note below)
- [ ] Form 8938 if foreign financial assets exceed threshold ($50K single, end of year)

## Validation summary
- Math: all passes
- Sanity:
  - Spain effective rate $10,387 / $43,280 = 24% — matches Spain non-resident statutory rate
  - General basket has unused FTC $2,995 — track carryforward
  - Passive basket fully credited (small amount, well under limitation)
  - $170K total gross + $134K taxable income → $26K US tax → $8,030 FTC → ~$18K residual US tax
- Next steps:
  - SE tax on Spain SE income: Spain has US Totalization Agreement; if Marcus had a Certificate of Coverage from SSA, he'd owe Spanish SS only and not US SE on the Spain portion. Without certificate, default is US SE on all SE income (Spain may still levy its own SS — double SS situation; CPA review needed for Spain SS portion)
  - Track $2,995 general-basket carryforward
  - Re-verify Spain consulting was bona fide foreign-source (services performed IN Spain, not remote work for Spain client from Austin)

## Sources cited in this draft
- IRS Form 1116, Rev. 2025
- IRS Instructions for Form 1116, Rev. 2025
- IRC §901, §904(a)-(d), §905
- Pub. 514
- IRS Yearly Average Currency Exchange Rates (2025 EUR rate)
- US-Spain Tax Treaty (1990, as amended)
- US-Spain Totalization Agreement (1988) — re SE tax / Spanish SS coordination
```

## Why each non-obvious choice

**Why two separate 1116s?** Passive and general baskets have different §904 limitations. They cannot be combined; each must compute its limitation independently. The summary 1116 sums the credits on Part IV.

**Why the standard deduction allocates differently across baskets.** Each basket's allocation ratio uses that basket's gross income / total gross income. So the standard deduction "shares" with each basket proportionally:
- Passive: $748 (small share, 4.99%)
- General: $3,811 (larger share, 25.41%)
- Remaining: $10,441 stays with US-source income (61.27%)
- Sum: $748 + $3,811 + $10,441 = $15,000 ✓

**Why Marcus's Spain expenses ($1,200) are definitely-related (Line 2), not pro-rata.** They were incurred specifically for the Spain engagement (project travel, project expenses). Definitely related = full allocation to that basket. This advantage compounds: it lowers Line 7 in the general basket but doesn't dilute the standard deduction.

**Why the QD/LTCG adjustment is $0.** Marcus's foreign-source dividends are mostly qualified (developed-market dividends often qualify), but his total foreign QD is well under the $20K de-minimis threshold and his bracket is mid-range. He qualifies for the simplified treatment per Pub 514 / Form 1116 instructions worksheet — Line 15 = 0.

**Why Marcus didn't use FEIE for the Spain income.** Two reasons:
1. He doesn't qualify — he was in Spain only 5 weeks (35 days), well short of the 330-day physical presence test
2. Even if he had qualified, FEIE requires being a tax home abroad for the whole period of qualification; Marcus's tax home is Austin (where his US business is)

**Why the Schedule C / SE coordination is tricky.** Marcus's Spain consulting is SE income subject to US SE tax (15.3% on net SE earnings up to $176,100 SS wage base). Spain may also levy Spanish social security under their Totalization Agreement; Marcus could obtain a Certificate of Coverage from US SSA to be exempt from Spain SS while paying US SE only. Without the certificate, double SS may apply. This is a coordination issue separate from Form 1116 — escalate to CPA if material.

## What Marcus should remember

- File the FBAR / FinCEN 114 separately if his Spain bank account (if any) ever exceeded $10,000
- Track the $2,995 general-basket FTC carryforward
- Keep documentation: Spain contract, payment receipts, Spanish withholding statements, travel records (showing services performed IN Spain — not remote)
- Consider obtaining Certificate of Coverage from SSA if he plans more Spain work (avoids Spanish social security)
- Each year, the basket assignment is per income source, not historical — same passive 1099-DIV mix as last year goes to passive again
