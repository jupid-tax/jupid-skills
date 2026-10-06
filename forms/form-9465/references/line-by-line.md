# Form 9465 Line-by-Line Reference

Every field on Form 9465, Installment Agreement Request, in the order it appears on the form. Built from the text of **Form 9465 (Rev. September 2020)** and the **Instructions for Form 9465 (Rev. July 2024)**, which are the current revisions listed on https://www.irs.gov/forms-pubs/about-form-9465 (page last reviewed 29-Apr-2026). Re-check that page before use; if either revision date has changed, rebuild this map from the new PDF text.

Sources:
- Form: https://www.irs.gov/pub/irs-pdf/f9465.pdf
- Instructions: https://www.irs.gov/pub/irs-pdf/i9465.pdf

The form has two pages. Part I (page 1) is required for every request. Part II (page 2) is required only in one narrow case (see Part II below).

---

## Header (top of page 1)

### "This request is for Form(s)"

Enter the return type(s) that created the balance, for example "1040" or "1040, 941". The form's own example reads "Form 1040 or Form 941".

- Use the form number that appears on the IRS notice or account transcript for each balance.
- Employment-tax returns (941, 943, 940) belong here only when they relate to a sole proprietor business that is **no longer operating** (i9465, "Who should use this form?").

### "Enter tax year(s) or period(s) involved"

The form's example reads "2018 and 2019, or January 1, 2019, to June 30, 2019". List every year or quarter whose balance is included on line 5 or line 6.

- Annual returns: the year (for example, "2024 and 2025").
- Quarterly returns: the quarter-ending dates or the date range.

---

## Line 1a — Names, SSNs, address

Fields:
- Your first name and initial / Last name / Your social security number
- If a joint return: spouse's first name and initial / Last name / Spouse's social security number
- Current address (number and street); P.O. box only if there is no home delivery; Apt. number
- City, town or post office, state, and ZIP code
- Foreign country name / Foreign province/state/county / Foreign postal code

Rules from the instructions:
- For a joint return, show the names and SSNs **in the same order as they appear on the tax return**.
- Foreign address: enter the city name on the city line only, then complete the three foreign-address spaces. Do not abbreviate the country name. Follow the country's practice for postal code and province.

## Line 1b — New address checkbox

Check the box if the address on line 1a is new since the last tax return was filed. Leave unchecked otherwise.

## Line 2 — Business name and EIN

"Name of your business (must no longer be operating)" and "Employer identification number (EIN)".

- Fill only when a balance on line 5 or 6 comes from a sole proprietor business that has **stopped operating** (for example, Form 941 balances of a closed business).
- An operating business that owes employment or unemployment taxes must not use Form 9465; it calls the number on its most recent notice (i9465, "Who should not use this form?").
- Leave blank when the balance is income tax only.

## Line 3 — Home phone

"Your home phone number" and "Best time for us to call".

## Line 4 — Work phone

"Your work phone number", "Ext.", and "Best time for us to call".

---

## Line 5 — Total amount owed per return(s) or notice(s)

"Enter the total amount you owe as shown on your tax return(s) (or notice(s))." The instructions add that the amount can include more than one tax year.

- Take the figure from the return being filed (the "amount you owe" line) or from the most recent IRS notice for each period. Do not estimate. If the user has neither, ask them to pull an account transcript (see `../../form-4506-t/SKILL.md`) or log in to their IRS Online Account.

## Line 6 — Additional balances not on line 5

"If you have any additional balances due that aren't reported on line 5, enter the amount here (even if the amounts are included in an existing installment agreement)."

- The instructions add: any adjustments or other charges not reported on a tax return or notice go here.
- Include balances already in an existing agreement. The request covers the user's total liability.

## Line 7 — Total

Line 5 + line 6.

## Line 8 — Payment sent with the request

"Enter the amount of any payment you're making with this request."

- With a return: make the payment with the return per the return's instructions.
- Standalone (for example, answering a notice): attach a check or money order payable to "United States Treasury". Do not send cash. Write on it the name, address, SSN/EIN, daytime phone, and the tax year and return (for example, "2023 Form 1040"), per i9465 "Line 8".
- Enter 0 if no payment is sent.

## Line 9 — Amount owed

Line 7 − line 8.

Thresholds tied to line 9 (i9465, "Line 9" caution and "Line 11b"):
- Over $25,000 but not more than $50,000: to qualify as streamlined without Form 433-F, the user must either complete lines 13a and 13b (direct debit) or check box 14 and attach a signed Form 2159 (payroll deduction).
- Greater than $50,000: complete and attach Form 433-F, Collection Information Statement.
- Not more than $50,000 including prior-year amounts: the user does not need Form 9465 and can apply online at IRS.gov/OPA (i9465 tip under "Line 9").

## Line 10 — Line 9 ÷ 72.0

"Divide the amount on line 9 by 72.0 and enter the result."

- This is the form's benchmark payment: the balance spread over 72 months, with no allowance for future interest or penalties.
- Round to cents. Compare line 11a (or 11b) against it.

## Line 11a — Proposed monthly payment

"Enter the amount you can pay each month."

- The form says to make the payment as large as possible because interest and penalty charges continue until the balance is paid.
- If the user has an existing installment agreement, line 11a is the **total** proposed monthly payment for all liabilities.
- If line 11a is left blank, the IRS sets the payment by dividing the line 9 balance by 72 months (form text; i9465 "Line 11a").
- If the proposed payment will not pay the balance in full by the Collection Statute Expiration Date (CSED), the request may be considered for a partial payment installment agreement (PPIA), which requires a financial statement (i9465 "Line 11a" and "Partial payment installment agreement").
- Never fill line 11a with a number the user did not state. Ask.

## Line 11b — Revised payment and the 433-F checkbox

"If the amount on line 11a is less than the amount on line 10 and you're able to increase your payment to an amount that is equal to or greater than the amount on line 10, enter your revised monthly payment."

Below the entry line, three bullets:
1. If the user cannot raise the payment to at least line 10: **check the box** and complete and attach **Form 433-F**.
2. If line 11a (or 11b) is at least line 10 and the amount owed is over $25,000 but not more than $50,000: Form 433-F is not required, but if it is not completed, the user **must complete line 13 or line 14**.
3. If line 9 is greater than $50,000: complete and attach **Form 433-F**.

The instructions (i9465 "Line 11b") add a fourth bullet: if the user defaulted on an installment agreement within the last 12 months, owes more than $25,000 but not more than $50,000, and line 11a (or 11b) is less than line 10, the user must complete **Part II** on page 2. That bullet does not displace bullet 1, so in that case prepare Part II and Form 433-F.

## Line 12 — Payment day

"Enter the date you want to make your payment each month. Don't enter a date later than the 28th."

- Any day from the 1st through the 28th (i9465 "Line 12").
- The IRS states the first due date in its approval. If the IRS has not replied by the chosen date, the user may send the first payment to the service center address that applies (see `filing.md`) or pay at IRS.gov/Payments.

---

## Line 13 — Direct debit

"If you want to make your payments by direct debit from your checking account, see the instructions and fill in lines 13a and 13b."

### Line 13a — Routing number

- Nine digits. The first two digits must be 01 through 12 or 21 through 32 (i9465 "Line 13a").
- If the check is payable through a different institution than the one holding the account, do not use the routing number printed on the check; the user must get the correct number from the bank.

### Line 13b — Account number

- Up to 17 characters, numbers and letters. Include hyphens; omit spaces and special symbols. Enter left to right and leave unused boxes blank. Do not include the check number (i9465 "Line 13b").

### Authorization text (printed under 13a/13b)

The user authorizes the U.S. Treasury and its Financial Agent to initiate monthly ACH debits. The authorization stays in effect until the user notifies the Financial Agent. To revoke a payment, the user must contact the Financial Agent at 1-800-829-1040 **no later than 14 business days before the payment (settlement) date**. The direct debit is not approved unless the user (and spouse, if a joint return) signs Form 9465 (i9465 caution under "Line 13b").

### Line 13c — Low-income taxpayers unable to use direct debit

Check only if the user is a low-income taxpayer (AGI for the most recent tax year at or below 250% of the federal poverty guidelines) and is **unable** to make electronic payments through a debit instrument. The user fee is then reimbursed when the agreement is completed. If 13c is not checked and 13a/13b are blank, the user is treated as able but choosing not to pay electronically, and the fee is not reimbursable (i9465 "Line 13c").

## Line 14 — Payroll deduction

Check the box to pay by payroll deduction and attach a completed and signed **Form 2159**, Payroll Deduction Agreement. The employer completes and signs the employer's portion of Form 2159 (i9465 "Line 14").

---

## Signature block

- "Your signature" and "Date".
- "Spouse's signature. If a joint return, both must sign." and "Date".
- The printed text above the signatures authorizes the IRS to contact third parties and disclose tax information to them to process and administer the agreement, and states the user agrees to the terms in the instructions if approved.
- The user signs. The agent never signs or generates a signature.

---

## Part II — Additional Information (page 2)

Complete Part II **only if all three** are true (form text and i9465 "Part II"):
1. The user defaulted on an installment agreement in the past 12 months;
2. The user owes more than $25,000 but not more than $50,000; and
3. Line 11a (or 11b, if applicable) is less than line 10.

The form adds: if the user owes more than $50,000, also complete and attach Form 433-F.

| Line | Question | Notes |
|------|----------|-------|
| 15 | County of primary residence | |
| 16a | Marital status: Single (skip 16b, go to 17) or Married (go to 16b) | |
| 16b | Do you share household expenses with your spouse? Yes / No | |
| 17 | How many dependents will you be able to claim on this year's tax return? | |
| 18 | How many people in your household are 65 or older? | |
| 19 | How often are you paid? Once a week / Once every 2 weeks / Once a month / Twice a month | |
| 20 | Net income per pay period (take-home pay) | Dollar amount |
| 21 | How often is your spouse paid? (same four choices) | Only if the spouse conditions below apply |
| 22 | Spouse's net income per pay period (take-home pay) | Only if the spouse conditions below apply |
| 23 | How many vehicles do you own? | |
| 24 | How many car payments do you have each month? | |
| 25a | Do you have health insurance? Yes (go to 25b) / No (skip to 26a) | |
| 25b | Are premiums deducted from your paycheck? Yes (skip to 26a) / No (go to 25c) | |
| 25c | Monthly health insurance premiums | Dollar amount |
| 26a | Do you make court-ordered payments? Yes (go to 26b) / No (go to 27) | |
| 26b | Are court-ordered payments deducted from your paycheck? Yes (go to 27) / No (go to 26c) | |
| 26c | Court-ordered payments each month | Dollar amount |
| 27 | Monthly child or dependent care, not counting court-ordered child and dependent support | Dollar amount |

### Lines 21 and 22 — when to complete

Complete them if the user is married and either (i9465 "Lines 21 and 22"):
- lives with and shares household expenses with the spouse, even if only one spouse owes the tax; or
- lives in a community property state, where a non-liable spouse's income may be factored into ability to pay.

Complete them whether the filing status is married filing jointly or married filing separately.

---

## Quick math map

```
Line 7  = Line 5 + Line 6
Line 9  = Line 7 − Line 8
Line 10 = Line 9 ÷ 72.0
Compare Line 11a (or 11b) with Line 10
Line 9 > $50,000                               → Form 433-F required
$25,000 < Line 9 ≤ $50,000 and 11a/11b ≥ Line 10 → Line 13 or Line 14 required unless 433-F attached
11a/11b < Line 10 and cannot be raised         → check 11b box + Form 433-F
Defaulted IA in last 12 months, $25,000 < Line 9 ≤ $50,000, 11a/11b < Line 10 → Part II as well
```
