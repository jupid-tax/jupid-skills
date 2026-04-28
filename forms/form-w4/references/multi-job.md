# Step 2 — Multi-Job Methods Reference

The biggest source of W-4 mistakes is multi-job households. Either employee has 2+ jobs, or both spouses work in MFJ. Each employer's withholding table assumes their salary is the worker's only income — so combined household income is taxed in higher brackets the W-4 doesn't see.

This reference covers the three Step 2 methods in detail.

## Why Step 2 Exists

Withholding tables in Pub 15-T are built per-employer, not per-household. Two simple examples:

**Example A — Single person with two jobs:**
- Job 1: $40,000/year
- Job 2: $30,000/year
- Combined: $70,000/year

Without Step 2, Job 1 withholds as if $40K is the worker's only income (about $3,160 federal tax). Job 2 withholds as if $30K is only income (about $1,876). Total withheld: $5,036.

Actual 2025 federal tax on $70K (single, std deduction): about $7,156.

Under-withholding: $2,120 → tax bill plus possible underpayment penalty.

**Example B — MFJ both spouses work:**
- Marcus: $95,000
- Jenna: $68,000
- Combined: $163,000

Without Step 2, Marcus's employer withholds for $95K MFJ (about $8,200). Jenna's for $68K MFJ (about $4,200). Total: $12,400.

Actual 2025 federal tax on $163K (MFJ, std deduction): about $15,800.

Under-withholding: $3,400.

---

## Method (a): IRS Tax Withholding Estimator

**URL:** https://www.irs.gov/individuals/tax-withholding-estimator

**When to use:** Always recommend first. Most precise method. Works for any combination of jobs, side income, and life events.

**What you need:**
- Most recent pay stub from each job (showing YTD wages and YTD federal withholding)
- Spouse's most recent pay stub if MFJ
- Estimate of any other income (side gig, interest, dividends, etc.)
- Filing status, dependent count
- Last year's tax return for reference (optional)

**How it works:**

The estimator walks through:
1. Current pay stub data → YTD wages, YTD federal withholding, expected total annual wages
2. Other income → other adjustments
3. Dependents → CTC and ODC computation
4. Standard vs itemized deduction
5. Final calculation: projected total tax minus expected total withholding = under/over by $X

**Output:**

The estimator gives you exact numbers to enter on your W-4:
- Step 3 dependent total
- Step 4(a) other income amount
- Step 4(c) extra per-pay-period withholding

It also tells you which spouse's W-4 to update (or both) and which pay periods remain in the year.

**Limitations:**
- Doesn't model state withholding (state forms are separate)
- Treats bonuses approximately — if a big bonus is coming, redo the estimator after the bonus hits
- Doesn't handle very large equity compensation cleanly — talk to a CPA for IPO/RSU vest situations

---

## Method (b): Multiple Jobs Worksheet

**Location:** Page 3 of Form W-4 (PDF)

**When to use:** When the user can't or doesn't want to use the online estimator. Less precise but doesn't require internet.

**The worksheet has 3 tables:**

1. **Married Filing Jointly or Qualifying Surviving Spouse** — top half of Page 3
2. **Single or Married Filing Separately** — middle of Page 3
3. **Head of Household** — bottom of Page 3

Each table is a 2D matrix:
- Rows: higher-paying job's annual wages
- Columns: lower-paying job's annual wages
- Cell value: additional annual federal withholding needed on the higher-paying job's W-4

**Step-by-step:**

1. Identify the household's two highest-paying jobs (if 3+ jobs, see special instructions on Page 3)
2. Round each to the nearest $1,000
3. Look up the row/column intersection in the right table for filing status
4. Take that cell value (annual amount)
5. Divide by the number of pay periods remaining in the year on the higher-paying job
6. Enter the result on Step 4(c) of the higher-paying job's W-4
7. Submit a W-4 with only Steps 1 and 5 to the lower-paying employer

**Example (MFJ table excerpt):**

```
                    Lower-paying job annual wages
Higher-paying      |  0-9,999  | 10K-19K  | 20K-29K  | 30K-39K  | 40K-49K  |
─────────────────────────────────────────────────────────────────────────────
$60,001 - $70,000  |   $890    |  $2,470  |  $3,690  |  $4,690  |  $5,690  |
$70,001 - $80,000  |   $890    |  $2,470  |  $3,690  |  $4,690  |  $5,690  |
$80,001 - $100,000 |   $890    |  $2,470  |  $3,690  |  $4,690  |  $5,690  |
```

(Real Page 3 table is much larger; these numbers are illustrative.)

For Marcus & Jenna ($95K + $68K, MFJ): row "$80,001-$100,000", column "$60K-$70K range" (estimated extension) ≈ $7,610. Divided by 26 biweekly = $293/check.

**Limitations:**
- The brackets in the table are coarser than real tax brackets, so it tends to over-withhold by $200-$800
- Doesn't account for already-withheld YTD amounts (the Estimator does)
- Doesn't handle 3-job households as cleanly

---

## Method (c): Step 2(c) Checkbox

**Location:** Step 2(c) of the W-4 itself

**When to use:** Only when:
- Exactly two jobs total in the household
- Both jobs pay roughly the same (within ~10%)
- User wants the simplest possible setup

**How it works:**

Each spouse checks the Step 2(c) box on their own W-4. The IRS instructs employers to apply a special "two-jobs-similar-pay" withholding rate that approximates the joint-bracket math.

**Math behind the scenes:**

When 2(c) is checked, the employer's payroll software uses a different table in Pub 15-T (the "Step 2 Multiple Jobs" version) which is calibrated for two earners with similar pay.

**Tradeoffs:**

- ✅ Simplest — just check a box
- ✅ No online tool, no worksheet
- ❌ Tends to over-withhold by $500-$1,500 for unequal pay (because it assumes equal pay)
- ❌ Doesn't account for dependents claimed on Step 3 nor side income on Step 4(a)
- ❌ Both spouses must check it; if only one does, the other still under-withholds

**Decision rule for 2(c):**

```
Higher-job wages / Lower-job wages

≤ 1.10  →  2(c) is reasonable
1.10 - 1.25  →  2(c) over-withholds slightly; OK if user wants simplicity
1.25 - 1.50  →  Use method (a) or (b) instead
> 1.50  →  Definitely use method (a) Estimator
```

---

## Special Cases

### Three or more jobs

The Multiple Jobs Worksheet has additional instructions on Page 3 for 3-job households:
1. Identify highest, second-highest, and third-highest paying jobs
2. Compute combined wages of jobs 2 and 3
3. Use the Worksheet treating those combined wages as the "lower-paying job" amount
4. Apply result to highest-paying job's Step 4(c)

The Estimator handles 3+ jobs natively — strongly recommended over the worksheet for this case.

### Mid-year job change

If a spouse starts or stops working mid-year:
1. Re-run the Estimator with the new situation
2. Submit a new W-4 to the affected employer
3. Don't try to "make up" the under-withheld amount through Step 4(c) for the rest of the year unless the gap is small (<$1,000); large gaps are easier to fix via Form 1040-ES

### One job, very large bonus

If one job has a single large bonus (e.g., $50K signing bonus):
1. The bonus has its own withholding rules — usually 22% supplemental rate up to $1M (IRS Reg §31.3402(g)-1)
2. The Step 2 multi-job math doesn't apply — there's only one employer
3. If the 22% supplemental rate is higher than your bracket, you'll get a refund. Lower → consider extra Step 4(c) on the regular paycheck to cover the gap

### Both jobs with the same employer

Example: working part-time for two divisions of the same employer. Treat as two separate jobs for Step 2 purposes — the divisions usually have separate withholding.

### Self-employed primary income + W-2 side job

If the user's main income is self-employment (Schedule C) and they have a small W-2 side job:
- Don't use Step 4(c) on the W-2 to cover all SE tax — too much
- Use Step 4(a) for the SE income and Step 4(c) for the SE tax portion
- OR pay quarterly Form 1040-ES for SE income/tax and let the W-4 only handle the W-2

---

## Coordination: One W-4 Carries the Credits

The single most important multi-job rule:

**Only complete Steps 3 and 4(a)/(b) on the HIGHEST-paying job's W-4.**

The lower-paying job(s) get a W-4 with only Steps 1 and 5 (just identifying info + signature). Why:

- Step 3 dependent credit is annual ($4,000 for 2 kids), not per-paycheck. If both spouses claim $4,000, withholding is reduced by $8,000 — but only $4,000 of CTC actually exists.
- Step 4(a) other income gross-up similarly is annual; double-counting under-withholds.
- Step 4(c) extra per-pay-period CAN go on either job, but the multi-job worksheet/estimator output should always go on the higher-paying job.

The sole exception: if both jobs pay equally and you're using Step 2(c) checkbox, both W-4s have only Step 1 + 2(c) + 5.
