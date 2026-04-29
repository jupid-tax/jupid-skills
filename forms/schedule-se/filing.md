# Filing Schedule SE (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, Browserbase) can take a completed Schedule SE draft and file it as part of the user's Form 1040. Schedule SE does not file independently — it always travels with Form 1040.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

The user picks the channel; if undecided, default to **IRS Free File Fillable Forms (FFFF)** — Schedule SE attaches cleanly there with deterministic field labels.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific.
    Schedule SE is computed automatically by the wizard once Schedule C is filled.
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's Self-Employment / Schedule SE section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Schedule SE is auto-generated from Schedule C
    inputs in nearly every paid product — the agent verifies the result.

User wants to file on paper?
  → Print Form 1040 + Schedule C + Schedule SE + supporting schedules, sign, mail.
    Use Section 3.

User wants to use IRS Direct File?
  → Note: as of early 2026, IRS Direct File supports limited Schedule C / SE
    scenarios. Check current scope before automating.
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. Outside that window, FFFF returns "season closed".

**Account model**: each tax year is a separate FFFF account.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Schedule SE draft from `SKILL.md`
- The completed Schedule C (or F, or K-1) that produced the SE earnings input
- Form 1040 inputs (filing status, dependents, W-2s if any) — Schedule SE rides on the 1040
- An email address the user controls (FFFF sends confirmations)

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** the "Start Free File Fillable Forms" link → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in** (first-time → create account; returning users only for current tax year)
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → Form 1040 landing
6. **Complete Schedule C / F / K-1 first** so Line 31 / Line 34 / Box 14 has a value
7. **Add Schedule SE**:
   - Click "Add a Form / Schedule"
   - Search "Schedule SE" or pick from the schedule list
   - The Schedule SE form opens with fields labeled by line number
8. **Fill Schedule SE from the draft** — field-by-field mapping:

| Schedule SE line | FFFF field label | Source (in draft) |
|------------------|------------------|-------------------|
| Name | "Name of person with self-employment income" | Filer name |
| SSN | "Social Security number" | Filer SSN |
| 1a | "Net farm profit" | Part I Line 1a |
| 1b | "Conservation Reserve Program payments" | Part I Line 1b |
| 2 | "Net profit or (loss) from Schedule C" | Part I Line 2 |
| 3 | (auto-computed) | Verify it equals draft Line 3 |
| 4a | "Line 3 × 0.9235" (auto-computed) | Verify Line 4a |
| 4b | "Optional method amount" | Part I Line 4b (Part II if used) |
| 4c | (auto-computed: 4a + 4b) | Verify |
| 5a | "Church employee income" | Part I Line 5a |
| 5b | (auto-computed: 5a × 0.9235) | Verify |
| 6 | (auto-computed: 4c + 5b) | Verify |
| 7 | (pre-printed: SS wage base for the year) | Match the figure for the year |
| 8a | "Total social security wages and tips (W-2 Box 3)" | Part I Line 8a |
| 8b | "Unreported tips subject to social security tax" | Part I Line 8b |
| 8c | "Wages subject to SS tax from Form 8919" | Part I Line 8c |
| 8d | (auto-computed) | Verify |
| 9 | (auto-computed: Line 7 − Line 8d) | Verify |
| 10 | (auto-computed: min(Line 6, Line 9) × 0.124) | Verify |
| 11 | (auto-computed: Line 6 × 0.029) | Verify |
| 12 | (auto-computed: Line 10 + Line 11) | Verify; flows to Schedule 2 Line 4 |
| 13 | (auto-computed: Line 12 × 0.5) | Verify; flows to Schedule 1 Line 15 |

   The agent fills each non-computed field from the draft. After each field, capture a screenshot. Most fields on Schedule SE are auto-computed by FFFF — the agent's job is to enter the inputs correctly and **verify** every computed field against the draft.

9. **Part II (only if optional method elected)**:
   - Click "Schedule SE Part II"
   - Section A (farm) — fill Lines 14, 15
   - Section B (non-farm) — fill Lines 16, 17
   - Verify the elected amount flows back to Line 4b

10. **Cross-check Schedule SE outputs feed Schedule 2 and Schedule 1**:
    - Schedule 2 Line 4 = Schedule SE Line 12
    - Schedule 1 Line 15 = Schedule SE Line 13
    - These are auto-linked in FFFF; verify the numbers match before final submission

11. **Run FFFF's "Check Form" / "Verify" tool** — flags math errors and missing required fields. Resolve every flag.

12. **Cross-check** every auto-computed field against the draft. If FFFF's number disagrees, **stop**; one of the two is wrong. Don't override blindly.

13. **Save the return** (FFFF stores progress server-side).

14. **Submit** the entire 1040 package (1040 + all schedules + all forms) when verified:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

15. **Capture the submission ID**. Save the screenshot.

16. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. On rejection, read the rejection code and fix.

### What the agent should NOT do

- Do not submit Schedule SE in isolation — it always travels with Form 1040
- Do not file Schedule SE if Line 4a < $400 and no optional method is elected
- Do not file Schedule SE for a spouse with no SE income (each spouse needs their own only if they have SE earnings)
- Do not store the user's SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Schedule SE not allowed — Line 4a below $400" | Filer doesn't owe SE tax | Remove Schedule SE from the package |
| "Line 12 disagrees with Schedule 2 Line 4" | Stale auto-link after editing inputs | Save and reopen; force recompute |
| "Line 8a exceeds Line 7" | W-2 SS wages > wage base (rare, multi-employer) | Confirm W-2 Box 3 is the correct figure (some employers report capped wages already) |
| "Form 8959 required" warning | Combined wages + SE > Additional Medicare Tax threshold | Add Form 8959 to the return |
| Optional method election rejected | User does not meet 2-of-3 prior years rule (non-farm) | Remove the election; verify prior-year SE earnings |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), Schedule SE is auto-generated from the Schedule C / F / K-1 sections — the user does not see the form until the review screen.

1. Sign in → start or resume a return
2. Complete the "Self-employment income" or "Business income" wizard (Schedule C)
3. The software computes Schedule SE automatically from Line 31
4. Review the "Schedule SE" line in the form summary or "View as PDF" → match against the draft
5. If the software's SE tax disagrees with the draft, find the source:
   - Wrong W-2 SS wages (Line 8a) entered in the W-2 section
   - Optional method silently elected
   - Multi-spouse return with SE income mis-attributed
6. Continue through Form 1040 review; the software files Schedule SE inside the e-file package
7. Pay the software fee; e-file

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. Rely on label text and human-readable navigation rather than DOM IDs.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, user preference).

### Assemble the return

The IRS expects this stack from top to bottom:

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in order (Schedule 2 picks up SE tax via Line 4)
3. **Schedule C** (signed)
4. **Schedule SE** (one per spouse with SE income; signed if required)
5. **Form 4562** (if Schedule C Line 13 > 0)
6. **Form 8829** (if Schedule C Line 30 used regular method)
7. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
8. **W-2 Copy B** stapled to the front of Form 1040
9. **1099s with federal withholding** also stapled

Single staple, upper-left corner. Letter paper, single-sided.

### Mailing addresses (verify each year)

The IRS posts current-year addresses at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Look up by tax form (1040), with/without payment, and filer's state. Do not hardcode — addresses shift annually.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy
- If paying SE tax with the return, attach Form 1040-V payment voucher

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **CP2000 / audit notice**

Status checks:

- E-file: Accepted within 24–48 hours typically
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission.

---

## Section 5 — Quarterly estimated tax (Form 1040-ES)

SE tax is part of total federal tax owed. If the filer expects ≥ $1,000 in tax owed at year-end, they must pay quarterly estimates (IRC §6654). Schedule SE feeds the estimate calculation.

The agent should remind the filer:

- Q1 due April 15
- Q2 due June 15
- Q3 due September 15
- Q4 due January 15 of the following year
- Estimate = (expected SE tax + expected income tax − expected withholding) ÷ 4

Form 1040-ES has its own skill — see the (forthcoming) `form-1040-es` skill for full coverage.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. Capture: "I authorize you to file Form 1040 (with Schedule SE) through FFFF on my behalf right now."
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
