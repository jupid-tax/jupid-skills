# Filing Form 1099-MISC (browser automation)

How an agent files Form 1099-MISC with the IRS and delivers Copy B to recipients. Complementary to `SKILL.md`, which produces the issuance plan or recipient reconciliation.

The agent must produce a complete `SKILL.md`-format issuance plan first, then pick a filing channel from the decision tree below, then execute channel-specific steps.

This file applies to the **payor side**. Recipients do not file 1099-MISC themselves — they receive Copy B and use the data on Schedule C / E / F / Schedule 1, which has its own filing path.

---

## Channel decision tree

```
Issuing 10+ information returns total in the calendar year (any 1099 + W-2 combined)?
  → Electronic filing is MANDATORY (IRC §6011(e)(2), TFA 2019)
  → Use IRIS (free) or FIRE (free, requires Transmitter Control Code) or a paid service

Issuing < 10 information returns total?
  → Electronic optional, paper allowed
  → Default recommendation: IRIS (free, easier than paper)

Already paying for tax software or payroll service that issues 1099s?
  → That software's 1099 module
```

---

## Section 1 — IRS IRIS (Information Returns Intake System)

URL: https://www.irs.gov/filing/e-file-information-returns

IRIS supports 1099-MISC, 1099-NEC, 1099-K, 1099-INT, 1099-DIV, 1099-B, 1099-C, 1099-R, 1099-S, 1099-G, 1099-OID, 1099-PATR, 1099-Q, 1099-SA, and W-2G.

**Account model**: payer registers an IRIS account (one per EIN). ID.me identity verification required for the responsible individual.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Payer's legal name, EIN, address, phone
- ID.me account or equivalent
- Each recipient's data: legal name, TIN, address, populated boxes
- Special attention for Box 6 (medical) and Box 10 (attorney) — these include corporate recipients
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
   - All applicable boxes (1-15) with amounts
   - State boxes (16-18) if state withholding or income reporting
   - Account number (optional)
   - Any checkboxes (Box 7 direct sales, Box 13 FATCA, "2nd TIN not.", "CORRECTED")
7. **CSV upload path** — generate CSV per IRIS schema (download current-year template), validate, upload
8. **Review summary** — IRIS displays totals; verify against issuance plan
9. **Submit** — IRIS produces Submission ID. Save screenshot.
10. **Distribute Copy B**:
    - IRIS option to e-deliver Copy B with recipient consent
    - Otherwise mail Copy B (postmark by **February 1**, slightly later than 1099-NEC's January 31 deadline)
11. **State filing**: if state in CF/SF, IRIS forwards. Otherwise file separately.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | ID.me biometric / document mismatch | Pause, ask user via ID.me portal |
| "Form rejected — TIN mismatch" | Recipient name/TIN wrong | Verify W-9, send B-Notice if needed |
| "Box 6 to corporation rejected" | (false alarm — IRIS accepts this) | Confirm submission status; corporate medical / attorney is correct |
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
   - Box 5: total amount reported (sum of payments — for Form 1099-MISC, this is sum of Boxes 1, 2, 3, 5, 6, 8, 9, 10, 14, 15 — verify which boxes are aggregated for Form 1096 Line 5 each year)
   - Box 6: form type code "95" for 1099-MISC

### Mailing address

Look up at https://www.irs.gov/instructions/i1099gi by:
1. Form type (1099-MISC)
2. Filer's state

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt**
- Postmark by **February 28** (1099-MISC paper IRS deadline) — note: this is later than 1099-NEC's January 31
- Keep a complete photocopy of the entire submission

### Copy B to recipient

- Print Copy B (black ink OK; only Copy A requires red ink scannable)
- Mail by **February 1**

---

## Section 3 — Generic third-party software pattern

For QuickBooks, Track1099, Tax1099, Gusto, Rippling, Bill.com, etc.:

1. Sign in → 1099 / Year-end module
2. Confirm payer info (EIN, address)
3. Import or enter recipients
4. Verify W-9 status and TIN matches
5. Enter box amounts. Watch out for boxes most platforms don't pre-populate (Box 9 crop insurance, Box 12 §409A, Box 14 golden parachute) — these may require manual entry.
6. Software files with IRS via FIRE under the platform's transmitter ID; distributes Copy B to recipients
7. Pay platform fee per form

Most platforms cover CF/SF states. Verify state coverage in platform docs.

---

## Section 4 — Backup withholding deposits (Form 945)

Same as 1099-NEC: any Box 4 amount on a 1099-MISC is backup withholding, deposited via EFTPS, reconciled annually on Form 945 by January 31.

The Form 945 covers all backup withholding regardless of which 1099 form (NEC, MISC, K, INT, DIV) the withholding came from.

---

## Section 5 — Corrections

If a 1099-MISC was filed with errors:

- **One-step correction** (wrong dollar amount, wrong recipient address): file a corrected 1099-MISC with the "Corrected" box checked, showing the correct amount.
- **Two-step correction** (wrong TIN, wrong recipient name, or wrong box):
  1. File a corrected 1099-MISC with original (incorrect) info and $0 in all boxes, marked Corrected
  2. File a separate new 1099-MISC with correct info

Common 1099-MISC correction scenarios:
- Amount allocated to wrong box (e.g., put $1,200 medical payment in Box 3 instead of Box 6) → two-step correction
- Plaintiff's settlement portion put in Box 10 instead of Box 3 → two-step correction (the boxes have different reporting consequences)

See IRS Pub. 1220 Section H for correction matrices.

---

## Section 6 — Submission state machine

After filing:

1. **Submitted** → IRIS / FIRE / paper
2. **Accepted** → IRS confirms; for IRIS, usually within minutes
3. **Processed** → posted to recipient's account
4. **Penalty notice** → CP2100 / CP2100A for TIN mismatches, CP14 for unpaid backup withholding

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at submission moment
2. **Never store SSN, EIN, TIN, or banking data** in agent logs
3. **Never bypass IRS identity verification or ID.me**
4. **Always capture submission confirmations** as screenshots stored under user's account
5. **TIN mismatches**: surface, do not silently file with a known-bad TIN
6. **Recipient consent for e-delivery**: required before e-delivering Copy B
7. **Box 6 / Box 10 to corporations**: do NOT exclude these from the issuance plan even though IRIS may surface a warning — the corporate exemption does NOT apply to medical or attorney payments. If unsure, verify against [`references/corporate-exception.md`](./references/corporate-exception.md).
