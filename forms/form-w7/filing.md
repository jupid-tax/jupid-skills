# Filing Form W-7 (submission playbook)

How an agent can take a completed Form W-7 application package and submit it via the right channel. Form W-7 cannot be e-filed — it requires physical document submission. The choice of channel matters because it affects (1) whether the applicant must mail original passports, (2) processing time, and (3) error rate.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
Does the applicant have access to a Certifying Acceptance Agent (CAA)?
  → YES, and applicant doesn't want to mail original documents
    → CAA channel (Section 1)
    → CAA reviews originals in person, certifies, sends certified copies to IRS
    → Originals stay with applicant; lower risk
    → Most operationally simple option

Does the applicant want to make an in-person appointment with the IRS?
  → IRS Taxpayer Assistance Center (TAC) (Section 2)
    → Schedule via 844-545-5640
    → Bring originals; IRS staff verifies on the spot
    → No mailing of originals
    → Limited TAC locations; appointment-only
    → Free; good if a TAC is geographically convenient

Does the applicant prefer to mail original documents directly to the IRS?
  → Mail with originals (Section 3)
    → IRS holds originals 60 days, returns by mail
    → Risk: original passport in transit for ~7-11 weeks
    → Free, simple, but high stakes for the applicant

Does the applicant have certified copies from the issuing authority?
  → Mail with certified copies (Section 4)
    → "Certified" = stamped/sealed by the issuing government office
      (e.g., the passport-issuing country's foreign affairs ministry; embassy/consulate of issuing country in the U.S.)
    → NOT a notarized copy from a U.S. notary public
    → Lower risk than mailing originals

Does the applicant have access to an Acceptance Agent (AA, not CAA)?
  → AA channel (Section 5)
    → AA reviews W-7 for completeness but doesn't certify documents
    → Applicant still mails originals or certified copies
    → Less common; AA helps with form prep, not document handling
```

**Recommendation tree**: CAA > TAC > certified copies > originals by mail > AA.

---

## Section 1 — Certifying Acceptance Agent (CAA)

A CAA is an IRS-authorized professional (CPA, EA, attorney, certain financial institutions) who has additional authority beyond a regular Acceptance Agent: they can verify originals in person, certify them, and submit certified copies — so the applicant never has to mail original documents.

### Pre-flight

Agent must have:
- The user's permission to coordinate with a CAA
- The completed W-7 draft from `SKILL.md`
- A list of the applicant's identification documents
- The supporting tax return (if not exception)

### Workflow

1. **Find a CAA**: <https://www.irs.gov/tin/itin/itin-acceptance-agents> — IRS publishes a state-by-state list.
2. **Schedule an appointment** with the CAA. The CAA will need to physically see the original documents (passport, etc.).
3. **Bring to the appointment**:
   - Completed W-7 (signed by applicant)
   - Original identification documents
   - The supporting tax return (signed)
4. **The CAA**:
   - Verifies original documents in person
   - Completes a Form W-7 (COA) — Certificate of Accuracy — signing as a CAA
   - Sends the W-7 + tax return + certified document copies (the CAA's certification, not the originals) to the IRS Austin ITIN Operation
   - Returns originals to the applicant immediately
5. **Wait 7-11 weeks** for IRS processing
6. **Receive CP-565** (assignment letter with new ITIN) at the mailing address on Line 2 of the W-7

### CAA fees

CAAs charge $100-$300+ depending on complexity. Some CAAs are part of larger CPA firms that bundle ITIN service with tax return preparation; others are standalone. The fee is paid by the applicant; the IRS does not charge.

### Why CAA is the recommended option

- Originals stay with applicant (no mail risk)
- CAA does the work of mailing the package correctly
- CAA's certification reduces IRS rejection rate (CAAs have a vested interest in clean submissions)
- For dependents under 18: CAAs can certify originals for the entire family in one visit

### What CAAs cannot do

- Issue an ITIN themselves (only the IRS can)
- Speed up IRS processing
- Override SSN eligibility — if the applicant qualifies for SSN, the CAA must redirect

---

## Section 2 — IRS Taxpayer Assistance Center (TAC)

TACs are physical IRS offices in major cities. A subset of TACs are designated as ITIN-Authentication TACs and can verify W-7 documents in person.

### Pre-flight

- Find a TAC: <https://www.irs.gov/help/contact-your-local-irs-office>
- Confirm the TAC is **ITIN-authentication-capable** (not all TACs are)
- Schedule appointment via 844-545-5640 (TAC scheduling line) — appointments only; no walk-ins
- Schedule 4-8 weeks ahead of time during peak season (Jan-April)

### Workflow

1. **Schedule appointment** at a designated TAC
2. **Bring to the appointment**:
   - Completed W-7 (signed)
   - Original identification documents
   - The supporting tax return (signed)
3. **At the appointment**:
   - IRS staff reviews originals
   - IRS staff verifies and stamps the W-7 application
   - IRS staff returns originals on the spot
   - The W-7 + tax return is submitted internally
4. **Wait 7-11 weeks** for IRS processing
5. **Receive CP-565** at the Line 2 address

### TAC pros

- Free
- Originals returned same day
- IRS staff catches errors before submission
- No need to coordinate with a third party

### TAC cons

- Limited locations (mostly major metros; rural applicants drive long distances)
- Appointments scarce during peak season
- Cannot verify if applicant is uncomfortable speaking English (some TACs have multilingual staff; many do not)

---

## Section 3 — Mail with originals

The applicant mails their original passport (or other ID documents) along with the W-7 and tax return to the IRS Austin ITIN Operation. The IRS holds the originals up to 60 days, then returns them by mail.

### Mailing address

```
Internal Revenue Service
ITIN Operation
P.O. Box 149342
Austin, TX 78714-9342
```

This address is **specific to W-7 submissions**. It is NOT the same as the regular 1040 mailing address. Mailing the package to the regular 1040 address will cause delays of 8+ weeks because the IRS will manually re-route.

### Workflow

1. **Assemble the package**:
   - Form W-7 (signed)
   - Original identification documents (passport is the ideal single document)
   - Federal tax return (if not exception) signed and complete
   - Any supporting evidence for an exception
2. **Make photocopies of every document** for the applicant's records
3. **Use a trackable, signature-on-delivery method** — USPS Priority Mail Express or a private carrier with delivery confirmation (FedEx, UPS). The address above accepts USPS only — for FedEx/UPS, use the **physical** address:

```
Internal Revenue Service
ITIN Operation
3651 S Interregional Hwy 35
Austin, TX 78741
```

4. **Wait 7-11 weeks**
5. **IRS returns originals** by mail (usually 60 days from receipt, separately from the ITIN letter)
6. **Receive CP-565** with new ITIN

### Pros

- Free
- No coordination with third parties
- Works from anywhere globally

### Cons

- Original passport away from applicant for ~7-11 weeks
- Risk of loss in transit (USPS reports ~0.4% package loss; the consequence here is severe)
- IRS sometimes returns originals separately and at different times from the ITIN letter
- Cannot travel internationally during the wait if the passport is the document submitted
- If the IRS rejects (e.g., wrong reason code, document insufficient), originals come back but the applicant must re-apply with corrections

---

## Section 4 — Mail with certified copies

Same flow as Section 3 but with **certified copies** of identification documents instead of originals. The originals stay with the applicant.

### What "certified" means

A certified copy is one that bears the **stamp/seal/certification of the issuing authority** — the same government office or agency that issued the original.

Examples of acceptable certifications:
- Foreign passport: certified by the embassy or consulate of the issuing country (in the U.S. or abroad)
- Foreign birth certificate: certified by the issuing country's vital records office
- U.S. driver's license: certified by the state DMV (relatively rare; most U.S. residents have an SSN already)

**NOT acceptable**:
- A copy notarized by a U.S. notary public — notaries verify signatures, not the authenticity of the underlying document. This is the single most common reason mail-with-certified-copies submissions are rejected.
- A copy stamped by a CPA, attorney, or other professional — only the issuing authority can certify
- A photocopy with no stamp — IRS treats as uncertified

### Workflow

1. Obtain certified copies from each issuing authority:
   - Passport: visit the relevant embassy/consulate; pay the fee (varies by country, typically $20-$50 per document); receive stamped copy
   - Birth certificate: order from issuing vital records agency
2. Assemble the package (W-7 + certified copies + tax return)
3. Mail to IRS Austin ITIN Operation (Section 3 address)
4. Wait 7-11 weeks
5. Receive CP-565

### Pros

- Originals stay with applicant
- Better than mailing originals if travel-restricted

### Cons

- Obtaining certified copies takes time (embassies are slow)
- Costs $20-$100 per document depending on issuing country
- Easy to get rejected if applicant submits notarized copies by mistake (see common mistake #1 in [`references/common-mistakes.md`](./references/common-mistakes.md))

---

## Section 5 — Acceptance Agent (AA, not CAA)

An Acceptance Agent reviews the W-7 for completeness but does NOT certify documents. The applicant still must mail originals or certified copies.

This option is rare today — most professionals are CAAs (which is more useful) or aren't ITIN agents at all. AAs are sometimes embassies, certain financial institutions, or specific government offices in some countries.

### Workflow

1. Find an AA: <https://www.irs.gov/tin/itin/itin-acceptance-agents>
2. Bring W-7 to AA for review and signing
3. AA mails the package to IRS Austin
4. Applicant still must include original or certified-copy documents in the package

### When to use

- Applicant is in a country where a CAA isn't available but an AA is (some embassies are AAs)
- Applicant wants form-prep help but not document certification

### Why not preferred

- Doesn't solve the original-document risk that's the main pain point
- Adds a step without a corresponding benefit

---

## Submission state machine

After submission via any channel:

1. **Received** — IRS Austin logged the package (no notification to applicant)
2. **In process** — IRS staff reviewing W-7 and documents
3. **Approved** — ITIN issued; CP-565 letter mailed
4. **Rejected** — ITIN denied; CP-566 letter mailed with reason code
5. **Information needed** — IRS sends a request for additional info; applicant has 60 days to respond

If 11 weeks have passed with no response, call:
- Inside U.S.: 1-800-908-9982
- International: 267-941-1000

The IRS does **not** confirm receipt by email or text. Applicants must wait for the CP-565 / CP-566 letter, or call to check status.

### Common rejection reasons (CP-566 codes)

- Wrong reason code (a-h) selected
- Document not on the Pub 1915 list of 13 acceptable documents
- Notarized copy submitted instead of certified copy from issuing authority
- Tax return not attached when it should have been
- Mismatched information between W-7 and tax return (different name spelling, different DOB)
- Identity document expired
- For dependents/spouses: missing primary filer info
- Two documents submitted but neither shows foreign status

If rejected, the applicant fixes the issue and resubmits. The IRS does NOT automatically retain the file — the applicant starts over.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never submit a W-7 without explicit user consent** at the moment of submission. "I authorize you to submit Form W-7 on my behalf via [channel]" must be captured.
2. **Never store the applicant's passport number, ITIN, or other ID document numbers** in agent logs, vector stores, or transcripts. Use at preparation time, discard.
3. **Never coordinate with a CAA the applicant has not vetted**. The CAA has access to original documents.
4. **Always advise the applicant to keep photocopies** of every document submitted, in case originals are lost in transit.
5. **Never tell an applicant that ITIN is a substitute for SSN if SSN-eligible**. If there's any chance the applicant qualifies for SSN, redirect to SSA — applying for ITIN when SSN-eligible can later complicate identity records.
6. **Never accept "I think I'm SSN-ineligible"** as a reason to skip Step 1. Verify against the SSA criteria.
