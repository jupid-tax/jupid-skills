# Online Account and Get Transcript by Mail — When to Use Them Instead of Form 4506-T

For most users, the IRS Individual Online Account (the online side of "Get Transcript") is faster, simpler, and free — and replaces the need for Form 4506-T entirely. This file documents when the online and mail/phone channels are the right choice and how to use them. Facts below were checked on 2026-10-06 against https://www.irs.gov/individuals/get-transcript, https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them, and https://www.irs.gov/help/creating-an-account-for-irsgov; re-check them each season.

URL: https://www.irs.gov/individuals/get-transcript

---

## What Get Transcript provides

Three channels under the same landing page:

### Individual Online Account

- Sign-in requires an **ID.me** account (irs.gov "Creating an account for IRS.gov")
- View, print, or download transcripts as PDFs; available any time
- All five transcript types:
  - Tax Return Transcript — current and three prior tax years
  - Tax Account Transcript — current and nine prior tax years
  - Record of Account — current and three prior tax years
  - Wage and Income Transcript — current and nine prior tax years; limited to about 85 income documents (above that, use Form 4506-T)
  - Verification of Non-filing Letter — after June 15 for the current tax year, anytime for the prior three tax years (older years: Form 4506-T)

### Get Transcript by MAIL

- Needs the mailing address from the user's latest return
- Mails the transcript to the address the IRS has on file
- Arrives in 5 to 10 calendar days
- Only Tax Return Transcript or Tax Account Transcript
- Account transcript by mail: current and three prior tax years

### Automated phone transcript service — 800-908-9946

- Same transcript types and delivery as Get Transcript by Mail

---

## Decision: Online vs. Mail vs. Form 4506-T

```
User wants a transcript

  → User can verify with ID.me (SSN or ITIN + photo ID + selfie or video agent)?
    → Yes → Individual Online Account  (all 5 types)

  → User can't verify online but the IRS has the current address?
    → Yes → Get Transcript by MAIL or 800-908-9946  (5-10 calendar days, return or account transcript only)

  → User needs IRS to mail to a third party (lender, school)?
    → Not available on any channel since July 2019. The user forwards the
      transcript, or the lender uses IVES (Form 4506-C)

  → User needs Wage and Income, Record of Account, or Verification of Non-filing
    AND can't verify online?
    → Form 4506-T  (mail and phone channels don't offer these types)

  → User needs years outside the online/mail windows, a fiscal-year return transcript,
    or a business transcript?
    → Form 4506-T

  → User is a fiduciary requesting on behalf of someone else?
    → Form 4506-T (with appropriate authorization documentation)

  → User has lender's pre-filled Form 4506-C?
    → Sign and return to lender (IVES — fastest channel for lender requests)
```

---

## ID.me identity verification (Individual Online Account)

The IRS uses ID.me to verify identity for online account sign-in (irs.gov "Creating an account for IRS.gov").

### Pre-flight requirements

- Social Security number or ITIN
- Valid government-issued photo ID, such as a driver's license, state ID, passport, or passport card
- For self-service: a smartphone or a computer with a webcam for the selfie; otherwise a video chat with an ID.me agent
- An email address and phone number the user controls (for the account and multi-factor sign-in)

### The verification flow

1. User signs in to the Individual Online Account → redirected to ID.me
2. **Sign up or sign in** with ID.me account
3. **Identity verification options**:
   - **Self-service path**: take a selfie with phone, photograph ID front + back, ID.me's automated face match. Usually instant if all photos clear.
   - **Video chat agent**: an ID.me agent reviews the ID over live video. Used as the fallback when self-service fails; wait times vary.
4. **Multi-factor authentication setup**: SMS, authenticator app, or hardware key
5. **Authorize ID.me to share verified identity with IRS**
6. **Returned to the IRS online account** as an authenticated user
7. **Select transcript type and year**
8. **Download PDF**

### Common failure modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Selfie verification fails repeatedly | Lighting, glasses, expression mismatch | Try again with better lighting; use live video session |
| ID photo rejected | Glare, low resolution, expired ID | Use a different ID; ensure ID is current |
| Address out of date with the IRS | User moved; IRS records still have old address | File Form 8822 to update the IRS. Note that Form 4506-T and mail/phone transcripts are also mailed only to the address of record |
| SSN doesn't match | Typo on user's part, or fraud history flag on the SSN | Re-enter; if persistent, fall back to Form 4506-T |
| Wait queue for video agent | High demand | Try another time, or fall back to Get Transcript by Mail / Form 4506-T |
| No smartphone available | User without compatible device | Use computer + webcam path, or fall back to Get Transcript by Mail / Form 4506-T |

### Why some users prefer 4506-T despite online availability

- **Privacy concern about ID.me**: some users object to handing biometric data (selfie) to a third-party private contractor for federal authentication. Form 4506-T uses traditional paper authentication.
- **Identity theft history**: users who've had tax-related identity theft sometimes cannot complete online verification; 4506-T is a manual workaround.
- **Older users**: comfort with paper forms; uncomfortable with selfie-based auth.
- **Lender-specific requirements**: some lenders ask the borrower to sign a Form 4506-C (IVES) instead; Form 4506-T cannot deliver to the lender.

---

## Get Transcript by Mail flow

For users who can't verify online but have a current address with the IRS:

1. Navigate to https://www.irs.gov/individuals/get-transcript
2. Click "Get transcript by mail" (or call 800-908-9946)
3. Enter the identifying information the tool asks for, including the mailing address from the latest return
4. Select transcript type:
   - Tax Return Transcript, OR
   - Tax Account Transcript
   (No other types via this channel)
5. Select the tax year
6. Submit
7. Wait 5-10 calendar days for the mailed transcript

The transcript is mailed to the address on file with IRS — NOT to any address you specify on the form. If the user moved without filing Form 8822 to update, the transcript goes to the old address.

### Failure modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Address doesn't match" | User moved; IRS records old | Use Form 8822 to update; retry after the IRS processes it |
| "Cannot verify identity" | DOB or SSN wrong | Re-enter; if persistent, use 4506-T |
| Transcript arrives but wrong type | User selected wrong | Re-submit with correct type |
| Transcript never arrives | Mail loss, IRS backlog | Try again; or call 1-800-908-9946 |

---

## Why the agent should always try online first

When an agent has the user's permission and the user has access to a smartphone:

1. **Time savings**: immediate once signed in vs. about 10 business days of processing plus mail for Form 4506-T
2. **Free**: no postage, no fax cost
3. **Audit trail**: PDF transcript is a clean record
4. **All transcript types available**: not limited to two

The agent's first prompt should be: "Have you tried your IRS online account? It gives you the transcript right away once you're verified." If yes and it didn't work, ask why, and escalate to the appropriate fallback. If no, walk them through it.

The Form 4506-T should only be reached after the online account and Get Transcript by Mail are ruled out (for the user's specific need or capability).

---

## When the agent should not push online auth

Don't push the online portal if:
- User has expressed privacy concerns about ID.me biometrics
- User has had tax-related identity theft and online verification keeps failing
- User is requesting on behalf of someone else (the online account is for the taxpayer only)

In those cases, go directly to Form 4506-T from the start.

---

## Sources

- Get Transcript landing: https://www.irs.gov/individuals/get-transcript
- Transcript types and ways to order them: https://www.irs.gov/individuals/transcript-types-and-ways-to-order-them
- ID.me at IRS: https://www.irs.gov/help/creating-an-account-for-irsgov
- Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Form 8822 (change of address): https://www.irs.gov/forms-pubs/about-form-8822
- IRS Identity Protection PIN: https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin
