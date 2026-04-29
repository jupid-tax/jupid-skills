# Delivering Form W-4R to the Payor

How an agent equipped with web-portal, email, fax, or mail tooling can take a completed Form W-4R draft and deliver it to the payor (IRA custodian, 401(k) plan administrator, employer paying severance, etc.). This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then collect the recipient's ink signature (or e-signature if the payor accepts), then execute the delivery channel.

**Form W-4R is NOT filed with the IRS.** It is delivered to the payor. The payor retains the form and applies the elected rate to the distribution.

---

## Channel decision tree

The right delivery channel depends entirely on the payor. Most major US payors accept multiple channels; check the payor's website or call their participant-services line to confirm.

```
Is the payor a major brokerage (Fidelity, Schwab, Vanguard, E*TRADE,
Merrill Lynch, etc.) with a participant web portal?
  → Section 1 — Web portal upload (preferred)

Is the payor a 401(k) recordkeeper (Empower, Voya, Principal, Alight,
Fidelity NetBenefits, Schwab Workplace, etc.)?
  → Section 1 — Web portal upload, OR Section 2 — Distribution-request
    intake form (sometimes W-4R is embedded in the distribution form)

Is the payor an employer paying severance (in-house payroll department)?
  → Section 3 — Submit to HR / payroll, typically via email or in person

Is the payor a small custodian / TPA without a portal?
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

1. **Log in** to the payor's participant portal
2. **Navigate** to the distribution / withdrawal request page (varies by payor):
   - Fidelity: "Move money" → "Withdraw money" → IRA / 401(k) selection
   - Schwab: "Service" → "Account distributions" → "Take an IRA distribution"
   - Vanguard: "Transact" → "Withdraw / sell" → "Distribute from an IRA"
   - Empower / employer 401(k) plans: "Distributions" or "Withdrawals" tab
3. **Select the source account** and distribution type:
   - Lump sum (typically nonperiodic — W-4R)
   - Substantially equal periodic payments (W-4P, not W-4R)
   - RMD (W-4R, default 10%)
   - Hardship withdrawal (W-4R, default 10%)
4. **Enter the withholding rate** when prompted. The portal usually presents:
   - Default rate (10% for nonperiodic, 20% for ERD) pre-checked
   - "Use a different rate" option that opens a percentage input
5. **Confirm the rate matches the W-4R draft**
6. **Sign electronically** if the portal supports e-signature (most do — typically a typed name + acknowledgment checkbox + MFA code)
7. **Capture confirmation**: confirmation number, screenshot, downloadable PDF receipt
8. **Verify the distribution amount and net (after-withholding) amount** displayed before final submission

### Payor-specific notes

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

- Distribution-request packet PDF from the payor (downloaded from portal or requested by phone)
- Completed W-4R draft from `SKILL.md`
- All ancillary information (direct deposit routing/account, beneficiary info if needed)

### Flow

1. **Open the packet** in a fillable-PDF tool
2. **Fill Page 1** with recipient info matching payor records exactly
3. **Fill Page 2** with the distribution amount and type
4. **Fill the W-4R section** (Page 3 typically) with the rate from the draft. Verify the rate is in the allowed range:
   - ERD: ≥ 20%
   - Other nonperiodic: 0–100
5. **Fill state-tax section** (Page 4) if applicable; if not handled by this skill, leave for the recipient or coordinate with a state-tax skill
6. **Fill payment method** (Page 5): direct deposit (provide routing + account) or check (confirm mailing address)
7. **Spousal consent** (if applicable): for ERISA plans where the participant is married, a qualified joint and survivor annuity (QJSA) or qualified preretirement survivor annuity (QPSA) waiver may require notarized spousal consent — the agent does not handle notarization; this becomes a manual step
8. **Recipient signs** Page 7 in ink (or e-signs if the payor accepts e-signatures)
9. **Submit via the channel listed on the packet**:
   - Upload to portal
   - Email to a specific address (typically distributions@ or service@ at the payor)
   - Fax to a participant-services fax line
   - Mail to a specific PO box

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form returned for missing field" | Incomplete intake form | Re-complete and resubmit |
| "Spousal consent required" | ERISA plan, married participant, no spousal waiver | Obtain notarized spousal consent and resubmit |
| "Rate below mandatory minimum" | ERD with rate < 20% | Correct to ≥ 20% and resubmit |
| "Account information mismatch" | Name / address / SSN doesn't match payor records | Update records with payor first, then resubmit |

---

## Section 3 — Severance from employer (HR / payroll)

When the payor is the recipient's employer paying lump-sum severance, the W-4R goes to HR or payroll, not to a third-party recordkeeper.

### Pre-flight

- Severance agreement copy (confirm the payment is lump-sum nonperiodic, not periodic salary continuation)
- HR / payroll contact (name, email, mailing address)
- Completed W-4R draft

### Flow

1. **Confirm severance is nonperiodic**. If it's salary continuation (paid biweekly or monthly for a defined period), it's periodic — use W-4P or, in some cases, regular W-4 wage withholding (employer's call). Lump-sum severance paid in one or two installments is typically nonperiodic — W-4R applies.
2. **Email or hand-deliver** the signed W-4R to HR / payroll. Most employers accept email PDF; some require a wet signature on hard copy.
3. **Confirm receipt** with HR.
4. **Verify on the severance payment** (or the pay stub) that the elected withholding rate was applied. If the employer's payroll system applies regular wage withholding instead of W-4R nonperiodic, escalate to HR — this is a setup error.

### Special case: severance treated as wages

Some employers and severance agreements treat severance as wages (subject to W-2 withholding under regular W-4 rules) rather than as a nonperiodic distribution under W-4R. Whether severance is wages or nonperiodic depends on the substance of the payment:

- **Wages**: tied to services rendered; subject to FICA / FUTA in addition to income tax
- **Nonperiodic distribution**: typically severance under a separation agreement that doesn't reflect ongoing services

Most severance is treated as wages by the employer — in which case W-4R doesn't apply and the recipient updates their regular W-4. If the recipient is uncertain, ask HR which form applies for *this specific payment*.

---

## Section 4 — Email or fax (smaller custodians, TPAs)

Some smaller IRA custodians and third-party administrators (TPAs) accept the form via email or fax.

### Pre-flight

- Payor's accepted channel (email address or fax number) — check the payor's website or call
- Completed and signed W-4R PDF
- Cover-letter template (Section 7 below)

### Flow

1. **Print the completed W-4R PDF**
2. **Sign in ink**
3. **Scan the signed form**
4. **Compose** an email (or prepare a fax cover sheet) to the payor with:
   - Subject: "W-4R for [Account Holder Name] — Account [last 4 digits]"
   - Body: brief reference to the upcoming distribution and the elected rate
   - Attachment: signed W-4R PDF
5. **Send** and **save the sent email** as proof of delivery
6. **Follow up** if no acknowledgment within 5 business days

### Email security considerations

W-4R contains an SSN. Do not send unencrypted email if the recipient or payor has any concern about email security:

- Use the payor's secure-message portal if available (most major payors have one)
- Use encrypted email (S/MIME, PGP) if both sides support it
- If neither, use fax or mail

---

## Section 5 — USPS or private delivery (paper mail)

The most secure but slowest option.

### Pre-flight

- Payor's mailing address for distribution requests (often a specific PO box, different from the general corporate address)
- Completed and signed W-4R
- Cover letter
- Tracking method (USPS Certified Mail or private delivery)

### Flow

1. **Print** the signed W-4R
2. **Print** the cover letter (Section 7 template)
3. **Assemble** in an envelope with the payor's mailing address
4. **Mail via USPS Certified Mail with Return Receipt** (recommended) or private delivery service with tracking
5. **Retain** the postmark receipt and tracking record
6. **Track delivery** until confirmed

### Mailing addresses

Pull from the payor's website, account statement, or a direct call. Do not hardcode addresses — they change.

---

## Section 6 — Cover-letter template

```
[Recipient Name]
[Recipient Address]

[Date]

[Payor Name]
[Payor Address — distribution requests department]

Re: Form W-4R for upcoming distribution
    Account holder: [Recipient Name]
    Account number: ****[last 4]
    Distribution date (expected): [MM/DD/YYYY]

Dear [Payor]:

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

For agents using `pypdf` or `pdftk` to fill the IRS Form W-4R PDF programmatically. Run `pdftk fw4r.pdf dump_data_fields` once to capture the current field list. Typical field names (verify against current revision):

- `topmostSubform[0].Page1[0].f1_1[0]` — first name and middle initial
- `topmostSubform[0].Page1[0].f1_2[0]` — last name
- `topmostSubform[0].Page1[0].f1_3[0]` — SSN
- `topmostSubform[0].Page1[0].f1_4[0]` — address
- `topmostSubform[0].Page1[0].f1_5[0]` — city, state, ZIP
- `topmostSubform[0].Page1[0].f1_6[0]` — payor name (Line 1a)
- `topmostSubform[0].Page1[0].f1_7[0]` — payor address (Line 1b)
- `topmostSubform[0].Page1[0].f1_8[0]` — withholding rate (Line 2)

Field names change with each revision. Re-run `dump_data_fields` whenever the form revision date changes.

---

## Section 8 — Submission state machine

After delivery to the payor:

1. **Submitted** — recipient signed, payor received (portal, email, fax, mail)
2. **Acknowledged** — payor confirms receipt (some payors email a confirmation; others don't)
3. **Applied** — payor applies the rate to the distribution and processes payment
4. **Paid** — recipient receives the net amount; gross and withholding shown on remittance
5. **Reported** — payor issues Form 1099-R in January reporting the gross distribution and federal withholding to the IRS and the recipient

If between submission and payment the recipient wants to change the rate, the recipient must submit a new W-4R *before* the payor processes the distribution. Most payors lock the rate at the moment they initiate the distribution; changes after that point are not accepted (the recipient must wait for the next distribution).

---

## Section 9 — Security and consent rules for the agent

These are non-negotiable:

1. **Never deliver Form W-4R without explicit recipient consent** at the moment of submission. "I authorize you to deliver Form W-4R with rate <X>% to <payor> on my behalf right now" must be captured.
2. **Never store SSN or full account number** in agent logs, vector stores, or transcripts. Pull at delivery time, use, discard.
3. **Never modify the rate after the recipient signed.** If the rate needs to change, the recipient must sign a new W-4R.
4. **Always capture delivery confirmations** (portal confirmation number, email acknowledgment, USPS tracking) as records under the recipient's account, not the agent's.
5. **Never advise on the underlying decision** of whether to take the distribution. That's the recipient's choice (or their CPA's). The skill withholds-tax-correctly on a decision the recipient has already made.
6. **For ERDs, never agree to enter a rate below 20%.** The payor will reject; even if accepted, the IRS will impose the 20% withholding under §3405(c) regardless. If the recipient wants to avoid withholding on an ERD, the only path is direct trustee-to-trustee rollover — surface this option clearly.
