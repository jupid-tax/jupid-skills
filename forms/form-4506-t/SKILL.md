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
  $43 fee per IRS, takes longer); current-year tax info before the IRS has
  finished processing (call IRS directly); third-party access to tax info for
  ongoing matters (Form 8821 Information Authorization or Form 2848 Power of
  Attorney); business return transcripts where the entity needs an EIN-based
  request (Form 4506-T still works but use the entity's name and EIN, not the
  individual filer's).
form: Form 4506-T (Request for Transcript of Tax Return)
audience: [individual]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f4506t.pdf
---

# Form 4506-T — Request for Transcript of Tax Return

This skill produces a correctly filled Form 4506-T to request one of five IRS transcript types: Tax Return Transcript, Tax Account Transcript, Record of Account Transcript, Wage and Income Transcript, or Verification of Non-filing Letter.

The form itself is short — one page. The complexity is in (a) picking the right transcript type for the user's purpose, (b) deciding whether to use the online "Get Transcript" portal first (free, instant for most users), and (c) routing the form to the correct IRS office (varies by the requester's state).

Transcripts are **free**. They are different from a full Form 4506 "copy of return" request, which costs $43 per return (IRS, current fee) and takes 60-75 days.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions "Form 4506-T", "tax transcript", or "transcript request"
- The user's mortgage lender, student loan servicer, SBA loan officer, or auditor is requesting a tax transcript
- The user lost a W-2 or 1099 and needs the IRS-reported income data
- The user is filling out FAFSA and needs Verification of Non-filing
- The user is replying to an IRS notice that requires proof of prior filings
- The user is in immigration / passport renewal proceedings requiring tax-history verification
- The user needs to confirm a balance owed, payment history, or penalty/interest detail

Do **not** engage this skill when:

- The user wants a **full copy** of their original Form 1040 with attachments — that is **Form 4506** (different form, $43 per return, takes 60-75 days)
- The user wants to authorize a third party to **discuss** tax matters with the IRS on an ongoing basis — that is Form 2848 (Power of Attorney) or Form 8821 (Tax Information Authorization)
- The user wants current-year information **before** the IRS has finished processing the return (transcripts typically available 2-3 weeks after e-file acceptance, 6-8 weeks after paper)
- The user is trying to obtain **someone else's** transcript without authorization — only the taxpayer (or their authorized representative via Form 2848/8821) can request

If the user just wants past-year totals for their own records, suggest they try **Get Transcript Online** first (https://www.irs.gov/individuals/get-transcript) — most users can authenticate and download instantly with no Form 4506-T needed.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop.

1. **Purpose** — what does the user actually need the transcript for? This determines which transcript type. Common purposes:
   - Mortgage application → Tax Return Transcript (last 2 years usually)
   - FAFSA → Tax Return Transcript (or Verification of Non-filing if no return was filed)
   - Replacing lost W-2 / 1099 → Wage and Income Transcript
   - Auditing PPP/EIDL loan → Tax Return Transcript
   - Disputing IRS balance / penalty → Tax Account Transcript or Record of Account
   - Personal records / financial planning → user picks based on data needed
2. **Filer's full legal name** — exactly as it appears on the original return
3. **Filer's SSN** (or ITIN) — the taxpayer ID under which the return was filed
4. **Spouse's name and SSN** if joint return — both spouses must be on Form 4506-T for a joint transcript (the IRS treats spouses as separate taxpayers; a joint return transcript is technically two transcripts)
5. **Current address** — the address where the IRS will mail the transcript
6. **Address on the most recent return filed** — if it differs from current address, both must be entered (Lines 3 and 4)
7. **Tax year(s) requested** — which year(s) the user needs. List each separately, in YYYY format (Form 4506-T accepts up to 4 years per request; for more, file additional 4506-T forms)
8. **Form number filed** — usually 1040, but could be 1040-SR, 1040-NR, 1120, 1120-S, 1065, etc. The transcript request is form-specific.
9. **Transcript type** — explicit choice of one of the five (or two for individual: 6a Return Transcript or 6b Account Transcript; 6c Record of Account; 7 Verification of Non-filing; 8 Wage and Income)
10. **Third-party recipient information** (if any) — name, address, phone of the lender / school / agency requesting the transcript. The IRS can mail directly to them via Line 5.
11. **Daytime phone** — IRS may call to verify
12. **Signature method** — Form 4506-T requires the taxpayer's wet signature OR an electronic signature acceptable to the IRS. The form has a signature box that must be filled.

For a joint return, **both spouses** must sign for full access. A non-signing spouse cannot request joint transcripts.

If the user is a fiduciary (executor, trustee, parent of minor child) requesting on behalf of someone else, additional documentation is required — flag for the user and possibly route to the (forthcoming) `form-2848` skill.

---

## Workflow

### Step 1 — Try Get Transcript Online first

Before filling out Form 4506-T, the agent should ask: "Have you tried the IRS Get Transcript online portal?"

URL: https://www.irs.gov/individuals/get-transcript

The online portal:
- Is free
- Returns transcripts immediately (after identity verification)
- Supports all five transcript types
- Available 24/7
- Works for the **taxpayer themselves** (not for third parties)

Identity verification uses ID.me (since Aug 2022). The user needs:
- Government-issued photo ID
- Smartphone with camera (for selfie verification) OR live video session
- Email + phone number under their name
- A Social Security number

If the user can authenticate, they download transcripts immediately and don't need 4506-T.

**When 4506-T is the right path:**
- User can't pass ID.me identity verification (no smartphone, identity-theft history, etc.)
- User wants the IRS to mail directly to a third party (lender, school)
- User is requesting a joint transcript and only one spouse can authenticate
- User needs the transcript for a specific business need that requires the formal 4506-T paper trail (some lenders explicitly require it)

### Step 2 — Confirm transcript type

Pick the right type based on the user's purpose. There is no "all" option; the user picks one (or files multiple Form 4506-Ts).

- **Line 6a — Return Transcript**: shows most line items from the originally-filed Form 1040 series (filing status, AGI, taxable income, total tax, etc.). Does NOT show changes made after the original filing (amendments, IRS adjustments). Available for current year and 3 prior tax years. **Most common for mortgage and lender purposes.**
- **Line 6b — Account Transcript**: shows filing date, return type, marital status, AGI, taxable income, return-related transactions (payments, penalties, interest, refunds, IRS adjustments). Available indefinitely (going back many years). **Use for IRS balance disputes.**
- **Line 6c — Record of Account**: combines 6a + 6b in one document. Available for current year and 3 prior tax years.
- **Line 7 — Verification of Non-filing Letter**: confirms the IRS has no record of a Form 1040 filed for the requested year. **Required for FAFSA when student or parent did not file taxes.**
- **Line 8 — Wage and Income Transcript**: shows third-party-reported income data (W-2, 1099-NEC, 1099-MISC, 1099-DIV, 1099-INT, 1099-R, K-1, 1098-mortgage interest, etc.). Available for last 10 years. **Use for replacing lost W-2/1099 documents.** Note: data appears 2-3 months after the issuing party reports it; current-year W-2s may not be available until mid-summer.

If the user is unsure, ask what data the recipient (lender, school, agency) needs. Often the recipient specifies — "we need a 2023 Tax Return Transcript" — and that maps directly to a single line.

### Step 3 — Confirm tax year(s)

For each year, format as YYYY (e.g., "2024", "2023"). Form 4506-T allows up to **4 years** per request. If the user needs more, file additional Form 4506-T forms.

Tax year ≠ calendar year for filing purposes. "Tax year 2024" means the return for income earned in calendar year 2024, which is filed in calendar year 2025. The transcript request is for the tax year the return covers.

For Wage and Income Transcripts (Line 8), tax years are also fiscal-year-of-income. A 2024 W-2 reports 2024 wages and would appear on the 2024 tax-year transcript.

### Step 4 — Confirm form number filed

Most individual filers file Form 1040, 1040-SR (for age 65+), or 1040-NR (nonresident aliens). The 4506-T request is form-specific — entering "1040" requests the 1040 transcript.

If the user filed an entity return (1065, 1120, 1120-S), Form 4506-T also handles those, but the request goes in the entity's name and EIN, not the individual. The address and signature must be the entity's authorized signatory.

### Step 5 — Determine routing

Form 4506-T submissions route to one of two IRS offices based on the **requester's** state of residence. The form's instructions include the routing chart. As of the current revision:
- Some states route to RAIVS (Return and Income Verification Services) Team in Kansas City, MO
- Others route to RAIVS in Ogden, UT or Austin, TX

The agent must look up the routing address in the form instructions for the user's state. Routing addresses are listed on page 2 of the form.

For fax, fax numbers are also state-dependent. Faxing is faster than mail (3-7 business days vs. 10-14 calendar days).

Some lenders use the **Income Verification Express Service (IVES)** — a paid IRS service for high-volume requesters. IVES requests use a different form variant (Form 4506-C). If the lender provides their own pre-filled form, it may be a 4506-C. Direct the user to sign that one — do not duplicate effort.

### Step 6 — Decide third-party delivery (Line 5) or self-delivery

Line 5 lets the user direct the IRS to mail the transcript directly to a third party (lender, school, agency).

- **If yes** (Line 5 filled): the IRS sends to the third party. The user does not get a copy. Faster for lenders; less paper trail for the user.
- **If no** (Line 5 blank): the IRS sends to the user's address (Line 3). The user then forwards to the third party.

If the lender accepts third-party delivery (most major lenders do), filling Line 5 is the simpler path. The lender's name, address, phone, and customer file number (often called "loan number") go in Line 5.

**Security caveat**: filling Line 5 means the IRS sends sensitive tax data to a third party. Confirm the user truly authorizes this and confirm the recipient address is correct. Wrong address = transcript goes to a stranger.

### Step 7 — Fill the form

Use [`references/line-by-line.md`](./references/line-by-line.md) for the complete map. High-level:

- Line 1a — Name shown on tax return (individual or entity)
- Line 1b — First taxpayer ID number (SSN/EIN/ITIN)
- Line 2a — Spouse's name (if joint return)
- Line 2b — Spouse's ID
- Line 3 — Current address (where transcript is sent if Line 5 is blank)
- Line 4 — Previous address shown on the last return filed (if different from Line 3)
- Line 5 — Third-party recipient (optional)
- Line 6 — Transcript type request (single line of: 6, 6a, 6b, or 6c)
- Line 7 — Verification of Non-filing
- Line 8 — Wage and Income Transcript
- Line 9 — Year(s) requested (up to 4)
- Signature box — taxpayer signature, date, phone
- Spouse signature (if joint)

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

A filled-form draft (PDF-equivalent in markdown), routing instructions (mail address or fax number), and submission checklist.

### Step 10 — Submit

User has three submission options:
- **Mail**: USPS to the routing address (slowest; allow 10-14 days for IRS processing, plus mail time)
- **Fax**: faster; usually 3-7 business days for IRS processing
- **Online via Get Transcript** (alternative): if the user can authenticate, skip the form entirely

If the agent has browser-automation tooling and the user authorizes, see [`filing.md`](./filing.md) for IRS portal flows (Get Transcript Online, Get Transcript by Mail).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level summary below.

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| 1a | Name on return | Filer's legal name as on 1040 | Match exactly — including suffix (Jr., III) if used |
| 1b | First taxpayer ID | SSN (or ITIN, EIN) | 9 digits; use dashes (XXX-XX-XXXX) |
| 2a | Spouse name | Joint-return spouse's legal name | Blank if not joint |
| 2b | Spouse ID | Joint spouse's SSN | Blank if not joint |
| 3 | Current address | Where IRS will mail (if Line 5 blank) | Street, city, state, ZIP |
| 4 | Previous address | Prior address shown on most recent return | Only if different from Line 3 |
| 5 | Third-party | Recipient name + address + phone + customer file number | Optional; risky — confirm |
| 6 | Transcript type | Choose ONE: 6, 6a (Return), 6b (Account), 6c (Record of Account) | Service Center listed below |
| 6a | Return Transcript | Check this box for return transcript | Most common for lenders |
| 6b | Account Transcript | Check this box for account transcript | For balance disputes |
| 6c | Record of Account | Check this box | Combines 6a + 6b |
| 7 | Verification of Non-filing | Check this box if requesting non-filing letter | For FAFSA, immigration |
| 8 | Wage and Income Transcript | Check this box for W-2/1099 history | For replacing lost income docs |
| 9 | Year(s) | Up to 4 years requested, format MM/DD/YYYY (use 12/31/YYYY for calendar-year filers) | Each line one year |
| Sig | Taxpayer signature | Wet signature (paper) or e-sig (some channels) | Required |
| Sig 2 | Spouse signature | If joint return | Required for joint transcripts |

---

## Validation

Before declaring the form ready, run these checks.

### Identity matching

- [ ] Name on Line 1a matches the legal name on the original return (including any suffix or middle name used)
- [ ] SSN on Line 1b is 9 digits, formatted XXX-XX-XXXX
- [ ] If joint return, spouse's name and SSN are on Lines 2a/2b — and both spouses will sign
- [ ] Current address on Line 3 matches the address the user wants the transcript mailed to (if Line 5 blank)
- [ ] If Line 4 is filled, the previous address matches the address on the most recent return filed (the IRS uses this to verify identity)

### Transcript type

- [ ] Exactly one transcript type box is checked (6a, 6b, 6c, 7, or 8 — not multiple)
- [ ] If user needs multiple types, file separate Form 4506-T forms (one per type)
- [ ] Transcript type matches the user's purpose (Step 2 mapping)

### Year(s)

- [ ] Up to 4 years requested
- [ ] Each year formatted correctly (often as 12/31/YYYY for calendar-year filers, or year-end date for fiscal-year)
- [ ] User has filed a return for each requested year (otherwise, switch to Verification of Non-filing on Line 7)

### Routing

- [ ] Mailing address matches the chart in the form instructions for the user's state
- [ ] If faxing, fax number matches the chart for the user's state
- [ ] If using IVES (Form 4506-C), the lender provided the form — do not duplicate

### Third-party (if Line 5 used)

- [ ] Third party's address verified (confirm with the user — wrong address sends sensitive data to wrong party)
- [ ] Customer file number (loan number, school ID) included if requested by the third party
- [ ] User explicitly authorized third-party delivery

### Signatures

- [ ] Taxpayer signed and dated
- [ ] Spouse signed and dated (if joint)
- [ ] Daytime phone provided
- [ ] Signature is no older than 120 days when received by IRS (per current form instructions)

---

## Output format

The agent's deliverable is a **filled draft** the user prints, signs, and submits.

```markdown
# Form 4506-T — DRAFT

## 1a. Name shown on tax return: <Full legal name>
## 1b. First social security number / ITIN / EIN: XXX-XX-XXXX

## 2a. Second name on tax return (spouse if joint): <Spouse name or blank>
## 2b. Second SSN: XXX-XX-XXXX (or blank)

## 3. Current name and address: <Filer's current address>

## 4. Previous address shown on the last return filed (if different from 3): <Prior address or "Same as Line 3">

## 5. Third party (mail transcript directly to):
   Name: <Lender / school / agency>
   Address: <Recipient address>
   Phone: <Recipient phone>
   Customer file number: <Loan number / file ID>
   (Or: blank — IRS will mail to Line 3)

## 6. Transcript requested: <Form 1040 / 1040-SR / 1120 / etc.>
   ☐ 6a. Return Transcript
   ☐ 6b. Account Transcript
   ☐ 6c. Record of Account
   (Check exactly ONE box)

## 7. ☐ Verification of Non-filing
   (Check if requesting non-filing letter — typically for FAFSA)

## 8. ☐ Wage and Income Transcript
   (Check if requesting W-2/1099 history)

## 9. Year(s) requested: (Enter MM/DD/YYYY for each)
   <12/31/YYYY>
   <12/31/YYYY>
   <12/31/YYYY>
   <12/31/YYYY>

## Signature box
Signature of taxpayer: ____________________
Date: ____________
Daytime telephone: <phone>
Print/type name: <name>
Title (if line 1a is a corporation, etc.): <title or blank>

Spouse's signature (if joint): ____________________
Date: ____________
Print/type name: <spouse name>

## Submission instructions
- Method: <Mail to: <address>> OR <Fax to: <fax number>>
- Routing based on your state: <state> → <office>
- Expected processing: 5-10 business days for fax; 10-14 days for mail (plus mail time)
- The transcript will be sent to: <Line 3 address> OR <Line 5 third party> [based on Line 5 fill]

## Validation summary
- Identity: <pass/fail per check>
- Transcript type: <pass/fail>
- Year(s): <pass/fail>
- Routing: <pass/fail>
- Signature: <pass/fail>

## Sources cited
- IRS Form 4506-T (current revision)
- IRS Get Transcript portal: https://www.irs.gov/individuals/get-transcript
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
```

The draft is the form ready to print, sign, and submit. The user signs in wet ink (or via accepted e-signature on certain submission channels) and sends to the routing address.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 4506-T line with notes and edge cases
- [`references/transcript-types.md`](./references/transcript-types.md) — Deep dive on all five transcript types, what each shows, and when to pick which
- [`references/get-transcript-online.md`](./references/get-transcript-online.md) — When and how to use the IRS Get Transcript online portal (faster than 4506-T)
- [`references/related-forms.md`](./references/related-forms.md) — Form 4506 (full copy), Form 4506-C (IVES), Form 2848 (POA), Form 8821 (information authorization) — when to use each
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 10 common errors that cause IRS to reject Form 4506-T
- [`filing.md`](./filing.md) — Browser-automation playbook for online and fax/mail submission

## Examples

- [`examples/mortgage-application.md`](./examples/mortgage-application.md) — Homebuyer's lender requests 2 years of Tax Return Transcripts; user tries Get Transcript online first, falls back to 4506-T
- [`examples/lost-w2-1099.md`](./examples/lost-w2-1099.md) — Freelancer who lost W-2/1099s for 2024 needs Wage and Income Transcript to file 2025 return
- [`examples/fafsa-non-filing.md`](./examples/fafsa-non-filing.md) — College student's parent didn't file taxes (income below threshold); FAFSA requires Verification of Non-filing Letter

## Sources

- [Form 4506-T (latest)](https://www.irs.gov/pub/irs-pdf/f4506t.pdf) — the form itself; instructions are on page 2 of the form (no separate i4506t.pdf)
- [About Form 4506-T](https://www.irs.gov/forms-pubs/about-form-4506-t) — IRS landing page
- [Get Transcript Online](https://www.irs.gov/individuals/get-transcript) — preferred channel for most users
- [Form 4506](https://www.irs.gov/forms-pubs/about-form-4506) — request for full COPY of return ($43 fee, 60-75 days)
- [Form 4506-C](https://www.irs.gov/forms-pubs/about-form-4506-c) — used by Income Verification Express Service (IVES) participants (high-volume lenders)
- [Form 2848](https://www.irs.gov/forms-pubs/about-form-2848) — Power of Attorney for ongoing IRS representation
- [Form 8821](https://www.irs.gov/forms-pubs/about-form-8821) — Tax Information Authorization (read-only third-party access)
- IRS RAIVS (Return and Income Verification Services) — the back office that processes 4506-T requests
- IRC §6103 — confidentiality of tax returns and disclosure rules

## Disclaimer

Form 4506-T is a procedural form for obtaining transcripts. The skill encodes routing and field-fill rules. It is not tax advice. The agent should remind the user that transcripts are official IRS documents and may contain sensitive data — handle and forward with care.
