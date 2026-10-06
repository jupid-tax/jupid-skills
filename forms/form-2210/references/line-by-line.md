# Form 2210 Line-by-Line Reference

Complete lookup for every line on Form 2210. Use this when the agent needs to confirm where an input belongs or what a line means.

**Revision**: verified against the 2025 Form 2210 (created 10/21/25) and the 2025 Instructions for Form 2210 (Feb 17, 2026), used for 2025 returns filed in 2026. Re-check the 2026 revision at https://www.irs.gov/forms-pubs/about-form-2210 before using this map for 2026 returns.

## Header

| Field | What goes here |
|-------|----------------|
| Name(s) shown on return | Same as Form 1040 header (joint string for MFJ) |
| Identifying number | Filer's SSN (the spouse's SSN does not appear on Form 2210 separately for MFJ) |

---

## Part I — Required Annual Payment

The "did the safe harbor save me from a penalty?" computation.

### Line 1 — Tax after credits

2025 Form 1040 line 22 (tax after nonrefundable credits; it already includes AMT and excess advance premium tax credit repayment from Schedule 2 line 3). Filers may exclude section 965 net tax liability.

### Line 2 — Other taxes

The total of these 2025 Schedule 2 lines: 4 (self-employment tax), 8 (additional tax on distributions only), 9 (household employment taxes, with the instructions' exception), 11 (Additional Medicare Tax), 12 (NIIT), 14, 15, 16, 17a, 17c–17j, 17l, 17z, and 19. Not included: lines 5 and 6 (social security and Medicare tax from Forms 4137 and 8919) and line 13 (uncollected tax on tips or group-term life insurance).

### Line 3 — Other payments and refundable credits

Entered in parentheses: earned income credit, additional child tax credit, refundable American opportunity credit (Form 8863 line 8), refundable adoption credit (Form 8839 line 13), premium tax credit (Form 8962), credit for federal tax paid on fuels, §1341(a)(5)(B) credit. If a §1062(a) election (qualified farmland sale) was made, include 75% of the applicable net tax liability (Notice 2026-3).

### Line 4 — Current-year tax

```
Line 4 = Line 1 + Line 2 − Line 3
```

This is the "current-year tax" against which the 90% safe harbor is measured. If line 4 is less than $1,000, stop: no penalty, don't file.

### Line 5 — 90% of Line 4

```
Line 5 = Line 4 × 0.90
```

This is the current-year safe harbor amount.

### Line 6 — Withholding

Form 1040 line 25d plus Schedule 3 line 11 (excess social security and tier 1 RRTA tax). Line 25d covers:
- W-2 Box 2 (federal income tax)
- 1099-R / 1099-MISC / 1099-NEC Box 4 (any 1099 with federal withholding)
- Form 8959 Line 24 (Additional Medicare Tax withheld)
- Backup withholding on 1099-INT / 1099-DIV
- Withholding on Social Security benefits (Form SSA-1099)

Don't include estimated tax payments. Treated as paid evenly across the four quarters under IRC §6654(g)(1) unless the filer establishes the actual withholding dates (box D).

### Line 7 — Line 4 minus Line 6

If line 7 is less than $1,000, the de minimis exception applies (IRC §6654(e)(1)) and the filer owes no penalty. The form says: "If less than $1,000, stop; you don't owe a penalty. Don't file Form 2210." Estimated payments are not subtracted here.

### Line 8 — Prior-year tax × 100% (or 110% if applicable)

2024 tax per the line 8 instructions: 2024 Form 1040 line 22, plus 2024 Schedule 2 lines 4, 8 (additional tax on distributions only), 9, 10, 11, 12, 14, 15, 16, 17a, 17c–17j, 17l, 17z, and 19, minus the 2024 refundable credits (EIC, additional child tax credit, refundable AOTC, premium tax credit, fuel tax credit, §1341 credit).

Multiply by:
- **100%** if 2024 AGI ≤ $150,000 (≤ $75,000 if MFS for 2025)
- **110%** if 2024 AGI > $150,000 (> $75,000 if MFS for 2025)

Joint for 2025 but not for 2024: add both spouses' 2024 tax. Single, HoH, or MFS for 2025 after a 2024 joint return: use your share of the 2024 joint tax. No 2024 return, or a 2024 tax year shorter than 12 months: skip line 8 and enter line 5 on line 9.

This is the prior-year safe harbor amount. Codified at IRC §6654(d)(1)(B)(ii) and §6654(d)(1)(C).

### Line 9 — Required annual payment

```
Line 9 = smaller of Line 5 or Line 8
```

The filer needed Line 9 in total payments (withholding + estimates) by year-end to avoid penalty. If they had less, the difference (per quarter) is the underpayment that accrues penalty.

---

## Part II — Reasons for Filing

Five boxes (A–E). If none applies, don't file Form 2210; the IRS figures any penalty and sends a bill.

### Box A — Waiver of the entire penalty

Check it and file page 1 only; the penalty is not figured. Grounds (IRC §6654(e)(3)):
- Retired after reaching age 62, or became disabled, in 2024 or 2025, and the underpayment was due to reasonable cause and not willful neglect; or
- The underpayment was due to a casualty, disaster, or other unusual circumstance and imposing the penalty would be inequitable

Attach a statement explaining why the estimated tax requirements were not met and the period covered, plus documentation: retirement date and age on that date, date of disability, or police and insurance reports.

### Box B — Waiver of part of the penalty

Same grounds and attachments as box A. Complete Form 2210 through line 18 without regard to the waiver, enter the waived amount in parentheses on the dotted line next to line 19, and subtract it.

Federally declared disasters: the IRS identifies taxpayers in covered areas by county or parish and applies relief automatically. Generally don't file Form 2210 for that underpayment; exception: file it if using Schedule AI.

### Box C — Annualized income installment method

Income varied during the year and Schedule AI reduces or eliminates the penalty. Figure the penalty with Schedule AI and file Form 2210.

### Box D — Withholding on actual dates

The penalty is lower when withholding is treated as paid on the dates it was actually withheld (IRC §6654(g)(1)). Figure the penalty and file Form 2210.

### Box E — Joint return in only one of the two years

A joint return was filed for 2024 or 2025 but not both, and line 8 is smaller than line 5. File page 1 only (the penalty need not be figured unless B, C, or D applies).

---

## Part III — Penalty Computation

Part III has two sections. Section A (lines 10–18) figures the underpayment for each column; Section B (line 19) carries the total from the penalty worksheet in the instructions. Complete lines 12–18 of one column before starting the next.

### Section A — Figure the underpayment (lines 10–18)

| Column | Income period (for Schedule AI) | Due date (2025 form) |
|--------|----------------------------------|----------------------|
| (a) | Jan 1 – Mar 31 | 4/15/25 |
| (b) | Jan 1 – May 31 | 6/15/25 |
| (c) | Jan 1 – Aug 31 | 9/15/25 |
| (d) | Jan 1 – Dec 31 | 1/15/26 |

- **Line 10 — Required installment.** 25% of line 9 in each column (not cumulative). If box C applies, Schedule AI line 27.
- **Line 11 — Estimated tax paid and tax withheld** in the column's window: through 4/15/25; after 4/15 through 6/15/25; after 6/15 through 9/15/25; after 9/15/25 through 1/15/26. Withholding (and excess social security / RRTA) counts one-fourth per column unless box D. A 2024 overpayment applied to 2025 is generally treated as paid 4/15/25. Mailed payments use the postmark date. A payment made on the next business day after a due date that falls on a weekend or holiday counts as made on the due date. If the return is filed and the tax paid by January 31, 2026, the amount paid with it goes in column (d) and there is no penalty for the January 15 installment (IRC §6654(h)). Column (a) line 11 also goes on line 15. If line 11 ≥ line 10 in every column, stop: no penalty.
- **Line 12** — overpayment (line 18) from the previous column.
- **Line 13** — lines 11 + 12.
- **Line 14** — lines 16 + 17 of the previous column (earlier underpayment still unpaid).
- **Line 15** — line 13 − line 14; zero or less → 0.
- **Line 16** — if line 15 is zero, line 14 − line 13; otherwise 0.
- **Line 17 — Underpayment.** If line 10 ≥ line 15, line 10 − line 15.
- **Line 18 — Overpayment.** If line 15 > line 10, line 15 − line 10.

Payments are applied first to the earliest unpaid installment, even if designated for a later period (IRC §6654(b)(3)). A payment on April 14 counts in column (a); a payment on April 16 counts in column (b) and first pays off the column (a) underpayment, which then accrues penalty for one day.

### Section B — Figure the penalty (line 19)

Use the Worksheet for Form 2210, Part III, Section B in the instructions. For each column's line 17 amount and each rate period:

```
Penalty = underpayment × (days unpaid in the rate period / 365) × rate

days unpaid = from the due date (or the start of the rate period) to the date the
              underpayment was paid, or the end of the rate period, whichever is earlier

2025 rate periods and rates (worksheet): 4/16/25–6/30/25, 7/1/25–9/30/25,
10/1/25–12/31/25, 1/1/26–4/15/26, each at 0.07
```

The penalty is simple interest (IRC §6622(b) excludes it from daily compounding). Table 2 of the instructions gives full-period day counts: column (a) 76 / 92 / 92 / 105; (b) 15 / 92 / 92 / 105; (c) 15 / 92 / 105; (d) 90.

### Total Penalty

```
Total penalty = worksheet line 14 = Form 2210 line 19

→ flows to Form 1040 line 38 (Estimated tax penalty)
```

---

## Schedule AI — Annualized Income Installment Method

Replaces the line 10 required installments with amounts based on actual cumulative income (Schedule AI line 27). Check box C. See `references/annualized-income-method.md` for full worksheet structure.

Schedule AI columns:

| Column | Period | Annualization factor | Cumulative installment % |
|--------|--------|---------------------|--------------------------|
| (a) | Jan 1 – Mar 31 | 4 | 22.5% |
| (b) | Jan 1 – May 31 | 2.4 | 45% |
| (c) | Jan 1 – Aug 31 | 1.5 | 67.5% |
| (d) | Jan 1 – Dec 31 | 1 | 90% |

For each column (2025 Schedule AI lines):
1. Line 1: AGI from January 1 through the column's end date (self-employed: after the deductible half of the period's SE tax)
2. Line 3: annualized income = line 1 × factor
3. Lines 4–13: subtract the full-year standard deduction (line 7, not prorated) or annualized itemized deductions (lines 4–6), and the QBI deduction (line 9)
4. Line 14: tax on line 13 (adjust for OBBBA provisions not handled elsewhere, e.g. Schedule 1-A deductions); line 15: annualized SE tax from Part II line 36; line 16: other taxes incl. Additional Medicare Tax, NIIT, AMT; line 18: credits
5. Line 21: line 19 × applicable percentage (no division by the factor; the percentage already reflects the part of the year)
6. Line 23: line 21 minus the line 27 amounts of earlier columns
7. Line 24: 25% of Form 2210 line 9; line 25: previous column's line 26 − line 27; line 26: line 24 + line 25
8. Line 27: smaller of line 23 or line 26 → Form 2210 Part III line 10

Part II (lines 28–36) annualizes SE tax: line 28 = period net earnings (profit × 92.35%; under $400 → 0); line 29 prorated social security limit $44,025 / $73,375 / $117,400 / $176,100; line 30 wages for the period; line 33 = 0.496 / 0.2976 / 0.186 / 0.124 × smaller of line 28 or line 31; line 35 = line 28 × 0.116 / 0.0696 / 0.0435 / 0.029; line 36 = line 33 + line 35.

Schedule AI requires:
- Cumulative income data for each period
- Itemized deductions by period, if itemizing
- Current-year tax brackets

If Schedule AI is used for any due date it is used for all of them (2025 instructions), but line 27 keeps the smaller of the annualized or the regular installment in each column, and reductions are recaptured in later columns (IRC §6654(d)(2)(A)(ii)).

---

## Special situations

### Farmers and fishermen

If at least two-thirds of gross income for 2024 or 2025 is from farming or fishing, special rules apply:
- Single payment by January 15 instead of four quarterly payments
- Different safe harbor (66 2/3% instead of 90%); the 110% rule does not apply
- No penalty at all if the return is filed and the entire tax paid by March 2, 2026 (2025 instructions)

These filers use **Form 2210-F** (separate form), not Form 2210, unless they meet the March 2 test. Out of scope for this skill; redirect to Form 2210-F if the user qualifies.

### Fiscal-year filers

Most individuals are calendar-year. If filer is fiscal-year (very rare), the quarterly due dates shift accordingly. See current-year Form 2210 instructions for fiscal-year due dates.

### Estates and trusts

Estates and trusts use Form 2210 too but with different rules (Schedule AI period ends 2/28, 4/30, 7/31, 11/30 and factors 6, 3, 1.71429, 1.09091). No penalty applies to a decedent's estate, or to a qualifying grantor trust that receives the residue, for any tax year ending before the date that is 2 years after the decedent's death (IRC §6654(l)(2); 2025 instructions). Out of scope for this skill — covers individuals.

### Joint return where one spouse died during the year

Use the surviving spouse's filing status; safe harbor uses the joint prior-year tax (the joint return for the prior year).

### Mid-year residency change (non-resident → resident or vice versa)

The required annual payment is computed only on the income subject to US tax during the residency period. See current-year Pub. 519 for rules.

### Large estimated payment at year-end

A January 15 estimated payment ("Q4 payment") is applied first to any unpaid Q1, Q2, and Q3 underpayments, then to the Q4 installment (IRC §6654(b)(3)). It stops the earlier underpayments from accruing further, but the penalty they accrued from their own due dates to January 15 stays. A common filer mistake: assuming a Q4 estimate "back-fills" earlier underpayments retroactively. It does not.

---

## Sources

- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf)
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf)
- IRC §6654 — Failure by individual to pay estimated income tax
- IRC §6654(b)(3) — Payments credited to the earliest unpaid installment
- IRC §6654(d)(1)(B) — 90% current-year / 100% prior-year required annual payment
- IRC §6654(d)(1)(C) — 110% safe harbor for high-AGI prior-year filers
- IRC §6654(d)(2) — Annualized income installment
- IRC §6654(e)(1) — $1,000 de minimis
- IRC §6654(e)(2) — No prior-year tax liability
- IRC §6654(e)(3) — Waivers
- IRC §6654(g)(1) — Withholding allocated equally across quarters unless actual dates are established
- IRC §6621 — Penalty rate (federal short-term rate + 3 points); IRC §6622(b) — no daily compounding
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Tax Withholding and Estimated Tax (points to the Form 2210 instructions for the penalty)
