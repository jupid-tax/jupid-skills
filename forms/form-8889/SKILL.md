---
name: form-8889
description: |
  Use this skill when a taxpayer with an HSA needs to file Form 8889 (Health Savings Accounts) with their Form 1040 for tax year 2026. Triggers: "fill out Form 8889", "claim HSA deduction", "report HSA contributions on tax return", "HSA distribution tax", "I have an HSA, what tax form".

  Do NOT use for: FSA (no separate form, employer reports), 401(k) (no special form), Archer MSA or Medicare Advantage MSA (Form 8853), the 6% excise tax on excess HSA contributions (use form-5329), or checking a custodian's Form 1099-SA / 5498-SA on its own (use form-1099-sa / form-5498-sa).
form: Form 8889
audience: [individual, solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8889.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8889.pdf
---

# Form 8889 — Health Savings Accounts (HSAs)

This skill produces an audit-grade draft of Form 8889 from the user's HSA contributions, distributions, and HDHP coverage facts. It walks through Part I (contributions and the deduction), Part II (distributions and taxability), and Part III (failure to maintain HDHP coverage after the last-month rule), validates the math, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mechanical. The judgment is in *eligibility month-by-month*, *which contributions belong on Line 2 vs. Line 9*, and *whether a distribution is qualified*. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Form 8889 + AI Agent Skill: HSA Contributions Guide 2026](https://jupid.com/blog/form-8889-hsa-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision.** The line map was verified against the 2025 Form 8889 (created 3/28/25) and the 2025 Instructions for Form 8889 (Nov 25, 2025), filed in 2026. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-8889 before using this skill for a 2026 return.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8889, "HSA tax form", or "Health Savings Account on my return"
- The user describes HSA activity: contributions made directly, employer HSA contributions on W-2 Box 12 code W, a 1099-SA from an HSA custodian, a 5498-SA, or a one-time IRA-to-HSA funding distribution
- The user asks "do I owe tax on my HSA withdrawal" or "is X a qualified medical expense"
- The user used the **last-month rule** in a prior year and may have failed the testing period

Do **not** engage this skill when:

- The user has a Flexible Spending Account (FSA) — no separate IRS form; the employer reports it. FSAs and HSAs are mutually exclusive in most cases.
- The user has an Archer Medical Savings Account (MSA) — that uses Form 8853, not 8889. The Archer MSA program is closed to new enrollees.
- The user has a Medicare Advantage MSA — also Form 8853.
- The user is asking about a 401(k), Traditional IRA, or Roth IRA — different forms and rules.
- The user wants to deduct medical expenses they paid out of pocket — that's Schedule A itemized medical, not Form 8889.

If the user has both an HSA and a general-purpose FSA in the same year, ASK — having a general-purpose FSA disqualifies HSA eligibility for that month, which materially affects the contribution limit.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 8889 for tax year 2025 is filed in 2026; for 2026, in 2027. Contribution limits and HDHP minimums depend on this year.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 8889 header. Each spouse files a separate Form 8889 if both have HSAs — do not combine.
3. **HDHP coverage type for each month** — self-only, family, or none. Coverage status on the **first day of each month** determines that month's contribution allowance. For months beginning after December 31, 2025, a bronze or catastrophic plan available as individual coverage through a Marketplace counts as an HDHP even if it misses the deductible and out-of-pocket figures (IRC §223(c)(2)(H), added by P.L. 119-21 §71307; Notice 2026-5 Q&A-4). For 2026 and later, ASK whether the user's plan is a Marketplace bronze or catastrophic plan before testing it against the HDHP minimums.
4. **HSA contributions made directly** (outside payroll) — from bank statements or HSA custodian's year-end statement.
5. **Employer HSA contributions** — from W-2 Box 12, code W. Includes cafeteria-plan (Section 125) contributions, which are technically employer contributions for tax purposes.
6. **1099-SA distributions** — total distributions from the HSA in the tax year (Box 1) and distribution code (Box 3).
7. **Qualified medical expenses paid from the HSA** — itemized list with dates, amounts, and brief description (doctor visit, prescription, dental, etc.). Each item must be on the IRC §213(d) / Pub 502 list (see [`references/qualified-medical-expenses.md`](./references/qualified-medical-expenses.md)).
8. **Age** — relevant for the catch-up contribution (55+) and the 20% penalty exception (65+).
9. **Medicare enrollment status and effective date** — Medicare enrollment (any part) disqualifies HSA contributions starting that month, including periods of retroactive coverage (Pub. 969 (2025), "Enrolled in Medicare"). Premium-free Part A taken after 65 starts **6 months back** from the sign-up or Social Security application, but not before the month the person turned 65 (https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start) — ASK about this if the user is 65+ or recently took Social Security.
10. **Other disqualifying coverage** — general-purpose FSA on the user or spouse, TRICARE, second non-HDHP plan via spouse's employer, dependent status on someone else's return. Not disqualifying: telehealth and other remote care coverage (IRC §223(c)(1)(B), plan years beginning after 2024), and, for months beginning after December 31, 2025, a direct primary care arrangement whose fees total no more than $150 a month ($300 if it covers more than one person) (IRC §223(c)(1)(E); Notice 2026-5).

Additionally ask, when relevant:

- **Last-month rule status**: If the user wasn't HSA-eligible all 12 months but was eligible on December 1, did they (or do they want to) use the last-month rule? Document opt-in explicitly.
- **Prior-year last-month rule**: If used in the prior year, did they remain HSA-eligible for the full 12-month testing period? If not, Part III applies.
- **Married filing jointly with two HSAs**: Each spouse files a separate 8889. Confirm whether the family contribution limit was split between them and document the split.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm HDHP coverage month-by-month

Build a 12-month table. For each month, record: (a) HDHP coverage type (self-only / family / none), (b) other disqualifying coverage (Y/N), (c) Medicare enrollment (Y/N), (d) dependent status (Y/N).

If coverage was the same all 12 months, this is one row. If it changed, walk every month. Do NOT default to "same all year" without asking.

### Step 2 — Determine HSA-eligibility for each month

A month counts as HSA-eligible only if **all four** are true on the first day of that month: HDHP coverage, no disqualifying coverage, no Medicare enrollment, not a dependent. See [`references/eligibility.md`](./references/eligibility.md).

### Step 3 — Compute the contribution limit (Line 3)

If eligible all 12 months with the same coverage: full annual limit (self-only or family per Step 1). If the user is 55+ at year-end and unmarried, or married with self-only coverage all year, add the $1,000 additional contribution on Line 3 (married with family coverage: it goes on Line 7 instead). Otherwise:

- **Not eligible on December 1**: Line 3 = Line 3 Limitation Chart and Worksheet total ÷ 12. Each month takes the coverage on the first day of that month ($4,300 self-only / $8,550 family for 2025; $5,300 / $9,550 if 55+, the $9,550 figure only if unmarried).
- **Eligible on December 1 (last-month rule)**: the user is treated as eligible for the whole year with the December 1 coverage. Line 3 = the greater of the worksheet result or the full amount for the December 1 coverage (2025 Instructions for Form 8889, Line 3 rules 2–5). **This starts a testing period from December 1 through December 31 of the next year** — if eligibility breaks during testing (other than death or disability), the contributions that exceed the worksheet amount are included in income in the year of failure plus a 10% additional tax (Part III).

If partial-year, **ASK how much the user contributed above the worksheet amount** and whether they expect to stay HSA-eligible through December 31 of next year. Only the part above the worksheet amount is exposed to the testing period. See [`references/contribution-limits.md`](./references/contribution-limits.md) for worked examples.

### Step 4 — Collect contributions and split between Line 2 and Line 9

- **Line 2**: contributions the user made *directly* (bank transfer, check, post-tax payroll deduction routed by the user). Comes from HSA custodian's year-end statement minus W-2 Box 12 W.
- **Line 9**: employer contributions, including cafeteria-plan (Section 125) contributions. Comes from W-2 Box 12 code W.

Cafeteria-plan contributions are **already excluded from Box 1 wages** — they cannot be deducted again on Line 13. Putting them on Line 2 is a frequent error.

If a contribution was made between January 1 and April 15 of the *next* year, ASK whether the user designated it for the prior year or current year. Custodians typically default to the current year unless the user specifies otherwise on the deposit slip. The IRS allows prior-year designation up to the unextended filing deadline (April 15).

### Step 5 — Compute Part I deduction (Lines 1–13)

```
Line 1  : Self-only / Family (plan in effect longer; Family if family coverage on Dec 1)
Line 2  : Direct contributions from user
Line 3  : Annual contribution limit (from Step 3)
Line 4  : Archer MSA contributions (almost always $0)
Line 5  : Line 3 − Line 4 (not less than 0)
Line 6  : Line 5 (or allocated share if spouses have separate HSAs and family coverage)
Line 7  : Additional contribution — only if 55+, married, and family coverage
Line 8  : Line 6 + Line 7
Line 9  : Employer contributions (W-2 Box 12 code W, incl. cafeteria plan)
Line 10 : Qualified HSA funding distribution (one-time IRA-to-HSA)
Line 11 : Line 9 + Line 10
Line 12 : Line 8 − Line 11 (not less than 0)
Line 13 : Smaller of Line 2 or Line 12  ← HSA deduction
```

Line 13 flows to **Schedule 1, Line 13** (HSA deduction). Above-the-line, no itemizing required.

If Line 2 > Line 13, the difference is an **excess contribution** (excess employer contributions are measured against Line 8 separately). The user can withdraw the excess plus earnings by the due date of the return, including extensions, and report the earnings as other income for the year of withdrawal; otherwise a **6% excise tax applies for every year** the excess remains. File Form 5329 Part VII to compute. See [`references/common-mistakes.md`](./references/common-mistakes.md).

### Step 6 — Compute Part II distributions (Lines 14a–17b)

```
Line 14a : Total distributions from 1099-SA Box 1
Line 14b : Rollovers to another HSA + excess contributions (and earnings) withdrawn by the due date incl. extensions
Line 14c : Line 14a − Line 14b
Line 15  : Qualified medical expenses paid from HSA
Line 16  : Line 14c − Line 15  (taxable portion)
Line 17a : Exceptions box (distribution after death, disability, or age 65)
Line 17b : Line 16 × 20%  (additional tax, unless 17a applies)
```

Every dollar on 1099-SA Box 1 must appear on Line 14a. Failing to report triggers a CP2000 notice within 12–18 months.

Line 16 flows to **Schedule 1, Line 8f** (Other income). Line 17b flows to **Schedule 2, Line 17c** (additional tax on HSA distributions).

The 20% penalty does NOT apply to distributions made after the account beneficiary dies, becomes disabled per IRC §72(m)(7), or turns age 65 (IRC §223(f)(4)(B)–(C)). After 65, non-qualified distributions are taxed as ordinary income but no 20% penalty.

A mistaken distribution the user repaid does not go on Line 14b: the custodian leaves it off Form 1099-SA or corrects the form (Instructions for Forms 1099-SA and 5498-SA, "HSA Mistaken Distributions").

For the qualified-expense determination, see [`references/qualified-medical-expenses.md`](./references/qualified-medical-expenses.md).

### Step 7 — Compute Part III if applicable (Lines 18–21)

Only complete Part III if the user failed to stay an eligible individual (other than because of death or disability) during a testing period that started with either:
1. The last-month rule in a **prior** year (testing period December 1 through December 31 of the following year), or
2. A qualified HSA funding distribution (testing period from the month of the transfer through the last day of the 12th month after it).

If either applies, Line 18 = contributions above what the Line 3 worksheet would have allowed without the last-month rule, Line 19 = the qualified HSA funding distribution, Line 20 = Line 18 + Line 19 (income), Line 21 = Line 20 × 10% (separate from the 20% non-qualified-distribution tax).

If the user was HSA-eligible all of the testing period, skip Part III entirely.

If the user is invoking the last-month rule for the *first* time in the current year, Part III does NOT apply this year. They must monitor eligibility for the next 12 months and complete Part III on next year's return only if eligibility breaks.

### Step 8 — Run validation checks

See **Validation** below. Run every check.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next forms the user will need:

- **Line 13 > 0** → Schedule 1, Line 13 (HSA deduction)
- **Line 16 > 0** → Schedule 1, Line 8f (taxable HSA distribution as other income)
- **Line 17b > 0** → Schedule 2, Line 17c (20% additional tax)
- **Line 20 > 0** → Schedule 1, Line 8f; **Line 21 > 0** → Schedule 2, Line 17d (10% additional tax)
- **Excess contributions not withdrawn by deadline** → Form 5329 (6% excise tax)
- **Married filing jointly with two HSAs** → second Form 8889 for the spouse
- **Form 8889 must be attached to Form 1040** in attachment-sequence order

### Step 11 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). It contains the Free File / FFFF / paid software / paper decision tree, field-by-field mapping, pre-flight checklist, submission state machine, and security rules.

If the user only wants a draft, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name** — filer's legal name (the HSA owner; not spouse)
- **SSN** — filer's SSN. If MFJ with two HSAs, each spouse uses their own SSN on their own 8889.

### Part I — Contributions

- **Line 1** — Self-only or Family box. If the user had both during the year, check the plan in effect for the longer period; if they had family coverage on the first day of the last month (December 1), check Family. Spouses where either has family coverage are both treated as family. If coverage type changed mid-year, see [`references/contribution-limits.md`](./references/contribution-limits.md).
- **Line 2** — Direct contributions only, including those made by April 15, 2026 for 2025. Exclude Line 9 amounts, rollovers, and Line 10.
- **Line 3** — Annual limit (full year or worksheet). For 2025: $4,300 self-only / $8,550 family (Rev. Proc. 2024-25). For 2026: $4,400 / $8,750 (Rev. Proc. 2025-19). Add $1,000 here if 55+ and unmarried or self-only all year.
- **Line 4** — Archer MSA, almost always $0.
- **Line 5** = Line 3 − Line 4
- **Line 6** = Line 5 (or split share if MFJ family-coverage spouses agreed to split)
- **Line 7** — Additional contribution only if the user was 55+ at year-end, married, and the user or spouse had family coverage: $1,000 × eligible months ÷ 12. Each spouse age 55+ gets their own, but it must go into their **own** HSA, not the spouse's.
- **Line 8** = Line 6 + Line 7
- **Line 9** — Employer contributions from W-2 Box 12 code W
- **Line 10** — One-time qualified HSA funding distribution from IRA. Niche.
- **Line 11** = Line 9 + Line 10
- **Line 12** = Line 8 − Line 11; if zero or less, enter -0-
- **Line 13** = Smaller of Line 2 or Line 12. **HSA deduction → Schedule 1 Line 13.**

### Part II — Distributions

- **Line 14a** — From 1099-SA Box 1
- **Line 14b** — Rollovers to another HSA, plus excess contributions and their earnings withdrawn by the due date including extensions
- **Line 14c** = Line 14a − Line 14b
- **Line 15** — Qualified medical expenses paid from HSA in this year
- **Line 16** = Line 14c − Line 15. **Flows to Schedule 1, Line 8f.**
- **Line 17a** — Check if exception applies (death, disability, 65+)
- **Line 17b** = Line 16 × 20% if no exception. **Flows to Schedule 2, Line 17c.**

### Part III — Failure to maintain HDHP coverage

- **Line 18** — Last-month rule: amount contributed minus the amount the Line 3 worksheet allows for that year without the rule
- **Line 19** — Qualified HSA funding distribution whose testing period failed
- **Line 20** — Line 18 + Line 19. **Flows to Schedule 1, Line 8f.**
- **Line 21** — Line 20 × 10% additional tax. **Flows to Schedule 2, Line 17d.**

Only complete if a last-month-rule or funding-distribution testing period failed this year.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 5 = Line 3 − Line 4
- [ ] Line 8 = Line 6 + Line 7
- [ ] Line 11 = Line 9 + Line 10
- [ ] Line 12 = max(0, Line 8 − Line 11)
- [ ] Line 13 = min(Line 2, Line 12)
- [ ] Line 14c = Line 14a − Line 14b
- [ ] Line 16 = Line 14c − Line 15, but not less than 0
- [ ] Line 17b = Line 16 × 0.20, unless 17a exception applies
- [ ] If Part III used: Line 21 = Line 20 × 0.10

### Sanity checks

Surface a warning if any of these are true:

- [ ] Line 2 > Line 13, or Line 9 + Line 10 > Line 8 → excess contribution; user must withdraw or pay 6% excise tax annually (Form 5329)
- [ ] Line 7 entered but user is under 55, unmarried, or had no family coverage → the additional amount belongs on Line 3 (or nowhere)
- [ ] Line 7 entered into a spouse's HSA → catch-up must go into the user's own HSA
- [ ] Coverage type changed mid-year and Line 3 = full annual limit → confirm the user had that coverage on December 1 and knows about the testing period
- [ ] Last-month rule invoked but user not HSA-eligible on December 1 → not allowed
- [ ] Plan treated as HDHP only because it is a Marketplace bronze/catastrophic plan → allowed for months from January 2026 only
- [ ] Line 9 looks like a cafeteria-plan contribution but user also reports same amount on Line 2 → double-counting; remove from Line 2
- [ ] User is 65+ and contributed to HSA → confirm Medicare enrollment status; Medicare disqualifies contributions retroactively
- [ ] Line 14a = 0 but user mentioned receiving 1099-SA → 1099-SA must be reported; cross-check
- [ ] Line 15 includes a non-qualified expense (gym, vitamins, cosmetic, individual-market premiums for under-65) → recategorize to Line 16
- [ ] User has both HSA contributions and a general-purpose FSA → ineligible for HSA contribution months when FSA active
- [ ] MFJ family-HDHP with both spouses claiming the full family limit ($8,550 for 2025, $8,750 for 2026) → family limit is shared, not doubled

### Cross-form checks

- [ ] If Line 13 > 0, Schedule 1 Line 13 must reflect the deduction
- [ ] If Line 16 > 0, Schedule 1 Line 8f must reflect the taxable amount
- [ ] If Line 17b > 0, Schedule 2 Line 17c must reflect the 20% tax
- [ ] If Line 21 > 0, Schedule 2 Line 17d must reflect the 10% tax
- [ ] If excess contribution: Form 5329 Part VII (excess HSA contributions)
- [ ] If MFJ with two HSAs: two separate Form 8889s, one per spouse, each with own SSN

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 8889 or paste into tax software. Format:

```markdown
# Form 8889 — DRAFT for tax year YYYY

## Header
Name of HSA owner: <filer name>
SSN: <filer SSN>
Coverage indicator (Line 1): Self-only | Family

## Part I — HSA Contributions
 1. HDHP coverage box:                 Self-only | Family
 2. HSA contributions (direct):        $X,XXX
 3. Contribution limit:                $X,XXX
 4. Archer MSA contributions:          $0
 5. Line 3 − Line 4:                   $X,XXX
 6. Line 5 (or allocated share):       $X,XXX
 7. Additional contribution (55+, married, family): $X,XXX
 8. Line 6 + Line 7:                   $X,XXX
 9. Employer contributions (W-2 12 W): $X,XXX
10. Qualified HSA funding distribution: $X,XXX
11. Line 9 + Line 10:                  $X,XXX
12. Line 8 − Line 11 (not < 0):        $X,XXX
13. HSA deduction (Schedule 1 L13):    $X,XXX

## Part II — HSA Distributions
14a. Total distributions (1099-SA):    $X,XXX
14b. Excess returns + rollovers:       $X,XXX
14c. Line 14a − Line 14b:              $X,XXX
15. Qualified medical expenses:        $X,XXX
16. Taxable HSA distributions:         $X,XXX
       → Schedule 1, Line 8f
17a. Exception (death/disabled/65+):   Yes | No
17b. Additional 20% tax:               $X,XXX
       → Schedule 2, Line 17c

## Part III — Failure to Maintain HDHP Coverage
   (Skip unless a last-month-rule or funding-distribution testing period failed)
18. Last-month rule excess:            $X,XXX
19. Qualified HSA funding distribution: $X,XXX
20. Total income (→ Schedule 1, 8f):   $X,XXX
21. Additional 10% tax (→ Schedule 2, 17d): $X,XXX

## Eligibility table (working — not transcribed to form)
| Month     | HDHP coverage | Other coverage | Medicare | Dependent | Eligible? |
|-----------|---------------|----------------|----------|-----------|-----------|
| January   | Family        | None           | No       | No        | Yes       |
| ...       | ...           | ...            | ...      | ...       | ...       |

## Required attachments
- [ ] Form 8889 attached to Form 1040
- [ ] Form 5329 (if excess contributions not withdrawn)
- [ ] Spouse's Form 8889 (if MFJ with two HSAs)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 8889 (revision date YYYY-MM)
- IRS Instructions for Form 8889 (revision date YYYY-MM)
- IRC §223 (Health Savings Accounts)
- IRC §213(d) (medical care definition)
- Rev. Proc. 2024-25 (2025 limits) / Rev. Proc. 2025-19 (2026 limits)
- IRS Publication 969, Publication 502
```

The draft is **not** the final filed form. The user transcribes it into Form 1040 e-file software or paper Form 8889. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line of Parts I, II, III with examples and edge cases
- [`references/eligibility.md`](./references/eligibility.md) — HDHP requirements + ineligibility (Medicare, other coverage, dependent status)
- [`references/contribution-limits.md`](./references/contribution-limits.md) — Full chart with last-month rule, partial-year proration, MFJ family-limit splitting
- [`references/qualified-medical-expenses.md`](./references/qualified-medical-expenses.md) — Per Pub 502 (doctor, prescription, dental, vision, mental health, long-term care, COBRA, post-65 Medicare A/B/D)
- [`references/triple-tax-advantage.md`](./references/triple-tax-advantage.md) — Strategy: contribute, invest, save receipts, withdraw later
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 8889 with the 1040 (Free File / FFFF / paid software / paper)

## Examples

End-to-end worked Form 8889s. Use these as patterns when the user's situation is similar.

- [`examples/family-hdhp-investing-for-retirement.md`](./examples/family-hdhp-investing-for-retirement.md) — Daniel + Lisa, family HDHP, max contribution, no distributions, paying medical from cash to invest the HSA
- [`examples/self-only-young-saver.md`](./examples/self-only-young-saver.md) — 28-year-old maxing self-only contributions through cafeteria plan
- [`examples/medicare-eligible-with-existing-hsa.md`](./examples/medicare-eligible-with-existing-hsa.md) — 65-year-old just enrolled in Medicare, can no longer contribute, can still distribute

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed — the IRS publishes a new Revenue Procedure for HSA limits each year (typically May or June for the following year).

- [Form 8889 + AI Agent Skill: HSA Contributions Guide 2026](https://jupid.com/blog/form-8889-hsa-2026) — Jupid's narrative companion to this skill
- [Form 8889 (latest)](https://www.irs.gov/pub/irs-pdf/f8889.pdf) — the form itself
- [Instructions for Form 8889 (latest)](https://www.irs.gov/pub/irs-pdf/i8889.pdf) — line-by-line IRS guidance with the Limitation Chart and Worksheet
- [About Form 8889](https://www.irs.gov/forms-pubs/about-form-8889) — IRS landing page with archive of past revisions
- [Form 1099-SA](https://www.irs.gov/forms-pubs/about-form-1099-sa) — Distributions From an HSA
- [Form 5498-SA](https://www.irs.gov/forms-pubs/about-form-5498-sa) — HSA, Archer MSA, or Medicare Advantage MSA Information
- [Form 5329](https://www.irs.gov/pub/irs-pdf/f5329.pdf) — Additional Taxes on Qualified Plans (excess HSA contributions, Part VII)
- [Schedule 1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) — where Line 13 deduction and Line 8f taxable distribution land
- [Schedule 2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) — where Line 17c additional 20% tax lands
- [Publication 969](https://www.irs.gov/publications/p969) — Health Savings Accounts and Other Tax-Favored Health Plans
- [Publication 502](https://www.irs.gov/publications/p502) — Medical and Dental Expenses (qualified expense list)
- IRC §223 (HSA eligibility, limits, distributions), §213(d) (medical care definition), §125 (cafeteria plans), §72(m)(7) (disability for penalty exception)
- Rev. Proc. 2024-25 — 2025 inflation-adjusted HSA limits and HDHP minimums
- Rev. Proc. 2025-19 — 2026 HSA limits ($4,400 / $8,750) and HDHP minimums ($1,700 / $3,400 deductible; $8,500 / $17,000 out-of-pocket)
- P.L. 119-21 §§71306–71308 and Notice 2026-5 — telehealth safe harbor (plan years after 2024), bronze/catastrophic Marketplace plans as HDHPs and direct primary care arrangements (months after December 31, 2025)
- Medicare.gov, "When does Medicare coverage start?" — Part A retroactivity of 6 months
- Notice 2004-50 — Comprehensive HSA Q&A (recordkeeping, qualified expenses, prohibited transactions)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-employer HSAs, Medicare timing, MFJ family-limit splitting, last-month-rule testing-period failures) warrant a licensed tax professional's review.
