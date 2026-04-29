# Self-Employment Tax, NIIT, Additional Medicare Tax, and AMT

The four "extras" that flow into Lines 9 and 10 of the 1040-ES Estimated Tax Worksheet. These are easy to forget but commonly bite filers who plan only for income-tax brackets.

---

## Self-Employment Tax (Schedule SE)

Reported on **Line 9** of the 1040-ES worksheet.

Self-employment tax replaces FICA for Schedule C, Schedule F, and partnership SE income. Computation:

```
SE_earnings = 0.9235 × net_self_employment_income
SS_portion = 0.124 × min(SE_earnings, SS_wage_base)
Medicare_portion = 0.029 × SE_earnings
SE_tax = SS_portion + Medicare_portion
```

The **0.9235 factor** is `1 − 0.0765` — equivalent to the half of FICA an employer would pay if the taxpayer were a W-2 employee. It's a statutory adjustment to put SE filers and W-2 filers on roughly equal footing.

The **SS wage base** caps the 12.4% Social Security portion. Above the cap, only the 2.9% Medicare portion (and Additional Medicare 0.9% if over income threshold) applies.

| Year | SS wage base | Source |
|------|-------------|--------|
| 2024 | $168,600 | SSA |
| 2025 | $176,100 | SSA |
| 2026 | TBD (announced ~Oct 2025) | SSA — verify |

The agent must verify the current year's wage base before computing. Source: https://www.ssa.gov/oact/cola/cbb.html.

### Coordination with W-2 wages

If the taxpayer also has W-2 wages, the SS wage base is **shared**. The SE tax SS portion only applies to SE earnings up to `(wage_base − W-2_SS_wages_already_taxed)`. Schedule SE Part I Line 8 handles this.

Example: 2025 wage base $176,100. Taxpayer has $200,000 W-2 wages and $50,000 SE income.
- W-2 wages already at wage base
- SE 12.4% SS portion = 0% (wage base fully consumed)
- SE 2.9% Medicare portion = 2.9% × (0.9235 × $50,000) = $1,339
- Total SE tax = $1,339 (not $7,065 if it were full 15.3%)

### Half-of-SE-tax above-the-line deduction

50% of SE tax is deductible above-the-line on Schedule 1 Line 15. This reduces AGI and therefore taxable income — but it does NOT reduce the SE tax itself. The agent must include the deduction in the AGI projection (back-end of the worksheet) but compute SE tax on the gross self-employment income.

---

## Net Investment Income Tax (NIIT) 3.8%

Reported on **Line 10** of the 1040-ES worksheet via Form 8960. Authority: IRC §1411.

Applies to the **lesser** of:
1. Net investment income, OR
2. AGI excess over MAGI threshold

| Filing status | MAGI threshold |
|---------------|----------------|
| Single, HOH | $200,000 |
| MFJ, QW | $250,000 |
| MFS | $125,000 |

**Thresholds are NOT inflation-adjusted** — they have been static since 2013.

### What counts as net investment income

- Interest (other than tax-exempt)
- Dividends (qualified and ordinary)
- Capital gains (short and long, including those on rental property sales)
- Rental and royalty income (passive)
- Non-qualified annuity income
- Income from trading financial instruments
- Income from passive activities (passive partnership / S-corp K-1 income)

### What does NOT count

- Wages, salary
- Active trade or business income (Schedule C, materially-participating S-corp / partnership K-1)
- Self-employment income
- Distributions from qualified retirement plans (401(k), traditional IRA, Roth)
- Tax-exempt interest
- Social Security benefits
- Gain on sale of personal residence (excluded portion under §121)

### Worked example

MFJ couple, AGI = $300,000, of which $40,000 is interest+dividends and $20,000 is long-term capital gain.

- Net investment income = $60,000
- AGI excess over threshold = $300,000 − $250,000 = $50,000
- NIIT base = min($60,000, $50,000) = $50,000
- NIIT = $50,000 × 3.8% = $1,900

This $1,900 goes on Line 10.

---

## Additional Medicare Tax 0.9%

Reported on **Line 10** of the 1040-ES worksheet via Form 8959. Authority: IRC §3101(b)(2).

Applies to **wages + SE earnings + RRTA compensation** above:

| Filing status | Threshold |
|---------------|-----------|
| Single, HOH, QW | $200,000 |
| MFJ | $250,000 |
| MFS | $125,000 |

**Thresholds are NOT inflation-adjusted** — static since 2013.

### Computation

```
total_compensation = wages + SE_earnings (×0.9235)
addl_medicare_base = max(0, total_compensation − threshold)
addl_medicare_tax = 0.009 × addl_medicare_base
```

### Coordination with employer withholding

Employers must withhold the additional 0.9% from any single employee's wages above $200,000 — regardless of filing status. This means:

- A married employee with $180K wages whose spouse earns $100K will have under-withholding (combined $280K > $250K MFJ threshold, but neither paycheck triggers employer 0.9% withholding)
- The taxpayer must cover the gap via estimated tax or W-4 additional withholding

### Worked example (planning)

MFJ couple, projected wages $400,000 (one spouse), no SE income.

- Threshold MFJ = $250,000
- Excess = $400,000 − $250,000 = $150,000
- Additional Medicare = $150,000 × 0.9% = $1,350

If the spouse's employer withheld on wages above $200,000 ($200,000 × 0.9% = $1,800 withheld), the taxpayer is **over-withheld** by $450 — which is fine, just a refund at year-end.

If both spouses earn $200,000 each, no employer triggers additional withholding (each is at exactly $200K), so the couple owes the full $1,350 via estimated tax.

The agent must surface this scenario when wages are near the threshold.

---

## Alternative Minimum Tax (AMT)

Reported on **Line 5** of the 1040-ES worksheet via Form 6251.

AMT is a parallel tax system that disallows certain deductions and preferences. After the TCJA (effective 2018), AMT affects far fewer filers than before — primarily:

- Households with significant Incentive Stock Option (ISO) exercises with held shares (the "bargain element" is an AMT preference item)
- Households with very high state tax write-offs (now capped at $10K SALT, so this trigger is rare)
- Very high private activity municipal bond interest

### AMT exemption (2025)

| Filing status | AMT exemption | Phase-out begins | Phase-out complete |
|---------------|---------------|------------------|--------------------|
| Single, HOH | $88,100 | $626,350 | $878,750 |
| MFJ, QW | $137,000 | $1,252,700 | $1,800,700 |
| MFS | $68,500 | $626,350 | $900,350 |

(Source: Rev. Proc. 2024-40 for 2025. Verify 2026 figures.)

### AMT rates

- 26% on AMTI up to $239,100 (2025) over the exemption
- 28% on AMTI above that

### Most filers' AMT calc

For most filers, AMT calculation = $0 because the AMT exemption fully covers AMTI. The agent should compute:

```
AMTI = regular_taxable_income + AMT_preferences + AMT_adjustments
tentative_minimum_tax = AMT_rate × max(0, AMTI − AMT_exemption)
AMT_owed = max(0, tentative_minimum_tax − regular_income_tax)
```

If `AMT_owed > 0`, add to Line 5 of the 1040-ES worksheet.

For a deeper computation, this skill defers to a full tax-software walk-through; the agent flags AMT exposure if any of these are present:

- ISO exercises with held shares
- Long-term capital gains pushed by other income above the AMT exemption
- Large depreciation on assets placed in service before 1999 (ACRS adjustments — rare in 2026)
- Large foreign tax credits

---

## Putting it together — the 1040-ES Line 9 + Line 10 worksheet

```
Line 9  = SE tax from Schedule SE (15.3% × 0.9235 × SE income, with SS cap)
Line 10 = Additional Medicare Tax + NIIT + other (mostly Add'l Medicare and NIIT)
```

For a Schedule C filer with $100,000 net profit, no other wages, MFJ filing:

- Line 9 (SE tax):
  - SE earnings = 0.9235 × $100,000 = $92,350
  - SS portion: 0.124 × $92,350 = $11,451 (under 2025 wage base $176,100)
  - Medicare portion: 0.029 × $92,350 = $2,678
  - SE tax = $14,129
- Line 10 (Other):
  - Additional Medicare: SE earnings $92,350 + spouse W-2 (e.g., $200K) = $292,350; over MFJ threshold $250K by $42,350; 0.9% × $42,350 = $381
  - NIIT: depends on investment income, separately

Total of Lines 9 + 10 in this scenario: $14,129 + $381 + (NIIT if any) = ~$14,510 in "extras" that the worksheet captures.

The agent must always include all four extras (SE, Add'l Medicare, NIIT, AMT) when projecting current-year tax — missing any of them is a common cause of under-projection.
