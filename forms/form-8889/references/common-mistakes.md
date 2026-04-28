# Common Form 8889 Mistakes

Top filer errors with examples, impacts, and fixes. The agent should screen drafts for each of these before declaring the form ready.

---

## Mistake 1 — Contributing past the annual limit

**Pattern**: User maxes out their HSA at work (cafeteria plan, Line 9) and *also* makes a direct contribution (Line 2), ending up over Line 8.

**Example**: User has $4,000 of cafeteria-plan contributions on W-2 Box 12 W. They also write a $1,000 personal check to the HSA. Self-only coverage all year (2025).

```
Line 2: $1,000
Line 3: $4,300
Line 8: $4,300
Line 9: $4,000
Line 11: $4,000
Line 12: $1,000 + $4,000 = $5,000  → cap at Line 8 = $4,300
Excess: $5,000 − $4,300 = $700
```

**Impact**: 6% excise tax every year the excess remains in the HSA. Form 5329 Part VII.

**Fix**: Withdraw the $700 excess plus earnings before the unextended filing deadline (April 15, with extensions allowed). Custodian has a "return of excess contribution" form. Earnings on the excess are taxable income for the year of the original excess.

**Agent action**: When `Line 2 + Line 9 > Line 8`, surface a warning. Calculate the excess. Recommend immediate withdrawal if the deadline hasn't passed.

---

## Mistake 2 — Cafeteria-plan contributions on Line 2

**Pattern**: User reports W-2 Box 12 code W amount on Line 2 (direct contribution) instead of Line 9 (employer contribution).

**Impact**: The user is double-deducting. The cafeteria-plan amount is **already excluded from Box 1 wages**. Putting it on Line 2 takes the deduction a second time, creating a fictitious deduction.

**Example**: User has $5,000 on W-2 Box 12 code W. They put $5,000 on Line 2 thinking "I contributed it through payroll, that's me contributing".

```
Wrong:
  Line 2: $5,000  (incorrectly includes cafeteria-plan)
  Line 9: $0
  Line 13: $5,000  ← wrong, double-deducting

Right:
  Line 2: $0
  Line 9: $5,000  (cafeteria plan is employer contribution)
  Line 13: $0   ← correct, deduction already taken via Box 1 exclusion
```

**Fix**: Remove cafeteria-plan amounts from Line 2. Put on Line 9 only.

**Agent action**: ASK explicitly: "Is the contribution amount you mentioned through your employer's cafeteria plan (W-2 Box 12 code W)?" If yes → Line 9, NOT Line 2.

---

## Mistake 3 — Forgetting partial-year proration

**Pattern**: User enrolled in HDHP mid-year (e.g., July 1) and contributes the full annual limit, claiming they were "eligible at year-end."

**Example**: User started family HDHP on July 1, 2025. Contributed $8,550 directly. Did not explicitly invoke the last-month rule.

Without the last-month rule, Line 3 should be prorated: 6 months × ($8,550 / 12) = $4,275. The $8,550 contribution exceeds Line 3 by $4,275.

**Impact**: Excess contribution of $4,275, subject to 6% excise tax annually. If the user does invoke the last-month rule retroactively (allowed at filing time), they become subject to a 12-month testing period — losing HSA eligibility in 2026 triggers Part III on the 2026 return.

**Fix**: Either prorate (and withdraw the excess) or commit to the last-month rule and stay HSA-eligible for all of 2026.

**Agent action**: When coverage starts mid-year, ASK: "Were you HSA-eligible all 12 months of the year, or did your coverage start partway through? If partway, do you want to prorate your contribution limit, or invoke the last-month rule to allow the full limit (which requires you to remain HSA-eligible for all of next year)?"

---

## Mistake 4 — Using the HSA for non-qualified expenses

**Pattern**: User uses HSA debit card for vitamins, gym membership, individual-market premiums, or cosmetic dental work.

**Example**: User has $5,000 of HSA distributions in 2025 (1099-SA Box 1 = $5,000). $4,000 was for qualified medical (doctor, prescriptions, dental). $1,000 was for a gym membership.

```
Line 14a: $5,000
Line 15: $4,000
Line 16: $1,000  → Schedule 1, Line 8f (taxable income)
Line 17b: $1,000 × 20% = $200  → Schedule 2, Line 17c (penalty)
```

If user is 22% bracket: $1,000 × 22% federal + $200 penalty = $420 of extra tax on a $1,000 expense.

**Impact**: 20% penalty plus ordinary income tax (under 65). At 22%, the effective rate on the non-qualified $1,000 is 42%.

**Fix**: Confirm expenses are on the Pub 502 list before swiping the HSA card. When in doubt, pay from a regular account.

**Agent action**: Walk through Line 15 entries against the qualified-expense list ([`qualified-medical-expenses.md`](./qualified-medical-expenses.md)). Surface any items that look non-qualified.

---

## Mistake 5 — Not reporting all 1099-SA distributions

**Pattern**: Custodian sends 1099-SA showing $5,000. User reports only the $3,000 they used for medical and ignores the rest.

**Impact**: The IRS receives the same 1099-SA. Within 12–18 months, the user receives a CP2000 notice proposing additional tax on the unreported $2,000. Penalties and interest accrue from the original filing date.

**Example**: Line 14a entered as $3,000 instead of $5,000. The user thought "the rest was rollover so I don't report it."

**Fix**: Every dollar on 1099-SA Box 1 must appear on Line 14a. Rollovers and excess returns subtract on Line 14b. Net distribution on Line 14c is what gets evaluated for taxability.

**Agent action**: ASK for the actual 1099-SA Box 1 amount. Cross-check that Line 14a = 1099-SA Box 1. Anything different goes on Line 14b with documentation.

---

## Mistake 6 — Contributing while enrolled in Medicare

**Pattern**: User turns 65, signs up for Medicare Part A (often automatic if they take Social Security), and continues HSA contributions.

**Impact**: Medicare enrollment disqualifies HSA contributions starting the month of enrollment. Continuing to contribute creates excess contributions, subject to 6% excise tax annually.

**Special case — retroactive Part A**: When someone takes Social Security after 65, Medicare Part A enrollment is automatic and **retroactive up to 6 months** (or back to the 65th birthday, whichever is later). This can retroactively disqualify HSA contributions made during those 6 months.

**Example**: User enrolls in Social Security at age 66. Medicare Part A auto-enrolls retroactive to age 65 birthday or 6 months back, whichever later. Any HSA contributions made during those retroactive months are now excess.

**Fix**: Stop HSA contributions the month before Medicare enrollment (or 6 months before claiming Social Security after 65). Withdraw any excess plus earnings before the filing deadline.

**Agent action**: ASK every user 64+ about Medicare enrollment status, current and planned. Surface a warning if the user took Social Security after 65 and made HSA contributions in the prior 6 months.

---

## Mistake 7 — Spouse's general-purpose FSA disqualifies HSA

**Pattern**: User has HDHP. Spouse has a general-purpose FSA at the spouse's employer. User contributes to HSA assuming they're eligible — but the spouse's FSA "is available to" the user, disqualifying HSA-eligibility.

**Example**: User has self-only HDHP through their employer. Spouse has a $2,000 general-purpose FSA at her employer. The FSA is technically "available" to use for the user's medical expenses — disqualifying HSA-eligibility for every month the FSA is active.

**Impact**: All of the user's HSA contributions during disqualified months become excess contributions. 6% excise tax annually. If the user took distributions during this period, those distributions can also be challenged.

**Fix**: Spouse elects a **limited-purpose FSA** (dental and vision only) or no FSA. The HSA holder spouse keeps HDHP and HSA. Confirm with both employers' benefits administrators before relying on this fix.

**Agent action**: ASK: "Does your spouse have any kind of FSA at their job? If so, is it a general-purpose FSA or a limited-purpose FSA (dental and vision only)?"

---

## Mistake 8 — MFJ family limit doubled instead of shared

**Pattern**: Both spouses covered under one family HDHP. Each contributes the family limit ($8,550 in 2025) to their own HSA, totaling $17,100.

**Impact**: The family limit is **shared, not doubled**. The combined contributions cap at $8,550 (plus catch-ups if 55+, which are individual). Excess: $8,550 over the family limit.

**Fix**: Allocate the family limit between spouses by agreement. Common: 100/0, 50/50. Document each spouse's allocated share on their own Line 6. Each catch-up is separate.

**Agent action**: When MFJ with two HSAs and family HDHP, ASK how the spouses agreed to split the limit. Refuse to draft until they confirm an allocation that totals to the family limit.

---

## Mistake 9 — Catch-up contribution into spouse's HSA

**Pattern**: Spouse A is 56 and HSA-eligible. Spouse B has the family HSA. Spouse A's $1,000 catch-up is contributed to Spouse B's HSA.

**Impact**: The catch-up is invalid — must go into the contributor's **own** HSA. The $1,000 in Spouse B's HSA becomes an excess contribution there.

**Fix**: Spouse A opens their own HSA (any custodian) and contributes the $1,000 there. If the wrong-HSA contribution already happened, withdraw the excess from Spouse B's HSA (plus earnings) before the filing deadline and re-contribute to Spouse A's HSA.

**Agent action**: When age 55+ catch-up is involved, ASK whether each catch-up went into the corresponding spouse's own HSA.

---

## Mistake 10 — Forgetting Form 8889 entirely

**Pattern**: User had no distributions and made only cafeteria-plan contributions. They think Form 8889 isn't needed because "the deduction is already on my W-2".

**Impact**: Form 8889 is **required** for anyone who made or received any HSA contributions during the year, including cafeteria-plan contributions on W-2 Box 12 code W. Failing to file means the IRS sees Box 12 W income exclusion without the corresponding 8889 — likely to trigger a notice.

**Fix**: File Form 8889 every year contributions occur, regardless of source. The form will show $0 on Line 13 if all contributions were cafeteria-plan, but it must still be filed.

**Agent action**: Even when Line 13 is $0, generate the Form 8889 draft if Line 9 > 0 or Line 14a > 0.

---

## Quick screening checklist

Before declaring a Form 8889 draft ready, the agent runs:

- [ ] `Line 2 + Line 9 ≤ Line 8`? If not, surface excess contribution
- [ ] Is the cafeteria-plan amount on Line 9 (not Line 2)?
- [ ] If partial-year coverage, is Line 3 prorated OR has the user explicitly opted into the last-month rule?
- [ ] If last-month rule used in prior year, has the user been asked about testing-period eligibility?
- [ ] Are all expenses on Line 15 on the qualified list?
- [ ] Does Line 14a match 1099-SA Box 1 exactly?
- [ ] If user is 64+, has Medicare enrollment status been confirmed?
- [ ] If MFJ with two HSAs, is the family limit split documented?
- [ ] If catch-up on Line 7, is it in the contributor's own HSA?
- [ ] If user has W-2 Box 12 code W or any 1099-SA distribution, is Form 8889 being filed at all?
