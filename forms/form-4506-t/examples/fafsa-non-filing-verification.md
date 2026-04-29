# Example: College Student Needs Verification of Non-filing Letter for FAFSA

A complete walkthrough for a student whose financial-aid office requires an IRS Verification of Non-filing Letter (VNF). The student's parent earned below the filing threshold and did not file a federal tax return for the prior year. Form 4506-T Line 7 produces the VNF. Note the year-availability quirk: VNFs are available for the prior 4 tax years, but transcript types differ for older years — pay attention to which line maps to which need.

## The filer

- **Name**: Jasmine Carter (the parent — she is the one who didn't file and whose VNF the school needs)
- **Filing status**: She would have filed as Head of Household if required, but her gross income was below the HoH filing threshold for the year, so she was not required to file
- **Tax year requested**: 2023 (the FAFSA year for academic year 2025–2026 uses 2023 income data — the "prior-prior year" rule)
- **State of residence**: Georgia
- **Purpose**: Her daughter Aliyah's college financial-aid office at Georgia State University requires a Verification of Non-filing Letter from the IRS confirming Jasmine did not file a 2023 federal return. Aliyah's FAFSA was selected for verification; the school's verification worksheet specifically asks for an IRS-issued VNF (a self-statement is not accepted).

## The situation

Aliyah filled out the 2025–2026 FAFSA and was selected for verification (about 25–30% of FAFSAs are flagged for verification each cycle). The school's verification process requires Jasmine, as the contributor parent, to either submit a Tax Return Transcript (if she filed) or a Verification of Non-filing Letter (if she did not file).

Jasmine did not file a 2023 return because her 2023 gross income was below the HoH filing threshold for someone under 65 ($21,150 for 2023). She earned about $19,400 from a part-time job; her employer withheld federal income tax, but the threshold for filing was higher than her income, so she had no filing obligation. (She could have filed to claim the withholding back as a refund, but she didn't.)

## Step 1 — Try Get Transcript Online

Jasmine first attempts the IRS Get Transcript Online portal. The portal does support VNFs, but ID.me identity verification requires a credit history that the IRS / ID.me can match against. Jasmine has limited credit history (no mortgage, no recent auto loan), and ID.me cannot complete the knowledge-based identity quiz.

She falls back to Form 4506-T sent by mail.

## Step 2 — Confirm transcript type

The school requires a **Verification of Non-filing Letter**. This maps to **Line 7** on Form 4506-T.

The VNF confirms that the IRS has no record of a Form 1040 (or 1040-SR / 1040-NR) filed for the requested year by the requesting taxpayer. It is a single-page IRS-issued letter that explicitly states "no record of return filed." Schools accept the VNF as official proof of non-filing.

## Step 3 — Confirm tax year

For the 2025–2026 academic-year FAFSA, the income data referenced is **tax year 2023** (FAFSA uses prior-prior year income under the FAFSA Simplification Act).

Format on Line 9: **12/31/2023** (calendar-year).

**Year-availability note**: VNFs via Form 4506-T are available for the **current year and 3 prior years** (4 years total). For tax years older than that, the VNF is not directly issuable via 4506-T — older non-filing verification has to go through written request to the IRS or via tax-account research, which is a slower process. Tax year 2023 is well within the 4-year window, so Line 7 works directly.

For older years (e.g., a school asking for 2018 VNF), the agent should warn the user that Form 4506-T may return "no record available" and route them to call the IRS or visit a TAC.

## Step 4 — Confirm form number filed

Line 6 form number: **1040** (the type of return she would have filed if required).

## Step 5 — Determine routing

Per the routing chart on page 2 of Form 4506-T, **Georgia** residents typically mail Form 4506-T to the **Kansas City, MO RAIVS** office (verify the current mailing address on the form's page 2).

Jasmine chose mail because she has time before the school's verification deadline (approximately 6 weeks). Fax would be faster but is unnecessary given the timeline.

## Step 6 — Decide third-party delivery

Jasmine could have the VNF mailed directly to the school via Line 5, but she prefers to receive it herself first to keep a copy for her records, then upload it to the school's verification portal. **Line 5 stays blank**; the IRS mails to her Line 3 address.

(Alternative scenario: if she fills Line 5, she would put: "Georgia State University, Office of Student Financial Services, P.O. Box 3982, Atlanta, GA 30302" with the school's customer file number being Aliyah's student ID. The school would receive directly. Either path is acceptable.)

## The completed Form 4506-T draft

```markdown
# Form 4506-T — DRAFT

## 1a. Name shown on tax return: Jasmine Carter
## 1b. First social security number: XXX-XX-XXXX

## 2a. Second name on tax return: (blank — Jasmine would have filed HoH if required, no spouse)
## 2b. Second SSN: (blank)

## 3. Current name and address:
   Jasmine Carter
   1487 Memorial Drive SE, Apt 2
   Atlanta, GA 30317

## 4. Previous address shown on the last return filed:
   Jasmine Carter
   2240 Cascade Road SW
   Atlanta, GA 30311
   (Address shown on Jasmine's 2022 Form 1040 — the most recent return she filed,
   for tax year 2022; her 2023 was the non-filing year)

## 5. Third party: (blank — Jasmine wants the VNF mailed to herself)

## 6. Transcript requested for: 1040
   [ ] 6a. Return Transcript
   [ ] 6b. Account Transcript
   [ ] 6c. Record of Account
   (No box checked on Line 6 — VNF requested via Line 7)

## 7. [X] Verification of Non-filing

## 8. [ ] Wage and Income Transcript

## 9. Year(s) requested:
   12/31/2023
   (blank)
   (blank)
   (blank)

## Signature box
Signature of taxpayer: Jasmine Carter (wet signature)
Date: 04/28/2026
Daytime telephone: (404) 555-0136
Print/type name: Jasmine Carter
Title: (blank — individual filer)

## Spouse signature: (not applicable)

## Submission instructions
- Method: Mail to Kansas City, MO RAIVS (verify current address on Form 4506-T page 2)
- Routing based on state: Georgia → Kansas City, MO
- Expected processing: 10-14 calendar days IRS processing + USPS transit each way
- Total round-trip: typically 3-4 weeks from drop to receipt
- Delivery: IRS will mail the Verification of Non-filing Letter to Jasmine's Line 3 address

## Validation summary
- Identity:
  - Name on Line 1a matches the legal name on her 2022 Form 1040 (last filed) ✓
  - SSN on Line 1b is 9 digits ✓
  - Single contributor; Lines 2a/2b blank ✓
  - Current address Line 3 (Memorial Drive); Line 4 shows the Cascade Road address from 2022 ✓
  - Line 4 critical here: the IRS uses the 2022 return address for identity matching ✓
- Transcript type:
  - Exactly one box checked: Line 7 (Verification of Non-filing) ✓
  - Lines 6a/6b/6c/8 all unchecked ✓
  - Matches purpose (FAFSA verification of non-filing) ✓
- Year(s):
  - 1 year (2023) — within 4-year availability for VNF ✓
  - Formatted as 12/31/2023 ✓
  - Confirmed Jasmine did not file 2023 (so VNF will return "no record found,"
    which is the desired result for FAFSA) ✓
- Routing:
  - Georgia → Kansas City, MO RAIVS — confirmed against form page 2 ✓
- Third-party: blank ✓ (Jasmine wants direct copy)
- Signatures:
  - Wet signature, dated 04/28/2026 ✓
  - Within 120-day validity window ✓
  - Daytime phone provided ✓

## Sources cited
- IRS Form 4506-T (current revision, page 2 for routing chart)
- IRS Get Transcript portal: https://www.irs.gov/individuals/get-transcript
- About Form 4506-T: https://www.irs.gov/forms-pubs/about-form-4506-t
- Federal Student Aid (FSA) Handbook, Verification chapter
- FAFSA Simplification Act (prior-prior year income reference)
- IRS Publication 501 (filing requirements and thresholds)
```

## Year-availability caveat for older VNFs

Form 4506-T can request VNFs for the current and prior 3 tax years. For tax years older than that, the IRS systems may not return a VNF directly, and the requester may need to:

1. Request a Tax Account Transcript (Line 6b) instead — for older years, the Account Transcript will show "no return filed" or no posted return data, which some schools will accept as equivalent to VNF.
2. Call the IRS directly (PPS for tax pros, or the general IRS line for individuals) and request a written non-filing statement.
3. Visit a Taxpayer Assistance Center for in-person verification.

If the school requests a 2019 VNF and the user attempts Line 7 on a 2026-filed 4506-T, the IRS may return "no record" (which is acceptable for non-filing proof) but may also return "request cannot be processed for tax years older than 4 years." In that case, escalate to one of the alternatives above.

This is why the SKILL workflow says: "Verification of Non-filing Letter — required for FAFSA when student or parent did not file taxes" — and notes that older years may require alternative paths.

## Why each non-obvious choice

**Why Line 7 and not Line 6a?** Line 6a (Return Transcript) is for *filed* returns. Jasmine did not file a 2023 return, so a Return Transcript would return "no record" — which is technically equivalent to the VNF, but schools specifically request the VNF document because it is an explicit IRS letter, not a "no record" empty transcript response. Line 7 produces the explicit VNF.

**Why does Line 4 (previous address) matter so much here?** Jasmine moved between her 2022 return (filed in 2023) and her current address. The IRS verifies identity by matching the address on the most recent return (her 2022 return showing the Cascade Road address). Line 4 must reflect that, not blank, or the IRS may reject for failed identity verification.

**Why use prior-prior year (2023 for 2025–2026 academic year)?** The FAFSA Simplification Act and prior FAFSA rules use **prior-prior year (PPY)** income data. A FAFSA submitted in fall 2024 for the 2025–2026 academic year asks about tax year 2023 income (the PPY). This lets families file FAFSA earlier in the cycle without waiting for the most recent year's tax return. The VNF must therefore be for tax year 2023, not 2024.

**Why didn't Jasmine just file a $0 return to avoid this hassle?** She could have. Filing a "zero return" (a return showing income below the threshold) would have produced a Tax Return Transcript via Line 6a, which the school accepts. But she didn't, so she now needs the VNF. (The agent might suggest filing a zero return for future years to avoid repeated VNF requests if Aliyah is a multi-year student.)

**Why is the VNF only valid for 4 years?** IRS RAIVS systems retain non-filing data for the current and prior 3 years actively. Older years require manual research. The 4-year window matches the FAFSA prior-prior year typical use case (which never goes back further than 2 years from the academic year start).

**Could Jasmine submit the IRS Tax Compliance Report from her IRS online account instead?** Some schools accept printouts from the IRS online account showing non-filing status. Verify with the financial-aid office before submitting Form 4506-T — it could save 3–4 weeks. But the formal VNF is universally accepted, while the online printout is not.

**Why doesn't the agent suggest IRS Get Transcript by Mail (a different IRS service) for VNFs?** Get Transcript by Mail is a separate IRS portal that delivers Tax Return Transcripts and Wage and Income Transcripts to the address on file but does **not** support Verification of Non-filing Letters. VNFs require Form 4506-T (or in-person at a TAC, or online via Get Transcript Online with successful ID.me).

## What if the IRS returns "no record found" but the school still rejects it?

The VNF *is* the school's expected document. If the school's verification worksheet specifically asks for "IRS Verification of Non-filing Letter," then the VNF Jasmine receives — even if it says "we have no record of a tax return filed" — is the correct document. She uploads it as-is.

If the school's intake clerk rejects it because they don't recognize the format, Jasmine can:
1. Point to the IRS letterhead and the explicit "no return filed" language
2. Ask the financial-aid office to escalate to a verifier who knows the FAFSA verification rules
3. Reference Federal Student Aid Handbook Chapter 4 (Verification), which specifies VNF as acceptable

The VNF is the correct document; rejection is usually a clerical issue, not a problem with the IRS response.
