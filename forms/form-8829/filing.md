# Filing Form 8829

Form 8829 is never filed alone. It is an attachment to Form 1040 (or 1040-SR / 1040-NR) that supports Schedule C line 30. This file covers how the completed draft reaches the IRS, which channel to use, where paper returns go, and the consent and security rules an agent must follow. Load it only after the draft in `SKILL.md` is complete and validated.

Facts below were checked on 2026-10-06 against irs.gov and the 2025 Instructions for Form 1040. Re-check every date and address for the filing year.

---

## What gets filed with what

| Item | Rule | Source |
|---|---|---|
| One Form 8829 per home | "Use a separate Form 8829 for each home you used for business during the year" | 2025 Form 8829 header |
| Attaches to | Schedule C (Form 1040); never to Schedule F or a partnership return | Form 8829 header; i8829 "Who cannot use Form 8829" |
| Attachment Sequence No. | 176 | Form 8829 header |
| Schedule C line 30 | Form 8829 line 36 (or the business's share of it); do not fill Schedule C's square-footage entry spaces | 2025 Schedule C instructions, Line 30 |
| Form 4562 | Only if the home was first used for business in the tax year or improvements were placed in service that year (line 19j) | i8829, Line 42 |
| Form 4684 | If line 35 has a casualty amount (Form 4684 line 27, "See Form 8829") | i8829, Line 35 |
| Statements | Line 7 special daycare computation ("See attached computation"); line 42 improvements ("See attached") | i8829, Part I and Line 42 |
| Simplified method instead | No Form 8829; Simplified Method Worksheet kept with records, amount on Schedule C line 30 | Schedule C instructions |

---

## Channel decision tree

```
Is the rest of the Form 1040 return ready (Schedule C, SE, 1040 lines)?
  No  → stop. Form 8829 cannot be filed separately. Finish the return first
        (see ../schedule-c/SKILL.md and ../form-1040/SKILL.md).

Does the user already use tax software or a preparer?
  Yes → enter the draft in that software's home-office section
        (Section B below). A paid preparer e-files after the user signs
        Form 8879 (IRS e-file Signature Authorization).

Does the user want to fill IRS forms directly, for free, online?
  Yes → IRS Free File Fillable Forms (Section A), if open.
        As of 2026-10-06 the irs.gov page says: "The program will close Oct. 15, 2026."
        After it closes → software, preparer, or paper.

Otherwise, or if e-file is rejected and cannot be fixed
  → paper return (Section C).
```

---

## Section A — IRS Free File Fillable Forms (FFFF)

- Page: https://www.irs.gov/e-file-providers/free-file-fillable-forms (reviewed 24-Sep-2026; open; closes Oct. 15, 2026).
- The IRS list of available FFFF forms (https://www.irs.gov/e-file-providers/list-of-available-free-file-fillable-forms) shows "Form 8829 Expenses for Business Use of Your Home - Known Limitations (Add from the Schedule C)". Read the Known Limitations page for the year before entering data.
- Flow: open Form 1040 → add Schedule C → add Form 8829 from the Schedule C → enter Part I, then Part III (if owner), then Part II → confirm the FFFF-computed line 36 equals the draft's line 36 → confirm Schedule C line 30 picked it up.
- If FFFF's computed amount differs from the draft by more than $1 of rounding, stop and find which side is wrong. Do not override.
- FFFF accounts are per filing year; identity verification uses prior-year AGI or a Self-Select PIN. Pause for the user at every identity step.

## Section B — Commercial software or a preparer

- Enter the draft by line number; most software asks home-office questions inside the Schedule C interview (square footage, method, expenses, home cost, land, first business-use date).
- After entry, open the software's Form 8829 view and compare all 44 lines with the draft, including zeros and both columns of lines 9–23.
- Carryovers: confirm lines 25 and 31 imported the prior-year amounts the user provided.
- Self-prepared software returns are signed with a Self-Select PIN; when a paid preparer e-files, the user signs Form 8879 first.

## Section C — Paper

Assemble Form 1040 and schedules in attachment-sequence order (the number in the top-right corner of each form). Form 8829 is sequence 176: it goes after Schedule C (sequence 09) and before Form 4562 (sequence 179). Sign Form 1040 in ink.

Mailing addresses, 2025 Instructions for Form 1040, "Where Do You File?" (page 126):

| If you live in | No payment enclosed | Payment enclosed |
|---|---|---|
| Alabama, Florida, Georgia, Louisiana, Mississippi, North Carolina, South Carolina, Tennessee, Texas | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 1214, Charlotte, NC 28201-1214 |
| Alaska, California, Colorado, Hawaii, Idaho, Kansas, Michigan, Montana, Nebraska, Nevada, North Dakota, Ohio, Oregon, South Dakota, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Arizona, Arkansas, New Mexico, Oklahoma | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| Connecticut, Delaware, District of Columbia, Illinois, Indiana, Iowa, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0002 | Internal Revenue Service, P.O. Box 931000, Louisville, KY 40293-1000 |
| A foreign country, U.S. territory, APO/FPO address, or filing Form 2555 or 4563, or dual-status alien | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 | Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303 |

Residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands: see Pub. 570 (same page). Only the U.S. Postal Service delivers to P.O. boxes; private delivery services cannot be used for payments sent to a P.O. box. Re-check https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment every year; addresses change.

Amended return to add, fix, or remove Form 8829 for a prior year: route to [../form-1040-x/SKILL.md](../form-1040-x/SKILL.md). Remember the simplified-method election for a year can be made only on a timely filed original return and is irrevocable for that year (Pub. 587).

---

## What the agent must not do

1. **No submission without explicit consent at the moment of filing.** Capture the user's words, for example: "I authorize you to e-file my 2025 Form 1040 with Form 8829 now."
2. **No storage of SSN, date of birth, Self-Select PIN, prior-year AGI, or bank details** in logs, memory, or transcripts. Use at filing time, then discard.
3. **No bypassing identity verification, MFA, or CAPTCHA.** Pause and let the user act.
4. **No overriding a software or FFFF computation** that disagrees with the draft. Stop, find the cause, tell the user.
5. **No filing a Form 8829 for a home** the user has not confirmed passes the exclusive-use and qualifying-use tests in [references/qualification-tests.md](./references/qualification-tests.md).
6. **Save confirmations** (submission ID, acceptance notice, or the mailing receipt) where the user controls them, not in the agent's storage.

## After filing

- Keep the filed Form 8829, the line 11 and depreciation computations, and floor-plan measurements with the user's records. Next year's lines 25 and 31 come from this year's lines 43 and 44, and the depreciation history matters when the home is sold (Pub. 587, Recordkeeping).
- Check acceptance or rejection through the channel used before telling the user the return is filed; refund status: https://www.irs.gov/refunds.
