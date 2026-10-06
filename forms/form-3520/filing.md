# Filing Form 3520 (mail)

How an agent equipped with browser/printing tooling helps the user file
Form 3520 with the IRS. The Instructions for Form 3520 (Rev. December
2025) give only a mailing address and describe no electronic filing
channel. Treat this as a deterministic mail flow.

The agent must produce a complete `SKILL.md`-format draft *first*, then
move data into the IRS fillable PDF, then assemble and mail.

---

## Channel decision tree

```
User wants to e-file Form 3520?
  → The current instructions describe no e-file channel (only the Ogden
    address). Re-check https://www.irs.gov/forms-pubs/about-form-3520;
    if still mail-only, proceed to the paper flow below.

User wants paper filing?
  → This is the only channel. Use Section 1.

User wants to file Form 3520 along with their Form 1040?
  → Form 3520 does NOT attach to Form 1040. It's filed separately to
    Ogden. The 1040 is filed normally (e-file or mail to the filer's state
    service center). See Section 2 for coordination.

User missed the deadline?
  → File late with a reasonable cause statement (IRC §6677(d) /
    §6039F(c)(2)). See Section 3.
```

---

## Section 1 — Paper filing flow

### Pre-flight

Agent must have:

- Completed Form 3520 draft from `SKILL.md` (all applicable Parts)
- Filer's full legal name, SSN/ITIN/EIN exactly as it appears on Form 1040
- Spouse's information if filing a joint Form 3520
- Trust identifying details (name, country, EIN if any) for any Part I/II/III
- For Part IV: each gift's date, description, FMV (line 54); for foreign
  corporation/partnership donors also name, address, TIN, type (line 55)
- All currency translations done in advance with documented exchange-rate
  source
- Substitute Form 3520-A if Part II applies and the trust didn't file its
  own (data needed: trust income, expenses, distributions, balance sheet,
  owners and beneficiaries; Owner Statement pages 3–4 and Beneficiary
  Statement page 5; signature of US owner)
- Line 1j statement if the user lives and works abroad (June 15 due date)
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
4. For the Part IV tables (lines 54 and 55): each row is a separate set of
   fields. Don't leave a row blank between filled rows; fill
   consecutively; use an attached statement if more rows are needed.
5. Save as flattened PDF — flatten before printing so checkboxes don't
   shift in print queue.
6. **Do NOT save in Adobe Reader's "Save with form data" mode if the PDF
   will be printed and mailed** — the print can sometimes drop checkbox
   state. Flatten first.

### Step 2 — Fill Form 3520-A (substitute) if Part II applies

If the foreign trust did not file Form 3520-A by March 15:

1. Download Form 3520-A fillable PDF
2. Fill on behalf of the US owner, to the best of the owner's ability.
   Check the "Substitute Form 3520-A" box at the top.
3. The US owner signs and dates it, entering the owner's name and TIN on
   the "Title" line of the signature box (Instructions for Form 3520-A,
   Who Must Sign).
4. Attach the completed substitute 3520-A (with the Owner Statement,
   pages 3–4, and Beneficiary Statement, page 5) to the main Form 3520,
   and send copies of those statements to the U.S. owners and U.S.
   beneficiaries by the Form 3520 due date.

### Step 3 — Print the package

Print order (top to bottom):

1. **Form 3520** — all pages, single-sided, full size on letter paper
2. **Substitute Form 3520-A** if applicable
3. **Foreign Grantor Trust Owner Statement** (if Part II and the trust
   filed — pages 3–4 of Form 3520-A)
4. **Foreign Grantor or Nongrantor Trust Beneficiary Statement** (if line
   29 or 30 is "Yes")
5. **Form 4970** worksheet (if Part III Schedule C is used) and the line 32
   explanation (Schedule A)
6. **Loan / sale documents and trust documents** required by lines 11b,
   14, and 18 (only the updates if attached within the previous 3 years)
7. **Line 1j statement** (if living and working abroad)
8. **Reasonable cause statement** if filing late

Use a single staple in the upper-left corner. Do not double-side print.
Sign and date every signature block (the instructions accept
e-signatures). Only a complete Form 3520 with all required attachments is
considered timely filed.

### Step 4 — Make a complete copy for the user's records

Photocopy the entire signed package before mailing. The IRS does not
return originals, and the user may need to produce the package for state
returns, an IRS notice response, or a future audit. Store digitally and
on paper.

### Step 5 — Mail via USPS Certified Mail with Return Receipt

Mailing address (Instructions for Form 3520, Rev. December 2025, When and
Where To File; re-check each year):

```
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409
```

Use **USPS Certified Mail with Return Receipt**. This gives proof of
timely mailing under IRC §7502 and proof of receipt. The address is a P.O.
box, which private delivery services cannot deliver to; the Form 3520
instructions give no street address, so use USPS.

Postmark by **April 15** for calendar-year individuals (the next business
day if April 15 is a Saturday, Sunday, or legal holiday). June 15 if the
user lives and works outside the United States and Puerto Rico (line 1j
statement attached). If the user was granted an extension for the income
tax return (e.g., Form 4868), Form 3520 is due October 15: check line 1k
and enter the extension's form number.

For a U.S. decedent or an estate, the 15th day of the 4th month after the
decedent's last tax year or the estate's tax year, or the 15th day of the
10th month if the income tax return was extended.

### Step 6 — Track delivery

The certified mail tracking number from USPS confirms delivery at Ogden,
typically 5-10 business days after mailing. Save the tracking confirmation
and the returned green card (Form 3811) in the same file as the filed copy.

### Step 7 — Wait for IRS processing

Form 3520 is an information return — the IRS does not send an "accepted"
notice the way it does for 1040 e-files. The first signal of processing
is usually:

- Silence (most common, means no issues identified)
- A penalty notice (the IRS believes the form was late or incomplete)
- A letter requesting additional information

If the user receives a penalty notice and they had reasonable cause,
respond with a written reasonable-cause statement by the deadline stated
on the notice. Whether any administrative waiver (such as first-time
abatement) can apply to a §6677 or §6039F penalty is a question for the
practitioner; this skill does not rely on it.

---

## Section 2 — Coordination with Form 1040

Form 3520 is filed **separately** from Form 1040, but the timing aligns:

| Filer type           | 3520 due | 3520 extension                                   |
|----------------------|----------|--------------------------------------------------|
| Individual (cal year)| Apr 15   | Oct 15 if the income tax return was extended (check line 1k) |
| US citizen/resident living and working abroad | Jun 15 (line 1j statement) | Oct 15 if the income tax return was extended |
| U.S. decedent / estate | 15th day of 4th month after the tax year | 15th day of 10th month if the income tax return was extended |

**Critical**: The 1040 goes to the filer's state service center (or
e-files); the 3520 goes to **Ogden, UT** regardless of state. Don't put
them in the same envelope.

If the user files Form 8938, assets reported on a timely Form 3520 are
"excepted specified foreign financial assets": count the Form 3520 on
Form 8938 Part IV, line 15, and check item C on Form 3520 (Instructions
for Form 3520, Item C; Instructions for Form 8938, Duplicative
reporting).

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

There is no "Where's My 3520" tool. Keep the certified-mail receipt and
tracking record as proof of filing.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** — capture the user's
   "yes, file this for me" before printing/mailing. The user signs the
   form personally; the agent does not.
2. **Never store SSN, ITIN, or EIN** in agent logs, vector stores, or
   transcripts. Pull at filing time, use, discard.
3. **Never mail the form on the user's behalf without the user's
   signature** — the user signs Form 3520 (and any substitute 3520-A)
   personally before it goes in the mail.
4. **Always retain a complete copy** of the filed package in the user's
   account, not the agent's.
5. **If anything looks wrong** — donor name doesn't match the user's
   description, currency conversion is off, Part assignments don't fit —
   stop and surface the issue before the package is mailed.

---

## Failure modes

| Symptom                                            | Likely cause                            | Fix                                                                |
|----------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------|
| User receives a penalty notice                     | IRS believes form was late or incomplete| Respond by the notice deadline with a reasonable cause statement   |
| User receives a letter questioning entries         | IRS questions specific entries          | Respond with documentation; user may need to amend                 |
| Trust didn't file 3520-A; user filed 3520 only     | Substitute 3520-A omitted               | File substitute 3520-A immediately with reasonable cause           |
| Wrong mailing address (e.g., user's state service) | Form went to wrong service center       | IRS may forward; if penalty notice arrives, contest with proof of mailing |
| User filed 3520 attached to 1040                   | Form was attached to 1040 instead of separate | Mail a complete Form 3520 to Ogden at once; ask a CPA about a reasonable cause statement |
| Currency conversion challenged                      | Auditor questions exchange rate used    | Provide source documentation (IRS yearly average page or the dated rate source) |
