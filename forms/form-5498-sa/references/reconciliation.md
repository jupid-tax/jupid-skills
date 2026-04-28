# Form 5498-SA Reconciliation — Diagnosis Tree

When the reconciliation between Form 5498-SA and Form 8889 fails, this diagnosis tree walks through the most common causes in order of frequency.

---

## The reconciliation formula

```
Form 8889 Line 2 (direct) + Form 8889 Line 9 (employer/cafeteria)
  =
Form 5498-SA Box 2 (current year's form)
  + Box 3 from next year's 5498-SA (prior-year-designated contributions made Jan–Apr after tax year)
  − Box 3 from current year's 5498-SA (prior-year-designated contributions made for the prior tax year, already counted on prior year's Form 8889)
```

In most cases, only the first term on the right side matters. The Box 3 corrections apply only when the filer made prior-year-designated contributions.

---

## When the formula fails — diagnosis order

### Cause 1 (most common): Prior-year contribution timing

**Symptom:** The user reports an amount on Form 8889 Line 2 that is higher than 5498-SA Box 2 by exactly the amount of a contribution they remember making in January, February, or March.

**Diagnosis:**

```
Did you make a contribution between January 1 and April 15 of the year following the tax year,
and tell the custodian it was for the prior tax year?
```

If yes, that contribution lands on the **next year's** 5498-SA Box 3, not the current year's Box 2. Pull the next year's 5498-SA (which will arrive in May of the following year) to confirm.

**Action:** Wait for the next year's 5498-SA. When it arrives, verify Box 3 contains the prior-year designation. No amendment needed — Form 8889 was correct.

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

- If the user wants the contribution to count for the original tax year, contact the custodian and ask them to recharacterize it as a prior-year contribution. This must be done before April 15 of the year after the tax year (or the extended deadline).
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

**Timeline:** Custodian corrections typically take 2-6 weeks. If the user is approaching the statute of limitations on Form 8889 amendment (3 years from filing), don't delay.

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
- Excess contribution (Box 2 > annual limit) → withdraw excess plus earnings before extended deadline OR pay 6% excise tax on Form 5329

**Action:** File Form 1040-X with corrected Form 8889. See [filing.md](../filing.md) for the workflow.

---

## Special case: missing 5498-SA

**Symptom:** The user has an HSA but never received a 5498-SA.

**Diagnosis:** Custodians are required to issue Form 5498-SA by May 31 if:

- The account had a balance on December 31 (regardless of contribution activity), OR
- Contributions were made during the tax year, OR
- A rollover or qualified HSA funding distribution occurred

If none of those apply (e.g., account closed mid-year with $0 balance and no contributions), no 5498-SA is required.

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
