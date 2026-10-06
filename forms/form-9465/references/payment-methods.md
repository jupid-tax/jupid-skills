# Payment Methods, Payment Day, and Keeping the Agreement Alive

How the user will pay under the agreement (lines 12, 13a, 13b, 13c, 14), what to send with a standalone request, and what ends an agreement. Use this file when filling lines 12–14 and when writing the "next steps" section of the draft.

Sources:
- Form 9465 (Rev. September 2020): https://www.irs.gov/pub/irs-pdf/f9465.pdf
- Instructions for Form 9465 (Rev. July 2024): https://www.irs.gov/pub/irs-pdf/i9465.pdf
- IRS, Payment plans; installment agreements (last reviewed 13-Aug-2026): https://www.irs.gov/payments/payment-plans-installment-agreements
- Form 2159, Payroll Deduction Agreement: https://www.irs.gov/pub/irs-pdf/f2159.pdf

---

## 1. Choosing the method

| Method | Form 9465 lines | Required when | Fee effect (Form 9465 = paper channel) |
|--------|-----------------|---------------|-----------------------------------------|
| Direct debit from checking (DDIA) | 13a, 13b | Line 9 > $25,000 and ≤ $50,000 without Form 433-F, unless payroll deduction is used | $107 (vs $178 non-DDIA); waived for low-income |
| Payroll deduction | 14 + Form 2159 | Alternative to direct debit for the $25,001–$50,000 tier | i9465 states $178 from July 1, 2024 |
| Check, money order, card, Direct Pay, EFTPS each month | none | User's choice when not required to use 13 or 14 | $178; $43 for low-income, reimbursable only if 13c is checked |

Ask the user which method they want. Do not default to direct debit, even though it is cheaper and harder to miss, because it requires their explicit authorization (see section 2).

## 2. Direct debit (lines 13a and 13b)

Rules from i9465 "Lines 13a, 13b, and 13c":
- The account must be a checking account at a bank or other financial institution (the instructions name mutual funds, brokerage firms, and credit unions as possible institutions). The user should confirm with the institution that direct debit is allowed and get the correct numbers.
- **13a routing number**: exactly 9 digits; the first two digits must be 01–12 or 21–32. If the check is payable through a different institution, get the routing number from the bank, not from the check.
- **13b account number**: up to 17 characters (numbers and letters); include hyphens; omit spaces and special symbols; enter left to right; leave unused boxes blank; never include the check number.
- The direct debit is not approved unless the user (and the spouse on a joint return) signs Form 9465.
- The printed authorization stays in force until the user tells the U.S. Treasury Financial Agent to stop. To revoke a payment, the user contacts the Financial Agent at 1-800-829-1040 no later than 14 business days before the payment (settlement) date (form text under line 13).
- Under direct debit, the IRS does not mail monthly notices; the bank statement is the payment record. The IRS still sends an annual statement (i9465 "After approving your request").

Validation the agent runs on the numbers the user types:
- Routing: `len == 9`, all digits, `int(first two) in 1..12 or 21..32`.
- Account: `1 <= len <= 17`, only letters, digits, hyphens.
- Read both back to the user for confirmation. Do not "fix" a number; ask.

Security: collect bank numbers only at the moment of filling the form, never echo them into logs, summaries, or memory, and mask them in the draft (for example `•••••6021`) unless the user asks to see the full numbers to transcribe.

## 3. Low-income box (line 13c)

- Check 13c only when the user is low-income (AGI for the most recent year available at or below 250% of the federal poverty guidelines) **and** cannot make electronic payments through a debit instrument.
- Effect: the reduced $43 fee is reimbursed on completion of the agreement.
- A low-income user who can use direct debit should fill 13a/13b instead; the fee is then waived.
- Leaving 13a, 13b, and 13c all blank means the user is able but choosing not to pay electronically; the fee is not reimbursable.
- Determining low-income status uses the Form 13844 table (see `agreement-types-and-fees.md`, section 4). Ask the user for AGI and family unit size from their most recent return; never infer them.

## 4. Payroll deduction (line 14)

- Check line 14 and attach a completed, signed Form 2159.
- The employer completes and signs the employer's portion of Form 2159 (i9465 "Line 14"). The agent cannot complete the employer portion; tell the user to get it from payroll or HR before mailing.

## 5. Payment day (line 12)

- Any day from the 1st through the 28th of the month (form text; i9465 "Line 12"). The instructions suggest picking a day that does not collide with rent or mortgage, for example the 15th when rent is due on the 1st.
- Ask the user for the day; do not pick one.
- The IRS tells the user the month and day of the first payment when it approves the request.
- If the IRS has not replied by the date the user chose for the first payment, the user can mail the first payment to the service center address that applies (the standalone-filing tables in `../filing.md`), using the check details in section 6, or pay electronically at IRS.gov/Payments.

## 6. Payment sent with a standalone request (line 8)

From i9465 "Line 8":
- With a tax return: pay with the return as the return instructions say.
- Standalone (for example in response to a notice): attach a check or money order payable to **"United States Treasury"**. Do not send cash. Include:
  - name, address, SSN/EIN, and daytime phone number;
  - the tax year and tax return the payment is for (for example, "2023 Form 1040").

The irs.gov payment plans page repeats the same items for monthly check payments (name, address, SSN, daytime phone, tax year, return type).

## 7. What the user agrees to

From i9465 "How the Installment Agreement Works" and "Requests to modify or terminate":
- Make each monthly payment on time.
- Meet all future tax obligations: enough withholding or estimated tax so future years are paid in full when the return is timely filed (route estimated tax to `../../form-1040-es/SKILL.md`).
- Timely file future returns.
- Provide updated financial information when requested.
- Refunds are applied to the balance; the regular payment is still due in the month a refund is applied.

## 8. Default and termination

- Missing payments or not paying a balance due on a later return puts the agreement in default; the IRS may terminate it. Before termination, the user may be entitled to appeal through the Collection Appeals Program (CAP). After termination, the IRS may file an NFTL or levy (i9465).
- Materially incomplete or inaccurate information given to obtain the agreement, or in response to a financial update request, can lead to termination. For a terminated agreement, see IRS.gov/CP523 (i9465 caution).
- A reinstatement fee may apply after default (irs.gov payment plans page). Current online revise/reinstate fee: $6; phone/mail: $89; low-income: $43 phone/mail or $6 online, may be reimbursed (irs.gov payment plans page, updated March 3, 2026). The 7-2024 instructions show $10 for an OPA reinstatement; use the irs.gov figure.
- Changes to an existing direct-debit agreement: $0 (irs.gov).

## 9. Modifying the agreement

- Online through IRS.gov/OPA or the IRS Online Account: change the monthly amount, change the due date, convert to direct debit, change the bank account on a direct-debit agreement, reinstate after default (irs.gov payment plans and OPA pages).
- By phone: 800-829-1040 (individuals), 800-829-4933 (business).
- If a revised amount does not meet the minimum, the IRS directs the user to Form 433-H, Form 433-F, or Form 433-B (irs.gov payment plans page).

## 10. Where payments go after approval

Payments are sent where the IRS correspondence says (irs.gov payment plans page: "When you send payments by mail, send them to the address listed in your correspondence"). The standalone filing addresses in `../filing.md` are for the request and for a first payment sent before the IRS replies.
