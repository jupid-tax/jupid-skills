# Form 8959 — Employer Withholding Rules (IRC §3102(f))

The employer's obligation to withhold the Additional Medicare Tax does NOT mirror the filer's filing-status threshold. Understanding the gap is the key to predicting whether a filer will owe at filing.

## The employer rule

Per IRC §3102(f) and Treasury Regulation §31.3102-4, an employer must:

1. Withhold the regular **1.45% Medicare tax** on every dollar of Medicare wages from dollar one
2. Withhold an **additional 0.9%** on wages it pays to an employee in excess of **$200,000 in the calendar year**

Both withholdings appear in W-2 Box 6 (Medicare tax withheld). The employer does NOT distinguish between filing statuses on the W-2 — it does not know the employee's filing status when computing payroll.

The $200,000 trigger is **per employer, per employee, per calendar year**.

## What this means for filers

### Single filer, single employer, $260K W-2 wages

- Employer withholds 1.45% × $260,000 = $3,770 (regular Medicare)
- Employer withholds 0.9% × ($260,000 − $200,000) = $540 (additional)
- W-2 Box 6 = $4,310
- Form 8959 Line 18 = $540 (owed)
- Form 8959 Line 24 = $540 (already withheld via Box 6)
- Net at filing = $0

Employer absorbs the surtax through payroll. Filer reconciles on Form 8959 but owes nothing additional.

### Single filer, two employers, $150K + $90K = $240K total

- Employer A withholds 1.45% × $150K = $2,175 (no additional, under $200K)
- Employer B withholds 1.45% × $90K = $1,305 (no additional)
- W-2 Box 6 total = $3,480
- Form 8959 Line 1 = $240,000
- Form 8959 Line 5 = $200,000 (single threshold)
- Form 8959 Line 7 = $360 owed
- Form 8959 Line 19 = $3,480
- Form 8959 Line 20 = $240K × 1.45% = $3,480
- Form 8959 Line 21 = $0 (no additional withheld)
- Form 8959 Line 24 = $0
- Net at filing = $360 owed

Filer owes $360 at filing because each individual employer was under its own $200K trigger.

### MFJ couple, two earners, $180K + $90K = $270K total

- Employer A (Spouse 1) withholds 1.45% × $180K = $2,610 (no additional, under $200K)
- Employer B (Spouse 2) withholds 1.45% × $90K = $1,305 (no additional)
- Combined W-2 Box 6 = $3,915
- Form 8959 Line 1 = $270,000 (combined)
- Form 8959 Line 5 = $250,000 (MFJ threshold)
- Form 8959 Line 7 = $180 owed
- Form 8959 Line 19 = $3,915
- Form 8959 Line 20 = $270K × 1.45% = $3,915
- Form 8959 Line 21 = $0
- Form 8959 Line 24 = $0
- Net at filing = $180 owed

The classic dual-earner MFJ pattern.

### Single filer, single employer, $400K W-2 wages

- Employer withholds 1.45% × $400K = $5,800 (regular)
- Employer withholds 0.9% × ($400K − $200K) = $1,800 (additional)
- W-2 Box 6 = $7,600
- Form 8959 Line 1 = $400,000
- Form 8959 Line 5 = $200,000 (single)
- Form 8959 Line 6 = $200,000
- Form 8959 Line 7 = $1,800 owed
- Form 8959 Line 19 = $7,600
- Form 8959 Line 20 = $400K × 1.45% = $5,800
- Form 8959 Line 21 = $1,800 (additional withheld)
- Form 8959 Line 24 = $1,800
- Net at filing = $0

Single filer with one high-wage employer: employer withholding is correct. No filing balance from Form 8959.

### MFS filer, single employer, $130K W-2 wages

- Employer withholds 1.45% × $130K = $1,885 (regular, no additional — under $200K trigger)
- W-2 Box 6 = $1,885
- Form 8959 Line 1 = $130,000
- Form 8959 Line 5 = $125,000 (MFS threshold — the lowest)
- Form 8959 Line 7 = $5,000 × 0.9% = $45 owed
- Form 8959 Line 24 = $0
- Net at filing = $45 owed

Filer owes $45 because MFS lowers the filer threshold to $125K but the employer trigger remains $200K.

## When over-withholding happens

Less common but exists. An employer can over-withhold under the additional 0.9% rule if:

- The filer is MFS at $125K threshold but the employer paid more than $200K — the employer correctly withheld the additional 0.9% on the over-$200K portion, but the filer's own Form 8959 calculation may show *more* surtax owed (filer's combined wages or SE income above $125K)
- The filer changes employers mid-year, and the second employer pays over $200K, withholding correctly above $200K from its own payroll, while the first employer also withheld correctly from its own — but the filer's combined wages exceed neither's individual trigger, leaving both withholdings correct from each employer's view but mismatched against the filer's combined position

The reconciliation at Form 8959 Line 21 always settles to the correct number. Over- or under-withheld amounts flow through Line 24 to Form 1040 Line 25c, and any imbalance against Line 18 (Schedule 2 Line 11) flows through normal Form 1040 totals.

## Multiple-employer planning

If a filer expects to be in the multiple-employer-under-trigger pattern next year (e.g., two W-2 jobs, neither over $200K, combined over the filing-status threshold), the agent should recommend:

1. **Updated Form W-4 with Step 4(c) extra withholding**: have one employer withhold an additional fixed amount per pay period to absorb the expected surtax. If the user expects $360 of surtax annually, $14 per biweekly paycheck covers it.
2. **Quarterly Form 1040-ES estimates**: alternative if the filer prefers to pay quarterly and not adjust W-4. Use the Additional Medicare Tax estimate as part of the total estimated tax computation.

The agent should NOT recommend asking the second employer to start withholding additional Medicare tax voluntarily — employers cannot withhold the 0.9% additional unless their own payroll to the employee crosses $200K.

## Self-employment has no employer-side withholding

For SE income, there is no withholding mechanism — the filer pays via quarterly estimated taxes (Form 1040-ES). If a filer expects to owe Additional Medicare Tax on SE income, they should include it in their quarterly estimates. See Form 1040-ES Worksheet for the computation.

## Sources

- IRC §3102(f) — Employer withholding obligation, 0.9% on wages above $200K from a single employer
- Treasury Reg. §31.3102-4 — Withholding rules for Additional Medicare Tax
- [Instructions for Form 8959](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — Part V reconciliation
- [Form W-4](https://www.irs.gov/pub/irs-pdf/fw4.pdf) — Step 4(c) for extra withholding
- [Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) — Quarterly estimated tax for SE Additional Medicare Tax
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (Additional Medicare Tax planning chapter)
