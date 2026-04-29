# Filing Form 8962 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 8962 draft and file it as part of the Form 1040 return. Form 8962 is always an attachment to Form 1040 / 1040-SR / 1040-NR — it never files alone.

The agent must produce a complete `SKILL.md`-format draft *first*, must have the Form 1095-A in hand, must have the rest of Form 1040 substantially complete (because MAGI flows from AGI), then pick a filing channel and execute.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific.
    Most providers handle Form 8962 automatically once 1095-A data is
    entered. Skip detailed mapping here.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software?
  → Form 8962 is auto-generated from 1095-A entry.
    Verify the software's PTC summary screen against the draft.
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Form 8962, sign, mail.
    Use Section 3.

User wants to use IRS Direct File?
  → Direct File supports Form 8962 in a growing set of states as of
    early 2026. Confirm the user's state is supported and that their
    1095-A scenario is in scope (single-policy, no allocation, no
    year-of-marriage alternative).
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year.

**Account model**: each tax year is a separate FFFF account.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI
- The completed Form 8962 draft from `SKILL.md`
- Form 1095-A (the *paper or PDF* form) in hand for cross-checking
- Form 1040 inputs substantially complete (for MAGI flow)
- Schedule 1 + Schedule 2 + Schedule 3 drafts if applicable
- Email address the user controls
- IP address the user is willing to file from

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Register / Sign in** for the current tax year
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → Form 1040
6. **Fill 1040 header and basic income** (W-2s, 1099s, Schedule C, etc.) — MAGI must be substantially complete before Form 8962
7. **Add Form 8962** via "Add a Form / Schedule"
8. **Fill Form 8962 from the draft** — field-by-field mapping:

| Form 8962 line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| Name(s) shown on return | "Name(s) shown on return" | Filer name |
| SSN | "Your social security number" | Filer SSN |
| 1 | "Tax family size" | Part I Line 1 |
| 2a | "Modified AGI" | Part I Line 2a |
| 2b | "Dependents' modified AGI" | Part I Line 2b |
| 3 | (auto-computed = 2a + 2b) | (verify) |
| 4 | "Federal poverty line" | Part I Line 4 |
| 5 | (auto-computed = (3 / 4) × 100) | (verify) |
| 7 | "Applicable figure" | Part I Line 7 |
| 8a | (auto-computed = 3 × 7) | (verify) |
| 8b | (auto-computed = 8a / 12) | (verify) |
| 9 | "Did you allocate policy amounts?" Yes/No radio | Line 9 |
| 10 | "Annual or monthly calculation?" Yes (annual) / No (monthly) | Line 10 |
| 11a–11f | Annual calculation columns (if Line 10 = Yes) | Line 11 |
| 12a–23f | Monthly columns Jan–Dec (if Line 10 = No) | Lines 12–23 |
| 24 | (auto-computed) | (verify) |
| 25 | (auto-computed) | (verify) |
| 26 | (auto-computed if Line 24 ≥ Line 25) | (verify) |
| 27 | (auto-computed if Line 24 < Line 25) | (verify) |
| 28 | "Repayment limitation" | Line 28 (from Pub 974 Table 5) |
| 29 | (auto-computed = lesser of 27 or 28) | (verify) |
| 30–33 | Part IV allocation rows (if Line 9 = Yes) | Part IV |
| 34–36 | Part V year-of-marriage (if applicable) | Part V |

   Capture screenshots after each section.

9. **Cross-check the routing** — Form 8962 Line 26 should populate Schedule 3 Line 9; Form 8962 Line 29 should populate Schedule 2 Line 2. FFFF auto-pulls these. Verify against the draft.
10. **Run FFFF's "Check Form" / "Verify"** — resolves math errors. Form 8962 commonly flags:
    - 1095-A monthly amounts don't match Column A/B/C totals
    - Tax family size doesn't match dependents on Form 1040
    - MAGI doesn't match AGI + tax-exempt interest + non-taxable SS
    - Applicable figure doesn't match the % FPL band
11. **Re-verify auto-computed fields** (Lines 3, 5, 8a, 8b, 11d, 11e, 24, 25, 26, 27, 29) against the draft.
12. **Save the return**.
13. **Submit** when 1040 + Form 8962 + all other attachments are complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit
14. **Capture submission ID** + screenshot.
15. **Wait 24–48 hours**, log back in to confirm acceptance.

### What the agent should NOT do

- Do not file without Form 8962 if the filer received APTC; the IRS will hold the refund and send a letter requiring Form 8962
- Do not estimate any 1095-A column amount — they must come from the actual Form 1095-A
- Do not submit without explicit user consent at step 13
- Do not bypass FFFF verification at step 10
- Do not store SSN, DOB, PIN, or 1095-A details in any log

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 8962 missing — APTC reported on 1095-A" | Filer received APTC but no 8962 attached | Add Form 8962, complete reconciliation |
| "Tax family size on 8962 doesn't match dependents" | Dependents on Form 1040 changed but Line 1 not updated | Sync Line 1 with Form 1040 dependents |
| "Applicable figure outside expected range" | % FPL band wrong | Recompute Line 5 with correct FPL table (prior-year HHS) |
| "Line 4 doesn't match HHS poverty guideline for state" | Used current-year FPL instead of prior-year | Switch to prior-year HHS guidelines |
| "1095-A column totals don't match" | Manual entry error | Re-enter from the actual 1095-A |
| Identity verification failed | Wrong prior-year AGI | Pull IRS transcript |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), Form 8962 is **never directly entered**. Instead:

1. Sign in → start or resume a return
2. Complete W-2, Schedule C / SE, dependents, etc. so MAGI is substantially set
3. Find the "Health insurance" or "Affordable Care Act" section (each provider names it differently)
4. Enter Form 1095-A data — typically by typing each month's Column A, B, C into a 12-row table OR by uploading a PDF that gets OCR'd
5. The software auto-computes Form 8962 and populates Schedule 2 Line 2 or Schedule 3 Line 9
6. Find the "Form 8962 review" or "Premium Tax Credit summary" screen — verify each line against the draft. Override only with documented discrepancy.
7. Continue through Form 1040 review
8. Pay the software fee; e-file

**Why this section is generic**: provider-specific selectors and wizards change every tax year. Rely on label text and human-readable navigation.

---

## Section 3 — Paper filing

When paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

The IRS expects this stack from top to bottom:

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in numeric order (Schedule 2 if Line 2 > 0; Schedule 3 if Line 9 > 0)
3. **Schedule SE** (if applicable)
4. **Form 8962** — placed in attachment-sequence order (sequence number printed top-right)
5. **Form 1095-A** — **NOT attached** to the return. Retain in records only.
6. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
7. **1099s with federal withholding** also stapled

Single staple in the upper-left corner. Don't paperclip. Don't double-side print.

### Mailing addresses

The IRS posts current-year addresses by state and by with/without payment at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Look up the address by:
1. Tax form (1040)
2. With or without payment
3. Filer's state

Do not hardcode addresses — they shift between years and split by state.

### Mailing best practices

- USPS Certified Mail with Return Receipt for IRC §7502 timely-mailing-as-timely-filing proof
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy
- If paying, attach Form 1040-V with check made out to "United States Treasury", with SSN + "Form 1040" + tax year on the memo line

### Producing the printable PDF

If the agent has IRS fillable PDFs:

1. Download the latest revision of f1040 and f8962 from https://www.irs.gov/forms-instructions
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms)
4. Save as flattened PDF for printing

Form-field names live in the IRS fillable PDF metadata.

---

## Section 4 — Submission state machine and follow-up

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Letter 12C** OR **CP series notice** OR **audit notice**

### Common Form 8962-related letters

- **Letter 12C** — IRS asks for Form 8962 because they have 1095-A data showing APTC was paid but no 8962 is on file. Standard remedy: file Form 8962 within 20 days of the letter.
- **CP12 / CP21A** — IRS recomputed PTC and either changed the refund amount or assessed additional tax. Verify the IRS calculation against the draft; if disagree, respond.

### Status checks

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status, and 30 days post-Acceptance to check for any IRS correspondence.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. Capture: "I authorize you to file Form 1040 with Form 8962 through FFFF on my behalf right now."
2. **Never store SSN, DOB, PIN, prior-year AGI, or 1095-A details** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, 1095-A discrepancy), **stop and surface the issue**. Don't retry blindly.
6. **Form 8962 never files alone** — confirm Form 1040 is also submitted in the same transaction.
7. **If the IRS later sends a Letter 12C or CP notice** about Form 8962, do not auto-respond; surface the letter to the user and confirm next steps with them.
