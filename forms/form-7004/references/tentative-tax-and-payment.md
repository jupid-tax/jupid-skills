# Form 7004 Lines 6 to 8: Tentative Tax, Payments, and the Cost of Paying Late

Form 7004 extends the time to **file**. It never extends the time to **pay**. This file covers how to estimate line 6, what goes on line 7, how to pay line 8, and what happens when the payment is short.

Primary sources: Instructions for Form 7004 (Rev. December 2025), https://www.irs.gov/pub/irs-pdf/i7004.pdf (Payment of Tax; Part II, lines 6 to 8); Treas. Reg. §1.6081-3 (corporations); 2025 Instructions for Forms 1065, 1120-S, and 1120; Rev. Proc. 2024-40 and Rev. Proc. 2025-32 (penalty amounts). Re-verify every dollar amount each year.

---

## Why line 6 matters

- The extension is granted only if the entity makes "a proper estimate of the tax (if applicable)" and pays "any tax that is due" (i7004, Purpose of Form).
- For corporations the regulation makes payment a condition: the corporation "must remit the amount of the properly estimated unpaid tax liability on or before the date prescribed for payment" (Treas. Reg. §1.6081-3(a)(3)).
- For corporations, line 6 also decides whether a late-payment penalty applies after the extension (90% rule below).

Do not invent the estimate. Ask the user (or their preparer) for the projected figures and show the arithmetic.

---

## Estimating line 6 by return type

i7004: "Enter the total tax, including any nonrefundable credits, the entity expects to owe for the tax year ... If you expect this amount to be zero, enter -0-."

### Form 1065 (code 09)

A partnership generally owes no income tax. Line 6 is -0- unless the return will show an amount on these 2025 Form 1065 lines:
- Line 24, look-back interest, completed long-term contracts (Form 8697)
- Line 25, look-back interest, income forecast method (Form 8866)
- Line 26, BBA AAR imputed underpayment
- Line 27, other taxes

Line 28 ("Total balance due. Add lines 24 through 27") is the figure being estimated. Ask: "Will the 2026 Form 1065 show any look-back interest, an imputed underpayment from an administrative adjustment request, or other taxes on lines 24 through 27?" If the user does not know, stop and ask their preparer.

### Form 1120-S (code 25)

An S corporation generally owes no income tax. Line 6 is -0- unless the return will show tax on 2025 Form 1120-S:
- Line 23a, excess net passive income or LIFO recapture tax
- Line 23b, tax from Schedule D (Form 1120-S) (built-in gains tax)
- Line 23c, total (with any additional taxes the instructions list)

Ask: "Was the corporation ever a C corporation, or did it acquire assets from one in a tax-free transaction? Does it have accumulated earnings and profits and passive investment income?" A "no" to all supports -0-. Any "yes" goes to the user's preparer for the estimate; do not compute these taxes here.

### Form 1120 (code 12)

Line 6 is the expected total tax: the 2025 Form 1120 page 1, line 31, which equals Schedule J, line 12. Schedule J builds it as:
- Income tax (line 1a). The rate is 21% of taxable income (IRC §11(b)).
- Plus other Schedule J taxes the return will carry: corporate alternative minimum tax (line 3, Form 4626), personal holding company tax (line 8), recapture and look-back items (lines 9a to 9z)
- Minus nonrefundable credits (lines 5a to 5f: foreign tax credit, general business credit, prior-year minimum tax credit, and others)

Minimum inputs to ask for: projected taxable income for the year, any nonrefundable credits with their forms, and whether any other Schedule J tax applies. For a foreign-owned disregarded entity filing a pro forma Form 1120 with Form 5472, the tax is -0- (it has no income tax return filing requirement of its own; Instructions for Form 5472, Rev. December 2024).

### Form 1041 (codes 03, 04, 05)

Use the estate's or trust's projected total tax from its preparer. A trust or REMIC gets the extension even if it cannot pay all of line 8, but "it should pay as much as it can to limit the amount of penalties and interest it will owe" (i7004, Line 8).

### Other codes

Use the specific instructions for the return named on line 1 (i7004, Line 6). If the user cannot produce a figure, stop and ask.

---

## Line 7: payments and refundable credits

i7004: "Enter the total payments and refundable credits."

Typical components (2025 Form 1120, Schedule J lines 13 to 20z; 2025 Form 1120-S line 24):
- Prior year's overpayment credited to this year
- This year's estimated tax payments (less any refund applied for on Form 4466)
- Withholding credited to the entity
- Refundable credits (Form 2439, Form 4136 fuel tax credit, chapter 3 or 4 withholding)

Exclude the payment to be made with Form 7004. The return later reports it on its own line: Form 1120 Schedule J line 17 and Form 1120-S line 24b ("Tax deposited with Form 7004"); Form 1065 line 30 ("Payment").

---

## Line 8: paying the balance

- Line 8 = line 6 − line 7. Corporations pay it "on or before the due date of the return" (i7004, Line 8).
- **EFTPS.** "Most entities must use electronic funds transfer (EFT) to make all federal tax deposits, including deposits for corporate income taxes. Generally, EFTs are made using the Electronic Federal Tax Payment System (EFTPS)." Enrollment: EFTPS.gov or 800-555-4477 (i7004).
- **Third party.** A tax professional, financial institution, payroll service, or other trusted third party can deposit on the entity's behalf (i7004).
- **Electronic Funds Withdrawal (EFW).** Available only when Form 7004 is e-filed; the authorized person signs Form 8878-A with a PIN, the ERO keeps it, and it is not sent to the IRS. To revoke a scheduled payment, contact the U.S. Treasury Financial Agent at 1-888-353-4537 no later than 2 business days before the settlement date (Form 8878-A, Rev. December 2008).
- **Other options:** IRS.gov/Pay (i7004, What's New).
- **Foreign corporations** with no U.S. office follow the deposit rules in the Form 1120-F or Form 1120-FSC instructions; Form 1042 filers follow the Form 1042 deposit rules (i7004, Line 8).
- **Expected NOL carryback.** A corporation can reduce the deposit by the expected overpayment from the carryback if all prior-year liabilities are paid and Form 1138 is filed with Form 7004 (i7004). If Form 7004 is e-filed, Form 1138 goes separately (https://www.irs.gov/Efile7004).

---

## When the payment is short

### Failure-to-pay penalty (i7004, Payment of Tax)

"Generally, a penalty of 1/2 of 1% of any tax not paid by the due date is charged for each month or part of a month that the tax remains unpaid. The penalty cannot exceed 25% of the amount due." It is not charged with reasonable cause.

### Corporate 90% relief (i7004, Payment of Tax)

"If a corporation is granted an extension of time to file a corporation income tax return, it will not be charged a late payment penalty if the tax shown on Part II, line 6 (or the amount of tax paid by the regular due date of the return), is at least 90% of the tax shown on the total tax line of your return, and the balance due shown on the return is paid by the extended due date."

Test, in order:
1. Final total tax T (Form 1120 line 31 when the return is done).
2. A = the larger of Form 7004 line 6 and the tax actually paid by the original due date.
3. If A ≥ 0.90 × T **and** the remaining balance is paid by the extended due date, no failure-to-pay penalty.
4. Otherwise the 0.5% per month penalty runs on the unpaid tax from the original due date.

### Interest

"Interest is charged on any tax not paid by the regular due date of the return from the due date until the tax is paid. It will be charged even if you have been granted an extension or have shown reasonable cause for not paying on time" (i7004). The rate is set under IRC §6621 (2025 Instructions for Form 1120) and changes quarterly; look it up at https://www.irs.gov/payments/quarterly-interest-rates. Do not hard-code a rate.

### Estimated tax penalty is separate

Form 7004 does not touch the corporate estimated tax penalty for short quarterly installments during the year (IRC §6655; Form 2220; 2025 Form 1120 line 34). Flag it when line 7 is well below line 6; hand the computation to the return preparer.

### Counting "each month or part of a month"

Count monthly periods starting the day after the due date. A payment made after the same day-of-month as the due date starts a new month. Example: tax due April 15, 2027 and paid September 14, 2027 = 5 months (Apr 16 to May 15, May 16 to June 15, June 16 to July 15, July 16 to Aug 15, Aug 16 to Sept 14).

```python
def months_or_part(due, paid):
    # due, paid: datetime.date; returns count of months or parts of months after due
    if paid <= due:
        return 0
    m = (paid.year - due.year) * 12 + (paid.month - due.month)
    if paid.day > due.day:
        m += 1
    return m
```

Check edge cases by hand when the due date is the 29th to 31st of a month.

---

## Late-filing penalties a timely Form 7004 avoids (year-dependent)

A valid extension moves the date these penalties start from the original due date to the extended due date. Amounts are inflation-adjusted every year; re-check the current Revenue Procedure.

| Penalty | Returns required to be filed in 2026 | Returns required to be filed in 2027 | Source |
|---|---|---|---|
| Partnership return (IRC §6698), per partner per month or part, max 12 months | $255 | $260 | 2025 i1065, Late Filing of Return; Rev. Proc. 2024-40 §2.56; Rev. Proc. 2025-32 §4.55 |
| S corporation return (IRC §6699), per shareholder per month or part, max 12 months | $255 | $260 | 2025 i1120-S; Rev. Proc. 2024-40 §2.57; Rev. Proc. 2025-32 §4.56 |
| Income tax return more than 60 days late (IRC §6651(a)), minimum | lesser of $525 or 100% of the tax | lesser of $535 or 100% of the tax | 2025 i1120; Rev. Proc. 2024-40 §2.53; Rev. Proc. 2025-32 §4.52 |
| Corporate late filing (IRC §6651(a)(1)) | 5% of unpaid tax per month or part, max 25% | same | 2025 i1120, Late filing of return |

The §6698 and §6699 multipliers count every person who was a partner (or shareholder) at any time during the tax year (2025 i1065; 2025 i1120-S). The §6699 penalty adds 5% of unpaid tax per month when an S corporation return shows tax due (2025 i1120-S).

Rev. Proc. URLs: https://www.irs.gov/pub/irs-drop/rp-24-40.pdf and https://www.irs.gov/pub/irs-drop/rp-25-32.pdf.

---

## Reasonable cause

"If you receive a notice about a penalty after you file your return, send the IRS an explanation and we will determine if you meet reasonable-cause criteria. Do not attach an explanation when you file your return" (i7004). Penalty relief requests after a notice are outside this skill; see [`form-843`](../../form-843/SKILL.md).
