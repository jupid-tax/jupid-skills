---
name: form-4506-t
description: >
  Use this skill when an individual taxpayer needs to request a transcript of
  their tax return, account, wages/income, or verification of non-filing from
  the IRS using Form 4506-T. Triggers on phrases like "request tax transcript",
  "Form 4506-T", "lender wants my tax transcript", "need my W-2 from IRS",
  "replace lost 1099", "verify non-filing for FAFSA", "Get Transcript online",
  "PPP audit transcript", "mortgage lender needs my taxes".
  Do NOT use for: full COPY of a previously filed return (use Form 4506 — paid,
  $30 fee per return, up to 75 calendar days); current-year tax info before the IRS has
  finished processing (call IRS directly); third-party access to tax info for
  ongoing matters (Form 8821 Information Authorization or Form 2848 Power of
  Attorney); business return transcripts where the entity needs an EIN-based
  request (Form 4506-T still works but use the entity's name and EIN, not the
  individual filer's).
form: Form 4506-T (Request for Transcript of Tax Return)
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f4506t.pdf
---

# Form 4506-T — Request for Transcript of Tax Return

This skill produces a correctly filled Form 4506-T to request one of five IRS transcript types: Tax Return Transcript, Tax Account Transcript, Record of Account Transcript, Wage and Income Transcript, or Verification of Non-filing Letter.

The form itself is short — one page plus a page of instructions and mailing charts. The complexity is in (a) picking the right transcript type for the user's purpose, (b) deciding whether the user's Individual Online Account or Get Transcript by Mail is a better channel (free, faster for most users), and (c) routing the form to the correct IRS office (varies by the state the user lived in when the return was filed, and by transcript type).

Transcripts are **free**. They are different from a full Form 4506 "copy of return" request, which costs $30 per return and may take up to 75 calendar days (Form 4506, April 2025).

**Form revision.** The line map in this skill was verified on 2026-10-06 against Form 4506-T (Rev. April 2025); the instructions and the mailing/fax charts are on page 2 of the form (there is no separate instructions PDF). Before use, check https://www.irs.gov/forms-pubs/about-form-4506-t for a newer revision and re-check the line numbers and charts if one exists.

**Third-party mailing no longer exists.** Since July 2019 the IRS mails transcripts requested on Form 4506-T only to the taxpayer's address of record; it does not mail them to lenders, schools, or other third parties (Form 4506-T, note under line 5 and "What's New"). A third party that needs transcripts directly uses the IRS Income Verification Express Service (IVES) and Form 4506-C.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions "Form 4506-T", "tax transcript", or "transcript request"
- The user's mortgage lender, student loan servicer, SBA loan officer, or auditor is requesting a tax transcript
- The user lost a W-2 or 1099 and needs the IRS-reported income data
- The user's school asked for an IRS Verification of Non-filing Letter or tax return transcript during FAFSA verification
- The user is replying to an IRS notice that requires proof of prior filings
- The user is in immigration / passport renewal proceedings requiring tax-history verification
- The user needs to confirm a balance owed, payment history, or penalty/interest detail

Do **not** engage this skill when:

- The user wants a **full copy** of their original Form 1040 with attachments — that is **Form 4506** (different form, $30 per return, up to 75 calendar days)
- The user wants to authorize a third party to **discuss** tax matters with the IRS on an ongoing basis — that is Form 2848 (Power of Attorney) or Form 8821 (Tax Information Authorization)
- The user wants current-year information **before** the IRS has finished processing the return (for a refund or no-balance-due return, IRS says allow 2-3 weeks after e-filing, 6-8 weeks after mailing a paper return; balance-due returns take longer — https://www.irs.gov/individuals/transcript-availability)
- The user is trying to obtain **someone else's** transcript without authorization — only the taxpayer (or their authorized representative via Form 2848/8821) can request

If the user just wants past-year totals for their own records, suggest the **Individual Online Account** first (reached from https://www.irs.gov/individuals/get-transcript) — users who can verify their identity with ID.me can view, print, or download all five transcript types with no Form 4506-T needed.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop.

1. **Purpose** — what does the user actually need the transcript for? This determines which transcript type. Common purposes:
   - Mortgage application → Tax Return Transcript (last 2 years usually); many lenders get it themselves through IVES with a Form 4506-C the borrower signs
   - FAFSA verification → whatever the school asked for. Since the 2024–25 FAFSA, federal tax data flows from the IRS to the Department of Education directly, and the IRS no longer accepts Form 8821 or Form 4506-C for FAFSA income verification (https://www.irs.gov/individuals/tax-information-for-federal-student-aid-applications). For IRS non-filers, the FSA Handbook (2025–26 AVG, Ch. 4) accepts a signed non-filing statement plus W-2s, so ask whether the school specifically wants an IRS Verification of Non-filing Letter before requesting one
   - Replacing lost W-2 / 1099 → Wage and Income Transcript
   - Auditing PPP/EIDL loan → Tax Return Transcript
   - Disputing IRS balance / penalty → Tax Account Transcript or Record of Account
   - Personal records / financial planning → user picks based on data needed
2. **Filer's full legal name** — exactly as it appears on the original return
3. **Filer's SSN** (or ITIN) — the taxpayer ID under which the return was filed
4. **Spouse's name and SSN** if joint return — entered on lines 2a/2b. Transcripts of a joint return may be furnished to either spouse, and only one signature is required (Form 4506-T page 2, "Individuals")
5. **Current address** — line 3. The IRS mails transcripts only to the **address of record**, so ask whether the IRS has the current address. If lines 3 and 4 differ and the user has not changed the address with the IRS, the form says to file Form 8822 (Form 8822-B for a business)
6. **Address on the last return filed** — line 4, only if different from line 3
7. **Tax year(s) or period(s) requested** — line 9 takes the period end date as MM/DD/YYYY (12/31/YYYY for a calendar year; each quarter for quarterly returns); the form has four date slots
8. **Form number filed** — usually 1040, but could be 1040-SR, 1040-NR, 1120, 1120-S, 1065, etc. Line 6 takes only one tax form number per request.
9. **Transcript type** — 6a Return Transcript, 6b Account Transcript, 6c Record of Account, 7 Verification of Nonfiling, or 8 Form W-2/1099/1098/5498 series (wage and income) transcript
10. **Customer file number** (optional, line 5) — up to 10 numeric characters that will print on the transcript, e.g., a loan number supplied by a lender. It must not contain an SSN or name. It does NOT send the transcript to the third party
11. **Phone number** of the taxpayer on line 1a or 2a
12. **Signer and authority** — the taxpayer on line 1a or 2a signs and dates, and must check the box attesting authority to sign, or the form is not processed. A corporate officer, partner, executor, trustee, or other non-taxpayer signer enters a title and attaches the authorization document; a representative signs only if Form 2848 line 5 delegates that authority, with the Form 2848 attached

If the user is a fiduciary (executor, trustee, guardian) or heir requesting on behalf of someone else, IRC §6103(e) controls and documentation is required — flag for the user (Form 2848 has no skill in this repo yet).

---

## Workflow

### Step 1 — Try the online and phone channels first

Before filling out Form 4506-T, the agent should ask: "Have you tried your IRS Individual Online Account, or Get Transcript by Mail?"

URL: https://www.irs.gov/individuals/get-transcript

Individual Online Account (per irs.gov "Get your tax records and transcripts" and "Transcript types for individuals and ways to order them"):
- Is free and available any time
- Lets the user view, print, or download all five transcript types after signing in
- Requires an ID.me account: SSN or ITIN, a government-issued photo ID, and either a selfie (self-service) or a video chat with an ID.me agent
- Works only for the **taxpayer themselves**

Get Transcript by Mail, or the automated phone line 800-908-9946:
- Tax return transcript or tax account transcript only
- Needs the mailing address from the latest return
- Arrives in 5 to 10 calendar days at the address the IRS has on file

**When 4506-T is the right path:**
- The user can't verify with ID.me and needs a record of account, wage and income transcript, or Verification of Non-filing Letter (mail and phone channels offer only return and account transcripts)
- The user needs an account transcript older than the current and nine prior tax years, or a Verification of Non-filing Letter older than the three prior tax years (irs.gov says to use Form 4506-T for those)
- The user filed a fiscal-year return (the form says fiscal-year filers must use Form 4506-T for a return transcript)
- The user is requesting for an entity, or as a fiduciary or authorized signer
- The online wage and income transcript will not generate because the user has more than about 85 information returns (irs.gov says to submit Form 4506-T)

### Step 2 — Confirm transcript type

Pick the right type based on the user's purpose. Availability below is from the form and from https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them.

- **Line 6a — Return Transcript**: most line items from the originally filed Form 1040-series return, with forms and schedules. Does NOT show changes made after the original filing. Available for the current year and returns processed during the prior 3 processing years. **Usually meets mortgage lenders' needs.**
- **Line 6b — Account Transcript**: return type, filing status, AGI, taxable income, payments, penalty assessments, and adjustments made after the return was filed. Online: current and nine prior tax years; by mail/phone: current and three prior; older years via Form 4506-T. **Use for IRS balance disputes.**
- **Line 6c — Record of Account**: combines 6a + 6b. Available for the current year and 3 prior tax years. The form suggests it when the user is unsure which transcript is needed.
- **Line 7 — Verification of Nonfiling**: proof that the IRS has no record of a processed Form 1040-series return for the year as of the request date; it does not say whether the user was required to file. Current-year requests only after June 15; no restriction on prior years when requested on Form 4506-T.
- **Line 8 — Form W-2, 1099, 1098, 5498 series transcript (wage and income)**: data from information returns the IRS received. Up to 10 years (form); online, the current and nine prior tax years. State or local W-2 information is not included. For the current processing year, irs.gov says data is generally available online in the first week of February but may be incomplete; the form's own text says current-year information is generally not available until the year after it is filed. **Use for replacing lost W-2/1099 data.**

If the user is unsure, ask what data the recipient (lender, school, agency) needs. Often the recipient specifies — "we need a 2024 Tax Return Transcript" — and that maps directly to a single line.

### Step 3 — Confirm tax year(s)

For each year, line 9 takes the period end date in MM/DD/YYYY format (12/31/2024 for a calendar-year 2024 Form 1040). The form has four date slots; for more periods, file additional Form 4506-T forms.

Tax year ≠ calendar year for filing purposes. "Tax year 2024" means the return for income earned in calendar year 2024, which is filed in calendar year 2025. The transcript request is for the tax year the return covers.

For Wage and Income Transcripts (Line 8), the year is the year the income was paid. A 2024 W-2 reports 2024 wages and appears on the 2024 transcript.

### Step 4 — Confirm form number filed

Most individual filers file Form 1040, 1040-SR (for age 65+), or 1040-NR (nonresident aliens). Line 6 takes one tax form number per request.

If the user filed an entity return (1065, 1120, 1120-S), Form 4506-T also handles those, but the request goes in the entity's name and EIN, signed by an authorized person with a title, and uses the "Chart for all other transcripts".

### Step 5 — Determine routing

Page 2 of the form has two charts: one for individual transcripts (Form 1040 series, Form W-2, and Form 1099) and one for all other transcripts. Each maps the state the user lived in (or the business was in) **when that return was filed** to an IRS RAIVS office address and fax number. If more than one transcript is requested and the chart shows two different addresses, send it to the address based on the most recent return. As of the April 2025 revision:

| Chart | Office | Mail | Fax |
|-------|--------|------|-----|
| Individual | Austin | Internal Revenue Service, RAIVS Team, Stop 6716 AUSC, Austin, TX 73301 | 855-587-9604 |
| Individual and all other | Kansas City | Internal Revenue Service, RAIVS Team, Stop 6705 S-2, Kansas City, MO 64999 | 855-821-0094 |
| Individual and all other | Ogden | Internal Revenue Service, RAIVS Team, P.O. Box 9941, Mail Stop 6734, Ogden, UT 84409 | 855-298-1145 |

Look up the user's state in the correct chart in [`filing.md`](./filing.md) (the full state lists are there). The same state can map to different offices in the two charts (e.g., Georgia: Austin for individual transcripts, Kansas City for all other transcripts).

Some lenders use the **Income Verification Express Service (IVES)** — a paid IRS service for lenders and other participants. IVES requests use Form 4506-C, which the lender prepares and the taxpayer authorizes. If the lender provides a Form 4506-C, direct the user to sign that one — do not duplicate effort.

### Step 6 — Customer file number (Line 5) and delivery

Line 5 is an optional **customer file number**: up to 10 numeric characters that print on the transcript so the user or a lender can match it to a file. It must not contain an SSN or name (if it does, the IRS prints the generic "9999999999").

Delivery: the IRS mails the transcript only to the taxpayer's address of record. If the user moved and has not updated the address with the IRS, file Form 8822 first (or with the request), or the transcript goes to the old address. If a lender needs the transcript directly, the lender must use IVES (Form 4506-C); Form 4506-T cannot send it to them.

### Step 7 — Fill the form

Use [`references/line-by-line.md`](./references/line-by-line.md) for the complete map. High-level:

- Line 1a — Name shown on tax return (first name shown on a joint return; entity name for a business)
- Line 1b — First SSN, ITIN, or EIN on the return (a Form 1040 with Schedule C uses the SSN)
- Line 2a — Spouse's name (if joint return)
- Line 2b — Second SSN or ITIN (if joint return)
- Line 3 — Current name and address (include apt., suite, P.O. box, or inmate number)
- Line 4 — Previous address shown on the last return filed (if different from Line 3)
- Line 5 — Customer file number (optional, up to 10 digits)
- Line 6 — Tax form number, then box 6a, 6b, or 6c
- Line 7 — Verification of Nonfiling
- Line 8 — Form W-2 / 1099 / 1098 / 5498 series transcript
- Line 9 — Year or period requested (MM/DD/YYYY, up to four)
- Signature area — authority checkbox, phone number, signature, date, title (entities), spouse's signature (optional)

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

A filled-form draft (PDF-equivalent in markdown), routing instructions (mail address or fax number), and submission checklist.

### Step 10 — Submit

User has these submission options for the paper form (Form 4506-T page 2, "Where to file"):
- **Mail** to the RAIVS address from the correct chart
- **Fax** to the fax number from the same chart

The form says most requests are processed within 10 business days; the transcript then travels by mail to the address of record. The online account, Get Transcript by Mail, and 800-908-9946 remain alternatives for the types they support.

If the agent has browser-automation tooling and the user authorizes, see [`filing.md`](./filing.md) for the channel flows.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level summary below (Form 4506-T, Rev. April 2025).

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| 1a | Name shown on tax return | Filer's name as on the return; first name shown on a joint return | Use the name on the return even if it has changed since |
| 1b | First SSN, ITIN, or EIN | SSN/ITIN for an individual return (including a 1040 with Schedule C); EIN for a business return | |
| 2a | Spouse's name | Joint-return spouse's name as on the return | Blank if not joint |
| 2b | Second SSN or ITIN | Joint spouse's number | Blank if not joint |
| 3 | Current name and address | Include apt., room, suite, P.O. box, or inmate number | The IRS mails only to the address of record; if lines 3 and 4 differ and the IRS address was not changed, file Form 8822 / 8822-B |
| 4 | Previous address shown on the last return filed | Only if different from line 3 | |
| 5 | Customer file number | Optional; up to 10 numeric characters; printed on the transcript | Never an SSN or name (IRS substitutes "9999999999"); does not send the transcript to anyone |
| 6 | Tax form number + box | One form number (1040, 1065, 1120, ...); check 6a, 6b, or 6c | One tax form number per request |
| 6a | Return Transcript | Current year and returns processed in the prior 3 processing years | Usually what mortgage lenders want |
| 6b | Account Transcript | Payments, penalties, adjustments after filing | Available for most returns |
| 6c | Record of Account | 6a + 6b combined; current year and 3 prior tax years | The form suggests it when unsure |
| 7 | Verification of Nonfiling | Proof the IRS has no record of a filed return for the year | Current year only after June 15; no restriction on prior years |
| 8 | Form W-2 / 1099 / 1098 / 5498 series transcript | Information-return data the IRS received | Up to 10 years; no state/local W-2 data |
| 9 | Year or period requested | Period end date, MM/DD/YYYY (12/31/YYYY for a calendar year; each quarter for quarterly returns) | Four date slots |
| Signature area | Authority checkbox, phone number of taxpayer on line 1a or 2a, signature, date, title (entities), spouse's signature | Box must be checked or the form is not processed; IRS must receive the form within 120 days of the signature date | On a joint return at least one spouse signs |

---

## Validation

Before declaring the form ready, run these checks.

### Identity matching

- [ ] Name on Line 1a matches the name on the original return (including any suffix or middle name used); a filer who changed names signs with both names
- [ ] Line 1b holds the SSN/ITIN (individual return) or EIN (business return) shown on the return
- [ ] If joint return, spouse's name and SSN are on Lines 2a/2b; at least one spouse will sign
- [ ] Line 3 is the current address; if it differs from the IRS address of record, Form 8822 is filed or the user accepts that the transcript goes to the address of record
- [ ] Line 4 is filled only if the last return showed a different address

### Transcript type

- [ ] Line 6 shows exactly one tax form number
- [ ] One transcript box is checked per form (6a, 6b, 6c, 7, or 8). The form does not say multiple boxes are rejected; one per form keeps each request clean. Use 6c to get return and account data together
- [ ] Transcript type matches the user's purpose (Step 2 mapping)

### Year(s)

- [ ] No more than four periods on line 9
- [ ] Each period entered as MM/DD/YYYY (12/31/YYYY for calendar-year filers, the fiscal year-end, or each quarter end)
- [ ] User has filed a return for each requested year (otherwise, switch to Verification of Nonfiling on Line 7); a current-year Line 7 request is dated after June 15

### Routing

- [ ] Correct chart used: individual transcripts (Form 1040 series, W-2, 1099) vs all other transcripts
- [ ] State = where the user lived (or the business was) when the return was filed; for multiple returns with different addresses, the most recent return's state
- [ ] Mailing address or fax number copied from that chart row
- [ ] If the lender uses IVES (Form 4506-C), the lender provided the form — do not duplicate

### Customer file number (if Line 5 used)

- [ ] 10 numeric characters or fewer, no SSN, no name
- [ ] User understands the transcript is mailed to the address of record, not to the lender

### Signatures

- [ ] Authority checkbox in the signature area is checked
- [ ] Taxpayer signed and dated (spouse optional on a joint return)
- [ ] Phone number of the taxpayer on line 1a or 2a provided
- [ ] Title entered and authorization document attached if the signer acts for a corporation, partnership, estate, or trust; Form 2848 attached if a representative signs
- [ ] IRS will receive the form within 120 days of the signature date

---

## Output format

The agent's deliverable is a **filled draft** the user prints, signs, and submits.

```markdown
# Form 4506-T (Rev. April 2025) — DRAFT

## 1a. Name shown on tax return: <Full legal name>
## 1b. First SSN / ITIN / EIN on tax return: XXX-XX-XXXX

## 2a. Spouse's name shown on tax return (if joint): <Spouse name or blank>
## 2b. Second SSN or ITIN (if joint): XXX-XX-XXXX (or blank)

## 3. Current name and address: <Filer's current address>

## 4. Previous address shown on the last return filed (if different from 3): <Prior address or blank>

## 5. Customer file number (optional, up to 10 digits): <digits or blank>

## 6. Transcript requested — tax form number: <1040 / 1040-SR / 1120 / etc.>
   ☐ 6a. Return Transcript
   ☐ 6b. Account Transcript
   ☐ 6c. Record of Account

## 7. ☐ Verification of Nonfiling

## 8. ☐ Form W-2, Form 1099 series, Form 1098 series, or Form 5498 series transcript

## 9. Year or period requested (MM/DD/YYYY):
   <12/31/YYYY>
   <12/31/YYYY or blank>
   <blank>
   <blank>

## Signature area
☐ Signatory attests authority to sign (must be checked)
Phone number of taxpayer on line 1a or 2a: <phone>
Signature: ____________________   Date: ____________
Title (if line 1a is a corporation, partnership, estate, or trust): <title or blank>
Spouse's signature (optional on a joint return): ____________________   Date: ____________

## Submission instructions
- Chart: <individual transcripts / all other transcripts>
- State when the return was filed: <state> → <Austin / Kansas City / Ogden RAIVS Team>
- Method: <Mail to: <address>> OR <Fax to: <fax number>>
- Processing: most requests within 10 business days (form), then mailed
- Delivery: to the taxpayer's address of record with the IRS (Form 8822 filed? <yes/no/not needed>)

## Validation summary
- Identity: <pass/fail per check>
- Transcript type: <pass/fail>
- Year(s): <pass/fail>
- Routing: <pass/fail>
- Signature: <pass/fail>

## Sources cited
- IRS Form 4506-T (Rev. April 2025), including page 2 instructions and charts
- Transcript types and ways to order them: https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
```

The draft is the form ready to print, sign, and submit to the routing address or fax number.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 4506-T line with notes and edge cases
- [`references/transcript-types.md`](./references/transcript-types.md) — The five transcript types, what each shows, availability, and when to pick which
- [`references/get-transcript-online.md`](./references/get-transcript-online.md) — Individual Online Account, Get Transcript by Mail, and the phone line, and when they replace Form 4506-T
- [`references/related-forms.md`](./references/related-forms.md) — Form 4506 (full copy), Form 4506-T-EZ, Form 4506-C (IVES), Form 2848, Form 8821, Form 8822 — when to use each
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Common errors that get Form 4506-T rejected or delayed
- [`filing.md`](./filing.md) — Channel playbook, full mailing/fax charts, online and paper flows

## Examples

- [`examples/lender-transcript-request.md`](./examples/lender-transcript-request.md) — Homebuyer's lender requests 2 years of Tax Return Transcripts; online verification fails, so she faxes Form 4506-T and forwards the transcripts
- [`examples/replace-lost-w2.md`](./examples/replace-lost-w2.md) — Filer who lost his 2024 W-2 and 1099-NECs requests a wage and income transcript to file late
- [`examples/fafsa-non-filing-verification.md`](./examples/fafsa-non-filing-verification.md) — Parent who did not file asks for a Verification of Non-filing Letter for a school's FAFSA verification

## Sources

- [Form 4506-T (Rev. April 2025)](https://www.irs.gov/pub/irs-pdf/f4506t.pdf) — the form itself; instructions and mailing/fax charts are on page 2 (no separate instructions PDF)
- [About Form 4506-T](https://www.irs.gov/forms-pubs/about-form-4506-t) — IRS landing page; check for a newer revision
- [Get your tax records and transcripts](https://www.irs.gov/individuals/get-transcript) — Individual Online Account, Get Transcript by Mail, 800-908-9946
- [Transcript types and ways to order them](https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them) — availability by type and channel
- [Transcript availability](https://www.irs.gov/individuals/transcript-availability) — current-year timing after filing
- [Creating an account for IRS.gov](https://www.irs.gov/help/creating-an-account-for-irsgov) — ID.me requirements
- [Form 4506 (April 2025)](https://www.irs.gov/forms-pubs/about-form-4506) — request for full COPY of return ($30 per return, up to 75 calendar days)
- [Form 4506-T-EZ (March 2025)](https://www.irs.gov/forms-pubs/about-form-4506-t-ez) — short form, individual tax return transcript only
- [Form 4506-C (Rev. October 2022)](https://www.irs.gov/forms-pubs/about-form-4506-c) and [IVES for participants](https://www.irs.gov/individuals/income-verification-express-service-for-participants) — lender channel, $4 per transcript charged to the participant
- [Tax information for federal student aid applications](https://www.irs.gov/individuals/tax-information-for-federal-student-aid-applications) — FAFSA data exchange; IRS no longer accepts Form 8821 or 4506-C for FAFSA income verification
- [Form 2848](https://www.irs.gov/forms-pubs/about-form-2848) — Power of Attorney; line 5 must delegate signing Form 4506-T
- [Form 8821](https://www.irs.gov/forms-pubs/about-form-8821) — Tax Information Authorization
- [Form 8822](https://www.irs.gov/forms-pubs/about-form-8822) — Change of Address
- IRS RAIVS (Return and Income Verification Services) — the team that processes Form 4506-T
- IRC §6103 — confidentiality of tax returns and disclosure rules; §6103(e) for heirs, fiduciaries, and dissolved entities

## Disclaimer

Form 4506-T is a procedural form for obtaining transcripts. The skill encodes routing and field-fill rules. It is not tax advice. The agent should remind the user that transcripts are official IRS documents and may contain sensitive data — handle and forward with care.
