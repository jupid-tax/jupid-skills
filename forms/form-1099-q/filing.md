# Filing Form 1099-Q-derived numbers (browser automation)

The user does **not** file Form 1099-Q. The 1099-Q is an information return that the 529 plan trustee or Coverdell custodian files with the IRS and copies to the user. The user files derived numbers (taxable earnings, 10% additional tax) on their Form 1040.

This file describes how an agent equipped with browser automation enters the derived numbers into the user's federal return after the SKILL.md worksheet is complete.

The agent must produce a complete `SKILL.md`-format worksheet *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User had a fully tax-free distribution (taxable earnings = $0)?
  → Nothing to file from the 1099-Q.
    Action: confirm the user retains the 1099-Q + expense receipts for 3+ years.
    Skip filing — there is nothing to enter on the return.

User has a taxable earnings portion or 10% additional tax owed?
  → Need to file Schedule 1 (Line 8z) and possibly Schedule 2 + Form 5329.
    Continue below.

User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Skip — proprietary flows; provider-specific.

User wants to fill the form themselves directly?
  → IRS Free File Fillable Forms (FFFF)
    Use Section 1 below.

User has paid tax software (TurboTax, H&R Block, FreeTaxUSA)?
  → Software's "Education" or "1099-Q" wizard section
    Use Section 2 (generic pattern).

User wants to file on paper?
  → Print Form 1040 + Schedule 1 + Schedule 2 + Form 5329, sign, mail
    Use Section 3.

User wants IRS Direct File?
  → Direct File supports limited 1099-Q scenarios; check current scope
    https://www.irs.gov/filing/irs-direct-file
    If the user has only basic 529 distributions and is otherwise eligible, may be supported. Verify before automating.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: Late January through mid-October each year.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI (for IRS identity verification)
- The completed SKILL.md worksheet showing derived numbers
- Form 1040 inputs (filing status, dependents, W-2s, etc.)
- A copy of the 1099-Q for cross-reference (the user retains the original; agent uses photo or PDF)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms"
3. **Register / Sign in** for the current tax year
4. **Identity verification** (prior-year AGI or self-select PIN)
5. **Start a new return** → Form 1040 landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)

7. **Add Schedule 1** (the agent does NOT add a Form 1099-Q form to FFFF — the 1099-Q is informational, kept by the user, not transmitted with their return):
   - Click "Add a Form / Schedule" → search "Schedule 1"
   - Schedule 1 opens with Part I (Additional Income) and Part II (Adjustments)
   - Navigate to **Line 8z — Other income**:
     - Description field: enter "Taxable 529 distribution" (or "Taxable Coverdell distribution" if Coverdell)
     - Amount field: enter the taxable earnings figure from the worksheet
   - If the user has multiple "Other income" items, FFFF allows multiple Line 8z rows; add a row for the 1099-Q if other items already exist

8. **Add Form 5329** if 10% additional tax applies:
   - Click "Add a Form / Schedule" → search "Form 5329"
   - Form 5329 opens
   - For 529 plans: navigate to **Part II — Additional Tax on Certain Distributions From Education Accounts and ABLE Accounts**
   - Enter:
     - Line 5 — distributions included in income (the taxable earnings portion)
     - Line 6 — distributions for educational expenses (any portion exempt from additional tax under exceptions, e.g., scholarship offset)
     - Line 7 — Line 5 minus Line 6 (subject to 10% additional tax)
     - Line 8 — Line 7 × 10% (the additional tax)
   - Verify against the worksheet
   - **Note**: the IRS revises Form 5329 part numbering periodically. Verify the current part covers 529/Coverdell distributions before filing. As of last verification, Part II covered education distributions; confirm against the latest [Form 5329 instructions](https://www.irs.gov/pub/irs-pdf/i5329.pdf).

9. **Add Schedule 2** if Form 5329 produced additional tax:
   - Click "Add a Form / Schedule" → search "Schedule 2"
   - Schedule 2 opens
   - **Line 8 — Additional tax on IRAs or other tax-favored accounts**: enter the Form 5329 Line 8 amount

10. **Verify auto-computed flow**:
    - Schedule 1 Line 10 (total additional income) updates → flows to Form 1040 Line 8
    - Schedule 2 Line 21 (total other taxes) updates → flows to Form 1040 Line 23

11. **Apply exceptions if any**:
    - If the user qualifies for an exception under IRC §529(c)(6)(B), Form 5329 has exception coding. Common codes (verify against current Form 5329):
      - Scholarship offset (no additional tax on amount equal to scholarship)
      - Beneficiary disability or death
      - U.S. service academy attendance
      - AOTC/LLC coordination (taxable solely because of credit coordination)
    - Enter the exception amount on Line 6, document the reason in agent records

12. **Run FFFF's "Check Form" / "Verify"** — resolve every flag before submission

13. **Cross-check against the worksheet**:
    - Schedule 1 Line 8z = worksheet "Taxable earnings"
    - Schedule 2 Line 8 = worksheet "Additional tax owed"
    - If FFFF computed values disagree with worksheet, **stop**; one is wrong

14. **Save the return** (FFFF stores progress server-side)

15. **Submit** when 1040 is complete (this typically follows other return components):
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

16. **Capture the submission ID** — save the screenshot

17. **Wait 24–48 hours**, then confirm IRS acceptance

### What the agent should NOT do

- Do not attach the 1099-Q to the return — it's an information return retained by the user
- Do not file Form 1099-Q itself — that's the trustee's job
- Do not enter Box 3 (basis) anywhere — basis is never taxable, never on the return
- Do not enter Box 1 directly — the taxable amount is *derived*, not the gross
- Do not submit without the user's explicit go-ahead at step 15
- Do not store SSN, DOB, or PIN in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| FFFF says "Form 5329 part not found" | Part numbering may have changed | Look at current Form 5329 instructions |
| Schedule 1 Line 8z amount doesn't flow to 1040 Line 8 | FFFF needs Schedule 1 Line 10 to populate | Verify all Line 8 sub-items are entered, not just 8z |
| User claims exception but no exception code on Form 5329 | The exception is reported as a Line 6 reduction, not a code | Reduce Line 6 by the exception amount and keep documentation |
| Distribution was a SECURE 2.0 Roth rollover | Not entered on the return at all if all 5 conditions met | Document the conditions in records; nothing on the 1040 |

---

## Section 2 — Generic tax-software pattern

For users with paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the typical flow:

1. Sign in → start or resume a return
2. Navigate to the **"Education"** section (sometimes labeled "Tuition and Fees" or "1099-Q")
3. The wizard asks:
   - "Did you receive a Form 1099-Q?" → Yes
   - It will ask for: trustee/payer name, recipient name + SSN, all four amount boxes
   - It will ask whether the recipient was the beneficiary (Box 6)
   - It will ask whether this was a trustee-to-trustee transfer (Box 4)
4. Wizard asks for the user's qualified education expenses for the same year
5. Wizard computes taxable earnings and any 10% additional tax automatically
6. **Verify**: at the "Schedule 1" / "Other income" review, confirm the taxable amount matches the SKILL.md worksheet
7. **Verify**: at the "Form 5329" / "Additional taxes" review, confirm the 10% additional tax matches
8. Most software handles AAQEE adjustment automatically *if* the user enters AOTC/LLC and 1099-Q in the same session — but the agent should still cross-check
9. Continue through Form 1040 review; software handles SE, dependent, and credit interaction
10. Pay software fee; e-file

**Provider-specific quirks**:
- TurboTax often asks "Did anyone use these expenses for AOTC?" mid-flow — agent must answer truthfully
- FreeTaxUSA puts 1099-Q in the "Income" section, not "Education"
- TaxSlayer asks for the 5329 exception code separately if applicable

If the wizard produces a number that disagrees with the worksheet, **pause**, recompute manually, and reconcile. Most disagreements come from the wizard not knowing about scholarships/AOTC the user already entered (or didn't enter yet).

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return, identity-theft concerns).

### Assemble the return

1. **Form 1040** (signed)
2. **Schedule 1** (with Line 8z populated — required for taxable earnings)
3. **Schedule 2** (with Line 8 populated — required if 10% additional tax)
4. **Form 5329** (computes the 10% additional tax)
5. Other forms as applicable (Form 8863 for AOTC/LLC, Form 8615 if kiddie tax applies to a student recipient)

The agent does **not** attach Form 1099-Q to the paper return. The user keeps it.

### Mailing addresses

The IRS mailing address depends on filer's state, with-or-without payment, and tax year. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

### Mailing best practices

- USPS Certified Mail with Return Receipt for proof of timely filing (IRC §7502)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy of the return + the 1099-Q + expense receipts for 3+ years (IRC §6501 statute of limitations)

---

## Section 4 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **CP2000 mismatch notice**

If the user did *not* report a 1099-Q that the IRS has on file, they will likely receive a CP2000 notice 12-18 months after filing, proposing additional tax + penalties + interest. The agent should pre-empt this by ensuring every 1099-Q is reflected in the worksheet and the return — even fully qualified distributions where no number flows to the return.

For fully qualified distributions, the user retains the worksheet and 1099-Q so they can respond to a future CP2000 by showing AAQEE ≥ Box 1.

Status checks:

- E-file: Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

---

## Security and consent rules

Non-negotiable:

1. **Never file without explicit user consent** at the moment of submission
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs or transcripts
3. **Never bypass identity verification or CAPTCHAs**
4. **Always capture submission confirmations** as screenshots stored under the user's account
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**
6. **Special for 1099-Q**: if Box 1 = Box 2 + Box 3 fails, the trustee's form is wrong. Do not "fix" the math by overriding numbers — instead, advise the user to request a corrected 1099-Q from the trustee. Filing with overridden trustee numbers triggers IRS mismatch notices.
