# Form 8962 Line-by-Line Reference

Complete lookup for every line on Form 8962. Use this when the agent needs to confirm what amount goes on a line, where it comes from, and how it's computed.

The form has five parts:

- **Part I — Annual and Monthly Contribution Amount** (Lines 1–8b)
- **Part II — Premium Tax Credit Claim and Reconciliation of APTC** (Lines 9–29)
- **Part III** — historically used for repayment limitation; current revisions fold into Lines 27–29
- **Part IV — Allocation of Policy Amounts** (Lines 30–33, shared policies)
- **Part V — Alternative Calculation for Year of Marriage** (Lines 34–36)

## Header

| Field | What goes here | Source |
|-------|----------------|--------|
| Name(s) shown on return | Filer's legal name as on Form 1040 | Form 1040 header |
| Your social security number | Filer's SSN or ITIN | Form 1040 header |

For MFJ returns, only the *primary* filer's SSN — same as Form 1040 page 1.

---

## Part I — Annual and Monthly Contribution Amount

### Line 1 — Tax family size

| Detail | Value |
|--------|-------|
| Definition | Filer + spouse (if MFJ) + every dependent claimed on the return |
| Citation | IRC §36B(d)(1)(B) |
| Pitfall | A child who is on the marketplace policy but is *claimed as a dependent on a different parent's return* is in that other parent's tax family, not the policyholder's |

### Line 2a — Modified AGI of taxpayer (and spouse if MFJ)

| Detail | Value |
|--------|-------|
| Computation | AGI (Form 1040 Line 11) + tax-exempt interest (Form 1040 Line 2a) + non-taxable Social Security benefits (Form 1040 Line 6a − Line 6b) + foreign earned income exclusion (Form 2555 Line 45) |
| Citation | IRC §36B(d)(2)(B) |

### Line 2b — Dependents' modified AGI

| Detail | Value |
|--------|-------|
| Definition | Sum of MAGI of every dependent who is *required to file a return* |
| Citation | IRC §36B(d)(2)(A)(ii) |
| Pitfall | A dependent who *chose* to file but wasn't required to file (e.g., a college student who filed only to claim a small refund of withholding) — their MAGI does NOT count |
| Filing requirement | Per Pub 501, depends on filing status, age, blindness, and gross income; for 2025 single dependents under 65 with only earned income, threshold is ~$15,000 (verify current year) |

### Line 3 — Household income

| Detail | Value |
|--------|-------|
| Computation | Line 2a + Line 2b |
| Citation | IRC §36B(d)(2)(A) |

### Line 4 — Federal poverty line for tax family size

| Detail | Value |
|--------|-------|
| Source | HHS Poverty Guidelines, **prior-year** value for state group (48+DC, AK, or HI) |
| Citation | IRC §36B(d)(3); Pub 974 Table 1 |
| Year rule | 2025 returns use 2024 FPL; 2026 returns use 2025 FPL — see [`fpl-tables.md`](./fpl-tables.md) |
| State groups | (a) 48 contiguous + DC; (b) Alaska; (c) Hawaii |

### Line 5 — Household income as percentage of FPL

| Detail | Value |
|--------|-------|
| Computation | (Line 3 / Line 4) × 100, rounded *down* to nearest whole percent |
| Cap | If household income > 400% FPL: enter 401% (or current-year cap) |
| Pitfall | "Rounded down" — 199.9% becomes 199%, not 200% |

### Line 6 — Reserved (or per current-year form)

Some revisions used Line 6 for a Yes/No on whether the filer is eligible for PTC. Current revisions may have absorbed this into the workflow. Check the current-year form revision.

### Line 7 — Applicable figure

| Detail | Value |
|--------|-------|
| Source | IRS Form 8962 Instructions, Table 2 (year-specific applicable figure table) |
| Citation | IRC §36B(b)(3)(A) |
| Year-aware | ARPA modified table for 2021–2022; IRA extended modification through 2025; for 2026, verify whether IRA further extended |
| See also | [`applicable-figure.md`](./applicable-figure.md) |

### Line 8a — Annual contribution amount

| Detail | Value |
|--------|-------|
| Computation | Line 3 × Line 7 |

### Line 8b — Monthly contribution amount

| Detail | Value |
|--------|-------|
| Computation | Line 8a / 12 |

---

## Part II — Premium Tax Credit Claim and Reconciliation

### Line 9 — Did you allocate policy amounts?

| Detail | Value |
|--------|-------|
| Yes / No | Yes if a marketplace policy was shared between two tax families during any month; No otherwise |
| If Yes | Complete Part IV before completing Lines 11–25 |

### Line 10 — Annual or monthly calculation?

| Detail | Value |
|--------|-------|
| Yes (Annual) | All 12 months had the same family size, the same applicable SLCSP, and no other Part I changes |
| No (Monthly) | Any month differed (family change, coverage change, allocation change, SLCSP change) |
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

12 rows for January through December. Each row has the same six columns as Line 11, sourced from the corresponding month of Form 1095-A. Months with no coverage have all zeros.

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
| Trigger | Line 24 ≥ Line 25 |
| Computation | Line 24 − Line 25 |
| Routes to | **Schedule 3 Line 9** (refundable credit) |

If Line 26 > 0, skip Lines 27–29.

### Line 27 — Excess advance payment of PTC

| Detail | Value |
|--------|-------|
| Trigger | Line 25 > Line 24 |
| Computation | Line 25 − Line 24 |

### Line 28 — Repayment limitation

| Detail | Value |
|--------|-------|
| Source | Pub 974 Table 5, year-specific; based on Line 5 (% FPL) and filing status |
| Citation | IRC §36B(f)(2)(B) |
| Year rule | Repayment cap differs from year to year as inflation-adjusted; see [`repayment-limitation.md`](./repayment-limitation.md) |
| Cliff rule | Above 400% FPL: pre-IRA → no cap (full excess owed); under IRA modification (through 2025) → cap with no cliff but verify current-year rules |

### Line 29 — Excess advance Premium Tax Credit repayment

| Detail | Value |
|--------|-------|
| Computation | Lesser of Line 27 or Line 28 |
| Routes to | **Schedule 2 Line 2** (additional tax) |

---

## Part IV — Allocation of Policy Amounts (Lines 30–33)

Used when a single marketplace policy covered two tax families during any month. Common cases:

- Divorced parents sharing a policy for joint children
- Adult child on parents' marketplace policy who files independently
- Married couple filing separately (rare; usually MFS = no PTC except in domestic abuse / spousal abandonment scenarios)

Lines 30–33 each represent one shared policy. For each, enter:

| Field | Detail |
|-------|--------|
| (a) Policy number | From Form 1095-A Box 2 |
| (b) SSN of other taxpayer | The other tax family's primary filer SSN |
| (c) Allocation start month | First month the allocation applies |
| (d) Allocation stop month | Last month the allocation applies |
| (e) Premium % | This filer's share (0%-100%) |
| (f) SLCSP % | This filer's share |
| (g) APTC % | This filer's share |

The percentages must total 100% across all tax families on the policy. Filers can negotiate the split or use a default rule; see [`allocation.md`](./allocation.md).

---

## Part V — Alternative Calculation for Year of Marriage (Lines 34–36)

If the filer married during the year and one or both spouses had marketplace coverage *before* marriage, Part V allows a more favorable computation that treats pre-marriage and post-marriage months differently.

| Line | Detail |
|------|--------|
| 34 | Alternative family size, alternative monthly contribution |
| 35 | Pre-marriage months for taxpayer |
| 36 | Pre-marriage months for spouse |

The alternative calculation prevents the marriage from inflating household income and reducing PTC retroactively for pre-marriage months. See [`year-of-marriage.md`](./year-of-marriage.md) for the worked computation.

---

## Routing summary

| Form 8962 Line | Destination |
|----------------|-------------|
| Line 26 (Net PTC) | Schedule 3 Line 9 (refundable credit) |
| Line 29 (Excess APTC repayment) | Schedule 2 Line 2 (additional tax) |

Lines 26 and 29 are mutually exclusive — exactly one is nonzero per Form 8962 (or both are zero, e.g., PTC and APTC both zero).
