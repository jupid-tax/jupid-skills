# Form 4506-T Line-by-Line Reference

Complete lookup for every field on Form 4506-T (Rev. April 2025), built from the form text; the instructions are on page 2 of the form. Re-check https://www.irs.gov/forms-pubs/about-form-4506-t for a newer revision before use. Use this when the agent needs to confirm what goes where or troubleshoot a rejected request.

---

## Tax form number (entered on line 6)

The top of the form carries a tip pointing to the online tools and 800-908-9946; there is no form-number field there. The form number goes on **line 6** ("Enter the tax form number here (1040, 1065, 1120, etc.)"), one form number per request.

The user enters the **form number** they originally filed:
- **1040** — most common (individual)
- **1040-SR** — for taxpayers age 65+ (different transcript than 1040 in some IRS systems)
- **1040-NR** — nonresident alien
- **1040-X** — amended return (transcript shows the X data)
- **1065** — partnership
- **1120** — C-corporation
- **1120-S** — S-corporation
- **990** — exempt organization

Enter the number as the form shows it ("1040", "1065", "1120").

Line 8 (W-2/1099/1098/5498 series transcript) is a separate request; the line 6 form number does not limit which information returns appear on it.

---

## Line 1 — First taxpayer

### Line 1a — Name shown on tax return

Name as it appeared on the tax return. For a joint return, the name shown first.

- Include **first, middle initial (or full middle name), last name**
- Include **suffix** if used on the return (Jr., Sr., II, III)
- For an entity (corporation, partnership), enter the entity's legal name

**Critical**: use the name as it appeared on the return. If the filer's name has changed since (marriage, divorce, court order), still use the return name on line 1a, put the current name on line 3, and sign with both names (form page 2, "Individuals").

### Line 1b — First taxpayer's social security number, ITIN, or EIN

Nine digits: XXX-XX-XXXX (SSN/ITIN) or XX-XXXXXXX (EIN).

- For individual returns: the first SSN or ITIN shown on the return — including a Form 1040 with Schedule C (form page 2, "Line 1b")
- For business returns: EIN

The IRS uses the taxpayer ID to find the account. A typo here sinks the request.

---

## Line 2 — Joint return spouse

### Line 2a — Second name shown on the return

If the return was filed jointly, enter the spouse's full legal name as on the return.

If the return was not joint, leave Line 2a blank.

### Line 2b — Second SSN or ITIN

Spouse's nine-digit SSN or ITIN.

Transcripts of jointly filed returns may be furnished to either spouse, and only one signature is required (form page 2, "Individuals"; the signature block says "at least one spouse must sign").

---

## Line 3 — Current name, address (including apt., room, suite, or inmate no.), city, state, and ZIP code

- Use the user's current address; include a P.O. box here if used; an incarcerated filer includes the inmate number
- For an entity, use the entity's current address
- This does NOT have to match the address on the most recent return — that's Line 4

**Delivery:** since July 2019 the IRS mails Form 4506-T transcripts only to the taxpayer's **address of record**. If the user moved and has not changed the address with the IRS, the form says to file Form 8822 (Form 8822-B for a business address) — otherwise the transcript goes to the old address on file.

If the user moved since the last return, Line 3 = current address, Line 4 = prior return address.

---

## Line 4 — Previous address shown on the last return filed if different from line 3

Required ONLY if the address on the last return filed differs from line 3.

- Format: street, city, state, ZIP
- If the user has not moved since the last return, leave Line 4 blank

A common error: the user moved 3 years ago, filed the last return at the new address, but thinks Line 4 should be the prior-prior address. The rule is: Line 4 = address on the **last return filed**. If the last return was filed from the current address (Line 3), Line 4 is blank.

---

## Line 5 — Customer file number (if applicable)

Optional. Enter up to **10 numeric characters** to create a customer file number that prints on the transcript (transcripts mask the SSN, so this number helps the user or a lender match the transcript to a file). It must not contain an SSN; if the user enters an SSN, a name, or both, the IRS will not input it and the transcript shows the generic "9999999999" (form page 2, "Line 5").

Line 5 is NOT a third-party mailing block. Since July 2019 the IRS no longer mails transcripts to third parties; it mails them only to the taxpayer's address of record. A lender or other third party that needs transcripts directly must use the Income Verification Express Service (IVES) with Form 4506-C (form, "What's New").

A lender's loan number that contains letters or dashes ("PNM-2026-04571") cannot be used as is; use only its digits (up to 10) or leave line 5 blank.

---

## Line 6 — Transcript requested

Form number — usually "1040" — entered in the prompt at the top of Line 6. Enter only one tax form number per request.

Then check ONE of the boxes (the form does not say multiple boxes are rejected, but one transcript type per form keeps the request clean; use 6c to get return and account data together):

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

**Available**: the current year and returns processed during the prior 3 processing years (form line 6a). Older years: Account Transcript.

**Most common use**: mortgage applications and business loan applications; irs.gov says a tax return transcript "usually meets the needs of lending institutions offering mortgages".

### 6b. Account Transcript

Filing date, marital status, AGI, taxable income, plus return-related transactions:
- Penalties and interest assessed
- Payments (estimated, with return, after notice)
- IRS adjustments (math errors, examination changes)
- Refunds issued
- Notices sent

**Available**: "for most returns" (form line 6b). Online: current and nine prior tax years; by mail or phone: current and three prior; older years only via Form 4506-T (irs.gov "Transcript types for individuals and ways to order them").

**Most common use**: disputing an IRS balance, verifying payment history, audit defense.

### 6c. Record of Account

Combines 6a + 6b in one document. Available for current year + 3 prior tax years. The form suggests requesting it when unsure which transcript is needed.

**Most common use**: when the user needs both the original return data and account activity for a specific year (e.g., responding to a CP2000 notice).

---

## Line 7 — Verification of Non-filing

A letter from the IRS stating it has no record of a processed Form 1040-series return for the requested year as of the date of the request. It does not say whether the user was required to file (irs.gov transcript types page).

**Availability**: current-year requests only after June 15; no restriction on prior years (form line 7).

**Most common use**:
- FAFSA verification, when the school asks for it. For IRS non-filers the 2025–26 FSA Handbook (Application and Verification Guide, Ch. 4) accepts a signed non-filing statement plus W-2s, so confirm the school specifically wants the IRS letter
- Immigration: visa applications and green card processes sometimes require proof of non-filing for specific years
- Court proceedings: divorce, child support, bankruptcy may require this

If the user filed but the return was rejected or never processed, the letter still says "no record" — which may be misleading.

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

**Available**: up to 10 years (form line 8); online, the current and nine prior tax years. State or local W-2 information is not included; for W-2 data needed for Social Security purposes, the form points to SSA at 1-800-772-1213.

**Important timing**: irs.gov says information for the current processing year is generally available online in the first week of February but shows only documents already filed with the IRS, so it may be incomplete early in the year. The form's line 8 text is more conservative: current-year information is generally not available until the year after it is filed. For a request in the first months of the year, warn the user the transcript may be incomplete.

**Most common use**: replacing lost W-2 / 1099 documents to prepare a tax return; verifying that all income was reported on a return; dealing with identity theft claims (showing the user what was reported to IRS in their name).

The Wage and Income Transcript shows **what was reported**, not necessarily what is correct. If a 1099 was issued in error, it shows on the W&I transcript regardless.

---

## Line 9 — Year or period requested

The form has **four** date slots. For more periods, file additional 4506-T forms.

Format: MM/DD/YYYY, the end date of the tax year or period (calendar year, fiscal year, or quarter; enter each quarter for quarterly returns). For calendar-year filers, use 12/31/YYYY.

Example for tax year 2024: 12/31/2024.

For fiscal-year filers (rare for individuals; some entities), use the entity's fiscal year-end date (e.g., 06/30/2024).

If requesting a period that has not ended or a return that has not been processed, there is nothing to transcribe yet; wait (see https://www.irs.gov/individuals/transcript-availability).

---

## Signature section

### Authority checkbox

"Signatory attests that he/she has read the attestation clause and upon so reading declares that he/she has the authority to sign the Form 4506-T." This box **must be checked**; the form will not be processed if it is unchecked (form page 2, Caution).

### Taxpayer signature

- The taxpayer on line 1a or 2a signs; on a joint return, at least one spouse must sign
- Sign exactly as the name appeared on the return; if the name changed, also sign the current name
- Corporations: an officer with authority to bind the corporation, a person designated by the board, or an officer/employee on written request of a principal officer; a 1%-or-more shareholder may request with documentation
- Partnerships: any person who was a member during any part of the period on line 9
- Estates, trusts, dissolved corporations, insolvent taxpayers, heirs: see IRC §6103(e); heirs, next of kin, or beneficiaries must establish a material interest
- Entities other than individuals attach the authorization document (e.g., letter from the principal officer, letters testamentary)
- A representative signs only if Form 2848 line 5 delegates that authority; attach the Form 2848

The signature declares the signer is the taxpayer or a person authorized to obtain the information. Never let an agent generate a faux signature.

### Date

The IRS must receive Form 4506-T within 120 days of the date signed or it will be rejected. Sign close to submission, after all applicable lines are completed ("Do not sign this form unless all applicable lines have been completed").

### Phone

"Phone number of taxpayer on line 1a or 2a." Use a number the user actually answers.

### Title

Only if Line 1a is a corporation, partnership, estate, or trust. Enter the signer's title (President, Trustee, Executor, General Partner, etc.). Leave blank for individuals.

### Spouse's signature

Optional on a joint return (one spouse's signature is enough). If the spouse signs, the spouse dates it too.

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
- [ ] Line 1b SSN/ITIN/EIN is 9 digits and is the first number shown on the return
- [ ] Lines 2a/2b filled if joint, blank if not
- [ ] Line 3 current address is complete; Form 8822 filed if the IRS address of record is out of date
- [ ] Line 4 = last-return address if different from line 3; otherwise blank
- [ ] Line 5 (if used) is ≤10 digits, no SSN, no name
- [ ] One form number on line 6 (1040, 1040-SR, etc.)
- [ ] One transcript type box checked (6a, 6b, 6c, 7, or 8)
- [ ] Line 9 period(s) as MM/DD/YYYY (12/31/YYYY for calendar-year filers), no more than four
- [ ] Authority checkbox checked; signature, date, phone complete; title + authorization document for entities
- [ ] IRS will receive the form within 120 days of the signature date

---

## Sources

- IRS Form 4506-T (Rev. April 2025), instructions on page 2 of the form
- Transcript types and ways to order them: https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- IRC §6103 — confidentiality and disclosure of tax returns
- IRS RAIVS (Return and Income Verification Services) — back-office processing
- Get Transcript portal: https://www.irs.gov/individuals/get-transcript
