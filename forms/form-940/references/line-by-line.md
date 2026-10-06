# Form 940 Line-by-Line Reference

Every line and box on Form 940, built from the text of the 2025 Form 940 (Created 6/2/25) and the 2025 Instructions for Form 940 (dated Nov 18, 2025). The 2026 draft Form 940 (Created 3/25/26) has the same lines and wording; differences that matter for 2026 are noted inline. Re-check the final 2026 form at https://www.irs.gov/forms-pubs/about-form-940 before use.

Source abbreviations: **F940** = Form 940 (2025); **I940** = Instructions for Form 940 (2025); **I940-26D** = 2026 draft instructions (dated Sep 22, 2026); **Pub 15** = Publication 15 (2026).

---

## Entry rules for the whole form (I940, "Completing Your Form 940")

- Business name and EIN on every page and every attachment.
- No dollar signs or decimal points typed; dollars left of the printed decimal, cents right of it. Commas optional.
- Rounding to whole dollars is allowed only if every entry is rounded: drop amounts under 50 cents, raise 50 to 99 cents. Figure an entry from unrounded components, round only the result.
- A line with a value of zero is left blank.
- Both pages must be completed and the form signed.

---

## Header (top of page 1)

| Field | Entry | Rule and source |
|---|---|---|
| Employer identification number (EIN) | XX-XXXXXXX | Must match the EIN the IRS assigned. No SSN or ITIN. If applied for and not received by the due date, write "Applied For" and the application date. An e-filed return needs a valid EIN. (I940, EIN section) |
| Name (not your trade name) | Legal name used on Form SS-4 | Sole proprietor: owner's name (e.g. "Ronald Smith"), business name on the trade name line. (I940) |
| Trade name (if any) | DBA | Blank if same as name |
| Address | Number, street, suite; city, state, ZIP; foreign fields if needed | Address change → Form 8822-B, mailed separately. Name change → letter to the "Without a payment" filing address. (I940) |

Disregarded entities (single-member LLCs not electing corporate treatment, QSubs, certain foreign disregarded entities) file under their own name and EIN, not the owner's (I940, "Disregarded entities").

## Type of Return (check all that apply)

| Box | Meaning | Rule (I940, "Type of Return") |
|---|---|---|
| a. Amended | Corrects a previously filed return for the same year | Use the same year's Form 940, fill in all amounts as they should have been, attach an explanation. Paper amended returns go to the "Without a payment" address even if a payment is enclosed. |
| b. Successor employer | You acquired substantially all property of a trade or business and kept one or more of its employees | Check if reporting predecessor wages (predecessor was a FUTA employer) or claiming the special credit for state tax a non-FUTA predecessor paid (IRC §3302(e)) |
| c. No payments to employees in YYYY | You must file (test met in prior year) but paid no employees this year | Check, go to Part 7, sign, file |
| d. Final: Business closed or stopped paying wages | You will not be liable for Form 940 in the future | Complete all applicable lines, sign, attach a statement with the name of the person keeping payroll records and the address where they will be kept |

## Aggregate Return Filers Only

Section 3504 agent, Certified Professional Employer Organization (CPEO), or Other third party. These filers attach Schedule R (Form 940). An ordinary employer leaves this blank. This skill does not cover aggregate returns.

---

## Part 1 — Tell us about your return

| Line | Text on form | Entry | Rule |
|---|---|---|---|
| 1a | If you had to pay state unemployment tax in one state only, enter the state abbreviation | Two-letter USPS code | Required even if the state rate was 0%. May be left blank (with 1b) only if all wages in all states were excluded from state unemployment tax; then line 9 is required when line 7 > 0. |
| 1b | If you had to pay state unemployment tax in more than one state, you are a multi-state employer | Checkbox | Complete and attach Schedule A (Form 940) |
| 2 | If you paid wages in a state that is subject to CREDIT REDUCTION | Checkbox | Complete Schedule A. Read the line 9 instructions first. 2025 credit reduction jurisdictions: California (0.012) and U.S. Virgin Islands (0.045) per Schedule A (Form 940) 2025, page 2. |

---

## Part 2 — Determine your FUTA tax before adjustments

### Line 3 — Total payments to all employees

All payments for employees' services during the calendar year, taxable for FUTA or not, however paid (hourly, piecework, percentage of profits). Include (I940, line 3):

- Compensation: salaries, wages, commissions, fees, bonuses, vacation allowances, pay to full-time, part-time, and temporary employees.
- Fringe benefits: sick pay (including third-party sick pay if liability transferred to the employer), value of goods, lodging, food, clothing, non-cash fringe benefits, section 125 (cafeteria) plan benefits.
- Retirement/pension: employer contributions to a 401(k) plan, payments to an Archer MSA, adoption assistance payments, SIMPLE contributions (including elective salary reduction contributions), amounts deferred under a nonqualified deferred compensation plan.
- Other: tips of $20 or more in a month reported to you; payments by a predecessor employer to employees of a business you acquired; payments to nonemployees treated as employees by the state unemployment agency.

Do not include partner draws or guaranteed payments to partners, payments to independent contractors, or S corporation distributions that are not wages (Pub 15, section 15 table).

IRS example (I940): $44,000 + $8,000 + $16,000 = $68,000 on line 3.

### Line 4 — Payments exempt from FUTA tax

Only payments already included on line 3. Check every box that applies (I940, line 4):

| Box | Category | Examples from the instructions |
|---|---|---|
| 4a | Fringe benefits | Value of certain meals and lodging; contributions to accident or health plans for employees, including certain employer payments to an HSA or Archer MSA; benefits excluded under a section 125 plan |
| 4b | Group-term life insurance | See Pub. 15-B |
| 4c | Retirement/Pension | Employer contributions to a qualified plan, including a SIMPLE (other than elective salary reduction contributions) and a 401(k) plan |
| 4d | Dependent care | Payments excludable under section 129: up to $5,000 per employee ($2,500 married filing separately) for 2025; up to $7,500 ($3,750) for 2026 per I940-26D (P.L. 119-21) |
| 4e | Other | Non-cash and certain cash agricultural pay and all H-2A pay; workers' compensation; domestic service pay if under $1,000 cash in every quarter of the current and prior year or if reported on Schedule H; services by your parent, spouse, or child under 21; certain fishing; certain statutory employees; nonemployees treated as employees by the state agency |

Moving expense and bicycle commuting reimbursements are subject to FUTA and never go on line 4 (I940 Reminders; I940-26D What's New).

For S corporations: health insurance premiums for a more-than-2% shareholder-employee are included in W-2 box 1 but excluded from Social Security, Medicare, and FUTA wages (Pub 15, section 5, "Health insurance plans"; Announcement 92-16). Include them on line 3 and report them on line 4, box 4a.

Family employment (Pub 15, section 3; IRC §3306(c)(5)): pay to your child under 21, your spouse, or your parent is exempt from FUTA when you, the individual, are the employer. If the employer is a corporation, a partnership (unless each partner is a parent of the child), or an estate, the pay is FUTA wages.

IRS example (I940): $2,000 health (Joan) + $500 retirement (Sara) + $2,000 health and retirement (John) = $4,500 on line 4; boxes 4a and 4c checked.

### Line 5 — Total of payments made to each employee in excess of $7,000

For each employee: payments − that employee's line 4 exempt payments − $7,000, floor zero. Sum across employees (I940, line 5).

IRS example: Joan $44,000 − $2,000 − $7,000 = $35,000; Sara $8,000 − $500 − $7,000 = $500; John $16,000 − $2,000 − $7,000 = $7,000; line 5 = $42,500.

Successor employer: include in an employee's payments the predecessor's payments only if the predecessor was required to file Form 940. IRS example: predecessor paid Susan $5,000, you paid $3,000; line 3 includes $8,000; line 5 includes $1,000 + $5,000 = $6,000.

### Line 6 — Subtotal

Line 4 + line 5.

### Line 7 — Total taxable FUTA wages

Line 3 − line 6. Check independently: Σ min($7,000, payments − exempt payments) per employee.

### Line 8 — FUTA tax before adjustments

Line 7 × 0.006. This assumes the maximum 5.4% credit against the 6.0% tax.

---

## Part 3 — Determine your adjustments

### Line 9 — ALL taxable FUTA wages excluded from state unemployment tax

Line 7 × 0.054, then go to line 12. Does not apply where the only reason no state tax was paid is a 0% assigned rate. If line 9 is used, lines 10 and 11 are blank and the worksheet is not completed; Schedule A is still completed if multi-state (I940, line 9).

### Line 10 — SOME wages excluded, or ANY state unemployment tax paid late

"Late" means after the due date for filing Form 940. Complete the Worksheet—Line 10 and enter its line 7. Keep the worksheet; do not attach it. Full worksheet: [`state-credit-line-9-10.md`](./state-credit-line-9-10.md).

### Line 11 — If credit reduction applies

Total from Schedule A (Form 940). Skip if line 9 was used. Mechanics: [`credit-reduction-schedule-a.md`](./credit-reduction-schedule-a.md).

---

## Part 4 — Determine your FUTA tax and balance due or overpayment

| Line | Text | Rule (I940) |
|---|---|---|
| 12 | Total FUTA tax after adjustments (lines 8 + 9 + 10 + 11) | If line 9 > 0, lines 10 and 11 must be zero |
| 13 | FUTA tax deposited for the year, including any overpayment applied from a prior year | Deposits only |
| 14 | Balance due (line 12 − line 13) | More than $500: you must deposit. $500 or less: deposit, pay by EFT, card, EFW with e-file, or check or money order with the return. Less than $1: do not pay. Paying an amount that should have been deposited may draw a penalty. Pay by EFT or card → file at the "Without a payment" address and do not send Form 940-V. |
| 15a | Overpayment (line 13 − line 12) | Under $1 → refunded or applied only on written request |
| 15b | Apply to next return / Send a refund | Check one. Neither or both → applied to next return. IRS may apply it to any past-due balance under the EIN. |
| 15c | Routing number | Nine digits; first two 01–12 or 21–32 |
| 15d | Type: Checking / Savings | Check one |
| 15e | Account number | Up to 17 characters; include hyphens, omit spaces and symbols |

Direct deposit is rejected (check mailed instead) if the account name does not match and the bank will not accept it, if a corporation's account is at a foreign bank or foreign branch, or if lines 15c–15e are crossed out or whited out.

Cannot pay in full: online installment agreement if the amount owed is $25,000 or less and payable within 24 months (I940, line 14).

---

## Part 5 — Report your FUTA tax liability by quarter only if line 12 is more than $500

| Line | Quarter | Rule (I940, line 16 and 17) |
|---|---|---|
| 16a | 1st quarter (January 1 – March 31) | Liability incurred, not deposits. Blank if no liability. |
| 16b | 2nd quarter (April 1 – June 30) | |
| 16c | 3rd quarter (July 1 – September 30) | |
| 16d | 4th quarter (October 1 – December 31) | Complete through line 12, copy line 12 to line 17, then 16d = line 17 − (16a + 16b + 16c). Credit reduction liability is recorded as fourth-quarter liability. |
| 17 | Total tax liability for the year | Must equal line 12 |

Quarterly liability = (first $7,000 of each employee's FUTA wages paid in that quarter) × 0.006, adjusted for any line 9/10 situation. IRS example: wages paid March 28 with FUTA of $200 and June 28 with FUTA of $400 → 16a $200, 16b $400; deposit of $600 due by July 31.

---

## Part 6 — May we speak with your third-party designee?

Yes: designee's name and phone, and a five-digit PIN the designee selects. Name a person, not a firm. The designee may supply missing information, ask about processing, and respond to certain math-error notices; the designee cannot bind the employer. Authorization covers only this form and year and expires one year after the Form 940 due date, regardless of extensions (I940, Part 6).

## Part 7 — Sign here

Signature, printed name and title, date, best daytime phone. Authorized signers (I940, "Who Must Sign Form 940?"):

| Entity | Signer |
|---|---|
| Sole proprietorship | The owner |
| Partnership (incl. LLC taxed as partnership) or unincorporated organization | A responsible and duly authorized partner, member, or officer with knowledge of its affairs |
| Corporation (incl. LLC taxed as corporation) | President, vice president, or other principal officer duly authorized to sign |
| Single-member LLC disregarded for income tax | Owner of the LLC or a principal officer duly authorized to sign |
| Trust or estate | The fiduciary |
| Any of the above | A duly authorized agent with a valid power of attorney or Form 8655 on file |

Corporate officers or authorized agents may sign by rubber stamp, mechanical device, or software under Rev. Proc. 2005-39. A paid preparer who is not an employee of the filer completes the Paid Preparer Use Only block (name, signature, PTIN, firm name, firm EIN, address, phone), signs paper returns manually, and gives the filer a copy.

---

## Form 940-V (page 3 of the PDF)

Use only when paying a balance due by check or money order: Box 1 EIN, Box 2 amount, Box 3 name and address. Check payable to "United States Treasury" with EIN, "Form 940", and the tax year written on it. Do not staple the voucher or payment to the return. Do not use Form 940-V for deposits (F940, page 3).

---

## Differences on the 2026 draft (I940-26D, F940 2026 draft)

- Year references change to 2026; due date February 1, 2027, or February 10, 2027 if all FUTA was deposited when due.
- Dependent care exemption limit $7,500 per employee ($3,750 MFS).
- New Automatic Exemption from Penalty (AEP) program, beginning July 2026, for the 2025 tax year and later: filers who timely filed Form 940 and timely paid for the prior 3 years are not assessed failure-to-file, failure-to-pay, or failure-to-deposit penalties (except failure to deposit by EFT). It replaces First Time Abate.
- Mailing table: Michigan and Wisconsin move from the Kansas City group to the Ogden group (see [`../filing.md`](../filing.md)).
- 2026 Schedule A draft shows California and the U.S. Virgin Islands with rates "0.0XX"; final rates follow the Department of Labor's November 2026 determination.
