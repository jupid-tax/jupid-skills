# Filing Form 8889 (browser automation)

How an agent equipped with browser tooling can take a completed Form 8889 draft and actually file it with the user's Form 1040. Form 8889 is **always** filed as an attachment to Form 1040 — it is not a standalone return.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific. Skip — flows change yearly.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer)?
  → That software's HSA / Form 8889 section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Form 8889 + supporting schedules, sign, mail
    Use Section 3.

User wants to use IRS Direct File?
  → As of early 2026, Direct File supports HSA / Form 8889 in a limited subset of
    states (verify the current scope at https://www.irs.gov/filing/irs-direct-file).
    If supported in the user's state, use Direct File. If not, redirect to FFFF.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. Outside that window, FFFF returns a "season closed" message — fall back to paper or wait.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years must register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 8889 draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, W-2s, Schedule 1, Schedule 2, etc.) — Form 8889 attaches to a 1040, never files alone
- HSA custodian's 1099-SA (digital copy or values transcribed) for distribution amounts
- W-2 with Box 12 code W amounts (for employer contributions)
- An email address the user controls
- An IP address the user is willing to file from

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in**:
   - First-time: "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: prior-year AGI or self-select PIN. If user lacks prior-year AGI, retrieve from IRS transcript (Form 4506-T) or pause and ask.
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Form 8889**:
   - Click "Add a Form / Schedule" or equivalent
   - Search "Form 8889" or pick from the schedule list
   - The form opens with fields labeled by line number (matching paper form)
8. **Fill Form 8889 from the draft** — field-by-field mapping:

| 8889 line | FFFF field label | Source (in draft) |
|-----------|------------------|-------------------|
| Name | "Name of HSA owner" | Filer name |
| SSN | "Social Security number" | Filer SSN |
| 1 | "Coverage under an HDHP" Self-only / Family radio | Header / Line 1 |
| 2 | "HSA contributions you made (or those made on your behalf)" | Part I Line 2 |
| 3 | "Contribution limit" (use Limitation Chart and Worksheet if needed) | Part I Line 3 |
| 4 | "Archer MSA contributions" | Part I Line 4 |
| 5 | (auto-computed) | (verify equals draft Line 5) |
| 6 | "Enter amount from line 5" or allocated share if MFJ | Part I Line 6 |
| 7 | "Additional contribution amount" (catch-up) | Part I Line 7 |
| 8 | (auto-computed) | (verify equals draft Line 8) |
| 9 | "Employer contributions made to your HSAs for 2025" | Part I Line 9 |
| 10 | "Qualified HSA funding distribution" | Part I Line 10 |
| 11 | (auto-computed) | (verify) |
| 12 | (auto-computed) | (verify) |
| 13 | "HSA deduction" | Part I Line 13 |
| 14a | "Total distributions" | Part II Line 14a |
| 14b | "Distributions of excess contributions" | Part II Line 14b |
| 14c | (auto-computed) | (verify) |
| 15 | "Unreimbursed qualified medical expenses" | Part II Line 15 |
| 16 | (auto-computed) — taxable HSA distributions | Part II Line 16 |
| 17a | "Exception applies" checkbox | Part II Line 17a |
| 17b | "Additional 20% tax" | Part II Line 17b |
| 18 | "Last-month rule" prior-year contributions (Part III) | Part III Line 18 |
| 19 | "Months of failure" | Part III Line 19 |
| 20 | (auto-computed) | (verify) |
| 21 | (auto-computed — 10% additional tax) | (verify) |

   After each field, capture a screenshot for the user's records.

9. **Cross-link Schedule 1**:
   - Open Schedule 1 in FFFF
   - Verify Line 13 (HSA deduction) carries the Form 8889 Line 13 amount automatically. If not, enter manually.
   - Verify Line 8f (Income from Form 8889) carries Form 8889 Line 16 automatically. If not, enter manually.
10. **Cross-link Schedule 2** (only if Form 8889 Line 17b > 0):
    - Open Schedule 2
    - Verify Line 17c carries the 20% additional tax from Form 8889 Line 17b
11. **If MFJ with two HSAs**: add a second Form 8889 for the spouse — FFFF allows two instances, one per filer SSN. Repeat steps 7–10 for the spouse's draft.
12. **Attach Form 5329** if excess contributions were not withdrawn — separate FFFF form, complete Part VII (Additional Tax on Excess HSA Contributions).
13. **Run FFFF's "Check Form" / "Verify"** — resolves math errors and missing required fields. Resolve every flag before submission.
14. **Cross-check** every auto-computed field against the draft. If FFFF disagrees, **stop**; one of the two is wrong.
15. **Save the return** (FFFF stores progress server-side).
16. **Submit** when verified and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit
17. **Capture the submission ID**. Save the screenshot.
18. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. On rejection, read the rejection code and fix.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 16
- Do not bypass FFFF's verification (step 13)
- Do not file FFFF for a tax year already filed (creates duplicate-filing audit flag)
- Do not store the user's SSN, DOB, PIN, or HSA account numbers in any log or transcript
- Do not put cafeteria-plan contributions on Line 2 — they belong on Line 9 only

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Retrieve from IRS transcript |
| "Form 8889 Line 3 limit exceeded" | Coverage type or limit wrong | Verify partial-year proration; check 2025 vs 2026 limits |
| "Schedule 1 Line 13 doesn't match Form 8889 Line 13" | Cross-link broken | Manually enter or remove and re-add Form 8889 |
| 1099-SA box 1 differs from custodian statement | Late distribution after January 1 | Use 1099-SA value; the IRS matches against 1099-SA |
| MFA / CAPTCHA | Routine | Pause for user input |

---

## Section 2 — Generic tax-software pattern

Most paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes) walks the user through HSA reporting via wizard:

1. Sign in → start or resume a return
2. Navigate to "Health Savings Account", "HSA", or "Medical and Dental" → "Form 8889" section
3. Wizard questions and how to answer from the draft:
   - "Did you contribute to an HSA in 2025?" → Yes if Line 2 + Line 9 > 0
   - "Were you covered by an HDHP in 2025?" → Yes; pick coverage type and months
   - "What was your HDHP coverage (self-only or family) on Dec 1?" → Header / Line 1
   - "How much did you contribute directly?" → Line 2
   - "Did your employer contribute (W-2 Box 12 code W)?" → import or type Line 9
   - "Are you 55 or older?" → triggers Line 7 catch-up
   - "Did you receive a 1099-SA?" → Yes if any distribution; enter Box 1 → Line 14a
   - "How much did you spend on qualified medical expenses?" → Line 15
   - "Did you use the last-month rule in a prior year? Did you stay HSA-eligible?" → Part III prompts
4. After the wizard, most software shows a "Form 8889 summary" — verify each line against the draft. Override anything that disagrees.
5. Confirm Schedule 1 Line 13 reflects the HSA deduction, Schedule 1 Line 8f reflects taxable distributions, Schedule 2 Line 17c reflects the 20% tax.
6. If MFJ with two HSAs, the wizard usually asks "Did your spouse also have an HSA?" — answer Yes and repeat the entire HSA flow for the spouse.
7. Continue through Form 1040 review; pay software fee; e-file.

**Why this section is generic**: provider selectors and wizard wording change yearly. Use label text and human-readable navigation rather than DOM IDs.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex MFJ situation, identity-theft concerns).

### Assemble the return

Order matters — IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Form 8889** (one per filer with an HSA — two if MFJ with two HSAs)
4. **Form 5329** (if excess HSA contributions, Part VII)
5. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
6. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)

Single staple in the upper-left corner. Don't paperclip. Don't double-side print.

### Mailing addresses

The IRS posts current-year addresses (split by state, with vs. without payment) at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Look up by tax form (1040), with/without payment, filer's state. Do not hardcode — addresses shift between years.

### Mailing best practices

- USPS Certified Mail with Return Receipt for proof of timely filing (IRC §7502 timely-mailing-as-timely-filing)
- Postmark by April 15 (or extension date if Form 4868 filed)
- Keep a complete photocopy of the return — including each Form 8889 — for the user's records
- HSA records (receipts, custodian statements) should be kept for at least 3 years after the year of the related distribution; longer is better given the open-ended reimbursement window

### Producing the printable PDF

1. Download latest revisions from https://www.irs.gov/forms-instructions: f8889.pdf, f1040.pdf, f1040s1.pdf, f1040s2.pdf, f5329.pdf if needed
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms — `f1_3` etc. — listable via `pypdf` or `pdftk`)
4. Save as flattened PDF for printing

---

## Section 4 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **CP2000 notice** (if 1099-SA mismatch detected)

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund: https://www.irs.gov/refunds (Where's My Refund tool)
- Account transcript: https://www.irs.gov/individuals/get-transcript

Set a follow-up reminder 7 days post-submission. Set a second reminder for 12–18 months out — that's the typical CP2000 window for 1099-SA matching mismatches.

---

## Security and consent rules for the agent

Non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 8889 with my Form 1040 through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, or HSA account numbers** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures, 1099-SA mismatch), **stop and surface the issue**. Don't retry blindly.
6. **Never submit a Form 8889 with `Line 15 > Line 14c`** — that's logically impossible and FFFF will reject it. Recompute first.
