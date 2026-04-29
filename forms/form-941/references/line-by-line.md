# Form 941 Line-by-Line Reference

Complete lookup for every line on Form 941. Use this when the agent needs to confirm where a payroll item belongs or what a line means.

The IRS revises Form 941 most tax years (often in March). Line numbers are stable but residual COVID-era credit lines (11b–11f, 13b–13z) shift labels. Always verify line labels against the most recent revision at https://www.irs.gov/pub/irs-pdf/f941.pdf.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| EIN | 9 digits, format XX-XXXXXXX | Cannot be SSN. Must match SS-4. |
| Name | Legal name as on SS-4 / EIN application | Spelling exact; IRS rejects mismatches |
| Trade name | DBA, if applicable | Blank if same as legal name |
| Address | Where the IRS mails notices | Address change → file Form 8822-B (not on 941) |
| Quarter check box | 1 (Jan–Mar), 2 (Apr–Jun), 3 (Jul–Sep), 4 (Oct–Dec) | Match to the calendar quarter; do not use fiscal year |

---

## Part 1 — Quarter Taxes

### Line 1 — Number of employees who received wages, tips, or compensation

Single-date snapshot, not an average. The IRS picks the same date each quarter:

| Quarter | Snapshot date |
|---------|--------------|
| Q1 | Pay period including March 12 |
| Q2 | Pay period including June 12 |
| Q3 | Pay period including September 12 |
| Q4 | Pay period including December 12 |

Includes anyone who got a paycheck in that pay period — full-time, part-time, seasonal. Excludes 1099 contractors and statutory non-employees.

### Line 2 — Wages, tips, and other compensation

Total federal-income-tax wages paid this quarter. Generally the same as Box 1 wages on year-end W-2s.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Salaries, hourly wages, overtime, bonuses, commissions | 1099 contractor payments (those go on Form 1099-NEC) |
| Taxable fringe benefits (e.g., personal use of company car, taxable group-term life over $50K coverage) | Pretax §125 cafeteria plan deductions (those reduce Line 2) |
| Sick pay paid by the employer | Pretax 401(k) deferrals (reduce Line 2) |
| Severance pay | Pretax HSA contributions via §125 (reduce Line 2) |
| Tips (also reported separately on Line 5b) | Workers' compensation benefits |
| Taxable reimbursements (e.g., commuting allowance over IRS limit) | Qualified retirement plan distributions |

Pretax deductions: §125 cafeteria plan (health, dental, FSA, dependent care up to limit), §401(k) traditional deferrals, §403(b), §457(b), §132 transit/parking up to monthly cap. These reduce Line 2 (federal income tax wages) but **do not** reduce Line 5a / 5c (FICA wages) — except §125 cafeteria plan, which does reduce both.

### Line 3 — Federal income tax withheld

Sum of all FIT withholding from this quarter's paychecks. Includes:

- Regular W-4 withholding
- Supplemental wage withholding (bonuses, commissions, severance) — flat 22% if separately identified, or aggregate method
- Backup withholding on W-2 wages (rare)
- Voluntary withholding on sick pay paid by third party (if employer is the payer of record)

If an employee claims exempt on Form W-4 (very narrow eligibility), $0 withheld but they still appear in Line 1 and 2.

### Line 4 — Wages not subject to SS or Medicare (checkbox)

Check **only if** all wages this quarter are exempt from both SS and Medicare. Rare. Examples:

- Employer is a state/local government with employees in a §218 agreement excluding them
- Employer is a religious organization with §3121(w) election
- Wages are paid to a child under age 18 by a parent's sole proprietorship (FICA-exempt under §3121(b)(3))

If checked, skip Lines 5a–5e.

### Line 5a — Taxable Social Security wages

| | Column 1 (wages) | Column 2 (tax) |
|---|------------------|----------------|
| 5a | SS wages this quarter, capped at YTD wage base | Column 1 × 0.124 |

**Wage base**: $176,100 for 2025 (SSA Press Release 2024-XX). Verify 2026 at https://www.ssa.gov/oact/cola/cbb.html — typically announced in October of the prior year.

The 12.4% combines:
- Employer SS tax: 6.2% (IRC §3111(a))
- Employee SS tax: 6.2% (IRC §3101(a))

Per-employee cap mechanics: Once an employee's YTD SS wages reach the wage base in any quarter, additional wages are SS-exempt for the rest of the calendar year. Restart at $0 in January.

### Line 5a(i) — Qualified sick leave wages (FFCRA / ARPA)

Default $0 for 2026 quarters. The Families First Coronavirus Response Act (FFCRA) and American Rescue Plan Act (ARPA) sick-leave credits expired September 30, 2021. Lines 5a(i) and 5a(ii) remain on the form so retroactive 941-X corrections can use them.

If $0, multiplier is 0.062 (employer-only SS, since the credit covered the employee share).

### Line 5a(ii) — Qualified family leave wages

Same as 5a(i). Default $0. Multiplier 0.062.

### Line 5b — Taxable Social Security tips

Tips reported by employees that are subject to SS tax. Usually only restaurants, salons, hospitality. The combined rate is 12.4% (same as 5a). Tips below $20/month per employee in a single establishment are not "wages" for FICA purposes (IRC §3121(a)(12)).

### Line 5c — Taxable Medicare wages and tips

Same wages as Line 5a but **without** the wage-base cap (Medicare has no cap). Includes tips from Line 5b.

| | Column 1 | Column 2 |
|---|----------|----------|
| 5c | Medicare wages + tips | Column 1 × 0.029 |

The 2.9% combines:
- Employer Medicare: 1.45% (IRC §3111(b))
- Employee Medicare: 1.45% (IRC §3101(b)(1))

Often Line 5c column 1 > Line 5a column 1 (because of high-income employees who maxed out SS but still owe Medicare on additional wages).

### Line 5d — Wages subject to Additional Medicare Tax withholding

Wages paid in excess of $200,000 to any individual employee in the calendar year. 0.9% Additional Medicare withholding applies (IRC §3101(b)(2)).

| | Column 1 | Column 2 |
|---|----------|----------|
| 5d | Wages > $200K threshold | Column 1 × 0.009 |

**Employer does not match** the 0.9% — employee-only. The $200,000 threshold is **per employer**, not per employee's total income across employers. Single threshold applies regardless of employee's marital status; the employee reconciles on Form 8959 with their personal return.

Mechanics: Once an employee's YTD wages from this employer cross $200,000, withhold 0.9% on the excess for each subsequent paycheck.

### Line 5e — Total Social Security and Medicare taxes

Sum of column 2 amounts: Line 5a + Line 5b + Line 5c + Line 5d.

### Line 5f — Section 3121(q) Notice and Demand

Tax on unreported tips that the IRS has formally demanded via a Section 3121(q) Notice and Demand letter. Rare. Default $0.

### Line 6 — Total taxes before adjustments

```
Line 6 = Line 3 + Line 5e + Line 5f
```

### Line 7 — Current quarter adjustment for fractions of cents

Reconciles the rounding mismatch between per-paycheck FICA (rounded to cents) and quarterly aggregate FICA (computed exactly on totals). Usually within ±$1 per quarter.

### Line 8 — Current quarter sick-pay adjustment

Negative adjustment when a third-party insurance carrier paid sick pay to employees and withheld the employee FICA share itself. The employer subtracts that amount from Line 6 because it's not the employer's liability.

### Line 9 — Current quarter adjustments for tips and group-term life insurance

Specific adjustments for:
- Uncollected employee FICA on tips (employee didn't have enough non-tip wages for the employer to withhold)
- Uncollected employee FICA on group-term life over $50K coverage paid to former employees

Default $0 unless these specific situations apply.

### Line 10 — Total taxes after adjustments

```
Line 10 = Line 6 + Line 7 + Line 8 + Line 9
```

### Line 11a — Qualified small business payroll tax credit for increasing research activities

If the employer is a qualified small business (gross receipts < $5M for current year and no gross receipts for any year before the 5-year window) and elected on Form 6765 to apply up to $500,000 of §41 R&D credit against payroll tax: enter the amount from Form 8974 here. See [`r-and-d-payroll-credit.md`](./r-and-d-payroll-credit.md).

### Lines 11b through 11f — Residual COVID-era credits

These lines reference FFCRA sick-leave credits, ARPA family-leave credits, employee retention credit (ERC). All expired:
- Sick/family leave credit: expired September 30, 2021
- ERC: ended for most employers September 30, 2021 (recovery startup businesses had until December 31, 2021)

Default $0. The lines persist on the form for 941-X retroactive corrections — and for completed 941-X claims, the IRS continues to process and audit ERC claims aggressively (see Notice 2021-49 and ongoing IRS enforcement campaigns).

### Line 11g — Total nonrefundable credits

Sum of 11a–11f.

### Line 12 — Total taxes after credits

```
Line 12 = Line 10 − Line 11g
```

### Line 13a — Total deposits this quarter

Sum of all federal tax deposits made via EFTPS during this quarter. Each deposit has a date and amount; the user must reconcile against EFTPS confirmation numbers.

### Lines 13b through 13z — Refundable COVID credits

Same residual structure as 11b–11f. Default $0.

### Line 13g — Total deposits + refundable credits

Sum of 13a + 13b + ... + 13z.

### Line 14 — Balance due

```
If Line 12 > Line 13g:  Line 14 = Line 12 − Line 13g
```

If > $0: pay with the return (check + Form 941-V payment voucher) OR pay via EFTPS. Late payment triggers FTD penalty + interest.

### Line 15 — Overpayment

```
If Line 13g > Line 12:  Line 15 = Line 13g − Line 12
```

Elect to **apply to next return** (recommended for ongoing employers) OR **request refund** (slow — 6+ weeks).

---

## Part 2 — Deposit Schedule and Tax Liability (Line 16)

Pick **exactly one** box.

### Box 1 — Liability under $2,500 + no $100K rule trigger

Eligible if:
- Total Line 12 for current quarter < $2,500, AND
- Line 12 for *prior* quarter was also < $2,500, AND
- No single-day liability ≥ $100,000 occurred (next-day deposit rule, IRS Reg. §31.6302-1(c)(3))

If eligible: pay the entire Line 14 with the return. No daily/monthly schedule entries.

### Box 2 — Monthly schedule depositor

Eligible if:
- Total taxes during the lookback period (Jul 1, two years ago through Jun 30, last year) ≤ $50,000, AND
- Box 1 doesn't apply

Fill in three monthly liability amounts. Total must equal Line 12. Each monthly amount represents the tax liability *incurred* during that month, regardless of when actually deposited.

### Box 3 — Semi-weekly schedule depositor

Required if:
- Total taxes during the lookback period > $50,000, OR
- A single-day liability ≥ $100,000 was incurred (any time during current/prior quarter — once triggered, semi-weekly applies for the rest of current year *and* the entire next year)

Attach **Schedule B (Form 941)** showing daily liability for each pay date during the quarter. Schedule B is a 3-month grid.

See [`deposit-schedules.md`](./deposit-schedules.md) for full mechanics.

---

## Part 3 — Final Return / Seasonal

### Line 17 — Stopped paying wages

Check if the employer permanently stopped paying wages this quarter and won't have to file in the future. Provide the final wage-paid date. Triggers IRS final-return processing.

### Line 18a — Seasonal employer

Check if the employer doesn't have to file 941 every quarter (e.g., resort hotel, agricultural processor). Marks the IRS to skip dunning notices for off-season quarters. The employer must still file every quarter when wages are paid.

### Line 18b — (newer revisions) Recovery Startup Business indicator for ERC

Was relevant for 2021 ERC. Default unchecked for 2026 quarters.

---

## Part 4 — Third-Party Designee

Optional. Authorizes the IRS to discuss the return with a third party (payroll bureau, CPA, payroll software vendor) without a separate Form 2848 / 8821. Requires:
- Designee's name
- Phone
- 5-digit PIN

Only valid for *this* return. For ongoing representation, file Form 2848 (POA) or Form 8821 (Tax Information Authorization).

---

## Part 5 — Sign Here

The return must be signed by an authorized officer:

- **Sole proprietor / SMLLC**: the owner
- **Corporation / S-corp**: president, vice president, or principal officer
- **Partnership / multi-member LLC**: a partner / member with authority
- **Single-member LLC taxed as corp**: an officer

Required fields:
- Print name
- Title
- Date
- Phone
- Signature (paper) or e-file PIN (94x Online Signature PIN, 10 digits)

The paid-preparer section is for CPAs / EAs filing on behalf of the employer. Solo employers leave it blank.
