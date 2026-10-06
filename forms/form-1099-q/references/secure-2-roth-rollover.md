# 529-to-Roth IRA Rollover (SECURE 2.0 §126)

The SECURE 2.0 Act of 2022 added IRC §529(c)(3)(E), allowing a 529 plan beneficiary to roll over leftover funds to a Roth IRA. Effective for distributions after December 31, 2023.

This is a major change. Before SECURE 2.0, leftover 529 funds could only be (a) used for qualified expenses, (b) rolled to another beneficiary in the family or to an ABLE account, or (c) withdrawn as non-qualified (with earnings taxable + 10% additional tax). The Roth rollover gives another option — but only if **all five** conditions are met and the money moves by direct trustee-to-trustee transfer.

If even one condition fails, the rollover is treated as a regular non-qualified distribution: the earnings portion is taxable on Schedule 1 Line 8z, and the 10% additional tax applies on Form 5329 → Schedule 2 Line 8.

---

## The five required conditions

### Condition 1 — 15-year account age

The 529 account must have been **open for at least 15 years** at the time of the rollover.

The statute requires the account to have been "maintained for the 15-year period ending on the date of such distribution" (IRC §529(c)(3)(E)(i)); Pub. 970 (2025) ch. 7 and the Form 5498 instructions say "open for more than 15 years". An account opened January 1, 2010 passes for a distribution after January 1, 2025. For a distribution within days of the anniversary, ask the plan how it measures the period.

**Open issue (as of last verification)**: Treasury has not issued final regulations clarifying whether changing the beneficiary "resets" the 15-year clock. Some practitioners interpret §529(c)(3)(E) conservatively (clock resets on beneficiary change); others interpret broadly (clock measured from account opening regardless). Until guidance is final, the conservative interpretation is safer.

**Verify before relying on**: a recently-changed-beneficiary scenario.

### Condition 2 — Beneficiary is the Roth IRA owner

The Roth IRA receiving the rollover must be the **529 beneficiary's** Roth IRA — not the account owner's, the parent's, or any other person's.

If the 529 account owner (parent) and the beneficiary (student) are the same person, the rollover can flow into the parent/beneficiary's own Roth IRA.

If the beneficiary doesn't have a Roth IRA, they must open one to receive the rollover. The Roth IRA must be in the beneficiary's own name with their own SSN.

**Verify**: Box 6 on the 1099-Q ("Check if the recipient is not the designated beneficiary") should be blank, because the plan lists the beneficiary as recipient for a direct transfer to the beneficiary's Roth IRA (1099-Q instructions, Recipient's Name and TIN). If Box 6 is checked, the recipient is not the beneficiary; ask the plan before treating the rollover as qualified.

### Condition 3 — Annual Roth IRA contribution limit

The amount rolled over in any year cannot exceed the **annual Roth IRA contribution limit** for the beneficiary, reduced by any other IRA contributions they made in that year (traditional or Roth).

For 2025: $7,000 (or $8,000 if beneficiary is 50+, though most 529 beneficiaries are under 50; 2025 Instructions for Form 5329, line 10). For 2026: $7,500 (or $8,600 if 50+; [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf)). Year-dependent: re-check the IRS notice for each later year.

The beneficiary must also have **earned income** (compensation) at least equal to the rollover amount. The Roth limit is the §219 maximum, which cannot exceed compensation (IRC §408A(c)(2)(A), §219(b)(1); compensation defined in §219(f)(1)). If the beneficiary has no earned income, no rollover is possible.

The Roth IRA MAGI phase-out does not reduce the room for a 529 rollover (IRC §408A(c)(3)(E)), so a high-income beneficiary can still receive one.

**Common failure mode**: a 22-year-old beneficiary with $3,000 of summer-job earned income wants to roll over $7,000. The rollover is capped at $3,000 (the earned income amount), not $7,000.

### Condition 4 — 5-year contribution age

The amount rolled over cannot exceed the total contributions made to the account **before the 5-year period ending on the date of the distribution**, plus the earnings on those contributions (IRC §529(c)(3)(E)(i)(I)). Contributions made in the last 5 years, and their earnings, cannot be rolled over.

This is an aggregate test, not a tracing rule. The plan tracks contribution dates; ask the plan (or the user's contribution history) for the amount eligible on the transfer date. A contribution made on June 1, 2020 counts for a distribution after June 1, 2025; a contribution made in 2024 does not count until 2029.

This means a brand-new 529 account funded in year 1 cannot do any rollover until year 5 — and even then, the account must also satisfy Condition 1 (15 years), which means **the account itself**, not just the contribution, must be 15+ years old.

### Condition 5 — Lifetime cap of $35,000

The total amount rolled over from a 529 to the beneficiary's Roth IRA cannot exceed **$35,000 lifetime per beneficiary** across all years and across all 529 accounts naming that beneficiary.

This is a hard ceiling. Once $35,000 has rolled over, no further rollovers for that beneficiary are allowed, ever.

**Tracking responsibility**: the beneficiary (and the trustee) must track lifetime rollover amounts. There's no IRS-issued central tracker. The 529 plan reports the transfer on Form 1099-Q with Box 4b checked and must send a report to the Roth IRA trustee (IRC §529(d)(2)); the Roth IRA trustee reports the rollover in Form 5498 box 10, Roth IRA contributions (2025 Instructions for Forms 1099-R and 5498).

---

## Trustee-to-trustee execution

The rollover must be executed as a **direct trustee-to-trustee transfer** (from 529 to Roth IRA); the statute requires it (IRC §529(c)(3)(E)(i)(II)). Box 4b ("QTP to Roth IRA") on the 1099-Q should be checked.

A **distribution-then-contribution** sequence (taking cash out of the 529, then depositing it into the Roth) does NOT qualify under §529(c)(3)(E). It would be a non-qualified 529 distribution + a regular Roth contribution, with all the regular tax consequences of each.

The 529 plan codes the transfer in Box 4b of Form 1099-Q (added in the April 2025 revision; 1099-Q instructions, What's New and Boxes 4a-4b). The receiving Roth IRA trustee includes it in Form 5498 box 10 (Roth IRA contributions), which covers "qualified rollover contributions made from a section 529 qualified tuition program" (2025 Instructions for Forms 1099-R and 5498, Box 10).

---

## What the agent must verify

When the user indicates a 529-to-Roth rollover, the agent must confirm **each** of the five conditions explicitly. Don't assume any are met.

```
Condition checklist:
[ ] 1. 529 account is at least 15 years old (open date: ____)
[ ] 2. Roth IRA owner = 529 beneficiary (Box 6 of 1099-Q blank)
[ ] 3. Rollover amount ≤ annual Roth limit ($____) AND ≤ beneficiary's earned income ($____)
[ ] 4. Rollover amount ≤ contributions made before ____ (5 years before the transfer date) plus their earnings ($____)
[ ] 5. Lifetime rollover so far ≤ $35,000 (current cumulative: $____)
[ ] Direct trustee-to-trustee transfer (Box 4b of 1099-Q checked)
```

If all six are satisfied: the rollover is **non-taxable** AND **not subject to the 10% additional tax**. Nothing flows to the user's 1040 from this transaction. The user retains the 1099-Q, the receiving Roth IRA's 5498, and the worksheet for records.

If any condition fails: the rollover is treated as a regular non-qualified distribution. Compute taxable earnings via the AQEE formula (Steps 4-6 of the SKILL.md workflow). The agent should explicitly tell the user **which** condition failed and why, so they understand the tax consequence.

---

## Coordination with regular Roth IRA contributions

The amount rolled over from a 529 to a Roth IRA **counts against** the beneficiary's annual Roth contribution limit for that year. If the beneficiary already made a $3,000 traditional IRA contribution and a $1,000 Roth IRA contribution for 2025, their remaining 2025 Roth contribution room is $7,000 − $4,000 = $3,000. They can roll over a maximum of $3,000 from the 529 in 2025.

The beneficiary cannot work around the limit by rolling over more in subsequent years; each year is independently limited.

---

## Open questions and pending guidance

As of last verification (2026-10-06), Treasury has not issued final regulations on §529(c)(3)(E), and Pub. 970 (2025) does not address these points. Open practitioner questions:

1. Does changing the beneficiary reset the 15-year clock? (Conservative: yes. Aggressive: no.)
2. Is there any exception to the $35,000 lifetime cap? (None has been identified in the statute.)
3. Can a Roth conversion from a traditional IRA take place in the same year as a 529-to-Roth rollover? (Most likely yes; they're independent transactions, but verify.)
4. What happens if the rollover is made and a condition is later found to be unmet (e.g., trustee discovers contribution wasn't 5 years old)? (Likely treated as a non-qualified 529 distribution + an excess Roth contribution; remediation would require the beneficiary to withdraw the excess from the Roth.)

The agent should flag any uncertainty and recommend the user consult a tax professional for edge cases.

---

## Authority

- IRC §529(c)(3)(E) — added by SECURE 2.0 Act of 2022, §126; effective for distributions after 12/31/2023
- IRC §408A — Roth IRA general rules
- IRC §408A(c)(2), §219(b)(1) — limit capped at compensation; §219(f)(1) defines compensation
- IRC §408A(c)(3)(E) — MAGI phase-out does not reduce 529 rollover room
- IRC §529(d)(2) — plan's report to the Roth IRA trustee
- Pub. 970 (2025), ch. 7, Rollovers and Other Transfers
- Instructions for Form 1099-Q (Rev. April 2025), Boxes 4a-4b
- 2025 Instructions for Forms 1099-R and 5498, Form 5498 box 10
- Notice 2025-67 — 2026 IRA limit $7,500, catch-up $1,100
