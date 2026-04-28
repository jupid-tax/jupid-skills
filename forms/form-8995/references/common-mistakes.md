# Form 8995 — Common Mistakes

Audit-trip mistakes that surface in IRS notices, Form 8995 filings reviewed by Jupid, and the §199A regulations. Each entry has the problem, the impact, and the fix.

---

## Mistake 1: Using Schedule C net profit as QBI without §199A adjustments

**Problem:** Filer enters Schedule C Line 31 ($50,000) directly as Column (iii) on Form 8995 Line 1a, without subtracting ½ SE tax, SE health insurance, and SE retirement.

**Impact:** Overstated QBI by 7-15% typically, leading to overstated deduction. IRS notice CP2000 if the IRS computer cross-checks Schedule SE and Schedule 1 against the Form 8995 QBI figure.

**Fix:** QBI = Schedule C Line 31 − ½ SE tax (Schedule SE Line 13) − SE health insurance (Schedule 1 Line 17) − SE retirement (Schedule 1 Line 16). Authority: Treas. Reg. §1.199A-3(b)(1)(vi).

---

## Mistake 2: Filing Form 8995 instead of Form 8995-A

**Problem:** Taxable income before QBI exceeds the threshold ($241,950 single / $483,900 MFJ for 2025), but the filer uses Form 8995 anyway because it's simpler.

**Impact:** Wrong form. E-file rejection or IRS notice. Above the threshold, W-2 wage and UBIA limits apply, plus SSTB phase-out — the simplified form does not capture these.

**Fix:** Compute taxable income before QBI. If above threshold or in the phase-in range ($75K above for single, $100K above for MFJ), switch to Form 8995-A. If exactly at threshold, Form 8995 is allowed.

---

## Mistake 3: Skipping Form 8995 entirely

**Problem:** Filer with QBI sources (Schedule C, K-1, REIT, PTP) leaves Form 1040 Line 13 blank because they don't realize they qualify or think the form is "too complicated."

**Impact:** Forfeits 20% deduction worth potentially thousands of dollars. The IRS does not auto-compute QBI and add it for the taxpayer.

**Fix:** If any pass-through income exists, file Form 8995 (or 8995-A above threshold). Below the threshold, the form takes 10-15 minutes once Schedule C and Schedule 1 are complete.

---

## Mistake 4: Including non-§199A income on Lines 1 or 5

**Problem:** Filer puts on Line 1 column (iii):
- Wages from W-2 work (not QBI)
- Capital gains from stock sales (not QBI)
- Ordinary dividends not designated as §199A (not QBI)
- Investment interest income (not QBI)
- Guaranteed payments from a partnership (not QBI per §199A(c)(4))

Or on Line 5:
- 1099-DIV Box 1a total dividends (instead of Box 5 §199A dividends)
- REIT capital gain distributions (Box 2a)

**Impact:** Overstated deduction. If the IRS cross-checks W-2 / 1099 totals against the QBI figure, an audit follows.

**Fix:** Only include income from a qualified trade or business as defined in §199A. Wage income, investment capital gain, non-§199A dividends, and guaranteed payments are excluded. Use 1099-DIV Box 5 specifically for REIT §199A dividends.

---

## Mistake 5: Forgetting to subtract net capital gain on Line 14

**Problem:** Filer enters $0 on Line 14 even though Form 1040 Line 3a (qualified dividends) or Schedule D Line 16 (net long-term capital gain) is positive.

**Impact:** Overstated Line 15 → overstated 20% taxable income limit on Line 16 → potential overstated final deduction on Line 17.

**Fix:** Line 14 = Form 1040 Line 3a (qualified dividends) + Schedule D Line 16 (net LTCG, if Schedule D is required). Even small qualified dividend amounts must be included. The §199A deduction excludes capital gain because Congress did not want to compound preferential rates.

---

## Mistake 6: Misreading partnership/S-corp K-1 Section 199A statement

**Problem:** Filer uses Box 1 (ordinary business income) of the K-1 instead of the Section 199A QBI figure in the attached statement (Box 20 code Z for partnership, Box 17 code V for S-corp).

**Impact:** Box 1 typically includes amounts that don't qualify for §199A (guaranteed payments, interest, etc.). Using Box 1 overstates QBI.

**Fix:** Use the QBI figure from the Section 199A statement, not Box 1. If the K-1 has "STMT" but no attached statement, request a corrected K-1.

---

## Mistake 7: Computing Line 13 (taxable income before QBI) wrong

**Problem:** Filer enters their AGI (Form 1040 Line 11) on Line 13 of Form 8995 instead of taxable income.

**Impact:** Overstated income limit on Line 16 → potentially overstated final deduction.

**Fix:** Line 13 is taxable income, not AGI. Practical formula: Line 13 = Form 1040 Line 15 + Form 1040 Line 13 (the QBI deduction itself). Or: AGI − standard or itemized deductions, before subtracting QBI.

---

## Mistake 8: Forgetting prior-year QBI loss carryforward

**Problem:** Filer had a Schedule C loss in the prior year that pushed Line 2 (prior year) to negative, generating a carryforward. They forget to enter the carryforward on this year's Line 3.

**Impact:** Misses the offset, claiming higher current-year QBI deduction than they're entitled to. Eventually reconciled by the IRS, with interest.

**Fix:** Check last year's Form 8995 Line 16 (or 8995-A equivalent). If negative, that's the carryforward — enter as a negative on this year's Line 3.

---

## Mistake 9: Treating SSTB status as relevant below threshold

**Problem:** Filer is in a specified service trade or business (SSTB — health, law, accounting, financial services, etc.) and below the threshold but still tries to apply phase-out logic.

**Impact:** Wastes time. Below the threshold, SSTB status is irrelevant — the full 20% deduction applies regardless. Phase-out only matters above the threshold.

**Fix:** Below the threshold, ignore SSTB status. Above the threshold, switch to Form 8995-A and apply phase-out per §199A(d)(3) and Treas. Reg. §1.199A-5.

---

## Mistake 10: Using Form 8995 when filer is a co-op patron

**Problem:** Patron of an agricultural or horticultural cooperative files Form 8995 because their income is below the threshold.

**Impact:** Wrong form. Co-op patrons must use Form 8995-A regardless of income to apply the §199A(g) cooperative reduction.

**Fix:** Switch to Form 8995-A. The form has additional schedules for the co-op patron computation.

---

## Mistake 11: Including rental income that doesn't qualify as a trade or business

**Problem:** Filer with passive rental income (single rental property, 50 hours/year of management) includes the net rental income as QBI on Line 1.

**Impact:** Most passive rentals don't meet the §162 trade-or-business standard or the §199A safe harbor (Notice 2019-7 — 250+ hours, separate books, contemporaneous records). Including non-qualifying rental income overstates QBI.

**Fix:** Apply the §199A safe harbor or §162 trade-or-business analysis. If neither is met, exclude the rental from QBI. Document the analysis in workpapers.

---

## Mistake 12: Aggregating without filing the §1.199A-4 election

**Problem:** Filer treats two related trades or businesses as a single source on Form 8995 without filing the aggregation election statement required by Treas. Reg. §1.199A-4(c).

**Impact:** Below the threshold, aggregation has no math impact (so the IRS rarely catches this). Above the threshold, aggregation can change the W-2/UBIA limits and an unfiled election can be denied on audit.

**Fix:** Below threshold, just list each trade or business as a separate row on Lines 1a-1e. Don't aggregate informally. Above threshold, formally elect aggregation per §1.199A-4(c) and attach the election statement.

---

## Mistake 13: Ignoring the holding-period rule for REIT dividends

**Problem:** Filer received REIT dividends but bought and sold the REIT shares within the holding period window (45 days during the 91-day period around the ex-dividend date).

**Impact:** The brokerage normally enforces this rule and excludes ineligible dividends from Box 5 of 1099-DIV. But if the filer manages this themselves (e.g., direct REIT purchase outside a brokerage), they must enforce it.

**Fix:** Per §199A(e)(3), only dividends meeting the holding period qualify. If unsure, defer to 1099-DIV Box 5 from the brokerage — they enforce this rule.

---

## Mistake 14: Not reconciling Form 8995 Line 17 with Form 1040 Line 13

**Problem:** Filer fills out Form 8995 but accidentally enters a different figure on Form 1040 Line 13 (e.g., transposes digits, uses Line 16 instead of Line 17).

**Impact:** IRS computer auto-checks. Discrepancy triggers a notice.

**Fix:** Always verify Form 8995 Line 17 = Form 1040 Line 13. If using e-file software, the software auto-links — but spot-check on the final review screen.

---

## Mistake 15: Filing Form 8995 standalone

**Problem:** Filer mails Form 8995 separately from Form 1040, thinking it's its own return.

**Impact:** IRS rejects the standalone form. Possibly Form 1040 was already filed without Form 8995 attached, leaving the QBI deduction unclaimed.

**Fix:** Form 8995 is **always** an attachment to Form 1040. Either e-file Form 1040 with Form 8995 attached (the software handles attachment), or mail Form 1040 + Form 8995 together with all other schedules. Never file Form 8995 alone.
