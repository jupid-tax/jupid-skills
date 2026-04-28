# Form 8919 — Filing Playbook

This is the browser-automation playbook for an agent filing Form 8919 on behalf of a user who has authorized submission. Form 8919 itself is **not** filed alone — it is always an attachment to Form 1040. Form SS-8 is filed separately by mail (no e-file path exists for SS-8 as of the 2026 tax year).

**Security baseline (apply to every step):**

- Never persist SSN, DOB, bank routing/account numbers, or e-file PIN to disk
- Hold sensitive values in process memory only; clear after submission
- Require explicit user consent immediately before submission ("type SUBMIT to file")
- Show a diff between the draft and the final on-screen values before clicking Submit
- Save the IRS submission confirmation number (not the SSN) to the user's record

---

## Decision Tree: Which Filing Channel?

```
Is the user's AGI ≤ $79,000 (2026 IRS Free File threshold; verify)?
├── Yes → IRS Free File (guided software, free) — preferred
└── No  → Continue
    │
Is the user comfortable filling forms directly (no guided interview)?
├── Yes → IRS Free File Fillable Forms (FFFF) — free, supports Form 8919
└── No  → Paid software (TurboTax / H&R Block / TaxAct)
    │
Is the user willing to mail a paper return?
├── Yes → Paper filing (slower processing, ~6-8 weeks)
└── No  → Stay on FFFF or paid software

Is the user using Direct File (IRS Direct File pilot)?
└── Verify Direct File supports Form 8919 for the tax year — historically it has
    been limited to simple returns. As of 2026, check the current Direct File
    scope at https://directfile.irs.gov before assuming it's available.
```

---

## Channel A: IRS Free File Fillable Forms (FFFF)

**URL:** https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Steps:**

1. Navigate the agent browser to the FFFF entry page
2. User creates account (if first time) — do not auto-fill SSN; user types it themselves
3. From the form list, select **Form 8919**
4. Fill the firm table (Line 1) row by row from the draft produced by SKILL.md:
   - Field labels in FFFF: "Name of firm", "Federal ID number", "Reason code", "Date of determination", "SS-8 filed", "Total wages"
5. Fill Lines 2-11 from the draft. FFFF does not auto-calculate — the agent must enter every line, including computed lines
6. After Form 8919 is complete, navigate to **Form 1040**:
   - Line 1g: enter the wage amount from Form 8919 Line 2
7. Navigate to **Schedule 2**:
   - Line 5: enter the FICA amount from Form 8919 Line 11
8. Navigate to Form 1040 Line 23 — confirm it reflects Schedule 2 total
9. Run FFFF's built-in check for errors. Resolve any flagged items
10. Before submission, show the user a final review with:
    - All Form 8919 line values
    - The two cross-form entries (1040 Line 1g, Schedule 2 Line 5)
    - Total tax change vs. baseline (income tax + FICA)
11. **Pause and ask: "Type SUBMIT to file."** Do not submit on inferred consent
12. After submission, capture the IRS confirmation number; report to user

**Field-by-field map (FFFF labels → SKILL.md draft fields):**

| FFFF label                          | SKILL.md draft field             |
|-------------------------------------|----------------------------------|
| Name of firm (col a)                | Line 1 row N column (a)          |
| Federal ID number (col b)           | Line 1 row N column (b)          |
| Reason code (col c)                 | Line 1 row N column (c)          |
| Date of determination (col d)       | Line 1 row N column (d)          |
| SS-8 filed checkbox (col e)         | Line 1 row N column (e)          |
| Total wages (col f)                 | Line 1 row N column (f)          |
| Line 2                              | Line 2                           |
| ... (every line through 11)         | matching SKILL.md Line N         |
| Form 1040 Line 1g                   | Form 8919 Line 2 amount          |
| Schedule 2 Line 5                   | Form 8919 Line 11 amount         |

---

## Channel B: Paid Software (TurboTax / H&R Block / TaxAct)

Each platform handles 8919 slightly differently. The common entry path:

1. Search the platform for "Form 8919" or "uncollected Social Security tax"
2. Answer the worker classification interview (the platform asks: "Did you receive a 1099 that you believe should have been a W-2?")
3. Enter the firm details, reason code, and wages
4. The platform auto-computes Lines 2-11 and routes to 1040 Line 1g and Schedule 2 Line 5
5. **Verify the auto-computed values match the SKILL.md draft** before submission. Software bugs in 8919 handling have been documented historically; trust but verify.

If the software does **not** support Form 8919 (rare but possible for stripped-down free editions), the user must upgrade or switch to FFFF.

---

## Channel C: Paper Filing

Paper Form 8919 is attached behind Form 1040 in the standard attachment order:

```
Form 1040
├── Schedule 1 (additional income and adjustments)
├── Schedule 2 (additional taxes — includes 8919 Line 11 on Line 5)
├── Schedule 3 (additional credits and payments)
├── Schedule A / B / C / D / E / SE (as applicable)
├── Form 8919   ← attach here
├── Form 8959 (if Additional Medicare Tax applies)
└── Other supporting forms
```

**Mailing addresses by state:** see the IRS [Where to File Form 1040](https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment) page. The address depends on:
- The user's state of residence
- Whether a payment is included
- Whether the user is filing with foreign address

**Tracking:** mail certified with return receipt. Save the green card.

**Processing time:** 6-8 weeks typical; 12+ weeks during peak season.

---

## Special Step: Form SS-8 (Mail Only)

Form SS-8 is **not e-filed**. Always mail it separately to:

```
Department of the Treasury
Internal Revenue Service
Stop 631
Holtsville, NY 11742-0631
```

**SS-8 timing:**

- File SS-8 **before** mailing/submitting the 1040 with Form 8919 — this establishes the SS-8 filing date for code G
- The IRS sends a copy of SS-8 to the firm and gives the firm 30 days to respond
- Determination typically issues 6-12 months after filing
- A determination is a **letter** (not an audit). It is non-precedential to the broader tax law but is conclusive for the user's specific situation.

**SS-8 mailing checklist (agent should produce this for the user):**

- [ ] Form SS-8 fully completed (multi-page questionnaire)
- [ ] All requested attachments (1099-NEC copies, contract, emails)
- [ ] Cover letter listing all enclosures
- [ ] Certified mail return receipt
- [ ] Copy retained in user's records

---

## Pre-Submission Checklist

Before pressing Submit on Form 1040 with Form 8919 attached:

- [ ] Common-law test result documented in user's records
- [ ] All firm rows on Line 1 reflect actual 1099 amounts (gross, not net)
- [ ] Reason code matches the user's situation
- [ ] If code A or G: SS-8 filed (or about to be mailed)
- [ ] Wage amount appears on Form 1040 Line 1g
- [ ] FICA amount appears on Schedule 2 Line 5
- [ ] No double-counting on Schedule C
- [ ] Additional Medicare check (Form 8959) added if applicable
- [ ] User consent recorded immediately before submission
- [ ] Confirmation number saved post-submission

---

## State Income Tax Implications

Form 8919 only handles **federal** FICA. State income tax handling varies:

- Some states (CA, NY, IL) follow federal classification — the misclassified income is treated as wages for state tax too
- Some states have their own classification tests (CA's ABC test under AB-5)
- A few states have separate disability or paid-family-leave taxes that may or may not apply

The agent should remind the user to check with a state tax professional for state-specific implications. **Do not auto-file state returns based on federal misclassification without explicit state-specific guidance.**

---

## Submission State Machine

```
DRAFT → REVIEWED → AWAITING_CONSENT → SUBMITTED → ACKNOWLEDGED →
  → ACCEPTED (IRS) → PROCESSED → REFUND_OR_NOTICE
```

- **DRAFT:** SKILL.md output produced
- **REVIEWED:** validation checks all pass
- **AWAITING_CONSENT:** waiting for user to type SUBMIT
- **SUBMITTED:** clicked through e-file or mailed
- **ACKNOWLEDGED:** IRS issued confirmation number (e-file)
- **ACCEPTED:** IRS accepted (typically 24-48 hours after submission)
- **PROCESSED:** return processed, refund issued or balance due assessed
- **REFUND_OR_NOTICE:** user receives outcome

If the IRS rejects the e-file (errors in 8919 cross-references, mismatched names, etc.), do **not** auto-correct and resubmit. Surface the rejection reason to the user and walk through the correction.

---

## When NOT to Auto-Submit

The agent should **refuse to auto-submit** and require human review when:

- The common-law test result is borderline (one of three categories points to employee, two ambiguous)
- The user has filed multiple SS-8s in prior years that were ruled adversely
- The misclassified income exceeds $250,000 (high audit risk)
- The firm is a known disputed-classification employer (rideshare, delivery platforms in certain states)
- The user has overlapping classification disputes in state agencies (DOL wage-and-hour claims, EDD claims in CA)

In these cases, produce the draft and tell the user: "This filing situation is complex enough that I recommend a tax professional or employment attorney review before submission."

---

## Sources

- [Form 8919 (PDF)](https://www.irs.gov/pub/irs-pdf/f8919.pdf)
- [About Form 8919](https://www.irs.gov/forms-pubs/about-form-8919)
- [Form SS-8 (PDF)](https://www.irs.gov/pub/irs-pdf/fss8.pdf) and [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8)
- [IRS Free File Fillable Forms](https://www.irs.gov/e-file-providers/free-file-fillable-forms)
- [IRS Direct File](https://directfile.irs.gov) — verify scope per tax year
- [Where to File Form 1040](https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment)
