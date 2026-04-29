# Filing Schedule 2 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Schedule 2 draft and file it as part of the Form 1040 return. Schedule 2 never files alone — it is always an attachment to Form 1040 / 1040-SR / 1040-NR.

The agent must produce a complete `SKILL.md`-format draft *first*, must have all upstream forms (6251, 8962, Schedule SE, 8959, 8960, 5329, 4137, 8919, Schedule H, 5405, 8611, 965-A) in completed form, then pick a filing channel and execute.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific.
    Most providers handle Schedule 2 automatically as the user enters
    upstream form data. Skip detailed mapping here.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software?
  → Schedule 2 is auto-generated from upstream form data.
    Verify the software's Schedule 2 summary screen against the draft.
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Schedule 2 + supporting forms, sign, mail.
    Use Section 3.

User wants to use IRS Direct File?
  → As of early 2026, Direct File supports a limited subset of
    Schedule 2 items (SE tax, basic AMT). Verify current scope.
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. Outside that window, FFFF returns "season closed".

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials — register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Schedule 2 draft from `SKILL.md`
- Every upstream form already drafted: 6251 (if Line 1), 8962 (if Line 2), Schedule SE (if Line 4), 4137 (if Line 5), 8919 (if Line 6), 5329 (if Line 8), Schedule H (if Line 9), 5405 (if Line 10), 8959 (if Line 11), 8960 (if Line 12), 965-A (if Line 13/20), 8611 (if Line 16), 8889 (if Line 17c or 17m)
- Form 1040 inputs (filing status, dependents, W-2s, etc.)
- An email address the user controls
- An IP address the user is willing to file from

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Register / Sign in** for the current tax year
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add upstream forms first** — Schedule 2 cannot be completed before its sources. In FFFF, add each upstream form via "Add a Form / Schedule" search. Recommended order:
   1. Schedule SE (if applicable)
   2. Form 8962
   3. Form 8959
   4. Form 8960
   5. Form 5329
   6. Form 6251
   7. Form 4137 / 8919 / Schedule H / 5405 / 8611 / 965-A / 8889 / 8611 as applicable
8. **Add Schedule 2** via "Add a Form / Schedule" → search "Schedule 2"
9. **Fill Schedule 2 from the draft** — field-by-field mapping:

| Schedule 2 line | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name(s) shown on return | "Name(s) shown on return" | Filer name |
| SSN | "Your social security number" | Filer SSN |
| 1 | "Alternative minimum tax. Attach Form 6251" | Part I Line 1 |
| 2 | "Excess advance premium tax credit repayment. Attach Form 8962" | Part I Line 2 |
| 3 | (auto-computed = Line 1 + Line 2) | (verify against draft) |
| 4 | "Self-employment tax. Attach Schedule SE" | Part II Line 4 |
| 5 | "Social security and Medicare tax on unreported tip income. Attach Form 4137" | Part II Line 5 |
| 6 | "Uncollected social security and Medicare tax on wages. Attach Form 8919" | Part II Line 6 |
| 7 | (auto-computed = Line 5 + Line 6) | (verify) |
| 8 | "Additional tax on IRAs or other tax-favored accounts. Attach Form 5329 if required" | Part II Line 8 |
| 9 | "Household employment taxes. Attach Schedule H" | Part II Line 9 |
| 10 | "Repayment of first-time homebuyer credit. Attach Form 5405 if required" | Part II Line 10 |
| 11 | "Additional Medicare Tax. Attach Form 8959" | Part II Line 11 |
| 12 | "Net investment income tax. Attach Form 8960" | Part II Line 12 |
| 13 | "Section 965 net tax liability from Form 965-A" | Part II Line 13 |
| 14 | "Interest on tax due on installment income from sale of certain residential lots and timeshares" | Part II Line 14 |
| 15 | "Interest on the deferred tax on gain from certain installment sales over $150,000" | Part II Line 15 |
| 16 | "Recapture of low-income housing credit. Attach Form 8611" | Part II Line 16 |
| 17a | "Recapture of other credits. List type and amount" — text + numeric | Part II Line 17a |
| 17b–17z | Per-subitem labels (HSA, ABLE, look-back, §72(p), etc.) | Part II Line 17 sub-items |
| 18 | (auto-computed = sum of 17a–17z) | (verify) |
| 19 | (reserved — leave blank) | — |
| 20 | "Section 965 net tax liability installment from Form 965-A" | Part II Line 20 |
| 21 | (auto-computed = Lines 4 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 18) | (verify against draft) |

   Capture a screenshot after every page for the user's records.

10. **Cross-check Form 1040** — Line 17 should now show Schedule 2 Line 3, and Line 23 should show Schedule 2 Line 21. FFFF auto-pulls these. Verify against the draft.
11. **Run FFFF's "Check Form" / "Verify"** — resolves math errors and missing required fields. Schedule 2 typically flags if an upstream form's amount doesn't match.
12. **Re-verify auto-computed fields** (Lines 3, 7, 18, 21) against the draft. If a number disagrees, **stop**; one is wrong.
13. **Save the return**.
14. **Submit** when 1040 + all attachments are complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit
15. **Capture submission ID** + screenshot.
16. **Wait 24–48 hours**, log back in to confirm acceptance.

### What the agent should NOT do

- Do not fill Schedule 2 before the upstream forms are complete and verified — entered numbers will be re-overwritten when upstream forms post their results, and the discrepancy can cause rejection
- Do not submit without the user's explicit go-ahead at step 14
- Do not bypass FFFF's verification (step 11)
- Do not store the user's SSN, DOB, or PIN in any log
- Do not enter a Schedule 2 amount that disagrees with the upstream form — fix the upstream form first

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Schedule 2 Line 4 does not match Schedule SE Line 12" | Schedule SE not posted, or draft mismatch | Verify Schedule SE; re-save |
| "Form 6251 required because Line 1 has a value" | Line 1 entered without attaching 6251 | Add Form 6251, fill, save |
| "Form 8962 not attached" | APTC reported on 1095-A but no 8962 | Add Form 8962; complete reconciliation |
| "Line 11 entered but Form 8959 missing" | Additional Medicare Tax without 8959 | Add Form 8959 |
| "Identity verification failed" | Wrong prior-year AGI | Pull IRS transcript |
| "Math error on Line 21" | One sub-line not posted | Recompute Line 21 manually; find missing line |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), Schedule 2 is **never directly entered**. Instead:

1. Sign in → start or resume a return
2. Enter each *upstream* form's data via the software's wizard:
   - "Did you have self-employment income?" → triggers Schedule SE → posts to Schedule 2 Line 4
   - "Did you receive Form 1095-A?" → triggers Form 8962 → posts to Schedule 2 Line 2 (if excess) or Schedule 3 Line 9 (if refundable PTC)
   - "Did you take an early IRA distribution?" → triggers Form 5329 → Schedule 2 Line 8
   - "Did your wages exceed $200,000?" → triggers Form 8959 → Schedule 2 Line 11
   - "Did you have investment income above the NIIT threshold?" → triggers Form 8960 → Schedule 2 Line 12
3. After each upstream wizard, the software auto-populates Schedule 2.
4. Find the "Schedule 2 review" or "Other taxes summary" screen — verify each line against the draft. Override only if there is a documented discrepancy with an upstream form.
5. Continue through Form 1040 review; software computes Lines 17 and 23 from Schedule 2.
6. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizards change every tax year. Rely on label text and human-readable navigation rather than DOM IDs.

---

## Section 3 — Paper filing

When paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

The IRS expects this stack from top to bottom:

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in numeric order (Schedule 2 is the second of the three)
3. **Schedule SE** (if Line 4 > 0)
4. **Form 6251** (if Line 1 > 0)
5. **Form 8962** (if Line 2 > 0)
6. **Form 8959** (if Line 11 > 0)
7. **Form 8960** (if Line 12 > 0)
8. **Form 5329** (if Line 8 > 0)
9. **Schedule H** (if Line 9 > 0)
10. **Other forms** (4137, 8919, 5405, 8611, 965-A, 8889) in attachment-sequence number order printed in the top-right corner of each form
11. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
12. **1099s with federal withholding** also stapled

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

1. Download the latest revision of f1040, f1040s2, and every required upstream form from https://www.irs.gov/forms-instructions
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms)
4. Save as flattened PDF for printing

Form-field names live in the IRS fillable PDF metadata; tooling like `pypdf` or `pdftk` can list them.

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Audit notice (CP2000, etc.)**

Schedule 2 lines are common audit triggers, especially:

- Line 1 (AMT) — IRS verifies against Form 6251 worksheet
- Line 2 (excess APTC) — IRS cross-checks against marketplace data (Form 1095-A)
- Line 4 (SE tax) — IRS compares against Schedule C / F / K-1 SE income
- Line 11 (Additional Medicare Tax) — IRS cross-checks against W-2 Medicare wages
- Line 12 (NIIT) — IRS cross-checks against Schedule B/D investment income

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status, and 30 days post-Acceptance to check for any CP-series notices.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. Capture: "I authorize you to file Form 1040 with Schedule 2 through FFFF on my behalf right now."
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, missing upstream form), **stop and surface the issue**. Don't retry blindly.
6. **Schedule 2 never files independently** — confirm Form 1040 is also submitted in the same transaction. Filing Schedule 2 alone is not a valid return and can create an account mismatch.
