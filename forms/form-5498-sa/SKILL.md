---
name: form-5498-sa
description: >
  Use this skill when an HSA, Archer MSA, or Medicare Advantage MSA account
  holder receives Form 5498-SA from their custodian and needs to reconcile it
  against Form 8889. Triggers on phrases like "received Form 5498-SA",
  "verify HSA contributions on tax return", "5498-SA vs 8889",
  "HSA contribution reporting form", "reconcile my HSA form", "what does
  Box 2 mean on 5498-SA", "do I file Form 5498-SA". Anti-triggers: filing
  Form 8889 itself (use form-8889 skill), HSA distributions reported on
  1099-SA (use form-1099-sa skill), excess-contribution excise tax (use
  form-5329 skill), Archer MSA filing on Form 8853 (no skill in this repo;
  follow the Instructions for Form 8853).
form: Form 5498-SA
audience: [individual, solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f5498sa.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099sa.pdf
---

# Form 5498-SA — HSA, Archer MSA, or Medicare Advantage MSA Information

This skill produces a reconciliation between an account holder's Form 5498-SA (received from their HSA custodian) and the Form 8889 they already filed (or are about to file). It walks through the form box by box, applies IRS reconciliation rules, validates the result, and emits a deliverable that flags any discrepancies and recommends action.

The math is mechanical. The judgment is in distinguishing custodian errors from filer errors, identifying timing-related discrepancies (prior-year contributions split across two 5498-SAs), and knowing when to amend Form 8889 versus when to call the custodian.

**Companion guide for end users:** [Form 5498-SA + AI Agent Skill: HSA Information Reporting Guide 2026](https://jupid.com/blog/form-5498-sa-hsa-information-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision.** Box map verified against the 2025 Form 5498-SA and the 2025 Instructions for Forms 1099-SA and 5498-SA (Mar 21, 2025): the form for 2025 contributions, furnished and filed by June 1, 2026. For 2026 contributions (furnished in 2027) the IRS switched to a continuous-use Form 5498-SA (Rev. December 2026) with the same six boxes, worded "the calendar year" / "the subsequent year". Re-check https://www.irs.gov/forms-pubs/about-form-5498-sa before use.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user says they received Form 5498-SA from their HSA custodian (Fidelity, Lively, HealthEquity, Optum Bank, HSA Bank, etc.)
- The user wants to reconcile their HSA contribution figures against what they reported on Form 8889
- The user asks "do I need to file Form 5498-SA?" (answer: no, the custodian files it; you reconcile against it)
- The user asks "what does Box 2 / Box 3 / Box 4 / Box 5 / Box 6 mean on Form 5498-SA?"
- The user notices a mismatch between Form 5498-SA and Form 8889 and wants help diagnosing the cause
- The user asks about prior-year HSA contributions and which 5498-SA they appear on

Do **not** engage this skill when:

- The user is filing Form 8889 itself (contributions and deduction calculation) → use the [`form-8889`](../form-8889/SKILL.md) skill
- The user is dealing with HSA distributions reported on **Form 1099-SA** → use the [`form-1099-sa`](../form-1099-sa/SKILL.md) skill
- The user has an Archer MSA and is filing **Form 8853** → no skill in this repo; follow the Instructions for Form 8853
- The user wants to set up a new HSA, choose a custodian, or pick investments → out of scope; refer to a financial advisor
- The user asks about HSA eligibility, HDHP requirements, or contribution limits → use the `form-8889` skill (eligibility reference)

If the user's situation is ambiguous (e.g., they received "an HSA tax form" but don't know which one), ask them to read the form name from the top of the document. Form 5498-SA is the contribution information return; Form 1099-SA is the distribution form; Form 8889 is the form they file with their 1040.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the 5498-SA covers. Look at the top of the form for "For Calendar Year YYYY".
2. **Custodian name** — Fidelity, Lively, HealthEquity, Optum Bank, HSA Bank, etc.
3. **Box 1** — Archer MSA contributions (typically $0 for HSA holders)
4. **Box 2** — Total HSA / Archer MSA contributions made **in** the calendar year, including contributions made in that year for the prior year and qualified HSA funding distributions from an IRA (the most important number)
5. **Box 3** — Total contributions made in the following year (by April 15) **for** the year on this form (only relevant if the user made a prior-year-designated contribution between January 1 and April 15)
6. **Box 4** — Rollover contributions (from another HSA or an Archer MSA)
7. **Box 5** — Fair market value of the account on December 31
8. **Box 6** — Account type (HSA / Archer MSA / Medicare Advantage MSA)
9. **W-2 Box 12 code W amount** for the same tax year — the employer + cafeteria plan contribution figure (needed to separate employer contributions from direct contributions)
10. **Form 8889 (filed or about to be filed)** — at minimum, Line 2 (direct contributions), Line 9 (employer contributions) and Line 10 (qualified HSA funding distribution)
11. **Box 3 of the prior year's 5498-SA** — the part of this year's Box 2 that was made in this year for the prior year

If the user is reconciling a prior-year contribution made between January 1 and April 15, also ask:

- **Does Box 3 of this year's 5498-SA show the prior-year-designated contribution?** Box 3 on the same form is where a January–April contribution for this tax year appears; the following year's Box 2 will also include it as money received in that calendar year.

For Form 8889 Line 9 reconciliation, additionally ask:

- **What does W-2 Box 12 code W say?** This is the authoritative source for employer + cafeteria plan contributions, not Form 5498-SA Box 2 alone.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the form is actually 5498-SA

Confirm the user is reading from Form 5498-SA, not Form 1099-SA (distributions) or Form 8889 (the form they file). The form title at the top reads "HSA, Archer MSA, or Medicare Advantage MSA Information". If they're holding a 1099-SA, redirect to the `form-8889` skill.

### Step 2 — Verify header information

Walk the user through the header:

- **Trustee/custodian name and TIN** — the financial institution that holds the HSA
- **Recipient name, address, SSN** — the account holder; verify name spelling, address current, SSN correct
- **Account number** — internal custodian identifier

If any header field is wrong (especially SSN), instruct the user to contact the custodian immediately for a corrected form. The IRS uses these fields to match the 5498-SA to the recipient's tax return.

### Step 3 — Map each box to its meaning

Produce this internal table from the user's data:

```
| Box | Label                         | Value     | Comment                                  |
|-----|-------------------------------|-----------|------------------------------------------|
| 1   | Archer MSA contributions      | $0        | $0 unless Archer MSA                     |
| 2   | Total contributions made in yr| $8,550    | Received in the calendar year (incl. prior-year-designated and IRA funding distributions) |
| 3   | Made next year for this year  | $0        | Jan 1–Apr 15 contributions designated for this year |
| 4   | Rollover contributions        | $0        | HSA-to-HSA or Archer MSA-to-HSA rollovers |
| 5   | Year-end FMV                  | $43,200   | Informational only                       |
| 6   | Account type                  | HSA       | HSA / Archer MSA / Medicare Adv MSA      |
```

### Step 4 — Pull Form 8889 figures

From the user's filed (or draft) Form 8889 for the tax year, pull:

- **Line 2** — Direct HSA contributions made by the account holder for the tax year
- **Line 9** — Employer contributions (W-2 Box 12 code W, adjusted by the Employer Contribution Worksheet when employer money crosses years)
- **Line 10** — Qualified HSA funding distribution from an IRA (reported by the custodian in Box 2)

If the user hasn't filed yet, redirect them to the `form-8889` skill to compute these first, then return to reconciliation.

### Step 5 — Reconcile Box 2 against Form 8889

The reconciliation formula:

```
Contributions for tax year Y
  = Box 2 of the year-Y 5498-SA
  − Box 3 of the year-(Y−1) 5498-SA   (made in year Y for year Y−1; already counted on last year's Form 8889)
  + Box 3 of the year-Y 5498-SA       (made Jan 1–Apr 15 of year Y+1 for year Y)

Contributions for tax year Y
  − Form 8889 Line 9 (employer + cafeteria, from W-2 Box 12 code W)
  − Form 8889 Line 10 (qualified HSA funding distribution)
  = Direct contributions (should match Form 8889 Line 2)
```

Box 2 counts money by the calendar year received; Box 3 shows the January–April money designated for the form's year (2025 Instructions for Forms 1099-SA and 5498-SA, Boxes 2 and 3). Excess employer contributions the employer took back under Notice 2008-59 Q&A-24 are not in Box 2.

If LHS = RHS, reconciliation passes. If not, see Step 6.

### Step 6 — Diagnose discrepancies

If the reconciliation fails, walk through the diagnosis tree in [`references/reconciliation.md`](./references/reconciliation.md). The five most common causes:

1. **Prior-year contribution timing** — A January–April contribution designated for the prior year appears in **Box 3 of the prior year's own form** (and in the next year's Box 2 as money received that year). A Box 2-only comparison misses it in one year and double-counts it in the other. Apply the formula above.
2. **December check timing** — A check mailed in late December reached the custodian in January, so it counts in the next year's Box 2 unless the user designated it for the prior year by April 15 (then it is also in the prior year's Box 3).
3. **Custodian clerical error** — The custodian double-counted a transfer, missed a deposit, or mis-allocated between contribution and rollover. Custodians issue corrected 5498-SAs ("CORRECTED" box checked) on request.
4. **W-2 Box 12 code W error** — The employer's payroll system reported the wrong cafeteria-plan amount. Contact employer payroll.
5. **Filer error** — The account holder reported the wrong amount on Form 8889 Line 2 or Line 9. Amend via Form 1040-X.

### Step 7 — Validate Box 5 against year-end statement

Box 5 (year-end FMV) should match the account holder's December 31 statement from the custodian. If it differs by more than rounding, contact the custodian. This rarely indicates a tax problem but is a sign of a bookkeeping error worth fixing.

### Step 8 — Run validation checks

See **Validation** below. Run every check. Don't skip even if the math looks clean.

### Step 9 — Produce the deliverable

See **Output format** below. The deliverable is a reconciliation report with: pass/fail status, line-by-line evidence, recommended actions for any discrepancies.

### Step 10 — Hand off downstream

State the next forms or actions the user will need:

- **Reconciliation passes** → file the 5498-SA with the year's tax records; no further action
- **Reconciliation fails due to filer error (under-reported contribution)** → file Form 1040-X with amended Form 8889 to claim additional deduction
- **Reconciliation fails due to filer error (over-contribution)** → withdraw excess plus earnings by the due date of the return including extensions (or within 6 months of the original due date with an amended return marked "Filed pursuant to section 301.9100-2"); otherwise Form 5329 Part VII for each year the excess remains (use the [`form-5329`](../form-5329/SKILL.md) skill)
- **Reconciliation fails due to custodian error** → contact the custodian promptly; request a corrected 5498-SA
- **Reconciliation fails due to employer payroll error (W-2 Box 12 code W)** → contact employer payroll; potentially request corrected W-2c

### Step 11 — File amendment if needed (optional, if the user wants the agent to file 1040-X)

If a Form 8889 amendment is required and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- When Form 1040-X is required vs. when a custodian correction suffices
- Decision tree for filing Form 1040-X (e-file through tax software where supported, otherwise paper; full mechanics in the [`form-1040-x`](../form-1040-x/SKILL.md) skill)
- Field-by-field map for Form 1040-X relating to HSA deduction changes
- Pre-flight checklist (corrected Form 8889, updated Schedule 1, supporting 5498-SA copy)
- Submission state machine and security rules

If the user only wants a reconciliation report and will file themselves, skip this step.

---

## Box-by-box guidance

For the full reference, load [`references/box-by-box.md`](./references/box-by-box.md). High-level summary below.

### Box 1 — Archer MSA Contributions

For Archer MSA holders only: regular contributions to the Archer MSA made in the year and through April 15 of the next year for that year, gross of any excess even if withdrawn. Most filers in 2026 see $0 here because Archer MSAs have been closed to new enrollees since 2007. No HSA information goes in Box 1. Archer MSAs are filed on Form 8853, not Form 8889.

### Box 2 — Total Contributions Made in the Calendar Year

The most important number on the form. Includes everything received during the calendar year:

- Direct contributions by the account holder
- Cafeteria plan / Section 125 contributions routed through payroll
- Employer-only contributions (those the employer makes without payroll withholding)
- Contributions made on the account holder's behalf by family
- Contributions made this year **for the prior year** (January 1–April 15)
- Qualified HSA funding distributions from an IRA (trustee-to-trustee transfers under IRC §408(d)(9))

Excludes rollovers (Box 4) and excess employer contributions the employer withdrew under Notice 2008-59 Q&A-24. Reconciles against Form 8889 Lines 2 + 9 + 10 only after the Box 3 adjustments in Step 5.

**Timing rule:** Box 2 covers contributions **received by the custodian during the calendar year**. A contribution mailed December 28 but received January 3 lands in the next year's Box 2.

### Box 3 — Contributions Made in the Following Year for This Year

Contributions made between January 1 and April 15 of the next year that the account holder designated for the year on this form (so they count on that year's Form 8889). Example: a March 15, 2026 contribution designated for 2025 appears in **Box 3 of the 2025 Form 5498-SA** and in Box 2 of the 2026 Form 5498-SA.

**Reconciliation note:** The deadline is the unextended due date of the return (April 15), not the extended date (IRC §223(d)(4)(B) applying §219(f)(3); 2025 Instructions for Form 8889, Line 2).

### Box 4 — Rollover Contributions

Rollovers received from another HSA or from an Archer MSA. Rollovers are not deductible (they are tax-free transfers), so they are tracked separately from Box 2. Qualified HSA funding distributions from an IRA are reported in Box 2, not Box 4.

**Limit:** An HSA can receive only one rollover contribution in a 1-year period (IRC §223(f)(5); 2025 Instructions for Form 8889, "Rollovers"). Trustee-to-trustee transfers are not rollovers, are not reported on Form 5498-SA, and are not subject to the limit.

### Box 5 — Fair Market Value at Year-End

Total balance in the account on December 31, including cash, mutual funds, ETFs, and any other invested assets at year-end market value.

Box 5 is informational. It does not flow to any Form 8889 line. Uses:

- The IRS receives it with the rest of the form
- Account holders use it to track HSA growth as a retirement asset
- Useful for estate and net-worth records

### Box 6 — Account Type

Check-box indicating account type:

- **HSA** — Health Savings Account (IRC §223)
- **Archer MSA** — Archer Medical Savings Account (IRC §220, closed to new enrollees since 2007)
- **Medicare Advantage MSA** — for Medicare beneficiaries enrolled in MA MSA plans (IRC §138)

If Box 6 reads anything other than what the user expected, contact the custodian immediately.

---

## Validation

Before declaring the reconciliation complete, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Box 2 ≥ 0; (Box 2 − prior year's Box 3 + this year's Box 3) ≤ annual HSA contribution limit + catch-up if 55+ ($4,300 / $8,550 for 2025, Rev. Proc. 2024-25; $4,400 / $8,750 for 2026, Rev. Proc. 2025-19; $1,000 catch-up)
- [ ] (Form 8889 Line 2 + Line 9 + Line 10) = (this year's Box 2 − prior year's Box 3 + this year's Box 3)
- [ ] (Form 8889 Line 9) = W-2 Box 12 code W, unless the Employer Contribution Worksheet moved employer money between years
- [ ] Box 5 (year-end FMV) matches December 31 custodian statement (within rounding)
- [ ] Box 4 (rollovers) consistent with the user's recollection of any rollover activity

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Contributions for the tax year > applicable annual contribution limit → potential excess contribution; check if user has corrected via withdrawal
- [ ] Box 4 > 0 and user reported more than one HSA-to-HSA rollover in the past 12 months → potential violation of one-rollover-per-12-months rule
- [ ] Box 5 grew by more than (Box 2 + Box 4 + plausible market growth) → unexpected; possible custodian error or untracked rollover
- [ ] Box 6 ≠ HSA but user expected HSA → custodian error or account type confusion
- [ ] No 5498-SA received for an HSA the user knows is open → the custodian still files it with the IRS to report the December 31 FMV, but if no contributions were made it may have furnished only a January FMV statement instead (2025 Instructions for Forms 1099-SA and 5498-SA, "Statements to Participants"); check the portal before calling
- [ ] Two 5498-SAs received for one HSA in the same year → likely a corrected form; verify "CORRECTED" box is checked on the second

### Cross-form checks

- [ ] (Form 8889 Line 2 + Line 9 + Line 10) reconciles against (this year's Box 2 − prior year's Box 3 + this year's Box 3)
- [ ] Form 8889 Line 9 = W-2 Box 12 code W (or the Employer Contribution Worksheet result)
- [ ] If Box 4 > 0, the rollover is NOT on Form 8889 Line 2 (rollovers are excluded from Line 2 and don't add to Line 13)
- [ ] If a prior-year contribution was made in this calendar year, the prior year's 5498-SA Box 3 was pulled

---

## Output format

The agent's deliverable is a **reconciliation report** the user can file with their tax records. Format:

```markdown
# Form 5498-SA Reconciliation Report — Tax Year YYYY

## Custodian and Account
- Custodian: <name>
- Account number: <last-4 digits>
- Account holder: <name>
- Tax year: YYYY

## 5498-SA Box Values
| Box | Label                         | Value     |
|-----|-------------------------------|-----------|
| 1   | Archer MSA contributions      | $X,XXX    |
| 2   | Total contributions made in yr| $X,XXX    |
| 3   | Made next year for this year  | $X,XXX    |
| 4   | Rollover contributions        | $X,XXX    |
| 5   | Year-end FMV                  | $X,XXX    |
| 6   | Account type                  | HSA       |

## Cross-Form Comparison
| Check                                 | 5498-SA   | 8889 / W-2 | Match?  |
|---------------------------------------|-----------|------------|---------|
| Total contributions for tax year      | $X,XXX    | $X,XXX     | Y/N     |
| Cafeteria/employer portion            | (derived) | $X,XXX     | Y/N     |
| Direct contributions                  | (derived) | $X,XXX     | Y/N     |
| Year-end balance vs. December stmt    | $X,XXX    | $X,XXX     | Y/N     |

## Reconciliation Status: PASS | FAIL

## Discrepancies (if any)
- Description: <what didn't match>
- Likely cause: <prior-year-designation / custodian error / W-2 error / filer error>
- Recommended action: <call custodian / amend Form 8889 / contact employer payroll / no action>

## Required Follow-Up Actions
- [ ] File 5498-SA with year's tax records
- [ ] (If FAIL) Contact <custodian / employer / file Form 1040-X>
- [ ] (If excess contribution) Withdraw excess plus earnings by the due date including extensions
- [ ] (If amendment needed) File Form 1040-X with corrected Form 8889

## Sources cited in this report
- IRS Form 5498-SA (2025, or Rev. December 2026 for 2026 contributions)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025, or Rev. December 2026)
- Form 8889 (as filed)
- W-2 Box 12 code W (employer figure)
- IRC §223
- (any other authority used)
```

The report is the finished product. The user files it with their tax records and acts on any FAIL items.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/box-by-box.md`](./references/box-by-box.md) — Detailed walk-through of each 5498-SA box with examples
- [`references/reconciliation.md`](./references/reconciliation.md) — Diagnosis tree for 5498-SA vs. Form 8889 mismatches
- [`references/timing-rules.md`](./references/timing-rules.md) — Calendar-year vs. tax-year timing, prior-year designations, December check rules
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top reconciliation mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: Form 1040-X amendment workflow if reconciliation reveals a Form 8889 error (loaded only when the user authorizes filing)

## Examples

End-to-end worked reconciliations. Use these as patterns when the user's situation is similar.

- [`examples/clean-reconciliation-family-hdhp.md`](./examples/clean-reconciliation-family-hdhp.md) — Marcus, family HDHP, cafeteria plan plus direct deposits, all numbers match
- [`examples/prior-year-designation-split.md`](./examples/prior-year-designation-split.md) — Filer made a March prior-year contribution; it shows in Box 3 of the same year's 5498-SA and in next year's Box 2
- [`examples/custodian-error-correction.md`](./examples/custodian-error-correction.md) — Custodian double-counted a transfer; corrected 5498-SA issued

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being reconciled — the IRS revises forms and instructions each cycle.

- [Form 5498-SA + AI Agent Skill: HSA Information Reporting Guide 2026](https://jupid.com/blog/form-5498-sa-hsa-information-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 5498-SA (latest)](https://www.irs.gov/pub/irs-pdf/f5498sa.pdf) — the form itself
- [Instructions for Forms 1099-SA and 5498-SA (latest)](https://www.irs.gov/pub/irs-pdf/i1099sa.pdf) — combined custodian filing instructions
- [About Form 5498-SA](https://www.irs.gov/forms-pubs/about-form-5498-sa) — IRS landing page
- [Form 8889 (latest)](https://www.irs.gov/pub/irs-pdf/f8889.pdf) — Health Savings Accounts (the form the recipient files)
- [Instructions for Form 8889 (latest)](https://www.irs.gov/pub/irs-pdf/i8889.pdf) — Form 8889 line-by-line guidance
- [Form 1040-X](https://www.irs.gov/forms-pubs/about-form-1040x) — Amended return, used if reconciliation reveals a Form 8889 error
- [Publication 969](https://www.irs.gov/publications/p969) — Health Savings Accounts and Other Tax-Favored Health Plans
- IRC §223 (HSAs), §223(h) (custodian reporting), §223(f)(5) (one rollover per 1-year period), §223(d)(4)(B) / §219(f)(3) (contributions by the unextended due date)
- [Pub. 1099 (2026)](https://www.irs.gov/publications/p1099) — Form 5498-SA furnishing date (May 31, next business day if a weekend: June 1, 2026 for 2025 forms) and the January 31 FMV-statement alternative
- Notice 2008-59 Q&A-24 (excess employer contributions withdrawn by the employer)
- IRC §220 (Archer MSAs), §220(h) (Archer MSA reporting)
- IRC §138 (Medicare Advantage MSAs)
- IRC §6721 (information return penalty)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a reconciliation report, that the output is a starting point and that complex situations (multi-state HSA portability, divorce-related HSA division, decedent HSA beneficiary issues) warrant a licensed tax professional's review.
