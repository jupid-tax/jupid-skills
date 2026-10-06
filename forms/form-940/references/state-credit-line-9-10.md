# State Unemployment Credit, Line 9, and the Line 10 Worksheet

How the 5.4% credit for state unemployment tax works on Form 940, when line 9 or line 10 applies, and how to run the Worksheet—Line 10. Built from the 2025 Instructions for Form 940 (I940), "Credit for State Unemployment Tax Paid to a State Unemployment Fund", line 9, line 10, and the worksheet on page 12; the 2026 draft instructions keep the same worksheet.

Authority: IRC §3301 (6.0% tax), IRC §3302(a) (credit for contributions paid; contributions paid after the Form 940 due date earn at most 90% of the credit they would have earned), IRC §3302(b) (additional credit for a reduced experience rate), IRC §3302(c)(1) (total credits capped at 90% of the tax, which is 5.4% of wages).

---

## 1. The baseline

FUTA is 6.0% of the first $7,000 of each employee's FUTA wages. Line 8 computes line 7 × 0.006, which already assumes the maximum 5.4% credit. Lines 9 and 10 add back credit the employer did not earn. Line 11 adds back credit taken away by a credit reduction.

The maximum credit is available if the employer paid all state unemployment tax by the due date of Form 940, or owed none because of a state experience rate (I940, "Figure Your Tax Liability").

## 2. What counts as state unemployment tax ("contributions")

Count: payments a state requires an employer to make to its unemployment fund, including tax paid on nonemployees the state treats as employees, and (for a successor) the special credit amounts under IRC §3302(e).

Do not count (I940; worksheet caution):

- Amounts deducted or deductible from employees' pay
- Penalties, interest, or special administrative taxes
- Voluntary contributions paid to get a lower assigned rate
- Surcharges, excise taxes, or employment and training taxes, which states usually list separately on the quarterly report

Ask the user for each state's report or account statement and separate these items before using any number.

## 3. "On time" for FUTA is the Form 940 due date, not the state due date

"On time" means paid by the due date for filing Form 940: February 2, 2026 for the 2025 return (or February 10, 2026 if that is your due date because all FUTA was deposited when due); February 1, 2027 for the 2026 return (or February 10, 2027). State tax paid late to the state but by that date still earns the full credit. This is true regardless of whether state law defers payment past that date (I940, "Credit for State Unemployment Tax Paid to a State Unemployment Fund").

## 4. Decide between line 9, line 10, or neither

```
Were ALL taxable FUTA wages excluded from state unemployment tax
(not merely taxed at a 0% assigned rate)?
  Yes → Line 9 = line 7 × 0.054. Leave lines 10 and 11 blank. No worksheet.
  No  → Were SOME FUTA wages excluded from state unemployment tax,
        or was ANY state unemployment tax paid after the Form 940 due date
        (including tax still unpaid at filing)?
          Yes → Run the Worksheet—Line 10. Enter worksheet line 7 on line 10
                (it may come out zero; then leave line 10 blank).
          No  → Lines 9 and 10 blank.
```

Examples of wages a state may exclude: corporate officer wages in certain states, certain union sick pay, certain fringe benefits (I940, "Figure Your Tax Liability"; Pub. 15 (2026), section 14). Never assume a state's rule; ask the user to confirm from the state agency or the state wage report.

## 5. Inputs the worksheet needs (ask for each)

- Form 940 line 7
- Taxable state unemployment wages (the state wage base may differ from $7,000)
- Every experience rate the state assigned for any part of the year, with the period
- State unemployment tax paid on time (by the Form 940 due date)
- State unemployment tax paid late (after the Form 940 due date)
- State unemployment tax still unpaid (not used in the worksheet but needed to explain the result)

Do not round any worksheet figure (I940 worksheet heading).

## 6. Worksheet—Line 10 (I940, page 12)

| Line | Computation | Stop rule |
|---|---|---|
| 1 | Maximum allowable credit = Form 940 line 7 × 0.054 | |
| 2 | Credit for timely state unemployment tax payments = amount paid on time | If line 2 ≥ line 1, stop; leave Form 940 line 10 blank |
| 3 | Additional credit: if every assigned rate was 5.4% or more, enter 0. Otherwise, for each state and rate period with a rate under 5.4%: taxable state unemployment wages at that rate × (0.054 − assigned rate). Total the rows. Six or more rates under 5.4% → use another sheet and carry the total. | |
| 4 | Subtotal = line 2 + line 3 | If line 4 ≥ line 1, stop; leave line 10 blank |
| 5a | Remaining allowable credit = line 1 − line 4 | |
| 5b | State unemployment tax paid late | |
| 5c | Smaller of 5a or 5b | |
| 5d | Allowable credit for late payment = line 5c × 0.900 | |
| 6 | FUTA credit = line 4 + line 5d | If line 6 ≥ line 1, stop; leave line 10 blank |
| 7 | Adjustment = line 1 − line 6 | Enter on Form 940 line 10 |

Keep the worksheet with the records. Do not attach it.

## 7. The IRS example, recomputed

Facts (I940, "Example for Using the Worksheet"): Jill Brown and Tom White are corporate officers whose wages the state excludes; Jack Davis's wages are not excluded. Paid in 2025: Jill $44,000, Tom $22,000, Jack $16,000. State wage base $8,000. Taxable FUTA wages (Form 940 line 7) $21,000. Taxable state wages $8,000. Experience rate 0.041. State tax paid on time $100.00, paid late $78.00, unpaid $150.00.

| Line | Computation | Result |
|---|---|---|
| 1 | 21,000.00 × 0.054 | 1,134.00 |
| 2 | Paid on time | 100.00 |
| 3 | 8,000 × (0.054 − 0.041 = 0.013) | 104.00 |
| 4 | 100.00 + 104.00 | 204.00 |
| 5a | 1,134.00 − 204.00 | 930.00 |
| 5b | Paid late | 78.00 |
| 5c | Smaller of 5a, 5b | 78.00 |
| 5d | 78.00 × 0.900 | 70.20 |
| 6 | 204.00 + 70.20 | 274.20 |
| 7 | 1,134.00 − 274.20 | 859.80 → Form 940 line 10 |

Form 940 then shows line 8 = 21,000 × 0.006 = 126.00 and line 12 = 126.00 + 859.80 = 985.80 (before any credit reduction).

Check of the example's own consistency: state tax due = 8,000 × 0.041 = 328.00 = 100.00 + 78.00 + 150.00.

## 8. Why a low experience rate can absorb a late or unpaid amount

When taxable state wages are at least as large as FUTA wages and the assigned rate is under 5.4%, line 3 (additional credit) can be large. If line 2 + line 3 reaches line 1, the worksheet stops at line 4 and line 10 stays blank even though some state tax was paid late. The worksheet decides; do not shortcut it. The additional credit under IRC §3302(b) is measured on contributions required at the assigned rate, so the user still owes the state the unpaid amount.

## 9. Fixing it later

If state tax is paid after the Form 940 was filed, the employer may file an amended Form 940 (box a) for that year to claim the 90% late-payment credit. The instructions give this as an example of a reason to amend: "tell us if you're filing to claim credit for tax paid to your state unemployment fund after the due date of Form 940" (I940, "Can You Amend a Return?"). Recompute the worksheet with the late payment on line 5b, attach an explanation, and follow [`../filing.md`](../filing.md) for where to send it.

## 10. Questions to ask, verbatim

- "For each state, what experience rate did the state assign you this year, and did it change during the year?"
- "What were your taxable state unemployment wages for the year in each state? Please use the state wage reports, not gross payroll."
- "How much state unemployment tax did you pay on or before [Form 940 due date], and how much after? Leave out penalties, interest, administrative or training surcharges, and anything withheld from employees."
- "Did your state exclude any of your employees' wages from unemployment tax, for example corporate officers? If yes, which employees and how much?"
