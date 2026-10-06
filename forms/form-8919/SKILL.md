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
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8919.pdf
official_instructions: https://www.irs.gov/forms-pubs/about-form-8919
---

# Form 8919 — Uncollected Social Security and Medicare Tax on Wages

This skill produces an audit-grade draft of Form 8919 for a worker who was paid as an independent contractor but believes they should have been classified as an employee. It walks through the common-law test, picks the correct reason code, computes the 7.65% FICA-equivalent tax, and routes the wage and tax amounts to the right places on Form 1040 and Schedule 2.

The math on Form 8919 is mechanical: 6.2% Social Security on wages up to the wage base, plus 1.45% Medicare with no cap. The judgment is in **whether the worker actually qualifies** under the IRS common-law test, which reason code their documents support, and (for code G) whether they have filed or will file Form SS-8 on or before the date they file the return. The agent should ask, not guess.

**Form revision:** the line map in this skill was verified against the **2025 Form 8919** ("Created 10/22/25"; instructions on page 2), filed with 2025 returns in 2026. The next revision must be re-checked before use: https://www.irs.gov/forms-pubs/about-form-8919.

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
   - Firm's federal identification number (column b — EIN, or SSN if the firm is an individual; the "PAYER'S TIN" on the 1099-NEC; "unknown" if it cannot be obtained)
   - Reason code (column c — A, C, G, or H — see workflow Step 3)
   - Date of the IRS determination letter (code A) or other IRS correspondence (code C) (column d)
   - Whether the firm issued a Form 1099-MISC and/or 1099-NEC for this pay (column e)
   - Total wages with no Social Security or Medicare withholding and not reported on a W-2 (column f — gross 1099 amount, NOT net of expenses)
   - Whether Form SS-8 was filed and when (needed for code G; code H must NOT be paired with SS-8)
4. **The user's other earned income for the tax year:**
   - W-2 wages (Box 1, and Box 3 Social Security wages)
   - W-2 Social Security tips (Box 7)
   - Railroad Retirement (RRTA) compensation subject to the 6.2% rate (if any)
   - Unreported tips subject to Social Security tax from Form 4137, line 10 (if any)
   - Other 1099 income that is **legitimately** self-employment (will go on Schedule C)
5. **Filing status** — single / MFJ / MFS / HoH (needed for Additional Medicare threshold check)
6. **The user's documented evidence** of misclassification:
   - Did the firm set hours / location / methods?
   - Did the firm provide tools, training, supervision?
   - Did the user have other clients?
   - Was the engagement project-based or indefinite?
   - Were benefits offered or denied?

If the user has not yet filed Form SS-8 and is using code G, **explicitly confirm they will file SS-8 on or before the date they file the return** (the form's rule for code G). Code A requires an SS-8 determination letter; code C requires other IRS correspondence; code H must not be paired with an SS-8 filing. Without the document a code requires, the IRS can reject the 8919 treatment.

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

For each misclassifying firm, determine which code applies (2025 Form 8919, page 1 "Reason codes"; one code per line):

| Code | Use When |
|------|----------|
| **A** | The user filed Form SS-8 and received a determination letter stating they are an employee of this firm |
| **C** | The user received other IRS correspondence stating they are an employee (includes a "section 530 employee" designation) |
| **G** | The user filed Form SS-8 and hasn't received a reply. Also the fallback: if no code applies but the user believes they were an employee, enter G and file Form SS-8 on or before the date the return is filed |
| **H** | The same firm issued the user a Form W-2 AND a Form 1099-MISC/NEC for the year, and the 1099 amount should have been W-2 wages. **Do not file Form SS-8 for code H** |

**Most common path for a worker with only a 1099: code G.** The user files SS-8 (mail or fax) no later than the return, then files Form 8919 with code G without waiting for the determination (the IRS says a determination may take at least six months).

If no code fits and the user will not file Form SS-8, **stop**. Tell the user: "Code G requires Form SS-8 filed on or before the date you file your return. Without it, this income goes on Schedule C and Schedule SE." Then offer to help them prepare SS-8 (separate task, see `references/ss-8-filing.md`). Full decision tree: `references/reason-codes.md`.

### Step 4 — Verify wage base for the tax year

The Social Security portion only applies up to the wage base (Form 8919 line 7, pre-printed). 2025: $176,100 (2025 Form 8919 line 7). 2026: $184,500 ([SSA](https://www.ssa.gov/oact/cola/cbb.html)). For any other year, read the amount printed on that year's form.

### Step 5 — Fill lines 1–5 and line 6

One row per firm on lines 1–5, columns (a)–(f). Line 6 = sum of column (f).

If the user has more than five firms, attach additional Forms 8919 with lines 1–5 completed, and complete lines 6–13 on only one Form 8919 (line 6 = total of all rows on all Forms 8919).

### Step 6 — Compute lines 7–11 (Social Security tax)

- **Line 7** = SS wage base for the tax year (pre-printed)
- **Line 8** = W-2 Box 3 + W-2 Box 7 (all W-2s) + RRTA compensation subject to 6.2% (not more than line 7) + Form 4137 line 10. **Do not include the Form 8919 wages.**
- **Line 9** = Line 7 − Line 8 (if line 8 is more than line 7, enter -0- here and on line 10)
- **Line 10** = smaller of Line 6 or Line 9
- **Line 11** = Line 10 × 0.062

If line 9 is zero (W-2 wages already reached the wage base), lines 10 and 11 are zero.

### Step 7 — Compute line 12 (Medicare tax)

- **Line 12** = **Line 6** × 0.0145 (Medicare has no wage base)

### Step 8 — Check Additional Medicare Tax (Form 8959)

Form 8919 has no Additional Medicare line. If Medicare wages (W-2 box 5 + Form 8919 line 6) or self-employment income exceed the filing-status threshold (single/HOH/QSS $200,000, MFJ $250,000, MFS $125,000), the 0.9% is figured on **Form 8959**; Form 8919 line 6 goes to Form 8959 line 3. Add Form 8959 to the required-attachments list if it applies.

### Step 9 — Compute line 13 (Total)

Line 13 = Line 11 + Line 12. This amount goes on **Schedule 2 (Form 1040), line 6** (or Form 1040-SS, Part I, line 6c).

### Step 10 — Route the wage and tax amounts

Entries on the user's return:

- **Wages on Form 1040 (or 1040-SR / 1040-NR), line 1g:** Form 8919 line 6 (the 2025 Form 1040 label reads "Wages from Form 8919, line 6")
- **Tax on Schedule 2, line 6:** Form 8919 line 13 → Schedule 2 line 21 → Form 1040 line 23
- **If the user also files Schedule SE:** Form 8919 line 10 → Schedule SE line 8c
- **If Form 8959 is required:** Form 8919 line 6 → Form 8959 line 3

### Step 11 — Run validation checks

See **Validation** below. Run every check.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next forms and steps the user will need:

- **Form SS-8** (if using code G and not yet filed) — file separately, never attached to the return. Mail to: Internal Revenue Service, Form SS-8 Determinations, P.O. Box 630, Stop 631, Holtsville, NY 11742-0630, or fax to 855-242-4481 (Instructions for Form SS-8, Rev. January 2024, "Where To File")
- **Form 8959** (if total wages exceed Additional Medicare threshold)
- **Schedule C + Schedule SE** (only for any genuinely self-employed income, separately tracked)
- **Form 1040-X for prior years** (if discovering older misclassification while the refund period is open: generally 3 years from filing or 2 years from payment, whichever is later, IRC §6511)
- **Documentation retention** — keep evidence of misclassification (emails, contracts, time records) for at least three years from filing

### Step 14 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). It covers:

- IRS Free File (guided software, AGI $89,000 or less) and Free File Fillable Forms with Form 8919 attached
- Paid software (TurboTax / H&R Block / TaxAct) — entry path
- Paper filing (mailing address by state)
- The separate Form SS-8 filing (mail or fax, Holtsville)
- Security rules (never store SSN/PIN; require explicit consent)

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below (2025 Form 8919).

### Header

- Name of the person who must file this form — the worker only. If married, complete a separate Form 8919 for each spouse who must file it.
- SSN — the worker's SSN, not the firm's EIN

### Lines 1–5 — One row per firm

One row per misclassifying firm (up to 5 per form). Columns:

- **(a)** Name of firm — exactly as on the 1099-MISC/NEC if one was received
- **(b)** Firm's federal identification number — EIN or SSN; "unknown" if it cannot be obtained (Form W-9 can be used to request it)
- **(c)** Reason code — A, C, G, or H (one per line; see workflow Step 3)
- **(d)** Date of IRS determination or correspondence — only for code A or C; blank otherwise
- **(e)** Check if Form 1099-MISC and/or 1099-NEC was received
- **(f)** Total wages received with no Social Security or Medicare withholding and not reported on Form W-2 — gross amount (1099-NEC Box 1), not net of expenses

### Line 6 — Total wages

Sum of column (f) → Form 1040 line 1g, and Form 8959 line 3 if Form 8959 is required.

### Lines 7–10 — Social Security wage-base limitation

Line 7 wage base; line 8 other SS wages (W-2 boxes 3 and 7, RRTA, Form 4137 line 10, never the 8919 wages); line 9 = line 7 − line 8 (not below zero); line 10 = smaller of line 6 or line 9. If W-2 wages already reached the wage base, no Social Security tax is due via Form 8919.

### Line 11 — Social Security tax = Line 10 × 6.2%

### Line 12 — Medicare tax = Line 6 × 1.45% (no cap)

### Line 13 — Total tax = Line 11 + Line 12 → Schedule 2 line 6

### Wage placement → Form 1040 line 1g

The wage amount (line 6) is entered on **Form 1040, line 1g** ("Wages from Form 8919, line 6" on the 2025 Form 1040). Re-check the label on the current Form 1040 each year.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 6 = sum of column (f) on lines 1–5 (all Forms 8919 if more than five firms)
- [ ] Line 8 excludes the Form 8919 wages
- [ ] Line 9 = MAX(0, Line 7 − Line 8)
- [ ] Line 10 = MIN(Line 6, Line 9)
- [ ] Line 11 = Line 10 × 0.062
- [ ] Line 12 = Line 6 × 0.0145
- [ ] Line 13 = Line 11 + Line 12

### Cross-form checks

- [ ] Form 1040 line 1g = Form 8919 line 6 (wage placement)
- [ ] Schedule 2 line 6 = Form 8919 line 13 (tax placement; line 5 is Form 4137, not 8919)
- [ ] If Schedule SE is filed, Schedule SE line 8c = Form 8919 line 10
- [ ] Code G: Form SS-8 has been filed, or will be filed on or before the return date (ask for proof)
- [ ] Code A: determination letter date in column (d); code C: correspondence date in column (d); codes G and H: column (d) blank
- [ ] Code H: no Form SS-8 filed for that firm
- [ ] Column (e) checked for every firm that issued a 1099-MISC/NEC
- [ ] The 1099 amount reported on Form 8919 is **not** also reported on Schedule C (no double-counting)
- [ ] If W-2 Social Security wages are at or above the wage base, line 11 is zero
- [ ] Medicare wages (W-2 box 5 + Form 8919 line 6) and SE income checked against the Additional Medicare Tax threshold; if exceeded, Form 8959 added to attachments

### Sanity checks

Surface a warning, do not block:

- [ ] Reason code is H but no W-2 from the same firm was provided → warn user
- [ ] Reason code is G but the user shows no evidence of an SS-8 filing → warn user, halt
- [ ] Reason code is A or C but the user has no IRS letter → halt and ask
- [ ] User has multiple firms with different reason codes → confirm each row independently
- [ ] User has only one firm AND clear self-employment indicators (multiple clients elsewhere, own equipment) → re-run common-law test before filing
- [ ] User wants to amend prior years → check the IRC §6511 refund period for each year

---

## Output format

The deliverable is a filled draft the user can transcribe to a paper Form 8919 or paste into tax software. Format:

```markdown
# Form 8919 — DRAFT for tax year YYYY

## Header
Name of person who must file (the worker): <name>
SSN: <SSN>

## Lines 1–5 — Firm information

| Line | (a) Firm name      | (b) Federal ID | (c) Code | (d) Date | (e) 1099 received | (f) Wages |
|------|--------------------|----------------|----------|----------|-------------------|-----------|
| 1    | ABC Consulting LLC | 12-3456789     | G        | (blank)  | ☑                 | $72,000   |
| ...  | ...                | ...            | ...      | ...      | ...               | ...       |

## Lines 6–13 — Tax calculation

| Line | Description                                              | Amount       |
|------|----------------------------------------------------------|--------------|
| 6    | Total wages (sum of column f)                            | $X,XXX       |
| 7    | SS wage base (pre-printed for the tax year)              | $XXX,XXX     |
| 8    | Other SS wages: W-2 boxes 3 + 7, RRTA, Form 4137 line 10 | $X,XXX       |
| 9    | Line 7 − Line 8 (not below zero)                         | $X,XXX       |
| 10   | Smaller of Line 6 or Line 9                              | $X,XXX       |
| 11   | SS tax = Line 10 × 6.2%                                  | $X,XXX       |
| 12   | Medicare tax = Line 6 × 1.45%                            | $X,XXX       |
| 13   | Total = Line 11 + Line 12                                | $X,XXX       |

## Routing on Form 1040
- Form 1040 line 1g: $<Line 6 amount> (wages from Form 8919)
- Schedule 2 line 6:  $<Line 13 amount> (uncollected SS and Medicare tax)
- Form 1040 line 23:  flows from Schedule 2 line 21
- Schedule SE line 8c: $<Line 10 amount> (only if Schedule SE is filed)
- Form 8959 line 3:   $<Line 6 amount> (only if Form 8959 is required)

## Required attachments
- [ ] Form SS-8 filed separately, on or before the return date (code G only; never for code H)
- [ ] Form 8959 (if Additional Medicare Tax applies)
- [ ] Documentation supporting misclassification claim (retain 3+ years)

## Validation summary
- Math: all checks passed | <list failures>
- Cross-form: <list any failures>
- Sanity: <list any warnings>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 8919 (tax year of the revision used; 2025 form created 10/22/25)
- Instructions for Form SS-8 (Rev. January 2024), if code G
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
- [`references/ss-8-filing.md`](./references/ss-8-filing.md) — Form SS-8 preparation and mail/fax workflow
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 audit-trip mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for filing 8919 via FFFF, paid software, or paper

## Examples

End-to-end worked Forms 8919. Use these as patterns when the user's situation is similar.

- [`examples/ana-misclassified-accountant.md`](./examples/ana-misclassified-accountant.md) — Single firm, code G, full-time misclassified employee; clean common-law test
- [`examples/dual-w2-1099-same-firm.md`](./examples/dual-w2-1099-same-firm.md) — Code H: same firm issued a W-2 and a 1099-NEC, and the 1099 amount was employee pay (no SS-8)
- [`examples/mixed-misclassified-and-genuine-1099.md`](./examples/mixed-misclassified-and-genuine-1099.md) — User has both 8919-eligible misclassified income AND legitimate Schedule C freelance income

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 8919 + AI Agent Skill: Misclassified Worker FICA Recovery Guide 2026](https://jupid.com/blog/form-8919-uncollected-fica-2026) — Jupid's narrative companion
- [Form 8919 (latest)](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — the form (instructions are included in the form PDF; no separate i8919.pdf)
- [About Form 8919](https://www.irs.gov/forms-pubs/about-form-8919) — IRS landing page with revisions
- [Form SS-8 (Rev. December 2023)](https://www.irs.gov/pub/irs-pdf/fss8.pdf) — Determination of Worker Status
- [Instructions for Form SS-8 (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/iss8.pdf) — where to file (mail/fax), determination process, statute of limitations, protective claim
- [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8) — IRS guidance for SS-8
- [Independent contractor (self-employed) or employee?](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee) — SS-8 determination "may take at least six months"
- [SSA Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html) — wage base ($176,100 for 2025, $184,500 for 2026)
- [Form 8959](https://www.irs.gov/pub/irs-pdf/f8959.pdf) — Additional Medicare Tax (cross-form)
- [Schedule 2 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) — Additional Taxes (line 6)
- [Schedule SE (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) — line 8c takes Form 8919 line 10
- [Publication 15-A](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — Employer's Supplemental Tax Guide (worker classification)
- [Publication 1779](https://www.irs.gov/pub/irs-pdf/p1779.pdf) — Independent Contractor or Employee
- [Publication 1976](https://www.irs.gov/pub/irs-pdf/p1976.pdf) — Section 530 Employment Tax Relief
- IRC §3101 (employee FICA), §3121(d) (employee definition), §3401 (employer/employee definitions for withholding)
- IRC §1401 (self-employment tax), §6017 (SE return requirements)
- IRC §6511 (statute of limitations on refund claims), §6662 (accuracy penalty), §7436 (Tax Court review of employment status; petition only by the service recipient, §7436(b)(1))
- Rev. Rul. 87-41, 1987-1 C.B. 296 (original 20-factor common-law test)
- Section 530, Revenue Act of 1978 (employer safe harbor; not a worker defense)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client or attorney-client relationship. Worker misclassification disputes can have legal consequences beyond federal tax (state employment law, wage-and-hour claims, benefits eligibility). The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations warrant a licensed tax professional's or employment attorney's review.
