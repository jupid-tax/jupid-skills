# Form 5498-SA — Common Reconciliation Mistakes

Top mistakes account holders make when handling Form 5498-SA, with examples and fixes.

---

## Mistake #1: Throwing the form away without reading it

**The error:** Form 5498-SA arrives in late May, looks like junk mail from the HSA custodian, and goes straight in the recycling.

**Why it happens:** Form 8889 was filed in April. By May, the user has moved on. The 5498-SA looks redundant.

**Impact:** If the form contains different numbers than what was reported on Form 8889, the IRS notices. The CP2000 notice arrives 12-18 months later proposing additional tax, interest, and penalties on the discrepancy.

**Fix:**

- When 5498-SA arrives in May, spend 10 minutes reconciling it against the filed Form 8889 and W-2 Box 12 code W
- File the form with that year's tax records (paper or digital folder, organized by tax year)
- Set a calendar reminder for late May each year to do this reconciliation

**Citation:** IRC §6501 (statute of limitations for assessment); Pub 17 (recordkeeping recommendations).

---

## Mistake #2: Treating Box 2 as the Form 8889 Line 2 number

**The error:** Filer sees Box 2 = $8,550 and copies it directly to Form 8889 Line 2, claiming an $8,550 deduction.

**Why it happens:** Box 2 is the "total contributions" number. Filers assume it's the deductible amount.

**Impact:** Box 2 includes employer + cafeteria plan contributions that already came out pre-tax on the W-2. Putting them on Line 2 (direct contributions) double-counts the deduction. The IRS catches this through Form W-2 cross-check and issues a CP2000.

**Fix:**

```
Form 8889 Line 2 = Form 5498-SA Box 2 − W-2 Box 12 code W
```

Line 2 reports only contributions made directly (outside payroll). Cafeteria plan and employer-only contributions go on Line 9.

**Citation:** Form 8889 instructions, "Line 2" definition; IRC §223(b).

---

## Mistake #3: Confusing Form 5498-SA with Form 1099-SA

**The error:** Filer receives both forms (1099-SA in January, 5498-SA in May) and conflates them. They report 1099-SA distributions on the wrong section of Form 8889 (or report 5498-SA contributions as distributions).

**Why it happens:** Both forms have "SA" in the name and come from the same custodian. The casual reader assumes they cover the same activity.

**Impact:** Either contributions or distributions are misreported, triggering IRS notices. Distribution-as-contribution errors can also trigger excess-contribution penalties.

**Fix:**

- **1099-SA = distributions OUT** (money leaving the HSA) → Form 8889 Part II (Lines 14a, 14b, 14c, 15, 16, 17a, 17b)
- **5498-SA = contributions IN** (money entering the HSA) → reconcile against Form 8889 Part I (Lines 2, 9)

Different forms, different roles, different parts of Form 8889.

**Citation:** IRS Instructions for Forms 1099-SA and 5498-SA; Form 8889 instructions.

---

## Mistake #4: Missing the prior-year contribution split across two 5498-SAs

**The error:** Filer made a $1,500 contribution in March 2026 for tax year 2025. They reconcile only against the **2025** 5498-SA, see only $4,300 in Box 2 (the 2025 calendar-year contributions), and panic that the $1,500 is missing.

**Why it happens:** The prior-year-designated contribution lands on the **2026** 5498-SA Box 3 (which won't arrive until May 2027), not the 2025 form.

**Impact:** Wasted hours arguing with the custodian about a contribution that is properly recorded — just on a different year's form. Sometimes filers preemptively amend Form 8889 to remove the "missing" contribution, then have to re-amend when they realize their mistake.

**Fix:**

- For any prior-year-designated contribution, **pull both years' 5498-SAs**:
  - The current tax year's 5498-SA → check Box 2
  - The next year's 5498-SA → check Box 3 for the prior-year designation
- Sum (current Box 2) + (next year Box 3) = total contributions for the tax year

**Citation:** Instructions for Forms 1099-SA and 5498-SA, "Box 3" definition.

---

## Mistake #5: Ignoring Box 5 (year-end fair market value)

**The error:** Filer ignores Box 5 because it doesn't flow to any Form 8889 line.

**Why it happens:** Most HSA tutorials focus on contributions and distributions. Box 5 is informational, so it gets glossed over.

**Impact:** Two issues:

1. The IRS uses Box 5 to flag potential excess contributions and untracked rollovers. If Box 5 grows by far more than (Box 2 + Box 4 + plausible market growth), the IRS may issue a query. Without tracking Box 5, you won't notice until the query arrives.
2. You lose track of the HSA as an asset for net-worth, estate, mortgage-application, and long-horizon planning purposes.

**Fix:**

- Record Box 5 each year alongside Box 2 and Box 4
- Build a multi-year HSA growth table: Year, Beginning balance (prior year Box 5), Contributions (Box 2), Rollovers (Box 4), Distributions (1099-SA), Ending balance (Box 5)
- Reconcile growth: Ending balance − Beginning balance = Contributions + Rollovers − Distributions + Investment growth/loss

**Citation:** IRC §223(h); Instructions for Forms 1099-SA and 5498-SA, "Box 5" definition.

---

## Mistake #6: Reconciling without W-2 Box 12 code W

**The error:** Filer tries to reconcile 5498-SA Box 2 against Form 8889 without consulting their W-2.

**Why it happens:** They figure 5498-SA and Form 8889 should match directly.

**Impact:** Reconciliation fails because Box 2 includes the employer + cafeteria portion that the W-2 captures separately. The filer either thinks there's a mismatch when there isn't, or fails to spot a mismatch because they're not comparing the right pairs.

**Fix:**

The full reconciliation requires three sources:

1. **Form 5498-SA Box 2** — total contributions received by custodian
2. **W-2 Box 12 code W** — employer + cafeteria plan contributions (which equals Form 8889 Line 9)
3. **Form 8889 Line 2** — direct contributions

Then: Box 2 − W-2 Box 12 W = Form 8889 Line 2 (should match exactly).

**Citation:** Form W-2 Box 12 codes; Instructions for Form 8889.

---

## Mistake #7: Filing Form 1040-X for a custodian-correctable error

**The error:** Filer notices a discrepancy, panics, and immediately files Form 1040-X to "fix" it. But the error was a custodian clerical error, not a filer error.

**Why it happens:** The 1040-X process is more familiar than the "request CORRECTED 5498-SA from custodian" process.

**Impact:** Filer pays tax preparer fees or wastes time on an unnecessary amendment. Once the custodian issues a CORRECTED 5498-SA, the IRS receives it directly — no 1040-X needed if the original Form 8889 was correct.

**Fix:**

Diagnosis order before amending:

1. Pull custodian's transaction history and compare against bank records
2. If custodian made the error → request CORRECTED 5498-SA; no 1040-X needed
3. If filer made the error → file Form 1040-X with corrected Form 8889
4. If timing-related (prior-year designation, December check) → no error, no amendment

**Citation:** Instructions for Form 1040-X; IRS Publication 17.

---

## Mistake #8: Missing CORRECTED 5498-SA

**The error:** Filer receives a CORRECTED Form 5498-SA after they've already filed Form 8889. They file the corrected form away without reconciling it against what they reported.

**Why it happens:** "I already filed; this must just be paperwork."

**Impact:** If the corrected figures change the deduction (Line 13), the original Form 8889 is now wrong. The IRS has the corrected figures (the custodian sent them too) and will issue a CP2000 if the discrepancy isn't resolved.

**Fix:**

- Treat any CORRECTED 5498-SA as a trigger event: re-run the reconciliation immediately
- If the corrected figures change Form 8889, file Form 1040-X
- If the corrected figures don't change Form 8889 (e.g., a Box 5 correction with no Box 2 change), file the corrected form with records and move on

**Citation:** General instructions for Form 5498-SA; Form 1040-X instructions.

---

## Mistake #9: Treating spouse's 5498-SA as your own

**The error:** Filer receives a 5498-SA addressed to their spouse and includes it on their own Form 8889.

**Why it happens:** Joint return mentality — "we file together, so we can pool HSAs."

**Impact:** HSAs are individual accounts under IRC §223(d). Each spouse files their own Form 8889 (or skips it if no contributions and no distributions). Including a spouse's HSA on your form creates a contribution-limit miscalculation and possibly double-counts a deduction (if both spouses claim the same dollars).

**Fix:**

- Each spouse reconciles their own 5498-SA against their own Form 8889
- On a joint return, each spouse files a separate Form 8889; they are not consolidated
- If the family contribution limit is split between two spousal HSAs, each spouse reports their own portion on their own Form 8889 Line 2 + Line 9

**Citation:** IRC §223(d); Form 8889 instructions, "Joint returns" section.

---

## Mistake #10: Letting an excess contribution sit

**The error:** Reconciliation reveals Box 2 > annual contribution limit. Filer files Form 5329 to pay the 6% excise tax and forgets about it. Next year, the excess is still in the HSA, and the 6% applies again. And again.

**Why it happens:** Filers think the 6% excise tax is a one-time penalty.

**Impact:** The 6% excise tax applies **every year** the excess remains in the HSA. A $1,000 excess contribution costs $60/year forever (until withdrawn). Over 20 years, the cumulative cost exceeds the original excess.

**Fix:**

- Withdraw the excess contribution **plus earnings** before the extended filing deadline (October 15 if the user filed for an extension)
- The earnings come out as taxable income for the year of the excess (not the year withdrawn) — but the 6% excise tax disappears
- If the deadline has passed: the excess can still be withdrawn later (paying ordinary income tax on the earnings) but the 6% applies for every year it remained in the HSA

**Citation:** IRC §4973; Form 5329 instructions; Pub 969.
