# 60-Month Rule Reference

The 60-month limitation in 26 CFR §301.7701-3(c)(1)(iv) is the single biggest trap on Form 8832. This file walks the rule in depth: when it applies, when it doesn't, and how to handle the two recognized exceptions.

---

## The rule

> **§301.7701-3(c)(1)(iv) — Limitation.** If an eligible entity makes an election under paragraph (c)(1)(i) of this section to change its classification (other than an election made by an existing entity to change its classification as of the effective date of this section), the entity cannot change its classification by election again during the sixty months succeeding the effective date of the election. However, the Commissioner may permit the entity to change its classification by election within the sixty months if more than fifty percent of the ownership interests in the entity as of the effective date of the subsequent election are owned by persons that did not own any interests in the entity on the filing date or on the effective date of the entity's prior election. An election by a newly formed eligible entity that is effective on the date of formation is not considered a change for purposes of this paragraph (c)(1)(iv).

(The parenthetical "as of the effective date of this section" refers to the January 1, 1997 transition date of the regulations; it is not a general exception for existing entities.)

Plain English: once you elect, you're locked in for 60 months. The clock starts on the effective date of the election (Line 8), not the filing date or the IRS acceptance date.

The rule applies regardless of how the prior election turned out — even if the entity later regrets the election, even if there's a change in tax law that makes the prior choice suboptimal, the entity must wait out the 60 months.

---

## What counts as a "prior election"

An election under §301.7701-3(c)(1)(i) — the affirmative classification election made via Form 8832.

What does **not** count as a prior election:

- **Default classification.** An LLC that has only ever operated under default partnership / disregarded classification has not made an election; the 60-month rule does not block its first Form 8832. That first election is still a *change* (box 1b), so it starts a new 60-month clock.
- **Initial classification by a newly-formed entity** (Line 1 box (a) / Line 2b "Yes"). A newly-formed entity that elects effective on the date of formation has made an election, but the last sentence of §301.7701-3(c)(1)(iv) says such an election "is not considered a change." The form codifies this in Line 2b: if the prior election was an initial classification effective on formation, the 60-month rule does not block.
- **Mere conversion under state law.** If an LLC converts to a corporation under state-law conversion statute (without a Form 8832), it has not made a §301.7701-3 election — the new entity is a state-law corporation classified by §301.7701-2(b)(1). The 60-month rule does not apply.

---

## When the 60-month rule applies

All three must be true:

1. The entity made a prior Form 8832 election that was a **change** (not initial classification)
2. The effective date of the prior election was **less than 60 months ago** (counted from the desired new effective date)
3. **Neither exception below applies**

If all three are true, the new election is blocked. Form 8832 line 2b ("No. Stop here.") tells the filer not to proceed; a filed election would be denied (CP278 is the IRS notice code for denial of Form 8832, IRS Document 6209 §9) and the entity must wait out the remaining months.

---

## Exception 1 — More than 50% new ownership (private letter ruling)

§301.7701-3(c)(1)(iv) lets the IRS (the Commissioner) permit a change within the 60 months if **more than 50% of the ownership interests** in the entity, as of the effective date of the new election, are owned by persons that did not own any interest in the entity on the filing date or on the effective date of the prior election.

This is a **discretionary** permission, not automatic, and the Form 8832 instructions (lines 2a and 2b) say it is granted **by private letter ruling**. The entity must:

- Request a private letter ruling from the IRS National Office under the current Rev. Proc. 20XX-1 (Rev. Proc. 2026-1 for 2026), with the user fee in its Appendix A; it is not claimed by attaching a statement to Form 8832
- Demonstrate who the new owners are and that they held no interest on the prior election's filing date or effective date (operating agreement amendments, capital account schedules, transfer documents)
- Be prepared for IRS scrutiny — ownership changes made only to qualify may be challenged

The regulation measures "ownership interests" without defining capital vs. profits; document both and let counsel frame the ruling request.

**Pattern**: original founder owned 100% of an LLC that elected C-corp 24 months ago. Founder sells 60% to a new investor who held no prior interest. The new investor wants to change the classification to partnership. The new owner holds more than 50%, so the entity can ask for a private letter ruling permitting the change; until the ruling is issued, do not file Form 8832.

---

## Exception 2 — Initial classification by newly-formed entity

If Line 2a = Yes (prior election in last 60 months) but Line 2b = Yes (prior election was the entity's first classification election effective on date of formation), the 60-month rule does not apply.

Why: the regulation excludes "an election made by an existing entity to change its classification". An entity that only ever made an initial-classification election has not "changed" classification — it set its initial classification. The new election is the first "change".

**Pattern**: LLC formed 2024-01-01 and elected C-corp effective 2024-01-01 (initial classification). In 2026, owner wants to revert to disregarded entity. Even though the election was 24 months ago (within 60 months), Line 2b = Yes means the rule does not block. The 2026 reversion is itself a change and starts a new 60-month clock.

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

If the user wants to file a new Form 8832 with effective date X, the prior effective date must be on or before X minus 60 months. The filing date also matters for the form: line 2a asks whether a prior election had an effective date "within the last 60 months," which reads from the date the new form is filed. A form filed before the 60-month anniversary answers 2a "Yes" and 2b "No," and the form says "Stop here." Do not pre-file; file after the anniversary (the new effective date may be up to 75 days before filing, but not earlier than the anniversary).

---

## What to do if blocked

If the 60-month rule blocks and no exception applies:

1. **Wait.** This is the cleanest path. Prepare the Form 8832 in advance, but mail it after the 60-month anniversary of the prior effective date (see "Calculating the 60-month window": line 2a looks back from the filing date).

2. **Request a private letter ruling for a >50% new-ownership change.** If more than 50% of the interests are now held by people who held none at the prior election, counsel can request a ruling permitting the change. The IRS decides; there is no attached-statement route on Form 8832.

3. **Operate within the current classification.** If the entity is locked as a C-corp and can't revert to disregarded, an option to raise with the user's CPA is an S election on top of the corporate classification (Form 2553) — assuming S-corp eligibility under §1361(b) (≤100 shareholders; individuals who are U.S. citizens or residents, certain trusts and estates, and certain exempt organizations; no nonresident aliens; one class of stock). The S election does not change the entity's classification (it stays an association), so it is not blocked by the 60-month entity-classification rule.

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

1. Do persons who held no interest on the prior election's filing date or
   effective date now own more than 50% of the ownership interests? If yes,
   the IRS may permit the change by private letter ruling (a separate
   request with a user fee, prepared by counsel). It cannot be claimed on
   Form 8832 itself.

2. Was the prior election the entity's INITIAL classification on the date
   of formation? If yes, the rule does not apply (see Line 2b).

If neither exception applies, the entity must wait until <earliest new
effective date> to file. Do not pre-file: Form 8832 line 2a looks back 60
months from the filing date, so a form filed earlier hits "Stop here" at
line 2b.
```

The agent does not silently proceed when the 60-month rule is in question. Block the workflow until the user confirms an exception applies or chooses to wait.
