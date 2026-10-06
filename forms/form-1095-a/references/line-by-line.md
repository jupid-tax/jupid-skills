# Form 1095-A and Form 8962 — Complete Line-by-Line Reference

This file walks every box on Form 1095-A and every line on Form 8962 with explanations, examples, edge cases, and pitfalls. Verified against the 2025 Form 1095-A (created 6/5/25), the 2025 Instructions for Form 1095-A (Oct 8, 2025), and the 2025 Form 8962 and instructions, used for 2025 returns filed in 2026. Re-check https://www.irs.gov/forms-pubs/about-form-1095-a for the next revision.

---

## Form 1095-A — Health Insurance Marketplace Statement

### Part I — Recipient Information (Lines 1–15)

#### Line 1 — Marketplace identifier
The Marketplace state name or abbreviation: the state where the user enrolled (2025 Instructions for Form 1095-A, Line 1). Pre-populated; verify it's not blank.

#### Line 2 — Marketplace-assigned policy number
A unique policy ID (last 15 characters if longer). If the user has multiple 1095-As (e.g., switched plans mid-year), each will have a different policy number. Enter it in Form 8962 Part IV column (a) when allocating.

#### Line 3 — Policy issuer's name
The insurance company providing the qualified health plan (e.g., Blue Cross Blue Shield, Kaiser, Ambetter). Distinct from the Marketplace itself.

#### Lines 4–6 — Recipient's name, SSN, date of birth
The person identified at enrollment as the tax filer who would take the PTC (or the primary applicant if no tax filer was identified). Line 6 DOB appears only if line 5 is blank. **Critical**: the line 5 SSN must match the SSN on Form 1040. If it doesn't, the Marketplace issued the form to the wrong person — request a corrected 1095-A. The copy may show only the last four digits.

#### Lines 7–9 — Spouse's name, SSN, date of birth
Filled only if the recipient has a spouse and APTC was paid for the coverage, even if APTC was not paid for the spouse's own coverage. Line 9 DOB only if line 8 is blank. Verify against the spouse on Form 1040.

#### Lines 10–11 — Policy start and termination dates
1/1/2025 if the policy was in effect at the start of the year; 12/31/2025 if still in effect at year end.

#### Lines 12–15 — Recipient address
Street address, city, state, country and ZIP. Does not need to match the Form 1040 address (e.g., taxpayer moved between coverage and filing).

### Part II — Covered Individuals (Lines 16–20)

Each row identifies one person covered under the policy (2025 Instructions for Form 1095-A, Part II):
- Column A — Name
- Column B — SSN
- Column C — Date of birth (only if column B is blank)
- Column D — Coverage start date
- Column E — Coverage termination date (12/31/2025 if covered at year end)

More than five covered people → one or more additional Forms 1095-A continue Part II. If APTC was paid or a tax family was identified, Part II lists only people the tax filer certified would be in their tax family; other enrollees get a separate Form 1095-A.

**For shared policy detection**: compare each Part II row's SSN against the filer's tax family. Anyone NOT on the tax return → triggers Part IV allocation on Form 8962.

**For partial-year coverage**: note start and end dates carefully. Part III will only have nonzero amounts for the months covered.

### Part III — Coverage Information (Lines 21–33)

The heart of the form. Lines 21–32 are January–December; line 33 is the annual totals. Each month has three columns:

#### Column A — Monthly enrollment premium
The full premium charged by the insurer for the plan, **before** APTC subsidy, limited to essential health benefits (plus the pediatric dental part of a stand-alone dental plan). Months whose premiums were not paid show -0- unless the first month of a grace period or a similar listed case applies.

For a family on a $1,200/month silver plan, Column A reads $1,200.00 in every month they had coverage.

If the user changed plans mid-year, Column A may change between months — that signals the monthly calculation is required on Form 8962.

#### Column B — Monthly second-lowest cost silver plan (SLCSP) premium
The benchmark premium the Marketplace uses to calculate PTC. This is **not** the plan the user enrolled in — it's the second-lowest-priced silver plan available in the user's coverage area for the user's family composition.

**Column B is $0 or blank in some months.** First check whether -0- is correct: the Marketplace enters -0- when every covered person enrolled after the first day of the month (unless coverage started on the date of birth, adoption, foster placement, or a court order), or when premiums for the month were not paid outside the listed grace-period cases. Column B is left blank when no financial assistance was requested and the Marketplace offers a lookup tool (2025 Instructions for Form 1095-A, Part III, column B). Other causes:
- A family member was added or removed mid-year
- The Marketplace identified the user as ineligible at one point and didn't compute SLCSP

If Column B is $0 or blank in a month that qualifies for PTC, use the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or the state Marketplace's tax tool to look up the correct SLCSP. Required inputs: zip code, coverage month, ages of covered individuals, family composition.

#### Column C — Monthly advance payment of premium tax credit (APTC)
The credit the Marketplace paid directly to the insurer on the user's behalf. The user's net out-of-pocket premium = Column A − Column C.

If the user paid no APTC (declined the advance and pays full premium, then claims PTC at year-end), Column C is blank in every month. The user can still receive a Net PTC refund through Form 8962.

If Column C is the only nonzero column for a month, the policy was terminated for nonpayment: no PTC for that month, but the APTC must still be reconciled (2025 Form 1095-A, Instructions for Recipient).

---

## Form 8962 — Premium Tax Credit

### Part I — Annual and Monthly Contribution Amount

#### Line 1 — Tax family size
Filer + spouse (if MFJ) + all dependents claimed on the return, whether or not they were on the policy. Critical: this may differ from "covered individuals" on Form 1095-A Part II.

Example: Filer is single with one child claimed as dependent. Both are on the 1095-A. Tax family size = 2.

Example: Filer is single, has one child, but the child's other parent claims the child as dependent. The child is on the 1095-A but is NOT on the filer's tax return. Tax family size = 1. Shared policy allocation required (Part IV).

#### Line 2a — Modified AGI for taxpayer
Form 1040 Line 11a (AGI) plus (2025 Form 8962 instructions, Worksheet 1-1):
- Tax-exempt interest (Form 1040 Line 2a)
- Excluded foreign earned income and housing (Form 2555, lines 45 and 50)
- Non-taxable Social Security benefits (Form 1040 line 6a minus 6b)

For most filers without these adjustments, Modified AGI = AGI.

#### Line 2b — Dependents' modified AGI
Add the modified AGI of any dependent who was REQUIRED to file a tax return for the year (not one filing only to get a refund of withholding). For 2025 a single dependent is generally required to file if (2025 Form 1040 instructions, Chart B):
- Earned income > $15,750, or
- Unearned income > $1,350, or
- Gross income > the larger of $1,350 or earned income (up to $15,300) plus $450, or
- Self-employment net earnings ≥ $400

Most filers' dependents don't meet the filing threshold and Line 2b = 0. But for high-earning teen children with W-2 jobs, this matters.

#### Line 3 — Household income
= Line 2a + Line 2b. The PTC is based on this number, not just the filer's AGI.

#### Line 4 — Federal Poverty Line (FPL)
Look up in Tables 1-1 (Alaska), 1-2 (Hawaii), and 1-3 (other 48 states and DC) of the Form 8962 instructions and check box a, b, or c.

For tax year 2025, use **2024 FPL** (HHS guidelines published January 2024).
For tax year 2026, use **2025 FPL** (HHS guidelines published January 2025).

Example: 2024 FPL for HH of 1 in 48 states = $15,060. For HH of 2 = $20,440. Each additional person adds $5,380.

#### Line 5 — Household income as percentage of FPL
= Line 3 ÷ Line 4 × 100, dropping any digits after the decimal point. Above 400%: enter 401 (2025 instructions, Worksheet 2).

Example: Line 3 = $42,000, Line 4 = $15,060 (HH of 1). Line 5 = 42,000 ÷ 15,060 × 100 = 278.88% → 278%.

**This number drives the applicable figure** in Line 7.

#### Line 6 — Reserved for future use
No entry. Skip.

#### Line 7 — Applicable Figure
From Table 2 in Form 8962 instructions, indexed by Line 5. Under ARPA/IRA-extended rules (2021–2025; 2025 Table 2, Rev. Proc. 2024-35):
- Line 5 ≤ 150% FPL → 0.0000
- Line 5 = 200% → 0.0200 (2.0% of income)
- Line 5 = 250% → 0.0400 (4.0%)
- Line 5 = 300% → 0.0600 (6.0%)
- Line 5 = 400% or more (401) → 0.0850 (8.5%)
- Linear between those points; use the Table 2 value for the exact whole percent (e.g., 278 → 0.0512)

For 2026 the expansion expired: Rev. Proc. 2025-25 sets 2.10% below 133%, 3.14%–4.19% for 133–150%, 4.19%–6.60% for 150–200%, 6.60%–8.44% for 200–250%, 8.44%–9.96% for 250–300%, and 9.96% for 300–400%; above 400% FPL there is no PTC.

#### Line 8a — Annual contribution amount
= Line 3 × Line 7, rounded to the nearest whole dollar. The amount the user is expected to contribute toward premiums; PTC fills the gap.

#### Line 8b — Monthly contribution amount
= Line 8a ÷ 12, rounded to the nearest whole dollar. Used in monthly calculation (Lines 12–23).

### Part II — Premium Tax Credit and Reconciliation

#### Line 9 — Allocation of policy amounts or year-of-marriage election
Yes/No. "Yes" if (1) the policy covered at least one individual in the user's tax family and at least one in another tax family, and (2) the user's 1095-A lists someone not in their tax family or omits a member of it, or the other family's 1095-A includes a member of the user's tax family; also "Yes" to elect the alternative calculation for year of marriage (2025 Form 8962 instructions, Line 9). "No" otherwise.

If "Yes", complete Part IV and/or Part V first, then return to Part II.

#### Line 10 — Annual or monthly calculation
"Yes" only if, for every policy covering the tax family, enrollment covered all 12 months, the enrollment premium (Column A) was the same every month, and the applicable SLCSP premium (Column B) was the same every month (2025 Form 8962 instructions, Line 10). Completing Part IV forces "No".

If "Yes" → Line 11 (annual). If "No" → Lines 12–23 (monthly). A change in APTC alone does not force "No".

#### Line 11 — Annual calculation
Six columns:
- (a) Annual enrollment premium = 1095-A line 33, Column A
- (b) Annual SLCSP = 1095-A line 33, Column B
- (c) Annual contribution = Line 8a
- (d) Maximum premium assistance = max(0, (b) − (c))
- (e) Annual PTC = lesser of (a) or (d)
- (f) Annual APTC = 1095-A line 33, Column C

#### Lines 12–23 — Monthly calculation
One row per month, same six columns. Each row's (a), (b), (f) come from the corresponding month on 1095-A (lines 21–32), multiplied by the Part IV percentages if allocating. (c) = Line 8b for every month. (d) = max(0, (b) − (c)). (e) = lesser of (a) or (d). Months without coverage are left blank.

#### Line 24 — Total Premium Tax Credit
= Sum of column (e) — annual or monthly. The total PTC the user qualified for.

#### Line 25 — Total APTC
= Sum of column (f) — should match annual sum of Form 1095-A Column C.

#### Line 26 — Net Premium Tax Credit
If Line 24 > Line 25: Line 26 = Line 24 − Line 25. This is a refundable credit, flows to Schedule 3 Line 9.
If Line 24 = Line 25: Line 26 = -0-; stop.
If Line 24 < Line 25: leave Line 26 blank; complete Lines 27–29.

### Part III — Repayment of Excess Advance PTC

#### Line 27 — Excess advance PTC
= Line 25 − Line 24 (only if positive). The amount of APTC the user received but didn't qualify for.

#### Line 28 — Repayment limitation
From Table 5 of the 2025 Form 8962 instructions, by filing status and Line 5 percentage:

| Line 5 | Single | Any other filing status |
|--------|--------|-------|
| Less than 200 | $375 | $750 |
| At least 200 but less than 300 | $975 | $1,950 |
| At least 300 but less than 400 | $1,625 | $3,250 |
| 400 or more | Leave blank (no limit) | Leave blank (no limit) |

For tax years beginning after December 31, 2025 there is no limitation at any income (P.L. 119-21 §71305; IRS FS-2025-10, Q31).

#### Line 29 — Excess APTC repayment
= Lesser of Line 27 or Line 28 (Line 27 if Line 28 is blank). Flows to Schedule 2 Line 1a as additional tax.

### Part IV — Allocation of Policy Amounts (Lines 30–34)

Up to four allocations (Lines 30–33) across multiple sharing taxpayers. Each row:
- (a) Policy number (Form 1095-A line 2)
- (b) SSN of other taxpayer
- (c) Allocation start month
- (d) Allocation stop month
- (e) Premium percentage allocation (your share, as a decimal such as "0.60")
- (f) SLCSP percentage allocation
- (g) APTC percentage allocation

Allocation percentages must total 100% across all sharing taxpayers (e.g., if you take 0.60 and the other party takes 0.40, sum is 100%). Line 34 asks whether all allocations are complete.

If there is no agreement, the default depends on the situation (2025 Form 8962 instructions, Allocation Situations 1–4): 50/50 for spouses who divorced or legally separated during the year; for any other shared policy, the number of individuals enrolled by one taxpayer who are in the other taxpayer's tax family divided by the total enrolled.

### Part V — Alternative Calculation for Year of Marriage (Lines 35–36)

Optional election for couples who married during the year (Table 4 eligibility, Worksheet 3, Pub 974 Worksheets I–V). It can only reduce excess APTC. Skip unless explicitly applicable; see the [`form-8962`](../../form-8962/SKILL.md) skill.
