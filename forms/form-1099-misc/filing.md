# Filing Form 1099-MISC (browser automation)

How an agent files Form 1099-MISC with the IRS and delivers Copy B to recipients. Complementary to `SKILL.md`, which produces the issuance plan or recipient reconciliation.

The agent must produce a complete `SKILL.md`-format issuance plan first, then pick a filing channel from the decision tree below, then execute channel-specific steps.

This file applies to the **payor side**. Recipients do not file 1099-MISC themselves — they receive Copy B and use the data on Schedule C / E / F / Schedule 1, which has its own filing path.

---

## Channel decision tree

```
Issuing 10+ information returns total in the calendar year (any 1099 + W-2 combined)?
  → Electronic filing is MANDATORY (IRC §6011(e); T.D. 9972)
  → Use IRIS (free) or a paid service. FIRE is retired: from filing season
    2027 (tax year 2026 forms) IRIS is the only IRS intake system for
    information returns (Pub. 1099 (2026), What's New)

Issuing < 10 information returns total?
  → Electronic optional, paper allowed
  → Default recommendation: IRIS (free, easier than paper)

Already paying for tax software or payroll service that issues 1099s?
  → That software's 1099 module
```

---

## Section 1 — IRS IRIS (Information Returns Intake System)

URL: https://www.irs.gov/filing/e-file-information-returns

IRIS is the free IRS portal for filing 1099-series forms. It has a Taxpayer Portal (manual entry / CSV upload, Pub. 5717) and an Application to Application channel (XML, Pub. 5718). A2A needs an IRIS Transmitter Control Code; Pub. 1099 (2026) says TCC applications typically take 45 business days, so apply early.

**Account model**: payer registers an IRIS account (one per EIN). The IRS may require ID.me identity verification for the responsible individual.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Payer's legal name, EIN, address, phone
- ID.me account or equivalent
- Each recipient's data: legal name, TIN, address, populated boxes
- Special attention for Box 6 (medical), Box 8, Box 10 (attorney), and Box 11 — these include corporate recipients
- The payment year, so the right revision and thresholds are used (Rev. April 2025 / $600 for 2025 payments; Rev. December 2026 / $2,000 for 2026 payments)
- Completed issuance plan from `SKILL.md`

### Browser flow

1. **Navigate** to https://www.irs.gov/filing/e-file-information-returns
2. **Click** "Sign in to IRIS" → ID.me login
3. **Complete identity verification** — pause here for user; do not bypass.
4. **Land on IRIS dashboard** → "File Forms" → "Form 1099-MISC"
5. **Choose method**:
   - **Manual entry**: form-by-form
   - **CSV upload**: bulk via IRIS template
6. **Manual entry path** — for each recipient, fill:
   - Recipient name, address, TIN
   - All applicable boxes with amounts (2026 forms add 13a cash tips, 13b TTOC, 14 overtime; usually blank for rent, medical and settlement payments)
   - State boxes (16-18) if state withholding or income reporting
   - Account number (optional; required if the FATCA box is checked)
   - Any checkboxes (Box 7 direct sales, FATCA (Box 13 on 2025 forms, unnumbered on 2026 forms), "2nd TIN not.", "CORRECTED")
7. **CSV upload path** — generate CSV per IRIS schema (download current-year template), validate, upload
8. **Review summary** — IRIS displays totals; verify against issuance plan
9. **Submit** — IRIS produces Submission ID. Save screenshot.
10. **Distribute Copy B**:
    - IRIS option to e-deliver Copy B with recipient consent
    - Otherwise mail Copy B by **January 31** (**February 15** if Box 8 or Box 10 has an amount); next business day if a weekend or legal holiday: February 1, 2027 and February 16, 2027 for 2026 forms
11. **State filing**: if the state is in CF/SF, IRIS can forward. Some participating states still require direct filing (e.g., Massachusetts). Ask, and check the state's rule.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | ID.me biometric / document mismatch | Pause, ask user via ID.me portal |
| "Form rejected — TIN mismatch" | Recipient name/TIN wrong | Verify W-9, send B-Notice if needed |
| Warning that a Box 6 / Box 10 recipient is a corporation | Generic corporate-recipient check | Proceed; corporate medical providers and attorneys are reportable |
| "Filing window closed" | Past deadline | Late-file with penalty (IRC §6721) |

---

## Section 2 — Paper filing (Form 1096 + Copy A)

For payers issuing < 10 information returns who prefer paper.

### Assemble the return

1. **Form 1099-MISC Copy A** for each recipient (red ink scannable form — must be ordered, cannot print and submit)
2. **Form 1096** — separate Form 1096 per type. If issuing 1099-MISC and 1099-NEC, two Form 1096s.
3. **Form 1096 boxes**:
   - Filer's name, address, TIN
   - Box 3: total number of 1099-MISC forms transmitted
   - Box 5: total amount reported — for Form 1099-MISC, the total of Boxes 1, 2, 3, 5, 6, 8, 9, 10, and 11 (Form 1096 (2026) instructions, Box 5)
   - Box 6: form type code "95" for 1099-MISC (Form 1096 (2026))

### Mailing address

Use the "Where To File" table in the Form 1096 instructions (https://www.irs.gov/pub/irs-pdf/f1096.pdf): Austin, Kansas City, or Ogden, by the filer's principal business state. Do not hardcode; re-read it each year.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt**
- Postmark by **February 28** (1099-MISC paper IRS deadline; March 1, 2027 for 2026 forms) — note: this is later than 1099-NEC's January 31
- Keep a complete photocopy of the entire submission

### Copy B to recipient

- Print Copy B (black ink OK; only Copy A requires red ink scannable)
- Mail by **January 31** (**February 15** with Box 8 or 10 amounts), next business day if a weekend or holiday

---

## Section 3 — Generic third-party software pattern

For QuickBooks, Track1099, Tax1099, Gusto, Rippling, Bill.com, etc.:

1. Sign in → 1099 / Year-end module
2. Confirm payer info (EIN, address)
3. Import or enter recipients
4. Verify W-9 status and TIN matches
5. Enter box amounts. Watch out for boxes most platforms don't pre-populate (Box 9 crop insurance, Box 12 §409A, Box 15) — these may require manual entry. Check that the platform uses the right year's form (Box 14 is reserved on the 2025 form and overtime on the 2026 form; golden parachute payments go on 1099-NEC box 3).
6. Software files with IRS under the platform's IRIS transmitter code; distributes Copy B to recipients
7. Pay platform fee per form

Most platforms cover CF/SF states. Verify state coverage in platform docs.

---

## Section 4 — Backup withholding deposits (Form 945)

Same as 1099-NEC: any Box 4 amount on a 1099-MISC is backup withholding (or Indian gaming withholding), deposited via EFTPS, reconciled annually on Form 945 (line 2 for backup withholding) by January 31 (February 1, 2027 for 2026).

The Form 945 covers all backup withholding regardless of which 1099 form (NEC, MISC, K, INT, DIV) the withholding came from.

---

## Section 5 — Corrections

If a 1099-MISC was filed with errors:

- **One-step correction** (Error Type 1: incorrect money amount, code, or checkbox — including an amount in the wrong box on the right form): file a corrected 1099-MISC with the "CORRECTED" box checked, showing the correct amounts. Send a corrected Copy B.
- **Two-step correction** (Error Type 2: wrong TIN, wrong recipient name, or wrong form type):
  1. File a corrected 1099-MISC with original (incorrect) info and $0 in all boxes, marked CORRECTED
  2. File a separate new original 1099-MISC (or the right form) with correct info
- **Filed when none was required** (e.g., below the threshold, or to a corporate landlord): one corrected form with all amounts $0.

Common 1099-MISC correction scenarios:
- Amount in the wrong box (e.g., $2,450 medical payment in Box 3 instead of Box 6) → one-step correction: Box 3 = $0, Box 6 = $2,450
- Attorney fees for the payer's own legal services reported in Box 10 instead of on 1099-NEC box 1a → wrong form type, two-step correction

See Pub. 1099 (2026), part H, for paper corrections; Pub. 5717 (IRIS Taxpayer Portal) and Pub. 5718 (IRIS A2A) for electronic corrections. Do not check the VOID box on a correction.

---

## Section 6 — Submission state machine

After filing:

1. **Submitted** → IRIS / paper
2. **Accepted** → IRS confirms; for IRIS, usually within minutes
3. **Processed** → posted to recipient's account
4. **Notices** → Notice 972CG proposes information-return penalties; CP2100 / CP2100A lists name/TIN mismatches that start the B-Notice process

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at submission moment
2. **Never store SSN, EIN, TIN, or banking data** in agent logs
3. **Never bypass IRS identity verification or ID.me**
4. **Always capture submission confirmations** as screenshots stored under user's account
5. **TIN mismatches**: surface, do not silently file with a known-bad TIN
6. **Recipient consent for e-delivery**: required before e-delivering Copy B
7. **Box 6 / 8 / 10 / 11 to corporations**: do NOT exclude these from the issuance plan even if a platform surfaces a warning — the corporate exemption does NOT apply to medical, substitute-payment, attorney, or fish-purchase payments. If unsure, verify against [`references/corporate-exception.md`](./references/corporate-exception.md).
