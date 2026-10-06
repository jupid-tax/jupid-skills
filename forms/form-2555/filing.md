# Filing Form 2555 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Browserbase, Selenium) takes a completed Form 2555 draft and files it. Form 2555 attaches to Form 1040 — it is never filed standalone. The exclusion amount flows to Schedule 1 as a negative adjustment.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User has AGI ≤ $89,000 (2026 filing season) and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Partner support for Form 2555 varies. Check the partner's form list.
    Browser flow is provider-specific.

User wants to fill the form directly?
  → IRS Free File Fillable Forms (FFFF)
    No income limit. Check that Form 2555 is on the current FFFF form list.
    FFFF closes for the 2026 season on October 15, 2026.
    Use Section 1.

User has paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer)?
  → Use the software's "foreign earned income" / "Form 2555" wizard.
    Use Section 2 (generic pattern).

User wants paper?
  → Print Form 1040 + Form 2555 + supporting schedules.
    Mail to the special Form 2555 addresses (Section 3), not the state-of-residence address.
    Use Section 3.
```

IRS Direct File was not offered in the 2026 filing season; do not offer it as a channel.

**Special note — deadlines** (i2555 "When To File"; Reg. §1.6081-5):
- A filer who, on the due date, lives outside the United States and Puerto Rico and has a tax home outside the United States and Puerto Rico gets an automatic 2-month extension to **June 15, 2026** for a 2025 return. It covers filing and paying, but interest runs on unpaid tax from April 15. Attach a statement saying the filer meets both conditions.
- Form 4868 extends filing to October 15, 2026.
- A first-year filer who will not meet the bona fide residence or physical presence test by the due date can file **Form 2350** (2025 revision) to extend to a date after qualifying. Form 2350 can be e-filed; on paper it goes to Department of the Treasury, Internal Revenue Service Center, Austin, TX 73301-0045 (f2350 instructions; i2555). The alternative is to file without the exclusion and amend with Form 1040-X.

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through October 15, 2026 for 2025 returns. Each tax year is a separate FFFF account.

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
8. **Fill Part I (General Information)** — field-by-field map (2025 Form 2555 line numbers):

| Form 2555 line | Field | Source |
|----------------|-------|--------|
| 1 | Your foreign address (including country) | Draft line 1 |
| 2 | Your occupation | Draft line 2 |
| 3 | Employer's name | Draft line 3 |
| 4a | Employer's U.S. address | Draft line 4a |
| 4b | Employer's foreign address | Draft line 4b |
| 5a–5e | Employer is: foreign entity / U.S. company / Self / foreign affiliate of a U.S. company / Other | Draft line 5 |
| 6a | Last year Form 2555 or 2555-EZ was filed | Draft line 6a |
| 6b | Never filed checkbox | Draft line 6b |
| 6c | Ever revoked either exclusion? | Draft line 6c (5-year lock-out) |
| 6d | Type of exclusion and year of revocation | Draft line 6d |
| 7 | Country of citizenship/nationality | Draft line 7 |
| 8a/8b | Separate foreign residence for family (adverse conditions); city, country, days | Draft lines 8a–8b |
| 9 | Tax home(s) and date(s) established | Draft line 9 |

9. **Fill Part II (Bona Fide Residence Test)** — only if using this test:
   - Line 10: date bona fide residence began and ended (or "Continues")
   - Line 11: kind of living quarters
   - Lines 12a–12b: family abroad, who and when
   - Lines 13a–13b: statement of nonresidence; required to pay foreign income tax
   - Line 14: U.S. presence table (dates, business days, U.S. business income)
   - Lines 15a–15e: employment terms, visa, U.S. home

10. **Fill Part III (Physical Presence Test)** — only if using this test:
    - Line 16: 12-month period (both dates)
    - Line 17: principal country of employment
    - **Line 18: travel table** — each row: country (including U.S.), date arrived, date left, full days present, days in U.S. on business, income earned in U.S. on business. Enter every row from the draft and confirm the full foreign days total ≥ 330.

11. **Fill Part IV (Foreign Earned Income)** — lines 19–26:
    - Line 19: wages, salaries, bonuses, commissions
    - Lines 20a–20b: personal-services share of business/profession or partnership income
    - Lines 21a–21d: noncash income (lodging, meals, car, other)
    - Lines 22a–22g: allowances (COLA, family, education, home leave, quarters, other; total)
    - Line 23: other foreign earned income
    - Line 24: total; line 25: excludable §119 meals and lodging; line 26: foreign earned income

12. **Fill Part V** — line 27 = line 26; answer the housing question.

13. **Fill Part VI (Housing)** — only if claiming the housing exclusion or deduction:
    - Line 28: qualified housing expenses
    - Lines 29a–29b: location (only if listed in Notice 2025-16) and limit on housing expenses
    - Line 30: smaller of 28 or 29b; line 31: qualifying days
    - Line 32: $56.99 × days ($20,800 for 365); line 33: housing amount
    - Lines 34–36: employer-provided amounts, ratio, housing exclusion (SE-only filers: line 36 = 0)

14. **Fill Part VII (Foreign Earned Income Exclusion)** — lines 37–42 ($130,000; days; ratio; prorated maximum; line 27 − line 36; smaller of the two).

15. **Fill Part VIII** — line 43 = line 36 + line 42; line 44 = deductions allocable to excluded income (the deductions stay in full on Schedule 1 / Schedule C; line 44 takes the disallowed part back out of the exclusion, i2555 line 44); line 45 = line 43 − line 44.

16. **Fill Part IX (Housing Deduction)** — only if line 33 > line 36 and line 27 > line 43: lines 46–50; line 50 flows to Schedule 1 line 24j.

17. **Verify Schedule 1**: line 8d shows Form 2555 line 45 as a negative amount; line 24j shows Form 2555 line 50 if any.

18. **Verify the Foreign Earned Income Tax Worksheet (in the Form 1040 instructions)** is applied to compute Form 1040 line 16 when line 15 is more than zero. FFFF does limited calculations; the agent computes the worksheet and checks the entry. This is the tax-stacking rule.

19. **Verify Schedule SE** reflects FULL self-employment income (excluded SE income is still subject to SE tax — IRC §1402(a)(11)). This is the most common trap. If the user's SE income is covered by a social security agreement country's system, the Schedule SE instructions say not to complete Schedule SE and to attach the foreign agency's coverage statement — verify separately.

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
- Do not file with a bona fide residence claim whose uninterrupted period does not yet include an entire tax year
- Do not double-deduct housing expenses (claim exclusion on 2555 AND deduct on Schedule A — the §911 disallowance prevents this)
- Do not skip Schedule SE for excluded SE income — SE tax applies
- Do not store SSN, DOB, PIN, or travel details in agent logs

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 2555 not yet supported" | Filing too early in the season | Wait until late January |
| "Travel days < 330" | Math error or actual short qualification | Recompute; if real, user fails physical presence — try BFR or skip FEIE |
| "Identity verification failed" | Wrong prior-year AGI; transcript needed | Get IRS transcript |
| Bona fide residence period does not yet include a full tax year | First-year filer; the full year ends after the due date | Use the physical presence test if it fits, or file Form 2350, or file without the exclusion and amend with Form 1040-X (i2555 "When to claim the exclusion(s)") |
| Line 6c Yes with a revocation within the last 5 years | Filer revoked FEIE (or claimed FTC/ACTC/EIC, treated as revocation) | Cannot re-elect without IRS approval, requested as a ruling from the Associate Chief Counsel (International) (Pub. 54, "Effect of Revoking the Exclusions") |
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
   - Disallowed deductions: confirm line 44 contains the Schedule C expenses and SE-tax deduction allocable to the excluded income, with the full amounts still on Schedule C / Schedule 1 (i2555 line 44)
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

1. **Form 1040** (signed in ink), with the June 15 extension statement attached if that extension is used
2. **Schedule 1, 2, 3** in order (Schedule 1 has the FEIE adjustment)
3. **Schedule A** if itemizing (with deductions reduced by §911 disallowance)
4. **Schedule C / SE** if SE filer (full SE earnings, full SE tax)
5. **Form 1116** if also claiming FTC on residual income (Attachment Sequence No. 19)
6. **Form 2555** (Attachment Sequence No. 34)
7. **Form 8938** if specified foreign financial assets exceed reporting threshold (Attachment Sequence No. 938)
8. **Other schedules** in attachment-sequence order
9. **W-2s, 1099s** with federal withholding stapled to front of 1040

Single staple, upper-left corner.

### Mailing addresses

A return with Form 2555 attached goes to the special international address, not the state-of-residence address (i2555 "Where To File"). For 2025 returns (2025 Instructions for Form 1040, "Where do you file?", row for "A foreign country, U.S. territory, APO/FPO, or file Form 2555 or 4563, or dual-status alien"):

- Without a payment: Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215
- With a payment: Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303

Re-verify each year at https://www.irs.gov/filing/international-where-to-file-form-1040-addresses-for-taxpayers-and-tax-professionals

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
