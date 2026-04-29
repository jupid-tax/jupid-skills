---
name: form-5329
description: >
  Use this skill when an individual taxpayer needs to report additional taxes
  (excise/penalty taxes) on retirement plans, IRAs, education savings accounts,
  HSAs, Archer MSAs, or ABLE accounts. Triggers on phrases like "10% early
  withdrawal penalty", "early distribution from IRA", "excess Roth contribution",
  "excess IRA contribution", "missed RMD", "missed required minimum distribution",
  "RMD penalty", "Form 5329", "qualified plan additional tax", "excess
  accumulation tax", "Section 72(t)", "request RMD waiver", "reasonable cause for
  missed RMD". Do NOT use for: routine IRA distributions with no penalty (those
  are reported only on Form 1040 Lines 4a/4b from a 1099-R, no 5329 needed); HSA
  excess contributions or non-qualified HSA distributions on their own (use the
  form-8889 skill for the HSA reporting; 5329 Part VII still applies only when
  HSA excise tax is owed); employer-sponsored 401(k) loans treated as
  distributions (those flow through 1099-R + 1040 unless a §72(t) penalty
  applies); plan-level excess contributions corrected by the custodian before
  the deadline.
form: Form 5329 (Additional Taxes on Qualified Plans, Including IRAs, and Other Tax-Favored Accounts)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f5329.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i5329.pdf
---

# Form 5329 — Additional Taxes on Qualified Plans (Including IRAs)

This skill produces an audit-grade draft of Form 5329 and any attached
explanatory statements (waiver requests, exception narratives) for the user's
situation. Form 5329 reports excise and additional taxes on retirement and
tax-favored account transactions that the regular Form 1040 cannot capture on
its own — early distributions, excess contributions, missed required minimum
distributions, prohibited transactions, and similar.

The form has nine numbered parts. The agent must invoke only the parts that
apply to the user's facts. Each part has its own statutory base (IRC §72(t),
§4973, §4974, etc.) and its own line-by-line logic.

The math is mechanical. The judgment is in *which Part applies*, *whether an
exception or waiver reduces the penalty*, and *what corrective action the user
took (or could still take) before the deadline*. This skill optimizes for
those branches — ask the user, don't guess.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user took a distribution from a traditional IRA, Roth IRA, 401(k),
  403(b), governmental 457(b), SEP-IRA, or SIMPLE IRA before age 59½ and is
  asking about the 10% additional tax (or wants to claim an exception)
- The user contributed more than the IRA / Roth IRA / Coverdell ESA / HSA /
  ABLE limit and is past the correction deadline (or is deciding between
  correction and the 6% excise tax)
- The user (or an inherited-IRA beneficiary) missed a required minimum
  distribution (RMD) and needs to compute the 25% excess-accumulation tax
  (or 10% if corrected within the 2-year correction window) and file a
  waiver request
- The user is a SIMPLE-IRA participant who took a distribution within the
  first 2 years of plan participation and faces the 25% additional tax (not
  10%)
- The user took an "early" Roth IRA distribution where part of the amount is
  earnings, triggering the 10% additional tax on the earnings portion
- The user has an excess accumulation in a Coverdell ESA or ABLE account

Do **not** engage this skill when:

- The user took a normal distribution after age 59½ from a traditional IRA
  or 401(k), with no penalty owed → reported on Form 1040 Lines 4a/4b or
  5a/5b only; no Form 5329
- A direct rollover (trustee-to-trustee or plan-to-IRA) from one qualified
  plan to another with no taxable event → no 5329 needed
- The user's plan custodian corrected an excess contribution + earnings
  before the user's tax filing deadline (including extensions) → corrected
  excess is removed; no 6% tax; no Part III/IV needed (but earnings are
  taxable on Form 1040 and the 10% additional tax may apply on the earnings
  portion if under 59½ — that's still 5329 Part I)
- The user is reporting an HSA distribution separately (use the `form-8889`
  skill for the distribution itself; Form 5329 Part VII applies only to
  excess HSA contribution excise tax)

If multiple Parts apply simultaneously (common: under-59½ user who *also*
made an excess Roth contribution and *also* missed a small RMD on an
inherited IRA), the agent fills each Part separately and totals them on
the appropriate Form 1040 schedule line.

For the parent return, see the (forthcoming) `form-1040` skill — Form 5329
attaches to Form 1040 (or Form 1040-NR / 1040-SR). Form 5329 can also be
**filed standalone** when the user is not otherwise required to file a 1040
(e.g., a low-income retiree who only owes the missed-RMD excise tax). In
that standalone case, the user signs Form 5329 itself and mails it.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are
missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Penalty rates and account contribution
   limits are year-specific. The user's age on the last day of the tax
   year (or on the date of distribution, depending on the Part) is what
   matters for early-distribution rules.

2. **Filer's legal name and SSN.** Required on the form header. If the
   user is filing standalone (not attaching to a 1040), the agent needs
   the user's full mailing address as well.

3. **Which event(s) triggered the form.** Walk the user through the nine
   Parts and confirm which apply:
   - Part I — Additional tax on early distributions (10%; 25% for SIMPLE
     IRAs in first 2 years)
   - Part II — Additional tax on certain distributions from education
     accounts and ABLE accounts
   - Part III — Additional tax on excess contributions to traditional IRAs
   - Part IV — Additional tax on excess contributions to Roth IRAs
   - Part V — Additional tax on excess contributions to Coverdell ESAs
   - Part VI — Additional tax on excess contributions to Archer MSAs
   - Part VII — Additional tax on excess contributions to HSAs
   - Part VIII — Additional tax on excess contributions to ABLE accounts
   - Part IX — Additional tax on excess accumulation in qualified
     retirement plans (including IRAs) — **the missed-RMD Part**

4. **For Part I (early distributions)**: total amount of early distributions
   for the year (gross), and a list of any §72(t) exceptions the user
   qualifies for. The exceptions, with their distribution-code numbers from
   Form 5329 instructions, are below in the "Line-by-line guidance" section.

5. **For Part III/IV (excess IRA / Roth contributions)**: the prior-year
   carryover of excess (if any), the current-year excess (= contribution −
   limit), and whether any excess was withdrawn (with earnings) before the
   filing deadline.

6. **For Part IX (missed RMD)**: the RMD amount that should have been
   distributed, the amount actually distributed, and **whether the user is
   requesting a waiver** under the "reasonable cause" provision of IRC
   §4974(d). If yes, the agent prepares the waiver attachment and the user
   reports the *excise tax of 0 on Line 55* (not the 25% calculation).

7. **For SECURE 2.0 corrected RMDs**: the date the missed RMD was actually
   distributed. If the user takes the missed amount within 2 years of the
   end of the tax year it should have been taken, the rate drops from 25%
   to 10% (IRC §4974(e), added by SECURE 2.0 Act §302).

8. **Filing channel**: is the user attaching this to a 1040, or filing
   standalone? Standalone changes the signature/mailing flow (see
   `filing.md`).

---

## Workflow

Execute these steps in order.

### Step 1 — Identify which Parts apply

Walk through the nine Parts with the user. For each Part the user might
be subject to, confirm with a one-line question:

> "Did you take any IRA / 401(k) / 403(b) distribution this year before
> turning 59½?"
> "Did you contribute more than $X to your Roth IRA?" (verify the limit
> for the tax year — see Sources)
> "Were you required to take an RMD this year (you turned 73, or you
> inherited an IRA), and did you miss any portion of it?"

Skip Parts the user clearly is not subject to. Don't add them with zero —
the IRS does not require unused Parts.

### Step 2 — For each Part, gather inputs

For each Part flagged in Step 1, collect the relevant numbers and
documents (1099-R Box 7 distribution code, prior-year 5329 if there's a
running excess balance, SIMPLE plan participation start date, etc.).

### Step 3 — Compute Part I (early distributions) if applicable

a) Sum the early distributions from 1099-Rs with codes 1, J, S, 2 (sometimes),
or where the user knows the distribution was under 59½ regardless of code.
The total goes on Line 1.

b) Apply exceptions from the IRC §72(t) catalog. The user gets to subtract
amounts that fall under each exception (medical, higher ed, first home, etc.).
The exception total goes on Line 2 with the corresponding code from the
Form 5329 instructions.

c) Line 3 = Line 1 − Line 2 (taxable early distribution amount).
d) Line 4 = Line 3 × 10% (or × 25% for SIMPLE-IRA distributions in first 2
years; see the SIMPLE-IRA flag on the form).

The result on Line 4 flows to Schedule 2 Line 8 (for tax year 2025/2026 forms).

### Step 4 — Compute Part III/IV (excess contributions) if applicable

The 6% excise tax is on the lesser of:
- The excess contribution + any prior-year excess still in the account, OR
- The value of the IRA on the last day of the tax year

Carrying excess forward without correcting compounds the 6% tax every year
until corrected. Surface this loudly to the user — most don't realize it.

If the user can still correct (return excess + attributable earnings before
the filing deadline including extensions), recommend correction over paying
6%. The user's custodian processes this as a "removal of excess
contribution"; the earnings portion is taxable in the year of contribution
and may itself trigger the 10% Part I additional tax if under 59½.

### Step 5 — Compute Part IX (missed RMD) if applicable

a) Line 52 — RMD that should have been taken (computed from the prior-year
12/31 account balance ÷ the applicable IRS Uniform Lifetime Table or Single
Life Table factor).

b) Line 53 — Amount actually distributed.

c) Line 54 — Excess accumulation = Line 52 − Line 53.

d) **Decision point**: is the user requesting a waiver?
- **Yes** → Line 55 = 0; attach a statement labeled "Form 5329 Line 54
  Waiver Request" explaining (i) the reasonable cause for the shortfall
  (illness, custodian error, recently inherited account, etc.) and (ii) the
  steps taken to remedy (the missed RMD has been or will be distributed by
  date X). The IRS grants these waivers liberally when reasonable cause is
  documented.
- **No** → compute Line 55 = Line 54 × 25% (or × 10% if the user qualifies
  for the SECURE 2.0 corrected-within-2-years reduction; check whether the
  missed RMD was distributed before the end of the second year following
  the year it should have been taken).

The result on Line 55 flows to Schedule 2 Line 8.

### Step 6 — Sum all Parts to produce Schedule 2 Line 8

Form 5329's separate Part totals all flow to a single line on Schedule 2
(Additional Taxes), which then flows to Form 1040 Line 23.

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below. If the user is requesting a waiver under
Part IX, the deliverable includes the waiver-statement attachment.

### Step 9 — Hand off

State next forms / actions:
- Schedule 2 (always, when 5329 has any Part with non-zero tax)
- Form 1040 Line 23 reflects total
- Schedule 1 if the user has any retirement-related deductions affected
- Reminder to take any uncorrected missed RMD now if not already done
- Reminder to update beneficiary designations and 12/31 balance tracking
  for next year

### Step 10 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md). Form 5329
is supported by IRS Free File Fillable Forms when attached to a 1040; the
standalone-5329 case requires paper filing or paid software.

---

## Line-by-line guidance

For full detail, load [`references/line-by-line.md`](./references/line-by-line.md).
High-level rules below.

### Part I — Additional tax on early distributions (Lines 1-4)

The 10% additional tax under IRC §72(t) applies to distributions from
qualified plans, IRAs, and similar tax-favored accounts when the recipient
is under 59½. SIMPLE IRAs in the first 2 years of participation use 25%
instead of 10%.

Exceptions (the user reduces Line 1 by the sum of qualifying amounts on
Line 2). Each exception has a code number listed in the Form 5329
instructions. Common ones:

| Code | Exception |
|------|-----------|
| 01 | Separation from service after age 55 (qualified plans only, not IRAs) |
| 02 | Distributions made as part of a series of substantially equal periodic payments (SoSEPP) under §72(t)(2)(A)(iv) |
| 03 | Disability (within meaning of §72(m)(7)) |
| 04 | Distributions to beneficiaries after death of the participant |
| 05 | Medical expenses exceeding 7.5% of AGI |
| 06 | IRS levy on the qualified plan |
| 07 | Higher education expenses (IRAs only) |
| 08 | First-time homebuyer (IRAs only, lifetime cap $10,000) |
| 09 | Reservist called to active duty |
| 10 | Birth or adoption (lifetime cap $5,000 per child) |
| 11 | Domestic abuse victim distribution (SECURE 2.0 §314, added 2024 — verify cap) |
| 12 | Terminal illness |
| 13 | Federally declared disaster (limits per Notice) |
| 14 | Emergency personal expense (SECURE 2.0 §115; $1,000 cap, once per year) |

For each exception claimed, the user must be ready to substantiate it.
The IRS does not request documentation up front but will in a CP2000 notice
or audit.

If the user qualifies for *multiple* exceptions for different portions of
the distribution, the agent enters each amount with its code in the
section labeled "Exception number" on Line 2.

### Part II — Distributions from education / ABLE accounts (Lines 5-8)

Applies to taxable distributions from Coverdell ESAs and ABLE accounts not
used for qualified expenses. The 10% additional tax applies on the taxable
portion. Exceptions: death, disability, scholarship-equivalent, military
academy attendance.

### Part III — Excess contributions to traditional IRAs (Lines 9-17)

The 6% tax on excess contributions to a traditional IRA. Excess =
contribution − deductible-or-nondeductible limit for the year.

Key inputs:
- Line 9 — current-year excess contribution
- Line 10 — prior-year excess from prior 5329 Line 16
- Line 16 — total excess remaining at end of year (carries forward)
- Line 17 — 6% × lesser of (Line 16) or (account value 12/31)

### Part IV — Excess contributions to Roth IRAs (Lines 18-25)

Mirrors Part III but for Roth IRAs. The income-based phaseout on Roth
contributions creates the most common error: a high-earner who contributed
$X early in the year, then crossed the phaseout threshold, and now has
excess. Custodians don't track this — the user must.

Two correction paths:
- **Withdraw excess + earnings before deadline**: no 6% excise tax. Earnings
  are taxable; if under 59½, earnings are also subject to the 10% Part I tax.
- **Recharacterize** to a traditional IRA before the deadline: treats the
  contribution as a traditional IRA contribution from the start. Eliminates
  the Roth-side excess. Does *not* eliminate a traditional-IRA-side excess
  if the user also exceeded the traditional limit.

### Part V — Excess contributions to Coverdell ESAs (Lines 26-32)

6% tax on excess contributions to a Coverdell ESA (excess = contribution
− $2,000 per beneficiary per year, plus phaseouts).

### Part VI — Excess contributions to Archer MSAs (Lines 33-39)

Rare. Most filers have HSAs (Part VII) instead.

### Part VII — Excess contributions to HSAs (Lines 40-47)

6% tax on excess HSA contributions. The HSA contribution limit is
account-type-dependent (self-only vs. family coverage) and changes annually.
Verify the limit for the tax year against IRS Rev. Proc. (typically issued
in May of the prior year for HDHP / HSA limits).

### Part VIII — Excess contributions to ABLE accounts (Lines 48-51)

6% tax on excess ABLE contributions. ABLE limit is the federal annual gift
tax exclusion ($18,000 for 2024, $19,000 for 2025; verify 2026).

### Part IX — Additional tax on excess accumulation (Lines 52-55) — Missed RMD

The big one. Lines 52-55:
- **Line 52** — Required minimum distribution (RMD) for the year
- **Line 53** — Amount actually distributed
- **Line 54** — Shortfall (Line 52 − Line 53)
- **Line 55** — Excise tax = 25% of Line 54 (10% if corrected per SECURE 2.0)

**Waiver request**: if the shortfall was due to reasonable cause and the
user is taking steps to remedy, the user can request a waiver. To request,
write 0 on Line 55 and attach a statement. The IRS approves these liberally
in practice. See [`references/missed-rmd.md`](./references/missed-rmd.md).

**SECURE 2.0 changes (effective 2023+)**:
- The penalty was 50% before 2023; SECURE 2.0 §302 dropped it to 25%
- A new "corrected within 2 years" reduction drops it to 10% if the missed
  RMD is distributed within 2 years of the year it should have been taken
- RMD age increased from 72 to 73 (further to 75 in 2033)

---

## Validation

Before declaring the form ready, run these checks. Surface any failure;
do not silently fix.

### Math checks

- [ ] Part I: Line 3 = Line 1 − Line 2; Line 4 = Line 3 × 10% (or × 25%)
- [ ] Part III: Line 16 = Line 9 + Line 10 − distributions of excess; Line 17
      = 6% × min(Line 16, account value 12/31)
- [ ] Part IV: same as Part III for Roth IRA
- [ ] Part IX: Line 54 = Line 52 − Line 53; Line 55 = Line 54 × 25% (or × 10%
      with SECURE 2.0 reduction; or 0 if waiver requested with attachment)
- [ ] Sum of all Part totals matches the number flowed to Schedule 2 Line 8

### Sanity checks (warn, do not block)

- [ ] Part I exception code claimed but the distribution code on the 1099-R
      doesn't match what the exception expects (e.g., user claims code 01
      "separation after 55" but the distribution is from an IRA, where
      that exception doesn't apply)
- [ ] Part III/IV: prior-year excess carried forward but no Part III/IV on
      the prior year's Form 5329 → user may have under-reported in prior
      years
- [ ] Part IX: waiver requested but no attachment statement drafted
- [ ] Part IX: Line 52 (RMD) = 0 → does the user actually have an RMD
      requirement? If turning 73 this year, the first RMD has an April 1
      of *next year* deadline (so might not be missed yet)
- [ ] Roth IRA excess: user's MAGI for the year was above the Roth phaseout,
      but no Part IV → user may not realize the contribution was fully
      ineligible
- [ ] SIMPLE IRA distribution within 2 years of plan participation: rate is
      25%, not 10% — confirm the agent applied the right rate
- [ ] Multiple exceptions claimed totaling more than Line 1 → impossible;
      stop and re-check

### Cross-form checks

- [ ] If Part I has a non-zero tax: confirm the corresponding 1099-R is
      reported on Form 1040 Lines 4a/4b or 5a/5b
- [ ] If Part IX has a corrected missed RMD: the corrected distribution
      itself appears on a 1099-R for the year it was actually taken
- [ ] Schedule 2 Line 8 total includes Form 5329 result

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe.
Format:

```markdown
# Form 5329 — DRAFT for tax year YYYY

## Header
Name: <filer name>
SSN: <SSN>
Filing standalone? Yes | No (if Yes, also include mailing address)

## Part I — Additional Tax on Early Distributions (if applicable)
1. Early distributions includible in income:        $X,XXX
2. Exception amount + code(s):                      $X,XXX (code NN)
3. Amount subject to additional tax (Line 1 - 2):   $X,XXX
4. Additional tax (Line 3 × 10% or × 25%):          $XXX

## Part II — Distributions From Education / ABLE Accounts (if applicable)
[lines as filled]

## Part III — Excess Contributions to Traditional IRAs (if applicable)
9.  Current-year excess:                            $X,XXX
10. Prior-year excess from last year's Line 16:     $X,XXX
[continue through Line 17]

## Part IV — Excess Contributions to Roth IRAs (if applicable)
[lines as filled]

## Part V/VI/VII/VIII — (if applicable)
[lines as filled]

## Part IX — Excess Accumulation (Missed RMD) (if applicable)
52. Required minimum distribution:                  $X,XXX
53. Amount actually distributed:                    $X,XXX
54. Shortfall (Line 52 − Line 53):                  $X,XXX
55. Additional tax: 25% × Line 54:                  $X,XXX
    [or "0 — waiver requested; see attached statement"]
    [or "10% × Line 54 — SECURE 2.0 corrected-within-2-years rate"]

## Total additional tax flowing to Schedule 2 Line 8: $X,XXX

## Required attachments
- [ ] Waiver-request statement (if Part IX waiver requested)
- [ ] Form 1040 (if not standalone)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 5329 (revision date YYYY-MM-DD)
- IRS Instructions for Form 5329 (revision date YYYY-MM-DD)
- IRC §72(t), §4973, §4974
- SECURE 2.0 Act §302 (RMD penalty reduction; effective 2023)
- (any other authority used)
```

If a waiver is being requested, the deliverable additionally includes:

```markdown
# Form 5329 Line 54 — Waiver Request Statement
Filer: <name>
SSN: <SSN>
Tax Year: YYYY
Account: <IRA / 401(k) / inherited IRA description>

Required distribution: $X,XXX
Distribution actually taken in YYYY: $X,XXX
Shortfall: $X,XXX

Reasonable cause: [user's explanation — e.g., "I inherited the account
in October YYYY and was not aware of the year-of-death RMD requirement
for the deceased account owner. I learned of the requirement on
[date] when I consulted with [advisor/CPA]."]

Steps to remedy: [user's explanation — e.g., "On [date], I requested
the missed distribution amount of $X,XXX from [custodian]; the
distribution was processed on [date]. I have set up automatic RMD
distributions for future years."]

I respectfully request that the IRS waive the 25% additional tax under
IRC §4974(d). I have entered $0 on Line 55 of Form 5329 pending review
of this waiver request.

Filer signature: _______________________  Date: __________
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 5329 line with examples and edge cases
- [`references/early-distribution-exceptions.md`](./references/early-distribution-exceptions.md) — All §72(t) exceptions with documentation requirements
- [`references/excess-contributions.md`](./references/excess-contributions.md) — How excess contributions arise, correction options, and 6% tax mechanics
- [`references/missed-rmd.md`](./references/missed-rmd.md) — RMD computation, waiver request playbook, SECURE 2.0 reductions
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Filing playbook (attached to 1040 vs. standalone)

## Examples

End-to-end worked Form 5329 drafts.

- [`examples/early-roth-emergency.md`](./examples/early-roth-emergency.md) — 28-year-old emergency Roth IRA withdrawal, Part I + medical exception analysis
- [`examples/missed-rmd-waiver.md`](./examples/missed-rmd-waiver.md) — 67-year-old who missed an inherited-IRA RMD by 6 months, Part IX with waiver request
- [`examples/excess-roth-high-earner.md`](./examples/excess-roth-high-earner.md) — High-earner who over-contributed to Roth IRA after crossing phaseout, recharacterization vs. 6% Part IV decision

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS
site for the tax year being filed.

- [Form 5329 (latest)](https://www.irs.gov/pub/irs-pdf/f5329.pdf)
- [Instructions for Form 5329 (latest)](https://www.irs.gov/pub/irs-pdf/i5329.pdf)
- [About Form 5329](https://www.irs.gov/forms-pubs/about-form-5329)
- [Publication 590-A](https://www.irs.gov/publications/p590a) — Contributions to IRAs
- [Publication 590-B](https://www.irs.gov/publications/p590b) — Distributions from IRAs
- [Publication 560](https://www.irs.gov/publications/p560) — Retirement Plans for Small Business (SEP, SIMPLE, qualified)
- [Publication 575](https://www.irs.gov/publications/p575) — Pension and Annuity Income
- IRC §72(t) — additional tax on early distributions
- IRC §4973 — tax on excess contributions to qualified retirement plans
- IRC §4974 — excise tax on accumulated retirement income
- SECURE 2.0 Act of 2022 (P.L. 117-328) — §302 (RMD penalty reduction), §314 (domestic-abuse exception), §115 (emergency-expense exception)
- Notice 2024-80 — 2025 inflation-adjusted retirement plan limits (verify 2026 limits in the equivalent fall-2025 IRS notice)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. The waiver-request narrative
is a template; the user's specific reasonable cause must be true and
substantiable. Complex situations (multiple plans, inherited IRAs spanning
multiple beneficiaries, plan-level corrections) warrant a licensed tax
professional's review before filing.
