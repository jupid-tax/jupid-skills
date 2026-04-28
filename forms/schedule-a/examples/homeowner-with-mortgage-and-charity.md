# Example: Homeowner with Mortgage and Charity (MFJ in California)

A complete walkthrough of Schedule A for a homeowner couple in a high-tax state with a mortgage, modest charity, and a moderate medical year. This is the canonical "post-OBBBA itemizer" pattern — the kind of filer for whom the SALT cap increase from $10K to $40K made itemizing worthwhile again.

This example mirrors the worked example in the [Jupid blog post on Schedule A](https://jupid.com/blog/schedule-a-itemized-deductions-2026).

## The filers

- **Names**: Patricia and Mike Reyes
- **Filing status**: Married Filing Jointly
- **State**: California
- **Tax year**: 2025 (filing in 2026)
- **AGI** (Form 1040 Line 11): $180,000
- **MAGI**: $180,000 (no foreign earned income, no add-backs)
- **Standard deduction MFJ 2025**: $30,000

## Inputs gathered (Step 2 of workflow)

### Medical (Lines 1-4)

Patricia had a knee surgery in 2025 that wasn't fully covered by insurance. After insurance, HSA, and FSA reimbursements:

| Item | Amount |
|------|--------|
| Knee surgery (out-of-pocket after insurance + HSA) | $11,200 |
| Prescription medications | $1,800 |
| Dental work (Mike) | $900 |
| Medical mileage (95 miles × 21¢) | $20 |
| Vision (glasses, exam) | $480 |
| Health insurance premiums (post-tax, supplemental) | $300 |
| **Total Line 1** | **$14,700** |

### SALT (Lines 5-7)

| Item | Amount |
|------|--------|
| California state income tax (W-2 box 17) | $14,000 |
| Real estate (property) tax on San Diego home | $9,500 |
| Personal property tax (CA vehicle registration value-based portion, 2 cars) | $0 (negligible; couple uses standard registration only) |

### Mortgage interest (Lines 8-10)

| Item | Amount |
|------|--------|
| Form 1098 box 1 (interest paid) | $11,800 |
| Form 1098 box 6 (points paid) | $0 |
| Form 1098 box 5 (PMI premiums) | $0 |
| Loan origination date | 2019-03-15 (post-12/15/2017, $750K cap applies) |
| Loan original principal | $620,000 |
| Loan current balance Jan 1, 2025 | $580,000 |

The loan is well within the $750K cap — full deductibility on Line 8a.

### Charity (Lines 11-14)

| Item | Amount |
|------|--------|
| Cash gifts to church (52 weeks × ~$80) | $4,200 |
| Non-cash to Goodwill (clothing, household goods) | $0 (not enough to track formally) |
| Carryover from prior year | $0 |
| **Raw total Line 14** | **$4,200** |

For 2025, no 0.5% AGI floor applies — full $4,200 deducts.

### Casualty (Line 15)

None.

### Other (Line 16)

None.

## The completed Schedule A draft

```markdown
# Schedule A — DRAFT for tax year 2025

## Filing context
Filing status: Married Filing Jointly
AGI (Form 1040 Line 11): $180,000
MAGI: $180,000
Standard deduction MFJ 2025: $30,000
SALT cap applicable: $40,000 (no phaseout; MAGI < $500,000)

## Lines 1-4 — Medical and Dental
1. Medical and dental expenses:        $14,700
2. AGI:                               $180,000
3. 7.5% × AGI:                         $13,500
4. Deductible medical (Line 1 − Line 3, ≥ 0): $1,200

## Lines 5-7 — Taxes
5a. State income tax (CA W-2 box 17):  $14,000
5b. Real estate taxes (San Diego home): $9,500
5c. Personal property taxes:               $0
5d. Sum 5a+5b+5c:                      $23,500
5e. SALT capped (smaller of 5d or $40K cap): $23,500
6.  Other taxes:                           $0
7.  Total taxes:                       $23,500

## Lines 8-10 — Interest
8a. Mortgage interest (Form 1098):     $11,800
8b. Mortgage interest not on 1098:         $0
8c. Points not on 1098:                    $0
8d. Mortgage insurance premiums:           $0  (Line 8d not available for 2025; reinstated for 2026+)
8e. Sum 8a-8d:                         $11,800
9.  Investment interest:                   $0
10. Total interest:                    $11,800

## Lines 11-14 — Charity
11. Cash contributions:                 $4,200
12. Non-cash contributions:                 $0
13. Carryover from prior year:              $0
14. Total charitable:                   $4,200
    Raw total: $4,200
    0.5% AGI floor (2026+ only): N/A for 2025
    Effective Line 14: $4,200

## Line 15 — Casualty and theft
15. Casualty/theft (Form 4684):             $0

## Line 16 — Other
16. Other itemized deductions:              $0

## Line 17 — Total itemized deductions
17. Total: Sum Lines 4+7+10+14+15+16:  $40,700

## Standard-vs-itemized comparison
Itemized (Line 17):       $40,700
Standard deduction MFJ:   $30,000
Recommendation: ITEMIZE
Difference: $10,700 (additional deduction by itemizing)

Federal tax savings at 22% bracket: ~$2,354

## Required attachments
- [ ] Form 8283 — NOT required (Line 12 = $0)
- [ ] Form 4684 — NOT required (Line 15 = $0)
- [ ] Form 4952 — NOT required (Line 9 = $0)

## Validation summary
- Math: all checks passed
- Sanity: no warnings raised
  - Line 17 ($40,700) > standard deduction ($30,000) ✓
  - Line 8d = 0 (correct for 2025) ✓
  - SALT cap $40K applied (correct for 2025 under OBBBA) ✓
  - Effective SALT cap = full $40K (MAGI $180K < $500K phaseout threshold) ✓
- Next steps: Schedule A attaches to Form 1040; Line 17 flows to 1040 Line 12

## Sources cited in this draft
- IRS Form 1040 Schedule A (2025 revision)
- IRS Instructions for Schedule A (2025 revision)
- IRC §164(b)(6) (SALT cap as amended by OBBBA 2025)
- Rev. Proc. 2024-40 (2025 inflation adjustments)
- Pub 502, 526, 936
```

## Why this filer itemizes (and why pre-OBBBA they wouldn't have)

The key driver is the SALT cap increase. Under TCJA's old $10,000 cap:

```
Line 5e (old cap): min($23,500, $10,000) = $10,000
Line 7 (old): $10,000
Line 17 (old): $1,200 + $10,000 + $11,800 + $4,200 = $27,200

Standard MFJ 2025: $30,000
Result under old cap: TAKE STANDARD DEDUCTION (gap $2,800)
```

Under OBBBA's $40,000 cap (2025):

```
Line 5e (new cap): min($23,500, $40,000) = $23,500 (full SALT deducts)
Line 7 (new): $23,500
Line 17 (new): $1,200 + $23,500 + $11,800 + $4,200 = $40,700

Standard MFJ 2025: $30,000
Result under new cap: ITEMIZE (gap $10,700)
```

OBBBA's SALT cap increase added $13,500 of deductible SALT to Patricia and Mike's return — moving them from "take standard" to "itemize" and saving roughly $2,354 in federal tax at their 22% bracket.

## Sensitivity check 1: Move to Texas (no state income tax)

If Patricia and Mike had moved to Austin, TX, before 2025:

```
Line 5a (state income tax): $0 (Texas has none) — or use sales tax via optional table
Line 5a (sales tax via IRS optional table at $180K MFJ in TX): ~$1,500
Line 5b (TX property tax — comparable home): $7,500
Line 5c: $0
Line 5d: $9,000
Line 5e: $9,000 (under cap)
Line 7: $9,000

Line 17: $1,200 + $9,000 + $11,800 + $4,200 = $26,200

Standard MFJ 2025: $30,000
Result: TAKE STANDARD DEDUCTION (gap $3,800)
```

The lesson: state income tax is what makes itemizing pay for typical homeowners. Without it (or without a high-property-tax state replacing it), the standard deduction wins even with a mortgage.

## Sensitivity check 2: Tax year 2026 instead of 2025

For tax year 2026, two OBBBA changes affect the math:

1. **PMI reinstated (Line 8d)**: Patricia and Mike don't pay PMI (their LTV was below 80% at origination), so this doesn't help them. Other filers with PMI gain a deduction.

2. **0.5% AGI charitable floor**: $180,000 × 0.5% = $900. Their $4,200 charitable becomes $4,200 − $900 = $3,300.

3. **SALT cap increases to $40,400**: Doesn't bind since their SALT is $23,500.

```
Line 4 (medical, unchanged):       $1,200
Line 7 (taxes, unchanged):         $23,500
Line 10 (interest, unchanged):     $11,800
Line 14 (charity, after floor):    $3,300  (was $4,200; lost $900 to floor)
Line 17 (total):                   $39,800

Standard MFJ 2026 (placeholder):   ~$30,800 (estimate; verify Rev. Proc.)
Result: ITEMIZE (gap ~$9,000)
```

Itemizing still wins, but the $900 charity floor cost them $198 of federal tax at 22%. For higher-income, higher-charity donors, the floor's bite is bigger — and bunching contributions becomes more valuable.

## Filing channel

Patricia and Mike will file via TurboTax (paid software) since they have W-2 wages, mortgage interest, and standard charitable activity. The TurboTax Schedule A interview will:

1. Auto-import Form 1098 from their lender (Wells Fargo)
2. Auto-import W-2 box 17 for state income tax
3. Ask "Did you make charitable contributions?" — they enter $4,200 cash to church
4. Ask "Did you have medical expenses out of pocket?" — they enter $14,700 with category breakdown
5. Compare itemized $40,700 vs standard $30,000 and recommend ITEMIZE
6. File electronically; e-file confirmation typically within 24-48 hours

If using FFFF instead, follow the field-by-field mapping in `filing.md` Section 1. If filing on paper, attach Schedule A behind Form 1040 in attachment-sequence order.

## Records to retain

- Form 1098 from lender (for 3 years from filing)
- Property tax bill (3 years; longer if disposing of property)
- W-2 (3 years; same as return)
- Church year-end giving statement (CWA — required since gifts ≥ $250 made annually)
- Medical receipts and EOBs (3 years)
- Insurance reimbursement records showing out-of-pocket calculation (3 years)

## Common variations to watch for

- **Refinance during the year**: split the loan into pre-refinance and post-refinance interest; both go on Line 8a if purposes were qualifying
- **Spouse 65 or older**: add additional standard deduction ($1,550 per qualifying spouse for 2025) — could shift the breakeven
- **Major home improvement funded by HELOC**: add HELOC interest to Line 8a if buy/build/improve traced
- **Donor-advised fund contribution**: would substantially boost Line 11 if used for bunching
- **Casualty loss in a federally declared disaster**: would add to Line 15
