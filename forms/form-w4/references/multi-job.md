# Step 2 — Multi-Job Methods Reference

The biggest source of W-4 mistakes is multi-job households. Either employee has 2+ jobs, or both spouses work in MFJ. Each employer's withholding assumes its wages are the worker's only wages — so combined household income is taxed in higher brackets the W-4 doesn't see.

This reference covers the three Step 2 methods on the **2026 Form W-4** (verified 2026-10-06; re-check the 2027 form at https://www.irs.gov/forms-pubs/about-form-w-4).

## Why Step 2 Exists

Withholding in Pub. 15-T (2026) is computed per job. Without the Step 2 box checked, each job's computation subtracts a full-year amount ($8,600 Single/HoH, $12,900 MFJ, Worksheet 1A line 1g) and starts the STANDARD rate schedule from the bottom bracket. Two examples (annual figures from the Pub. 15-T (2026) Annual Percentage Method; tax from the 2026 rate schedules in Rev. Proc. 2025-32 with the 2026 standard deduction; computed in python):

**Example A — Single person with two jobs:**
- Job 1: $40,000/year
- Job 2: $30,000/year
- Combined: $70,000/year

Without Step 2, Job 1 withholds as if $40,000 is the worker's only income ($2,620 federal income tax). Job 2 withholds as if $30,000 is the only income ($1,420). Total withheld: $4,040.

2026 federal tax on $70,000 (single, $16,100 standard deduction, taxable $53,900): $6,570.

Under-withholding: $2,530 → tax bill plus possible underpayment penalty.

**Example B — MFJ both spouses work:**
- Marcus: $95,000
- Jenna: $68,000
- Combined: $163,000

Without Step 2, Marcus's employer withholds for $95,000 MFJ ($7,040). Jenna's for $68,000 MFJ ($3,800). Total: $10,840.

2026 federal tax on $163,000 (MFJ, $32,200 standard deduction, taxable $130,800): $18,200.

Under-withholding: $7,360.

---

## Method (a): IRS Tax Withholding Estimator

**URL:** www.irs.gov/W4App (landing page https://www.irs.gov/individuals/tax-withholding-estimator)

**When to use:** The form calls it the most accurate option and says to use it if you or your spouse have self-employment income. Also the form's choice when the W-4 is completed after the start of the year, for part-year work, and for changes during the year (2026 Form W-4, page 1 TIP and page 2).

**What you need:**
- Most recent pay stub from each job (showing YTD wages and YTD federal withholding)
- Spouse's most recent pay stub if MFJ
- Estimate of any other income (self-employment, interest, dividends, etc.)
- Filing status, dependent count
- Last year's tax return for reference (optional)

**Output:** the entries for the W-4, including the extra per-pay-period amount for Step 4(c).

**Limitations (agent-facing):**
- Doesn't model state withholding (state forms are separate)
- A mid-year W-4 based on the Estimator can be wrong once the next calendar year starts; Pub. 15 (2026), section 9 tells employers to remind such employees to rerun it in early January
- Large equity compensation or bonuses: rerun after the payment; supplemental wages have their own withholding rules (Pub. 15 (2026), section 7)

---

## Method (b): Multiple Jobs Worksheet

**Location:** the worksheet is on page 3 of Form W-4; the tables are on page 5.

**When to use:** When the user can't or doesn't want to use the online estimator.

**The page 5 tables, in order:**

1. **Married Filing Jointly or Qualifying Surviving Spouse**
2. **Single or Married Filing Separately**
3. **Head of Household**

Each table is a 2D matrix:
- Rows: "Higher Paying Job Annual Taxable Wage & Salary"
- Columns: "Lower Paying Job Annual Taxable Wage & Salary", $10,000 bands from $0–9,999 to $110,000–120,000
- Cell value: additional annual withholding for the household

**Step-by-step (worksheet lines):**

1. Line 1 (two jobs): find the cell at the higher-paying job's row and the lower-paying job's column; skip to line 3
2. Line 2 (three jobs): 2a = cell for the highest job (row) and the next-highest job (column); 2b = cell for the sum of the two highest jobs (row) and the third job (column); 2c = 2a + 2b
3. Line 3: pay periods per year for the highest-paying job (52, 26, 24, 12…)
4. Line 4: line 1 (or 2c) ÷ line 3
5. Enter line 4 (plus any other extra amount) in Step 4(c) of the highest-paying job's W-4
6. The other job(s) get a W-4 with Steps 2 through 4(b) blank

**2026 MFJ table excerpt (page 5):**

```
                     Lower Paying Job Annual Taxable Wage & Salary
Higher Paying Job    |  $0-9,999 | 10,000-19,999 | 20,000-29,999 | 30,000-39,999 | 40,000-49,999 | 50,000-59,999 | 60,000-69,999 |
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
$60,000 - 69,999     |   $1,020  |    2,220      |    3,420      |    3,990      |    4,190      |    4,360      |    4,760      |
$70,000 - 79,999     |   $1,020  |    2,220      |    3,420      |    3,990      |    4,190      |    4,760      |    5,760      |
$80,000 - 99,999     |   $1,020  |    2,220      |    3,420      |    4,240      |    5,440      |    6,610      |    7,610      |
$100,000 - 149,999   |   $1,870  |    4,070      |    6,270      |    7,840      |    9,040      |   10,210      |   11,210      |
```

For Marcus & Jenna ($95,000 + $68,000, MFJ): row "$80,000 - 99,999", column "$60,000 - 69,999" = $7,610. Divided by 26 biweekly = $292.69 → $293/check.

**Limitations:**
- Bands are $10,000 wide, so the result is approximate (Example B: table $7,610 vs a computed gap of $7,360)
- The worksheet works on full-year amounts; it doesn't account for withholding already taken this year (the Estimator does)
- If more than one job has annual wages over $120,000 or there are more than three jobs, the form sends the user to Pub. 505 or the Estimator

---

## Method (c): Step 2(c) Checkbox

**Location:** Step 2(c) of the W-4 itself

**When to use:** Only when there are exactly two jobs in the household. The box must be checked on the W-4 for both jobs.

**How it works:**

"If the box is checked, the standard deduction and tax brackets will be cut in half for each job to calculate withholding" (2026 Form W-4, page 2). Payroll uses the Pub. 15-T "Form W-4, Step 2, Checkbox, Withholding Rate Schedules" and skips the Worksheet 1A line 1g subtraction.

**Accuracy rule (form text):** "This option is generally more accurate than Step 2(b) if pay at the lower paying job is more than half of the pay at the higher paying job. Otherwise, Step 2(b) is more accurate." With unequal pay, more tax than necessary is withheld, and the extra grows with the pay difference.

**Tradeoffs:**

- ✅ Simplest — check a box on each W-4
- ✅ No online tool, no worksheet
- ❌ Over-withholds when one job pays much more than the other
- ❌ Both W-4s must check it; if only one does, the household under-withholds
- Steps 3 through 4(b) still go on only one of the two W-4s

**Decision rule for 2(c):**

```
Lower-job wages > 50% of higher-job wages  →  2(c) generally more accurate than 2(b)
Lower-job wages ≤ 50% of higher-job wages  →  2(b) more accurate; (a) most accurate
Self-employment income in the household    →  (a) Estimator (form instruction)
```

Example B under 2(c): Marcus's job withholds $12,070 and Jenna's $6,130 (Pub. 15-T (2026) checkbox schedule, MFJ), total $18,200, equal to the projected 2026 tax. $68,000 is more than half of $95,000, so the form's rule points to 2(c) here.

---

## Special Cases

### Three jobs

Use worksheet line 2 (see Method (b)): the two highest jobs first, then their combined wages as the row against the third job. The Estimator handles any number of jobs.

### Mid-year job change

If a spouse starts or stops working mid-year:
1. Re-run the Estimator with the new situation
2. Submit a new W-4 to the affected employer (within 10 days if the change reduces the withholding you're entitled to, Pub. 505 (2026), chapter 1)
3. Ask whether the user prefers to close the gap through Step 4(c) for the remaining paychecks or with a Form 1040-ES payment. For the underpayment penalty, withholding is treated as paid in equal amounts on the four installment dates unless the taxpayer elects actual dates (Pub. 505 (2026), chapter 2), so late-year extra withholding still counts for the whole year

### One job, very large bonus

If one job has a single large bonus (e.g., $50K signing bonus):
1. The bonus has its own withholding rules: 22% optional flat rate, and 37% mandatory on supplemental wages above $1 million for the year (Pub. 15 (2026), section 7)
2. The Step 2 multi-job math doesn't apply — there's only one employer
3. If the 22% flat rate is higher than the user's top bracket, expect a refund; if lower, consider extra Step 4(c) on the regular paycheck to cover the gap

### Two positions with the same employer

If both positions are paid through one payroll and appear on one W-2, it is one job for W-4 purposes. If they are separate employers (separate W-2s), treat them as two jobs. Ask the user which applies.

### Self-employment income + W-2 job

If the user has self-employment income (Schedule C) and a W-2 job:
- Do NOT put the self-employment income on Step 4(a); the form says not to include it there
- Use the Estimator (Step 2(a)) and enter its result in Step 4(c), OR
- Pay quarterly Form 1040-ES for the self-employment income tax and SE tax and let the W-4 handle only the wages

---

## Coordination: One W-4 Carries the Credits

The single most important multi-job rule (2026 Form W-4, Step 2 note):

**Complete Steps 3 through 4(b) on only ONE W-4 — most accurate on the highest-paying job's.**

The other job(s) leave Steps 3 through 4(b) blank. Why:

- Step 3 dependent credit is annual ($4,400 for 2 kids in 2026), not per-paycheck. If both spouses claim $4,400, withholding is reduced by $8,800 — but only $4,400 of CTC actually exists.
- Step 4(a) other income and Step 4(b) deductions are annual too; double-counting skews withholding.
- Step 4(c) extra per-pay-period CAN go on either job; the Multiple Jobs Worksheet result goes on the highest-paying job's W-4.

With the Step 2(c) checkbox, both W-4s check the box, and Steps 3 through 4(b) still appear on only one of them.
