# Form 8919 — Filing Playbook

This is the browser-automation playbook for an agent filing Form 8919 on behalf of a user who has authorized submission. Form 8919 itself is **not** filed alone — it is always an attachment to Form 1040, 1040-SR, 1040-NR, or 1040-SS. Form SS-8 (code G) is filed separately by mail or fax, never with the return (Instructions for Form SS-8, Rev. January 2024).

**Security baseline (apply to every step):**

- Never persist SSN, DOB, bank routing/account numbers, or e-file PIN to disk
- Hold sensitive values in process memory only; clear after submission
- Require explicit user consent immediately before submission ("type SUBMIT to file")
- Show a diff between the draft and the final on-screen values before clicking Submit
- Save the IRS submission confirmation number (not the SSN) to the user's record

---

## Decision Tree: Which Filing Channel?

```
Is the user's AGI $89,000 or less (IRS Free File guided software limit for the
2026 filing season; re-check https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free)?
├── Yes → IRS Free File (guided software, free) — confirm the partner supports Form 8919
└── No  → Continue
    │
Is the user comfortable filling forms directly (no guided interview)?
├── Yes → IRS Free File Fillable Forms (FFFF) — free, supports Form 8919
└── No  → Paid software (TurboTax / H&R Block / TaxAct)
    │
Is the user willing to mail a paper return?
├── Yes → Paper filing (slower processing)
└── No  → Stay on FFFF or paid software
```

IRS Direct File was not offered in the 2026 filing season (irs.gov/filing/irs-direct-file returns 404 as of 2026-10-06). Do not offer it as a channel.

Free File Fillable Forms for 2025 returns closes **October 15, 2026** (https://www.irs.gov/e-file-providers/free-file-fillable-forms). For 2026 returns (filed in 2027), check the page for the new season's dates.

---

## Channel A: IRS Free File Fillable Forms (FFFF)

**URL:** https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Steps:**

1. Navigate the agent browser to the FFFF entry page
2. User creates account (if first time) — do not auto-fill SSN; user types it themselves
3. From the form list, select **Form 8919**
4. Fill the firm rows (lines 1–5) one by one from the draft produced by SKILL.md, matching the form's column headings: (a) name of firm, (b) federal identification number, (c) reason code, (d) date of IRS determination or correspondence, (e) Form 1099-MISC/NEC received checkbox, (f) total wages
5. Fill lines 6–13 from the draft. Check every computed value on screen against the draft
6. After Form 8919 is complete, navigate to **Form 1040**:
   - Line 1g: enter the wage amount from Form 8919 line 6
7. Navigate to **Schedule 2**:
   - Line 6: enter the amount from Form 8919 line 13 (not line 5, which is Form 4137)
8. Navigate to Form 1040 line 23 — confirm it reflects Schedule 2 line 21
   - If Schedule SE is also filed: Schedule SE line 8c = Form 8919 line 10
   - If Form 8959 is filed: Form 8959 line 3 = Form 8919 line 6
9. Run FFFF's built-in check for errors. Resolve any flagged items
10. Before submission, show the user a final review with:
    - All Form 8919 line values
    - The two cross-form entries (1040 line 1g, Schedule 2 line 6)
    - Total tax change vs. baseline (income tax + FICA)
11. **Pause and ask: "Type SUBMIT to file."** Do not submit on inferred consent
12. After submission, capture the IRS confirmation number; report to user

**Field-by-field map (form fields → SKILL.md draft fields):**

| Form field (2025 Form 8919)                  | SKILL.md draft field             |
|----------------------------------------------|----------------------------------|
| (a) Name of firm                             | Line N (1–5) column (a)          |
| (b) Firm's federal identification number     | Line N column (b)                |
| (c) Reason code                              | Line N column (c)                |
| (d) Date of IRS determination or correspondence | Line N column (d) (codes A, C only) |
| (e) 1099-MISC/NEC received checkbox          | Line N column (e)                |
| (f) Total wages                              | Line N column (f)                |
| Lines 6 through 13                           | matching SKILL.md lines 6–13     |
| Form 1040 line 1g                            | Form 8919 line 6 amount          |
| Schedule 2 line 6                            | Form 8919 line 13 amount         |

---

## Channel B: Paid Software (TurboTax / H&R Block / TaxAct)

Each platform handles 8919 slightly differently. The common entry path:

1. Search the platform for "Form 8919" or "uncollected Social Security tax"
2. Answer the worker classification interview (the platform asks: "Did you receive a 1099 that you believe should have been a W-2?")
3. Enter the firm details, reason code, and wages
4. The platform computes lines 6–13 and routes to 1040 line 1g and Schedule 2 line 6
5. **Verify the auto-computed values match the SKILL.md draft** before submission. Software bugs in 8919 handling have been documented historically; trust but verify.

If the software does **not** support Form 8919 (rare but possible for stripped-down free editions), the user must upgrade or switch to FFFF.

---

## Channel C: Paper Filing

Paper Form 8919 is attached behind Form 1040 in the standard attachment order:

```
Form 1040
├── Schedule 1 (additional income and adjustments)
├── Schedule 2 (additional taxes — includes 8919 line 13 on line 6)
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

**Tracking:** mail certified with return receipt. Save the receipt.

**Processing time:** paper returns take longer than e-filed returns; check the current estimate on https://www.irs.gov/refunds before quoting one.

---

## Special Step: Form SS-8 (Mail or Fax, Code G Only)

Form SS-8 is **not e-filed** and never attached to the return. Mail it to:

```
Internal Revenue Service
Form SS-8 Determinations
P.O. Box 630
Stop 631
Holtsville, NY 11742-0630
```

or fax it to 855-242-4481 (Instructions for Form SS-8, Rev. January 2024, "Where To File"). Do not file Form SS-8 for a firm listed with code H.

**SS-8 timing:**

- File SS-8 **on or before** the date the return with Form 8919 is filed (2025 Form 8919, reason code G)
- The IRS acknowledges receipt and sends the firm a blank Form SS-8 to complete; the worker's information may be shared with the firm
- The IRS says a determination may take at least six months
- A determination is a **letter**, not an examination. It applies only to the worker (or class of workers) requesting it and is binding on the IRS if the facts and law don't change.

**SS-8 mailing checklist (agent should produce this for the user):**

- [ ] Form SS-8 fully completed (multi-page questionnaire)
- [ ] All requested attachments (1099-NEC copies, contract, emails)
- [ ] Cover letter listing all enclosures
- [ ] Certified mail return receipt or fax confirmation
- [ ] Copy retained in user's records

---

## Pre-Submission Checklist

Before pressing Submit on Form 1040 with Form 8919 attached:

- [ ] Common-law test result documented in user's records
- [ ] All firm rows on lines 1–5 reflect actual 1099 amounts (gross, not net)
- [ ] Reason code matches the user's documents (A: determination letter; C: IRS correspondence; G: SS-8 filed; H: W-2 + 1099 from the same firm, no SS-8)
- [ ] If code G: SS-8 filed on or before the return date
- [ ] Wage amount appears on Form 1040 line 1g
- [ ] Form 8919 line 13 appears on Schedule 2 line 6
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
- [Instructions for Form SS-8 (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/iss8.pdf) — where to file (mail/fax)
- [IRS Free File](https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free) — guided software, AGI $89,000 or less (2026 filing season)
- [IRS Free File Fillable Forms](https://www.irs.gov/e-file-providers/free-file-fillable-forms) — closes October 15, 2026 for 2025 returns
- [Where to File Form 1040](https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment)
