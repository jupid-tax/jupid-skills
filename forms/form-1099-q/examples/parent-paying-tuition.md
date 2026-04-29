# Example: Parent Withdraws $30,000 from 529 for Daughter's Tuition (Fully Qualified, Tax-Free)

The canonical "everything works as intended" pattern. A parent uses 529 funds to pay college tuition and required expenses for a half-time-or-more enrolled beneficiary. The full distribution is qualified; nothing flows to the parent's 1040.

## The filer

- **Account owner / 1099-Q recipient**: Robert Carter (father)
- **Designated beneficiary**: Sophia Carter (daughter, 19, sophomore at State U)
- **Plan**: New York's 529 Direct Plan (a state 529)
- **Tax year**: 2025 (filing in 2026)
- **Robert's filing status**: MFJ; AGI $145,000

## 1099-Q received

```
Box 1 (Gross distribution):        $30,000
Box 2 (Earnings):                  $11,400
Box 3 (Basis):                     $18,600
Box 4 (Trustee-to-trustee):        Unchecked
Box 5 (Program type):              State 529
Box 6 (Designated beneficiary):    Unchecked (recipient is the parent, not the beneficiary)
Recipient: Robert Carter (account owner)
Payer: NY 529 Direct
```

Verification: Box 1 = Box 2 + Box 3 → $30,000 = $11,400 + $18,600 ✓

## Qualified Education Expenses (Step 3)

Sophia is a sophomore at State U, enrolled full-time, living in an on-campus dorm. The Carters provide:

| Category                            | Amount   | Source                        |
|-------------------------------------|----------|-------------------------------|
| Tuition and required fees           | $14,800  | Form 1098-T Box 1             |
| Required books, supplies, equipment | $1,200   | Receipts; required by syllabi |
| Room and board (on-campus dorm)     | $13,500  | Within school's COA cap       |
| Computer (Sophia's primary use)     | $1,400   | One MacBook Air, used by her  |
| **Total QHEE**                      | **$30,900** | |

Validation:
- Sophia is enrolled full-time (more than half-time) → room and board qualifies
- The $13,500 dorm cost is below State U's published cost-of-attendance for on-campus housing ($14,200), so the full amount is qualified
- The MacBook is primarily used by Sophia for coursework; agent confirmed via family discussion

## AAQEE Adjustment (Step 4)

Robert reports:
- Tax-free scholarships: $0 (Sophia received no scholarships in 2025)
- Employer education assistance: $0
- AOTC claimed: $4,000 (the Carters claim AOTC, yielding $2,500 credit; Sophia is in her first 4 years)
- LLC claimed: $0

```
AAQEE = $30,900 (QHEE)
        − $0 (scholarships)
        − $0 (employer assistance)
        − $4,000 (AOTC)
        − $0 (LLC)
      = $26,900
```

## Step 5 — Compute taxable earnings

```
Box 1 = $30,000
AAQEE = $26,900

Non-qualified portion = $30,000 − $26,900 = $3,100
Earnings ratio = $11,400 / $30,000 = 0.38

Taxable earnings = $3,100 × 0.38 = $1,178
```

The Carters spent $30,000 from the 529 but only had $26,900 of expenses available after AOTC coordination — so $3,100 of the distribution is non-qualified, and $1,178 of earnings is taxable to Robert (the recipient).

## Step 6 — 10% additional tax

The $1,178 of earnings is taxable solely because the Carters used $4,000 of the same expenses for AOTC. IRC §529(c)(6)(B)(iii) waives the 10% additional tax in this case.

```
10% additional tax = $0 (waived under AOTC coordination exception)
```

Robert reports $1,178 on Schedule 1 Line 8z but Form 5329 shows the AOTC-coordination exception, so Schedule 2 Line 8 = $0.

## The completed worksheet

```markdown
# Form 1099-Q — DRAFT WORKSHEET for tax year 2025

## 1099-Q received
- Recipient: Robert Carter (account owner)
- Trustee/custodian: NY 529 Direct Plan
- Box 1 (Gross distribution): $30,000
- Box 2 (Earnings): $11,400
- Box 3 (Basis): $18,600
- Box 4 (Trustee-to-trustee transfer): No
- Box 5 (Program type): State 529
- Box 6 (Designated beneficiary is recipient): No (recipient is parent, not Sophia)

## Qualified Education Expenses
| Category                            | Amount   |
|-------------------------------------|----------|
| Tuition and required fees           | $14,800  |
| Required books and supplies         | $1,200   |
| Room and board (half-time+)         | $13,500  |
| Computer, software, internet        | $1,400   |
| **Total QHEE**                      | $30,900  |

## AAQEE Adjustment
- Tax-free scholarships:               −$0
- Employer education assistance:       −$0
- Expenses used for AOTC:              −$4,000
- Expenses used for LLC:               −$0
- **Adjusted QHEE (AAQEE)**:           $26,900

## Taxable amount calculation
- Box 1:                          $30,000
- AAQEE:                          $26,900
- Non-qualified portion:          $3,100
- Earnings ratio (Box 2 / Box 1): 0.38
- **Taxable earnings**:           $1,178

## 10% additional tax
- Subject to 10% additional tax: No (exception)
- Exception applied:             AOTC coordination (IRC §529(c)(6)(B)(iii))
- **Additional tax owed**:       $0

## Where this goes on the return
- Schedule 1 Line 8z: $1,178 (description: "Taxable 529 distribution")
- Schedule 2 Line 8 via Form 5329 Part II: $0 (exception applied)
- 1040 Line 8: includes $1,178 from Schedule 1 Line 10
- 1040 Line 23: $0 from Schedule 2

## Validation summary
- Math: all checks passed
  - Box 1 = Box 2 + Box 3: ✓
  - AAQEE ≤ Total QHEE: ✓
  - Taxable earnings ≤ Box 2: ✓
- Sanity: no warnings raised
- Next steps:
  - Robert files Schedule 1, Schedule 2, and Form 5329 with his MFJ 1040
  - Form 8863 for AOTC ($4,000 expenses → $2,500 credit)
  - Net tax impact: $1,178 included in income at 22% MFJ marginal rate ≈ $259 federal tax;
    AOTC = $2,500 credit. Net benefit from AOTC + 529 = $2,500 − $259 = $2,241 vs. $0
    if Robert had used 529 for the full $30,900 with no AOTC.
  - Robert retains 1099-Q, Form 1098-T, dorm receipt, computer receipt, and worksheet for 3+ years

## Sources cited in this draft
- IRS Form 1099-Q (Rev. 2025)
- IRC §529 (Qualified Tuition Programs)
- IRC §529(c)(3)(D) — Earnings allocation
- IRC §529(c)(6)(B)(iii) — AOTC-coordination exception to 10% additional tax
- IRC §25A — American Opportunity Tax Credit
- Pub 970 chapter 8
```

## Why each non-obvious choice

**Why is the AOTC coordination beneficial despite triggering Schedule 1 income?** The math:
- AOTC credit value: $2,500 (refundable up to $1,000)
- Schedule 1 income added: $1,178
- Federal tax on $1,178 at 22% marginal rate: ~$259
- Net benefit: $2,500 − $259 = $2,241

Without AOTC, the entire $30,000 distribution would be tax-free (AAQEE = $30,900 ≥ Box 1), but the $2,500 credit would be lost. AOTC coordination wins by ~$2,200.

**Why is the 10% additional tax $0?** IRC §529(c)(6)(B)(iii) explicitly waives the 10% additional tax when a distribution is taxable solely because of AOTC/LLC coordination. The earnings portion is still in income (Schedule 1 Line 8z), but Form 5329 Line 6 includes the $1,178 as exempt distribution, so the additional-tax base is $0.

**Why is the recipient Robert and not Sophia?** Robert is the account owner of the 529. The check (or direct payment to State U) was issued in his name as account owner. Box 6 (designated beneficiary = recipient) is unchecked because Sophia is the beneficiary but Robert is the recipient. So Robert reports the taxable portion on his MFJ 1040.

**Why isn't transportation included in QHEE?** Sophia drove home over Thanksgiving and bought a $400 plane ticket for spring break. Per Pub 970 chapter 8, transportation is not a qualified expense for 529 (it's only qualified for Coverdell K-12, not higher education for either plan type).

**Why is the computer fully qualified?** IRC §529(e)(3)(A)(iii) (added by PATH Act 2015) qualifies "computer technology, equipment, or services" if used **primarily** by the beneficiary while enrolled. The Carters confirmed the MacBook is Sophia's, used by her for coursework. If the family said "we all share it," only the beneficiary-use portion would qualify.

**What if the Carters had been audited?** Their audit defense:
1. Form 1098-T from State U substantiates tuition and required fees ($14,800)
2. Bookstore receipts substantiate required books ($1,200)
3. State U dorm contract substantiates room and board ($13,500), and State U's published COA proves the figure is within cap
4. Apple Store receipt + Sophia's enrollment status substantiate the computer
5. Sophia's enrollment record (full-time) substantiates room-and-board eligibility
6. AOTC coordination documented in the worksheet — auditor sees the AAQEE allocation and verifies no double-dipping
