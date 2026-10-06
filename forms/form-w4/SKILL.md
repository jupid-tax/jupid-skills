---
name: form-w4
description: >
  Use this skill when a W-2 employee needs to fill out, update, or troubleshoot
  IRS Form W-4 (Employee's Withholding Certificate). Triggers on phrases like
  "fill out W-4", "update withholding", "starting a new job", "W-4 for two
  jobs", "claim dependents on W-4", "want bigger paycheck", "underpaid taxes
  last year", "spouse just started working", "got married — update W-4". Do
  NOT use for contractors/freelancers (they need W-9, not W-4; use form-w9),
  pension recipients (Form W-4P), nonperiodic distributions or rollovers
  (Form W-4R; use form-w-4r), quarterly estimated tax (use form-1040-es), or
  nonresident aliens claiming a treaty exemption (Form 8233; Notice 1392
  governs their W-4).
form: Form W-4 (Employee's Withholding Certificate)
audience: [individual, employer]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/fw4.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/fw4.pdf
---

# Form W-4 — Employee's Withholding Certificate

This skill produces an audit-grade W-4 draft from the user's job, dependents, and side-income facts. It walks through the five steps of the form, applies the IRS rules at each step, validates the result against the IRC §6654 safe-harbor math, and emits a completed W-4 the user can submit to HR or upload to a payroll platform (Workday, Gusto, ADP, BambooHR, Paychex, paper).

The math is mostly mechanical — most of the judgment is in *which steps the user completes* and *whether their multi-job, dependent, or side-income situation requires the IRS Tax Withholding Estimator instead of the on-form worksheets*. This skill optimizes for the latter — the agent should ask, not guess.

**Form revision.** The step map and worksheets in this skill were verified on 2026-10-06 against the **2026 Form W-4** (Cat. No. 10220Q, created 12/8/25; the instructions, the Step 2(b) Multiple Jobs Worksheet, the Step 4(b) Deductions Worksheet and the page 5 tables are printed on the form) and Pub. 15-T (2026). The form changes every year: re-check the 2027 revision before using this skill for wages paid in 2027 (https://www.irs.gov/forms-pubs/about-form-w-4).

**Companion guide for end users:** [Form W-4 + AI Agent Skill: Employee Withholding Certificate Guide 2026](https://jupid.com/blog/form-w4-employee-withholding-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form W-4, "W-4", "withholding form", or "tax withholding"
- The user is starting a new job and needs to fill out new-hire paperwork
- The user mentions a life event affecting withholding: marriage, divorce, new baby, child turning 17, spouse job change, second job, side gig
- The user asks how to get a bigger paycheck, or complains about owing taxes / underpayment penalty last year
- The user describes two jobs (themselves) or a working spouse (MFJ)
- The user wants to update withholding because they got a large refund or owed a lot

Do **not** engage this skill when:

- The user is a contractor, freelancer, or 1099 worker → use the [`form-w9`](../form-w9/SKILL.md) skill instead
- The user is receiving pension or annuity periodic payments → that's Form W-4P
- The user is taking a nonperiodic distribution or rollover → use the [`form-w-4r`](../form-w-4r/SKILL.md) skill
- The user is a nonresident alien claiming a treaty exemption for wages → that's Form 8233 instead of Form W-4 (Pub. 15 (2026), section 9). A nonresident alien who completes a W-4 must follow Notice 1392 (no exemption claim, Single box, no Step 3 except for certain treaty residents, "Nonresident Alien" or "NRA" written below Step 4(c)); flag this and point the user to Notice 1392 before drafting
- The user wants to make estimated tax payments instead → use the [`form-1040-es`](../form-1040-es/SKILL.md) skill
- The user is asking about state withholding → state forms (CA DE-4, NY IT-2104, etc.) are out of scope

If the user's classification is ambiguous, ask before proceeding. The most common confusion: someone freelancing for one big client thinks they're an "employee" — they're not, unless the client is issuing a W-2.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the W-4 will apply to. Form W-4 is updated annually. The 2026 form applies to wages paid in calendar year 2026.
2. **Filer's legal name and SSN.** Used in Step 1(a)/(b). Must match the Social Security card; if not, the form tells the user to contact SSA so they get credit for their earnings. An ITIN is not accepted in place of an SSN (Pub. 15 (2026), section 4).
3. **Filing status** the user expects to use on their tax return: Single / MFS, MFJ / QSS, or HoH. Do not let the user check HoH unless they confirm: unmarried + paid more than half cost of home + qualifying person lived there more than half the year.
4. **Number of jobs in the household:**
   - Just one job (this one)?
   - Two jobs (this one + a second one for the same person)?
   - MFJ with both spouses working?
5. **Dependents:**
   - Number of qualifying children under age 17 at year-end who are the user's dependents and have an SSN valid for employment
   - Number of other dependents (children 17+, parents, qualifying relatives)
   - Whether the user (or the spouse, if MFJ) has an SSN valid for employment: the 2026 form warns that certain credits and deductions require it (2026 Form W-4, Step 1(c) caution and page 2, Step 3)
6. **Total expected income** for the year — Step 3 applies only if it will be $200,000 or less ($400,000 or less if MFJ) (2026 Form W-4, Step 3). If above, leave Step 3 blank and recommend the Estimator.
7. **Other income without withholding** (annual estimated), split into two groups because the form treats them differently:
   - Not from jobs or self-employment: interest, dividends, capital gains, retirement income, rental income, unemployment, gambling → Step 4(a)
   - Self-employment net profit (side gig, 1099-NEC/1099-K business income) → NOT Step 4(a). The form says to use the Estimator when the user or spouse has self-employment income and to enter the result in Step 4(c); the alternative is Form 1040-ES (2026 Form W-4, Step 2(a) and Step 4(a) instructions)
8. **Deductions Worksheet inputs** (2026 Form W-4, page 4). Ask about each; do not default to $0: qualified tips, qualified overtime (the "and-a-half" portion), qualified passenger vehicle loan interest, age 65 or older (user and spouse), student loan interest / deductible IRA / educator expenses / alimony paid and other Schedule 1 Part II adjustments, expected itemized deductions (medical, state and local taxes, mortgage interest, charity, other), and, if the user will take the standard deduction, cash gifts to charity.
9. **Last year's tax outcome**: refund, balance due, or break-even? Big refund or big balance due means the prior W-4 was off.
10. **Payroll frequency**: weekly (52), biweekly (26), semi-monthly (24), monthly (12), or other. Needed to convert annual extra withholding amounts (Step 4(c)) to per-pay-period amounts.
11. **Exemption question**: does the user want to claim exemption from withholding? Allowed only if they had no federal income tax liability in 2025 AND expect none in 2026 (2026 Form W-4, page 2, "Exemption from withholding").
12. **Date**: is the W-4 being completed after the start of the year? The form recommends the Estimator for mid-year changes, part-year work, and multiple-job situations.

For multi-job households, additionally ask:
- Annual wages from each job (gross, before withholding) and how many jobs in total
- Whether they want to use the IRS Tax Withholding Estimator (most accurate), the Multiple Jobs Worksheet (page 3 of the W-4, tables on page 5), or the Step 2(c) checkbox (only two jobs in total)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the user is a W-2 employee

Confirm they were issued a W-4 by an employer (not a W-9 by a client). Wrong form → redirect to `form-w9` skill.

### Step 2 — Collect filing status and household structure

Determine: filing status, single-job vs multi-job, dependents, side income. Capture in this internal table:

```
| Field                          | Value           |
|--------------------------------|-----------------|
| Filing status                  | MFJ             |
| Employee's annual wages        | $135,000        |
| Spouse working?                | Yes ($48,000)   |
| Other jobs (employee)?         | No              |
| Qualifying children under 17   | 2               |
| Other dependents               | 0               |
| Self-employment net profit     | $14,000 Etsy    |
| Other income (not jobs/SE)     | $0              |
| Itemize?                       | No (standard)   |
| Total household income         | $197,000        |
| Above CTC phaseout ($400K)?    | No              |
```

### Step 3 — Decide which steps the user needs to complete

Apply this decision tree:

- **Step 1**: Always required.
- **Step 2**: Complete if MORE than one job in household (employee has 2+ jobs at the same time OR MFJ with both spouses working). Determine which option (a / b / c) — see Step 4 below.
- **Steps 3 through 4(b)**: Complete on only ONE of the household's W-4s; withholding is most accurate if that is the highest-paying job's W-4 (2026 Form W-4, Step 2 note). Step 3 only if total income will be $200,000 or less ($400,000 or less MFJ).
- **Step 4**: Complete only if user has other income not from jobs or self-employment (4a), a Deductions Worksheet result (4b), or wants extra withholding, including the multiple-jobs or self-employment amount (4c).
- **Exempt from withholding**: only if the user meets both exemption conditions; then complete Steps 1(a), 1(b), and 5 only.
- **Step 5**: Always required.

### Step 4 — For multi-job households, pick the Step 2 method

Three options. Recommend in this order:

**(a) IRS Tax Withholding Estimator** — most accurate (www.irs.gov/W4App, landing page https://www.irs.gov/individuals/tax-withholding-estimator). The form directs users with self-employment income (user or spouse) to this option (2026 Form W-4, Step 2(a)). Walk the user through it with their most recent pay stubs. Output: the amounts to enter, including a Step 4(c) extra-withholding amount.

**(b) Multiple Jobs Worksheet** (worksheet on page 3, tables on page 5) — less accurate than (a) but needs no online tool. Look up the higher-paying job's annual wages (row) and the lower-paying job's annual wages (column) in the page 5 table for the filing status; divide by the higher-paying job's pay periods per year; enter in Step 4(c) of the highest-paying job's W-4. If more than one job pays over $120,000 or there are more than three jobs, the form sends the user to Pub. 505 or the Estimator.

**(c) Step 2(c) checkbox** — only if there are exactly two jobs in total; the box must be checked on both W-4s. Payroll then cuts the standard deduction and tax brackets in half for each job. The form says this is generally more accurate than (b) if the lower-paying job pays more than half of the higher-paying job; otherwise (b) is more accurate (2026 Form W-4, Step 2(c) and page 2).

### Step 5 — Compute Step 3 (dependents)

If under the phaseout AND user has dependents:

```
Qualifying children under 17 × $2,200 = $___
Other dependents             × $500   = $___
Other credits expected (ask; e.g. education, foreign tax credit) = $___
                                          ━━━━━
Total — Step 3                          = $___
```

The $2,200 per child is printed on the 2026 form (OBBBA increase; Rev. Proc. 2025-32 §4.05). Enter on one W-4 only (the highest-paying job's for best accuracy). The other W-4s leave Step 3 blank.

### Step 6 — Compute Step 4 fields

**Step 4(a) — Other income (not from jobs).** Annual amount of expected income without withholding: interest, dividends, retirement income, rental, and similar. Do NOT include wages or self-employment income (2026 Form W-4, Step 4(a) instructions). Step 4(a) adjusts federal income tax withholding only.

**Step 4(b) — Deductions.** Enter Deductions Worksheet line 15 (2026 Form W-4, page 4). It can be more than $0 even for a standard-deduction taker: lines 1a–1c (tips, overtime, car loan interest), lines 3a–3b (age 65+), line 5 (Schedule 1 adjustments) and line 12 (cash gifts to charity) do not depend on itemizing. See [`references/line-by-line.md`](./references/line-by-line.md) for every worksheet line.

**Step 4(c) — Extra withholding per pay period.** Combine: result from the Step 2 method (if any) + any amount for income tax and SE tax on self-employment income (Estimator result, or a projection the user asks the agent to build with Pub. 505 Worksheets 1-3 and 1-5) if the user prefers withholding over Form 1040-ES. Convert annual amounts to per-pay-period using payroll frequency.

### Step 7 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next steps:

- Submit the W-4 to HR/payroll. A new hire's W-4 applies from the first wage payment; a replacement W-4 must be in effect no later than the start of the first payroll period ending on or after the 30th day after the employer receives it (Pub. 15 (2026), section 9).
- If user has self-employment income they did NOT cover via Step 4(c), remind them to set up quarterly Form 1040-ES estimated payments.
- Bookmark the [Tax Withholding Estimator](https://www.irs.gov/individuals/tax-withholding-estimator) for a check-in later in the year and again in early January (the form tells users to recheck at the start of each year).
- Changes that reduce the withholding the user is entitled to (filing status change from MFJ, another job started after using the worksheet or Estimator, losing an expected Child Tax Credit, credits down more than $500, deductions down more than $2,300, no longer exempt) require a new W-4 within 10 days (Pub. 505 (2026), chapter 1). Other changes can be made any time.
- An exemption claim expires: a new W-4 is due by February 16, 2027 to keep it (2026 Form W-4, page 2).

### Step 10 — File the return (optional, if the user wants the agent to submit)

If the agent has browser-automation tooling and the user explicitly authorizes submission, follow [`filing.md`](./filing.md). It contains:

- Decision tree to identify the user's payroll platform (Workday, Gusto, ADP, Paychex, BambooHR, Rippling, paper)
- Field-by-field mapping from this skill's draft to each platform's W-4 entry screen
- Pre-flight checklist (employee ID, SSN re-confirmation, electronic signature consent)
- Post-submission verification: confirm withholding takes effect within 1-2 pay periods
- Security rules — never persist SSN or DOB; require explicit consent at submission

If the user only wants a draft and will enter it themselves, skip this step.

---

## Step-by-step guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Step 1 — Personal Information (Required)

- **1(a)**: Full legal name + address
- **1(b)**: SSN — must match Social Security card; no ITIN
- **1(c)**: Filing status — Single/MFS, MFJ/QSS, or HoH. It sets the standard deduction and rates payroll uses

### Step 2 — Multiple Jobs / Spouse Works (Conditional)

Three options:
- (a) Tax Withholding Estimator → result on Step 4(c); the form's choice when there is self-employment income
- (b) Multiple Jobs Worksheet (page 3; tables on page 5) → line 4 result on Step 4(c) of the highest-paying job's W-4
- (c) Exactly two jobs → check Step 2(c) on both W-4s; generally more accurate than (b) when the lower pay is more than half of the higher pay

**Critical rule**: Complete Steps 3 through 4(b) on only ONE W-4 in the household (most accurate on the highest-paying job's). Leave them blank on the others.

### Step 3 — Dependents (Conditional)

Complete only if total income will be $200,000 or less ($400,000 or less MFJ).

```
Qualifying children under 17 × $2,200
+ Other dependents × $500
+ Other expected credits (ask the user)
= Step 3 total
```

### Step 4 — Other Adjustments (Optional)

- **4(a)**: Annual income not from jobs or self-employment (interest, dividends, retirement income) → extra income tax withholding.
- **4(b)**: Deductions Worksheet line 15 (page 4)
- **4(c)**: Flat per-pay-period extra withholding

### Exempt from withholding (Conditional)

Check the box below Step 4(c) only if the user had no federal income tax liability in 2025 (2025 Form 1040 line 24 is zero or less than lines 27a + 28 + 29 + 30, or no return was required) AND expects none in 2026. Then complete only Steps 1(a), 1(b), and 5. Social security and Medicare tax is still withheld (Pub. 15 (2026), section 9).

### Step 5 — Sign and Date (Required)

The form is not valid unless signed. If the employer has no valid W-4 (and no earlier valid one), it withholds as if the employee checked Single or Married filing separately and made no entries in Steps 2, 3, or 4 (Pub. 15 (2026), section 9).

---

## Validation

Before declaring the W-4 ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Step 1(c) filing status matches the household structure described
- [ ] Step 3 dependents math: (children × $2,200) + (other deps × $500) + other credits = total entered
- [ ] Steps 3 through 4(b) present on only ONE W-4 in the household (if multi-job)
- [ ] Step 4(a) annual amount matches the user's stated other income and contains no wages or self-employment income
- [ ] Step 4(b) equals Deductions Worksheet line 15, and every worksheet line is shown (including zeros)
- [ ] Step 4(c) per-pay amount × pay periods per year ≈ expected annual extra withholding
- [ ] If Step 2(b) Worksheet used: looked up correctly in the page 5 table for the filing status, divided by the highest-paying job's pay periods (worksheet line 3)
- [ ] If exempt box checked: no entries in Steps 2, 3, or 4 (Pub. 15 lets the employer treat such a form as invalid)

### Sanity checks

Surface a warning, do not block:

- [ ] Step 3 claims more children than the user mentioned having
- [ ] Step 3 amount > $0 but household income > phaseout threshold → Step 3 should be $0
- [ ] Step 3 claimed on BOTH spouses' W-4s when filing MFJ → must be on only one
- [ ] Self-employment income entered on Step 4(a) → move it out; use the Estimator → Step 4(c), or Form 1040-ES (Step 4(a) never covers SE tax)
- [ ] User has 2 jobs but Step 2 is blank → high under-withholding risk; flag
- [ ] User says they got a >$3,000 refund last year → over-withholding; suggest reducing Step 4(c) or claiming legitimate Step 3 credits
- [ ] User says they owed >$1,000 last year → under-withholding; suggest higher Step 4(c) and verify Step 2/3/4 are correct
- [ ] Pay frequency × Step 4(c) > annual income gap → over-withholding flag
- [ ] HoH claimed but user is married → not allowed unless the user is "considered unmarried" (lived apart from the spouse for the last 6 months of the year and meets the other Pub. 501 tests)

### Cross-form checks

- [ ] If side gig present, ensure user knows about Schedule C + Schedule SE at filing time (or set up Form 1040-ES quarterly)
- [ ] If user has spouse working, both W-4s must be coordinated (Steps 3 through 4(b) only on one; Step 2(c) on both or neither)
- [ ] If user is over the SS wage base ($184,500 for 2026, SSA) across multiple employers, excess SS tax is claimed on Schedule 3 (Form 1040) line 11 (line number per the 2025 schedule) — note for filing time

---

## Output format

The agent's deliverable is a **filled draft** the user can submit to HR or paste into a payroll platform. Format:

```markdown
# Form W-4 — DRAFT for tax year YYYY

## Step 1 — Personal Information
1(a) Name: <full legal name>
1(a) Address: <street, city, state, zip>
1(b) SSN: <XXX-XX-XXXX>
1(c) Filing status: ☑ Single/MFS | ☐ MFJ/QSS | ☐ HoH

## Step 2 — Multiple Jobs or Spouse Works
Method used: (a) Tax Withholding Estimator | (b) Multiple Jobs Worksheet | (c) Step 2(c) box | N/A
☐ Step 2(c) box checked? Yes | No
(Result of method (a) or (b) goes to Step 4(c) below)

## Step 3 — Dependents
Qualifying children under 17 × $2,200 = $X,XXX
Other dependents × $500              = $XXX
Other credits                        = $X
Total (enter on Step 3):             $X,XXX

## Step 4 — Other Adjustments
4(a) Other income (not from jobs or self-employment): $X,XXX
4(b) Deductions (Deductions Worksheet line 15):     $X,XXX
     Worksheet lines 1a, 1b, 1c, 2, 3a, 3b, 4, 5, 6a–6e, 7, 8a, 8b, 9, 10, 11, 12, 13, 14, 15: <each value, zeros included>
4(c) Extra withholding per pay:       $XXX

## Exempt from withholding: ☐ (if checked, Steps 2–4 must be blank)

## Step 5 — Signature
Signed: <name>
Date: YYYY-MM-DD

## Pay frequency assumed: <weekly | biweekly | semi-monthly | monthly>
## Total annual withholding effect (estimate):
   - From standard table for filing status: $X,XXX
   - From Step 3 (dependent credit reduction): -$X,XXX
   - From Step 4(a) (other income gross-up): +$X,XXX
   - From Step 4(c) (per-pay × periods): +$X,XXX
   ────────────────────────────────────────
   Estimated annual federal income tax withheld: $X,XXX

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Coordination with spouse's W-4: <required actions>
- Side-gig SE tax coverage: <covered via Step 4(c) | requires 1040-ES>

## Submission
Submit to: <employer HR / payroll platform>
Effective: new hire — first wage payment; replacement — no later than the first payroll period ending ≥30 days after receipt
```

The draft is **not** the final filed form. The user still has to submit it to HR or via the payroll platform. The deliverable's value is that every step is computed, traceable, and coordinated across spouses' jobs.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete walkthrough of all five steps, the exempt box, the Multiple Jobs Worksheet and every Deductions Worksheet line
- [`references/multi-job.md`](./references/multi-job.md) — Step 2 methods (Estimator / Worksheet / 2(c) box) with worked examples
- [`references/dependents.md`](./references/dependents.md) — CTC, ODC, phaseout rules, who qualifies as a child vs other dependent
- [`references/side-income.md`](./references/side-income.md) — Step 4(a) vs Form 1040-ES decision tree, SE tax handling
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 W-4 mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for submitting W-4 via Workday / Gusto / ADP / Paychex / BambooHR / paper

## Examples

End-to-end worked W-4s. Use these as patterns when the user's situation is similar.

- [`examples/sarah-single-one-job.md`](./examples/sarah-single-one-job.md) — Single, one job, no dependents, no side income (Steps 1 + 5 only)
- [`examples/marcus-jenna-mfj-both-work.md`](./examples/marcus-jenna-mfj-both-work.md) — MFJ both spouses work, no kids — Step 2(b) worksheet vs Step 2(c) checkbox, computed with Pub. 15-T (2026)
- [`examples/patricia-mfj-kids-side-gig.md`](./examples/patricia-mfj-kids-side-gig.md) — MFJ with two kids + Etsy side gig — Step 2(b) + Step 3 + Step 4(c), self-employment income kept off Step 4(a)

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed — the IRS revises Form W-4 and Pub 15-T each cycle.

- [Form W-4 + AI Agent Skill: Employee Withholding Certificate Guide 2026](https://jupid.com/blog/form-w4-employee-withholding-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form W-4 (2026)](https://www.irs.gov/pub/irs-pdf/fw4.pdf) — the form itself with its instructions (pages 1–2), the Multiple Jobs Worksheet (page 3), the Deductions Worksheet (page 4) and the Multiple Jobs tables (page 5)
- [About Form W-4](https://www.irs.gov/forms-pubs/about-form-w-4) — IRS landing page with archive of past revisions
- [Tax Withholding Estimator](https://www.irs.gov/individuals/tax-withholding-estimator) — interactive tool the IRS recommends for multi-job and side-income households
- [Publication 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) — Employer's Tax Guide, section 9 (W-4 effective dates, missing or invalid W-4, exemption, nonresident aliens, lock-in letters) and section 4 (SSN; no ITIN)
- [Publication 15-T (2026)](https://www.irs.gov/pub/irs-pdf/p15t.pdf) — Federal Income Tax Withholding Methods (Worksheet 1A, the STANDARD and Step 2 Checkbox withholding rate schedules)
- [Publication 505 (2026)](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (10-day rule for changes, Worksheets 1-3 and 1-5)
- [Publication 501](https://www.irs.gov/publications/p501) — Dependents, Standard Deduction, and Filing Information
- [Notice 1392](https://www.irs.gov/pub/irs-pdf/n1392.pdf) — Supplemental Form W-4 Instructions for Nonresident Aliens
- IRC §3402 (income tax collected at source on wages), §3402(f) (withholding certificates), §1 (brackets), §63 (standard deduction), §24 (CTC; §24(b) reduction of $50 per $1,000), §6654 (estimated tax safe harbor), §6682 ($500 civil penalty for a W-4 statement with no reasonable basis that decreases withholding)
- P.L. 119-21 (One Big Beautiful Bill Act, July 4, 2025) — CTC $2,200, Schedule 1-A deductions and the higher SALT limit reflected on the 2026 Deductions Worksheet
- Rev. Proc. 2025-32 — 2026 inflation adjustments (standard deduction $16,100 / $32,200 / $24,150, brackets, CTC $2,200, qualifying-relative gross income $5,300); Rev. Proc. 2024-40 — 2025 adjustments

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (large bonuses, equity compensation, multi-state employment, nonresident alien status) warrant a licensed tax professional's review.
