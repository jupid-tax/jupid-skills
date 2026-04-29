# EFAST2 filing system — overview, credentials, attachments, signatures

EFAST2 (ERISA Filing Acceptance System) is the DOL's electronic filing portal for Form 5500 / 5500-SF. Form 5500-EZ filers may also file electronically via EFAST2 (since plan year 2020) but the IRS still accepts paper for 5500-EZ.

This reference covers the credentialing and submission mechanics in depth. The skill's `filing.md` covers the browser-automation flow; this file covers the underlying system the agent and user need to understand.

---

## What EFAST2 is and is not

**Is**:
- The DOL Employee Benefits Security Administration's (EBSA) electronic intake system for the Form 5500 series
- The exclusive filing channel for Form 5500 and Form 5500-SF since plan year 2009
- A shared system feeding data to the DOL, IRS, and PBGC
- Free to use (no filing fee charged by DOL for the filing itself)

**Is not**:
- A bookkeeping or recordkeeping system for the plan
- A replacement for plan documentation (the plan document still must exist and be available)
- A check on the plan's underlying compliance — it accepts the data the user provides and validates structure, not substance

URL: https://www.efast.dol.gov

---

## Credential types

EFAST2 has **two distinct credential types** that must be set up before filing. Many filers confuse them.

### Filer credentials

Used by the person submitting the filing on behalf of the plan. The filer can be:

- The plan administrator
- A third-party administrator (TPA)
- A recordkeeper (Fidelity, Empower, Guideline, Human Interest, etc.)
- A CPA or ERISA attorney acting on behalf of the plan

**How to obtain**: Online registration at https://www.efast.dol.gov. Receive User ID and PIN by email within minutes. No postal-mail step.

**Storage**: The filer's User ID is associated with the filer (not the plan). One filer can submit returns for multiple plans.

### Signer credentials

Used by the **plan administrator** (or a corporate officer of the sponsor designated as signer) to sign the filing. The signature is electronic; the signer's credentials authenticate the signature.

**How to obtain**: Apply at https://www.efast.dol.gov via "Register" → choose "Signer". Receive User ID by email; receive PIN by **postal mail** (USPS) at the address provided. Allow 7–14 days.

**Storage**: The signer's User ID + PIN are tied to the individual person, not the plan. The same individual can sign for multiple plans they administer.

**If the plan has multiple administrators or co-signers** (some defined benefit plans require both the sponsor and the trustee to sign), each individual obtains their own signer credentials. The filing requires both signatures.

### Why the two-step credential model

The DOL separates filer and signer credentials so that:

- TPAs can prepare filings (filer credentials) without ever having signature authority
- Signers (plan administrators) can review and sign filings prepared by others
- Plan sponsors can authorize a TPA to file but retain control over the signature

A filing prepared by a TPA but unsigned by the plan administrator will sit in "unsigned" status in EFAST2 until the administrator completes the signature step.

---

## IFILE — the browser form-completion tool

EFAST2's primary submission interface for filers without specialized software is **IFILE** — a browser-based form-completion app inside the EFAST2 portal.

IFILE features:

- Form 5500 / 5500-SF / 5500-EZ templates with all schedules
- Attachment uploads (PDF for IQPA audit reports, plan documents, etc.)
- Real-time validation (math checks, schedule consistency, field-format checks)
- Save and resume — partially completed filings stored on EFAST2 servers
- Multi-user collaboration — TPA fills, plan administrator reviews and signs

IFILE is NOT a tax-preparation tool. It does not pull data from accounting systems. The user (or TPA) enters data manually or pastes from a working spreadsheet.

### Validation flags in IFILE

IFILE validates on every save and on submission:

- **Format errors** (EIN format, plan number range, percentage values 0–100) — block submission
- **Math errors** (Schedule H rollforward not balancing, total participants ≠ active + retired + beneficiaries) — block submission
- **Schedule inconsistencies** (large plan box checked but no Schedule H attached, insurance contract indicated but no Schedule A) — block submission
- **Sanity warnings** (unusual participant count change, year-over-year asset drop) — warning only, do not block

The user must address all blocking errors before submission. Sanity warnings can be acknowledged and submitted with explanation.

---

## XML upload (software-prepared filings)

If the plan administrator or TPA uses a Form 5500 software product (Datair, ftwilliam.com, Relius, FT William, Pension Solutions, etc.), the software produces an EFAST2-compliant XML file. The XML is uploaded to EFAST2 instead of using IFILE.

XML upload is preferred when:

- The plan has a complex Schedule H with many asset categories
- The TPA files for multiple plans and wants standardized output
- The audit firm provides Schedule H data in a software-compatible format

XML upload still requires filer + signer credentials and goes through the same validation as IFILE.

---

## Attachments

Schedule H requires several attachments for large plans. Common attachments:

| Attachment | When required | Format |
|------------|---------------|--------|
| **IQPA audit report** | Large pension plan with Schedule H | PDF |
| **Schedule of assets (held at end of year)** | Large pension plan with Schedule H | PDF |
| **Schedule of reportable transactions** | Large pension plan with Schedule H, if reportable transactions exceed 5% of plan assets | PDF |
| **Schedule of delinquent contributions** | Late deferrals reported on Schedule H Line 4a | PDF |
| **Plan document** | Generally NOT required as attachment; available on request from DOL | PDF (if requested) |
| **Plan opinion letter / determination letter** | DB plans (Schedule SB) | PDF |
| **Actuarial certification** | DB plans (Schedule SB) | PDF |
| **Schedule SSA** | Reporting separated participants with vested benefits | Filed separately with IRS, not via EFAST2 |

Attachment file size limits apply (typically 100 MB per attachment, 200 MB total per filing). Compress PDFs if the audit report is large.

---

## Signature requirements

The plan administrator (or, in the case of a multi-employer plan, the joint board of trustees / authorized representative) signs. The signature is electronic — the signer enters their EFAST2 User ID and PIN, and EFAST2 records the signature as authoritative.

For plans where the **sponsor and administrator are different entities** (rare; usually the same), both may sign depending on the plan structure. The 5500 form has a single signature block for the administrator; the sponsor is identified but does not sign on the form itself.

For **terminated plans being filed as final**, the same signature requirements apply as for an ongoing plan.

For **delinquent filings under DFVC**, the signer signs as if filing on time. The DFVC penalty is paid separately (not via EFAST2).

### Signature timing

The signer can sign:

- Before submission (signer signs, then filer submits)
- After submission (filer submits as "unsigned"; signer logs in later and signs; the filing's effective date is the date of signature)

A filing not signed within 30 days of submission may be flagged. Sign promptly.

---

## Submission and acknowledgment

After all signatures and validation pass, the filer clicks "Submit". EFAST2 processes in real time:

1. **Acceptance** — typically within 1–2 minutes for IFILE; a few seconds for XML
2. **Acknowledgment ID** — generated and displayed; save this. It's the proof of filing.
3. **Status update** — viewable in the filer's filing history

If EFAST2 rejects, the rejection reason is displayed (specific error codes). Common rejection reasons:

- Duplicate filing for the same plan year (TPA already filed)
- Plan number mismatch with prior year
- Missing required schedule
- IQPA audit report not attached when Schedule H Line 1c indicates audit performed
- Signer credentials invalid

Address the issue and resubmit. Each new submission generates a new Acknowledgment ID.

---

## Public disclosure

Once accepted by EFAST2, the filing is publicly available within ~24 hours at https://www.efast.dol.gov/5500search. Anyone can search by:

- Plan name
- Sponsor name
- Sponsor EIN
- Plan number
- Plan year

Form 5500-EZ is **not** public — IRS-only (the IRS does not publish 5500-EZ data).

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

For 5500-EZ amendments, file a new paper return marked "amended" or use EFAST2 (since plan year 2020).

---

## Common credential mistakes

1. **Trying to use Tax software EFIN as EFAST2 credentials** — completely separate systems. EFIN is for IRS e-file (1040, 1120, etc.); EFAST2 has its own credentialing.

2. **Sharing signer credentials across people** — the User ID and PIN are tied to one individual. Sharing creates audit-trail problems and may invalidate the signature.

3. **Using expired credentials** — EFAST2 credentials don't formally expire but have not been used for 1+ years may need re-verification. Test login a week before filing.

4. **Plan administrator changes mid-year, but the new administrator hasn't gotten signer credentials** — apply early. The 7–14 day postal-mail wait can derail a filing deadline.

5. **TPA filed on behalf of plan but the sponsor doesn't have access to the EFAST2 record** — the sponsor should obtain filer credentials and add their plan to their dashboard for visibility.
