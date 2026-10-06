# Form 8919 — Common Mistakes (Audit-Trip List)

The top 10 mistakes that get Form 8919 filings either rejected by the IRS, audited, or quietly disallowed. Each entry includes the problem, the impact, the fix, and the citation.

---

## Mistake 1: Using Code G Without Filing SS-8

**Problem:** The user files Form 8919 with reason code G but never files Form SS-8.

**Impact:** Code G states "I filed Form SS-8 with the IRS and haven't received a reply," and the form requires Form SS-8 to be filed on or before the date the return is filed. (Column (e) is a different check: whether a 1099-MISC/NEC was received.) Without SS-8 on file, the IRS can:

- Disallow the 8919 treatment
- Reassess the income as self-employment, charging full SE tax (15.3% × 0.9235 × wages)
- Add interest from the original due date
- Potentially add an accuracy-related penalty under IRC §6662 (20% of the underpayment)

**Fix:** File Form SS-8 (mail or fax, separately from the return) on or before the date the return is filed, then file Form 8919 with code G. Keep the fax confirmation or certified mail receipt as proof of the filing date. Even with SS-8 on file, the form warns that if the IRS doesn't agree the worker is an employee, the worker may be billed for the additional tax, penalties, and interest.

**Citation:** 2025 Form 8919, page 1 (reason code G) and page 2 (column (c) caution); IRC §6662(b)(1) (negligence or disregard of rules).

---

## Mistake 2: Double-Reporting Misclassified Income on Schedule C

**Problem:** The user puts the same 1099-NEC amount on both Form 8919 (column (f) of lines 1–5) and on Schedule C as gross receipts. Often this happens because tax software auto-imports 1099s and the user forgets to delete the duplicate.

**Impact:** The IRS sees double the actual income. The user overpays income tax on the duplicate, and may also owe SE tax on the duplicate via Schedule SE. The CP2000 mismatch process will eventually catch this and trigger a notice.

**Fix:** When using Form 8919 for a 1099-NEC, **delete that 1099 from Schedule C entirely**. Manually verify in tax software that the misclassified 1099 appears on Form 8919 only.

**Citation:** Form 8919 instructions; IRC §61 (gross income — counted once).

---

## Mistake 3: Putting the SS-8 Filing in the Wrong Tax Year

**Problem:** The user files SS-8 in March 2027 (citing tax year 2026) but then accidentally cites the SS-8 filing on a Form 8919 attached to their 2025 1040 (or vice versa).

**Impact:** Mismatched years create an audit flag. The IRS expects SS-8 and the 8919 for the same year to align.

**Fix:** SS-8 should reference the same tax year(s) as the Form 8919 filings that rely on it. Part I, line 1 of Form SS-8 asks for all the years services were provided, so one SS-8 can cover several years for the same firm; the 8919 for each year relies on the same SS-8. A determination can only be made for years with open statutes.

**Citation:** Instructions for Form SS-8 (Rev. January 2024), "Part I, line 1" and "When To File".

---

## Mistake 4: Treating Net Income as Wages in Column (f)

**Problem:** The user subtracts business expenses from the 1099-NEC amount before entering it in column (f). For example, if the 1099-NEC shows $72,000 and the user spent $5,000 on supplies, they enter $67,000.

**Impact:** Form 8919 treats the income as **wages**, not as net self-employment profit. Wages are not netted against expenses. Entering net income understates wages, which may trigger a CP2000 mismatch with the 1099-NEC and underpays the tax on lines 11 and 12.

**Fix:** Enter the **gross** 1099-NEC Box 1 amount in column (f). Do not subtract any expenses. (If the user wants to deduct legitimate business expenses, they need to be on Schedule C — but that means the income isn't 8919-eligible.)

**Citation:** Form 8919 column (f) instruction; IRC §3121 (FICA wage definition).

---

## Mistake 5: Forgetting Form 1040 Line 1g

**Problem:** The user fills out Form 8919, routes the tax to Schedule 2 line 6, but forgets to add the wage amount to Form 1040 line 1g.

**Impact:** Income tax is computed on a smaller base than the IRS expects. The IRS matches 1099-NECs to your return; not seeing the 1099 on Schedule C and not seeing it on Line 1g, the IRS issues a CP2000 adding the missing income plus tax plus interest.

**Fix:** Always make **two** entries when using Form 8919:

1. Wages on Form 1040 line 1g (= Form 8919 line 6)
2. Tax on Schedule 2 line 6 (= Form 8919 line 13)

If using tax software, verify both entries are present after the 8919 interview completes. Schedule 2 line 5 belongs to Form 4137 (unreported tips), not Form 8919.

**Citation:** 2025 Form 8919 lines 6 and 13; 2025 Form 1040 line 1g ("Wages from Form 8919, line 6"); 2025 Schedule 2 line 6.

---

## Mistake 6: Ignoring the Social Security Wage Base Interaction

**Problem:** A user with significant W-2 income also files Form 8919 for misclassified work. They compute SS tax on the full 8919 wage amount without checking whether the W-2 wages already exceeded the wage base.

**Impact:** Overpayment of Social Security tax. The wage base ($176,100 for 2025, $184,500 for 2026) applies to **combined** wages from W-2 + 8919. If W-2 wages alone are at the cap, no additional SS tax via 8919.

**Fix:** Compute lines 7–10 exactly as the form does:

- Line 8 = W-2 Box 3 + W-2 Box 7 + RRTA (not more than line 7) + Form 4137 line 10. **Do not add the Form 8919 wages to line 8**; adding them double-counts and shrinks line 9.
- Line 9 = MAX(0, Line 7 − Line 8)
- Line 10 = MIN(Line 6, Line 9)

If line 9 = 0, no SS via 8919 (line 11 = 0). Medicare still applies in full on line 12 (line 6 × 1.45%).

**Citation:** 2025 Form 8919 lines 7–12 and page 2 "Line 8"; IRC §3121(a)(1) (SS wage base); SSA https://www.ssa.gov/oact/cola/cbb.html.

---

## Mistake 7: Filing 8919 for Genuinely Self-Employed Income

**Problem:** A freelancer with multiple clients, set their own hours, and use their own equipment files Form 8919 to lower the tax bill on their consulting income.

**Impact:** This is tax fraud. The IRS audits, reclassifies the income as self-employment, assesses SE tax + interest + accuracy penalty under IRC §6662 (20%). In egregious cases, civil fraud penalty under IRC §6663 (75%) or criminal penalty under IRC §7201.

**Fix:** Apply the common-law test honestly (`references/common-law-test.md`). Genuine self-employment indicators:

- Multiple clients (more than 2 active)
- Worker sets own hours
- Worker uses own equipment
- Worker bears profit/loss risk
- Worker advertises services to public

Two or three of those = self-employment, file Schedule SE.

**Citation:** IRC §6662, §6663, §7201; Rev. Rul. 87-41.

---

## Mistake 8: Not Filing for Prior Years Within Statute of Limitations

**Problem:** The user discovers in 2027 that they were misclassified in 2022, 2023, 2024, 2025, and 2026. They file Form 8919 for 2026 only and assume the prior years are out of reach.

**Impact:** Lost refunds. IRC §6511 allows refund claims for **3 years from original filing date** (or 2 years from tax payment, whichever is later). Each prior year that's still open represents a potential refund of the difference between the SE tax paid and the employee-share tax on Form 8919, reduced by the income tax effect of losing the half-SE-tax deduction and any QBI deduction on that income. Filing Form SS-8 does not stop the refund period from running; the SS-8 instructions tell workers to file a protective Form 1040-X to keep it open.

**Fix:** When discovering misclassification:

1. Calculate which years are still open under the 3-year statute
2. File Form 1040-X with Form 8919 attached for each open year
3. If the SS-8 determination is still pending, file a protective claim instead: Form 1040-X marked "Protective Claim" with the statement the SS-8 instructions prescribe

For Ana's $72,000 example (2026 figures), the SE tax vs. Form 8919 tax difference is $4,665 a year, but the net federal difference after the lost half-SE-tax and QBI deductions is about $2,285 a year (see `examples/ana-misclassified-accountant.md`). Each amended year is computed with that year's own rates and wage base.

**Citation:** IRC §6511; Instructions for Form SS-8 (Rev. January 2024), "Time for filing a claim for refund" and "Protecting your statute of limitations"; Form 1040-X instructions.

---

## Mistake 9: Filing Form 8919 Without Documentation

**Problem:** The user has a feeling they're misclassified but no documentation — no contract, no email trail showing direction, no time records, no evidence of supervision. They file 8919 anyway.

**Impact:** If the IRS audits or the firm contests the SS-8, the user has no defense. The classification dispute defaults to the IRS's interpretation of the facts, which without documentation often means the worker is deemed a contractor.

**Fix:** Before filing 8919, gather and preserve:

- All 1099 forms
- Contract or engagement letter
- Email exchanges showing direction (hours, methods, supervision)
- Time records or timesheets if any
- Records of equipment provided by the firm
- Notes on supervision, performance reviews, training
- Any HR-style communications

Retain documentation for at least 3 years from filing the 1040 (longer if audit risk is elevated).

**Citation:** Treasury Regulation §1.6001-1 (recordkeeping); Rev. Rul. 87-41 (factors require evidence).

---

## Mistake 10: Mishandling State Tax Implications

**Problem:** The user files Form 8919 for federal purposes but ignores state tax. If the state follows federal classification, the income is also "wages" for state tax — but the user files as self-employment for state, creating mismatch.

**Impact:** State tax notice; underpayment of state employment-related taxes (SDI, paid family leave, etc.); potential state audit.

**Fix:** Check whether the user's state follows federal classification:

- **CA, NY, IL** — generally follow federal; if 8919 federal, treat as wages for state too
- **CA's ABC test (AB-5)** — even stricter than federal; many federal contractors are CA employees
- **TX, FL, NV** — no state income tax, so income tax mismatch not an issue, but unemployment insurance may be

The agent should flag state implications and advise consulting a state tax professional before filing.

**Citation:** State-specific (varies); CA Labor Code §2775 (ABC test).

---

## Summary Table

| # | Mistake | Severity | Fix Time |
|---|---------|----------|----------|
| 1 | Code G without SS-8 | High | Mail SS-8 immediately |
| 2 | Double-report on Schedule C | High | Delete from Schedule C |
| 3 | Wrong tax year on SS-8 | Medium | Match years on form |
| 4 | Net income in column (f) | Medium | Use gross 1099 amount |
| 5 | Forgetting 1040 line 1g | High | Check both routings |
| 6 | Ignoring wage base interaction | Medium | Recompute lines 7–10 |
| 7 | 8919 for genuine SE income | Critical (fraud) | Apply common-law test |
| 8 | Not amending prior years | Medium (lost refund) | File 1040-X within 3 years |
| 9 | No documentation | High (audit defense) | Gather and preserve |
| 10 | Ignoring state tax | Medium | Consult state pro |
