# Filing Schedule C (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Schedule C draft and actually file it. This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

The user picks the channel. If they don't know, default to **IRS Free File Fillable Forms (FFFF)** — it's the canonical "fill out the form online" option directly with the IRS, free, and the field labels match the paper form 1:1, which makes browser automation deterministic.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific (TaxAct Free, FreeTaxUSA, etc.)
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's Schedule C section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Don't write provider-specific flows here.

User wants to file on paper?
  → Print Form 1040 + Schedule C + supporting schedules, sign, mail
    "Browser automation": prepare the printable PDF + give mailing address.
    Use Section 3.

User wants to use IRS Direct File?
  → Note: as of early 2026, IRS Direct File supports limited Schedule C scenarios.
    Check current scope before automating. If unsupported, redirect to FFFF or paper.
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: FFFF is open from late January through mid-October each year. Outside that window, it returns a "season closed" message and the agent must fall back to paper or wait.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials — the agent must register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Schedule C draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, W-2s if any, etc.) — Schedule C alone isn't a return; it attaches to a 1040
- An email address the user controls (FFFF sends confirmations)
- An IP address the user is willing to file from (FFFF logs the submission IP)

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** the "Start Free File Fillable Forms" link → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in**:
   - First-time: click "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: FFFF asks for prior-year AGI or a self-select PIN. If the user doesn't have prior-year AGI handy, retrieve from IRS transcript via Form 4506-T or pause and ask.
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Schedule C**:
   - Click "Add a Form / Schedule" or the equivalent
   - Search "Schedule C" or pick from the schedule list
   - The Schedule C form opens with fields labeled by line number (matching paper form)
8. **Fill Schedule C from the draft** — field-by-field mapping:

| Schedule C line | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name of proprietor | "Name of proprietor" | Filer name |
| SSN | "Social Security number" | Filer SSN |
| A | "Principal business or profession" | Header A |
| B | "Business code" | Header B (6 digits) |
| C | "Business name" | Header C |
| D | "Employer ID number (EIN)" | Header D (or blank) |
| E | "Business address" | Header E |
| F | "Accounting method" — Cash / Accrual / Other radio | Header F |
| G | "Did you 'materially participate'..." Yes/No radio | Header G |
| H | "If you started or acquired this business in 2025, check here" | Header H checkbox |
| I | "Did you make any payments..." Yes/No radio | Header I |
| J | "If 'Yes,' did you or will you file required Form(s) 1099?" | Header J |
| 1 | "Gross receipts or sales" | Part I Line 1 |
| 2 | "Returns and allowances" | Part I Line 2 |
| 3 | (auto-computed) | (verify it equals draft Line 3) |
| 4 | "Cost of goods sold" | Part I Line 4 (= Part III Line 42) |
| 5 | (auto-computed) | (verify) |
| 6 | "Other income" | Part I Line 6 |
| 7 | (auto-computed) | (verify) |
| 8 | "Advertising" | Part II Line 8 |
| 9 | "Car and truck expenses" | Part II Line 9 |
| 10 | "Commissions and fees" | Part II Line 10 |
| 11 | "Contract labor" | Part II Line 11 |
| 12 | "Depletion" | Part II Line 12 |
| 13 | "Depreciation and section 179 expense deduction" | Part II Line 13 |
| 14 | "Employee benefit programs" | Part II Line 14 |
| 15 | "Insurance (other than health)" | Part II Line 15 |
| 16a | "Mortgage (paid to banks, etc.)" | Part II Line 16a |
| 16b | "Other interest" | Part II Line 16b |
| 17 | "Legal and professional services" | Part II Line 17 |
| 18 | "Office expense" | Part II Line 18 |
| 19 | "Pension and profit-sharing plans" | Part II Line 19 |
| 20a | "Vehicles, machinery, and equipment" rent | Part II Line 20a |
| 20b | "Other business property" rent | Part II Line 20b |
| 21 | "Repairs and maintenance" | Part II Line 21 |
| 22 | "Supplies" | Part II Line 22 |
| 23 | "Taxes and licenses" | Part II Line 23 |
| 24a | "Travel" | Part II Line 24a |
| 24b | "Deductible meals" | Part II Line 24b |
| 25 | "Utilities" | Part II Line 25 |
| 26 | "Wages (less employment credits)" | Part II Line 26 |
| 27a | "Other expenses (from line 48)" | Part II Line 27a |
| 28 | (auto-computed) | (verify) |
| 29 | (auto-computed) | (verify) |
| 30 | "Expenses for business use of your home" | Line 30 (with method indicator) |
| 31 | (auto-computed) | (verify Line 31) |
| 32 | If loss, "32a" or "32b" radio | Line 32 |

   The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records (the user may want to verify visually before submission).

9. **Part III (COGS) — only if Line 4 > 0**:
   - Click "Schedule C Part III" tab/expand
   - Fill Lines 33 (radio for inventory method), 34 (Yes/No radio), 35–41 (numeric)
   - Line 42 auto-computes
10. **Part IV (Vehicle) — only if Line 9 > 0 and not depreciating on Form 4562**:
    - Fill Lines 43 (date), 44a–44c (mileage breakdown), 45–47 (Yes/No radios)
11. **Part V (Other Expenses) — only if Line 27a > 0**:
    - Click "Add row" for each Part V item
    - Each row: Description (text) + Amount (numeric)
    - Sum at Line 48 must match Line 27a
12. **Attach related forms** if the draft requires them:
    - Form 4562 if Line 13 > 0 — separate FFFF form, fill before final submission
    - Form 8829 if Line 30 used regular method — separate FFFF form
    - Schedule SE if Line 31 > $400 — separate FFFF form
13. **Run FFFF's "Check Form" / "Verify" tool** — it flags math errors and missing required fields. Resolve every flag before submission.
14. **Cross-check** every auto-computed field against the draft. If FFFF's number disagrees with the draft, **stop**; one of the two is wrong. Don't override blindly.
15. **Save the return** (FFFF stores progress server-side; the user can resume).
16. **Submit** when the draft is verified, attachments are present, and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number the user picks, plus prior-year AGI for identity proof)
    - Submit
17. **Capture the submission ID** that FFFF displays. Save the screenshot.
18. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. FFFF emails an acceptance or rejection notice. On rejection, read the rejection code (e.g., R0000-194 = duplicate SSN), fix, resubmit.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 16
- Do not bypass FFFF's verification (step 13) even if it looks like a false positive
- Do not file FFFF for a tax year where the user has already filed (FFFF will reject; trying creates a duplicate-filing audit flag)
- Do not store the user's SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Ask user for IRS transcript (https://www.irs.gov/individuals/get-transcript) |
| "Form not yet supported" | Filing too early in the season | Wait until late January |
| "Math error on Line N" | Draft and FFFF disagree | Recompute draft; one is wrong |
| Session timeout | Idle > 30 min | FFFF saves progress; log back in |
| MFA / CAPTCHA | Routine | Pause for user input |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is:

1. Sign in → start or resume a return
2. Navigate to "Self-employment" / "Business income" / "Schedule C" section
3. The software asks the user a wizard-style series of questions; the agent maps wizard answers from the draft:
   - "Did you have any 1099-NEC income?" → from Income table
   - "Did you have any 1099-K income?" → from Income table
   - "What kind of business?" → A/B header
   - "Where do you do business?" → E header
   - "Do you have a home office?" → Line 30
   - "Did you drive for business?" → Line 9 + Part IV
4. The wizard typically aggregates expenses by *category* with custom names that map to Schedule C lines. Use [`references/line-by-line.md`](./references/line-by-line.md) to translate.
5. After the wizard, most software shows a "Schedule C summary" or "Review Schedule C" screen — verify each line against the draft. Override anything that disagrees.
6. Continue through Form 1040 review; software computes Schedule SE automatically.
7. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. An agent should rely on label text (visible to the user) and human-readable navigation rather than DOM IDs that break each January. If the user has a specific provider, the agent can ask the user to point to the relevant screens by URL or screenshot.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, user preference, identity-theft concerns).

### Assemble the return

Order matters — the IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule C** (signed)
4. **Schedule SE** (if Line 31 > $400)
5. **Form 4562** (if Schedule C Line 13 > 0)
6. **Form 8829** (if Schedule C Line 30 used regular method)
7. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
8. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
9. **1099s with federal withholding** also stapled

Use a single staple in the upper-left corner. Don't paperclip. Don't double-side print. Each form printed at full size on letter paper.

### Mailing addresses (verify each year)

The IRS mailing address for paper Form 1040 *with payment* differs from *without payment*, and varies by state. The IRS posts the current-year addresses at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

The agent must look up the current address by:
1. Tax form (1040)
2. With or without payment
3. Filer's state

Do not hardcode addresses — they shift between years and are split by state.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502 timely-mailing-as-timely-filing rule)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy of the entire return for the user's records
- If paying, attach Form 1040-V payment voucher with check made out to "United States Treasury", with SSN + "Form 1040" + tax year written on the check memo line

### Producing the printable PDF

If the agent has access to the IRS fillable PDFs, the deterministic flow is:

1. Download the latest revision of each required form from https://www.irs.gov/forms-instructions
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (which are stable on IRS forms — `f1_3` etc.)
4. Save as flattened PDF for printing

Form-field name lookups for Schedule C live in the IRS fillable PDF metadata; tooling like `pypdf` or `pdftk` can list them. The agent should fetch the field list once per tax year and cache.

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Amended-return required** OR **Audit notice (CP2000, etc.)**

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool, requires SSN + filing status + refund amount)
- Account transcript: https://www.irs.gov/individuals/get-transcript (shows all activity once Processed)

The agent should set a follow-up reminder 7 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Schedule C through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If the IRS or software asks the user to prove identity, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
