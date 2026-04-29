# 529-to-Roth IRA Rollover (SECURE 2.0 §126)

The SECURE 2.0 Act of 2022 added IRC §529(c)(3)(E), allowing a 529 plan beneficiary to roll over leftover funds to a Roth IRA. Effective for distributions after December 31, 2023.

This is a major change. Before SECURE 2.0, leftover 529 funds could only be (a) used for qualified expenses, (b) rolled to another beneficiary in the family, or (c) withdrawn as non-qualified (with earnings taxable + 10% additional tax). The Roth rollover gives a fourth option — but only if **all five** conditions are met.

If even one condition fails, the rollover is treated as a regular non-qualified distribution: the earnings portion is taxable on Schedule 1 Line 8z, and the 10% additional tax applies on Form 5329 → Schedule 2 Line 8.

---

## The five required conditions

### Condition 1 — 15-year account age

The 529 account must have been **open for at least 15 years** at the time of the rollover.

Account age is measured from the opening date of the 529 account, not from when the beneficiary was named. If the account was opened January 1, 2010, it qualifies for rollovers starting January 1, 2025.

**Open issue (as of last verification)**: Treasury has not issued final regulations clarifying whether changing the beneficiary "resets" the 15-year clock. Some practitioners interpret §529(c)(3)(E) conservatively (clock resets on beneficiary change); others interpret broadly (clock measured from account opening regardless). Until guidance is final, the conservative interpretation is safer.

**Verify before relying on**: a recently-changed-beneficiary scenario.

### Condition 2 — Beneficiary is the Roth IRA owner

The Roth IRA receiving the rollover must be the **529 beneficiary's** Roth IRA — not the account owner's, the parent's, or any other person's.

If the 529 account owner (parent) and the beneficiary (student) are the same person, the rollover can flow into the parent/beneficiary's own Roth IRA.

If the beneficiary doesn't have a Roth IRA, they must open one to receive the rollover. The Roth IRA must be in the beneficiary's own name with their own SSN.

**Verify**: Box 6 on the 1099-Q should be checked (designated beneficiary = recipient). If Box 6 is unchecked, the recipient is not the beneficiary, and the Roth-rollover qualification fails.

### Condition 3 — Annual Roth IRA contribution limit

The amount rolled over in any year cannot exceed the **annual Roth IRA contribution limit** for the beneficiary, reduced by any other IRA contributions they made in that year (traditional or Roth).

For 2025: $7,000 (or $8,000 if beneficiary is 50+, though most 529 beneficiaries are under 50). The 2026 limit is set by the IRS via inflation adjustment — verify before relying on a specific figure.

The beneficiary must also have **earned income** at least equal to the rollover amount. The earned income requirement applies to all Roth IRA contributions (IRC §219(f)(1)). If the beneficiary has no earned income, no rollover is possible.

**Common failure mode**: a 22-year-old beneficiary with $3,000 of summer-job earned income wants to roll over $7,000. The rollover is capped at $3,000 (the earned income amount), not $7,000.

### Condition 4 — 5-year contribution age

The contribution being rolled over (or the earnings on it) must have been in the 529 account for **at least 5 years** prior to the rollover.

The first-in-first-out (FIFO) rule applies: the trustee tracks the date each contribution was made. Rollovers come from the oldest contributions first. A contribution made in 2020 can be rolled over starting in 2025; a contribution made in 2024 cannot be rolled over until 2029.

This means a brand-new 529 account funded in year 1 cannot do any rollover until year 5 — and even then, the account must also satisfy Condition 1 (15 years), which means **the account itself**, not just the contribution, must be 15+ years old.

### Condition 5 — Lifetime cap of $35,000

The total amount rolled over from a 529 to the beneficiary's Roth IRA cannot exceed **$35,000 lifetime per beneficiary** across all years and across all 529 accounts naming that beneficiary.

This is a hard ceiling. Once $35,000 has rolled over, no further rollovers for that beneficiary are allowed, ever.

**Tracking responsibility**: the beneficiary (and the trustee) must track lifetime rollover amounts. There's no IRS-issued central tracker; the trustee receiving the rollover and the trustee sending it should both report on Form 1099-Q and Form 5498 to enable IRS cross-checking.

---

## Trustee-to-trustee execution

The rollover must be executed as a **trustee-to-trustee transfer** (direct from 529 to Roth IRA). Box 4 on the 1099-Q should be checked.

A **distribution-then-contribution** sequence (taking cash out of the 529, then depositing it into the Roth) does NOT qualify under §529(c)(3)(E). It would be a non-qualified 529 distribution + a regular Roth contribution, with all the regular tax consequences of each.

The trustee must code the 1099-Q to indicate the rollover. As of last verification, IRS has not issued a specific 1099-Q box for "Roth rollover" — Box 4 (trustee-to-trustee) is checked, and the 5498 from the receiving Roth IRA shows the contribution as a "rollover from 529". Verify against current Form 1099-Q and Form 5498 instructions before relying on box-level coding.

---

## What the agent must verify

When the user indicates a 529-to-Roth rollover, the agent must confirm **each** of the five conditions explicitly. Don't assume any are met.

```
Condition checklist:
[ ] 1. 529 account is at least 15 years old (open date: ____)
[ ] 2. Roth IRA owner = 529 beneficiary (Box 6 of 1099-Q checked)
[ ] 3. Rollover amount ≤ annual Roth limit ($____) AND ≤ beneficiary's earned income ($____)
[ ] 4. The rolled-over contribution has been in the 529 for at least 5 years (oldest contribution date: ____)
[ ] 5. Lifetime rollover so far ≤ $35,000 (current cumulative: $____)
[ ] Trustee-to-trustee transfer (Box 4 of 1099-Q checked)
```

If all six are satisfied: the rollover is **non-taxable** AND **not subject to the 10% additional tax**. Nothing flows to the user's 1040 from this transaction. The user retains the 1099-Q, the receiving Roth IRA's 5498, and the worksheet for records.

If any condition fails: the rollover is treated as a regular non-qualified distribution. Compute taxable earnings via the AAQEE formula (Steps 4-6 of the SKILL.md workflow). The agent should explicitly tell the user **which** condition failed and why, so they understand the tax consequence.

---

## Coordination with regular Roth IRA contributions

The amount rolled over from a 529 to a Roth IRA **counts against** the beneficiary's annual Roth contribution limit for that year. If the beneficiary already made a $3,000 traditional IRA contribution and a $1,000 Roth IRA contribution for 2025, their remaining 2025 Roth contribution room is $7,000 − $4,000 = $3,000. They can roll over a maximum of $3,000 from the 529 in 2025.

The beneficiary cannot work around the limit by rolling over more in subsequent years; each year is independently limited.

---

## Open questions and pending guidance

As of last verification (2026-04-29), Treasury has not issued final regulations on §529(c)(3)(E). Open practitioner questions:

1. Does changing the beneficiary reset the 15-year clock? (Conservative: yes. Aggressive: no.)
2. Is there any exception to the $35,000 lifetime cap? (None has been identified in the statute.)
3. Can a Roth conversion from a traditional IRA take place in the same year as a 529-to-Roth rollover? (Most likely yes; they're independent transactions, but verify.)
4. What happens if the rollover is made and a condition is later found to be unmet (e.g., trustee discovers contribution wasn't 5 years old)? (Likely treated as a non-qualified 529 distribution + an excess Roth contribution; remediation would require the beneficiary to withdraw the excess from the Roth.)

The agent should flag any uncertainty and recommend the user consult a tax professional for edge cases.

---

## Authority

- IRC §529(c)(3)(E) — added by SECURE 2.0 Act of 2022, §126; effective for distributions after 12/31/2023
- IRS guidance: as of last verification, IRS Notice 2024-2 (general SECURE 2.0 Q&A), Notice 2024-22 (further Q&A) — verify against latest IRS guidance
- IRC §408A — Roth IRA general rules
- IRC §219(f)(1) — earned income requirement for IRA contributions
- Pub 970 — when updated for SECURE 2.0 §126, will include the rollover rules
