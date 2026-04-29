# Form 1040-ES Line-by-Line Reference

Complete walkthrough of every line on the 2026 Estimated Tax Worksheet (page 8 of f1040es.pdf) and every field on the four payment vouchers (pages 9–12).

Form 1040-ES is unusual: the worksheet is for the user's records (not filed), and only the four vouchers are mailed (and only when paying by check). The agent uses the worksheet to compute the per-quarter installment.

---

## 2026 Estimated Tax Worksheet

### Line 1 — Adjusted Gross Income expected

Sum of all income the taxpayer expects, minus above-the-line adjustments:

**Income**:
- W-2 wages
- Schedule C net profit (after all expenses)
- Schedule E net rental, royalty, K-1 income
- Schedule F net farm profit
- Interest, dividends, capital gain (from sales projected for the year)
- Pension, IRA, 401(k) distributions
- Social Security (taxable portion)
- Roth conversion amount (fully taxable in year converted)
- Alimony from pre-2019 divorces (post-2018 alimony is not income to recipient)
- Unemployment compensation
- Gambling winnings, prize money

**Above-the-line adjustments** (Schedule 1 Part II):
- Educator expenses (up to $300, verify 2026 amount)
- HSA contribution
- Self-employed health insurance
- Half of self-employment tax (computed on Schedule SE Line 13)
- SEP-IRA, SIMPLE, solo 401(k) contributions (employer side)
- Self-employed retirement plan contributions
- Student loan interest (up to $2,500, verify 2026 phase-out)

**Critical**: do NOT include Roth IRA contributions (not deductible). Do NOT include traditional IRA contributions if covered by employer plan and over phase-out.

### Line 2a — Standard or itemized deduction

Pick the larger of:

- **Standard deduction** for 2026 — set by Rev. Proc. issued in late 2025; verify before filing. Estimate based on 2025 figures + inflation adjustment.
  - 2025 Single: $15,000 (Rev. Proc. 2024-40)
  - 2025 MFJ: $30,000
  - 2025 HOH: $22,500
  - Add'l for 65+ / blind: $1,600 MFJ each, $2,000 single (2025)
- **Itemized deduction** estimate (if user expects to itemize): SALT (capped $10,000), mortgage interest, charitable, medical > 7.5% AGI

Use whichever is larger.

### Line 2b — QBI deduction

20% of qualified business income from pass-through entities (Schedule C, partnership, S-corp, sole proprietorship, certain rental). Subject to taxable-income thresholds and SSTB limitations under IRC §199A.

For 2025: QBI threshold $241,950 single / $483,900 MFJ (Rev. Proc. 2024-40). 2026 figures: verify.

If the user has straightforward QBI under threshold, simply: 20% × min(QBI, taxable income excluding LTCG). If over threshold, load `references/qbi.md` (or punt to a CPA).

### Line 3 — Taxable income

`Line 1 − Line 2a − Line 2b`. If negative, enter 0.

### Line 4 — Tax from rate schedule

Apply the **2026 tax brackets** to Line 3. The agent must verify the brackets against the most recent Rev. Proc. before computing.

For 2025 (Rev. Proc. 2024-40), single brackets are:
- 10%: $0 – $11,925
- 12%: $11,925 – $48,475
- 22%: $48,475 – $103,350
- 24%: $103,350 – $197,300
- 32%: $197,300 – $250,525
- 35%: $250,525 – $626,350
- 37%: $626,350+

(MFJ, HOH, MFS brackets differ; verify each against Rev. Proc. 2024-40.)

For 2026, brackets shift by ~2-3% inflation; **verify before filing**.

**Special rate handling**:
- Long-term capital gain & qualified dividend: separate 0% / 15% / 20% rates per IRC §1(h). Use the Qualified Dividends and Capital Gain Tax Worksheet (in 1040 instructions) instead of the regular table.
- Section 1250 unrecaptured gain: 25% max
- Collectibles gain: 28% max

### Line 5 — Alternative Minimum Tax (AMT)

If applicable (Form 6251). Most filers under the 2026 AMT exemption (verify amount; 2025 was $88,100 single / $137,000 MFJ per Rev. Proc. 2024-40) will not owe AMT. High earners with significant ISO exercises, large state-tax write-offs (no longer matters post-TCJA capping), or complex deductions may.

### Line 6 — Add Lines 4 and 5

### Line 7 — Credits

Project nonrefundable credits the user expects:

- Child Tax Credit: $2,000 per qualifying child under 17 (verify 2026 amount)
- Credit for Other Dependents: $500 per non-CTC dependent
- Foreign Tax Credit (Form 1116)
- Retirement Savings Contributions Credit (Form 8880)
- Child & Dependent Care Credit (Form 2441)
- Lifetime Learning Credit (Form 8863) up to $2,000
- American Opportunity Credit (Form 8863) up to $2,500
- Energy efficient home improvement credit (Form 5695)
- Plug-in EV credit (Form 8936)

### Line 8 — Subtract Line 7 from Line 6

### Line 9 — Self-employment tax

Computed on Schedule SE:

```
SE_earnings = 0.9235 × net SE income (Schedule C profit + partnership SE income)
SS_portion = 0.124 × min(SE_earnings, SS_wage_base)
Medicare_portion = 0.029 × SE_earnings
SE_tax = SS_portion + Medicare_portion
```

For 2025: SS wage base = $176,100 (per SSA). For 2026: announced ~Oct 2025, **verify**.

If wages already at SS wage base from W-2 employment, no SS portion on SE income (only the 2.9% Medicare portion).

### Line 10 — Other taxes

- **Additional Medicare 0.9%** (Form 8959): on wages + SE earnings above:
  - Single $200,000
  - MFJ $250,000
  - MFS $125,000
- **NIIT 3.8%** (Form 8960): on lesser of net investment income or AGI excess over MAGI threshold. Same thresholds as Additional Medicare. Investment income includes interest, dividends, capital gains, rental income (passive), royalties.
- **Section 965 transition tax**: rare for individuals
- **First-time homebuyer credit recapture**: from old credit
- **Excess APTC repayment** (Form 8962): if Marketplace premium tax credit advance was overcollected
- **Section 1411 trust NIIT pass-through**: if K-1 has it

### Line 11a — Total tax

`Line 8 + Line 9 + Line 10`

### Line 11b — Refundable credits

- Earned Income Credit
- Additional Child Tax Credit
- Premium Tax Credit (refundable portion)
- American Opportunity Credit (40% refundable)

### Line 11c — Net total tax

`Line 11a − Line 11b`. This is the figure used in the safe harbor.

### Line 12a — 90% safe harbor target

`0.90 × Line 11c`

### Line 12b — Prior-year safe harbor target

```
prior_year_tax × (1.10 if prior_AGI > 150,000 (or 75,000 MFS) else 1.00)
```

The "tax" here is prior-year Form 1040 Line 24 (total tax). Check IRS Pub. 505 for the precise definition each year.

**Edge case**: if the prior tax year was less than 12 months (e.g., short-period return), Line 12b is generally not available — use Line 12a only.

### Line 12c — Required annual payment

`min(Line 12a, Line 12b)`. The taxpayer pays at least this much across the year (via withholding + estimated payments) to avoid §6654 penalty.

### Line 13 — Income tax withheld (expected)

Sum of:
- Federal withholding from W-2 (estimate based on YTD pay stub × 12/months-elapsed)
- Withholding from 1099-R pension distributions
- Voluntary withholding from Social Security (Form W-4V)
- Withholding from gambling 1099-G or backup withholding from 1099-NEC

Withholding is treated as paid evenly across the year per IRC §6654(g), even if actually withheld in Q4. This is a powerful planning lever — if the user can increase W-2 withholding late in the year, it counts as evenly distributed.

### Line 14a — Net required estimated payments

`Line 12c − Line 13`. If ≤ $0, no estimated payments required.

If `Line 14a` is between $0 and $1,000, the de minimis exception under §6654(e)(1) excuses the taxpayer (verify the threshold has not changed for the year being filed).

### Line 14b — Per-quarter installment

`Line 14a / 4` (for equal-installment method).

This is the amount written on each of the four payment vouchers (Q1, Q2, Q3, Q4).

---

## Payment vouchers (pages 9–12 of f1040es.pdf)

Each voucher has identical fields. Voucher number 1, 2, 3, or 4 is preprinted; the agent does not change it.

| Field | What goes here | Notes |
|-------|----------------|-------|
| Calendar year (top) | "2026" (or write in the year) | Matches the tax year |
| Voucher number | Preprinted (1, 2, 3, or 4) | |
| Amount of payment | From Line 14b (or adjusted for unequal installments) | Whole dollars + cents allowed |
| Filer's first name + initial + last name | Full legal name | Match SSA records |
| Filer's SSN | 9 digits | |
| If joint, spouse's first name + initial + last name | Match SSA records | Only if MFJ |
| If joint, spouse's SSN | 9 digits | Only if MFJ |
| Address | Street | |
| City, State, ZIP | Current mailing address | |
| Foreign country, province, postal code | Only if foreign address | |

The voucher is mailed with a check made out to "United States Treasury". Memo line: "2026 Form 1040-ES" + SSN.

If paying electronically, the voucher is **not** mailed.

---

## Due dates for tax year 2026

| Voucher | Period covered | Due date |
|---------|----------------|----------|
| 1 | Jan 1 – Mar 31, 2026 | April 15, 2026 |
| 2 | Apr 1 – May 31, 2026 | June 15, 2026 |
| 3 | Jun 1 – Aug 31, 2026 | September 15, 2026 |
| 4 | Sep 1 – Dec 31, 2026 | January 15, 2027 |

**Verify each year**: when a due date falls on a Saturday, Sunday, or legal holiday (DC and federal), the deadline shifts to the next business day per IRC §7503. Reconfirm against the IRS calendar before filing.

**Special rules**:
- **Farmers/fishers** (>2/3 gross from farming/fishing per IRC §6654(i)): single payment due Jan 15, 2027 OR file & pay by March 1, 2027.
- **Filing 1040 by Jan 31 with full payment**: replaces the Q4 voucher (per IRC §6654(h)).
- **Disaster relief**: when IRS announces a disaster postponement, due dates may shift; check https://www.irs.gov/newsroom/tax-relief-in-disaster-situations.

---

## Worksheet computation order (algorithm summary)

```
1. AGI = sum of all income − above-the-line adjustments
2. Taxable income = AGI − standard/itemized deduction − QBI
3. Tentative tax = bracket(taxable_income, filing_status, tax_year)
4. Add AMT if applicable
5. Subtract nonrefundable credits
6. Add SE tax (from Schedule SE)
7. Add other taxes (Add'l Medicare, NIIT, etc.)
8. = total_tax
9. Subtract refundable credits → net_total_tax
10. safe_harbor_90 = 0.90 × net_total_tax
11. safe_harbor_prior = prior_tax × (1.10 if high-AGI else 1.00)
12. required = min(safe_harbor_90, safe_harbor_prior)
13. net_estimated = required − expected_withholding
14. per_quarter = net_estimated / 4
```

The agent runs this algorithm with the user's numbers and surfaces the result for each line as shown in the SKILL.md output template.
