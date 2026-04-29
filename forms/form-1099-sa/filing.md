# Filing Form 8889 (with 1099-SA inputs) — browser automation

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, Browserbase) can take a completed Form 8889 Part II draft (computed from a received 1099-SA) and file it as part of the user's Form 1040.

The 1099-SA itself is **not filed** by the recipient — it's a source document the custodian sends to both the recipient and the IRS. The recipient files **Form 8889** (HSA) or **Form 8853** (Archer / MA MSA) which incorporates the 1099-SA data.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

The user picks the channel; if undecided, default to **IRS Free File Fillable Forms (FFFF)**.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific.
    Most Free File partners support Form 8889 in their guided wizard.
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's "Health Savings Account" or "1099-SA" section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Most products auto-generate Form 8889
    from the 1099-SA + QME inputs the wizard collects.

User wants to file on paper?
  → Print Form 1040 + Form 8889 + supporting schedules, sign, mail.
    Use Section 3.

User wants to use IRS Direct File?
  → Note: as of early 2026, IRS Direct File supports limited HSA scenarios
    (depending on state and complexity). Check current scope.
    See https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. Outside that window, FFFF returns "season closed".

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI
- The 1099-SA(s) received (PDFs or transcribed boxes)
- The Form 8889 Part II draft from `SKILL.md`
- QME documentation summary (totals only; receipts are retained, not filed)
- Form 1040 inputs (filing status, dependents, W-2s)
- Email address and IRS account access

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms"
3. **Register / Sign in** (per-tax-year accounts)
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → Form 1040 landing
6. **Add Form 8889**:
   - Click "Add a Form / Schedule"
   - Search "Form 8889"
   - The Form 8889 form opens with Parts I, II, III labeled
7. **Fill Form 8889 Part II from the draft** — field-by-field mapping:

| Form 8889 Line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| Header | Name(s) shown on Form 1040 | Filer name |
| Header | Social security number of HSA beneficiary | Filer SSN |
| 14a | "Total distributions you received in YYYY from all HSAs" | Sum of Box 1 from all 1099-SAs |
| 14b | "Distributions included on line 14a that you rolled over to another HSA" | Rollover amount; usually $0 |
| 14c | (auto-computed: 14a − 14b) | Verify |
| 15 | "Qualified medical expenses paid using HSA distributions" | User-supplied QME total |
| 16 | (auto-computed: 14c − 15, floor 0) | Verify; this is the taxable portion |
| 17a | "Exception" (checkbox: age 65+, disabled, died) | Per Step 5 in SKILL workflow |
| 17b | (auto-computed: 16 × 0.20 if no exception) | Verify |

   The agent fills each non-computed field. After each field, capture a screenshot.

   **Note on Line 14b**: FFFF labels Line 14b as "Distributions you rolled over" — different from the SKILL.md draft where 14b was QME. Reconcile carefully: Form 8889 reorders these. The actual IRS Form 8889 Part II structure is:
   - 14a = Total distributions
   - 14b = Rollovers (subtract these — they're not real distributions)
   - 14c = 14a − 14b
   - 15 = QME amount
   - 16 = 14c − 15 = taxable

   The SKILL.md draft used "14b = QME" as a teaching simplification; the actual form has a rollover line in 14b. The agent must recognize this difference when transcribing.

8. **Verify auto-linking to Schedule 1 and Schedule 2**:
   - Schedule 1 Line 8f = Form 8889 Line 16 (taxable HSA distribution)
   - Schedule 2 Line 17c = Form 8889 Line 17b (20% additional tax)
   - These should auto-link in FFFF; verify before submission

9. **If Code 2 (excess contributions)**: also add Form 5329 to handle the 6% excise on the contribution side. This is a separate flow — see the (forthcoming) `form-5329` skill.

10. **If Code 4 or 5 (death of account holder, prohibited transaction)**: surface to the user that the situation is unusual and a tax pro review is recommended. Filing through FFFF is technically possible but the consequences (e.g., entire HSA deemed distributed under Code 5) merit a second opinion.

11. **Run FFFF's "Check Form" tool** — flags math errors and missing required fields. Resolve every flag.

12. **Cross-check** every auto-computed field against the draft. Stop on any disagreement.

13. **Save the return** (FFFF stores progress server-side).

14. **Submit** the entire 1040 package when verified:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

15. **Capture the submission ID**. Save the screenshot.

16. **Wait 24–48 hours**, then log back in to confirm IRS acceptance.

### What the agent should NOT do

- Do not file Form 8889 if the user did not actually have an HSA in the tax year
- Do not file the 1099-SA itself — it's a source document, not a filed form
- Do not invent QME amounts. If the user can't substantiate, the conservative answer is to treat the unsubstantiated portion as taxable.
- Do not store the user's SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 8889 requires the HSA contribution section completed" | User had contributions in addition to distributions; Part I needed | Complete Form 8889 Part I as well (or use the forthcoming `form-8889` skill) |
| "Schedule 1 Line 8f mismatch" | FFFF didn't auto-link | Manually transcribe Form 8889 Line 16 to Schedule 1 Line 8f |
| "Excess contribution flag" | Code 2 1099-SA but no Form 5329 | Add Form 5329 to handle the 6% excise |
| "Multiple HSAs not aggregated" | User has 2+ HSAs but only 1 1099-SA entered | Aggregate Box 1 from all 1099-SAs into Line 14a |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software, the flow is:

1. Sign in → start or resume a return
2. Navigate to "Health Savings Account" / "HSA distributions" / "Form 1099-SA" section
3. The wizard typically asks:
   - "Did you receive a Form 1099-SA?" → Yes
   - "What's in Box 1 (gross distribution)?" → enter Box 1
   - "What's the distribution code in Box 3?" → enter Box 3
   - "How much of the distribution was for qualified medical expenses?" → enter QME total
   - "Were you age 65 or older / disabled / did the account holder die?" → answer per Step 5
4. The software auto-generates Form 8889 Part II
5. Review the Form 8889 line-by-line in the summary screen — match against the draft
6. Continue through Form 1040 review; the software files Form 8889 inside the e-file package
7. Pay the software fee; e-file

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. Rely on label text and human-readable navigation rather than DOM IDs.

---

## Section 3 — Paper filing

Sometimes paper is the right answer.

### Assemble the return

The IRS expects this stack from top to bottom:

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in order
3. **Form 8889** (one per HSA holder; if both spouses have HSAs, two Form 8889s)
4. **Form 8853** (if Archer / MA MSA distributions)
5. **Form 5329** (if Code 2 excess contributions or other excise issues)
6. **All other schedules and forms** in attachment-sequence order
7. **W-2 Copy B** stapled to the front of Form 1040
8. **1099s with federal withholding** stapled

Single staple, upper-left corner. Letter paper, single-sided.

### Mailing addresses

Verify each year at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment by tax form (1040), with/without payment, and filer's state. Do not hardcode.

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502)
- Postmark by April 15 (or extension date)
- Keep a complete photocopy
- The 1099-SA itself is NOT mailed to the IRS by the recipient — only the resulting Form 8889 / 8853

---

## Section 4 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges and basic validation passed
3. **Processed** — fully ingested
4. **Refund issued** OR **Balance due notice** OR **CP2000 / audit notice**

Status checks:

- E-file: Accepted within 24–48 hours
- Paper: 4–8 weeks
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status.

---

## Section 5 — Receipt retention (post-filing)

The user's job after filing:

1. **Retain QME receipts** for at least 3 years from the filing date (IRC §6501 audit window).
2. **Retain the 1099-SA** with the tax-year file. The custodian also keeps a copy.
3. **Retain HSA portal "Distribution by category" report** if used for QME totals.
4. **For "shoebox" reimbursements** (claiming HSA reimbursement years after the QME was incurred — allowed under Notice 2004-50 Q&A 39): retain receipts indefinitely. The IRS may request them at any time the reimbursement is claimed.

The agent should remind the user: "Your QME receipts substantiate Line 15 on Form 8889. The IRS does not require attaching them to the return, but if audited within 3 years you'll need to produce them."

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. Capture: "I authorize you to file Form 1040 (with Form 8889) through FFFF on my behalf right now."
2. **Never store SSN, DOB, PIN, or HSA account numbers** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** Pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Never invent QME amounts.** If the user is uncertain, prompt them to consult their HSA portal or receipts. The agent does NOT estimate.
