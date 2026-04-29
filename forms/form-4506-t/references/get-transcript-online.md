# Get Transcript Online — When to Use It Instead of Form 4506-T

For most users, the IRS Get Transcript online portal is faster, simpler, and free — and replaces the need for Form 4506-T entirely. This file documents when Get Transcript Online is the right choice and how to use it.

URL: https://www.irs.gov/individuals/get-transcript

---

## What Get Transcript provides

Two channels under the same landing page:

### Get Transcript ONLINE

- Authenticates user via **ID.me** (since August 2022)
- Returns transcripts immediately as downloadable PDFs
- Available 24/7
- All five transcript types supported:
  - Tax Return Transcript
  - Tax Account Transcript
  - Record of Account
  - Wage and Income Transcript
  - Verification of Non-filing Letter
- Year ranges:
  - Return Transcript: current year + 3 prior
  - Account Transcript: many years back
  - Record of Account: current year + 3 prior
  - Wage and Income: last 10 years
  - Verification of Non-filing: any year

### Get Transcript by MAIL

- Authenticates via simpler check: SSN + DOB + address-on-file
- Mails the transcript to the address IRS has on file (no third-party delivery)
- 5-10 business days
- Limited transcript types: only Return Transcript and Account Transcript
- Year ranges: current year + 3 prior

---

## Decision: Online vs. Mail vs. Form 4506-T

```
User wants a transcript

  → User can authenticate online (smartphone, photo ID)?
    → Yes → Get Transcript ONLINE  (instant, all 5 types)

  → User can't authenticate online but address with IRS is current?
    → Yes → Get Transcript by MAIL  (5-10 days, only 2 types)

  → User needs IRS to mail to a third party (lender, school)?
    → Form 4506-T Line 5  (third-party delivery only available via paper form)

  → User needs Wage and Income, Record of Account, or Verification of Non-filing
    AND can't auth online?
    → Form 4506-T  (Get Transcript by Mail doesn't support these types)

  → User is a fiduciary requesting on behalf of someone else?
    → Form 4506-T (with appropriate authorization documentation)

  → User has lender's pre-filled Form 4506-C?
    → Sign and return to lender (IVES — fastest channel for lender requests)
```

---

## ID.me identity verification (Get Transcript Online)

Since August 2022, the IRS contracted ID.me to handle online identity verification. The user must:

### Pre-flight requirements

- Government-issued photo ID:
  - US driver's license, state ID, or passport
  - Permanent Resident Card (green card) for non-citizens
- Smartphone with camera (preferred) OR computer with webcam
- Email address registered to the user
- Phone number registered to the user
- Social Security number
- Home address as on tax records

### The verification flow

1. User clicks "Get Transcript Online" → redirected to ID.me
2. **Sign up or sign in** with ID.me account
3. **Identity verification options**:
   - **Self-service path**: take a selfie with phone, photograph ID front + back, ID.me's automated face match. Usually instant if all photos clear.
   - **Live video session**: live human agent reviews ID and live video. Used as fallback when self-service fails. Wait time can be 30 minutes to several hours during peak season.
4. **Multi-factor authentication setup**: SMS, authenticator app, or hardware key
5. **Authorize ID.me to share verified identity with IRS**
6. **Returned to IRS Get Transcript** as authenticated user
7. **Select transcript type and year**
8. **Download PDF**

### Common failure modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Selfie verification fails repeatedly | Lighting, glasses, expression mismatch | Try again with better lighting; use live video session |
| ID photo rejected | Glare, low resolution, expired ID | Use a different ID; ensure ID is current |
| Address mismatch | User moved; IRS records still have old address | File Form 8822 to update IRS, wait 4-6 weeks; OR use Form 4506-T with both Lines 3 and 4 |
| SSN doesn't match | Typo on user's part, or fraud history flag on the SSN | Re-enter; if persistent, fall back to Form 4506-T |
| Wait queue for live agent | Peak season (Feb-April) | Try off-hours (early morning, late evening) or weekends; or fall back to mail |
| No smartphone available | User without compatible device | Use computer + webcam path, or fall back to Get Transcript by Mail / Form 4506-T |

### Why some users prefer 4506-T despite online availability

- **Privacy concern about ID.me**: some users object to handing biometric data (selfie) to a third-party private contractor for federal authentication. Form 4506-T uses traditional paper authentication.
- **Identity theft history**: users who've had tax-related identity theft sometimes find online auth fails repeatedly because the IRS has flagged their account; 4506-T is a manual workaround.
- **Older users**: comfort with paper forms; uncomfortable with selfie-based auth.
- **Lender-specific requirements**: some lenders explicitly want a 4506-T with Line 5 third-party delivery.

---

## Get Transcript by Mail flow

For users who can't authenticate online but have a current address with IRS:

1. Navigate to https://www.irs.gov/individuals/get-transcript
2. Click "Get Transcript by Mail"
3. Enter:
   - SSN (or ITIN)
   - Date of birth
   - Mailing address as on most recent return
4. Select transcript type:
   - Tax Return Transcript, OR
   - Tax Account Transcript
   (No other types via this channel)
5. Select tax year (current + 3 prior)
6. Submit
7. Wait 5-10 business days for mailed transcript

The transcript is mailed to the address on file with IRS — NOT to any address you specify on the form. If the user moved without filing Form 8822 to update, the transcript goes to the old address.

### Failure modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Address doesn't match" | User moved; IRS records old | Use Form 8822 to update; wait 4-6 weeks; retry |
| "Cannot verify identity" | DOB or SSN wrong | Re-enter; if persistent, use 4506-T |
| Transcript arrives but wrong type | User selected wrong | Re-submit with correct type |
| Transcript never arrives | Mail loss, IRS backlog | Try again; or call 1-800-908-9946 |

---

## Why the agent should always try online first

When an agent has the user's permission and the user has access to a smartphone:

1. **Time savings**: instant vs. 5-14 days
2. **Free**: no postage, no fax cost
3. **Audit trail**: PDF transcript is a clean record
4. **All transcript types available**: not limited to two

The agent's first prompt should be: "Have you tried the IRS Get Transcript online portal? It's instant for most users." If yes and it didn't work, ask why, and escalate to the appropriate fallback. If no, walk them through it.

The Form 4506-T should only be reached after Get Transcript Online and Get Transcript by Mail are ruled out (for the user's specific need or capability).

---

## When the agent should not push online auth

Don't push the online portal if:
- User has expressed privacy concerns about ID.me biometrics
- User has had tax-related identity theft and IRS has placed an Identity Protection PIN (IP PIN) on the account — auth may fail repeatedly
- User is requesting on behalf of someone else (not allowed online)
- User needs third-party delivery to a lender / school (only Form 4506-T Line 5 supports this)

In those cases, go directly to Form 4506-T from the start.

---

## Sources

- Get Transcript landing: https://www.irs.gov/individuals/get-transcript
- ID.me at IRS: https://www.irs.gov/help/sign-in-help-faqs (covers ID.me transition)
- Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Form 8822 (change of address): https://www.irs.gov/forms-pubs/about-form-8822
- IRS Identity Protection PIN: https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin
