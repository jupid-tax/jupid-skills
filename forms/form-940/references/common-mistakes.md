# Common Form 940 Mistakes

Errors the agent should check for before declaring a draft ready. Each entry: symptom, rule with authority, fix. Sources are the 2025 Form 940 and Instructions for Form 940 (I940), the 2025 Schedule A (Form 940), and Publication 15 (2026) unless noted.

---

## 1. Whole payroll on line 7

**Symptom.** Line 7 equals line 3, or line 7 divided by the employee count exceeds $7,000.

**Rule.** Only the first $7,000 paid to each employee in the calendar year, after exempt payments, is FUTA wages. Line 5 removes the excess; line 7 = line 3 − (line 4 + line 5) (I940, lines 5–7; IRC §3306(b)(1)).

**Fix.** Rebuild line 5 employee by employee. Recompute line 7 as Σ min($7,000, payments − exempt payments) and compare.

## 2. Exempt payments subtracted twice

**Symptom.** Line 5 computed as payments − $7,000 while line 4 also holds the same employee's health premiums, so line 7 is understated.

**Rule.** Line 5 is "after subtracting any payments exempt from FUTA tax shown on line 4" (I940, line 5). Each employee's excess = payments − exempt − $7,000.

**Fix.** Recompute the excess per employee with the exempt amount removed first.

## 3. Employee 401(k) deferrals on line 4

**Symptom.** Box 4c checked for amounts employees elected to defer.

**Rule.** Line 4c covers employer contributions to a qualified plan, "other than elective salary reduction contributions" (I940, line 4). Line 3 lists elective salary reduction contributions to a SIMPLE among payments to include.

**Fix.** Keep employee elective deferrals in FUTA wages. Put only employer contributions on 4c.

## 4. Payments on line 4 that were never on line 3

**Symptom.** Line 4 includes workers' compensation or partner draws that were not counted on line 3.

**Rule.** "You only report a payment as exempt from FUTA tax on line 4 if you included the payment on line 3" (I940, line 4). Partner payments are not employee payments at all (Pub. 15, section 15 table: payments to partners exempt).

**Fix.** Either add the payment to line 3 and line 4, or remove it from both if it was never a payment to an employee.

## 5. Moving expense or bicycle commuting reimbursements on line 4

**Symptom.** Box 4a or 4e includes relocation or bicycle reimbursements.

**Rule.** These reimbursements are subject to FUTA; "Don't include moving expense or bicycle commuting reimbursements on Form 940, line 4" (I940 Reminders; 2026 draft instructions: P.L. 119-21 made the elimination permanent).

**Fix.** Remove from line 4.

## 6. Line 9 used when only some wages were excluded

**Symptom.** Line 9 = line 7 × 0.054 although some employees' wages were taxed by the state.

**Rule.** Line 9 is for ALL taxable FUTA wages excluded from state unemployment tax. SOME excluded → line 10 worksheet. A 0% assigned rate is not an exclusion (I940, lines 9 and 10).

**Fix.** Run the line 10 worksheet; leave line 9 blank.

## 7. State tax "late" judged by the state's due date

**Symptom.** Line 10 filled because a quarterly state payment missed the state deadline, though it was paid before the Form 940 due date.

**Rule.** "On time" means paid by the due date for filing Form 940 (I940, worksheet). The state may still charge its own penalty.

**Fix.** Treat payments made by the Form 940 due date as on time; rerun the worksheet.

## 8. Schedule A missing or incomplete

**Symptom.** California or U.S. Virgin Islands wages in 2025 with line 2 unchecked; or a multi-state employer checks only the credit reduction state on Schedule A.

**Rule.** Multi-state employers check every state where they paid state unemployment tax, even states with a zero rate; any employer with wages in a credit reduction state completes Schedule A (Schedule A page 2, Step 1; I940, lines 1b and 2).

**Fix.** Check every state; compute credit reduction only for states with a rate above zero; carry the total to line 11.

## 9. Credit reduction computed on state wages or on wages above $7,000

**Symptom.** Schedule A FUTA Taxable Wages box shows the state wage base or gross pay.

**Rule.** Enter FUTA taxable wages paid in that state (combined $7,000 per employee across states), excluding wages excluded from that state's unemployment tax; do not enter state unemployment wages (Schedule A page 2, Step 2 and Example 2).

**Fix.** Rebuild per employee; for transferred employees, allocate the $7,000 in payment order across states.

## 10. Deposits reported in Part 5

**Symptom.** Lines 16a–16d mirror EFTPS deposits (e.g. $0 in Q1 and the full amount in Q2).

**Rule.** "Report the amount of your FUTA tax liability for each quarter; do NOT enter the amount you deposited" (F940, line 16). Part 5 is completed only if line 12 is more than $500.

**Fix.** Recompute liability by quarter from wages paid; credit reduction goes on 16d.

## 11. Missed deposit after crossing $500

**Symptom.** Cumulative liability passed $500 in Q2, nothing was deposited until the return was filed, and line 14 shows the balance.

**Rule.** Deposit by the last day of the month after the quarter in which cumulative undeposited liability exceeds $500 (I940; Treas. Reg. §31.6302(c)-3). Paying a required deposit with the return draws a 10% failure-to-deposit penalty (Pub. 15, section 11; IRC §6656).

**Fix.** Do not change the return. Flag the penalty exposure, deposit any remaining balance by EFT, and tell the user that abatement requests go on Form 843 or in reply to the notice.

## 12. Household employees reported twice

**Symptom.** A business owner's nanny is on Form 940 line 3 and also on Schedule H.

**Rule.** Household FUTA goes on Schedule H, or, by choice for an employer with other employees, on Form 940 together with Form 941/943/944 for the Social Security and Medicare taxes; payments for domestic services reported on Schedule H are exempt on Form 940 line 4 (I940, "For Employers of Household Employees" and line 4; Pub. 926 (2026), "Business employment tax returns").

**Fix.** Pick one route; remove the wages from the other return.

## 13. Family-member pay misclassified

**Symptom.** A sole proprietor's 19-year-old child's wages counted as FUTA wages; or a corporation treats the owner's child's wages as exempt.

**Rule.** Pay for services of your child under 21, your spouse, or your parent is FUTA-exempt when you are an individual employer (sole proprietorship, or a partnership in which each partner is a parent of the child). Pay from a corporation, a partnership with a non-parent partner, or an estate is FUTA wages (Pub. 15, section 3; IRC §3306(c)(5)).

**Fix.** Ask who legally employs the family member; adjust line 4 (box 4e).

## 14. S corporation distributions on line 3, or 2% shareholder health premiums left in FUTA wages

**Symptom.** Line 3 includes K-1 distributions; or the shareholder-officer's health premiums from W-2 box 1 are inside line 7.

**Rule.** Only reasonable-compensation wages are wages (Pub. 15, section 15 table). Health insurance for a more-than-2% shareholder is excluded from FUTA wages (Pub. 15, section 5; Announcement 92-16).

**Fix.** Remove distributions entirely; put the premiums on line 3 and line 4 (box 4a).

## 15. Wrong name, EIN, or owner's SSN

**Symptom.** Disregarded LLC files under the owner's SSN or name; trade name used as legal name.

**Rule.** Use the business legal name from Form SS-4 and the entity's EIN; disregarded entities file under their own name and EIN; never an SSN or ITIN (I940, EIN and "Disregarded entities").

**Fix.** Correct the header; if no EIN exists, apply first ([`../../form-ss-4/SKILL.md`](../../form-ss-4/SKILL.md)) or write "Applied For" and the date.

## 16. Using a potential credit reduction rate

**Symptom.** A 2026 draft uses 0.015 or 0.053 for California.

**Rule.** DOL's January list is "potential"; the final list follows the November 10 deadline, and the IRS publishes the rates on the final Schedule A (DOL potential 2026 list; 2026 draft Schedule A shows "0.0XX").

**Fix.** Leave the rate as pending and do not file until the final Schedule A for the year is available.
