---
name: form-8919
description: >
  Use this skill when an individual taxpayer received a 1099-NEC (or 1099-MISC)
  but believes they should have been classified as an employee, and wants to
  pay only the 7.65% employee FICA share instead of the 15.3% self-employment
  tax. Triggers on phrases like "misclassified as contractor", "1099 should be
  W-2", "uncollected Social Security tax", "Form 8919", "SS-8 determination",
  "worker classification dispute", "employee vs independent contractor". Do NOT
  use for legitimate self-employment (use schedule-se), unreported tip income
  (use Form 4137), or employer-side classification (employer files SS-8 alone
  and remediates via Form 941-X / W-2c — not Form 8919).
form: Form 8919 (Uncollected Social Security and Medicare Tax on Wages)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f8919.pdf
official_instructions: https://www.irs.gov/forms-pubs/about-form-8919
---

# Form 8919 — Uncollected Social Security and Medicare Tax on Wages

This skill produces an audit-grade draft of Form 8919 for a worker who was paid as an independent contractor but believes they should have been classified as an employee. It walks through the common-law test, picks the correct reason code, computes the 7.65% FICA-equivalent tax, and routes the wage and tax amounts to the right places on Form 1040 and Schedule 2.

The math on Form 8919 is mechanical: 6.2% Social Security on wages up to the wage base, plus 1.45% Medicare with no cap. The judgment is in **whether the worker actually qualifies** under the IRS common-law test — and whether they have filed (or will file) Form SS-8 to support codes A and G. This skill optimizes for the latter; the agent should ask, not guess.

**Companion guide for end users:** [Form 8919 + AI Agent Skill: Misclassified Worker FICA Recovery Guide 2026](https://jupid.com/blog/form-8919-uncollected-fica-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **all** of the following are true:

- The user received compensation reported on a 1099-NEC, 1099-MISC, or paid in cash without proper FICA withholding
- The user believes — based on documented facts about behavioral control, financial control, and relationship type — that they were misclassified
- The user wants to pay employee FICA (7.65%) instead of full SE tax (15.3%)

Engage this skill when the user uses any of these phrases:

- "Form 8919", "8919", "uncollected Social Security and Medicare tax"
- "I'm being treated as a contractor but I think I'm an employee"
- "1099 should be W-2", "misclassified as 1099", "misclassified worker"
- "How do I avoid SE tax on this income"
- "SS-8 determination", "worker status determination", "Form SS-8"
- "I have a 1099 but I work like an employee"

Do **not** engage this skill when:

- The user is genuinely self-employed (multiple clients, control over methods, profit/loss risk) → use the `schedule-se` skill
- The user is reporting unreported tip income → use Form 4137 (separate skill or IRS form)
- The user is a statutory employee already on a W-2 with Box 13 checked → no 8919 needed
- The user is the **employer** trying to clean up classification → they file Form SS-8 alone, then Form 941-X and W-2/W-2c to remediate (not 8919)
- The user is a foreign worker or non-resident alien → different rules apply (IRC §1441, Form W-8BEN); refer to a tax professional

If the user's classification is ambiguous, **walk them through the common-law test before producing the form**. See `references/common-law-test.md` for the questionnaire.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 8919 for tax year 2026 is filed in 2027. Wage base and additional Medicare thresholds are year-specific.
2. **Filer's legal name and SSN.** Used in the form header. Do not invent.
3. **Firm information** for each misclassifying payer:
   - Legal firm name (column a)
   - Firm's EIN (column b — from Box 6 of 1099-NEC)
   - Reason code (column c — A, C, G, or H — see workflow Step 3)
   - Whether Form SS-8 was filed (column e)
   - If SS-8 determination received, the date (column d)
   - Total compensation received (column f — gross 1099 amount, NOT net of expenses)
4. **The user's other earned income for the tax year:**
   - W-2 wages (Box 1 and Box 3)
   - W-2 Social Security tips (Box 7)
   - Railroad Retirement compensation (if any)
   - Other 1099 income that is **legitimately** self-employment (will go on Schedule C)
5. **Filing status** — single / MFJ / MFS / HoH (needed for Additional Medicare threshold check)
6. **The user's documented evidence** of misclassification:
   - Did the firm set hours / location / methods?
   - Did the firm provide tools, training, supervision?
   - Did the user have other clients?
   - Was the engagement project-based or indefinite?
   - Were benefits offered or denied?

If the user has not yet filed Form SS-8 and is using code G, **explicitly confirm they will file SS-8 before mailing the 1040**. SS-8 is a prerequisite for codes A and G. Without it, the IRS will reject the 8919 treatment.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm classification ambiguity, then run the common-law test

Ask the user to describe a typical workday at the misclassifying firm. Then walk through the three-category common-law test from IRS Publication 15-A:

- **Behavioral control:** Who controls what work is done and how? Did the firm dictate hours, location, methods, training, evaluation criteria?
- **Financial control:** Who controls the business and financial aspects? Did the user have other clients? Bear loss risk? Make significant tool investment?
- **Relationship type:** What did the parties say about the relationship? Was there a written contract? Were benefits offered? Was the engagement indefinite?

Use `references/common-law-test.md` for the full questionnaire. Score each category. If two of the three clearly point to "employee," Form 8919 likely applies. If one or fewer, the user is likely self-employed → redirect to `schedule-se` skill.

**Do not silently decide.** Tell the user the result, why, and ask them to confirm before proceeding.

### Step 2 — Determine if Schedule C income is also present

A user can have **both** Form 8919 income (misclassified employee work) and Schedule C income (legitimate self-employment) in the same year. If the user describes other work that fits the self-employment pattern (multiple clients, own equipment, project-based), that work is **not** on 8919. It goes on Schedule C and Schedule SE separately.

Surface this distinction explicitly. The most common error is double-counting: putting the misclassified income on both Schedule C and Form 8919.

### Step 3 — Pick the correct reason code

For each misclassifying firm, determine which code applies:

| Code | Use When |
|------|----------|
| **A** | The user already filed Form SS-8 and has an IRS determination letter ruling them an employee |
| **C** | The same firm issued the user a W-2 AND a 1099-MISC/NEC for 2026, and the 1099 portion was for the same job; SS-8 not required |
| **G** | The user filed Form SS-8 and is awaiting IRS determination; reasonably believes they are an employee |
| **H** | Same as C, except the firm filed a Form W-2c that did not include the 1099 amount as wages |

**Most common path: code G.** The user files SS-8 in early tax season, then attaches Form 8919 with code G to their 1040 without waiting for the determination (which can take 6-12 months).

If the user has not filed SS-8 and the situation doesn't fit code C or H, **stop**. Tell the user: "You need to file Form SS-8 first to support this filing. Codes A and G both require an SS-8 filing on record." Then offer to help them prepare SS-8 (separate task, see `references/ss-8-filing.md`).

### Step 4 — Verify wage base for the tax year

The Social Security portion of FICA only applies up to the wage base. For tax year 2025 the wage base was $176,100. For 2026 the SSA announces the new figure in October 2025 — verify on [SSA.gov](https://www.ssa.gov/oact/cola/cbb.html) before computing Line 3.

### Step 5 — Compute Line 1 columns and Line 2

For each firm row, fill columns (a)-(f). Sum column (f) → Line 2 (total wages).

If the user has more than five firms, attach an additional Form 8919 (or schedule). The math sums across.

### Step 6 — Compute Lines 3-7 (Social Security tax)

- **Line 3** = SS wage base for tax year
- **Line 4** = Line 2 + W-2 Box 3 + W-2 Box 7 + Railroad Retirement (if any)
- **Line 5** = Line 3 − Line 4 (zero if negative)
- **Line 6** = smaller of Line 2 or Line 5
- **Line 7** = Line 6 × 6.2% (rounded to nearest dollar)

If Line 5 is zero (user already maxed out SS wage base via W-2), Line 7 is zero.

### Step 7 — Compute Lines 8-9 (Medicare tax)

- **Line 8** = Line 2 (Medicare has no wage base)
- **Line 9** = Line 8 × 1.45% (rounded to nearest dollar)

### Step 8 — Check Additional Medicare Tax (Line 10 / Form 8959)

If total wages (W-2 + 8919 + SE) exceed the filing-status threshold (single $200,000 / MFJ $250,000 / MFS $125,000), an additional 0.9% applies to the excess. **This is computed on Form 8959, not directly on Form 8919.** Add Form 8959 to the user's required-attachments list if applicable.

### Step 9 — Compute Line 11 (Total)

Line 11 = Line 7 + Line 9. This is the number that flows to Schedule 2 Line 5.

### Step 10 — Route the wage and tax amounts

Two separate entries on the user's 1040:

- **Wages on Form 1040, Line 1g:** the amount from Form 8919, Line 2 (or Line 6 of older form revisions — verify against current revision)
- **FICA tax on Schedule 2, Line 5:** the amount from Form 8919, Line 11 → flows to Form 1040 Line 23

### Step 11 — Run validation checks

See **Validation** below. Run every check.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next forms and steps the user will need:

- **Form SS-8** (if not yet filed and using codes A or G) — mail to: Department of the Treasury, Internal Revenue Service, Stop 631, Holtsville, NY 11742-0631
- **Form 8959** (if total wages exceed Additional Medicare threshold)
- **Schedule C + Schedule SE** (only for any genuinely self-employed income, separately tracked)
- **Form 1040-X for prior years** (if discovering older misclassification within three-year statute of limitations under IRC §6511)
- **Documentation retention** — keep evidence of misclassification (emails, contracts, time records) for at least three years from filing

### Step 14 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). It covers:

- IRS Free File Fillable Forms with Form 8919 attached
- Paid software (TurboTax / H&R Block / TaxAct) — entry path
- Paper filing (mailing address by state)
- The SS-8 mailing requirement (Holtsville address)
- Security rules (never store SSN/PIN; require explicit consent)

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- Name(s) on return — match Form 1040
- SSN — your SSN, not the firm's EIN

### Line 1 — Firm Information Table

One row per misclassifying firm (up to 5). Columns:

- **(a)** Firm name — legal name as shown on the 1099 or W-2
- **(b)** Firm EIN — from 1099 Box 6 ("Payer's TIN") or W-2 Box b
- **(c)** Reason code — A, C, G, or H (see workflow Step 3)
- **(d)** Date of IRS determination letter — only for code A; blank otherwise
- **(e)** SS-8 filed? — checked if codes A or G; required
- **(f)** Total compensation — gross 1099 amount (Box 1 of 1099-NEC) or unreported wages

### Line 2 — Total wages

Sum of column (f) across all rows.

### Lines 3-6 — Social Security wage-base limitation

Limits SS tax to the portion of combined wages below the year's wage base. If the user has W-2 wages already at or above the cap, no additional SS tax via 8919.

### Line 7 — Social Security tax = Line 6 × 6.2%

### Lines 8-9 — Medicare tax (no cap; full Line 2 × 1.45%)

### Line 10 — Reserved for Additional Medicare (computed on Form 8959, not directly here in current form revision — verify)

### Line 11 — Total tax = Line 7 + Line 9 → Schedule 2 Line 5

### Wage placement → Form 1040 Line 1g

The wage amount (Line 2) must be entered on **Form 1040, Line 1g** ("Wages from Form 8919, line 6" — note: line reference may shift between form revisions; always cross-check the current 1040 line label against the current 8919 line).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 2 = sum of column (f) on Line 1 rows
- [ ] Line 5 = Line 3 − Line 4 (zero if negative)
- [ ] Line 6 = MIN(Line 2, Line 5)
- [ ] Line 7 = ROUND(Line 6 × 0.062)
- [ ] Line 8 = Line 2
- [ ] Line 9 = ROUND(Line 8 × 0.0145)
- [ ] Line 11 = Line 7 + Line 9

### Cross-form checks

- [ ] Form 1040 Line 1g = Form 8919 Line 2 (wage placement)
- [ ] Schedule 2 Line 5 = Form 8919 Line 11 (FICA placement)
- [ ] If reason code is A or G, the SS-8 box (column e) is checked and Form SS-8 has been filed (or will be before 1040 mailing)
- [ ] The 1099-NEC reported on Form 8919 is **not** also reported on Schedule C (no double-counting)
- [ ] If user has W-2 wages at/above SS wage base, Line 7 is zero
- [ ] Total wages (W-2 + 8919 Line 2 + SE income) checked against Additional Medicare Tax threshold; if exceeded, Form 8959 added to attachments

### Sanity checks

Surface a warning, do not block:

- [ ] Reason code is C or H but no W-2 from same firm was provided → warn user
- [ ] Reason code is G but user shows no evidence of SS-8 filing → warn user, halt
- [ ] User has multiple firms with different reason codes → confirm each row independently
- [ ] User has only one firm AND clear self-employment indicators (multiple clients elsewhere, own equipment) → re-run common-law test before filing
- [ ] User wants to amend prior years → check three-year statute of limitations under IRC §6511

---

## Output format

The deliverable is a filled draft the user can transcribe to a paper Form 8919 or paste into tax software. Format:

```markdown
# Form 8919 — DRAFT for tax year YYYY

## Header
Name on return: <name>
SSN: <SSN>

## Line 1 — Firm information

| (a) Firm name      | (b) EIN     | (c) Code | (d) Date | (e) SS-8 | (f) Wages |
|--------------------|-------------|----------|----------|----------|-----------|
| ABC Consulting LLC | 12-3456789  | G        | (blank)  | ☑        | $72,000   |
| ...                | ...         | ...      | ...      | ...      | ...       |

## Lines 2-11 — Tax calculation

| Line | Description                              | Amount       |
|------|------------------------------------------|--------------|
| 2    | Total wages (sum of column f)            | $X,XXX       |
| 3    | SS wage base (verify SSA for tax year)   | $XXX,XXX     |
| 4    | Total SS wages (Line 2 + W-2 Box 3 + 7)  | $X,XXX       |
| 5    | Line 3 − Line 4                          | $X,XXX       |
| 6    | MIN(Line 2, Line 5)                      | $X,XXX       |
| 7    | SS tax = Line 6 × 6.2%                   | $X,XXX       |
| 8    | Wages subject to Medicare (= Line 2)     | $X,XXX       |
| 9    | Medicare tax = Line 8 × 1.45%            | $X,XXX       |
| 10   | Additional Medicare (Form 8959)          | $X,XXX       |
| 11   | Total = Line 7 + Line 9                  | $X,XXX       |

## Routing on Form 1040
- Form 1040 Line 1g: $<Line 2 amount> (wages from Form 8919)
- Schedule 2 Line 5:  $<Line 11 amount> (FICA from Form 8919)
- Form 1040 Line 23:  flows from Schedule 2

## Required attachments
- [ ] Form SS-8 filed separately (codes A and G)
- [ ] Form 8959 (if Additional Medicare Tax applies)
- [ ] Documentation supporting misclassification claim (retain 3+ years)

## Validation summary
- Math: all checks passed | <list failures>
- Cross-form: <list any failures>
- Sanity: <list any warnings>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 8919 (revision date YYYY-MM-DD)
- IRS Publication 15-A
- IRC §3101, §3121(d), §1401
- Rev. Rul. 87-41 (common-law test)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or a paper Form 8919 attached to a paper 1040. The deliverable's value is that every row is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 8919 line with examples and edge cases
- [`references/common-law-test.md`](./references/common-law-test.md) — Three-category common-law test questionnaire (IRS Pub 15-A)
- [`references/reason-codes.md`](./references/reason-codes.md) — Decision tree for codes A / C / G / H with examples
- [`references/ss-8-filing.md`](./references/ss-8-filing.md) — Form SS-8 preparation and mailing workflow
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 audit-trip mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for filing 8919 via FFFF, paid software, or paper

## Examples

End-to-end worked Forms 8919. Use these as patterns when the user's situation is similar.

- [`examples/ana-misclassified-accountant.md`](./examples/ana-misclassified-accountant.md) — Single firm, code G, full-time misclassified employee; clean common-law test
- [`examples/dual-w2-1099-same-firm.md`](./examples/dual-w2-1099-same-firm.md) — Code C: same firm issued W-2 and 1099 for the same job
- [`examples/mixed-misclassified-and-genuine-1099.md`](./examples/mixed-misclassified-and-genuine-1099.md) — User has both 8919-eligible misclassified income AND legitimate Schedule C freelance income

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8919 + AI Agent Skill: Misclassified Worker FICA Recovery Guide 2026](https://jupid.com/blog/form-8919-uncollected-fica-2026) — Jupid's narrative companion
- [Form 8919 (latest)](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — the form (instructions are included in the form PDF; no separate i8919.pdf)
- [About Form 8919](https://www.irs.gov/forms-pubs/about-form-8919) — IRS landing page with revisions
- [Form SS-8 (latest)](https://www.irs.gov/pub/irs-pdf/fss8.pdf) — Determination of Worker Status
- [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8) — IRS guidance for SS-8
- [Form 8959](https://www.irs.gov/pub/irs-pdf/f8959.pdf) — Additional Medicare Tax (cross-form)
- [Schedule 2 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) — Additional Taxes
- [Publication 15-A](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — Employer's Supplemental Tax Guide (worker classification)
- [Publication 1779](https://www.irs.gov/pub/irs-pdf/p1779.pdf) — Independent Contractor or Employee
- [Publication 1976](https://www.irs.gov/pub/irs-pdf/p1976.pdf) — Section 530 Employment Tax Relief
- IRC §3101 (employee FICA), §3121(d) (employee definition), §3401 (employer/employee definitions for withholding)
- IRC §1401 (self-employment tax), §6017 (SE return requirements)
- IRC §6511 (statute of limitations on refund claims), §6662 (accuracy penalty), §7436 (judicial review of classification)
- Rev. Rul. 87-41, 1987-1 C.B. 296 (original 20-factor common-law test)
- Section 530, Revenue Act of 1978 (employer safe harbor; not a worker defense)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client or attorney-client relationship. Worker misclassification disputes can have legal consequences beyond federal tax (state employment law, wage-and-hour claims, benefits eligibility). The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's or employment attorney's review.
