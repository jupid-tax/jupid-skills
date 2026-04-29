# Form 2210 — Annualized Income Installment Method (Schedule AI)

The annualized income installment method is the filer's tool for back-loaded income. If income arrives late in the year — Q4 capital gain, year-end bonus, year-end Roth conversion, business with seasonal Q4 — the regular method's "25% per quarter" required installment overcharges the early quarters relative to actual income. Schedule AI replaces the regular method with quarter-specific amounts based on actual cumulative income through each quarter-end.

## When Schedule AI helps

Schedule AI helps when:

- Income is materially back-loaded (one quarter > 40% of annual)
- The filer didn't estimate-pay early quarters because no income existed yet
- The regular method's penalty is more than ~$50 (otherwise the analytical effort exceeds the benefit)

Schedule AI does NOT help when:

- Income is roughly even across the year
- Income is front-loaded (Schedule AI may produce *higher* required installments for early quarters)

The agent should compute both methods and compare. The filer uses whichever gives the lower required installment per quarter — there is no "all-or-nothing" requirement.

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
Step 1: Cumulative AGI through column-end date (e.g., 3/31, 5/31, 8/31, 12/31)
Step 2: Annualized AGI = cumulative × column factor
Step 3: Annualized deductions:
        - Standard deduction: full year (do NOT prorate; Schedule AI uses the full-year amount)
        - Itemized deductions: cumulative × factor (prorate same as income)
        - Personal exemptions: full year (zero post-TCJA through 2025)
Step 4: Annualized taxable income = annualized AGI − annualized deductions
Step 5: Annualized tax = current-year tax brackets applied to annualized taxable income
Step 6: De-annualize: column tax = annualized tax × (1 / column factor)
        (e.g., Q1 column tax = annualized tax / 4)
Step 7: Required cumulative installment = column tax × column percentage
Step 8: Compare to regular method's cumulative required installment (smaller value applies)
```

## Worked example

Filer is a freelance designer with the following income pattern:

| Quarter | Income | Cumulative |
|---------|--------|-----------|
| Q1 (Jan–Mar) | $0 | $0 |
| Q2 (Apr–May) | $5,000 | $5,000 |
| Q3 (Jun–Aug) | $15,000 | $20,000 |
| Q4 (Sep–Dec) | $80,000 | $100,000 |

Annual: $100,000. Filer is single, takes standard deduction ($15,000 — verify for tax year), no other income.

**Annual tax** (current-year brackets, single, $100K AGI − $15K = $85K taxable):
- Approx tax = $13,500 (varies by tax year — verify against current brackets)

**Required annual payment under regular method** (assume 90% safe harbor applies; prior-year tax not relevant for this example):
- 90% × $13,500 = $12,150
- Quarterly required installments: $3,038 / $6,075 / $9,113 / $12,150 (cumulative)

**Schedule AI Column (a) — through 3/31:**
- Cumulative AGI: $0
- Annualized: $0 × 4 = $0
- Annualized deductions: $15,000 (full year standard deduction)
- Annualized taxable income: max($0 − $15,000, 0) = $0
- Annualized tax: $0
- De-annualized tax: $0 / 4 = $0
- Required Q1 cumulative installment: $0 × 22.5% = $0

**Compare to regular Q1 required: $3,038. Schedule AI saves $3,038 of required installment for Q1.**

**Schedule AI Column (b) — through 5/31:**
- Cumulative AGI: $5,000
- Annualized: $5,000 × 2.4 = $12,000
- Annualized deductions: $15,000
- Annualized taxable income: max($12,000 − $15,000, 0) = $0
- Annualized tax: $0
- Required Q2 cumulative installment: $0 × 45% = $0

**Compare to regular Q2 required: $6,075. Schedule AI saves $6,075.**

**Schedule AI Column (c) — through 8/31:**
- Cumulative AGI: $20,000
- Annualized: $20,000 × 1.5 = $30,000
- Annualized deductions: $15,000
- Annualized taxable income: $30,000 − $15,000 = $15,000
- Annualized tax: ~$1,538 (10% bracket plus part of 12% — exact amount depends on year)
- De-annualized tax: $1,538 / 1.5 = $1,025
- Required Q3 cumulative installment: $1,025 × 67.5% = $692

**Compare to regular Q3 required: $9,113. Schedule AI saves $8,421.**

**Schedule AI Column (d) — through 12/31:**
- Cumulative AGI: $100,000 (full year)
- Annualized: $100,000 × 1 = $100,000
- Annualized deductions: $15,000
- Annualized taxable income: $85,000
- Annualized tax: ~$13,500
- De-annualized tax: $13,500 / 1 = $13,500
- Required Q4 cumulative installment: $13,500 × 90% = $12,150

**Schedule AI Q4 = $12,150, same as regular method.** This is by design — Schedule AI for the full-year column converges to the regular method.

### Penalty comparison

Assume filer paid no estimates and had no withholding (all SE income).

Regular method:
- Q1 underpayment: $3,038 (penalty accrues from 4/15)
- Q2 underpayment: additional $3,037 (penalty from 6/15)
- Q3 underpayment: additional $3,038 (penalty from 9/15)
- Q4 underpayment: additional $3,037 (penalty from 1/15)

Total penalty (assume ~7% annualized rate, ~365 days for Q1, ~305 days for Q2, ~213 days for Q3, ~90 days for Q4):
≈ $3,038 × 7% × 1.0 + $3,037 × 7% × 0.83 + $3,038 × 7% × 0.58 + $3,037 × 7% × 0.25
≈ $213 + $176 + $123 + $53 = ~$565

Schedule AI:
- Q1 underpayment: $0
- Q2 underpayment: $0
- Q3 underpayment: $692
- Q4 underpayment: additional $11,458

Penalty:
≈ $692 × 7% × 0.58 + $11,458 × 7% × 0.25
≈ $28 + $200 = ~$228

**Schedule AI saves ~$337** in this scenario. The filer should file Form 2210 with Schedule AI rather than letting IRS compute (which uses regular method).

## When Schedule AI hurts

If income is front-loaded — say, a consultant who finishes a major project in Q1 and bills $80,000, then has small income afterward — Schedule AI's Q1 required installment (annualizing $80K to $320K of "annual-equivalent" income for the column) may *exceed* the regular method's 25%-of-actual-tax. In that case, the regular method's required installment applies for that quarter (filer always uses the lower of the two per quarter).

Schedule AI also requires substantial recordkeeping — quarterly cumulative AGI, deductions, and tax recomputation. The agent should ask the filer if they can produce quarterly bank statements and brokerage records before recommending Schedule AI.

## Practical tips

1. **Standard deduction is NOT prorated** under Schedule AI — the full annual amount applies in every column. This is favorable to filers with low early-quarter income.

2. **Itemized deductions ARE prorated** — the agent must capture which deductions occurred in which quarter (e.g., property tax payment in Q4 only counts in column (d)).

3. **Self-employment tax is not handled inside Schedule AI** — SE tax must be computed separately and added to the annualized tax in each column. See current-year Schedule AI worksheet for the exact mechanic.

4. **Capital gains rates apply per column** — long-term gains are taxed at the preferential rate within each column's annualized tax computation.

5. **Estimated payments still allocated by actual date** — the underpayment for each quarter is computed against Schedule AI's required installment for that quarter, with payments credited by actual due date.

6. **Withholding allocation election interacts with Schedule AI** — if the filer elects to allocate withholding by actual dates (rather than evenly), this election applies to both methods. See current-year instructions.

## What the agent should do

1. Ask: "Was your income roughly even across the year, or concentrated in one or two quarters?" If concentrated, compute Schedule AI.
2. Ask for quarterly cumulative AGI: through 3/31, 5/31, 8/31, 12/31. The 12/31 figure is the annual return total — already known. The other three require historical statements.
3. Compute both methods. Present the side-by-side penalty comparison.
4. Recommend whichever method gives the lower penalty.
5. If Schedule AI is recommended, file Form 2210 with Schedule AI attached. If regular method is lower, the filer can let IRS compute (no Form 2210 required).

## Sources

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — Schedule AI worksheet
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — detailed Schedule AI line-by-line
- IRC §6654(d)(2) — Annualized income installment method
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Chapter 4, Schedule AI examples
