# Filing Schedule E

Schedule E is not filed alone. It is an attachment to Form 1040, 1040-SR, or 1040-NR (form header: "Attach to Form 1040, 1040-SR, 1040-NR, or 1041"), and its total reaches the return through Schedule 1 (Form 1040), line 5. Filing Schedule E therefore means filing the individual return it belongs to. This file covers the channel choice, the Schedule E specifics inside each channel, paper assembly, mailing addresses, and the consent and security rules.

Out of scope: estates and trusts filing Schedule E with Form 1041. Redirect them to a fiduciary return preparer.

The agent produces a complete draft from `SKILL.md` first, gets the user's review, then picks a channel.

---

## Channel decision tree

```
Is the user's whole Form 1040 being prepared in commercial tax software
(or by a paid preparer)?
  → Section 1. Enter the draft into the software's rental/royalty and K-1 screens.

Does the user want to file directly with the IRS, without software,
and is it before the Free File Fillable Forms closing date?
  → Section 2 (IRS Free File Fillable Forms).
     FFFF lists Schedule E (Form 1040), Form 8582, Form 4562, Form 6198 and Form 4797,
     each with "Known Limitations" (irs.gov "List of available Free File Fillable Forms",
     entries dated 01/26/2026). Form 7203, Form 461 and Form 8990 did not appear on that
     list when checked on 2026-10-06: if the draft needs one of them, use Section 1 or 3.
     The irs.gov FFFF page (reviewed 24-Sep-2026) says the program closes Oct. 15, 2026.
     Read the Known Limitations page for Schedule E and Form 8582 before starting.

FFFF closed, user prefers paper, or a needed form is not supported?
  → Section 3 (paper).
```

Ask the user which channel. Do not choose for them.

---

## Section 1: Commercial software or a paid preparer

1. Use the software's own rental property, royalty, and K-1 interview screens. Do not type totals into an override field.
2. Enter each property separately, with the same line 1b code and line 2 day counts as the draft.
3. Enter depreciation through the software's asset screens so Form 4562 is generated (placed-in-service date, basis, 27.5-year residential rental or 39-year nonresidential, mid-month).
4. Enter prior-year carryovers: Form 8582 suspended losses by activity, Worksheet 5-1 carryovers by property, Form 7203 suspended losses, Form 6198 carryovers.
5. When the software produces Schedule E, Form 8582 and Form 4562, compare every line with the draft. Any difference: stop and find which one is wrong. Do not accept the software's number without an explanation.
6. If the user works with a preparer, hand over the draft, the Form 8582 and Worksheet 5-1 worksheets, the day-count calendar, and the K-1s.

Selectors and screens change every season; rely on visible labels, not DOM IDs.

## Section 2: IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

Pre-flight: the user's permission to act, Form 1040 inputs (FFFF needs the whole return), prior-year AGI or self-select PIN for signing, an email address the user controls, and the completed Schedule E draft plus every attachment draft.

Schedule E specifics:

1. Add Schedule E from the form list after Form 1040 is started.
2. Fill lines A and B, then each property column (1a, 1b, 2, 3–22). FFFF has one set of columns per Schedule E; add another copy for more than three properties and put lines 23a–26 totals on one copy only.
3. Add Form 4562 for any property placed in service in 2025, any vehicle (listed property), §179, or amortization that began in 2025. Use a separate Form 4562 per activity.
4. Add Form 8582 when the draft required it. Line 22 must equal the Form 8582 allowed loss for that property.
5. Page 2: one row per K-1 line on line 28, including separate PYA and UPE rows; check columns (e) and (f) as in the draft. Add Form 6198 if column (f) is checked. Form 7203 was not on the FFFF form list when checked: if column (e) requires it, switch to Section 1 or Section 3 unless the current list shows it.
6. Verify line 26 or line 41 equals Schedule 1, line 5.
7. Run FFFF's error check; fix every flag; compare every computed field with the draft.
8. Stop. Show the user the summary and ask for explicit consent before "E-file" (see Security and consent).
9. After submission, save the confirmation, then check for the acceptance email.

## Section 3: Paper

### Assembly

Stack the return in attachment sequence order (the number printed at the top right of each form). Verified on the 2025 PDFs: Schedule E is sequence 13; Form 6252 is 67; Form 8829 is 176; Form 4562 is 179; Form 8582 is 858. Schedule E therefore goes before Form 4562 and Form 8582. Form 1040 is on top; W-2s and 1099s with withholding are attached as the Form 1040 instructions direct. Sign Form 1040 in ink.

Attachments that commonly travel with Schedule E: Form 4562, Form 8582, Form 6198, Form 7203, Form 461, Form 8990, the line 1b code 8 description statement, the line 12/13 "See attached" statements, the §469(c)(7)(A) election statement (real estate professionals, first year only), and Form 8082 if a K-1 item is reported differently.

### Mailing address (Form 1040)

From the 2025 Instructions for Form 1040, "Where Do You File?" (page 126). Use the left address if not enclosing a payment, the right one if enclosing a check or money order.

| If you live in | No payment enclosed | Payment enclosed |
|---|---|---|
| Alabama, Florida, Georgia, Louisiana, Mississippi, North Carolina, South Carolina, Tennessee, Texas | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 1214, Charlotte, NC 28201-1214 |
| Alaska, California, Colorado, Hawaii, Idaho, Kansas, Michigan, Montana, Nebraska, Nevada, North Dakota, Ohio, Oregon, South Dakota, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Arizona, Arkansas, New Mexico, Oklahoma | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Connecticut, Delaware, District of Columbia, Illinois, Indiana, Iowa, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| A foreign country, U.S. territory, APO or FPO address, or filing Form 2555 or 4563, or a dual-status alien | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 | Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303 |

Residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands: see Pub. 570 (same table footnote). Only the U.S. Postal Service delivers to P.O. boxes; private delivery services cannot be used for payments sent to a P.O. box (same page).

Addresses change. Before mailing, re-check https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment and the current year's Form 1040 instructions. An amended return (Form 1040-X) has its own addresses: route to `../form-1040-x/SKILL.md`.

Recommend a mailing method that gives proof of mailing (for example, USPS Certified Mail) and a complete copy kept by the user.

---

## After filing: records the user must keep

- The Schedule E draft, the day-count calendar, Worksheet 5-1, the Form 8582 worksheets (including Parts VII–IX carryforwards), Form 7203/basis schedules, depreciation schedules, closing statements, and receipts.
- The Schedule E instructions (Recordkeeping) say to keep records that support each item reported. Keep depreciation and basis records until the property is sold; the sale is reported with `../form-4797/SKILL.md`.

---

## Security and consent rules

1. Never submit without the user's explicit consent at the moment of submission ("I authorize you to file my 2025 Form 1040 with Schedule E now").
2. Never store SSNs, EINs from K-1s, dates of birth, PINs, prior-year AGI, or bank account numbers in logs, memory, or transcripts. Use them only in the live form, then discard.
3. Never bypass identity verification, multi-factor prompts, or CAPTCHAs; pause and let the user respond.
4. Save confirmations (submission ID, acceptance) to the user's own storage, not the agent's.
5. If a computed field disagrees with the draft, an unexpected screen appears, or verification fails: stop and report. Do not retry blindly or override numbers.
6. Remind the user once, before filing, that the draft is not tax advice and that loss limits (basis, at-risk, passive, excess business loss), real estate professional status, and Schedule C vs Schedule E questions warrant CPA review.
