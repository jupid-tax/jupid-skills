# Form 7004 Line-by-Line Reference

Every field on Form 7004 (Rev. December 2025), mapped from the text of the official PDF (https://www.irs.gov/pub/irs-pdf/f7004.pdf, footer "Cat. No. 13804A Form 7004 (Rev. 12-2025)") and the rules in the Instructions for Form 7004 (Rev. December 2025) (https://www.irs.gov/pub/irs-pdf/i7004.pdf). The form is one page: an identification block, Part I (line 1), and Part II (lines 2 through 8).

Before using this map, open https://www.irs.gov/forms-pubs/about-form-7004 and confirm that December 2025 is still the current revision. If a newer revision exists, re-map every line from its PDF text.

Printed instructions at the top of the form:
- "File a separate application for each return."
- "Note: File request for extension by the due date of the return. See instructions before completing this form."

---

## Identification block

| Field (as printed) | What goes here | Rule and source |
|---|---|---|
| Name | The entity's legal name **as it appeared on the previous year's return** | i7004, Specific Instructions: "If your name has changed since you filed your tax return for the previous year, enter on Form 7004 your name as you entered it on the previous year's income tax return." |
| Identifying number | EIN (or SSN where the return uses one) | i7004: "If the name entered on Form 7004 does not match the IRS database and/or the identifying number is incorrect, you will not have a valid extension." |
| Number and street (If P.O. box, see instructions.) | Street address | i7004: use a P.O. box only "if the post office does not deliver mail to the street address and the entity has a P.O. box" |
| Room or suite no. | Suite, room, or other unit number | i7004: "Include the suite, room, or other unit number after the street address." |
| City or town / State or province / Country / ZIP or foreign postal code | Mailing address | Foreign address: city, province or state, and country, in that order; follow the country's postal-code practice; "Do not abbreviate the country name." (i7004) |

Rules that trip filers:

- A new address on Form 7004 does not change the IRS record. i7004: "A new address shown on Form 7004 will not update your record." Use Form 8822-B (business) or Form 8822 to change it.
- A name change is not made on Form 7004. Use last year's name. The IRS e-file page lists "Name change applications" among requests that cannot be e-filed (https://www.irs.gov/Efile7004).
- If the entity has no EIN, stop. Form 7004 cannot be valid without a correct identifying number (i7004). The EIN application is a separate process (see [`form-ss-4`](../../form-ss-4/SKILL.md)).
- No signature line exists. i7004: "Signature. No signature is required on this form."

---

## Part I — Automatic Extension for Certain Business Income Tax, Information, and Other Returns

### Line 1 — Form code

Printed text: "Enter the form code for the return listed below that this application is for."

Enter the two-digit code from the table printed on the form. The full table, with the exact labels from the PDF:

| Application is for | Code | Application is for | Code |
|---|---|---|---|
| Form 706-GSD (Form 706-GS(D)) | 01 | Form 1120-ND | 19 |
| Form 706-GST (Form 706-GS(T)) | 02 | Form 1120-ND (section 4951 taxes) | 20 |
| Form 708 | 37 | Form 1120-PC | 21 |
| Form 1041 (bankruptcy estate only) | 03 | Form 1120-POL | 22 |
| Form 1041 (estate other than a bankruptcy estate) | 04 | Form 1120-REIT | 23 |
| Form 1041 (trust) | 05 | Form 1120-RIC | 24 |
| Form 1041-N | 06 | Form 1120-S | 25 |
| Form 1041-QFT | 07 | Form 1120-SF | 26 |
| Form 1042 | 08 | Form 3520-A | 27 |
| Form 1065 | 09 | Form 8612 | 28 |
| Form 1066 | 11 | Form 8613 | 29 |
| Form 1120 | 12 | Form 8725 | 30 |
| Form 1120-C | 34 | Form 8804 | 31 |
| Form 1120-F | 15 | Form 8831 | 32 |
| Form 1120-FSC | 16 | Form 8876 | 33 |
| Form 1120-H | 17 | Form 8924 | 35 |
| Form 1120-L | 18 | Form 8928 | 36 |

Codes 10, 13, and 14 do not appear on the December 2025 form. Never enter a code that is not in the table.

Special cases for line 1 (all from i7004 unless noted):

- **Homeowners association electing Form 1120-H.** "If an association is electing to file Form 1120-H ... it should file for an extension on Form 7004 using the original form type assigned to the entity." Ask the user which return type the IRS assigned (EIN confirmation letter or prior filings) before choosing between code 17 and the original form's code.
- **Form 1041-A.** Not covered. "The trustee of a trust required to file Form 1041-A must use Form 8868, instead of Form 7004."
- **Foreign-owned U.S. disregarded entity filing a pro forma Form 1120 with Form 5472.** Use code 12 (Form 1120) and write "Foreign-owned U.S. DE" across the top of Form 7004 (Instructions for Form 5472, Rev. December 2024, "Extension of time to file").
- **Two returns, two applications.** "File a separate Form 7004 for each return" (i7004, No Blanket Requests). A partnership that files Form 1065 and Form 8804 files two Forms 7004 (codes 09 and 31).

---

## Part II — All Filers Must Complete This Part

### Line 2 — Foreign corporation with no U.S. office

Printed text: "If the organization is a foreign corporation that does not have an office or place of business in the United States, check here."

- Check only for a foreign corporation with no office or place of business in the United States.
- Deadline differs: "The entity must file Form 7004 by the due date of the return (the 15th day of the 6th month following the close of the tax year)" (i7004, Line 2). See IRC §6072(c) for that return due date.
- Deposits for these corporations follow the Form 1120-F or Form 1120-FSC instructions (i7004, Line 8).

### Line 3 — Common parent of a consolidated group

Printed text: "If the organization is a corporation and is the common parent of a group that intends to file a consolidated return, check here. If checked, attach a statement listing the name, address, and employer identification number (EIN) for each member covered by this application."

- "Only the common parent or agent of a consolidated group can request an extension of time to file the group's consolidated return" (i7004).
- Paper format for the member list (i7004): 8.5 x 11, 20 lb. white paper; 12-point Courier, Arial, or Times New Roman; black ink; one-sided; at least a one-half inch margin; two columns (names and addresses on the left, EIN on the right, one-half inch between columns); two blank lines between affiliates.
- A member that must file a separate short-period return files its own Form 7004 for that period (i7004; Treas. Reg. §1.1502-76).
- Any member of a controlled group or affiliated group not joining in the consolidated return files a separate Form 7004 (i7004, Caution).
- "Failure to list members of the affiliated group on an attachment may result in the group's inability to elect to file a consolidated return" (i7004, Note).

### Line 4 — Regulations section 1.6081-5 filers

Printed text: "If the organization is a corporation or partnership that qualifies under Regulations section 1.6081-5, check here."

Who qualifies (i7004, Line 4; Treas. Reg. §1.6081-5(a)):
- Partnerships that keep their books and records outside the United States and Puerto Rico
- A foreign corporation that maintains an office or place of business in the United States
- A domestic corporation that transacts its business and keeps its books and records of account outside the United States and Puerto Rico
- A domestic corporation whose principal income is from sources within the territories of the United States

How it works:
- These entities already have until the 15th day of the 6th month after the tax year closes to file **and pay**, without Form 7004. They attach a statement to the return saying they qualify.
- If they still cannot file by then, they file Form 7004 with line 4 checked for an **additional** extension of time to file (not to pay): 3 months for partnerships and S corporations, 4 months for C corporations and Form 1120-POL filers (i7004).

### Line 5a — Tax year

Printed text: "The application is for calendar year 20__, or tax year beginning ______, 20__, and ending ______, 20__."

- Calendar year: complete the two digits after the preprinted "20" (for tax year 2026, "26").
- Fiscal year or short year: "If you do not use a calendar year, complete the lines showing the beginning and ending dates for the tax year" (i7004).

### Line 5b — Short tax year

Printed text: "Short tax year. If this tax year is less than 12 months, check the reason: Initial return / Final return / Change in accounting period / Consolidated return to be filed / Other (See instructions—attach explanation.)"

- Check exactly one box only when the year is less than 12 months.
- **Change in accounting period:** "the entity must have applied for approval to change its tax year unless certain conditions have been met" (i7004; Form 1128; Pub. 538). The IRS will not accept this case electronically unless prior approval has been applied for or the conditions are met (https://www.irs.gov/Efile7004).
- **Other:** attach a statement that "clearly explain[s] the circumstances that caused the short tax year" (i7004, Line 5a heading "Periods and Methods").
- A short year that ends anytime in June is treated as ending June 30 for the extension-length rule (i7004, Extension Period, Note).
- The IRS e-file page says Form 7004 cannot be e-filed for "Filing short period extension due to termination of 1120-S status" (https://www.irs.gov/Efile7004).

### Line 6 — Tentative total tax

Printed text: "Tentative total tax."

- "Enter the total tax, including any nonrefundable credits, the entity expects to owe for the tax year. See the specific instructions for the applicable return to estimate the amount of the tentative tax. If you expect this amount to be zero, enter -0-." (i7004)
- Read "including any nonrefundable credits" as the total tax after nonrefundable credits, the figure that the return's total tax line will show (Form 1120 (2025) page 1, line 31, which equals Schedule J, line 12 after Schedule J, line 6 credits).
- Return lines that hold the tax being estimated (2025 forms): Form 1120 line 31; Form 1120-S line 23c; Form 1065 line 28 (lines 24 through 27, including line 26 "BBA AAR imputed underpayment").
- Corporations: line 6 also drives the 90% late-payment relief (see line 8).

### Line 7 — Total payments and credits

Printed text: "Total payments and credits. See instructions."

- "Enter the total payments and refundable credits" (i7004).
- Typical sources (2025 Form 1120 Schedule J, lines 13 through 20z): preceding year's overpayment credited, current year's estimated tax payments, less any refund applied for on Form 4466, withholding, refundable credits (Forms 2439, 4136, credit for chapter 3 or 4 withholding).
- For Form 1120-S: line 24a (estimated payments and prior-year overpayment) and line 24c (fuel tax credit).
- Do not include the payment that will be made with Form 7004 itself; that payment settles line 8.

### Line 8 — Balance due

Printed text: "Balance due. Subtract line 7 from line 6. See instructions."

- Line 8 = line 6 − line 7.
- "Form 7004 does not extend the time to pay tax." Corporations "must remit the amount of the unpaid tax liability shown on line 8 on or before the due date of the return" (i7004).
- Payment methods named in i7004: EFTPS (EFTPS.gov, 800-555-4477), a tax professional or other trusted third party depositing on the entity's behalf, Electronic Funds Withdrawal when the form is e-filed (Form 8878-A), other options at IRS.gov/Pay.
- Net operating loss carryback: a corporation can reduce the deposit by the overpayment from an expected carryback if all prior-year liabilities are paid and Form 1138 is filed with Form 7004 (i7004). When e-filing, send Form 1138 separately (https://www.irs.gov/Efile7004).
- Trusts (Form 1041) and REMICs (Form 1066) get the extension even if they cannot pay all of line 8; they should pay as much as they can (i7004).
- Form 1042 deposits follow the Instructions for Form 1042 (i7004).
- Form 7004 has no overpayment or refund line, and the IRS lists "Requests for refunds" among items Form 7004 cannot handle electronically (https://www.irs.gov/Efile7004). If line 7 exceeds line 6, do not enter a negative number; ask the user's preparer or software how it reports the zero balance, and claim the overpayment on the return.

---

## Rounding (i7004, Rounding Off to Whole Dollars)

- The entity can round to whole dollars; if it rounds, it must round all amounts.
- Drop amounts under 50 cents; raise 50 to 99 cents to the next dollar ($1.39 becomes $1; $2.50 becomes $3).
- When adding two or more amounts for one line, add with cents and round only the total.
- Form 8878-A, Part I takes Form 7004 lines 6, 7, and 8 in whole dollars only.

---

## What is not on the form

- No signature, no reason for the extension, no preparer section (i7004).
- No approval is mailed: "We will notify you only if your request for an extension is disallowed" (i7004, Extension Period).
- The IRS may terminate the extension by mailing a notice at least 10 days before the termination date (i7004; Treas. Reg. §1.6081-3(c), §1.6081-2(f)).
