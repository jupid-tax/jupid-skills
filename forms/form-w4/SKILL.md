---
name: form-w4
description: >
  Use this skill when a W-2 employee needs to fill out, update, or troubleshoot
  IRS Form W-4 (Employee's Withholding Certificate). Triggers on phrases like
  "fill out W-4", "update withholding", "starting a new job", "W-4 for two
  jobs", "claim dependents on W-4", "want bigger paycheck", "underpaid taxes
  last year", "spouse just started working", "got married — update W-4". Do
  NOT use for contractors/freelancers (they need W-9, not W-4), pension
  recipients (Form W-4P), nonperiodic distributions (Form W-4R), or
  nonresident aliens with treaty exemptions (Form 8233 + Notice 1392).
form: Form W-4 (Employee's Withholding Certificate)
audience: [individual, employer]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/fw4.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/fw4.pdf
---

# Form W-4 — Employee's Withholding Certificate

This skill produces an audit-grade W-4 draft from the user's job, dependents, and side-income facts. It walks through the five steps of the form, applies the IRS rules at each step, validates the result against the IRC §6654 safe-harbor math, and emits a completed W-4 the user can submit to HR or upload to a payroll platform (Workday, Gusto, ADP, BambooHR, Paychex, paper).

The math is mostly mechanical — most of the judgment is in *which steps the user completes* and *whether their multi-job, dependent, or side-income situation requires the IRS Tax Withholding Estimator instead of the on-form worksheet*. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Form W-4 Employee Withholding Guide 2026](https://jupid.com/blog/form-w4-employee-withholding-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

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

- The user is a contractor, freelancer, or 1099 worker → use the (forthcoming) `form-w9` skill instead
- The user is receiving pension or annuity periodic payments → that's Form W-4P
- The user is taking a nonperiodic distribution or rollover → that's Form W-4R
- The user is a nonresident alien with treaty benefits → that's Form 8233 + a modified W-4 per Notice 1392
- The user wants to make estimated tax payments instead → use the (forthcoming) `form-1040-es` skill
- The user is asking about state withholding → state forms (CA DE-4, NY IT-2104, etc.) are out of scope

If the user's classification is ambiguous, ask before proceeding. The most common confusion: someone freelancing for one big client thinks they're an "employee" — they're not, unless the client is issuing a W-2.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the W-4 will apply to. Form W-4 is updated annually. The 2026 form applies to wages paid in calendar year 2026.
2. **Filer's legal name and SSN.** Used in Step 1(a)/(b). Must match Social Security card exactly.
3. **Filing status** the user expects to use on their tax return: Single / MFS, MFJ / QSS, or HoH. Do not let the user check HoH unless they confirm: unmarried + paid more than half cost of home + qualifying person lived there more than half the year.
4. **Number of jobs in the household:**
   - Just one job (this one)?
   - Two jobs (this one + a second one for the same person)?
   - MFJ with both spouses working?
5. **Dependents:**
   - Number of qualifying children under age 17 at year-end with a valid SSN
   - Number of other dependents (children 17+, parents, qualifying relatives)
6. **Total expected household income** for the year — needed to check whether the user is below the CTC phaseout ($200K single/HoH/MFS, $400K MFJ). If above, Step 3 must be $0.
7. **Other income without withholding** (annual estimated):
   - Side gig / 1099 / freelance net profit
   - Interest, dividends, capital gains
   - Rental income
   - Unemployment, gambling, etc.
8. **Itemized deductions** (only if user explicitly says they itemize via Schedule A; otherwise default to standard deduction).
9. **Last year's tax outcome**: refund, balance due, or break-even? Big refund or big balance due means the prior W-4 was off.
10. **Payroll frequency**: weekly (52), biweekly (26), semi-monthly (24), monthly (12), or other. Needed to convert annual extra withholding amounts (Step 4(c)) to per-pay-period amounts.

For multi-job households, additionally ask:
- Annual wages from each job (gross, before withholding)
- Whether they want to use the IRS Tax Withholding Estimator (recommended), the Multiple Jobs Worksheet (Page 3 of W-4), or the Step 2(c) checkbox (only if both jobs pay similarly)

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
| Other (non-wage) income        | $14,000 Etsy    |
| Itemize?                       | No (standard)   |
| Total household income         | $197,000        |
| Above CTC phaseout ($400K)?    | No              |
```

### Step 3 — Decide which steps the user needs to complete

Apply this decision tree:

- **Step 1**: Always required.
- **Step 2**: Complete if MORE than one job in household (employee has 2+ jobs OR MFJ with both spouses working). Determine which option (a / b / c) — see Step 4 below.
- **Step 3**: Complete ONLY on the highest-paying job's W-4, AND ONLY if total household income is under the phaseout ($200K single/HoH/MFS, $400K MFJ).
- **Step 4**: Complete only if user has other income (4a), itemized deductions above standard (4b), or wants extra withholding (4c).
- **Step 5**: Always required.

### Step 4 — For multi-job households, pick the Step 2 method

Three options. Recommend in this order:

**(a) IRS Tax Withholding Estimator** — most precise. URL: https://www.irs.gov/individuals/tax-withholding-estimator. Walk the user through it with their YTD pay stubs. Output: a recommended Step 4(c) extra-withholding amount.

**(b) Multiple Jobs Worksheet (Page 3 of W-4)** — less precise but doesn't require online tool. Use when user can't access the estimator. Look up the higher-paying and lower-paying job's annual wages in the Page-3 table for their filing status. Result goes on Step 4(c) of the higher-paying job's W-4.

**(c) Step 2(c) checkbox** — only if user has exactly two jobs total AND the pay at both is roughly similar (within ~10%). Each employer applies a higher-bracket rate. Simplest but tends to over-withhold.

### Step 5 — Compute Step 3 (dependents)

If under the phaseout AND user has dependents:

```
Qualifying children under 17 × $2,000 = $___
Other dependents             × $500   = $___
Other credits expected (rare; mostly $0) = $___
                                          ━━━━━
Total — Step 3                          = $___
```

Enter on the higher-paying job's W-4 only. Other spouse leaves Step 3 blank.

### Step 6 — Compute Step 4 fields

**Step 4(a) — Other income.** Annual amount of expected non-wage income (interest, dividends, side gig, rental). Note: this only adjusts federal income tax withholding. It does NOT cover the 15.3% self-employment tax for side-gig income — flag this to the user; they need either a higher Step 4(c) or quarterly Form 1040-ES.

**Step 4(b) — Deductions above standard.** Use the Deductions Worksheet on Page 3 of the W-4. Default to $0 if the user takes the standard deduction (90% of filers).

**Step 4(c) — Extra withholding per pay period.** Combine: result from Step 2 multi-job method (if any) + any extra to cover SE tax on side gig (if user prefers W-4 over 1040-ES). Convert annual amounts to per-pay-period using payroll frequency.

### Step 7 — Run validation checks

See **Validation** below. Run every check. Don't skip checks even if the math looks clean.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next steps:

- Submit the W-4 to HR/payroll. The employer must implement by the start of the first payroll period ending on or after the 30th day after receipt.
- If user has side-gig income they did NOT cover via Step 4(a)/(c), remind them to set up quarterly Form 1040-ES estimated payments.
- Bookmark the [Tax Withholding Estimator](https://www.irs.gov/individuals/tax-withholding-estimator) for an October check-in to verify projection.
- Plan to revisit the W-4 within 30 days of any life change (marriage, baby, second job, etc.).

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
- **1(b)**: SSN — must match Social Security card exactly
- **1(c)**: Filing status — Single/MFS, MFJ/QSS, or HoH

### Step 2 — Multiple Jobs / Spouse Works (Conditional)

Three options:
- (a) Tax Withholding Estimator → result on Step 4(c)
- (b) Multiple Jobs Worksheet (Page 3) → result on Step 4(c)
- (c) Both jobs similar pay → check Step 2(c) on both W-4s

**Critical rule**: If completing Step 2, do NOT also complete Steps 3 and 4 on the lower-paying job's W-4. Only the highest-paying job claims dependents and adjustments.

### Step 3 — Dependents (Conditional)

Skip if total income > $200K single/HoH/MFS or > $400K MFJ (CTC phases out).

```
Qualifying children under 17 × $2,000
+ Other dependents × $500
+ Other expected credits (default $0)
= Step 3 total
```

### Step 4 — Other Adjustments (Optional)

- **4(a)**: Annual non-wage income → triggers extra income tax withholding to cover it. Does NOT cover SE tax.
- **4(b)**: Itemized deductions above standard (Page 3 worksheet)
- **4(c)**: Flat per-pay-period extra withholding

### Step 5 — Sign and Date (Required)

Without signature the form is invalid. Employer must withhold at the highest single-no-adjustments rate.

---

## Validation

Before declaring the W-4 ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Step 1(c) filing status matches the household structure described
- [ ] Step 3 dependents math: (children × $2,000) + (other deps × $500) + other credits = total entered
- [ ] Step 3 only present on the HIGHEST-paying job's W-4 (if multi-job)
- [ ] Step 4(a) annual amount is reasonable given user's stated other income
- [ ] Step 4(c) per-pay amount × pay periods per year ≈ expected annual extra withholding
- [ ] If Step 2(b) Worksheet used: looked up correctly in Page 3 table for filing status

### Sanity checks

Surface a warning, do not block:

- [ ] Step 3 claims more children than the user mentioned having
- [ ] Step 3 amount > $0 but household income > phaseout threshold → Step 3 should be $0
- [ ] Step 3 claimed on BOTH spouses' W-4s when filing MFJ → must be on only one
- [ ] Step 4(a) > $0 from a side gig but user did not factor in SE tax → flag and suggest either higher Step 4(c) or 1040-ES
- [ ] User has 2 jobs but Step 2 is blank → high under-withholding risk; flag
- [ ] User says they got a >$3,000 refund last year → over-withholding; suggest reducing Step 4(c) or claiming legitimate Step 3 credits
- [ ] User says they owed >$1,000 last year → under-withholding; suggest higher Step 4(c) and verify Step 2/3/4 are correct
- [ ] Pay frequency × Step 4(c) > annual income gap → over-withholding flag
- [ ] HoH claimed but user is married → not allowed

### Cross-form checks

- [ ] If side gig present, ensure user knows about Schedule C + Schedule SE at filing time (or set up Form 1040-ES quarterly)
- [ ] If user has spouse working, both W-4s must be coordinated (Step 3 only on one)
- [ ] If user is over the SS wage base across multiple jobs, excess SS tax can be reclaimed on Form 1040 Line 11 of Schedule 3 — note for filing time

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
Qualifying children under 17 × $2,000 = $X,XXX
Other dependents × $500              = $XXX
Other credits                        = $X
Total (enter on Step 3):             $X,XXX

## Step 4 — Other Adjustments
4(a) Other income (not from jobs):    $X,XXX
4(b) Deductions:                      $X,XXX
4(c) Extra withholding per pay:       $XXX

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
Effective: first payroll period ending ≥30 days after submission
```

The draft is **not** the final filed form. The user still has to submit it to HR or via the payroll platform. The deliverable's value is that every step is computed, traceable, and coordinated across spouses' jobs.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete walkthrough of all five steps with examples and edge cases
- [`references/multi-job.md`](./references/multi-job.md) — Step 2 methods (Estimator / Worksheet / 2(c) box) with worked examples
- [`references/dependents.md`](./references/dependents.md) — CTC, ODC, phaseout rules, who qualifies as a child vs other dependent
- [`references/side-income.md`](./references/side-income.md) — Step 4(a) vs Form 1040-ES decision tree, SE tax handling
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 W-4 mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for submitting W-4 via Workday / Gusto / ADP / Paychex / BambooHR / paper

## Examples

End-to-end worked W-4s. Use these as patterns when the user's situation is similar.

- [`examples/sarah-single-one-job.md`](./examples/sarah-single-one-job.md) — Single, one job, no dependents, no side income (Steps 1 + 5 only)
- [`examples/marcus-jenna-mfj-both-work.md`](./examples/marcus-jenna-mfj-both-work.md) — MFJ both spouses work, no kids — coordinated Step 2 + 4(c)
- [`examples/patricia-mfj-kids-side-gig.md`](./examples/patricia-mfj-kids-side-gig.md) — MFJ with two kids + Etsy side gig — Step 3 + Step 4(a)/(c) full treatment

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed — the IRS revises Form W-4 and Pub 15-T each cycle.

- [Form W-4 Employee Withholding Guide 2026](https://jupid.com/blog/form-w4-employee-withholding-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form W-4 (latest)](https://www.irs.gov/pub/irs-pdf/fw4.pdf) — the form itself with embedded instructions and Page 3 worksheets
- [About Form W-4](https://www.irs.gov/forms-pubs/about-form-w-4) — IRS landing page with archive of past revisions
- [Tax Withholding Estimator](https://www.irs.gov/individuals/tax-withholding-estimator) — interactive tool the IRS recommends for multi-job and side-income households
- [Publication 15](https://www.irs.gov/pub/irs-pdf/p15.pdf) — Employer's Tax Guide
- [Publication 15-T](https://www.irs.gov/pub/irs-pdf/p15t.pdf) — Federal Income Tax Withholding Methods (the tables employers use)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax
- [Publication 501](https://www.irs.gov/publications/p501) — Dependents, Standard Deduction, and Filing Information
- IRC §3402 (income tax collected at source on wages), §3402(f) (W-4 accuracy requirement), §1 (brackets), §63 (standard deduction), §24 (CTC), §6654 (estimated tax safe harbor)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (large bonuses, equity compensation, multi-state employment, nonresident alien status) warrant a licensed tax professional's review.
