# Example: Freelancer Lost W-2 and 1099-NECs — Wage and Income Transcript

A complete walkthrough for a filer who needs to file the prior-year return but lost the W-2 and 1099-NEC source documents. Form 4506-T Line 8 (Form W-2/1099 series transcript, called the Wage and Income Transcript online) returns the third-party-reported income data the IRS already has on file. Form 4506-T, Rev. April 2025.

## The filer

- **Name**: Marcus Reilly
- **Filing status**: Single (no spouse, no dependents)
- **Tax year requested**: 2024 (he needs to file the 2024 return; he is past the original April 15, 2025 deadline and now well into 2026 — late filing)
- **State of residence**: Texas
- **Purpose**: Marcus had a W-2 from a part-time job (Jan–Apr 2024) and 1099-NECs from three freelance clients (Apr–Dec 2024). He moved twice in 2024–2025 and his hardcopies are lost. His old employer doesn't respond to requests for a W-2 reprint, and one of the freelance clients went out of business. He needs the IRS-reported figures to file an accurate Schedule C and Form 1040 for 2024.

## The situation

Marcus realizes he never filed his 2024 return when he gets a CP59 notice from the IRS in spring 2026 ("We have no record of your 2024 tax return"). He wants to file accurately rather than guess at the numbers. The Wage and Income Transcript on Form 4506-T Line 8 will return all third-party-reported W-2s, 1099-NECs, 1099-MISCs, 1099-DIVs, 1099-INTs, etc. that the IRS received under his SSN for tax year 2024.

For tax year 2024, the issuers' filings were due in early 2025, so by spring 2026 the data has long been on the IRS system (irs.gov: current-processing-year data generally appears online in the first week of February and may be incomplete early on). Form 4506-T says this transcript is available for up to 10 years.

## Step 1 — Try the Individual Online Account

Marcus tries his IRS online account first. He verifies through ID.me on the first try and downloads the **2024 Wage and Income Transcript** as a PDF immediately. Get Transcript by Mail would not help here: it offers only return and account transcripts.

In an alternate scenario where ID.me verification failed, he would fall back to Form 4506-T. The example below assumes the fallback path so the form fill is shown end-to-end.

## Step 2 — Confirm transcript type

Marcus needs the third-party income data, not the return data (he didn't file a return for 2024). The correct type is:

**Line 8 — Wage and Income Transcript**

This shows W-2s, 1099-NECs, 1099-MISCs, 1099-DIVs, 1099-INTs, 1099-Rs, K-1s, 1098-mortgage interest forms, etc., with reporting party name and amounts. It is the source of truth for what issuers reported under his SSN.

## Step 3 — Confirm tax year

Single year requested: **2024**. Format on Line 9: **12/31/2024** (calendar-year).

## Step 4 — Confirm form number filed

For Wage and Income Transcripts, the form number on Line 6 should reflect the type of return associated with the data. Marcus will eventually file Form 1040; he enters **1040** on Line 6. (Note: Wage and Income Transcript via Line 8 is keyed to the SSN and tax year; the form-number entry is informational.)

## Step 5 — Determine routing

The "Chart for individual transcripts" on page 2 of Form 4506-T routes by the state the filer lived in **when the return was filed**, and when in doubt the form points to the address of the most recent return. There is no 2024 return; Marcus's most recent return (2023) was filed from New York, which routes to the **Kansas City RAIVS Team**: Internal Revenue Service, RAIVS Team, Stop 6705 S-2, Kansas City, MO 64999 (fax 855-821-0094). (Texas would route to Austin.) The agent tells Marcus this reading is the conservative one because the form does not address a request where no return was filed for the year.

Marcus chose mail rather than fax because he has no fax access. He is not under deadline pressure (no closing, no FAFSA cutoff).

**Delivery address.** The IRS mails transcripts only to the address of record, which is still the Brooklyn address from his 2023 return. The form says that when lines 3 and 4 differ and the address has not been changed with the IRS, file Form 8822. Marcus mails Form 8822 first; otherwise the transcript would go to Brooklyn.

## Step 6 — Customer file number

Marcus doesn't need one. **Line 5 stays blank.** (Line 5 is only an optional customer file number of up to 10 digits; it never redirects delivery.)

## The completed Form 4506-T draft

```markdown
# Form 4506-T — DRAFT

## 1a. Name shown on tax return: Marcus Reilly
## 1b. First social security number: XXX-XX-XXXX

## 2a. Second name on tax return: (blank — Single filer)
## 2b. Second SSN: (blank)

## 3. Current name and address:
   Marcus Reilly
   3712 Burnet Road, Apt 12
   Austin, TX 78757

## 4. Previous address shown on the last return filed:
   Marcus Reilly
   2105 Greene Avenue, Apt 3R
   Brooklyn, NY 11225
   (Address shown on Marcus's 2023 Form 1040 — most recent return filed)

## 5. Customer file number: (blank)

## 6. Transcript requested for: 1040
   [ ] 6a. Return Transcript
   [ ] 6b. Account Transcript
   [ ] 6c. Record of Account
   (No box checked on Line 6 — Wage and Income Transcript requested via Line 8)

## 7. [ ] Verification of Non-filing

## 8. [X] Wage and Income Transcript

## 9. Year(s) requested:
   12/31/2024
   (blank)
   (blank)
   (blank)

## Signature area
[X] Signatory attests authority to sign
Phone number of taxpayer on line 1a: (512) 555-0117
Signature of taxpayer: Marcus Reilly (signed by hand)
Date: 04/28/2026
Title: (blank — individual filer)

## Spouse signature: (not applicable — Single filer)

## Submission instructions
- Method: Mail to Internal Revenue Service, RAIVS Team, Stop 6705 S-2, Kansas City, MO 64999
- Routing: most recent return (2023) filed from New York → Kansas City (individual-transcripts chart)
- Expected processing: most requests within 10 business days of receipt (form), plus USPS transit each way
- Delivery: IRS mails the transcript to the address of record; Form 8822 mailed first so that is the Austin address

## Validation summary
- Identity:
  - Name on Line 1a matches the legal name on his 2023 Form 1040 (last filed) ✓
  - SSN on Line 1b is 9 digits ✓
  - Single filer; Lines 2a/2b blank ✓
  - Current address Line 3 (Austin) is current; Line 4 shows the Brooklyn address from the 2023 return ✓
  - Form 8822 filed so the address of record matches Line 3 ✓
- Transcript type:
  - Exactly one box checked: Line 8 (Wage and Income Transcript) ✓
  - Lines 6a/6b/6c/7 all unchecked ✓
  - Matches purpose (replace lost W-2 and 1099-NECs to file 2024 return) ✓
- Year(s):
  - 1 year (2024) — within the 10-year availability on the form ✓
  - Formatted as 12/31/2024 ✓
- Routing:
  - Most recent return from New York → Kansas City RAIVS — confirmed against form page 2 ✓
- Customer file number: blank ✓
- Signatures:
  - Authority box checked ✓
  - Signed and dated 04/28/2026; IRS will receive it well within 120 days ✓
  - Phone provided ✓

## Sources cited
- IRS Form 4506-T (Rev. April 2025), page 2 for routing chart
- IRS Get Transcript page: https://www.irs.gov/individuals/get-transcript
- Form 8822 (Change of Address)
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- IRC §6103 (confidentiality of tax returns)
- IRS Publication 17 (general individual filing guidance, late filing)
```

## What the transcript will return

Once received, Marcus's 2024 Wage and Income Transcript will list, for each issuer:

- Reporting party name and EIN
- Form type (W-2, 1099-NEC, 1099-MISC, etc.)
- Box-by-box amounts (gross wages, federal withholding, state withholding, nonemployee compensation, etc.)
- Recipient name and SSN match

Marcus expects to see:
- One W-2 from his Jan–Apr part-time employer (gross wages, federal/state withholding)
- Three 1099-NECs from his freelance clients (Box 1 nonemployee compensation each)
- Possibly a 1099-INT from his bank if he had savings interest above the $10 reporting threshold

He uses these to reconstruct his 2024 income and prepare:
- Form 1040 (wages on Line 1a from the W-2; Schedule C income from the 1099-NECs)
- Schedule C for his freelance net profit
- Schedule SE for self-employment tax on the Schedule C net

## Why each non-obvious choice

**Why Wage and Income Transcript (Line 8) and not Return Transcript (Line 6a)?** Marcus didn't file a 2024 return. There is no 2024 Return Transcript to retrieve. Wage and Income Transcript pulls the *third-party-reported* income data from the IRS's information-return system, which exists independently of whether Marcus filed.

**Why do Line 4 and Form 8822 matter here?** Marcus moved from Brooklyn (his 2023 return address) to Austin. Line 4 must show the address on his last return. And because the IRS mails transcripts only to the address of record, he files Form 8822 so the transcript reaches Austin; the form itself tells filers to do this when lines 3 and 4 differ and the address was not changed with the IRS.

**Why mail and not fax?** Marcus has no fax access and no deadline. Mail is fine. Fax would skip the inbound mail time.

**What if the Wage and Income Transcript is missing one of the 1099-NECs?** The IRS only has data the issuer reported. If the failed freelance client went out of business and never filed the 1099-NEC, that income won't appear on the transcript. Marcus is still required to report it on Schedule C (his obligation is on actual income earned, not on what was reported), so he reconstructs the missing client's payments from his bank statements and reports the full amount.

**Why doesn't Marcus also need a 2024 Return Transcript?** He didn't file. A Return Transcript would just confirm "no return on file" — which is what the CP59 notice already says. The Wage and Income Transcript gives him what he needs to file accurately.

**Could Marcus also request 2025 Wage and Income data on the same form?** Yes — line 9 has four date slots. In April 2026 the 2025 data may still be incomplete (the form says current-year information is generally not available until the year after it is filed). He did not add it because he wants to focus on the overdue 2024 return first.

**Penalty exposure note (mention to user, not part of the form):** Marcus is filing late. He may owe failure-to-file penalty (5% per month, capped at 25%) and failure-to-pay penalty (0.5% per month) plus interest on any 2024 balance owed. If a refund was due, no penalty — but the IRS only refunds if the return is filed within 3 years of the original due date.

## What if the IRS rejects the request?

Common rejection reasons and Marcus's responses:

1. **Authority box unchecked** → the form is returned unprocessed; check it, re-sign, resubmit.
2. **Name mismatch** → ensure the name matches exactly what's on the 2023 return (suffix, middle name, hyphenation).
3. **Signature too old** → the IRS must receive the form within 120 days of signing; re-sign with current date.
4. **Transcript sent to Brooklyn** → Form 8822 not yet processed; wait for it, then request again.

If the transcript is missing a 1099-NEC, the issuer may never have filed it; Marcus contacts each 1099 issuer directly or reconstructs the income from bank records (he must report it either way).
