# Common Form 982 Mistakes (Audit-Trip List)

The top mistakes the IRS catches on Form 982, with citations and fixes. Use this checklist when reviewing a draft before submission.

---

## 1. Claiming insolvency without doing Worksheet 2

**The error**: User received a 1099-C, feels broke, checks Box 1b on Form 982 with the full canceled amount on Line 2.

**Why wrong**: Insolvency is a TECHNICAL test under §108(d)(3): liabilities > FMV of assets immediately before discharge, including ALL assets (retirement, life insurance cash value, all real estate). Many users with substantial 401(k) balances are technically solvent.

**Fix**: Complete Pub 4681 Worksheet 2 before checking Box 1b. If liabilities ≤ assets, do NOT claim insolvency exclusion.

**Audit trigger**: The IRS routinely asks for the Worksheet 2 supporting calculation in audits of Form 982 with Box 1b. Lack of documentation → exclusion disallowed.

---

## 2. Forgetting retirement accounts in Worksheet 2

**The error**: User excludes 401(k) / IRA balances from "assets" because "I can't touch that money."

**Why wrong**: §108(d)(3) doesn't have a "touchability" test. Retirement accounts are assets at vested FMV. Pub 4681 specifically lists them as included.

**Fix**: Include vested 401(k), IRA, and other retirement balances at FMV. Use the most recent statement date closest to the discharge date.

**Audit trigger**: Tax court has consistently held that retirement accounts must be included (Carlson v. Commissioner, T.C. Memo 2012-76, among others).

---

## 3. Excluding the canceled debt from "liabilities" in Worksheet 2

**The error**: "The debt is being canceled, so I don't include it in my liabilities."

**Why wrong**: §108(d)(3) measures insolvency IMMEDIATELY BEFORE the discharge. At that moment, the debt is still owed.

**Fix**: Include the canceled debt amount in liabilities. Use Box 2 of the 1099-C.

**Audit trigger**: Recomputing Worksheet 2 with the canceled debt INCLUDED often changes the insolvency conclusion.

---

## 4. Checking multiple Box 1 exclusions

**The error**: User checks Box 1a (bankruptcy) AND Box 1b (insolvency) on the same Form 982.

**Why wrong**: §108(a)(2) gives bankruptcy priority over insolvency. If the discharge occurred in a Title 11 case, Box 1a applies and Box 1b doesn't. Multiple boxes confuse the IRS and may trigger rejection.

**Fix**: Check exactly ONE box on Line 1. If multiple discharges in the same year qualify under different exclusions, file SEPARATE Forms 982 (one per exclusion).

**Audit trigger**: E-file may auto-reject; paper filings draw a notice.

---

## 5. Excluding more than the canceled amount

**The error**: User has a 1099-C for $24,000 and enters $30,000 on Form 982 Line 2.

**Why wrong**: Cannot exclude more than was discharged. Line 2 ≤ Box 2 of 1099-C.

**Fix**: Cap Line 2 at the actual canceled amount.

**Audit trigger**: IRS cross-matches 1099-C Box 2 with Form 982 Line 2.

---

## 6. Failing to report the non-excluded portion on Schedule 1 Line 8c

**The error**: User excludes $20,000 of a $30,000 1099-C under insolvency, but doesn't report the remaining $10,000 anywhere.

**Why wrong**: The portion NOT excluded is ordinary income on Schedule 1 Line 8c.

**Fix**: Reconcile: 1099-C Box 2 = Form 982 Line 2 + Schedule 1 Line 8c. Both must add up.

**Audit trigger**: 1099-C amount not fully accounted for → CP2000 notice for unreported income.

---

## 7. Skipping attribute reduction (§108(b))

**The error**: User excludes under bankruptcy or insolvency but doesn't fill in Part II of Form 982.

**Why wrong**: §108(b) MANDATES attribute reduction for these exclusions. The form requires Part II to be completed.

**Fix**: Complete Lines 4-11 totaling Line 2. Track which attributes are reduced and update next year's records.

**Audit trigger**: Empty Part II with non-zero Line 2 (under Box 1a or 1b) → form rejection.

---

## 8. Checking §108(b)(5) election (Line 3) without depreciable property

**The error**: User checks Line 3 to "preserve NOLs" but has no depreciable property.

**Why wrong**: The §108(b)(5) election applies basis reduction to depreciable property. Without depreciable property, the election produces no effect — the default order proceeds anyway.

**Fix**: Don't check Line 3 unless the user has depreciable property worth reducing. The election is irrevocable.

**Audit trigger**: Not always caught by the IRS, but the election can be confusing in records.

---

## 9. Claiming principal residence exclusion in a year it's lapsed

**The error**: User checks Box 1e for a 2026 discharge without verifying the §108(a)(1)(E) exclusion is still in effect.

**Why wrong**: The qualified principal residence exclusion has been extended multiple times by Congress. As of last verification (2026-04-28), it was extended through tax year 2025. For 2026+, verify against the most recent legislation. If the extension has lapsed, Box 1e is unavailable.

**Fix**: Before checking Box 1e, verify the exclusion is in effect for the user's tax year. Look up the latest Pub 4681 or recent legislation.

**Audit trigger**: IRS systems will flag if the exclusion isn't available for the tax year.

---

## 10. Claiming principal residence exclusion for non-qualifying debt

**The error**: User refinanced the home, took cash out for a vacation, and now has the debt forgiven. Tries to use Box 1e.

**Why wrong**: §108(h) defines "qualified principal residence indebtedness" as debt incurred to BUY, BUILD, or substantially IMPROVE the principal residence. Cash-out refinances for non-home purposes are NOT qualified.

**Fix**: Only the qualifying portion (acquisition / improvement) of the debt qualifies. Cash-out for non-home purposes is treated under insolvency or income.

**Audit trigger**: Home equity loans / refinances with cash out commonly draw scrutiny.

---

## 11. Claiming principal residence exclusion for vacation home or rental

**The error**: User had a vacation home foreclosed and tries Box 1e.

**Why wrong**: §108(h)(1) requires the property to be the user's PRINCIPAL residence (the §121 definition applies — used as primary home for 2 of last 5 years).

**Fix**: Vacation homes and rentals don't qualify. Try insolvency (Box 1b) instead. For rentals used in trade/business, QRPBI (Box 1d) may be available.

---

## 12. Forgetting to reduce home basis after Box 1e exclusion

**The error**: User excludes $75K under principal residence indebtedness and forgets to track the basis reduction.

**Why wrong**: §108(h)(1) requires basis reduction in the residence by the excluded amount. This affects the §121 capital gain calculation when the home is later sold.

**Fix**: After excluding under Box 1e, document the basis reduction in the user's home records:
```
Original basis:               $X
Less §108(h) basis reduction: $Y
Adjusted basis:               $X − Y
```
Retain for the future home sale.

**Audit trigger**: When the home is later sold, the IRS will check basis. Failure to reduce → IRS-imposed reduction + interest.

---

## 13. Filing Form 982 when no exclusion applies

**The error**: User received a 1099-C, doesn't qualify for any exclusion, but files Form 982 anyway with hopes of "trying" insolvency.

**Why wrong**: Filing Form 982 without a qualifying exclusion is a misrepresentation. Adds to audit risk.

**Fix**: If no exclusion fits (user is solvent, not in bankruptcy, debt isn't on principal residence), do NOT file Form 982. Report the full 1099-C amount as ordinary income on Schedule 1 Line 8c.

**Audit trigger**: IRS focuses on Form 982 filings as audit candidates.

---

## 14. Bankruptcy exclusion without discharge order

**The error**: User filed for bankruptcy but the case hasn't been discharged yet (still in proceeding) — claims Box 1a anyway.

**Why wrong**: §108(a)(1)(A) requires a discharge by the bankruptcy court. The petition alone doesn't qualify.

**Fix**: Wait for the discharge order before filing Form 982. If the year of discharge differs from the year of debt cancellation, this gets complex — refer to a CPA.

**Audit trigger**: IRS may request the discharge order.

---

## 15. Confusing §108 exclusion with §108(f) student loan exclusion

**The error**: User has a forgiven student loan under PSLF or §108(f)(5). Files Form 982 with Box 1b checked.

**Why wrong**: §108(f) student loan exclusions are AUTOMATIC — generally do NOT require Form 982. Different statutory mechanism.

**Fix**: For §108(f) discharges, simply don't include the amount in income. No Form 982 needed (verify against current Pub 4681).

The temporary §108(f)(5) broad exclusion (American Rescue Plan, 2021-2025) — covered most student loan discharges. Verify current scope.

---

## Final review checklist (before declaring the form ready)

- [ ] Pub 4681 Worksheet 2 completed if Box 1b
- [ ] Retirement accounts and life insurance cash value included as assets (Box 1b)
- [ ] Canceled debt itself included in liabilities (Box 1b, "immediately before")
- [ ] Exactly ONE box checked on Line 1
- [ ] Line 2 ≤ Form 1099-C Box 2
- [ ] Schedule 1 Line 8c = (1099-C Box 2) − (Form 982 Line 2)
- [ ] Lines 4-11 total = Line 2 (if Box 1a or 1b)
- [ ] §108(b)(5) election decision documented (Line 3)
- [ ] Bankruptcy discharge order on file (Box 1a)
- [ ] Principal residence exclusion verified in effect for tax year (Box 1e)
- [ ] Acquisition indebtedness verified (Box 1e)
- [ ] Property is principal residence per §121 test (Box 1e)
- [ ] Home basis reduction recorded for future sale (Box 1e)
- [ ] Reduced NOL / credits / basis tracked for next year's return
- [ ] All supporting documentation retained for at least 3 years
