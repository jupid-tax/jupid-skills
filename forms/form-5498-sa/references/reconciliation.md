# Form 5498-SA Reconciliation — Diagnosis Tree

When the reconciliation between Form 5498-SA and Form 8889 fails, this diagnosis tree walks through the most common causes in order of frequency.

---

## The reconciliation formula

```
Form 8889 Line 2 (direct) + Line 9 (employer/cafeteria) + Line 10 (IRA funding distribution)
  =
Box 2 of this year's 5498-SA (all money received this calendar year)
  − Box 3 of LAST year's 5498-SA (money received this year but designated for last year)
  + Box 3 of THIS year's 5498-SA (money received Jan 1–Apr 15 of next year, designated for this year)
```

In most cases, only the first term on the right side matters. The Box 3 corrections apply only when the filer made prior-year-designated contributions (2025 Instructions for Forms 1099-SA and 5498-SA, Boxes 2 and 3). Line 9 can also differ from W-2 code W when the Employer Contribution Worksheet moves employer money between years (2025 Instructions for Form 8889, Line 9).

---

## When the formula fails — diagnosis order

### Cause 1 (most common): Prior-year contribution timing

**Symptom:** The user reports an amount on Form 8889 Line 2 that is higher than 5498-SA Box 2 by exactly the amount of a contribution they remember making in January, February, or March of the next year — or this year's Box 2 is higher than expected by a contribution made early this year for last year.

**Diagnosis:**

```
Did you make a contribution between January 1 and April 15 of the year following the tax year,
and tell the custodian it was for the prior tax year?
```

If yes, that contribution appears in **Box 3 of the same tax year's 5498-SA** (and later in the next year's Box 2). Read Box 3 on the form in hand.

**Action:** Confirm Box 3 shows the designated amount. If it does, no amendment is needed — Form 8889 was correct. If Box 3 is $0 but the custodian's history shows the designation, ask the custodian for a corrected 5498-SA. Next year, subtract this Box 3 from next year's Box 2.

**Note:** This cause causes more reconciliation panic than any other. Always check it first.

---

### Cause 2: December check timing

**Symptom:** User wrote a check on December 28 for an HSA contribution. Bank cleared the check on January 3. User counted it on Form 8889 for the year of the check date; custodian counted it for the year of the deposit date.

**Diagnosis:**

```
Did you write a check in late December that may not have cleared by December 31?
```

If yes, the contribution likely lands on the **next year's** Box 2 (calendar year of receipt by custodian, not year of mailing).

**Action:**

- If the user wants the contribution to count for the original tax year, contact the custodian and ask them to record it as a prior-year contribution. The designation is only possible for a contribution made by April 15 of the year after the tax year (not the extended deadline); custodian policies on changing a designation vary.
- If recharacterization isn't possible, amend Form 8889 to remove the contribution from Line 2; the contribution will count for the next tax year automatically.

---

### Cause 3: Custodian clerical error

**Symptom:** Box 2 differs from the user's records by an amount that doesn't fit timing explanations.

**Diagnosis steps:**

1. Pull custodian's transaction history (online portal usually shows a year's contribution-by-contribution list)
2. Compare each transaction to user's bank records
3. Identify the discrepancy: missing deposit, double-counted deposit, mis-allocated rollover, etc.

**Common custodian errors:**

- **Double-counting** — a rollover deposit was credited as both Box 2 and Box 4
- **Missing deposit** — a transfer in late December wasn't picked up in Box 2
- **Mis-allocation** — a direct contribution was incorrectly tagged as a rollover (so it appeared in Box 4 instead of Box 2, where you'd expect)
- **Wrong account holder** — a contribution to a different person's HSA was credited to this account (rare, but happens with name overlaps)

**Action:** Contact custodian. Provide bank records. Custodian issues **CORRECTED 5498-SA** with corrected boxes; the IRS receives a corrected copy automatically. No 1040-X needed if the custodian's correction matches what was originally reported on Form 8889.

**Timeline:** Custodian turnaround varies. If the user is approaching the refund statute of limitations for an amendment (3 years from filing or 2 years from payment, IRC §6511), don't delay.

---

### Cause 4: W-2 Box 12 code W error

**Symptom:** Form 8889 Line 9 doesn't match W-2 Box 12 code W.

**Diagnosis:**

```
Does your W-2 Box 12 code W amount match the cafeteria plan / employer
contribution figure your employer reported on Form 5498-SA Box 2?
```

If the W-2 figure is wrong, the source of error is usually the employer's payroll system — not the HSA custodian.

**Action:**

- Contact employer payroll and request a corrected Form W-2c
- Once the W-2c is issued, file Form 1040-X with corrected Form 8889 Line 9 reflecting the new W-2 Box 12 code W
- Note: this cascades — corrected Line 9 changes Line 13 (deduction), which changes Schedule 1 Line 13, which changes AGI

---

### Cause 5: Filer error on Form 8889

**Symptom:** None of the above causes apply, and the discrepancy is real.

**Diagnosis:**

The user reported the wrong amount on Form 8889 Line 2 or Line 9. Either:

- Under-reported (claimed less deduction than entitled) → easy fix; refund coming
- Over-reported (claimed more deduction than entitled) → file 1040-X to repay tax + interest
- Excess contribution (contributions for the year > annual limit) → withdraw excess plus earnings by the due date including extensions OR pay 6% excise tax on Form 5329

**Action:** File Form 1040-X with corrected Form 8889. See [filing.md](../filing.md) for the workflow.

---

## Special case: missing 5498-SA

**Symptom:** The user has an HSA but never received a 5498-SA.

**Diagnosis:** Custodians file Form 5498-SA for each person for whom they maintained an HSA during the year, due May 31 (June 1, 2026 for 2025 forms) (2025 Instructions for Forms 1099-SA and 5498-SA):

- If the account was open at year-end, the form is filed even with no contributions (to report the December 31 FMV); the participant may get only a January 31 FMV statement instead of a separate 5498-SA when no contributions or rollovers were made
- If the account was fully distributed during the year and no contributions were made for that year, no 5498-SA is needed

**Action:**

- If the account is open and has a balance: contact custodian; the form may be lost in mail or delivered electronically (check the custodian's online portal)
- If the account was closed mid-year: confirm with custodian that no 5498-SA was required; document the explanation

---

## Special case: two 5498-SAs for one account

**Symptom:** User receives two separate 5498-SAs from the same custodian for the same tax year.

**Diagnosis:** One of two things:

1. **CORRECTED form** — the second one has "CORRECTED" checked at the top. The custodian issued an original, then corrected an error. The corrected form supersedes the original.
2. **Two accounts** — the user actually has two HSAs at the same custodian (e.g., one personal HSA and one inherited HSA). Each gets its own 5498-SA.

**Action:**

- If CORRECTED: reconcile against the corrected version only
- If two accounts: reconcile each separately; sum Box 2 of both for the total contribution comparison

---

## Special case: spouse HSA confusion

**Symptom:** User receives Form 5498-SA addressed to their spouse, or vice versa.

**Diagnosis:** Each spouse must have a separate HSA — the IRS does not allow joint HSAs (IRC §223(d)). On a joint return, each spouse reconciles their own 5498-SA separately and files separate Form 8889s.

**Action:** If addressed to the wrong spouse, contact custodian to verify name and SSN on the account. Do not include another person's HSA on your own Form 8889.
