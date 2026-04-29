# Form 2210 Line-by-Line Reference

Complete lookup for every line on Form 2210. Use this when the agent needs to confirm where an input belongs or what a line means.

**Important caveat**: Form 2210 has been renumbered between revisions. The line labels are stable; line *numbers* have shifted. Always verify against the current-year form before transcribing. The structure below reflects the post-2018 revisions (Tax Cuts and Jobs Act onward) and should match the current form, but check.

## Header

| Field | What goes here |
|-------|----------------|
| Name(s) shown on return | Same as Form 1040 header (joint string for MFJ) |
| Your social security number | Filer's SSN (the spouse's SSN does not appear on Form 2210 separately for MFJ) |

---

## Part I — Required Annual Payment

The "did the safe harbor save me from a penalty?" computation.

### Line 1 — Current-year tax

Form 1040 Line 22 (per the worksheet in the current-year Form 2210 instructions) — generally total tax minus refundable credits (excluding the Earned Income Credit and the additional child tax credit), plus other items per worksheet.

### Line 2 — Other taxes per current-year worksheet

Includes self-employment tax (Schedule SE), Additional Medicare Tax (Form 8959), Net Investment Income Tax (Form 8960), uncollected SS/Medicare on tips (Form 4137), and certain other items. See current-year Form 2210 Line 2 worksheet.

### Line 3 — Refundable credits

Premium tax credit (Form 8962), refundable child credit, recovery rebate credit (year-specific), etc.

### Line 4 — Subtotal

```
Line 4 = Line 1 + Line 2 − Line 3
```

This is the "current-year tax" against which the 90% safe harbor is measured.

### Line 5 — 90% of Line 4

```
Line 5 = Line 4 × 0.90
```

This is the current-year safe harbor amount.

### Line 6 — Withholding

Total federal income tax withheld during the year:
- W-2 Box 2 (federal income tax)
- 1099-R / 1099-MISC / 1099-NEC Box 4 (any 1099 with federal withholding)
- Form 8959 Line 24 (Additional Medicare Tax withheld)
- Backup withholding on 1099-INT / 1099-DIV
- Withholding on Social Security benefits (Form SSA-1099)

Treated as paid evenly across the four quarters under IRC §6654(g)(1) absent an election to use actual dates.

### Line 7 — Line 5 minus Line 6

If Line 7 ≤ $1,000, the de minimis exception applies (IRC §6654(d)(1)(A)) and the filer owes no penalty. The form has a flowchart instruction at this line: "If Line 7 ≤ $1,000, stop here. You do not owe a penalty."

### Line 8 — Prior-year tax × 100% (or 110% if applicable)

Prior-year total tax (per a parallel worksheet to Lines 1–4 above, applied to the prior-year return).

Multiply by:
- **100%** if prior-year AGI ≤ $150,000 (≤ $75,000 if MFS)
- **110%** if prior-year AGI > $150,000 (> $75,000 if MFS)

This is the prior-year safe harbor amount. Codified at IRC §6654(d)(1)(B)(ii) and §6654(d)(1)(C).

### Line 9 — Required annual payment

```
Line 9 = smaller of Line 5 or Line 8
```

The filer needed Line 9 in total payments (withholding + estimates) by year-end to avoid penalty. If they had less, the difference (per quarter) is the underpayment that accrues penalty.

---

## Part II — Reasons for Filing

Three checkboxes for waiver requests. The filer must check at least one box to require Form 2210 to be filed (otherwise the IRS computes automatically). If filer is using Schedule AI without a waiver, see Part III box.

### Box A — Request waiver based on retirement (after age 62) or disability

Available if the filer:
- Retired after age 62 in the prior or current year, AND
- The underpayment was due to reasonable cause and not willful neglect

The IRS reviews the waiver claim. Substantiation required: retirement letter or disability documentation.

### Box B — Request waiver based on casualty, disaster, or other unusual circumstances

Available for:
- Federally declared disaster (the IRS often automatically extends deadlines for these; check if extension already applies)
- Casualty loss (fire, flood, theft) directly causing the underpayment
- Other unusual circumstances per IRS judgment

Substantiation required: insurance claims, police reports, or formal disaster declaration.

### Box C — Per current-year form

Sometimes used for COVID-era waivers or other discretionary categories. Verify against the current-year form.

### Box for Schedule AI

Separate from waivers — checked if the filer is using the annualized income installment method (Schedule AI) to compute the penalty. Schedule AI is opt-in.

---

## Part III — Penalty Computation (Regular Method)

### Section A — Required Installments

For each of the four quarterly periods:

| Quarter | Period covered | Cumulative % of required annual payment | Due date |
|---------|----------------|------------------------------------------|----------|
| Q1 | Jan 1 – Mar 31 | 25% | April 15 |
| Q2 | Apr 1 – May 31 | 50% | June 15 |
| Q3 | Jun 1 – Aug 31 | 75% | September 15 |
| Q4 | Sep 1 – Dec 31 | 100% | January 15 of following year |

Required installment for each quarter:

```
Q1 required = 25% × Line 9 required annual payment
Q2 required = 50% × Line 9 (cumulative)
Q3 required = 75% × Line 9 (cumulative)
Q4 required = 100% × Line 9 (cumulative)
```

If using Schedule AI, replace these with Schedule AI's quarter-specific amounts (which are usually lower for back-loaded income, higher for front-loaded income).

### Section B — Withholding Allocated

Default: total annual withholding ÷ 4 per quarter (cumulatively: W/4, 2W/4, 3W/4, W).

Election to use actual dates: per IRC §6654(g)(1) flush language, the filer can elect to treat withholding as paid on actual dates rather than evenly. This benefits filers with concentrated withholding (e.g., big Q4 bonus). Election is per current-year instructions.

### Section C — Estimated Tax Payments

Each estimated tax payment counts toward the quarter in which it was made (or earlier quarters via the "applied to prior quarter" mechanic, but generally not — payments are applied to the quarter when received).

A payment on April 14 counts toward Q1. A payment on April 16 counts toward Q2 (Q1 underpayment accrues penalty from April 15 to April 16 for that day).

### Section D — Underpayment per Quarter

```
Quarterly underpayment = max(cumulative required − cumulative paid, 0)

cumulative paid = withholding allocated to date + estimated tax paid by quarter due date
```

### Section E — Penalty per Quarter

```
Penalty for quarter = underpayment × (days late / 365) × penalty rate

days late = days from quarter due date until either:
            - the date the underpayment is satisfied by a later payment, OR
            - April 15 of the following year, whichever is earlier

penalty rate = federal short-term rate + 3%, set by IRS Revenue Ruling each quarter
              (rate compounds daily)
```

Form 2210 has a worksheet ("Short Method" or quarter-by-quarter table) that simplifies this — see current-year instructions for the rate table.

### Total Penalty

```
Total penalty = sum of penalties across the four quarters

→ flows to Form 1040 Line 38 (Estimated tax penalty)
```

---

## Schedule AI — Annualized Income Installment Method

Replaces Section A required installments with quarter-by-quarter amounts based on actual cumulative income. See `references/annualized-income-method.md` for full worksheet structure.

Schedule AI columns:

| Column | Period | Annualization factor | Cumulative installment % |
|--------|--------|---------------------|--------------------------|
| (a) | Jan 1 – Mar 31 | 4 | 22.5% |
| (b) | Jan 1 – May 31 | 2.4 | 45% |
| (c) | Jan 1 – Aug 31 | 1.5 | 67.5% |
| (d) | Jan 1 – Dec 31 | 1 | 90% |

For each column:
1. Cumulative AGI through the column's end date
2. Annualized AGI = cumulative × factor
3. Tax on annualized AGI using current-year brackets
4. De-annualized tax = tax × (1 / factor)
5. Required cumulative installment = de-annualized tax × column percentage

Schedule AI requires:
- Quarter-by-quarter income data
- Quarter-by-quarter deduction data (or pro-rated standard deduction)
- Knowledge of current-year tax brackets

If Schedule AI's required installment for a quarter is *less than* the regular method's installment, the lower figure applies for that quarter. The filer always uses whichever method gives the lower required installment per quarter — there is no "all-or-nothing" requirement.

---

## Special situations

### Farmers and fishermen

If at least 2/3 of gross income is from farming or fishing, special rules apply:
- Different installment percentages
- Single payment by January 15 instead of four quarterly payments
- Different safe harbor (66.67% vs. 90%)

These filers use **Form 2210-F** (separate form), not Form 2210. Out of scope for this skill; redirect to Form 2210-F if the user qualifies.

### Fiscal-year filers

Most individuals are calendar-year. If filer is fiscal-year (very rare), the quarterly due dates shift accordingly. See current-year Form 2210 instructions for fiscal-year due dates.

### Estates and trusts

Estates and trusts use Form 2210 too but with different rules. For estates, no penalty applies in the year of death and the following year (IRC §6654(l)(2)). Trusts have specific rules under IRC §6654(l). Out of scope for this skill — covers individuals.

### Joint return where one spouse died during the year

Use the surviving spouse's filing status; safe harbor uses the joint prior-year tax (the joint return for the prior year).

### Mid-year residency change (non-resident → resident or vice versa)

The required annual payment is computed only on the income subject to US tax during the residency period. See current-year Pub. 519 for rules.

### Large estimated payment at year-end

A January 15 estimated payment ("Q4 payment") satisfies Q4 required installment. It does NOT retroactively satisfy Q1, Q2, or Q3 required installments — those accrue penalty from their respective due dates until either paid (via earlier payment) or April 15. A common filer mistake: assuming a Q4 estimate "back-fills" earlier underpayments. It does not.

---

## Sources

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf)
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf)
- IRC §6654 — Failure by individual to pay estimated income tax
- IRC §6654(d)(1)(A) — $1,000 de minimis
- IRC §6654(d)(1)(B) — First-year exception, prior-year safe harbor
- IRC §6654(d)(1)(C) — 110% safe harbor for high-AGI prior-year filers
- IRC §6654(g)(1) — Withholding allocated equally across quarters absent election
- IRC §6621 — Penalty rate (federal short-term rate + 3%)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax
