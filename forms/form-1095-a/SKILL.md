---
name: form-1095-a
description: >
  Use this skill when an individual taxpayer received Form 1095-A (Health
  Insurance Marketplace Statement) from healthcare.gov or a state-based
  exchange (Covered California, NY State of Health, MNsure, Pennie, etc.)
  and needs to reconcile the Premium Tax Credit on Form 8962. Triggers on
  phrases like "received 1095-A", "marketplace health insurance tax form",
  "premium tax credit", "Form 8962 prep", "advance premium tax credit
  reconciliation", "healthcare.gov tax form", "ACA tax form", "APTC owed
  back", "shared policy allocation". Do NOT use for Form 1095-B
  (Medicaid/CHIP/some employer coverage — informational only, not used on
  the return) or Form 1095-C (employer-provided insurance — informational
  only, not used on the return). Those forms do not require reconciliation
  and do not feed Form 8962.
form: Form 1095-A (Health Insurance Marketplace Statement) + Form 8962
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1095a.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1095a.pdf
---

# Form 1095-A — Health Insurance Marketplace Statement (and Form 8962 reconciliation)

This skill produces an audit-grade Form 8962 reconciliation from a user's Form 1095-A, household income, and family details. It walks through the form box by box, applies IRC §36B at each step, validates the result against the repayment limitation in Table 5 of the Form 8962 instructions (tax years before 2026 only), and emits a deliverable the user can transcribe to a paper or e-file Form 8962 with confidence.

**Form revision.** The Form 1095-A map was verified against the 2025 Form 1095-A (created 6/5/25) and the 2025 Instructions for Form 1095-A (Oct 8, 2025); the Form 8962 lines against the 2025 Form 8962 and its instructions, as used for 2025 returns filed in 2026. Re-check https://www.irs.gov/forms-pubs/about-form-1095-a and https://www.irs.gov/forms-pubs/about-form-8962 for the next revision before use. For the full Form 8962 computation, the [`form-8962`](../form-8962/SKILL.md) skill is the reference; this skill must stay consistent with it.

The math is mechanical. The judgment is in *which year's FPL applies, what the applicable figure is for the user's income bracket, whether shared policy allocation is needed, and when a rule depends on a fact the user hasn't mentioned*. This skill optimizes for those — the agent should ask, not guess.

**Companion guide for end users:** [Form 1095-A + AI Agent Skill: Marketplace Health Insurance Guide 2026](https://jupid.com/blog/form-1095-a-marketplace-statement-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1095-A, "Marketplace tax form", "healthcare.gov tax form", or "ACA tax statement"
- The user describes receiving a form from healthcare.gov or a state Marketplace (Covered California, NY State of Health, MNsure, Pennie, MA Health Connector, etc.)
- The user mentions Premium Tax Credit, advance Premium Tax Credit (APTC), or PTC reconciliation
- The user asks "do I owe back my health insurance subsidy" or "did I get enough health credit"
- The user is preparing Form 8962 and needs to know which numbers to use

Do **not** engage this skill when:

- The user received **Form 1095-B** (coverage from Medicaid, CHIP, or some small/medium employers) — this is informational only, no entry on the tax return, no Form 8962
- The user received **Form 1095-C** (employer-provided coverage from a large employer, generally 50+ FTEs) — this is informational only, no entry on the tax return, no Form 8962
- The user only had Medicare or TRICARE — no Marketplace coverage, no PTC
- The user purchased health insurance directly from an insurer outside the Marketplace — not eligible for PTC
- The user is asking about the self-employed health insurance deduction → that's Schedule 1 Line 17, not Form 8962
- The user was enrolled only in a Marketplace catastrophic plan or a stand-alone dental plan → no Form 1095-A should be issued and no PTC is allowed for that coverage (2025 Form 1095-A, Instructions for Recipient)

If the user is unsure which 1095 they received, ask them to read the form's title:
- "Form 1095-A — Health Insurance Marketplace Statement" → use this skill
- "Form 1095-B — Health Coverage" → no action needed; do not use this skill
- "Form 1095-C — Employer-Provided Health Insurance Offer and Coverage" → no action needed; do not use this skill

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 1095-A for tax year 2025 is furnished by January 31, 2026 and used on the 2025 return filed in 2026. The FPL table, applicable figures, and repayment limits depend on this. For 2026 the enhanced credits have expired: Rev. Proc. 2025-25 sets the applicable percentages (2.10% to 9.96%), household income above 400% FPL gets no PTC (IRC §36B(c)(1)(A)), and excess APTC is repaid in full with no limitation (P.L. 119-21 §71305). No extension had been enacted as of 2026-10-06; re-check IRS.gov/Form8962 before computing a 2026 return.
2. **Filer's filing status** — Single, Married Filing Jointly, Married Filing Separately (note: MFS generally cannot claim PTC; ask whether one of the narrow exceptions applies — domestic abuse or spousal abandonment, claimed by checking the box on Form 8962 line A), Head of Household, Qualifying Surviving Spouse.
3. **Tax family size** — filer + spouse (if MFJ) + every dependent claimed on the return, whether or not on the policy. Ask explicitly; don't infer from the 1095-A Part II covered individuals.
4. **Modified AGI for the tax family** — AGI from Form 1040 Line 11a + tax-exempt interest (Line 2a) + excluded foreign earned income and housing (Form 2555, lines 45 and 50) + non-taxable Social Security (2025 Form 8962 instructions, Worksheet 1-1). Ask whether dependents were required to file; if so, their modified AGI is added too (Line 2b).
5. **State of residence during the year** — drives whether the user used the federal Marketplace (healthcare.gov) or a state Marketplace, which affects how to look up missing SLCSP amounts. Also: 48 contiguous states + DC use one FPL table; Alaska and Hawaii each have a higher FPL table. If the user lived in Alaska or Hawaii for part of the year, or joint filers lived in different states, use the higher table (2025 Form 8962 instructions, Line 4).
6. **Form 1095-A Part III monthly amounts** (lines 21–32, totals on line 33) — Column A (premium), Column B (SLCSP), Column C (APTC) for each month coverage was in force. Ask for all 12 months even if the same number repeats; this is how you detect a missing-month problem.
7. **Whether the annual calculation is allowed** — Form 8962 Line 10 = Yes only if everyone in the tax family was enrolled all 12 months with the same enrollment premium (Column A) and the same applicable SLCSP premium (Column B) every month, and Part IV is not completed. Otherwise the monthly calculation (Lines 12–23) applies (2025 Form 8962 instructions, Line 10).
8. **Whether this is a shared policy** — did the policy cover someone in the user's tax family and someone in another tax family, and does the user's 1095-A list someone not in their tax family or miss a member of it? Common scenarios: divorced parents sharing a child's coverage, unmarried parents sharing a child's coverage, an adult child enrolled who files their own return. If yes, Form 8962 Line 9 = Yes and Part IV allocation is required (2025 Form 8962 instructions, Line 9).

For the worked example below, ask:
- "What's your filing status?"
- "How many people are on your tax return — you, your spouse, and any dependents?"
- "What's your AGI estimate or actual AGI?"
- "What's on your 1095-A Part III for each month? Especially: Column B values, since those are often $0 by mistake."
- "Did anyone else share this Marketplace policy who isn't on your tax return?"

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm form type

Confirm the user has Form 1095-A (not 1095-B or 1095-C). If 1095-B or 1095-C, explain it's informational only and the tax return doesn't change. Stop.

### Step 2 — Verify Part I and Part II

Check that the recipient name (line 4), SSN (line 5), and policy number (line 2) on Part I match the filer. Check Part II covered individuals (lines 16–20) and identify anyone who is NOT on the tax return — flag for shared policy allocation in Step 8. If the VOID box is checked, ignore that form; if CORRECTED is checked, use it instead of the original (2025 Form 1095-A, Instructions for Recipient).

### Step 3 — Check Part III for missing or zero values

For each month coverage was in force:
- Column A should be greater than zero (monthly premium)
- Column B should be greater than zero (SLCSP)
- Column C may be zero (no APTC) or positive

**If Column B is zero or blank in any month with coverage**, walk the user through using the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or their state's equivalent to look up the correct SLCSP. Don't proceed with zero — the PTC calculation will be wrong. Exception: the Marketplace reports -0- when every covered person enrolled after the first day of the month (and none by birth, adoption, foster placement, or court order), or the premiums for the month were not paid; no PTC is allowed for that month (2025 Instructions for Form 1095-A, Part III, column B). ASK before looking anything up.

**If Column C is the only nonzero column for a month**, the insurer terminated the policy for nonpayment: no PTC for that month, but the APTC must still be reconciled (2025 Form 1095-A, Instructions for Recipient, Column C).

If a 1095-A appears to have other errors (wrong APTC, wrong dates), tell the user to call the Marketplace and request a corrected 1095-A before filing.

### Step 4 — Determine annual vs. monthly calculation

Ask if anything changed during the year:
- Different plan or enrollment premium in different months?
- Different SLCSP premium in different months (family size change, move, birth, death)?
- Any month without coverage?
- Any shared-policy allocation (Part IV)?

If the tax family was enrolled all 12 months with the same Column A and the same Column B every month and no Part IV → annual calculation (Line 11). Otherwise → monthly calculation (Lines 12–23). A change in APTC alone does not force the monthly method.

### Step 5 — Collect household income and family size

Compute:
- Tax family size (Line 1)
- Modified AGI (Line 2a) = AGI + tax-exempt interest + excluded foreign earned income + non-taxable Social Security
- Dependent modified AGI (Line 2b) — only if dependents were required to file
- Household income (Line 3) = Line 2a + Line 2b
- Federal Poverty Line (Line 4) — use **prior-year FPL table** (2024 HHS guidelines for tax year 2025; 2025 HHS guidelines for tax year 2026), correct table for 48 states+DC, Alaska, or Hawaii; check box a, b, or c
- Household income as % of FPL (Line 5) = Line 3 ÷ Line 4 × 100, dropping any digits after the decimal point; if above 400%, enter 401 (2025 instructions, Worksheet 2)

Reference [`references/fpl-tables.md`](./references/fpl-tables.md) for FPL values by family size and state group.

### Step 6 — Look up Applicable Figure

Use Table 2 in Form 8962 instructions, indexed by Line 5 percentage, and enter it on Line 7. The ARPA/IRA expansion (2021–2025) lowered applicable figures and removed the upper FPL cap (2025: 0% up to 150% FPL, 8.5% at 400% and above; Rev. Proc. 2024-35). For 2026 the expansion expired: Rev. Proc. 2025-25 sets 2.10% to 9.96%, and above 400% FPL there is no PTC. Reference [`references/applicable-figures.md`](./references/applicable-figures.md) for the year-by-year table.

Compute:
- Annual contribution amount (Line 8a) = Line 3 × Line 7, rounded to the nearest whole dollar
- Monthly contribution amount (Line 8b) = Line 8a ÷ 12, rounded to the nearest whole dollar

### Step 7 — Compute PTC (Annual or Monthly)

For annual (Line 11):
- 11(a) = Annual enrollment premium = 1095-A line 33, Column A
- 11(b) = Annual SLCSP = 1095-A line 33, Column B
- 11(c) = Annual contribution = Line 8a
- 11(d) = Maximum premium assistance = max(0, 11(b) − 11(c))
- 11(e) = PTC = lesser of 11(a) or 11(d)
- 11(f) = Annual APTC = 1095-A line 33, Column C

For monthly (Lines 12–23): same formulas applied per row, with column (c) = Line 8b.

### Step 8 — Apply shared policy allocation if needed

If Step 2 flagged a shared policy, complete Form 8962 Part IV (Lines 30–34) before Line 10. Each row: (a) policy number from 1095-A line 2, (b) SSN of other taxpayer, (c)/(d) start and stop month, (e)/(f)/(g) allocation percentage for premium / SLCSP / APTC as a decimal (e.g., "0.67"). Allocations must total 100% across all sharing taxpayers. Completing Part IV forces Line 10 = No (monthly calculation).

Default if no agreement depends on the situation (2025 Form 8962 instructions, Table 3 and Allocation Situations 1–4; Treas. Reg. §1.36B-4): spouses who divorced or legally separated during the year use 50/50 and the same percentage for all three amounts; married filing separately uses 50% under Situation 2 rules; any other shared policy (e.g., parents divorced in an earlier year, an adult child filing their own return) defaults to the number of individuals enrolled by one taxpayer who are in the other taxpayer's tax family divided by the total enrolled. See [`references/shared-policy.md`](./references/shared-policy.md). Best practice: both parties confirm the same percentages before either files.

### Step 9 — Reconcile

- Line 24 = Total PTC = sum of column (e)
- Line 25 = Total APTC = sum of column (f), should equal sum of 1095-A Column C (after any Part IV allocation)
- If Line 24 > Line 25 → Net PTC (Line 26) = Line 24 − Line 25 → flows to Schedule 3 Line 9 (refundable). If equal, enter -0- on Line 26.
- If Line 25 > Line 24 → leave Line 26 blank; Excess APTC (Line 27) = Line 25 − Line 24 → repayment limit (Line 28) → Line 29 = lesser of Line 27 or Line 28 → flows to Schedule 2 Line 1a

### Step 10 — Apply repayment limit

For tax year 2025, if income is below 400% FPL, the excess APTC repayment is capped per Table 5 of the 2025 Form 8962 instructions. The cap depends on filing status (single vs. all others) and FPL bracket:

| Income % FPL (Line 5) | Single | Any other filing status |
|--------------|--------|---------------------|
| Less than 200% | $375 | $750 |
| At least 200% but less than 300% | $975 | $1,950 |
| At least 300% but less than 400% | $1,625 | $3,250 |
| 400% or more | Leave Line 28 blank (no limit) | Leave Line 28 blank (no limit) |

For tax years beginning after December 31, 2025 there is no repayment limitation at any income: Line 29 = Line 27 (P.L. 119-21 §71305; IRS FS-2025-10, Q31). Married filing separately: Table 5 applies to each spouse separately based on the household income on each return.

Reference [`references/repayment-limits.md`](./references/repayment-limits.md) for year-by-year table.

### Step 11 — Run validation checks

See **Validation** below. Run every check.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next forms:
- **Net PTC (Line 26)** → Schedule 3 Line 9 → Form 1040
- **Excess APTC (Line 29)** → Schedule 2 Line 1a → Form 1040
- **Form 8962 itself** must be attached to Form 1040 — do not e-file without it

### Step 14 — File the return (optional)

If the agent has browser automation and the user authorizes filing, follow [`filing.md`](./filing.md). For the full Form 8962 draft, the [`form-8962`](../form-8962/SKILL.md) skill covers every line; for the parent return see [`form-1040`](../form-1040/SKILL.md) and [`schedule-2`](../schedule-2/SKILL.md).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Form 1095-A Part I — Recipient Information (Lines 1–15)

These are identifying fields populated by the Marketplace. The agent verifies but does not edit.

- **Line 1** — Marketplace identifier (the state where the user enrolled); **Line 2** — Marketplace-assigned policy number (goes in Form 8962 Part IV column (a)); **Line 3** — policy issuer's name
- **Lines 4–6** — Recipient's name, SSN, date of birth (DOB only if no SSN)
- **Lines 7–9** — Spouse's name, SSN, DOB (only if APTC was paid; DOB only if no SSN)
- **Lines 10–11** — Policy start and termination dates
- **Lines 12–15** — Street address, city, state, country and ZIP

If the Line 5 SSN does not match the filer's SSN on Form 1040, the recipient is the wrong person and a corrected 1095-A is needed.

### Form 1095-A Part II — Covered Individuals

Lines 16–20, one row per enrollee: (A) name, (B) SSN, (C) DOB only if no SSN, (D) coverage start date, (E) coverage termination date. More than five people → an additional Form 1095-A continues Part II. Used for shared policy allocation analysis.

### Form 1095-A Part III — Monthly amounts

The three columns that drive Form 8962:

- **Column A — Monthly enrollment premium**: The full premium (before subsidy) the insurer charged for the plan you enrolled in
- **Column B — Monthly SLCSP premium**: The benchmark premium for the second-lowest cost silver plan in your coverage area for your family. Note: this is a pricing reference, not the plan you bought.
- **Column C — Monthly APTC**: The credit the Marketplace paid your insurer on your behalf each month

Lines 21–32 are January through December; line 33 holds the annual totals. Column A includes only premiums for essential health benefits (plus the pediatric dental portion of a stand-alone dental plan, if any).

### Form 8962 Part I — Annual and Monthly Contribution Amount (Lines 1–8b)

- **Line 1** — Tax family size
- **Line 2a** — Modified AGI of filer (and spouse if MFJ)
- **Line 2b** — Modified AGI of dependents who had a filing requirement
- **Line 3** — Household income = Line 2a + Line 2b
- **Line 4** — FPL for tax family size (use prior-year table; check box a Alaska, b Hawaii, or c other 48 states and DC)
- **Line 5** — Income as % of FPL = Line 3 ÷ Line 4, expressed as whole percent rounded down (401 if above 400%)
- **Line 6** — Reserved for future use (no entry)
- **Line 7** — Applicable Figure (from Table 2 in Form 8962 instructions)
- **Line 8a** — Annual contribution = Line 3 × Line 7, rounded to whole dollars
- **Line 8b** — Monthly contribution = Line 8a ÷ 12, rounded to whole dollars

### Form 8962 Part II — Premium Tax Credit (Line 9–10 + Line 11 OR Lines 12–23)

- **Line 9** — Yes/No: are you allocating policy amounts with another taxpayer or electing the alternative calculation for year of marriage? (If yes, complete Part IV and/or Part V first.)
- **Line 10** — Yes only if the tax family was enrolled all 12 months with the same enrollment premium and the same applicable SLCSP premium every month and Part IV was not completed → Line 11 (annual). Otherwise No → Lines 12–23 (monthly).

For Line 11 or Lines 12–23, the columns are:
- **(a)** — Premium amount (1095-A Col A)
- **(b)** — SLCSP (1095-A Col B)
- **(c)** — Contribution (Line 8a or 8b)
- **(d)** — Max premium assistance = max(0, (b) − (c))
- **(e)** — PTC = lesser of (a) or (d)
- **(f)** — APTC (1095-A Col C)

### Form 8962 Part III — Repayment of Excess APTC (Lines 27–29)

- **Line 27** — Excess APTC = Line 25 − Line 24 (only if positive)
- **Line 28** — Repayment limitation from Table 5 of the Form 8962 instructions (2025; blank if Line 5 is 400 or more); none for tax years after 2025
- **Line 29** — Excess APTC repayment = lesser of Line 27 or Line 28 → Schedule 2 Line 1a

### Form 8962 Part II Line 26 — Net Premium Tax Credit

If Line 24 > Line 25, Line 26 = Line 24 − Line 25 → Schedule 3 Line 9 (refundable credit). If equal, -0-. If Line 25 > Line 24, leave blank and go to Part III.

### Form 8962 Part IV — Allocation of Policy Amounts (Lines 30–34)

Up to four allocations (Lines 30–33). Each row:
- (a) Policy number (Form 1095-A line 2)
- (b) SSN of other taxpayer
- (c) Allocation start month, (d) stop month
- (e) Premium, (f) SLCSP, (g) APTC allocation percentage as decimals (must total 100% across all sharers)

Line 34 asks whether all allocations are complete; the allocated monthly amounts then go on Lines 12–23.

### Form 8962 Part V — Alternative Calculation for Year of Marriage (Lines 35–36)

Optional election for couples who were both unmarried on January 1, married on December 31, file jointly, had someone in the tax family enrolled before the first full month of marriage, and were paid excess APTC (2025 instructions, Table 4 and Worksheet 3). It can only reduce the excess APTC repayment. See Pub 974, Worksheets I–V, and the [`form-8962`](../form-8962/SKILL.md) skill.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 2a + Line 2b
- [ ] Line 5 = Line 3 ÷ Line 4 × 100, rounded down to whole percent (401 if above 400%)
- [ ] Line 8a = Line 3 × Line 7, rounded to whole dollars
- [ ] Line 8b = Line 8a ÷ 12, rounded to whole dollars
- [ ] For each Lines 12–23 row, column (e) = lesser of column (a) or column (d)
- [ ] Line 24 = sum of column (e) — annual or monthly
- [ ] Line 25 = sum of column (f) = annual sum of 1095-A Column C
- [ ] If Line 24 > Line 25 → Line 26 = Line 24 − Line 25, no Lines 27–29
- [ ] If Line 25 > Line 24 → Line 27 = Line 25 − Line 24, Line 29 = lesser of Line 27 or Line 28

### Data-cross-check

- [ ] 1095-A Part I line 5 SSN matches filer SSN
- [ ] 1095-A Part II covered individuals = tax family OR shared policy allocation completed (Part IV)
- [ ] 1095-A Part III Column B has nonzero values for every month with coverage
- [ ] Sum of 1095-A Column A annual = Form 8962 Line 11(a) or sum of monthly column (a)
- [ ] Sum of 1095-A Column B annual = Form 8962 Line 11(b) or sum of monthly column (b)
- [ ] Sum of 1095-A Column C annual = Form 8962 Line 11(f) or sum of monthly column (f) = Line 25

### Sanity checks

Surface a warning, do not block:

- [ ] Filing status is MFS without exception checkbox → not eligible for PTC
- [ ] Line 5 (income % FPL) is below 100% → check eligibility (some states' Medicaid expansion gap rules apply)
- [ ] Line 5 is over 400% → tax year 2025: applicable figure 0.0850 and no repayment limit; tax year 2026: no PTC at all and all APTC is repaid with no cap (confirm no extension was enacted after 2026-10-06)
- [ ] Tax year 2026 and Line 25 > Line 24 → no repayment limitation at any income (P.L. 119-21 §71305); Line 29 = Line 27
- [ ] APTC was received but Line 24 is zero → user is not eligible for PTC and must repay the APTC (2025: subject to Table 5; 2026: in full)
- [ ] Column B has $0 in any month with coverage → block: must look up SLCSP
- [ ] Part I line 1 (Marketplace state) or lines 12–15 address differ from the user's state of residence → double-check which FPL table applies
- [ ] User claims an exception to MFS rule but didn't provide reason → ask
- [ ] Year-of-marriage alternative calculation might apply but wasn't considered → ask

### Cross-form checks

- [ ] If Line 26 > 0, ensure Schedule 3 Line 9 is on the user's to-do list
- [ ] If Line 29 > 0, ensure Schedule 2 Line 1a is on the user's to-do list
- [ ] Form 8962 must be physically attached to Form 1040 — flag if user is paper-filing

---

## Output format

The agent's deliverable is a **filled draft** of Form 8962 the user can transcribe to a paper Form 8962 or paste into tax software. Format:

```markdown
# Form 8962 — DRAFT for tax year YYYY

## Inputs from Form 1095-A
Recipient: <name>, SSN: <last 4>
Policy issuer: <insurer>
Months of coverage: <e.g. Jan–Dec>

## Form 1095-A Part III Summary
| Month | Col A (Premium) | Col B (SLCSP) | Col C (APTC) |
|-------|-----------------|---------------|--------------|
| Jan   | $XXX            | $XXX          | $XXX         |
| Feb   | $XXX            | $XXX          | $XXX         |
| ...   | ...             | ...           | ...          |
| **Total** | **$X,XXX** | **$X,XXX**    | **$X,XXX**   |

## Form 8962 Part I
1.  Tax family size:                    X
2a. Modified AGI:                       $XX,XXX
2b. Dependent modified AGI:             $X,XXX
3.  Household income:                   $XX,XXX
4.  FPL (HH of X, 48 states+DC):        $XX,XXX
5.  Income as % of FPL:                 XXX%
7.  Applicable Figure:                  0.XXXX
8a. Annual contribution:                $X,XXX
8b. Monthly contribution:               $XXX

## Form 8962 Part II
9.  Allocation of policy amounts:       Yes | No
10. Annual or monthly calculation:      Annual (Line 11) | Monthly (Lines 12–23)

## Line 11 (if annual)
11a. Annual enrollment premium:         $X,XXX
11b. Annual SLCSP:                      $X,XXX
11c. Annual contribution:               $X,XXX
11d. Max premium assistance:            $X,XXX
11e. Annual PTC allowed:                $X,XXX
11f. Annual APTC:                       $X,XXX

## OR Lines 12–23 (monthly)
[full monthly table if applicable]

## Reconciliation
24. Total PTC:                          $X,XXX
25. Total APTC:                         $X,XXX

## Result
[If Line 24 > Line 25:]
26. Net Premium Tax Credit:             $X,XXX → Schedule 3 Line 9 (refundable)

[If Line 25 > Line 24:]
27. Excess APTC:                        $X,XXX
28. Repayment limit (Table 5; 2025 only): $X,XXX
29. Excess APTC repayment:              $X,XXX → Schedule 2 Line 1a (additional tax)

## Required attachments
- [ ] Form 8962 (always attached when 1095-A is received)
- [ ] Form 1095-A (do NOT attach to return; keep in records)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 13>

## Sources cited in this draft
- IRS Form 1095-A (revision date YYYY-MM)
- IRS Form 8962 and instructions (revision date YYYY-MM)
- IRS Publication 974
- IRC §36B
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 8962.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 1095-A box and Form 8962 line with examples and edge cases
- [`references/fpl-tables.md`](./references/fpl-tables.md) — Federal Poverty Line tables by family size and state group (48 states+DC, Alaska, Hawaii)
- [`references/applicable-figures.md`](./references/applicable-figures.md) — Year-by-year applicable figure tables (pre-ARPA vs. ARPA/IRA-extended)
- [`references/repayment-limits.md`](./references/repayment-limits.md) — Form 8962 instructions Table 5 repayment limits by year and filing status (none after 2025)
- [`references/shared-policy.md`](./references/shared-policy.md) — Allocation rules for divorced parents, unmarried parents, dependents who file their own returns
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 8962 via IRS Free File, Free File Fillable Forms, paid software, or paper

## Examples

End-to-end worked Form 8962 reconciliations. Use these as patterns when the user's situation is similar.

- [`examples/lisa-freelancer-owes-back.md`](./examples/lisa-freelancer-owes-back.md) — Single freelancer, full-year coverage, income came in higher than estimated, owes back capped excess APTC (2025)
- [`examples/family-net-ptc-refund.md`](./examples/family-net-ptc-refund.md) — Married couple with two kids, full-year coverage, income lower than estimated, owed net PTC as refund (2025)
- [`examples/divorced-parents-shared-policy.md`](./examples/divorced-parents-shared-policy.md) — Shared policy allocation across two tax returns, monthly calculation (2025)

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Form 1095-A + AI Agent Skill: Marketplace Health Insurance Guide 2026](https://jupid.com/blog/form-1095-a-marketplace-statement-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1095-A (latest)](https://www.irs.gov/pub/irs-pdf/f1095a.pdf) — the form itself
- [Instructions for Form 1095-A (latest)](https://www.irs.gov/pub/irs-pdf/i1095a.pdf) — Marketplace-facing instructions; recipient guidance is on the back of the form
- [About Form 1095-A](https://www.irs.gov/forms-pubs/about-form-1095-a) — IRS landing page
- [Form 8962 (latest)](https://www.irs.gov/pub/irs-pdf/f8962.pdf) — the reconciliation form
- [Instructions for Form 8962 (latest)](https://www.irs.gov/pub/irs-pdf/i8962.pdf) — line-by-line IRS guidance with FPL and applicable figure tables
- [Publication 974](https://www.irs.gov/publications/p974) — Premium Tax Credit (the comprehensive guide)
- [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) — SLCSP lookup for federal Marketplace
- IRC §36B (Premium Tax Credit), including §36B(f)(3) (Marketplace information reporting on Form 1095-A); §5000A (individual shared responsibility payment reduced to $0 for months after 2018; state mandates remain in CA, DC, MA, NJ, RI, VT)
- Rev. Proc. 2024-35 — 2025 applicable percentage table; Rev. Proc. 2025-25 — 2026 applicable percentage table (2.10% to 9.96%)
- ARPA / Inflation Reduction Act — 2021–2025 expansion of PTC (§36B(b)(3)(A)(iii), (c)(1)(E))
- P.L. 119-21 §71305 — no repayment limitation for tax years beginning after December 31, 2025; IRS FS-2025-10 Q31
- HHS poverty guidelines: 2024 (89 FR 2961) for 2025 returns; 2025 (90 FR 5917) for 2026 returns

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (shared policies, MFS exceptions, year-of-marriage calculations, partial-year eligibility) warrant a licensed tax professional's review.
