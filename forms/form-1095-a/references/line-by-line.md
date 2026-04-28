# Form 1095-A and Form 8962 — Complete Line-by-Line Reference

This file walks every box on Form 1095-A and every line on Form 8962 with explanations, examples, edge cases, and pitfalls.

---

## Form 1095-A — Health Insurance Marketplace Statement

### Part I — Recipient Information (Lines 1–15)

#### Line 1 — Marketplace identifier
The federal Marketplace uses "1" or a state code identifying which Marketplace issued the policy. State-based exchanges use their own codes. Pre-populated; verify it's not blank.

#### Line 2 — Marketplace-assigned policy number
A unique policy ID. If the user has multiple 1095-As (e.g., switched plans mid-year), each will have a different policy number.

#### Line 3 — Policy issuer's name
The insurance company providing the qualified health plan (e.g., Blue Cross Blue Shield, Kaiser, Ambetter). Distinct from the Marketplace itself.

#### Lines 4–7 — Recipient name, SSN, DOB, mailing address
The taxpayer responsible for reconciling on Form 8962. **Critical**: SSN must match the SSN on Form 1040. If it doesn't, the Marketplace issued the form to the wrong person — request a corrected 1095-A.

#### Lines 8–13 — Spouse information
Filled if the recipient is married and the policy covers the spouse. SSN here may differ from filer's spouse on Form 1040 if there's a separation or unusual situation — verify carefully.

#### Lines 14–15 — Recipient mailing address
Used by the Marketplace for mailing. Does not need to match Form 1040 mailing address (e.g., taxpayer moved between coverage and filing).

### Part II — Covered Individuals (Lines 16+)

Each row identifies one person covered under the policy:
- Name
- SSN
- Date of birth
- Coverage start date (typically January 1 or the enrollment date)
- Coverage end date (typically December 31 or the termination date)

**For shared policy detection**: compare each Part II row's SSN against the filer's tax family. Anyone NOT on the tax return → triggers Part IV allocation on Form 8962.

**For partial-year coverage**: note start and end dates carefully. Part III will only have nonzero amounts for the months covered.

### Part III — Coverage Information (12 monthly rows)

The heart of the form. Each month has three columns:

#### Column A — Monthly enrollment premium
The full premium charged by the insurer for the plan, **before** APTC subsidy. This is what the plan would cost if no PTC applied.

For a family on a $1,200/month silver plan, Column A reads $1,200.00 in every month they had coverage.

If the user changed plans mid-year, Column A may change between months — that signals the monthly calculation is required on Form 8962.

#### Column B — Monthly second-lowest cost silver plan (SLCSP) premium
The benchmark premium the Marketplace uses to calculate PTC. This is **not** the plan the user enrolled in — it's the second-lowest-priced silver plan available in the user's coverage area for the user's family composition.

**Common error**: Column B is $0 in some months. The Marketplace failed to calculate the benchmark, often because:
- The user enrolled mid-month or mid-year
- A family member was added or removed mid-year
- The Marketplace identified the user as ineligible at one point and didn't compute SLCSP

If Column B is $0 in a month with coverage, use the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or the state Marketplace's tax tool to look up the correct SLCSP. Required inputs: zip code, coverage month, ages of covered individuals, family composition.

#### Column C — Monthly advance payment of premium tax credit (APTC)
The credit the Marketplace paid directly to the insurer on the user's behalf. The user's net out-of-pocket premium = Column A − Column C.

If the user paid no APTC (declined the advance and pays full premium, then claims PTC at year-end), Column C is $0 in every month. The user can still receive a Net PTC refund through Form 8962.

---

## Form 8962 — Premium Tax Credit

### Part I — Annual and Monthly Contribution Amount

#### Line 1 — Tax family size
Filer + spouse (if MFJ) + all dependents claimed on the return. Critical: this may differ from "covered individuals" on Form 1095-A Part II.

Example: Filer is single with one child claimed as dependent. Both are on the 1095-A. Tax family size = 2.

Example: Filer is single, has one child, but the child's other parent claims the child as dependent. The child is on the 1095-A but is NOT on the filer's tax return. Tax family size = 1. Shared policy allocation required (Part IV).

#### Line 2a — Modified AGI for taxpayer
Form 1040 Line 11 (AGI) plus:
- Tax-exempt interest (Form 1040 Line 2a)
- Excluded foreign earned income (Form 2555)
- Non-taxable Social Security benefits

For most filers without these adjustments, Modified AGI = AGI.

#### Line 2b — Dependents' modified AGI
Add the modified AGI of any dependent who was REQUIRED to file a tax return for the year. A dependent is required to file if:
- Earned income > $14,600 (2024) or
- Unearned income > $1,300 (2024) or
- Self-employment net earnings ≥ $400

Most filers' dependents don't meet the filing threshold and Line 2b = 0. But for high-earning teen children with W-2 jobs, this matters.

#### Line 3 — Household income
= Line 2a + Line 2b. The PTC is based on this number, not just the filer's AGI.

#### Line 4 — Federal Poverty Line (FPL)
Look up in Table 1 of Form 8962 instructions. Three columns:
- 48 contiguous states + DC
- Alaska
- Hawaii

For tax year 2025, use **2024 FPL** (released January 2024).
For tax year 2026, use **2025 FPL** (released January 2025).

Example: 2024 FPL for HH of 1 in 48 states = $15,060. For HH of 2 = $20,440. Each additional person adds $5,380.

#### Line 5 — Household income as percentage of FPL
= Line 3 ÷ Line 4 × 100, rounded down to the nearest whole percent.

Example: Line 3 = $42,000, Line 4 = $15,060 (HH of 1). Line 5 = 42,000 ÷ 15,060 × 100 = 278.88% → rounded down to 278%.

**This number drives the applicable figure** in Line 7.

#### Line 6 — Reserved
No entry. Skip.

#### Line 7 — Applicable Figure
From Table 2 in Form 8962 instructions, indexed by Line 5. Under ARPA/IRA-extended rules (2021–2025):
- Line 5 < 150% FPL → 0.0000
- Line 5 = 150% → 0.0000
- Line 5 = 200% → 0.0200 (2.0% of income)
- Line 5 = 250% → 0.0400 (4.0%)
- Line 5 = 300% → 0.0600 (6.0%)
- Line 5 = 400% or more → 0.0850 (8.5%)
- Linear interpolation between brackets

For 2026, verify whether ARPA/IRA expansion was extended; if it lapsed, the pre-ARPA table applies (different brackets, capped at 400% FPL).

#### Line 8a — Annual contribution amount
= Line 3 × Line 7. The amount the user is expected to contribute toward premiums; PTC fills the gap.

#### Line 8b — Monthly contribution amount
= Line 8a ÷ 12. Used in monthly calculation (Lines 12–23).

### Part II — Premium Tax Credit and Reconciliation

#### Line 9 — Allocation of policy amounts
Yes/No. "Yes" if any covered individual on Form 1095-A Part II is not on the user's tax return. "No" otherwise.

If "Yes", complete Part IV first, then return to Part II.

#### Line 10 — Annual or monthly calculation
Yes/No. "Yes" if all of these were true for all 12 months:
- (a) Same insurance plan
- (b) Same family composition
- (c) Same APTC amount
- (d) Coverage all 12 months

If "Yes" → Line 11 (annual). If "No" → Lines 12–23 (monthly).

#### Line 11 — Annual calculation
Six columns:
- (a) Annual enrollment premium = sum of Column A on 1095-A
- (b) Annual SLCSP = sum of Column B on 1095-A
- (c) Annual contribution = Line 8a
- (d) Maximum premium assistance = max(0, (b) − (c))
- (e) Annual PTC = lesser of (a) or (d)
- (f) Annual APTC = sum of Column C on 1095-A

#### Lines 12–23 — Monthly calculation
One row per month, same six columns. Each row's (a), (b), (f) come from the corresponding month on 1095-A. (c) = Line 8b for every month. (d) = max(0, (b) − (c)). (e) = lesser of (a) or (d).

#### Line 24 — Total Premium Tax Credit
= Sum of column (e) — annual or monthly. The total PTC the user qualified for.

#### Line 25 — Total APTC
= Sum of column (f) — should match annual sum of Form 1095-A Column C.

#### Line 26 — Net Premium Tax Credit
If Line 24 > Line 25: Line 26 = Line 24 − Line 25. This is a refundable credit, flows to Schedule 3 Line 9.
If Line 24 ≤ Line 25: Line 26 = 0; complete Lines 27–29.

### Part III — Repayment of Excess Advance PTC

#### Line 27 — Excess advance PTC
= Line 25 − Line 24 (only if positive). The amount of APTC the user received but didn't qualify for.

#### Line 28 — Repayment limitation
From Pub 974 Table 5, by filing status and Line 5 percentage:

| Line 5 | Single | Other |
|--------|--------|-------|
| < 200% | $375 | $750 |
| 200% to under 300% | $975 | $1,950 |
| 300% to under 400% | $1,625 | $3,250 |
| 400%+ | No cap | No cap |

(2025 figures; verify for current year.)

#### Line 29 — Excess APTC repayment
= Lesser of Line 27 or Line 28. Flows to Schedule 2 Line 1a as additional tax.

### Part IV — Allocation of Policy Amounts (Lines 30–34)

Up to four allocations across multiple sharing taxpayers. Each row:
- (a) SSN of other taxpayer
- (b) Allocation start month
- (c) Allocation stop month
- (d) Premium percentage allocation (your share)
- (e) SLCSP percentage allocation
- (f) APTC percentage allocation

Allocation percentages must total 100% across all sharing taxpayers (e.g., if you take 60% and the other party takes 40%, sum is 100%).

If no agreement is documented, default is 50/50.

### Part V — Alternative Calculation for Year of Marriage (Line 35)

Optional simplified calculation for couples who married mid-year. Formula in Pub 974 Chapter 4. Skip unless explicitly applicable.
