# Example — PCORI Fee for a Self-Insured Health Plan

A small business with a self-insured group health plan computes and reports the PCORI fee on Q2 Form 720.

---

## Taxpayer facts

- **Entity**: Lakeshore Manufacturing, Inc. (S-corp, EIN 47-1234567)
- **Plan**: Self-insured medical plan covering W-2 employees and dependents
- **Plan year**: January 1, 2025 – December 31, 2025 (calendar plan year)
- **Plan administrator**: the entity itself (no third-party administrator pass-through of PCORI liability)
- **Counting method**: snapshot method (4 quarterly snapshot dates)
- **Snapshot counts**:
  - March 31, 2025: 42 covered lives (employees + dependents on plan)
  - June 30, 2025: 44
  - September 30, 2025: 45
  - December 31, 2025: 43

The CFO needs to file the PCORI fee for the plan year ending December 31, 2025.

---

## Determining the filing

### Quarter and due date

PCORI for a plan year ending January 1 – December 31, 2025 is reported on the **Q2 2026 Form 720** with a due date of **July 31, 2026**.

| Plan year ends | Form 720 quarter | Due date |
|----------------|------------------|----------|
| Dec 31, 2025 | Q2 2026 | July 31, 2026 |

### Applicable rate

The rate is set by IRS notice based on the **plan-year-ending date**. For plan years ending October 1, 2024 – September 30, 2025, the rate is **$3.22 per covered life** (IRS Notice 2024-83). Lakeshore's plan year ends December 31, 2025, which falls in the **October 1, 2025 – September 30, 2026** band — verify against the IRS notice issued in late 2025 (typically Notice 2025-XX). For this example, assume the rate is **$3.47** (estimate; verify before filing).

The agent must look up the actual notice before filing — never default a forward-looking rate.

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
Fee = 43.5 × $3.47 = $150.95
```

Round to whole dollars per Form 720 instructions: **$151**.

---

## Form 720 — Part II, IRS No. 133

| Line | Field | Value |
|------|-------|-------|
| Quarter | 2 | Q2 2026 |
| Filer name | | Lakeshore Manufacturing, Inc. |
| EIN | | 47-1234567 |
| Address | | (entity address) |
| IRS No. 133 — Avg covered lives | | 43.5 |
| IRS No. 133 — Rate | | $3.47 |
| IRS No. 133 — Tax | | $151 |
| Schedule A | | N/A (PCORI is annual; Schedule A is for semi-monthly liability filers) |
| Schedule C | | N/A (no claims) |

### Part III — totals

| Line | Field | Value |
|------|-------|-------|
| Total tax (Part I + Part II) | | $151 |
| Less Schedule C credits | | $0 |
| Balance due | | $151 |

---

## Filing channel

Lakeshore has only the PCORI fee — no fuel taxes, no manufacturer's tax, no other Form 720 line items. This is a "PCORI-only" filing, the simplest Form 720 scenario.

Options:
1. **Paper filing**: complete Form 720, mail to IRS with check. Address per Form 720 instructions (varies by state).
2. **E-filing via PCORI-focused provider**: providers like Tax720.com, Simple720, ExpressTaxFilings support PCORI-only filings for ~$10-30. The agent enters plan-year end, average covered lives, counting method; the provider auto-applies the rate.

For Lakeshore (small entity, single fee), e-filing via a low-cost provider is recommended for simplicity and electronic confirmation.

---

## Payment

PCORI fee is paid via:
- **EFTPS** (Electronic Federal Tax Payment System) — required for entities with prior-year aggregate excise tax liability ≥ $2,500 (rare for PCORI-only filers)
- **Check with paper Form 720** — acceptable for most PCORI-only filers; make payable to "United States Treasury" with EIN, "Form 720", and "Q2 2026 PCORI" on the memo line
- **Direct Pay through IRS.gov** — available for some excise tax payments; verify availability

For Lakeshore, a check accompanying paper Form 720 is the simplest path.

---

## Documentation to retain

The CFO retains for at least 4 years past the filing:
- Snapshot dates and per-day covered-life counts (HRIS/payroll export)
- The IRS notice citation (Notice 2025-XX) showing the rate used
- Calculation worksheet (sum, average, multiplication)
- Copy of filed Form 720 with confirmation number (e-file) or certified mail receipt (paper)
- Check stub or EFTPS confirmation for payment

---

## Common errors avoided

1. **Wrong rate**: Lakeshore's plan year ends in 2025 but the rate is set by the band the plan-year-end falls in. Don't use the prior year's $3.22 rate without verifying the current notice.
2. **Wrong quarter**: PCORI is filed on the Q2 form following the end of the plan year. Filing on Q4 of the same calendar year as the plan-year end is incorrect.
3. **Counting method inconsistency**: snapshot dates must be in approximately the same position within each quarter (e.g., last day of quarter). Mixing arbitrary dates across quarters invalidates the count.
4. **Forgetting HRA**: if Lakeshore also sponsored a separate HRA on top of the medical plan, the HRA counts as its own separate self-insured plan and may require a separate PCORI line — but if the HRA is integrated with the medical plan and only covers actual medical-plan participants, the lives are typically counted once. Check IRS Reg. §46.4376-1(c)(2)(iv).
5. **Missing the July 31 deadline**: the deadline is hard. Failure to file on time triggers §6651 late-filing penalty (5% per month, up to 25%) plus interest. There is no extension for Form 720 PCORI filings.

---

## Output for the user

The agent delivers to the CFO:

1. **Filing summary**: Q2 2026 Form 720, IRS No. 133, $151 PCORI fee, due July 31, 2026
2. **Computation worksheet**: snapshot counts, average lives, rate citation, total
3. **Filing checklist**: provider choice, payment method, signature/PIN requirements
4. **Reminder**: set calendar reminder for July 2026 (rate verification + filing)
