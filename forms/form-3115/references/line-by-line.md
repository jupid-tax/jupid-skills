# Form 3115 Line-by-Line Reference

Complete lookup for Form 3115 fields. The form is structured in four parts plus several schedules; this file covers the general parts and points to schedule-specific guidance.

---

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name of filer | Filer's legal name | Match income tax return |
| Identifying number | SSN (sole prop) or EIN | Entity returns use EIN |
| Principal business activity code | NAICS code | Match Schedule C / Schedule E / entity return |
| Tax year of change begins / ends | First day and last day of year of change | Year of change = first year using the new method |
| Type of accounting method change | Check the appropriate box | Cash↔accrual, depreciation, inventory, etc. |
| Name of person to contact | Filer or representative | Required |
| Telephone | Contact phone | Required |

---

## Part I — Information

### Line 1 — Type of change request

- **Line 1(a)** — Automatic consent. **DCN required**: enter the Designated Change Number from the current Rev. Proc. (Rev. Proc. 2024-23 or successor lists DCNs).
- **Line 1(b)** — Advance consent (non-automatic). User fee required; Part III applies.

If the taxpayer claims automatic consent but the DCN doesn't actually cover the change, the IRS treats the filing as defective — could be deemed non-filed, or treated as a request for advance consent without the user fee (and rejected).

### Line 2 — Year of change

Date the year of change begins and ends. For calendar-year filers, this is the calendar year (Jan 1 – Dec 31). For fiscal-year filers, the fiscal year.

### Line 3 — Type of return

Check the applicable box:
- 1040 (individual, including Schedule C)
- 1041 (estate or trust)
- 1065 (partnership)
- 1120 (C-corp)
- 1120-S (S-corp)
- 1120-F (foreign corporation)
- Other (specify)

### Line 4 — Description of present method

Plain-English description of the method currently used. Be specific:

- "Cash method overall, with COGS reported on cash basis"
- "Modified accelerated cost recovery system, 39-year SL nonresidential method, applied to a residential rental property placed in service 04/15/2022"
- "FIFO inventory cost method"
- "Cash method for a service business with no inventory"

Vague descriptions ("we depreciate things") are insufficient. The IRS uses Line 4 to validate that the present method is actually a method (used for ≥2 years) and that the change is what's claimed.

### Line 5 — Description of proposed method

Plain-English description of the method being adopted. Same specificity:

- "Accrual method overall"
- "MACRS 27.5-year SL residential rental method, mid-month convention"
- "LIFO inventory cost method, dollar-value LIFO with double-extension"

### Line 6 — Business activity description

Brief description of the trade or business plus NAICS code. Used by the IRS to identify the activity for examination purposes.

---

## Part II — Information for all requests

### Lines 7–9 — Status questions

- **Line 7**: Has the applicant filed a federal income tax return for the immediately preceding year?
- **Line 8**: Has the applicant requested a similar change in any prior year?
- **Line 9**: Is the applicant's return currently under IRS examination, or before Appeals or a federal court?

**Yes on Line 9 has consequences**: if the issue is part of an exam, the change generally requires IRS area office consent (not automatic). If exam is for unrelated issues, some changes still permitted. Verify per Rev. Proc. 2015-13 Section 8.

### Lines 10–13 — Group / consolidated questions

- **Line 10**: Is the applicant a member of an affiliated group filing a consolidated return?
- **Line 11**: List any item that is similar to the change requested but is not being changed.
- **Line 12**: Has the applicant made a federal income tax method-of-accounting change in any of the 5 prior tax years for the same item?
- **Line 13**: Various tax-shelter, partnership-level, allocation questions.

**Yes on Line 12 has consequences**: under Rev. Proc. 2015-13 Section 5, automatic consent generally not available within 5 years of a prior change for the same item. Must file non-automatic.

### Line 14 — Detailed description

Free-form section where the taxpayer attaches a detailed statement covering:
- Description of present method (expanding Line 4)
- Description of proposed method (expanding Line 5)
- Business reasons for the change
- Statement that the taxpayer agrees to terms of Rev. Proc. 2024-23 (if automatic) or the audit-protection conditions

This statement is the "meat" of the filing. The IRS uses it to evaluate compliance with the procedure.

---

## Part III — Information for advance consent only

Skipped entirely for automatic-consent filings.

For advance consent:

### Line 15 — Reason for change

Why the taxpayer wants the change beyond business reasons. The IRS evaluates whether the change clearly reflects income.

### Line 16 — Material item

If the change is to a "material item" (one that affects timing of income/expense recognition), this is where the analysis goes.

### Lines 17–20 — Conditions

Various conditions the taxpayer agrees to as part of the change (e.g., consistency with method elsewhere, audit protection limits).

---

## Part IV — §481(a) Adjustment

### Line 25 — Net §481(a) adjustment

The cumulative income/expense effect of using the new method since inception, less what was actually reported under the old method.

- Positive = increases income (taxpayer pays more tax over the spread period)
- Negative = decreases income (taxpayer gets a deduction)
- Zero = unusual; verify the change actually affects income/expense timing

### Line 26 — Spread

How the §481(a) adjustment is included in income:

| Spread type | When applied |
|-------------|--------------|
| 1-year (year of change) | Negative §481(a) (default); positive <$50,000 if elected |
| 4-year (year of change + 3 succeeding) | Positive §481(a) ≥$50,000 (default) |
| Other | Specific changes in Rev. Proc. mandate different spreads |

The 4-year spread is *not* present-value-adjusted; the IRS recognizes 1/4 each year nominally.

### Line 27 — Year-by-year

If 4-year spread:
```
Year of change:       Line 25 / 4
Year of change + 1:   Line 25 / 4
Year of change + 2:   Line 25 / 4
Year of change + 3:   Line 25 / 4
```

If 1-year spread:
```
Year of change:       Line 25 (full)
```

### Acceleration rules

If during the spread period:
- Taxpayer ceases to engage in the trade or business: remaining §481(a) accelerated to year of cessation
- Taxpayer dies (sole prop): accelerated to year of death
- Entity is liquidated: accelerated to year of liquidation

---

## Schedules — when to use which

### Schedule A — Change in overall method (cash↔accrual)

For changes to or from the overall cash, accrual, or hybrid method. Common DCNs:
- DCN 32 (cash to accrual, voluntary)
- DCN 233 (cash to accrual, required by §448)

### Schedule B — Deferral method for advance payments

For advance payments under Reg. §1.451-8 (deferral of revenue). Less common for solo filers.

### Schedule C — Long-term contracts

For contractors using percentage-of-completion or completed-contract methods. Form 8697 may also apply.

### Schedule D — Inventory

For inventory method changes:
- LIFO ↔ FIFO ↔ specific identification
- UNICAP §263A adoption
- Lower of cost or market vs. cost
- Retail inventory method

### Schedule E — Depreciation/Amortization

Most common for solo filers. For each affected asset:

| Column | Content |
|--------|---------|
| (a) Description | Asset description |
| (b) Date placed in service | Original placed-in-service date |
| (c) Cost or basis | Original basis |
| (d) Accumulated depreciation under old method | Cumulative depreciation taken |
| (e) Accumulated depreciation under new method | What should have been taken |
| (f) §481(a) per asset | (e) − (d) |

Sum of column (f) = Line 25.

DCN 7 (impermissible to permissible depreciation method) is the most common automatic DCN here.

### Schedule F — Financial institutions

Banks, S&Ls, mutual savings. Rare for solo filers.

---

## Common errors

1. **Line 1(a) DCN not in current Rev. Proc.** — DCN renumbering is common; verify
2. **Line 5 description vague** — "use the right method" is not a description
3. **§481(a) computation missing** — the schedule supporting Line 25 must be attached
4. **Spread on Line 27 doesn't match Line 25** — 4 × Line 27 amounts ≠ Line 25 → math error
5. **Schedule E asset-by-asset detail missing** — for depreciation changes, each asset must be listed
6. **Yes on Line 9 (under exam) without explanation** — automatic consent may not be available
7. **Yes on Line 12 (prior change) without 5-year analysis** — automatic consent may not be available
8. **Signature missing** — both original and duplicate must be signed
