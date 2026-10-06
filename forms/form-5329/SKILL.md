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
last_verified: 2026-10-06
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

**Companion guide for end users:** [Form 5329 (2026): Early-Withdrawal and Excess-Contribution Penalties + AI Agent Skill](https://jupid.com/blog/form-5329-retirement-penalties-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision.** The line map was verified against the 2025 Form 5329 (created 6/12/25) and the 2025 Instructions for Form 5329 (Nov 19, 2025), filed in 2026. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-5329 before using this skill for a 2026 return.

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
  (or 10% if corrected within the correction window) and file a
  waiver request
- The user is a SIMPLE-IRA participant who took a distribution within the
  first 2 years of plan participation and faces the 25% additional tax (not
  10%)
- The user took an "early" Roth IRA distribution where part of the amount is
  earnings (or a recent conversion), triggering the 10% additional tax on
  that portion
- The user has excess contributions to a Coverdell ESA or ABLE account, or
  a taxable Coverdell / QTP / ABLE distribution (Part II)

Do **not** engage this skill when:

- The user took a normal distribution after age 59½ from a traditional IRA
  or 401(k), with no penalty owed → reported on Form 1040 Lines 4a/4b or
  5a/5b only; no Form 5329
- A direct rollover (trustee-to-trustee or plan-to-IRA) from one qualified
  plan to another with no taxable event → no 5329 needed
- The user's plan custodian corrected an excess contribution + earnings
  before the user's tax filing deadline (including extensions) → corrected
  excess is removed; no 6% tax; no Part III/IV needed (but earnings are
  taxable on Form 1040; if under 59½ they go on Part I Line 1 and Line 2
  with exception 21, so no 10% tax)
- The user's 1099-R box 7 shows code 2, 3, or 4 and that exception covers
  the whole distribution → no Form 5329 needed; or box 7 code 1 and the user
  owes the 10% on the full amount → the tax may go straight on Schedule 2
  (Form 1040), line 8 without Form 5329 (2025 Instructions, "Who Must File")
- The user is reporting an HSA distribution separately (use the `form-8889`
  skill for the distribution itself; Form 5329 Part VII applies only to
  excess HSA contribution excise tax)

If multiple Parts apply simultaneously (common: under-59½ user who *also*
made an excess Roth contribution and *also* missed a small RMD on an
inherited IRA), the agent fills each Part separately and totals them on
the appropriate Form 1040 schedule line.

For the parent return, see the [`form-1040`](../form-1040/SKILL.md) skill —
Form 5329 attaches to Form 1040 (or Form 1040-NR / 1040-SR). Form 5329 can
also be **filed standalone** when the user is not otherwise required to
file a 1040 (e.g., a low-income retiree who only owes the missed-RMD excise
tax). In that standalone case, the user completes the address on page 1,
signs page 3, and mails it; it cannot be e-filed.

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

4. **For Part I (early distributions)**: each 1099-R (box 1, box 2a, box 7
   code), the taxable early amount, Form 8606 Part III for Roth IRA
   distributions, and a list of any §72(t) exceptions the user qualifies
   for. The exception numbers from the Form 5329 instructions are below in
   the "Line-by-line guidance" section.

5. **For Part III/IV (excess IRA / Roth contributions)**: the prior-year
   carryover of excess (if any), the current-year excess (= contribution −
   limit), and whether any excess was withdrawn (with earnings) before the
   filing deadline.

6. **For Part IX (missed RMD)**: the RMD amount that should have been
   distributed, the amount actually distributed during the year, and
   **whether the user is requesting a waiver** under the "reasonable cause"
   provision of IRC §4974(d). If yes, the agent prepares the waiver
   attachment and enters "RC" and the waived amount in parentheses next to
   Line 54a/54b, reducing that line (to 0 for a full waiver).

7. **For SECURE 2.0 corrected RMDs**: the date the missed RMD was actually
   distributed. If the full shortfall is distributed, and the return
   reflecting the tax is filed, during the correction window (ends no later
   than the last day of the second taxable year beginning after the year
   the tax is imposed; earlier if the IRS mails a deficiency notice or
   assesses the tax), that plan goes on Lines 52a/53a at 10% instead of 25%
   (IRC §4974(e), added by SECURE 2.0 Act §302).

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

a) Sum the taxable early distributions from 1099-Rs with codes 1, J, S,
L, 8/P earnings, or 2 when the exception does not cover the whole amount,
or where the user knows the distribution was under 59½ regardless of code.
For Roth IRAs use Form 8606 line 25c plus any recapture amount. The total
goes on Line 1.

b) Apply exceptions from the IRC §72(t) catalog. The user gets to subtract
amounts that fall under each exception (medical, higher ed, first home,
corrective earnings, etc.). The exception total goes on Line 2 with the
exception number from the Form 5329 instructions (99 if more than one).

c) Line 3 = Line 1 − Line 2 (taxable early distribution amount).
d) Line 4 = Line 3 × 10% (or × 25% for SIMPLE-IRA distributions in first 2
years; see the SIMPLE-IRA flag on the form).

The result on Line 4 flows to Schedule 2 Line 8 (2025 form).

### Step 4 — Compute Part III/IV (excess contributions) if applicable

The 6% excise tax is on the lesser of:
- The excess contribution + any prior-year excess still in the account, OR
- The value of the IRA on the last day of the tax year

Carrying excess forward without correcting compounds the 6% tax every year
until corrected. Surface this loudly to the user — most don't realize it.

If the user can still correct (return excess + attributable earnings before
the filing deadline including extensions), recommend correction over paying
6%. The user's custodian processes this as a "removal of excess
contribution"; for IRAs the earnings portion is taxable for the year of
contribution (Pub. 590-A). If under 59½, report the earnings on Part I
Line 1 and Line 2 with exception 21 (no 10% tax for corrective
distributions made on or after December 29, 2022). A timely filer who
missed the deadline still has 6 months after the due date excluding
extensions, with an amended return marked "Filed pursuant to section
301.9100-2".

### Step 5 — Compute Part IX (missed RMD) if applicable

a) Lines 52a / 52b — RMD that should have been taken (prior-year 12/31
account balance ÷ the applicable Pub. 590-B Appendix B factor: Table III
Uniform Lifetime for most owners, Table I Single Life for beneficiaries).
Line 52a holds plans whose full shortfall was distributed during the
correction window; Line 52b all other plans.

b) Lines 53a / 53b — Amount actually distributed during the tax year from
those plans (not distributions after the RMD deadline or during the
correction window).

c) Line 54a = (52a − 53a) × 10%; Line 54b = (52b − 53b) × 25%.

d) **Decision point**: is the user requesting a waiver?
- **Yes** → enter "RC" and the shortfall to be waived in parentheses on
  the dotted line next to Line 54a/54b, subtract it, and enter the result;
  attach a statement explaining (i) the reasonable error behind the
  shortfall (illness, custodian error, recently inherited account, etc.)
  and (ii) the steps taken to remedy it (the missed RMD has been or will be
  distributed by date X). The IRS reviews the request and notifies the user
  if it is not granted.
- **No** → Lines 54a/54b as computed in step c.

Line 55 = Line 54a + Line 54b.

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
- Form 1040 Line 23 reflects total (2025 form)
- Form 8606 if the user had a nonqualified Roth IRA distribution or a
  nondeductible traditional IRA contribution (see the 2025 Form 8606)
- Schedule 1 if the user has any retirement-related deductions affected
- Reminder to take any uncorrected missed RMD now if not already done
- Reminder to update beneficiary designations and 12/31 balance tracking
  for next year

### Step 10 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md). Form 5329
is supported by IRS Free File Fillable Forms when attached to a 1040 (FFFF
cannot carry a waiver statement); a standalone Form 5329 cannot be filed
electronically and must be mailed.

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
Line 2). Each exception has a number listed in the 2025 Form 5329
instructions, Line 2:

| No. | Exception |
|------|-----------|
| 01 | Qualified plan (not IRA) distributions after separation from service in or after the year of age 55 (50 for qualified public safety employees and private sector firefighters, or 25 years of service) |
| 02 | Series of substantially equal periodic payments (SoSEPP) under §72(t)(2)(A)(iv) |
| 03 | Total and permanent disability (§72(m)(7)) |
| 04 | Death (not modified endowment contracts) |
| 05 | Unreimbursed medical expenses minus 7.5% of AGI |
| 06 | QDRO payments to an alternate payee (not IRAs) |
| 07 | IRA distributions for health insurance premiums while unemployed |
| 08 | IRA distributions for qualified higher education expenses |
| 09 | IRA distributions for a first home (lifetime cap $10,000) |
| 10 | IRS levy on the qualified plan |
| 11 | Qualified reservist distributions (active duty 180+ days) |
| 12 | Distributions coded 1, J, or S received at 59½ or older |
| 13 | Section 457 plan distributions not from a qualified-plan rollover |
| 14 | Pre-March 1, 1986 written election |
| 15 | Section 404(k) dividends |
| 16 | Annuity investment before August 14, 1982 |
| 17 | Federal phased retirement annuity payments |
| 18 | §414(w) permissible withdrawals (automatic enrollment) |
| 19 | Qualified birth or adoption distribution (up to $5,000, within 1 year; attach a statement with the child's name, age, TIN) |
| 20 | Terminal illness (death expected within 84 months) |
| 21 | Corrective distribution of income on excess contributions by the due date including extensions |
| 22 | Domestic abuse victim distribution (lesser of $10,300 for 2025 / $10,500 for 2026 or 50% of vested balance) |
| 23 | Emergency personal expense distribution (one per year; lesser of $1,000 or vested balance over $1,000) |
| 99 | More than one exception applies |

Qualified disaster recovery distributions (up to $22,000 per disaster) are
not reported on Form 5329; they go on Form 8915-F (Pub. 590-B (2025),
chapter 3).

For each exception claimed, the user must be ready to substantiate it.
The IRS does not request documentation up front but can in a notice or
audit.

If the user qualifies for *multiple* exceptions for different portions of
the distribution, enter the total excepted amount on Line 2 with exception
number **99** and keep a worksheet of the pieces.

### Part II — Distributions from education / ABLE accounts (Lines 5-8)

Applies to amounts included in income from Coverdell ESAs, qualified
tuition programs (QTPs), and ABLE accounts. The 10% additional tax applies
on the taxable portion. Line 6 exceptions: death or disability of the
beneficiary, tax-free scholarships, U.S. military academy attendance, and
amounts taxable only because the expenses were used for the American
opportunity or lifetime learning credit.

### Part III — Excess contributions to traditional IRAs (Lines 9-17)

The 6% tax on excess contributions to a traditional IRA. Excess =
contribution − the limit for the year (smaller of taxable compensation or
$7,000 / $8,000 if 50+ for 2025; $7,500 / $8,600 for 2026, Notice 2025-67).

Key inputs (2025 form):
- Line 9 — prior-year excess from the 2024 Form 5329 Line 16
- Lines 10-12 — unused 2025 limit, 2025 taxable distributions, and 2025
  distributions of prior-year excess; Line 13 = 10 + 11 + 12
- Line 14 — prior-year excess remaining (Line 9 − Line 13)
- Line 15 — 2025 excess contributions (not counting amounts withdrawn
  with earnings by the due date)
- Line 16 — total excess remaining at end of year (Line 14 + Line 15;
  carries forward)
- Line 17 — 6% × the smaller of Line 16 or the 12/31 account value

### Part IV — Excess contributions to Roth IRAs (Lines 18-25)

Mirrors Part III but for Roth IRAs: Line 18 prior-year excess (2024 Line
24), Line 19 unused Roth limit, Line 20 Roth distributions, Line 22 prior
excess remaining, Line 23 2025 excess, Line 24 total, Line 25 6%. The
income-based phaseout on Roth contributions creates the most common error:
a high-earner who contributed $X early in the year, then crossed the
phaseout threshold, and now has excess. Custodians don't track this — the
user must. Phaseouts: 2025 $150,000–$165,000 single / $236,000–$246,000
MFJ (Notice 2024-80); 2026 $153,000–$168,000 / $242,000–$252,000 (Notice
2025-67); MFS who lived with the spouse $0–$10,000.

Two correction paths:
- **Withdraw excess + earnings before deadline**: no 6% excise tax. Earnings
  are taxable; if under 59½, they go on Part I Line 1 and Line 2 with
  exception 21, so no 10% tax.
- **Recharacterize** to a traditional IRA before the deadline: treats the
  contribution as a traditional IRA contribution from the start. Eliminates
  the Roth-side excess. Does *not* eliminate a traditional-IRA-side excess
  if the user also exceeded the traditional limit.

### Part V — Excess contributions to Coverdell ESAs (Lines 26-33)

6% tax on excess contributions to a Coverdell ESA (limit: smaller of
$2,000 or the sum the contributors may contribute, with contributor
phaseouts).

### Part VI — Excess contributions to Archer MSAs (Lines 34-41)

Rare. Most filers have HSAs (Part VII) instead.

### Part VII — Excess contributions to HSAs (Lines 42-49)

6% tax on excess HSA contributions. The HSA contribution limit is
coverage-dependent: 2025 $4,300 self-only / $8,550 family (Rev. Proc.
2024-25); 2026 $4,400 / $8,750 (Rev. Proc. 2025-19); +$1,000 at 55+. Line
44 takes Form 8889 line 16; Line 47 is Form 8889 line 2 over line 12 (not
counting excess withdrawn by the due date) plus excess employer
contributions. See [`../form-8889/SKILL.md`](../form-8889/SKILL.md).

### Part VIII — Excess contributions to ABLE accounts (Lines 50-51)

6% tax on excess ABLE contributions. ABLE limit is the federal annual gift
tax exclusion ($19,000 for 2025 and 2026; Rev. Procs. 2024-40 and
2025-32), plus an additional allowance for employed beneficiaries.

### Part IX — Additional tax on excess accumulation (Lines 52a-55) — Missed RMD

The big one (2025 form):
- **Lines 52a / 52b** — RMD for plans whose full shortfall was distributed
  during the correction window / for all other plans
- **Lines 53a / 53b** — Amount distributed during the year from those plans
- **Line 54a** — (52a − 53a) × 10%; **Line 54b** — (52b − 53b) × 25%
- **Line 55** — Line 54a + Line 54b → Schedule 2, line 8

**Waiver request**: if the shortfall was due to reasonable error and the
user is taking reasonable steps to remedy it, the user can request a
waiver: enter "RC" and the waived amount in parentheses next to Line
54a/54b, subtract it, complete Line 55, and attach a statement. See
[`references/missed-rmd.md`](./references/missed-rmd.md).

**SECURE 2.0 changes (effective 2023+)**:
- The penalty was 50% before 2023; SECURE 2.0 §302 dropped it to 25%
- The correction-window reduction drops it to 10% (window ends no later
  than the last day of the second taxable year beginning after the year
  the tax is imposed; e.g., 12/31/2027 for a missed 2025 RMD)
- RMD age increased from 72 to 73, and to 75 for individuals who reach
  74 after December 31, 2032 (IRC §401(a)(9)(C)(v))

---

## Validation

Before declaring the form ready, run these checks. Surface any failure;
do not silently fix.

### Math checks

- [ ] Part I: Line 3 = Line 1 − Line 2; Line 4 = Line 3 × 10% (25% on the
      SIMPLE first-2-years part)
- [ ] Part III: Line 13 = 10 + 11 + 12; Line 14 = max(0, Line 9 − Line 13);
      Line 16 = Line 14 + Line 15; Line 17 = 6% × min(Line 16, 12/31 value)
- [ ] Part IV: Line 21 = 19 + 20; Line 22 = max(0, 18 − 21); Line 24 = 22 +
      23; Line 25 = 6% × min(Line 24, 12/31 value)
- [ ] Part IX: Line 54a = (52a − 53a) × 10%; Line 54b = (52b − 53b) × 25%
      (each reduced by any "RC" waived amount); Line 55 = 54a + 54b
- [ ] Sum of all Part totals matches the number flowed to Schedule 2 Line 8

### Sanity checks (warn, do not block)

- [ ] Part I exception number claimed but the account type doesn't match
      what the exception expects (e.g., user claims 01 "separation after
      55" but the distribution is from an IRA, where that exception doesn't
      apply); more than one exception but number other than 99
- [ ] Part III/IV: prior-year excess carried forward but no Part III/IV on
      the prior year's Form 5329 → user may have under-reported in prior
      years
- [ ] Part IX: waiver requested but no attachment statement drafted
- [ ] Part IX: Line 52a + 52b (RMD) = 0 → does the user actually have an RMD
      requirement? If turning 73 this year, the first RMD has an April 1
      of *next year* deadline (so might not be missed yet)
- [ ] Part IX: a distribution made after the RMD deadline or during the
      correction window included on Line 53a/53b → remove it
- [ ] Roth IRA excess: user's MAGI for the year was above the Roth phaseout,
      but no Part IV → user may not realize the contribution was fully
      ineligible
- [ ] SIMPLE IRA distribution within 2 years of plan participation: rate is
      25%, not 10% — confirm the agent applied the right rate
- [ ] Multiple exceptions claimed totaling more than Line 1 → impossible;
      stop and re-check
- [ ] Earnings on a timely withdrawn excess IRA contribution taxed at 10% →
      should be on Line 2 with exception 21

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
2. Exception amount + number:                       $X,XXX (NN, or 99 if several)
3. Amount subject to additional tax (Line 1 - 2):   $X,XXX
4. Additional tax (Line 3 × 10% or × 25%):          $XXX

## Part II — Distributions From Education / ABLE Accounts (if applicable)
[lines as filled]

## Part III — Excess Contributions to Traditional IRAs (if applicable)
9.  Prior-year excess (2024 Form 5329 Line 16):     $X,XXX
10. Unused current-year limit:                      $X,XXX
[continue through Line 17; Line 15 = current-year excess]

## Part IV — Excess Contributions to Roth IRAs (if applicable)
[lines as filled]

## Part V/VI/VII/VIII — (if applicable)
[lines as filled]

## Part IX — Excess Accumulation (Missed RMD) (if applicable)
52a. RMD, plans fully corrected in the window:      $X,XXX
52b. RMD, all other plans:                          $X,XXX
53a. Distributed during the year (52a plans):       $X,XXX
53b. Distributed during the year (52b plans):       $X,XXX
54a. (52a − 53a) × 10%:                             $X,XXX  [RC ($X,XXX) if waiver]
54b. (52b − 53b) × 25%:                             $X,XXX  [RC ($X,XXX) if waiver]
55.  Line 54a + Line 54b:                           $X,XXX

## Total additional tax flowing to Schedule 2 Line 8: $X,XXX

## Required attachments
- [ ] Waiver-request statement (if Part IX waiver requested)
- [ ] Form 1040 (if not standalone)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 5329 (2025, created 6/12/25)
- IRS Instructions for Form 5329 (2025, Nov 19, 2025)
- IRC §72(t), §4973, §4974
- SECURE 2.0 Act §302 (RMD penalty reduction; effective 2023)
- (any other authority used)
```

If a waiver is being requested, the deliverable additionally includes:

```markdown
# Form 5329 Lines 54a/54b — Waiver Request Statement
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

I respectfully request that the IRS waive the additional tax under
IRC §4974(d). I have entered "RC" and the waived amount next to Line
54a/54b of Form 5329 as the instructions direct.

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
- [`examples/missed-rmd-waiver.md`](./examples/missed-rmd-waiver.md) — 67-year-old who missed a 2025 inherited-IRA RMD, Part IX with waiver request
- [`examples/excess-roth-high-earner.md`](./examples/excess-roth-high-earner.md) — High-earner who over-contributed to Roth IRA after crossing phaseout, recharacterization vs. 6% Part IV decision

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS
site for the tax year being filed.

- [Form 5329 (2026): Early-Withdrawal and Excess-Contribution Penalties + AI Agent Skill](https://jupid.com/blog/form-5329-retirement-penalties-2026) — Jupid's narrative companion to this skill
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
- SECURE 2.0 Act of 2022 (P.L. 117-328) — §302 (RMD penalty reduction), §314 (domestic-abuse exception), §115 (emergency-expense exception), §333 (no 10% tax on corrective-distribution earnings)
- IRC §6501(l)(4) — for IRA §4973/§4974 taxes the income tax return starts the assessment period (6 years for unreported §4973 excess-contribution tax)
- Notice 2024-80 — 2025 limits ($7,000 IRA, $1,000 catch-up; Roth phaseout $150,000–$165,000 single, $236,000–$246,000 MFJ; domestic abuse cap $10,300)
- Notice 2025-67 — 2026 limits ($7,500 IRA, $1,100 catch-up; Roth phaseout $153,000–$168,000 single, $242,000–$252,000 MFJ; domestic abuse cap $10,500)
- Rev. Procs. 2024-25 / 2025-19 — 2025 / 2026 HSA limits
- Notice 2024-55 — emergency personal expense and domestic abuse distributions

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. The waiver-request narrative
is a template; the user's specific reasonable cause must be true and
substantiable. Complex situations (multiple plans, inherited IRAs spanning
multiple beneficiaries, plan-level corrections) warrant a licensed tax
professional's review before filing.
