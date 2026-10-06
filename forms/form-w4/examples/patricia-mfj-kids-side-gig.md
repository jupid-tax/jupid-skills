# Example — Patricia, MFJ, Two Kids + Etsy Side Gig

The full W-4 treatment: Step 2 (multi-job), Step 3 (dependents), and Step 4(c) (side income + extra), with the self-employment income kept off Step 4(a) as the 2026 form requires.

All numbers use the 2026 Form W-4 (instructions and page 5 MFJ table), Pub. 15-T (2026) Worksheet 1A with the STANDARD Annual Percentage Method schedule, the 2026 rate schedule and standard deduction (Rev. Proc. 2025-32), and Schedule SE rules. Math checked in python.

## Background

- Patricia Sanchez, age 38, Senior Product Manager
  - Salary: $135,000/year, biweekly (26 checks)
- David Sanchez, age 39, high school teacher
  - Salary: $48,000/year, biweekly (26 checks)
- Married, filing MFJ; both have SSNs valid for employment
- Two children, both with SSNs valid for employment:
  - Sofia, age 7, in 2nd grade
  - Marco, age 4, in pre-K
- Patricia runs a small Etsy shop (handmade jewelry):
  - Expected 2026 net profit: $14,000
  - Patricia files Schedule C + Schedule SE
- Standard deduction; no Deductions Worksheet items (no tips, overtime, car loan interest, student loan interest, IRA, charity)
- Prior-year return: balance due plus an underpayment penalty
- Combined household income: $135K + $48K + $14K = **$197,000**
- Step 3 test: total income $400,000 or less (MFJ) ✓
- Updating W-4s on January 9, 2026, so full-year amounts apply

## The Problem

Patricia and David's old W-4 setup (filed when the form's Step 3 used $2,000 per child):
- Patricia: Step 3 = $4,000 (2 kids × $2,000)
- David: also Step 3 = $4,000 (double-counted!)
- Neither completed Step 2 (multi-job) → combined wages under-withheld
- Etsy income not covered by withholding or by quarterly Form 1040-ES

Carried into 2026 unchanged (Pub. 15-T (2026)):
- Patricia: $135,000 − $12,900 = $122,100 → $11,600 + 22% × ($122,100 − $120,100) = $12,040, minus $4,000 Step 3 = $8,040
- David: $48,000 − $12,900 = $35,100 → 10% × ($35,100 − $19,300) = $1,580, minus $4,000 Step 3 = $0 (can't go below zero)
- Total withheld: **$8,040**

Projected 2026 tax:
- SE tax: $14,000 × 0.9235 = $12,929 × 15.3% = **$1,978**; half of SE tax deduction $989
- AGI: $135,000 + $48,000 + $14,000 − $989 = $196,011
- Taxable income before QBI: $196,011 − $32,200 = $163,811
- QBI deduction: 20% × ($14,000 − $989) = $2,602 (below the $403,500 2026 threshold; 20% of taxable income is higher)
- Taxable income: $161,209 → tax $11,600 + 22% × ($161,209 − $100,800) = $24,890
- Child Tax Credit: 2 × $2,200 = −$4,400
- Total tax: $24,890 − $4,400 + $1,978 = **$22,468**

Shortfall if nothing changes: $22,468 − $8,040 = **$14,428**, plus an underpayment penalty under IRC §6654 (withholding below both safe harbors).

## Agent Conversation Flow

**Agent:** Patricia, there are FOUR issues with your W-4 setup:

1. **Both you and David claimed the kids on Step 3.** Only ONE W-4 should carry Step 3 — the highest-paying job's for best accuracy.
2. **Neither of you completed Step 2.** With both working, a multiple-jobs adjustment is needed.
3. **The Etsy income isn't covered.** The 2026 form says self-employment income does NOT go on Step 4(a); it says to use the IRS Tax Withholding Estimator and put the result in Step 4(c), or to pay quarterly Form 1040-ES.
4. **SE tax (15.3% of 92.35% of profit) isn't covered either.**

The form's route for a household with self-employment income is the Estimator (www.irs.gov/W4App). Do you want to run it, or should I build the numbers on paper with the Multiple Jobs Worksheet plus a projection of the Etsy tax (Pub. 505 Worksheets 1-3 and 1-5)?

**Patricia:** Paper, please. And I want the Etsy tax handled through my paycheck, not quarterly payments.

**Agent:** Here's the build:

- **Step 3:** 2 × $2,200 = $4,400, on your W-4 only
- **Wages (Step 2(b)):** MFJ table, row "$100,000 - 149,999" (your $135,000), column "$40,000 - 49,999" (David's $48,000) = $9,040 → ÷ 26 = $347.69 → $348 per check
- **Etsy (Step 4(c) add-on):** projected tax with the Etsy profit ($22,468) minus without it ($18,200: taxable $150,800 → $22,600 − $4,400 CTC) = $4,268 → ÷ 26 = $164.15 → $165 per check
- **Step 4(c) total:** $348 + $165 = **$513 per check**
- Half-pay test for Step 2(c): $48,000 is less than half of $135,000, so the form says Step 2(b) is more accurate than the checkbox here.

If you'd rather pay the Etsy part quarterly: $4,268 ÷ 4 = $1,067 per Form 1040-ES installment, and Step 4(c) drops to $348.

**Patricia:** Withholding, $513.

## Patricia's W-4 (higher-paying job, carries all credits)

```markdown
# Form W-4 — Patricia Sanchez — DRAFT for tax year 2026

## Step 1
1(a) Patricia Sanchez, 2230 Pine Ridge Drive, Denver CO 80211
1(b) SSN: XXX-XX-3456
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs or Spouse Works
Method: (b) Multiple Jobs Worksheet
  Line 1: $9,040 (MFJ table, $100,000–149,999 row × $40,000–49,999 column)
  Line 3: 26
  Line 4: $347.69 → $348 (to Step 4(c))
Step 2(c) box: ☐ Not checked (David's pay is less than half of Patricia's)

## Step 3 — Dependents (THIS W-4 ONLY — David's is blank)
Qualifying children under 17 × $2,200 = 2 × $2,200 = $4,400
Other dependents × $500 = 0 × $500 = $0
Other credits = $0 (asked: none expected)
Total — enter on Step 3: $4,400

## Step 4 — Other Adjustments
4(a) Other income (not from jobs or self-employment): $0
     (Etsy profit is self-employment income: kept off 4(a) per the 2026 form)
4(b) Deductions: $0 (Deductions Worksheet line 15 = $0: lines 1a–7 $0; 8a $197,000; 8b $197,000; 9 $768,700; 10 $0; 11 $32,200; 12 $0; 13 $32,200; 14 $0)
4(c) Extra withholding per pay period:
   - $348 (Multiple Jobs Worksheet line 4)
   - + $165 (Etsy income tax + SE tax: $4,268 / 26)
   - = $513 per pay period

## Exempt from withholding: ☐ not claimed

## Step 5
Signed: Patricia Sanchez
Date: 2026-01-09

## Pay frequency: biweekly (26)

## Estimated annual withholding effect (Pub. 15-T (2026) Worksheet 1A):
   - Adjusted annual wage amount: $135,000 − $12,900 = $122,100 → $12,040
   - Step 3 reduction: −$4,400
   - Step 4(c) addition: $513 × 26 = +$13,338
   ──────────────────────────────────────
   Total federal income tax withheld: $20,978

## Validation summary
- Math: $4,400 Step 3; $348 + $165 = $513 Step 4(c); $513 × 26 = $13,338 ✓
- Sanity warnings:
  * Total household income $197K, under the $400K MFJ Step 3 limit ✓
  * Step 3 only on Patricia's W-4 (David's is blank) ✓
  * No self-employment income on Step 4(a) ✓
  * Etsy SE tax covered via Step 4(c) ✓
- Coordination: David's W-4 has Steps 2–4 blank; Step 2(c) unchecked on both
- Side-gig: income tax and SE tax covered via Step 4(c); no 1040-ES planned
```

## David's W-4 (lower-paying job)

```markdown
# Form W-4 — David Sanchez — DRAFT for tax year 2026

## Step 1
1(a) David Sanchez, 2230 Pine Ridge Drive, Denver CO 80211
1(b) SSN: XXX-XX-7890
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
N/A — Patricia's W-4 carries the worksheet result in Step 4(c); Step 2(c) not checked

## Step 3
$0 — Patricia's W-4 carries the dependent claims

## Step 4
4(a) $0
4(b) $0
4(c) $0

## Exempt from withholding: ☐ not claimed

## Step 5
Signed: David Sanchez
Date: 2026-01-09

## Estimated annual withholding: $1,580 ($48,000 − $12,900 = $35,100 → 10% × ($35,100 − $19,300); Pub. 15-T (2026) STANDARD schedule, MFJ)
```

## Year-End (Projected)

| Component | Amount |
|-----------|--------|
| Patricia federal withholding | $20,978 |
| David federal withholding | $1,580 |
| **Total household withholding** | **$22,558** |

Projected total tax liability (from above): **$22,468** (income tax $24,890 − CTC $4,400 + SE tax $1,978).

Refund or balance due: $22,558 − $22,468 = **$90 refund**.

## Key Comparison: Before vs After

| Metric | Old setup carried into 2026 | Corrected W-4s |
|--------|-------------------|------------------------|
| Patricia Step 3 | $4,000 (both spouses) | $4,400 (this W-4 only) |
| David Step 3 | $4,000 (DUPLICATE) | $0 (removed) |
| Step 2 method | None | (b) Worksheet, $9,040 → $348/check |
| Step 4(a) | $0 | $0 (self-employment income never goes here) |
| Step 4(c) | $0 | $513/check (Patricia) |
| Quarterly 1040-ES | $0 | $0 (covered via W-4) |
| Projected April result | −$14,428 + penalty | +$90 refund |

## Key Takeaways

- An MFJ household with kids + a side gig needs: Step 2 for the second job, Step 3 on one W-4 only, and the self-employment amount in Step 4(c) (or 1040-ES), never in Step 4(a)
- The form's default route for self-employment income is the Estimator; a paper build uses the Multiple Jobs Worksheet for wages plus a with/without projection for the side income
- Self-employment tax (15.3% of 92.35% of profit) is separate from income tax and must be covered too
- Two paths for the side gig: Step 4(c) OR quarterly Form 1040-ES — present both and let the user choose
- Recheck with the Estimator during the year and again in early January; submit a new W-4 if the Etsy profit changes materially
