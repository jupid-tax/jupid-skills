# Form 8919 — Line-by-Line Reference

Line-by-line guidance for Form 8919 (Uncollected Social Security and Medicare Tax on Wages), built from the text of the **2025 Form 8919** ("Form 8919 (2025) Created 10/22/25"), which is attached to 2025 returns filed in 2026. The instructions are printed on page 2 of the form; there is no separate instructions PDF. Before using this map for another year, re-check the current revision at https://www.irs.gov/forms-pubs/about-form-8919: the wage base on line 7 changes every year and line numbers can shift.

---

## Header Section

### Name of person who must file this form

Only the worker's name. The form says: "If married, complete a separate Form 8919 for each spouse who must file this form." On a joint return where only one spouse was misclassified, the form carries that spouse's name only. If both spouses were misclassified, each completes a separate Form 8919.

### Social security number

The SSN of the person named in the header (the worker), not the primary taxpayer's SSN if the worker is the other spouse.

---

## Who must file (top of form)

The worker must file Form 8919 if **all** of these apply (2025 Form 8919, "Who must file"):

- You performed services for a firm.
- You believe your pay from the firm wasn't for services as an independent contractor.
- The firm didn't withhold your share of social security and Medicare taxes from your pay.
- One of the reasons listed under Reason codes applies to you.

"Firm" means any individual, business enterprise, company, nonprofit organization, state, or other entity for which you performed services (page 2, "Firm").

Do not use the form for services performed as an independent contractor (use Schedule C and Schedule SE) or for tips not reported to the employer (use Form 4137) (page 2, "Don't use this form").

---

## Lines 1 through 5 — One row per firm

The form has five rows (lines 1–5). Complete a separate line for each firm. If the worker was an employee of more than five firms, attach additional Forms 8919 with lines 1 through 5 completed, and complete lines 6 through 13 on only one Form 8919; its line 6 is the combined total of all rows on all Forms 8919 (page 2, "Lines 1 through 5").

### Column (a) — Name of firm

The name of the firm the worker worked for. If the worker received a Form 1099-MISC and/or 1099-NEC from the firm, enter the name exactly as it appears on that form (page 2, "Column (a)").

### Column (b) — Firm's federal identification number

An EIN (format XX-XXXXXXX) or, if the firm is an individual, an SSN (format XXX-XX-XXXX). If the worker received a 1099-MISC/NEC, use the number shown on it (1099-NEC "PAYER'S TIN"). If the worker doesn't know it, they can request it with Form W-9; if they can't obtain it, enter "unknown" (page 2, "Column (b)").

If two documents show different numbers for the same firm, ask the user which document is correct before filing.

### Column (c) — Reason code

Enter **one** reason code on each line (page 2, "Column (c)"). The 2025 form lists four codes:

| Code | Text on the 2025 form |
|------|-----------------------|
| **A** | I filed Form SS-8 and received a determination letter stating that I am an employee of this firm. |
| **C** | I received other correspondence from the IRS stating that I am an employee. (Also use C if the IRS designated you a "section 530 employee": determined to be an employee, but the employer was granted section 530 relief.) |
| **G** | I filed Form SS-8 with the IRS and haven't received a reply. |
| **H** | I received a Form W-2 and a Form 1099-MISC and/or 1099-NEC from this firm for 2025. The amount on Form 1099-MISC and/or 1099-NEC should have been included as wages on Form W-2. (Don't file Form SS-8 if you select reason code H.) |

If none of the codes apply but the worker believes they should have been treated as an employee, enter **code G** and file Form SS-8 on or before the date the tax return is filed. Do not attach Form SS-8 to the return; it is filed separately.

Earlier revisions had more codes (the 2007 form also listed B, D, E, and F: pre-1997 section 530 designation, prior employee treatment, co-workers treated as employees, co-workers' SS-8 determinations). They are not on the current form; do not enter them.

See `reason-codes.md` for the decision tree.

### Column (d) — Date of IRS determination or correspondence

Complete **only** if reason code A or C is entered in column (c) (page 2, "Column (d)"). Format MM/DD/YYYY. Leave blank for codes G and H.

### Column (e) — Check if Form 1099-MISC and/or 1099-NEC was received

Check the box if the firm issued the worker a Form 1099-MISC and/or 1099-NEC for this pay. This column is **not** an SS-8 checkbox; the form has no place to certify the SS-8 filing other than the reason code itself.

### Column (f) — Total wages received with no social security or Medicare tax withholding and not reported on Form W-2

The gross pay from this firm that had no social security or Medicare withholding and was not reported on a W-2. For a 1099-NEC this is normally Box 1.

**Gross, not net.** The amount is wages. Business expenses are not subtracted, because the income is not being reported as self-employment.

If part of the pay from the same firm was for genuine independent-contractor work, that part goes on Schedule C, not in column (f). Ask the user to split the amount and document the split.

---

## Line 6 — Total wages

Combine lines 1 through 5 in column (f).

Enter the same amount on:
- **Form 1040, 1040-SR, or 1040-NR, line 1g** ("Wages from Form 8919, line 6" on the 2025 Form 1040).
- **Form 8959, line 3**, if the worker must file Form 8959 (page 2, "Line 6").

---

## Line 7 — Maximum amount of wages subject to social security tax

Pre-printed on the form.

| Tax year | Amount | Source |
|----------|--------|--------|
| 2025 | $176,100 | 2025 Form 8919, line 7 and What's New |
| 2026 | $184,500 | SSA, https://www.ssa.gov/oact/cola/cbb.html (re-check against the 2026 Form 8919 when it is released) |

---

## Line 8 — Social security wages already counted

Total of:
- W-2 box 3 (social security wages) and box 7 (social security tips) from all Forms W-2,
- railroad retirement (RRTA) compensation subject to the 6.2% rate (do not include more than the line 7 amount, $176,100 for 2025; page 2, "Line 8"), and
- unreported tips subject to social security tax from Form 4137, line 10.

Do **not** include the Form 8919 wages from line 6. Line 8 holds only the worker's other wages that already used up part of the wage base. Do not use W-2 box 1 (it can differ from box 3, for example because of 401(k) deferrals).

---

## Line 9 — Room left under the wage base

Line 7 minus line 8. If line 8 is more than line 7, enter -0- here and on line 10.

---

## Line 10 — Wages subject to social security tax

The smaller of line 6 or line 9.

This amount also goes to **Schedule SE, line 8c** if the worker files Schedule SE for separate self-employment income (2025 Schedule SE line 8c: "Wages subject to social security tax from Form 8919, line 10").

**Example (2025):** line 6 $72,000, no W-2 → line 8 $0, line 9 $176,100, line 10 $72,000.

**Example (2025):** line 6 $40,000, W-2 box 3 $150,000 → line 8 $150,000, line 9 $26,100, line 10 $26,100. The remaining $13,900 of Form 8919 wages is above the wage base: no social security tax on it, but Medicare tax still applies on line 12.

---

## Line 11 — Social security tax

Line 10 × 0.062 (6.2%, the employee rate under IRC §3101(a)). The employer's matching 6.2% is not charged here.

---

## Line 12 — Medicare tax

**Line 6** × 0.0145 (1.45%, the employee rate under IRC §3101(b)(1)). Medicare has no wage base, so the multiplier is applied to all Form 8919 wages, not to line 10.

The 0.9% Additional Medicare Tax is not on Form 8919; it is figured on Form 8959 (Form 8919 line 6 goes to Form 8959 line 3).

---

## Line 13 — Total

Line 11 + line 12. Enter on **Schedule 2 (Form 1040), line 6** ("Uncollected social security and Medicare tax on wages. Attach Form 8919"), or on Form 1040-SS, Part I, line 6c. Schedule 2 line 21 then flows to Form 1040 line 23.

Schedule 2 **line 5** is a different line (Form 4137, unreported tips). Do not put the Form 8919 amount there.

---

## Cross-Form Mapping Summary (2025 forms)

| From | To | Amount |
|------|-----|--------|
| Form 8919 line 6 | Form 1040 / 1040-SR / 1040-NR line 1g | Wages subject to income tax |
| Form 8919 line 6 | Form 8959 line 3 (if Form 8959 is required) | Medicare wages for the 0.9% test |
| Form 8919 line 10 | Schedule SE line 8c (if Schedule SE is filed) | Wages that used part of the SS wage base |
| Form 8919 line 13 | Schedule 2 line 6 (or Form 1040-SS Part I line 6c) | Employee share of SS + Medicare |
| Schedule 2 line 21 | Form 1040 line 23 | All other taxes |

---

## Verification Math

```
Line 6  = sum of column (f), all rows, all Forms 8919
Line 9  = MAX(0, Line 7 − Line 8)
Line 10 = MIN(Line 6, Line 9)
Line 11 = Line 10 × 0.062
Line 12 = Line 6 × 0.0145
Line 13 = Line 11 + Line 12

When Line 8 = 0 and Line 6 ≤ Line 7: Line 13 = Line 6 × 0.0765
```

Round each line to whole dollars consistently (the 1040 instructions allow rounding to whole dollars).

---

## Edge Cases

### Worker has no W-2 wages

Line 8 = 0; line 9 = line 7; line 10 = smaller of line 6 or line 7. For 2025, a worker with $72,000 on line 6: line 9 = $176,100, line 10 = $72,000, line 11 = $4,464, line 12 = $1,044, line 13 = $5,508.

### Worker has W-2 social security wages at or above the wage base

Line 8 ≥ line 7 → line 9 = 0 → line 10 = 0 → line 11 = 0. Medicare (line 12) still applies to all of line 6.

### Worker has both Form 8919 wages and genuine self-employment

Only the misclassified firms go on lines 1–5. The self-employment income goes on Schedule C and Schedule SE. On Schedule SE, enter Form 8919 line 10 on line 8c so the combined social security wage base is applied once.

### Worker discovers the misclassification after filing

File Form 1040-X with Form 8919 attached for each open year (refund claims: generally 3 years from filing or 2 years from payment, whichever is later, IRC §6511). The amended return replaces the Schedule C / Schedule SE treatment of that income with Form 8919. The net refund is smaller than the SE-tax difference alone, because the amended return also gives up the deduction for half of SE tax and any QBI deduction on that income.

---

## Cross-References

- 2025 Form 8919, https://www.irs.gov/pub/irs-pdf/f8919.pdf (page 2 holds the instructions)
- About Form 8919, https://www.irs.gov/forms-pubs/about-form-8919
- IRC §3101 — Employee FICA rates
- IRC §3121(d) — Definition of "employee"
- IRC §6511 — Statute of limitations on refund claims
- Rev. Rul. 87-41 — Common-law worker classification factors
- IRS Pub 15-A — Employer's Supplemental Tax Guide
- Form 8959 — Additional Medicare Tax
- Form SS-8 (Rev. December 2023) and Instructions (Rev. January 2024) — Determination of Worker Status
- Schedule 2 (Form 1040) — Additional Taxes; Schedule SE (Form 1040) line 8c
