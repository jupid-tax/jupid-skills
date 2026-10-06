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
Form 8889 Line 2 = (Box 2 − last year's Box 3 + this year's Box 3) − W-2 Box 12 code W − Line 10
```

Line 2 reports only contributions made directly (outside payroll) for the tax year. Cafeteria plan and employer-only contributions go on Line 9; an IRA funding distribution (also in Box 2) goes on Line 10.

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

## Mistake #4: Reading only Box 2 when a prior-year contribution was made

**The error:** Filer made a $1,500 contribution in March 2026 for tax year 2025. They reconcile the **2025** 5498-SA by Box 2 only, see $4,300 (the money received in 2025), and panic that the $1,500 is missing. A year later they compare the 2026 Box 2 to their 2026 Form 8889 and think the custodian over-reported by $1,500.

**Why it happens:** The prior-year-designated contribution appears in **Box 3 of the 2025 form** and again in **Box 2 of the 2026 form** (money received in 2026).

**Impact:** Wasted hours arguing with the custodian about a contribution that is properly recorded. Sometimes filers preemptively amend Form 8889 to remove the "missing" contribution, then have to re-amend when they realize their mistake.

**Fix:**

- Contributions for 2025 = 2025 Box 2 − 2024 Box 3 + 2025 Box 3
- Contributions for 2026 = 2026 Box 2 − 2025 Box 3 + 2026 Box 3

**Citation:** 2025 Instructions for Forms 1099-SA and 5498-SA, Box 2 ("Include any contribution made in 2025 for 2024") and Box 3.

---

## Mistake #5: Ignoring Box 5 (year-end fair market value)

**The error:** Filer ignores Box 5 because it doesn't flow to any Form 8889 line.

**Why it happens:** Most HSA tutorials focus on contributions and distributions. Box 5 is informational, so it gets glossed over.

**Impact:** Two issues:

1. Box 5 is reported to the IRS every year. If Box 5 grows by far more than (Box 2 + Box 4 + plausible market growth − distributions), something was recorded that you did not expect; without tracking Box 5, you won't notice.
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

Then: (Box 2 − last year's Box 3 + this year's Box 3) − W-2 Box 12 W − Form 8889 Line 10 = Form 8889 Line 2 (should match exactly).

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

**Citation:** IRC §223(d); 2025 Instructions for Form 8889, "Name and social security number (SSN)" (separate Form 8889 for each spouse); Pub. 969 ("You can't have a joint HSA").

---

## Mistake #10: Letting an excess contribution sit

**The error:** Reconciliation reveals contributions for the year > annual contribution limit. Filer files Form 5329 to pay the 6% excise tax and forgets about it. Next year, the excess is still in the HSA, and the 6% applies again. And again.

**Why it happens:** Filers think the 6% excise tax is a one-time penalty.

**Impact:** The 6% excise tax applies **every year** the excess remains in the HSA. A $1,000 excess contribution costs $60/year forever (until withdrawn). Over 20 years, the cumulative cost exceeds the original excess.

**Fix:**

- Withdraw the excess contribution **plus earnings** by the due date of the return including extensions (October 15 if the user filed for an extension; a timely filer without an extension has until 6 months after the original due date with an amended return marked "Filed pursuant to section 301.9100-2")
- The earnings are taxable as other income for the year withdrawn — but the 6% excise tax disappears (2025 Instructions for Form 8889, Line 13)
- If the deadline has passed: the 6% applies for every year the excess remained. A later withdrawal is a regular distribution (taxable on Form 8889 Line 16, plus 20% unless an exception applies) that reduces the excess on Form 5329 Line 44; or the excess is absorbed when a later year's contributions are below that year's limit (Form 5329 Line 43)

**Citation:** IRC §4973; Form 5329 instructions; Pub 969.
