# Form 2210 — Common Mistakes

Audit-trip patterns the agent should watch for. Each mistake includes a citation, a worked failure mode, and the correct fix.

## 1. Filing Form 2210 when the IRS would compute a smaller penalty

**Mistake**: Filer attaches Form 2210 with the regular method when the IRS's automatic computation would have produced a lower penalty (or the IRS might have applied a waiver the filer didn't know to request).

**Why it happens**: Filer assumes filing Form 2210 is mandatory whenever a penalty is owed. It isn't — for the regular method, the IRS computes automatically.

**Fix**: File Form 2210 only if a Part II box applies: A or B (waiver), C (Schedule AI), D (withholding on actual dates), or E (joint return in only one of the two years and line 8 < line 5). Boxes A and E alone need page 1 only. Otherwise let the IRS compute and leave Form 1040 line 38 blank.

**Citation**: Form 2210 page 1 flowchart and Part II; 2025 Instructions for Form 2210, "The IRS Will Figure the Penalty for You".

## 2. Using the wrong prior-year tax figure on Line 8

**Mistake**: Filer uses prior-year *balance owed at filing* as Line 8 figure, instead of prior-year *tax* (prior Form 1040 line 22 plus the Schedule 2 taxes listed in the line 8 instructions, minus the listed refundable credits).

**Why it happens**: Filers remember "I owed $X last year" but conflate balance owed with total tax.

**Fix**: Line 8 uses prior-year *total tax* (the full federal tax burden), not balance owed. A filer with $50K total tax and $48K withholding owes $2K at filing — but the safe harbor figure is 100% of $50K = $50K, not $2K.

**Citation**: Form 2210 Instructions, Line 8 worksheet; IRC §6654(d)(1)(B)(ii).

## 3. Applying 100% safe harbor when prior AGI > $150K (should be 110%)

**Mistake**: Filer with prior AGI of $200K applies 100% × prior tax as safe harbor; falls short, owes penalty.

**Why it happens**: 100% is the default rule; the 110% bump is a separate provision under IRC §6654(d)(1)(C) that filers and software sometimes miss.

**Fix**: Check prior-year AGI. If > $150,000 (or > $75,000 for MFS), use 110% × prior-year tax for Line 8.

**Citation**: IRC §6654(d)(1)(C).

## 4. Treating a Q4 estimated payment as back-filling earlier underpayments

**Mistake**: Filer paid $0 in Q1, Q2, Q3, then made a $20,000 estimated payment on January 15. Assumes "I paid the required annual amount by year-end, so no penalty."

**Why it happens**: Logical but wrong. The penalty is computed quarter-by-quarter; year-end totals don't undo earlier underpayments.

**Fix**: Each quarter's underpayment accrues penalty from its own due date. The January 15 payment is applied first to the Q1, Q2, and Q3 underpayments (stopping their penalty on January 15), then to Q4. It does NOT retroactively cure the penalty those quarters accrued before January 15.

**Citation**: IRC §6654(b)(2), (b)(3); Form 2210 Part III lines 12–17.

## 5. Forgetting that withholding allocates evenly by default

**Mistake**: Filer with all $40K of W-2 withholding concentrated in Q4 (year-end bonus with massive withholding) computes "all $40K applies to Q4" against actual quarterly required installments. Fails Q1/Q2/Q3 cumulative requirements.

**Why it happens**: Filer reads withholding column literally — it was actually withheld in Q4.

**Fix**: Default treatment under IRC §6654(g)(1) is *evenly across the year*. The $40K is treated as $10K per quarter for the safe harbor test. This benefits the filer in this scenario — they're better off with the default than with actual-date treatment.

**Citation**: IRC §6654(g)(1); Form 2210 Part III line 11 instructions.

But note: filers can use actual withholding dates if that lowers the penalty. A filer with concentrated withholding in Q1 (e.g., a year-end bonus paid in early January for the prior year's work) might prefer actual dates. Check box D in Part II, enter withholding by actual dates on line 11, and attach Form 2210.

## 6. Not using Schedule AI when income is back-loaded

**Mistake**: Filer with $0 Q1, $80K Q4 lets IRS compute the penalty (regular method); pays about $948 when Schedule AI would have produced about $447 (worked example in `annualized-income-method.md`).

**Why it happens**: Filer doesn't know Schedule AI exists; or knows but assumes it's too complex.

**Fix**: When income is materially back-loaded (one quarter > 40% of annual), compute Schedule AI. The agent should always offer to compute it when the income pattern is uneven.

**Citation**: IRC §6654(d)(2); Form 2210 Schedule AI.

## 7. Using Schedule AI when income is even

**Mistake**: Filer with steady $25K/quarter income spends hours on Schedule AI, hoping to reduce penalty. With even income the annualized amounts are about the same as (or higher than) the regular installments, line 27 falls back to the regular amounts, and nothing is saved.

**Why it happens**: Filer assumes Schedule AI always helps.

**Fix**: Compute both methods. Schedule AI helps only when income is uneven (back-loaded). For steady income, the regular method's 25% per quarter is roughly right and Schedule AI doesn't improve on it.

**Citation**: Form 2210 Schedule AI structure.

## 8. Claiming a waiver without supporting documentation

**Mistake**: Filer checks Box A (waiver of the entire penalty, e.g. after retiring at 63) without attaching a written explanation or supporting documents. IRS denies the waiver and bills the full penalty.

**Why it happens**: Filer thinks the checkbox alone is sufficient.

**Fix**: Box A and Box B waivers require:
- A written statement explaining the basis for the waiver
- Supporting documentation (retirement date and age on that date, disability date, police and insurance reports for a casualty)
The IRS reviews waiver claims; missing documentation = denial. Federally declared disasters are the exception: the IRS applies that relief automatically, and Form 2210 is generally not filed for it.

**Citation**: 2025 Instructions for Form 2210, Waiver of Penalty; IRC §6654(e)(3).

## 9. Computing penalty against the wrong "underpayment" figure

**Mistake**: Using *balance owed at filing* (current-year tax minus withholding minus estimates) as the "underpayment" rather than the Part III line 17 figure for each column.

**Why it happens**: Conflating "underpayment" (a Form 2210 term meaning quarter-specific shortfall against required installment) with "balance owed at filing" (a Form 1040 term).

**Fix**: Each quarter has its own underpayment computation against its own required installment. The penalty is computed separately per quarter. Total balance owed at filing is a different concept and may be larger, smaller, or equal to the sum of quarterly underpayments depending on payment timing.

**Citation**: Form 2210 Part III worksheet; IRC §6654(a).

## 10. Filing Form 2210 with prior-year tax of zero

**Mistake**: Filer with zero prior-year tax (recent graduate, first-year filer) files Form 2210 anyway, computing required annual payment as 90% of current-year tax. Pays a penalty that doesn't apply.

**Why it happens**: The no-prior-year-liability exception under IRC §6654(e)(2) is not always surfaced clearly in tax software wizards.

**Fix**: If prior-year tax was *zero* AND prior year was a full 12-month return AND filer was a US citizen/resident for the full prior year, no penalty applies regardless of how short withholding fell. Don't file Form 2210.

**Citation**: IRC §6654(e)(2).

## 11. Computing the penalty with stale rates

**Mistake**: Agent uses the prior year's penalty rate table because that's what's saved in memory. The rate has changed for the current year.

**Why it happens**: Rates change quarterly; filers and agents sometimes default to recent figures.

**Fix**: Always pull the rates from the current-year Form 2210 instructions penalty worksheet before computing (2025: 0.07 in every rate period; 2026 so far: 7%, 6%, 7%, 7% by quarter). Rates are set per IRC §6621; the current Revenue Ruling controls.

**Citation**: IRC §6621; current-year Form 2210 instructions penalty worksheet; https://www.irs.gov/payments/quarterly-interest-rates.

## 12. Confusing Form 2210 with Form 843

**Mistake**: Filer paid a penalty assessed by the IRS in a prior year and wants to dispute it; uses Form 2210 to "recompute" the penalty.

**Why it happens**: Form 2210 is the form for penalties on the current return. Form 843 is for refund claims and abatement requests on already-paid penalties.

**Fix**: For a paid penalty: file Form 843 (Claim for Refund and Request for Abatement) with documentation. For a current-year penalty being computed for the first time: Form 2210 (or let IRS compute).

**Citation**: Form 843; Form 2210 scope.

## 13. Using Form 2210 when the filer is a farmer/fisherman

**Mistake**: Filer with at least 2/3 of gross income from farming uses Form 2210 with regular quarterly schedule. Should use Form 2210-F.

**Why it happens**: Farmer/fisherman special rules are easy to miss.

**Fix**: If at least 2/3 of gross income for the current or prior year is from farming or fishing, use **Form 2210-F** (separate form) with its single annual installment due January 15. No penalty at all if the return is filed and the tax paid by March 1 (March 2, 2026 for 2025 returns).

**Citation**: IRC §6654(i); Form 2210-F.

## 14. Forgetting that married filers each need their own first-year analysis (joint return)

**Mistake**: Couple files MFJ for the first time; one spouse had prior-year tax of zero (first job, fully covered by deductions) and the other had $30K. Filer claims first-year exception based on "one spouse had zero".

**Why it happens**: First-year exception is at the *return* level, not the filer level.

**Fix**: For an MFJ return, the prior-year tax for safe harbor purposes is the *joint* prior-year tax (or, if filers were not married last year, the sum of each spouse's prior-year tax computed on their separate prior-year returns). One spouse having zero doesn't qualify the joint return for the exception.

**Citation**: IRC §6654(d)(1)(B); Form 2210 Instructions, joint return rules.

## 15. Including the penalty itself on Line 1 (current-year tax)

**Mistake**: Filer who paid an estimated tax penalty in a prior year, or who is computing this year's penalty, accidentally includes the penalty in Line 1 (current-year total tax).

**Why it happens**: Confusion about what counts as "tax."

**Fix**: Line 1 is Form 1040 line 22 (tax after credits). The estimated tax penalty itself is on Form 1040 line 38 — separate from line 1. Don't double-count.

**Citation**: 2025 Instructions for Form 2210, Line 1; Form 1040 line 38.

## Sources

- IRC §6654, §6621, §6622(b), §1274(d)
- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf)
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf)
- [Form 2210-F](https://www.irs.gov/forms-pubs/about-form-2210-f) (farmers and fishermen variant)
- [Form 843](https://www.irs.gov/pub/irs-pdf/f843.pdf) (refund/abatement claims)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf)
