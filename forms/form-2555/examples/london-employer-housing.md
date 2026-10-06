# Example — Bona Fide Resident in London with Employer-Paid Housing

## Facts

- **Filer**: David Patel, US citizen, married filing jointly with non-citizen spouse Priya (no US income; ITIN already issued in 2022)
- **Tax year**: 2025
- **Occupation**: Senior product manager at a UK subsidiary of a US tech firm (employee, W-2 paid through UK payroll)
- **Foreign tax home**: London, UK — established January 2022 on a long-term assignment under a Tier 2/Skilled Worker visa, indefinite duration
- **Family**: Priya and two school-age children live with David in London. Children attend British International School. Priya is a UK tax resident.
- **Tax filing in UK**: David files HMRC Self Assessment as a UK tax resident; pays UK income tax + National Insurance on his full wages
- **Wages**: $185,000 USD equivalent (£146,000 at 2025 IRS yearly average rate ~$1.27/£)
- **Employer-provided housing**: Company leases a flat in Chelsea (zone 2 London) and pays £52,000/year (~$66,000) directly to landlord. This amount is included in David's UK PAYE compensation as a benefit-in-kind (and reported on his W-2 equivalent box for noncash income — $66,000)
- **No US-source income** in 2025
- **No prior FEIE election** before 2024 — David first claimed FEIE for tax year 2024
- **State of domicile**: Texas (left California in 2021; surrendered CA license, sold home, no California ties)

## Analysis

### Eligibility check

- US citizen — eligible
- Tax home in London — yes, established 2022 with continuous foreign presence, family residence, UK tax filing as resident
- Abode is NOT in the US — no US home, no family in US, no significant US ties
- Not a §901(j) sanctioned country
- Not a federal employee

Eligible.

### Test selection — Bona Fide Residence

David's situation is textbook BFR:

- Continuous residence in UK since January 2022 (entire tax years 2022, 2023, 2024, 2025 covered)
- UK tax resident, files Self Assessment, pays UK tax on worldwide income
- Family lives with him in London
- Indefinite assignment (Tier 2 visa renewable; no fixed end date)
- Children in British schools; integrated into UK community
- No statement to UK authorities that he's a non-resident (Line 13 of Form 2555 = No)

For 2025, BFR covers all 365 days. Use Part II of Form 2555.

### FEIE cap (2025)

Per Rev. Proc. 2024-40: 2025 FEIE cap = **$130,000** (full amount, since BFR covers entire tax year — no pro-ration)

### Foreign earned income

- Cash wages (line 19): $185,000
- Employer-provided housing, fair rental value (line 21a, noncash income: home): $66,000
- **Line 24 / 26 / 27 (foreign earned income)**: $251,000

Note: employer-paid housing is included in foreign earned income (IRC §911(b)(1)(A); Reg. §1.911-3(c)) — it's noncash compensation. It is not a §119 exclusion (line 25 = $0: a leased flat in Chelsea is not on the employer's business premises). The same $66,000 is the housing expense on line 28, and Part VI excludes the part above the base amount; Part VII line 41 then subtracts that housing exclusion before the FEIE cap is applied, so nothing is excluded twice.

### Foreign housing exclusion (Part VI — employee, employer-paid)

David is an **employee** (paid through the UK subsidiary's payroll) with no self-employment income. All of his foreign earned income is an employer-provided amount, so the whole housing amount is excluded in Part VI (Pub. 54, "Foreign Housing Exclusion"); Part IX does not apply.

Housing expenses: $66,000 (rent paid by employer to the landlord; included in income as noncash compensation)

**Limit on housing expenses for London**: London is listed in Notice 2025-16 at **$67,000** for a full year of 2025 ($183.56 per day). Under Notice 2026-25 §4 he could elect the 2026 London figure, $68,600; it changes nothing here because his expenses are below either limit.

**Base housing amount**: $20,800 (365 days; 2025 Form 2555 line 32)

**Housing exclusion calculation (2025 Form 2555)**:

- Line 28 (qualified housing expenses): $66,000
- Line 29a (location): London, United Kingdom
- Line 29b (limit on housing expenses): $67,000
- Line 30 (smaller of 28 or 29b): $66,000
- Line 31 (qualifying days in 2025): 365
- Line 32 (base housing amount): $20,800
- Line 33 (30 − 32): $45,200
- Line 34 (employer-provided amounts: wages + rent paid to landlord): $251,000
- Line 35 (34 ÷ 27): 1.000
- Line 36 (housing exclusion = 33 × 35, not more than 34): **$45,200**

### Foreign earned income exclusion (Part VII)

- Line 37 (maximum exclusion): $130,000
- Line 38 (days): 365; line 39: 1.000
- Line 40 (37 × 39): $130,000
- Line 41 (27 − 36): $251,000 − $45,200 = $205,800
- Line 42 (smaller of 40 or 41): **$130,000**
- Line 43 (36 + 42): $175,200
- Line 44 (AGI deductions allocable to excluded income): $0
- Line 45 (to Schedule 1 line 8d, negative): **$175,200**

### Residual taxable foreign earned income

- Total foreign earned income: $251,000
- Total exclusion: $175,200
- **Residual taxable**: $75,800

This residual is taxable on Form 1040. Tax-stacking (§911(f)) applies — the $75,800 is taxed at the marginal rate that would apply if the $175,200 were included.

### Foreign Tax Credit on the residual (Form 1116)

David paid UK income tax on his full $251,000 (UK doesn't have an FEIE-equivalent — UK taxes worldwide income for residents, with foreign tax credits/treaty for double-tax relief).

**Allocation rule (Reg. §1.911-6)**: foreign tax paid on EXCLUDED income is NOT creditable. Foreign tax paid on the RESIDUAL is creditable.

UK tax allocation:
- Total UK tax paid: ~$80,000 (illustrative; depends on UK rates)
- Allocated to excluded income ($175,200 / $251,000 = 69.8%): $55,840 — NOT creditable
- Allocated to residual ($75,800 / $251,000 = 30.2%): $24,160 — creditable on Form 1116 (general category)

The $24,160 FTC offsets US tax on the $75,800 residual. Result: David likely owes $0 US income tax on his wages (UK tax > US tax on residual due to UK's higher rates).

### No carryover for the exclusion

There is no carryover for the housing exclusion, and housing expenses above the line 29b limit are simply not counted. The only carryover in Form 2555 is the 1-year carryover of a housing **deduction** (self-employment earnings) that exceeded the Part IX limit (IRC §911(c)(4)(C); i2555 Part IX).

### SE tax

David is a W-2-equivalent employee (UK PAYE), not self-employed. No Schedule SE. Social tax was UK National Insurance, not US FICA — and under the **US-UK Totalization Agreement**, David's NI contributions exempt him from US FICA on the same earnings (his employer obtains a Certificate of Coverage from UK). No US Social Security/Medicare tax owed.

### State tax (Texas)

Texas has no state income tax. No state coordination needed.

### Spouse's situation

Priya has an ITIN (issued 2022). She has no US income. They file MFJ to access the higher standard deduction ($31,500 for MFJ in 2025, 2025 Form 1040) and broader brackets. Taxable income: $75,800 − $31,500 = $44,300; with stacking, the Foreign Earned Income Tax Worksheet gives tax of about $10,002 (tax on $219,500 minus tax on $175,200 at 2025 MFJ rates, Rev. Proc. 2024-40 Table 1), which the creditable UK tax covers through Form 1116.

Priya is a non-citizen US tax resident under the §6013(g) election (election to treat non-resident spouse as a resident for joint filing). She must report worldwide income — but she has none.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Flat 4, 22 Cheyne Walk, London SW3 5HJ, UK |
| 2 | Occupation | Senior Product Manager |
| 3 | Employer's name | [UK subsidiary name] |
| 5 | Employer is | d A foreign affiliate of a U.S. company |
| 6a | Last year Form 2555 filed | 2024 |
| 6c | Ever revoked either exclusion | No |
| 7 | Citizenship | United States |
| 8a | Separate foreign residence for family | No |
| 9 | Tax home | London, UK; established 01/15/2022 |
| 10 | Bona fide residence began / ended | 01/15/2022 / Continues |
| 11 | Living quarters | d Quarters furnished by employer |
| 12a / 12b | Family lived with you abroad | Yes / spouse and 2 children, all of 2025 |
| 13a | Statement of nonresidence submitted | No |
| 13b | Required to pay UK income tax | Yes (UK Self Assessment) |
| 14 | U.S. presence table | Each U.S. trip in 2025 with dates; business days and U.S. business income, if any (ask) |
| 15b | Visa type | Skilled Worker |
| 15d | Home maintained in U.S. | No |
| 19 | Wages, salaries | $185,000 |
| 21a | Noncash income: home (lodging) | $66,000 |
| 24 / 26 / 27 | Foreign earned income | $251,000 |
| 25 | §119 meals and lodging | $0 |
| 28 | Qualified housing expenses | $66,000 |
| 29a / 29b | Location / limit | London, UK / $67,000 |
| 30 | Smaller of 28 or 29b | $66,000 |
| 31 | Qualifying days | 365 |
| 32 | Base housing amount | $20,800 |
| 33 | Housing amount | $45,200 |
| 34 | Employer-provided amounts | $251,000 |
| 35 | Ratio | 1.000 |
| 36 | Housing exclusion | $45,200 |
| 37 | Maximum exclusion | $130,000 |
| 38 / 39 / 40 | Days / ratio / prorated maximum | 365 / 1.000 / $130,000 |
| 41 | Line 27 − line 36 | $205,800 |
| 42 | Foreign earned income exclusion | $130,000 |
| 43 | Lines 36 + 42 | $175,200 |
| 44 | Allocable deductions | $0 |
| 45 | To Schedule 1 line 8d (negative) | $175,200 |

## Required attachments

- [x] Form 2555 (this draft)
- [x] Form 1116 (general category: $24,160 of UK tax allocable to the residual; the credit is limited to the US tax on that income, about $10,002, and the excess carries over)
- [x] Schedule 1 (negative $175,200 from Form 2555 Line 45)
- [ ] Schedule SE (not required — employee)
- [ ] FBAR / FinCEN 114 separately if UK bank account aggregate exceeded $10,000
- [ ] Form 8938 if specified foreign assets exceed thresholds (MFJ abroad: > $400K end-of-year or > $600K any time)

## Lessons

1. **Employer-paid housing is income**: $66,000 is added to Line 24 (Part IV) AND excluded via Part VI. Net effect: zero double-count, but make sure both sides are recorded.
2. **High-cost city housing limits matter**: London's $67,000 (Notice 2025-16) vs. the $39,000 standard limit — the difference is significant. Always check the current year's notice (and the next year's, for the §4 election).
3. **BFR is more flexible than PPT for ongoing expats**: David doesn't need to count days. He can return to US for vacation/business without losing qualification.
4. **Foreign tax allocation under §911**: tax on excluded income isn't creditable. Allocate UK tax pro-rata between excluded and residual income.
5. **Totalization Agreements** eliminate double social tax — David's UK NI replaces US FICA.
6. **§6013(g) election** for non-resident spouse: if elected, spouse is taxed on worldwide income. Useful when spouse has no income; risky if spouse has substantial foreign income.
7. **Housing exclusion ≠ housing deduction**: employees use exclusion (Part VI); SE filers use deduction (Part IX). Same arithmetic, different mechanic.

## Citations

- IRC §911(b)(1)(A) — wages and noncash compensation included in FEI
- IRC §911(c)(1) — housing exclusion / deduction
- IRC §911(c)(2) — limit on housing expenses, geographic adjustment
- IRC §911(c)(4)(D) — employer-provided amounts
- IRC §911(d)(1)(A) — bona fide residence test
- IRC §911(f) — tax-stacking rule
- IRC §6013(g) — election to treat non-resident spouse as resident
- Reg. §1.911-3(c) — noncash compensation in FEI
- Reg. §1.911-6 — allocation of deductions and credits
- Rev. Proc. 2024-40 — 2025 FEIE cap $130,000
- Notice 2025-16 — 2025 London limit $67,000; Notice 2026-25 §4 — option to use the 2026 limit ($68,600)
- 2025 Form 2555 and Instructions (lines 21a, 25, 29b, 34–36, 37–45)
- US-UK Totalization Agreement (effective January 1, 1985)
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
