# Form 8919 — Common Mistakes (Audit-Trip List)

The top 10 mistakes that get Form 8919 filings either rejected by the IRS, audited, or quietly disallowed. Each entry includes the problem, the impact, the fix, and the citation.

---

## Mistake 1: Using Code G Without Filing SS-8

**Problem:** The user files Form 8919 with reason code G but never files Form SS-8.

**Impact:** Code G certifies on column (e) that SS-8 was filed. Without SS-8 on file, the IRS will:

- Disallow the 8919 treatment
- Reassess the income as self-employment, charging full SE tax (15.3% × 0.9235 × wages)
- Add interest from the original due date
- Potentially add an accuracy-related penalty under IRC §6662 (20% of the underpayment)

**Fix:** Always file SS-8 first, then attach Form 8919 with code G to the 1040. Keep the certified mail receipt for SS-8 as proof of filing date.

**Citation:** Form 8919 instructions; IRC §6662(b)(1) (negligence or disregard of rules).

---

## Mistake 2: Double-Reporting Misclassified Income on Schedule C

**Problem:** The user puts the same 1099-NEC amount on both Form 8919 (Line 1 column f) and on Schedule C as gross receipts. Often this happens because tax software auto-imports 1099s and the user forgets to delete the duplicate.

**Impact:** The IRS sees double the actual income. The user overpays income tax on the duplicate, and may also owe SE tax on the duplicate via Schedule SE. The CP2000 mismatch process will eventually catch this and trigger a notice.

**Fix:** When using Form 8919 for a 1099-NEC, **delete that 1099 from Schedule C entirely**. Manually verify in tax software that the misclassified 1099 appears on Form 8919 only.

**Citation:** Form 8919 instructions; IRC §61 (gross income — counted once).

---

## Mistake 3: Putting the SS-8 Filing in the Wrong Tax Year

**Problem:** The user files SS-8 in March 2027 (citing tax year 2026) but then accidentally cites the SS-8 filing on a Form 8919 attached to their 2025 1040 (or vice versa).

**Impact:** Mismatched years create an audit flag. The IRS expects SS-8 and the 8919 for the same year to align.

**Fix:** SS-8 should reference the same tax year(s) as the Form 8919 filings that rely on it. If the misclassification spans multiple years, the SS-8 can list multiple years; the 8919 for each year still cites the same SS-8.

**Citation:** Form SS-8 instructions; Form 8919 column (d) instruction.

---

## Mistake 4: Treating Net Income as Wages on Line 1 Column (f)

**Problem:** The user subtracts business expenses from the 1099-NEC amount before entering it in column (f). For example, if the 1099-NEC shows $72,000 and the user spent $5,000 on supplies, they enter $67,000.

**Impact:** Form 8919 treats the income as **wages**, not as net self-employment profit. Wages are not netted against expenses. Entering net income understates the wage base, which may trigger CP2000 mismatch with the 1099-NEC and underpay FICA.

**Fix:** Enter the **gross** 1099-NEC Box 1 amount in column (f). Do not subtract any expenses. (If the user wants to deduct legitimate business expenses, they need to be on Schedule C — but that means the income isn't 8919-eligible.)

**Citation:** Form 8919 column (f) instruction; IRC §3121 (FICA wage definition).

---

## Mistake 5: Forgetting Form 1040 Line 1g

**Problem:** The user fills out Form 8919 perfectly, routes the FICA tax to Schedule 2 Line 5, but forgets to add the wage amount to Form 1040 Line 1g.

**Impact:** Income tax is computed on a smaller base than the IRS expects. The IRS matches 1099-NECs to your return; not seeing the 1099 on Schedule C and not seeing it on Line 1g, the IRS issues a CP2000 adding the missing income plus tax plus interest.

**Fix:** Always make **two** entries when using Form 8919:

1. Wages on Form 1040 Line 1g (= Form 8919 Line 2)
2. FICA on Schedule 2 Line 5 (= Form 8919 Line 11)

If using tax software, verify both entries are present after the 8919 interview completes.

**Citation:** Form 1040 Line 1g instruction; Schedule 2 Line 5 instruction.

---

## Mistake 6: Ignoring the Social Security Wage Base Interaction

**Problem:** A user with significant W-2 income also files Form 8919 for misclassified work. They compute SS tax on the full 8919 wage amount without checking whether the W-2 wages already exceeded the wage base.

**Impact:** Overpayment of Social Security tax. The wage base cap (e.g., $176,100 in 2025) applies to **combined** wages from W-2 + 8919. If W-2 wages alone are at the cap, no additional SS tax via 8919.

**Fix:** Compute Lines 3-6 carefully:

- Line 4 = Line 2 + W-2 Box 3 + W-2 Box 7 + RRTA
- Line 5 = MAX(0, Line 3 − Line 4)
- Line 6 = MIN(Line 2, Line 5)

If Line 5 = 0, no SS via 8919 (Line 7 = 0). Medicare still applies in full on Line 9.

**Citation:** Form 8919 instructions, Lines 3-7; IRC §3121(a)(1) (SS wage base).

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

**Impact:** Lost refunds. IRC §6511 allows refund claims for **3 years from original filing date** (or 2 years from tax payment, whichever is later). Each prior year that's still open represents potential refund of the 7.65% tax difference (full SE tax minus FICA).

**Fix:** When discovering misclassification:

1. Calculate which years are still open under the 3-year statute
2. File Form 1040-X with Form 8919 attached for each open year
3. Include a copy of the SS-8 filing or determination

For Ana's $72,000 example, each prior year amendment recovers ~$4,665 in tax (the SE tax vs FICA difference). Over 3 open years that's ~$14,000.

**Citation:** IRC §6511; Form 1040-X instructions.

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

**Citation:** State-specific (varies); CA Labor Code §2775 (ABC test); IRS PMTA on state tax conformity.

---

## Summary Table

| # | Mistake | Severity | Fix Time |
|---|---------|----------|----------|
| 1 | Code G without SS-8 | High | Mail SS-8 immediately |
| 2 | Double-report on Schedule C | High | Delete from Schedule C |
| 3 | Wrong tax year on SS-8 | Medium | Match years on form |
| 4 | Net income on Line 1(f) | Medium | Use gross 1099 amount |
| 5 | Forgetting 1040 Line 1g | High | Check both routings |
| 6 | Ignoring wage base interaction | Medium | Recompute Lines 3-6 |
| 7 | 8919 for genuine SE income | Critical (fraud) | Apply common-law test |
| 8 | Not amending prior years | Medium (lost refund) | File 1040-X within 3 years |
| 9 | No documentation | High (audit defense) | Gather and preserve |
| 10 | Ignoring state tax | Medium | Consult state pro |
