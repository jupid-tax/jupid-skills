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
  ITIN-holders who become SSN-eligible (rescind ITIN — see references);
  PTIN for tax preparers (Form W-12).
form: Form W-7 (Application for IRS Individual Taxpayer Identification Number)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/fw7.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/iw7.pdf
---

# Form W-7 — Application for IRS Individual Taxpayer Identification Number (ITIN)

This skill produces a complete Form W-7 ITIN application package — including the W-7 itself, the supporting tax return that triggers the ITIN need, the right combination of identification documents, and the correct submission channel (mail, Acceptance Agent, Certifying Acceptance Agent, or in-person at an IRS Taxpayer Assistance Center).

The W-7 is **not a standalone form**. With a few specific exceptions, it must be filed **together with a federal tax return** that requires the ITIN. This is the single most-misunderstood mechanic — applicants frequently mail W-7s by themselves, get rejected, and lose time. This skill optimizes for getting the package right the first time.

The math is mechanical (there's no math on a W-7 itself). The judgment is in **picking the correct reason code (a-h)**, **handling identification documents** (originals are most reliable but lose them in the mail; certified copies must come from the issuing authority, not a notary; CAAs can sidestep mailing originals), **and timing** (when ITIN is needed, the tax return cannot be e-filed; it must be paper-filed with the W-7 attached).

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
- An existing ITIN holder has just received an SSN — they should **rescind the ITIN** (write to the IRS Austin TX ITIN Operation — out of scope for this skill, see [`references/itin-rescission.md`](./references/itin-rescission.md))

If the user's eligibility for an SSN is ambiguous (e.g., they have DACA status or work authorization), redirect them to verify with the SSA before applying for an ITIN. The IRS will reject Form W-7 applications from anyone the SSA could grant an SSN to.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Applicant's full legal name** (as it appears on identification documents) — both name at birth and current legal name if different
2. **Date of birth** and **place of birth** (city + country)
3. **Country of citizenship** (or countries — dual nationals list both)
4. **Foreign tax ID number** (if the applicant has one in their home country) — optional but reduces friction
5. **Mailing address** — where the IRS will send the ITIN. Cannot be a third party's address (no CPA office, no relative). Must be where applicant actually receives mail. Foreign address acceptable.
6. **Foreign address** if different from mailing address — for the W-7 record
7. **Reason for applying** — this is the **reason code** from W-7 boxes (a) through (h). See [`references/reason-codes.md`](./references/reason-codes.md) for a decision tree. The agent **must** identify the right reason code; picking the wrong one is the most common rejection cause.
8. **Identification documents the applicant will submit** — the IRS accepts 13 specific document types per Pub 1915. **Originals or certified copies from the issuing authority.** Notary copies are NOT accepted. See [`references/identification-documents.md`](./references/identification-documents.md).
9. **The federal tax return the W-7 is attached to** (almost always Form 1040 / 1040-NR) — the W-7 is filed *with* the return, with one exception list (treaty benefits, certain Schedule K-1 situations — see exception checkbox on W-7).
10. **For dependents/spouses being claimed on someone else's return**: the primary filer's name, SSN, and the relationship
11. **Submission channel preference**: mail (originals to Austin TX), Acceptance Agent (AA), Certifying Acceptance Agent (CAA), or in-person at an IRS Taxpayer Assistance Center (TAC)

For ITIN renewals, additionally ask:
- **Existing ITIN number** (9 digits, format `9XX-XX-XXXX`)
- **Has the ITIN been used on any tax return in the last 3 years?** (If yes and not expired by IRS notice, no renewal needed)
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

If unclear, instruct the user to apply for an SSN first; if SSA denies, the denial letter is evidence supporting an ITIN application.

### Step 2 — Identify the correct reason code (a-h on W-7)

Use [`references/reason-codes.md`](./references/reason-codes.md) to walk through the decision tree. Common cases:

- **(a)** Nonresident alien required to file U.S. tax return → typically with Form 1040-NR
- **(b)** U.S. resident alien filing U.S. tax return → typically Form 1040
- **(c)** Dependent of U.S. citizen/resident alien → name and SSN of primary filer required
- **(d)** Spouse of U.S. citizen/resident alien (e.g., MFJ filing) → name and SSN of primary filer required
- **(e)** Nonresident alien student, professor, or researcher claiming treaty exemption → check exceptions list
- **(f)** Nonresident alien needing ITIN to claim treaty benefits → typically with Form 8233 or W-8BEN; W-7 may be filed without a 1040
- **(g)** Dependent/spouse of nonresident alien holding U.S. visa → less common
- **(h)** Other (specify) — for unusual cases (e.g., FIRPTA seller, beneficiary of trust)

Picking the wrong code → automatic rejection. The instructions list specific evidence required for each code.

### Step 3 — Verify identification documents

The IRS accepts 13 document types (Pub 1915, Table 1). **Passport** is the only single document that proves both identity and foreign status — strongly preferred. If no passport, the applicant must submit **two** documents: one for identity, one for foreign status (with overlap allowed if a single document does both).

For dependents (under 18), at least one document must contain a photo (waived if the dependent is under 6 and accompanied by a primary medical/school record).

**Document submission options**:

| Option | What you submit | Who handles |
|--------|-----------------|-------------|
| Mail originals | Original passport / birth certificate / etc. | IRS Austin holds 60 days, returns by mail |
| Mail certified copies | Certified copies from issuing authority (e.g., passport-issuing govt) | IRS Austin |
| Acceptance Agent (AA) | AA reviews originals in person, mails copies + W-7 to IRS | IRS Austin |
| Certifying Acceptance Agent (CAA) | CAA reviews originals in person, certifies, sends certified copies to IRS (originals stay with applicant) | IRS Austin |
| IRS Taxpayer Assistance Center (TAC) | Bring originals to in-person appointment | IRS staff |

CAA is the operationally simplest option — the applicant doesn't risk losing original documents in the mail. See [`references/identification-documents.md`](./references/identification-documents.md).

### Step 4 — Determine if the W-7 attaches to a tax return or qualifies for an exception

Default rule: W-7 must be filed **with** a federal tax return that requires the ITIN. The return is paper-filed (cannot e-file when an ITIN is being applied for); the W-7 sits on top of the return packet.

**Exceptions** (W-7 can be filed alone, no tax return attached). These are listed on the W-7 instructions, including:
- **Exception 1**: Third-party withholding on passive income (Form 1042-S, etc.)
- **Exception 2**: Other income (including treaty-exempt scholarship)
- **Exception 3**: Mortgage interest reporting (for U.S. real estate buyers needing ITIN for §6045 reporting)
- **Exception 4**: §1445 FIRPTA withholding (foreign sellers of U.S. real estate)
- **Exception 5**: Reporting under §6038A (foreign-owned U.S. corporations)

If applying under an exception, attach the supporting evidence (e.g., the FIRPTA closing statement, the K-1 showing distributable share). See [`references/exceptions.md`](./references/exceptions.md).

### Step 5 — Prepare the supporting tax return (if not exception)

The W-7 is the application; the underlying return is what triggers the ITIN need. For a 1040 filer claiming a dependent without an SSN:

- The dependent's SSN field on Form 1040 is left **blank**
- A note in the dependent space says "ITIN applied for"
- The W-7 is on top of the 1040 packet
- The 1040 cannot be e-filed; mail it to the IRS Austin ITIN Operation (not the regular 1040 address)

For nonresident alien filing 1040-NR with an ITIN application, similar logic applies.

### Step 6 — Fill out the W-7

Walk through every field on the W-7 form. Most fields are straightforward (name, address, DOB, country of citizenship). Critical fields:

- **Reason for applying** (top of form): check the right box (a-h) per Step 2
- **Visa information** (Line 6c): if applicant has a U.S. visa, enter type and expiration; otherwise blank
- **Identification document type** (Line 6d): which document(s) the applicant is submitting
- **Date of entry into U.S.** (Line 6e): for nonresident aliens; otherwise N/A
- **Other information** (Line 6f): any dependent / spouse claim relationships

See [`references/line-by-line.md`](./references/line-by-line.md) for full guidance.

### Step 7 — Assemble the package

Assemble in this order:

1. Form W-7 (signed)
2. Identification documents (originals OR certified copies OR CAA certifications)
3. Federal tax return (1040 / 1040-NR / etc.) with "ITIN applied for" written where SSN would go
4. Any supporting evidence for an exception (if Step 4 applied)

### Step 8 — Submit via the chosen channel

See [`filing.md`](./filing.md) for full submission mechanics. Key facts:

- **Mail** to IRS Austin ITIN Operation (different from regular 1040 mailing address)
- **CAA / AA**: applicant brings to professional, who forwards
- **TAC**: applicant brings to in-person IRS appointment

### Step 9 — Wait and track

- Processing time: **7-11 weeks** (peak season Jan-April: longer; summer: shorter)
- IRS does **not** confirm receipt by email — applicant must wait for the assignment letter (CP-565 with new ITIN, or CP-566 with rejection + reason)
- If 11 weeks passes with no response: call 1-800-908-9982 (within U.S.) or 267-941-1000 (international)

### Step 10 — Use the ITIN

Once issued, the ITIN appears on a CP-565 letter. The applicant can use it to:

- File future tax returns
- Open U.S. bank accounts (some banks accept ITIN; verify with bank)
- Claim tax treaty benefits

### Step 11 — Renew if expiring

ITINs expire after **3 years of non-use** on a tax return. Also, ITINs with middle digits 70-87 were systematically expired by IRS notice (CP48) in 2016-2019; verify if the applicant's middle digits fall in that range. Renewal uses the same Form W-7 with the renewal box checked.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Top of form — Reason for applying

Check **exactly one** box (a-h). If multiple seem to apply, pick the most specific. See [`references/reason-codes.md`](./references/reason-codes.md).

For renewals: also check the "Renew an existing ITIN" box at the top.

### Line 1a/1b — Name

- 1a: Name as it appears on identification documents (most authoritative source)
- 1b: Name at birth if different (e.g., maiden name)

### Lines 2-3 — Address

- Line 2: Mailing address where IRS sends correspondence and the ITIN letter
- Line 3: Foreign address (home country); leave blank if mailing address is the foreign address

### Lines 4-5 — Birth and identity

- Line 4: Date of birth (MM/DD/YYYY) and city/state/country of birth
- Line 5: Gender

### Line 6 — Identifying information

- 6a: Country of citizenship (or list multiple if dual)
- 6b: Foreign tax ID number (optional)
- 6c: U.S. visa information (type, expiration date) — only if applicable
- 6d: Identification document(s) submitted — type, issuing country, ID number, expiration date
- 6e: Date of entry into U.S. (nonresident aliens only)
- 6f: Any other relevant information (e.g., previous ITIN if renewing)

### Sign and date

Applicant signs (or parent/guardian signs for a minor). Date the application. Phone number for IRS contact (must be one IRS can reach the applicant on).

### For renewals

Check the "Renew" box and provide the previously issued ITIN. The IRS uses W-7 for both new applications and renewals.

---

## Validation

Before declaring the application package ready, run these checks. Surface anything that fails — don't silently fix.

### Completeness checks

- [ ] All required fields on the W-7 filled (no blank required lines)
- [ ] One and only one reason code (a-h) checked at the top
- [ ] Identification documents listed on Line 6d match the documents being submitted
- [ ] Mailing address on Line 2 is one the applicant can receive mail at (not a third-party office)
- [ ] Form is signed and dated
- [ ] Federal tax return (1040 / 1040-NR) is attached if no exception applies
- [ ] Supporting evidence is attached if an exception is claimed

### Document-quality checks

- [ ] Originals or **certified copies from the issuing authority** (NOT notarized copies)
- [ ] Documents are unexpired (or, for certain documents like birth certificates, no expiration)
- [ ] If submitting two documents, one shows identity and one shows foreign status
- [ ] If applicant is a dependent: photo on at least one document (or under-6 exemption applies)
- [ ] Passport number, name, and date of birth on document match what's on Form W-7

### Reason-code-specific checks

- [ ] Reason **(a)** or **(b)**: federal tax return is attached
- [ ] Reason **(c)** or **(d)**: primary filer's name and SSN are listed; relationship is stated
- [ ] Reason **(e)** or **(f)**: visa info on Line 6c is complete; treaty article cited if treaty benefit claimed
- [ ] Reason **(h)**: applicant explained the "Other" basis specifically

### Submission checks

- [ ] If mailing originals: applicant accepts that documents are away from them for ~7-11 weeks
- [ ] If using a CAA: the CAA's name, ITIN, and signature are on the W-7
- [ ] If using a TAC: in-person appointment is scheduled in advance via 844-545-5640

### Renewal checks

- [ ] If renewing: previous ITIN entered correctly (9 digits, `9XX-XX-XXXX` format)
- [ ] If renewing: tax return for the year the ITIN is being used is attached (or exception applies)
- [ ] If middle digits 70-87: applicant aware of the systematic expiration cycle

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
- For (c) / (d): primary filer name <name> and SSN <XXX-XX-XXXX>; relationship <child / spouse / etc.>

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
- Expected processing time: 7-11 weeks

## Federal tax return attached (if not under exception)
- Form: <1040 / 1040-NR / etc.>
- Tax year: <YYYY>
- Note on dependent/spouse SSN field: "ITIN applied for"

## Exception claim (if applicable)
- Exception #: <1 / 2 / 3 / 4 / 5>
- Supporting evidence attached: <document name>

## Validation summary
- Completeness: all required fields filled / <list missing>
- Documents: originals OR certified copies from issuing authority / <flag if notarized>
- Reason code: <code> matches the situation
- Submission channel: chosen and applicant aware of timing

## Sources cited in this draft
- IRS Form W-7 (latest revision)
- IRS Instructions for Form W-7
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
- [`references/itin-renewal.md`](./references/itin-renewal.md) — Renewal mechanics, expiration triggers (middle digits 70-87, 3 years non-use), CP48 notices
- [`references/itin-rescission.md`](./references/itin-rescission.md) — When an ITIN holder gets an SSN — how to rescind the ITIN and consolidate tax records
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with citations
- [`filing.md`](./filing.md) — Submission playbook: mail vs. CAA vs. AA vs. TAC, addresses, timing, status checking

## Examples

End-to-end worked W-7 packages. Use these as patterns when the user's situation is similar.

- [`examples/spouse-mfj.md`](./examples/spouse-mfj.md) — Foreign spouse of U.S. resident alien filing MFJ — Form W-7 attached to 1040, reason code (d)
- [`examples/firpta-real-estate.md`](./examples/firpta-real-estate.md) — Foreign seller of U.S. real estate needing ITIN for §1445 FIRPTA withholding — Exception 4, no 1040 needed
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
- IRC §6109 — Identifying numbers (TIN requirements)
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance rules
- IRC §1445 — FIRPTA withholding (relevant for Exception 4)
- IRC §6045 — Information returns (relevant for Exception 3)
- PATH Act of 2015 (Pub. L. 114-113) — ITIN expiration rules

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship or attorney-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations — especially those involving treaty benefits, FIRPTA withholding amounts, or ITIN-to-SSN conversions — warrant a licensed tax professional or immigration attorney's review.
