# Submitting Form 4506-T (or skipping it via Get Transcript)

How an agent equipped with browser tooling can take a user's transcript request from "I need my tax transcript" to a delivered transcript. There are three submission channels:

1. **Get Transcript Online** (no Form 4506-T needed; instant; user authenticates)
2. **Get Transcript by Mail** (no Form 4506-T needed; uses the IRS web tool that mails to the address on file; 5-10 business days)
3. **Form 4506-T** (paper form, mailed or faxed; required when channels 1-2 don't work or third-party delivery is needed)

The agent's first job is **routing**: pick the right channel and execute it. Form 4506-T is the fallback, not the default.

---

## Channel decision tree

```
User wants a transcript? Why?

  → They themselves need to view it (any reason)
    → Try Get Transcript Online (Channel 1) first
      Identity verification via ID.me
      Available 24/7, instant download

  → They need IRS to mail to their home address (no online auth needed)
    → Use Get Transcript by Mail (Channel 2)
      No Form 4506-T needed
      Uses prior-year filing data for identity check (less stringent than ID.me)
      5-10 business days to receive

  → They need IRS to mail directly to a third party (lender, school)
    → Form 4506-T Line 5 (Channel 3, mail or fax)
      Get Transcript portals don't support third-party mailing

  → They can't authenticate online (no smartphone, identity theft history, etc.)
    → Form 4506-T (Channel 3)

  → They need a transcript type Get Transcript doesn't support
    → Form 4506-T (rare; Get Transcript supports all five types as of 2024+)

  → A lender provided their own pre-filled Form 4506-C (IVES)
    → User signs that — do not duplicate with 4506-T
```

---

## Channel 1 — Get Transcript Online

URL: https://www.irs.gov/individuals/get-transcript

### Pre-flight

User needs:
- Government-issued photo ID (driver's license, passport, state ID)
- Smartphone with camera (for ID.me selfie verification) OR access to a live video session
- Email address and phone number registered to the user
- Social Security number
- Their own home address (to verify against IRS records)

### Browser flow

1. **Navigate** to https://www.irs.gov/individuals/get-transcript
2. **Click** "Get Transcript Online"
3. **Sign in or create ID.me account**:
   - First time: email + password + identity verification (selfie + ID upload OR live video session with ID.me agent)
   - Returning: email + password + MFA
4. **Select transcript type**: Return Transcript, Account Transcript, Record of Account, Wage and Income, or Verification of Non-filing
5. **Select tax year**: pick a year from the dropdown. Available years differ by transcript type:
   - Return Transcript: current year + 3 prior
   - Account Transcript: many years back (10+ for some)
   - Record of Account: current year + 3 prior
   - Wage and Income: last 10 years
   - Verification of Non-filing: any year
6. **Download PDF**: the transcript appears as a PDF for instant download
7. **Save** the PDF locally and (if requested) forward to lender / school

### What the agent should NOT do

- Do not attempt to bypass ID.me identity verification
- Do not store the user's ID.me credentials or selfie in agent logs
- Do not request transcripts for someone other than the user themselves (illegal — IRC §6103 confidentiality)

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| ID.me verification fails | Photo ID rejected, face match failure, address mismatch | Use live video verification path on ID.me, OR fall back to Get Transcript by Mail / Form 4506-T |
| "We can't process your transcript request right now" | Recent return not yet processed | Wait 2-3 weeks after e-file acceptance, 6-8 weeks after paper |
| Wrong year shows | User picked wrong year from dropdown | Re-select |
| ID.me times out | Session expired | Restart, expect to re-verify |

---

## Channel 2 — Get Transcript by Mail

URL: https://www.irs.gov/individuals/get-transcript

### Pre-flight

User needs:
- SSN
- Date of birth
- Mailing address as it appears on the most recent tax return filed
- (No ID.me required — uses simpler authentication)

The IRS will mail the transcript to the address on file. If the user has moved since the last return, they must first update their address with the IRS (Form 8822) before this channel works.

### Browser flow

1. **Navigate** to https://www.irs.gov/individuals/get-transcript
2. **Click** "Get Transcript by Mail"
3. **Enter** SSN, DOB, address from most recent return
4. **Select** transcript type and year
5. **Submit** — confirmation page shows transcript will be mailed to the address on file
6. **Wait** 5-10 business days

### Limitations

- Cannot direct to a third-party address (transcript only goes to address on file)
- Only Tax Return Transcript and Tax Account Transcript are supported via this channel (not Record of Account, Wage and Income, or Verification of Non-filing — those require Channel 1 or Channel 3)
- Address must match prior-year filing exactly

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Address doesn't match" | User moved, didn't update IRS address | File Form 8822 to update, wait 4-6 weeks, retry. Or use Channel 1 / Channel 3. |
| "We can't verify your identity" | DOB or SSN mismatch | Confirm DOB matches IRS records. If doesn't, use Channel 3. |

---

## Channel 3 — Form 4506-T (mail or fax)

When Channels 1-2 don't work, or when third-party mailing is needed.

### Pre-flight

Agent needs:
- A complete `SKILL.md`-format draft Form 4506-T
- The user's wet signature (paper) or e-signature acceptable to IRS
- Routing address or fax number for the user's state (looked up from the form's instruction page or current IRS chart)
- A submission method (USPS / Fax / Certified mail)

### Routing

The IRS routes Form 4506-T submissions based on the **requester's state of residence** as listed in Line 3 (current address). The form's instruction page has a state-by-state chart. As of recent revisions:

- **Mail**: one of three IRS RAIVS offices — Kansas City MO, Ogden UT, or Austin TX
- **Fax**: state-specific fax number provided in the same chart

The agent must consult the **current revision's** instruction page for routing, since addresses and fax numbers are subject to change. Use the routing chart from page 2 of the actual Form 4506-T downloaded fresh from https://www.irs.gov/pub/irs-pdf/f4506t.pdf.

### Browser flow (if filling and submitting via fax)

This is feasible if the agent has access to a fax service and the user's signed PDF.

1. **Generate the filled PDF** from the SKILL.md draft (using a PDF tool that supports IRS fillable PDFs)
2. **Have the user sign** in wet ink (print, sign, scan) OR via an IRS-acceptable e-signature
3. **Look up** the fax number for the user's state from the form's instruction chart
4. **Send via fax service** (efax, HelloFax, etc.) — capture the confirmation
5. **Wait** 5-10 business days

### Browser flow (if mailing)

1. **Generate the filled PDF** from the SKILL.md draft
2. **Have the user sign** in wet ink (print, sign)
3. **Look up** the mailing address for the user's state
4. **Mail** via USPS — Certified Mail with Return Receipt recommended for proof
5. **Wait** 10-14 days (plus mail transit time)

### Tracking

There is no online tracking for Form 4506-T submissions. The user just waits. If after the expected window no transcript arrives:
- Call IRS at 1-800-908-9946 (transcript hotline) or 1-800-829-1040 (general)
- Check Get Transcript Online to see if the request is queued
- Re-submit if necessary (signature must be < 120 days old at IRS receipt)

### What the agent should NOT do

- Do not submit Form 4506-T without the user's wet signature (or accepted e-signature)
- Do not store the user's signed PDF in agent logs after fax/mail confirmation
- Do not submit a Form 4506-T for a year where the IRS hasn't processed the return yet (it will be returned)
- Do not check more than one transcript type per Form 4506-T (will be rejected)

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Form returned: "Multiple transcript types selected" | More than one box checked on Lines 6-8 | Submit separate forms |
| Form returned: "Signature too old" | Signature dated > 120 days before IRS receipt | Re-sign with current date |
| Form returned: "Address mismatch" | Line 4 doesn't match prior-year filing address | Update Line 4 with the actual prior address |
| Form returned: "Joint return missing spouse signature" | Only one spouse signed | Both spouses must sign |
| No response after 14 days | Lost in mail, IRS backlog | Call 1-800-908-9946; resubmit if needed |
| Wrong transcript received | User checked wrong box | Submit a new request for correct type |

---

## Channel 4 — IVES via Form 4506-C (lender-driven)

If the user is interacting with a high-volume lender (Quicken / Rocket, Wells Fargo, Chase mortgage, SoFi, etc.), the lender may use the **Income Verification Express Service (IVES)**, which uses **Form 4506-C** instead of 4506-T.

The lender provides a pre-filled Form 4506-C; the user signs and returns to the lender; the lender submits to the IRS via the IVES electronic system. Turnaround is typically 1-2 business days.

If the user has Form 4506-C from the lender:
- Direct the user to sign that
- Do not duplicate with Form 4506-T (which goes through the slower RAIVS channel)
- The lender pays IRS the IVES fee ($2 per transcript currently); the user pays nothing

If the user is unsure whether they need 4506-T or 4506-C, ask the lender. The lender's loan officer can tell them.

---

## Submission state machine

After submission (any channel):

1. **Submitted** → request sent to IRS
2. **Queued** → IRS RAIVS office receives (no notification to user typically)
3. **Processed** → transcript generated
4. **Mailed / Delivered** → transcript sent to address on form

Status checks:
- **Channel 1 (Online)**: instant — no waiting
- **Channel 2 (Mail)**: ~5-10 business days
- **Channel 3 (4506-T fax)**: ~5-10 business days
- **Channel 3 (4506-T mail)**: ~10-14 days + mail transit
- **Channel 4 (IVES 4506-C)**: ~1-2 business days

If past expected window with no result:
- Call IRS transcript hotline: 1-800-908-9946
- Have SSN, DOB, current address, prior-year AGI ready

---

## Security and consent rules

These are non-negotiable:

1. **Never request a transcript** for someone other than the user themselves (or with documented authorization via Form 2848 / Form 8821).
2. **Never store** SSN, DOB, ID.me credentials, signed PDFs, or transcript content in agent logs after submission. Process at submission time, then discard.
3. **Verify Line 5 third-party address carefully** — wrong address sends sensitive tax data to a stranger.
4. **Confirm the user's wet signature** before mailing/faxing. Do not generate a faux signature.
5. **Refuse** to submit a Form 4506-T with multiple transcript types checked (will be rejected).
6. **If anything looks wrong** (rejection notice, wrong transcript, missing year), surface and let the user respond — don't retry blindly.

---

## Sources

- IRS Form 4506-T (current revision): https://www.irs.gov/pub/irs-pdf/f4506t.pdf
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Get Transcript: https://www.irs.gov/individuals/get-transcript
- Form 4506: https://www.irs.gov/forms-pubs/about-form-4506
- Form 4506-C (IVES): https://www.irs.gov/forms-pubs/about-form-4506-c
- IRC §6103 — confidentiality of tax returns and disclosure rules
- IRS RAIVS (Return and Income Verification Services) — the back office that processes 4506-T paper/fax requests
- IVES (Income Verification Express Service) — IRS electronic service for high-volume lender requests
