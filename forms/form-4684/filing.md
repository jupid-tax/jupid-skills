# Filing Form 4684 (browser automation)

How an agent equipped with browser tooling can take a completed Form 4684 draft from `SKILL.md` and actually file it. Form 4684 is always attached to a Form 1040 (or 1040-SR / 1040-NR) — it is never filed standalone. This file describes the deterministic flows the agent can follow.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
User's loss is large (>$50K) and complex (multi-property, partial insurance, disputed claim)?
  → Strongly recommend a CPA, not self-file.
    The skill can still produce a draft for the CPA.

User wants to file the prior-year disaster-year election (§165(i))?
  → Form 1040-X for the prior year + Form 4684 attached.
    Browser flow: paid software is easier than FFFF for amended returns.
    Use Section 4 (Amended return).

User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partner)
    Most partners support Form 4684 but not all. Check the partner's form list before starting.
    Skip — provider flows change too often for deterministic automation.

User wants to fill the form directly with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA, etc.)?
  → That software's casualty/theft section.
    Use Section 2 (generic pattern).

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Form 4684.
    Redirect to FFFF, paid software, or paper. Verify current scope at
    https://www.irs.gov/filing/irs-direct-file before automating.

User wants to file on paper?
  → Print Form 1040 + Form 4684 + supporting forms, sign, mail.
    Use Section 3.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each tax year.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 4684 draft from `SKILL.md`
- All Form 1040 inputs (filing status, dependents, W-2s, etc.) — Form 4684 alone isn't a return
- For Section A: the **FEMA disaster declaration number** (e.g., "DR-4856-FL"). FFFF will reject the form without it.
- For Section A: confirmation that the user will itemize (Schedule A). If standard deduction is bigger, the casualty loss provides no benefit — pause and check before filing.
- Documentation references the user retains (police report number, insurance claim number, repair estimates) — not entered on the form but should be ready in case of IRS notice
- An email address the user controls
- Explicit consent at the moment of submission

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Register / Sign in** for the current tax year
4. **Identity verification** (prior-year AGI or self-select PIN)
5. **Start a new return** → Form 1040 landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Form 4684**:
   - Click "Add a Form / Schedule"
   - Search "4684" or pick from the list
   - The form opens with sections labeled A, B, C, D
8. **Fill Section A from the draft** — field-by-field:

| Form 4684 line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| Header — FEMA number | "Federally declared disaster" + disaster number text field | Draft Header |
| 1 | "Description of properties" (Property A/B/C/D) | Draft Line 1 per property |
| 2 | "Cost or other basis" | Draft Line 2 |
| 3 | "Insurance or other reimbursement" | Draft Line 3 |
| 4 | "Gain from casualty or theft" (auto if Line 3 > Line 2) | (verify) |
| 5 | "Fair market value before" | Draft Line 5 |
| 6 | "Fair market value after" | Draft Line 6 |
| 7 | (auto = Line 5 − Line 6) | (verify) |
| 8 | (auto = smaller of Line 2 or Line 7) | (verify) |
| 9 | (auto = Line 8 − Line 3) | (verify) |
| 10 | "Casualty or theft loss" total | Draft Line 10 |
| 11 | "$100 reduction" — fixed | $100 |
| 12 | (auto = Line 10 − Line 11) | (verify) |

If multiple casualty events, FFFF lets you add additional Form 4684 instances. Roll up:

| 13 | "Total of Line 12" across forms | Draft Line 13 |
| 14 | "Total gains" | Draft Line 14 |
| 15-16 | (auto from Lines 13, 14) | (verify) |
| 17 | "10% of AGI" | Draft Line 17 |
| 18 | (auto = Line 16 − Line 17) | (verify) |

9. **Fill Section B** — only if business or income-producing losses exist:

| Form 4684 line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| 19 | "Description of properties" | Draft Line 19 |
| 20-27 | Per-item basis, insurance, FMV, decline, loss | Draft Lines 20-27 |
| Cols (b)(i) trade/business and (b)(ii) income-producing | Two-column entry | Match draft column |
| 28-39 | Aggregate to Form 4797 / Schedule A | (auto) |

10. **Fill Section C** — only if Ponzi-type theft under Rev. Proc. 2009-20. Most filers skip.

11. **Fill Section D** — check the box if electing prior-year deduction. If checked, the agent must STOP and switch to the amended-return flow (see Section 4); FFFF will not let you file 4684 with the current-year return AND simultaneously claim the loss in the prior year.

12. **Attach Form 4797** if Section B Line 38 > 0:
    - Click "Add a Form" → search 4797
    - Carry the loss to Form 4797 Part II Line 14 (ordinary loss)

13. **Attach Schedule A** if Section A Line 18 > 0 OR Section B Line 39 > 0:
    - Section A → Schedule A Line 15
    - Section B income-producing → Schedule A Line 16
    - Confirm itemized total > standard deduction; otherwise the casualty loss has no tax benefit

14. **Run FFFF's "Check Form" / "Verify"** — common 4684 errors:
    - Missing FEMA disaster number on Section A
    - Line 18 doesn't match Schedule A Line 15
    - Section B losses claimed without Form 4797
    - $100 Line 11 reduction applied per-item instead of per-event

15. **Cross-check** every auto-computed field against the draft. If FFFF disagrees, **stop**.

16. **Save the return**.

17. **Submit** when the user gives explicit go-ahead:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN)
    - Submit

18. **Capture the submission ID**. Save the screenshot.

19. **Wait 24-48 hours**, log back in, confirm IRS acceptance. Common rejection codes for 4684:
    - **F4684-001** (illustrative): missing FEMA disaster number
    - **F4684-005** (illustrative): math error
    - Verify actual rejection codes against the IRS Modernized e-File business rules

### What the agent should NOT do

- Do not submit without explicit user consent at step 17
- Do not bypass FFFF's verification (step 14) — Form 4684 errors are common
- Do not file Section A without a FEMA disaster number — the loss is not deductible
- Do not store the user's SSN, DOB, PIN, FEMA case file numbers, or insurance claim numbers in any agent log
- Do not advise on §1033 deferral — out of scope

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "FEMA disaster number invalid" | Wrong format or non-existent declaration | Verify at https://www.fema.gov/disaster/declarations |
| "Line 18 ≠ Schedule A Line 15" | Manual edit broke the link | Re-enter Line 18 to refresh |
| "Form 4797 required" | Section B business loss without 4797 attached | Add Form 4797 |
| "Math error Line 8" | User entered FMV-after greater than FMV-before | Recheck FMV inputs |
| "Insurance reimbursement creates gain" | Reimbursement > basis | Switch to gain reporting; consult §1033 deferral CPA |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the casualty section flow:

1. Sign in → start or resume a return
2. Navigate to "Deductions" → "Casualty / Theft Losses" or "Disaster Loss"
3. The wizard asks:
   - "Was the loss in a federally declared disaster area?" → Section A test
   - "Was the property used personally, in a business, or for income production?" → routing
   - "Did you receive insurance or other reimbursement?" → reimbursement entry
   - "What was the cost basis?" "What was the FMV before / after?" → per-item entry
   - "What's your AGI?" → already known from earlier sections
4. Software computes Line 12, applies $100 + 10% AGI floors, fills Schedule A automatically
5. Review the "Casualty Loss Summary" screen; verify each line against the draft
6. Continue through Form 1040 review
7. Pay software fee; e-file

**Provider notes**:
- **TurboTax**: deeply guided wizard; will surface the disaster area requirement clearly.
- **FreeTaxUSA**: simpler form-style entry; less hand-holding on the §165(h)(5) test.
- **H&R Block**: similar to TurboTax.

If the user has a specific provider, ask them to point to the relevant screen or share a screenshot.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, prior-year amendment, complex multi-event loss).

### Assemble the return

Top-to-bottom stack:

1. **Form 1040** (signed)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule A** (if Section A or B income-producing loss claimed)
4. **Form 4684** (signed not required; attached behind Schedule A)
5. **Form 4797** (if Section B business loss)
6. **Statement with FEMA disaster number** (Section A) — plain paper, identifies the disaster
7. **Other forms** in attachment-sequence order (top-right corner)
8. **W-2s, 1099s** with federal withholding — stapled to the front

Single staple, upper-left. Letter paper. No double-sided.

### Mailing addresses

Address depends on (a) state, (b) with-payment vs. without-payment. Look up at:
https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they shift.

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502 timely-mailing rule)
- Postmark by April 15 or extension date
- Keep complete photocopy of the return + all documentation (FEMA registration, insurance correspondence, repair estimates, photos)

---

## Section 4 — Amended return (disaster-year election)

If the user is electing under §165(i) to claim a federally declared disaster loss in the **prior year**:

1. Pull the prior-year tax return.
2. Prepare **Form 1040-X** for the prior year.
3. Attach **Form 4684** with the loss.
4. Attach a **statement** with:
   - The text: "Election under IRC §165(i) to deduct loss in preceding year"
   - The FEMA disaster declaration number (e.g., "DR-4856-FL")
   - The date of the disaster
   - The address of the property
   - The taxpayer's name and SSN
5. Re-compute the prior-year tax with the loss included.
6. The election deadline is generally six months after the original due date of the loss-year return (e.g., for a 2025 disaster, election deadline ~October 15, 2026 — verify against current Pub 547).
7. The election is **irrevocable** once filed.
8. Mail the 1040-X to the IRS amended-return address for the user's state. E-filing 1040-X is supported for recent years but not all; verify before automating.

---

## Section 5 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS basic validation passed
3. **Processed** — IRS fully ingested
4. **Refund issued** OR **Notice issued** OR **Audit (CP2000, etc.)**

Status checks:

- E-file: usually Accepted within 24-48 hours
- Paper: 4-8 weeks for Acceptance acknowledgment
- Amended return: up to 16 weeks for Processing
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission. For Section A with a large loss, the IRS may issue a CP2000 or a request for documentation; the user should retain the FEMA registration confirmation, insurance correspondence, photos, repair estimates, and any police report.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 4684 and the associated Form 1040 right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, FEMA case numbers, or insurance claim numbers** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.**
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (math disagreement, FEMA number rejected, reimbursement creates a gain unexpectedly), **stop and surface the issue**. Don't retry blindly.
6. **Disaster losses are audit-prone.** Remind the user to retain ALL supporting documentation for at least 3 years (longer for §1033 deferrals or carryforward NOLs).
