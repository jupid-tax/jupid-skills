# Annual vs. Monthly Calculation Method

Form 8962 Line 10 reads: "See the instructions to determine if you can use line 11 or must complete lines 12 through 23." Yes → annual method (Line 11). No → monthly method (Lines 12–23). The decision changes how the form is filled and which math runs.

## Default rule

Per the 2025 Form 8962 instructions (Line 10), check "Yes" (annual) only if **all** of the following apply for each qualified health plan anyone in the tax family was enrolled in:

1. Enrolled in the plan for all 12 months of the year (fewer than 12 months → "No")
2. The enrollment premium (Form 1095-A Part III column A) was the same every month
3. The correct applicable SLCSP premium (column B) was the same every month. If the 1095-A SLCSP may be wrong (no APTC paid, or an unreported change in circumstances such as a newborn, a family member gaining other MEC, a death, or a move), determine the correct SLCSP per Pub 974 or HealthCare.gov/Tax-Tool first

Also check "No" if Part IV was completed (instructions, Part IV). The factors below (family size changes, eligibility changes, shared policies) matter because they usually change the premium or the correct SLCSP for some months.

If any item is false, **monthly method is required**.

## Decision tree

### Did your tax family size change during the year?

- **Yes** (birth, adoption, death, marriage, divorce, dependent ceased to qualify) → **monthly**
- **No** → continue

### Did your marketplace eligibility change?

- **Yes** (turned 65 / Medicare enrollment, started a job with affordable employer coverage offered, became eligible for Medicaid mid-year) → **monthly**
- **No** → continue

### Was the policy shared between two tax families during any month?

- **Yes** (divorced parents, adult dependent on parents' policy who files independently) → **monthly** (and Part IV)
- **No** → continue

### Did the SLCSP change month-to-month?

- **Yes** (rare; usually only if covered persons changed mid-year) → **monthly**
- **No** → continue

### Did you have marketplace coverage for fewer than 12 months?

- **Yes** (started or ended coverage mid-year) → **monthly** (months without coverage have all-zero rows)
- **No** → continue

### → All checks passed → **annual method (Line 11)**

## When monthly is required, the computation

Form 8962 Lines 12–23 each represent one calendar month. For each month:

| Column | Source / computation |
|--------|----------------------|
| (a) Premium | Form 1095-A Column A for that month |
| (b) Applicable SLCSP | Form 1095-A Column B for that month |
| (c) Monthly contribution | Line 8b (Line 8a / 12) |
| (d) Maximum premium assistance | max(0, Column b − Column c) |
| (e) Premium Tax Credit allowed | min(Column a, Column d) |
| (f) Advance Premium Tax Credit | Form 1095-A Column C for that month |

For months without coverage, leave the row blank (if columns (a) and (b) are blank, leave column (c) blank; 2025 instructions, Lines 12 Through 23, Column (c)).

Sum Column E across all 12 rows to get Line 24 (Total PTC). Sum Column F to get Line 25 (Total APTC).

## Worked decision examples

### Example A: Single freelancer, full-year same coverage

- Family size 1 all 12 months
- Same marketplace policy Jan–Dec
- Same SLCSP all 12 months
- No employer coverage, no Medicare, no Medicaid

→ **Annual method**. Line 11 sums all 12 months into a single row.

### Example B: Couple married July 15

- Each spouse had own marketplace coverage Jan–June
- Both on combined marketplace policy July–Dec
- Family size changed at marriage (now MFJ filing)

→ **Monthly method**. Pre-marriage months use individual SLCSP; post-marriage months use combined-policy SLCSP. Also consider Part V (alternative calculation for year of marriage) for more favorable computation.

### Example C: Filer turned 65 on August 12

- Marketplace coverage Jan 1 – August 11 (8.4 months coverage)
- Medicare eligibility started August 1 (the entire month of August is Medicare-eligible per §36B(c)(2)(B) "look-back" — actually disqualifies for August)

→ **Monthly method**. Months Jan–July have full coverage and PTC eligibility. August on, no marketplace PTC because filer is Medicare-eligible. Form 1095-A may show August premium and APTC if the marketplace didn't terminate coverage; Form 8962 reconciliation will show those August amounts on Line 12-23 with appropriate handling per Pub 974.

### Example D: Divorced parents share children's policy

- Parent A files single, claims child as dependent
- Parent B files single, no dependent
- Both parents and child are on a single marketplace policy
- Both parents share APTC

→ **Monthly method + Part IV allocation**. Each parent files Form 8962 with allocation percentages summing to 100% across the two tax families. See [`allocation.md`](./allocation.md).

### Example E: Birth of child on March 22

- Family size: 2 in Jan and Feb; 3 starting March
- Same marketplace policy all year (added baby to the policy)
- SLCSP changed when baby was added

→ **Monthly method**. Pre-birth months use family-of-2 contribution amount and pre-birth SLCSP. Post-birth months use family-of-3 contribution amount and post-birth SLCSP.

## Why this matters

The annual method is simpler but loses information when months differ. The monthly method preserves month-by-month accuracy and is required when:

- The filer's tax situation isn't uniform across the year
- The IRS would otherwise overcredit or undercredit the filer

Using the wrong method (annual when monthly is required) can cause:

- IRS reject of e-filed return with notice that monthly method must be used
- Audit notice if math doesn't reconcile against 1095-A monthly amounts
- Wrong PTC amount and incorrect routing to Schedule 2 or 3

## Pointer

The agent should always verify by walking through the decision tree with the filer rather than defaulting to annual. The questions are short and the answers determine the entire shape of the form.
