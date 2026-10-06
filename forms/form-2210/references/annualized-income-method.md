# Form 2210 — Annualized Income Installment Method (Schedule AI)

The annualized income installment method is the filer's tool for back-loaded income. If income arrives late in the year — Q4 capital gain, year-end bonus, year-end Roth conversion, business with seasonal Q4 — the regular method's "25% per quarter" required installment overcharges the early quarters relative to actual income. Schedule AI replaces the regular method with quarter-specific amounts based on actual cumulative income through each quarter-end.

## When Schedule AI helps

Schedule AI helps when:

- Income is materially back-loaded (one quarter > 40% of annual)
- The filer didn't estimate-pay early quarters because no income existed yet
- The regular method's penalty is more than ~$50 (otherwise the analytical effort exceeds the benefit)

Schedule AI does NOT help when:

- Income is roughly even across the year
- Income is front-loaded (the annualized amounts exceed the regular installments, line 27 falls back to the regular amounts, and nothing is saved)

The agent should compute both methods and compare the total penalty. If Schedule AI is used for any due date, it is used for all of them (2025 instructions), but its line 27 keeps the smaller of the annualized installment or the regular installment (plus any unused regular amount carried forward) in each column. A reduction in an early column is recaptured in later columns (IRC §6654(d)(2)(A)(ii)).

## The columns

Schedule AI has four columns, one for each cumulative period:

| Column | Period | Annualization factor | Cumulative installment % |
|--------|--------|---------------------|--------------------------|
| (a) | Jan 1 – Mar 31 | 4 | 22.5% |
| (b) | Jan 1 – May 31 | 2.4 | 45% |
| (c) | Jan 1 – Aug 31 | 1.5 | 67.5% |
| (d) | Jan 1 – Dec 31 | 1 | 90% |

**Why these factors?** They convert "cumulative income through period N" into "annual-equivalent income". Q1 (3 months) × 4 = annualized. Q1+Q2 (5 months) × 2.4 = annualized. Etc.

**Why these percentages?** They mirror the regular method's 25/50/75/100 progression but applied to the 90% current-year safe harbor. So 22.5% = 90% × 25%, 45% = 90% × 50%, 67.5% = 90% × 75%, 90% = 90% × 100%.

## The worksheet (high-level)

For each column, the agent computes:

```
Step 1 (line 1): AGI from January 1 through the column-end date (3/31, 5/31, 8/31, 12/31);
        self-employed filers subtract the deductible half of the period's SE tax
Step 2 (line 3): Annualized income = line 1 × column factor
Step 3 (lines 4–10): Deductions:
        - Standard deduction: full year (do NOT annualize; line 7 uses the full amount)
        - Itemized deductions: period amount × factor (lines 4–6)
        - QBI deduction (line 9), figured on the annualized amounts
        - Personal exemptions: none for Form 1040 filers (line 12 = 0)
Step 4 (lines 11–13): Annualized taxable income
Step 5 (line 14): Tax on line 13 with current-year tax tables or worksheets; adjust here for
        OBBBA items not handled elsewhere (e.g., Schedule 1-A deductions)
Step 6 (lines 15–19): Add annualized SE tax (Part II line 36), other taxes (Additional
        Medicare Tax, NIIT, AMT), subtract credits
Step 7 (line 21): Line 19 × applicable percentage. No division by the factor.
Step 8 (lines 22–27): Line 23 = line 21 − earlier line 27s; line 26 = 25% of Form 2210
        line 9 + unused amount carried from the previous column; line 27 = smaller of
        line 23 or line 26 → Form 2210 Part III line 10
```

## Worked example

Filer is a freelance designer (all income is Schedule C profit) with this pattern in 2025:

| Period | Profit in period | Cumulative |
|--------|------------------|-----------|
| Jan–Mar | $0 | $0 |
| Apr–May | $5,000 | $5,000 |
| Jun–Aug | $15,000 | $20,000 |
| Sep–Dec | $80,000 | $100,000 |

Single, standard deduction $15,750 (2025 Form 1040), no other income, no withholding, no estimated payments. Assume 100%/110% of the prior-year tax is larger than 90% of the 2025 tax, so line 9 is the 90% figure.

**Full-year tax (Form 1040):** SE tax $14,130 (Schedule SE: $92,350 × 15.3%); AGI $92,935 ($100,000 − $7,065); QBI deduction $15,437 (20% of taxable income before QBI, $77,185); taxable income $61,748; income tax $8,494 (2025 Tax Table). Total tax $22,624.

**Regular method:** line 9 = 90% × $22,624 = $20,362; required installment $5,090.50 in each column.

**Schedule AI (2025 lines; whole dollars):**

| Line | (a) 1/1–3/31 | (b) 1/1–5/31 | (c) 1/1–8/31 | (d) 1/1–12/31 |
|------|-------------|-------------|-------------|--------------|
| 28 Net SE earnings for the period | $0 | $4,618 | $18,470 | $92,350 |
| 36 Annualized SE tax (lines 33 + 35) | $0 | $1,695 | $4,238 | $14,129 |
| 1 AGI for the period (profit − ½ of line 36 ÷ factor) | $0 | $4,647 | $18,587 | $92,935 |
| 2 Factor | 4 | 2.4 | 1.5 | 1 |
| 3 Annualized income | $0 | $11,153 | $27,881 | $92,935 |
| 8 Standard deduction (full year) | $15,750 | $15,750 | $15,750 | $15,750 |
| 9 QBI deduction (annualized) | $0 | $0 | $2,426 | $15,437 |
| 13 Taxable income | $0 | $0 | $9,705 | $61,748 |
| 14 Tax | $0 | $0 | $973 | $8,494 |
| 17 Total tax (14 + 15 + 16) | $0 | $1,695 | $5,211 | $22,623 |
| 20 Applicable percentage | 22.5% | 45% | 67.5% | 90% |
| 21 Line 19 × line 20 | $0 | $762.75 | $3,517.43 | $20,360.70 |
| 23 Line 21 − earlier line 27s | $0 | $762.75 | $2,754.68 | $16,843.27 |
| 26 Regular installment + carried amount | $5,090.50 | $10,181.00 | $14,508.75 | $16,844.57 |
| 27 Smaller of 23 or 26 → Part III line 10 | **$0** | **$762.75** | **$2,754.68** | **$16,843.27** |

The annualized tax on line 19 is multiplied by the applicable percentage directly. There is no step that divides it by the factor: 22.5% already equals 90% × 25% (one of four installments), 45% equals 90% × 50%, and so on.

The four Schedule AI installments total $20,360.70, about the same as line 9 ($20,362; the $1.30 gap is whole-dollar rounding in Part II). Schedule AI does not lower the total due for the year; it moves the requirement to the columns where the income was earned.

### Penalty comparison

No payments; the balance is paid with the return on April 15, 2026. 2025 rate 7% in every rate period (2025 worksheet). Days to April 15, 2026: column (a) 365, (b) 304, (c) 212, (d) 90.

Regular method:
- (a) $5,090.50 × 7% × 365/365 = $356.34
- (b) $5,090.50 × 7% × 304/365 = $296.78
- (c) $5,090.50 × 7% × 212/365 = $206.97
- (d) $5,090.50 × 7% × 90/365 = $87.86
- Total ≈ $947.95

Schedule AI:
- (a) $0
- (b) $762.75 × 7% × 304/365 = $44.47
- (c) $2,754.68 × 7% × 212/365 = $112.00
- (d) $16,843.27 × 7% × 90/365 = $290.72
- Total ≈ $447.19

**Schedule AI saves about $501** in this scenario. The filer checks box C and files Form 2210 with Schedule AI rather than letting the IRS compute (the IRS uses the regular method unless Schedule AI is attached).

## When Schedule AI hurts

If income is front-loaded — say, a consultant who finishes a major project in Q1 and bills $80,000, then has small income afterward — Schedule AI's line 23 for column (a) (annualizing $80K to $320K of "annual-equivalent" income) may *exceed* the regular installment. Line 27 then takes the regular amount (line 26) for that column, so Schedule AI cannot raise a column above the regular installment plus carried amounts; it just may not save anything.

Schedule AI also requires substantial recordkeeping — quarterly cumulative AGI, deductions, and tax recomputation. The agent should ask the filer if they can produce quarterly bank statements and brokerage records before recommending Schedule AI.

## Practical tips

1. **Standard deduction is NOT prorated** under Schedule AI — the full annual amount applies in every column. This is favorable to filers with low early-quarter income.

2. **Itemized deductions ARE prorated** — the agent must capture which deductions occurred in which quarter (e.g., property tax payment in Q4 only counts in column (d)).

3. **Self-employment tax is handled in Schedule AI Part II** (lines 28–36): net earnings for the period on line 28, the prorated social security limit on line 29 ($44,025 / $73,375 / $117,400 / $176,100 for 2025), wages for the period on line 30, and annualizing rates 0.496 / 0.2976 / 0.186 / 0.124 and 0.116 / 0.0696 / 0.0435 / 0.029. Line 36 goes to line 15. Additional Medicare Tax on SE income is figured in Part I (line 16).

4. **Capital gains rates apply per column** — long-term gains are taxed at the preferential rate within each column's annualized tax computation.

5. **Estimated payments still allocated by actual date** — the underpayment for each quarter is computed against Schedule AI's required installment for that quarter, with payments credited by actual due date.

6. **Withholding on actual dates is a separate box** — box D can be checked together with box C. Withholding still counts one-fourth per column unless box D is checked.

## What the agent should do

1. Ask: "Was your income roughly even across the year, or concentrated in one or two quarters?" If concentrated, compute Schedule AI.
2. Ask for quarterly cumulative AGI: through 3/31, 5/31, 8/31, 12/31. The 12/31 figure is the annual return total — already known. The other three require historical statements.
3. Compute both methods. Present the side-by-side penalty comparison.
4. Recommend whichever method gives the lower penalty.
5. If Schedule AI is recommended, file Form 2210 with Schedule AI attached. If regular method is lower, the filer can let IRS compute (no Form 2210 required).

## Sources

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — Schedule AI worksheet
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — detailed Schedule AI line-by-line
- IRC §6654(d)(2) — Annualized income installment method (applicable percentages 22.5 / 45 / 67.5 / 90; recapture)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — the 2026 edition points to the Form 2210 instructions for Schedule AI
