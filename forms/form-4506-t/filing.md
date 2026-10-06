# Submitting Form 4506-T (or skipping it via Get Transcript)

How an agent equipped with browser tooling can take a user's transcript request from "I need my tax transcript" to a delivered transcript. There are three submission channels:

1. **Individual Online Account** (no Form 4506-T needed; immediate once the user verifies with ID.me)
2. **Get Transcript by Mail or 800-908-9946** (no Form 4506-T needed; return or account transcript mailed to the address on file in 5-10 calendar days)
3. **Form 4506-T** (paper form, mailed or faxed; required when channels 1-2 don't cover the need)

No channel mails a transcript to a lender, school, or other third party; since July 2019 the IRS mails transcripts only to the taxpayer's address of record. Lenders that need transcripts directly use IVES (Form 4506-C, Channel 4).

The agent's first job is **routing**: pick the right channel and execute it. Form 4506-T is the fallback, not the default.

---

## Channel decision tree

```
User wants a transcript? Why?

  → They themselves need to view it (any reason)
    → Try the Individual Online Account (Channel 1) first
      Identity verification via ID.me
      All five transcript types

  → They need a return or account transcript mailed to them (no online verification)
    → Get Transcript by Mail or 800-908-9946 (Channel 2)
      No Form 4506-T needed
      Needs the mailing address from the latest return
      5-10 calendar days to receive at the address on file

  → They need a third party (lender) to receive it directly
    → Not available on Form 4506-T. User forwards the transcript,
      or the lender uses IVES (Channel 4)

  → They can't verify online AND need record of account, wage and income,
    or verification of non-filing; or years outside the online windows;
    or a fiscal-year or business transcript
    → Form 4506-T (Channel 3)

  → A lender provided their own pre-filled Form 4506-C (IVES)
    → User signs that — do not duplicate with 4506-T
```

---

## Channel 1 — Individual Online Account

URL: https://www.irs.gov/individuals/get-transcript (links to the online account sign-in)

### Pre-flight

User needs (irs.gov "Creating an account for IRS.gov"):
- SSN or ITIN
- Valid government-issued photo ID (driver's license, state ID, passport, or passport card)
- Smartphone or computer with webcam for the ID.me selfie, OR an ID.me video chat agent session
- Email address and phone number the user controls

### Browser flow

1. **Navigate** to https://www.irs.gov/individuals/get-transcript
2. **Click** the sign-in link for the online account
3. **Sign in or create ID.me account**:
   - First time: email + password + identity verification (selfie + ID upload OR live video session with ID.me agent)
   - Returning: email + password + MFA
4. **Select transcript type**: Return Transcript, Account Transcript, Record of Account, Wage and Income, or Verification of Non-filing
5. **Select tax year**: pick a year from the dropdown. Available years differ by transcript type (irs.gov transcript types page):
   - Return Transcript: current year + 3 prior
   - Account Transcript: current year + 9 prior
   - Record of Account: current year + 3 prior
   - Wage and Income: current year + 9 prior (about 85 documents max online)
   - Verification of Non-filing: current year after June 15; prior 3 years anytime
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
| "We can't process your transcript request right now" | Recent return not yet processed | Use the timing table at https://www.irs.gov/individuals/transcript-availability (2-3 weeks after e-file, 6-8 weeks after paper, for refund or no-balance returns) |
| Wrong year shows | User picked wrong year from dropdown | Re-select |
| ID.me times out | Session expired | Restart, expect to re-verify |

---

## Channel 2 — Get Transcript by Mail

URL: https://www.irs.gov/individuals/get-transcript

### Pre-flight

User needs:
- The identifying information the tool asks for, including the mailing address from the latest return
- (No ID.me required)

The IRS will mail the transcript to the address on file in 5-10 calendar days. The same service is available by phone at 800-908-9946. If the user has moved since the last return, they must first update their address with the IRS (Form 8822) before this channel works.

### Browser flow

1. **Navigate** to https://www.irs.gov/individuals/get-transcript
2. **Click** "Get Transcript by Mail"
3. **Enter** SSN, DOB, address from most recent return
4. **Select** transcript type and year
5. **Submit** — confirmation page shows transcript will be mailed to the address on file
6. **Wait** 5-10 calendar days

### Limitations

- Cannot direct to a third-party address (transcript only goes to address on file)
- Only Tax Return Transcript and Tax Account Transcript are supported via this channel (not Record of Account, Wage and Income, or Verification of Non-filing — those require Channel 1 or Channel 3)
- Account transcripts by mail cover the current and three prior tax years

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Address doesn't match" | User moved, didn't update IRS address | File Form 8822 to update, retry after the IRS processes it. Or use Channel 1. |
| "We can't verify your identity" | Identifying data doesn't match IRS records | Confirm the data against the latest return. If it still fails, use Channel 3. |

---

## Channel 3 — Form 4506-T (mail or fax)

When Channels 1-2 don't cover the need.

### Pre-flight

Agent needs:
- A complete `SKILL.md`-format draft Form 4506-T
- The user's signature (the form is printed, signed, and mailed or faxed), with the authority box checked
- The correct chart and state (below)
- A submission method (mail or fax)
- Confirmation that the IRS has the user's current address (else Form 8822 first — transcripts go to the address of record)

### Routing (Form 4506-T, Rev. April 2025, page 2)

Mail or fax to the office for the state the user lived in, or the state the business was in, **when that return was filed**. If more than one transcript is requested and the chart shows two different addresses, use the address based on the most recent return. Re-check these charts on the current revision before use.

**Chart for individual transcripts (Form 1040 series, Form W-2, and Form 1099)**

| If the individual return was filed while living in | Mail or fax to |
|---|---|
| Alabama, Arizona, Arkansas, Florida, Georgia, Louisiana, Mississippi, New Mexico, North Carolina, Oklahoma, South Carolina, Tennessee, Texas, a foreign country, American Samoa, Puerto Rico, Guam, the Commonwealth of the Northern Mariana Islands, the U.S. Virgin Islands, or an A.P.O. or F.P.O. address | Internal Revenue Service, RAIVS Team, Stop 6716 AUSC, Austin, TX 73301 — fax 855-587-9604 |
| Connecticut, Delaware, District of Columbia, Illinois, Indiana, Iowa, Kentucky, Maine, Maryland, Massachusetts, Minnesota, Missouri, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Virginia, West Virginia, Wisconsin | Internal Revenue Service, RAIVS Team, Stop 6705 S-2, Kansas City, MO 64999 — fax 855-821-0094 |
| Alaska, California, Colorado, Hawaii, Idaho, Kansas, Michigan, Montana, Nebraska, Nevada, North Dakota, Ohio, Oregon, South Dakota, Utah, Washington, Wyoming | Internal Revenue Service, RAIVS Team, P.O. Box 9941, Mail Stop 6734, Ogden, UT 84409 — fax 855-298-1145 |

**Chart for all other transcripts**

| If you lived in or your business was in | Mail or fax to |
|---|---|
| Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, Wyoming, a foreign country, American Samoa, Puerto Rico, Guam, the Commonwealth of the Northern Mariana Islands, the U.S. Virgin Islands, or an A.P.O. or F.P.O. address | Internal Revenue Service, RAIVS Team, P.O. Box 9941, Mail Stop 6734, Ogden, UT 84409 — fax 855-298-1145 |
| Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin | Internal Revenue Service, RAIVS Team, Stop 6705 S-2, Kansas City, MO 64999 — fax 855-821-0094 |

### Browser flow (if filling and submitting via fax)

This is feasible if the agent has access to a fax service and the user's signed PDF.

1. **Generate the filled PDF** from the SKILL.md draft (using a PDF tool that supports IRS fillable PDFs)
2. **Have the user check the authority box, sign, and date** (print, sign, scan)
3. **Look up** the fax number in the correct chart above
4. **Send via fax service** (efax, HelloFax, etc.) — capture the confirmation
5. **Wait** — most requests are processed within 10 business days (form), then the transcript is mailed to the address of record

### Browser flow (if mailing)

1. **Generate the filled PDF** from the SKILL.md draft
2. **Have the user check the authority box, sign, and date** (print, sign)
3. **Look up** the mailing address in the correct chart above
4. **Mail** via USPS — Certified Mail with Return Receipt recommended for proof
5. **Wait** — most requests are processed within 10 business days after receipt, plus mail time both ways

### Tracking

There is no online tracking for Form 4506-T submissions. The user just waits. If after the expected window no transcript arrives:
- Call IRS at 800-908-9946 (transcript line printed on the form) or 800-829-1040 (general individual line)
- Re-submit if necessary (the IRS must receive the form within 120 days of the signature date)

### What the agent should NOT do

- Do not submit Form 4506-T without the user's own signature and the authority box checked
- Do not store the user's signed PDF in agent logs after fax/mail confirmation
- Do not submit a Form 4506-T for a year where the IRS hasn't processed the return yet
- Do not check more than one transcript type per Form 4506-T (one form number per request; keep one type per form)

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Form returned unprocessed | Authority box in the signature area unchecked | Check the box, re-sign, resubmit |
| Form rejected: signature too old | IRS received it more than 120 days after the signature date | Re-sign with current date |
| Form rejected: incomplete or illegible | A required line blank, or signed before all lines were completed | Complete every applicable line, then sign |
| Transcript went to an old address | IRS address of record not updated | File Form 8822, then request again |
| No response after about 3 weeks | Lost in mail, IRS backlog | Call 800-908-9946; resubmit if needed |
| Wrong transcript received | User checked wrong box | Submit a new request for correct type |

---

## Channel 4 — IVES via Form 4506-C (lender-driven)

If the lender is an IVES participant, it uses the **Income Verification Express Service (IVES)** with **Form 4506-C (Rev. October 2022)** instead of 4506-T. IVES is the only way a lender receives transcripts directly.

The lender prepares the Form 4506-C request; the taxpayer authorizes it (on paper, or in their IRS online account for near-real-time delivery, per irs.gov "Income Verification Express Service for participants"); the lender receives the transcript.

If the user has Form 4506-C from the lender:
- Direct the user to sign or authorize that
- Do not duplicate with Form 4506-T
- The IRS charges the IVES participant $4 per transcript (IVES FAQs, updated Dec. 23, 2024)

If the user is unsure whether they need 4506-T or 4506-C, ask the lender. The lender's loan officer can tell them.

---

## Submission state machine

After submission (any channel):

1. **Submitted** → request sent to IRS
2. **Queued** → IRS RAIVS office receives (no notification to user typically)
3. **Processed** → transcript generated
4. **Mailed / Delivered** → transcript sent to address on form

Status checks:
- **Channel 1 (Online)**: immediate once verified
- **Channel 2 (Mail / phone)**: 5-10 calendar days
- **Channel 3 (4506-T fax or mail)**: most within 10 business days of receipt, plus mail time
- **Channel 4 (IVES 4506-C)**: near real time when authorized online

If past expected window with no result:
- Call the IRS transcript line: 800-908-9946
- Have SSN, DOB, current address, prior-year AGI ready

---

## Security and consent rules

These are non-negotiable:

1. **Never request a transcript** for someone other than the user themselves (or with documented authorization via Form 2848 / Form 8821).
2. **Never store** SSN, DOB, ID.me credentials, signed PDFs, or transcript content in agent logs after submission. Process at submission time, then discard.
3. **Line 5 is a customer file number only** (≤10 digits, no SSN or name). Never tell the user the IRS will mail the transcript to a lender.
4. **Confirm the user's own signature and the checked authority box** before mailing/faxing. Do not generate a faux signature.
5. **Refuse** to submit a Form 4506-T with more than one tax form number on line 6; keep one transcript type per form.
6. **If anything looks wrong** (rejection notice, wrong transcript, missing year), surface and let the user respond — don't retry blindly.

---

## Sources

- IRS Form 4506-T (Rev. April 2025): https://www.irs.gov/pub/irs-pdf/f4506t.pdf
- Transcript types and ways to order them: https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them
- IVES for participants: https://www.irs.gov/individuals/income-verification-express-service-for-participants
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Get Transcript: https://www.irs.gov/individuals/get-transcript
- Form 4506: https://www.irs.gov/forms-pubs/about-form-4506
- Form 4506-C (IVES): https://www.irs.gov/forms-pubs/about-form-4506-c
- IRC §6103 — confidentiality of tax returns and disclosure rules
- IRS RAIVS (Return and Income Verification Services) — the back office that processes 4506-T paper/fax requests
- IVES (Income Verification Express Service) — IRS electronic service for high-volume lender requests
