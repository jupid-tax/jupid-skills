# Filing Form 2555 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Browserbase, Selenium) takes a completed Form 2555 draft and files it. Form 2555 attaches to Form 1040 — it is never filed standalone. The exclusion amount flows to Schedule 1 as a negative adjustment.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Most partners support Form 2555. Check the partner's form list.
    Browser flow is provider-specific.

User wants to fill the form directly?
  → IRS Free File Fillable Forms (FFFF)
    FFFF supports Form 2555 in most years. Verify on the current form list.
    Use Section 1.

User has paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer)?
  → Use the software's "foreign earned income" / "Form 2555" wizard.
    Use Section 2 (generic pattern).

User wants paper?
  → Print Form 1040 + Form 2555 + supporting schedules.
    Filers abroad typically mail to the Austin TX service center.
    Use Section 3.

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Form 2555 in most scopes.
    Verify current scope. If unsupported, redirect to FFFF or paper.
```

**Special note**: filers physically located outside the US get an automatic 2-month filing extension to **June 15** (IRC §6081, Reg. §1.6081-5). Further extension to October 15 via Form 4868. Tax owed is still due April 15 to avoid interest, but no late-filing penalty if filed by June 15.

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October. Each tax year is a separate FFFF account.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address (US or foreign), prior-year AGI for identity verification
- The completed Form 2555 draft from `SKILL.md`
- Form 1040 inputs (filing status, dependents, full income picture including non-excluded foreign and US income)
- Travel dates if physical presence test (FFFF requires the table)
- Foreign housing expense itemization if claiming housing exclusion/deduction
- An email address the user controls
- An IP address to file from (FFFF logs filing IP)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Sign in / Register** (current tax year only)
4. **Identity verification**: prior-year AGI or self-select PIN. Filers abroad without prior-year AGI may need an IRS transcript via Form 4506-T.
5. **Start a new return** → Form 1040 landing
6. **Fill 1040 header** (name, SSN, filing status, dependents). Use the foreign address if the filer is abroad — FFFF allows international addresses.
7. **Add Form 2555**:
   - Click "Add a Form / Schedule" → search "2555"
   - Select the form (some years FFFF distinguishes Form 2555 from Form 2555-EZ; 2555-EZ was discontinued 2018, so only Form 2555)
8. **Fill Part I (General Information)** — field-by-field map:

| Form 2555 line | FFFF field | Source |
|----------------|-----------|--------|
| 1 | "Foreign address" | Draft Line 1 |
| 2 | "Occupation" | Draft Line 2 |
| 3 | "Filer's US employer (if any)" | Draft Line 3 |
| 4a | "Employer name" | Draft Line 4a |
| 4b | "US employer address" | Draft Line 4b |
| 4c | "Foreign employer address" | Draft Line 4c |
| 4d | "Type" radio | Draft Line 4d |
| 5 | "Last year FEIE claimed" | Draft Line 5 |
| 6a | "Test used last year" radio | Draft Line 6a |
| 6b | "Form 2555 filed for any prior year?" | Draft Line 6b |
| 6c | "Revocation date if applicable" | Draft Line 6c (5-year lock-out) |
| 6d | "Country of citizenship" | Draft Line 6d |
| 7 | "Bona fide resident or physical presence test?" radio | Draft Line 7 |
| 8a/b | "Family in foreign country?" | Draft Line 8 |
| 9 | "Tax home address" | Draft Line 9 |

9. **Fill Part II (Bona Fide Residence Test)** — only if using BFR:
   - Line 10: bona fide residence start date (must cover entire tax year)
   - Lines 11-15: living quarters, family, statements to foreign authorities, ties

10. **Fill Part III (Physical Presence Test)** — only if using PPT:
    - Line 16: 12-month qualifying period
    - Line 17: principal country
    - **Line 18: travel table** — FFFF provides a multi-row entry for travel periods. Each row: country, date entered, date left, full days outside US. The agent enters every row from the draft. FFFF auto-sums; verify ≥ 330.

11. **Fill Part IV (Foreign Earned Income)** — Lines 19-26:
    - Line 19: salaries/wages
    - Line 20: allowances/reimbursements
    - Line 21: SE compensation share
    - Line 22: noncash income (employer-provided housing FMV, etc.)
    - Line 23: other earned
    - Line 24: total (auto)
    - Lines 25-26: US employer compensation breakdown (informational)

12. **Fill Part V (All Filers)** — Lines 27-28:
    - Line 27 typically = Line 24

13. **Fill Part VI (Housing Exclusion — Employees)** — only if claiming housing exclusion:
    - Lines 28-30: housing expenses by type, paid by filer or employer
    - Line 31: housing expense limit (30% of FEIE cap, with city adjustment)
    - Line 32: lesser of (28 or 31)
    - Line 33: base housing amount (16% × FEIE cap × days/365)
    - Line 34: 32 − 33
    - Lines 35-36: exclusion amount

14. **Fill Part VII (Foreign Earned Income Exclusion)**:
    - Line 37: max exclusion (FEIE cap pro-rated)
    - Lines 38-43: excluded amount calculation
    - Line 45: total exclusion to Schedule 1

15. **Fill Part VIII (Disallowed Deductions)**:
    - Lines 46-50: deductions allocable to excluded income — these are NOT deductible. The agent must NOT also include them on Schedule A or Schedule C.

16. **Fill Part IX (Housing Deduction — SE only)** — only if SE filer claiming housing deduction (not exclusion):
    - Lines 51-53: housing deduction calculation; flows to Schedule 1

17. **Verify Schedule 1** auto-populates with Line 45 (or the housing deduction from Part IX) on the appropriate line.

18. **Verify Foreign Earned Income Tax Worksheet (in Form 1040 instructions)** is applied to compute Line 16 (tax) — FFFF should auto-compute, but the agent verifies. This is the tax-stacking rule.

19. **Verify Schedule SE** reflects FULL self-employment income (excluded SE income is still subject to SE tax — IRC §1402, §911 only excludes from income tax not SE tax). This is the most common trap. If the user is in a Totalization Agreement country and has Certificate of Coverage, SE tax may not apply — verify separately.

20. **Run FFFF's "Check Form" / "Verify"** — resolve every flag.

21. **Cross-check** every auto-computed field against the draft. If FFFF disagrees, **stop**.

22. **Save the return** (FFFF stores progress server-side).

23. **Submit** when 2555, 1040, and any other schedules are complete:
    - Click "E-file Now"
    - Sign with Self-Select PIN + prior-year AGI
    - Submit

24. **Capture the submission ID** — save the screenshot.

25. **Wait 24-48 hours**, log back in to confirm IRS acceptance. On rejection, read the rejection code and fix.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 23
- Do not bypass the qualifying-test verification (FFFF may auto-flag if travel days < 330)
- Do not file with a bona fide residence claim that doesn't span an entire tax year
- Do not double-deduct housing expenses (claim exclusion on 2555 AND deduct on Schedule A — the §911 disallowance prevents this)
- Do not skip Schedule SE for excluded SE income — SE tax applies
- Do not store SSN, DOB, PIN, or travel details in agent logs

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 2555 not yet supported" | Filing too early in the season | Wait until late January |
| "Travel days < 330" | Math error or actual short qualification | Recompute; if real, user fails physical presence — try BFR or skip FEIE |
| "Identity verification failed" | Wrong prior-year AGI; transcript needed | Get IRS transcript |
| FFFF rejects "Bona fide residence start date is in tax year" | BFR requires entire tax year — can't START mid-year | Use physical presence test instead, or wait for following year |
| "Revocation period not yet expired" | Filer revoked FEIE within last 5 years | Cannot re-elect without IRS consent (Form 3115 or PLR) |
| Schedule SE not auto-filed | Software thinks excluded income = no SE tax | Manual override; force Schedule SE |

---

## Section 2 — Generic tax-software pattern

For users with paid software:

1. Sign in → start or resume return
2. Navigate to "Foreign income" / "Form 2555" / "Foreign earned income exclusion" section
3. Wizard typically asks:
   - "Did you live or work outside the US?" → triggers 2555 path
   - "Bona fide resident or physical presence?" → maps to test choice
   - "What dates were you abroad?" → travel table
   - "What was your foreign salary / SE income?" → Part IV inputs
   - "Did you have foreign housing expenses?" → Part VI/IX
4. After the wizard, find a "Form 2555 review" or "Foreign income summary" screen. Compare every line to the draft.
5. **Critical override checks** in tax software:
   - Tax-stacking: most software handles automatically, but verify Form 1040 Line 16 reflects stacking
   - SE tax on excluded SE income: many software packages incorrectly zero out SE tax — manual override may be required
   - Disallowed deductions: ensure the software didn't double-count expenses on Schedule C/A AND in Part VIII
6. Continue to Form 1040 review.
7. E-file.

Provider-specific notes:

- **TurboTax**: solid 2555 support; the "Foreign Earned Income" wizard is dedicated. Watch SE tax handling.
- **FreeTaxUSA**: explicitly asks the bona fide / physical presence question. Good support.
- **H&R Block**: solid for employees, less polished for SE. Verify the housing deduction (Part IX) calculation.
- **TaxSlayer / TaxAct**: 2555 support exists; verify tax-stacking.

---

## Section 3 — Paper filing

### Assemble the return

Order (top to bottom):

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in order (Schedule 1 has the FEIE adjustment)
3. **Schedule A** if itemizing (with deductions reduced by §911 disallowance)
4. **Schedule C / SE** if SE filer (full SE earnings, full SE tax)
5. **Form 2555**
6. **Form 1116** if also claiming FTC on residual income
7. **Form 8938** if specified foreign financial assets exceed reporting threshold
8. **Other schedules** in attachment-sequence order
9. **W-2s, 1099s** with federal withholding stapled to front of 1040

Single staple, upper-left corner.

### Mailing addresses

Filers abroad mail to a special IRS service center (typically Austin, TX). Verify each year at:
**https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment**

Filers can also use foreign country private delivery services authorized by the IRS (DHL, FedEx International, UPS Worldwide).

### Mailing best practices

- USPS Priority Mail International with tracking, OR an IRS-authorized private courier
- Postmark by April 15 (June 15 for filers abroad — automatic extension)
- Photocopy entire return
- If paying, attach Form 1040-V; check made to "United States Treasury" with SSN + "Form 1040" + tax year on memo

### Producing the printable PDF

1. Download Form 2555 from https://www.irs.gov/pub/irs-pdf/f2555.pdf
2. Open in fillable-PDF tool
3. Map draft values to PDF field names (stable on IRS forms)
4. Save flattened for printing

---

## Section 4 — Submission state machine

After filing:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (24-48 hours e-file; 4-8 weeks paper, longer for foreign-filed paper)
3. **Processed** — fully ingested
4. **Refund / balance due / notice** — IRS may request substantiation of foreign residence (passport stamps, lease agreement, foreign tax return)

Follow-up checks:

- **E-file**: status via tax software or "Where's My Refund"
- **Account transcript**: https://www.irs.gov/individuals/get-transcript
- **CP2000 / CP3219N notices**: common for FEIE filers when IRS doesn't see the foreign income matching reported W-2-equivalent. Respond with foreign payslip / employer letter / passport stamps showing presence.

The agent should set a 7-day post-submission reminder.

---

## Security and consent rules

Non-negotiable:

1. **Never file without explicit consent** at the moment of submission
2. **Never store SSN, DOB, PIN, prior-year AGI, or travel dates** in agent logs or transcripts
3. **Never bypass identity verification or CAPTCHA**
4. **Always capture submission confirmations** as screenshots stored under the user's account
5. **If anything looks wrong** — math disagreement, unexpected screen, MFA failures — **stop and surface the issue**. Don't retry blindly.
6. **Foreign documentation retention**: keep passport entry/exit stamps, lease agreements, foreign payslips, foreign tax returns for at least 6 years (the IRS can audit FEIE qualification beyond the standard 3-year statute when income is omitted).
