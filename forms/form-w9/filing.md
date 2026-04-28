# Delivering Form W-9 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) takes a completed W-9 draft and delivers it to the requestor through a secure channel. The W-9 is **not** filed with the IRS — there is no IRS submission flow. This file covers the delivery half: how to get the signed W-9 from the user's hands into the requestor's system without exposing the SSN/EIN.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a delivery channel from the decision tree below, then execute the channel-specific steps.

---

## Why "filing" is misleading for W-9

Three properties make W-9 different from Schedule C, Form 1040, and most other IRS forms:

1. **No IRS endpoint.** The form goes from the filer to the requestor. The IRS receives it only indirectly, via the 1099 the requestor files at year-end.
2. **Identity-theft-grade payload.** The form contains the filer's full legal name + SSN/EIN + address. Email-without-encryption exposes the SSN to interception, server-side storage, and phishing. The delivery channel matters more than the form contents.
3. **No statutory deadline.** The user can deliver whenever, but in practice the requestor will withhold 24% backup withholding (IRC §3406) on payments until the W-9 arrives, so the user's incentive is to deliver before the first invoice.

---

## Channel decision tree

The user picks the channel. If they don't know, default to **e-signature platform (DocuSign or Adobe Sign)** — it's encrypted, audit-logged, and IRS Pub 1345-compliant.

```
Requestor sent a DocuSign / Adobe Sign / Gusto / Bill.com link?
  → Use the requestor's link (Section 1)
    Best option: encrypted, audit-logged, no risk of SSN in email.

Requestor has a vendor / contractor portal (Stripe Connect, Upwork, Fiverr, Etsy)?
  → Upload directly through the portal (Section 2)
    Most platforms collect W-9 info via a built-in form, not a PDF upload.

Requestor said "just email me your W-9"?
  → Use a password-protected PDF (Section 3)
    Send password via a separate channel (text message, Signal, phone call).
    Plain-text email is NOT acceptable — block.

Requestor is a small client with no e-signature system?
  → Encrypted email (PGP / S/MIME) OR password-protected PDF (Section 3)

Requestor only accepts paper / fax?
  → Fax (Section 4) or certified mail (Section 5)
    Fax is point-to-point and surprisingly secure.
    Mail is slow but acceptable.

Plain-text email with W-9 PDF attached?
  → BLOCK. Never. SSN over plain SMTP is a known phishing harvesting target.
```

---

## Section 1 — E-signature platform (DocuSign / Adobe Sign / Gusto)

These are the canonical channels for W-9 delivery in 2026. They meet IRS Pub 1345 e-signature standards (signer identity, intent, document, audit trail) and avoid the SSN-in-email problem entirely.

### Pre-flight

Agent must have:

- The user's permission to fill the W-9 on their behalf
- The completed Schedule W-9 draft from `SKILL.md`
- Access to the user's email account (the e-signature platform sends a signing link to the user's email)
- The user's intent to sign (explicit consent at submission — "I authorize delivery to <requestor> via <channel>")

### Browser flow — DocuSign envelope sent BY the requestor

This is the most common case: the requestor initiates a DocuSign envelope and emails the link to the user.

1. **Open** the DocuSign email and click "Review Document"
2. **Verify** at the DocuSign landing page:
   - The sender's name + email matches the requestor the user expected
   - The document is in fact a Form W-9 (not something else attached)
   - The signing certificate footer shows DocuSign Inc. as the issuer
3. **Click** "Continue" and accept the electronic-records and signatures disclosure
4. **Field-by-field mapping** from the SKILL.md draft to DocuSign field labels:

| W-9 Line | DocuSign field label (typical) | Source (in draft) |
|----------|--------------------------------|-------------------|
| 1 | "Name (as shown on your income tax return)" | Identity Line 1 |
| 2 | "Business name / disregarded entity name" | Identity Line 2 |
| 3a (Individual/sole proprietor) | "Individual/sole proprietor" checkbox | Line 3 |
| 3a (C Corporation) | "C Corporation" checkbox | Line 3 |
| 3a (S Corporation) | "S Corporation" checkbox | Line 3 |
| 3a (Partnership) | "Partnership" checkbox | Line 3 |
| 3a (Trust/estate) | "Trust/estate" checkbox | Line 3 |
| 3a (LLC) | "Limited liability company" checkbox + classification letter | Line 3 |
| 3b | "Pass-through FATCA exemption" checkbox | Line 3b |
| 4 — Exempt payee code | "Exempt payee code (if any)" | Line 4 (usually blank) |
| 4 — FATCA reporting code | "Exemption from FATCA reporting code (if any)" | Line 4 (usually blank) |
| 5 | "Address (number, street, and apt. or suite no.)" | Line 5 |
| 6 | "City, state, and ZIP code" | Line 6 |
| 7 | "List account number(s) here (optional)" | Line 7 |
| Part I | "Social security number" boxes OR "Employer identification number" boxes | TIN |
| Part II | "Signature of U.S. person" + "Date" | Certification |

5. **Verify TIN format** — DocuSign typically renders the SSN as nine separate boxes (or two/three groups for SSN/EIN respectively). The agent must enter exactly nine digits. Pause for the user to confirm visually before signing.

6. **Item 2 strike-through (if applicable)** — if the user has a current IRS BUW notice in effect, the agent must strike through item 2 of the certification before signing. DocuSign provides a "strike-through" annotation tool; some W-9 templates have an explicit "Strike item 2" checkbox.

7. **Sign** — DocuSign captures a signature (drawn / typed / uploaded image) plus an audit-trail timestamp + IP address.

8. **Click** "Finish". DocuSign emails both parties a copy of the executed document with the audit-trail PDF.

9. **Save** the executed W-9 + audit trail to the user's secure storage. Do **not** save to agent logs or vector stores.

### Browser flow — Adobe Sign

Same pattern as DocuSign; field labels are slightly different but functionally equivalent. The "Final Receipt" PDF includes the audit log.

### Browser flow — Gusto / Bill.com / Deel contractor onboarding

Vendor onboarding platforms typically use a built-in W-9 form (not a PDF). The agent fills the form fields directly, signs in the platform, and clicks Submit. Field labels match the IRS PDF 1:1.

### What the agent should NOT do

- Do not sign without explicit user consent at the moment of signing
- Do not bypass DocuSign's identity-verification email click-through
- Do not download the W-9 PDF and re-host it anywhere outside the user's storage
- Do not log the SSN/EIN in agent transcripts or telemetry

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | DocuSign's KBA (knowledge-based authentication) tripped | User completes KBA personally; agent does not impersonate |
| "Document expired" | Requestor's envelope timed out (typically 30 days) | Ask requestor to re-send |
| Field labels don't match draft | Requestor used a custom W-9 template | Map by visual position on the form, fall back to the official IRS field labels |
| "Cannot use this browser" | DocuSign blocks headless browsers | Use a non-headless Playwright run; respect DocuSign's anti-automation rules |

---

## Section 2 — Vendor / contractor portal

For platforms that maintain their own contractor records (Upwork, Fiverr, Etsy, Stripe Connect, Amazon Vendor, Uber, DoorDash, Bill.com, Tipalti):

### Pre-flight

- The user's existing platform account credentials (the agent MUST NOT create a new account)
- Two-factor authentication available (the agent pauses for the user)

### Browser flow

1. Sign in to the platform
2. Navigate to "Tax info" / "W-9" / "Payment & Tax" / "Vendor info" — naming varies
3. Most platforms render a structured W-9 form with the same fields as the IRS PDF
4. Fill from the draft using the field-label mapping above
5. Sign electronically (platform captures audit trail)
6. Submit. Platform stores W-9 internally; the agent does not receive a copy
7. Capture a screenshot of the confirmation for the user's records

### What the agent should NOT do

- Do not export the W-9 PDF from the platform unless the user explicitly wants a copy in their own storage
- Do not change the address on the platform without confirming the user wants it changed (it may be the user's payout address)

---

## Section 3 — Encrypted email / password-protected PDF

Use only when the requestor cannot offer an e-signature platform or portal. Two acceptable variants:

### Variant 3a — Password-protected PDF + separate password channel

1. Fill the IRS fillable PDF (https://www.irs.gov/pub/irs-pdf/fw9.pdf) using a PDF tool
2. Sign electronically (agent must verify the signature meets IRS Pub 1345 standards: identity, intent, document, audit trail)
3. Apply a strong password to the PDF (PDF native encryption; 12+ character random password)
4. Email the password-protected PDF to the requestor
5. Send the password via a SEPARATE channel: SMS, Signal, or phone call. **Never** in the same email or email thread
6. Confirm the requestor received and opened the file; rotate the password if the email seems compromised

### Variant 3b — PGP / S/MIME encrypted email

1. Verify the requestor's public key (out-of-band fingerprint check)
2. Encrypt the W-9 PDF to the requestor's key
3. Sign with the user's private key
4. Send

### What the agent should NOT do

- Do not attach an unencrypted W-9 PDF to plain email — block this every time
- Do not include the password in the same email body or signature
- Do not post the PDF to a "share link" that doesn't expire (Google Drive public link, Dropbox public link)

---

## Section 4 — Fax

Surprisingly secure because fax is point-to-point. Use if the requestor specifies fax as their preferred channel.

1. Verify the fax number from the requestor's official website (not from a cold email)
2. Print the W-9 (or use an e-fax service like HelloFax / eFax)
3. Send during business hours so the recipient retrieves the page promptly
4. Confirm receipt by phone

E-fax services typically encrypt in transit and store the document on their servers — confirm the e-fax provider has SOC 2 / HIPAA-grade controls if the user is sensitive about server-side storage.

---

## Section 5 — Certified mail

Slowest channel. Use for users who prefer paper or have identity-theft concerns about digital channels.

1. Print the completed W-9
2. Sign in ink
3. Mail via USPS Certified Mail with Return Receipt to the requestor's official mailing address
4. Keep the certified-mail receipt as proof of delivery

The W-9 itself does not require a postmark date for IRS purposes (it's not filed with IRS), but a certified-mail receipt protects the user if the requestor claims they never received it and applies backup withholding.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never send a W-9 without explicit user consent** at the moment of delivery. "I authorize you to send the W-9 to <requestor> via <channel> right now" must be captured.
2. **Never store SSN, EIN, DOB, or signature image** in agent logs, vector stores, or transcripts. Pull at delivery time, use, discard.
3. **Never email a W-9 unencrypted.** No exceptions. If the requestor refuses anything else, the user should reconsider the engagement.
4. **Never bypass the requestor's verification.** If the e-signature platform asks the user to prove identity (KBA, MFA, email click-through), pause and let the user respond directly.
5. **Always capture delivery confirmations** as screenshots or audit-log PDFs stored under the user's account, not the agent's.
6. **If the requestor seems suspicious** (unsolicited request, mismatched email domain, urgent pressure tactics), **stop and surface the issue.** Phishing for W-9s is common and well-documented.
7. **Rotate the W-9** if the user suspects compromise. Forming a new EIN may be required if SSN is exposed and identity theft occurs.

---

## Archival and recordkeeping

After delivery, advise the user:

- Keep an **encrypted copy** of every W-9 sent, with: requestor name, requestor email, delivery channel, delivery date, executed PDF, audit-trail PDF
- For security archives, **redact** the TIN from working copies — keep the unredacted version only in a password manager or encrypted vault
- Maintain a **W-9 ledger**: which clients have your W-9 on file, the version sent, the date sent. When the user's address / name / TIN changes, re-issue to every active requestor on the ledger.
- Backup withholding amounts (if any were applied before the W-9 arrived) appear on **Form 1099 Box 4** at year-end and credit against the user's tax liability via Form 1040 Line 25c.
