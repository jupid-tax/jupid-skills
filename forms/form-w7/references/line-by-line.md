# Form W-7 Line-by-Line Reference

Complete lookup for every field on Form W-7. Use this when the agent needs to confirm where information goes.

Line numbers below are from the latest revision of Form W-7 at <https://www.irs.gov/pub/irs-pdf/fw7.pdf>. Verify against the current form before filing — the IRS occasionally renumbers lines.

---

## Top of form

### Application type checkboxes

Check **exactly one**:

- **Apply for a new ITIN** — first-time application
- **Renew an existing ITIN** — applicant has a previously issued ITIN that needs renewal

If renewing, the previously issued ITIN must be entered on Line 6f.

### Reason for submitting Form W-7

Check **exactly one** of (a) through (h). This is the most consequential field on the form. Picking the wrong code is the #1 rejection reason. See [`reason-codes.md`](./reason-codes.md) for the decision tree.

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

Additional sub-questions appear depending on the box checked:
- (d), (e): name and SSN of primary U.S. citizen/resident alien
- (g): visa type held by primary alien
- (h): explanation of "Other" basis

### Treaty country and treaty article

If applying under a tax treaty (often boxes (a), (e), (f)), enter the country and the specific treaty article. Example: "Canada, Article XV" for Canadian residents claiming the U.S.-Canada tax treaty's dependent personal services exemption.

For non-treaty applications, leave blank.

---

## Line 1a — Name

Enter the applicant's name **exactly as it appears on identification documents**. If the passport says "MARIA DEL CARMEN RODRIGUEZ HERNANDEZ", that's what goes on Line 1a — every part. Order: First / Middle / Last (Last is the family name; for cultures with two surnames, both go in Last).

If a single document doesn't match Line 1a exactly, the IRS rejects.

## Line 1b — Name at birth (if different)

Enter the applicant's name at birth if it differs from Line 1a. Common cases: maiden name (changed at marriage), legal name change.

If same as Line 1a, leave blank.

---

## Line 2 — Mailing address

Where the IRS sends correspondence (CP-565 / CP-566 letters) and the ITIN.

Constraints:
- Must be where the applicant **actually receives mail**
- Cannot be a P.O. Box outside the U.S. (foreign P.O. Box not accepted in some cases — verify on instructions; foreign physical address is fine)
- Cannot be a third party's office (CPA, attorney, employer) — the IRS rejects these to prevent identity-linking issues
- For incarcerated applicants, the prison's mailing address is acceptable

Foreign address fully acceptable.

## Line 3 — Foreign address

If different from mailing address, enter the applicant's foreign (home country) address. Used for IRS records.

If same as mailing address, leave blank.

---

## Line 4 — Birth information

| Sub-field | Format |
|-----------|--------|
| Date of birth | MM/DD/YYYY |
| Place of birth | City, State (or province), Country |

City and country are required; state/province if applicable in the home country. If the applicant doesn't know the city (e.g., orphaned, refugee), they enter "Unknown" with a note.

## Line 5 — Gender

Male / Female. The W-7 form does not currently have a non-binary option.

---

## Line 6 — Other information

### 6a — Country of citizenship

Country (or countries — list both for dual nationals). Use the formal name (e.g., "United Kingdom" not "UK"; "United States of America" not "US"... but "United States" is fine).

### 6b — Foreign tax identification number

If the applicant has a tax ID from their home country, enter it. Optional but reduces friction; the IRS uses it to cross-reference if a treaty issue arises.

If none, leave blank or enter "None".

### 6c — Type of U.S. visa (if any)

For applicants who entered the U.S. on a visa: enter visa type (F-1, J-1, B-1, B-2, M-1, etc.) and expiration date.

For applicants without a U.S. visa or undocumented residents: leave blank.

### 6d — Identification document(s)

This is where the applicant lists the documents they're submitting to prove identity and foreign status.

| Sub-field | Description |
|-----------|-------------|
| Type | Passport / Birth certificate / National ID card / etc. |
| Issued by | Country (or U.S. state) issuing the document |
| Number | Document number (passport number, etc.) |
| Expiration | Document expiration date (or "N/A" if no expiration) |

If submitting two documents, fill out one row per document. The form has space for two — the applicant can add an attachment if more.

See [`identification-documents.md`](./identification-documents.md) for the 13 acceptable types.

### 6e — Date of entry into the United States

For nonresident aliens: the date of most recent entry to the U.S. on the visa being used. For applicants who never entered the U.S. (e.g., Exception 4 FIRPTA sellers operating from abroad), enter "N/A".

### 6f — Other information

Catchall for additional info:
- Previous ITIN (for renewal applications) — enter the 9-digit ITIN
- IRSN (Internal Revenue Service Number) if the IRS previously assigned one — temporary placeholder, less common today
- Any spouse / dependent linkage info

---

## Line 7 — Signature and date

Applicant signs and dates the form. For minors, a parent or court-appointed guardian signs and indicates relationship.

Phone number for IRS to contact the applicant. Best practice: provide a phone the applicant can answer (mobile preferred over landline; international numbers acceptable).

For minors, the parent/guardian's phone is acceptable.

---

## CAA / AA section (if using one)

If submitting via a Certifying Acceptance Agent or Acceptance Agent:

- AA / CAA prints name, signs, dates
- AA / CAA enters their **AA / CAA tracking number** (8 digits)
- AA / CAA office address and phone

The CAA additionally completes Form W-7 (COA) — Certificate of Accuracy — separately; that goes in the package.

---

## Common field-level errors

1. **Name mismatch between W-7 and identification documents** → rejected. The W-7 name must match exactly. If passport says "JOSE LUIS HERNANDEZ-LOPEZ", the W-7 cannot say "Jose Luis Hernandez Lopez" without the hyphen — it must match.
2. **Date format inconsistency** → use MM/DD/YYYY everywhere on the form (U.S. style)
3. **Mailing address that's a third party** (CPA office, attorney's address) → rejected
4. **Reason code (a-h) and supporting evidence don't match** → rejected
5. **Incomplete Line 6d** (e.g., missing document expiration date) → may be rejected or trigger a CP-566 information request
6. **Foreign date format** (DD/MM/YYYY) on Line 4 → causes confusion; convert to U.S. format

---

## Citation summary

- IRS Form W-7 (latest revision): <https://www.irs.gov/pub/irs-pdf/fw7.pdf>
- IRS Instructions for Form W-7: <https://www.irs.gov/pub/irs-pdf/iw7.pdf>
- IRS Pub 1915: <https://www.irs.gov/pub/irs-pdf/p1915.pdf>
- IRC §6109 — TIN requirements
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance
