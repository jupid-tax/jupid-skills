# Form 8995-A — Common Mistakes

Eight high-frequency errors and how to avoid them.

---

## 1. Filing Form 8995 instead of Form 8995-A above the threshold

**Problem:** Tax software defaults to Form 8995 (the simplified version) and the filer doesn't notice they're above the threshold.

**Impact:** The simplified form ignores the W-2/UBIA limit and the SSTB phase-in. Above the threshold, this almost always overstates the deduction. The IRS receives Schedule C / K-1 data, recomputes §199A on its end, and issues a CP2000 notice with the corrected (lower) deduction plus interest.

**Citation:** IRC §199A(b)(2)(B); Treas. Reg. §1.199A-1(d)(2)(iv).

**Fix:** Always check threshold position FIRST. If taxable income before QBI > $241,950 single / $483,900 MFJ for 2025, use Form 8995-A. If the user has any SSTB activity, use 8995-A regardless of income.

---

## 2. Including S-corp owner's reasonable comp in QBI

**Problem:** S-corp K-1 box 1 ordinary income is $300,000. Owner draws $100,000 W-2 from the corp. Filer enters $300,000 + $100,000 = $400,000 as QBI.

**Impact:** Inflated QBI by $100,000 → tentative deduction overstated by $20,000. Audit risk if K-1 box 17 code V is on file.

**Citation:** Treas. Reg. §1.199A-3(b)(2)(ii)(H).

**Fix:** Use box 1 directly (the corp already deducted the owner's W-2 wages as a corporate expense). The $100,000 W-2 is reported on Form 1040 Line 1a separately and counts in the corp's W-2 wages for Part II Line 4.

---

## 3. Forgetting Schedule C SE-tax / SE-HI / SE-retirement adjustments

**Problem:** Sole proprietor with $100,000 Schedule C profit reports $100,000 as QBI without subtracting the deductible portion of SE tax, self-employed health insurance, and SEP-IRA contributions allocable to that business.

**Impact:** QBI overstated by 5-15%. Tentative deduction overstated proportionally.

**Citation:** Treas. Reg. §1.199A-3(b)(1)(vi); IRS QBI FAQ #33.

**Fix:** QBI = Schedule C Line 31 net profit MINUS (½ SE tax + SE HI + SE retirement contributions), all allocable to that business.

---

## 4. Including land or intangibles in UBIA

**Problem:** Real estate investor includes the cost of land in UBIA when applying the 2.5% UBIA limit. Or a software company includes acquired intellectual property.

**Impact:** Inflated UBIA → inflated W-2/UBIA limit → overstated deduction.

**Citation:** Treas. Reg. §1.199A-2(c)(1)(iii) — only depreciable tangible property within its depreciable period; land excluded.

**Fix:** UBIA = unadjusted basis of depreciable tangible property (buildings yes, land no; equipment yes, intangibles no) within its depreciable period. The depreciable period is the longer of 10 years or the MACRS recovery period.

---

## 5. Skipping the Net Capital Gains Cap (Part IV Line 36)

**Problem:** Filer with $400,000 taxable income before QBI and $300,000 of long-term capital gains computes the overall cap as 20% × $400,000 = $80,000. Should be 20% × ($400,000 − $300,000) = $20,000.

**Impact:** Overstated deduction by up to $60,000 in this example.

**Citation:** IRC §199A(a)(1)(B); Treas. Reg. §1.199A-1(c)(1).

**Fix:** Always subtract net capital gains (LTCG from Schedule D + qualified dividends from 1040 Line 3a) on Line 34 before applying the 20% cap on Line 36.

---

## 6. Misclassifying a Business as Non-SSTB When It Is

**Problem:** A solo financial planner treats their advisory practice as non-SSTB ("I'm a registered investment advisor, not really 'financial services'"). At $260,000 taxable income, they take the full deduction without Schedule A.

**Impact:** SSTB phase-in ignored. Full $40,000+ deduction taken when only $25,000-30,000 was allowed (depending on phase-in percentage). IRS notice on CP2000.

**Citation:** IRC §199A(d)(2)(A); Treas. Reg. §1.199A-5(b)(2)(ix) — financial services SSTB explicitly includes investment advisors.

**Fix:** Use the SSTB classification reference. When in doubt, treat as SSTB and let the Schedule A computation reduce the deduction. Better than an audit.

---

## 7. Aggregating an SSTB with non-SSTB businesses

**Problem:** Owner of a consulting firm and a software firm tries to aggregate them on Schedule B for W-2 wage purposes.

**Impact:** Schedule B election is invalid because consulting is SSTB. The IRS could disallow the entire aggregation — meaning the software business's W-2 wages cannot support the consulting business's deduction.

**Citation:** Treas. Reg. §1.199A-4(b)(1)(iv) — none of the businesses being aggregated may be SSTB.

**Fix:** Don't aggregate any SSTB. Compute each business separately. The consulting firm uses its own W-2 wages and applies SSTB rules; the software firm uses its own W-2 wages.

---

## 8. Forgetting the QBI Loss Carryforward Between Years

**Problem:** Last year's Form 8995-A had aggregate QBI of negative $50,000 (carried forward). This year, the filer doesn't enter the carryforward, so this year's Form 8995-A computes a $40,000 deduction on $200,000 of positive QBI.

**Impact:** Overstated deduction by $50,000 × 20% = $10,000. IRS will catch this when reconciling year-over-year forms; CP2000 notice.

**Citation:** IRC §199A(c)(2); Treas. Reg. §1.199A-1(d)(2)(iii).

**Fix:** Always check prior-year Form 8995-A for a QBI loss carryforward. Enter on this year's Form 8995-A as a negative-QBI business in the loss-netting computation. The carryforward continues until fully offset.

---

## Bonus: Reasonable comp wage-vs-distribution planning around the threshold

Not strictly a "mistake" but a frequently missed planning opportunity:

**Scenario:** S-corp owner with $400,000 expected profit. Pays $100,000 reasonable comp + $300,000 distribution. Joint taxable income before QBI: $500,000 (just above MFJ threshold).

If the owner had paid $150,000 W-2 + $250,000 distribution:
- W-2 wages of business: $150,000 (vs. $100,000) — supports W-2/UBIA limit better
- QBI: $250,000 (vs. $300,000) — slightly less
- Owner's total income: same
- W-2/UBIA limit at 50% × $150,000 = $75,000 (vs. $50,000) — bigger limit

If the W-2/UBIA limit was binding, the higher reasonable comp produces a bigger §199A deduction — but the owner pays more SS/Medicare tax (15.3% × $50K extra wages = $7,650 of extra payroll tax, but with the SS wage base limit of $176,100 for 2025, only the Medicare portion of 2.9% × $50K = $1,450 typically applies for owners already maxing SS).

The break-even depends on the binding constraint. Run both scenarios.
