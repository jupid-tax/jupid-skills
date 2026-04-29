# Filing Schedule 8812 (browser automation)

How an agent equipped with browser tooling can take a completed Schedule 8812 worksheet and file it with Form 1040. The agent must produce a complete `SKILL.md`-format worksheet *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific.
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → That software's "Dependents" or "Child Tax Credit" wizard
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Schedule 8812 + supporting schedules, sign, mail
    Use Section 3.

User wants IRS Direct File?
  → As of early 2026, IRS Direct File supports CTC for many filers.
    Check current scope: https://www.irs.gov/filing/irs-direct-file
    If supported, use Section 4.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: Late January through mid-October each year.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- Each dependent's full legal name, SSN (or ITIN/ATIN), relationship, birthdate
- The completed SKILL.md worksheet
- Form 1040 inputs (filing status, AGI, tax before credits, etc.)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms"
3. **Register / Sign in** for the current tax year
4. **Identity verification** (prior-year AGI or self-select PIN)
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
   - For each dependent, enter: name, SSN, relationship, qualify-for-CTC checkbox, qualify-for-ODC checkbox
   - The CTC checkbox should be checked **only** for qualifying children under 17 with SSN by due date
   - The ODC checkbox should be checked for dependents who don't meet CTC criteria
   - **DO NOT check both** for the same dependent
7. **Add Schedule 8812**:
   - Click "Add a Form / Schedule"
   - Search "Schedule 8812"
   - Schedule 8812 opens

8. **Fill Schedule 8812 from the worksheet** — field-by-field mapping (line numbers may vary; verify against current revision):

| Schedule 8812 line | FFFF field label | Source (in worksheet) |
|--------------------|------------------|----------------------|
| Part I — Heading lines | Filing status confirmation | Filing status |
| Line for "Number of qualifying children with SSN" | Number | N_CTC |
| Line for "Number of other dependents" | Number | N_ODC |
| Tentative CTC line | Computed | (N_CTC × $2,000) |
| Tentative ODC line | Computed | (N_ODC × $500) |
| MAGI line | Numeric | MAGI |
| Threshold line | Numeric (auto by filing status) | $200K or $400K |
| Excess MAGI line (rounded up to nearest $1,000) | Numeric | Computed |
| Phase-out reduction line | Computed | Excess × $5 / $1,000 |
| Allowed credit line | Computed | Tentative − Reduction |
| Tax-liability limit line | Pulled from 1040 Line 18 | Tax before credits |
| Non-refundable credit (→ 1040 Line 19) | Computed | min(Allowed, Tax limit) |
| **Part II-A** — ACTC (most filers) | | |
| Earned income line | Numeric | Earned income |
| Earned income excess ($2,500) | Computed | Earned income − $2,500 |
| 15% computation | Computed | Excess × 0.15 |
| Per-child cap ($1,700 × N_CTC) | Computed | Per-child cap |
| ACTC tentative | Computed | min(Leftover, EI method, Per-child cap) |
| **Part II-B** — Alternative SS-tax method (3+ qualifying children only) | | |
| SS + Medicare + ½ SE tax | Numeric | If applicable |
| Larger of EI method or SS-tax method | Computed | If applicable |
| **Final ACTC (→ 1040 Line 28)** | Computed | Per the worksheet |

9. **Verify auto-computed flow**:
   - Schedule 8812 non-refundable credit → Form 1040 Line 19
   - Schedule 8812 ACTC → Form 1040 Line 28
   - Form 1040 totals tax (Line 22) and payments (Line 33) update

10. **Run FFFF's "Check Form" / "Verify"** — resolve every flag before submission

11. **Cross-check against the worksheet**:
    - Each FFFF computed line matches the worksheet
    - Each dependent's SSN entered is exactly what's in IRS records (typo = rejection)
    - Phase-out reduction matches (FFFF rounds up to nearest $1,000 for excess MAGI)

12. **Save the return** (FFFF stores progress server-side)

13. **Submit** when 1040 is complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

14. **Capture the submission ID** — save the screenshot

15. **Wait 24–48 hours**, then confirm IRS acceptance. The most common rejection is **R0000-504-02** (dependent SSN/name mismatch with IRS records). On rejection:
    - Verify name spelling against the dependent's Social Security card (not informal nicknames)
    - Verify SSN
    - If correct, the dependent's name+SSN may be on another return — investigate and resolve before resubmitting

### What the agent should NOT do

- Do not check both "qualifying child" and "other dependent" boxes for the same dependent
- Do not enter ITIN/ATIN children as qualifying children — they go in the ODC count
- Do not skip the SSN-by-due-date check for any qualifying child
- Do not submit without the user's explicit go-ahead
- Do not store SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| R0000-504-02 (dependent SSN mismatch) | Name typo, wrong SSN, or someone else claimed the dependent | Verify against Social Security card; check with other parent if divorced |
| FFFF says "qualifying child age limit exceeded" | Child turned 17 during the year | Reclassify as ODC ($500 instead of $2,000) |
| FFFF won't allow CTC for dependent with ITIN | ITIN doesn't qualify for CTC | Enter as ODC instead |
| ACTC computed as $0 despite leftover credit | Earned income < $2,500 | Confirm earned income figure; if correct, ACTC truly is $0 |
| Phase-out reduces credit to $0 | High MAGI | Verify MAGI; user may not be eligible at all |
| Two FFFF returns claim the same dependent | Tiebreaker rules apply per IRC §152(c)(4) | The first filer wins typically; second is rejected with R0000-507-01 |

---

## Section 2 — Generic tax-software pattern

For users with paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the typical flow:

1. Sign in → start or resume a return
2. Navigate to the **"Dependents"** section (sometimes labeled "My Family" or "Personal Info")
3. For each dependent, the wizard asks:
   - Name, SSN, birthdate, relationship
   - "Did this person live with you more than half the year?"
   - "Did you provide more than half their support?"
   - "Did this person have a Social Security Number issued by [due date]?"
   - The wizard auto-classifies as qualifying child or qualifying relative
4. Continue to **"Tax Credits"** or **"Child Tax Credit"** section
5. The software typically shows a summary of CTC + ODC + ACTC computed automatically
6. **Verify** against the SKILL.md worksheet:
   - N_CTC and N_ODC match
   - Phase-out reduction matches
   - Non-refundable amount matches Form 1040 Line 19
   - ACTC matches Form 1040 Line 28
7. If the software's ACTC differs from the worksheet, **pause** and recompute. Most disagreements come from:
   - The software using a different earned income figure (it may include or exclude items the agent didn't)
   - The software using the alternative SS-tax method when the agent used earned income method (or vice versa)
   - The software handling MFS / Form 2120 / divorced-parents scenarios differently
8. Continue through Form 1040 review; software handles totals automatically
9. Pay software fee; e-file

**Provider-specific quirks**:
- TurboTax often asks "Do you have a custody agreement?" mid-flow for divorced parents — answer truthfully; tiebreaker rules (IRC §152(c)(4)) apply
- FreeTaxUSA puts the CTC review on a single screen with all credits
- H&R Block sometimes asks "Did anyone else claim this child?" — if yes, the user must coordinate with the other claimant before filing

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

1. **Form 1040** (signed)
2. **Schedule 8812** (computes CTC + ODC + ACTC)
3. **Schedule 1, 2, 3** as applicable
4. **Schedule EIC** if EITC also claimed (separate computation but often relevant for the same children)
5. Other forms in attachment-sequence order

### Mailing

The IRS mailing address depends on filer's state, with-or-without payment, and tax year. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502 timely-mailing rule)
- Postmark by April 15 (or extension date)
- Keep complete photocopy
- If ACTC is claimed and the return triggers PATH Act delays (Pub 5089), the IRS holds refunds until at least mid-February for returns claiming ACTC or EITC — the user should expect delay

---

## Section 4 — IRS Direct File

Direct File is the IRS's free electronic filing option, expanding annually. As of early 2026, it supports many simple Schedule 8812 scenarios but:

- Verify current scope at https://www.irs.gov/filing/irs-direct-file
- Direct File requires the filer to be in a participating state
- Direct File supports CTC and ODC for filers with simple income (W-2, no Schedule C, etc.)
- ACTC is supported for most cases

If supported, the wizard flow is similar to Section 2 (generic software). The agent navigates the wizard, verifying each computation against the worksheet at each summary screen.

---

## Section 5 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **Audit/CP2000 notice**

For returns claiming ACTC:

- **PATH Act delay**: returns claiming ACTC or EITC are held by the IRS until at least mid-February for fraud screening (per the Protecting Americans from Tax Hikes Act of 2015). Refunds typically issue late February at earliest.
- **Common audit trigger**: claiming a child also claimed by another taxpayer (e.g., divorced parents, custody dispute). The IRS applies tiebreaker rules under IRC §152(c)(4) — typically, the parent with whom the child lived longer wins; if equal, higher AGI wins.

Status checks:

- E-file: Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool)
- Account transcript: https://www.irs.gov/individuals/get-transcript

---

## Security and consent rules

Non-negotiable:

1. **Never file without explicit user consent** at the moment of submission
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs or transcripts (this is especially sensitive for dependents — children's SSNs are common identity-theft targets)
3. **Never bypass identity verification or CAPTCHAs**
4. **Always capture submission confirmations** as screenshots stored under the user's account
5. **If anything looks wrong** (math disagreement, dependent SSN mismatch warning, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Special for Schedule 8812**: if a dependent's SSN was issued after the due date, the user must NOT claim CTC for that dependent (IRC §24(h)(7)). The agent should reclassify as ODC and document the reason. Filing CTC with a post-due-date SSN is a deliberate misstatement that can trigger §6695A or §6694 preparer penalties if the agent is held to preparer standards.
