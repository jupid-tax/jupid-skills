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
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f1099q.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099qa.pdf
---

# Form 1099-Q — Payments From Qualified Education Programs (529, Coverdell)

This skill processes a Form 1099-Q that the user has received from a 529 plan trustee or Coverdell ESA custodian. It determines whether the distribution is fully tax-free, partially taxable, or fully taxable; computes any earnings portion that flows to Schedule 1; identifies whether the 10% additional tax under IRC §529(c)(6) applies; and produces an audit-grade worksheet the user can attach to their records.

The arithmetic is simple. The judgment is in (1) what counts as a Qualified Higher Education Expense (QHEE), (2) how AOTC / Lifetime Learning Credit coordination forces certain expenses out of the QHEE pool, and (3) when the SECURE 2.0 §126 529-to-Roth rollover qualifies for tax-free treatment. The agent must ASK before guessing on any of these.

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
- The user's question is about the AOTC or Lifetime Learning Credit alone — use Form 8863 skill (forthcoming)

If the user has both a 1099-Q and education-credit (AOTC/LLC) eligibility, run this skill **first** to determine whether the 529 distribution covered all qualifying expenses; whatever expenses remain after the 529 allocation can be applied to the credit. Coordination is mandatory under IRC §25A and Pub 970 — same dollar of expense cannot be used for both a tax-free 529 distribution and a credit.

---

## Prerequisites

Before producing anything, the agent must collect the following. If any are missing, **ASK** with a tight question and stop.

1. **Tax year** the 1099-Q reports. Box on the form is labeled with the year. The skill defaults to the calendar year of distribution.

2. **Recipient identity**. Who is named in the "Recipient" box of the 1099-Q?
   - If the account owner (e.g., parent), the recipient is the account owner.
   - If the beneficiary (the student), the distribution went directly to them or to their school on their behalf.
   - **Tax consequence depends on this**: any taxable earnings are reported on the recipient's return, not someone else's.

3. **All four amount boxes** from the 1099-Q:
   - **Box 1** — Gross distribution
   - **Box 2** — Earnings portion
   - **Box 3** — Basis (return of contributions)
   - Verify: Box 1 = Box 2 + Box 3. If not, the form is wrong; ask the user to check.

4. **Box 4** — Trustee-to-trustee transfer indicator. If checked, this distribution is generally non-taxable to the recipient (it went directly to another qualified program). Confirm with the user.

5. **Box 5** — Program type. Check one:
   - "Private 529" — sponsored by a private educational institution
   - "State 529" — most common
   - "Coverdell ESA" — IRC §530, lower contribution limit, broader use cases

6. **Box 6** — Designated beneficiary checkbox. If checked, the recipient *is* the designated beneficiary. If unchecked, recipient is someone other than the beneficiary (commonly the account owner).

7. **Total Qualified Higher Education Expenses (QHEE)** for the beneficiary in the same tax year. The user must provide:
   - Tuition and required fees (paid to an eligible educational institution)
   - Required books, supplies, equipment
   - Room and board (only if beneficiary is enrolled at least half-time; capped at the school's published cost of attendance for room and board, or the school's actual charge for on-campus housing — whichever applies)
   - Computer/peripherals/software/internet primarily used by beneficiary while enrolled (IRC §529(e)(3)(A)(iii), since 2015)
   - For 529 only (not Coverdell): K-12 tuition up to $10,000/year per beneficiary (IRC §529(c)(7), since TCJA 2018)
   - For 529 only: Registered apprenticeship program fees, books, supplies, equipment (IRC §529(c)(8), since SECURE Act 2019)
   - For 529 only: Qualified student loan repayment up to $10,000 lifetime per beneficiary, plus $10,000 lifetime per sibling (IRC §529(c)(9), since SECURE Act 2019)

   See [`references/qualified-expenses.md`](./references/qualified-expenses.md) for the full eligible list and ineligible items (transportation, health insurance, optional fees).

8. **Scholarships, employer education assistance, AOTC/LLC expenses used.** Any of these reduce QHEE — see the AAQEE adjustment in [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md). The skill must ask: "Did the beneficiary receive any tax-free scholarship, employer-paid tuition, or did anyone claim AOTC or Lifetime Learning Credit using the same expenses?"

9. **Was this a SECURE 2.0 529-to-Roth rollover?** If yes, the rollover triggers an entirely different ruleset under IRC §529(c)(3)(E). See Step 6 of the workflow and [`references/secure-2-roth-rollover.md`](./references/secure-2-roth-rollover.md).

For non-qualified distributions, additionally ask:
- Did the beneficiary receive a tax-free scholarship in the same year? (exception to the 10% additional tax for scholarship offset, IRC §529(c)(6)(B))
- Did the beneficiary die, become disabled, or attend a U.S. military academy? (each is an exception)
- Was the distribution included in income because of AOTC/LLC coordination? (also exception)

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm form type and identify the recipient

Read Box 5 (program type) and Box 6 (designated beneficiary). Confirm with the user:

- "The 1099-Q says the recipient is [name]. Is that you, or someone else in the family?"

If recipient = account owner (parent), the parent reports any taxable portion on the parent's return. If recipient = beneficiary (student), the student reports it. This drives whose 1040 the skill produces output for.

### Step 2 — Check Box 4 (trustee-to-trustee transfer)

If Box 4 is checked, the distribution was rolled directly from one 529 plan to another (or from one Coverdell to another) within 60 days. Result: non-taxable, no further action needed beyond keeping the 1099-Q for records. The agent should still confirm:

- The rollover happened within 60 days
- This is the first 529-to-529 rollover for the beneficiary in 12 months (only one rollover per beneficiary per 12 months, IRC §529(c)(3)(C)(iii))

If both conditions are satisfied, document and stop. If not, see [`references/rollovers.md`](./references/rollovers.md).

### Step 3 — Collect Qualified Higher Education Expenses (QHEE)

Build the QHEE table:

```
| Expense category                    | Amount  | Notes                          |
|-------------------------------------|---------|--------------------------------|
| Tuition and required fees           | $X,XXX  | From Form 1098-T Box 1         |
| Required books, supplies, equipment | $X,XXX  |                                |
| Room and board (if half-time+)      | $X,XXX  | Not to exceed cost of attendance|
| Computer, software, internet        | $X,XXX  | Primary use by beneficiary     |
| K-12 tuition (529 only, max $10K)   | $X,XXX  | Pre-college only               |
| Apprenticeship costs (529 only)     | $X,XXX  | Registered programs only       |
| Student loan repayment (529 only)   | $X,XXX  | $10K lifetime per beneficiary  |
| **Total QHEE**                      | $X,XXX  |                                |
```

Coverdell ESA: K-12 expenses for elementary and secondary school are also qualified, including tuition, fees, books, tutoring, special needs services, room and board if living away from home, uniforms, transportation, and computer technology (IRC §530(b)(3)).

### Step 4 — Apply the AAQEE adjustment

**Adjusted Qualified Education Expenses (AAQEE)** = Total QHEE − (tax-free scholarships + employer-paid tuition + AOTC expenses + LLC expenses).

Same dollar of expense cannot fund (a) tax-free 529 distribution, (b) AOTC, (c) LLC, or (d) be paid by tax-free scholarship simultaneously. Pub 970 chapter 8 walks through the allocation. See [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md).

If AAQEE ≥ Box 1 of 1099-Q, the entire distribution is tax-free. Skip to Step 7.

If AAQEE < Box 1, a portion of the distribution is non-qualified — proceed to Step 5.

### Step 5 — Compute the taxable earnings portion

Formula (Pub 970 chapter 8):

```
Taxable amount = Box 2 × (1 − AAQEE / Box 1)
```

Equivalently:

```
Non-qualified portion of Box 1 = Box 1 − AAQEE
Taxable earnings = Non-qualified portion × (Box 2 / Box 1)
```

The taxable earnings portion is reported on **Schedule 1, Line 8z** (Other income) with the description "Taxable 529 distribution" (or "Taxable Coverdell distribution"). It flows to Form 1040 Line 8.

### Step 6 — Determine if the 10% additional tax applies

The taxable earnings portion is generally subject to a **10% additional tax** under IRC §529(c)(6) (and §530(d)(4) for Coverdell). It's reported on **Schedule 2, Line 8** via Form 5329 Part II (529) or Part VII (Coverdell — verify against latest Form 5329).

Exceptions (no additional tax) under IRC §529(c)(6)(B):

- Beneficiary died — distribution to estate or another beneficiary
- Beneficiary became disabled — IRC §72(m)(7) definition
- Beneficiary received a tax-free scholarship — additional tax waived up to scholarship amount
- Beneficiary attended a U.S. service academy — waived up to costs of attendance
- Distribution was included in income only because of AOTC/LLC coordination — additional tax waived up to AOTC/LLC expenses
- Distribution was rolled over to another 529 / Coverdell within 60 days (covered by Step 2, not this step)
- SECURE 2.0 529-to-Roth rollover that qualifies — see Step 7

If an exception applies, document which exception and the dollar amount excluded. Form 5329 has the exception codes.

### Step 7 — SECURE 2.0 529-to-Roth IRA rollover (special path)

If the user indicated this distribution was a 529-to-Roth rollover under IRC §529(c)(3)(E) (added by SECURE 2.0 §126, effective for distributions after 2023), check **all** of the following:

1. The 529 account has been open for **15 years or more** (account age, not contribution age)
2. The Roth IRA recipient is **the beneficiary** of the 529 account (not the account owner unless they are also the beneficiary)
3. The amount transferred this year does not exceed the **annual Roth IRA contribution limit** for the beneficiary, reduced by any other IRA contributions they made for the year ($7,000 for 2025; 2026 limit set by IRS — verify)
4. The contribution being rolled over (or earnings on it) was in the 529 for **at least 5 years** before the rollover
5. **Lifetime cap of $35,000** per beneficiary across all years
6. The transfer is **trustee-to-trustee** (Box 4 should be checked)

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
- **10% additional tax applies** → Schedule 2 Line 8 via Form 5329
- **AOTC/LLC also being claimed** → Form 8863 with adjusted AAQEE
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
| 1 | Gross distribution | Total dollar amount distributed in the tax year |
| 2 | Earnings | Earnings portion of Box 1 (computed by trustee using §529 rules — IRC §529(c)(3)(D)) |
| 3 | Basis | Box 1 − Box 2 (return of contributions, never taxable) |
| 4 | Trustee-to-trustee transfer | Checkbox; if checked, distribution is generally non-taxable |
| 5 | Program type | 529 (state or private) or Coverdell ESA |
| 6 | Designated beneficiary | Checkbox; checked if recipient = beneficiary |

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

- [ ] Box 1 = Box 2 + Box 3 (Pub 970 — the trustee should have computed this; if it's off by more than rounding, the form is wrong)
- [ ] AAQEE ≤ Total QHEE
- [ ] Taxable earnings ≤ Box 2
- [ ] If Box 4 checked, taxable earnings = $0 (rollover is non-taxable)
- [ ] If Box 1 = Box 3 (i.e., Box 2 = $0), no taxable amount possible regardless of QHEE
- [ ] 10% additional tax = Taxable earnings × 10% (unless an exception applies)

### Sanity checks

Surface as warnings, do not block:

- [ ] Box 1 > $50,000 in a single year — confirm; large distributions sometimes indicate paying multiple semesters
- [ ] AAQEE is exactly equal to Box 1 — confirm the user isn't double-counting expenses already used for AOTC/LLC
- [ ] User claims SECURE 2.0 rollover but account is < 15 years old — does not qualify under IRC §529(c)(3)(E)
- [ ] User claims SECURE 2.0 rollover for $35,000+ in one year — exceeds annual Roth contribution limit; only the lower of the two caps applies
- [ ] Box 6 unchecked but recipient is the beneficiary per user — form may be wrong; ask trustee for corrected 1099-Q
- [ ] User had a tax-free scholarship but did not adjust QHEE downward — likely error; confirm
- [ ] User has K-12 expenses on a Coverdell — qualified; on a 529 — capped at $10,000/year per beneficiary
- [ ] Student loan repayment is being claimed but beneficiary already used the $10,000 lifetime cap — confirm
- [ ] Computer/internet expenses are claimed but the user describes mostly personal use — beneficiary primary-use test fails

### Cross-form checks

- [ ] If AOTC or LLC is also being claimed (Form 8863), AAQEE was reduced by the credit-claimed expenses
- [ ] If beneficiary is not the recipient on 1099-Q, taxable earnings go on the *recipient's* return, which may be a different return entirely (kiddie tax considerations may apply if recipient is the student under 24)
- [ ] If 10% additional tax applies, Form 5329 is included and the exception code (if any) is the right one

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
- Box 4 (Trustee-to-trustee transfer): [Yes | No]
- Box 5 (Program type): [State 529 | Private 529 | Coverdell ESA]
- Box 6 (Designated beneficiary is recipient): [Yes | No]

## Qualified Education Expenses
| Category                            | Amount  |
|-------------------------------------|---------|
| Tuition and required fees           | $X,XXX  |
| Required books and supplies         | $X,XXX  |
| Room and board (half-time+)         | $X,XXX  |
| Computer, software, internet        | $X,XXX  |
| K-12 tuition (529, ≤$10,000)        | $X,XXX  |
| Apprenticeship (529)                | $X,XXX  |
| Student loan repayment (529, ≤$10K) | $X,XXX  |
| **Total QHEE**                      | $X,XXX  |

## AAQEE Adjustment
- Tax-free scholarships:               −$X,XXX
- Employer education assistance:       −$X,XXX
- Expenses used for AOTC:              −$X,XXX
- Expenses used for LLC:               −$X,XXX
- **Adjusted QHEE (AAQEE)**:           = $X,XXX

## Taxable amount calculation
- Box 1:                          $X,XXX
- AAQEE:                          $X,XXX
- Non-qualified portion:          $X,XXX  (Box 1 − AAQEE)
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
- Trustee-to-trustee:            [Yes | No]
- **Qualifies for tax-free**:    [Yes | No]

## Where this goes on the return
- Schedule 1 Line 8z: $X,XXX (description: "Taxable 529/Coverdell distribution")
- Schedule 2 Line 8 via Form 5329 Part II/VII: $X,XXX (10% additional tax)
- 1040 Line 8: includes Schedule 1 Line 8z
- 1040 Line 23: includes Schedule 2 Line 8

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings raised>
- Next steps: <handoff items>

## Sources cited in this draft
- IRS Form 1099-Q (Rev. YYYY-MM)
- IRS Instructions for Forms 1099-Q and 1099-QA (Rev. YYYY-MM)
- IRC §529 (Qualified Tuition Programs)
- IRC §530 (Coverdell Education Savings Accounts)
- IRC §529(c)(3)(E) — SECURE 2.0 529-to-Roth rollover
- Pub 970 (Tax Benefits for Education), chapter 8
- Form 5329 (Additional Taxes on Qualified Plans)
```

The worksheet is the user's audit trail — IRS does not require it to be attached, but the user should keep it for at least 3 years (IRC §6501) along with the 1099-Q copy B and supporting expense receipts.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every box of Form 1099-Q with examples
- [`references/qualified-expenses.md`](./references/qualified-expenses.md) — Full eligible/ineligible list with citations
- [`references/aaqee-adjustment.md`](./references/aaqee-adjustment.md) — Coordination with scholarships, AOTC, LLC
- [`references/secure-2-roth-rollover.md`](./references/secure-2-roth-rollover.md) — IRC §529(c)(3)(E) requirements
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-trip mistakes with citations
- [`filing.md`](./filing.md) — How an agent enters 1099-Q-derived numbers into Form 1040 via FFFF, Direct File, paid software, or paper

## Examples

End-to-end worked personas. Use these when the user's situation is similar.

- [`examples/parent-paying-tuition.md`](./examples/parent-paying-tuition.md) — Parent withdraws $30,000 from 529 for daughter's tuition; fully qualified, fully tax-free
- [`examples/non-qualified-withdrawal.md`](./examples/non-qualified-withdrawal.md) — Recipient takes $5,000 non-qualified distribution; computes taxable earnings + 10% additional tax + Schedule 1/2 entries
- [`examples/secure-2-roth-rollover.md`](./examples/secure-2-roth-rollover.md) — 16-year-old 529 account; $7,000 rolled to beneficiary's Roth IRA under SECURE 2.0 §126

## Sources

Authoritative sources used. Re-verify each year — IRS revises forms and figures annually.

- [Form 1099-Q (latest)](https://www.irs.gov/pub/irs-pdf/f1099q.pdf) — the form itself
- [Instructions for Forms 1099-Q and 1099-QA](https://www.irs.gov/pub/irs-pdf/i1099qa.pdf) — combined instructions
- [About Form 1099-Q](https://www.irs.gov/forms-pubs/about-form-1099-q) — IRS landing page
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education (chapter 7 for Coverdell, chapter 8 for 529)
- [Form 5329](https://www.irs.gov/forms-pubs/about-form-5329) — Additional Taxes on Qualified Plans (10% additional tax on non-qualified distributions)
- [Form 8863](https://www.irs.gov/forms-pubs/about-form-8863) — Education Credits (AOTC, LLC) — coordination
- IRC §529 — Qualified Tuition Programs
- IRC §529(c)(3)(D) — Earnings allocation rule
- IRC §529(c)(3)(E) — 529-to-Roth IRA rollover (SECURE 2.0 §126, effective distributions after 12/31/2023)
- IRC §529(c)(6) — 10% additional tax and exceptions
- IRC §529(c)(7) — K-12 tuition (TCJA 2018, capped $10,000/year per beneficiary)
- IRC §529(c)(8) — Apprenticeship expenses (SECURE Act 2019)
- IRC §529(c)(9) — Qualified student loan repayments (SECURE Act 2019, $10,000 lifetime per beneficiary)
- IRC §530 — Coverdell Education Savings Accounts
- SECURE 2.0 Act of 2022, §126 — 529-to-Roth rollover

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and statute. It is not tax advice. Coordination with AOTC/LLC and the SECURE 2.0 rollover rules contain edge cases (kiddie tax, multiple beneficiaries, mid-year transfers) where a licensed tax professional should review the result before filing.
