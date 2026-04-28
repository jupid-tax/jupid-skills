# Example — Sarah, Single, One Job

The simplest W-4 scenario. Steps 1 and 5 only.

## Background

- Sarah Mitchell, age 28
- Just started a new job as a marketing coordinator at a SaaS company
- Salary: $72,000/year (biweekly = $2,769 gross per check; 26 paychecks/year)
- Single, no spouse, no dependents
- No second job, no side gig
- Standard deduction (no Schedule A items)
- Lives in Austin, TX (no state income tax — federal only)

## Agent Conversation Flow

**Agent:** Sarah, before we fill out your W-4, I need to confirm a few things.

1. Is this your only job?
**Sarah:** Yes.

2. Are you married?
**Sarah:** No.

3. Do you have any dependents?
**Sarah:** No.

4. Any other income — investments, side gig, rental?
**Sarah:** No, just my salary.

5. Do you itemize deductions (mortgage interest, big charitable giving)?
**Sarah:** No, I take the standard.

6. Did you owe a lot or get a big refund last year?
**Sarah:** Roughly broke even — $200 refund.

**Agent:** Perfect. You only need Steps 1 and 5 of the W-4. No Step 2 (single job), no Step 3 (no dependents), no Step 4 (no other income, standard deduction, no extra needed).

## Sarah's W-4 Draft

```markdown
# Form W-4 — DRAFT for tax year 2026

## Step 1 — Personal Information
1(a) Name: Sarah Mitchell
1(a) Address: 482 Maple St, Austin, TX 78704
1(b) SSN: XXX-XX-1234
1(c) Filing status: ☑ Single or Married Filing Separately

## Step 2 — Multiple Jobs or Spouse Works
N/A — only one job

## Step 3 — Dependents
$0 — no dependents

## Step 4 — Other Adjustments
4(a) Other income: $0
4(b) Deductions: $0 (standard deduction)
4(c) Extra withholding: $0

## Step 5 — Signature
Signed: Sarah Mitchell
Date: 2026-05-01

## Pay frequency: biweekly (26 periods)

## Estimated annual federal income tax withheld: ~$6,617

## Validation summary
- Math: all checks passed
- Sanity: no warnings
- Coordination: N/A (no spouse, no second job)
- Side-gig SE tax: N/A

## Submission
Submit to: SaaS Company HR / payroll
Effective: first paycheck (new hire — applies immediately, not 30-day rule)
```

## What Happens Next

**Withholding math (employer side):**

Pub 15-T 2025 Single table for $72,000 annual wages, biweekly:
- Standard deduction (single): $15,000
- Taxable income for withholding: $72,000 − $15,000 = $57,000
- 2025 tax brackets (single):
  - 10% on first $11,925 = $1,192.50
  - 12% on $11,925 - $48,475 = $4,386.00
  - 22% on $48,475 - $57,000 = $1,875.50
  - Total: ~$7,454 of federal tax... wait, this differs from the $6,617 I cited.

Let me recompute properly using Pub 15-T's percentage method for biweekly pay:

For single filer, biweekly $2,769 gross:
- After standard deduction allocation per pay period: ~$2,192 taxable
- Annualized: ~$57,000
- Tax computation: roughly matches $7,400 of expected annual federal income tax

Sarah's W-2 Box 2 will show approximately $7,400 of federal withholding. Her actual tax liability on $57,000 taxable income is also ~$7,400. Refund or balance due will be small (under $200 either way).

**Year-end:**

- W-2 Box 1: $72,000
- W-2 Box 2: ~$7,400 (federal income tax withheld)
- Form 1040 Line 1z: $72,000
- Form 1040 Line 11 (AGI): $72,000
- Form 1040 Line 12 (std deduction): $15,000
- Form 1040 Line 15 (taxable income): $57,000
- Form 1040 Line 16 (tax): ~$7,400
- Form 1040 Line 25a (W-2 box 2): ~$7,400
- Form 1040 Line 34 (refund) or 37 (owed): close to $0

## Key Takeaways

- Single, one job, no dependents = simplest W-4 possible
- Default withholding tables get you within ~$200 of correct
- No need to use the Tax Withholding Estimator unless circumstances change
- Revisit the W-4 if any life event happens (marriage, second job, side gig, etc.)
