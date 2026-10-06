---
name: form-8962
description: >
  Use this skill when an individual filer needs to compute the Premium Tax
  Credit (PTC) on IRS Form 8962 and reconcile any advance Premium Tax
  Credit (APTC) received during the year. Triggers on phrases like
  "Form 8962", "Premium Tax Credit", "PTC", "reconcile health insurance
  subsidy", "advance premium tax credit", "owe back marketplace credit",
  "marketplace health insurance tax filing", "1095-A on tax return",
  "ACA tax credit", "healthcare.gov tax form". Required if the filer
  received APTC during the year OR wants to claim PTC at filing time
  for marketplace coverage. Do NOT use for: employer-sponsored health
  insurance (no PTC eligibility); Medicare or Medicaid enrollees (no
  PTC eligibility); filers who only received Form 1095-B or 1095-C
  (those are informational only and require no Form 8962); the
  Premium Tax Credit *for prior tax years* if amending — same skill,
  but verify the year-specific FPL and applicable percentage tables.
form: Form 8962 (Premium Tax Credit)
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8962.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8962.pdf
---

# Form 8962 — Premium Tax Credit

This skill produces an audit-grade draft of Form 8962 from the user's Form 1095-A data, household composition, household income, and family-size facts. It applies IRC §36B and the Federal Poverty Line (FPL) tables in the Form 8962 instructions (Tables 1-1, 1-2, 1-3) to compute the Premium Tax Credit (PTC), reconcile any advance Premium Tax Credit (APTC) the filer received, and route the result to either Schedule 3 Line 9 (refundable PTC) or Schedule 2 Line 1a (excess APTC repayment). Line map verified against the 2025 Form 8962 and its instructions (dated Oct 1, 2025), filed in 2026; re-check the next revision at https://www.irs.gov/forms-pubs/about-form-8962 before use.

The math is mechanical once the inputs are correct. The judgment is in three areas: (1) which FPL table applies (prior-year HHS guidelines), (2) whether to use the annual or monthly computation method, and (3) the repayment limitation under IRC §36B(f)(2)(B) when household income ends up below 400% FPL (2025 and earlier tax years only; P.L. 119-21 §71305 removed the limitation for tax years beginning after December 31, 2025). The skill optimizes for getting these right.

**Companion guide for end users:** [Form 8962 (Premium Tax Credit) 2026: How to Reconcile Your Marketplace Subsidy](https://jupid.com/blog/form-8962-premium-tax-credit-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 8962, Premium Tax Credit, PTC, or marketplace insurance reconciliation
- The user received Form 1095-A from a Health Insurance Marketplace (federal `healthcare.gov` or a state-based marketplace)
- The user enrolled in marketplace health insurance with advance Premium Tax Credit (APTC) reducing their monthly premium
- The user paid full marketplace premiums and wants to claim PTC at filing
- The user is asking why the IRS held their refund pending a missing Form 8962

Do **not** engage this skill when:

- The user has only employer-sponsored coverage (no marketplace) — no PTC, no Form 8962
- The user has Medicare or Medicaid — generally not eligible for PTC for the same coverage period
- The user only received Form 1095-B (private insurer) or 1095-C (employer) — these are informational; no Form 8962 required
- The user is filing as MFS and was a victim of domestic abuse/spousal abandonment — they may be eligible to compute PTC under MFS using the Pub 974 special rules; engage with caution and follow Pub 974 chapter on MFS exceptions
- The user is in a state expansion of Medicaid and was eligible for Medicaid all year — no PTC even with marketplace enrollment

For the parent return, see the [`form-1040`](../form-1040/SKILL.md) skill. For routing the result to Schedule 2, see the [`schedule-2`](../schedule-2/SKILL.md) skill. For routing the result to Schedule 3, see the `schedule-3` skill (forthcoming). Form 1095-A data entry has its own dedicated [`form-1095-a`](../form-1095-a/SKILL.md) skill — invoke that first if the filer has the form but hasn't extracted the monthly column data.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The FPL table used is the **prior-year** HHS poverty guidelines (e.g., 2025 returns use 2024 FPL; 2026 returns use 2025 FPL). The applicable percentage table in IRC §36B(b)(3)(A) was modified by ARPA / IRA for tax years 2021 through 2025 only (§36B(b)(3)(A)(iii)). For 2026, Rev. Proc. 2025-25 sets the table (2.10% to 9.96%), household income above 400% FPL gets no PTC (§36B(c)(1)(A)), and excess APTC is repaid in full (P.L. 119-21 §71305). No extension of the enhanced credits had been enacted as of 2026-10-06; re-check IRS.gov/Form8962 and IRS.gov/Pub974 before computing a 2026 return.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 8962 header.
3. **Filer's tax family size**. This is the filer + spouse (if MFJ) + every dependent the filer claims on the return. Critical: the *tax* family size, not "people on the policy". A child claimed as a dependent counts whether or not on the marketplace policy.
4. **Filer's modified AGI (MAGI) for PTC**. MAGI = AGI + tax-exempt interest (§103) + non-taxable Social Security benefits + foreign earned income exclusion (§911). This requires the rest of the Form 1040 to be substantially complete before Form 8962 can finalize.
5. **Each dependent's MAGI** if they are required to file a return. Dependent's MAGI is added to filer's MAGI to produce **household income** (Form 8962 Line 2b). If a dependent is not required to file, their MAGI does not count.
6. **State of residence during the tax year**. FPL tables differ for Alaska and Hawaii. The 48 contiguous states + DC use the same table. If the filer lived in Alaska and/or Hawaii for part of the year, or spouses filing jointly lived in different states, use the table with the higher amounts (2025 Form 8962 instructions, Line 4).
7. **Form 1095-A** with all 12 months of:
   - Column A — Monthly enrollment premiums
   - Column B — Monthly second lowest cost silver plan (SLCSP)
   - Column C — Monthly APTC paid
8. **Whether the filer's circumstances changed during the year**. Specifically:
   - Did family size change (birth, adoption, marriage, divorce, dependent ceased)?
   - Did marketplace eligibility change (Medicare enrollment mid-year, Medicaid enrollment, employer coverage offer)?
   - Did the SLCSP change month-to-month?
   - Was the policy shared between two tax families (e.g., adult child on parents' policy who files independently; divorced couple sharing children's coverage)?

   If any answer is yes, **monthly method** is required; otherwise annual method is allowed.

9. **For shared-policy allocation** (if applicable), the agreed-upon allocation percentage between the tax families. This is a negotiation between filers. If they do not agree, the default depends on the allocation situation: 50/50 for spouses who divorced or legally separated during the year (Treas. Reg. §1.36B-4(b)(3)); otherwise the number of enrolled individuals in the other tax family divided by the number enrolled in the policy (Treas. Reg. §1.36B-4(a)(1)(ii)(B)(2); Form 8962 instructions, Allocation Situations 1 and 4).

For each missing input, ask before proceeding. Do not estimate FPL, MAGI, or family size.

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm Form 1095-A is in hand

Confirm the filer received Form 1095-A. If they enrolled through the marketplace but didn't receive the form, route them to the marketplace (not the IRS) for a corrected or replacement copy. Do not use 1095-B or 1095-C — those are different forms.

If multiple 1095-A forms (multiple marketplace policies during the year), each is processed separately on its own column set in Form 8962 Part II, then summed.

### Step 2 — Determine household income (Lines 1, 2a, 2b, 3)

- **Line 1**: Tax family size (count of filer + spouse + dependents)
- **Line 2a**: Filer's MAGI (and spouse's, if MFJ)
- **Line 2b**: Sum of dependent MAGIs (only those required to file)
- **Line 3**: Line 2a + Line 2b = household income

### Step 3 — Determine household income as percentage of FPL (Lines 4, 5)

- **Line 4**: Federal poverty line for the family size. Use prior-year HHS poverty guidelines and the appropriate state group (48+DC, AK, or HI). See [`references/fpl-tables.md`](./references/fpl-tables.md).
- **Line 5**: (Line 3 / Line 4) × 100, rounded down to nearest whole percent. If household income exceeds 400% FPL: enter 401 (2025 instructions, Worksheet 2). For 2025, 401 still gets an applicable figure of 0.0850; for 2026, above 400% means no PTC.

### Step 4 — Decide annual vs. monthly method

Use [`references/annual-vs-monthly.md`](./references/annual-vs-monthly.md) to decide. Line 10 = Yes (annual, Line 11) only if, for every qualified health plan anyone in the tax family was enrolled in, (a) enrollment covered all 12 months, (b) the enrollment premium (1095-A column A) was the same every month, and (c) the correct applicable SLCSP premium (column B) was the same every month (2025 Form 8962 instructions, Line 10). Otherwise Line 10 = No (monthly, Lines 12–23). Typical triggers for monthly:

- Marriage during the year
- Birth, adoption, or death changed family size
- Coverage started or ended mid-year
- Filer became eligible for non-marketplace coverage mid-year (Medicare, Medicaid, employer)
- Policy was shared between two tax families (completing Part IV forces Line 10 = No)
- Different applicable SLCSP or enrollment premium across months

For monthly method, the 12-row Part II is filled month-by-month with separate calculations. For annual, Line 11 is used and all 12 months are summed into one row.

### Step 5 — Compute applicable figure (Line 7)

The applicable figure is the percentage of household income the filer is "expected" to contribute to premiums. Sliding scale by % of FPL.

For 2025 (ARPA table as extended by IRA §12001; Rev. Proc. 2024-35; 2025 Form 8962 instructions Table 2):

| % of FPL | Applicable figure |
|----------|-------------------|
| ≤ 150% | 0.00 |
| 150% – 200% | 0.00 → 0.02 (sliding) |
| 200% – 250% | 0.02 → 0.04 (sliding) |
| 250% – 300% | 0.04 → 0.06 (sliding) |
| 300% – 400% | 0.06 → 0.085 (sliding) |
| ≥ 400% | 0.085 (IRA modification, tax years 2021–2025) |

For 2026, the enhanced credits expired (§36B(b)(3)(A)(iii) and (c)(1)(E) apply only to tax years beginning before January 1, 2026). Rev. Proc. 2025-25 sets the 2026 table: below 133% FPL 2.10%; 133–150% 3.14% → 4.19%; 150–200% 4.19% → 6.60%; 200–250% 6.60% → 8.44%; 250–300% 8.44% → 9.96%; 300–400% 9.96%. Above 400% FPL there is no PTC and all APTC is repaid with no cap (P.L. 119-21 §71305). No extension had been enacted as of 2026-10-06. Re-check IRS.gov/Form8962 before filing.

The exact interpolation formula is in IRC §36B(b)(3)(A) and reproduced in Form 8962 Instructions Table 2. See [`references/applicable-figure.md`](./references/applicable-figure.md).

### Step 6 — Compute annual contribution amount (Line 8a)

Line 8a = Line 3 (household income) × Line 7 (applicable figure), rounded to the nearest whole dollar.

For monthly method, Line 8b = Line 8a / 12, rounded to the nearest whole dollar, and is the monthly contribution.

### Step 7 — Compute Premium Tax Credit (Lines 11–23)

For each month (or for the year if annual method):

- **Column A** — Premiums (from 1095-A Column A)
- **Column B** — Annual SLCSP (from 1095-A Column B; for annual method, sum 12 months)
- **Column C** — Contribution amount (Line 8b for monthly; Line 8a for annual)
- **Column D** — Maximum premium assistance = Column B − Column C, but not less than zero
- **Column E** — Monthly PTC = lesser of Column A or Column D
- **Column F** — Monthly APTC (from 1095-A Column C)

For annual method: Line 11 in 6 columns (a-f).
For monthly method: Lines 12-23, each row is one month, same 6 columns.

### Step 8 — Total PTC and reconcile (Lines 24–29)

- **Line 24**: Total PTC = Column E total
- **Line 25**: Total APTC = Column F total (matches Form 1095-A Column C totals)

If Line 24 ≥ Line 25:

- **Line 26**: Net Premium Tax Credit = Line 24 − Line 25 (enter -0- if they are equal)
- → **Schedule 3 Line 9** (refundable credit). Skip Lines 27–29.

If Line 24 < Line 25 (leave Line 26 blank and go to Part III):

- **Line 27**: Excess APTC = Line 25 − Line 24
- **Line 28**: Repayment limitation = Form 8962 instructions Table 5 lookup based on % FPL (Line 5) and filing status. 2025 amounts: below 200% $375 single / $750 other; 200–<300% $975 / $1,950; 300–<400% $1,625 / $3,250; 400 or more, leave Line 28 blank (no limit). For tax years beginning after December 31, 2025 there is no limitation at any income (P.L. 119-21 §71305; IRS FS-2025-10, Q31).
- **Line 29**: Excess APTC repayment = lesser of Line 27 or Line 28 (Line 27 if Line 28 is blank)
- → **Schedule 2 Line 1a** (additional tax owed).

### Step 9 — Allocation if shared policy (Part IV)

If the policy was shared between two tax families, complete Part IV. See [`references/allocation.md`](./references/allocation.md) for divorced parents, adult dependents on parental policies, and other shared-policy scenarios. The percentages must sum to 100% across all tax families on the policy.

### Step 10 — Alternative calculation for year of marriage (Part V)

If the filers were both unmarried on January 1, married on December 31, file jointly, someone in the tax family was enrolled before the first full month of marriage, and excess APTC was paid (Table 4 and Worksheet 3 in the instructions), Part V (Lines 35–36) may reduce the excess APTC repayment. It never increases the net PTC. See [`references/year-of-marriage.md`](./references/year-of-marriage.md).

### Step 11 — Run validation checks

See **Validation** below.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next action items:

- **If Line 26 > 0** → transcribe to **Schedule 3 Line 9** (Net Premium Tax Credit, refundable)
- **If Line 29 > 0** → transcribe to **Schedule 2 Line 1a** (Excess APTC repayment)
- **Form 8962 must be attached** to the return either way
- **Form 1095-A must be retained** in the filer's records (not attached to the return)
- If the filer was MFS and is claiming the domestic-abuse / spousal-abandonment exception, check the box on line A of Form 8962. Do not attach documentation of the abuse or abandonment; keep it with the filer's records (2025 Form 8962 instructions, Victims of domestic abuse or spousal abandonment)

### Step 14 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md). Form 8962 cannot be filed alone; it attaches to Form 1040.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name** — Filer's legal name as on Form 1040
- **SSN** — Filer's SSN or ITIN
- **Line A** — Check only if filing MFS under the domestic-abuse / spousal-abandonment exception

### Part I — Annual and Monthly Contribution Amount (Lines 1–8b)

- **Line 1** — Tax family size
- **Line 2a** — Filer (and spouse) MAGI
- **Line 2b** — Dependents' MAGI total
- **Line 3** — Household income
- **Line 4** — FPL for tax family size (prior-year HHS table); check box a (Alaska), b (Hawaii), or c (other 48 states and DC)
- **Line 5** — Household income as % of FPL
- **Line 6** — Reserved for future use (2025 form)
- **Line 7** — Applicable figure
- **Line 8a** — Annual contribution amount = Line 3 × Line 7, rounded to whole dollars
- **Line 8b** — Monthly contribution amount = Line 8a / 12, rounded to whole dollars

### Part II — Premium Tax Credit Claim and Reconciliation of APTC (Lines 9–26)

- **Line 9** — Allocating policy amounts with another taxpayer, or electing the alternative calculation for year of marriage? Yes → Part IV and/or Part V first
- **Line 10** — Yes = annual (Line 11); No = monthly (Lines 12–23)
- **Line 11** — Annual calculation (one row, columns a-f) — used if Line 10 = Yes
- **Lines 12–23** — Monthly calculation (12 rows for January–December, columns a-f) — used if Line 10 = No
- **Line 24** — Total Premium Tax Credit (Column E total)
- **Line 25** — Total APTC (Column F total)
- **Line 26** — Net Premium Tax Credit (if Line 24 > Line 25; -0- if equal)

### Part III — Repayment of Excess Advance Payment of the PTC (Lines 27–29)

- **Line 27** — Excess APTC (if Line 25 > Line 24)
- **Line 28** — Repayment limitation (Table 5; blank if Line 5 is 400 or more; no limitation for tax years after 2025)
- **Line 29** — Excess APTC repayment → Schedule 2 Line 1a

### Part IV — Allocation of Policy Amounts

For shared policies. Lines 30–33 (one row per allocation, up to four): (a) policy number, (b) SSN of other taxpayer, (c) start month, (d) stop month, (e) premium %, (f) SLCSP %, (g) APTC %. Line 34 asks whether all allocations are complete.

### Part V — Alternative Calculation for Year of Marriage

Special calculation for filers who married during the year. Lines 35 (filer) and 36 (spouse): (a) alternative family size, (b) alternative monthly contribution amount, (c) start month, (d) stop month.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 2a + Line 2b
- [ ] Line 5 = (Line 3 / Line 4) × 100, rounded down (capped at 401% if applicable)
- [ ] Line 8a = Line 3 × Line 7, rounded to the nearest whole dollar
- [ ] Line 8b = Line 8a / 12, rounded to the nearest whole dollar
- [ ] For each row, Column D = max(0, Column B − Column C)
- [ ] For each row, Column E = min(Column A, Column D)
- [ ] Line 24 = sum of Column E across all rows
- [ ] Line 25 = sum of Column F across all rows = sum of Form 1095-A Column C
- [ ] Either Line 26 > 0 OR Line 29 > 0 — not both
- [ ] If Line 26 > 0: Line 26 = Line 24 − Line 25
- [ ] If Line 29 > 0: Line 27 = Line 25 − Line 24, Line 29 = min(Line 27, Line 28)

### Input checks

- [ ] Form 1095-A monthly Column A, B, C amounts come from the actual 1095-A, not estimated
- [ ] FPL on Line 4 matches the **prior-year** HHS guidelines for the filer's state group
- [ ] Tax family size on Line 1 matches the dependents claimed on Form 1040
- [ ] MAGI on Line 2a matches AGI + tax-exempt interest + non-taxable Social Security + foreign earned income exclusion

### Sanity checks (warnings, not blockers)

- [ ] If Line 5 < 100%: filer was likely Medicaid-eligible. Verify they didn't enroll in marketplace by mistake.
- [ ] If Line 5 ≥ 400% and tax year 2021–2025: applicable figure is 0.0850 (IRA modification) and Line 28 is blank (no repayment limit).
- [ ] If Line 5 > 400% and tax year 2026: no PTC; all APTC is repaid with no cap. Confirm no extension was enacted after 2026-10-06.
- [ ] If tax year 2026 and Line 25 > Line 24: no repayment limitation applies at any income level (P.L. 119-21 §71305); Line 29 = Line 27.
- [ ] If a dependent's MAGI was excluded: confirm the dependent was *not required* to file a return (gross income test, not just "didn't file").
- [ ] If the policy was shared but Line 9 = "No": verify and switch to Yes if needed.
- [ ] If Line 26 > 0 while Line 25 > Line 24: impossible combination. Line 26 is used only when Line 24 ≥ Line 25. Re-verify.

### Cross-form checks

- [ ] If Line 26 > 0 → Schedule 3 Line 9 = Line 26
- [ ] If Line 29 > 0 → Schedule 2 Line 1a = Line 29
- [ ] Form 8962 attached to Form 1040
- [ ] Form 1095-A retained (not attached, but kept for audit)

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to e-file software or paper Form 8962. Format:

```markdown
# Form 8962 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <filer name>
Your social security number: <SSN>

## Part I — Annual and Monthly Contribution Amount
1.  Tax family size:                                      <count>
2a. Modified AGI of taxpayer (and spouse if MFJ):         $<amount>
2b. Dependents' modified AGI:                             $<amount>
3.  Household income (Line 2a + 2b):                      $<amount>
4.  Federal poverty line (FPL) for family size:           $<amount>
5.  Household income as % of FPL (rounded down):          <%> %
6.  (Reserved for future use):                            —
7.  Applicable figure:                                    <0.0xxx>
8a. Annual contribution amount (Line 3 × Line 7):         $<amount>
8b. Monthly contribution amount (Line 8a / 12):           $<amount>

## Part II — Premium Tax Credit Claim and Reconciliation
9.  Allocating policy amounts or using Part V? Yes / No:  <Y/N>
10. Annual calculation? Yes / No:                         <Y/N>

(if Line 10 = Yes — annual calculation)
11. Annual calculation:
    a. Annual enrollment premiums:                        $<amount>
    b. Annual applicable SLCSP premium:                   $<amount>
    c. Annual contribution amount:                        $<amount>  (= Line 8a)
    d. Annual maximum premium assistance (b − c, ≥ 0):    $<amount>
    e. Annual Premium Tax Credit (lesser of a or d):      $<amount>
    f. Annual advance payment of PTC:                     $<amount>

(if Line 10 = No — monthly calculation; show 12 rows)
12. January   a. <prem> b. <SLCSP> c. <contrib> d. <max>  e. <PTC> f. <APTC>
13. February  ...
14. March     ...
... (through December)
23. December  ...

24. Total Premium Tax Credit (Column E total):            $<amount>
25. Advance Premium Tax Credit (Column F total):          $<amount>

(If Line 24 ≥ Line 25:)
26. Net Premium Tax Credit (Line 24 − Line 25):           $<amount>
    → enter on Schedule 3 Line 9
27. (skip)
28. (skip)
29. (skip)

(If Line 24 < Line 25:)
26. (leave blank)
27. Excess APTC (Line 25 − Line 24):                      $<amount>
28. Repayment limitation (instructions Table 5; blank if
    Line 5 ≥ 400 or tax year 2026+):                      $<amount>
29. Excess APTC repayment (lesser of 27 or 28):           $<amount>
    → enter on Schedule 2 Line 1a

## Part IV — Allocation (if shared policy)
30. (a) policy no. (b) other taxpayer SSN (c) start month (d) stop month
    (e) premium % (f) SLCSP % (g) APTC %:                 <details>
34. All allocations completed? Yes / No:                  <Y/N>

## Part V — Alternative Calculation for Year of Marriage (if applicable)
35-36. (a) alternative family size (b) alternative monthly contribution
       (c) start month (d) stop month:                    <details>

## Routing
- Line 26 → Schedule 3 Line 9 (refundable PTC):           $<amount>
- Line 29 → Schedule 2 Line 1a (excess APTC repayment):   $<amount>

## Required attachments
- [x] Form 8962 attached to Form 1040
- [ ] Form 8962 instructions Table 5 referenced for repayment limitation (kept in records)
- [x] Form 1095-A retained in records (not attached)

## Validation summary
- Math: all checks passed | <list failures>
- Inputs: <FPL year, dependents, MAGI sources verified>
- Sanity: <list warnings raised>

## Sources cited in this draft
- IRS Form 8962 (revision date YYYY-MM-DD)
- IRS Instructions for Form 8962 (revision date YYYY-MM-DD)
- IRS Publication 974 — Premium Tax Credit (revision date YYYY-MM-DD)
- IRC §36B; §36B(b)(3)(A) (applicable figure); §36B(d)(3)(B) (FPL determination date); §36B(f)(2)(B) (repayment limitation, tax years before 2026)
- Treas. Reg. §1.36B-4 (reconciliation, allocation, year of marriage)
- HHS Poverty Guidelines published the January before the tax year (used for FPL on Line 4)
- (any other authority used)
```

The draft is **not** the filed form. The user still has to enter it into Form 1040 e-file software or paper Form 8962.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8962 line with citation and edge cases
- [`references/fpl-tables.md`](./references/fpl-tables.md) — Federal Poverty Line tables (48+DC, AK, HI), prior-year HHS guidelines and how to determine which year applies
- [`references/applicable-figure.md`](./references/applicable-figure.md) — Applicable figure interpolation formula and tables, year-aware (2025 ARPA/IRA table; 2026 Rev. Proc. 2025-25 table)
- [`references/annual-vs-monthly.md`](./references/annual-vs-monthly.md) — Decision tree for annual vs. monthly calculation method
- [`references/allocation.md`](./references/allocation.md) — Shared-policy allocation rules (divorce, adult dependents, etc.) and Part IV completion
- [`references/repayment-limitation.md`](./references/repayment-limitation.md) — Form 8962 instructions Table 5 with year-aware values (no limitation from 2026)
- [`references/year-of-marriage.md`](./references/year-of-marriage.md) — Alternative calculation under Treas. Reg. §1.36B-4(b)(2) (Part V)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 8–12 audit-trip mistakes filers make on Form 8962

## Examples

End-to-end worked Form 8962s. Use these as patterns when the user's situation is similar.

- [`examples/full-year-coverage-refund.md`](./examples/full-year-coverage-refund.md) — Low-income freelancer with full-year coverage; PTC > APTC = refundable credit
- [`examples/mfj-income-spike-repayment.md`](./examples/mfj-income-spike-repayment.md) — MFJ couple with Q4 income surge owing excess APTC repayment
- [`examples/divorced-parents-shared-policy.md`](./examples/divorced-parents-shared-policy.md) — Divorced parents sharing a marketplace policy for the children, requiring Part IV allocation

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8962 (latest)](https://www.irs.gov/pub/irs-pdf/f8962.pdf) — the form itself
- [Instructions for Form 8962 (latest)](https://www.irs.gov/pub/irs-pdf/i8962.pdf) — line-by-line IRS guidance
- [About Form 8962](https://www.irs.gov/forms-pubs/about-form-8962) — IRS landing page with archive
- [Publication 974](https://www.irs.gov/publications/p974) — Premium Tax Credit (2025 edition, Jan 12, 2026); uses the FPL tables (Tables 1-1 to 1-3), applicable figure table (Table 2), and repayment limitation table (Table 5) printed in the Form 8962 instructions
- [HHS Poverty Guidelines](https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines) — annual FPL values (use prior-year guidelines for current-year PTC); 2024 guidelines 89 FR 2961 (Jan 17, 2024); 2025 guidelines 90 FR 5917 (Jan 17, 2025)
- [About Form 1095-A](https://www.irs.gov/forms-pubs/about-form-1095-a) — input form
- IRC §36B (Premium Tax Credit), §36B(b)(3)(A) (applicable percentage), §36B(c)(1)(A) (100%–400% FPL applicable taxpayer), §36B(d)(3)(B) (FPL determination date), §36B(f)(2)(B) (repayment limitation, tax years before 2026)
- Treas. Reg. §1.36B-4(a)(1)(ii) (shared-policy allocation), §1.36B-4(a)(3) (repayment limitation), §1.36B-4(b)(2) (year of marriage), §1.36B-4(b)(3) (divorce allocation), §1.36B-4(b)(4) (MFS allocation)
- American Rescue Plan Act of 2021 (ARPA), Section 9661 — temporary 2021/2022 expansion
- Inflation Reduction Act of 2022 (IRA), Section 12001 — extended ARPA expansion through 2025
- [Rev. Proc. 2024-35](https://www.irs.gov/pub/irs-drop/rp-24-35.pdf) — 2025 applicable percentage table and 9.02% required contribution percentage
- [Rev. Proc. 2025-25](https://www.irs.gov/pub/irs-drop/rp-25-25.pdf) — 2026 applicable percentage table (2.10%–9.96%) and 9.96% required contribution percentage
- P.L. 119-21 (One Big Beautiful Bill Act) §71305 — repayment limitation removed for tax years beginning after December 31, 2025; §71302 — lawfully present aliens below 100% FPL no longer treated as applicable taxpayers for tax years beginning after December 31, 2025; §71304 — no PTC for plans enrolled through an income-based special enrollment period, plan years beginning after December 31, 2025; §71301 — eligible-alien limits from tax years beginning after December 31, 2026
- [IRS Fact Sheet FS-2025-10](https://www.irs.gov/pub/taxpros/fs-2025-10.pdf) (Dec. 2025) — PTC FAQs updated for P.L. 119-21 (Q7 income limits, Q31 repayment caps)
- For tax year 2026: no extension of the enhanced credits had been enacted as of 2026-10-06. Re-check IRS.gov/Form8962 and IRS.gov/Pub974 before filing.

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations — particularly shared-policy allocations, year-of-marriage alternative calculations, and MFS exceptions — warrant a licensed tax professional's review.
