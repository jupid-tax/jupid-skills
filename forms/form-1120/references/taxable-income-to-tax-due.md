# Form 1120: From Taxable Income to Tax Due (Lines 28–37 and Schedule J)

Covers the net operating loss deduction, the charitable contribution limit, the 21% tax on Schedule J, payments, the estimated-tax rules and Form 2220, and the boundary items the agent flags instead of computing. Sources are the 2025 Instructions for Form 1120, the 2025 Instructions for Form 2220, Publication 542 (Rev. January 2024), the Internal Revenue Code, and Rev. Proc. 2025-32. Recheck year-dependent amounts at https://www.irs.gov/forms-pubs/about-form-1120 and https://www.irs.gov/forms-pubs/about-form-2220.

---

## 1. Order of operations

1. Line 28 = line 11 − line 27 (taxable income before NOL and special deductions).
2. Line 29b = Schedule C line 24 (dividends-received and other special deductions, after the section 246(b) limit).
3. Line 29a = NOL deduction, not more than taxable income after special deductions (Instr., Line 29a).
4. Line 29c = 29a + 29b; line 30 = 28 − 29c.
5. Schedule J line 1a = line 30 × 21%; finish Schedule J; carry J12 to line 31 and J23 to line 33.
6. Lines 34 through 37.

The charitable deduction on line 19 sits inside line 27, but its limit depends on the NOL deduction. See section 3.

---

## 2. Net operating loss deduction (line 29a)

### Facts to ask for

- Each loss year, the original NOL, and the amount already used.
- Whether each loss arose in a tax year beginning before January 1, 2018 or after December 31, 2017.
- Whether an ownership change under section 382 occurred (more than 50 percentage points over a testing period), whether the corporation acquired another corporation or its assets (section 384), and whether a qualifying shipping election applies. Any "yes" → flag; the limits need a CPA.

### The 2025 limit (Instr., Line 30, Net operating loss)

The NOL deduction for tax year 2025 cannot exceed:

- the aggregate NOLs arising in tax years beginning before January 1, 2018 carried to the year, **plus**
- the lesser of (1) the aggregate NOLs arising in tax years beginning after December 31, 2017 carried to the year, or (2) **80%** of the excess, if any, of taxable income determined without any NOL deduction, section 199A deduction, or section 250 deduction, over any pre-2018 NOL carryover to the year.

The 80% taxable-income limit does not apply to insurance companies other than life insurance companies.

In practice, for a corporation with only post-2017 losses and no section 250 deduction: deduction = lesser of the carryover or 80% × (line 28 − line 29b, with any section 250 amount added back). Round consistently with the rest of the return.

### Carrybacks and carryforwards

- Only farming losses and losses of an insurance company (other than a life insurance company) can be carried back; the carryback period is 2 years (Instr., Line 30). Other post-2017 NOLs carry forward (IRC §172(b)(1)(A)).
- A corporation with a carryback-eligible NOL may elect to waive the carryback by checking Schedule K item 11 on a timely filed return (including extensions); the election is generally irrevocable (Instr., Item 11).
- Schedule K item 12: enter the NOL carryover available from prior years without reducing it by this year's line 29a (Instr., Item 12).
- Attach a statement showing the NOL computation (Instr., Line 29a).

### Statement format

| Loss year | Pre-2018 or post-2017 | Original NOL | Used before this year | Available (item 12) | Deducted on 29a | Carried forward |
|-----------|----------------------|--------------|-----------------------|---------------------|-----------------|-----------------|

---

## 3. Charitable contributions (line 19)

### 2025 rule (Instr., Line 19)

- Deduct contributions paid during the year plus carryovers, up to 10% of taxable income computed without: the contribution deduction, the special deductions on line 29b, the section 249 bond-premium limit, any NOL carryback, any capital loss carryback, and the specified cooperative deduction.
- With an NOL **carryover**, the 10% limit uses taxable income after the NOL deduction.
- Excess contributions carry forward 5 years.
- An accrual-method corporation may treat a contribution as paid in the year if the board authorized it during the year and it is paid by the 15th day of the 4th month after year end (IRC §170(a)(2); the 2025 instructions phrase it as paid by the return due date, not including extensions); attach a declaration with the resolution date.
- Substantiation: a bank record or written communication for any cash gift; a contemporaneous written acknowledgment for gifts of $250 or more; Form 8283 for noncash property over the thresholds in the instructions.

### Circular computations

The charitable limit uses taxable income after the NOL deduction, and the NOL limit uses taxable income after the charitable deduction. Check the contribution against the limit computed both ways:

- Way A: NOL deduction from line 28 as filed; charitable base = line 28 + line 19 contributions − NOL deduction.
- Way B: NOL deduction from (line 28 + contributions); charitable base = that amount − that NOL deduction.

If the contribution is below 10% of the base both ways, the limit does not bind; record both checks in the statement. If it binds either way, stop and have the CPA or software determine the deduction.

### Tax years beginning after December 31, 2025

IRC §170(b)(2)(A), as amended by P.L. 119-21 §70426 (effective for taxable years beginning after December 31, 2025), allows corporate contributions only to the extent the aggregate exceeds 1% of taxable income and does not exceed 10% of taxable income. Contributions disallowed by the 1% floor carry forward only from years in which the 10% limit is also exceeded (IRC §170(d)(2)(C)). Apply this to 2026 returns only after checking the 2026 Instructions for Form 1120.

---

## 4. Schedule J tax computation

- **Line 1a:** line 30 × 21% (Instr., Schedule J line 1a; IRC §11(b)). The same rate applies to personal service corporations.
- **Lines 1b–1z:** other chapter 1 taxes (Form 1120-L, section 1291, Form 8978, section 197(f), base erosion minimum tax, Form 4255 column (q), other).
- **Line 3:** corporate alternative minimum tax from Form 4626. Boundary. Schedule K question 29: a corporation meeting the safe harbor answers "Yes" to 29c and does not file Form 4626; the instructions say corporations generally qualify if average annual adjusted financial statement income for the 3 preceding years is less than $800 million (Instr., Question 29).
- **Line 1f:** base erosion minimum tax. Boundary. Applies only with gross receipts of at least $500 million in any 1 of the 3 preceding tax years (Instr., Question 22).
- **Line 8:** personal holding company tax. Boundary. A corporation is a PHC if at least 60% of adjusted ordinary gross income is PHC income and more than 50% in value of its stock is owned by five or fewer individuals at any time in the last half of the year (Instr., Line 8). If both may be true, check item A box 2, attach Schedule PH, and hand off.
- **Credits (5a–5f):** take amounts from the credit forms (Form 3800 for the general business credit). The agent does not compute credits; it carries totals and flags the forms.

---

## 5. Payments (Schedule J lines 13–23)

| Line | Entry |
|------|-------|
| 13 | Prior year's overpayment credited to this year (from last year's line 37a) |
| 14 | Estimated tax payments for this year, each with date and amount in the workpapers |
| 15 | Refund applied for on Form 4466 (parentheses) |
| 17 | Tax deposited with Form 7004 |
| 18 | Backup or other withholding |
| 19 | 13 + 14 − 15 + 17 + 18 |
| 20a–20z, 21 | Refundable credits (Forms 2439, 4136, 1042-S/8805/8288-A, other) |
| 22a | Form 3800 elective payment election amount |
| 22b | Section 1062 applicable net tax liability (Form 1062 line 14) |
| 23 | 19 + 21 + 22a + 22b → page 1 line 33 |

**Form 4466 quick refund:** available when the estimated tax overpayment is at least 10% of the expected tax liability and at least $500; file after the year ends and before the return, no later than the original due date (Instr., Line 15; Pub. 542). The IRS acts within 45 days (Pub. 542).

---

## 6. Estimated tax and the Form 2220 handoff

### Requirement and dates

- Required when the corporation expects total tax (less applicable credits) of $500 or more (Instr., Estimated Tax Payments; IRC §6655).
- Due the 15th day of the 4th, 6th, 9th, and 12th months of the tax year; a weekend or legal holiday moves the date to the next business day. Calendar year: April 15, June 15, September 15, December 15. June 30 year end: October 15, December 15, March 15, June 15 (Pub. 542).
- Payment by electronic funds transfer only (EFTPS or the IRS business tax account).

### Required installment (Pub. 542, Rev. January 2024)

- **Method 1:** each installment is 25% of the tax shown on the current-year return.
- **Method 2:** each installment is 25% of the tax shown on the previous year's return, only if that return was filed, covered a full 12 months, and showed a positive tax liability.
- Use whichever gives the smaller installment.
- **Large corporation:** taxable income of $1 million or more (excluding NOL and capital loss carrybacks and carryovers) in any of the 3 immediately preceding tax years. A large corporation may use Method 2 only for the first installment (Pub. 542; Instr. for Form 2220, Line 8).
- Annualized income and adjusted seasonal installment methods can lower installments for uneven income (IRC §6655(e)); if used, Form 2220 must be attached.

### Form 1120-W status

Form 1120-W, Estimated Tax for Corporations, and its instructions are historical; the 2022 revisions were the last (Pub. 542, Rev. January 2024, What's New). Use the Pub. 542 estimated tax worksheet or the Method 1/Method 2 rules above.

### Form 2220 and line 34

- The penalty is figured separately for each installment and runs at the IRS underpayment rate for the period (Pub. 542). Current rates: https://www.irs.gov/payments/quarterly-interest-rates.
- The IRS can figure the penalty and bill the corporation. Attach Form 2220, even if no penalty is owed, when the corporation used the annualized income or adjusted seasonal method, or is a large corporation figuring its first installment from the prior year's tax (Instr., Line 34). If the return includes a CAMT liability, attach Form 2220 and enter an amount on line 34 even if zero (Instr., Line 34; Notice 2025-27).
- The agent's job: list each installment due, required, paid, and the shortfall. If any shortfall exists, state that Form 2220 applies and hand the computation to the software or CPA.

### Next year's installments

After the draft is final, state next year's dates and the Method 2 amount (25% of this year's line 31 tax, if this year covers 12 months and shows tax), and reduce the first installment by any line 37a credit if the user chose one.

---

## 7. Lines 34–37

- Line 35 (amount owed) = lines 31 + 32 + 34 − line 33 when positive. Pay by electronic funds transfer by the original due date; an extension does not extend payment. Online installment agreement available if the corporation cannot pay in full, owes $25,000 or less, and can pay within 24 months (Instr., Line 35).
- Line 36 (overpayment) = line 33 − (31 + 32 + 34) when positive.
- Line 37a + 37b = 36. The 37a credit to next year's estimated tax cannot be changed later (Instr., Line 37a).

---

## 8. Penalties to mention in the validation summary

- Late filing: 5% of unpaid tax per month or part of a month, up to 25%; for returns required to be filed in 2026 that are more than 60 days late, the minimum is the smaller of the tax due or $525 (Instr., Late filing of return). For returns required to be filed in 2027, the minimum is the lesser of $535 or 100% of the tax required to be shown (Rev. Proc. 2025-32, §4.52).
- Late payment: 0.5% of unpaid tax per month or part of a month, up to 25% (Instr., Late payment of tax).
- Interest runs on late tax even with an extension (Instr., Interest).
- If the IRS sends a penalty notice, reply with the reasonable-cause explanation then; do not attach one to the return (Instr., Note).

---

## 9. Section 1202 (qualified small business stock): boundary only

Section 1202 excludes gain for a noncorporate shareholder who sells qualified small business stock. Form 1120 has no line for it, and nothing on the corporation's return claims it. If the user raises it, say that the corporation's records (gross assets when stock was issued, active business use of assets) matter to shareholders later, and refer the user to a CPA. Do not state exclusion percentages or caps in the draft.

Sources: Instructions for Form 1120 (2025): Estimated Tax Payments (p. 5), Interest and Penalties (p. 6), Line 19 (p. 14), Line 29a (p. 16), Line 30 and Line 34 (p. 17), Schedule J (pp. 22–23), Schedule K items 11–12 (p. 25), Question 22, Question 29; Instructions for Form 2220 (2025); Publication 542 (Rev. January 2024), Estimated Tax; Rev. Proc. 2025-32 §4.52; IRC §§ 11(b), 170(a)(2), 170(b)(2), 170(d)(2), 172, 382, 6655; P.L. 119-21 §70426.
