# Filing Form 3520 (paper only)

How an agent equipped with browser/printing tooling helps the user file
Form 3520 with the IRS. As of tax year 2025, **Form 3520 is paper only —
not e-filable**. Treat this as a deterministic mail flow.

The agent must produce a complete `SKILL.md`-format draft *first*, then
move data into the IRS fillable PDF, then assemble and mail.

---

## Channel decision tree

```
User wants to e-file Form 3520?
  → Not supported. The IRS has not opened Form 3520 to e-filing as of 2026.
    Verify status at https://www.irs.gov/forms-pubs/about-form-3520
    If still paper-only, proceed to the paper flow below.

User wants paper filing?
  → This is the only channel. Use Section 1.

User wants to file Form 3520 along with their Form 1040?
  → Form 3520 does NOT attach to Form 1040. It's filed separately to
    Ogden. The 1040 is filed normally (e-file or mail to the filer's state
    service center). See Section 2 for coordination.

User missed the deadline?
  → File late with a reasonable cause statement (IRC §6677(d) /
    §6039F(d)). See Section 3.
```

---

## Section 1 — Paper filing flow

### Pre-flight

Agent must have:

- Completed Form 3520 draft from `SKILL.md` (all applicable Parts)
- Filer's full legal name, SSN/ITIN/EIN exactly as it appears on Form 1040
- Spouse's information if filing a joint Form 3520
- Trust identifying details (name, country, EIN if any) for any Part I/II/III
- Donor identifying details (name, address, country, type) for Part IV
- All currency translations done in advance with documented exchange-rate
  source
- Substitute Form 3520-A if Part II applies and the trust didn't file its
  own (data needed: trust income, expenses, distributions, year-end FMV,
  identification of beneficiaries, signature of US owner)
- The IRS fillable PDF for Form 3520 (latest revision) downloaded from
  https://www.irs.gov/pub/irs-pdf/f3520.pdf
- The IRS fillable PDF for Form 3520-A if substitute is needed:
  https://www.irs.gov/pub/irs-pdf/f3520a.pdf
- Printer, envelope, postage, USPS Certified Mail with Return Receipt slip
- The Ogden mailing address (verify in current Form 3520 instructions)

### Step 1 — Fill the fillable PDF

1. Open Form 3520 PDF in a tool that supports AcroForm fields (Adobe
   Reader, pdftk, pypdf with form support, or browser-based PDF editor)
2. Map every field from the draft to its PDF field name. The IRS uses
   stable field naming on production PDFs (e.g., `f1_1`, `f1_2` for line 1
   sublines). Cache the field map per tax year.
3. Fill identifying info first (page 1 top), then check the Part(s)
   applicable boxes, then fill each applicable Part in order.
4. For Part IV donor table: each row is a separate set of fields. Don't
   leave a row blank between filled rows; fill consecutively.
5. Save as flattened PDF — flatten before printing so checkboxes don't
   shift in print queue.
6. **Do NOT save in Adobe Reader's "Save with form data" mode if the PDF
   will be printed and mailed** — the print can sometimes drop checkbox
   state. Flatten first.

### Step 2 — Fill Form 3520-A (substitute) if Part II applies

If the foreign trust did not file Form 3520-A by March 15:

1. Download Form 3520-A fillable PDF
2. Fill on behalf of the US owner. Check the box at top indicating this is
   a "substitute" 3520-A.
3. The US owner signs in the trustee's signature block (with notation that
   this is a substitute filed by the US owner under Notice 97-34).
4. Attach the completed substitute 3520-A behind the main Form 3520.

### Step 3 — Print the package

Print order (top to bottom):

1. **Form 3520** — all pages, single-sided, full size on letter paper
2. **Substitute Form 3520-A** if applicable
3. **Foreign Grantor Trust Owner Statement** (if Part II — page 3 of 3520-A)
4. **Foreign Nongrantor Trust Beneficiary Statement** (if Part III actual)
5. **Schedule A / B / C of Part III** if used
6. **Trust instrument** — optional but recommended for Part I large transfers
7. **Reasonable cause statement** if filing late

Use a single staple in the upper-left corner. Do not double-side print.
Sign every signature block in **blue ink** (preferred) — black is
acceptable but blue distinguishes the original from a copy.

### Step 4 — Make a complete copy for the user's records

Photocopy the entire signed package before mailing. The IRS does not
return originals, and the user may need to produce the package for state
returns, an IRS notice response, or a future audit. Store digitally and
on paper.

### Step 5 — Mail via USPS Certified Mail with Return Receipt

Mailing address (verify against the current-year Form 3520 instructions —
the IRS shifts service centers periodically):

```
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409
```

Use **USPS Certified Mail with Return Receipt** (Form 3811 green card).
This establishes timely-mailing-as-timely-filing under IRC §7502 and
provides proof of receipt at Ogden. Private delivery services (FedEx, UPS)
also qualify under §7502 for IRS-designated services — see Notice 2016-30
for the current list of designated services and addresses (private
delivery cannot use a P.O. Box; use the IRS street address from the
instructions).

Postmark by **April 15** (or April 18 if 15 falls on a weekend/holiday) for
calendar-year individuals. If the filer extended Form 1040 via Form 4868,
the Form 3520 deadline extends to October 15 automatically — no separate
extension form needed for individuals.

For domestic trusts and estates filing Form 3520, the deadline tracks
Form 1041 (April 15 for calendar-year, 15th day of 4th month after fiscal
year-end) and Form 7004 extends both 1041 and 3520.

### Step 6 — Track delivery

The certified mail tracking number from USPS confirms delivery at Ogden,
typically 5-10 business days after mailing. Save the tracking confirmation
and the returned green card (Form 3811) in the same file as the filed copy.

### Step 7 — Wait for IRS processing

Form 3520 is an information return — the IRS does not send an "accepted"
notice the way it does for 1040 e-files. The first signal of processing
is usually:

- Silence (most common, means no issues identified)
- A CP15 / CP215 / 3520 penalty notice (means the IRS believes the form
  was late or incomplete)
- A letter requesting additional information

If the user receives a penalty notice and they had reasonable cause,
respond with a written reasonable-cause statement within the response
window stated on the notice (typically 30 days). The First-Time Abate
program does NOT apply to §6677 or §6039F penalties (per IRM 20.1.9 — the
IRS treats foreign trust/gift penalties as outside the FTA scope).

---

## Section 2 — Coordination with Form 1040

Form 3520 is filed **separately** from Form 1040, but the timing aligns:

| Filer type           | 1040 due | 3520 due | 3520 extension                                   |
|----------------------|----------|----------|--------------------------------------------------|
| Individual (cal year)| Apr 15   | Apr 15   | Auto with 1040's Form 4868; no separate filing   |
| US person abroad     | Jun 15   | Jun 15   | Auto with the abroad-filer 2-month extension     |
| Domestic trust/estate| Apr 15   | Apr 15   | Form 7004 extends 1041 and 3520 together         |

**Critical**: The 1040 goes to the filer's state service center (or
e-files); the 3520 goes to **Ogden, UT** regardless of state. Don't put
them in the same envelope.

If the user e-files Form 1040 with Form 8938 (foreign financial assets) on
the same trust assets reported on Form 3520, the data should match
exactly. Common mismatch: trust EIN reported on 8938 differs from 3520
because the trust has both an EIN and a country-specific tax ID. Use the
US EIN on both.

---

## Section 3 — Late filing with reasonable cause

If the user is filing Form 3520 after the deadline, attach a written
**reasonable cause statement** signed under penalty of perjury. The
statement should:

1. Identify the form, tax year, and Part(s) being filed
2. State the date the form was due and the date being filed
3. Describe the facts and circumstances that constitute reasonable cause —
   typical successful arguments:
   - Reliance on a tax professional who failed to advise on the filing
     (must show user disclosed all relevant facts to the professional)
   - Serious illness, death in the family, or disaster
   - The filer was unaware they had a foreign trust interest (e.g.,
     learned of an inheritance after the fact; trust was set up by a
     parent without the user's knowledge)
4. Affirm under penalty of perjury

The IRS evaluates reasonable cause case by case. Lack of knowledge of the
filing requirement, by itself, is generally NOT sufficient — the user is
charged with constructive knowledge of US tax law. The strongest cases
combine genuine ignorance of the underlying transaction (not the rule)
with prompt corrective action upon discovery.

For a Streamlined Filing Compliance Procedures (SFCP) submission — when
the user is also amending prior years for foreign income — Form 3520 for
each open year goes in the SFCP package; the agent should not file 3520
piecemeal if SFCP is the chosen path. Refer to a practitioner for SFCP.

---

## Section 4 — Submission state machine

After filing, the form moves through:

1. **Mailed** — postmark date + tracking number
2. **Received** — Ogden processing center records receipt; not externally
   visible
3. **Processed** — IRS ingests the form into IDRS (Integrated Data
   Retrieval System); also not externally visible to the user
4. **Action** — silence (most common), notice of deficiency, or
   penalty assessment

There is no "Where's My 3520" tool. The user can request an account
transcript at https://www.irs.gov/individuals/get-transcript to see if a
3520 module appears for the tax year.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** — capture the user's
   "yes, file this for me" before printing/mailing. The user signs the
   form personally; the agent does not.
2. **Never store SSN, ITIN, or EIN** in agent logs, vector stores, or
   transcripts. Pull at filing time, use, discard.
3. **Never mail the form on the user's behalf without the signed
   original** — the user must wet-ink-sign Form 3520 before it goes in
   the mail.
4. **Always retain a complete copy** of the filed package in the user's
   account, not the agent's.
5. **If anything looks wrong** — donor name doesn't match the user's
   description, currency conversion is off, Part assignments don't fit —
   stop and surface the issue before the package is mailed.

---

## Failure modes

| Symptom                                            | Likely cause                            | Fix                                                                |
|----------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------|
| User receives CP15 penalty notice                  | IRS believes form was late or incomplete| Respond within 30 days with reasonable cause statement             |
| User receives Letter 6291 / 6292                   | IRS questions specific entries          | Respond with documentation; user may need to amend                 |
| Trust didn't file 3520-A; user filed 3520 only     | Substitute 3520-A omitted               | File substitute 3520-A immediately with reasonable cause           |
| Wrong mailing address (e.g., user's state service) | Form went to wrong service center       | IRS may forward; if penalty notice arrives, contest with proof of mailing |
| User filed 3520 attached to 1040                   | Form was attached to 1040 instead of separate | The 1040 service center forwards to Ogden, but timing may slip; verify with transcript |
| Currency conversion challenged                      | Auditor questions exchange rate used    | Provide source documentation (Treasury yearly average page or spot rate publication) |
