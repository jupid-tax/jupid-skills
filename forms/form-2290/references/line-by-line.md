# Form 2290 — Line-by-Line Reference

Full reference for every field on Form 2290 and Schedule 1. Loaded by `SKILL.md` Step 4 onward when classifying vehicles and computing tax.

**Verified against:** Form 2290 (Rev. July 2026, created 4/8/26) and Instructions for Form 2290 (Rev. July 2026, dated April 15, 2026), tax period July 1, 2026, through June 30, 2027. The IRS issues a new revision each July. Before using this map for the period starting July 1, 2027, compare it with the current [Form 2290](https://www.irs.gov/pub/irs-pdf/f2290.pdf) and [Instructions](https://www.irs.gov/pub/irs-pdf/i2290.pdf) ([About Form 2290](https://www.irs.gov/forms-pubs/about-form-2290)).

---

## Header

| Element | What goes here | Notes |
|---------|---------------|-------|
| Tax period | Nothing to enter | Printed on the revision ("For the period July 1, 2026, through June 30, 2027"). Use the revision for the period you are filing. |
| Name | Legal business name as registered with IRS | Must match the EIN's name control (e-file rejects on mismatch) |
| Address | Street, room or suite, city, state, country, ZIP | P.O. box only if the post office doesn't deliver to the street address |
| EIN | 9-digit Employer ID Number | **Required.** SSN not accepted. |
| Address Change box | Check if the address changed | |
| Amended Return box | Check **only** to report (a) additional tax from an increase in taxable gross weight or (b) suspended vehicles that exceeded the mileage use limit. Write the month of the increase or of the mileage overage to the right of the box. | "Don't check this box for any other reason." |
| VIN Correction box | Check if correcting a VIN listed on a previously filed Schedule 1 | Use the Form 2290 revision for the period being corrected; list the corrected VIN(s) on Schedule 1; attach an explanation. "Don't check this box for any other reason." |
| Final Return box | Check if you no longer have taxable vehicles to report | Sign and file |

The form labels these four boxes "Check if applicable"; they have no letters.

---

## Part I — Figuring the Tax

### Line 1 — Month of First Use

Enter the month of first use during the tax period as **YYYYMM**. July first use for the 2026-27 period = **202607**; August = 202608; ... June 2027 = 202706 (chart under "When To File" in the instructions).

One return covers one first-use month. Vehicles first used in different months go on separate returns (instructions "When To File", Example 3).

Exception: a used vehicle bought from a private seller who already paid this period's tax, first used by the buyer in the month of sale: enter the month **after** the sale (e.g., November 2026 = 202611). The due date doesn't change.

### Line 2 — Tax

Enter the total of column (4) of the Tax Computation table on page 2 of the form (categories A–V).

For each category:
- Column (1)(a): annual tax, vehicles used in July (non-logging); column (1)(b): logging
- Column (2)(a)/(2)(b): partial-period tax for vehicles first used after July, from Table I (non-logging) or Table II (logging) at the end of the instructions
- Column (3)(a)/(3)(b): number of vehicles
- Column (4): tax amount × number of vehicles

Total of column (3) for A–V must equal Schedule 1, Part I, line c. Category W vehicles are counted in column (3) on the W line but contribute $0.

Don't report additional tax from a weight increase on line 2; that goes on line 3. Tax for a previously suspended vehicle that exceeded the mileage limit **does** go on line 2 (with the Amended Return box checked).

### Line 3 — Additional Tax From Increase in Taxable Gross Weight

Only when a vehicle's taxable gross weight increased during the period and it moved into a new category. Line 3 worksheet (instructions p. 6), one per vehicle, attached:

1. Month the taxable gross weight increased (also written next to the Amended Return box)
2. Partial-Period Tax Table amount for the **new** category, in that month's column
3. Partial-Period Tax Table amount for the **previous** category, in the same column
4. Additional tax = line 2 − line 3 → Form 2290 line 3

If the increase happens in July after the return was filed, use the page 2 annual amounts instead of the partial-period tables. Due date: last day of the month following the month of the increase. Don't report tax on line 2 unless other taxable vehicles are on the same return.

Most filings have $0 here.

### Line 4 — Total Tax

Line 2 + Line 3.

### Line 5 — Credits

Credit for tax already paid on a vehicle that was:

- **Sold** before June 1 and not used during the rest of the period
- **Destroyed** (not economical to rebuild) or **stolen** before June 1 and not used during the rest of the period
- **Used 5,000 miles or less** (7,500 agricultural) during the **prior** period

Credit worksheet for destroyed, stolen, or sold vehicles (one per vehicle):

1. Tax previously reported on Form 2290 line 4 for the vehicle
2. Partial-period tax for the months of use (first day of the first-use month through the last day of the month of sale, theft, or destruction), found in the Partial-Period Tax Tables using the number of months shown in parentheses at the top of each column
3. Credit = line 1 − line 2 → Form 2290 line 5

Low-mileage vehicle: credit = tax paid; claimable only after the period ends, on the first Form 2290 filed for the next period (or a refund on Form 8849).

Rules:
- Line 5 can't exceed line 4. Claim the excess as a refund on Form 8849 with Schedule 6. Use Schedule 6 also for overpayments from a mistake on a previously filed Form 2290.
- Attach an explanation per credit: VIN, category, date of destruction/theft/sale, the worksheet, and for a vehicle sold on or after July 1, 2015, the purchaser's name and address. The claim may be disallowed without it.
- No credit for an occasional light load or a discontinued or changed use.

### Line 6 — Balance Due

Line 4 − Line 5. Check the **EFTPS** or **Credit or debit card** box when paying that way.

---

## Part II — Statement in Support of Suspension

Complete the lines that apply. Attach sheets if needed.

### Line 7 — Vehicles Suspended This Period

Declare that the category W vehicles on Schedule 1 are expected to be used on public highways **5,000 miles or less** and/or **7,500 miles or less for agricultural vehicles** during the period (check the box or boxes that apply). The VINs themselves go on Schedule 1, Part II, as category W; their count goes on Schedule 1, Part I, line b.

### Line 8a / 8b — Prior-Period Suspended Vehicles

- **8a:** check to declare that vehicles listed as suspended on the Form 2290 for the prior period (July 1, 2025, through June 30, 2026, on the July 2026 revision) were not subject to the tax for that period, except vehicles listed on 8b.
- **8b:** VINs of prior-period suspended vehicles that exceeded the mileage limit. Their tax must be reported and paid on a separate Form 2290 for the prior period.

### Line 9 — Prior-Period Suspended Vehicles Sold or Transferred

VINs of vehicles listed as suspended for the prior period that were sold or transferred, with the buyer's name and the date. At the time of transfer they must still have been eligible for suspension. The seller gives the buyer a statement (seller name, address, EIN; VIN; date of sale; odometer at start of period and at sale; buyer name, address, EIN), and the buyer attaches it to the buyer's Form 2290.

---

## Schedule 1 — Schedule of Heavy Highway Vehicles

The most operationally important part of the filing — this is what the state DMV requires. File both copies on paper; one is stamped and returned.

### Header

Name, EIN and address exactly as on Form 2290. **Month of first use** box: same YYYYMM as Form 2290 line 1.

### Part I — Summary of Reported Vehicles

| Line | What it captures |
|------|------------------|
| a | Total number of reported vehicles (all vehicles on page 2, A–W) |
| b | Number of suspended vehicles (category W) |
| c | Total taxable vehicles = line a − line b (must match the column (3) total on page 2) |

### Part II — Vehicles You Are Reporting

For each vehicle: the full 17-character VIN (from the registration, title, or vehicle; the truck's VIN, not the trailer's) and its category, A through V, or W for suspended. A missing or partial VIN may prevent state registration.

### Consent to Disclosure of Tax Information (Schedule 1, page 2)

Optional. Signing, dating, and entering the EIN lets the IRS share the VINs and payment verification with the Department of Transportation, U.S. Customs and Border Protection, and state DMVs (via AAMVA). Must reach the IRS within 120 days of the date signed.

### How Schedule 1 Becomes the DMV Document

- **Paper file:** the IRS stamps the second copy and mails it back.
- **E-file:** a Schedule 1 with an IRS watermark is sent to the e-file provider, usually within minutes of acceptance.
- No stamped copy? A photocopy of the filed Form 2290 with Schedule 1 plus both sides of the canceled check is accepted as proof of payment (instructions "Proof of payment").
- July, August, September registrations: the state may accept the prior period's stamped Schedule 1 (Reg. §41.6001-2(b)(4)); the current return is still due on time.
- A vehicle bought within the last 60 days: the bill of sale can stand in for proof of payment; the return is still due.

---

## Tax Computation Table (Page 2 of Form 2290)

| Column | Content |
|--------|---------|
| (1)(a) | Annual tax, vehicles used during July, non-logging ($100.00 for A ... $550.00 for V) |
| (1)(b) | Annual tax, logging vehicles ($75.00 ... $412.50) |
| (2)(a) | Partial-period tax, non-logging, from Table I of the instructions |
| (2)(b) | Partial-period tax, logging, from Table II of the instructions |
| (3)(a) / (3)(b) | Number of vehicles, non-logging / logging |
| (4) | Amount of tax = column (1) or (2) × column (3) |

Categories A–V carry tax; W (tax-suspended) carries a vehicle count only. The partial-period amounts are not printed on page 2; copy them from Table I or Table II in the instructions (Table II amounts can be $0.01 lower than annual × 0.75 × months ÷ 12, so do not recompute them for filing).

For worked lookups, see [`tax-table.md`](./tax-table.md).

---

## Form 2290-V — Payment Voucher

Only for payment by check or money order (payable to "United States Treasury"; write EIN, "Form 2290," and the line 1 YYYYMM on it).

| Box | Content |
|-----|---------|
| 1 | EIN |
| 2 | Amount paid (Form 2290 line 6) |
| 3 | Date as shown on Form 2290 line 1 (YYYYMM) |
| 4 | Name and address as shown on Form 2290 |

Mail with the paper return to: Internal Revenue Service, P.O. Box 932500, Louisville, KY 40293-2500. If the return was e-filed, send only the voucher and payment. Don't staple. Checks drawn on an international financial institution go to the International Accounts address in the instructions' "Where To File" table. Don't file the voucher when paying by EFW, EFTPS, or card.

---

## Common Field Errors

| Error | Symptom | Fix |
|-------|---------|-----|
| EIN typo (one digit off) | E-file rejection (name control mismatch) | Verify against IRS EIN confirmation letter |
| VIN typo | Stamped Schedule 1 doesn't match the registration; DMV rejects it | File Form 2290 for that period with the **VIN Correction** box checked, corrected VIN on Schedule 1, explanation attached (can be e-filed) |
| Weight category too high, or logging vehicle reported at the standard rate | Overpaid | Refund claim for a mistake on Form 8849, Schedule 6 |
| Weight category too low | Tax underpaid | The Amended Return box covers only a weight **increase** during the period; for a reporting error, ask the e-file provider or call the Form 2290 call site (866-699-4096) before filing a correction |
| Vehicles with different first-use months on one return | Wrong tax for the later vehicles | One return per first-use month |
| Suspension without line 7 completed | Suspension claim incomplete | Complete Part II line 7 |
| Credit on Line 5 without supporting explanation | IRS may disallow the credit | Attach the explanation and worksheet |
| Filing under SSN | E-file rejects | Apply for an EIN; wait four weeks; file |
| Duplicate e-file (same EIN, period, VIN) | "Duplicate filing" rejection | List only new vehicles on the new return (FAQs for truckers who e-file) |
