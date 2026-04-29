# Form 4506-T Line-by-Line Reference

Complete lookup for every field on Form 4506-T. Use this when the agent needs to confirm what goes where or troubleshoot a rejected request.

---

## Top of form — Form number requested

Just below the header, the form has a field labeled "Tip — Use Form 4506-T to order a transcript or other return information free of charge."

The user enters the **form number** they originally filed:
- **1040** — most common (individual)
- **1040-SR** — for taxpayers age 65+ (different transcript than 1040 in some IRS systems)
- **1040-NR** — nonresident alien
- **1040-X** — amended return (transcript shows the X data)
- **1065** — partnership
- **1120** — C-corporation
- **1120-S** — S-corporation
- **990** — exempt organization

Enter the form number in the field provided. Some IRS instructions specify "Form 1040" while the form just shows "1040" — match what the form layout asks.

If requesting a Wage and Income Transcript (Line 8), the form number is informational; the W&I transcript covers all third-party-reported income forms regardless.

---

## Line 1 — First taxpayer

### Line 1a — Name shown on tax return

Filer's full legal name as it appeared on the original tax return.

- Include **first, middle initial (or full middle name), last name**
- Include **suffix** if used on the return (Jr., Sr., II, III)
- For an entity (corporation, partnership), enter the entity's legal name

**Critical**: must match the return EXACTLY. If the filer's name has changed (marriage, divorce, court order) since the return was filed, use the name as it appeared on the return, not the current name. The IRS matches by SSN-name combination and rejects mismatches.

### Line 1b — First taxpayer's social security number, ITIN, or EIN

Nine digits. Format with dashes: XXX-XX-XXXX (SSN/ITIN) or XX-XXXXXXX (EIN).

- For individual returns: SSN or ITIN
- For entity returns: EIN

The IRS uses the taxpayer ID as the primary key for transcript retrieval. A typo here is fatal.

---

## Line 2 — Joint return spouse

### Line 2a — Second name shown on the return

If the return was filed jointly, enter the spouse's full legal name as on the return.

If the return was not joint, leave Line 2a blank.

### Line 2b — Second SSN or ITIN

Spouse's nine-digit ID, with dashes.

For joint returns, **both** spouses are considered taxpayers, and **both** must sign Form 4506-T to authorize transcript release. A spouse not signing the form cannot get the joint transcript on their own — they would need to file a separate Form 4506-T or use Form 2848.

---

## Line 3 — Current name, address (including apt., room, or suite no.), city, state, and ZIP code

Where the IRS will mail the transcript **if Line 5 is blank**.

- Use the user's current mailing address
- For an entity, use the entity's current address
- This does NOT have to match the address on the most recent return — that's Line 4

If the user moved since the last return, Line 3 = current address, Line 4 = prior return address.

---

## Line 4 — Previous address shown on the last return filed if different from line 3

Required ONLY if the user moved since the most recent return.

- Format: street, city, state, ZIP
- The IRS uses Line 4 to verify identity by matching against their records
- If the user has not moved since the last return, leave Line 4 blank (or write "Same as Line 3")

A common rejection cause: user moved 3 years ago, last return was filed at the new address, but they think Line 4 should be the prior-prior address. The rule is: Line 4 = address on the **most recent return filed**. If the most recent return was filed from the current address (Line 3), Line 4 is blank.

---

## Line 5 — Customer file number (third-party)

If the user wants the IRS to mail the transcript directly to a third party, fill Line 5 with:
- **Third party's name** (lender, school, agency)
- **Third party's address** (street, city, state, ZIP)
- **Third party's telephone**
- **Customer file number** (loan number, school ID, file ID — provided by the third party; up to 10 characters)

The customer file number helps the third party route the incoming transcript to the right user file.

If Line 5 is blank, IRS mails to Line 3 address.

**Security flag**: filling Line 5 sends sensitive tax data to a third party. Confirm:
- The user explicitly authorizes this third-party delivery
- The third party's address is verified (call to confirm if uncertain)
- The customer file number is correct

If the third party's address is wrong, the transcript goes to a stranger. Tax data is highly sensitive (SSN, AGI, income breakdown). Wrong-address mailing is a privacy incident.

---

## Line 6 — Transcript requested

Form number — usually "1040" — entered in the prompt at the top of Line 6.

Then check exactly ONE of the boxes:

### 6a. Return Transcript

Most line items from the originally-filed Form 1040 series:
- Filing status
- AGI
- Taxable income
- Total tax
- Federal income tax withheld
- Refund or balance due
- Schedules and attachments (in summary form)

Does NOT show:
- Changes made after original filing (amendments, IRS adjustments)
- Penalty / interest charges
- Detailed payment history

**Available**: current tax year and 3 prior tax years. Older years require Account Transcript or Record of Account.

**Most common use**: mortgage applications, student loan applications, business loan applications. Lenders specifically request "Tax Return Transcript" because it confirms the income shown to them by the borrower.

### 6b. Account Transcript

Filing date, marital status, AGI, taxable income, plus return-related transactions:
- Penalties and interest assessed
- Payments (estimated, with return, after notice)
- IRS adjustments (math errors, examination changes)
- Refunds issued
- Notices sent

**Available**: many years back (10+ for some accounts). Use when the user needs deep history or needs to confirm IRS account activity.

**Most common use**: disputing an IRS balance, verifying payment history, audit defense.

### 6c. Record of Account

Combines 6a + 6b in one document. Available for current year + 3 prior tax years.

**Most common use**: when the user needs both the original return data and account activity for a specific year (e.g., responding to a CP2000 notice).

Pick one. Multiple-checked forms get rejected.

---

## Line 7 — Verification of Non-filing

A letter from the IRS stating they have no record of a Form 1040 (or other specified form) filed for the requested year(s).

**Most common use**:
- FAFSA: parents or students who didn't file taxes need a Verification of Non-filing Letter to prove they had no filing requirement
- Immigration: visa applications and green card processes sometimes require proof of non-filing for specific years
- Court proceedings: divorce, child support, bankruptcy may require this

Available for any year where the user did not file (the IRS confirms absence of return). If the user did file but it was rejected or never processed, the letter still says "no record" — which may be misleading.

Check this box only when the user genuinely did not file. Do not check it for years where the user filed (use Return or Account Transcript instead).

---

## Line 8 — Wage and Income Transcript

Shows third-party-reported income data for the requested year:
- W-2 (employer wage reports)
- 1099-NEC (contractor income)
- 1099-MISC (other income)
- 1099-DIV (dividends)
- 1099-INT (interest)
- 1099-R (retirement)
- 1099-K (third-party network payments)
- 1098-mortgage interest
- 1098-T (tuition)
- K-1 (partnership / S-corp)
- 5498 (IRA contributions)
- Etc.

**Available**: last 10 years.

**Important timing**: third parties report this data to the IRS by January 31 of the following year, but the IRS doesn't always have the data immediately. Wage and Income Transcripts for the current year are usually NOT available until **mid-summer** (June-July) of the following year. For the most current year's data, the user must wait.

**Most common use**: replacing lost W-2 / 1099 documents to prepare a tax return; verifying that all income was reported on a return; dealing with identity theft claims (showing the user what was reported to IRS in their name).

The Wage and Income Transcript shows **what was reported**, not necessarily what is correct. If a 1099 was issued in error, it shows on the W&I transcript regardless.

---

## Line 9 — Year or period requested

Up to **4 years** per Form 4506-T. For more, file additional 4506-T forms.

Format: usually MM/DD/YYYY (the IRS uses fiscal-year-end dates). For calendar-year filers, use 12/31/YYYY.

Example for tax year 2024: 12/31/2024.

For fiscal-year filers (rare for individuals; some entities), use the entity's fiscal year-end date (e.g., 06/30/2024).

If requesting a period that doesn't yet exist (i.e., the year hasn't ended), the IRS will reject. If requesting a year before the user's filing history begins, the IRS will return a Verification of Non-filing for that year (which may not be what the user wanted).

---

## Signature section

### Taxpayer signature

- The person whose name is on Line 1 must sign
- For joint returns, BOTH spouses sign (or use Line 5 third-party with appropriate authorization)
- Wet signature on paper, OR electronic signature acceptable to IRS via specific approved channels (limited)

The signature certifies under penalty of perjury that:
- The signer is authorized to request the transcript
- The information on the form is true and correct

False signatures are a federal crime. Never let an agent generate a faux signature.

### Date

Date of signature. Per current Form 4506-T instructions, signature is valid for 120 days. If older than 120 days when the IRS receives the form, it will be rejected. Always sign close to submission.

### Phone

Daytime telephone where the IRS can reach the user with questions. Use a number the user actually answers.

### Print/type name

Same as signed name, but printed legibly so a clerk can read it.

### Title

Only required if Line 1a is an entity (corporation, trust, partnership, estate). Enter the signer's title (President, CEO, Trustee, Executor, General Partner, etc.).

For individual filers, leave the title blank.

### Spouse signature

If joint return, spouse signs separately with own date, printed name. Both signatures within 120 days of submission.

---

## Common formatting traps

- **Names with hyphens or apostrophes**: enter exactly as on the return. "O'Brien" stays "O'Brien", not "OBrien".
- **Compound surnames**: "Smith-Jones" — enter as on the return.
- **Suffix placement**: "Jr." may be on a separate line on the return or after last name. Match the return.
- **Apartment numbers**: include in Line 3 / Line 4 ("Apt 4B" or "#4B").
- **Boxes vs. street addresses**: use the address as it appears on tax records. PO Box may not match street address; if both exist, use the one on file with IRS.
- **Foreign addresses**: include country name in full, postal code per country format.

---

## Validation checklist

- [ ] Line 1a name matches return exactly
- [ ] Line 1b SSN/ID is 9 digits with correct dashes
- [ ] Lines 2a/2b filled if joint, blank if not
- [ ] Line 3 current address is complete and accurate
- [ ] Line 4 = prior return address if user moved; otherwise blank
- [ ] Line 5 third-party (if used) has accurate address; user authorized this delivery
- [ ] Form number entered correctly (1040, 1040-SR, etc.)
- [ ] Exactly ONE transcript type box checked (6a, 6b, 6c, 7, or 8)
- [ ] Line 9 year(s) formatted correctly (12/31/YYYY for calendar-year filers)
- [ ] Up to 4 years requested
- [ ] Signature, date, phone, printed name complete
- [ ] Spouse signature complete if joint
- [ ] Signature within 120 days of expected IRS receipt

---

## Sources

- IRS Form 4506-T, current revision (instructions on page 2 of the form)
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- IRC §6103 — confidentiality and disclosure of tax returns
- IRS RAIVS (Return and Income Verification Services) — back-office processing
- Get Transcript portal: https://www.irs.gov/individuals/get-transcript
