# Example: Married Filing Jointly with Two Kids (Garcia Family)

A complete walkthrough of the 2025 Form 1040 (filed in 2026) for a married couple with two qualifying children, claiming the Child Tax Credit and the Dependent Care Credit. This is the canonical "two-income family with kids" pattern. Line numbers follow the 2025 form; math checked in python.

## The filers

- **Names**: Miguel Garcia (33) and Sofia Garcia (31), MFJ
- **Children**: Mateo (5) and Lucia (2), both U.S. citizens with SSNs valid for employment, both lived with parents in the U.S. all year
- **Parents' SSNs**: both valid for employment (required for the CTC from 2025)
- **Tax year**: 2025 (filing in 2026)
- **State**: Illinois

## Inputs gathered

### Miguel's W-2 (software engineer at TechCo)

| Box | Item | Amount |
|-----|------|--------|
| 1 | Federal wages | $115,000 |
| 2 | Federal income tax withheld | $14,200 |
| 3 | Social Security wages | $123,000 |
| 4 | Social Security tax withheld | $7,626 |
| 5 | Medicare wages | $123,000 |
| 6 | Medicare tax withheld | $1,784 |
| 12 | Code D (401(k)) | $8,000 |

### Sofia's W-2 (registered nurse at Memorial Hospital)

| Box | Item | Amount |
|-----|------|--------|
| 1 | Federal wages | $72,000 |
| 2 | Federal income tax withheld | $7,800 |
| 3 | Social Security wages | $72,000 |
| 4 | Social Security tax withheld | $4,464 |
| 5 | Medicare wages | $72,000 |
| 6 | Medicare tax withheld | $1,044 |
| 12 | Code DD (employer health coverage cost — informational) | $14,400 |

Sofia contributed $4,000 to her own Traditional IRA outside of work (no employer retirement plan).

### Other income

- Joint Vanguard taxable brokerage:
  - 1099-DIV box 1a (ordinary dividends): $2,400
  - 1099-DIV box 1b (qualified dividends): $2,200
  - 1099-INT box 1 (cash sweep): $180
- Joint Wells Fargo savings: 1099-INT box 1 = $560
- No 1099-NEC, no Schedule C income
- No capital gains realized in 2025

### Childcare

- Daycare for Lucia (age 2): $14,000/year at licensed center
- After-school program for Mateo (age 5): $3,200/year
- **Total qualifying childcare**: $17,200 (capped at $6,000 on Form 2441)
- Both Miguel and Sofia worked all year (both had earned income)

### Schedule A potential

| Item | Amount |
|------|--------|
| Mortgage interest (1098 from lender) | $11,800 |
| Property tax | $7,200 |
| Illinois state income tax (W-4 withholding) | $9,400 |
| Charitable contributions (church, food bank) | $1,800 |
| Total | $30,200 |

SALT limit for 2025 = $40,000 MFJ, reduced only when MAGI exceeds $500,000 (2025 Schedule A line 5e). State income tax + property tax = $16,600, fully deductible.

Schedule A total: mortgage interest $11,800 + SALT $16,600 + charitable $1,800 = **$30,200**

### Standard vs itemized

- Standard deduction (MFJ 2025): $31,500
- Itemized total: $30,200
- **Standard wins**: $31,500 > $30,200 by $1,300. Take standard. (Close call: rerun if any Schedule A item is missing.)

### IRA deduction (Sofia)

Sofia contributed $4,000 to a Traditional IRA (2025 limit $7,000). She is NOT covered by an employer retirement plan, but Miguel IS (401(k)), so her deduction phases out between MFJ modified AGI $236,000 and $246,000 for 2025 (Pub. 590-A, Table 1-3) — well above the Garcias' AGI. Full $4,000 deductible.

### Schedule 1 adjustments

- L20 IRA deduction: $4,000 (Sofia's Traditional IRA)
- **Total Schedule 1 Line 26**: **$4,000**

### Form 2441 (Dependent Care Credit)

- Qualifying expenses: $6,000 (2025 cap — two or more qualifying persons under 13)
- Earned income test: both spouses have > $6,000 earned income, passes
- AGI: $186,140 (computed below)
- AGI over $43,000, so credit rate = 20% (2025 Form 2441 line 8)
- Credit = 20% × $6,000 = **$1,200** → Schedule 3 line 2

### Schedule 8812 (CTC)

- 2 qualifying children under 17 with SSNs valid for employment; parents' SSNs valid for employment
- Tentative CTC: 2 × $2,200 = $4,400 (P.L. 119-21)
- Modified AGI $186,140 < $400,000 MFJ threshold — no reduction
- Credit limit: tax on line 18 ($23,695) exceeds $4,400, so line 14 = $4,400 → Form 1040 Line 19
- Refundable Additional CTC: $0 (full credit used against tax)

## The completed Form 1040 draft

```markdown
# Form 1040 — DRAFT for tax year 2025

## Header
Filing status: Married Filing Jointly (MFJ)
Filer name: Miguel Garcia     SSN: XXX-XX-1111
Spouse name: Sofia Garcia     SSN: XXX-XX-2222
Address: 920 Maple Ave, Chicago, IL 60614
Main home in the U.S. more than half of 2025: [x]
Digital assets question: No

Dependents (rows (1)–(7)):
| (1)–(2) Name   | (3) SSN      | (4) Relationship | (5)(a) Lived with you >½ year | (5)(b) In the U.S. | (6) FT student / disabled | (7) CTC | (7) ODC |
|----------------|--------------|------------------|------|------|---------|-----|-----|
| Mateo Garcia   | XXX-XX-3333  | Son              | [x]  | [x]  | [ ] [ ] | [x] | [ ] |
| Lucia Garcia   | XXX-XX-4444  | Daughter         | [x]  | [x]  | [ ] [ ] | [x] | [ ] |

## Page 1 — Income
1a. Total W-2 wages (115,000 + 72,000): $187,000
1b. Household employee wages:           $0
1c. Tip income:                         $0
1d. Medicaid waiver payments:           $0
1e. Taxable dependent care benefits:    $0
1f. Adoption benefits:                  $0
1g. Form 8919 wages:                    $0
1h. Other earned income:                $0
1i. Nontaxable combat pay election:     $0
1z. Sum of 1a-1h:                       $187,000

2a. Tax-exempt interest:                $0
2b. Taxable interest (180 + 560):       $740
3a. Qualified dividends:                $2,200
3b. Ordinary dividends:                 $2,400
4a. IRA distributions:                  $0
4b. Taxable IRA distributions:          $0
5a. Pensions and annuities:             $0
5b. Taxable pensions:                   $0
6a. Social Security benefits:           $0
6b. Taxable SS:                         $0
6c. Lump-sum election:                  [ ]
6d. MFS lived apart:                    [ ]
7a. Capital gain/loss (Sch D):          $0
7b. Schedule D not required / child's gain: [ ] [ ]
8. Schedule 1 additional income:        $0
9. TOTAL INCOME:                        $190,140

10. Adjustments (Schedule 1 L26):       $4,000
11a. AGI:                               $186,140

## Page 2 — Tax, Credits, Payments
11b. AGI (from 11a):                    $186,140
12a–12d. Dependent / spouse itemizes / dual-status / 65+ / blind: all [ ]
12e. Standard deduction (MFJ):          $31,500
13a. QBI deduction (Form 8995):         $0     (no business income)
13b. Schedule 1-A deductions:           $0     (no qualified tips, overtime, new-car loan interest; under 65)
14. Sum of 12e + 13a + 13b:             $31,500
15. TAXABLE INCOME:                     $154,640
16. Tax (Qualified Dividends and Capital Gain Tax Worksheet): $23,695
17. Schedule 2 L3:                      $0
18. Sum:                                $23,695
19. CTC / ODC (Sch 8812):               $4,400
20. Other credits (Sch 3 L8):           $1,200   (Dependent care credit)
21. Sum of 19 + 20:                     $5,600
22. Line 18 − line 21:                  $18,095
23. Other taxes (Sch 2 L21):            $0
24. TOTAL TAX:                          $18,095

25a. W-2 withholding (14,200 + 7,800):  $22,000
25b. 1099 withholding:                  $0
25c. Other withholding:                 $0
25d. Total withholding:                 $22,000
26. Estimated tax payments:             $0
27a. EIC:                               $0       (AGI too high)
28. Additional CTC (Sch 8812):          $0       (full CTC used against tax)
29. American opportunity credit:        $0
30. Refundable adoption credit:         $0
31. Sch 3 L15 refundable:               $0
32. Sum (27a + 28 + 29 + 30 + 31):      $0
33. TOTAL PAYMENTS:                     $22,000

34. Overpayment (refund):               $3,905
35a. Refunded directly:                 $3,905
35b. Routing #:                         (entered at filing)
35c. Account type:                      Checking
35d. Account #:                         (entered at filing)
36. Applied to next year:               $0
37. Amount you owe:                     $0
38. Estimated tax penalty:              N/A (refund)

## Required attachments
- [x] Schedule 1 (IRA deduction L20 = $4,000)
- [x] Schedule 3 (Dependent care credit L2 = $1,200)
- [x] Schedule 8812 (CTC for 2 children = $4,400)
- [x] Form 2441 (Dependent care for Mateo and Lucia)
- [x] Schedule B (ordinary dividends $2,400 are over $1,500; interest $740 alone would not require it)
- [ ] Schedule 2 — not needed (no SE tax, no AMT, no NIIT under threshold)
- [ ] Schedule A — not needed (standard deduction wins $31,500 vs $30,200)

## Validation summary
- Math: all checks passed
- Sanity warnings:
  - Schedule B required (ordinary dividends over $1,500)
  - QDCG Worksheet used because qualified dividends > $0 — $23,695 vs $23,849 on the regular rates, saving $154
  - CTC fully used against tax (credit limit not hit)
  - No SEP/Solo 401(k) since no SE income
  - Sofia's IRA fully deductible (she isn't covered; Miguel is; MAGI under $236,000)
  - Itemized would have been $30,200 < standard $31,500 — standard wins narrowly
- Next steps:
  - Receive $3,905 refund via direct deposit
  - Note only: Miguel deferred $8,000; the 2025 elective deferral limit was $23,500 under age 50 (Pub. 560)
  - Dependent care: the credit used $6,000 of their $17,200; the employer dependent care assistance exclusion is $5,000 for 2025 and $7,500 for 2026 (P.L. 119-21; 2026 Pub. 15-B) if an employer offers a plan

## Sources cited in this draft
- IRS Form 1040 (2025) and 2025 Instructions for Form 1040 (QDCG worksheet)
- IRC §1(j) (rate tables); IRC §1(h) (preferential rate on qualified dividends)
- IRC §21 (Dependent Care Credit); 2025 Form 2441
- IRC §24 (CTC, $2,200 per child for 2025 under P.L. 119-21); 2025 Schedule 8812
- IRC §63 as amended by P.L. 119-21 (standard deduction MFJ $31,500)
- IRC §164(b)(7) (SALT limit $40,000 for 2025)
- IRC §219 (IRA deduction); Pub. 590-A (2025)
- Rev. Proc. 2024-40 (2025 brackets and QDCG breakpoints)
```

## Why each non-obvious choice

**Why use the QDCG Worksheet?** The Garcias have $2,200 in qualified dividends. Using regular brackets would tax them at the 22% marginal rate; the QDCG worksheet taxes them at 15% (their taxable income is above the $96,700 MFJ 0% limit). Tax on the $152,440 ordinary part is $23,365; plus 15% × $2,200 = $330; total $23,695 vs $23,849 without the worksheet, saving $154 ($2,200 × 7%). The $200 of non-qualified dividends stays at ordinary rates.

**Why is Sofia's full $4,000 IRA contribution deductible?** Two rules:
1. Sofia is NOT covered by an employer retirement plan (the hospital didn't offer her one she enrolled in).
2. As the non-covered spouse, her phaseout starts at MFJ AGI $236,000 for 2025 — and the Garcias' AGI is $186,140, comfortably below. Full deduction.

If both spouses had been covered by employer plans, Sofia's deduction would phase out between $126,000–$146,000 (2025 MFJ, Pub. 590-A Table 1-2). Always check the active-participant box on the W-2 (box 13 retirement plan checkbox).

**Why no Schedule A despite mortgage and property tax?** The math:
- Mortgage interest: $11,800
- SALT: $7,200 property + $9,400 state income = $16,600 (under the 2025 $40,000 limit)
- Charitable: $1,800
- Total Schedule A: $30,200

Standard MFJ 2025 = $31,500. Standard wins by $1,300. The higher 2025 SALT limit (P.L. 119-21) brought them close; a little more mortgage interest or charity would flip the answer, so the agent should always compute both.

**Why no Additional CTC (refundable)?** Their Line 18 tax ($23,695) is far above the $4,400 CTC, so the whole credit is used on Line 19. The Additional CTC (refundable up to $1,700/child for 2025) only comes into play when the tax is less than the CTC. The Garcias used the full CTC against tax owed.

**Why doesn't the family qualify for Saver's Credit?** AGI limit for MFJ Saver's Credit (2025) = $79,000 (2025 Form 8880 line 9). Garcias AGI = $186,140. No credit.

**Why is the dependent care expense capped at $6,000?** For 2025, Form 2441 caps qualifying expenses at $3,000 for one qualifying person OR $6,000 for two or more. The Garcias spent $17,200 on childcare, but the credit applies to only the first $6,000. Credit rate at AGI over $43,000 is 20% → $1,200 credit.

**Why no Net Investment Income Tax (NIIT)?** NIIT applies when MFJ modified AGI exceeds $250,000. Garcias at $186,140 are well below the threshold.

**Why no Additional Medicare Tax?** Triggered when combined MFJ Medicare wages exceed $250,000. Garcias' combined Medicare wages are $195,000 ($123,000 + $72,000) — below.

## What if the Garcias had been audited?

Their audit defense:
1. W-2s from both employers match IRS records (employers file copies with SSA)
2. 1099-INT and 1099-DIV from Vanguard and Wells Fargo match brokerage records
3. Sofia's Traditional IRA contribution documented via Form 5498 from custodian
4. Childcare receipts with provider's EIN on Form 2441 — provider also reports on their own return (cross-check)
5. Both children have valid SSNs from Social Security cards
6. Mortgage interest matches Form 1098 from lender
7. Charitable contributions backed by receipts and bank/credit card records (>$250 individual gifts need written acknowledgment)

## Key lessons from the Garcia family return

1. **Two-income MFJ doesn't automatically need MFS**: MFJ wider brackets and combined deductions usually win. MFS only for liability concerns or specific income-driven student loan optimization.
2. **Standard vs itemized can be close**: with the 2025 $31,500 standard deduction and the $40,000 SALT limit, this homeowner family missed itemizing by $1,300. Run both ways.
3. **CTC at $2,200 per child is huge for middle-income families**: 2 kids × $2,200 = $4,400 directly off tax. Combined with the Dependent Care Credit, $5,600 of credits.
4. **QDCG Worksheet matters when you have qualified dividends**: the IRS doesn't compute it automatically; tax software does. Manual filers must use the worksheet.
5. **Sofia's IRA deduction depended on the active-participant rule**: knowing whether each spouse is "covered" by an employer plan determines phaseout thresholds. Check the W-2 box 13 retirement plan checkbox.
6. **Employer dependent care benefits interact with the credit**: amounts excluded under an employer plan ($5,000 for 2025, $7,500 for 2026) reduce the expenses that count for the credit on Form 2441. Ask whether either employer offers one.
