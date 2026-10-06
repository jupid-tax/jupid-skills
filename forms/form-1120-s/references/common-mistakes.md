# Form 1120-S Common Mistakes

The errors that most often break a Form 1120-S draft, each with the rule, the fix, and the citation. Use this list when validating a draft or reviewing a prior-year return. Citations are to the 2025 Form 1120-S and the 2025 Instructions for Form 1120-S ("Instr.") unless noted.

---

## 1. No officer wages while distributions flow

**Pattern:** The shareholder runs the business full time. Line 7 is $0; Schedule K, line 16d shows $90,000 of distributions.

**Rule:** "Distributions and other payments by an S corporation to a corporate officer must be treated as wages to the extent the amounts are reasonable compensation for services rendered to the corporation" (Instr., lines 7 and 8). The IRS may adjust items under §1366(e).

**Fix:** Do not invent a salary. Ask what the officer did, whether payroll was run, and how pay was set. Record the facts as an open item and refer to a CPA. If wages were paid but booked as draws, the payroll filings (Forms 941, W-2) must be corrected first.

## 2. Owner salary on line 8

**Pattern:** The shareholder-president's wages are on line 8 with the staff.

**Rule:** Line 7 is "the total compensation of all officers"; officer status follows state law (Instr., lines 7 and 8).

**Fix:** Move officer pay to line 7. If total receipts are $500,000 or more, Form 1125-E is required regardless of which line was used.

## 3. More-than-2% shareholder health insurance on line 18

**Pattern:** Premiums for the owner's family plan are deducted as an employee benefit program.

**Rule:** Line 18 covers fringe benefits only for employees owning 2% or less. For more-than-2% shareholders, report fringe benefits on line 7 or 8, whichever applies, and as wages in W-2 box 1 (Instr., lines 7, 8 and 18).

**Fix:** Move the premiums to line 7 (officer) or line 8 (non-officer); confirm they appear in W-2 box 1; the shareholder may then use Schedule 1 (Form 1040), line 17.

## 4. Section 179 or charitable contributions deducted on page 1

**Pattern:** A $22,600 machine is expensed under §179 inside line 14, and a $2,750 donation sits in line 20.

**Rule:** "Don't include any section 179 expense deduction on this line" (Instr., line 14); §179 passes through on Schedule K, line 11. Charitable contributions are Schedule K, lines 12a/12b, and line 20 excludes "items that must be reported separately on Schedules K and K-1" (Instr., line 20).

**Fix:** Move §179 to K line 11 and contributions to K line 12a/12b; recompute line 22, K line 18, the AAA and every K-1. Bonus depreciation stays on line 14 via Form 4562.

## 5. Bank interest and dividends on page 1

**Pattern:** Interest on the operating account and money-market dividends are included in line 5.

**Rule:** Report only trade or business income on lines 1a–5; portfolio income goes on Schedule K (Instr., Income caution; Portfolio Income). Interest on customer receivables in the ordinary course of business is line 5.

**Fix:** Move portfolio interest to K line 4, dividends to K lines 5a/5b; include them in K line 17a investment income.

## 6. Skipping Schedule M-2 because question 11 was "Yes"

**Pattern:** The draft leaves Schedules L, M-1 and M-2 blank.

**Rule:** Question 11 says only that "the corporation is not required to complete Schedules L and M-1" (Form 1120-S, page 2). The Instructions recommend that every S corporation maintain the AAA (Instr., Schedule M-2, column (a)).

**Fix:** Roll the AAA forward on Schedule M-2 every year. Ask for last year's ending balance; if no one ever tracked it, flag that the opening AAA must be reconstructed and say so in the validation summary.

## 7. Misreading the $250,000 test

**Pattern:** The draft compares line 1c (after returns) or line 22 with $250,000, or ignores year-end assets.

**Rule:** Total receipts = line 1a + lines 4 and 5 + income on K lines 3a, 4, 5a, 6 + income or net gain on K lines 7, 8a, 9, 10 + Form 8825 lines 2, 21, 22a; AND year-end total assets; both under $250,000 (Instr., Question 11).

**Fix:** Show the test as a computed table in the draft (see schedules-l-m1-m2.md, section 1).

## 8. Equal K-1 percentages after a mid-year share change

**Pattern:** A shareholder sold part of their stock in April, but every K-1 shows the year-end ownership percentage.

**Rule:** Items are allocated per share, per day (IRC §1377(a)(1); Instr., item G). The only exceptions are a §1377(a)(2) terminating election or a qualifying-disposition election, each with consent and an attached statement.

**Fix:** Recompute item G with day-weighted percentages; reallocate every K-1 box except distributions and loan repayments (which go to the actual recipient).

## 9. Treating distributions as income or as a deduction

**Pattern:** Distributions are added to K-1 income, or deducted on page 1.

**Rule:** Distributions are reported on K line 16d and K-1 box 16, code D; they reduce AAA and stock basis and are taxable to the shareholder only above basis (Shareholder's Instructions for Schedule K-1, Basis Limitations). Dividends from AE&P go on K line 17c and Form 1099-DIV.

**Fix:** Remove distributions from income and deductions. Report them only on 16d and in Schedule M-2, line 7.

## 10. Non-pro-rata distributions ignored

**Pattern:** One shareholder took $30,000 more than their share; the draft just reports what each received.

**Rule:** Reporting what each shareholder actually received is correct (Instr., line 16d), but unequal per-share distributions raise the one-class-of-stock question under Reg. §1.1361-1(l), which can threaten the election.

**Fix:** Report actual amounts, add a sanity warning with the per-share math, ask about the governing documents, and refer to a CPA.

## 11. Filing Form 1120-S for a year before the election took effect

**Pattern:** The S election was effective January 1, 2026; the agent drafts a 2025 Form 1120-S.

**Rule:** "Don't file Form 1120-S for any tax year before the year the election takes effect" (Instr., Who Must File).

**Fix:** Route the 2025 year to Form 1120 (corporation), Form 1065 (multi-member LLC) or Schedule C (single-member LLC).

## 12. Entering zero on lines 23a–23c without the history screen

**Pattern:** A corporation that converted from C status in 2023 sold appreciated equipment; the draft enters $0 on line 23b.

**Rule:** The built-in gains tax applies to dispositions during the 5-year recognition period beginning on the first day of the first S year (Instructions for Schedule D (Form 1120-S), Part III); Schedule B item 8 must show the net unrealized built-in gain.

**Fix:** Run the history screen in SKILL.md Step 2 and the screens in schedules-l-m1-m2.md, section 6; mark the lines "PENDING — CPA" when a screen fails.

## 13. Missing the K-2/K-3 decision

**Pattern:** The corporation paid $410 of foreign tax through a brokerage account and checked nothing on K line 14.

**Rule:** The domestic filing exception allows foreign activity only if limited to passive category income with not more than $300 of creditable foreign tax shown on a payee statement, plus shareholder notification and no timely request (S Corporation Instructions for Schedules K-2 and K-3, 2025).

**Fix:** Unless the small S corporation exception applies (question 11 "Yes"), flag K-2/K-3 preparation for a CPA.

## 14. Item I and Schedule L, line 19 disagree

**Pattern:** The books show a $25,000 loan from a shareholder on Schedule L, line 19, but item I on that shareholder's K-1 is blank.

**Rule:** Item I reports debt owed directly to the shareholder at the beginning and end of the year; Schedule L, line 19 should reconcile to the sum of the K-1 amounts (Instr., Item I).

**Fix:** Fill item I; exclude guarantees and co-borrowed debt.

## 15. Payroll and return disagree

**Pattern:** Line 7 + line 8 = $214,000; the Forms W-2 box 1 total is $221,400.

**Rule:** Lines 7 and 8 exclude wages in cost of goods sold and elective deferrals (Instr., lines 7 and 8); fringe benefits for more-than-2% shareholders are included.

**Fix:** Reconcile in the draft (officer-compensation.md, Reconciliation). List any unexplained gap; do not adjust the return to force a match.
