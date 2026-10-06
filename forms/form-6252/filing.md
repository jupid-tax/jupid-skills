# Filing Form 6252

Form 6252 is not filed by itself. It is an attachment to the seller's income tax return (Attachment Sequence No. 67 on the 2025 form), filed with Form 1040 for individuals, or with Form 1065, 1120-S, 1120, or 1041 for entities. One Form 6252 per installment sale (form header), filed for the year of sale and every later year until and including the year of the final payment, even in a year with no payment (Form 6252 instructions, "Purpose of Form").

Produce the complete draft from [`SKILL.md`](./SKILL.md) first. File only with the user's explicit consent at the moment of submission.

---

## What travels with Form 6252

| Situation | Also attach / complete |
|-----------|------------------------|
| Year of sale of depreciable property | Form 4797 (Part III for recapture; line 13 for line 12 amounts; line 4 or 10 for line 26) |
| §1231 gain on any year's line 26 | Form 4797 line 4 |
| Capital asset | Schedule D (line 4 or 11); Form 8949 is not used for the Form 6252 gain itself |
| §1250 property | Schedule D, line 19 via the Unrecaptured Section 1250 Gain Worksheet (worksheet kept, not attached) |
| §1252/§1254/§1255 recapture | Form 4797 line 15 |
| §453A interest | Schedule 2 line 15, with a statement showing the computation |
| Sale of a business's assets (year of sale) | Form 8594 |
| Line 29e checked | Explanation statement |
| Several assets reported on one Form 6252 | Attached per-asset schedule (Pub. 537, "Reporting an Installment Sale") |
| Interest received | Schedule B (buyer's name, address, SSN on line 1 if the buyer used the property as a personal residence) |
| Election out on an amended return | Form 1040-X marked "Filed pursuant to section 301.9100-2" ([`../form-1040-x/SKILL.md`](../form-1040-x/SKILL.md)) |

---

## Channel decision tree

```
Is the seller an entity (partnership, S corp, C corp, estate, trust)?
  → Attach Form 6252 to that entity's return and file through the entity's channel:
    ../form-1065/SKILL.md, ../form-1120-s/SKILL.md, ../form-1120/SKILL.md (Form 1041: preparer software).

Individual (Form 1040). Does the user already use commercial tax software or a preparer?
  → File through that software or preparer (e-file). The software's "installment sale" or
    "Form 6252" section maps to the draft line by line; verify every computed line against the draft.

Wants to fill IRS forms directly online, free?
  → IRS Free File Fillable Forms (FFFF): https://www.irs.gov/e-file-providers/free-file-fillable-forms
    The IRS list of available FFFF forms includes Form 6252, Form 4797, Schedule B, Schedule D,
    Schedule 2, and Form 8594. Form 6252, Form 4797, Schedule B, and Form 8594 are marked
    "Known Limitations"; read those pages before relying on FFFF for them.
    Status on irs.gov (page reviewed 24-Sep-2026): open; the program closes Oct. 15, 2026.
    After that date FFFF is unavailable until the next season; use software, a preparer, or paper.

Paper?
  → Print Form 1040 with Form 6252 and every related schedule in attachment-sequence order,
    sign, and mail to the address below.
```

Do not use any channel the user has not chosen. Do not create accounts or file without the user present to consent.

---

## Paper filing: Form 1040 mailing addresses

From the 2025 Instructions for Form 1040, "Where Do You File?" (page 126). Re-check each year at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment; addresses change.

| If you live in | No check or money order enclosed (or refund) | Check or money order enclosed |
|----------------|-----------------------------------------------|-------------------------------|
| Alabama, Florida, Georgia, Louisiana, Mississippi, North Carolina, South Carolina, Tennessee, Texas | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 1214, Charlotte, NC 28201-1214 |
| Alaska, California, Colorado, Hawaii, Idaho, Kansas, Michigan, Montana, Nebraska, Nevada, North Dakota, Ohio, Oregon, South Dakota, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Arizona, Arkansas, New Mexico, Oklahoma | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Connecticut, Delaware, District of Columbia, Illinois, Indiana, Iowa, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| A foreign country, U.S. territory, or APO/FPO address; or filing Form 2555 or 4563; or a dual-status alien | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 | Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303 |

Residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands: see Pub. 570 (Form 1040 instructions footnote). Only the U.S. Postal Service can deliver to P.O. boxes. To use a private delivery service, follow "Private Delivery Services" in the Form 1040 instructions.

Entity returns use their own instructions' addresses; amended returns (election out) use the Form 1040-X addresses.

### Assembly

Order attachments by the "Attachment Sequence No." printed on each form (Schedule D, Form 4797, Form 6252 No. 67, and so on). Form 1040 on top, then schedules and forms in sequence order, then supporting statements (§453A computation, line 29e explanation, multi-asset schedule) labeled with name, SSN, and the form and line they support.

---

## Every later year

Set a recurring reminder for each year until the final payment:

1. Collect the buyer's statement of principal and interest for the year.
2. Prepare Form 6252 with Part I copied from the year-of-sale form, line 19 unchanged, line 20 = 0, line 23 cumulative.
3. For a related-party sale, complete Part III in the 2 years after the year of sale, and ask about any resale or other disposition.
4. Ask whether the note was pledged, sold, gifted, cancelled, or modified.
5. Track the remaining unrecaptured §1250 gain.

---

## Security and consent rules

1. **Explicit consent at submission.** Capture the user's statement authorizing the specific filing ("Submit my 2025 Form 1040 with Form 6252 through <channel> now").
2. **Never store** SSNs (the user's or the buyer's), dates of birth, IP PINs, prior-year AGI, or bank details in logs, memory, or transcripts. The buyer's SSN for Schedule B line 1 is entered at filing time and discarded.
3. **Do not bypass** identity verification, MFA, or CAPTCHAs; pause for the user.
4. **Stop on disagreement.** If software or FFFF computes a line differently from the draft, stop and find which one is wrong before submitting.
5. **Keep confirmations** (submission ID, acceptance notice) in the user's records, not the agent's.
6. **No legal certifications on the user's behalf.** The user signs the return (or authorizes the e-file PIN) personally.
