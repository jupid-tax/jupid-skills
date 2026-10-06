# Filing Form 982 (browser automation)

How an agent equipped with browser tooling can take a completed Form 982 draft from `SKILL.md` and actually file it. Form 982 is always attached to a Form 1040 (or 1040-SR / 1040-NR) — never filed standalone. This file describes the deterministic flows the agent can follow.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps. Line numbers follow Form 982 (Rev. March 2018); channel facts were checked on irs.gov on 2026-10-06.

---

## Channel decision tree

```
User had a complex bankruptcy or large discharge ($100K+) with multiple attributes to reduce?
  → Strongly recommend a CPA, not self-file.
    The skill can still produce a draft for the CPA.

User received the 1099-C in a prior year and didn't claim the exclusion?
  → Amend that year's return with Form 1040-X + Form 982.
    Use Section 4 (Amended return).

User has AGI ≤ $89,000 and wants free guided software?
  → IRS Free File (guided software from IRS partners; AGI limit for the
    2026 season, https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free)
    Check the partner's supported forms for Form 982 before choosing.
    Skip — provider flows change too often for deterministic automation.

User wants to fill the form directly with no software help?
  → IRS Free File Fillable Forms (FFFF). Any income level. Closes Oct. 15, 2026.
    Form 982 is on the FFFF list of available forms.
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA, etc.)?
  → That software's "Cancellation of Debt" / "Form 1099-C" section.
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Form 982 + supporting schedules, sign, mail.
    Use Section 3.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: the program for 2025 returns closes Oct. 15, 2026 (FFFF page). Form 982 is listed on https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms (entry dated 01/26/2026). FFFF has limited error checking and prepares no state return.

**Account model**: create a new account for the current filing year, even if the user used the program before. The account needs an email address and a 10-digit U.S. cell phone number that can receive text messages (FFFF page).

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address, prior-year AGI
- The completed Form 982 draft from `SKILL.md`
- All Form 1040 inputs (filing status, dependents, etc.) — Form 982 alone isn't a return
- The Form 1099-C the user received (Box 2 amount must be reconcilable with Form 982 Line 2 + any taxable amount on Schedule 1 Line 8c / Schedule C Line 6 / Schedule E Line 3)
- For insolvency exclusion (Box 1b): the completed Pub. 4681 Insolvency Worksheet (kept with records, not filed)
- The §1017 basis-reduction statement, if Part II reduces basis (lines 4, 5, 10a, 11a–11c)
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
   - FFFF presents electronic versions of IRS forms, so the fields follow the form's own line text. Confirm each field against the PDF line before typing.
8. **Fill Part I — General Information** — field-by-field:

| Form 982 line | Form text | Source (in draft) |
|---------------|-----------|-------------------|
| 1a | Discharge of indebtedness in a title 11 case | Draft Line 1a |
| 1b | Discharge of indebtedness to the extent insolvent (not in a title 11 case) | Draft Line 1b |
| 1c | Discharge of qualified farm indebtedness | Draft Line 1c |
| 1d | Discharge of qualified real property business indebtedness | Draft Line 1d |
| 1e | Discharge of qualified principal residence indebtedness | Draft Line 1e |
| 2 | Total amount of discharged indebtedness excluded from gross income | Draft Line 2 |
| 3 | Elect to treat all §1221(a)(1) real property held for sale to customers as depreciable property? Yes / No | Draft Line 3 (usually No) |

Line 1 says "check applicable box(es)": check every box the draft checks. More than one is allowed on one Form 982 (Pub. 4681 examples: 1b+1c, 1b+1d).

9. **Fill Part II — Reduction of Tax Attributes** — every line the draft shows, including zeros (each is an amount excluded from gross income):

| Form 982 line | Form text (short) | Source (in draft) |
|---------------|-------------------|-------------------|
| 4 | QRPBI applied to reduce basis of depreciable real property | Draft Line 4 |
| 5 | Elected under §108(b)(5) to reduce basis of depreciable property first | Draft Line 5 |
| 6 | Net operating loss | Draft Line 6 |
| 7 | General business credit carryover | Draft Line 7 |
| 8 | Minimum tax credit | Draft Line 8 |
| 9 | Net capital loss and capital loss carryovers | Draft Line 9 |
| 10a | Basis of nondepreciable and depreciable property not reduced on line 5 | Draft Line 10a |
| 10b | Basis of principal residence (only if line 1e checked) | Draft Line 10b |
| 11a–11c | Farm debt basis reductions | Draft Lines 11a–11c |
| 12 | Passive activity loss and credit carryovers | Draft Line 12 |
| 13 | Foreign tax credit carryover | Draft Line 13 |

Part II does not have to add up to Line 2; it is smaller when the attributes run out (i982 Line 2). There is no total line.

10. **Skip Part III** (corporate consent under §1081(b)/§1082(a)(2) — N/A for individuals).

11. **Reconcile the taxable remainder**:
    - If the entire 1099-C amount is excluded → nothing on the income line
    - If only part is excluded → Schedule 1 Line 8c (nonbusiness), Schedule C Line 6 (sole proprietorship), or Schedule E Line 3 (rental) = canceled debt − Form 982 Line 2
    - The user should NOT report any portion of excluded debt as income

12. **Run FFFF's checks, then the agent's own.** FFFF "performs basic calculations and has limited error checking" (FFFF page), so it won't catch Form 982 logic errors. Re-run the SKILL.md validation before saving:
    - Part II lines exceed Line 2, or an attribute was skipped out of order
    - A box the §108(a)(2) coordination rules shut off is checked (1b–1e in a title 11 case)
    - Line 2 exceeds the canceled debt
    - Insolvency exclusion exceeds Insolvency Worksheet line 38
    - Line 10b filled for a home the user no longer owns

13. **Cross-check** every field against the draft. Verify:
    - The 1099-C amount NOT excluded appears on the right income line (Schedule 1 Line 8c, Schedule C Line 6, or Schedule E Line 3)
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
- Do not check a box the §108(a)(2) coordination rules shut off (1b–1e for a title 11 discharge)
- Do not exclude more than the Form 1099-C Box 2 amount
- Do not exclude under insolvency more than the computed insolvency from the Insolvency Worksheet
- Do not store the user's SSN, DOB, PIN, or the 1099-C Box 2 amount in agent logs
- Do not advise on whether to file bankruptcy — out of scope
- Do not skip the attribute reduction step for bankruptcy/insolvency — §108(b) is mandatory

### Failure modes

These are the agent's own checks (FFFF won't raise them):

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Part II total exceeds Line 2 | Math error in attribute reduction | Recompute; Part II can be less than Line 2, never more |
| Credit line shows the credit reduction instead of excluded dollars | Lines 7, 8, 12 (credits), 13 mis-entered | Enter excluded dollars applied (3 × the credit absorbed) |
| Line 2 exceeds the canceled debt | Tried to exclude more than discharged | Reduce Line 2 to the actual discharged amount |
| Taxable remainder not on the return | User missed the income reporting | Add it to Schedule 1 Line 8c / Schedule C Line 6 / Schedule E Line 3 |
| Box 1e checked for a 2026 discharge | QPRI exclusion ended for discharges after 2025 | Confirm a written arrangement dated before Jan. 1, 2026; otherwise test insolvency |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the canceled-debt section flow:

1. Sign in → start or resume a return
2. Navigate to "Cancellation of Debt" / "Form 1099-C" / "Forgiven Debt"
3. The wizard asks:
   - "Did you receive a Form 1099-C?" → Yes
   - "What was the amount in Box 2?"
   - "Was the debt discharged in bankruptcy?" → Section A test
   - "Were you insolvent at the time of discharge?" → Section B test, walks user through the insolvency worksheet
   - "Was this debt on your principal residence used to buy/build/improve it?" → Section E test
4. Software computes Form 982 Line 2 based on the qualifying exclusion
5. For bankruptcy or insolvency, the software walks the user through attribute reduction (or asks for prior-year carryovers)
6. Review the "Form 982 Summary" screen; verify each line against the draft
7. Continue through Form 1040 review
8. Pay software fee; e-file

**Provider notes**: screens and wording differ by provider and change each season; this skill doesn't describe any specific provider. Confirm the exclusion path is selected (not "include as income"), that every Part II line matches the draft, and that the software doesn't force Part II to equal Line 2.

If the user has a specific provider, ask them to point to the relevant screen or share a screenshot.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, large complex discharge, prior-year amendment, identity-theft concerns).

### Assemble the return

Per the 2025 Form 1040 instructions ("Assemble Your Return"):

1. **Form 1040** (signed)
2. **Schedules and forms behind it in order of the "Attachment Sequence No."** in each form's upper-right corner (Schedule 1 is No. 01; Form 982 is No. 94)
3. **Supporting statements** (for example the §1017 basis-reduction statement for Part II) arranged in the same order as the forms they support, attached last
4. **Forms W-2 (and 2439)** attached to Form 1040; **Forms W-2G and 1099-R** only if tax was withheld

Use standard-size paper. Don't attach correspondence or other items unless required.

### Documentation to retain (NOT mailed with the return)

- Form 1099-C (kept by filer)
- Pub. 4681 Insolvency Worksheet (insolvency)
- Bankruptcy discharge order (Title 11)
- Copy of the §1017 basis-reduction statement
- Basis-reduction schedule (post-reduction asset register)
- Principal residence basis reduction record
- Mortgage closing documents (qualified principal residence indebtedness)

### Mailing addresses

Look up at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

### Mailing best practices

- USPS Certified Mail with Return Receipt (IRC §7502)
- Postmark by the due date (April 15, 2026 for 2025 returns) or the extended due date
- Keep complete photocopy of the return + all supporting documentation

---

## Section 4 — Amended return

If the user received the 1099-C in a prior year and didn't claim the exclusion (or claimed it incorrectly):

1. Pull the prior-year tax return.
2. Prepare **Form 1040-X** for the prior year.
3. Attach **Form 982** for the prior year.
4. If insolvency: you may attach the Insolvency Worksheet computation as a supporting statement; Pub. 4681 marks the worksheet "Keep for Your Records", so it is not required.
5. If bankruptcy: keep the discharge order with the records; the Form 982 instructions don't require attaching it.
6. Re-compute the prior-year tax with the exclusion applied.
7. Elections have a shorter window: a §108(b)(5) election (Line 5) or QRPBI election (Line 1d) left off a timely filed return can be made only on an amended return filed within 6 months of the original due date (excluding extensions), marked "Filed pursuant to section 301.9100-2" and filed where the original was filed (i982 When To File).
8. Note: for a refund, Form 1040-X must generally be filed within 3 years (including extensions) after the date the original return was filed or within 2 years after the tax was paid, whichever is later; an early return counts as filed on the due date (Instructions for Form 1040-X, When To File; IRC §6511).
9. E-filing 1040-X is supported for recent years; older years require paper. Verify the user's year before automating.

---

## Section 5 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed
3. **Processed** — fully ingested
4. **Refund issued** OR **Notice issued** OR **Audit (CP2000, etc.)**

Status checks:
- E-file: usually Accepted within 24-48 hours
- Paper: no electronic acknowledgment; track through the refund tool or the account transcript
- Amended return: generally 8 to 12 weeks, in some cases up to 16 weeks; up to 3 weeks to appear in Where's My Amended Return (Instructions for Form 1040-X)
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission. If the IRS questions an insolvency claim, the Insolvency Worksheet and its statements are the support. Retain documentation as long as it may become material (i982 Paperwork Reduction Act notice); generally 3 years for the return, and records relating to property (including basis reductions) until the period of limitations expires for the year the property is disposed of (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records).

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 982 and the associated Form 1040 right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, 1099-C amounts, bankruptcy case numbers, or Insolvency Worksheet details** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.**
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **If anything looks wrong** (insolvency math doesn't tie out, Part II exceeds Line 2 or skips an attribute, a box the coordination rules shut off is checked), **stop and surface the issue**. Don't retry blindly.
6. **Keep the support.** Remind the user to retain the Insolvency Worksheet, bankruptcy discharge order, and original 1099-C for as long as they may become material, and basis records until the limitations period runs for the year the property is sold.
7. **Do not advise on whether to file bankruptcy.** That's a legal decision; refer to a bankruptcy attorney if the user is considering it.
