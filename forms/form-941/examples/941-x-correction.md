# Example: Employer Files 941-X to Add Misclassified Wages (Correcting Q2 2025)

A complete walkthrough of Form 941-X (Rev. April 2026) for an employer who discovers in May 2026 that a "1099 contractor" paid $18,000 in Q2 2025 was actually a W-2 employee under common-law factors. The employer must add the wages to Q2 2025 retroactively and pay the tax at the IRC §3509 rates.

## The filer

- **Business name**: Aspen Studio LLC
- **EIN**: 91-XXXXXXX
- **Entity**: Multi-member LLC, taxed as partnership
- **Original Q2 2025 941**: Filed July 28, 2025; reported $42,000 wages, $5,800 FIT, $5,208 Social Security tax, $1,218 Medicare tax
- **Worker reclassified**: Jordan Reyes, paid $18,000 in Q2 2025 (April 15 – June 30) and $18,000 in Q3 2025 (through September 30) as a "1099 contractor"
- **2025 Form 1099-NEC for Jordan**: filed January 26, 2026, box 1 = $36,000
- **Issue discovered**: May 11, 2026
- **Quarter being corrected**: Q2 2025 (a separate 941-X corrects Q3 2025)
- **Filing date for 941-X**: May 22, 2026

## The reclassification analysis

The CFO discovered during an internal review that Jordan worked exclusively for Aspen, used Aspen's equipment, followed Aspen's schedule, was supervised daily, and had no separate business. Under the IRS common-law test (behavioral control + financial control + relationship), Jordan is an employee, not a contractor.

The CFO consulted with a CPA who recommended:

1. File 941-X for Q2 2025 to add Jordan's wages
2. File a separate 941-X for Q3 2025 (same issue)
3. File a 2025 Form W-2 for Jordan (none was issued; the January 31 deadline has passed, so late-filing penalties may apply)
4. File a corrected 1099-NEC so Jordan's income is not reported twice
5. Use the **Section 3509 rates**: they apply whether the IRS or the employer makes the reclassification, as long as the employer did not intentionally disregard the withholding requirements and did not withhold income tax while skipping FICA (Instructions for Form 941-X, lines 19–22)

### Section 3509 rates

The rate depends on whether the employer filed the required information returns (here, Form 1099-NEC) for the worker:

| Tax | Information returns filed | Information returns NOT filed |
|-----|---------------------------|-------------------------------|
| Federal income tax withholding | 1.5% of wages | 3.0% of wages |
| Social Security (6.2% employer + share of 6.2% employee) | 6.2% + 20% × 6.2% = 7.44% | 6.2% + 40% × 6.2% = 8.68% |
| Medicare (1.45% employer + share of 1.45% employee) | 1.45% + 20% × 1.45% = 1.74% | 1.45% + 40% × 1.45% = 2.03% |
| Additional Medicare Tax | 0.18% of wages over $200,000 | 0.36% |

Aspen filed the 1099-NEC for Jordan on January 26, 2026, so the left column applies. §3509 rates are not available at all for intentional disregard; then the full rates apply. Source: Instructions for Form 941-X (Rev. April 2026), lines 19–22.

## The corrections to Q2 2025

### Original Q2 2025 941 (as filed)

```
Line 1: 8 employees
Line 2: $42,000.00
Line 3: $5,800.00
Line 5a col 1: $42,000.00 ; col 2: $5,208.00
Line 5c col 1: $42,000.00 ; col 2: $1,218.00
Line 5d: $0
Line 5e: $6,426.00
Line 6: $12,226.00
Line 7-9: $0
Line 10: $12,226.00
Line 11: $0
Line 12: $12,226.00
Line 13: $12,226.00 (deposits matched)
Line 14: $0
```

### Corrected Q2 2025 amounts (with Jordan added)

Adding Jordan's $18,000 wages with §3509 rates (information returns filed):

| Item | Calculation | Amount |
|------|-------------|--------|
| Line 6 wages (Form 941 line 2) | $42,000 → $60,000 | +$18,000.00 (no tax in column 4) |
| Line 19 special addition to wages for federal income tax | $18,000 × 1.5% | $270.00 |
| Line 20 special addition to wages for Social Security taxes | $18,000 × 7.44% | $1,339.20 |
| Line 21 special addition to wages for Medicare taxes | $18,000 × 1.74% | $313.20 |
| Line 23 subtotal / Line 27 total | $270.00 + $1,339.20 + $313.20 | $1,922.40 |

Interest-free treatment: the 941-X is filed by the due date of the Form 941 for the quarter in which the error was discovered (Q2 2026 return, due July 31, 2026) and the $1,922.40 is paid when filing, so no interest is charged (IRC §6205; Instructions for Form 941-X, "Underreported tax"). Had Aspen missed that window, interest would run from the original due date at the IRS underpayment rate (7% for every quarter of 2025, 7% for Q1 2026, 6% for Q2 2026; https://www.irs.gov/payments/quarterly-interest-rates).

## The completed Form 941-X draft

```markdown
# Form 941-X (Rev. April 2026) — DRAFT correcting Q2 2025 (filed May 22, 2026)

## Header
Employer name (legal):       Aspen Studio LLC
EIN:                         91-XXXXXXX
Address:                     789 Pine St, Denver, CO 80202
Return you're correcting:    [X] 941  [ ] 941-SS
Quarter you're correcting:   [ ] 1  [X] 2  [ ] 3  [ ] 4
Calendar year:               2025
Date you discovered errors:  05/11/2026

## Part 1 — Select ONLY one process
  [X] 1. Adjusted employment tax return (underreported tax; pay with the form)
  [ ] 2. Claim (overreported tax only; refund / abatement)

## Part 2 — Certifications
  [X] 3. I certify that I've filed or will file Forms W-2 or W-2c, as required.
  Lines 4 and 5: skipped (correcting underreported amounts only)

## Part 3 — Corrections for this quarter
Columns: 1 = total corrected amount; 2 = amount originally reported; 3 = difference; 4 = tax correction

| Line | Col 1 | Col 2 | Col 3 | Col 4 |
|------|-------|-------|-------|-------|
| 6 Wages, tips, other compensation (941 line 2) | $60,000.00 | $42,000.00 | $18,000.00 | — (use col 3 for W-2s) |
| 19 Special addition to wages for federal income tax | $18,000.00 | $0.00 | $18,000.00 | × 1.5% = $270.00 |
| 20 Special addition to wages for social security taxes | $18,000.00 | $0.00 | $18,000.00 | × 7.44% = $1,339.20 |
| 21 Special addition to wages for Medicare taxes | $18,000.00 | $0.00 | $18,000.00 | × 1.74% = $313.20 |
| 23 Subtotal (column 4, lines 7–22) | | | | $1,922.40 |
| 27 Total (lines 23 through 26c) | | | | $1,922.40 |

Lines 7, 8, and 12 are left blank: the reclassified worker's wages go on lines 19–21 when §3509 rates are used.

Line 27 is more than zero: pay $1,922.40 by the time the form is filed.

## Part 4 — Explain your corrections
  [ ] 41. Corrections include both underreported and overreported amounts
  [X] 42. Corrections involve reclassified workers
  43. Explanation:

  On May 11, 2026, an internal review found that Jordan Reyes — paid $18,000
  from April 15 through June 30, 2025 as an independent contractor — was a
  common-law employee under Treas. Reg. §31.3121(d)-1(c): Jordan worked only
  for Aspen Studio LLC, used company equipment, followed company schedules,
  was supervised daily, and had no independent business.

  Section 3509 rates apply: the reclassification is the employer's own, the
  employer did not intentionally disregard the withholding requirements, no
  income tax was withheld from the payments, and Form 1099-NEC reporting the
  payments was filed on January 26, 2026. Rates used (information returns
  filed): 1.5% federal income tax, 7.44% social security, 1.74% Medicare.

  Computation: $18,000 × 1.5% = $270.00; $18,000 × 7.44% = $1,339.20;
  $18,000 × 1.74% = $313.20; total $1,922.40. Line 6 increases from
  $42,000.00 to $60,000.00.

  Q3 2025 is affected by the same issue; a separate Form 941-X for Q3 2025
  is being filed with this one.

## Part 5 — Sign here
Title: Managing Member
Phone: 720-555-0118
Date: May 22, 2026
Signature: __________

## Required attachments / related filings
- [X] Line 43 explanation (above)
- [ ] Form 8974 — N/A
- [ ] Q3 2025 941-X — separate form, filed together
- [ ] 2025 Form W-2 / W-3 for Jordan — late; file now via SSA Business Services Online
- [ ] Corrected 2025 Form 1099-NEC for Jordan

## Validation summary
- Math: all checks passed
  - $18,000 × 1.5% = $270.00 ✓
  - $18,000 × 7.44% = $1,339.20 ✓
  - $18,000 × 1.74% = $313.20 ✓
  - Line 23 = Line 27 = $1,922.40 ✓
- Sanity:
  - §3509 eligibility documented: no intentional disregard, no income tax withheld, 1099-NEC filed before discovery
  - Period of limitations: Forms 941 for 2025 count as filed April 15, 2026, so the underreported-tax window for Q2 2025 runs to April 15, 2029 (Instructions for Form 941-X)
  - Interest-free: filed by July 31, 2026 (due date of the Q2 2026 Form 941) with payment
  - The employer cannot recover the §3509 tax from Jordan (Instructions for Form 941-X, lines 19–22)
- Next steps:
  - File 941-X for Q3 2025 (same computation on that quarter's $18,000)
  - File the 2025 W-2 for Jordan (Box 1 = $36,000 for Q2 + Q3)
  - File the corrected 1099-NEC
  - Pay the $1,922.40 (plus the Q3 amount) electronically when filing
  - State unemployment / state withholding implications — consult the Colorado Department of Labor and Employment and Department of Revenue
  - Review remaining 1099 contractors for similar misclassification risk

## Sources cited in this draft
- IRS Form 941-X (Rev. April 2026)
- IRS Instructions for Form 941-X (Rev. April 2026), lines 6, 19–22, 27, 42, 43; "Underreported tax"; "Is There a Deadline for Filing Form 941-X?"
- IRC §3509 (reclassified worker rates)
- IRC §6205 (interest-free adjustment for employment taxes)
- Treas. Reg. §31.3121(d)-1(c) (common-law employee factors)
- IRC §6501 (assessment period), §6513(c)(1) (Forms 941 deemed filed April 15)
- IRS quarterly interest rates (https://www.irs.gov/payments/quarterly-interest-rates)
- Pub. 15-A (Employer's Supplemental Tax Guide) — worker classification
```

## Why each non-obvious choice

**Why §3509 rates and not full rates?** Aspen didn't intentionally disregard the rules, withheld no income tax from Jordan, and filed the 1099-NEC, so the lowest §3509 rates apply. Full rates would be $18,000 × 15.3% = $2,754 of FICA plus income tax withholding the employer can no longer collect. Without the 1099-NEC, the §3509 rates would be 3.0% / 8.68% / 2.03% = $2,467.80.

**Why are the employee FICA rates reduced (20% of 6.2% and 1.45%)?** Section 3509 sets a reduced employee-share rate because the employer can't realistically recover FICA from wages already paid; the employer pays it and can't collect it from the worker.

**Why Part 1, line 1 (Adjustment) and not line 2 (Claim)?** Line 1 is required for underreported tax (Aspen owes more). Line 2 is only for overreported tax.

**Why lines 19–21 and not lines 7, 8, and 12?** The instructions put wage corrections for reclassified workers at §3509 rates on lines 19–22 (column 1 = the reclassified worker's wages only, column 2 = amounts previously reported for that worker). Lines 8 and 12 use the full rates.

**Why does the 1099-NEC need a correction?** If Jordan now has a W-2 for the same pay, an outstanding 1099-NEC double-reports the income and can trigger a CP2000 inquiry on Jordan's personal return.

**Can this be e-filed?** Yes. Form 941-X can be filed through Modernized e-File, and the IRS encourages it. On paper, a Colorado employer mails to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0005 (Instructions for Form 941-X, Rev. April 2026, "Where Should You File Form 941-X?").

**What about Q1 2025?** The agent should ask: did Jordan also work in Q1 2025? The user confirmed Jordan started April 15, 2025, so Q1 is unaffected.

**Audit defense for the 941-X:**
1. Worker classification analysis with common-law factors documented
2. Engagement records showing Jordan's exclusive work, equipment, schedule
3. Filed 1099-NEC (proof for the lower §3509 rates)
4. CPA opinion supporting reclassification
5. Internal memo recording the decision and discovery date
6. Computations showing §3509 application
