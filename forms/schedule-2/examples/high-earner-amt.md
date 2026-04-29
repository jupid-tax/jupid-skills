# Example: High Earner with ISO Exercise Triggering AMT

A complete walkthrough of Schedule 2 for a single tech employee who exercised and held incentive stock options, triggering AMT (Form 6251 → Schedule 2 Line 1). Also has small NIIT exposure from dividends.

## The filer

- **Name**: Daniel Park
- **Filing status**: Single
- **Occupation**: Senior software engineer at a private tech company
- **W-2 wages (Box 1)**: $284,000
- **W-2 Medicare wages (Box 5)**: $310,000 (RSU vesting + bonus pushed Medicare wages above Box 1)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### ISO exercise

- 12,000 ISO shares exercised on June 14, 2025
- Strike price: $4 / share
- FMV at exercise: $19 / share
- Bargain element: ($19 − $4) × 12,000 = **$180,000**
- Daniel held the shares past 12/31/2025 (no qualifying disposition in 2025)
- → AMT preference under IRC §56(b)(3) and §57(a)(8): $180,000 added to AMTI

### Other AMT items

- State income tax deducted on Schedule A: $24,800 (capped at $10,000 by SALT cap; the deducted amount is added back to AMTI)
- Property tax: $0 (renter)
- Misc itemized deductions: $0 (TCJA suspended)
- No private activity bond interest
- No depreciation differences

### Investment income

- Brokerage account dividends (taxable): $4,200
- Brokerage account capital gains (long-term, sold in 2025): $11,500
- Brokerage interest (taxable): $620
- Total investment income: $16,320

### NIIT analysis

- MAGI = AGI = approximately $290,000 (after adjustments)
- Filing status threshold: $200,000 (single)
- MAGI excess over threshold: $90,000
- Net investment income: $16,320
- NIIT base = lesser of $16,320 or $90,000 = $16,320
- NIIT = 3.8% × $16,320 = **$620**

### Additional Medicare Tax analysis

- Medicare wages: $310,000
- Filing-status threshold: $200,000 (single)
- Wages above threshold: $110,000
- Additional Medicare Tax = 0.9% × $110,000 = **$990**
- Employer withheld 0.9% × ($310,000 − $200,000) = $990 ✓ (no excess or shortfall in this case; employer was correct because Daniel is single with one job)

### No SE income

- No Schedule SE; Line 4 = $0

### No early retirement distributions, no household employees, no ACA marketplace

- Lines 2, 5, 6, 8, 9, 10 = $0

## Form 6251 result

Daniel's preparer ran Form 6251:

- AMTI (Line 4): regular taxable income $266,400 + ISO bargain element $180,000 + SALT add-back $10,000 = **$456,400**
- AMT exemption (Line 5): single 2025 exemption $88,100, phaseout starts $626,350 → Daniel below phaseout, full exemption applies = $88,100
- AMTI after exemption (Line 6): $456,400 − $88,100 = $368,300
- Tentative minimum tax (Line 7): 26% × $239,100 + 28% × ($368,300 − $239,100) = $62,166 + $36,176 = **$98,342**
- Regular tax (Line 9): $63,140 (from regular tax computation)
- AMT (Line 11): $98,342 − $63,140 = **$35,202**

→ **Schedule 2 Line 1 = $35,202**

## Form 8960 result (NIIT)

→ **Schedule 2 Line 12 = $620**

## Form 8959 result (Additional Medicare Tax)

- Form 8959 Line 18 = $990
- Form 8959 Line 24 (withheld) = $990 → flows to Form 1040 Line 25c (NOT Schedule 2)

→ **Schedule 2 Line 11 = $990**

## The completed Schedule 2 draft

```markdown
# Schedule 2 (Form 1040) — DRAFT for tax year 2025

## Header
Name(s) shown on Form 1040: Daniel Park
Your social security number: XXX-XX-XXXX

## Part I — Tax
 1.  Alternative minimum tax. Attach Form 6251:           $35,202
 2.  Excess advance premium tax credit repayment.
     Attach Form 8962:                                    $0
 3.  Add lines 1 and 2. Enter here and on Form 1040,
     1040-SR, or 1040-NR, line 17:                        $35,202

## Part II — Other Taxes
 4.  Self-employment tax. Attach Schedule SE:             $0
 5.  Social security and Medicare tax on unreported
     tip income. Attach Form 4137:                        $0
 6.  Uncollected social security and Medicare tax on
     wages. Attach Form 8919:                             $0
 7.  Total additional social security and Medicare tax.
     Add lines 5 and 6:                                   $0
 8.  Additional tax on IRAs or other tax-favored accounts.
     Attach Form 5329 if required:                        $0
 9.  Household employment taxes. Attach Schedule H:       $0
10.  Repayment of first-time homebuyer credit.
     Attach Form 5405 if required:                        $0
11.  Additional Medicare Tax. Attach Form 8959:           $990
12.  Net investment income tax. Attach Form 8960:         $620
13.  Section 965 net tax liability. From Form 965-A:      $0
14.  Interest on tax due on installment income from sale
     of certain residential lots and timeshares:          $0
15.  Interest on the deferred tax on gain from certain
     installment sales > $150,000:                        $0
16.  Recapture of low-income housing credit.
     Attach Form 8611:                                    $0
17.  Other additional taxes:                              $0
18.  Total Other Additional Taxes (sum of 17a–17z):       $0
19.  Reserved for future use:                             —
20.  Section 965 net tax liability installment from
     Form 965-A (does not roll into Line 21):             $0
21.  Add lines 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
     and 18. Enter here and on Form 1040, 1040-SR, or
     1040-NR, line 23:                                    $1,610

## Form 1040 routing
Form 1040 Line 17 (from Schedule 2 Line 3):               $35,202
Form 1040 Line 23 (from Schedule 2 Line 21):              $1,610

## Required upstream forms attached
- [x] Form 6251 (Line 1 = $35,202)
- [x] Form 8959 (Line 11 = $990)
- [x] Form 8960 (Line 12 = $620)

## Validation summary
- Math:
  - Line 3 = $35,202 + $0 = $35,202 ✓
  - Line 21 = $0 + $0 + $0 + $0 + $0 + $990 + $620 + $0 + $0 + $0 + $0 + $0 = $1,610 ✓
- Cross-form: 6251, 8959, 8960 all attached
- Sanity:
  - AMT $35,202 is large but proportionate to $180K ISO bargain element — confirmed
  - Additional Medicare Tax $990 with $310K Medicare wages — within expected range
  - NIIT $620 with $16,320 investment income at 3.8% — within expected range

## Sources cited in this draft
- IRS Form 1040 Schedule 2, Rev. 2025
- IRS Instructions for Form 1040 and 1040-SR, Rev. 2025, Schedule 2 section
- IRC §55, §56(b)(3), §57(a)(8) (ISO bargain element AMT preference)
- IRC §1411 (NIIT)
- IRC §3101(b)(2) (Additional Medicare Tax)
- Rev. Proc. 2024-40 (2025 AMT exemption $88,100 single)
- Form 6251 Instructions (i6251), 2025 revision
- Form 8959 Instructions (i8959), 2025 revision
- Form 8960 Instructions (i8960), 2025 revision
```

## Why each non-obvious choice

**Why didn't the SALT cap eliminate the AMT preference?** TCJA capped the *regular-tax* deduction at $10K, but the AMT add-back still applies to whatever was deducted on Schedule A — capped at the $10K Daniel actually deducted. Without TCJA, his $24,800 would all be added back; with TCJA, only $10K is added back. AMT was still triggered by the much larger ISO preference.

**Why did Daniel's employer withhold the right Additional Medicare Tax?** Single filers are the easy case: employer withholds 0.9% on Medicare wages > $200K, and the threshold matches the employee's filing-status threshold. No Form 8959 reconciliation gap. For MFJ, the calculus is different.

**Why hold ISO shares past year-end?** Daniel did this to start the long-term capital gain holding clock for the eventual sale (need 2 years from grant + 1 year from exercise for qualifying disposition treatment). The cost is the AMT now — Daniel got an AMT credit (Form 8801) carryforward equal to the AMT he paid on the ISO preference, to offset future regular tax when AMTI > regular tax flips back.

**What should Daniel watch in 2026?** The Form 8801 AMT credit carryforward ($35,202 in 2025) can offset regular tax in years when his AMTI is below his regular-tax income. In a year he sells the ISO shares (capital gain), his regular tax may exceed AMTI and the AMT credit can be applied. This is tracked separately from Schedule 2.

**Why didn't NIIT include the long-term capital gains?** Long-term capital gains *are* in NII (IRC §1411(c)(1)(A)(i)). Daniel's $11,500 LTCG is included in the $16,320 NII figure. He didn't have any capital losses to net against.

## What if Daniel were audited?

His audit defense would be:

1. ISO grant agreement showing strike price $4 and grant date
2. Form 3921 from his employer documenting the exercise and FMV
3. Form 6251 worksheet with traceable add-back for the $180,000 preference
4. W-2 with Medicare wages $310,000 supporting Form 8959
5. 1099-DIV and 1099-B from his brokerage supporting Form 8960
6. Schedule A with $10,000 SALT deduction supporting the AMT add-back
7. Daniel's 2025 broker statements showing he still holds the ISO shares at year-end (no qualifying disposition yet)
