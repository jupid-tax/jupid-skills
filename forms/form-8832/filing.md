# Filing Form 8832 (mail / fax playbook)

How an agent equipped with mailing or fax tooling can take a completed Form 8832 draft and actually file it. This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then collect the required signatures, then execute the mailing channel. Form 8832 cannot be e-filed.

---

## Channel decision tree

Form 8832 has only one filing channel: **paper mail to an IRS service center**. Fax is not accepted for Form 8832 (different from Form 2553, which has a fax option for some service centers).

```
User has printer + ability to collect ink signatures + mailing service?
  → USPS Certified Mail with Return Receipt (recommended)
    Use Section 1 below.

User wants overnight / signature-required private delivery?
  → IRS-designated private delivery service per IRC §7502(f)
    (FedEx Priority Overnight, UPS Next Day Air, DHL Express, etc.)
    Use Section 2 below.

User has no scanner / printer / mailing infrastructure?
  → Pause and ask. Form 8832 must be on paper with ink signatures from
    each consenting owner. There is no IRS portal upload for Form 8832.
```

---

## Section 1 — USPS Certified Mail (recommended)

**Why Certified Mail**: IRC §7502 (timely-mailing-as-timely-filing) only applies if the mailing carrier provides a postmark or tracking record. Certified Mail with Return Receipt gives the agent a date-stamped receipt that the IRS treats as the filing date.

### Pre-flight

The agent must have:

- The user's permission to print, sign-collect, and mail Form 8832 on their behalf
- The completed Form 8832 draft from `SKILL.md`
- All required owner signatures (Line 11) — collected in advance, ink on paper
- The IRS service center address (Kansas City or Ogden — see Step 2)
- USPS Certified Mail forms (Form 3800) and Return Receipt cards (Form 3811)
- A printable copy of the latest Form 8832 PDF (revision December 2013 as of 2026-04-29)

### Mailing flow

1. **Download** the latest Form 8832 PDF from <https://www.irs.gov/pub/irs-pdf/f8832.pdf>
2. **Verify the revision date** in the upper-left of the form. As of 2026-04-29 the current revision is December 2013. If a later revision exists, use that and re-verify line numbers against the SKILL.md output template.
3. **Fill the PDF** (either via a fillable-PDF tool like `pypdf` / `pdftk` mapping to stable field names, or print blank and have the user fill by hand from the draft).
4. **Print** the completed form. Single-sided. Letter size. Black ink only.
5. **Collect signatures**:
   - Each owner with an interest on the effective date signs Line 11
   - Print the owner's name and title next to each signature
   - Use a single date for all signatures (the latest signature date controls the filing window)
6. **Assemble the mailing**:
   - Form 8832 (signed)
   - If Part II late relief: reasonable-cause statement and consistent-returns statement, both signed under penalties of perjury
   - If officer/manager signing on behalf of all owners: evidence of authority (operating agreement excerpt, board resolution, or state-law citation)
7. **Determine the service center**:
   - Connecticut, Delaware, DC, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, NH, NJ, NY, NC, Ohio, Pennsylvania, RI, SC, Tennessee, Vermont, Virginia, WV, Wisconsin, or **principal place of business outside the US** → **Kansas City, MO 64999**
   - All other states → **Ogden, UT 84201**
   - Re-verify against the "Where to File" table on Form 8832 page 6 — IRS occasionally consolidates centers
8. **Address the envelope**:
   ```
   Department of the Treasury
   Internal Revenue Service Center
   <Kansas City, MO 64999  |  Ogden, UT 84201>
   ```
9. **Take to USPS**, request **Certified Mail with Return Receipt**:
   - USPS Form 3800 (Certified Mail) — keep the green tracking sticker stub
   - USPS Form 3811 (Return Receipt) — costs more but provides legal proof of delivery
10. **Postmark date** is the filing date for IRC §7502 purposes. Photograph the postmarked sticker before leaving the post office.
11. **Track delivery** at <https://tools.usps.com/go/TrackConfirmAction>. Typical delivery 3–7 business days.
12. **Retain proof** indefinitely:
    - Photocopy of the entire signed Form 8832
    - USPS Certified Mail receipt
    - USPS Return Receipt card (when it returns)
    - Tracking record showing delivery

### Acknowledgment timing

- IRS typically responds within **60 days** by mail
- **CP277 letter** = election accepted; entity is now classified as elected
- **CP278 letter** = election denied (eligibility failure, late without relief, missing consent)
- If 90 days pass with no response, call IRS Business and Specialty Tax Line at **800-829-4933** with the entity's EIN and the certified-mail tracking number

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| CP278 — eligibility failure | Entity is per-se corp / state-law corp | Cannot remedy; entity is permanently classified by §301.7701-2 |
| CP278 — 60-month rule | Re-election within 60 months | Wait out the 60 months OR petition under 50%-ownership-change exception |
| CP278 — missing consent | Owner did not sign Line 11 | Re-collect signatures and re-file; new effective-date window applies |
| CP278 — late, no Part II | Effective date > 75 days back, no late-relief request | File new Form 8832 with Part II under Rev. Proc. 2009-41 |
| No response after 90 days | Lost in IRS mail | Call IRS BST line 800-829-4933 with EIN + tracking number |

---

## Section 2 — Private delivery service (IRC §7502(f))

For users who want overnight delivery or proof of receipt at the service center loading dock.

### IRS-designated private delivery services (as of 2026-04-29)

Per [Notice 2016-30](https://www.irs.gov/irb/2016-19_IRB#NOT-2016-30), updated by subsequent annual notices — verify against the latest IRS-designated PDS list:

- **FedEx**: First Overnight, Priority Overnight, Standard Overnight, 2 Day, International Next Flight Out, International Priority, International Economy
- **UPS**: Next Day Air Early AM, Next Day Air, Next Day Air Saver, 2nd Day Air, 2nd Day Air A.M., Worldwide Express Plus, Worldwide Express
- **DHL Express**: 9:00, 10:30, 12:00, Worldwide, Envelope, Import Express 10:30, Import Express 12:00, Import Express Worldwide

USPS Priority Mail and USPS Express Mail are NOT private delivery services for §7502(f) — they are USPS and use the postmark rule.

### Private delivery addresses (DIFFERENT from USPS)

Private delivery services cannot deliver to the IRS PO Box. Use the IRS street addresses:

- **Kansas City service center**: Internal Revenue Service, 333 W. Pershing Road, Kansas City, MO 64108
- **Ogden service center**: Internal Revenue Service, 1973 Rulon White Blvd., Ogden, UT 84201

**Re-verify these addresses** against the IRS [Submission Processing Center Street Addresses for Private Delivery Service](https://www.irs.gov/filing/submission-processing-center-street-addresses-for-private-delivery-service-pds) page before using.

### Filing date with PDS

Per IRC §7502(f)(2), the date the private delivery service marks on the package is the filing date — same rule as USPS postmark. Retain the PDS shipping label and tracking record.

---

## Section 3 — Cover-letter template (for late-relief filings)

When filing under Rev. Proc. 2009-41 (Part II late relief), include a cover letter on top of the Form 8832 packet. Template:

```
[Entity Name]
[Entity Address]

[Date]

Department of the Treasury
Internal Revenue Service Center
[Kansas City, MO 64999  |  Ogden, UT 84201]

Re: Form 8832 — Late Election Relief Request under Rev. Proc. 2009-41
    Entity: [Name]
    EIN: [XX-XXXXXXX]
    Requested effective date: [MM/DD/YYYY]

Dear Sir or Madam:

[Entity Name], EIN [XX-XXXXXXX], hereby requests entity classification election
relief under Rev. Proc. 2009-41 to be classified as a [association / partnership /
disregarded entity] effective [MM/DD/YYYY].

Enclosed:
  1. Form 8832 with Parts I and II completed and signed
  2. Reasonable-cause statement (Part II, Line 11)
  3. Statement of consistent returns (Part II, Line 12)
  4. [Evidence of officer/manager authority, if applicable]

The entity satisfies the requirements of Rev. Proc. 2009-41:
  - This request is filed within 3 years and 75 days of the requested
    effective date.
  - The entity has filed all required federal tax returns consistent with
    the requested classification (or commits to amend any inconsistent
    returns).
  - The entity has reasonable cause for the late filing, as described in
    the attached statement.

Please direct any questions to the contact person listed on Form 8832 Line 9.

Sincerely,

[Authorized Signer Name]
[Title]
[Phone]
[Email]
```

---

## Section 4 — PDF field-mapping cheat sheet

For agents using `pypdf` or `pdftk` to fill the IRS Form 8832 PDF programmatically, the field names in the December 2013 revision are stable. Run `pdftk f8832.pdf dump_data_fields` once to capture the current field list — fields are typically named like:

- `topmostSubform[0].Page1[0].f1_1[0]` — entity name
- `topmostSubform[0].Page1[0].f1_2[0]` — EIN
- `topmostSubform[0].Page1[0].c1_1[0]` — Box 1(a) checkbox
- `topmostSubform[0].Page1[0].f1_8[0]` — Line 8 effective date

The exact field tree changes when the IRS releases a new revision. Re-run `dump_data_fields` whenever the form revision date changes. Cache the field map per revision.

---

## Section 5 — Submission state machine

After mailing, the entity's election moves through:

1. **Mailed** — postmarked / PDS-marked; this is the filing date
2. **Received by IRS** — typically 3-7 days for USPS, 1-2 for PDS overnight
3. **Under review** — IRS classification unit reviews eligibility, timing, and consents
4. **Accepted** — CP277 letter issued, typically 60 days after receipt
5. **Rejected** — CP278 letter issued with reason code

If the entity has NOT received CP277 or CP278 within 90 days of the postmark:

- Call IRS Business and Specialty Tax Line: 800-829-4933 (M-F 7am-7pm local)
- Have the entity's EIN, USPS or PDS tracking number, and effective date ready
- The agent representative can confirm whether the form is in process or was received

The agent should set a follow-up reminder 60 days post-postmark to check CP277/CP278 status.

---

## Section 6 — Security and consent rules for the agent

These are non-negotiable:

1. **Never mail Form 8832 without explicit user consent** at the moment of mailing. "I authorize you to print, collect signatures from owners, and mail Form 8832 to the IRS on my behalf right now" must be captured.
2. **Never store SSN, EIN, or owner SSNs** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never forge a signature.** Each owner must physically sign Line 11 in ink, OR an officer/manager with documented state-law authority signs on their behalf with the authority document attached.
4. **Always capture mailing confirmations** (USPS Certified receipt, PDS shipping label) as photographs stored under the user's account, not the agent's.
5. **If an eligibility flag fires** (per-se corp, 60-month rule, missing consent), **stop and surface to the user**. Don't paper over the issue and mail anyway — the IRS will reject and the entity loses the desired effective date.
6. **Never advise on the underlying tax strategy** (whether C-corp is worth electing). That's CPA / tax attorney territory. The skill files the form once the user has decided.
