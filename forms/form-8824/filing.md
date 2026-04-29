# Filing Form 8824 (browser automation)

How an agent equipped with browser tooling can take a completed Form 8824 draft and actually file it. Form 8824 attaches to the user's main income tax return (Form 1040 for individuals, 1065 / 1120-S / 1041 for entities) — it is never filed standalone.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Some Free File providers support Form 8824, others do not. Verify before starting.
    Browser automation: provider-specific. Skip — flows change.

User wants to fill the form directly with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    FFFF supports Form 8824. Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxAct)?
  → That software's "Like-Kind Exchanges" or "Sale of Property" section
    Browser automation: provider-specific. Use Section 2 (generic pattern).

User wants paper filing?
  → Print Form 1040 + Form 8824 + Form 4797 (or Sch D), sign, mail
    Use Section 3.

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Form 8824.
    Redirect to FFFF or paid software. Verify scope at https://www.irs.gov/filing/irs-direct-file each year.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. FFFF supports Form 8824 as a 1040 attachment.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 8824 draft from `SKILL.md`
- The completed Form 4797 (or Schedule D) reflecting Line 22 recognized gain
- Form 1040 inputs (filing status, dependents, W-2s if any)
- Documentation retained (not filed) for audit defense:
  - QI exchange agreement
  - Written 45-day identification notice
  - Closing statements (HUD-1 / ALTA) for both relinquished and replacement
  - Basis records for relinquished property (purchase docs, improvement receipts, depreciation schedule)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → tax-year launchpad
3. **Sign in / register** for the current tax year's account
4. **Identity verification** — prior-year AGI or self-select PIN. If unavailable, retrieve via Form 4506-T or Get Transcript.
5. **Start a new return** → Form 1040 landing
6. **Add Form 8824**:
   - Click "Add a Form / Schedule" → search "8824" or pick from list
   - Form 8824 opens with fields labeled by line number matching paper form
7. **Fill Form 8824 from the draft** — field-by-field mapping:

| Form 8824 line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| Top — Name | "Name(s) shown on return" | Filer name |
| Top — ID number | "Your taxpayer identification number" | SSN/EIN |
| 1 | "Description of like-kind property given up" | Part I Line 1 |
| 2 | "Description of like-kind property received" | Part I Line 2 |
| 3 | "Date like-kind property given up was originally acquired" | Part I Line 3 |
| 4 | "Date you actually transferred your property given up" | Part I Line 4 |
| 5 | "Date like-kind property you received was identified" | Part I Line 5 |
| 6 | "Date you actually received the like-kind property" | Part I Line 6 |
| 7 | "Was the exchange of property given up or received made with a related party..." Yes/No | Part I Line 7 |
| 8 | "Name of related party" | Part II Line 8 (if 7=Yes) |
| 9 | "Relationship to you" | Part II Line 9 |
| 10 | Yes/No — disposed during this year | Part II Line 10 |
| 11 | Exception checkbox(es) | Part II Line 11 |
| 12 | "FMV of other property given up" | Part III Line 12 |
| 13 | "Adjusted basis of other property given up" | Part III Line 13 |
| 14 | (auto-computed) | (verify equals draft Line 14) |
| 15 | "Cash received, FMV of other property received, plus net liabilities..." | Part III Line 15 |
| 16 | "FMV of like-kind property you received" | Part III Line 16 |
| 17 | (auto-computed) | (verify) |
| 18 | "Adjusted basis of like-kind property you gave up..." | Part III Line 18 |
| 19 | (auto-computed) | (verify Line 19 = realized gain/loss) |
| 20 | (auto-computed) | (verify) |
| 21 | "Ordinary income under recapture rules" | Part III Line 21 (often 0 for §1250 property) |
| 22 | (auto-computed) | (verify Line 22 = recognized gain) |
| 23 | (auto-computed) | (verify Line 23) |
| 24 | (auto-computed) | (verify Line 24 = deferred gain) |
| 25 | (auto-computed) | (verify Line 25 = basis of replacement) |

8. **Add Form 4797** (if Line 22 > 0 and property was business-use real estate):
   - Click "Add a Form / Schedule" → search "4797"
   - Recognized gain from 8824 Line 22 enters Form 4797 Part III if §1250 recapture, otherwise Part I or II depending on holding period
9. **Or add Schedule D + Form 8949** if the relinquished property was held as investment and not for trade/business use
10. **Run FFFF "Check Form" / "Verify"** — it flags math errors and missing required fields
11. **Cross-check** every auto-computed field against the draft. If FFFF and draft disagree, **stop**; one of the two is wrong.
12. **Save the return** — FFFF stores progress server-side
13. **Submit** when 1040 + 8824 + 4797/Sch D are complete:
    - "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit
14. **Capture the submission ID** and screenshot
15. **Wait 24-48 hours** then confirm IRS acceptance via FFFF email or login

### What the agent should NOT do

- Do not submit without explicit user consent at step 13
- Do not bypass FFFF's verification (step 10)
- Do not file if any timing deadline (45-day or 180-day) was missed — the exchange does not qualify, and filing as if it did is improper. Restate and recognize the gain normally.
- Do not store SSN, DOB, PIN, or QI account numbers in any log

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| FFFF auto-compute Line 19 disagrees with draft | Boot calculation in Line 15 or basis in Line 18 misallocated | Recompute draft per `references/boot-rules.md` |
| "Form 4797 amount doesn't match Form 8824 Line 22" | Wrong gain-recognition form chosen | Use 4797 if business-use real property; Sch D + 8949 if investment-only |
| FFFF rejects "related-party Part II incomplete" | Line 7 set to Yes but Lines 8-11 missing | Fill Part II or change Line 7 to No (but only if accurate) |
| State return rejects (CA) | Missing Form 3840 | File CA FTB 3840 separately each year until deferred gain is recognized |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software:

1. Sign in → start or resume a return
2. Navigate to "Sale of property" / "Investment income" / "Like-kind exchange" section. Wizard wording varies.
3. Wizard typically asks:
   - "Did you sell or exchange a property this year?" → Yes
   - "Was this a §1031 like-kind exchange?" → Yes
   - "What was the property?" (real estate, etc.)
   - "Date acquired / Date sold / Date identified replacement / Date received replacement" → from draft Lines 3-6
   - "Was a Qualified Intermediary used?" → Yes (most cases)
   - "Was this with a related party?" → from draft Line 7
   - Cash + boot received, FMV of replacement, debt assumed/relieved → from draft Lines 15-18
4. After the wizard, locate the "Form 8824 review" or "Like-kind exchange summary" and verify each line against the draft
5. Software auto-fills Form 4797 or Schedule D based on property classification — verify
6. Continue through 1040 review, e-file

**Why generic**: provider selectors change every tax year. Rely on visible label text rather than DOM IDs.

---

## Section 3 — Paper filing

### Assemble the return

Stack order (top to bottom):

1. **Form 1040** (signed)
2. **Schedule 1, 2, 3** if applicable
3. **Schedule D** (if Line 22 flows to Sch D) OR **Form 4797** (if Line 22 flows to 4797)
4. **Form 8824** (the like-kind exchange itself)
5. **Form 8949** (if Sch D used)
6. **All other schedules and forms** in attachment-sequence order (top-right corner of each form)
7. **W-2 Copy B** stapled to the front of Form 1040
8. **1099s with federal withholding** also stapled

Single staple in upper-left corner. No paper clips. Letter paper, full size, single-sided.

### Mailing address

Look up current-year address by tax form (1040), with/without payment, and filer's state at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they change.

### Mailing best practices

- USPS Certified Mail with Return Receipt for proof of timely filing (IRC §7502)
- Postmark by April 15 (or extension date if Form 4868 filed)
- Photocopy entire return for user's records
- If paying, attach Form 1040-V with check made out to "United States Treasury"

### Producing the printable PDF

1. Download latest Form 8824 from https://www.irs.gov/forms-instructions
2. Open in PDF tool that supports form filling
3. Map draft values to PDF fields (IRS PDF field names like `f1_3` are stable)
4. Save as flattened PDF for printing

---

## Section 4 — Submission state machine

After filing (any channel):

1. **Submitted** → sent to IRS
2. **Accepted** → basic validation passed (24-48 hours e-file, 4-8 weeks paper)
3. **Processed** → fully ingested
4. **Refund / Balance due / Notice / Audit (CP2000, etc.)**

Status checks:
- E-file: usually Accepted within 24-48 hours
- Paper: 4-8 weeks for acceptance acknowledgment
- Refund: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission.

**§1031-specific watchpoint**: the IRS scrutinizes large §1031 deferrals. If the user receives a CP2000 or audit notice referencing the like-kind exchange, the QI exchange agreement, written 45-day identification, and closing statements become critical evidence. Make sure the user has retained these.

---

## Security and consent rules

1. **Never file without explicit user consent** at the moment of submission
2. **Never store SSN, DOB, PIN, prior-year AGI, or QI account information** in agent logs
3. **Never bypass identity verification or CAPTCHAs**
4. **Always capture submission confirmations** as screenshots
5. **If anything looks wrong** (math disagreement, missing form, deadline miss surfacing only at filing), **stop and surface** — don't retry blindly
6. **Refuse to file** if either of the §1031 deadlines (45-day, 180-day) was missed. The exchange does not qualify; filing Form 8824 as if it did is a misrepresentation. Surface and redirect to standard gain recognition.
