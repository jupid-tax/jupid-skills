# Foreign Housing Exclusion / Deduction

The Foreign Housing Exclusion (paid with employer-provided amounts) and Foreign Housing Deduction (paid with self-employment earnings) under IRC §911(c) provide additional benefit beyond the FEIE for the cost of foreign housing. Both start from the same housing amount in Form 2555 Part VI; the split between exclusion and deduction depends on how much of the filer's foreign earned income is employer-provided.

Figures below are for tax year 2025 (2025 Form 2555 and Instructions; Notice 2025-16) with 2026 values from Notice 2026-25. Year-dependent; re-check https://www.irs.gov/forms-pubs/about-form-2555 and the current notice each year.

## High-level formula

```
Housing amount (line 33) = lesser of (qualified housing expenses, limit on housing expenses) − base housing amount
```

- **Base housing amount** (line 32) = 16% of the FEIE cap computed per day × qualifying days in the tax year (IRC §911(c)(1)(B))
- **Limit on housing expenses** (line 29b) = 30% of the FEIE cap computed per day × qualifying days, adjusted for listed high-cost locations (IRC §911(c)(2))

Result:
- Share paid with **employer-provided amounts** → Foreign Housing **Exclusion** (Form 2555 line 36); reduces gross income through Schedule 1 line 8d
- Share paid with **self-employment earnings** → Foreign Housing **Deduction** (Form 2555 Part IX, line 50); above-the-line on Schedule 1 line 24j

## What counts as qualified housing expenses

Includable (i2555 line 28; IRC §911(c)(3)):

- Rent
- Utilities other than telephone charges
- Real and personal property insurance
- Nonrefundable fees paid to obtain a lease
- Rental of furniture and accessories
- Residential parking
- Household repairs
- Fair rental value of housing provided by the employer, unless excluded under §119 on line 25

NOT includable (i2555 line 28):

- Lavish or extravagant expenses
- Deductible interest and taxes (mortgage interest, real estate taxes)
- Amounts deductible by a cooperative tenant-stockholder
- The cost of buying or improving a house; mortgage principal payments
- Depreciation on the house
- Domestic labor (housekeeper, gardener, cook)
- Pay television
- Buying furniture or accessories
- Housing in Cuba while in violation of U.S. travel restrictions (i2555 "Travel to Cuba")

Count only expenses for the part of the year the filer meets the tax home test and one of the two tests. A second foreign household for the spouse and dependents counts only when living conditions at the tax home are dangerous, unhealthful, or otherwise adverse (i2555 "Second foreign household"; Form 2555 line 8a).

## Base amount (line 32)

```
Base = $56.99 × qualifying days in 2025 (line 31); $20,800 if line 31 is 365
```

- 2025: **$20,800** full year (16% × $130,000; 2025 Form 2555 line 32; Notice 2025-16 §2)
- 2026: **$21,264** full year (16% × $132,900; Notice 2026-25 §2)

The base represents the amount the IRS assumes the filer would have spent on US housing anyway. Only the excess over the base is a housing amount.

## Limit on housing expenses (line 29b)

Standard limit: 30% × FEIE cap per day × qualifying days.

- 2025: **$39,000** full year, or **$106.85 per day** (i2555 line 29b)
- 2026: **$39,870** full year (Notice 2026-25 §2)

Locations listed in the annual IRS notice get a higher limit, figured on the Limit on Housing Expenses Worksheet—Line 29b (full-year amount if line 31 is 365; daily amount × days otherwise). Enter the location on line 29a only if it is listed.

### Selected locations (verified against the notices)

| Location | 2025 limit, Notice 2025-16 (full year / daily) | 2026 limit, Notice 2026-25 (full year) |
|----------|-----------------------------------------------|----------------------------------------|
| Hong Kong | $114,300 / $313.15 | $114,300 |
| Geneva | $102,600 / $281.10 | $116,900 |
| Singapore | $82,900 / $227.12 | $86,700 |
| London | $67,000 / $183.56 | $68,600 |
| Tokyo | $67,700 / $185.48 | $67,300 ("Tokyo City") |
| Paris | $65,700 / $180.00 | $73,600 |
| Sydney | $62,300 / $170.68 | $65,600 |
| Dubai | $57,174 / $156.64 | $57,174 |
| Surrey (UK) | $48,402 / $132.61 | $48,402 |
| Mexico City | $47,900 / $131.23 | $47,900 |
| Lisbon | $40,000 / $109.59 | $44,800 ("Alverca and Lisbon") |
| Any location not listed | $39,000 / $106.85 | $39,870 |

The notices list about 100 locations each; look up the exact location rather than relying on this excerpt.

**Election to use the next year's table.** A filer who incurred 2025 housing expenses in a listed location may apply the 2026 limits from Notice 2026-25 instead of Notice 2025-16 (Notice 2026-25 §4). Ask the user before applying it and note the election in the draft.

### How location designation works

Use the location where the housing expenses were incurred. If the filer lived in Surrey and worked in London, Surrey is the location, and Surrey has its own listed limit ($48,402 for 2025), lower than London's. If the filer moved during the year, complete one worksheet per location using the days lived there and add the results (i2555 "More than one foreign location").

## Housing exclusion (Part VI, lines 34–36)

The exclusion covers the part of the housing amount paid for with employer-provided amounts (IRC §911(c)(4)(D); Pub. 54, "Foreign Housing Exclusion"). Employer-provided amounts are any amounts the employer paid or incurred on the filer's behalf that are foreign earned income included in gross income: wages and salary, rent paid to the landlord, housing and education reimbursements, tax equalization payments, and the fair rental value of employer housing not excluded on line 25 (i2555 line 34).

Mechanic:

1. Qualified housing expenses: line 28
2. Limit on housing expenses: line 29b
3. Lesser of the two: line 30
4. Qualifying days: line 31
5. Base: line 32
6. Housing amount: line 33 = line 30 − line 32 (zero or less: stop; no exclusion or deduction)
7. Employer-provided amounts: line 34
8. Line 35 = line 34 ÷ line 27 (at least three decimals, not over 1.000)
9. **Housing exclusion** (line 36) = line 33 × line 35, not more than line 34

A filer with no self-employment income has line 34 equal to line 27, so line 35 is 1.000 and the whole housing amount is excluded, even if the filer paid the rent personally (Pub. 54: "If you do not have self-employment income, all of your earnings are employer-provided amounts").

A filer whose foreign earned income is all self-employment income skips lines 34–35, enters zero on line 36, and figures the deduction in Part IX (i2555 line 34).

The exclusion is figured before the foreign earned income exclusion; Part VII line 41 subtracts it from foreign earned income, so the housing exclusion comes off the top before the FEIE cap is applied (Pub. 54, "Choosing the exclusion").

### Worked example — London employee

- Filer is a US citizen, employee of a UK firm, bona fide resident in London for all of 2025
- Salary: $200,000 (cash)
- Employer pays the London apartment's rent directly to the landlord: $60,000/year
- Fair rental value of the employer-provided flat goes on line 21a (noncash income: home) → line 24 includes $60,000
- Foreign earned income (lines 26 and 27): $200,000 + $60,000 = $260,000

Form 2555 Part VI:

- Line 28: Housing expenses = $60,000
- Line 29a: London, United Kingdom
- Line 29b: London limit for 2025 = $67,000 (Notice 2025-16)
- Line 30: lesser of $60,000 or $67,000 = $60,000
- Line 31: 365
- Line 32: Base = $20,800
- Line 33: $60,000 − $20,800 = $39,200
- Line 34: Employer-provided amounts = $260,000 (salary + rent paid to landlord)
- Line 35: $260,000 ÷ $260,000 = 1.000
- Line 36 (Housing exclusion): $39,200 × 1.000 = **$39,200**

Form 2555 Part VII (FEIE):
- Line 37: $130,000; line 38: 365; line 39: 1.000; line 40: $130,000
- Line 41: $260,000 − $39,200 = $220,800
- Line 42: lesser of $130,000 or $220,800 = **$130,000**

Part VIII:
- Line 43: $39,200 + $130,000 = $169,200
- Line 44: $0 (no AGI deductions allocable to the excluded wages)
- Line 45: **$169,200** → Schedule 1 line 8d as a negative amount

The remaining $260,000 − $169,200 = **$90,800** of foreign earned income is taxable in the US (subject to FTC on Form 1116 for UK tax allocable to it).

## Housing deduction (Part IX) — self-employment earnings

The part of the housing amount not paid with employer-provided amounts is a **deduction** in figuring AGI (IRC §911(c)(4)(A)), entered on Schedule 1 line 24j.

Complete Part IX only if line 33 is more than line 36 and line 27 is more than line 43 (form header).

```
Line 46 = line 33 − line 36            (housing amount not excluded)
Line 47 = line 27 − line 43            (foreign earned income not already excluded)
Line 48 = smaller of line 46 or line 47
Line 50 = line 48 + line 49 carryover from the prior year
```

The deduction can't exceed foreign earned income minus the FEIE and the housing exclusion (IRC §911(c)(4)(B)). If the FEIE absorbs all foreign earned income, line 47 is zero and there is no current-year deduction.

### Worked example — SE consultant in Mexico City

- Filer is self-employed, consulting from Mexico City, bona fide resident for all of 2025
- Gross receipts from services performed in Mexico: $150,000; no business expenses (so gross = net)
- Housing expenses paid: $24,000 (rent + utilities)

Form 2555 calculations:

- Line 20a / line 27: Foreign earned income = $150,000
- Line 28: $24,000; line 29a: Mexico City, Mexico; line 29b: $47,900 (Notice 2025-16)
- Line 30: $24,000; line 31: 365; line 32: $20,800
- Line 33: $24,000 − $20,800 = $3,200
- Lines 34–35: skipped (all self-employment income); line 36: $0
- Line 40: $130,000; line 41: $150,000 − $0 = $150,000; line 42: **$130,000**
- Line 43: $130,000
- Line 44: deductible part of SE tax allocable to the excluded income. SE tax on $150,000 = $150,000 × 0.9235 × 15.3% = $21,194; deductible half $10,597; allocable share $10,597 × ($130,000 ÷ $150,000) = **$9,184**
- Line 45: $130,000 − $9,184 = **$120,816** → Schedule 1 line 8d

Part IX (housing deduction):
- Line 46: $3,200 − $0 = $3,200
- Line 47: $150,000 − $130,000 = $20,000
- Line 48: lesser of $3,200 or $20,000 = $3,200
- Line 50: **$3,200** → Schedule 1 line 24j

AGI from this income: $150,000 (Schedule C) − $120,816 (line 8d) − $10,597 (SE tax deduction, Schedule 1 line 15, reported in full) − $3,200 (line 24j) = **$15,387**. SE tax is still owed on the full $150,000 (IRC §1402(a)(11)). Mexico has no social security agreement with the US (2025 Schedule SE instructions list), so there is no certificate-of-coverage exemption.

## Coordination with FEIE

The housing exclusion is ON TOP OF the FEIE; they are separate amounts.

Order of operations (Form 2555 Parts VI–IX):
1. Housing amount and housing exclusion first (Part VI)
2. FEIE = lesser of (foreign earned income − housing exclusion, prorated cap) (Part VII)
3. Housing deduction last, limited to the foreign earned income left after both exclusions (Part IX)

## Carryover for housing deduction (SE only)

If line 46 is more than line 47, the difference carries forward ONE YEAR (IRC §911(c)(4)(C); i2555 Part IX "1-year carryover"). It is deductible in the next year only up to that year's remaining limit; any part not deductible then is lost. Use the Housing Deduction Carryover Worksheet—Line 49 in the next year's instructions.

There is no carryover for housing expenses above the line 29b limit, and none for the housing exclusion.

## What the agent should do

1. **Ask** for itemized housing expenses by type (rent, utilities, etc.) and the dates they cover
2. **Ask** whether any foreign earned income is self-employment income (this decides exclusion vs. deduction), and whether the employer provided lodging or paid rent
3. **Look up the location** in the current notice (Notice 2025-16 for 2025; Notice 2026-25 for 2026, or for 2025 under its §4 election)
4. **Compute** lines 28–36 and, if applicable, Part IX lines 46–50
5. **Show the math** in the deliverable: limit and its source, base, housing amount, employer-provided ratio

Do NOT:

- Use the $39,000 standard limit when the filer's location is listed in the notice
- Include mortgage interest, real estate taxes, domestic labor, pay TV, or telephone in housing expenses
- Deny the exclusion to an employee because the employee, not the employer, paid the rent
- Claim a housing deduction larger than foreign earned income left after the exclusions

## Citations

- IRC §911(c)(1) — housing cost amount; §911(c)(1)(B) 16% base
- IRC §911(c)(2) — 30% limit and geographic adjustment
- IRC §911(c)(3) — housing expenses; second foreign household
- IRC §911(c)(4) — deduction for amounts not employer-provided; limit; 1-year carryover; employer-provided amounts defined
- Reg. §1.911-4 — definitions and computation
- 2025 Form 2555, Part VI and Part IX; 2025 Instructions for Form 2555, lines 28–36 and Part IX worksheets
- Notice 2025-16 (2025 limits); Notice 2026-25 (2026 limits; §4 election for 2025)
- Pub. 54 (Rev. December 2025), ch. 4 "Foreign Housing Exclusion and Deduction"
