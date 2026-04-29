# Throwback Rules and the Form 3520 Default Method

When a US beneficiary receives a distribution from a **foreign non-grantor
trust**, the throwback rules of IRC §§665-668 apply. The Form 3520
default method (Schedule C of Part III) is the IRS-prescribed calculation
when the trust does not provide a Foreign Nongrantor Trust Beneficiary
Statement. This reference walks the mechanics.

## Why the throwback rules exist

Foreign non-grantor trusts can accumulate income tax-free in their home
jurisdiction for years and then distribute large lumps to US
beneficiaries. Without throwback, the US beneficiary would pay tax only
on the year-of-distribution income (DNI) and the prior-year accumulations
would escape US tax entirely.

The throwback rules close this loophole by:

1. Identifying the portion of a distribution that represents accumulated
   income from prior years (UNI — Undistributed Net Income)
2. Treating that portion as if it had been distributed in the years it
   was earned ("throwing back" to those years)
3. Computing tax at the beneficiary's average tax rate over the throwback
   years
4. Adding an interest charge (IRC §668(a)) for the deferred tax

## DNI vs UNI

- **DNI (Distributable Net Income)** — current-year trust income,
  computed under IRC §643(a). Distributions up to DNI carry out
  current-year income to beneficiaries.
- **UNI (Undistributed Net Income)** — prior-years' accumulated income
  that was not distributed. Distributions in excess of current-year DNI
  carry out UNI under §665(a).

## Actual method (Beneficiary Statement provided)

If the trust provides a Foreign Nongrantor Trust Beneficiary Statement:

- The statement allocates each distribution between current-year DNI,
  UNI, and corpus (trust principal — tax-free)
- The beneficiary uses the statement's allocations directly
- UNI carryout still triggers §667 throwback tax if any, but the
  computation uses the actual years and income types

## Default method (no Beneficiary Statement)

Without a Beneficiary Statement, the default method applies. The Form
3520 instructions describe it formally; here is the working version.

### Step 1 — Determine current-year distribution

Sum all distributions received from this foreign non-grantor trust in
the current tax year. Convert to USD using the spot rate on each
distribution date (or yearly average if applied consistently). This is
the **current distribution**.

### Step 2 — Compute the average prior-year distribution

Take the **3 prior tax years** (immediately preceding the current year).
For each year:

- If the beneficiary received distributions from this trust, sum them
  (in USD)
- If they received nothing, that year contributes 0

Average = (Year 1 + Year 2 + Year 3) ÷ 3

### Step 3 — Determine the "excess distribution"

Excess = Current distribution − (1.25 × Average prior-year distribution)

If the result is ≤ 0, there is no excess distribution. Stop. The current
distribution is treated as carryout of current-year DNI (or corpus, if
the user attests to that based on facts known) and no throwback tax
applies.

If the result is > 0, the excess is treated as a deemed accumulation
distribution under IRC §665(b).

### Step 4 — Allocate the excess across throwback years

Under default method, the excess is deemed to have been distributed
**ratably over the trust's prior years**, starting with the year the
trust was created (or the year the beneficiary first became a US person,
whichever is later) up to the year before the current year.

Example: Trust created in 2010, beneficiary became US person in 2015,
current year is 2026. Throwback years are 2015-2025, 11 years. The
excess is divided by 11 and a deemed distribution is allocated to each
year.

### Step 5 — Compute the throwback tax (Form 4970)

For each throwback year:

1. Take the deemed amount allocated to that year (excess ÷ number of
   throwback years)
2. Add it to the beneficiary's actual taxable income for that year
3. Compute the increase in tax that would have resulted (in that year's
   tax law, with that year's rates and brackets)
4. Sum the per-year tax increases

This sum is the throwback tax. It's reported on **Form 4970** (Tax on
Accumulation Distribution of Trusts) and added to the current year's
Form 1040 tax.

For practical reasons, the IRS allows a **simplifying election**: instead
of recomputing year-by-year tax, use the beneficiary's **highest
marginal tax rate** in any of the 3 immediately preceding years and
multiply by the entire excess. This usually approximates the rigorous
method and avoids reconstructing prior-year tax computations.

### Step 6 — Compute the §668(a) interest charge

The interest charge approximates the time-value cost of the deferred tax.
Computed roughly as:

- Determine the "pre-distribution period" for each throwback year (years
  from the throwback year to the current distribution year)
- Apply the IRS underpayment interest rate (compounded daily) to the
  per-year tax for the pre-distribution period
- Sum the interest amounts

Form 3520 Schedule C provides a worksheet. The instructions describe a
simplified method using the average underpayment rate. The skill should
follow whichever method the form's current-year instructions present.

The interest charge is also reported on Form 1040 (typically as
"additional taxes" with reference to §668).

## Why default method usually hurts

Two structural reasons:

1. **Throwback years span the trust's life** — even if the trust
   accumulated income only in recent years, the default method allocates
   the excess across many years, including some when the beneficiary
   wasn't yet a US person. The interest charge accumulates linearly with
   age.

2. **Highest marginal rate** — the simplification uses the beneficiary's
   highest recent marginal rate, often 32-37%, applied to the entire
   excess. The actual mix of capital gains, qualified dividends, and
   ordinary income that the trust accumulated would normally yield a
   blended rate closer to 20-25%.

In practice, the default method commonly produces an effective tax rate
of **40-60%** on the excess distribution after factoring in the interest
charge. Compared to the actual method (which might tax the same
distribution at 15-25% as long-term capital gains), default is
punishing.

## Recommendation for the US beneficiary

If the user is receiving distributions from a foreign non-grantor trust:

1. **Always request a Beneficiary Statement** from the trustee for the
   current year and going forward
2. **If the trustee won't or can't provide one**, document the request
   and consider working with an international tax practitioner to
   reconstruct the trust's UNI from available records (sometimes
   possible if the trust's accountings are detailed)
3. **As a last resort**, use the default method and accept the higher
   tax. File Form 4970 with the 1040 and the Schedule C of Part III on
   Form 3520.

## Form 4970 mechanics

Form 4970 (Tax on Accumulation Distribution of Trusts) is the schedule
that converts the deemed accumulation distribution into actual tax
liability. It is **attached to Form 1040** (not Form 3520) and the tax
shown flows to Schedule 2 of Form 1040.

The §668 interest charge is also reported on Form 1040 (Schedule 2, line
17z "Other Taxes" with notation "§668 interest").

## Cross-form reconciliation

The numbers must reconcile across:

- Form 3520 Part III — describes the distribution and computes the
  excess
- Form 3520 Schedule C — default method calculation
- Form 4970 — converts excess to throwback tax
- Form 1040 Schedule 2 — picks up the throwback tax + §668 interest

If any one of these is missing, the IRS computer system flags the return
as incomplete (3520 with Schedule C but no 4970 → notice). The skill's
validation must check that all four pieces are coordinated.

## A worked numerical example

User received $300,000 from UK family non-grantor trust in 2026. No
Beneficiary Statement.

Prior 3 years of distributions from this trust to this beneficiary:
- 2023: $0
- 2024: $20,000
- 2025: $40,000

Average = ($0 + $20,000 + $40,000) ÷ 3 = $20,000

Excess = $300,000 − (1.25 × $20,000) = $300,000 − $25,000 = $275,000

If the trust was established in 2018 and beneficiary became US person in
2018 (start of throwback period), throwback years are 2018-2025 = 8
years. Excess per year = $275,000 ÷ 8 = $34,375.

Using simplified method with beneficiary's highest recent marginal rate
of 32%: throwback tax = 32% × $275,000 = $88,000.

§668 interest charge (rough): if average pre-distribution period is 4
years and average underpayment rate is 6%, interest ≈ $88,000 × 0.06 ×
4 = $21,120.

Total additional tax = $88,000 + $21,120 = $109,120 on a $300,000
distribution = effective rate of 36.4%.

If a Beneficiary Statement had been available and the distribution was
mostly long-term capital gains: tax might have been $300,000 × 20% =
$60,000, savings of $49,120.

The skill should run this comparison whenever the user is forced into
default method, so they understand the cost and the value of obtaining a
Beneficiary Statement next year.
