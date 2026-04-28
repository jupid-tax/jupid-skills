# Filing Schedule A (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Schedule A draft and actually file it. This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, run the standard-vs-itemized comparison (if standard wins, **stop** — don't file Schedule A), then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

Schedule A always attaches to Form 1040; it is never filed standalone. The channel is the same channel the user files Form 1040 through.

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
  → That software's "Deductions & Credits" / "Itemized Deductions" section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Don't write provider-specific flows here.

User wants to file on paper?
  → Print Form 1040 + Schedule A + supporting forms (4684, 4952, 8283), sign, mail
    "Browser automation": prepare the printable PDF + give mailing address.
    Use Section 3.

User wants to use IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Schedule A itemized
    deductions in any participating state. Direct File is standard-deduction-only.
    Redirect the user to FFFF, paid software, or paper.
    Verify scope before each tax year at https://www.irs.gov/filing/irs-direct-file
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
- Spouse's name and SSN if MFJ
- The completed Schedule A draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, W-2s, 1099s, etc.) — Schedule A alone isn't a return; it attaches to a 1040
- An email address the user controls (FFFF sends confirmations)
- An IP address the user is willing to file from (FFFF logs the submission IP)
- Confirmation that itemized total (Line 17) > standard deduction — otherwise don't file Schedule A at all

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
7. **Fill 1040 income lines** (W-2, interest, dividends, capital gains, etc.) so Line 11 (AGI) is computed — Schedule A's medical floor, charity floor, casualty floor, and SALT phaseout all depend on AGI, so AGI must be settled before Schedule A.
8. **Add Schedule A**:
   - Click "Add a Form / Schedule" or the equivalent
   - Search "Schedule A" or pick from the schedule list
   - The Schedule A form opens with fields labeled by line number (matching paper form)
9. **Fill Schedule A from the draft** — field-by-field mapping:

| Schedule A line | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name(s) shown on Form 1040 | "Name(s) shown on Form 1040" | Filer name(s) |
| Your social security number | "SSN" | Filer SSN |
| 1 | "Medical and dental expenses" | Lines 1-4 block, Line 1 |
| 2 | "Enter amount from Form 1040, line 11" | AGI |
| 3 | "Multiply line 2 by 7.5% (0.075)" | (auto-computed; verify) |
| 4 | "Subtract line 3 from line 1" | (auto-computed; verify) |
| 5a | "State and local income taxes or general sales taxes" | Lines 5-7 block, Line 5a |
| 5a checkbox | Check box if entry is sales taxes (not income taxes) | (from draft note) |
| 5b | "State and local real estate taxes" | Line 5b |
| 5c | "State and local personal property taxes" | Line 5c |
| 5d | "Add lines 5a through 5c" | (auto-computed; verify) |
| 5e | "Smaller of line 5d or [SALT cap]" | Line 5e (apply year-specific cap and phaseout) |
| 6 | "Other taxes" + description | Line 6 |
| 7 | "Add lines 5e and 6" | (auto-computed; verify) |
| 8a | "Home mortgage interest and points reported on Form 1098" | Line 8a |
| 8b | "Home mortgage interest not reported on Form 1098" + payee info | Line 8b (with seller name/SSN) |
| 8c | "Points not reported to you on Form 1098" | Line 8c |
| 8d | "Mortgage insurance premiums" (2026+ only) | Line 8d (or blank for 2025) |
| 8e | "Add lines 8a through 8d" | (auto-computed; verify) |
| 9 | "Investment interest" + Form 4952 attached | Line 9 |
| 10 | "Add lines 8e and 9" | (auto-computed; verify) |
| 11 | "Gifts by cash or check" | Line 11 |
| 12 | "Other than by cash or check" + Form 8283 attached if > $500 | Line 12 |
| 13 | "Carryover from prior year" | Line 13 |
| 14 | "Add lines 11 through 13" (with 0.5% AGI floor for 2026+) | Line 14 effective |
| 15 | "Casualty and theft losses" + Form 4684 attached | Line 15 |
| 16 | "Other — list type and amount" | Line 16 (with description) |
| 17 | "Add the amounts in the far right column" | (auto-computed; verify equals Form 1040 Line 12) |
| Itemize-instead-of-standard checkbox | "Check this box if you elect to itemize even though less than your standard deduction" | (almost never check; only for MFS coordination cases) |

   The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records (the user may want to verify visually before submission).

10. **Attach related forms** if the draft requires them:
    - Form 4952 if Line 9 > 0 — separate FFFF form, fill before final submission
    - Form 8283 if Line 12 > $500 — separate FFFF form
    - Form 4684 if Line 15 > 0 — separate FFFF form
11. **Confirm Form 1040 Line 12** updates to the Schedule A Line 17 amount (FFFF should auto-flow). If Form 1040 Line 12 still shows the standard deduction, the Schedule A election didn't register — recheck.
12. **Run FFFF's "Check Form" / "Verify" tool** — it flags math errors and missing required fields. Resolve every flag before submission.
13. **Cross-check** every auto-computed field against the draft. If FFFF's number disagrees with the draft, **stop**; one of the two is wrong. Don't override blindly. Common disagreements: SALT cap (FFFF may use prior-year cap if forms not yet updated for OBBBA), 0.5% charity floor (2026+), PMI deductibility (2026+).
14. **Save the return** (FFFF stores progress server-side; the user can resume).
15. **Submit** when the draft is verified, attachments are present, and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number the user picks, plus prior-year AGI for identity proof)
    - Submit
16. **Capture the submission ID** that FFFF displays. Save the screenshot.
17. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. FFFF emails an acceptance or rejection notice. On rejection, read the rejection code (e.g., R0000-194 = duplicate SSN, F8283-001 = Form 8283 missing), fix, resubmit.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 15
- Do not bypass FFFF's verification (step 12) even if it looks like a false positive
- Do not file Schedule A if Line 17 ≤ standard deduction — it's tax-neutral or harmful
- Do not file FFFF for a tax year where the user has already filed (creates a duplicate-filing audit flag)
- Do not store the user's SSN, DOB, PIN, or charity acknowledgments in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Ask user for IRS transcript (https://www.irs.gov/individuals/get-transcript) |
| "Form not yet supported" | Filing too early in the season; OBBBA-amended Schedule A may release late | Wait until late January / early February |
| "Math error on Line 5e" | FFFF using prior-year SALT cap | Verify cap = $40K (2025) / $40,400 (2026); flag IRS issue if FFFF still has $10K |
| "Math error on Line 14" | FFFF not applying 0.5% AGI floor for 2026 | Check tax year; recompute; flag if FFFF version is stale |
| "Form 8283 required but missing" | Non-cash > $500 without 8283 attached | Add Form 8283 |
| Session timeout | Idle > 30 min | FFFF saves progress; log back in |
| MFA / CAPTCHA | Routine | Pause for user input |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is:

1. Sign in → start or resume a return
2. Complete the income sections so AGI is fixed
3. Navigate to "Deductions & Credits" / "Itemized Deductions" / "Schedule A" section
4. The software asks the user a wizard-style series of questions; the agent maps wizard answers from the draft:
   - "Did you pay medical expenses out of pocket?" → from Lines 1-4
   - "Did you pay state or local taxes?" → from Lines 5-7 (the software typically auto-imports W-2 box 17)
   - "Do you own a home with a mortgage?" → from Lines 8-10 (the software typically auto-imports Form 1098)
   - "Did you make charitable contributions?" → from Lines 11-14 (cash and non-cash separated)
   - "Did you have a casualty loss in a federally declared disaster?" → from Line 15
5. Most software runs the standard-vs-itemized comparison automatically and recommends the higher of the two. Verify the recommendation matches the draft — if the draft says "itemize" and the software says "standard", check whether the software is using outdated SALT cap or missed an entry.
6. After the wizard, most software shows a "Schedule A summary" or "Review your itemized deductions" screen — verify each line against the draft. Override anything that disagrees.
7. Continue through Form 1040 review.
8. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. An agent should rely on label text (visible to the user) and human-readable navigation rather than DOM IDs that break each January. If the user has a specific provider, the agent can ask the user to point to the relevant screens by URL or screenshot.

**Special note on OBBBA-era software lag**: Some providers historically take 4–8 weeks after a major statute change to update their interview flows. For the first 2025/2026 filing season after OBBBA, double-check that the software applies the $40K/$40,400 SALT cap, the 0.5% charity floor (2026), and PMI on Line 8d (2026). If the software is using the old $10K SALT cap, the user will under-deduct; flag immediately.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, user preference, identity-theft concerns).

### Assemble the return

Order matters — the IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule A** (no separate signature; goes immediately after Schedule 3)
4. **Form 8283** (if Schedule A Line 12 > $500)
5. **Form 4684** (if Schedule A Line 15 > 0)
6. **Form 4952** (if Schedule A Line 9 > 0)
7. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner; Schedule A is sequence 07)
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

1. Download the latest revision of Schedule A from https://www.irs.gov/forms-instructions
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (which are stable on IRS forms — `f1_3` etc.)
4. Save as flattened PDF for printing

Form-field name lookups for Schedule A live in the IRS fillable PDF metadata; tooling like `pypdf` or `pdftk` can list them. The agent should fetch the field list once per tax year and cache.

---

## Section 4 — Substantiation rules (what records to keep, and for how long)

Schedule A is records-driven. The IRS routinely audits itemizers (selection rate is roughly 3-4× higher than standard-deduction filers). Required records by category:

### Medical (Lines 1-4)

- Receipts for every medical expense claimed
- Insurance EOBs showing what insurance reimbursed (only the unreimbursed amount is deductible)
- Mileage log if claiming medical mileage (date, destination, miles, purpose)
- Doctor's letter for any deduction whose medical purpose isn't obvious (e.g., capital home improvements for medical reasons, special diets, weight-loss program for a specific disease)

### SALT (Lines 5-7)

- Property tax bills (showing value-based assessment, not flat fees)
- W-2 box 17 / 1099 withholding statements / state estimated tax payment confirmations
- For sales tax: receipts (if using actual) or the IRS optional sales tax table calculation (if using table)

### Mortgage interest (Lines 8-10)

- Form 1098 from each lender
- Closing/HUD-1 statement for points paid in year of purchase
- Documentation that HELOC/equity loan was used for buy/build/improve (purchase contracts, contractor invoices)
- For seller-financed mortgages: payment ledger, amortization schedule, seller's name + SSN

### Charity (Lines 11-14)

- **Single gift < $250**: bank record (canceled check, credit card statement) OR receipt
- **Single gift ≥ $250**: contemporaneous written acknowledgment from the charity stating the gift amount and whether goods/services were provided in return — **must be received before the earlier of (a) the date the return is filed or (b) the due date including extensions**
- **Non-cash > $500**: Form 8283 + records of how FMV was determined
- **Single non-cash item > $5,000**: qualified appraisal (signed by appraiser; appraiser meets IRS-defined credentials)
- **Donated vehicles**: Form 1098-C from the charity within 30 days
- **Out-of-pocket expenses for volunteer charity work**: receipts + acknowledgment from the charity

### Casualty (Line 15)

- FEMA disaster declaration (cite by name and reference number)
- Adjusted basis records (purchase price, improvements over time)
- FMV before and after (typically appraisal or competent estimate)
- Insurance reimbursement records
- Police report for theft losses (in disaster contexts where personal property was stolen)
- Form 4684

### Retention period

- **Default**: 3 years from the date the return was filed (IRS general statute of limitations under IRC §6501)
- **Charity > $5,000**: 7 years (longer audit window for high-value non-cash gifts)
- **Property records (mortgage, basis for casualty)**: keep until 3 years after disposition of the property
- **If under-reported income > 25% of gross income**: 6-year statute applies — keep 7 years to be safe

The agent should remind the user: *"Keep these records for at least 3 years after the filing date. For charitable gifts over $5,000 and property-related records, keep 7 years."*

---

## Section 5 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Amended-return required** OR **Audit notice (CP2000, examination letter, etc.)**

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool, requires SSN + filing status + refund amount)
- Account transcript: https://www.irs.gov/individuals/get-transcript (shows all activity once Processed)

**Common Schedule A audit flags** to be ready for:

- Charitable contributions disproportionate to AGI (common DIF flag at 10%+ of AGI)
- Mortgage interest claimed without matching Form 1098 on file with IRS
- Large non-cash gifts without Form 8283
- Casualty losses without a FEMA declaration
- Itemized deductions much higher than national averages for the user's AGI band

The agent should set a follow-up reminder 7 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 1040 with Schedule A through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, charity acknowledgments, or medical receipts** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If the IRS or software asks the user to prove identity, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures, software using outdated SALT cap), **stop and surface the issue**. Don't retry blindly.
6. **Never file Schedule A when standard deduction wins.** The check at Step 12 of `SKILL.md` is non-negotiable; surface the standard-vs-itemized comparison to the user before any field is filled.
