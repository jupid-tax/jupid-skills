# Filing Form 8824 (browser automation)

How an agent equipped with browser tooling can take a completed Form 8824 draft and actually file it. Form 8824 attaches to the user's main income tax return (Form 1040 for individuals, 1065 / 1120-S / 1041 for entities) — it is never filed standalone.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ $89,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners; $89,000 AGI limit for the 2026 filing season,
    https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free)
    Some Free File providers support Form 8824, others do not. Verify before starting.
    Browser automation: provider-specific. Skip — flows change.

User wants to fill the form directly with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    FFFF lists Form 8824 as available (01/26/2026, tax year 2025). Use Section 1 below.
    FFFF cannot attach documents other than its own forms: if the return needs a
    Line 11c explanation, a multi-asset exchange statement, or a multiple-exchange
    summary statement, use paid software or paper instead.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxAct)?
  → That software's "Like-Kind Exchanges" or "Sale of Property" section
    Browser automation: provider-specific. Use Section 2 (generic pattern).

User wants paper filing?
  → Print Form 1040 + Form 8824 + Form 4797 (or Sch D), sign, mail
    Use Section 3.
```

IRS Direct File was not offered in the 2026 filing season. Do not offer it as a channel.

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: for tax year 2025, FFFF forms opened 01/26/2026 and the program closes Oct. 15, 2026 (https://www.irs.gov/e-file-providers/free-file-fillable-forms). Form 8824 is on the available-forms list (https://www.irs.gov/e-file-providers/list-of-available-free-file-fillable-forms). Known limitation: only one Form 4797 can be added.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 8824 draft from `SKILL.md`
- The completed Form 4797 (or Schedule D) reflecting Line 21 and Line 22
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
| 8 | "Name of related party", "Relationship to you", "Related party's identifying number", address | Part II Line 8 (if 7=Yes) |
| 9 | Yes/No — related party disposed of property received from you | Part II Line 9 |
| 10 | Yes/No — you disposed of property you received | Part II Line 10 |
| 11a–11c | Exception checkbox(es) | Part II Line 11 |
| 12 | "FMV of other property given up" | Part III Line 12 |
| 12a | Description of other property given up | Part III Line 12a |
| 13 | "Adjusted basis of other property given up" | Part III Line 13 |
| 14 | (auto-computed) | (verify equals draft Line 14) |
| 15 | "Cash received, FMV of other property received, plus net liabilities..." | Part III Line 15 |
| 15a | Description of other property received | Part III Line 15a |
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
| 25a–25c | Basis allocated to §1250 / §1245-type / intangible like-kind property | Part III Lines 25a–25c |

8. **Add Form 4797** (if Line 21 or Line 22 > 0 and property was used in a trade or business, including rentals):
   - Click "Add a Form / Schedule" → search "4797"
   - Form 8824 Line 21 goes on Form 4797 line 16; Line 22 goes on Form 4797 line 5 (§1231, held more than 1 year) or line 16 (held 1 year or less)
9. **Or add Schedule D** if the relinquished property was a capital asset held for investment: Line 22 goes on Schedule D line 4 (short-term) or line 11 (long-term); no Form 8949 entry
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
| "Form 4797 amount doesn't match Form 8824 Line 22" | Wrong gain-recognition form chosen | Use 4797 (line 5 or 16) if business-use real property; Schedule D (line 4 or 11) if a capital asset |
| FFFF rejects "related-party Part II incomplete" | Line 7 set to Yes but Lines 8-10 missing | Fill Part II or change Line 7 to No (but only if accurate) |
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
2. **All schedules and forms in attachment-sequence order** (the "Attachment Sequence No." in the top-right corner of each form). For this exchange the relevant ones are Schedule D (Sequence No. 12), Form 4797 (No. 27), and Form 8824 (No. 109), after Schedules 1, 2, 3 and any others with lower numbers
3. **Supporting statements** (Line 11c explanation, multi-asset or multiple-exchange statement) after the forms, with name and identifying number on each page
4. **W-2 Copy B** attached to the front of Form 1040, plus Forms W-2G and 1099-R if tax was withheld

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
