# Example — Sarah, Single, One Job

The simplest W-4 scenario. Steps 1 and 5 only.

## Background

- Sarah Mitchell, age 28
- Just started a new job as a marketing coordinator at a SaaS company
- Salary: $72,000/year (biweekly = $2,769.23 gross per check; 26 paychecks/year)
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

5. Any of these for 2026: tips, overtime, car loan interest on a new car, student loan interest, IRA contributions, or deductions you'd itemize (mortgage interest, big charitable giving)?
**Sarah:** None. I take the standard deduction and I'm not giving to charity this year.

6. Did you owe a lot or get a big refund last year?
**Sarah:** Roughly broke even — $200 refund.

7. Did you have a federal income tax liability for 2025? (Checks the exemption box.)
**Sarah:** Yes, I paid tax.

**Agent:** Then you can't claim exemption, and you only need Steps 1 and 5 of the W-4. No Step 2 (single job), no Step 3 (no dependents), no Step 4 (no other income, Deductions Worksheet line 15 is $0, no extra needed).

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
4(b) Deductions: $0 (Deductions Worksheet: lines 1a–7 $0; 8a $72,000; 8b $72,000; 9 $640,600; 10 $0; 11 $16,100; 12 $0; 13 $16,100; 14 $0 (line 13 > line 10, so line 12); 15 $0)
4(c) Extra withholding: $0

## Exempt from withholding: ☐ not claimed (Sarah had 2025 tax liability)

## Step 5 — Signature
Signed: Sarah Mitchell
Date: 2026-05-01

## Pay frequency: biweekly (26 periods)

## Estimated annual federal income tax withheld: $7,010 ($269.62 per check)

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

**Withholding math (employer side), Pub. 15-T (2026) Worksheet 1A, annual percentage method:**

- Line 1c annual wages: $2,769.23 × 26 = $72,000
- Line 1g (Step 2 box not checked, Single): $8,600
- Line 1i adjusted annual wage amount: $72,000 − $8,600 = $63,400
- STANDARD Withholding Rate Schedule, Single: $57,900–$113,200 row → $5,800 + 22% × ($63,400 − $57,900) = $5,800 + $1,210 = $7,010
- Per paycheck: $7,010 / 26 = $269.62

**Projected 2026 tax (Rev. Proc. 2025-32):**

- Taxable income: $72,000 − $16,100 standard deduction = $55,900
- Tax: $5,800 + 22% × ($55,900 − $50,400) = $7,010 (rate schedule; the 2026 Tax Table, which uses $50 bands, can differ by a few dollars)

Withholding and tax match: the STANDARD schedule's 0% band ($7,500) plus the $8,600 line 1g amount equals the $16,100 standard deduction. Refund or balance due will be a few dollars either way (and rounding of per-check amounts).

**Year-end (line numbers from the 2025 Form 1040; re-check them on the 2026 form):**

- W-2 Box 1: $72,000
- W-2 Box 2: ~$7,010 (federal income tax withheld)
- Form 1040 Line 1a / 1z: $72,000
- Form 1040 Line 11a (AGI): $72,000
- Form 1040 Line 12e (standard deduction): $16,100
- Form 1040 Line 15 (taxable income): $55,900
- Form 1040 Line 16 (tax): ~$7,010
- Form 1040 Line 25a (W-2 box 2): ~$7,010
- Form 1040 Line 34 (overpaid) or 37 (owed): close to $0

## Key Takeaways

- Single, one job, no dependents = simplest W-4 possible
- With one job, the standard deduction and no other items, Pub. 15-T withholding lands within a few dollars of the tax
- No need to use the Tax Withholding Estimator unless circumstances change
- Revisit the W-4 if any life event happens (marriage, second job, side gig, etc.)
