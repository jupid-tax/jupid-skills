# Filing Form 7004 (e-file, paper, fax)

How an agent takes a completed Form 7004 draft from `SKILL.md` and gets it to the IRS by the original due date. Produce and validate the draft first, then pick the channel, then execute.

Sources: Instructions for Form 7004 (Rev. December 2025), https://www.irs.gov/pub/irs-pdf/i7004.pdf (How and Where To File; Where To File table on page 5); IRS "E-filing Form 7004" page, https://www.irs.gov/Efile7004; IRS "Where to file Form 7004" page, https://www.irs.gov/filing/where-to-file-form-7004; Instructions for Form 5472 (Rev. December 2024), https://www.irs.gov/pub/irs-pdf/i5472.pdf; Form 8878-A (Rev. December 2008). Re-check the address table every season; the IRS moves states between service centers.

---

## Channel decision tree

```
Is the entity a foreign-owned U.S. disregarded entity (pro forma Form 1120 + Form 5472)?
  → Fax or mail to the dedicated PIN Unit address. Section 3. Never the regular address.

Is line 1 code 28, 29, 30, 32, 33 or 01 (Forms 8612, 8613, 8725, 8831, 8876, 706-GS(D))?
  → Paper only (i7004, How and Where To File). Section 2.

Tax year 2025 and line 1 code 37, 35 or 36 (Forms 708, 8924, 8928)?
  → Paper only for tax year 2025 (i7004, What's New). Section 2.

Does the request include any of these (https://www.irs.gov/Efile7004 "cannot be e-filed")?
  - a name change application
  - reasonable cause for failing to pay timely, or for failing to file the application timely
  - a refund request
  - an election to make installment payments for part of the balance due
  - change in accounting period without prior approval applied for (or the conditions met)
  - a short-period extension because the 1120-S status terminated
  - a filing before the end of the tax period
  → Paper (or resolve the issue first). Section 2.
    Note: an NOL carryback Form 1138 or a Form 2848 does NOT block e-file; send them
    separately, not with the e-filed Form 7004 (https://www.irs.gov/Efile7004).

Will the return itself be e-filed?
  → E-file Form 7004 too. i7004 warns: a paper Form 7004 with an e-filed return
    "may be processed before the extension is granted. This may result in a penalty notice."
    Section 1.

Otherwise
  → User's choice: e-file (Section 1) or paper (Section 2).
```

---

## Section 1 — E-file through Modernized e-File (MeF)

"Form 7004 can be e-filed through the Modernized e-File (MeF) platform" (https://www.irs.gov/Efile7004). MeF submissions go through business tax software that supports Form 7004 or through an electronic return originator (ERO) and transmitter (Form 8878-A; Pub. 4163). The agent does not transmit to MeF itself.

### Pre-flight

- The validated draft (every field, lines 1 to 8)
- The user's explicit authorization to submit through the named software or provider
- The entity's name exactly as on last year's return and the EIN (a mismatch means no valid extension; i7004)
- If line 8 > 0: the payment plan. With e-file, Electronic Funds Withdrawal is available; an authorized person signs Form 8878-A with a PIN and the ERO keeps it (do not send it to the IRS). Otherwise EFTPS by the original due date.
- If line 3 is checked: the member list (name, address, EIN of each member)

### Flow

1. In the software, open the Form 7004 extension module for the entity.
2. Enter the identification block, line 1 code, and Part II exactly as in the draft.
3. Compare the software's computed line 8 with the draft. If they differ, stop; one of them is wrong.
4. If paying by EFW, enter the bank account and the settlement date (on or before the original due date). The authorized person signs Form 8878-A. Revocation: U.S. Treasury Financial Agent, 1-888-353-4537, no later than 2 business days before settlement (Form 8878-A).
5. Ask for explicit confirmation, then transmit.
6. Save the submission ID and wait for the acknowledgment (accepted or rejected, with reason; Form 8878-A, Part II).
7. On rejection, read the reason, fix the field (most often a name/EIN mismatch or wrong code), and retransmit before the original due date. If the due date has passed, see "Missed deadline" below.
8. Store the acceptance acknowledgment with the entity's records. The IRS sends nothing else unless the extension is disallowed (i7004).

---

## Section 2 — Paper

### Assemble

1. Download the current PDF from https://www.irs.gov/pub/irs-pdf/f7004.pdf and confirm the revision in the upper left ("Rev. December 2025" as of 2026-10-06).
2. Fill from the draft. No signature is required (i7004).
3. Attach only what the form calls for:
   - Line 3 checked: member statement in the i7004 format (8.5 x 11, 20 lb. white paper; 12-point Courier, Arial, or Times New Roman; black ink; one-sided; at least one-half inch margin; names and addresses in the left column, EINs in the right column one-half inch apart; two blank lines between affiliates)
   - Line 5b "Other": statement explaining the short tax year
   - Expected NOL carryback reducing the deposit: Form 1138 filed with Form 7004 (i7004, Line 8)
4. Do not attach a reasonable-cause explanation (i7004).
5. Pay line 8 electronically (EFTPS) by the original due date unless the user's preparer directs otherwise (i7004, Line 8; IRS.gov/Pay).

### Where to mail (i7004 Where To File, Rev. December 2025)

| IF the form is | AND the settlor (or decedent) or the principal business, office, or agency is in | THEN mail to |
|---|---|---|
| 708, 706-GS(T), 706-GS(D) | A resident U.S. citizen, resident alien, nonresident U.S. citizen, or alien | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0019 |
| 1041, 1120-H | Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0019 |
| 1041, 1120-H | Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045 |
| 1041, 1120-H | A foreign country or U.S. territory | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |
| 1041-QFT, 8725, 8831, 8876, 8924, 8928 | Any location | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0019 |
| 1042, 1120-F, 1120-FSC, 3520-A, 8804 | Any location | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |
| 1066, 1120-C, 1120-PC | The United States | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045 |
| 1066, 1120-C, 1120-PC | A foreign country or U.S. territory | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |
| 1041-N, 1120-POL, 1120-L, 1120-ND, 1120-SF | Any location | Department of the Treasury, Internal Revenue Service, Ogden, UT 84409-0045 (as printed) |
| 1065, 1120, 1120-REIT, 1120-RIC, 1120-S, 8612, 8613 | Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin; total assets at the end of the tax year **less than $10 million** | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0019 |
| 1065, 1120, 1120-REIT, 1120-RIC, 1120-S, 8612, 8613 | Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin; total assets at the end of the tax year **$10 million or more** | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045 |
| 1065, 1120, 1120-REIT, 1120-RIC, 1120-S, 8612, 8613 | Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, Wyoming (no asset test) | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045 |
| 1065, 1120, 1120-L, 1120-ND, 1120-REIT, 1120-RIC, 1120-S, 1120-SF, 8612, 8613 | A foreign country or U.S. territory | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |

Two quirks in the official table, reproduced as printed and matching https://www.irs.gov/filing/where-to-file-form-7004 on 2026-10-06:
- The 1041-N / 1120-POL / 1120-L / 1120-ND / 1120-SF row prints ZIP "84409-0045" with a Department of the Treasury street-style address, while every other Ogden street-style address uses 84201-0045.
- 1120-L, 1120-ND, and 1120-SF appear both in the "Any location" row and in the foreign-country row.

For any of those return types, tell the user about the quirk and recommend e-filing (Section 1) instead of guessing.

### Mail it

- Postmark by the original due date. IRC §7502 treats a timely postmark (or a designated private delivery service record) as timely filing.
- USPS Certified Mail with Return Receipt gives a dated receipt.
- Private delivery services cannot deliver to P.O. boxes; use USPS for P.O. Box 409101. For a PDS street address, use IRS.gov/PDSstreetAddresses (2025 Instructions for Form 1120, Private Delivery Services).
- Keep a full copy of what was mailed and the receipt.

---

## Section 3 — Foreign-owned U.S. disregarded entity (Form 5472 filer)

From the Instructions for Form 5472 (Rev. December 2024):

- Line 1: the code for Form 1120 (12), because the DE's Form 5472 is attached to a pro forma Form 1120.
- Write "Foreign-owned U.S. DE" across the top of Form 7004.
- File by the due date (excluding extensions) of the return by:
  - Fax (300 DPI or higher) to 855-887-7737, or
  - Mail to: Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112, Attn: PIN Unit, Ogden, UT 84201
- "For these entities, do not use the regular filing address listed in the Instructions for Form 7004."
- Form 5472 for a foreign-owned U.S. DE cannot be filed electronically; plan the extension on the same fax/mail channel. See [`form-5472`](../form-5472/SKILL.md) for the return itself.

Keep the fax transmission report or the mailing receipt as proof.

---

## Missed deadline

A Form 7004 filed after the original due date does not extend the return (i7004, Purpose of Form and When To File). The IRS will not accept an e-filed Form 7004 claiming "Reasonable cause for failing to file application timely" (https://www.irs.gov/Efile7004). Tell the user to file the return as soon as possible, pay what is owed to stop the failure-to-pay penalty and interest, and answer any penalty notice with a reasonable-cause explanation (i7004, Reasonable cause). Do not file a late Form 7004 as if it were valid.

---

## After filing

- No approval letter. "We will notify you only if your request for an extension is disallowed" (i7004).
- The IRS can terminate the extension by mailing a notice at least 10 days before the termination date (i7004; Treas. Reg. §1.6081-3(c)). If one arrives, the return is due by the date in the notice.
- Put the extended due date on the calendar. For partnerships, the extended date is also the Schedule K-1 deadline (Treas. Reg. §1.6031(b)-1T(b)).
- When the return is filed, report the Form 7004 payment on the return's line for it: Form 1120 Schedule J line 17, Form 1120-S line 24b, Form 1065 line 30 (2025 forms).

---

## Security and consent rules for the agent

1. **Explicit consent at the moment of submission.** Capture a statement such as "I authorize you to submit Form 7004 for <entity>, code <NN>, tax year <YYYY>, with a $<amount> payment, through <software/fax/mail> now." No consent, no submission.
2. **Payment consent is separate.** Confirm the amount, the account (last four digits only), and the settlement date before scheduling EFW or EFTPS.
3. **Do not store** EINs, bank account and routing numbers, PINs, EFTPS credentials, or e-file passwords in logs, memory, or transcripts. Use them at submission time and discard.
4. **Never bypass identity checks, MFA, or CAPTCHAs.** Pause and let the user complete them.
5. **Stop on any mismatch** between the draft and the software's computed values, a rejected acknowledgment, or an address-table ambiguity. Surface it; do not retry blindly.
6. **Keep proof under the user's control:** e-file acknowledgment, fax confirmation, or certified-mail receipt, saved where the user stores tax records.
