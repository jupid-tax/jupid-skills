# Filing Form 8959 (browser automation)

How an agent equipped with browser tooling can take a completed Form 8959 draft and actually file it. This file describes deterministic flows for filing Form 8959 as part of a Form 1040 return — Form 8959 is **never filed standalone**; it always attaches to the filer's individual income tax return.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

Form 8959 attaches to Form 1040. The filer cannot e-file Form 8959 on its own — the channel decision is whichever channel handles the parent 1040 return.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific (TaxAct Free, FreeTaxUSA, etc.)
    Skip — proprietary flows change too often for deterministic automation.
    Note: most Free File partners support Form 8959 since high-income filers
    above the threshold typically exceed the Free File AGI cap anyway. The
    common case is the filer paying for tax software.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has already paid for tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's "Other Taxes" / "Additional Medicare Tax" section
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). The wizard usually auto-derives Form
    8959 from W-2 + Schedule SE inputs without an explicit Form 8959 screen.

User wants to file on paper?
  → Print Form 1040 + Form 8959 + Schedule 2 + supporting forms, sign, mail
    Use Section 3.

User wants to use IRS Direct File?
  → As of early 2026, IRS Direct File supports Form 8959 in scope. Verify
    against current Direct File scope page before automating:
    https://www.irs.gov/filing/irs-direct-file
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: FFFF is open from late January through mid-October each year. Outside that window it returns a "season closed" message and the agent must fall back to paper or wait.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials — the agent must register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 8959 draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, all W-2s, Schedule SE if applicable, all other schedules)
- An email address the user controls (FFFF sends confirmations)
- An IP address the user is willing to file from (FFFF logs the submission IP)

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** the "Start Free File Fillable Forms" link → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in**:
   - First-time: click "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: FFFF asks for prior-year AGI or a self-select PIN. If the user doesn't have prior-year AGI, retrieve from IRS transcript via Form 4506-T or pause and ask.
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header and main form** (name, SSN, filing status, dependents, W-2 wages, etc.) — that produces a Form 1040 in progress
7. **Fill Schedule SE** if the filer has self-employment income (Form 8959 Line 8 depends on Schedule SE Part I Line 6)
8. **Add Form 8959**:
   - Click "Add a Form / Schedule" or the equivalent
   - Search "Form 8959" or pick from the list under "Other Taxes"
   - The form opens with fields labeled by line number (matching paper form)
9. **Fill Form 8959 from the draft** — field-by-field mapping:

| Form 8959 field | FFFF field label | Source (in draft) |
|-----------------|------------------|-------------------|
| Name(s) | "Name(s) shown on return" | matches Form 1040 header |
| SSN | "Your social security number" | filer SSN |
| Line 1 | "Medicare wages and tips" | Part I Line 1 |
| Line 2 | "Unreported tips" | Part I Line 2 |
| Line 3 | "Wages from Form 8919" | Part I Line 3 |
| Line 4 | (auto-computed) | (verify it equals draft Line 4) |
| Line 5 | "Threshold" — usually pre-filled by FFFF based on filing status | (verify matches Step 1 threshold) |
| Line 6 | (auto-computed) | (verify) |
| Line 7 | (auto-computed) | (verify Line 7) |
| Line 8 | "Self-employment income" | Part II Line 8 (from Schedule SE Line 6) |
| Line 9 | "Threshold" | (auto-filled, same as Line 5) |
| Line 10 | (auto-pulled from Line 4) | (verify) |
| Line 11 | (auto-computed) | (verify) |
| Line 12 | (auto-computed) | (verify) |
| Line 13 | (auto-computed) | (verify) |
| Line 14 | "RRTA compensation" | Part III Line 14 (often blank) |
| Line 15 | "Threshold" | (auto-filled) |
| Line 16 | (auto-computed) | (verify) |
| Line 17 | (auto-computed) | (verify) |
| Line 18 | (auto-computed total) | (verify Line 18 = Line 7 + 13 + 17) |
| Line 19 | "Medicare tax withheld from Form W-2 Box 6" | Part V Line 19 |
| Line 20 | (auto-computed: Line 1 × 1.45%) | (verify) |
| Line 21 | (auto-computed) | (verify) |
| Line 22 | (auto-computed or manual depending on year) | (verify) |
| Line 23 | "RRTA Additional Medicare Tax withheld" | Part V Line 23 (often blank) |
| Line 24 | (auto-computed total withheld) | (verify Line 24) |

The agent fills each labeled field from the draft. After each field, capture a screenshot for the user's records.

10. **Verify Schedule 2 Line 11** carries the value from Form 8959 Line 18. FFFF auto-flows it; if the auto-flow fails (rare), manually enter on Schedule 2.

11. **Verify Form 1040 Line 25c** carries the value from Form 8959 Line 24. Same auto-flow rule. If Line 25c also has W-2 federal income tax withholding from Box 2, ensure both are summed correctly — Box 2 (federal income tax) is *separate* from Box 6 (Medicare), and Form 8959 Line 24 must add to Form 1040 Line 25c, not replace it.

12. **Run FFFF's "Check Form" / "Verify" tool** — it flags math errors and missing required fields on Form 8959 itself, on Schedule 2, and on Form 1040. Resolve every flag.

13. **Cross-check** every auto-computed field against the draft. If FFFF's number disagrees with the draft, **stop**; one of the two is wrong. Don't override blindly. The most common disagreement: filer entered the wrong filing status earlier in the 1040, which propagates the wrong threshold to Line 5/9/15.

14. **Save the return** (FFFF stores progress server-side).

15. **Submit** when the draft is verified, all attachments are present, and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number plus prior-year AGI for identity proof)
    - Submit

16. **Capture the submission ID** that FFFF displays. Save the screenshot.

17. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. On rejection, read the rejection code and fix.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 15
- Do not bypass FFFF's verification (step 12) even if it looks like a false positive
- Do not store the user's SSN, DOB, or PIN in any log or transcript
- Do not file Form 8959 standalone — it requires Form 1040 as the parent return
- Do not silently change the filing status on Form 1040 to "fix" a Line 5 mismatch — fix the source data instead

### Failure modes specific to Form 8959

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Line 5 / Line 9 / Line 15 = $200,000 but filer is MFJ | Filing status not set on 1040 yet; FFFF defaults to single threshold | Complete 1040 filing status first |
| Line 21 < 0 (negative) | W-2 Box 6 less than 1.45% of Box 5 | Reconcile with W-2 issuer; possible reporting error |
| Line 8 doesn't match Schedule SE Line 6 | Schedule SE not filled or not yet propagated | Fill Schedule SE first; refresh FFFF |
| Line 18 not flowing to Schedule 2 Line 11 | Schedule 2 not added to return | Add Schedule 2 explicitly |
| Line 24 not flowing to 1040 Line 25c | Field-mapping bug in current FFFF revision | Manually enter on 1040 Line 25c after verifying against draft |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow is:

1. Sign in → start or resume a return
2. Enter all W-2s in the wage section and any Schedule C / Schedule SE in the self-employment section. **Do not look for a Form 8959 entry screen first** — most consumer software auto-derives Form 8959 from these inputs.
3. Continue past income sections until the software computes total tax.
4. Look for the "Other Taxes" or "Additional Taxes" review screen — the software typically shows "Additional Medicare Tax" as a line item with the Form 8959 result.
5. **Verify against the draft**:
   - Find the Form 8959 line on the software's "Forms view" (usually accessible via a "Tools" / "View Forms" menu — not all packages expose this on the cheapest tier)
   - Match Line 18 against the draft
   - Match Line 24 against the draft
6. If the software's number disagrees with the draft by > $1, investigate before filing. Common causes:
   - Wrong filing status entered earlier in the wizard
   - Missing W-2 (filer forgot to enter all W-2s)
   - Schedule SE Line 6 differs from what the draft used (often because the wizard recalculated SE earnings)
7. After review, continue through Form 1040 review; software computes Schedule 2 Line 11 and Form 1040 Line 25c automatically.
8. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. Most software packages do not show Form 8959 as a distinct entry screen — the user enters W-2s and Schedule SE, and the software computes 8959 silently. The agent's job is to verify the silent computation matches the draft, not to fill 8959 explicitly.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

Order matters — the IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable (Schedule 2 is required when Form 8959 is filed)
3. **Form 8959** — attached after Schedule 2 in attachment-sequence order
4. **Schedule SE** (if the filer has SE income; required input for Form 8959 Line 8)
5. **Form 8960** (NIIT) if also required — separate but commonly co-filed
6. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
7. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)

Use a single staple in the upper-left corner. Don't paperclip. Don't double-side print.

### Mailing addresses (verify each year)

The IRS mailing address for paper Form 1040 *with payment* differs from *without payment*, and varies by state. Look up the current-year address at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they shift between years and are split by state.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502 timely-mailing-as-timely-filing rule)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy of the entire return for the user's records
- If paying, attach Form 1040-V payment voucher with check made out to "United States Treasury", with SSN + "Form 1040" + tax year written on the check memo line

### Producing the printable PDF

If the agent has access to the IRS fillable PDFs:

1. Download the latest revision of Form 8959 from https://www.irs.gov/forms-pubs/about-form-8959
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (which are stable on IRS forms — `f1_3` etc.)
4. Save as flattened PDF for printing

Form-field name lookups for Form 8959 live in the IRS fillable PDF metadata; tooling like `pypdf` or `pdftk` can list them. The agent should fetch the field list once per tax year and cache.

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Amended-return required** OR **Audit notice (CP2000, etc.)**

**CP2000 risk for Form 8959**: if the filer received Additional Medicare Tax withholding (W-2 Box 6 above 1.45% of Box 5) from one employer but did not file Form 8959, the IRS will issue a CP2000 notice. The notice typically arrives 12–24 months post-filing. The agent should advise filers to retain W-2 originals for 7 years.

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool, requires SSN + filing status + refund amount)
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 8959 along with my Form 1040 through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If the IRS or software asks the user to prove identity, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement between Form 8959 draft and FFFF auto-computation, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Show the diff** between draft and final FFFF state to the user before submission. The user must be able to read and approve every line.
