# Foreign Housing Exclusion / Deduction

The Foreign Housing Exclusion (employees) and Foreign Housing Deduction (self-employed) under IRC §911(c) provide additional benefit beyond the FEIE for the cost of foreign housing. The mechanics differ slightly between employees and SE; the math is similar.

## High-level formula

```
Allowable housing amount = (Qualified housing expenses, capped) − Base amount
```

- **Base amount** = 16% of FEIE cap × (qualifying days / 365)
- **Cap on qualified expenses** = 30% of FEIE cap × (qualifying days / 365), with city-specific high-cost adjustments

Result:
- **Employees** → Foreign Housing **Exclusion** (Part VI of Form 2555); reduces gross income
- **Self-employed** → Foreign Housing **Deduction** (Part IX of Form 2555); above-the-line on Schedule 1

## What counts as qualified housing expenses

Includable (per Reg. §1.911-4):

- Rent
- Utilities (electricity, gas, water, sewer) — NOT telephone
- Property and renter's insurance
- Occupancy taxes that are not deductible elsewhere
- Nonrefundable security deposits and rental fees
- Property repairs and maintenance
- Residential parking
- Furniture rental (residential)

NOT includable:

- Lavish or extravagant expenses
- Mortgage interest (deductible on Schedule A if itemizing, subject to limits)
- Mortgage principal payments
- Real estate taxes (deductible on Schedule A if itemizing)
- Domestic labor (housekeeper, gardener, cook)
- Pay TV subscriptions, internet beyond reasonable
- Telephone (mobile or landline)
- Food and alcohol
- Capital improvements, additions
- Depreciation on owned home (not allowed as housing expense even if rented to another)
- Educational expenses (school for children abroad)
- Entertainment

## Base amount (Line 33)

```
Base = 16% × Annual FEIE cap × (qualifying days in tax year / 365)
```

For 2025: 16% × $130,000 = **$20,800** (full year qualifying).

For 2026: 16% × 2026 FEIE cap (TBD; verify Rev. Proc. for the announced 2026 cap).

The base represents the imputed amount the IRS assumes the filer would have spent on US housing anyway. Only excess over base qualifies for exclusion.

## Maximum housing amount (Line 31)

Default: 30% × FEIE cap × (qualifying days / 365). For 2025 full year: **$39,000**.

But many cities have higher costs of living, and the IRS publishes city-specific high-cost adjustments annually (typically by Notice issued in late prior year). The capped maximum can be substantially higher for high-cost cities.

### Example city limits (illustrative — verify current Notice for the actual figures)

For 2024, the IRS Notice 2024-XX (verify exact notice number) listed example high-cost limits:

| City | Annual housing limit |
|------|---------------------|
| Hong Kong | ~$114,300 |
| London | ~$78,400 |
| Geneva | ~$67,200 |
| Paris | ~$72,800 |
| Tokyo | ~$74,200 |
| Singapore | ~$67,400 |
| Dubai | ~$58,400 |
| Sydney | ~$48,500 |
| New York (returning to US, but listed for comparison) | n/a |
| Default (all other cities) | 30% of FEIE cap |

These figures change each year. The Notice typically comes out in fall before the tax year. **Always verify against the most current Notice before filing.**

For 2025, the IRS issues a similar notice (e.g., Notice 2025-XX). For 2026, the notice will be issued late 2025 or early 2026.

### How city designation works

Use the city where the filer's qualifying residence is located. If the filer lived in Surrey but worked in London, the qualifying residence is Surrey — and Surrey may not have a special high-cost designation, so the default 30% applies. The IRS Notice lists exactly which cities qualify.

## Housing exclusion (Part VI) — for employees

Employees can exclude housing benefit (cash + employer-provided FMV) up to the Excess Housing Expense.

Mechanic:

1. Compute total housing expenses paid (by filer or employer): Line 28
2. Cap at 30% of FEIE cap (city-adjusted): Line 31
3. Take lesser: Line 32
4. Subtract base (16% of FEIE cap): Line 33
5. Result: Excess Housing Expense (Line 34) — eligible for exclusion
6. Compare to amount paid by employer (Line 35)
7. **Housing exclusion** (Line 36) = lesser of Line 34 or Line 35

If the employer paid all housing, Line 35 = Line 32, and the exclusion = Line 34 (full Excess Housing Expense).

If the filer paid all housing personally (out of pocket), Line 35 = $0, and the exclusion = $0. The filer instead may use the housing **deduction** if SE — but employees with self-paid housing don't get a benefit on the housing side. Their relief is only via FEIE on wages.

(Wait — that last paragraph requires correction. Per Form 2555 instructions, employees who pay their own housing CAN take the housing exclusion based on the amount the employer reimbursed in cash. Cash housing allowance counts as "employer-provided" housing for Line 35 purposes. The mechanic ensures the user only excludes what was provided by the employer in some form.)

### Worked example — London expat

- Filer is a US citizen, employee at a UK firm, BFR resident in London for entire 2025
- Salary: $200,000 (cash)
- Employer pays London apartment directly: $60,000/year
- Housing FMV ($60K) is included in Line 22 (noncash income) → Line 24 includes $60K
- Total foreign earned income (Line 24): $200K cash + $60K housing FMV = $260,000

Form 2555 Part VI:

- Line 28: Housing expenses = $60,000 (employer-paid rent)
- Line 31: City-adjusted limit for London = $78,400 (illustrative; verify for 2025)
- Line 32: lesser of $60,000 or $78,400 = $60,000
- Line 33: Base = 16% × $130,000 = $20,800
- Line 34: 32 − 33 = $39,200
- Line 35: Employer-paid housing = $60,000
- Line 36 (Housing exclusion): lesser of $39,200 or $60,000 = **$39,200**

Form 2555 Part VII (FEIE):
- Line 37: FEIE cap = $130,000 (full year)
- Line 42 (Earned income exclusion): lesser of (Line 24 − Line 36, Line 37) = lesser of (260,000 − 39,200, 130,000) = lesser of (220,800, 130,000) = **$130,000**
- Line 45: Total exclusion = $130,000 + $39,200 = **$169,200**

This $169,200 reduces Schedule 1 income. The remaining $260,000 − $169,200 = **$90,800** of FEI is taxable in the US (subject to FTC if UK tax was paid on it).

## Housing deduction (Part IX) — for self-employed

SE filers can't exclude housing (no employer providing it). Instead, they get a **deduction** on Schedule 1, above-the-line.

Mechanic:

```
Housing deduction = Lesser of:
  - Excess Housing Expense (from Part VI Line 34, even though SE filers fill Part IX)
  - Foreign earned income remaining after FEIE
```

The deduction can't exceed FEI minus the FEIE excluded amount.

Worked example — SE consultant in Mexico City

- Filer SE consulting in Mexico, full year 2025 BFR
- SE net income: $150,000
- Housing expenses paid: $24,000 (rent + utilities)

Form 2555 calculations:

- Line 24: Total FEI = $150,000
- Line 32: housing capped = lesser of $24,000 or $39,000 (default 30% × $130K, no special high-cost) = $24,000
- Line 33: Base = $20,800
- Line 34: Excess = 32 − 33 = $3,200
- FEIE Line 42: lesser of ($150,000, $130,000) = $130,000
- Line 45: Housing exclusion (Part VI) = $0 for SE filer (Part VI is for employees only)

Part IX (Housing deduction):
- $3,200 (excess housing)
- Capped at FEI remaining after FEIE: $150,000 − $130,000 = $20,000
- Housing deduction = lesser of $3,200 or $20,000 = **$3,200**

The $3,200 is deducted on Schedule 1 (above-the-line). FEIE excludes $130,000.

Total benefit: $130,000 (FEIE) + $3,200 (housing deduction) = $133,200 reduction.

Remaining $150,000 − $133,200 = $16,800 taxable. Plus, SE tax is owed on FULL $150,000 (FEIE doesn't reduce SE tax — common trap).

## Coordination with FEIE

The housing exclusion / deduction is ON TOP OF FEIE — they're separate amounts.

Order of operations:
1. Compute housing exclusion / deduction first (or simultaneously)
2. Then FEIE = lesser of (FEI − housing exclusion, max FEIE cap)

This ordering ensures the housing exclusion comes from the "top" of FEI, before FEIE eats up the cap.

## Carryover for housing deduction (SE only)

If the SE filer's housing deduction exceeds FEI remaining after FEIE, the excess CARRIES FORWARD ONE YEAR (IRC §911(c)(4)). After one year, unused housing deduction is lost.

This rarely matters because most SE filers' FEI exceeds the FEIE cap by enough to absorb the housing deduction.

## What the agent should do

1. **Ask** for itemized housing expenses by type (rent, utilities, etc.)
2. **Ask** if employer provided housing or reimbursed in cash
3. **Verify city** against current-year Notice for high-cost designation
4. **Compute** the housing exclusion (employees) or deduction (SE) per Part VI / Part IX
5. **Show the math** in the deliverable — base, capped expense, excess, employer-paid

Do NOT:

- Default to the 30% default cap if the filer is in a known high-cost city — pull the Notice
- Include mortgage interest in housing expenses (use Schedule A instead)
- Include domestic labor or food
- Forget that telephone is excluded from housing expenses

## Citations

- IRC §911(c)(1) — qualified housing expenses
- IRC §911(c)(2) — base amount (16%) and ceiling (30%)
- IRC §911(c)(3) — high-cost area adjustments
- IRC §911(c)(4) — carryover for SE deduction
- Reg. §1.911-4 — definitions and computation
- IRS Notice (current year) — high-cost city table
- Pub. 54 — examples and edge cases
