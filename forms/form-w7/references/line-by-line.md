# Form W-7 Line-by-Line Reference

Complete lookup for every field on Form W-7. Use this when the agent needs to confirm where information goes.

Line numbers below are from **Form W-7 (Rev. December 2024)** and the **Instructions for Form W-7 (Rev. December 2024)**, the current revisions on irs.gov as of 2026-10-06 (<https://www.irs.gov/pub/irs-pdf/fw7.pdf>). Re-check <https://www.irs.gov/forms-pubs/about-form-w-7> for a newer revision before filing — the IRS occasionally renumbers lines.

General rule from the instructions: enter "N/A" on every section of a line that does not apply. Don't leave any section blank (line 4, for example, needs three entries).

---

## Top of form

### Application type checkboxes

Check **exactly one**:

- **Apply for a new ITIN** — first-time application
- **Renew an existing ITIN** — applicant has a previously issued ITIN that needs renewal

If renewing, the previously issued ITIN must be entered on Line 6f.

### Reason for submitting Form W-7

Check the one box of (a) through (h) that best explains the reason, even for renewals. Box a, and box f when claiming an exception, also require box h. This is the most consequential field on the form. See [`reason-codes.md`](./reason-codes.md) for the decision tree.

| Box | Description | Common applicants |
|-----|-------------|-------------------|
| (a) | Nonresident alien required to get ITIN to claim tax treaty benefit | Foreign students, scholars, performers claiming treaty exemption |
| (b) | Nonresident alien filing a U.S. federal tax return | Most non-immigrant aliens with U.S. income |
| (c) | U.S. resident alien (based on days present in U.S.) filing a U.S. federal tax return | Resident aliens without SSN eligibility |
| (d) | Dependent of U.S. citizen/resident alien | Child / parent of U.S. citizen, taxpayer claiming dependent |
| (e) | Spouse of U.S. citizen/resident alien | MFJ filing where spouse is foreign |
| (f) | Nonresident alien student, professor, or researcher filing a U.S. federal tax return or claiming an exception | F/J/M/Q visa holders |
| (g) | Dependent/spouse of a nonresident alien holding a U.S. visa | Less common; dependents of NRA visa holders |
| (h) | Other (must specify) | FIRPTA seller, beneficiary of estate or trust, etc. |

Additional entries depend on the box checked:
- (d): relationship to the U.S. citizen/resident alien on the dotted line
- (d), (e): full name and SSN or ITIN of the U.S. citizen/resident alien on the dotted line
- (g): attach a copy of the applicant's visa; date of entry on line 6d
- (h): description of the reason, or the exception designation (e.g., "Exception 1d-Pension Income", "Exception 3-Mortgage Interest", "Exception 5, T.D. 9363")

### Treaty country and treaty article

"Additional information for a and f": if claiming a treaty benefit under box (a) or (f), enter the treaty country and the specific treaty article number. Example: "Canada, Article XV" for Canadian residents claiming the U.S.-Canada tax treaty's dependent personal services exemption. The treaty country must match the country on line 3.

For non-treaty applications, enter N/A.

---

## Line 1a — Name

Enter the applicant's name **exactly as it appears on identification documents**. If the passport says "MARIA DEL CARMEN RODRIGUEZ HERNANDEZ", that's what goes on Line 1a — every part. Order: First / Middle / Last (Last is the family name; for cultures with two surnames, both go in Last).

If a single document doesn't match Line 1a exactly, the IRS rejects.

## Line 1b — Name at birth (if different)

Enter the applicant's name as it appears on the birth certificate if it differs from Line 1a. Common cases: maiden name (changed at marriage), legal name change.

If same as Line 1a, enter N/A.

---

## Line 2 — Mailing address

Where the IRS sends notices (CP565 / CP566 / CP567) and returns original documents.

Constraints (Instructions for Form W-7, line 2):
- Must be where the applicant **actually receives mail**
- If the U.S. Postal Service won't deliver to the physical location, a USPS P.O. box is allowed; a P.O. box owned by a private firm is not
- No P.O. box or "in care of" (c/o) address if line 3 shows only a country name — the application may be rejected
- The IRS updates its address records from line 2 only if a tax return is attached; otherwise file Form 8822 for a changed home address

Foreign address fully acceptable.

## Line 3 — Foreign address

Enter the complete foreign (non-U.S.) address in the country where the applicant permanently or normally resides, **even if it is the same as line 2** (re-enter it). No P.O. box, no c/o address.

If the applicant relocated to the U.S. and no longer has a permanent foreign residence, enter only the name of the foreign country where they last resided. Exception: reason (b) requires the complete foreign address of the most recent residence. A treaty claim requires the treaty country to match line 3.

---

## Line 4 — Birth information

| Sub-field | Format |
|-----------|--------|
| Date of birth | MM/DD/YYYY |
| Country of birth | Required |
| City and state or province | Optional (enter if available) |

The birth country must be recognized as a foreign country by the U.S. Department of State (Pub 1915).

## Line 5 — Gender

Male / Female. The W-7 form does not currently have a non-binary option.

---

## Line 6 — Other information

### 6a — Country of citizenship

Country (or countries — list both for dual nationals). Use the formal name (e.g., "United Kingdom" not "UK"; "United States of America" not "US"... but "United States" is fine).

### 6b — Foreign tax identification number

If the applicant has a tax ID from their home country, enter it. Optional but reduces friction; the IRS uses it to cross-reference if a treaty issue arises.

If none, enter N/A.

### 6c — Type of U.S. visa (if any), number, and expiration date

Enter only U.S. nonimmigrant visa information: USCIS classification, visa number, and expiration date in MM/DD/YYYY (e.g., "F-1/F-2 123456 05/31/2027"). Attach copies of any I-20/I-94.

For applicants without a U.S. visa: enter N/A.

### 6d — Identification document(s) submitted, and date of entry

Check the box for the document type (Passport / Driver's license/State I.D. / USCIS documentation / Other) and complete:

| Sub-field | Description |
|-----------|-------------|
| Issued by | Country, U.S. state, or other issuer |
| Number | Document number (if any) |
| Exp. date | Document expiration date, MM/DD/YYYY |
| Date of entry into the United States | Complete date the applicant entered the U.S. for the purpose of the ITIN request, MM/DD/YYYY; "Never entered the United States" if never entered |

Enter only the **first** document on this line. For additional documents, attach a separate sheet with the same information and the applicant's name and "Form W-7" at the top.

A passport (or certified copy) needs no other document for identity and foreign status; enter its visa information on 6c and include the U.S. visa pages if a visa is required. A passport with no U.S. date of entry is not stand-alone for dependents who must prove U.S. residency.

See [`identification-documents.md`](./identification-documents.md) for the 13 acceptable types.

### 6e — Previously received an ITIN or IRSN?

Check "Yes" if the applicant ever received an ITIN and/or an Internal Revenue Service Number (IRSN) and complete line 6f. Check "No/Don't know" if never issued or the number is unknown, and skip 6f. Renewals must answer this line.

### 6f — ITIN and/or IRSN and name under which it was issued

Enter the ITIN and/or IRSN and the first, middle, and last name under which it was issued. List additional IRSNs on a separate sheet with the applicant's name and "Form W-7" at the top. Renewals must enter the previously assigned ITIN and the name it was applied under; if the legal name changed, attach the marriage certificate or court order.

### 6g — Name of college/university or company

Box (f) applicants: name of the educational institution, city and state, and length of stay in the U.S. Applicants temporarily in the U.S. for business: company name, city and state, and length of stay. Otherwise N/A.

---

## Signature and date (no line number)

The applicant signs and dates the form and gives a phone number; the signature must be original. A parent or court-appointed guardian may sign for a dependent under 18 who can't sign (print name, check relationship box; attach court papers for a guardian). Any other delegate needs Form 2848. A spouse can't sign for a spouse unless the Power of attorney box is checked and Form 2848 is attached. An applicant who can't sign makes a mark in front of a witness, who also signs.

---

## Acceptance Agent's Use ONLY (if using one)

If submitting via a Certifying Acceptance Agent or Acceptance Agent, the agent completes this block:

- Signature, date, phone, fax
- Name and title, name of company, EIN, PTIN
- **Office code**: the eight-digit office code issued by the ITIN Program Office

The CAA additionally completes Form W-7 (COA) — Certificate of Accuracy (current revision August 2025) — and includes it in the package.

---

## Common field-level errors

1. **Name mismatch between W-7 and identification documents** → rejected. The W-7 name must match exactly. If passport says "JOSE LUIS HERNANDEZ-LOPEZ", the W-7 cannot say "Jose Luis Hernandez Lopez" without the hyphen — it must match.
2. **Date format inconsistency** → use MM/DD/YYYY everywhere on the form (U.S. style)
3. **Blank sections** instead of "N/A" → application suspended or rejected for incomplete information (Pub 1915)
4. **Reason code (a-h) and supporting evidence don't match** → rejected
5. **Incomplete Line 6d** (e.g., missing document expiration date or date of entry) → may be rejected or trigger a CP566 information request
6. **Foreign date format** (DD/MM/YYYY) on Line 4 → causes confusion; convert to U.S. format

---

## Citation summary

- IRS Form W-7 (Rev. December 2024): <https://www.irs.gov/pub/irs-pdf/fw7.pdf>
- IRS Instructions for Form W-7 (Rev. December 2024): <https://www.irs.gov/pub/irs-pdf/iw7.pdf>
- IRS Pub 1915: <https://www.irs.gov/pub/irs-pdf/p1915.pdf>
- IRC §6109 — TIN requirements
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance
