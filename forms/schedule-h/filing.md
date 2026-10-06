# Filing Schedule H and the Household W-2s

How an agent takes a completed Schedule H draft from `SKILL.md` to filed forms: Schedule H with the income tax return or by itself, Forms W-2 and W-3 with the Social Security Administration, payment, and the consent and security rules. Load this file only when the user asks the agent to file or to prepare a filing package.

Sources: 2025 Instructions for Schedule H (ISH25) "When and Where To File", "Filing Form W-2 and Form W-3", address table on page 11; 2026 draft instructions (ISH26D); Publication 926 (2026) (P926); IRS "List of available Free File Fillable Forms" (https://www.irs.gov/e-file-providers/list-of-available-free-file-fillable-forms).

---

## 1. Channel decision tree

```
Did the user choose to report the household employee on business payroll (Form 941/944/943 + 940)?
  Yes → Not a Schedule H filing. Route to ../form-941/SKILL.md and ../form-940/SKILL.md. Stop.
  No  ↓
Is the user required to file Form 1040, 1040-SR, 1040-NR, 1040-SS, or 1041 for the year?
  Yes → Schedule H is attached to that return (Section 2). E-filing is encouraged (ISH25).
  No  → Schedule H is filed by itself on paper with Part IV completed (Section 3).
Separately, every year with a required W-2 → Section 4 (SSA), due before Schedule H.
State unemployment and state withholding filings → state agency; out of scope.
```

## 2. Schedule H attached to the income tax return

| Option | Notes |
|---|---|
| Commercial tax software | Enter Schedule H through the software's household employment section; compare every line with the draft before submission |
| IRS Free File Fillable Forms (FFFF) | The IRS list for filing season 2026 (tax year 2025) includes Schedule H (Form 1040) and Schedule 2 (Form 1040). FFFF field labels follow the paper form. Re-check the list for the season being filed |
| Paid preparer | Hand off the package in Section 6 |
| Paper | Attach Schedule H to the return and mail to the address in the Form 1040 instructions by April 15 (ISH25) |

Due date: with the return, by April 15, 2026 for 2025 and April 15, 2027 for 2026; an extension of the return extends Schedule H; fiscal-year filers use the fiscal-year return due date (ISH25; P926). The extension does not extend the April 15 date that decides whether state contributions were late (ISH25, line 23).

Carry line 26 to Schedule 2 (Form 1040) line 9 for 2025, or line 17a on the 2026 draft Schedule 2; Form 1040-SS Part I line 4; Form 1041 Schedule G Part I line 7 (Schedule H line 27 chart).

Only two Schedules H can be attached to a Form 1040, 1040-SR, or 1040-SS: one for each spouse (ISH25).

### Pre-flight checklist

- [ ] Draft passed every check in `SKILL.md` Validation
- [ ] EIN present (or "Applied For" and the date); never an SSN in the EIN box
- [ ] Tax-year values match the form revision (test amount, wage base, Schedule 2 line)
- [ ] Section B worksheets kept with records (not attached)
- [ ] W-2s already filed with the SSA (due before Schedule H)
- [ ] User's explicit consent for this return (Section 7)

## 3. Schedule H filed by itself

When no return is required, file Schedule H alone by April 15 (April 15, 2026 for 2025; April 15, 2027 for 2026) (ISH25; ISH26D; P926):

1. Complete Schedule H including **Part IV** (address and signature). The paid preparer block is completed only by a paid preparer who is not the filer's employee.
2. Put Schedule H and a check or money order in an envelope. Payable to "United States Treasury". Do not send cash. Do not make a separate payment for income tax.
3. Write on the check: name, address, SSN, daytime phone number, and "2025 Schedule H" (or "2026 Schedule H").
4. Mail to the address for where the filer lives. No street address is needed.

The IRS recommends paying electronically when possible (IRS.gov/Pay); confirm with the user how the payment will be matched before choosing that route for a stand-alone filing.

### Addresses for a stand-alone Schedule H (ISH25, page 11)

| If you live in... | Use this address |
|---|---|
| Alabama, Arizona, Arkansas, Florida, Georgia, Louisiana, Mississippi, New Mexico, North Carolina, Oklahoma, South Carolina, Tennessee, Texas | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0002 |
| Connecticut, Delaware, District of Columbia, Illinois, Indiana, Iowa, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0002 |
| Alaska, California, Colorado, Hawaii, Idaho, Kansas, Michigan, Montana, Nebraska, Nevada, Ohio, Oregon, North Dakota, South Dakota, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0002 |
| A foreign country, a U.S. territory, an APO or FPO address, or filing Form 2555 or 4563, or a dual-status alien | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 |

Residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands: see Pub. 570 (ISH25 footnote).

**2026 draft change (ISH26D):** Illinois, Indiana, Minnesota, and Wisconsin move from the Kansas City list to the Ogden list. Use the table in the final instructions for the year being filed.

## 4. Forms W-2 and W-3 with the Social Security Administration

| Item | Rule | Source |
|---|---|---|
| Who gets a W-2 | Each household employee with Social Security and Medicare wages at or above the test ($2,800 for 2025; $3,000 for 2026) or with federal income tax withheld | P926, "Form W-2"; ISH25 |
| Due | Copies B, C, and 2 to the employee and Copy A with Form W-3 to the SSA by February 2, 2026 (2025 forms) / February 1, 2027 (2026 forms) | ISH25; P926 |
| Electronic | SSA Employer W-2 Filing Instructions & Information, SSA.gov/employer; W-2 Online generates the W-3 data | ISH25 |
| Paper | Social Security Administration, Direct Operations Center, Wilkes-Barre, PA 18769-0001; Certified Mail ZIP 18769-0002; IRS-approved private delivery service: add "Attn: W-2 Process, 1150 E. Mountain Drive" and use ZIP 18702-7997 | ISH25 (same in ISH26D) |
| Do not double-file | If filed electronically, do not mail paper W-2/W-3 | ISH25 |
| Form W-3 | Check "Hshld. emp." in box b, Kind of Payer | ISH25 |
| State copies | Check whether the state, city, or locality requires Copy 1 | ISH25 |

## 5. Corrections after filing

- Filed with Form 1040, 1040-SR, or 1040-NR → Form 1040-X with a corrected Schedule H ([`../form-1040-x/SKILL.md`](../form-1040-x/SKILL.md)).
- Filed by itself → a new stand-alone Schedule H with "CORRECTED" and the discovery date in bold in the top margin, an explanation statement, and "ADJUSTED" or "REFUND" for an overpayment (P926).
- Matching Form W-2c to the SSA when wages or withholding change (P926).

Details: [`references/paying-and-correcting.md`](./references/paying-and-correcting.md).

## 6. Preparer handoff package

1. The Schedule H draft, worker classification table, quarterly wage table (current and prior year)
2. W-2/W-3 data and SSA filing confirmation
3. State unemployment statements with payment dates
4. Section B worksheets if used
5. Payment plan (W-4/W-4P changes, 1040-ES payments)
6. Validation warnings and anything not verified

Share through the preparer's portal or another encrypted channel.

## 7. Consent and security rules

1. File or submit only after the user says, for this specific form and year, "I authorize you to file it now." Capture the statement.
2. Never store the user's or the employee's SSN, the EIN with bank details, IP PINs, or e-file PINs in logs, memory, or vector stores. Mask SSNs in drafts (XXX-XX-1234 at most).
3. Never bypass identity verification, MFA, or CAPTCHAs. Hand control to the user.
4. Show a side-by-side of the draft and what will be submitted, and get explicit approval before clicking submit.
5. If anything is unexpected (software computes different FUTA, Schedule 2 line differs, rejected W-2), stop and report. Do not retry blindly.
6. Do not file the employee's W-2 without the employee's correct name and SSN as shown on the Social Security card (P926, "Employee's SSN").

## 8. After submission

| State | Agent action |
|---|---|
| Return submitted (e-file) | Save the acknowledgment; confirm Schedule H and Schedule 2 were included |
| Return mailed | Recommend Certified Mail; keep a full copy |
| W-2 accepted by SSA | Save the SSA confirmation |
| IRS notice | Read it with the user; corrections through Section 5 |

Keep Schedule H, W-2, W-3, and W-4 copies for at least 4 years after the Schedule H due date or the date the taxes were paid, whichever is later (ISH25; P926).

## 9. Failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| SSA rejects W-2 | Boxes 3–6 filled for wages below the test | Leave 3–6 blank; only boxes 1 and 2 |
| Software FUTA ≠ draft | Section A chosen despite a late payment or credit reduction state | Answer lines 10–12 as in the draft; complete Section B |
| Return rejected for missing EIN | EIN not yet issued | Apply first ([`../form-ss-4/SKILL.md`](../form-ss-4/SKILL.md)). The instructions allow "Applied For" and the application date; e-file software may still require an issued EIN, so ask the user whether to wait or file on paper |
| Schedule 2 total off | Wrong Schedule 2 line for the year | Use the line printed on that year's Schedule H line 27 |
