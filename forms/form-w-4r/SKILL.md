---
name: form-w-4r
description: >
  Use this skill when an individual needs to tell a payer (IRA custodian,
  401(k)/403(b)/governmental 457(b) plan administrator, insurance company
  paying a commercial annuity, or other retirement-plan trustee) how much
  federal income tax to withhold from a NONPERIODIC payment or an eligible
  rollover distribution. Triggers on phrases like "W-4R", "Form W-4R",
  "withholding on IRA distribution", "withholding on 401(k) cash-out",
  "lump sum distribution withholding", "nonperiodic payment withholding",
  "ESOP distribution withholding", "20% mandatory withholding", "opt out of
  withholding on IRA", "rollover withholding", "withholding on Roth
  conversion". Also engages when the user asks "how much will be withheld
  from my $X distribution". Do NOT use for wages, bonuses, or severance pay
  (wages; use form-w4). Do NOT use for periodic pension or annuity payments
  spread over more than one year (Form W-4P). Do NOT use for nonresident
  aliens or foreign estates (the form says not to; see Pub. 515 and Pub.
  519). Do NOT use for state-tax withholding on retirement distributions
  (state-specific forms; varies).
form: Form W-4R (Withholding Certificate for Nonperiodic Payments and Eligible Rollover Distributions)
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/fw4r.pdf
---

# Form W-4R — Withholding on Nonperiodic Payments and Eligible Rollover Distributions

This skill produces a properly filled Form W-4R that an individual gives to the payer of a retirement payment (IRA custodian, plan administrator, insurance company) to set federal income tax withholding on a nonperiodic payment or an eligible rollover distribution. The form has only six entries (name, SSN, address, city/state/ZIP, the line 2 rate, signature and date), but the consequences of getting the rate wrong are real: under-withholding can trigger §6654 estimated-tax penalties, and over-withholding ties up cash until refund.

The judgment is concentrated in two places: (a) **classifying the payment correctly** — eligible rollover distribution (20% default and floor) vs. other nonperiodic payment (10% default, 0–100% allowed) vs. periodic payment (wrong form, W-4P) vs. wages (wrong form, W-4) — and (b) **picking the line 2 rate** given the recipient's overall tax position, using the 2026 Marginal Rate Tables printed on the form or a full projection.

**Form revision.** The line map, rates and tables in this skill were verified on 2026-10-06 against the **2026 Form W-4R** (Cat. No. 75085T, created 12/12/25). Its instructions are printed on the form (pages 1–3); there is no separate instructions PDF. The tables change every year: re-check the 2027 form before using this skill for 2027 payments (https://www.irs.gov/forms-pubs/about-form-w-4r).

Form W-4R took over nonperiodic payments and eligible rollover distributions from Form W-4P (the form's Privacy Act notice still refers to "a previous Form W-4P that you completed with respect to your nonperiodic payments"). For payments that began before 2026, the current election (or the default rate) stays in effect unless a new W-4R is submitted (2026 Form W-4R, page 2).

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form W-4R, "W-4R", or "withholding certificate for nonperiodic payments"
- The user is taking a traditional, SEP, or SIMPLE IRA distribution (IRA distributions payable on demand are nonperiodic, per the form)
- The user is taking a lump-sum or partial cash-out from a 401(k), 403(b), governmental 457(b), or other employer retirement plan
- The user is rolling over a 401(k) to an IRA and wants to know about the 20% withholding (and whether it applies)
- The user is receiving a lump-sum pension payment, an ESOP distribution, or a nonperiodic payment from a commercial annuity
- The user is converting a traditional IRA to a Roth IRA and wants to set or opt out of withholding
- The user mentions "10% default withholding" or "20% mandatory withholding"

Do **not** engage this skill when:

- The user is asking about wage withholding from a job, a bonus, or **severance pay** → use [`form-w4`](../form-w4/SKILL.md). Severance payments are wages subject to income tax withholding, social security, Medicare and FUTA (Pub. 15 (2026), "Severance payments", and section 7: severance pay is a supplemental wage)
- The user is receiving periodic pension or annuity payments (installments at regular intervals over more than 1 year) → Form W-4P (no skill in this repo yet)
- The user receives military retirement pay or payments from certain nonqualified deferred compensation plans → Form W-4, not W-4P/W-4R (Pub. 505 (2026), chapter 1)
- The user is a nonresident alien or a foreign estate → the form says "Do not use Form W-4R"; see Pub. 515 and Pub. 519 (payers generally document foreign persons on Form W-8BEN)
- The user is asking about state income tax withholding → state-specific; ask the payer which state form it uses
- The user is the payer asking how to apply the form → payer rules are in Pub. 15-A and Pub. 15-T; this skill is for the payee
- The user is making a direct rollover or a trustee-to-trustee transfer → no withholding applies (Pub. 575 (2025), Table 1); no W-4R needed

If the payment type is ambiguous, ask before proceeding. The most common confusion: "rollover" can mean (a) a direct rollover or trustee-to-trustee transfer (no withholding, no W-4R) or (b) a 60-day rollover where the distribution is paid to the participant, who deposits it within 60 days (20% withholding applies if the payment is an eligible rollover distribution from an employer plan). These are very different.

---

## Prerequisites

Before producing anything, the agent must have these inputs. **If any are missing, ask explicitly and stop until you get an answer.** Do not pick a rate for the user — the wrong rate either over-withholds (cash flow drag) or under-withholds (penalty exposure).

### Always required

1. **Recipient's first name, middle initial, and last name** (line 1a) — as on file with the payer
2. **Recipient's SSN** (line 1b). An estate enters its EIN in the SSN space (form, "Line 1b")
3. **Recipient's address and city/state/ZIP** — the payer needs a U.S. or U.S.-territory home address to honor an election below 10% (Pub. 505 (2026), "Payments delivered outside the United States")
4. **Payer and account** — not entered on the form (the form has no payer lines), but needed to deliver it and to match the account
5. **Payment type**, classified as one of:
   - **Eligible rollover distribution (ERD)** — a distribution from a qualified plan (e.g., 401(k), governmental 457(b)) or a tax-sheltered annuity (403(b)) that is eligible to be rolled over to an IRA or qualified plan. **20% default; the recipient can't choose less than 20% (including "-0-")**; a higher rate is allowed. The form says not to give a W-4R to the payer unless the recipient wants more than 20%.
   - **Other nonperiodic payment** — e.g., a traditional IRA cash withdrawal, an RMD, a hardship withdrawal, a nonperiodic commercial annuity payment. **10% default**; the recipient can enter any rate from 0% ("-0-") to 100%, except that generally no rate below 10% is allowed for payments delivered outside the United States and its territories.
   - **Periodic payment** — wrong form; use W-4P.
   - **Wages (including severance)** — wrong form; use W-4.
6. **Taxable amount** of the payment — withholding applies only to the taxable part (Pub. 505 (2026), "Nontaxable part"; Pub. 575 (2025))
7. **Desired withholding rate**, or a request that the agent compute one (Step 3 Path B)
8. **Tax year** of the payment — drives the form revision and the Marginal Rate Tables

### Required for a rate recommendation (Step 3 Path B)

If the user asks the agent to recommend a rate:

- Filing status (Single/MFS, MFJ/QSS, HoH)
- Total income for the year **not including** this payment, and the taxable amount of the payment
- Whether the tax on all other income is already covered by other withholding or estimated payments (the tables assume it is)
- Age (for the §72(t) 10% additional tax) and any §72(t) exception the user claims
- Items the tables ignore that matter for this user: Social Security benefits that become taxable, the additional standard deduction for 65+/blind, the Schedule 1-A senior deduction, capital gains

If these inputs are not available, tell the user the default rate that will apply (20% ERD, 10% other) and that it may not match their tax; do not invent a rate.

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Classify the payment

Walk [`references/distribution-types.md`](./references/distribution-types.md). Block early if the payment is:

- **Wages or severance** → wrong form. Redirect to [`form-w4`](../form-w4/SKILL.md).
- **Periodic (installments at regular intervals over more than 1 year)** → wrong form. Redirect to W-4P. IRA distributions payable on demand are nonperiodic even if taken regularly (2026 Form W-4R, page 2).
- **Direct rollover / trustee-to-trustee transfer** → no withholding, no W-4R (Pub. 575 (2025), Table 1). This includes a direct rollover of a pre-tax 401(k) balance to a Roth IRA: taxable, but not subject to withholding.
- **Roth distribution the payer reasonably believes is not includible in income** (e.g., a qualified Roth distribution) → no withholding (Pub. 575 (2025): "There will be no withholding on any part of a distribution where it is reasonable to believe that it won't be includible in gross income"). Ask the custodian how it treats the payment.
- **Required minimum distribution, hardship distribution, or another item on the form's non-ERD list** (PLESA, domestic abuse victim, qualified disaster recovery, qualified birth or adoption, qualified long-term care, emergency personal expense distributions) → not an ERD; other nonperiodic, 10% default.
- **Nonresident alien or foreign estate** → stop; the form says not to use W-4R.

If the payment is an ERD, the recipient is bound by the 20% floor. A rate below 20% is not allowed; the only way to avoid withholding on an ERD is a direct rollover.

### Step 2 — Confirm the recipient information

Copy the recipient's name, SSN, and address from the payer's records (a recent statement). If the recipient does not provide an SSN or the IRS tells the payer the SSN is incorrect, the payer must withhold 10% and can't honor a lower rate (form, page 2 Note).

### Step 3 — Determine the withholding rate

Two paths:

**Path A — User specifies the rate.** Take it. Validate that it is a whole number within the allowed range:
- ERD: 20–100 (a W-4R is only needed for more than 20)
- Other nonperiodic: 0–100 (10–100 if the payment is delivered outside the U.S. and its territories)

**Path B — User asks the agent to recommend.** Walk [`references/withholding-rates.md`](./references/withholding-rates.md). Use the form's method:

1. Find the Marginal Rate Table rate for total income **without** the payment.
2. Find the rate for total income **including** the taxable amount of the payment.
3. If the rates match, enter that rate. If they differ, split the payment between the two brackets, multiply each part by its rate, add, divide by the payment, and round up to the next whole number (form Example 2: $3,750 on $20,000 → 19%).
4. The tables are accurate only if tax on all other income is already covered by other withholding or estimated tax. If it isn't, the form says to enter a higher rate.
5. When the tables don't fit (Social Security becomes taxable, 65+ deductions, capital gains), build a with/without projection on the 2026 rate schedule (Rev. Proc. 2025-32) instead and divide the extra tax by the payment.
6. If the recipient is under 59½ and no §72(t) exception applies, tell them the 10% additional tax is not in the tables; they may add 10 points to line 2 or pay estimated tax. Ask which.

Present the computed rate with its math and let the user choose; never pick silently.

For ERDs, if the recipient wants no withholding (because they intend to roll over the full amount), they cannot do that on the W-4R — they must request a **direct rollover**.

### Step 4 — Fill Form W-4R

Walk [`references/line-by-line.md`](./references/line-by-line.md). The 2026 form has:

- Line 1a: First name and middle initial; Last name
- Line 1b: Social security number (estate: EIN)
- Address; City or town, state, and ZIP code
- Line 2: Rate, as a whole number (no decimals), only if different from the default
- Signature and date ("This form is not valid unless you sign it")

That's it. No payer lines, no allowances, no dependents.

### Step 5 — Confirm signature requirements

The recipient signs and dates. The payer does not sign; it keeps the form. The recipient keeps a copy.

### Step 6 — Run validation checks

See **Validation** below.

### Step 7 — Produce the deliverable

See **Output format** below.

### Step 8 — Hand off downstream

State the next steps the recipient should be aware of:

- **Future payments**: the election generally applies to future payments from the same plan or IRA until a new W-4R is submitted (form, page 1).
- **Estimated tax**: if withholding is short of the recipient's tax, a §6654 penalty may apply; suggest Form 1040-ES (see [`form-1040-es`](../form-1040-es/SKILL.md)) if the gap is significant. Withholding counts as paid evenly through the year unless the taxpayer elects actual dates (Pub. 505 (2026), chapter 2).
- **§72(t) additional tax**: if the recipient is under 59½ and no exception applies, the 10% additional tax is reported on Schedule 2 (Form 1040) line 8, with Form 5329 when required (2025 Schedule 2; 2025 Instructions for Form 5329). The default rates don't account for it.
- **State tax withholding**: separate state rules; ask the payer.
- **Form 1099-R**: the payer reports the payment and withholding on Form 1099-R (box 1 gross, box 2a taxable amount, box 4 federal income tax withheld, box 7 code). Box 4 goes on Form 1040 line 25b (2025 form).
- **Direct rollover alternative (for ERDs)**: if the recipient hasn't decided, surface that a direct rollover avoids the 20% withholding entirely.

### Step 9 — Deliver the form to the payer

Form W-4R is not filed with the IRS. The form says: "Give Form W-4R to the payer of your retirement payments."

If the agent has access to the payer's web portal or document-upload mechanism and the user explicitly authorizes delivery, follow [`filing.md`](./filing.md). It contains:

- Decision tree for delivery channel (payer portal, distribution-request packet, email/fax, mail)
- Pre-flight checklist
- Field map for the fillable PDF
- Security rules

If the user only wants the form filled and will hand it to the payer themselves, skip this step.

---

## Line-by-line guidance

Full reference at [`references/line-by-line.md`](./references/line-by-line.md). Summary of the 2026 form:

### Line 1a, 1b and address

| Field | What goes here |
|-------|----------------|
| 1a First name and middle initial | As on file with the payer |
| 1a Last name | As on file with the payer |
| 1b Social security number | 9-digit SSN; an estate enters its EIN |
| Address | Street address on file with the payer |
| City or town, state, and ZIP code | Same |

### Line 2 — Withholding rate

Complete only for a rate different from the default. Whole number, no decimals.

- **Eligible rollover distribution**: 20% default; can't choose less than 20% (including "-0-"); enter a higher rate if wanted.
- **Other nonperiodic payment**: 10% default; any rate 0–100, "-0-" for no withholding; generally not below 10% if delivered outside the U.S. and its territories.
- Disability payments for injuries from a terrorist attack that are not taxable: enter "-0-" (form, page 2; Pub. 3920).

### Signature block

Recipient signs and dates. "This form is not valid unless you sign it." A form that isn't properly completed leaves the payment at the default rate (Privacy Act notice).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Classification checks

- [ ] Payment type confirmed: ERD vs. other nonperiodic vs. periodic vs. wages
- [ ] If ERD: rate ≥ 20% (and the W-4R is only needed if the rate is above 20)
- [ ] If periodic: STOP — wrong form, use W-4P
- [ ] If wages or severance: STOP — wrong form, use W-4
- [ ] If direct rollover or trustee-to-trustee transfer: STOP — no W-4R needed
- [ ] If nonresident alien or foreign estate: STOP — the form says not to use W-4R
- [ ] If Roth distribution: confirm with the custodian whether any part is taxable

### Recipient identification checks

- [ ] Name on form matches the payer's records
- [ ] SSN (or estate EIN) on form matches the payer's records
- [ ] Address is a U.S. or territory home address if the rate is below 10%

### Rate checks

- [ ] Line 2 is a whole number from 0 to 100 (no decimals, no "%")
- [ ] If the rate was computed: the Marginal Rate Table lookup (or projection) and its arithmetic are shown, and the rounding is up to the next whole number

Surface a warning, do not block, if any of these are true:

- [ ] Rate = 0% on a large taxable distribution → likely under-withholding; recipient should consider estimated tax payments
- [ ] Rate below the rate computed with the form's Marginal Rate Tables → under-withholding unless other withholding covers it
- [ ] Rate well above the computed rate → over-withholding (cash tied up until refund)
- [ ] Recipient is under 59½ and taking a taxable IRA / plan distribution with no exception → 10% §72(t) additional tax applies on top of income tax; the default rates don't cover it
- [ ] 60-day rollover of an ERD planned → the 20% withheld must be replaced from other funds to roll over the full amount; any part not rolled over (including the withheld amount) is taxable and may be subject to §72(t) (Pub. 575 (2025), "Rolling over more than amount received")

### Cross-form checks

- [ ] If recipient also has a W-4P on file (periodic pension), the two forms cover different payment streams; both elections stand
- [ ] If recipient has W-2 wages, check that W-4 withholding plus this W-4R withholding covers the year (Tax Withholding Estimator or a Form 1040-ES projection)

---

## Output format

The agent's deliverable is a **filled W-4R** the recipient signs and gives to the payer. Format:

```markdown
# Form W-4R — DRAFT for [Recipient Name]

## Filing summary (not on the form)
- Recipient: <name>
- Payer and account: <payer name, account ****1234>
- Payment type: <ERD | other nonperiodic>
- Payment amount / taxable amount: <$X,XXX / $X,XXX>
- Elected withholding rate: <X%> (line 2 <blank | X>)
- Default rate that would apply without a W-4R: <20% (ERD) | 10% (other)>
- Tax year of payment: <YYYY>

## Form W-4R (2026) entries

1a  First name and middle initial: <first M.>     Last name: <last>
1b  Social security number: XXX-XX-XXXX
    Address: <street>
    City or town, state, and ZIP code: <city, state, ZIP>
2   Rate: <X> %   (whole number; blank if the default applies)
    Signature: ____________________   Date: __________

## Rate computation (if Path B)
- Total income without payment: $<X> → table rate <a%>
- Total income with payment: $<Y> → table rate <b%>
- Split / projection: <math>
- §72(t) 10% added: <yes/no — user's choice>
- Rate entered: <X%>

## Required actions
- [ ] Recipient signs and dates the form
- [ ] Form delivered to payer (portal, mail, fax, or email per payer's accepted channels)
- [ ] Recipient retains a copy

## Validation summary
- Classification: <pass — ERD | other nonperiodic>
- Rate within allowed range: <pass | fail>
- Recipient ID matches payer records: <pass | fail>
- Sanity warnings: <list>

## Estimated tax impact
- Taxable amount: $<amount>
- Withholding at <X>%: $<amount>
- Cash to recipient after withholding: $<amount>
- Projected tax on this payment (income tax + any §72(t)): $<amount>; difference vs. withholding: <±$amount>

## Reminders
- §72(t) 10% additional tax if under 59½ with no exception — Schedule 2 line 8 (Form 5329 if required)
- State income tax withholding may apply — check with payer
- Form 1099-R from payer; box 4 goes on Form 1040 line 25b
- 60-day rollover of an ERD: replace the 20% withheld from other funds to roll over the full amount

## Sources cited in this draft
- IRS Form W-4R (2026), including its Marginal Rate Tables and instructions
- IRC §3405(b) (nonperiodic distributions), §3405(c) (eligible rollover distributions)
- IRC §402(c) (eligible rollover distribution definition)
- IRC §72(t) (additional tax on early distributions)
- Pub. 505 (2026), chapter 1; Pub. 575 (2025); Pub. 590-B (2025)
```

The draft is **not** delivered to the IRS — Form W-4R goes to the payer, which keeps it and applies the rate.

---

## References

Loaded on demand based on what the recipient's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — every entry on the 2026 Form W-4R, the line 2 rules, what is not on the form (§72(t), 1099-R, direct rollovers)
- [`references/distribution-types.md`](./references/distribution-types.md) — ERD vs. other nonperiodic vs. periodic vs. wages; classification decision tree with §3405 and §402(c) citations
- [`references/withholding-rates.md`](./references/withholding-rates.md) — default and floor rates, the 2026 Marginal Rate Tables, the form's rate-selection method, special cases (Roth, §72(t), state)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — top recipient mistakes with citations and fixes
- [`filing.md`](./filing.md) — delivery playbook for handing the form to the payer (portal, packet, email/fax, mail) and the PDF field map

## Examples

End-to-end worked W-4Rs (2026 numbers, math checked in python).

- [`examples/ira-lump-sum-withdrawal.md`](./examples/ira-lump-sum-withdrawal.md) — 65-year-old MFJ retiree taking a $50,000 traditional IRA withdrawal; projection gives 8% vs. the 10% default
- [`examples/401k-direct-rollover.md`](./examples/401k-direct-rollover.md) — 401(k) participant doing a direct rollover to an IRA — no W-4R needed, contrasted with a 60-day rollover
- [`examples/laid-off-401k-cash-out.md`](./examples/laid-off-401k-cash-out.md) — laid-off 38-year-old: severance goes through payroll as wages (W-4, not W-4R); a $24,000 401(k) cash-out is an ERD, rate set with the Marginal Rate Tables plus the §72(t) 10%

## Sources

Authoritative sources used by this skill. Re-verify each year against the IRS site for the year of the payment.

- [Form W-4R (2026)](https://www.irs.gov/pub/irs-pdf/fw4r.pdf) — the form itself; instructions, the 2026 Marginal Rate Tables and Examples 1–2 are printed on the form (no separate instructions PDF)
- [About Form W-4R](https://www.irs.gov/forms-pubs/about-form-w-4r) — IRS landing page with revision history
- IRC §3405 — withholding on pensions, annuities, and certain other deferred income
- IRC §3405(a) — periodic payments (Form W-4P)
- IRC §3405(b) — nonperiodic distributions (10%; election out allowed)
- IRC §3405(c) — eligible rollover distributions (20%; §3405(c)(2) exception for direct rollovers)
- IRC §402(c) — eligible rollover distribution definition; §402(c)(4) exclusions (substantially equal periodic payments, RMDs, hardship distributions)
- IRC §72(t) — 10% additional tax on early distributions (exceptions listed in the Instructions for Form 5329)
- IRC §6654 — underpayment-of-estimated-tax penalty
- [Pub. 505 (2026)](https://www.irs.gov/pub/irs-pdf/p505.pdf) — chapter 1, Pensions and Annuities (nonperiodic, ERD, delivery outside the U.S.)
- [Pub. 575 (2025)](https://www.irs.gov/pub/irs-pdf/p575.pdf) — Withholding Tax and Estimated Tax; Rollovers; Table 1
- [Pub. 590-B (2025)](https://www.irs.gov/pub/irs-pdf/p590b.pdf) — IRA distributions, RMDs (age 73), trustee-to-trustee transfers
- [Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) — severance payments are wages; supplemental wage rules (section 7)
- [Pub. 515](https://www.irs.gov/pub/irs-pdf/p515.pdf) and [Pub. 519](https://www.irs.gov/pub/irs-pdf/p519.pdf) — nonresident aliens and foreign estates
- [Instructions for Form 5329 (2025)](https://www.irs.gov/pub/irs-pdf/i5329.pdf) — §72(t) exception numbers 01–23
- [Instructions for Forms 1099-R and 5498](https://www.irs.gov/pub/irs-pdf/i1099r.pdf) — payer reporting, distribution codes
- Rev. Proc. 2025-32 — 2026 brackets and standard deduction (the basis of the Marginal Rate Tables)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Withholding-rate selection has direct cash-flow and penalty consequences — the agent invoking this skill should remind the recipient that the output is a starting point and that complex situations (large lump sums, multiple income sources, Roth conversions, §72(t) early withdrawals, partial rollovers) warrant a licensed tax professional's review before signing.
