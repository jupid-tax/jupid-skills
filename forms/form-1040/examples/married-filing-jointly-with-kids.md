# Example: Married Filing Jointly with Two Kids (Garcia Family)

A complete walkthrough of Form 1040 for a married couple with two qualifying children, claiming the Child Tax Credit and the Dependent Care Credit. This is the canonical "two-income family with kids" pattern.

## The filers

- **Names**: Miguel Garcia (33) and Sofia Garcia (31), MFJ
- **Children**: Mateo (5) and Lucia (2), both have SSNs, both lived with parents all year
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
| 3 | Social Security wages | $76,000 |
| 4 | Social Security tax withheld | $4,712 |
| 5 | Medicare wages | $76,000 |
| 6 | Medicare tax withheld | $1,102 |
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

SALT cap = $10,000 (state income tax + property tax = $16,600 capped at $10,000).

Schedule A total: mortgage interest $11,800 + capped SALT $10,000 + charitable $1,800 = **$23,600**

### Standard vs itemized

- Standard deduction (MFJ 2025): $30,000
- Itemized total: $23,600
- **Standard wins**: $30,000 > $23,600. Take standard.

### IRA deduction (Sofia)

Sofia contributed $4,000 to a Traditional IRA. Since she is NOT covered by an employer retirement plan, she has no income-based phaseout for her IRA deduction. Miguel IS covered (401(k)), but for Sofia (the non-covered spouse), the phaseout starts at MFJ AGI $236,000 for 2025 — well above the Garcias' AGI. Full $4,000 deductible.

### Schedule 1 adjustments

- L20 IRA deduction: $4,000 (Sofia's Traditional IRA)
- **Total Schedule 1 Line 26**: **$4,000**

### Form 2441 (Dependent Care Credit)

- Qualifying expenses: $6,000 (capped — two qualifying children under 13)
- Earned income test: both spouses have > $6,000 earned income, passes
- AGI: $186,140 (estimated; will recompute below)
- AGI > $43,000, so credit rate = 20%
- Credit = 20% × $6,000 = **$1,200**

### Schedule 8812 (CTC)

- 2 qualifying children under 17 with valid SSNs
- Tentative CTC: 2 × $2,000 = $4,000
- AGI $186,140 < $400,000 MFJ phaseout — no reduction
- Non-refundable portion: $4,000 (fully absorbed by tax)
- Refundable Additional CTC: $0 (full credit absorbed by tax liability; no refundable carryover needed)

## The completed Form 1040 draft

```markdown
# Form 1040 — DRAFT for tax year 2025

## Header
Filing status: Married Filing Jointly (MFJ)
Filer name: Miguel Garcia     SSN: XXX-XX-1111
Spouse name: Sofia Garcia     SSN: XXX-XX-2222
Address: 920 Maple Ave, Chicago, IL 60614
Digital assets question: No
Someone can claim you as dependent: No
Spouse itemizes on separate return: N/A
Miguel 65+: No
Sofia 65+: No
Both blind: No

Dependents:
| Name           | SSN          | Relationship | CTC | ODC |
|----------------|--------------|--------------|-----|-----|
| Mateo Garcia   | XXX-XX-3333  | Son          | [x] | [ ] |
| Lucia Garcia   | XXX-XX-4444  | Daughter     | [x] | [ ] |

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
7. Capital gain/loss (Sch D):           $0
8. Schedule 1 additional income:        $0
9. TOTAL INCOME:                        $190,140

10. Adjustments (Schedule 1 L26):       $4,000
11. AGI:                                $186,140
12. Standard deduction (MFJ):           $30,000
13. QBI deduction (Form 8995):          $0     (no business income)
14. Sum of 12 + 13:                     $30,000
15. TAXABLE INCOME:                     $156,140

## Page 2 — Tax, Credits, Payments
16. Tax (QDCG Worksheet — qualified divs):  $23,608
17. Other taxes (Sch 2 L3):             $0
18. Sum:                                $23,608
19. CTC / ODC (Sch 8812):               $4,000
20. Other credits (Sch 3 L8):           $1,200   (Dependent care credit)
21. Subtract:                           $18,408
22. Other taxes (Sch 2 L21):            $0
23. TOTAL TAX:                          $18,408

25a. W-2 withholding (14,200 + 7,800):  $22,000
25b. 1099 withholding:                  $0
25c. Other withholding:                 $0
26. Estimated tax payments:             $0
27. EITC:                               $0       (AGI too high)
28. Additional CTC (Sch 8812):          $0       (full CTC absorbed by tax)
29. Refundable AOTC:                    $0
31. Sch 3 L15 refundable:               $0
32. Sum (27 + 28 + 29 + 31):            $0
33. TOTAL PAYMENTS:                     $22,000

34. Overpayment (refund):               $3,592
35a. Refunded directly:                 $3,592
35b. Routing #:                         (entered at filing)
35c. Account type:                      Checking
35d. Account #:                         (entered at filing)
36. Applied to next year:               $0
37. Amount you owe:                     $0
38. Estimated tax penalty:              N/A (refund)

## Required attachments
- [x] Schedule 1 (IRA deduction L20 = $4,000)
- [x] Schedule 3 (Dependent care credit L2 = $1,200)
- [x] Schedule 8812 (CTC for 2 children = $4,000)
- [x] Form 2441 (Dependent care for Mateo and Lucia)
- [ ] Schedule 2 — not needed (no SE tax, no AMT, no NIIT under threshold)
- [ ] Schedule A — not needed (standard deduction wins $30,000 vs $23,600)
- [ ] Schedule B — not needed (interest $740 + dividends $2,400 = $3,140 > $1,500 → Schedule B IS REQUIRED)

WAIT — correction:
- [x] Schedule B (combined interest + dividends $3,140 > $1,500 threshold)

## Validation summary
- Math: all checks passed
- Sanity warnings:
  - Schedule B required (combined interest + dividends > $1,500)
  - QDCG Worksheet used because qualified dividends > $0 — saves ~$330 vs regular brackets
  - CTC fully absorbed by tax (non-refundable cap not hit)
  - No SEP/Solo 401(k) since no SE income
  - Sofia's IRA fully deductible (not covered by employer plan; AGI < phaseout)
  - Itemized would have been $23,600 < standard $30,000 — standard wins
- Next steps:
  - Receive $3,592 refund via direct deposit
  - Consider increasing 401(k) contributions in 2026 if cash flow allows (Miguel only at $8,000; max is $23,000 for under 50 in 2025)
  - Sofia could open a SEP if she does any 1099 work in 2026
  - Childcare credit maxes out at $6,000 of expenses for 2+ children — they spent $17,200, so they could explore Dependent Care FSA (up to $5,000 pre-tax) for 2026

## Sources cited in this draft
- IRS Form 1040, Rev. 2025
- IRC §1(a) (MFJ rate schedule)
- IRC §1(h) (preferential rate on qualified dividends)
- IRC §21 (Dependent Care Credit)
- IRC §24 (CTC)
- IRC §63 (standard deduction MFJ $30,000)
- IRC §219 (IRA deduction)
- Rev. Proc. 2024-40 (2025 figures)
```

## Why each non-obvious choice

**Why use the QDCG Worksheet?** The Garcias have $2,200 in qualified dividends. Using regular brackets would tax them at 22% marginal rate; the QDCG worksheet taxes them at 15% LTCG rate. Saves ~$154 ($2,200 × 7% rate differential). Also, ordinary dividends $2,400 − qualified $2,200 = $200 in non-qualified that's still taxed at ordinary rates. The worksheet handles all of this automatically.

**Why is Sofia's full $4,000 IRA contribution deductible?** Two rules:
1. Sofia is NOT covered by an employer retirement plan (the hospital didn't offer her one she enrolled in).
2. As the non-covered spouse, her phaseout starts at MFJ AGI $236,000 for 2025 — and the Garcias' AGI is $186,140, comfortably below. Full deduction.

If both spouses had been covered by employer plans, Sofia's deduction would phase out between $123,000–$143,000 (2025 MFJ — the "active participant" thresholds). Always check the active-participant box on the W-2 (box 13 retirement plan checkbox).

**Why no Schedule A despite mortgage and property tax?** The math:
- Mortgage interest: $11,800
- SALT: $7,200 property + $9,400 state income = $16,600, capped at $10,000
- Charitable: $1,800
- Total Schedule A: $23,600

Standard MFJ 2025 = $30,000. Standard wins by $6,400. The SALT cap is what kills itemizing for Illinois middle-income families — they hit the cap easily, lose value on every dollar of state tax above $10,000.

**Why no Additional CTC (refundable)?** Their tax liability before CTC was $18,408 + $4,000 = enough to fully absorb the $4,000 non-refundable CTC. The Additional CTC (refundable up to $1,700/child) is only triggered when tax liability is less than the CTC amount. The Garcias paid the full CTC against tax owed.

**Why doesn't the family qualify for Saver's Credit?** AGI threshold for MFJ Saver's Credit (2025) = $79,000. Garcias AGI = $186,140. No credit.

**Why is the dependent care expense capped at $6,000?** Form 2441 caps qualifying expenses at $3,000 for one qualifying person OR $6,000 for two or more. The Garcias spent $17,200 on childcare, but the credit applies to only the first $6,000. Credit rate at AGI > $43,000 is 20% → $1,200 credit.

**Why no Net Investment Income Tax (NIIT)?** NIIT kicks in at MFJ AGI > $250,000. Garcias at $186,140 are well below the threshold.

**Why no Additional Medicare Tax?** Triggered at MFJ wages > $250,000. Garcias combined W-2 wages $187,000 — well below.

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
2. **Standard deduction wins for many homeowners post-TCJA**: SALT cap makes itemizing harder. Run both ways.
3. **CTC at $2,000 per child is huge for middle-income families**: 2 kids × $2,000 = $4,000 directly off tax. Combined with Dependent Care Credit, families with childcare effectively get ~$5,200 of tax relief.
4. **QDCG Worksheet matters when you have qualified dividends**: the IRS doesn't compute it automatically; tax software does. Manual filers must use the worksheet.
5. **Sofia's IRA deduction depended on the active-participant rule**: knowing whether each spouse is "covered" by an employer plan determines phaseout thresholds. Check the W-2 box 13 retirement plan checkbox.
6. **Dependent Care FSA might beat the credit**: at higher incomes, a Dependent Care FSA (up to $5,000 pre-tax MFJ) saves more than the 20% credit on $6,000 of expenses. Worth exploring for 2026.
