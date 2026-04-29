# Filing / Paying Form 1040-ES (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can submit an estimated tax payment after producing a complete Form 1040-ES plan from `SKILL.md`.

The agent must produce the full plan first, get explicit user consent for the specific dollar amount and quarter, then pick a channel from the decision tree below.

---

## Channel decision tree

```
User wants to pay now from a checking/savings account, no enrollment?
  → IRS Direct Pay
    Browser automation: feasible, deterministic.
    Use Section 1.

User wants recurring scheduled payments and is willing to enroll?
  → EFTPS
    Browser automation: requires enrollment lead time (5–7 business days for PIN).
    Use Section 2.

User wants to pay by debit/credit card?
  → Third-party processors (Pay1040, ACI Payments)
    Browser automation: possible but processors charge a fee (~$2.50 debit, ~1.85% credit).
    Use Section 3.

User wants to pay by check?
  → Mail Form 1040-ES voucher + check
    "Browser automation": prepare printable voucher PDF, address lookup.
    Use Section 4.

User uses IRS Online Account?
  → Pay through irs.gov/account (requires ID.me sign-in)
    Browser automation: ID.me identity proofing breaks deterministic flows.
    Skip — fall back to Direct Pay.
```

**Default channel**: IRS Direct Pay. No enrollment, no fee, ACH from any US checking/savings, deterministic flow.

---

## Section 1 — IRS Direct Pay

URL: https://www.irs.gov/payments/direct-pay

**Availability**: 24/7 except for routine maintenance windows (typically Sun overnight). Same-day payments accepted until 8 PM ET; later submissions post next business day.

**Account model**: no account required. Each payment is a discrete session; the user re-enters identity info each time.

### Pre-flight

Agent must have:

- The user's permission to submit a payment for a specific dollar amount and quarter
- Filer's full legal name, SSN, date of birth, mailing address (must match a recent return on file)
- A prior-year return on file (any year 2018 or later) — Direct Pay verifies identity by matching this
- Bank routing number and account number for the funding account
- Email address (Direct Pay sends a confirmation; user may want it)
- The completed plan from `SKILL.md` (specifically the per-voucher amount + quarter)

### Browser flow

The agent navigates and interacts deterministically. Field labels are stable but DOM IDs may change between sessions; treat label text as canonical.

1. **Navigate** to https://www.irs.gov/payments/direct-pay
2. **Click** "Make a Payment" → loads the 5-step Direct Pay wizard
3. **Step 1 — Reason for Payment**:
   - Reason: "Estimated Tax"
   - Apply Payment To: "1040ES (for 1040, 1040A, 1040EZ)"
   - Tax Period: select the tax year (e.g., "2026")
   - Click "Continue"
4. **Step 2 — Verify Identity**:
   - Tax Year for Verification: pick a prior tax year on file (most recent is best; e.g., "2024" for a return filed in 2025)
   - Filing Status (from that prior year): Single | MFJ | MFS | HOH | QW
   - First Name, Middle Initial, Last Name (must match prior return exactly)
   - SSN / ITIN
   - Date of Birth
   - Country of Residence: typically United States
   - Address line 1, City, State, ZIP (must match prior return)
   - Click "Continue"
   - **Failure mode**: if any field doesn't match the prior return, Direct Pay returns "We were unable to verify your identity" and the agent must stop and ask the user to confirm exact spelling/address from the prior return.
5. **Step 3 — Your Payment Information**:
   - Payment Amount: the dollar figure from the plan (e.g., $4,250.00)
   - Payment Date: today's date for immediate, or any date up to 365 days in the future for scheduling
   - Bank Routing Number: 9 digits
   - Bank Account Number: variable digits
   - Account Type: Checking | Savings
   - Click "Continue"
6. **Step 4 — Review & Sign**:
   - Verify every field against the plan and the user's banking info
   - Read the disclosure (electronic-signature consent + ACH authorization)
   - Check "I agree to the Terms"
   - Click "Submit"
7. **Step 5 — Confirmation**:
   - Direct Pay displays a **Confirmation Number** (format: XXXXX-XXXXX-XXXXX-XXXXX)
   - **Capture this number** — required for any future inquiry, cancellation, or proof of payment
   - Optional: enter email to receive a confirmation copy
   - Print or screenshot the confirmation page
8. **Post-submission**: payment posts to IRS within 1–2 business days; user can verify via [IRS Online Account](https://www.irs.gov/payments/online-account) or their bank statement.

### Cancellation / modification

A scheduled (future-dated) Direct Pay payment can be canceled or modified up to 11:59 PM ET two business days before the scheduled date. Use the "Look Up a Payment" link with the confirmation number + SSN.

A payment that has already processed cannot be canceled through Direct Pay; the user would have to contact the IRS at 1-800-829-1040 to dispute.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at Step 6
- Do not retry a failed identity verification more than twice — Direct Pay locks the SSN for 24 hours after 3 failed attempts
- Do not store the user's bank routing/account numbers in any log or transcript
- Do not store the SSN, DOB, or confirmation number beyond the session
- Do not assume "Estimated Tax" applies — confirm with the user it's not a balance-due payment from a prior year (different "Reason for Payment")

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "We were unable to verify your identity" | Address/name mismatch with prior return | Ask user for exact prior-return values |
| "Bank routing number is invalid" | Typo or wrong format | Re-confirm 9-digit ABA number |
| "Payment date must be a business day" | Selected weekend/holiday | Pick next business day |
| "You have exceeded the limit" | More than 2 same-day same-tax-period payments attempted | Wait 24 hours or use EFTPS |
| Session timeout | Idle > 15 min | Restart wizard from Step 1 |

---

## Section 2 — EFTPS (Electronic Federal Tax Payment System)

URL: https://www.eftps.gov

**Enrollment lag**: 5–7 business days from enrollment to receipt of PIN by mail. Plan ahead — EFTPS can NOT be used same-day for a first-time enrollee.

### Pre-flight

- Filer's enrollment status: enrolled with PIN, or needs to enroll
- EIN or SSN, depending on enrollment type (individuals enroll with SSN)
- Internet Password (separate from PIN; user sets at first login)
- Bank routing + account numbers (set during enrollment, can be changed in profile)

### Browser flow (already-enrolled user)

1. Navigate to https://www.eftps.gov
2. Click "Make a Payment"
3. Sign in with: SSN/EIN + PIN + Internet Password
4. Select "1040ES" as the tax form
5. Select tax period (year): e.g., 2026
6. Enter payment amount and effective date (1 to 365 days future-dated)
7. Confirm bank info
8. Submit → confirmation number issued (format: EFT XX XXX XXX XX XX)
9. Capture confirmation number

EFTPS allows scheduling **all four 1040-ES installments at once**, up to 365 days in advance — useful for the predictable plan output of this skill.

### Failure modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "PIN is locked" | 3 wrong PIN attempts | Call EFTPS Customer Service: 1-800-555-4477 |
| "Tax form not allowed" | Wrong form code | Use "1040ES", not "1040" |
| Future date > 365 days | Out of range | Reschedule within window |

---

## Section 3 — Pay by Card (third-party processors)

The IRS authorizes three payment processors. The agent picks one based on the user's preference for fee structure:

| Processor | Debit fee | Credit fee | URL |
|-----------|-----------|------------|-----|
| Pay1040 | $2.50 flat | 1.75% | https://www.pay1040.com |
| ACI Payments | $2.20 flat | 1.85% | https://www.acipayonline.com |
| (Verify the current authorized list at https://www.irs.gov/payments/pay-your-taxes-by-debit-or-credit-card before automating — list and fees change.) |

**Pre-flight**: card number, CVV, billing address, exact expiration. The agent should confirm the user understands the fee is non-refundable even if the IRS later refunds.

**Generic flow**:
1. Navigate to processor URL
2. Pick "Personal" → "1040 Estimated Taxes (1040ES)"
3. Pick tax year
4. Enter SSN + verification info (typically name + ZIP)
5. Enter amount + card details
6. Submit → confirmation

The processor returns a confirmation number; the IRS posts the payment within 1–2 business days. Card processors do **not** allow cancellation — the user would have to dispute with the card issuer.

---

## Section 4 — Paper voucher + check

When electronic isn't available (or the user prefers paper):

### Assemble the payment

1. Print the appropriate voucher (1, 2, 3, or 4) from page 9–12 of the latest f1040es.pdf
2. Fill in: filer name, SSN, spouse name + SSN if MFJ, address, payment amount
3. Write a check payable to "United States Treasury"
4. On the check memo line: "2026 Form 1040-ES" + filer's SSN
5. Do not staple, paperclip, or fold the voucher. Mail flat.

### Mailing addresses (verify each year)

The IRS publishes 1040-ES mailing addresses on the voucher's accompanying instruction page (varies by state). The agent must look up the current address from the most recent f1040es.pdf each tax year — addresses shift between years.

Example structure (always re-verify):

```
If you live in: AL, FL, GA, LA, MS, NC, SC, TN, TX
Mail to:        Internal Revenue Service
                P.O. Box 1300
                Charlotte, NC 28201-1300
```

(This example is illustrative; the agent must pull the current mapping from the official PDF.)

### Mailing best practices

- USPS Certified Mail with Return Receipt for proof of timely filing (IRC §7502 timely-mailing-as-timely-filing rule)
- Postmark **on or before** the installment due date
- Keep a photocopy of the voucher and check before mailing
- Track via USPS tracking number; expect 4–6 weeks for IRS to credit the payment in the user's account

---

## Section 5 — Submission state machine

After payment (any channel), the user's installment moves through:

1. **Submitted** — sent to IRS / processor
2. **Pending** — being processed; bank ACH not yet drawn
3. **Posted** — IRS account credited; visible on IRS Online Account
4. **Reflected on Form 1040** — at year-end filing, total estimated payments appear on Form 1040 Line 26

Status checks:

- Direct Pay: "Look Up a Payment" with confirmation number + SSN
- EFTPS: payment history visible after sign-in
- Card: processor's confirmation page + IRS Online Account 1–2 days later
- Paper: 4–6 weeks for IRS to acknowledge; verify via IRS Online Account or account transcript

The agent should set a follow-up reminder 7 days post-submission to verify the payment posted.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never submit a payment without explicit user consent at the moment of submission.** "I authorize you to submit $X via Direct Pay for Q[N] of [year] right now" must be captured.
2. **Never store SSN, DOB, bank routing/account numbers, card numbers, CVV, or PINs** in agent logs, vector stores, or transcripts. Pull at submission time, use, discard.
3. **Never bypass identity verification.** If Direct Pay or EFTPS rejects identity, pause and let the user provide accurate values. Do not retry by guessing variations.
4. **Always capture confirmation numbers** as the user's record, stored under the user's account, not the agent's.
5. **If the channel returns an error or unexpected screen**, stop and surface the issue. Do not retry blindly — repeated failed attempts can trigger anti-fraud lockouts on the user's SSN.
6. **Verify the dollar amount and tax period one last time** before clicking Submit. A misrouted payment (wrong tax year, wrong "Reason") is a multi-week recovery process with the IRS.
