# Form 8962 Line-by-Line Reference

Complete lookup for every line on Form 8962. Use this when the agent needs to confirm what amount goes on a line, where it comes from, and how it's computed.

The form has five parts:

- **Part I — Annual and Monthly Contribution Amount** (Lines 1–8b)
- **Part II — Premium Tax Credit Claim and Reconciliation of APTC** (Lines 9–26)
- **Part III — Repayment of Excess Advance Payment of the PTC** (Lines 27–29)
- **Part IV — Allocation of Policy Amounts** (Lines 30–34, shared policies)
- **Part V — Alternative Calculation for Year of Marriage** (Lines 35–36)

Line map verified against the 2025 Form 8962 (Created 3/25/25) and the 2025 Instructions for Form 8962 (Oct 1, 2025), filed in 2026. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-8962 before use.

## Header

| Field | What goes here | Source |
|-------|----------------|--------|
| Name(s) shown on return | Filer's legal name as on Form 1040 | Form 1040 header |
| Your social security number | Filer's SSN or ITIN | Form 1040 header |
| Line A (checkbox) | Check only if filing MFS under the domestic-abuse / spousal-abandonment exception (Exception 2); do not attach documentation | 2025 instructions, Victims of domestic abuse or spousal abandonment |

For MFJ returns, only the *primary* filer's SSN — same as Form 1040 page 1.

---

## Part I — Annual and Monthly Contribution Amount

### Line 1 — Tax family size

| Detail | Value |
|--------|-------|
| Definition | Filer + spouse (if MFJ) + every dependent claimed on the return |
| Citation | IRC §36B(d)(1) |
| Pitfall | A child who is on the marketplace policy but is *claimed as a dependent on a different parent's return* is in that other parent's tax family, not the policyholder's |

### Line 2a — Modified AGI of taxpayer (and spouse if MFJ)

| Detail | Value |
|--------|-------|
| Computation | AGI (2025 Form 1040 Line 11a) + tax-exempt interest (Form 1040 Line 2a) + non-taxable Social Security benefits (Form 1040 Line 6a − Line 6b) + excluded foreign earned income and housing (Form 2555 Lines 45 and 50); Worksheet 1-1 in the instructions |
| Citation | IRC §36B(d)(2)(B) |

### Line 2b — Dependents' modified AGI

| Detail | Value |
|--------|-------|
| Definition | Sum of MAGI of every dependent who is *required to file a return* |
| Citation | IRC §36B(d)(2)(A)(ii) |
| Pitfall | A dependent who *chose* to file but wasn't required to file (e.g., a college student who filed only to claim a small refund of withholding) — their MAGI does NOT count |
| Filing requirement | Per Pub 501, depends on filing status, age, blindness, and gross income; for 2025 a single dependent under 65 and not blind must file if earned income was over $15,750 or unearned income over $1,350 (2025 Form 1040 instructions, Chart B); re-check each year |

### Line 3 — Household income

| Detail | Value |
|--------|-------|
| Computation | Line 2a + Line 2b (combine even if negative; if the total is less than zero, enter -0-) |
| Citation | IRC §36B(d)(2)(A) |

### Line 4 — Federal poverty line for tax family size

| Detail | Value |
|--------|-------|
| Source | HHS Poverty Guidelines, **prior-year** value for state group (48+DC, AK, or HI) |
| Citation | IRC §36B(d)(3)(B); Form 8962 instructions Tables 1-1, 1-2, 1-3 |
| Year rule | 2025 returns use 2024 FPL; 2026 returns use 2025 FPL — see [`fpl-tables.md`](./fpl-tables.md) |
| State groups | Checkbox (a) Alaska; (b) Hawaii; (c) other 48 states and DC. If the filer lived in Alaska and/or Hawaii for part of the year, or joint filers lived in different states, use the table with the higher amounts |

### Line 5 — Household income as percentage of FPL

| Detail | Value |
|--------|-------|
| Computation | (Line 3 / Line 4) × 100, rounded *down* to nearest whole percent |
| Cap | If household income > 400% FPL: enter 401 (2025 instructions, Worksheet 2) |
| Pitfall | "Rounded down" — 199.9% becomes 199%, not 200% |

### Line 6 — Reserved for future use

On the 2025 form, Line 6 reads "Reserved for future use." Leave it blank.

### Line 7 — Applicable figure

| Detail | Value |
|--------|-------|
| Source | IRS Form 8962 Instructions, Table 2 (year-specific applicable figure table) |
| Citation | IRC §36B(b)(3)(A) |
| Year-aware | ARPA modified table for 2021–2022; IRA extended it through 2025 (2025: 0% to 8.5%, Table 2); 2026 uses Rev. Proc. 2025-25 (2.10% to 9.96%) and allows no PTC above 400% FPL |
| See also | [`applicable-figure.md`](./applicable-figure.md) |

### Line 8a — Annual contribution amount

| Detail | Value |
|--------|-------|
| Computation | Line 3 × Line 7, rounded to the nearest whole dollar |

### Line 8b — Monthly contribution amount

| Detail | Value |
|--------|-------|
| Computation | Line 8a / 12, rounded to the nearest whole dollar |

---

## Part II — Premium Tax Credit Claim and Reconciliation

### Line 9 — Allocating policy amounts or using the alternative calculation for year of marriage?

| Detail | Value |
|--------|-------|
| Yes / No | Yes if a marketplace policy must be allocated with another tax family during any month (instructions, Line 9 and Table 3), or if electing the alternative calculation for year of marriage (Table 4); No otherwise |
| If Yes | Complete Part IV and/or Part V before Line 10 |

### Line 10 — Annual or monthly calculation?

| Detail | Value |
|--------|-------|
| Yes (Annual) | For every qualified health plan: enrolled all 12 months, the same enrollment premium (1095-A column A) every month, and the same correct applicable SLCSP premium (column B) every month (2025 instructions, Line 10) |
| No (Monthly) | Fewer than 12 months of enrollment, any month's premium or SLCSP differed, or Part IV was completed |
| If Yes | Complete Line 11 (one row); skip Lines 12–23 |
| If No | Skip Line 11; complete Lines 12–23 (12 rows) |

### Line 11 — Annual calculation (used if Line 10 = Yes)

Single row with six columns:

| Column | Detail |
|--------|--------|
| 11a — Annual enrollment premiums | Sum of 1095-A Column A for the months coverage was in force |
| 11b — Annual applicable SLCSP premium | Sum of 1095-A Column B |
| 11c — Annual contribution amount | = Line 8a |
| 11d — Annual maximum premium assistance | = max(0, Column 11b − Column 11c) |
| 11e — Annual Premium Tax Credit allowed | = min(Column 11a, Column 11d) |
| 11f — Annual advance payment of PTC | Sum of 1095-A Column C |

### Lines 12–23 — Monthly calculation (used if Line 10 = No)

12 rows for January through December. Each row has the same six columns as Line 11, sourced from the corresponding month of Form 1095-A. Months with no coverage are left blank (if columns (a) and (b) are blank, leave column (c) blank).

| Line | Month |
|------|-------|
| 12 | January |
| 13 | February |
| 14 | March |
| 15 | April |
| 16 | May |
| 17 | June |
| 18 | July |
| 19 | August |
| 20 | September |
| 21 | October |
| 22 | November |
| 23 | December |

### Line 24 — Total Premium Tax Credit

| Detail | Value |
|--------|-------|
| Computation | Sum of Column E (annual: Line 11e; monthly: Lines 12e through 23e) |

### Line 25 — Advance payment of PTC

| Detail | Value |
|--------|-------|
| Computation | Sum of Column F (annual: Line 11f; monthly: Lines 12f through 23f) |
| Cross-check | Should equal sum of Form 1095-A Column C across all 12 months |

### Line 26 — Net Premium Tax Credit

| Detail | Value |
|--------|-------|
| Trigger | Line 24 ≥ Line 25 (enter -0- if equal; leave blank if Line 25 > Line 24) |
| Computation | Line 24 − Line 25 |
| Routes to | **Schedule 3 Line 9** (refundable credit) |

If Line 26 > 0, skip Lines 27–29. If Part V was elected and Line 24 > Line 25, enter -0- on Line 26.

## Part III — Repayment of Excess Advance Payment of the PTC (Lines 27–29)

### Line 27 — Excess advance payment of PTC

| Detail | Value |
|--------|-------|
| Trigger | Line 25 > Line 24 |
| Computation | Line 25 − Line 24 |

### Line 28 — Repayment limitation

| Detail | Value |
|--------|-------|
| Source | Form 8962 instructions Table 5, year-specific; based on Line 5 (% FPL) and filing status (single vs. any other) |
| Citation | IRC §36B(f)(2)(B) (tax years before 2026); Treas. Reg. §1.36B-4(a)(3) |
| Year rule | 2025: $375/$750 below 200%; $975/$1,950 at 200–<300%; $1,625/$3,250 at 300–<400%; see [`repayment-limitation.md`](./repayment-limitation.md) |
| 400% rule | Line 5 of 400 or more: leave Line 28 blank, no limitation (2025 instructions, Line 28) |
| 2026 rule | No limitation at any income: P.L. 119-21 §71305 struck §36B(f)(2)(B) for tax years beginning after December 31, 2025. The 2026 Form 8962 was not yet released on 2026-10-06; follow its instructions for how Line 28 is handled |

### Line 29 — Excess advance Premium Tax Credit repayment

| Detail | Value |
|--------|-------|
| Computation | Lesser of Line 27 or Line 28; if Line 28 is blank, Line 27 |
| Routes to | **Schedule 2 Line 1a** (additional tax) |

---

## Part IV — Allocation of Policy Amounts (Lines 30–34)

Used when a single marketplace policy covered two tax families during any month. Common cases:

- Divorced parents sharing a policy for joint children
- Adult child on parents' marketplace policy who files independently
- Married couple filing separately (rare; usually MFS = no PTC except in domestic abuse / spousal abandonment scenarios)

Lines 30–33 each represent one allocation (up to four). For each, enter:

| Field | Detail |
|-------|--------|
| (a) Policy number | From Form 1095-A line 2 (last 15 characters if longer) |
| (b) SSN of other taxpayer | The other tax family's primary filer SSN |
| (c) Allocation start month | First month the allocation applies ("01"–"12") |
| (d) Allocation stop month | Last month the allocation applies ("01"–"12") |
| (e) Premium % | This filer's share as a decimal (e.g., "0.50") |
| (f) SLCSP % | This filer's share as a decimal |
| (g) APTC % | This filer's share as a decimal |

Line 34 asks whether all allocations are complete; Yes → apply the percentages to the 1095-A amounts and enter the combined monthly totals on Lines 12–23, columns (a), (b), (f). The percentages must total 100% across all tax families on the policy. Filers can negotiate the split or use a default rule; see [`allocation.md`](./allocation.md).

---

## Part V — Alternative Calculation for Year of Marriage (Lines 35–36)

If the filers were each unmarried on January 1, married on December 31, file jointly, had someone enrolled before the first full month of marriage, and received excess APTC, Part V can reduce the excess APTC repayment for pre-marriage months. It cannot increase the net PTC.

| Line | Detail |
|------|--------|
| 35 | Filer: (a) alternative family size, (b) alternative monthly contribution amount, (c) alternative start month, (d) alternative stop month |
| 36 | Spouse: same four columns |

Each spouse uses one-half of the couple's household income (Line 3 / 2) and the family size they would have had without the marriage (Pub 974, Worksheets I and III). See [`year-of-marriage.md`](./year-of-marriage.md) for the worked computation.

---

## Routing summary

| Form 8962 Line | Destination |
|----------------|-------------|
| Line 26 (Net PTC) | Schedule 3 Line 9 (refundable credit) |
| Line 29 (Excess APTC repayment) | Schedule 2 Line 1a (additional tax) |

Lines 26 and 29 are mutually exclusive — exactly one is nonzero per Form 8962 (or both are zero, e.g., PTC and APTC both zero).
