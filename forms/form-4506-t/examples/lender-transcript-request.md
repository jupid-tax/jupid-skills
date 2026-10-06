# Example: Homebuyer's Mortgage Lender Requests 2 Years of Tax Return Transcripts

A complete walkthrough for a buyer in escrow whose mortgage underwriter requires Tax Return Transcripts for the last two filed tax years. The user tries her IRS online account first; when ID.me identity verification fails, she faxes Form 4506-T, and the IRS mails the transcripts to her so she can forward them. (Form 4506-T, Rev. April 2025.)

## The filer

- **Name**: Priya Anand
- **Filing status**: Single (filed as Single for both years requested)
- **Tax year(s) requested**: 2023 and 2024 (the most recent two filed years; the lender wants two consecutive complete years)
- **State of residence**: Washington
- **Purpose**: Conventional 30-year mortgage application for a primary residence; lender is Pacific Northwest Mortgage; the underwriter requires IRS Tax Return Transcripts (not just W-2 copies) per Fannie Mae underwriting guidelines

## The situation

Priya is closing on a house in 21 days. Her loan officer emailed: "We need IRS Tax Return Transcripts for tax years 2023 and 2024. Send us the transcripts you receive from the IRS." Priya's loan number is **PNM-2026-04571**.

The agent first asks whether the lender is an IVES participant that could pull the transcripts itself with a Form 4506-C (faster, and the only way a lender receives transcripts directly). The loan officer says no, so Priya must get them herself.

## Step 1 — Try the Individual Online Account

Priya first tries to sign in to her IRS Individual Online Account from https://www.irs.gov/individuals/get-transcript. Identity verification is via ID.me.

She has:
- Government-issued driver's license (Washington state)
- iPhone with camera
- Email and phone in her name

She begins ID.me verification. The selfie capture flow times out twice; on the third attempt, ID.me returns "We could not verify your identity." ID.me offers a video chat agent as a backup, but the wait is longer than she wants.

Get Transcript by Mail would deliver a return transcript to her address on file in 5-10 calendar days, and is a reasonable alternative. Priya decides on Form 4506-T by fax because she wants both years on one request with a customer file number printed on the transcripts. The agent tells her: the IRS says most Form 4506-T requests are processed within 10 business days, and the transcripts are then mailed to her address of record, so she should also keep trying the online account.

## Step 2 — Confirm transcript type

The lender specifically requested **Tax Return Transcripts**. This maps to **Line 6a — Return Transcript**.

A Tax Return Transcript shows most line items from the originally-filed Form 1040 (filing status, AGI, taxable income, total tax, refundable credits). It does not show subsequent IRS adjustments. For mortgage underwriting that relies on AGI and total income figures, this is the correct type.

## Step 3 — Confirm tax year(s)

Two years requested: 2023 and 2024. Both are within the window for Return Transcript availability (current year and the prior 3 processing years); line 9 has four date slots.

Format on Line 9: **12/31/2023** and **12/31/2024** (calendar-year filer).

## Step 4 — Confirm form number filed

Priya filed Form 1040 for both years. Line 6 entry: **1040**.

## Step 5 — Determine routing

Per the "Chart for individual transcripts" on page 2 of Form 4506-T (Rev. April 2025), a return filed while living in Washington goes to the **Ogden RAIVS Team**: Internal Revenue Service, RAIVS Team, P.O. Box 9941, Mail Stop 6734, Ogden, UT 84409, **fax 855-298-1145**. She lived in Washington when she filed both returns.

## Step 6 — Customer file number and delivery

Line 5 is a customer file number only: up to 10 numeric characters printed on the transcript. The IRS will not mail the transcripts to the lender (since July 2019 it mails Form 4506-T transcripts only to the taxpayer's address of record). The loan number PNM-2026-04571 has letters and dashes, so Priya enters only its digits: **202604571**. The agent confirms her current address is the one the IRS has on file (she has not moved since filing), so no Form 8822 is needed.

## The completed Form 4506-T draft

```markdown
# Form 4506-T — DRAFT

## 1a. Name shown on tax return: Priya Anand
## 1b. First social security number: XXX-XX-XXXX

## 2a. Second name on tax return: (blank — Priya filed Single)
## 2b. Second SSN: (blank)

## 3. Current name and address:
   Priya Anand
   2814 NE 47th Street, Apt 6
   Seattle, WA 98105

## 4. Previous address shown on the last return filed:
   (blank — same as line 3)

## 5. Customer file number: 202604571

## 6. Transcript requested for: 1040
   [X] 6a. Return Transcript
   [ ] 6b. Account Transcript
   [ ] 6c. Record of Account
   (One box — 6a — checked)

## 7. [ ] Verification of Non-filing
## 8. [ ] Wage and Income Transcript

## 9. Year(s) requested:
   12/31/2023
   12/31/2024
   (blank)
   (blank)

## Signature area
[X] Signatory attests authority to sign
Phone number of taxpayer on line 1a: (206) 555-0142
Signature of taxpayer: Priya Anand (signed by hand)
Date: 04/28/2026
Title: (blank — individual filer)

## Spouse signature: (not applicable — Single filer)

## Submission instructions
- Method: Fax to 855-298-1145 (Ogden RAIVS Team, individual-transcripts chart)
- Routing based on state when the returns were filed: Washington → Ogden, UT
- Expected processing: most requests within 10 business days (form), then mailed
- Delivery: IRS mails the transcripts to Priya's address of record; she scans and sends them to the lender
- Priya retains a copy of the signed 4506-T for her records

## Validation summary
- Identity:
  - Name on Line 1a matches the legal name on her 2023 and 2024 Form 1040 ✓
  - SSN on Line 1b is 9 digits ✓
  - Single filer; Lines 2a/2b blank ✓
  - Current address Line 3 matches the address she would mail it from ✓
  - Line 4 blank (no address change since the last return) ✓
- Transcript type:
  - One form number (1040) and one box (6a Return Transcript) ✓
  - Matches purpose (mortgage underwriting) ✓
- Year(s):
  - 2 years (2023, 2024) — within the four date slots ✓
  - Both formatted as 12/31/YYYY ✓
  - Both years had returns filed (verify) ✓
- Routing:
  - Washington → Ogden, UT RAIVS, fax 855-298-1145 — confirmed against form page 2 ✓
- Customer file number (Line 5):
  - 9 digits, no SSN, no name ✓
- Signatures:
  - Authority box checked ✓
  - Signed and dated 04/28/2026; IRS will receive it well within 120 days ✓
  - Phone provided ✓

## Sources cited
- IRS Form 4506-T (Rev. April 2025), page 2 for the routing chart
- IRS Get Transcript page: https://www.irs.gov/individuals/get-transcript
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Fannie Mae Selling Guide B3-3.1-06 (use of IRS transcripts in mortgage underwriting)
```

## Why each non-obvious choice

**Why try the online account first?** It's free and immediate once verified, and avoids the processing and mail time of Form 4506-T. The fallback to 4506-T only happens because ID.me failed.

**Why fax instead of mail?** Fax reaches the same RAIVS office without inbound USPS transit. The transcript still comes back by mail to her address of record.

**Why not have the IRS send the transcripts to the lender?** It can't. Since July 2019 the IRS mails Form 4506-T transcripts only to the taxpayer's address of record; Line 5 is only a customer file number. A lender that wants transcripts directly uses IVES (Form 4506-C).

**Why include the customer file number?** Transcripts mask the SSN, so a number printed on the transcript helps the underwriter match it to the loan file. Only digits are allowed (up to 10), so she uses the digits of her loan number.

**Why not request 4506-C instead?** Form 4506-C is for IVES participants. This lender is not one, so Priya gets the transcripts herself. If a lender sends a Form 4506-C, the borrower signs that one and does not duplicate it with a 4506-T.

**Why didn't Priya request 6c Record of Account?** The lender specifically asked for **Return Transcript**. Record of Account combines Return + Account but is a heavier document; it would still satisfy the request, but the simpler 6a is what the underwriter expects to see.

## What if the IRS rejects the request?

Common rejection reasons and Priya's responses:

1. **Name/SSN mismatch with IRS records** → re-check name spelling and SSN; if she changed her name (e.g., marriage), the IRS may have the prior name on record. Resubmit with the name on the original return.
2. **Signature older than 120 days** → re-sign with current date and resubmit.
3. **Authority box unchecked** → the form is returned unprocessed; check the box, re-sign, refax.
4. **Transcript went to an old address** → the IRS mails only to the address of record; if she had moved, she would file Form 8822 first.

If the deadline becomes critical, Get Transcript by Mail (or 800-908-9946) sends a return transcript to the address on file in 5-10 calendar days, and the online account remains the fastest path if ID.me verification succeeds on a later try.
