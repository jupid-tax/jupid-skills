# Form 2290 — Line-by-Line Reference

Full reference for every field on Form 2290 and Schedule 1. Loaded by `SKILL.md` Step 4 onward when classifying vehicles and computing tax.

The form revision changes annually. Cross-reference with the [current Instructions for Form 2290](https://www.irs.gov/pub/irs-pdf/i2290.pdf) before relying on any specific line number — the IRS occasionally renumbers.

---

## Header

| Element | What goes here | Notes |
|---------|---------------|-------|
| Tax period | "July 1, YYYY through June 30, YYYY+1" | Federal fiscal year, not calendar year |
| Name | Legal business name as registered with IRS | Must match EIN registration |
| Address | Business street, city, state, ZIP | If changed since last filing, also check Box A |
| EIN | 9-digit Employer ID Number | **Required.** SSN not accepted. |
| Box A — Address Change | Check if address differs from prior IRS records | File Form 8822-B for permanent changes |
| Box B — Amended Return | Check if filing to amend a previously-filed 2290 | Common reasons: mileage exceeded suspension, weight increase |
| Box C — VIN Correction | Check if correcting a VIN typo from a prior 2290 | No additional tax due; just clerical |
| Box D — Final Return | Check if no longer have any qualifying vehicles | Tells IRS to stop expecting future filings |

---

## Part I — Tax Calculation

### Line 1 — Date of First Use

The earliest date during the period that any reported vehicle was first used on public highways. For most full-year filers, this is July of the period start year (e.g., 07/2025 for the 2025-26 period).

For partial-period filers (mid-year first use), this is the actual first-use month for the new vehicle.

**Format:** Two-digit month, four-digit year (MM/YYYY).

### Line 2 — Tax (from Tax Computation table)

The sum of tax across all reported vehicles, computed from the Tax Computation table on page 2 of the form.

For each vehicle:
- Look up the row for the vehicle's weight category (A through V)
- Look up the column for the appropriate filing type (Annual / Partial-period)
- Apply the 25% reduction if logging
- Sum across all vehicles

Suspended (Category W) vehicles contribute $0 to Line 2.

### Line 3 — Additional Tax from Increase in Taxable Gross Weight

Only used when a vehicle's taxable gross weight increased mid-period and the user is filing an Amended Return (Box B).

Calculation:
- Determine the new annual tax for the higher weight category
- Subtract the originally-paid tax for the same vehicle
- Multiply by (months remaining in period ÷ 12)

Most filings have $0 here.

### Line 4 — Total Tax

Line 2 + Line 3. The total tax owed before credits.

### Line 5 — Credits

Credits available for prior-period vehicles where:

- **Sold, destroyed, or stolen** during the prior period — credit = prior-period tax × (months remaining when event occurred ÷ 12)
- **Used 5,000 miles or fewer** (7,500 if agricultural) when full tax was paid in the prior period — credit = full prior-period tax

**Required:** Attach a statement to the return listing each vehicle's VIN, date of event, and credit calculation. Without it, the IRS holds or denies the credit.

### Line 6 — Balance Due

Line 4 − Line 5. The amount the user pays.

---

## Part II — Statement in Support of Suspension

Required only if any vehicle is filed under Category W (suspended).

### Statement (a) — Vehicles Suspended This Period

For each suspended vehicle, certify:

- VIN
- Vehicle will be used **5,000 miles or fewer** (or **7,500 if agricultural**) on public highways during the period

The user signs the statement. This is a sworn certification; mileage records must support it.

### Statement (b) — Sold Prior-Period Suspended Vehicles

If a vehicle was suspended in the **prior** period and was **sold** during that period, list it here. This protects the user from being expected to file 2290 for that vehicle in subsequent periods.

### Statement (c) — Carry-Forward Suspended Vehicles

Vehicles that were suspended in the **prior** period and stayed under the mileage threshold (no tax owed). The user certifies this and lists VINs to support the $0 carry-forward.

---

## Schedule 1 — Vehicles for Which Tax Is Reported

The most operationally important part of the filing — this is what the state DMV requires.

### Part I — Vehicles Reported

For each vehicle reported on this return:

| Field | What to enter |
|-------|---------------|
| (a) VIN | 17-character VIN |
| (b) Weight category | Single letter A through V (active) or W (suspended) |

Order doesn't matter, but consistency with the Tax Computation table makes auditing easier.

### Part II — Summary

| Line | What it captures |
|------|------------------|
| (a) Total taxable vehicles | Count of vehicles reported with active categories (A-V) |
| (b) Suspended vehicles | Count of Category W vehicles |
| (c) Total | Sum of (a) and (b) — all vehicles on the return |

### How Schedule 1 Becomes the DMV Document

- **Paper file:** File Schedule 1 in **duplicate**. The IRS keeps one copy, stamps the other, and mails it back. Takes 4-6 weeks.
- **E-file:** Schedule 1 is automatically generated and stamped electronically by the IRS, returned within minutes as a watermarked PDF.

The stamped Schedule 1 lists every VIN that the IRS has accepted as filed. State DMVs use this to verify HVUT compliance before issuing or renewing plates.

---

## Tax Computation Table (Page 2 of Form 2290)

The table has rows for weight categories A through V, columns for filing type:

| Column | When to use |
|--------|------------|
| (1) Vehicles other than logging — Annual | Full-period (July 1 first use), non-logging |
| (2) Logging vehicles — Annual | Full-period, logging (25% reduced) |
| (3) Vehicles other than logging — Partial period | Mid-year first use, non-logging |
| (4) Logging vehicles — Partial period | Mid-year first use, logging |

The IRS provides the exact dollar amounts in columns (3) and (4) for every combination of weight category and first-use month — do not compute proration manually unless verifying. Use the table.

For a complete worked example of the table lookup, see [`tax-table.md`](./tax-table.md).

---

## Form 2290-V — Payment Voucher

Used only if paying by check or money order. Provides:

- Filer name and EIN
- Tax period
- Amount enclosed
- Mailing address per the instructions

Detach the voucher and mail with payment. The address depends on the filer's state and whether payment is enclosed — see page 12 of the current instructions.

---

## Common Field Errors

| Error | Symptom | Fix |
|-------|---------|-----|
| EIN typo (one digit off) | E-file rejection | Verify against IRS EIN confirmation letter |
| VIN typo | E-file may accept; state DMV will reject | Amended Return with Box C (VIN Correction) |
| Wrong weight category | E-file accepts; tax is wrong | Amended Return with Box B (recompute Line 3) |
| Missing logging flag | Overpaid by 25% | Amended Return for refund, or claim on next period's Line 5 |
| Missing first-use month for partial-period vehicle | E-file rejects or computes wrong tax | Re-enter with correct month |
| Suspension without Part II completed | E-file rejects | Complete Part II Statement |
| Credit on Line 5 without supporting statement | IRS holds or denies credit | Attach statement (PDF for e-file) |
| Filing under SSN | E-file rejects immediately | Apply for EIN; wait 2 weeks; re-file |
