# Filing Form 1040 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 1040 draft and actually file it. This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, including every required schedule (Schedule 1, 2, 3, plus form-specific schedules), then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

The user picks the channel. If they don't know, default to **IRS Free File Fillable Forms (FFFF)** — it's the canonical "fill out the form online" option directly with the IRS, free, and the field labels match the paper form 1:1.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Verify the 2026 AGI threshold at https://www.irs.gov/filing/free-file-do-your-federal-taxes-for-free
    Browser automation: provider-specific (TaxAct Free, FreeTaxUSA, etc.)
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has a simple return (W-2 only, no Schedule C, eligible state)?
  → IRS Direct File
    Verify the 2026 state list and supported scenarios at https://directfile.irs.gov
    As of early 2026, Direct File does NOT support Schedule C self-employment.
    Eligibility check is the first decision; if unsupported, redirect to FFFF or commercial software.
    Use Section 4 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer)?
  → That software's 1040 flow
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Don't write provider-specific flows here.

User wants to file on paper?
  → Print Form 1040 + all schedules + supporting forms, sign, mail
    "Browser automation": prepare the printable PDF + look up the current mailing address.
    Use Section 3.
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
- Spouse's name, SSN, DOB if MFJ
- The completed Form 1040 draft from `SKILL.md`
- All required schedules already drafted (Schedule 1, 2, 3, A/B/C/D/E as needed, SE if applicable, Forms 8995, 8812, 2441, 8863, 8889 as needed)
- An email address the user controls (FFFF sends confirmations)
- An IP address the user is willing to file from (FFFF logs the submission IP)
- Bank routing + account numbers if expecting a refund via direct deposit (collect at submission time, do not store)

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** the "Start Free File Fillable Forms" link → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in**:
   - First-time: click "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: FFFF asks for prior-year AGI or a self-select PIN. If the user doesn't have prior-year AGI handy, retrieve from IRS transcript via Form 4506-T or pause and ask.
5. **Start a new return** → Form 1040 is the default form for individual returns.
6. **Fill Form 1040 header** — field-by-field crosswalk:

| 1040 line | FFFF field label | Source (in draft) |
|-----------|------------------|-------------------|
| Filing status | Five radio buttons | Header |
| Your first name + MI | "Your first name and middle initial" | Header |
| Your last name | "Last name" | Header |
| Your SSN | "Your social security number" | Header |
| Spouse first name + MI | (only enabled MFJ/MFS) | Header |
| Spouse last name | (only enabled MFJ/MFS) | Header |
| Spouse SSN | (only enabled MFJ/MFS) | Header |
| Address | "Home address (number and street)" | Header |
| Apt | "Apt. no." | Header |
| City, State, ZIP | "City, town, or post office" | Header |
| Foreign country / province / postal code | (only if foreign address) | Header |
| Presidential Election | "Check here if you... want $3 to go to this fund" | Header |
| Digital assets | "At any time during 2025, did you..." Yes/No | Header |
| Standard deduction boxes | "Someone can claim... You as a dependent" / spouse / dual-status | Header |
| Age/blindness | "You: born before January 2, 1961 / Blind" + spouse equivalents | Header |
| Dependents grid | "First name", "Last name", "SSN", "Relationship", "CTC", "ODC" per row | Header dependents table |

7. **Fill Page 1 — Income** — field-by-field:

| 1040 line | FFFF field label | Source (in draft) |
|-----------|------------------|-------------------|
| 1a | "Total amount from Form(s) W-2, box 1" | Page 1 Line 1a |
| 1b | "Household employee wages..." | Line 1b |
| 1c | "Tip income not reported on line 1a" | Line 1c |
| 1d | "Medicaid waiver payments..." | Line 1d |
| 1e | "Taxable dependent care benefits..." | Line 1e |
| 1f | "Employer-provided adoption benefits..." | Line 1f |
| 1g | "Wages from Form 8919, line 6" | Line 1g |
| 1h | "Other earned income" | Line 1h |
| 1i | "Nontaxable combat pay election" | Line 1i |
| 1z | (auto-computed) | (verify it equals draft 1z) |
| 2a | "Tax-exempt interest" | Line 2a |
| 2b | "Taxable interest" | Line 2b |
| 3a | "Qualified dividends" | Line 3a |
| 3b | "Ordinary dividends" | Line 3b |
| 4a | "IRA distributions" | Line 4a |
| 4b | "Taxable amount" | Line 4b |
| 5a | "Pensions and annuities" | Line 5a |
| 5b | "Taxable amount" | Line 5b |
| 6a | "Social security benefits" | Line 6a |
| 6b | "Taxable amount" | Line 6b |
| 6c | (checkbox if lump-sum election) | Line 6c |
| 7 | "Capital gain or (loss)" | Line 7 |
| 8 | "Additional income from Schedule 1, line 10" | Line 8 |
| 9 | (auto-computed) | (verify) |
| 10 | "Adjustments to income from Schedule 1, line 26" | Line 10 |
| 11 | (auto-computed = AGI) | (verify) |
| 12 | "Standard deduction or itemized deductions" | Line 12 |
| 13 | "Qualified business income deduction" | Line 13 |
| 14 | (auto-computed) | (verify) |
| 15 | (auto-computed = taxable income) | (verify) |

8. **Fill Page 2 — Tax, Credits, Payments**:

| 1040 line | FFFF field label | Source (in draft) |
|-----------|------------------|-------------------|
| 16 | "Tax" + checkbox for method (8814/4972/other) | Line 16 |
| 17 | "Amount from Schedule 2, line 3" | Line 17 |
| 18 | (auto-computed) | (verify) |
| 19 | "Child tax credit or credit for other dependents" | Line 19 |
| 20 | "Amount from Schedule 3, line 8" | Line 20 |
| 21 | (auto-computed, floored at 0) | (verify) |
| 22 | "Other taxes, from Schedule 2, line 21" | Line 22 |
| 23 | (auto-computed = total tax) | (verify) |
| 25a | "Federal income tax withheld from Form W-2" | Line 25a |
| 25b | "...Form(s) 1099" | Line 25b |
| 25c | "Other forms" | Line 25c |
| 26 | "2025 estimated tax payments..." | Line 26 |
| 27 | "Earned income credit (EIC)" | Line 27 |
| 28 | "Additional child tax credit from Schedule 8812" | Line 28 |
| 29 | "American opportunity credit from Form 8863, line 8" | Line 29 |
| 31 | "Amount from Schedule 3, line 15" | Line 31 |
| 32 | (auto-computed) | (verify) |
| 33 | (auto-computed = total payments) | (verify) |
| 34 | "If line 33 is more than line 23, subtract line 23 from line 33" | Line 34 |
| 35a | "Amount of line 34 you want refunded to you" | Line 35a |
| 35b | "Routing number" | (collected at filing time) |
| 35c | (Checking / Savings radio) | (collected at filing time) |
| 35d | "Account number" | (collected at filing time) |
| 36 | "Amount of line 34 you want applied to your 2026 estimated tax" | Line 36 |
| 37 | "Subtract line 33 from line 23. This is the amount you owe" | Line 37 |
| 38 | "Estimated tax penalty" | Line 38 |

   The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records.

9. **Add required schedules** — for each schedule in the draft's "Required attachments" list:
   - Click "Add a Form / Schedule" or the equivalent
   - Search by name (e.g., "Schedule 1", "Schedule C", "Form 8995")
   - Fill the schedule from the corresponding sibling skill's draft (e.g., from `schedule-c` skill output)
   - Confirm the schedule's bottom-line number flows to the correct 1040 line

10. **Run FFFF's "Check Form" / "Verify" tool** — it flags math errors and missing required fields. Resolve every flag before submission. Pay special attention to:
    - Cross-form math (Schedule C Line 31 → Schedule 1 Line 3 → 1040 Line 8)
    - SE tax flow (Schedule SE → Schedule 2 Line 4 → 1040 Line 22)
    - QBI flow (Form 8995 Line 15 → 1040 Line 13)
    - CTC flow (Schedule 8812 Line 14 → 1040 Line 19; Line 27 → 1040 Line 28)

11. **Cross-check** every auto-computed field on 1040 against the draft. If FFFF's number disagrees with the draft, **stop**; one of the two is wrong. Don't override blindly.

12. **Save the return** (FFFF stores progress server-side; the user can resume).

13. **Submit** when the draft is verified, all schedules are present, and the user has explicitly authorized:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number the user picks, plus prior-year AGI for identity proof). MFJ: both spouses sign with their own PINs.
    - Submit

14. **Capture the submission ID** that FFFF displays. Save the screenshot.

15. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. FFFF emails an acceptance or rejection notice. On rejection, read the rejection code and fix:
    - **R0000-194** — duplicate SSN (someone else filed using this SSN; possible identity theft)
    - **R0000-902** — taxpayer info doesn't match SSA records (often a name mismatch)
    - **IND-031-04** — prior-year AGI doesn't match IRS records
    - **F1040-525** — dependent SSN already claimed on another return

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 13
- Do not bypass FFFF's verification (step 10) even if it looks like a false positive
- Do not file FFFF for a tax year where the user has already filed (FFFF will reject; trying creates a duplicate-filing audit flag)
- Do not store the user's SSN, DOB, PIN, or bank account numbers in any log or transcript
- Do not save the user's prior-year AGI longer than the active filing session

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Ask user for IRS transcript (https://www.irs.gov/individuals/get-transcript) |
| "Form not yet supported" | Filing too early in the season | Wait until late January |
| "Math error on Line N" | Draft and FFFF disagree | Recompute draft; one is wrong |
| Session timeout | Idle > 30 min | FFFF saves progress; log back in |
| MFA / CAPTCHA | Routine | Pause for user input |
| Dependent SSN already claimed | Other parent filed first | Cannot overwrite via FFFF; user must paper-file with documentation |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is:

1. Sign in → start or resume a return
2. The wizard typically opens with personal info: name, SSN, filing status, dependents
3. Income section: import W-2s by EIN + control number, or enter manually. Same for 1099s.
4. The software asks the user a wizard-style series of questions; the agent maps wizard answers from the draft:
   - "Did you have any self-employment income?" → if Schedule C, yes
   - "Did you sell stocks or crypto?" → if Schedule D / Form 8949, yes
   - "Do you have kids?" → flows to dependents grid + CTC
   - "Did you pay for childcare?" → Form 2441
   - "Did you pay college tuition?" → Form 8863 + 1098-T
5. The software produces a "Federal Review" or "Form 1040 summary" screen — verify each line against the draft. Override anything that disagrees.
6. State return follows federal — the agent should confirm state inputs match before submission.
7. Pay the software fee; e-file federal + state.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. An agent should rely on label text (visible to the user) and human-readable navigation rather than DOM IDs that break each January. If the user has a specific provider, the agent can ask the user to point to the relevant screens by URL or screenshot.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns, large estate amendments).

### Assemble the return

Order matters — the IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule A** (if itemizing)
4. **Schedule B** (if interest + dividends > $1,500 or foreign accounts)
5. **Schedule C** (if self-employed)
6. **Schedule D + Form 8949** (if capital gains)
7. **Schedule E** (if rentals / K-1)
8. **Schedule SE** (if self-employment net earnings > $400)
9. **Form 8995 / 8995-A** (if QBI deduction)
10. **Schedule 8812** (if CTC claimed)
11. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
12. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
13. **1099s with federal withholding** also stapled

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
- If paying, attach **Form 1040-V** payment voucher with check made out to "United States Treasury", with SSN + "Form 1040" + tax year written on the check memo line. Do not staple the check to the return.

### Producing the printable PDF

If the agent has access to the IRS fillable PDFs:

1. Download the latest revision of each required form from https://www.irs.gov/forms-instructions
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (which are stable on IRS forms — `f1_3` etc.)
4. Save as flattened PDF for printing

---

## Section 4 — IRS Direct File

URL: https://directfile.irs.gov

Direct File launched as a pilot in 2024 and expanded for the 2026 filing season. Verify the current state list and supported scenarios before relying on it.

### Eligibility (verify for current year)

As of early 2026, Direct File supports:
- W-2 wages
- Social Security and railroad retirement
- Unemployment compensation
- Interest income
- Limited credits (CTC, EITC, Saver's, ACTC, Premium Tax Credit, Credit for Other Dependents)
- Limited adjustments (HSA, educator expenses, student loan interest)
- Standard deduction only (no itemized)

Direct File does **NOT** support (as of early 2026):
- Schedule C self-employment income
- Schedule D capital gains beyond limited categories
- Schedule E rental / passthrough income
- Itemized deductions
- AMT, NIIT, Additional Medicare Tax

For self-employed filers, this skill's user almost always falls outside Direct File scope. Redirect to FFFF or commercial software.

### Browser flow (eligible users only)

1. Navigate to https://directfile.irs.gov
2. Sign in via ID.me or Login.gov
3. Run the eligibility check — Direct File asks structured questions and self-disqualifies the user if they fall outside scope
4. Complete the wizard sections: Personal info → Family/dependents → Income → Deductions/credits → Review
5. Submit electronically; signs via ID.me identity verification (no separate PIN)
6. Receive submission confirmation

The agent should not attempt Direct File if the eligibility check fails — fall back to FFFF or commercial software.

---

## Section 5 — Submission state machine

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

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 1040 through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, or bank account numbers** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If the IRS or software asks the user to prove identity, pause and let the user respond directly.
4. **Always show the diff** between the draft from `SKILL.md` and what's about to be submitted. The user must see and confirm any change.
5. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
6. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
7. **MFJ requires both spouses' PINs** — the agent must collect both and confirm both spouses authorize filing.
