# Example — Patricia, MFJ, Two Kids + Etsy Side Gig

The full W-4 treatment: Step 2 (multi-job), Step 3 (dependents), and Step 4(a)/(c) (side income + extra).

## Background

- Patricia Sanchez, age 38, Senior Product Manager
  - Salary: $135,000/year, biweekly (26 checks)
- David Sanchez, age 39, high school teacher
  - Salary: $48,000/year, biweekly (26 checks)
- Married, filing MFJ
- Two children:
  - Sofia, age 7, in 2nd grade
  - Marco, age 4, in pre-K
- Patricia runs a small Etsy shop (handmade jewelry):
  - Expected 2026 net profit: $14,000
  - Patricia files Schedule C + Schedule SE
- Standard deduction (no Schedule A items above $30K MFJ standard)
- Last year: balance due of $4,800 plus underpayment penalty
- Combined household income: $135K + $48K + $14K = **$197,000**
- Below MFJ CTC phaseout threshold ($400K) ✓

## The Problem

Patricia and David's last-year W-4 setup:
- Patricia: claimed Step 3 = $4,000 (2 kids × $2,000)
- David: also claimed Step 3 = $4,000 (double-counted!)
- Neither claimed Step 2 (multi-job) → under-withheld combined wages
- Neither mentioned Etsy on Step 4(a) → no withholding for $14K side income
- No quarterly Form 1040-ES paid

Combined effect:
- Step 3 double-claim: -$4,000 of inappropriately reduced withholding
- Multi-job under-withholding: ~-$3,500
- Etsy income tax (~22%) and SE tax (15.3%) uncovered: ~$3,080 income tax + $1,978 SE tax = ~$5,058
- Penalty under IRC §6654 because they paid less than 90% of current year or 100% of prior year

Total damage at filing: **$4,800 owed + ~$300 underpayment penalty.**

## Agent Conversation Flow

**Agent:** Patricia, you owed $4,800 plus a penalty last year. There are FOUR issues with your W-4 setup:

1. **Both you and David claimed your kids on Step 3.** Only ONE spouse should — typically the higher-paying one.
2. **Neither of you completed Step 2.** With both working, multi-job withholding adjustment is needed.
3. **Etsy income wasn't on either W-4.** $14K of profit had no withholding all year.
4. **You didn't pay quarterly Form 1040-ES** to cover the Etsy SE tax (15.3% on profit).

Let's fix all four. Run the IRS Tax Withholding Estimator first, then I'll lay out the W-4 entries.

[After running Estimator]

**Patricia:** The estimator says I should claim $4,000 on Step 3, $14,000 on Step 4(a), and $92/check on Step 4(c). David's W-4 stays simple.

**Agent:** That's right. But Step 4(a) covers federal income tax on the Etsy profit. It does NOT cover SE tax (15.3% × $14K = $1,978). You have two options:

(a) Add SE tax to Step 4(c): $1,978 / 26 = $76/check. Combined Step 4(c): $92 + $76 = $168/check.

(b) Pay quarterly Form 1040-ES of ~$494 per quarter ($1,978 / 4) to cover SE tax separately. Step 4(c) stays at $92.

Both work. Option (a) is "set and forget"; option (b) preserves more cash flow and lets you adjust if Etsy income changes.

**Patricia:** Option (a) — I want to forget about it.

**Agent:** Then your final Step 4(c) is $168/check.

## Patricia's W-4 (higher-paying job, carries all credits)

```markdown
# Form W-4 — Patricia Sanchez — DRAFT for tax year 2026

## Step 1
1(a) Patricia Sanchez, 2230 Pine Ridge Drive, Denver CO 80211
1(b) SSN: XXX-XX-3456
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs or Spouse Works
Method: (a) IRS Tax Withholding Estimator
Step 2(c) box: ☐ Not checked (using estimator output)

## Step 3 — Dependents (THIS W-4 ONLY — David's is blank)
Qualifying children under 17 × $2,000 = 2 × $2,000 = $4,000
Other dependents × $500 = 0 × $500 = $0
Other credits = $0
Total — enter on Step 3: $4,000

## Step 4 — Other Adjustments
4(a) Other income (Etsy net profit, expected 2026): $14,000
4(b) Deductions: $0 (taking standard)
4(c) Extra withholding per pay period:
   - $92 (estimator multi-job recommendation)
   - + $76 (SE tax coverage: $14,000 × 0.9235 × 0.153 / 26)
   - = $168 per pay period

## Step 5
Signed: Patricia Sanchez
Date: 2026-05-01

## Pay frequency: biweekly (26)

## Estimated annual withholding effect:
   - Baseline ($135K MFJ table): ~$15,800
   - Step 3 reduction: -$4,000 (annual CTC effect)
   - Step 4(a) addition: +$3,080 (income tax on $14K Etsy)
   - Step 4(c) addition: $168 × 26 = +$4,368
   ──────────────────────────────────────
   Total federal income tax + SE tax withheld: ~$19,248

## Validation summary
- Math: $4,000 + $14,000 + $168/check checks ✓
- Sanity warnings:
  * Total household income $197K well under $400K MFJ phaseout for CTC ✓
  * Step 3 only on Patricia's W-4 (David's is blank) ✓
  * Etsy SE tax covered via Step 4(c) addition ✓
- Coordination: David's W-4 has Steps 2/3/4 all blank
- Side-gig: Self-employment tax covered via Step 4(c); no need for 1040-ES
```

## David's W-4 (lower-paying job)

```markdown
# Form W-4 — David Sanchez — DRAFT for tax year 2026

## Step 1
1(a) David Sanchez, 2230 Pine Ridge Drive, Denver CO 80211
1(b) SSN: XXX-XX-7890
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
N/A — Patricia's W-4 handles the multi-job math

## Step 3
$0 — Patricia's W-4 carries the dependent claims

## Step 4
4(a) $0
4(b) $0
4(c) $0

## Step 5
Signed: David Sanchez
Date: 2026-05-01

## Estimated annual withholding: ~$3,000 (baseline $48K MFJ table — small because most of household tax is on Patricia's W-4)
```

## Year-End (Projected)

| Component | Amount |
|-----------|--------|
| Patricia federal withholding | $19,248 (from above) |
| David federal withholding | $3,000 |
| **Total household withholding** | **$22,248** |

Expected total tax liability:
- W-2 income tax: ~$15,800 (on $183K wages, MFJ, std deduction, after $4K CTC)
- Etsy income tax (22% bracket effective): ~$3,080
- Etsy SE tax: ~$1,978
- **Total: ~$20,858**

Refund or balance due: $22,248 − $20,858 = **+$1,390 refund** (small over-withholding, acceptable buffer)

## Key Comparison: Before vs After

| Metric | Before (last year) | After (corrected W-4) |
|--------|-------------------|------------------------|
| Patricia Step 3 | $4,000 (incorrect — both spouses) | $4,000 (only this W-4) |
| David Step 3 | $4,000 (DUPLICATE) | $0 (removed) |
| Step 2 method | None (under-withheld) | (a) Estimator (Patricia $92) |
| Step 4(a) | $0 (Etsy ignored) | $14,000 |
| Step 4(c) | $0 | $168/check (Patricia) |
| Quarterly 1040-ES | $0 | $0 (covered via W-4) |
| April result | -$4,800 + penalty | +$1,390 refund |

## Key Takeaways

- High-earning MFJ household with kids + side gig requires ALL of: Step 2 multi-job, Step 3 dependents (one spouse only), Step 4(a) side income, Step 4(c) SE tax
- Both spouses claiming Step 3 dependents is the most expensive common mistake — caused $4,000 of the $4,800 shortfall
- Self-employment tax (15.3%) is separate from income tax — Step 4(a) does NOT cover it
- Two paths for SE tax: bake into Step 4(c) OR pay quarterly Form 1040-ES — both valid
- Re-run the Estimator each October to confirm Etsy income projection against actual YTD numbers; adjust Step 4(c) if needed
