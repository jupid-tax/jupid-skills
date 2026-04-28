# Filing Schedule 1 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser) can take a completed Schedule 1 draft and actually file it. This file describes deterministic flows the agent can follow; it complements `SKILL.md`, which produces the draft.

Schedule 1 is **not filed in isolation** — it always attaches to Form 1040. The agent must produce a complete `SKILL.md`-format draft for Schedule 1 *and* have the rest of Form 1040 ready before submission.

The agent picks a filing channel from the decision tree below, then executes the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific (TaxAct Free, FreeTaxUSA, etc.)
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's "Other income / Adjustments" section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Schedule 1 + supporting schedules, sign, mail
    Use Section 3.

User wants to use IRS Direct File?
  → Note: IRS Direct File supports a subset of scenarios. Schedule 1 simple cases
    (unemployment income, student loan interest, educator expenses) are typically
    supported; Schedule C / Schedule SE flows in Direct File depend on the year's
    rollout. Check current scope before automating.
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: FFFF is open from late January through mid-October each year. Outside that window, fall back to paper or wait.

**Account model**: each tax year is a separate FFFF account.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Schedule 1 draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, W-2s if any, etc.) — Schedule 1 alone isn't a return
- All supporting schedules and forms (Schedule C, Schedule SE, Form 8889, Form 3903, Form 2106, Form 8853 — whichever apply)
- An email address the user controls
- An IP address the user is willing to file from

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → redirects to the FFFF launchpad
3. **Register / Sign in** (first-time: create account; returning: only the current tax year's account works)
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Schedule 1**:
   - Click "Add a Form / Schedule"
   - Search "Schedule 1" or pick from the list
   - Schedule 1 opens with fields labeled by line number (matching paper form)
8. **Fill Schedule 1 from the draft** — field-by-field mapping:

| Schedule 1 line | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name(s) | "Name(s) shown on Form 1040" | From 1040 header |
| SSN | "Your social security number" | From 1040 header |
| 1099-K personal | "Amount reported on 1099-K in error or for personal items sold at a loss" | Top of Part I header |
| 1 | "Taxable refunds, credits, or offsets of state and local income taxes" | Part I Line 1 |
| 2a | "Alimony received" | Part I Line 2a |
| 2b | "Date of original divorce or separation agreement" | Part I Line 2b |
| 3 | "Business income or (loss)" | Part I Line 3 |
| 4 | "Other gains or (losses)" — checkbox 4797/4684 | Part I Line 4 |
| 5 | "Rental real estate, royalties, partnerships, S corporations, trusts" | Part I Line 5 |
| 6 | "Farm income or (loss)" | Part I Line 6 |
| 7 | "Unemployment compensation" — checkbox if repaid | Part I Line 7 |
| 8a | "Net operating loss" | Part I Line 8a (negative) |
| 8b | "Gambling" | Part I Line 8b |
| 8c | "Cancellation of debt" | Part I Line 8c |
| 8d | "Foreign earned income exclusion from Form 2555" | Part I Line 8d (negative) |
| 8e | "Income from Form 8853" | Part I Line 8e |
| 8f | "Income from Form 8889" | Part I Line 8f |
| 8g | "Alaska Permanent Fund dividends" | Part I Line 8g |
| 8h | "Jury duty pay" | Part I Line 8h |
| 8i | "Prizes and awards" | Part I Line 8i |
| 8j | "Activity not engaged in for profit income" | Part I Line 8j |
| 8k | "Stock options" | Part I Line 8k |
| 8l | "Income from rental of personal property…" | Part I Line 8l |
| 8m | "Olympic and Paralympic medals and USOC prize money" | Part I Line 8m |
| 8n-8u | (sub-lines for §951(a), §951A(a), §461(l), ABLE, scholarships, Medicaid waiver, deferred comp, incarceration wages) | Part I Lines 8n-8u |
| 8v | "Digital assets received as ordinary income not reported elsewhere" | Part I Line 8v |
| 8z | "Other income — list type and amount" | Part I Line 8z |
| 9 | (auto-computed) | Verify equals draft Line 9 |
| 10 | (auto-computed) | Verify equals draft Line 10 |
| 11 | "Educator expenses" | Part II Line 11 |
| 12 | "Certain business expenses of reservists, performing artists, and fee-basis government officials" | Part II Line 12 |
| 13 | "Health savings account deduction" | Part II Line 13 |
| 14 | "Moving expenses for members of the Armed Forces" | Part II Line 14 |
| 15 | "Deductible part of self-employment tax" | Part II Line 15 |
| 16 | "Self-employed SEP, SIMPLE, and qualified plans" | Part II Line 16 |
| 17 | "Self-employed health insurance deduction" | Part II Line 17 |
| 18 | "Penalty on early withdrawal of savings" | Part II Line 18 |
| 19a | "Alimony paid" | Part II Line 19a |
| 19b | "Recipient's SSN" | Part II Line 19b |
| 19c | "Date of original divorce or separation agreement" | Part II Line 19c |
| 20 | "IRA deduction" | Part II Line 20 |
| 21 | "Student loan interest deduction" | Part II Line 21 |
| 22 | (always blank) | (skip) |
| 23 | "Archer MSA deduction" | Part II Line 23 |
| 24a-24k | Sub-line text fields for each adjustment type | Part II Lines 24a-24k |
| 24z | "Other adjustments — list type and amount" | Part II Line 24z |
| 25 | (auto-computed) | Verify equals draft Line 25 |
| 26 | (auto-computed) | Verify equals draft Line 26 |

   The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records.

9. **Attach related forms** if the draft requires them:
   - Form 8889 if Line 13 > 0
   - Form 3903 if Line 14 > 0
   - Schedule SE if Line 15 > 0
   - Form 2106 if Line 12 > 0
   - Form 8853 if Line 23 > 0
   - Schedule C if Line 3 ≠ 0
   - Schedule E if Line 5 ≠ 0
   - Schedule F if Line 6 ≠ 0

10. **Run FFFF's "Check Form" / "Verify" tool** — resolve every flag before submission.

11. **Cross-check** every auto-computed field against the draft. If FFFF's number disagrees with the draft, **stop**; one of the two is wrong. Don't override blindly.

12. **Cross-check Form 1040 receipt of Schedule 1 totals**:
    - Form 1040 Line 8 should equal Schedule 1 Line 10
    - Form 1040 Line 10 should equal Schedule 1 Line 26

13. **Save the return** (FFFF stores progress server-side).

14. **Submit** when the draft is verified, attachments are present, and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number, plus prior-year AGI for identity proof)
    - Submit

15. **Capture the submission ID** that FFFF displays. Save the screenshot.

16. **Wait 24-48 hours**, then log back in to confirm IRS acceptance.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 14
- Do not bypass FFFF's verification (step 10) even if it looks like a false positive
- Do not file FFFF for a tax year where the user has already filed
- Do not store the user's SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Pull IRS transcript at https://www.irs.gov/individuals/get-transcript |
| "Form not yet supported" | Filing too early in the season | Wait until late January |
| "Math error on Line N" | Draft and FFFF disagree | Recompute draft; one is wrong |
| Session timeout | Idle > 30 min | FFFF saves progress; log back in |
| "Missing Schedule SE" | Line 15 used but Schedule SE not attached | Add Schedule SE before resubmitting |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is wizard-based:

1. Sign in → start or resume a return
2. The wizard typically asks separate questions for each Schedule 1 input rather than presenting Schedule 1 directly:
   - "Did you receive unemployment?" → Line 7
   - "Did you have self-employment income?" → routes to Schedule C wizard → Line 3
   - "Did you contribute to an HSA?" → Form 8889 wizard → Line 13
   - "Did you pay student loan interest?" → Line 21 with phaseout calc
   - "Did you contribute to a SEP, SIMPLE, or solo 401(k)?" → Line 16
   - "Did you pay self-employed health insurance?" → Line 17
   - "Did you receive a 1099-K for personal items?" → top-of-form 1099-K line
3. After the wizard, most software shows a "Schedule 1 review" or "Adjustments review" screen. Verify each line against the draft. Override anything that disagrees.
4. Software computes Line 10 and Line 26 automatically; the agent's role is verifying the source amounts feeding those lines, not the totals.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. Rely on label text and human-readable navigation rather than DOM IDs.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

Order matters:

1. **Form 1040** (signed)
2. **Schedule 1** (no separate signature; signed via 1040)
3. **Schedule 2, 3** if applicable
4. **Schedule C** (if Line 3 of Schedule 1 ≠ 0)
5. **Schedule SE** (if Line 15 of Schedule 1 > 0)
6. **Schedule E** (if Line 5 of Schedule 1 ≠ 0)
7. **Schedule F** (if Line 6 of Schedule 1 ≠ 0)
8. **Form 8889** (if Line 13 of Schedule 1 > 0)
9. **Form 3903** (if Line 14 of Schedule 1 > 0)
10. **Form 2106** (if Line 12 of Schedule 1 > 0)
11. **Form 8853** (if Line 23 of Schedule 1 > 0)
12. **All other schedules and forms** in attachment-sequence order
13. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
14. **1099s with federal withholding** also stapled

Use a single staple in the upper-left corner. Schedule 1's attachment sequence number is **01**.

### Mailing addresses

The IRS mailing address depends on the filer's state and whether payment is enclosed. Look up the current-year address at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they shift between years.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502)
- Postmark by April 15 (or extension date if Form 4868 filed)
- Keep a complete photocopy of the entire return for the user's records
- If paying, attach Form 1040-V with check made out to "United States Treasury"

### Producing the printable PDF

If the agent has access to the IRS fillable PDFs:

1. Download Schedule 1 from https://www.irs.gov/pub/irs-pdf/f1040s1.pdf
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms — `f1_3` etc.)
4. Save as flattened PDF for printing

---

## Section 4 — Submission state machine

After filing, the user's return moves through:

1. **Submitted** → sent to IRS
2. **Accepted** → IRS acknowledges receipt and basic validation passed
3. **Processed** → IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Amended-return required** OR **Audit notice (CP2000, etc.)**

Status checks:

- E-file: usually Accepted within 24-48 hours
- Paper: 4-8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file this return through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Particular Schedule 1 risk**: a phaseout-sensitive adjustment (Line 21 student loan interest) computed on incomplete MAGI data may produce a different number than software's wizard. Always verify MAGI before locking in Line 21.
