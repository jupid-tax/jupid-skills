---
name: form-w7
description: >
  Use this skill when an individual who is not eligible for a U.S. Social
  Security Number needs an Individual Taxpayer Identification Number (ITIN)
  to file a U.S. tax return, claim treaty benefits, or be claimed as a
  dependent / spouse on someone else's return. Triggers on phrases like
  "ITIN application", "Form W-7", "renew ITIN", "tax ID for non-resident
  alien", "ITIN for spouse without SSN", "dependent ITIN", "FIRPTA ITIN",
  or "I need an ITIN to file Form 1040".
  Do NOT use for: SSN-eligible individuals (apply via Form SS-5 with the
  Social Security Administration, not the IRS); business EINs (Form SS-4);
  ITIN-holders who have received an SSN (use the SSN and tell the IRS so it
  updates its records; no W-7); PTIN for tax preparers (Form W-12).
form: Form W-7 (Application for IRS Individual Taxpayer Identification Number)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/fw7.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/iw7.pdf
---

# Form W-7 — Application for IRS Individual Taxpayer Identification Number (ITIN)

This skill produces a complete Form W-7 ITIN application package — including the W-7 itself, the supporting tax return that triggers the ITIN need, the right combination of identification documents, and the correct submission channel (mail, Acceptance Agent, Certifying Acceptance Agent, or in-person at an IRS Taxpayer Assistance Center).

The W-7 is **not a standalone form**. With a few specific exceptions, it must be filed **together with a federal tax return** that requires the ITIN. This is the single most-misunderstood mechanic — applicants frequently mail W-7s by themselves, get rejected, and lose time. This skill optimizes for getting the package right the first time.

The math is mechanical (there's no math on a W-7 itself). The judgment is in **picking the correct reason code (a-h)**, **handling identification documents** (originals are most reliable but lose them in the mail; certified copies must come from the issuing authority, not a notary; CAAs can sidestep mailing originals), **and timing** (when ITIN is needed, the tax return cannot be e-filed; it must be paper-filed with the W-7 attached).

Line map verified against **Form W-7 (Rev. December 2024)** and **Instructions for Form W-7 (Rev. December 2024)**, still the current revisions on irs.gov as of 2026-10-06. Re-check <https://www.irs.gov/forms-pubs/about-form-w-7> for a newer revision before use.

**Companion guide for end users:** [What Is an ITIN and How to Apply (2026): Guide for Non-US Founders](https://jupid.com/blog/what-is-an-itin-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form W-7, ITIN, "Individual Taxpayer Identification Number"
- The user describes a person who needs to file a U.S. tax return but isn't eligible for an SSN: nonresident alien with U.S. income, undocumented resident, dependent or spouse of a U.S. resident/citizen who isn't eligible for SSN, foreign student/scholar with treaty benefits
- The user mentions claiming a non-citizen spouse on a Married Filing Jointly return when the spouse has no SSN
- The user describes a foreign person buying or selling U.S. real estate (FIRPTA §1445 withholding triggers an ITIN need)
- The user has an ITIN that has expired (no use in 3+ years) and needs to renew
- The user is a foreign student or scholar applying for treaty benefits via Form 8233 or Form W-8BEN

Do **not** engage this skill when:

- The person is **eligible for an SSN** — they must apply for an SSN via Form SS-5 with the Social Security Administration, not an ITIN. See <https://www.ssa.gov/forms/ss-5.pdf>. The IRS will not issue an ITIN to anyone eligible for an SSN.
- The user needs an **EIN for a business entity** → Form SS-4, not W-7
- The user is a **paid tax preparer needing a PTIN** → Form W-12, not W-7
- An existing ITIN holder has just received an SSN — they stop using the ITIN, use the SSN, and tell the IRS so it can update its records and credit taxes withheld under the ITIN (IRS "Understanding your CP565 notice" page; out of scope for this skill)

If the user's eligibility for an SSN is ambiguous (e.g., they have DACA status or work authorization), redirect them to verify with the SSA before applying for an ITIN. The IRS will reject Form W-7 applications from anyone the SSA could grant an SSN to.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Applicant's full legal name** (as it appears on identification documents) — both name at birth and current legal name if different
2. **Date of birth** and **place of birth** (city + country)
3. **Country of citizenship** (or countries — dual nationals list both)
4. **Foreign tax ID number** (if the applicant has one in their home country) — optional but reduces friction
5. **Mailing address** — where the IRS will send the ITIN notice and return original documents. Must be where the applicant can receive mail. Foreign address acceptable. No P.O. box owned by a private firm; no P.O. box or "in care of" address if line 3 will show only a country name (Instructions for Form W-7, line 2 and line 3).
6. **Foreign address** — the complete foreign address in the country where the applicant permanently or normally resides, even if it is the same as the mailing address (re-enter it). If the applicant relocated to the U.S. and has no permanent foreign residence, only the country name, except for reason b, which requires a complete foreign address.
7. **Reason for applying** — this is the **reason code** from W-7 boxes (a) through (h). See [`references/reason-codes.md`](./references/reason-codes.md) for a decision tree. The agent **must** identify the right reason code; picking the wrong one is the most common rejection cause.
8. **Identification documents the applicant will submit** — the IRS accepts 13 specific document types per Pub 1915. **Originals or certified copies from the issuing authority.** Notary copies are NOT accepted. See [`references/identification-documents.md`](./references/identification-documents.md).
9. **The federal tax return the W-7 is attached to** (almost always Form 1040 / 1040-NR) — the W-7 is filed *with* the return unless one of Exceptions 1-5 in the instructions' Exceptions Tables applies (the exception is written on the dotted line next to box h; there is no separate exception checkbox).
10. **For dependents/spouses being claimed on someone else's return**: the U.S. citizen/resident alien's full name and SSN or ITIN, the relationship (dependents), and the allowable tax benefit the applicant is claimed for (joint return, head of household, qualifying surviving spouse, AOTC, PTC, child and dependent care credit, or credit for other dependents). No allowable tax benefit and no own return means no ITIN.
11. **Submission channel preference**: mail (originals to Austin TX), Acceptance Agent (AA), Certifying Acceptance Agent (CAA), or in-person at an IRS Taxpayer Assistance Center (TAC)

For ITIN renewals, additionally ask:
- **Existing ITIN number** (9 digits, format `9XX-XX-XXXX`)
- **Has the ITIN been included on a U.S. federal tax return for at least one of the last 3 consecutive tax years?** (If yes, and it was assigned in 2013 or later or was renewed since, no renewal needed)
- **Has the IRS sent a CP48 notice that this ITIN is expiring or has expired?**

---

## Workflow

Execute these steps in order. Each step is a discrete decision the agent must make.

### Step 1 — Confirm SSN ineligibility

Walk the applicant through SSA eligibility:
- Is the applicant a U.S. citizen? → Must use SSN (apply via Form SS-5)
- Is the applicant a U.S. lawful permanent resident (green card)? → Eligible for SSN (apply via Form SS-5)
- Does the applicant have work authorization (e.g., DACA, EAD card, H-1B)? → Eligible for SSN; must apply for SSN first
- Is the applicant a non-resident alien with no work authorization? → Can apply for ITIN
- Is the applicant an undocumented resident with U.S. tax filing obligation? → Can apply for ITIN

If unclear, instruct the user to apply for an SSN first. Do not file a W-7 while an SSN application is pending. If the SSA determines the applicant is not eligible, the SSA denial letter must be attached to the W-7, with or without a tax return (Instructions for Form W-7, "Social security numbers"). Students on F-1, J-1, or M-1 visas who will not work may attach a DSO/RO letter instead (box f).

### Step 2 — Identify the correct reason code (a-h on W-7)

Use [`references/reason-codes.md`](./references/reason-codes.md) to walk through the decision tree. Common cases:

- **(a)** Nonresident alien required to get an ITIN to claim a tax treaty benefit → no return filed; must also check box h and enter Exception 1 or 2 plus treaty country and article
- **(b)** Nonresident alien filing a U.S. federal tax return → typically with Form 1040-NR; line 3 must be a complete foreign address
- **(c)** U.S. resident alien (substantial presence test) filing a U.S. federal tax return → Form 1040; date of entry on line 6d
- **(d)** Dependent of U.S. citizen/resident alien → relationship plus full name and SSN/ITIN of the U.S. citizen/resident alien on the dotted line; claimed for an allowable tax benefit
- **(e)** Spouse of U.S. citizen/resident alien (e.g., joint return) → full name and SSN/ITIN of the U.S. citizen/resident alien on the dotted line
- **(f)** Nonresident alien student, professor, or researcher filing a return or claiming an exception → complete lines 6a, 6c, 6d, 6g; passport with valid U.S. visa; if claiming an exception, also check h
- **(g)** Dependent/spouse of a nonresident alien holding a U.S. visa → attach a copy of the visa; date of entry on line 6d
- **(h)** Other → describe the reason; for an exception enter its designation (e.g., "Exception 3-Mortgage Interest", "Exception 4", "Exception 5, T.D. 9363") on the dotted line

If more than one box applies, check the one that best explains the reason (boxes a and f claiming an exception also take box h). A wrong or unsupported code gets the application suspended (CP566) or rejected (CP567).

### Step 3 — Verify identification documents

The IRS accepts 13 document types (Supporting Documentation table in the W-7 instructions and Pub 1915). **Passport** is the only stand-alone document that proves both identity and foreign status — strongly preferred. If no passport, the applicant must submit at least **two** documents from the table that together prove identity and foreign status.

At least one document must contain a photograph unless the applicant is a dependent under 14 (under 18 if a student). Applicants under 18 without a valid passport must include an original civil birth certificate. Dependents (reason d) must also prove U.S. residency unless they are dependents of U.S. military personnel stationed overseas, or from Canada or Mexico and claimed for a benefit other than the credit for other dependents; a passport without a U.S. date of entry is not stand-alone for them.

**Document submission options**:

| Option | What you submit | Who handles |
|--------|-----------------|-------------|
| Mail originals | Original passport / birth certificate / etc. | IRS Austin returns them within 60 days |
| Mail certified copies | Certified copies from issuing authority (e.g., passport-issuing govt) | IRS Austin |
| Acceptance Agent (AA) | AA helps with the W-7 and mails the package; must submit original documents or certified copies to the IRS | IRS Austin |
| Certifying Acceptance Agent (CAA) | CAA authenticates documents in person, returns them immediately, sends copies with Form W-7 (COA). Cannot authenticate foreign military IDs; for dependents, only passports and birth certificates | IRS Austin |
| IRS Taxpayer Assistance Center (TAC) | Bring originals to in-person appointment (by appointment only, 844-545-5640); for dependents, TACs verify passports, national ID cards, and birth certificates | IRS staff |

CAA is the operationally simplest option — the applicant doesn't risk losing original documents in the mail. Some VITA sites also have CAAs and offer free ITIN service. See [`references/identification-documents.md`](./references/identification-documents.md).

### Step 4 — Determine if the W-7 attaches to a tax return or qualifies for an exception

Default rule: W-7 must be filed **with** a federal tax return that requires the ITIN. The return is paper-filed (cannot e-file when an ITIN is being applied for); the W-7 sits on top of the return packet.

**Exceptions** (W-7 can be filed alone, no tax return attached). These are the five Exceptions Tables in the W-7 instructions:
- **Exception 1**: Passive income—third-party withholding or tax treaty benefits (partnership income, interest, pensions, annuities, rents, royalties, dividends; Forms 1042-S, 1099-INT, 1099-MISC, 8805, Schedule K-1). Not available if the applicant must file a return.
- **Exception 2**: Other income—treaty benefits on wages/honoraria (Form 8233), scholarships/fellowships/grants (with or without a treaty claim), or gambling winnings through a gaming official acting as Acceptance Agent
- **Exception 3**: Mortgage interest—third-party reporting (home mortgage loan on U.S. real property; Form 1098)
- **Exception 4**: Disposition by a foreign person of a U.S. real property interest—third-party withholding (Forms 8288, 8288-A, 8288-B)
- **Exception 5**: Reporting obligations under T.D. 9363 (non-U.S. representative of a foreign corporation who needs an ITIN for its e-filing requirement)

If applying under an exception, attach the documentation the Exceptions Tables require (e.g., Form 8288/8288-A/8288-B plus the sales contract or Closing Disclosure for Exception 4; the page of the partnership agreement showing the EIN and the applicant as partner for Exception 1(a)). See [`references/exceptions.md`](./references/exceptions.md).

### Step 5 — Prepare the supporting tax return (if not exception)

The W-7 is the application; the underlying return is what triggers the ITIN need. For a 1040 filer claiming a dependent without an SSN:

- The dependent's SSN field on Form 1040 is left **blank** (no notation; the IRS writes in the ITIN when it is assigned)
- The box for the allowable tax benefit is checked (e.g., "Credit for other dependents" next to the dependent's name) and the related form is attached (Form 2441, 8863, 8962) — listing a dependent alone is not an allowable tax benefit
- The W-7 is attached to the front of the 1040
- The 1040 cannot be e-filed; mail it to the IRS Austin ITIN Operation (not the regular 1040 address)

For nonresident alien filing 1040-NR with an ITIN application, similar logic applies.

### Step 6 — Fill out the W-7

Walk through every field on the W-7 form. Most fields are straightforward (name, address, DOB, country of citizenship). Critical fields:

- **Reason for applying** (top of form): check the right box (a-h) per Step 2; relationship and the U.S. person's name and SSN/ITIN go on the dotted lines next to boxes d/e
- **Visa information** (Line 6c): U.S. nonimmigrant visa classification, number, and expiration date; otherwise N/A
- **Identification document** (Line 6d): first document only (type, issuer, number, expiration date) plus **date of entry into the United States**; additional documents on an attached sheet
- **Prior ITIN/IRSN** (Line 6e Yes/No, Line 6f number and name it was issued under): required for renewals
- **College/university or company** (Line 6g): box f applicants and business visitors; length of stay

Enter "N/A" in every section that does not apply; do not leave blanks.

See [`references/line-by-line.md`](./references/line-by-line.md) for full guidance.

### Step 7 — Assemble the package

Assemble in this order:

1. Form W-7 (signed)
2. Identification documents (originals OR certified copies OR CAA certifications)
3. Federal tax return (1040 / 1040-NR / etc.) with the SSN area left blank for each ITIN applicant
4. Any supporting evidence for an exception (if Step 4 applied)

### Step 8 — Submit via the chosen channel

See [`filing.md`](./filing.md) for full submission mechanics. Key facts:

- **Mail** to IRS Austin ITIN Operation (different from regular 1040 mailing address)
- **CAA / AA**: applicant brings to professional, who forwards
- **TAC**: applicant brings to in-person IRS appointment

### Step 9 — Wait and track

- Processing time: allow **7 weeks**; **9-11 weeks** if submitted January 15 through April 30 or from overseas (Instructions for Form W-7, "Processing times")
- IRS does **not** confirm receipt by email — applicant waits for a notice: CP565 (ITIN assigned), CP566 (more information needed; reply within 45 days), or CP567 (application rejected)
- If that window passes with no response: call 800-829-1040 (within U.S.) or 267-941-1000 (outside the U.S., not toll-free)

### Step 10 — Use the ITIN

Once issued, the ITIN appears on a CP565 notice. The applicant can use it to:

- File future tax returns
- Open U.S. bank accounts (some banks accept ITIN; verify with bank)
- Claim tax treaty benefits

### Step 11 — Renew if expiring

An ITIN not included on a U.S. federal tax return for 3 consecutive tax years expires on December 31 of the third consecutive tax year. ITINs assigned before 2013 that were never renewed have also expired (the middle-digit expiration waves under the PATH Act are complete). Renew only if the ITIN will be included on a federal tax return; ITINs used only on information returns (e.g., Form 1099) need no renewal. Renewal uses the same Form W-7 with "Renew an existing ITIN" checked, a reason box checked, lines 6e/6f completed, and a tax return attached unless an exception applies.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Top of form — Reason for applying

Check the one box (a-h) that best explains the reason. Box a, and box f when claiming an exception, also require box h with the exception designation. "Renewing an ITIN" is not a valid reason by itself. See [`references/reason-codes.md`](./references/reason-codes.md).

Application type (top right): check "Apply for a new ITIN" or "Renew an existing ITIN" (one box).

### Line 1a/1b — Name

- 1a: Legal name as it appears on identification documents (most authoritative source)
- 1b: Name as it appears on the birth certificate, if different from 1a (e.g., maiden name)

### Lines 2-3 — Address

- Line 2: Mailing address where IRS sends the ITIN notice and returns original documents
- Line 3: Complete foreign address where the applicant permanently or normally resides, even if the same as line 2; country name only if relocated to the U.S. with no foreign residence (complete address required for reason b). No P.O. box or c/o address.

### Lines 4-5 — Birth and identity

- Line 4: Date of birth (MM/DD/YYYY), country of birth (required), city and state or province (optional)
- Line 5: Male / Female

### Line 6 — Other information

- 6a: Country(ies) of citizenship, full names, no abbreviations
- 6b: Foreign tax ID number (if any)
- 6c: U.S. nonimmigrant visa classification, number, and expiration date (attach I-20/I-94 copies if held)
- 6d: First identification document submitted — type box, issued by, number, expiration date — and date of entry into the United States ("Never entered the United States" if none)
- 6e: Previously received an ITIN or IRSN? Yes / No-Don't know
- 6f: Prior ITIN and/or IRSN and the name under which it was issued (required for renewals)
- 6g: College/university or company name, city and state, and length of stay

### Sign and date

Applicant signs (a parent or court-appointed guardian may sign for a dependent under 18; others need Form 2848). Date the application and give a phone number. A spouse cannot sign for a spouse without Form 2848.

### For renewals

Check "Renew an existing ITIN", still check a reason box, answer line 6e "Yes", and enter the previously issued ITIN and name on line 6f. The IRS uses W-7 for both new applications and renewals.

---

## Validation

Before declaring the application package ready, run these checks. Surface anything that fails — don't silently fix.

### Completeness checks

- [ ] All fields on the W-7 filled; "N/A" in every section that does not apply (no blanks)
- [ ] One reason box (a-h) checked; box h also checked with the exception designation when box a, or box f with an exception, is used
- [ ] Identification documents listed on Line 6d match the documents being submitted
- [ ] Mailing address on Line 2 is one the applicant can receive mail at (no private-firm P.O. box)
- [ ] Form is signed and dated
- [ ] Federal tax return (1040 / 1040-NR) is attached if no exception applies
- [ ] Supporting evidence is attached if an exception is claimed

### Document-quality checks

- [ ] Originals or **certified copies from the issuing authority** (NOT notarized copies)
- [ ] Documents are unexpired (or, for certain documents like birth certificates, no expiration)
- [ ] If submitting two documents, one shows identity and one shows foreign status
- [ ] Photo on at least one document unless the applicant is a dependent under 14 (under 18 if a student); original civil birth certificate if under 18 with no passport
- [ ] Dependent (reason d) needing proof of U.S. residency: passport shows a U.S. date of entry, or a U.S. residency document is included
- [ ] Passport number, name, and date of birth on document match what's on Form W-7 (lines 1a, 1b, 4, 6a)

### Reason-code-specific checks

- [ ] Reason **(b)**, **(c)**, **(d)**, **(e)**, **(f)**, or **(g)**: federal tax return is attached unless an exception applies
- [ ] Reason **(a)**: box h also checked with Exception 1 or 2 designation; treaty country and article entered
- [ ] Reason **(d)**: relationship stated; **(d)** or **(e)**: U.S. citizen/resident alien's full name and SSN/ITIN on the dotted line
- [ ] Reason **(f)**: lines 6a, 6c, 6d, 6g complete; passport with valid U.S. visa (not needed if foreign address is in Canada, Mexico, or Bermuda)
- [ ] Reason **(g)**: copy of visa attached; date of entry on line 6d
- [ ] Reason **(h)**: reason described, or exception designation entered (e.g., "Exception 4")

### Submission checks

- [ ] If mailing originals: applicant accepts that documents come back within 60 days of processing
- [ ] If using a CAA or AA: the "Acceptance Agent's Use ONLY" block has signature, name and title, company, EIN/PTIN, and eight-digit office code; a CAA attaches Form W-7 (COA)
- [ ] If using a TAC: in-person appointment is scheduled in advance via 844-545-5640

### Renewal checks

- [ ] If renewing: line 6e "Yes" and previous ITIN plus the name it was issued under entered on line 6f (9 digits, `9XX-XX-XXXX` format)
- [ ] If renewing: tax return on which the ITIN will be used is attached (or exception applies)
- [ ] If the ITIN was assigned before 2013 and never renewed: treat it as expired

---

## Output format

The agent's deliverable is a **complete application package draft** the user can transcribe to the actual W-7, attach to their tax return, and submit.

```markdown
# Form W-7 ITIN Application — DRAFT

## Applicant identification
- **Full legal name**: <First> <Middle> <Last>
- **Name at birth (if different)**: <if applicable>
- **Date of birth**: MM/DD/YYYY
- **Place of birth**: <City, State, Country>
- **Country of citizenship**: <country>
- **Foreign tax ID**: <if any>

## Reason for applying
- Box checked: (a / b / c / d / e / f / g / h)
- Specific basis: <explain>
- For (d) / (e): U.S. citizen/resident alien name <name> and SSN/ITIN <XXX-XX-XXXX>; for (d) relationship <child / parent / etc.>
- For (a) / (f) / (h): exception designation <e.g., Exception 2c>; treaty country <country>, article <number>

## Mailing and foreign address
- **Mailing address**: <street, city, state, ZIP, country>
- **Foreign address (if different)**: <street, city, country>

## Visa information (if applicable)
- Visa type: <e.g., F-1, B-1, J-1, none>
- Expiration: <MM/DD/YYYY or N/A>
- Date of entry into U.S.: <MM/DD/YYYY or N/A>

## Identification documents (Line 6d)
| Document type | Issuing country | ID number | Expiration |
|---------------|-----------------|-----------|------------|
| Passport | <country> | <number> | <date> |
| (Second document if no passport) | ... | ... | ... |

## Submission channel
- Channel: <Mail originals / Mail certified copies / CAA / AA / TAC>
- Submission address: <Austin TX ITIN Operation — see filing.md>
- Expected processing time: 7 weeks (9-11 weeks Jan 15-Apr 30 or from overseas)

## Federal tax return attached (if not under exception)
- Form: <1040 / 1040-NR / etc.>
- Tax year: <YYYY>
- SSN field for each ITIN applicant: left blank
- Allowable tax benefit claimed for each spouse/dependent applicant: <joint return / HOH / QSS / AOTC / PTC / CDCC / ODC>

## Exception claim (if applicable)
- Exception #: <1 / 2 / 3 / 4 / 5>
- Supporting evidence attached: <document name>

## Validation summary
- Completeness: all required fields filled / <list missing>
- Documents: originals OR certified copies from issuing authority / <flag if notarized>
- Reason code: <code> matches the situation
- Submission channel: chosen and applicant aware of timing

## Sources cited in this draft
- IRS Form W-7 (Rev. December 2024)
- IRS Instructions for Form W-7 (Rev. December 2024)
- IRS Pub 1915 — Understanding Your IRS ITIN
- IRC §6109 (TIN requirements)
- Treas. Reg. §301.6109-1(d)(3)
```

The draft is **not** the final filed application. The user still has to physically sign the W-7 and prepare the documents. The deliverable's value is that every field is mapped, every required document is identified, and the submission channel is confirmed.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete reference for every line on Form W-7
- [`references/reason-codes.md`](./references/reason-codes.md) — Decision tree for reason codes (a-h) — picking the wrong one is the most common rejection cause
- [`references/identification-documents.md`](./references/identification-documents.md) — The 13 acceptable documents per Pub 1915, certification rules, and CAA mechanics
- [`references/exceptions.md`](./references/exceptions.md) — When the W-7 can be filed alone (without an attached tax return)
- [`filing.md`](./filing.md) — Submission playbook: mail vs. CAA vs. AA vs. TAC, addresses, timing, status checking

Renewal and expiration rules are in Step 11 above and in [`examples/itin-renewal.md`](./examples/itin-renewal.md); field-level mistakes are listed at the end of [`references/line-by-line.md`](./references/line-by-line.md).

## Examples

End-to-end worked W-7 packages. Use these as patterns when the user's situation is similar.

- [`examples/spouse-mfj.md`](./examples/spouse-mfj.md) — Foreign spouse of a U.S. citizen filing MFJ — Form W-7 attached to 1040, reason code (e)
- [`examples/firpta-real-estate.md`](./examples/firpta-real-estate.md) — Foreign buyer of U.S. rental property with a U.S. mortgage — Exception 3 (box h), no 1040 needed now; Form 8288-B and Exception 4 context for the later sale
- [`examples/itin-renewal.md`](./examples/itin-renewal.md) — Existing ITIN expired due to 3 years of non-use — renewal with current-year tax return

## Sources

Authoritative sources used by this skill. Re-verify each year against the IRS site.

- [Form W-7](https://www.irs.gov/pub/irs-pdf/fw7.pdf) — the application form
- [Instructions for Form W-7](https://www.irs.gov/pub/irs-pdf/iw7.pdf) — line-by-line guidance, reason codes, exceptions
- [About Form W-7](https://www.irs.gov/forms-pubs/about-form-w-7) — IRS landing page
- [Publication 1915](https://www.irs.gov/pub/irs-pdf/p1915.pdf) — Understanding Your IRS Individual Taxpayer Identification Number
- [Publication 519](https://www.irs.gov/publications/p519) — U.S. Tax Guide for Aliens (residency rules, treaty benefits)
- [ITIN landing page](https://www.irs.gov/tin/itin/individual-taxpayer-identification-number-itin) — current ITIN program info
- [ITIN Acceptance Agent Program](https://www.irs.gov/tin/itin/itin-acceptance-agents) — find a CAA / AA
- [How to apply for an ITIN](https://www.irs.gov/individuals/how-do-i-apply-for-an-itin) — addresses, in-person options, processing times, CP565/CP566/CP567
- [How to renew an ITIN](https://www.irs.gov/individuals/itin-expiration-faqs) — expiration and renewal rules
- [ITIN supporting documents](https://www.irs.gov/tin/itin/itin-supporting-documents) — 13 documents, proof of U.S. residency for dependents, certified copies
- [Form W-7 (COA)](https://www.irs.gov/pub/irs-pdf/fw7coa.pdf) — Certificate of Accuracy used by CAAs (Aug. 2025)
- IRC §6109 — Identifying numbers (TIN requirements)
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance rules
- IRC §1445 — FIRPTA withholding (relevant for Exception 4)
- IRC §6050H — Mortgage interest information reporting, Form 1098 (relevant for Exception 3)
- T.D. 9363 — e-filing requirement behind Exception 5
- PATH Act of 2015 (Pub. L. 114-113) — ITIN expiration rules

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship or attorney-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations — especially those involving treaty benefits, FIRPTA withholding amounts, or ITIN-to-SSN conversions — warrant a licensed tax professional or immigration attorney's review.
