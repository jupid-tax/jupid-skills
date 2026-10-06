# Delivering Form W-4R to the Payer

How an agent equipped with web-portal, email, fax, or mail tooling can take a completed Form W-4R draft and deliver it to the payer (IRA custodian, 401(k) plan administrator, insurance company paying an annuity, etc.). Severance pay is wages and never goes on a W-4R (Pub. 15 (2026)); use the [`form-w4`](../form-w4/SKILL.md) skill for it. This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then collect the recipient's ink signature (or e-signature if the payer accepts), then execute the delivery channel.

**Form W-4R is NOT filed with the IRS.** "Give Form W-4R to the payer of your retirement payments" (2026 Form W-4R). The payer retains the form and applies the elected rate to the distribution.

The portal menu paths and payer-specific notes below are typical layouts, not verified against each payer's current site; payers rename menus often. Follow the on-screen labels and compare the rate shown before the user signs.

---

## Channel decision tree

The right delivery channel depends entirely on the payer. Most major US payers accept multiple channels; check the payer's website or call their participant-services line to confirm.

```
Is the payer a major brokerage (Fidelity, Schwab, Vanguard, E*TRADE,
Merrill Lynch, etc.) with a participant web portal?
  → Section 1 — Web portal upload (preferred)

Is the payer a 401(k) recordkeeper (Empower, Voya, Principal, Alight,
Fidelity NetBenefits, Schwab Workplace, etc.)?
  → Section 1 — Web portal upload, OR Section 2 — Distribution-request
    intake form (sometimes W-4R is embedded in the distribution form)

Is the payer an insurance company paying a commercial annuity
(nonperiodic payment or surrender)?
  → Section 3 — Insurance company service center

Is the payer a small custodian / TPA without a portal?
  → Section 4 — Email or fax

Recipient prefers paper?
  → Section 5 — USPS or private delivery
```

---

## Section 1 — Web portal upload (Fidelity, Schwab, Vanguard, etc.)

Most major brokerages and recordkeepers have a participant portal where the recipient can submit Form W-4R as part of the distribution request workflow. The form is often embedded directly in the distribution-request screen — no PDF upload needed; the user fills it inline.

### Pre-flight

The agent must have:

- The recipient's permission to log in / submit on their behalf
- The recipient's portal credentials (username + password + MFA code at submission time)
- The completed Form W-4R draft from `SKILL.md`
- Distribution-request details (amount, payment method, source account)

### Generic portal flow

1. **Log in** to the payer's participant portal
2. **Navigate** to the distribution / withdrawal request page (varies by payer):
   - Fidelity: "Move money" → "Withdraw money" → IRA / 401(k) selection
   - Schwab: "Service" → "Account distributions" → "Take an IRA distribution"
   - Vanguard: "Transact" → "Withdraw / sell" → "Distribute from an IRA"
   - Empower / employer 401(k) plans: "Distributions" or "Withdrawals" tab
3. **Select the source account** and distribution type:
   - Lump sum or partial withdrawal (nonperiodic or ERD — W-4R)
   - Plan installments over more than 1 year (periodic — W-4P); IRA distributions payable on demand are nonperiodic (W-4R) per the form
   - RMD (W-4R, default 10%)
   - Hardship withdrawal (W-4R, default 10%)
4. **Enter the withholding rate** when prompted. The portal usually presents:
   - Default rate (10% for nonperiodic, 20% for ERD) pre-checked
   - "Use a different rate" option that opens a percentage input
5. **Confirm the rate matches the W-4R draft**
6. **Sign electronically** if the portal supports e-signature (most do — typically a typed name + acknowledgment checkbox + MFA code)
7. **Capture confirmation**: confirmation number, screenshot, downloadable PDF receipt
8. **Verify the distribution amount and net (after-withholding) amount** displayed before final submission

### Payer-specific notes

**Fidelity** (NetBenefits 401(k), retail IRA): the W-4R is embedded in the distribution workflow; the portal asks for the withholding rate and stores the form server-side. The participant doesn't upload a PDF.

**Schwab**: the W-4R is similarly embedded for IRA distributions. For inherited IRAs and certain RMDs, the portal may ask for both federal and state withholding rates on the same screen.

**Vanguard**: the participant can fill the withholding rate in the distribution-request flow OR upload a signed W-4R PDF. Both approaches accepted.

**Empower / Voya / Principal / Alight (employer 401(k) recordkeepers)**: the participant typically must request a paper packet OR fill the distribution form online with W-4R fields embedded. Some recordkeepers require the participant to also submit a paper signature; the portal will indicate.

**TIAA**: distinct flow for 403(b) plans; check TIAA's specific instructions.

---

## Section 2 — Distribution-request intake form

Many recordkeepers issue a multi-page distribution request form that includes Form W-4R as one section. The recipient fills the entire packet at once and submits it via email, fax, mail, or upload.

### Common intake-form structure

Page 1: Participant identification (name, SSN, DOB, account number)
Page 2: Distribution election (lump sum, partial, percentage, RMD, etc.)
Page 3: Federal tax withholding (Form W-4R section embedded)
Page 4: State tax withholding (if applicable)
Page 5: Direct deposit / payment method
Page 6: Beneficiary acknowledgment (for spousal QDRO or beneficiary distributions)
Page 7: Signature block + spousal consent (if required for ERISA-covered plans)

### Pre-flight

The agent must have:

- Distribution-request packet PDF from the payer (downloaded from portal or requested by phone)
- Completed W-4R draft from `SKILL.md`
- All ancillary information (direct deposit routing/account, beneficiary info if needed)

### Flow

1. **Open the packet** in a fillable-PDF tool
2. **Fill Page 1** with recipient info matching payer records exactly
3. **Fill Page 2** with the distribution amount and type
4. **Fill the W-4R section** (Page 3 typically) with the rate from the draft. Verify the rate is in the allowed range:
   - ERD: ≥ 20%
   - Other nonperiodic: 0–100
5. **Fill state-tax section** (Page 4) if applicable; if not handled by this skill, leave for the recipient or coordinate with a state-tax skill
6. **Fill payment method** (Page 5): direct deposit (provide routing + account) or check (confirm mailing address)
7. **Spousal consent** (if applicable): for ERISA plans where the participant is married, a qualified joint and survivor annuity (QJSA) or qualified preretirement survivor annuity (QPSA) waiver may require notarized spousal consent — the agent does not handle notarization; this becomes a manual step
8. **Recipient signs** Page 7 in ink (or e-signs if the payer accepts e-signatures)
9. **Submit via the channel listed on the packet**:
   - Upload to portal
   - Email to a specific address (typically distributions@ or service@ at the payer)
   - Fax to a participant-services fax line
   - Mail to a specific PO box

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form returned for missing field" | Incomplete intake form | Re-complete and resubmit |
| "Spousal consent required" | ERISA plan, married participant, no spousal waiver | Obtain notarized spousal consent and resubmit |
| "Rate below mandatory minimum" | ERD with rate < 20% | Correct to ≥ 20% and resubmit |
| "Account information mismatch" | Name / address / SSN doesn't match payer records | Update records with payer first, then resubmit |

---

## Section 3 — Insurance company (commercial annuity)

Form W-4R covers nonperiodic payments from an annuity, "including a commercial annuity" (2026 Form W-4R, Purpose of form), e.g., a partial withdrawal or full surrender of a nonqualified deferred annuity. Withholding applies only to the taxable part (Pub. 575 (2025)).

### Pre-flight

- Contract number and the insurer's withdrawal/surrender request form
- Completed W-4R draft (other nonperiodic: 10% default, 0–100% allowed)
- Taxable amount estimate from the insurer (gain over investment in the contract)

### Flow

1. **Request the withdrawal or surrender packet** from the insurer's service center or portal
2. **Attach the signed W-4R** (or complete the insurer's embedded withholding section with the same rate)
3. **Submit** through the channel the packet lists (portal upload, fax, mail)
4. **Confirm** on the confirmation statement that the elected rate was applied to the taxable amount

### Not a W-4R case: severance pay

If the user says their former employer asked for a W-4R for severance: "Severance payments are wages subject to social security and Medicare taxes, federal income tax withholding, and FUTA tax" (Pub. 15 (2026)). The employer withholds as on supplemental wages (Pub. 15 (2026), section 7); the employee's tool is Form W-4. Ask HR what the form is for; if the payment is from a retirement plan (not severance), classify it with [`references/distribution-types.md`](./references/distribution-types.md).

---

## Section 4 — Email or fax (smaller custodians, TPAs)

Some smaller IRA custodians and third-party administrators (TPAs) accept the form via email or fax.

### Pre-flight

- Payer's accepted channel (email address or fax number) — check the payer's website or call
- Completed and signed W-4R PDF
- Cover-letter template (Section 6 below)

### Flow

1. **Print the completed W-4R PDF**
2. **Sign in ink**
3. **Scan the signed form**
4. **Compose** an email (or prepare a fax cover sheet) to the payer with:
   - Subject: "W-4R for [Account Holder Name] — Account [last 4 digits]"
   - Body: brief reference to the upcoming distribution and the elected rate
   - Attachment: signed W-4R PDF
5. **Send** and **save the sent email** as proof of delivery
6. **Follow up** if no acknowledgment within 5 business days

### Email security considerations

W-4R contains an SSN. Do not send unencrypted email if the recipient or payer has any concern about email security:

- Use the payer's secure-message portal if available (most major payers have one)
- Use encrypted email (S/MIME, PGP) if both sides support it
- If neither, use fax or mail

---

## Section 5 — USPS or private delivery (paper mail)

The most secure but slowest option.

### Pre-flight

- Payer's mailing address for distribution requests (often a specific PO box, different from the general corporate address)
- Completed and signed W-4R
- Cover letter
- Tracking method (USPS Certified Mail or private delivery)

### Flow

1. **Print** the signed W-4R
2. **Print** the cover letter (Section 6 template)
3. **Assemble** in an envelope with the payer's mailing address
4. **Mail via USPS Certified Mail with Return Receipt** (recommended) or private delivery service with tracking
5. **Retain** the postmark receipt and tracking record
6. **Track delivery** until confirmed

### Mailing addresses

Pull from the payer's website, account statement, or a direct call. Do not hardcode addresses — they change.

---

## Section 6 — Cover-letter template

```
[Recipient Name]
[Recipient Address]

[Date]

[Payer Name]
[Payer Address — distribution requests department]

Re: Form W-4R for upcoming distribution
    Account holder: [Recipient Name]
    Account number: ****[last 4]
    Distribution date (expected): [MM/DD/YYYY]

Dear [Payer]:

Please find enclosed Form W-4R electing federal income tax withholding
of [X]% on the upcoming nonperiodic distribution from my account
referenced above. Please apply this rate to the distribution and
include the withholding on the Form 1099-R for tax year [YYYY].

If you have any questions, please contact me at [phone] or [email].

Thank you,

[Recipient signature]
[Recipient printed name]
[Date]
```

---

## Section 7 — PDF field-mapping cheat sheet

For agents using `pypdf` or `pdftk` to fill the IRS Form W-4R PDF programmatically. The 2026 fw4r.pdf has exactly six text fields (dumped with pypdf on 2026-10-06; mapped by position on page 1; the form has no payer lines):

- `topmostSubform[0].Page1[0].Line1a[0].f1_01[0]` — 1a first name and middle initial
- `topmostSubform[0].Page1[0].Line1a[0].f1_02[0]` — 1a last name
- `topmostSubform[0].Page1[0].f1_05[0]` — 1b social security number (max 11 characters)
- `topmostSubform[0].Page1[0].Line1a[0].f1_03[0]` — address
- `topmostSubform[0].Page1[0].Line1a[0].f1_04[0]` — city or town, state, and ZIP code
- `topmostSubform[0].Page1[0].f1_06[0]` — line 2 rate (max 3 characters, whole number)

Field names change with each revision. Re-dump the fields (`pypdf.PdfReader('fw4r.pdf').get_fields()` or `pdftk fw4r.pdf dump_data_fields`) whenever the form year changes. The signature is not a fillable field: the recipient signs and dates.

---

## Section 8 — Submission state machine

After delivery to the payer:

1. **Submitted** — recipient signed, payer received (portal, email, fax, mail)
2. **Acknowledged** — payer confirms receipt (some payers email a confirmation; others don't)
3. **Applied** — payer applies the rate to the distribution and processes payment
4. **Paid** — recipient receives the net amount; gross and withholding shown on remittance
5. **Reported** — payer issues Form 1099-R in January reporting the gross distribution and federal withholding to the IRS and the recipient

If between submission and payment the recipient wants to change the rate, the recipient must submit a new W-4R *before* the payer processes the distribution. Most payers lock the rate at the moment they initiate the distribution; changes after that point are not accepted (the recipient must wait for the next distribution).

---

## Section 9 — Security and consent rules for the agent

These are non-negotiable:

1. **Never deliver Form W-4R without explicit recipient consent** at the moment of submission. "I authorize you to deliver Form W-4R with rate <X>% to <payer> on my behalf right now" must be captured.
2. **Never store SSN or full account number** in agent logs, vector stores, or transcripts. Pull at delivery time, use, discard.
3. **Never modify the rate after the recipient signed.** If the rate needs to change, the recipient must sign a new W-4R.
4. **Always capture delivery confirmations** (portal confirmation number, email acknowledgment, USPS tracking) as records under the recipient's account, not the agent's.
5. **Never advise on the underlying decision** of whether to take the distribution. That's the recipient's choice (or their CPA's). The skill withholds-tax-correctly on a decision the recipient has already made.
6. **For ERDs, never agree to enter a rate below 20%.** The form doesn't allow it ("You can't choose withholding at a rate of less than 20% (including '-0-')"), and the payer must withhold 20% under §3405(c) regardless. If the recipient wants to avoid withholding on an ERD, the only path is a direct rollover — surface this option clearly.
