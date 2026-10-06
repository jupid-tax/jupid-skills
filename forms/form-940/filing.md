# Filing Form 940

How an agent takes a completed Form 940 draft from `SKILL.md` to a filed return: channel choice, e-file signature options, payment, paper addresses, amended returns, and the consent and security rules. Load this file only when the user asks the agent to file or to prepare a filing package.

Sources: 2025 Instructions for Form 940 (I940) "Where Do You File?", "How Must You Deposit Your FUTA Tax?", line 14, "Can You Amend a Return?", Reminders; 2026 draft instructions (I940-26D); Form 940-V; IRS pages "E-file employment tax forms", "Using a Form 94x online signature PIN to e-file employment tax forms", and "Modernized e-File (MeF) for employment taxes: Frequently asked questions".

---

## 1. Channel decision tree

```
Does a payroll provider (full-service payroll, PEO) already file the user's Form 940?
  Yes → Do not file again. Pull the provider's filed copy, compare it line by line with
        the draft, and report differences. A duplicate return creates processing problems.
        If the provider's return is wrong, the fix is an amended Form 940 (Section 5).
  No  ↓
Does a CPA or enrolled agent file for the user?
  Yes → Hand off the package in Section 6. Stop.
  No  ↓
Does the user want to e-file?
  Yes → Section 2 (IRS-approved 94x software or transmitter). The IRS encourages e-filing;
        a fee may be charged (I940, "Where Do You File?" and Reminders).
  No  → Section 4 (paper).
```

The IRS does not accept Form 940 transmitted directly by the employer. Employer self-filers send returns through a third-party transmitter using IRS-approved software (IRS, "Using a Form 94x online signature PIN"). The list of approved providers is at https://www.irs.gov/e-file-providers/94x-mef-providers. Do not recommend a specific vendor.

## 2. E-file through 94x software

### Signature options (IRS MeF for employment taxes FAQ)

1. **Form 94x online signature PIN.** A 10-digit PIN that makes the signer an IRS authorized signer for the company's 94x returns. Apply through the software. It may take up to 45 days to receive. Eligible signers include the sole proprietor, a partner with 5% or more interest or a person authorized to act in legal or tax matters, and the president, vice president, secretary, or treasurer of a corporation.
2. **Practitioner PIN** (used by a tax professional filing for the client).
3. **Form 8453-EMP.** Manually signed, scanned to PDF, and attached by the transmitter. No PIN.

If the user has no PIN and the due date is less than 45 days away, plan on Form 8453-EMP or paper.

### Pre-flight checklist

- [ ] Draft passed every Validation check in `SKILL.md`
- [ ] Legal name and EIN exactly as on the IRS records (Form SS-4 / CP 575 notice)
- [ ] Schedule A data ready if line 1b or 2 is checked; final credit reduction rates for the year are published
- [ ] For a final return, the statement naming the records custodian and address
- [ ] For an amended return, box a checked and the explanation text ready (MeF accepts an attachment)
- [ ] Signer identified and allowed for the entity type (see `references/line-by-line.md`, Part 7)
- [ ] Payment route chosen (Section 3)
- [ ] User's explicit consent captured for this specific return (Section 7)

### Generic software flow

1. Sign in to the user's account in the software (the user authenticates; the agent does not handle passwords unless the user's credential manager supplies them).
2. Select Form 940 and the tax year.
3. Enter the business header: EIN, legal name, trade name, address. Check type-of-return boxes.
4. Enter Part 1 (1a or 1b, 2) and, if prompted, Schedule A states, FUTA taxable wages, and rates.
5. Enter lines 3, 4 (with boxes 4a–4e), and 5. Let the software compute lines 6–8; compare with the draft.
6. Enter line 9 or line 10 (worksheet result) and line 11.
7. Enter line 13 deposits. Confirm line 14 or 15a matches the draft. For a refund, enter routing and account numbers only at this moment, from the user.
8. Enter Part 5 quarterly liability if line 12 is more than $500.
9. Part 6 designee and Part 7 signer details; apply the signature method.
10. Show the user a side-by-side of the draft and the software's summary. Get explicit approval.
11. Submit. Save the submission ID and acknowledgment.

## 3. Paying a balance

| Situation | Method | Source |
|---|---|---|
| Amount was required to be deposited (cumulative over $500) | EFT deposit: EFTPS, IRS Direct Pay, or the IRS business tax account, or a same-day wire via the bank. Never with the return. | I940, "How Must You Deposit Your FUTA Tax?" |
| Line 14 is $500 or less | Deposit, EFT payment, credit or debit card (processor fee), EFW if e-filing, or check or money order with Form 940-V | I940, line 14 |
| Line 14 is less than $1 | Do not pay | I940, line 14 |
| Cannot pay in full | Online installment agreement if $25,000 or less and payable within 24 months (IRS.gov/OPA) | I940, line 14 |

If the balance is paid by EFT or card, file a paper return at the "Without a payment" address and do not send Form 940-V (I940, line 14). The 2025 instructions note Executive Order 14247 and ask filers to pay balances electronically; refunds are issued by direct deposit.

Form 940-V: Box 1 EIN, Box 2 amount, Box 3 name and address. Check or money order payable to "United States Treasury", with the EIN, "Form 940", and the tax year written on it. Do not send cash. Do not staple the voucher or the payment to the return or to each other.

## 4. Paper filing

### Assemble

1. Form 940, both pages, signed in Part 7
2. Schedule A (Form 940) if line 1b or line 2 is checked
3. For a final return: the records-custodian statement
4. For an amended return: the explanation
5. Form 940-V and the check, loose, only if paying by check

Do not attach the line 10 worksheet. Put the name and EIN on every page and attachment.

### Mailing addresses (I940 2025, "Mailing Addresses for Form 940")

| If you're in... | Without a payment | With a payment |
|---|---|---|
| Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0046 | Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 |
| Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, Wyoming | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0046 | Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 |
| Puerto Rico, U.S. Virgin Islands | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 | Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 |
| Legal residence, principal place of business, office, or agency not listed | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 | Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 |
| Exception: tax-exempt organizations; federal, state, and local governments; Indian tribal governments, regardless of location | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0046 | Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 |

**2026 draft change (I940-26D):** Michigan and Wisconsin move from the Kansas City group to the Ogden group. Use the table in the final instructions for the year being filed. The instructions warn that the filing address may differ from prior years.

### Mailing rules

- Timely if properly addressed, with enough postage, and postmarked by USPS on or before the due date, or handed to an IRS-designated private delivery service (PDS) by the due date (I940, "When Must You File Form 940?").
- A PDS cannot deliver to a P.O. box. For a PDS, use the street address at IRS.gov/PDSstreetAddresses for the same state as the "Without a payment" address (I940, "Where Do You File?").
- Recommend USPS Certified Mail with a return receipt and keep a full copy.

## 5. Amended returns

- Use the same year's Form 940 (no Form 940-X). Check box a, fill in every amount as it should have been, sign, attach an explanation (I940, "Can You Amend a Return?").
- E-filing an amended Form 940 is available through MeF (I940, Reminders).
- A paper amended return goes to the "Without a payment" address even if a payment is included.
- Common reason named by the IRS: claiming credit for state unemployment tax paid after the Form 940 due date (90% credit; rerun the line 10 worksheet).
- Ask the user's CPA how to present lines 13 to 15 when the original return was paid with a check rather than deposits; do not guess.

## 6. CPA or payroll handoff package

1. The draft from `SKILL.md`, including the per-employee table, deposit log, and any worksheet
2. Payroll register totals by employee and quarter
3. EFTPS or Direct Pay confirmations
4. State unemployment reports and payment confirmations, with dates
5. Validation warnings raised
6. A note of what the agent could not verify

Send through the CPA's portal or another encrypted channel. Never email EINs with bank details in plain text.

## 7. Consent and security rules

1. File only after the user says, for this return, "I authorize filing Form 940 for [year] now." Capture it.
2. Never store the EIN together with bank routing and account numbers or a signature PIN in logs, memory, or vector stores. Use them at entry time, then discard.
3. Never create, guess, or reuse a 94x signature PIN. It is issued by the IRS to the signer.
4. Never bypass identity checks, MFA, or CAPTCHAs. Hand control to the user.
5. Strip employee names and SSNs from anything logged; Form 940 itself needs no SSNs.
6. Show a side-by-side diff of the draft and what will be submitted, and get approval before clicking submit.
7. If anything is unexpected (math mismatch, rejection, duplicate-filing message, different prefilled data), stop and report. Do not retry blindly.

## 8. After submission

| State | Meaning | Agent action |
|---|---|---|
| Submitted | Sent to the transmitter or mailed | Save submission ID or certified-mail receipt |
| Accepted / Rejected | Transmitter acknowledgment | If rejected, report the reject code and the field; fix only with user approval |
| Processed | IRS posted the return | Form 940 return transcripts for tax years 2023 and later are available in the IRS business tax account (I940, What's New) |
| Notice | IRS letter (math error, penalty, balance due) | Read it to the user; penalty relief requests go on Form 843 or in reply to the notice, not on Form 940 |

Business and Specialty Tax Line for questions: 800-829-4933 (I940, "How Can You Get More Help?").

## 9. Failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| Rejected for name/EIN mismatch | Legal name differs from IRS records | Confirm the name on the EIN notice; a name change is reported by letter to the "Without a payment" address |
| Duplicate return | Payroll provider already filed | Stop; compare; amend if needed |
| Software computes a different line 8 | Exempt payments or line 5 entered differently | Recheck the per-employee table |
| Schedule A required error | Line 1b or 2 checked without states | Enter every state with an unemployment account |
| Software will not accept a 2026 credit reduction rate | Final rates not yet released | Wait for the final 2026 Schedule A |
