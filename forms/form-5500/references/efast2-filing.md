# EFAST2 filing system — overview, credentials, attachments, signatures

EFAST2 (ERISA Filing Acceptance System) is the DOL's electronic filing portal for Form 5500 / 5500-SF. Form 5500-EZ filers may also file electronically via EFAST2 (plan years beginning after 2019). Paper 5500-EZ is still accepted, except that for plan years beginning on or after January 1, 2025 a filer required to file at least 10 returns of any type with the IRS during the calendar year must file 5500-EZ through EFAST2 (2025 Form 5500-EZ instructions; Treas. Reg. §301.6058-2).

This reference covers the credentialing and submission mechanics in depth. The skill's `filing.md` covers the browser-automation flow; this file covers the underlying system the agent and user need to understand.

---

## What EFAST2 is and is not

**Is**:
- The DOL Employee Benefits Security Administration's (EBSA) electronic intake system for the Form 5500 series
- The required filing channel for Form 5500 and Form 5500-SF (both must be filed electronically, 2025 instructions)
- A shared system feeding data to the DOL, IRS, and PBGC
- Free to use (no filing fee charged by DOL for the filing itself)

**Is not**:
- A bookkeeping or recordkeeping system for the plan
- A replacement for plan documentation (the plan document still must exist and be available)
- A check on the plan's underlying compliance — it accepts the data the user provides and validates structure, not substance

URL: https://www.efast.dol.gov

---

## Credential types

Source: EFAST2 Guide for Filers and Service Providers (Document Version 4.0, December 2, 2024), Chapters 1–3.

**Sign-in**: Since January 1, 2024, the EFAST2 website is reached only through **Login.gov** (email, password, and two-factor authentication). The old EFAST2 User ID and password no longer sign anyone in.

**Registration**: After signing in with Login.gov, each person registers an EFAST2 profile and receives a **User ID** (the letter "A" plus seven digits) and a **4-digit PIN** on the confirmation page. There is no postal-mail step. Credentials belong to the individual, are not linked to a plan or EIN, cannot be transferred or shared, and can be used for multiple plans and years.

**User types** (select every one the person needs):

- **Filing Author**: creates, imports, validates, submits, and amends filings in IFILE; cannot sign unless also a Filing Signer
- **Filing Signer**: plan administrators, employers/plan sponsors, or DFEs who sign electronically; also service providers signing under written authorization
- **Schedule Author**: completes individual schedules in IFILE for import by a Filing Author
- **Transmitter**: submits filings through EFAST2-approved third-party software

The User ID + PIN together are the electronic signature. A filing that the plan administrator does not sign is subject to rejection and civil penalties (2025 Form 5500 instructions, Signature and Date). If the plan administrator is an entity, the signature must be in the name of a person authorized to sign for it.

**Service provider signature option**: A service provider with written authorization may sign electronically if the filing includes a PDF of the Form 5500 (or 5500-SF) bearing the plan administrator's manual signature; that signature image is then published with the filing.

---

## IFILE — the browser form-completion tool

EFAST2's primary submission interface for filers without specialized software is **IFILE** — a browser-based form-completion app inside the EFAST2 portal.

IFILE is the government's free internet-based filing application on the EFAST2 website. It handles Form 5500, 5500-SF, 5500-EZ, their schedules, PDF attachments, and Form 5558 (from January 1, 2025). A Filing Author prepares the filing; a Filing Signer signs it.

IFILE is NOT a tax-preparation tool. It does not pull data from accounting systems. The user (or TPA) enters data manually or pastes from a working spreadsheet.

### Error checking

Entries must be in the proper format or the software will not submit them. Check the return for errors before signing and submitting; IFILE and approved software both run error checks. After submission, EFAST2 should report a filing status within about 20 minutes, listing any errors or warnings; a clean filing shows "Filing Received". Filings with errors are subject to rejection and penalties; correct them with an amended filing (2025 Form 5500-SF instructions, How To File; EFAST2 Guide Chapter 5).

---

## XML upload (software-prepared filings)

If the plan administrator or TPA uses EFAST2-approved third-party software (list on the EFAST2 website), the software transmits the filing to EFAST2 instead of using IFILE. The person transmitting needs the Transmitter user type.

XML upload is preferred when:

- The plan has a complex Schedule H with many asset categories
- The TPA files for multiple plans and wants standardized output
- The audit firm provides Schedule H data in a software-compatible format

Software-transmitted filings still require a Filing Signer's User ID and PIN and receive the same EFAST2 filing status checks.

---

## Attachments

Schedule H requires several attachments for large plans. Common attachments:

| Attachment | When required | Format |
|------------|---------------|--------|
| **IQPA audit report** | Large pension plan with Schedule H | PDF |
| **Schedule of assets (held at end of year)** | Large pension plan with Schedule H | PDF |
| **Schedule of reportable transactions** | Large pension plan with Schedule H, if reportable transactions exceed 5% of plan assets | PDF |
| **Schedule of delinquent participant contributions** | Late deferrals reported on Schedule H line 4a | PDF |
| **Plan document** | Generally NOT required as attachment; available on request from DOL | PDF (if requested) |
| **Schedule SB and its attachments** | Single-employer DB plans, signed by the enrolled actuary | Schedule + PDF attachments |
| **Form 8955-SSA** (separated participants with deferred vested benefits) | Pension plans with such participants | Filed directly with the IRS; it cannot be attached to an EFAST2 filing |

The maximum size of one filing is 300 MB (EFAST2 Guide, Chapter 4). Compress PDFs if the audit report is large. Do not include attachments that show Social Security numbers; that can cause rejection.

---

## Signature requirements

The plan administrator (or, in the case of a multi-employer plan, the joint board of trustees / authorized representative) signs. The signature is electronic — the signer enters their EFAST2 User ID and PIN, and EFAST2 records the signature as authoritative.

For plans where the **sponsor and administrator are different entities** (rare; usually the same), both may sign depending on the plan structure. The 5500 form has a single signature block for the administrator; the sponsor is identified but does not sign on the form itself.

For **terminated plans being filed as final**, the same signature requirements apply as for an ongoing plan.

For **delinquent filings under DFVC**, check the DFVC box in Part I (Form 5500 line D, Form 5500-SF line C) and pay the DFVC penalty separately through the DOL's online DFVC system (not via EFAST2).

After submitting, check the filing status. "Processing Stopped" or "Unprocessable" can mean the filing lacked a valid electronic signature and may be treated as not filed (2025 Form 5500 instructions, Signature and Date).

---

## Submission and acknowledgment

After all signatures and checks pass, the filer clicks "Submit". Then:

1. **Acknowledgment ID (AckID)** — generated by EFAST2 to identify the filing; save it
2. **Filing status** — available within about 20 minutes on the Submissions page; "Filing Received" when no errors or warnings were found
3. **Records** — keep the signed filing and any acknowledgments (EFAST2 Guide §7.1)

If EFAST2 rejects, the rejection reason is displayed (specific error codes). Common rejection reasons:

- Duplicate filing for the same plan year (TPA already filed)
- Plan number mismatch with prior year
- Missing required schedule
- IQPA report not attached while Schedule H Part III (line 3a) reports an opinion
- Signer credentials invalid

Address the issue and resubmit. Each new submission generates a new Acknowledgment ID.

---

## Public disclosure

Nearly all Form 5500 and 5500-SF filings are posted on the Form 5500 Search page of the EFAST2 website, which needs no sign-in (EFAST2 Guide, Chapter 5). Anyone can search by:

- Plan name
- Sponsor name
- Sponsor EIN
- Plan number
- Plan year

Form 5500-EZ information is open to public inspection on request (IRC §6104(b)), but 5500-EZ returns, whether filed on paper or through EFAST2, are not published on the internet (2025 Form 5500-EZ instructions, Note (2); EFAST2 Guide, Chapter 5).

This public-disclosure obligation is one reason large plan sponsors review filings carefully — the DOL site is the source of competitive intelligence on benefit plans.

---

## Amendments

To amend a previously filed 5500 / 5500-SF, file an **amended return** via EFAST2:

1. Log in with filer credentials
2. Start a new filing for the same plan year
3. Mark "amended return" box
4. Fill the entire form with corrected data (not just the changes)
5. Attach updated schedules
6. Sign and submit

Amended returns supersede the prior filing. The original Acknowledgment ID is retained in EFAST2 history.

For 5500-EZ amendments: if the original was filed on paper, amend on a paper Form 5500-EZ with the IRS; if it was filed electronically (as 5500-EZ, or earlier as 5500-SF), amend electronically on Form 5500-EZ, never on 5500-SF (2025 Form 5500-EZ instructions, Amended Return).

---

## Common credential mistakes

1. **Trying to use Tax software EFIN as EFAST2 credentials** — completely separate systems. EFIN is for IRS e-file (1040, 1120, etc.); EFAST2 has its own credentialing.

2. **Sharing signer credentials across people** — the User ID and PIN are tied to one individual. Sharing creates audit-trail problems and may invalidate the signature.

3. **Trying to sign in with the old EFAST2 User ID and password** — since January 1, 2024 sign-in is through Login.gov only; the User ID and PIN are still used to sign. Test the Login.gov sign-in a week before filing.

4. **Plan administrator changes mid-year, but the new administrator hasn't registered as a Filing Signer** — register early; credentials are personal and cannot be handed over by the prior administrator.

5. **TPA filed on behalf of plan but the sponsor doesn't have access to the EFAST2 record** — the sponsor should obtain filer credentials and add their plan to their dashboard for visibility.
