# Example — PCORI Fee for a Self-Insured Health Plan

A small business with a self-insured group health plan computes and reports the PCORI fee on Q2 Form 720.

---

## Taxpayer facts

- **Entity**: Lakeshore Manufacturing, Inc. (S-corp, EIN 47-1234567)
- **Plan**: Self-insured medical plan covering W-2 employees and dependents
- **Plan year**: January 1, 2025 – December 31, 2025 (calendar plan year)
- **Plan administrator**: the entity itself (no third-party administrator pass-through of PCORI liability)
- **Counting method**: snapshot method, snapshot count variant (one date per quarter, each the last day of the quarter's final month; dates in quarters 2–4 correspond to the first-quarter date as Treas. Reg. §46.4376-1(c)(2)(iv)(A) requires)
- **Snapshot counts**:
  - March 31, 2025: 42 covered lives (employees + dependents on plan)
  - June 30, 2025: 44
  - September 30, 2025: 45
  - December 31, 2025: 43

The CFO needs to file the PCORI fee for the plan year ending December 31, 2025.

---

## Determining the filing

### Quarter and due date

The fee is due July 31 of the calendar year immediately following the last day of the plan year (i720 "Reporting and paying the fee"). A plan year ending December 31, 2025 is reported on the **Q2 2026 Form 720**, due **July 31, 2026** (a Friday).

| Plan year ends | Form 720 quarter | Due date |
|----------------|------------------|----------|
| Dec 31, 2025 | Q2 2026 | July 31, 2026 |

### Applicable rate

The rate is set by IRS notice based on the **plan-year-ending date**. For plan years ending October 1, 2024 – September 30, 2025, the rate is $3.47 per covered life (Notice 2024-83). Lakeshore's plan year ends December 31, 2025, which falls in the **October 1, 2025 – September 30, 2026** band: **$3.84 per covered life** (Notice 2025-61, I.R.B. 2025-45). On Form 720 (Rev. June 2026) this is row **133(d)**, "applicable self-insured health plans ... plan year ending on or after October 1, 2025, and before October 1, 2026".

The agent must look up the actual notice for the plan year end before filing; never default a forward-looking rate.

---

## Computation

### Step 1 — Average covered lives (snapshot method)

```
Sum of snapshot counts: 42 + 44 + 45 + 43 = 174
Number of snapshots:    4
Average covered lives:  174 / 4 = 43.5
```

### Step 2 — Fee owed

```
Fee = 43.5 × $3.84 = $167.04
```

Enter **$167.04** (the instructions don't call for rounding this line).

---

## Form 720 — Part II, IRS No. 133

| Line | Field | Value |
|------|-------|-------|
| Quarter | 2 | Q2 2026 |
| Filer name | | Lakeshore Manufacturing, Inc. |
| EIN | | 47-1234567 |
| Address | | (entity address) |
| IRS No. 133(d) — (a) Avg. number of lives covered | | 43.5 |
| IRS No. 133(d) — (b) Rate | | $3.84 |
| IRS No. 133(d) — (c) Fee | | $167.04 |
| IRS No. 133 — Tax column | | $167.04 |
| Part II line 2 | | $167.04 |
| Schedule A | | N/A (Part II taxes are not reported on Schedule A) |
| Schedule C | | N/A (no claims) |

### Part III — totals

| Line | Field | Value |
|------|-------|-------|
| Line 3 — Total tax (line 1 + line 2) | | $167.04 |
| Line 4 — Claims | | $0 |
| Line 5 — Deposits made for the quarter | | $0 (no deposits are required for the PCOR fee) |
| Line 6 — Overpayment from previous quarters | | $0 |
| Line 7 — Form 720-X amount included on line 6 | | $0 |
| Line 8 — Line 5 + line 6 | | $0 |
| Line 9 — Line 4 + line 8 | | $0 |
| Line 10 — Balance due | | $167.04 |

---

## Filing channel

Lakeshore has only the PCORI fee — no fuel taxes, no manufacturer's tax, no other Form 720 line items. This is a "PCORI-only" filing, the simplest Form 720 scenario.

Options:
1. **Paper filing**: complete Form 720, mail it with Form 720-V and a check to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0009 (i720 "Where To File").
2. **E-filing** through a provider on the IRS 720 MeF list (https://www.irs.gov/e-file-providers/720-mef-providers). E-filing is optional and the provider charges a fee. The agent checks that the provider puts the fee on row 133(d) at $3.84.

Both channels work for Lakeshore; let the user choose. Because Lakeshore files Form 720 only for the PCOR fee, it doesn't file Q1, Q3, or Q4 returns (i720 "How To File").

---

## Payment

No deposits are required for the PCOR fee (i720 "Payment of Taxes"). Pay the line 10 balance by the due date with:
- **EFTPS** or **IRS Direct Pay**; if paid through EFTPS, apply the payment to the second quarter (i720 "Reporting and paying the fee")
- **Electronic funds withdrawal** when e-filing
- **Check or money order with Form 720-V** when paper filing: payable to "United States Treasury", with the EIN, "Form 720", and the tax period (2nd quarter 2026) written on it

Don't file Form 720-V if paying electronically.

---

## Documentation to retain

The CFO retains for at least 4 years past the filing:
- Snapshot dates and per-day covered-life counts (HRIS/payroll export)
- The IRS notice citation (Notice 2025-61) showing the rate used
- Calculation worksheet (sum, average, multiplication)
- Copy of filed Form 720 with confirmation number (e-file) or certified mail receipt (paper)
- Check stub or EFTPS confirmation for payment

---

## Common errors avoided

1. **Wrong rate**: Lakeshore's plan year ends December 31, 2025, so it uses $3.84 on row 133(d), not $3.47 on row 133(c) (plan years ending before October 1, 2025).
2. **Wrong quarter**: PCORI is filed on the Q2 form following the end of the plan year. Filing on Q4 of the same calendar year as the plan-year end is incorrect.
3. **Counting method inconsistency**: each snapshot date in quarters 2–4 must be within three days of the date corresponding to the first-quarter date, and the same method must be used all plan year (Treas. Reg. §46.4376-1(c)(2)(ii), (iv)(A)).
4. **Forgetting an HRA**: if Lakeshore also sponsored an HRA with the same plan year, it may treat the HRA and the medical plan as one plan, so a person in both counts once; HRA-only participants are added as one life each (Treas. Reg. §46.4376-1(b)(1)(iii), (c)(2)(vi)).
5. **Missing the July 31 deadline**: failure to file on time triggers the §6651(a)(1) penalty (5% of the unpaid tax per month or part of a month, up to 25%) plus interest. Form 7004 doesn't list Form 720, so there is no automatic extension.

---

## Output for the user

The agent delivers to the CFO:

1. **Filing summary**: Q2 2026 Form 720, IRS No. 133 (row d), $167.04 PCORI fee, due July 31, 2026
2. **Computation worksheet**: snapshot counts, average lives, rate citation, total
3. **Filing checklist**: provider choice, payment method, signature/PIN requirements
4. **Reminder**: set a calendar reminder for the 2026 plan year: Q2 2027 Form 720 due July 31, 2027, at the rate in the notice for plan years ending Oct 1, 2026 – Sep 30, 2027 (not yet published on 2026-10-06)
