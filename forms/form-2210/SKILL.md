---
name: form-2210
description: >
  Use this skill when an individual filer needs to determine whether they owe
  an underpayment of estimated tax penalty and how much, or whether they meet
  one of the safe harbors that exempts them from the penalty. Triggers on
  phrases like "underpayment penalty", "Form 2210", "estimated tax penalty",
  "should I file 2210", "annualized income method", "Schedule AI", "safe
  harbor estimated tax", "I owe more than $1,000, do I have a penalty",
  "uneven income annualized", "withholding wasn't enough", or any request to
  reconcile quarterly estimated tax payments + withholding against a current
  year's required minimum payments. Do NOT use for business estimated tax
  (corporations use Form 1120-W); first-year-of-tax-liability filers
  (statutorily exempt under IRC §6654(d)(1)(B) — no Form 2210 needed); penalty
  waiver requests for reasonable cause (Form 843 is the channel for refund
  claims of paid penalties); or estate/trust underpayment (Form 2210 has a
  separate variant for estates and trusts; this skill covers Form 2210 for
  individuals only).
form: Form 2210 (Underpayment of Estimated Tax by Individuals, Estates, and Trusts)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f2210.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2210.pdf
---

# Form 2210 — Underpayment of Estimated Tax by Individuals

This skill produces an audit-grade analysis of whether the filer owes an underpayment-of-estimated-tax penalty under IRC §6654, applies the safe harbors, computes the penalty using the regular method or the annualized income installment method (Schedule AI), and emits a deliverable showing the math line by line.

The form is structured around a flowchart on page 1 — many filers don't actually need to file Form 2210 because the IRS will compute the penalty automatically and bill the filer. The agent's job is to (a) determine whether filing the form is required, (b) determine whether filing is *advantageous* (e.g., to claim Schedule AI relief or annualize income), and (c) compute the correct penalty if required.

The key insight: **the safe harbor is met if total withholding alone (no estimated payments) is at least 90% of current-year tax OR 100% of prior-year tax (110% if prior AGI > $150K).** Filers often don't realize how much W-2 withholding does on their behalf — and the most common penalty case is a freelancer with no withholding at all.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2210, "underpayment penalty", or "estimated tax penalty"
- The user owes more than $1,000 at filing (the penalty trigger threshold under IRC §6654(d)(1)(A))
- The user has uneven income across the year (Q4 capital gain, year-end bonus, sale of property, large Roth conversion) and wants to know if Schedule AI annualization saves penalty
- The user's withholding fell below 90% of current-year tax and they want to check the prior-year safe harbor (100%, or 110% if prior AGI > $150K)
- The user got a CP14 or CP161 notice with a penalty for underpayment of estimated tax and wants to verify or contest

Do **not** engage this skill when:

- The user is a **C corporation** — corporations use **Form 1120-W** for estimated tax computation (different rules under IRC §6655)
- The user is a **first-year-of-tax-liability filer** — IRC §6654(d)(1)(B) statutorily exempts filers with zero prior-year tax liability for a full 12-month tax year. No Form 2210 needed.
- The user owes ≤ $1,000 at filing after withholding — IRC §6654(d)(1)(A) creates a de minimis exception. No penalty, no Form 2210.
- The user wants a **penalty waiver for reasonable cause** for a *paid* penalty — that is **Form 843** (Claim for Refund and Request for Abatement). Form 2210 has Part II Box A/B/C for waiver requests on the *current* return; Form 843 is for after-the-fact refund claims.
- The user is filing Form 2210-F (farmers and fishermen) or Form 2210 for an **estate or trust** (different variant; out of scope here)

If the user is unclear whether they meet the de minimis exception or the first-year exception, walk through the prerequisites and let the agent determine which path applies.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 2210 fields and quarterly due dates are tied to the tax year. The 2025 quarterly due dates were April 15, June 16, September 15, and January 15, 2026. For 2026, dates announced annually — verify current-year instructions.
2. **Filer's filing status** for the current year — affects safe harbor thresholds when prior AGI > $150K (110% safe harbor for high-AGI filers).
3. **Current-year total tax** — Form 1040 Line 22 minus refundable credits (Form 2210 Line 1 calculation; verify against current-year line numbers). This is the "tax liability" against which safe harbors are measured.
4. **Current-year withholding** — sum of all federal income tax withheld during the year (W-2 Box 2, 1099 Box 4, Form 8959 Line 24 if applicable). Withholding is treated as paid evenly across the four quarters under IRC §6654(g)(1) **unless the filer elects actual-payment-date treatment**.
5. **Current-year estimated tax payments** — by quarter, with payment dates. The agent must capture each Form 1040-ES payment, EFW (electronic funds withdrawal), or IRS Direct Pay transaction with its date. The penalty is computed quarter by quarter, and a payment one day late can shift it.
6. **Prior-year total tax** — Form 1040 Line 22 from the prior return (minus refundable credits; see Form 2210 Line 8 worksheet for the exact prior-year figure to use). Required for the 100%/110% safe harbor.
7. **Prior-year AGI** — to determine whether the 110% safe harbor applies. AGI > $150,000 (or $75,000 if MFS) triggers the higher 110% threshold.
8. **Whether the filer wants the IRS to compute the penalty** — most filers can let the IRS bill them post-filing. If the filer wants to use the annualized income installment method (Schedule AI) or claim a waiver, they must file Form 2210.
9. **Whether income was uneven across the year** — ask: "Did you have a large income event in any single quarter (year-end bonus, capital gain on a sale, Roth conversion, RSU vesting)?" If yes, Schedule AI may reduce the penalty. If no, the regular method applies.
10. **For uneven income (Schedule AI only)** — quarter-by-quarter income, deductions, and tax computation. Asks for cumulative AGI through 3/31, 5/31, 8/31, and 12/31. Most filers don't have this readily — be prepared to ask whether they can produce it from bank statements and brokerage records, or whether Schedule AI is too costly to compute relative to penalty savings.

If the user does not know any of these, do not guess. Ask. The penalty math depends on every input.

---

## Workflow

Execute these steps in order. Don't skip ahead.

### Step 1 — Run the page 1 flowchart

Form 2210 page 1 has a flowchart that determines whether the form must be filed. The agent runs this check first:

```
Is the unpaid balance (current-year tax minus withholding minus estimates) ≤ $1,000?
  Yes → No penalty, no Form 2210 needed (IRC §6654(d)(1)(A) de minimis exception)
  No  → continue

Was the prior-year tax liability $0 (and prior-year was a 12-month return, and filer was a US citizen/resident for the full prior year)?
  Yes → No penalty, no Form 2210 needed (IRC §6654(d)(1)(B) first-year exception)
  No  → continue

Is current-year withholding ≥ 90% of current-year tax?
  Yes → Safe harbor met (current-year 90% test); no penalty; no Form 2210 needed unless
        filer wants to claim Schedule AI for a different reason
  No  → continue

Is current-year withholding ≥ 100% of prior-year tax (or 110% if prior AGI > $150K)?
  Yes → Safe harbor met (prior-year safe harbor); no penalty; no Form 2210 needed
  No  → continue

→ Penalty likely owed. Filer must file Form 2210 OR let IRS compute and bill.
```

If the flowchart resolves to "no penalty", produce a one-line summary and stop. The user is done.

### Step 2 — Decide: file Form 2210 or let IRS compute?

If a penalty is owed:

- **Let IRS compute (no Form 2210 filed)**: simplest. IRS bills the penalty after processing the return. Works when the regular method gives the smallest penalty and the filer has no waiver claim.
- **File Form 2210 (regular method)**: required if the filer is requesting a waiver (Box A, B, C in Part II of the form) OR if the filer is a high-AGI prior-year filer needing to demonstrate the 110% safe harbor calculation.
- **File Form 2210 with Schedule AI (annualized method)**: required if income was uneven across the year and Schedule AI reduces the penalty below the regular method. Schedule AI is opt-in and requires quarter-by-quarter income detail.

Walk through these options with the user. If they ask "should I file?", the answer is:

- File if Schedule AI saves money and the filer can produce quarterly income data
- File if the filer is requesting a waiver
- Otherwise let IRS compute

### Step 3 — Compute required annual payment (Part I)

Part I of Form 2210 produces the "required annual payment" — the smaller of:

- 90% of current-year tax
- 100% of prior-year tax (110% if prior-year AGI > $150,000, or > $75,000 if MFS)

```
Line 1 = current-year total tax (after refundable credits)  [verify line label per current-year form]
Line 4 = Line 1 × 90%                                        (current-year safe harbor)
Line 5 = (other adjustments per current-year instructions)
Line 6 = current-year withholding
Line 7 = Line 4 − Line 6                                     (shortfall under current-year test)
Line 8 = prior-year tax × 100% (or 110% if prior AGI > $150K)
Line 9 = smaller of Line 5 or Line 8                         (the "required annual payment")
```

The required annual payment splits into four equal quarterly required installments under the regular method. If the filer's actual quarterly payments + allocated withholding fall short of the required installment in any quarter, that quarter is underpaid.

### Step 4 — Allocate withholding across quarters

Default (under IRC §6654(g)(1)): treat total annual withholding as paid evenly — $W ÷ 4 per quarter — *unless* the filer elects actual-date treatment. For most filers (steady W-2 income), even allocation is correct.

If the filer had withholding concentrated in one part of the year (e.g., a one-time bonus with high withholding in Q4), they may benefit from electing actual-date treatment for withholding. This is opt-in via Schedule AI Line 27 / Part III adjustments — see current-year instructions.

### Step 5 — Compute quarterly underpayments (Part III, regular method)

For each of the four quarterly periods, the agent computes:

```
Cumulative required = (quarter-end fraction) × required annual payment
                     (25% by 4/15, 50% by 6/15, 75% by 9/15, 100% by 1/15 next year)

Cumulative paid = withholding allocated to date + estimated payments made by the due date

Underpayment for quarter = max(Cumulative required − Cumulative paid, 0)
```

A payment made *after* a quarter's due date counts toward later quarters but not the current one. The penalty accumulates daily on each quarterly underpayment from the due date until the payment date (or April 15 of the following year, whichever is earlier).

### Step 6 — Apply the penalty rate

The penalty rate is the **federal short-term rate plus 3%**, set by IRS Revenue Ruling each quarter (e.g., the Q1 2026 rate was published in late 2025; verify against the current-quarter Revenue Ruling). The rate compounds daily.

Form 2210 has a worksheet that simplifies the daily-rate computation; the agent should pull the current-year rates from the Form 2210 instructions.

For 2025 quarterly rates (verify against current Form 2210 instructions before using):
- Rate may have varied across quarters; consult the rate table in the current Form 2210 instructions

The penalty for each quarter:

```
Penalty = underpayment × (number of days late ÷ 365) × penalty rate
```

Total penalty = sum of penalties across the four quarters.

### Step 7 — If using Schedule AI (annualized method), recompute Step 3 quarter-by-quarter

Schedule AI replaces the "required annual payment ÷ 4" with quarter-specific amounts based on actual cumulative income through each quarter-end. This benefits filers with back-loaded income (Q4 sale, year-end bonus).

The Schedule AI columns:
- Column (a): 1/1 through 3/31 → annualization factor 4
- Column (b): 1/1 through 5/31 → annualization factor 2.4
- Column (c): 1/1 through 8/31 → annualization factor 1.5
- Column (d): 1/1 through 12/31 → annualization factor 1

For each column, compute:
1. Cumulative AGI through the column-end date
2. Annualize: AGI × annualization factor
3. Compute tax on the annualized AGI (using current-year brackets)
4. De-annualize: tax × (1 ÷ annualization factor)
5. Apply the 22.5% / 45% / 67.5% / 90% multipliers per column to get the cumulative installment requirement

If Schedule AI's installment requirement is *lower* than the regular method's installment for a given quarter, the filer benefits. The agent uses Schedule AI for quarters where it reduces the underpayment, and the regular method for quarters where Schedule AI is higher (the filer always uses whichever method is lower per quarter — there is no "all-or-nothing" requirement).

See `references/annualized-income-method.md` for the full Schedule AI worksheet structure.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next steps:

- **If no penalty (safe harbor met)**: no Form 2210 to file; one-line confirmation in the return file
- **If penalty + filer chose IRS-computes**: Form 1040 Line 38 left blank or filled per current-year guidance; IRS bills after processing
- **If penalty + Form 2210 filed**: Form 2210 attached to Form 1040, penalty amount enters Form 1040 Line 38
- **For next year**: based on this year's experience, recommend updated Form W-4 (extra withholding), updated quarterly estimates via Form 1040-ES, or both. The goal is to land within the safe harbor next year.

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains the FFFF / paid software / paper decision tree and field-by-field mapping for Form 2210 specifically. If the user only wants a draft and will file themselves, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Required Annual Payment

Determines whether a penalty is even possible by checking the safe harbors.

| Line | What goes here |
|------|----------------|
| 1 | Current-year total tax (Form 1040 Line 22 minus refundable credits — verify per current-year worksheet) |
| 2 | Other taxes (per worksheet) |
| 3 | Refundable credits |
| 4 | Line 1 + Line 2 − Line 3 (current-year tax for safe-harbor purposes) |
| 5 | Line 4 × 90% |
| 6 | Withholding |
| 7 | Line 5 − Line 6 (positive only; if ≤ $1,000 then de minimis) |
| 8 | Maximum required annual payment (smaller of 90% current or 100%/110% prior) |
| 9 | The required annual payment |

(Line numbers are approximate — verify against current-year Form 2210; lines have been renumbered between revisions.)

### Part II — Reasons for Filing (Waivers)

Three waiver checkboxes:

- **Box A**: Request waiver due to retirement (after age 62) or becoming disabled in the prior or current year
- **Box B**: Request waiver due to casualty, disaster, or other unusual circumstances
- **Box C**: (Various per current year — verify)

Waiver requests require a written explanation attached.

### Part III — Short Method (Regular Method, Quarterly Underpayments)

For filers using the regular method:

```
Each quarter:
  Required cumulative installment = (cumulative %) × Line 9 required annual payment
  Cumulative paid = allocated withholding + estimated tax paid by due date
  Underpayment = required − paid (positive only)
  Penalty = underpayment × days late × penalty rate
```

### Schedule AI — Annualized Income Installment Method

Quarter-by-quarter recomputation of required installments based on actual cumulative income. Opt-in. See `references/annualized-income-method.md` for full worksheet structure.

---

## Validation

Run every check. Surface failures — don't silently fix.

### Math checks

- [ ] Line 1 (current-year total tax) matches Form 1040 Line 22 minus refundable credits (per current-year worksheet)
- [ ] Line 5 = Line 4 × 0.90
- [ ] Line 6 (withholding) sums to W-2 Box 2 + 1099 Box 4 + Form 8959 Line 24
- [ ] Line 9 (required annual payment) = smaller of Line 5 or Line 8
- [ ] Each quarterly underpayment = max(cumulative required − cumulative paid, 0)
- [ ] Each quarterly penalty = underpayment × (days late / 365) × penalty rate
- [ ] Total penalty = sum of quarterly penalties
- [ ] Schedule AI cumulative percentages: 22.5% (Q1), 45% (Q2), 67.5% (Q3), 90% (Q4)
- [ ] Schedule AI annualization factors: 4 (Q1), 2.4 (Q2), 1.5 (Q3), 1 (Q4)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filer used Schedule AI but income was actually fairly even across the year — Schedule AI may not save money; show the regular method too
- [ ] Filer did NOT use Schedule AI but income was clearly uneven (one quarter > 50% of total) — flag that Schedule AI may save money; offer to compute it
- [ ] Filer's withholding alone covers the prior-year safe harbor → no penalty; the agent should confirm before computing the Schedule AI math
- [ ] Filer's prior-year tax was zero AND prior year was a full 12-month return → first-year exception applies; no penalty; no Form 2210
- [ ] Filer paid all quarterly estimates exactly on the due date but used a payment method (paper check) that took 3+ days to clear → confirm the IRS-recorded payment date matches the filer's "paid by" date
- [ ] Penalty < $50 → consider just letting IRS compute and bill; the analytical effort exceeds the dollar value
- [ ] Filer is using prior-year safe harbor (Line 8) but prior-year AGI was > $150K and applied 100% threshold → should be 110%; recompute
- [ ] Filer made a Q4 estimated tax payment on January 15+ to "back-fill" a Q1/Q2/Q3 underpayment — this DOES NOT undo the prior-quarter penalty; it only stops further accrual on the underpaid amount

### Cross-form checks

- [ ] If Form 2210 is filed, Form 1040 Line 38 should reflect the penalty (or "see Form 2210" if claiming a waiver)
- [ ] If filer let IRS compute (no Form 2210 attached), Form 1040 Line 38 is left blank per current-year guidance
- [ ] If filer claims a waiver via Box A/B/C, the written explanation is attached
- [ ] If next-year planning suggests increased withholding, Form W-4 update should be filed with the employer
- [ ] If next-year planning suggests increased estimated tax, Form 1040-ES voucher schedule should be drafted

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 2210 or paste into tax software. Format:

```markdown
# Form 2210 — DRAFT for tax year YYYY

## Filing decision
- [ ] No Form 2210 needed (safe harbor met or de minimis exception)
- [ ] No Form 2210 — let IRS compute penalty and bill
- [ ] File Form 2210 with regular method
- [ ] File Form 2210 with Schedule AI (annualized income installment method)

## Header
Name(s) shown on return:    <filer name(s)>
Your SSN:                   <SSN>
Filing status:              <Single | HoH | QSS | MFJ | MFS>
Prior-year AGI:             $XXX,XXX  → safe-harbor multiplier: 100% | 110%

## Part I — Required Annual Payment
1. Current-year total tax:                          $XX,XXX
2. (Other taxes per worksheet):                     $XXX
3. (Refundable credits):                            $XXX
4. Subtotal:                                        $XX,XXX
5. Line 4 × 90%:                                    $XX,XXX
6. Current-year withholding:                        $XX,XXX
7. Line 5 − Line 6 (≤ $1,000 → de minimis):        $XX,XXX
8. Prior-year tax × (100% or 110%):                 $XX,XXX
9. Required annual payment (smaller of 5 or 8):     $XX,XXX

## Part II — Waivers (if any)
- [ ] Box A: Retirement (age 62+) or disability waiver
- [ ] Box B: Casualty / disaster / unusual circumstances
- [ ] Box C: (per current-year form)
- [ ] No waiver claimed
Written explanation: <attached | N/A>

## Part III — Quarterly Underpayment Computation (Regular Method)

| Quarter | Due date | Cumulative req'd installment | Withholding allocated | Estimates paid by due date | Cumulative paid | Underpayment |
|---------|----------|------------------------------|----------------------|----------------------------|----------------|--------------|
| Q1      | 4/15     | (25% of Line 9)              | (W ÷ 4)              | $X                         | $X             | $X           |
| Q2      | 6/15     | (50%)                        | (W × 2/4)            | $X                         | $X             | $X           |
| Q3      | 9/15     | (75%)                        | (W × 3/4)            | $X                         | $X             | $X           |
| Q4      | 1/15     | (100%)                       | (W)                  | $X                         | $X             | $X           |

## Penalty computation per quarter

| Quarter | Underpayment | Days late (to next-year 4/15) | Rate | Penalty |
|---------|--------------|-------------------------------|------|---------|
| Q1      | $X           | XXX days                      | X.X% | $XX     |
| Q2      | $X           | XXX days                      | X.X% | $XX     |
| Q3      | $X           | XXX days                      | X.X% | $XX     |
| Q4      | $X           | XXX days                      | X.X% | $XX     |
| **Total penalty** |     |                               |      | **$XXX** |

## Schedule AI — Annualized Income Installment Method (if used)
(See references/annualized-income-method.md for full worksheet)
Q1 cumulative AGI:            $XX,XXX  →  Q1 required: $X,XXX  (vs. regular: $X,XXX)
Q2 cumulative AGI:            $XX,XXX  →  Q2 required: $X,XXX  (vs. regular: $X,XXX)
Q3 cumulative AGI:            $XX,XXX  →  Q3 required: $X,XXX  (vs. regular: $X,XXX)
Q4 cumulative AGI:            $XX,XXX  →  Q4 required: $X,XXX  (vs. regular: $X,XXX)

Schedule AI total penalty:                                   $XXX
Regular method total penalty:                                $XXX
Method chosen (lower):                                       <Schedule AI | regular>

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Filing decision: <see top — Form 2210 needed and chosen method>
- Penalty: $XXX (or $0 if safe harbor met)
- Next steps:
  - <handoff items from Step 10>
  - <updated Form W-4 / Form 1040-ES recommendation for next year>

## Sources cited in this draft
- IRS Form 2210 (revision date YYYY-MM-DD)
- IRS Instructions for Form 2210 (revision date YYYY-MM-DD)
- IRC §6654 (estimated tax penalty for individuals)
- IRC §6654(d)(1)(A) ($1,000 de minimis)
- IRC §6654(d)(1)(B) (first-year exception)
- IRC §6654(g)(1) (withholding allocated evenly across quarters by default)
- IRS Revenue Ruling YYYY-XX (penalty rate for Q[N] of year YYYY)
- (any other authority used)
```

Show every line, including zeros. The deliverable is a starting point — the user still has to enter it into Form 1040 e-file software or paper Form 2210.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 2210 line with examples and edge cases
- [`references/safe-harbors.md`](./references/safe-harbors.md) — The 90% / 100% / 110% rules under IRC §6654(d), with worked safe-harbor examples
- [`references/annualized-income-method.md`](./references/annualized-income-method.md) — Schedule AI worksheet, annualization factors, when it saves penalty
- [`references/penalty-rates.md`](./references/penalty-rates.md) — How the penalty rate is set (federal short-term rate + 3%), historical rates, where to look up current-quarter rate
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 2210 alongside Form 1040 via FFFF, paper, or generic tax software

## Examples

End-to-end worked Form 2210 drafts. Use these as patterns when the user's situation is similar.

- [`examples/w2-plus-side-gig.md`](./examples/w2-plus-side-gig.md) — W-2 employee with under-withheld side-gig income; analyzes 90% / 100% safe harbor; minimal penalty
- [`examples/freelancer-uneven-income.md`](./examples/freelancer-uneven-income.md) — Freelancer with $0 Q1, $80K Q4; Schedule AI saves significant penalty vs. regular method
- [`examples/retiree-roth-conversion.md`](./examples/retiree-roth-conversion.md) — Retiree with steady SS + IRA distribution + large Q4 Roth conversion; uses prior-year safe harbor to avoid penalty entirely

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — the form itself
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — line-by-line IRS guidance, current-year penalty rate table
- [About Form 2210](https://www.irs.gov/forms-pubs/about-form-2210) — IRS landing page with archive of past revisions
- [Form 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) — Estimated Tax for Individuals (the quarterly voucher; companion to Form 2210)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (chapter on underpayment penalty and Schedule AI)
- [Form 843](https://www.irs.gov/pub/irs-pdf/f843.pdf) — Claim for Refund and Request for Abatement (used for after-the-fact penalty waiver requests on already-paid penalties)
- IRC §6654 — Failure by individual to pay estimated income tax
- IRC §6654(d)(1)(A) — $1,000 de minimis exception
- IRC §6654(d)(1)(B) — First-year exception
- IRC §6654(d)(1)(C) — Higher-AGI 110% safe harbor for filers with prior-year AGI > $150K
- IRC §6654(g)(1) — Withholding allocated equally across quarters absent election
- IRC §6621 — Determination of penalty interest rate (federal short-term rate + 3%)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and IRC sections. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations — multi-state residency, retroactive payments, partial waiver claims, fiscal-year filers — warrant a licensed tax professional's review.
