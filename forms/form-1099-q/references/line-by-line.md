# Form 1099-Q — Box-by-Box Reference

Complete lookup for every box on Form 1099-Q. Use when the agent needs to confirm what each box means or how it interacts with the user's return.

Form 1099-Q is filed by the **payer** (529 plan trustee, Coverdell custodian, qualified tuition program). The **recipient** receives copy B and uses it to compute their own tax. The recipient does NOT file Form 1099-Q itself — they file derived numbers on their Form 1040 / Schedule 1 / Schedule 2 / Form 5329.

Source: [Form 1099-Q (Rev. April 2025)](https://www.irs.gov/pub/irs-pdf/f1099q.pdf), [Instructions for Form 1099-Q (Rev. April 2025)](https://www.irs.gov/pub/irs-pdf/i1099q.pdf), Pub. 970 (2025). Box map verified 2026-10-06 against the April 2025 revision (continuous use). Re-check https://www.irs.gov/forms-pubs/about-form-1099-q for a newer revision before relying on this map.

---

## Header — Identifying the parties

| Field | What it shows | Notes |
|-------|---------------|-------|
| Payer's name and TIN | Trustee/custodian (e.g., "Vanguard 529", "Fidelity Coverdell") | Use to verify the form is from the right plan |
| Recipient's name and TIN | Person who received the distribution | This is the person whose return reports any taxable amount |
| Account number | Plan-specific account ID | Useful when the user has multiple 529 accounts |

The recipient is set by the 1099-Q instructions (Recipient's Name and TIN):

- **QTP (529)**: the designated beneficiary is the recipient only if the distribution was paid (a) directly to the beneficiary, (b) to an eligible educational institution for the beneficiary, or (c) by direct trustee-to-trustee transfer to a Roth IRA for the beneficiary. Otherwise the account owner (e.g., parent) is the recipient
- **Coverdell ESA**: the designated beneficiary is always the recipient

This matters because Box 6 is checked when the recipient is NOT the designated beneficiary, and the **taxable portion is reported on the recipient's tax return** — not the account owner's, if those are different.

---

## Box 1 — Gross distribution

The **total dollar amount distributed in the tax year**, including both basis (Box 3) and earnings (Box 2). This is the headline figure.

**What goes here:**
- Cash distributions to the recipient
- In-kind distributions (tuition credits or certificates, payment vouchers, tuition waivers)
- Direct payments to an eligible educational institution on behalf of the beneficiary
- Distributions used for qualified higher education expenses (still reported here even if tax-free)
- Distributions used for non-qualified purposes
- Refunds to the account owner or beneficiary, and payments to the beneficiary on death or disability
- Trustee-to-trustee transfers, on a separate Form 1099-Q with Box 4a or 4b checked

**What does NOT go here:**
- Internal account growth that wasn't withdrawn (no taxable event)
- The original contribution if it stayed in the account
- A change of designated beneficiary to a member of the former beneficiary's family (no Form 1099-Q is filed)

Source: 1099-Q instructions, Box 1 and Box 2 ("file a separate Form 1099-Q for any trustee-to-trustee transfer"), Specific Instructions (beneficiary change).

**Validation**: Box 1 must equal Box 2 + Box 3. If it doesn't, the trustee's form is wrong; ask for a corrected 1099-Q. Exception: for a Coverdell ESA, the trustee may leave boxes 2 and 3 blank and report the year-end fair market value in Box 7 labeled "FMV"; figure earnings and basis with the Coverdell ESA Taxable Distributions and Basis worksheet in Pub. 970 ch. 6.

---

## Box 2 — Earnings

The **earnings portion of Box 1**, computed by the trustee with the earnings ratio in Prop. Reg. §1.529-3, Notice 2001-81, and Notice 2016-13 (1099-Q instructions, Box 2). This represents investment growth on contributions, allocated proportionally to the distribution. Box 2 shows a loss only in the final year of distributions from the account; otherwise a loss is reported as zero.

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

## Boxes 4a and 4b — Type of transfer

Two **checkboxes** (Box 4b was added in the April 2025 revision):

- **4a Trustee-to-trustee**: direct transfer from one QTP to another, or from a QTP to an ABLE account; for a Coverdell ESA, a direct transfer to another Coverdell ESA or to a QTP
- **4b QTP to Roth IRA**: direct transfer from a QTP to a Roth IRA maintained for the QTP beneficiary

A cash distribution that the user redeposits into another QTP or an ABLE account within 60 days is a rollover too, but it arrives on a 1099-Q with Box 4 blank; ask the user.

**Tax consequence**: a qualifying trustee-to-trustee transfer is **non-taxable** to the recipient. Effectively, the funds never left the qualified-program system.

Conditions for non-taxable treatment (verify):

- For a cash rollover, redeposit within 60 days of the distribution (IRC §529(c)(3)(C)(i))
- Same beneficiary OR a member of the family of the original beneficiary (IRC §529(e)(2))
- QTP to ABLE: the amount plus other ABLE contributions for the year stays within the ABLE annual limit (IRC §529(c)(3)(C)(i), flush sentence; made permanent by P.L. 119-21 §70117)
- For 529-to-529 same-beneficiary rollovers: only one such rollover per beneficiary per 12-month period (IRC §529(c)(3)(C)(iii))
- Coverdell-to-Coverdell rollovers: same one-per-12-months rule
- 529-to-Roth IRA rollovers under SECURE 2.0 (IRC §529(c)(3)(E)) require all 5 conditions in [`secure-2-roth-rollover.md`](./secure-2-roth-rollover.md) — Box 4b should be checked but the agent must verify the additional conditions

**Caution**: Box 4a or 4b only confirms the type of transfer. It does NOT certify all the other conditions are met. The recipient is responsible for verifying.

If Box 4a or 4b is checked but a condition fails (e.g., second rollover within 12 months), the distribution is treated as **non-qualified** and Steps 5-6 of the workflow apply.

---

## Boxes 5a to 5c — Distribution is from

Three **checkboxes indicating the type of qualified program**:

- **5a Private QTP** — established by one or more private eligible educational institutions (IRC §529(b)(1)(A)(ii))
- **5b State QTP** — established by a state or its agency (IRC §529(b)(1)(A)(i)); the most common
- **5c Coverdell ESA** — IRC §530 account (different rules: $2,000/year contribution limit, lower income phase-outs, K-12 expenses always qualified)

**Why this matters:**

- Coverdell qualified expenses include K-12 tuition, fees, books, supplies, equipment, academic tutoring, special needs services, room and board, uniforms, transportation, and computers — IRC §530(b)(3)(A). No dollar cap. 529 K-12 expenses are capped per beneficiary at $10,000 for 2025 and $20,000 for taxable years beginning after Dec. 31, 2025 (IRC §529(e)(3)(A)).
- Coverdell additional tax is under IRC §530(d)(4); 529 additional tax under IRC §529(c)(6), which applies the same tax. Both are 10% and both go on Form 5329 Part II, lines 5 to 8 (2025 Form 5329).
- 529-to-Roth rollover (IRC §529(c)(3)(E)) is **only for 529 plans**, not Coverdell.

---

## Box 6 — Check if the recipient is not the designated beneficiary

A **checkbox**. If checked, the recipient (Box "Recipient's name") is NOT the designated beneficiary — typically the account owner (parent) who took a distribution payable to themselves rather than to the student or the school.

If blank, the recipient IS the designated beneficiary of the 529/Coverdell account. Source: 1099-Q instructions, "Box 6. Designated Beneficiary Checkbox".

**Tax consequence:**

- Whose return reports the taxable portion: the recipient's, period. If recipient = beneficiary (Box 6 blank), the student reports it. If recipient ≠ beneficiary (Box 6 checked), the account owner reports it.
- For SECURE 2.0 529-to-Roth rollover: the rollover must be to the **beneficiary's** Roth IRA, not the account owner's, and the instructions list the beneficiary as recipient for that transfer. So if Box 6 is checked AND the user claims a 529-to-Roth rollover, the rollover does not qualify.

---

## Box 7 — FMV or distribution code (Copy B)

- For a Coverdell ESA, if the trustee did not report earnings and basis, Box 7 shows the account's fair market value as of December 31, labeled "FMV". Use the Pub. 970 ch. 6 Coverdell worksheet.
- Otherwise the trustee may, but is not required to, enter a distribution code: **1** distributions (including transfers); **2** excess Coverdell contributions plus earnings taxable in the current year; **3** excess contributions plus earnings taxable in the prior year; **4** disability; **5** death; **6** prohibited transaction.
- Code 4 or 5 points to an exception to the 10% additional tax; still confirm the facts with the user.

Source: Form 1099-Q (Rev. April 2025) Copy B; 1099-Q instructions, Box 1 caution and Distribution Codes.

## Account number box

The form has an **Account number** box (required when the payer files more than one Form 1099-Q for the recipient). There are no state boxes on Form 1099-Q. State tax treatment varies (e.g., recapture of state tax deductions for non-qualified distributions) and is out of scope for this federal skill; the user should keep the form for state filing.

---

## What gets reported on the user's return

The recipient enters **derived** numbers on their Form 1040, not the raw 1099-Q boxes:

| Computed amount | Reported on |
|-----------------|-------------|
| Taxable earnings portion | Schedule 1 Line 8z (description: "Taxable 529 distribution" or "Taxable Coverdell distribution") → flows to 1040 Line 8 |
| 10% additional tax | Form 5329 Part II lines 5 to 8 (file it for any taxable QTP/Coverdell distribution, even if line 8 is $0) → Schedule 2 Line 8 → 1040 Line 23 |
| Tax-free portion | Not reported anywhere; retain records |
| 529-to-Roth rollover (qualifying) | Not reported; retain records of the 5 conditions |
| Trustee-to-trustee 529-to-529 transfer | Not reported; retain records |

The user does **not** attach the 1099-Q to the return — paper or electronic. The trustee already filed copy A with the IRS; the user keeps copy B for at least 3 years (IRC §6501).

---

## Common mismatches and how to handle them

**Box 1 ≠ Box 2 + Box 3**: trustee error. Request a corrected 1099-Q. Don't override.

**Recipient's name is the parent but Box 6 is blank (or the student with Box 6 checked)**: trustee error or unusual structure. Ask user to confirm with trustee.

**Box 4a checked but the user describes spending the money on tuition**: the user may be confusing "distribution to school" (Box 4a blank, distribution to school is qualified spending — but not a trustee-to-trustee transfer) with "rolled over to another 529" (Box 4a checked). Ask user to confirm.

**Multiple 1099-Q forms for the same beneficiary**: the user took distributions from multiple plans. Each 1099-Q is processed separately, but QHEE can only be allocated once across all plans + AOTC/LLC. The agent should aggregate Box 1 across forms when computing AQEE.

**1099-Q recipient is the beneficiary (student) and the student is a dependent**: the taxable portion is on the student's return, not the parent's. Watch for kiddie tax (Form 8615) if the student is under 24 and meets the criteria. Out of scope for this skill — note and refer to a tax professional if applicable.
