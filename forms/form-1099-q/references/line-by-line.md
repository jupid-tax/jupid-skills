# Form 1099-Q — Box-by-Box Reference

Complete lookup for every box on Form 1099-Q. Use when the agent needs to confirm what each box means or how it interacts with the user's return.

Form 1099-Q is filed by the **payer** (529 plan trustee, Coverdell custodian, qualified tuition program). The **recipient** receives copy B and uses it to compute their own tax. The recipient does NOT file Form 1099-Q itself — they file derived numbers on their Form 1040 / Schedule 1 / Schedule 2 / Form 5329.

Source: [Form 1099-Q (Rev.)](https://www.irs.gov/pub/irs-pdf/f1099q.pdf), [Instructions for Forms 1099-Q and 1099-QA](https://www.irs.gov/pub/irs-pdf/i1099qa.pdf), Pub 970.

---

## Header — Identifying the parties

| Field | What it shows | Notes |
|-------|---------------|-------|
| Payer's name and TIN | Trustee/custodian (e.g., "Vanguard 529", "Fidelity Coverdell") | Use to verify the form is from the right plan |
| Recipient's name and TIN | Person who received the distribution | This is the person whose return reports any taxable amount |
| Account number | Plan-specific account ID | Useful when the user has multiple 529 accounts |

The recipient is the person to whom the check was payable, OR the person on whose behalf the trustee paid the school. Per IRS rules:

- If distribution went to the **account owner** (e.g., parent), recipient = account owner
- If distribution went to the **beneficiary** (student) directly or to their school, recipient = beneficiary

This matters because Box 6 indicates whether the recipient is the designated beneficiary, and the **taxable portion is reported on the recipient's tax return** — not the account owner's, if those are different.

---

## Box 1 — Gross distribution

The **total dollar amount distributed in the tax year**, including both basis (Box 3) and earnings (Box 2). This is the headline figure.

**What goes here:**
- Cash distributions to the recipient
- Direct payments to an eligible educational institution on behalf of the beneficiary
- Distributions used for qualified higher education expenses (still reported here even if tax-free)
- Distributions used for non-qualified purposes
- Refunds of contributions previously withdrawn (depends on §529 rules)

**What does NOT go here:**
- Internal account growth that wasn't withdrawn (no taxable event)
- Trustee-to-trustee rollovers between two 529 plans (those *are* Box 1, but Box 4 is checked)
- The original contribution if it stayed in the account

**Validation**: Box 1 must equal Box 2 + Box 3. If it doesn't, the trustee's form is wrong; ask for a corrected 1099-Q.

---

## Box 2 — Earnings

The **earnings portion of Box 1**, computed by the trustee using the §529(c)(3)(D) formula. This represents investment growth on contributions, allocated proportionally to the distribution.

The trustee tracks contributions vs. earnings on each contribution date. When the recipient takes a distribution, the trustee computes earnings as:

```
Earnings = Distribution × (Account earnings on date of distribution / Total account value on date of distribution)
```

The recipient does **not** recompute this; the trustee's number on Box 2 is authoritative.

**Tax consequence**: Box 2 is the **only portion** that can ever be taxable. Box 3 (basis) is already-taxed contributions and is never taxable.

If Box 2 = $0, the distribution is entirely return of basis (no earnings), and no part is ever taxable regardless of how the user spent it.

If Box 2 > $0 and the distribution is non-qualified, a fraction of Box 2 — proportional to the non-qualified portion of Box 1 — is taxable. See [`aaqee-adjustment.md`](./aaqee-adjustment.md) for the calculation.

---

## Box 3 — Basis

The **return of contributions** portion of Box 1. The recipient's after-tax money coming back out.

```
Box 3 = Box 1 − Box 2
```

Basis is **never taxable**, regardless of how the user spent the distribution. It's the same dollars that went in, returning back out.

For a Coverdell ESA, basis includes the original contribution. For a 529, basis includes:
- Original contributions
- Rollovers from another 529 (basis carries over)
- Re-contributions of refunded tuition within 60 days (IRC §529(c)(3)(D))

State tax treatment may differ — some states recapture state tax deductions on basis if used non-qualified. Out of scope for this federal skill.

---

## Box 4 — Trustee-to-trustee transfer

A **checkbox**. If checked, the distribution was a direct rollover from one qualified tuition program to another (or from one Coverdell ESA to another), executed within the §529 60-day rollover window.

**Tax consequence**: a qualifying trustee-to-trustee transfer is **non-taxable** to the recipient. Effectively, the funds never left the qualified-program system.

Conditions for non-taxable treatment (verify):

- 60-day window between the distributing plan and the receiving plan (IRC §529(c)(3)(C))
- Same beneficiary OR a member of the family of the original beneficiary (IRC §529(e)(2))
- For 529-to-529 same-beneficiary rollovers: only one such rollover per beneficiary per 12-month period (IRC §529(c)(3)(C)(iii))
- Coverdell-to-Coverdell rollovers: same one-per-12-months rule
- 529-to-Roth IRA rollovers under SECURE 2.0 (IRC §529(c)(3)(E)) require all 5 conditions in [`secure-2-roth-rollover.md`](./secure-2-roth-rollover.md) — Box 4 should be checked but the agent must verify the additional conditions

**Caution**: Box 4 only confirms the transfer was trustee-to-trustee. It does NOT certify all the other conditions are met. The recipient is responsible for verifying.

If Box 4 is checked but a condition fails (e.g., second rollover within 12 months), the distribution is treated as **non-qualified** and Steps 5-6 of the workflow apply.

---

## Box 5 — Program type

A **checkbox indicating the type of qualified program**:

- **Private 529** — sponsored by a private educational institution under IRC §529(b)(1)(A)(ii) (e.g., Independent 529)
- **State 529** — sponsored by a state government or agency under IRC §529(b)(1)(A)(i) (the most common — every state has one)
- **Coverdell ESA** — IRC §530 account (different rules: $2,000/year contribution limit, lower income phase-outs, K-12 expenses always qualified)

**Why this matters:**

- Coverdell qualified expenses include K-12 tuition, fees, books, supplies, equipment, tutoring, special needs services, room and board, uniforms, transportation, and computers — IRC §530(b)(3). Broader than 529 K-12 (which is limited to $10,000/year tuition).
- Coverdell additional tax is under IRC §530(d)(4); 529 additional tax under IRC §529(c)(6). Both are 10%, but reported in different parts of Form 5329 — verify against the current Form 5329 instructions.
- 529-to-Roth rollover (IRC §529(c)(3)(E)) is **only for 529 plans**, not Coverdell.

---

## Box 6 — Designated beneficiary

A **checkbox**. If checked, the recipient (Box "Recipient's name") IS the designated beneficiary of the 529/Coverdell account.

If unchecked, the recipient is someone other than the designated beneficiary — typically the account owner (parent) when the account owner takes a distribution payable to themselves rather than directly to the school.

**Tax consequence:**

- Whose return reports the taxable portion: the recipient's, period. If recipient = beneficiary (Box 6 checked), the student reports it. If recipient ≠ beneficiary, the account owner reports it.
- For SECURE 2.0 529-to-Roth rollover: the rollover must be to the **beneficiary's** Roth IRA, not the account owner's. So if Box 6 is unchecked AND the user claims a 529-to-Roth rollover, the rollover does not qualify.

---

## State / Account number boxes

Lower portion of the form may include:

- **State** — sometimes included if the trustee is reporting state-level information
- **State identification number** — trustee's state TIN
- **State distribution** — amount distributed reportable to the state (some states require separate reporting)

These are **informational only** for federal purposes. State tax treatment varies (e.g., recapture of state tax deductions for non-qualified distributions). Out of scope for federal Form 1040 — but the user should retain the form for state filing.

---

## What gets reported on the user's return

The recipient enters **derived** numbers on their Form 1040, not the raw 1099-Q boxes:

| Computed amount | Reported on |
|-----------------|-------------|
| Taxable earnings portion | Schedule 1 Line 8z (description: "Taxable 529 distribution" or "Taxable Coverdell distribution") → flows to 1040 Line 8 |
| 10% additional tax | Form 5329 Part II → Schedule 2 Line 8 → 1040 Line 23 |
| Tax-free portion | Not reported anywhere; retain records |
| 529-to-Roth rollover (qualifying) | Not reported; retain records of the 5 conditions |
| Trustee-to-trustee 529-to-529 transfer | Not reported; retain records |

The user does **not** attach the 1099-Q to the return — paper or electronic. The trustee already filed copy A with the IRS; the user keeps copy B for at least 3 years (IRC §6501).

---

## Common mismatches and how to handle them

**Box 1 ≠ Box 2 + Box 3**: trustee error. Request a corrected 1099-Q. Don't override.

**Recipient's name is the parent but Box 6 is checked (designated beneficiary)**: trustee error or unusual structure. Ask user to confirm with trustee.

**Box 4 checked but the user describes spending the money on tuition**: the user may be confusing "distribution to school" (Box 4 unchecked, distribution to school is qualified spending — but not a trustee-to-trustee transfer) with "rolled over to another 529" (Box 4 checked). Ask user to confirm.

**Multiple 1099-Q forms for the same beneficiary**: the user took distributions from multiple plans. Each 1099-Q is processed separately, but QHEE can only be allocated once across all plans + AOTC/LLC. The agent should aggregate Box 1 across forms when computing AAQEE.

**1099-Q recipient is the beneficiary (student) and the student is a dependent**: the taxable portion is on the student's return, not the parent's. Watch for kiddie tax (Form 8615) if the student is under 24 and meets the criteria. Out of scope for this skill — note and refer to a tax professional if applicable.
