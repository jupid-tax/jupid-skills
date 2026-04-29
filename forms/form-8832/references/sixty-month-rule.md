# 60-Month Rule Reference

The 60-month limitation in 26 CFR §301.7701-3(c)(1)(iv) is the single biggest trap on Form 8832. This file walks the rule in depth: when it applies, when it doesn't, and how to handle the two recognized exceptions.

---

## The rule

> **§301.7701-3(c)(1)(iv) — Limitation.** If an eligible entity makes an election under paragraph (c)(1)(i) of this section to change its classification (other than an election made by an existing entity to change its classification as of the effective date of this section), the entity cannot change its classification by election again during the sixty months succeeding the effective date of the election.

Plain English: once you elect, you're locked in for 60 months. The clock starts on the effective date of the election (Line 8), not the filing date or the IRS acceptance date.

The rule applies regardless of how the prior election turned out — even if the entity later regrets the election, even if there's a change in tax law that makes the prior choice suboptimal, the entity must wait out the 60 months.

---

## What counts as a "prior election"

An election under §301.7701-3(c)(1)(i) — the affirmative classification election made via Form 8832.

What does **not** count as a prior election:

- **Default classification.** An LLC that has only ever operated under default partnership / disregarded classification has not made an election; the 60-month rule does not apply on its first Form 8832.
- **Initial classification by a newly-formed entity** (Line 1 box (a) / Line 2b "Yes"). A newly-formed entity that elects on the date of formation has technically made an election, but §301.7701-3(c)(1)(iv) explicitly excludes "an election made by an existing entity to change its classification" — and an initial election is by definition not a change. The form codifies this in Line 2b: if the prior election was an initial classification, the 60-month rule does not block.
- **Mere conversion under state law.** If an LLC converts to a corporation under state-law conversion statute (without a Form 8832), it has not made a §301.7701-3 election — the new entity is a state-law corporation classified by §301.7701-2(b)(1). The 60-month rule does not apply.

---

## When the 60-month rule applies

All three must be true:

1. The entity made a prior Form 8832 election that was a **change** (not initial classification)
2. The effective date of the prior election was **less than 60 months ago** (counted from the desired new effective date)
3. **Neither exception below applies**

If all three are true, the new election is blocked. The IRS will reject (CP278) and the entity must wait out the remaining months.

---

## Exception 1 — More than 50% change in ownership

§301.7701-3(c)(1)(iv) lets the IRS waive the 60-month rule if **more than 50% of the ownership interests** in the entity have changed hands since the prior effective date.

This is a **discretionary** waiver, not automatic. The entity must:

- Demonstrate the ownership change with documentary evidence (operating agreement amendments, capital account schedules, member addition/withdrawal records, transfer documents)
- Make the showing in the Form 8832 filing itself (attached statement) or in response to an IRS inquiry
- Be prepared for IRS scrutiny — large ownership changes solely to qualify for re-election may be challenged as a sham

The 50% test is generally measured by capital interests OR profits interests (the regs are not crystal clear on the standard; in practice the IRS looks at whichever metric reflects the true economic change). Document both.

**Pattern**: original founder owned 100% of an LLC that elected C-corp 24 months ago. Founder sells 60% to a new investor. The new investor wants to revert the LLC to disregarded entity (for the founder, after redemption) or to partnership (multi-owner). The 50% change qualifies for the waiver — but the entity must lay out the facts in an attached statement and the IRS may take longer than the typical 60-day acknowledgment window.

---

## Exception 2 — Initial classification by newly-formed entity

If Line 2a = Yes (prior election in last 60 months) but Line 2b = Yes (prior election was the entity's first classification election effective on date of formation), the 60-month rule does not apply.

Why: the regulation excludes "an election made by an existing entity to change its classification". An entity that only ever made an initial-classification election has not "changed" classification — it set its initial classification. The new election is the first "change".

**Pattern**: LLC formed 2024-01-01 and elected C-corp effective 2024-01-01 (initial classification). In 2026, owner wants to revert to disregarded entity. Even though the election was 24 months ago (within 60 months), Line 2b = Yes means the rule does not block.

---

## What's NOT an exception (common confusion)

These patterns do NOT qualify:

- **Tax-law change.** TCJA, OBBBA, or any subsequent law change does not unlock the 60-month rule. Even if the prior election no longer makes sense given new rates, the entity is locked in.
- **Mistake or regret.** "I didn't understand the deemed-liquidation consequences" is not an exception. The entity is locked.
- **Bankruptcy or insolvency.** §301.7701-3(c)(1)(iv) makes no exception for distressed entities. The classification persists through bankruptcy.
- **Death of an owner.** Estate succession does not unlock unless it independently triggers a >50% ownership change (e.g., if the deceased owned >50% and the estate distribution shifts ownership to others).
- **Dissolution and re-formation under state law.** Some practitioners attempt to dissolve the LLC and form a new LLC to escape the 60-month rule. The IRS may collapse this as a step transaction or treat the new entity as a continuation of the old. This is risky and should not be attempted without counsel.

---

## Calculating the 60-month window

The 60 months are calculated from the **effective date of the prior election** (Line 8 on the prior Form 8832).

Examples:

| Prior Form 8832 effective date | Earliest new effective date |
|--------------------------------|------------------------------|
| 2021-01-01 | 2026-01-01 |
| 2022-06-15 | 2027-06-15 |
| 2024-12-31 | 2029-12-31 |

If the user wants to file a new Form 8832 with effective date X, the prior effective date must be on or before X minus 60 months. Postmark / filing dates are irrelevant — only the prior effective date matters.

---

## What to do if blocked

If the 60-month rule blocks and no exception applies:

1. **Wait.** This is the cleanest path. The entity can pre-file a Form 8832 up to 12 months before the desired effective date, so once the 60-month window expires, the entity can mail the form a year in advance and have it ready.

2. **Document an ownership change >50%.** If the business reality includes a major ownership shift, complete the new Form 8832 with an attached statement laying out the change. The IRS will review.

3. **Operate within the current classification.** If the entity is locked as a C-corp and can't revert to disregarded, the next-best move may be to elect S-corp on top of the C-corp classification (Form 2553) — assuming S-corp eligibility (≤100 shareholders, all US residents/citizens, single class of stock). The S-corp election is a different procedure and is not blocked by the 60-month entity-classification rule.

4. **Sell the entity and re-form.** Heavy-handed and potentially treated as a step transaction; only viable with major business-purpose support and counsel guidance.

---

## How to surface this to the user

When the agent detects the 60-month rule may apply (prior Line 8 effective date within 60 months, current Line 2b = No), the SKILL.md output should include this exact warning:

```
⚠ 60-month limitation flagged

Your prior Form 8832 election (effective <date>) is less than 60 months
from your desired new effective date (<desired date>). Under 26 CFR
§301.7701-3(c)(1)(iv), a re-election is generally blocked until <earliest
new effective date>.

Two exceptions to consider:

1. Has more than 50% of the ownership interest in the entity changed hands
   since the prior effective date? If yes, the IRS may waive the rule on
   showing of facts. We can attach a statement documenting the ownership
   change.

2. Was the prior election the entity's INITIAL classification on the date
   of formation? If yes, the rule does not apply (see Line 2b).

If neither exception applies, the entity must wait until <earliest new
effective date> to file. Form 8832 may be pre-filed up to 12 months
before the desired effective date.
```

The agent does not silently proceed when the 60-month rule is in question. Block the workflow until the user confirms an exception applies or chooses to wait.
