# Example: Homebuyer's Mortgage Lender Requests 2 Years of Tax Return Transcripts

A complete walkthrough for a buyer in escrow whose mortgage underwriter requires Tax Return Transcripts for the last two filed tax years. The user attempts Get Transcript Online first; when ID.me identity verification fails, they fall back to Form 4506-T sent by fax.

## The filer

- **Name**: Priya Anand
- **Filing status**: Single (filed as Single for both years requested)
- **Tax year(s) requested**: 2023 and 2024 (the most recent two filed years; the lender wants two consecutive complete years)
- **State of residence**: Washington
- **Purpose**: Conventional 30-year mortgage application for a primary residence; lender is Pacific Northwest Mortgage; the underwriter requires IRS Tax Return Transcripts (not just W-2 copies) per Fannie Mae underwriting guidelines

## The situation

Priya is closing on a house in 21 days. Her loan officer emailed: "We need IRS Tax Return Transcripts for tax years 2023 and 2024 within 7 business days. We can accept transcripts mailed to you OR sent directly to us via your signed authorization." Priya's loan number is **PNM-2026-04571**.

## Step 1 — Try Get Transcript Online

Priya first attempts the IRS Get Transcript Online portal at https://www.irs.gov/individuals/get-transcript. Identity verification is via ID.me.

She has:
- Government-issued driver's license (Washington state)
- iPhone with camera
- Email and phone in her name

She begins ID.me verification. The selfie capture flow times out twice; on the third attempt, ID.me returns "We could not verify your identity" — this happens occasionally when the ID photo and selfie don't match cleanly enough for the algorithm. ID.me offers a live video session as a backup, but the next available slot is 4 days out.

Given the 7-business-day deadline, Priya decides to fall back to Form 4506-T submitted by fax (faster than mail).

## Step 2 — Confirm transcript type

The lender specifically requested **Tax Return Transcripts**. This maps to **Line 6a — Return Transcript**.

A Tax Return Transcript shows most line items from the originally-filed Form 1040 (filing status, AGI, taxable income, total tax, refundable credits). It does not show subsequent IRS adjustments. For mortgage underwriting that relies on AGI and total income figures, this is the correct type.

## Step 3 — Confirm tax year(s)

Two years requested: 2023 and 2024. Both are within the 3-year window for Return Transcript availability (Form 4506-T allows up to 4 years per request).

Format on Line 9: **12/31/2023** and **12/31/2024** (calendar-year filer).

## Step 4 — Confirm form number filed

Priya filed Form 1040 for both years. Line 6 entry: **1040**.

## Step 5 — Determine routing

Per the routing chart on page 2 of Form 4506-T, Washington state residents fax Form 4506-T to the **Ogden, UT RAIVS** office. Priya looks up the current fax number from the IRS instructions (the form's page 2 is the authoritative source — verify the current number on the IRS-published revision).

## Step 6 — Decide third-party delivery

The lender accepts third-party delivery, and Priya wants the transcripts sent directly to them to save 2–3 days. She fills **Line 5** with the lender's information:

- Name: **Pacific Northwest Mortgage, Attn: Underwriting**
- Address: **1450 Westlake Ave N, Suite 400, Seattle, WA 98109**
- Phone: **(206) 555-0188**
- Customer file number: **PNM-2026-04571** (her loan number)

She confirms the address with her loan officer by phone before submitting (sending sensitive tax data to the wrong address would be a serious problem).

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
   Same as Line 3 (no change in address since 2023 return)

## 5. Third party (mail transcript directly to):
   Name: Pacific Northwest Mortgage, Attn: Underwriting
   Address: 1450 Westlake Ave N, Suite 400, Seattle, WA 98109
   Phone: (206) 555-0188
   Customer file number: PNM-2026-04571

## 6. Transcript requested for: 1040
   [X] 6a. Return Transcript
   [ ] 6b. Account Transcript
   [ ] 6c. Record of Account
   (Exactly one box — 6a — checked)

## 7. [ ] Verification of Non-filing
## 8. [ ] Wage and Income Transcript

## 9. Year(s) requested:
   12/31/2023
   12/31/2024
   (blank)
   (blank)

## Signature box
Signature of taxpayer: Priya Anand (wet signature)
Date: 04/28/2026
Daytime telephone: (206) 555-0142
Print/type name: Priya Anand
Title: (blank — individual filer)

## Spouse signature: (not applicable — Single filer)

## Submission instructions
- Method: Fax to Ogden, UT RAIVS (verify current fax number on Form 4506-T page 2)
- Routing based on state: Washington → Ogden, UT
- Expected processing: 5-10 business days for IRS to fax/mail
- Delivery: IRS will mail transcripts directly to Pacific Northwest Mortgage (Line 5)
- Priya retains a copy of the signed 4506-T for her records

## Validation summary
- Identity:
  - Name on Line 1a matches the legal name on her 2023 and 2024 Form 1040 ✓
  - SSN on Line 1b is 9 digits ✓
  - Single filer; Lines 2a/2b blank ✓
  - Current address Line 3 matches the address she would mail it from ✓
  - Line 4 same as Line 3 (no prior address change) ✓
- Transcript type:
  - Exactly one box (6a Return Transcript) checked ✓
  - Matches purpose (mortgage underwriting) ✓
- Year(s):
  - 2 years (2023, 2024) — within 4-year limit ✓
  - Both formatted as 12/31/YYYY ✓
  - Both years had returns filed (verify) ✓
- Routing:
  - Washington → Ogden, UT RAIVS — confirmed against form page 2 ✓
- Third-party (Line 5):
  - Lender address verified by phone with loan officer ✓
  - Customer file number PNM-2026-04571 included ✓
  - User explicitly authorized direct delivery to lender ✓
- Signatures:
  - Wet signature, dated 04/28/2026 ✓
  - Within 120-day validity window ✓
  - Daytime phone provided ✓

## Sources cited
- IRS Form 4506-T (current revision, page 2 for routing chart)
- IRS Get Transcript portal: https://www.irs.gov/individuals/get-transcript
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Fannie Mae Selling Guide B3-3.1-06 (use of IRS transcripts in mortgage underwriting)
```

## Why each non-obvious choice

**Why try Get Transcript Online first?** It's free, instant, and avoids the 5–10 business day IRS processing window. For a 7-business-day lender deadline, the online path saves the entire mailing cycle. The fallback to 4506-T only happens because ID.me failed.

**Why fax instead of mail?** Fax routes the same form to the same RAIVS office but skips USPS transit time. IRS internal processing is comparable; the savings are 3–5 days on each side. With a tight closing schedule, fax is the right choice.

**Why third-party delivery (Line 5)?** Mailing to Priya first would require her to forward to the lender, adding 2–3 days. The lender accepts direct IRS delivery, so Line 5 is the faster path.

**Why include the customer file number?** The lender's intake system uses the customer file number (loan number) to attach the transcript to the right loan file. Without it, the underwriter has to manually match the IRS-mailed transcript to a borrower — adding delay.

**Why verify the lender's address by phone?** Wrong address sends two years of confidential tax data to a stranger. The 30 seconds of verification is cheap insurance against an identity-theft incident.

**Why not request 4506-C instead?** Form 4506-C is for IVES participants (high-volume lenders with IRS-approved IVES accounts). The lender did not provide a pre-filled 4506-C, so 4506-T is the correct form for Priya to submit on her own. If the lender later sends a pre-filled 4506-C, Priya signs that one — she does not duplicate.

**Why didn't Priya request 6c Record of Account?** The lender specifically asked for **Return Transcript**. Record of Account combines Return + Account but is a heavier document; it would still satisfy the request, but the simpler 6a is what the underwriter expects to see.

## What if the IRS rejects the request?

Common rejection reasons and Priya's responses:

1. **Name/SSN mismatch with IRS records** → re-check name spelling and SSN; if she changed her name (e.g., marriage), the IRS may have the prior name on record. Resubmit with the name on the original return.
2. **Signature older than 120 days** → re-sign with current date and resubmit.
3. **Address on Line 3 doesn't match IRS records** → fill Line 4 with the prior address (the one on the 2023/2024 returns) and resubmit. The IRS uses Line 4 to match identity.
4. **Multiple boxes checked on Line 6** → only one box allowed; resubmit with exactly one.

If the deadline becomes critical, the loan officer may accept a stamped IRS transcript copy from Get Transcript by Mail (a separate IRS service that sends transcripts to the address on file in 5–10 days), or a CPA-prepared income verification letter as a temporary substitute pending the official transcript.
