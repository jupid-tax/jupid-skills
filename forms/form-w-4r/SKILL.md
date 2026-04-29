---
name: form-w-4r
description: >
  Use this skill when an individual needs to instruct a payor (IRA custodian,
  401(k) plan administrator, employer paying severance, ESOP, or other
  retirement-plan trustee) how much federal income tax to withhold from a
  NONPERIODIC payment. Triggers on phrases like "W-4R", "Form W-4R",
  "withholding on IRA distribution", "withholding on 401(k) rollover",
  "lump sum distribution withholding", "nonperiodic payment withholding",
  "severance withholding", "ESOP distribution withholding", "20% mandatory
  withholding", "opt out of withholding on IRA", "rollover withholding".
  Also engages when the user asks "how much will be withheld from my
  $X distribution". Do NOT use for regular wage withholding (use Form W-4).
  Do NOT use for periodic pension or annuity payments lasting more than
  one year (use Form W-4P). Do NOT use for non-resident alien withholding
  on US-source retirement payments (use Form W-8BEN / W-8 series). Do NOT
  use for state-tax withholding on retirement distributions (state-specific
  forms; varies).
form: Form W-4R (Withholding Certificate for Nonperiodic Payments and Eligible Rollover Distributions)
audience: [individual]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/fw4r.pdf
---

# Form W-4R — Withholding on Nonperiodic Payments and Eligible Rollover Distributions

This skill produces a properly filled Form W-4R that an individual hands to a payor (IRA custodian, 401(k) trustee, employer, ESOP, etc.) to set federal income tax withholding on a nonperiodic distribution. The form has only a few fields, but the consequences of getting them wrong are real: under-withholding can trigger §6654 estimated-tax penalties, and over-withholding ties up cash until refund.

The judgment is concentrated in two places: (a) **classifying the payment correctly** — eligible rollover distribution (default 20% mandatory) vs. other nonperiodic (default 10%) vs. periodic (wrong form — use W-4P) — and (b) **picking the right withholding rate** given the recipient's overall tax position, especially when the distribution stacks on top of wages, Social Security, or other income.

The form was redesigned in 2022 (effective 2023) to decouple from Form W-4. Pre-2023 filers who used the old combined form must switch to W-4R (or W-4P, depending on payment type).

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form W-4R, "W-4R", or "withholding certificate for nonperiodic payments"
- The user is taking an IRA distribution (Traditional, SEP, SIMPLE — Roth withdrawals generally don't require W-4R because they're often non-taxable, but see Step 1)
- The user is taking a lump-sum distribution from a 401(k), 403(b), 457(b), or other employer retirement plan
- The user is rolling over a 401(k) to an IRA and wants to know about the 20% mandatory withholding (and whether it applies)
- The user is receiving severance, a lump-sum pension, or an ESOP distribution
- The user is opting out of default withholding on a Roth IRA conversion
- The user mentions "10% default withholding" or "20% mandatory withholding"

Do **not** engage this skill when:

- The user is asking about wage withholding from a job → use [`form-w-4`](../form-w-4/SKILL.md) (forthcoming)
- The user is receiving periodic pension or annuity payments scheduled for more than one year → use [`form-w-4p`](../form-w-4p/SKILL.md) (forthcoming). Periodic = monthly/quarterly/annual recurring; nonperiodic = one-time or unscheduled.
- The user is a non-resident alien receiving US-source retirement payments → use Form W-8BEN (NRA withholding rules under IRC §1441)
- The user is asking about state income tax withholding → state-specific forms; varies by state. Some payors handle state withholding on the same intake form as W-4R; others require a separate state form.
- The user is the payor (IRA custodian, plan administrator) asking how to apply the form → see Pub. 15-A and Pub. 15-T from the payor's perspective; this skill is for the payee
- The user is making a direct trustee-to-trustee rollover (no W-4R needed — the distribution is not subject to withholding because the funds never go to the participant)

If the payment type is ambiguous, ask before proceeding. The most common confusion: "rollover" can mean (a) direct trustee-to-trustee transfer (no withholding, no W-4R) or (b) 60-day indirect rollover where the distribution is paid to the participant who then deposits it into an IRA within 60 days (20% mandatory withholding applies). These are very different.

---

## Prerequisites

Before producing anything, the agent must have these inputs. **If any are missing, ask explicitly and stop until you get an answer.** Do not pick defaults — the wrong rate either over-withholds (cash flow drag) or under-withholds (penalty exposure).

### Always required

1. **Recipient's full legal name** — must match the SSN on file with the payor
2. **Recipient's SSN** — for the form header
3. **Recipient's address** — match the address on file with the payor (if changed, update with the payor first)
4. **Payment type**, classified as one of:
   - **Eligible rollover distribution (ERD)** — IRC §402(c) / §3405(c). Examples: 401(k) lump sum to participant, partial 401(k) cash-out, profit-sharing plan distribution to participant. **Default 20% mandatory withholding** applies if paid to participant. The recipient cannot reduce below 20% on the W-4R but can request a *higher* rate.
   - **Other nonperiodic distribution** — IRC §3405(b). Examples: traditional IRA cash withdrawal, severance, ESOP cash, lump-sum pension that does not qualify as ERD. **Default 10% withholding** applies. The recipient can request 0% (opt out) or any rate up to 100%.
   - **Periodic payment** — wrong form; use W-4P instead.
5. **Payor name and address** — Form W-4R Line 1a / 1b. The plan / custodian / employer paying the distribution. Required so the payor can match the form to the right account.
6. **Desired withholding rate**, expressed as a percentage 0% through 100%. Constraints depend on payment type:
   - **ERD**: minimum 20%; higher allowed up to 100%
   - **Other nonperiodic**: 0% (opt out) through 100%; 10% if Line 2 left blank
7. **Tax year** the distribution will occur in — drives the form revision and the marginal-rate analysis if the user wants the agent to recommend a rate

### Required for rate recommendation (optional Step 4)

If the user asks the agent to recommend a withholding rate (rather than picking one themselves):

- Recipient's filing status (single, MFJ, MFS, HoH, QW)
- Estimated total taxable income for the year (wages, SS, other distributions, business income, investment income, etc.)
- Estimated total federal tax liability before considering the distribution
- Distribution amount being withheld on
- Whether other withholding sources (W-2, prior W-4P, 1099 voluntary withholding) cover the rest of the tax liability

If these inputs are not available, the agent recommends the **default** (20% for ERD, 10% for other nonperiodic) and notes the user should consult a tax pro for a more precise rate.

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Classify the payment

Walk [`references/payment-types.md`](./references/payment-types.md). Block early if the payment is:

- **Periodic (>1 year scheduled)** → wrong form. Redirect to W-4P.
- **Direct trustee-to-trustee rollover** → no W-4R needed. The distribution is not subject to withholding because the funds never reach the participant.
- **Roth qualified distribution** → no W-4R typically needed; the distribution is generally not taxable (recipient meets §408A(d)(2) qualified-distribution requirements) so no withholding applies. If the Roth distribution is non-qualified (early withdrawal of earnings), the taxable portion is subject to default 10% withholding and W-4R applies.
- **Required Minimum Distribution (RMD)** — these are typically nonperiodic and W-4R applies; default 10% unless the recipient elects otherwise.
- **Hardship withdrawal** — treated as a nonperiodic distribution for withholding (not an ERD because hardship withdrawals are not eligible to be rolled over). Default 10% applies.

If the payment is genuinely an ERD, the recipient is bound by the 20% floor on the W-4R. The recipient can elect a higher rate but cannot go below 20% (the payor will reject below-20% requests on ERDs).

### Step 2 — Confirm the recipient information

Pull the recipient's name, SSN, and address from the payor's records (the user's most recent statement from the IRA custodian, 401(k) plan administrator, or employer). Mismatches between Form W-4R and payor records will delay the distribution.

### Step 3 — Determine the withholding rate

Two paths:

**Path A — User specifies the rate.** Take it. Validate that it falls within the allowed range for the payment type:
- ERD: 20–100
- Other nonperiodic: 0–100

**Path B — User asks the agent to recommend.** Walk [`references/rate-selection.md`](./references/rate-selection.md). Use the recipient's filing status and estimated total income to identify the marginal bracket the distribution will land in. Common patterns:

- **High-income recipient already over-withheld via W-2**: 0% on the W-4R may be appropriate (other nonperiodic) — the W-2 covers the additional tax
- **Retiree with no other withholding**: pick the marginal bracket rate that the distribution lands in (10%, 12%, 22%, 24%, 32%, 35%, 37% for 2026)
- **Young recipient taking early withdrawal**: remember the additional 10% §72(t) penalty is NOT covered by W-4R — the recipient must pay it via Form 5329 / quarterly estimates
- **Roth conversion (taxable amount is the conversion)**: typically 0% on W-4R, then pay tax via quarterly estimates from non-IRA cash so the converted amount stays in the Roth

For ERDs, if the recipient does not want any actual withholding (because they intend to roll over the full amount), they cannot do that via W-4R — they must do a **direct trustee-to-trustee rollover** instead, which bypasses withholding entirely.

### Step 4 — Fill Form W-4R

Walk [`references/line-by-line.md`](./references/line-by-line.md). The form has very few lines:

- Header: Name, SSN, Address
- Line 1a: Payor name
- Line 1b: Payor address
- Line 2: Withholding rate (whole percentage, 0–100)
- Signature block: signature, date

That's it. The form has no "allowances" or dependents (unlike W-4 / W-4P) — just the rate.

### Step 5 — Confirm signature requirements

The recipient signs and dates. The payor does not sign; the payor retains the form in its records. The recipient may want a copy for their records; the payor is required to retain.

For ERDs paid jointly to spouses (e.g., spousal QDRO distribution), each spouse files their own W-4R for their respective share of the distribution.

### Step 6 — Run validation checks

See **Validation** below.

### Step 7 — Produce the deliverable

See **Output format** below.

### Step 8 — Hand off downstream

State the next steps the recipient should be aware of:

- **Estimated tax**: if the W-4R rate is below the recipient's actual marginal rate, the recipient may owe a §6654 underpayment penalty. Recommend pay-via-Form-1040-ES if the gap is significant.
- **§72(t) early-withdrawal penalty**: if the recipient is under 59½ (or applicable exception age), the additional 10% penalty applies to the taxable distribution. W-4R does NOT withhold for §72(t) — the recipient pays this with Form 5329 / quarterly estimates.
- **State tax withholding**: most states have separate state-tax withholding rules for retirement distributions. Some payors handle state withholding on the same intake form; others require a state-specific form. Check with the payor.
- **Form 1099-R**: the payor will issue Form 1099-R in January reporting the distribution and the federal income tax withheld. The recipient uses this to file Form 1040 for the year of the distribution.
- **Direct rollover alternative (for ERDs)**: if the recipient hasn't decided yet, surface that a direct trustee-to-trustee rollover bypasses the 20% mandatory withholding entirely. This is often the right move when the goal is to move funds from one retirement account to another without taking constructive receipt.

### Step 9 — File the form (i.e., deliver to payor)

Form W-4R is not filed with the IRS. It is given directly to the **payor** (the IRA custodian, plan administrator, or employer). The payor retains it and applies the elected rate to the distribution.

If the agent has access to the payor's web portal or document-upload mechanism and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree for delivery channel (payor portal upload, email, fax, mail)
- Pre-flight checklist
- Common payor-portal patterns (Fidelity, Schwab, Vanguard, large 401(k) recordkeepers)
- Security rules

If the user only wants the form filled and will hand it to the payor themselves, skip this step.

---

## Line-by-line guidance

The form is short. Full reference at [`references/line-by-line.md`](./references/line-by-line.md). Summary:

### Header

| Field | What goes here |
|-------|----------------|
| Name | Full legal name as on file with the payor |
| Social Security number | 9-digit SSN |
| Address | Match address on file with payor |
| City, state, ZIP | Match address on file with payor |

### Line 1 — Payor identification

- **1a**: Payor's name (e.g., "Fidelity Brokerage Services LLC", "Charles Schwab & Co.", "Vanguard Marketing Corp.", "ABC Company 401(k) Plan")
- **1b**: Payor's address (street + city/state/ZIP). Pull from a recent statement.

### Line 2 — Withholding rate

Enter a whole percentage from 0 to 100. Constraints:

- **Eligible rollover distribution**: minimum 20%. Entering below 20% is invalid; the payor will apply 20% by default.
- **Other nonperiodic distribution**: 0–100. Blank = 10% default.

### Signature block

Recipient signs and dates. Penalty-of-perjury declaration applies — the recipient certifies the form is correct.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Classification checks

- [ ] Payment type confirmed: ERD vs. other nonperiodic vs. periodic
- [ ] If ERD: rate ≥ 20%
- [ ] If periodic: STOP — wrong form, use W-4P
- [ ] If direct trustee-to-trustee rollover: STOP — no W-4R needed
- [ ] If Roth qualified distribution: confirm distribution is non-taxable; if so, no W-4R needed

### Recipient identification checks

- [ ] Name on form matches name on payor's records
- [ ] SSN on form matches SSN on payor's records
- [ ] Address on form matches address on payor's records (or recipient confirmed update with payor)

### Rate sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Rate = 0% on a large taxable distribution → likely under-withholding; recipient should consider quarterly estimated tax payments
- [ ] Rate < marginal bracket rate × 0.5 → likely under-withholding for the taxpayer's situation
- [ ] Rate > marginal bracket rate × 1.5 → likely over-withholding (cash tied up until refund)
- [ ] Recipient is under 59½ and taking IRA / 401(k) distribution → §72(t) 10% penalty applies in addition to ordinary income tax; W-4R does NOT cover this
- [ ] Recipient is rolling over within 60 days but distribution is paid to participant (indirect rollover) and rate < 20% → invalid for ERD; rate must be ≥ 20%; recipient must "make whole" the rolled amount with non-IRA cash to avoid taxable distribution on the withheld 20%

### Cross-form checks

- [ ] If recipient also has a W-4P on file (periodic pension), confirm the two forms are coordinated — they apply to different payment streams from potentially different payors
- [ ] If recipient has W-2 wages with W-4 withholding, recommend an annual reconciliation against total tax liability via a Form 1040-ES projection

---

## Output format

The agent's deliverable is a **filled W-4R** the recipient signs and hands to the payor. Format:

```markdown
# Form W-4R — DRAFT for [Recipient Name]

## Filing summary
- Recipient: <name>
- SSN: <XXX-XX-XXXX>
- Payor: <payor name>
- Payment type: <ERD | other nonperiodic>
- Distribution amount: <$X,XXX> (informational; not on the form)
- Elected withholding rate: <X%>
- Default rate that would apply if blank: <20% (ERD) | 10% (other)>
- Tax year of distribution: <YYYY>

## Form W-4R (printable)

Withholding Certificate for Nonperiodic Payments and Eligible Rollover Distributions
For tax year <YYYY>

Step 1 — Personal Information

Name: <full legal name>
Social Security number: XXX-XX-XXXX
Address: <street>
City, state, ZIP: <city, state, ZIP>

Step 2 — Withholding Rate

1a. Payor name: <Fidelity / Schwab / Vanguard / employer / etc.>
1b. Payor address: <street, city, state, ZIP>

2.  Complete this line if you would like a rate of withholding that is
    different from the default withholding rate.
    
    Rate: ____% (whole percentage 0–100; if ERD, must be 20 or higher)
    [Recipient enters: <X>%]

Step 3 — Sign Here

Signature: ____________________
Date: ____________________

[Recipient signs in ink and dates the form]

## Required actions
- [ ] Recipient signs and dates the form
- [ ] Form delivered to payor (mail, fax, portal upload, or email per
       payor's accepted channels)
- [ ] Recipient retains a copy

## Validation summary
- Classification: <pass — ERD | other nonperiodic>
- Rate within allowed range: <pass | fail>
- Recipient ID matches payor records: <pass | fail>
- Sanity warnings: <list>

## Estimated tax impact
- Distribution: $<amount>
- Withholding at <X>%: $<amount>
- After-withholding cash to recipient: $<amount>
- Estimated additional federal tax owed at filing (or refund) given
  marginal rate of <Y>%: <±$amount> (informational; based on inputs
  provided; not a tax projection)

## Reminders
- §72(t) early-withdrawal 10% penalty if under 59½ — paid separately on
  Form 5329, NOT covered by W-4R
- State income tax withholding may apply — check with payor for state form
- Form 1099-R issued by payor in January; reconcile on Form 1040
- If indirect rollover within 60 days: ERD 20% withholding must be
  "made whole" with non-IRA cash to avoid a taxable distribution on
  the withheld portion

## Sources cited in this draft
- IRS Form W-4R (Rev. <YYYY>, current as of 2026-04-29)
- IRC §3405 (withholding on retirement plan distributions)
- IRC §3405(b) (other nonperiodic — 10% default)
- IRC §3405(c) (eligible rollover distributions — 20% mandatory)
- IRC §72(t) (early-withdrawal additional tax — separate from W-4R)
- IRC §402(c) (eligible rollover distribution definition)
- Pub. 15-A (Employer's Supplemental Tax Guide — payor's perspective)
- Pub. 575 (Pension and Annuity Income)
- Pub. 590-A (IRA Contributions)
- Pub. 590-B (IRA Distributions)
```

The draft is **not** the form delivered to the IRS — Form W-4R is delivered to the payor. The payor retains it and applies the rate.

---

## References

Loaded on demand based on what the recipient's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — every field on Form W-4R with examples
- [`references/payment-types.md`](./references/payment-types.md) — ERD vs. other nonperiodic vs. periodic; full classification flowchart with §3405 citations
- [`references/rate-selection.md`](./references/rate-selection.md) — how to pick a rate given filing status, marginal bracket, other withholding sources
- [`references/rollover-mechanics.md`](./references/rollover-mechanics.md) — direct vs. indirect rollover, 60-day rule, "make whole" mechanics for 20% withheld
- [`references/common-mistakes.md`](./references/common-mistakes.md) — top recipient mistakes with citations and fixes
- [`filing.md`](./filing.md) — delivery playbook for handing the form to the payor (portal upload, fax, mail)

## Examples

End-to-end worked W-4Rs.

- [`examples/ira-lump-sum.md`](./examples/ira-lump-sum.md) — Traditional IRA holder taking $50K lump sum, opting for 12% default-bracket withholding
- [`examples/401k-direct-rollover.md`](./examples/401k-direct-rollover.md) — 401(k) participant doing direct rollover to IRA — no W-4R needed, contrast with indirect-rollover scenario
- [`examples/severance-payment.md`](./examples/severance-payment.md) — Employee receiving $30K lump-sum severance, classification as W-4R (not W-4)

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the year of the distribution.

- [Form W-4R](https://www.irs.gov/pub/irs-pdf/fw4r.pdf) — the form itself; instructions are printed on the form (no separate iw4r.pdf exists)
- [About Form W-4R](https://www.irs.gov/forms-pubs/about-form-w-4r) — IRS landing page with revision history
- IRC §3405 — withholding on retirement plan distributions (general)
- IRC §3405(a) — periodic payments (use W-4P)
- IRC §3405(b) — other nonperiodic distributions (10% default, can opt out)
- IRC §3405(c) — eligible rollover distributions (20% mandatory if paid to participant)
- IRC §402(c) — eligible rollover distribution definition
- IRC §402(c)(4) — items that are NOT ERDs (RMDs, hardship, substantially-equal periodic payments, etc.)
- IRC §72(t) — 10% additional tax on early withdrawals (separate from W-4R)
- IRC §6654 — underpayment-of-estimated-tax penalty (relevant if W-4R rate is too low)
- [Pub. 15-A — Employer's Supplemental Tax Guide](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — payor's perspective on W-4R application
- [Pub. 575 — Pension and Annuity Income](https://www.irs.gov/pub/irs-pdf/p575.pdf)
- [Pub. 590-A — Contributions to IRAs](https://www.irs.gov/pub/irs-pdf/p590a.pdf)
- [Pub. 590-B — Distributions from IRAs](https://www.irs.gov/pub/irs-pdf/p590b.pdf)
- [Form 5329](https://www.irs.gov/pub/irs-pdf/f5329.pdf) — additional taxes on qualified plans (where §72(t) penalty is reported)
- [Form 1099-R](https://www.irs.gov/pub/irs-pdf/f1099r.pdf) — payor's reporting of the distribution and withholding

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Withholding-rate selection has direct cash-flow and penalty consequences — the agent invoking this skill should remind the recipient that the output is a starting point and that complex situations (large lump sums, multiple income sources, Roth conversions, §72(t) early withdrawals, partial rollovers) warrant a licensed tax professional's review before signing.
