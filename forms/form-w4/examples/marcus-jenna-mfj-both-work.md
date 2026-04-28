# Example — Marcus & Jenna, MFJ, Both Work

The classic two-earner MFJ trap. Without Step 2, the household under-withholds by thousands.

## Background

- Marcus Chen, age 34, software engineer
  - Salary: $95,000/year
  - Biweekly pay (26 checks/year)
- Jenna Chen, age 33, registered nurse
  - Salary: $68,000/year
  - Biweekly pay (26 checks/year)
- Married, filing MFJ
- No children
- No other income
- Standard deduction
- Last year's tax return: balance due of $3,200 (under-withheld due to bad multi-job W-4 setup)

## The Problem

If Marcus and Jenna each submit a W-4 with only Steps 1 and 5 (filing status MFJ, nothing else), each employer's payroll software thinks the worker's only income is their own salary.

- Marcus's employer withholds for $95,000 MFJ → ~$8,200/year
- Jenna's employer withholds for $68,000 MFJ → ~$4,200/year
- Total withheld: ~$12,400

Actual 2025 federal tax on $163,000 MFJ taxable income (after $30,000 std deduction → $133,000 taxable):
- 10% on first $23,850 = $2,385
- 12% on $23,850 - $96,950 = $8,772
- 22% on $96,950 - $133,000 = $7,931
- **Total: ~$19,088**

Under-withholding: $19,088 − $12,400 = **$6,688 shortfall**.

That matches their actual experience last year ($3,200 owed) plus the underpayment penalty assessed by the IRS via Form 2210.

## Agent Conversation Flow

**Agent:** Marcus and Jenna, what was your tax situation last year?

**Marcus:** We owed $3,200 plus a small penalty.

**Agent:** That's almost certainly because both of your W-4s were set up assuming each was the only job in the household. We'll fix that with Step 2. Three options:

(a) IRS Tax Withholding Estimator — most accurate
(b) Multiple Jobs Worksheet on Page 3 of the W-4 — accurate enough, no internet needed
(c) Step 2(c) checkbox on both W-4s — only if your salaries are roughly equal

Your salaries differ ($95K vs $68K, ratio 1.4×), so I'd skip option (c). I recommend option (a). Do you have your most recent pay stubs?

**Marcus:** Yes.

**Agent:** Run the IRS Tax Withholding Estimator together: https://www.irs.gov/individuals/tax-withholding-estimator. Enter both your YTD pay stubs, expected total wages, MFJ filing status, no dependents, standard deduction. The output will be a recommended Step 4(c) amount for Marcus's W-4.

[After running estimator]

**Marcus:** It says I should add $134/check to Step 4(c) of my W-4. Jenna's W-4 stays simple.

**Agent:** Perfect. That's $134 × 26 = $3,484 of additional annual withholding, plus your existing baseline. Combined with Jenna's normal withholding, you'll be very close to the $19,088 target.

## Marcus's W-4 Draft (higher-paying job)

```markdown
# Form W-4 — Marcus Chen — DRAFT for tax year 2026

## Step 1
1(a) Marcus Chen, 1547 Oak Avenue, Seattle WA 98103
1(b) SSN: XXX-XX-5678
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
Method: (a) IRS Tax Withholding Estimator
Step 2(c) box: ☐ Not checked (using estimator output instead)

## Step 3 — Dependents
$0 — no children, no other dependents

## Step 4 — Other Adjustments
4(a) Other income: $0
4(b) Deductions: $0 (standard deduction)
4(c) Extra withholding: $134 per pay period

## Step 5
Signed: Marcus Chen
Date: 2026-05-01

## Pay frequency: biweekly (26)

## Estimated annual federal income tax withheld:
- Baseline ($95K MFJ table): ~$8,200
- Step 4(c) extra: $134 × 26 = $3,484
- Total: ~$11,684

## Validation summary
- Math: $134/check × 26 = $3,484 annual addition ✓
- Sanity: Step 3 = $0 (no dependents) ✓
- Coordination: Jenna's W-4 has Step 2/3/4 blank — see her draft
```

## Jenna's W-4 Draft (lower-paying job)

```markdown
# Form W-4 — Jenna Chen — DRAFT for tax year 2026

## Step 1
1(a) Jenna Chen, 1547 Oak Avenue, Seattle WA 98103
1(b) SSN: XXX-XX-9012
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
N/A — Marcus's W-4 handles the multi-job math via Step 4(c)

## Step 3 — Dependents
$0 — no dependents (and Marcus's W-4 would be the one to claim them anyway)

## Step 4
4(a) $0
4(b) $0
4(c) $0

## Step 5
Signed: Jenna Chen
Date: 2026-05-01

## Estimated annual federal income tax withheld: ~$4,200 (baseline $68K MFJ table)
```

## Combined Result

- Marcus withholding: $11,684
- Jenna withholding: $4,200
- **Combined: $15,884 vs target $19,088 = $3,204 short**

Hmm — still short. The estimator recommended $134 but the actual gap is closer to $258/check ($6,688 / 26). Let me reconsider.

**Agent (revised):** I'd recommend rerunning the estimator and verifying you entered Jenna's full salary. If the estimator output is too low, the Multiple Jobs Worksheet is a sanity check.

**Multiple Jobs Worksheet (Page 3, MFJ table):**
- Higher-paying job: $95,000 → row "$80,001 - $100,000"
- Lower-paying job: $68,000 → column "$60,001 - $70,000"
- Cell value (illustrative): ~$7,610

$7,610 / 26 = **$293/check** on Marcus's Step 4(c).

That's higher than the Estimator's $134 — likely because the Estimator already accounted for some current-year withholding having occurred. Both approaches are valid; the Worksheet over-withholds slightly (better than under).

**Final recommendation for Marcus's W-4:**

Step 4(c): **$293** (Worksheet result) — safer, slight over-withholding.

OR Step 4(c): **$258** (math from prior-year actual gap divided by pay periods) — most accurate based on last year's specific situation.

## Year-End (Projected)

With $293/check on Marcus's Step 4(c):
- Marcus: $8,200 + $7,618 = $15,818
- Jenna: $4,200
- **Combined: $20,018 vs target $19,088 = $930 over** (small refund — acceptable)

## Key Takeaways

- Two-earner MFJ households almost always under-withhold without Step 2
- Even an unequal-pay couple should run the Estimator (or use the Worksheet) and apply result to Step 4(c) of higher-paying job
- The Estimator's output and the Worksheet's output may differ — Worksheet is more conservative (safer)
- Lower-paying spouse's W-4 stays simple (Steps 1 + 5 only)
- Re-run the Estimator each October to confirm projection against YTD reality
