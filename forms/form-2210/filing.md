# Filing Form 2210 (browser automation)

How an agent equipped with browser tooling can take a completed Form 2210 draft and actually file it. Form 2210 attaches to Form 1040 — it is **never filed standalone**.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

Form 2210 is unusual in that **the filer does not always have to file it even when a penalty is owed**. The IRS will compute the penalty automatically and bill the filer post-processing. Form 2210 is filed only when a Part II box applies (2025 Form 2210, page 1):

1. Box A — waiver of the entire penalty (page 1 only), OR
2. Box B — waiver of part of the penalty (figure the penalty), OR
3. Box C — Schedule AI (annualized income installment method) reduces the penalty, OR
4. Box D — withholding treated as paid on the dates actually withheld, OR
5. Box E — joint return for 2024 or 2025 but not both, and line 8 is smaller than line 5 (page 1 only)

Tax software may compute Form 2210 automatically; it should attach the form only in these cases.

```
Did the SKILL.md flowchart resolve to "no penalty / no Form 2210 needed"?
  Yes → No filing needed; produce the no-penalty confirmation and stop
  No  → continue

Does any Part II box (A–E) apply?
  Yes → Form 2210 must be filed (page 1 only for A or E alone); use the channel below
  No  → Don't file Form 2210. Either let IRS compute (leave Form 1040 line 38 blank)
        or figure the penalty on Form 2210 as a worksheet and enter it on line 38
        without attaching the form. Default: let IRS compute (simpler); but verify
        any penalty estimate flag from tax software so the filer knows what to expect

User has AGI ≤ $89,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific
    Skip — proprietary flows change too often

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic
    Use Section 1 below.

User has already paid for tax software?
  → That software's "Other Taxes" / "Underpayment Penalty" section
    Browser automation: provider-specific
    Use Section 2 (generic pattern)

User wants to file on paper?
  → Print Form 1040 + Form 2210 + Schedule AI (if used), sign, mail
    Use Section 3.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: FFFF is open from late January through mid-October each year (the 2026 season closes Oct. 15, 2026, per the IRS FFFF page). Outside that window, paper or wait.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials — register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 2210 draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, all W-2s, all schedules)
- An email address the user controls
- An IP address the user is willing to file from

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** the "Start Free File Fillable Forms" link
3. **Register / Sign in**:
   - First-time: click "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → "Form 1040" landing
6. **Fill Form 1040 main return** (header, income, deductions, credits, other taxes including Schedule 2 if applicable)
7. **Add Form 2210** by clicking "Add a Form / Schedule" or equivalent
8. **Fill Form 2210 from the draft** — field-by-field mapping:

| Form 2210 field | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name(s) | "Name(s) shown on return" | matches Form 1040 header |
| SSN | "Your social security number" | filer SSN |
| Part I Line 1 | Form 1040 line 22 amount | Part I Line 1 |
| Part I Lines 2–3 | Other taxes; refundable credits | Part I Lines 2–3 |
| Part I Line 4 | (auto-computed subtotal) | (verify) |
| Part I Line 5 | (auto-computed: Line 4 × 90%) | (verify) |
| Part I Line 6 | "Withholding" | Part I Line 6 |
| Part I Line 7 | (auto-computed) | (verify) |
| Part I Line 8 | "100% of prior-year tax" or "110% if AGI > $150K" | Part I Line 8 (verify which threshold) |
| Part I Line 9 | (auto-computed: smaller of Line 5 or Line 8) | (verify) |
| Part II checkboxes | Box A / B / C / D / E | Part II selection (if any) |
| Part II explanation | "Explanation" textarea | Written explanation if waiver claimed |
| Part III quarterly columns | Each quarter's installment / payments / underpayment | Part III table from draft |
| Part III penalty | (auto-computed if FFFF supports; otherwise manual) | Penalty computation table |

   FFFF behavior on Form 2210 has historically been less polished than other forms — it may not auto-compute the daily penalty rate. The agent should verify each penalty figure manually against the draft.

9. **Schedule AI (if used)**:
   - Click "Schedule AI" tab/section within Form 2210
   - Fill the four columns (a/b/c/d) for the quarter-end periods
   - Each column requires cumulative AGI, deductions, tax computation
   - The annualization factors (4 / 2.4 / 1.5 / 1) are usually pre-applied by FFFF; verify

10. **Verify Form 1040 Line 38**: the penalty from Form 2210 line 19 should flow here. With box B, line 19 is the penalty after subtracting the waived amount (shown in parentheses next to line 19). With box A or box E alone, only page 1 is filed, the penalty is not figured, and line 38 is left blank.

11. **Run FFFF's "Check Form" / "Verify" tool** — resolve every flag.

12. **Cross-check** every figure against the draft. If FFFF disagrees with the draft by more than $1, **stop**; investigate.

13. **Save the return**.

14. **Submit** when verified:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

15. **Capture the submission ID** that FFFF displays.

16. **Wait 24–48 hours**, then log back in to confirm IRS acceptance.

### What the agent should NOT do

- Do not submit without explicit user consent at step 14
- Do not bypass FFFF's verification step
- Do not store the user's SSN, DOB, or PIN in any log
- Do not file Form 2210 standalone — it requires Form 1040 as the parent return
- Do not check the Box A or B waiver without an attached written explanation

### Failure modes specific to Form 2210

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| FFFF computes a different penalty than the draft | Draft used a stale rate, or payments were applied in the wrong order | Use the rates printed in the current-year penalty worksheet (2025: 0.07 for every period) and apply payments to the earliest underpayment first |
| Schedule AI columns don't accept input | Schedule AI is tied to box C in Part II | Check box C first |
| Penalty calculated despite the de minimis exception ($1,000) | Refundable credits not entered on line 3, or estimated payments expected to count in the test | Enter refundable credits on line 3; line 7 is line 4 minus withholding only |
| Filer's prior-year tax was zero but FFFF still computes penalty | The IRC §6654(e)(2) exception has no checkbox on Form 2210 | Do not file Form 2210 — let IRS process the return without it and leave line 38 blank |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is:

1. Sign in → start or resume a return
2. Enter all income, withholding, and estimated tax payments. Most software auto-computes Form 2210 silently from these inputs.
3. After the income sections, look for the "Other Taxes" or "Underpayment Penalty" review screen.
4. The software will typically:
   - Show a "Form 2210 — Underpayment of Estimated Tax" screen
   - Ask whether to use the annualized income installment method (yes/no)
   - Ask whether to claim a waiver (yes/no)
   - Compute the penalty and display it
5. **Verify against the draft**:
   - Find Form 2210 in the software's "Forms view"
   - Match Line 9 (required annual payment), Part III quarterly underpayments, and the total penalty
6. If the software's number disagrees with the draft by > $5, investigate before filing. Common causes:
   - Wrong prior-year AGI entered (changes the 100% / 110% threshold)
   - Withholding not allocated correctly across quarters
   - Estimated payments missing or with wrong dates
   - Different penalty rate (software may have updated; draft may be stale)
7. Decide whether to attach Form 2210 to the return:
   - Most software defaults to "let IRS compute" if the regular method gives the smallest penalty
   - Override to attach Form 2210 if claiming Schedule AI or a waiver, or if box D or E applies
8. Continue through Form 1040 review; software computes Line 38.
9. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. Form 2210 specifically often requires the filer to *opt in* to the annualized method — many filers miss this and pay more than necessary.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns, or large Schedule AI worksheet that's easier on paper).

### Assemble the return

Order matters — IRS expects this stack:

1. **Form 1040** (signed, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Form 2210** with **Schedule AI** stapled behind it (if used)
4. **Written waiver explanation** (if Box A or B checked)
5. **All other schedules and forms** in attachment-sequence order
6. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)

Use a single staple in the upper-left corner. Don't paperclip.

### Mailing addresses (verify each year)

The IRS mailing address for paper Form 1040 with payment differs from without payment, and varies by state. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they shift between years.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy of the entire return for the user's records
- If paying, attach Form 1040-V payment voucher with check made out to "United States Treasury", with SSN + "Form 1040" + tax year on the memo line

### Producing the printable PDF

If the agent has access to the IRS fillable PDFs:

1. Download the latest revision of Form 2210 (and Schedule AI within it) from https://www.irs.gov/forms-pubs/about-form-2210
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms)
4. Save as flattened PDF for printing

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice (with penalty if Form 2210 was not attached)** OR **Amended-return required** OR **Audit notice**

**Penalty bill timing**:
- If Form 2210 was attached: penalty is settled with the return
- If Form 2210 was NOT attached but penalty is owed: IRS sends a CP30 notice (https://www.irs.gov/individuals/understanding-your-cp30-notice) with the penalty amount, or includes it on a CP14 balance-due notice; no interest is charged on the penalty if it is paid by the date on the bill and the return was filed by April 15 (2025 Instructions for Form 2210)
- If filer disagrees with IRS-computed penalty: file Form 843 (Claim for Refund and Request for Abatement) with documentation

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status, and a 60-day reminder to check for any IRS-computed penalty notice if Form 2210 was not attached.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 2210 along with my Form 1040 through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.**
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (penalty math disagreement, unexpected screen, MFA failures), **stop and surface the issue**.
6. **Show the diff** between draft and final FFFF/software state to the user before submission.
7. **Before claiming a waiver via Box A or B**, confirm the filer can substantiate the waiver basis with documentation. The IRS will request supporting evidence (medical records, casualty documentation, retirement letter) if it processes the waiver claim.
