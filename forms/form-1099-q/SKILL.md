---
name: form-1099-q
description: >
  Use this skill when an individual receives Form 1099-Q after a withdrawal from
  a 529 qualified tuition program or a Coverdell Education Savings Account
  (ESA) and needs to determine whether the distribution is tax-free, partially
  taxable, or subject to the 10% additional tax. Triggers on phrases like
  "received 1099-Q", "529 plan distribution", "Coverdell ESA withdrawal",
  "529 to Roth IRA rollover", "non-qualified 529 withdrawal tax", "is my 529
  distribution taxable", "earnings portion of 1099-Q". Do NOT use for Form
  1099-R (retirement plan distributions), for contributions TO a 529 (no
  federal form is filed for contributions — state tax forms may apply), or for
  ABLE account distributions (Form 1099-QA, separate filing).
form: Form 1099-Q (Payments From Qualified Education Programs)
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1099q.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099q.pdf
---

# Form 1099-Q — Payments From Qualified Education Programs (529, Coverdell)

This skill processes a Form 1099-Q that the user has received from a 529 plan trustee or Coverdell ESA custodian. It determines whether the distribution is fully tax-free, partially taxable, or fully taxable; computes any earnings portion that flows to Schedule 1; identifies whether the 10% additional tax under IRC §529(c)(6) applies; and produces an audit-grade worksheet the user can attach to their records.

The arithmetic is simple. The judgment is in (1) what counts as a Qualified Higher Education Expense (QHEE), (2) how AOTC / Lifetime Learning Credit coordination forces certain expenses out of the QHEE pool, and (3) when the SECURE 2.0 §126 529-to-Roth rollover qualifies for tax-free treatment. The agent must ASK before guessing on any of these.

The box map in this skill was verified against Form 1099-Q (Rev. April 2025) and the Instructions for Form 1099-Q (Rev. April 2025), a continuous-use revision used for tax year 2025 and later until superseded. Return-side line references were verified against the 2025 Form 5329, Schedule 1, and Schedule 2 (filed in 2026). Before use, re-check https://www.irs.gov/forms-pubs/about-form-1099-q for a newer revision and redo the box map if one exists.

---

## When to invoke

Engage this skill when **any** of these is true:

- The user explicitly mentions Form 1099-Q, "1099-Q", or a 529/Coverdell distribution
- The user describes withdrawing money from a 529 plan or Coverdell ESA — for tuition, room and board, K-12 expenses, apprenticeship, student-loan repayment, or a Roth IRA rollover
- The user asks "is my 529 distribution taxable?" or "do I owe a penalty on my 529 withdrawal?"
- The user got a 1099-Q showing a distribution they didn't ask for (e.g., trustee error, forced rollover) and wants to know the tax consequences

Do **not** engage this skill when:

- The user got a Form 1099-R (retirement plan distribution) — different form, different rules
- The user is asking how to *contribute* to a 529 — there's no federal form for contributions; state tax deduction may apply, but that's outside scope
- The user got a Form 1099-QA (ABLE account) — different form for disability savings accounts (IRC §529A)
- The user wants to know whether to *open* a 529 or pick a state plan — that's planning, not filing
- The user's question is about the AOTC or Lifetime Learning Credit alone (Form 8863). That is out of scope for this skill; there is no Form 8863 skill in this repo

If the user has both a 1099-Q and education-credit (AOTC/LLC) eligibility, run this skill **first** to determine whether the 529 distribution covered all qualifying expenses; whatever expenses remain after the 529 allocation can be applied to the credit. Coordination is mandatory under IRC §529(c)(3)(B)(v) and Pub. 970 ch. 7 — same dollar of expense cannot be used for both a tax-free 529 distribution and a credit.

---

## Prerequisites

Before producing anything, the agent must collect the following. If any are missing, **ASK** with a tight question and stop.

1. **Tax year** the 1099-Q reports. Box on the form is labeled with the year. The skill defaults to the calendar year of distribution.

2. **Recipient identity**. Who is named in the "Recipient" box of the 1099-Q?
   - If the account owner (e.g., parent), the recipient is the account owner.
   - If the beneficiary (the student), the distribution went directly to them or to their school on their behalf.
   - **Tax consequence depends on this**: any taxable earnings are reported on the recipient's return, not someone else's.

3. **All three amount boxes** from the 1099-Q:
   - **Box 1** — Gross distribution
   - **Box 2** — Earnings portion
   - **Box 3** — Basis (return of contributions)
   - Verify: Box 1 = Box 2 + Box 3. If not, the form is wrong; ask the user to check.
   - Exception: for a Coverdell ESA distribution the trustee may leave boxes 2 and 3 blank and report the account's year-end fair market value in box 7 labeled "FMV". Then figure earnings and basis with the Coverdell ESA Taxable Distributions and Basis worksheet in Pub. 970 ch. 6 (1099-Q instructions, Box 1 caution). Ask for the year-end FMV and the user's total contributions.

4. **Boxes 4a and 4b** — Type of transfer. 4a = trustee-to-trustee transfer (QTP to QTP, QTP to ABLE account, Coverdell to Coverdell, Coverdell to QTP). 4b = direct transfer from a QTP to a Roth IRA for the beneficiary. A qualifying transfer is generally non-taxable. Confirm with the user.

5. **Boxes 5a to 5c** — Distribution is from:
   - 5a "Private QTP" — established by one or more private eligible educational institutions
   - 5b "State QTP" — most common
   - 5c "Coverdell ESA" — IRC §530, lower contribution limit, broader use cases

6. **Box 6** — "Check if the recipient is not the designated beneficiary." If checked, the recipient is someone other than the beneficiary (the account owner). If blank, the recipient *is* the designated beneficiary.

7. **Box 7** (Copy B) — Either the Coverdell year-end FMV (see item 3) or an optional distribution code: 1 distributions (including transfers), 2 and 3 excess Coverdell contributions plus earnings, 4 disability, 5 death, 6 prohibited transaction. Code 4 or 5 points to an exception in Step 6.

8. **Total Qualified Higher Education Expenses (QHEE)** for the beneficiary in the same tax year. The user must provide:
   - Tuition and required fees (paid to an eligible educational institution)
   - Required books, supplies, equipment
   - Room and board (only if beneficiary is enrolled at least half-time; capped at the school's cost-of-attendance allowance for room and board or, if greater, the actual amount charged for school-owned housing, IRC §529(e)(3)(B)(ii))
   - Computer/peripherals/software/internet primarily used by beneficiary while enrolled (IRC §529(e)(3)(A)(iii), since 2015)
   - For 529 only (not Coverdell): K-12 expenses, capped per beneficiary per year at $10,000 for 2025 and $20,000 for taxable years beginning after Dec. 31, 2025 (IRC §529(e)(3)(A); P.L. 119-21 §70413(b)). Tuition only for distributions through July 4, 2025; for distributions after July 4, 2025, also curricular materials, books, online materials, qualifying outside tutoring, standardized and admission test fees, dual enrollment fees, and educational therapies (IRC §529(c)(7)(A)-(H); P.L. 119-21 §70413(a)). Ask for the distribution date.
   - For 529 only: Registered apprenticeship program fees, books, supplies, equipment (IRC §529(c)(8), since SECURE Act 2019)
   - For 529 only: Qualified student loan repayment up to $10,000 lifetime per beneficiary, plus $10,000 lifetime per sibling (IRC §529(c)(9), since SECURE Act 2019)
   - For 529 only: Qualified postsecondary credentialing expenses for distributions after July 4, 2025: tuition, fees, books, supplies, and equipment for a recognized postsecondary credential program, plus required testing and continuing education fees (IRC §529(e)(3)(C), (f); P.L. 119-21 §70414)

   See [`references/qualified-expenses.md`](./references/qualified-expenses.md) for the full eligible list and ineligible items (transportation, health insurance, optional fees).

9. **Scholarships, employer education assistance, AOTC/LLC expenses used.** Any of these reduce QHEE — see the AQEE adjustment in [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md). The skill must ask: "Did the beneficiary receive any tax-free scholarship, employer-paid tuition, or did anyone claim AOTC or Lifetime Learning Credit using the same expenses?"

10. **Was this a SECURE 2.0 529-to-Roth rollover?** If yes, the rollover triggers an entirely different ruleset under IRC §529(c)(3)(E). See Step 7 of the workflow and [`references/secure-2-roth-rollover.md`](./references/secure-2-roth-rollover.md).

For non-qualified distributions, additionally ask:
- Did the beneficiary receive a tax-free scholarship, veterans' educational assistance, or employer-provided educational assistance in the same year? (exception to the 10% additional tax, IRC §530(d)(4)(B)(iii) applied by §529(c)(6))
- Did the beneficiary die, become disabled, or attend a U.S. military academy? (each is an exception)
- Was the distribution included in income because of AOTC/LLC coordination? (also exception)

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm form type and identify the recipient

Read Boxes 5a-5c (program type) and Box 6 (checked = recipient is not the designated beneficiary). Confirm with the user:

- "The 1099-Q says the recipient is [name]. Is that you, or someone else in the family?"

If recipient = account owner (parent), the parent reports any taxable portion on the parent's return. If recipient = beneficiary (student), the student reports it. This drives whose 1040 the skill produces output for. For a QTP, the plan lists the beneficiary as recipient only when it paid the beneficiary, paid an eligible educational institution for the beneficiary, or transferred directly to the beneficiary's Roth IRA; otherwise it lists the account owner. For a Coverdell ESA the recipient is always the designated beneficiary (1099-Q instructions, Recipient's Name and TIN).

### Step 2 — Check Boxes 4a and 4b (type of transfer)

If Box 4b is checked, go to Step 7 (529-to-Roth IRA). If Box 4a is checked, the distribution moved directly from one 529 plan to another, from a 529 plan to an ABLE account, or between Coverdell accounts. A cash distribution the user redeposited into another QTP or an ABLE account within 60 days is also a rollover (IRC §529(c)(3)(C)(i)). Result: non-taxable, no further action needed beyond keeping the 1099-Q for records. The agent should still confirm:

- A cash rollover was redeposited within 60 days
- For a rollover to another QTP for the same beneficiary: no other such transfer within the prior 12 months (IRC §529(c)(3)(C)(iii))
- For a QTP-to-ABLE rollover: the amount plus other ABLE contributions for the year stays within the ABLE annual limit (IRC §529(c)(3)(C)(i), flush language)

If the conditions are satisfied, document and stop. If not, the amount is not a qualifying rollover: treat it as a distribution and continue with Steps 3 to 6 (Pub. 970 ch. 7, Rollovers and Other Transfers).

### Step 3 — Collect Qualified Higher Education Expenses (QHEE)

Build the QHEE table:

```
| Expense category                    | Amount  | Notes                          |
|-------------------------------------|---------|--------------------------------|
| Tuition and required fees           | $X,XXX  | From Form 1098-T Box 1         |
| Required books, supplies, equipment | $X,XXX  |                                |
| Room and board (if half-time+)      | $X,XXX  | COA allowance or on-campus charge, if greater |
| Computer, software, internet        | $X,XXX  | Primary use by beneficiary     |
| K-12 expenses (529; $10K 2025, $20K 2026+) | $X,XXX  | Pre-college only        |
| Apprenticeship costs (529 only)     | $X,XXX  | Registered programs only       |
| Student loan repayment (529 only)   | $X,XXX  | $10K lifetime per beneficiary  |
| Credentialing (529; after 7/4/2025) | $X,XXX  | Recognized credential program  |
| **Total QHEE**                      | $X,XXX  |                                |
```

Coverdell ESA: K-12 expenses for elementary and secondary school are also qualified, including tuition, fees, academic tutoring, books, supplies, special needs services, room and board, uniforms, and transportation required or provided by the school, and computer technology used by the beneficiary and the family (IRC §530(b)(3)(A)).

### Step 4 — Apply the AQEE adjustment

**Adjusted Qualified Education Expenses (AQEE)** = Total QHEE − (tax-free scholarships and Pell grants + veterans' educational assistance + employer-provided educational assistance + other tax-free educational assistance + AOTC expenses + LLC expenses).

Same dollar of expense cannot fund (a) tax-free 529 distribution, (b) AOTC, (c) LLC, or (d) be paid by tax-free scholarship simultaneously. Pub. 970 ch. 7 (Figuring the Taxable Portion of a Distribution) walks through the allocation. See [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md).

If AQEE ≥ Box 1 of 1099-Q, the entire distribution is tax-free. Skip to Step 8.

If AQEE < Box 1, a portion of the distribution is non-qualified — proceed to Step 5.

### Step 5 — Compute the taxable earnings portion

Formula (Pub. 970 ch. 7):

```
Taxable amount = Box 2 × (1 − AQEE / Box 1)
```

Equivalently:

```
Non-qualified portion of Box 1 = Box 1 − AQEE
Taxable earnings = Non-qualified portion × (Box 2 / Box 1)
```

The taxable earnings portion is reported on **Schedule 1, Line 8z** (Other income) with the description "Taxable 529 distribution" (or "Taxable Coverdell distribution"). It flows to Form 1040 Line 8.

### Step 6 — Determine if the 10% additional tax applies

The taxable earnings portion is generally subject to a **10% additional tax** under IRC §529(c)(6) (and §530(d)(4) for Coverdell). It's reported on **Schedule 2, Line 8** via Form 5329 Part II, lines 5 to 8, which covers both QTP and Coverdell distributions (2025 Form 5329). Form 5329 must be filed for any taxable QTP or Coverdell distribution, even when an exception brings the additional tax to $0 (2025 Instructions for Form 5329, Who Must File).

Exceptions (no additional tax) under IRC §530(d)(4)(B), applied to QTPs by §529(c)(6); Pub. 970 ch. 7:

- Beneficiary died — distribution to estate or another beneficiary
- Beneficiary became disabled — IRC §72(m)(7) definition
- Beneficiary received a tax-free scholarship, veterans' educational assistance, employer-provided educational assistance, or other tax-free educational assistance — additional tax waived to the extent the distribution does not exceed that amount
- Beneficiary attended a U.S. service academy — waived up to costs of attendance
- Distribution was included in income only because of AOTC/LLC coordination — additional tax waived up to AOTC/LLC expenses
- Distribution was rolled over to another 529 / Coverdell within 60 days (covered by Step 2, not this step)
- SECURE 2.0 529-to-Roth rollover that qualifies — see Step 7

If an exception applies, document which exception and the dollar amount excluded. Form 5329 Part II has no exception codes: enter the exempt amount on line 6.

### Step 7 — SECURE 2.0 529-to-Roth IRA rollover (special path)

If the user indicated this distribution was a 529-to-Roth rollover under IRC §529(c)(3)(E) (added by SECURE 2.0 §126, effective for distributions after 2023), check **all** of the following:

1. The 529 account has been open for **15 years or more** (account age, not contribution age)
2. The Roth IRA recipient is **the beneficiary** of the 529 account (not the account owner unless they are also the beneficiary)
3. The amount transferred this year does not exceed the **annual Roth IRA contribution limit** for the beneficiary, reduced by any other IRA contributions they made for the year, and does not exceed the beneficiary's compensation for the year (IRC §408A(c)(2), §219(b)(1)). Limit: $7,000 for 2025 ($8,000 age 50+; 2025 Instructions for Form 5329); $7,500 for 2026 ($8,600 age 50+; Notice 2025-67). The Roth MAGI phase-out does not reduce this room (IRC §408A(c)(3)(E))
4. The amount does not exceed the contributions made more than **5 years** before the distribution date, plus earnings on them (IRC §529(c)(3)(E)(i)(I))
5. **Lifetime cap of $35,000** per beneficiary across all years
6. The transfer is a **direct trustee-to-trustee transfer** to the beneficiary's Roth IRA (IRC §529(c)(3)(E)(i)(II); Box 4b should be checked)

If all conditions are met, the rollover is **non-taxable and not subject to the 10% additional tax**. Document the conditions checked.

If any condition fails, the rollover is treated as a regular non-qualified distribution — Steps 5 and 6 apply normally. The most common failure mode is the 15-year account age requirement.

See [`references/secure-2-roth-rollover.md`](./references/secure-2-roth-rollover.md) for IRS guidance and known open issues (Treasury has not issued final regs as of last verification — confirm before relying on edge cases).

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next forms the user will need on their return:

- **Taxable earnings portion > $0** → Schedule 1 Line 8z, then Form 1040 Line 8
- **Taxable earnings > $0** → Form 5329 Part II (required even if the additional tax is $0); if line 8 > $0, Schedule 2 Line 8. See [`../form-5329/SKILL.md`](../form-5329/SKILL.md)
- **AOTC/LLC also being claimed** → Form 8863, using only expenses not already counted in AQEE
- **Estimated tax** if the user owes additional tax this year

### Step 11 — File the return (optional, if the user wants the agent to file)

If the agent is also filing Form 1040 for the user, follow [`filing.md`](./filing.md) for how to enter the 1099-Q data into IRS Free File Fillable Forms or generic tax software. If the user only wants the worksheet, skip this step.

---

## Line-by-line guidance

For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### The 1099-Q form (received, not filed)

The user does not *file* Form 1099-Q. The trustee files copy A with the IRS; the user gets copy B for records. The user files the **derived numbers** on their 1040.

| Box | Label | Use |
|-----|-------|-----|
| 1 | Gross distribution | Total dollar amount distributed in the tax year (including in-kind) |
| 2 | Earnings | Earnings portion of Box 1 (trustee's earnings ratio under Prop. Reg. §1.529-3, Notice 2001-81, Notice 2016-13) |
| 3 | Basis | Box 1 − Box 2 (return of contributions, never taxable) |
| 4a | Type of transfer: Trustee-to-trustee | Checkbox; QTP to QTP or ABLE, Coverdell to Coverdell or QTP |
| 4b | Type of transfer: QTP to Roth IRA | Checkbox; 529-to-Roth rollover, see Step 7 |
| 5a-5c | Distribution is from | Private QTP, State QTP, or Coverdell ESA |
| 6 | Check if the recipient is not the designated beneficiary | Checked = recipient is the account owner |
| 7 | FMV or distribution code (Copy B) | Coverdell year-end FMV, or optional code 1-6 |

### Where the numbers go on the 1040

| Origin | Destination |
|--------|-------------|
| Taxable earnings portion (computed in Step 5) | Schedule 1 Line 8z → 1040 Line 8 |
| 10% additional tax (computed in Step 6) | Form 5329 Part II → Schedule 2 Line 8 → 1040 Line 23 |
| Tax-free distribution | Not reported on 1040; keep records |
| 529-to-Roth rollover (qualified) | Not reported on 1040; keep records of the 5 conditions |

The basis portion (Box 3) is never taxable. It's a return of the user's after-tax contribution.

---

## Validation

Run every check before declaring the worksheet ready.

### Math checks

- [ ] Box 1 = Box 2 + Box 3 (1099-Q instructions, Box 3: "must equal box 1 minus box 2"; a Coverdell form with boxes 2 and 3 blank and FMV in box 7 is the one allowed exception)
- [ ] AQEE ≤ Total QHEE
- [ ] Taxable earnings ≤ Box 2
- [ ] If Box 4a or 4b is checked and the transfer qualifies, taxable earnings = $0
- [ ] If Box 1 = Box 3 (i.e., Box 2 = $0), no taxable amount possible regardless of QHEE
- [ ] 10% additional tax = (Form 5329 line 5 − line 6) × 10%

### Sanity checks

Surface as warnings, do not block:

- [ ] Box 1 > $50,000 in a single year — confirm; large distributions sometimes indicate paying multiple semesters
- [ ] AQEE is exactly equal to Box 1 — confirm the user isn't double-counting expenses already used for AOTC/LLC
- [ ] User claims SECURE 2.0 rollover but account is < 15 years old — does not qualify under IRC §529(c)(3)(E)
- [ ] User claims SECURE 2.0 rollover for $35,000+ in one year — exceeds annual Roth contribution limit; only the lower of the two caps applies
- [ ] Box 6 checked but the user says the recipient is the beneficiary (or blank but the recipient is the owner) — form may be wrong; ask trustee for corrected 1099-Q
- [ ] User had a tax-free scholarship but did not adjust QHEE downward — likely error; confirm
- [ ] User has K-12 expenses on a Coverdell — qualified; on a 529 — capped per beneficiary at $10,000 for 2025 and $20,000 for 2026 and later
- [ ] Student loan repayment is being claimed but beneficiary already used the $10,000 lifetime cap — confirm
- [ ] Computer/internet expenses are claimed but the user describes mostly personal use — beneficiary primary-use test fails

### Cross-form checks

- [ ] If AOTC or LLC is also being claimed (Form 8863), AQEE was reduced by the credit-claimed expenses
- [ ] If beneficiary is not the recipient on 1099-Q, taxable earnings go on the *recipient's* return, which may be a different return entirely (kiddie tax considerations may apply if recipient is the student under 24)
- [ ] If there are taxable earnings, Form 5329 Part II is included (even when the additional tax is $0) and any exception amount is on line 6 (Part II has no exception codes)

---

## Output format

The deliverable is a worksheet the user retains and a set of line entries for Schedule 1 / Schedule 2 / Form 5329. Format:

```markdown
# Form 1099-Q — DRAFT WORKSHEET for tax year YYYY

## 1099-Q received
- Recipient: <name> (<owner|beneficiary>)
- Trustee/custodian: <name>
- Box 1 (Gross distribution): $X,XXX
- Box 2 (Earnings): $X,XXX
- Box 3 (Basis): $X,XXX
- Box 4a (Trustee-to-trustee): [Checked | Blank]
- Box 4b (QTP to Roth IRA): [Checked | Blank]
- Box 5 (Distribution is from): [5a Private QTP | 5b State QTP | 5c Coverdell ESA]
- Box 6 (Recipient is not the designated beneficiary): [Checked | Blank]
- Box 7 (FMV or distribution code): <value or blank>

## Qualified Education Expenses
| Category                            | Amount  |
|-------------------------------------|---------|
| Tuition and required fees           | $X,XXX  |
| Required books and supplies         | $X,XXX  |
| Room and board (half-time+)         | $X,XXX  |
| Computer, software, internet        | $X,XXX  |
| K-12 expenses (529, ≤$10,000 2025 / ≤$20,000 2026+) | $X,XXX  |
| Apprenticeship (529)                | $X,XXX  |
| Student loan repayment (529, ≤$10K) | $X,XXX  |
| Postsecondary credentialing (529)   | $X,XXX  |
| **Total QHEE**                      | $X,XXX  |

## AQEE Adjustment
- Tax-free scholarships:               −$X,XXX
- Employer education assistance:       −$X,XXX
- Expenses used for AOTC:              −$X,XXX
- Expenses used for LLC:               −$X,XXX
- **Adjusted QHEE (AQEE)**:            = $X,XXX

## Taxable amount calculation
- Box 1:                          $X,XXX
- AQEE:                           $X,XXX
- Non-qualified portion:          $X,XXX  (Box 1 − AQEE)
- Earnings ratio (Box 2 / Box 1): X.XXX
- **Taxable earnings**:           $X,XXX  (Non-qualified × Earnings ratio)

## 10% additional tax
- Subject to 10% additional tax: [Yes | No]
- Exception applied (if any):    <code + description>
- **Additional tax owed**:       $X,XXX

## SECURE 2.0 529-to-Roth rollover (if applicable)
- 15-year account age:           [Yes | No]
- Beneficiary = Roth recipient:  [Yes | No]
- Within annual Roth limit:      [Yes | No]
- 5-year contribution age:       [Yes | No]
- Lifetime cap not exceeded:     [Yes | No] ($X,XXX of $35,000 used)
- Direct trustee-to-trustee (Box 4b): [Yes | No]
- **Qualifies for tax-free**:    [Yes | No]

## Where this goes on the return
- Schedule 1 Line 8z: $X,XXX (description: "Taxable 529/Coverdell distribution")
- Form 5329 Part II lines 5 to 8, then Schedule 2 Line 8: $X,XXX (10% additional tax)
- 1040 Line 8: includes Schedule 1 Line 8z
- 1040 Line 23: includes Schedule 2 Line 8

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings raised>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 1099-Q (Rev. April 2025)
- IRS Instructions for Form 1099-Q (Rev. April 2025)
- IRC §529 (Qualified Tuition Programs)
- IRC §530 (Coverdell Education Savings Accounts)
- IRC §529(c)(3)(E) — SECURE 2.0 529-to-Roth rollover
- Pub. 970 (Tax Benefits for Education), chapter 7 (QTP) or chapter 6 (Coverdell)
- Form 5329 (Additional Taxes on Qualified Plans), Part II
```

The worksheet is the user's audit trail — IRS does not require it to be attached, but the user should keep it for at least 3 years (IRC §6501) along with the 1099-Q copy B and supporting expense receipts.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every box of Form 1099-Q with examples
- [`references/qualified-expenses.md`](./references/qualified-expenses.md) — Full eligible/ineligible list with citations
- [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md) — AQEE coordination with scholarships, AOTC, LLC
- [`references/secure-2-roth-rollover.md`](./references/secure-2-roth-rollover.md) — IRC §529(c)(3)(E) requirements
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-trip mistakes with citations
- [`filing.md`](./filing.md) — How an agent enters 1099-Q-derived numbers into Form 1040 via IRS Free File, Free File Fillable Forms, paid software, or paper

## Examples

End-to-end worked personas. Use these when the user's situation is similar.

- [`examples/parent-paying-tuition.md`](./examples/parent-paying-tuition.md) — Parent withdraws $30,000 from 529 for daughter's tuition; fully qualified, fully tax-free
- [`examples/non-qualified-withdrawal.md`](./examples/non-qualified-withdrawal.md) — Recipient takes $5,000 non-qualified distribution; computes taxable earnings + 10% additional tax + Schedule 1/2 entries
- [`examples/secure-2-roth-rollover.md`](./examples/secure-2-roth-rollover.md) — 16-year-old 529 account; $7,000 rolled to beneficiary's Roth IRA under SECURE 2.0 §126

## Sources

Authoritative sources used. Re-verify each year — IRS revises forms and figures annually.

- [Form 1099-Q (latest)](https://www.irs.gov/pub/irs-pdf/f1099q.pdf) — the form itself
- [Instructions for Form 1099-Q (Rev. April 2025)](https://www.irs.gov/pub/irs-pdf/i1099q.pdf) — box definitions, recipient rule, distribution codes
- [About Form 1099-Q](https://www.irs.gov/forms-pubs/about-form-1099-q) — IRS landing page
- [Publication 970 (2025)](https://www.irs.gov/publications/p970) — Tax Benefits for Education (chapter 6 for Coverdell, chapter 7 for QTP/529)
- [Form 5329](https://www.irs.gov/forms-pubs/about-form-5329) — Additional Taxes on Qualified Plans; Part II lines 5 to 8 (2025) for the 10% additional tax on QTP and Coverdell distributions
- [Form 8863](https://www.irs.gov/forms-pubs/about-form-8863) — Education Credits (AOTC, LLC) — coordination
- IRC §529 — Qualified Tuition Programs
- IRC §529(c)(3)(A)-(B) — distributions taxed under §72; exclusion for QHEE; §529(c)(3)(B)(v) AOTC/LLC coordination
- IRC §529(c)(3)(E) — 529-to-Roth IRA rollover (SECURE 2.0 §126, effective distributions after 12/31/2023)
- IRC §529(c)(6) — applies the §530(d)(4) 10% additional tax to QTPs; exceptions in §530(d)(4)(B)
- IRC §529(c)(7) — K-12 expenses (TCJA 2018; list expanded by P.L. 119-21 §70413(a) for distributions after July 4, 2025)
- IRC §529(e)(3)(A) — K-12 cap per beneficiary: $10,000; $20,000 for taxable years beginning after Dec. 31, 2025 (P.L. 119-21 §70413(b))
- IRC §529(e)(3)(C), (f) — qualified postsecondary credentialing expenses (P.L. 119-21 §70414, distributions after July 4, 2025)
- [IRC §529 with amendment notes (LII)](https://www.law.cornell.edu/uscode/text/26/529)
- [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) — 2026 IRA contribution limit $7,500 (catch-up $1,100)
- IRC §529(c)(8) — Apprenticeship expenses (SECURE Act 2019)
- IRC §529(c)(9) — Qualified student loan repayments (SECURE Act 2019, $10,000 lifetime per beneficiary)
- IRC §530 — Coverdell Education Savings Accounts
- SECURE 2.0 Act of 2022, §126 — 529-to-Roth rollover

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and statute. It is not tax advice. Coordination with AOTC/LLC and the SECURE 2.0 rollover rules contain edge cases (kiddie tax, multiple beneficiaries, mid-year transfers) where a licensed tax professional should review the result before filing.
