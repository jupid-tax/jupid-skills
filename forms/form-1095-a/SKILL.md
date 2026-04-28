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
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1095a.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1095a.pdf
---

# Form 1095-A — Health Insurance Marketplace Statement (and Form 8962 reconciliation)

This skill produces an audit-grade Form 8962 reconciliation from a user's Form 1095-A, household income, and family details. It walks through the form box by box, applies IRC §36B at each step, validates the result against repayment limits in Pub 974 Table 5, and emits a deliverable the user can transcribe to a paper or e-file Form 8962 with confidence.

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
- The user is asking about employer health insurance deduction → that's Schedule 1 Line 17 (self-employed health insurance), not Form 8962

If the user is unsure which 1095 they received, ask them to read the form's title:
- "Form 1095-A — Health Insurance Marketplace Statement" → use this skill
- "Form 1095-B — Health Coverage" → no action needed; do not use this skill
- "Form 1095-C — Employer-Provided Health Insurance Offer and Coverage" → no action needed; do not use this skill

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 1095-A for tax year 2025 is filed in 2026; for tax year 2024, in 2025. The FPL table, applicable figures, and repayment limits depend on this.
2. **Filer's filing status** — Single, Married Filing Jointly, Married Filing Separately (note: MFS generally cannot claim PTC; ask whether one of the narrow exceptions applies — domestic abuse or spousal abandonment), Head of Household, Qualifying Surviving Spouse.
3. **Tax family size** — filer + spouse (if MFJ) + dependents claimed on the return. Ask explicitly; don't infer from the 1095-A Part II covered individuals (which may include people not on the tax return).
4. **Modified AGI for the tax family** — AGI from Form 1040 Line 11 + tax-exempt interest + excluded foreign earned income + non-taxable Social Security. Ask whether dependents had a filing requirement; if so, their modified AGI is added too.
5. **State of residence** — drives whether the user used the federal Marketplace (healthcare.gov) or a state Marketplace, which affects how to look up missing SLCSP amounts. Also: 48 contiguous states + DC use one FPL table; Alaska and Hawaii each have a higher FPL table.
6. **Form 1095-A Part III monthly amounts** — Column A (premium), Column B (SLCSP), Column C (APTC) for each month coverage was in force. Ask for all 12 months even if the same number repeats; this is how you detect a missing-month problem.
7. **Whether all 12 months had identical coverage details** — same plan, same family size, same APTC. If yes, the annual calculation (Form 8962 Line 11) applies. If no, the monthly calculation (Lines 12–23) applies.
8. **Whether this is a shared policy** — was anyone on the 1095-A NOT on the user's tax return? Common scenarios: divorced parents sharing a child's coverage, unmarried parents sharing a child's coverage, an adult child enrolled who files their own return. If yes, Form 8962 Part IV allocation is required.

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

Check that the recipient SSN, name, and policy number on Part I match the filer. Check Part II covered individuals and identify anyone who is NOT on the tax return — flag for shared policy allocation in Step 7.

### Step 3 — Check Part III for missing or zero values

For each month coverage was in force:
- Column A should be greater than zero (monthly premium)
- Column B should be greater than zero (SLCSP)
- Column C may be zero (no APTC) or positive

**If Column B is zero in any month with coverage**, walk the user through using the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or their state's equivalent to look up the correct SLCSP. Don't proceed with zero — the PTC calculation will be wrong.

If a 1095-A appears to have other errors (wrong APTC, wrong dates), tell the user to call the Marketplace and request a corrected 1095-A before filing.

### Step 4 — Determine annual vs. monthly calculation

Ask if anything changed during the year:
- Different plan in different months?
- Family size change (marriage, divorce, baby, death)?
- APTC changed mid-year (income update with the Marketplace)?
- Any month without coverage?

If everything was identical for all 12 months → annual calculation (Line 11). Otherwise → monthly calculation (Lines 12–23).

### Step 5 — Collect household income and family size

Compute:
- Tax family size (Line 1)
- Modified AGI (Line 2a) = AGI + tax-exempt interest + excluded foreign earned income + non-taxable Social Security
- Dependent modified AGI (Line 2b) — only if dependents had filing requirement
- Household income (Line 3) = Line 2a + Line 2b
- Federal Poverty Line (Line 4) — use **prior-year FPL table** (2024 FPL for tax year 2025; 2025 FPL for tax year 2026), correct table for 48 states+DC, Alaska, or Hawaii
- Household income as % of FPL (Line 5) = Line 3 ÷ Line 4 × 100, rounded down to whole percent

Reference [`references/fpl-tables.md`](./references/fpl-tables.md) for FPL values by family size and state group.

### Step 6 — Look up Applicable Figure

Use Table 2 in Form 8962 instructions, indexed by Line 5 percentage. Note the ARPA/IRA expansion (2021–2025) lowered applicable figures and removed the upper FPL cap; 2026 status depends on legislation. Reference [`references/applicable-figures.md`](./references/applicable-figures.md) for the year-by-year table.

Compute:
- Annual contribution amount (Line 8b) = Line 3 × Line 8a
- For monthly: divide Line 8b by 12

### Step 7 — Compute PTC (Annual or Monthly)

For annual (Line 11):
- 11(a) = Annual enrollment premium = sum of 1095-A Column A for the year
- 11(b) = Annual SLCSP = sum of 1095-A Column B for the year
- 11(c) = Annual contribution = Line 8b
- 11(d) = Maximum premium assistance = max(0, 11(b) − 11(c))
- 11(e) = PTC = lesser of 11(a) or 11(d)
- 11(f) = Annual APTC = sum of 1095-A Column C for the year

For monthly (Lines 12–23): same formulas applied per row.

### Step 8 — Apply shared policy allocation if needed

If anyone on Part II of 1095-A is not on the tax return, complete Form 8962 Part IV (Lines 30–34). Each row: SSN of other taxpayer, allocation percentage for premium / SLCSP / APTC. Allocations must total 100% across all sharing taxpayers.

Default if no agreement: 50/50. Best practice: get a written agreement signed by both parties.

### Step 9 — Reconcile

- Line 24 = Total PTC = sum of column (e)
- Line 25 = Total APTC = sum of column (f), should equal sum of 1095-A Column C
- If Line 24 > Line 25 → Net PTC (Line 26) = Line 24 − Line 25 → flows to Schedule 3 Line 9 (refundable)
- If Line 25 > Line 24 → Excess APTC = Line 25 − Line 24 → apply repayment limit (Line 28) → Line 29 = lesser of excess or limit → flows to Schedule 2 Line 1a

### Step 10 — Apply repayment limit

If income is below 400% FPL, the excess APTC repayment is capped per Pub 974 Table 5. The cap depends on filing status (single vs. all others) and FPL bracket:

| Income % FPL | Single | Other Filing Status |
|--------------|--------|---------------------|
| Under 200% | $375 | $750 |
| At least 200% but less than 300% | $975 | $1,950 |
| At least 300% but less than 400% | $1,625 | $3,250 |
| 400% or more | No cap | No cap |

(2025 figures from Pub 974; verify for the year you're filing.)

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

If the agent has browser automation and the user authorizes filing, follow [`filing.md`](./filing.md).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Form 1095-A Part I — Recipient Information (Lines 1–15)

These are identifying fields populated by the Marketplace. The agent verifies but does not edit.

- **Lines 1–7** — Marketplace identifier and policy number; if blank or wrong, contact the Marketplace
- **Lines 8–15** — Recipient name, SSN, DOB, address, policy issuer

If Line 1 SSN does not match the filer's SSN on Form 1040, the recipient is the wrong person and a corrected 1095-A is needed.

### Form 1095-A Part II — Covered Individuals

Each row identifies one enrollee. Names + SSN + DOB + coverage start/end dates. Used for shared policy allocation analysis.

### Form 1095-A Part III — Monthly amounts

The three columns that drive Form 8962:

- **Column A — Monthly enrollment premium**: The full premium (before subsidy) the insurer charged for the plan you enrolled in
- **Column B — Monthly SLCSP premium**: The benchmark premium for the second-lowest cost silver plan in your coverage area for your family. Note: this is a pricing reference, not the plan you bought.
- **Column C — Monthly APTC**: The credit the Marketplace paid your insurer on your behalf each month

Each row is one month, January through December.

### Form 8962 Part I — Annual and Monthly Contribution Amount (Lines 1–8b)

- **Line 1** — Tax family size
- **Line 2a** — Modified AGI of filer (and spouse if MFJ)
- **Line 2b** — Modified AGI of dependents who had a filing requirement
- **Line 3** — Household income = Line 2a + Line 2b
- **Line 4** — FPL for tax family size (use prior-year table; 48 states + DC vs. Alaska vs. Hawaii)
- **Line 5** — Income as % of FPL = Line 3 ÷ Line 4, expressed as whole percent rounded down
- **Line 6** — Reserved (no entry)
- **Line 7** — Applicable Figure (from Table 2 in Form 8962 instructions)
- **Line 8a** — Annual contribution = Line 3 × Line 7
- **Line 8b** — Monthly contribution = Line 8a ÷ 12

### Form 8962 Part II — Premium Tax Credit (Line 9–10 + Line 11 OR Lines 12–23)

- **Line 9** — Yes/No: are you allocating policy amounts with another taxpayer? (If yes, complete Part IV first.)
- **Line 10** — Yes/No: do all of these apply: (a) coverage all 12 months, (b) same plan, (c) same family, (d) same APTC? If yes → Line 11 (annual). If no → Lines 12–23 (monthly).

For Line 11 or Lines 12–23, the columns are:
- **(a)** — Premium amount (1095-A Col A)
- **(b)** — SLCSP (1095-A Col B)
- **(c)** — Contribution (Line 8a or 8b)
- **(d)** — Max premium assistance = max(0, (b) − (c))
- **(e)** — PTC = lesser of (a) or (d)
- **(f)** — APTC (1095-A Col C)

### Form 8962 Part III — Repayment of Excess APTC (Lines 27–29)

- **Line 27** — Excess APTC = Line 25 − Line 24 (only if positive)
- **Line 28** — Repayment limitation from Pub 974 Table 5
- **Line 29** — Excess APTC repayment = lesser of Line 27 or Line 28 → Schedule 2 Line 1a

### Form 8962 Part II Line 26 — Net Premium Tax Credit

If Line 24 > Line 25, Line 26 = Line 24 − Line 25 → Schedule 3 Line 9 (refundable credit)

### Form 8962 Part IV — Allocation of Policy Amounts (Lines 30–34)

Up to four allocations. Each row:
- Other taxpayer SSN
- Months of allocation (start/end)
- Allocation percentage for premium, SLCSP, and APTC (must total 100% across all sharers)

### Form 8962 Part V — Alternative Calculation for Year of Marriage (Line 35)

Optional simplified calculation for couples who married during the year. Only applies if marriage occurred mid-year and one or both spouses had Marketplace coverage before the marriage. See Pub 974 Chapter 4.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 3 = Line 2a + Line 2b
- [ ] Line 5 = Line 3 ÷ Line 4 × 100, rounded down to whole percent
- [ ] Line 8a = Line 3 × Line 7
- [ ] Line 8b = Line 8a ÷ 12
- [ ] For each Lines 12–23 row, column (e) = lesser of column (a) or column (d)
- [ ] Line 24 = sum of column (e) — annual or monthly
- [ ] Line 25 = sum of column (f) = annual sum of 1095-A Column C
- [ ] If Line 24 > Line 25 → Line 26 = Line 24 − Line 25, no Lines 27–29
- [ ] If Line 25 > Line 24 → Line 27 = Line 25 − Line 24, Line 29 = lesser of Line 27 or Line 28

### Data-cross-check

- [ ] 1095-A Part I SSN matches filer SSN
- [ ] 1095-A Part II covered individuals = tax family OR shared policy allocation completed (Part IV)
- [ ] 1095-A Part III Column B has nonzero values for every month with coverage
- [ ] Sum of 1095-A Column A annual = Form 8962 Line 11(a) or sum of monthly column (a)
- [ ] Sum of 1095-A Column B annual = Form 8962 Line 11(b) or sum of monthly column (b)
- [ ] Sum of 1095-A Column C annual = Form 8962 Line 11(f) or sum of monthly column (f) = Line 25

### Sanity checks

Surface a warning, do not block:

- [ ] Filing status is MFS without exception checkbox → not eligible for PTC
- [ ] Line 5 (income % FPL) is below 100% → check eligibility (some states' Medicaid expansion gap rules apply)
- [ ] Line 5 is over 400% → if 2026 reverted to pre-ARPA rules, no PTC at all; if ARPA/IRA still applies, full PTC available capped by 8.5% of income
- [ ] APTC was received but Line 24 is zero → user is not eligible for PTC and must repay entire APTC (subject to limits)
- [ ] Column B has $0 in any month with coverage → block: must look up SLCSP
- [ ] User's state shows in Part II as different from user's filing-state → double-check residency
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
28. Repayment limit (from Pub 974):     $X,XXX
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
- [`references/repayment-limits.md`](./references/repayment-limits.md) — Pub 974 Table 5 repayment limits by year and filing status
- [`references/shared-policy.md`](./references/shared-policy.md) — Allocation rules for divorced parents, unmarried parents, dependents who file their own returns
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 8962 via IRS Free File Fillable Forms, IRS Direct File, paid software, or paper

## Examples

End-to-end worked Form 8962 reconciliations. Use these as patterns when the user's situation is similar.

- [`examples/lisa-freelancer-owes-back.md`](./examples/lisa-freelancer-owes-back.md) — Single freelancer, full-year coverage, income came in higher than estimated, owes back capped excess APTC
- [`examples/family-net-ptc-refund.md`](./examples/family-net-ptc-refund.md) — Married couple with two kids, full-year coverage, income lower than estimated, owed net PTC as refund
- [`examples/divorced-parents-shared-policy.md`](./examples/divorced-parents-shared-policy.md) — Shared policy allocation across two tax returns

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
- IRC §36B (Premium Tax Credit), §6055 (information reporting for minimum essential coverage), §5000A (individual shared responsibility — repealed federal penalty as of 2019 but state mandates remain in CA, DC, MA, NJ, RI, VT)
- Rev. Proc. 2024-36 — 2025 inflation-adjusted applicable figure percentages
- ARPA / Inflation Reduction Act — 2021–2025 expansion of PTC

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (shared policies, MFS exceptions, year-of-marriage calculations, partial-year eligibility) warrant a licensed tax professional's review.
