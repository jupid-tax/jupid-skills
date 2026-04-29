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

- Cash wages: $185,000
- Employer-provided housing FMV (noncash compensation): $66,000
- **Total Line 24 (foreign earned income)**: $251,000

Note: employer-paid housing is included in foreign earned income (per IRC §911(b)(1)(A) and Reg. §1.911-3(c)) — it's noncash compensation. It's then potentially excluded again via the housing exclusion in Part VI. The form mechanics handle this without double-counting because the housing exclusion in Line 36 reduces total exclusion but the housing FMV is part of the income being excluded.

### Foreign housing exclusion (Part VI — employee, employer-paid)

David is an **employee** (W-2-equivalent paid through UK payroll subsidiary). Use Part VI (housing **exclusion**), not Part IX (deduction for SE).

Housing expenses: $66,000 (rent paid by employer; included in wages as noncash)

**Maximum housing amount for London (high-cost city)**:

London is on the IRS high-cost cities list. For 2025, Notice 2024-XX (verify the actual notice number for the current year) sets London's housing limit at **$71,500** (illustrative — verify against current Notice). Most years London is among the higher-listed cities ($65K-$75K range).

For this example, use $71,500. (If the actual current-year notice gives a different number, substitute.)

**Base housing amount**: 16% × $130,000 = **$20,800**

**Housing exclusion calculation**:

- Line 28 (housing expenses): $66,000
- Line 31 (housing expense limit; max for London): $71,500
- Line 32 (lesser of 28 or 31): $66,000
- Line 33 (base housing amount): $20,800
- Line 34 (32 - 33): $45,200
- Line 35 (housing paid by employer): $66,000
- Line 36 (housing exclusion = lesser of 34 or 35): **$45,200**

### Foreign earned income exclusion (Part VII)

- Line 37 (max exclusion, full year): $130,000
- Line 38-40 (no pro-ration): 365/365 = 1.000
- Line 41 (pro-rated max): $130,000
- Line 42 (earned income exclusion = lesser of (Line 24 - Line 36, Line 41)):
  - Line 24 - Line 36 = $251,000 - $45,200 = $205,800
  - Line 41 = $130,000
  - Lesser = **$130,000**
- Line 45 (total exclusion to Schedule 1): $45,200 + $130,000 = **$175,200**

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

### Carryforward — housing exclusion mechanics

The housing exclusion has its own carryover rules under §911(c)(2) and (4). If housing expenses exceed the maximum housing amount in a given year (didn't happen here — $66K < $71.5K limit), the excess can be **carried forward to the next year only** (one-year carryforward). Track on Form 2555 Line 30 of the next year if applicable.

### SE tax

David is a W-2-equivalent employee (UK PAYE), not self-employed. No Schedule SE. Social tax was UK National Insurance, not US FICA — and under the **US-UK Totalization Agreement**, David's NI contributions exempt him from US FICA on the same earnings (his employer obtains a Certificate of Coverage from UK). No US Social Security/Medicare tax owed.

### State tax (Texas)

Texas has no state income tax. No state coordination needed.

### Spouse's situation

Priya has an ITIN (issued 2022). She has no US income. They file MFJ to access the higher standard deduction ($30,800 for MFJ in 2025) and broader brackets.

Priya is a non-citizen US tax resident under the §6013(g) election (election to treat non-resident spouse as a resident for joint filing). She must report worldwide income — but she has none.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Flat 4, 22 Cheyne Walk, London SW3 5HJ, UK |
| 2 | Occupation | Senior Product Manager |
| 4a | Employer name | [UK subsidiary name] |
| 4d | Type | Foreign affiliate of US company |
| 5 | Last year FEIE claimed | 2024 |
| 6c | Revocation history | None (no 5-year lock-out) |
| 7 | Test used | Bona Fide Residence |
| 8 | Family in foreign country | Yes (spouse + 2 children) |
| 9 | Tax home | London, established 01/15/2022 |
| 10 | BFR start date | 01/15/2022 |
| 11 | Living quarters | Furnished apartment, leased by employer |
| 12 | Family lived with filer | Yes |
| 13 | Statement to foreign authorities re non-resident | No (filed UK Self Assessment as resident) |
| 14 | Required to pay foreign country income tax | Yes (UK Self Assessment) |
| 19 | Wages, salary | $185,000 |
| 22 | Noncash income (employer housing FMV) | $66,000 |
| 24 | Total foreign earned income | $251,000 |
| 27 | = Line 24 | $251,000 |
| 28 | Housing expenses | $66,000 |
| 31 | Housing limit (London adjusted) | $71,500 |
| 32 | Lesser of 28 or 31 | $66,000 |
| 33 | Base housing amount | $20,800 |
| 34 | 32 - 33 | $45,200 |
| 35 | Employer-paid housing | $66,000 |
| 36 | Housing exclusion | $45,200 |
| 37 | Max exclusion | $130,000 |
| 42 | Earned income exclusion | $130,000 |
| 45 | Total exclusion to Schedule 1 | $175,200 |

## Required attachments

- [x] Form 2555 (this draft)
- [x] Form 1116 (general category, $24,160 FTC for UK tax allocable to residual)
- [x] Schedule 1 (negative $175,200 from Form 2555 Line 45)
- [ ] Schedule SE (not required — employee)
- [ ] FBAR / FinCEN 114 separately if UK bank account aggregate exceeded $10,000
- [ ] Form 8938 if specified foreign assets exceed thresholds (MFJ abroad: > $400K end-of-year or > $600K any time)

## Lessons

1. **Employer-paid housing is income**: $66,000 is added to Line 24 (Part IV) AND excluded via Part VI. Net effect: zero double-count, but make sure both sides are recorded.
2. **High-cost city housing limits matter**: London's $71,500 vs. default $39,000 — the difference is significant. Always check the current year's IRS Notice for city tables.
3. **BFR is more flexible than PPT for ongoing expats**: David doesn't need to count days. He can return to US for vacation/business without losing qualification.
4. **Foreign tax allocation under §911**: tax on excluded income isn't creditable. Allocate UK tax pro-rata between excluded and residual income.
5. **Totalization Agreements** eliminate double social tax — David's UK NI replaces US FICA.
6. **§6013(g) election** for non-resident spouse: if elected, spouse is taxed on worldwide income. Useful when spouse has no income; risky if spouse has substantial foreign income.
7. **Housing exclusion ≠ housing deduction**: employees use exclusion (Part VI); SE filers use deduction (Part IX). Same arithmetic, different mechanic.

## Citations

- IRC §911(b)(1)(A) — wages and noncash compensation included in FEI
- IRC §911(c)(1) — housing exclusion / deduction
- IRC §911(c)(2) — housing amount carryforward (one-year)
- IRC §911(d)(1)(A) — bona fide residence test
- IRC §911(f) — tax-stacking rule
- IRC §6013(g) — election to treat non-resident spouse as resident
- Reg. §1.911-3(c) — noncash compensation in FEI
- Reg. §1.911-6 — allocation of deductions and credits
- Rev. Proc. 2024-40 — 2025 FEIE cap $130,000
- IRS Notice (current year) — high-cost city housing limits, including London
- US-UK Totalization Agreement (effective January 1, 1985)
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
