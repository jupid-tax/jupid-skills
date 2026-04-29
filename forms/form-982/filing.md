# Filing Form 982 (browser automation)

How an agent equipped with browser tooling can take a completed Form 982 draft from `SKILL.md` and actually file it. Form 982 is always attached to a Form 1040 (or 1040-SR / 1040-NR) — never filed standalone. This file describes the deterministic flows the agent can follow.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
User had a complex bankruptcy or large discharge ($100K+) with multiple attributes to reduce?
  → Strongly recommend a CPA, not self-file.
    The skill can still produce a draft for the CPA.

User received the 1099-C in a prior year and didn't claim the exclusion?
  → Amend that year's return with Form 1040-X + Form 982.
    Use Section 4 (Amended return).

User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partner)
    Most partners support Form 982 but not all — verify the partner's form list.
    Skip — provider flows change too often for deterministic automation.

User wants to fill the form directly with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA, etc.)?
  → That software's "Cancellation of Debt" / "Form 1099-C" section.
    Use Section 2 (generic pattern).

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Form 982.
    Redirect to FFFF, paid software, or paper. Verify scope at
    https://www.irs.gov/filing/irs-direct-file before automating.

User wants to file on paper?
  → Print Form 1040 + Form 982 + supporting schedules, sign, mail.
    Use Section 3.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each tax year.

**Account model**: each tax year is a separate FFFF account.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address, prior-year AGI
- The completed Form 982 draft from `SKILL.md`
- All Form 1040 inputs (filing status, dependents, etc.) — Form 982 alone isn't a return
- The Form 1099-C the user received (Box 2 amount must be reconcilable with Form 982 Line 2 + any Schedule 1 Line 8c income)
- For insolvency exclusion (Box 1b): the completed Pub 4681 Worksheet 2 (kept with records, not filed)
- For bankruptcy (Box 1a): bankruptcy discharge order (kept with records)
- For qualified principal residence (Box 1e): mortgage statement / closing documents establishing the debt was acquisition indebtedness
- Explicit consent at the moment of submission

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Register / Sign in** for the current tax year
4. **Identity verification** (prior-year AGI or self-select PIN)
5. **Start a new return** → Form 1040 landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Form 982**:
   - Click "Add a Form / Schedule"
   - Search "982"
   - Form opens with Parts I, II, III labeled
8. **Fill Part I — General Information** — field-by-field:

| Form 982 line | FFFF field label | Source (in draft) |
|---------------|------------------|-------------------|
| 1a | "Discharge in a Title 11 case" checkbox | Draft Line 1a |
| 1b | "Discharge to extent insolvent" checkbox | Draft Line 1b |
| 1c | "Qualified farm indebtedness" checkbox | Draft Line 1c |
| 1d | "Qualified real property business indebtedness" checkbox | Draft Line 1d |
| 1e | "Qualified principal residence indebtedness" checkbox | Draft Line 1e |
| 2 | "Total amount of discharged indebtedness excluded from gross income" | Draft Line 2 |
| 3 | "Apply §108(b)(5) election" checkbox | Draft Line 3 |

Only ONE of 1a-1e should be checked (per Form 982 instructions). Use of multiple boxes is unusual and may require multiple Form 982 instances.

9. **Fill Part II — Reduction of Tax Attributes** — only if Box 1a or 1b checked:

| Form 982 line | FFFF field label | Source (in draft) |
|---------------|------------------|-------------------|
| 4 | "Reduction of basis under §108(b)(5) or §108(c)" | Draft Line 4 |
| 5 | "Reduction of NOL" | Draft Line 5 |
| 6 | "Reduction of general business credit" | Draft Line 6 |
| 7 | "Reduction of minimum tax credit" | Draft Line 7 |
| 8 | "Reduction of net capital loss / capital loss carryovers" | Draft Line 8 |
| 9 | "Reduction of other basis" | Draft Line 9 |
| 10 | "Reduction of passive activity loss / credit" | Draft Line 10 |
| 11 | "Reduction of foreign tax credit" | Draft Line 11 |

**The total of Lines 4-11 must equal Line 2** for bankruptcy/insolvency exclusions. FFFF will flag this if it doesn't.

10. **Skip Part III** (corporate consent — N/A for individuals).

11. **Reconcile with Schedule 1 Line 8c**:
    - If the entire 1099-C amount is excluded → Schedule 1 Line 8c = $0
    - If only part is excluded → Schedule 1 Line 8c = (Box 2 of 1099-C) − (Form 982 Line 2)
    - The user should NOT report any portion of excluded debt on Line 8c

12. **Run FFFF's "Check Form" / "Verify"** — common 982 errors:
    - Box 1a or 1b checked but Part II Lines 4-11 don't sum to Line 2
    - Multiple boxes 1a-1e checked simultaneously
    - Line 2 exceeds Form 1099-C Box 2
    - Insolvency exclusion exceeds insolvency amount per Worksheet 2 (FFFF can't verify this — agent must)

13. **Cross-check** every field against the draft. Verify:
    - The 1099-C amount NOT excluded appears on Schedule 1 Line 8c
    - Reduced NOL is recorded for next year's filing
    - Reduced basis is documented in user's records

14. **Save the return**.

15. **Submit** when the user gives explicit go-ahead:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN)
    - Submit

16. **Capture the submission ID**. Save the screenshot.

17. **Wait 24-48 hours**, log back in, confirm IRS acceptance.

### What the agent should NOT do

- Do not submit without explicit user consent at step 15
- Do not check multiple exclusion boxes (1a-1e) simultaneously
- Do not exclude more than the Form 1099-C Box 2 amount
- Do not exclude under insolvency more than the computed insolvency from Worksheet 2
- Do not store the user's SSN, DOB, PIN, or the 1099-C Box 2 amount in agent logs
- Do not advise on whether to file bankruptcy — out of scope
- Do not skip the attribute reduction step for bankruptcy/insolvency — §108(b) is mandatory

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Lines 4-11 don't sum to Line 2" | Math error in attribute reduction | Recompute; the sum must equal Line 2 for (1a) or (1b) |
| "Multiple boxes checked on Line 1" | Unintended | Pick one; if multiple exclusions truly apply, file separate Forms 982 |
| "Line 2 exceeds 1099-C Box 2" | Tried to exclude more than discharged | Reduce Line 2 to the actual discharged amount |
| "Form 1099-C amount not on Schedule 1" | User missed the income reporting | Add Schedule 1 Line 8c for the non-excluded portion |
| "Box 1e claimed but discharge year not eligible" | The principal residence exclusion lapsed | Switch to insolvency or bankruptcy if eligible |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the canceled-debt section flow:

1. Sign in → start or resume a return
2. Navigate to "Cancellation of Debt" / "Form 1099-C" / "Forgiven Debt"
3. The wizard asks:
   - "Did you receive a Form 1099-C?" → Yes
   - "What was the amount in Box 2?"
   - "Was the debt discharged in bankruptcy?" → Section A test
   - "Were you insolvent at the time of discharge?" → Section B test, walks user through Worksheet 2
   - "Was this debt on your principal residence used to buy/build/improve it?" → Section E test
4. Software computes Form 982 Line 2 based on the qualifying exclusion
5. For bankruptcy or insolvency, the software walks the user through attribute reduction (or asks for prior-year carryovers)
6. Review the "Form 982 Summary" screen; verify each line against the draft
7. Continue through Form 1040 review
8. Pay software fee; e-file

**Provider notes**:
- **TurboTax**: deeply guided wizard, walks Worksheet 2 carefully. Sometimes pushes users toward simpler "include as income" path; agent should confirm exclusion path is selected.
- **FreeTaxUSA**: simpler form-style entry; less hand-holding.
- **H&R Block**: similar to TurboTax.

If the user has a specific provider, ask them to point to the relevant screen or share a screenshot.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, large complex discharge, prior-year amendment, identity-theft concerns).

### Assemble the return

Top-to-bottom stack:

1. **Form 1040** (signed)
2. **Schedule 1** (with Line 8c entry for non-excluded portion of 1099-C, if any)
3. **Schedule 2, 3** if applicable
4. **Form 982** (signed not required; attached behind Schedule 1)
5. **Other forms** in attachment-sequence order
6. **W-2s, 1099s** with federal withholding — stapled to the front

Single staple, upper-left. Letter paper. No double-sided.

### Documentation to retain (NOT mailed with the return)

- Form 1099-C (kept by filer)
- Pub 4681 Worksheet 2 (insolvency)
- Bankruptcy discharge order (Title 11)
- §108(c) QRPBI election statement (qualified real property business)
- Basis-reduction schedule (post-reduction asset register)
- Principal residence basis reduction record
- Mortgage closing documents (qualified principal residence indebtedness)

### Mailing addresses

Look up at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502)
- Postmark by April 15 or extension date
- Keep complete photocopy of the return + all supporting documentation

---

## Section 4 — Amended return

If the user received the 1099-C in a prior year and didn't claim the exclusion (or claimed it incorrectly):

1. Pull the prior-year tax return.
2. Prepare **Form 1040-X** for the prior year.
3. Attach **Form 982** for the prior year.
4. If insolvency: attach the Pub 4681 Worksheet 2 computation (good practice; Worksheet 2 itself is not required to be filed but documents the calculation).
5. If bankruptcy: attach a copy of the discharge order.
6. Re-compute the prior-year tax with the exclusion applied.
7. Note: amended returns can be filed up to 3 years after the original return's due date (or 2 years from when tax was paid, if later) — IRC §6511. After that, the refund is barred.
8. E-filing 1040-X is supported for recent years; older years require paper. Verify the user's year before automating.

---

## Section 5 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed
3. **Processed** — fully ingested
4. **Refund issued** OR **Notice issued** OR **Audit (CP2000, etc.)**

Status checks:
- E-file: usually Accepted within 24-48 hours
- Paper: 4-8 weeks for Acceptance acknowledgment
- Amended return: up to 16 weeks
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission. Form 982 with insolvency claims is a common audit topic — the IRS sometimes requests the Worksheet 2 supporting calculation. The user should retain ALL documentation for at least 3 years post-filing (longer for basis-reduction effects on future depreciation or §121 computations on future home sales).

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 982 and the associated Form 1040 right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, 1099-C amounts, bankruptcy case numbers, or Worksheet 2 details** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.**
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (insolvency math doesn't tie out, Lines 4-11 don't sum to Line 2, multiple exclusion boxes accidentally checked), **stop and surface the issue**. Don't retry blindly.
6. **Form 982 with insolvency or bankruptcy claims is audit-prone.** Remind the user to retain the Worksheet 2 calculation, bankruptcy discharge order, and original 1099-C for at least 3 years.
7. **Do not advise on whether to file bankruptcy.** That's a legal decision; refer to a bankruptcy attorney if the user is considering it.
