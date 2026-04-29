# Filing Form 941 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, Browserbase) can take a completed Form 941 draft and file it. This file describes deterministic flows. It's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute channel-specific steps.

**Important difference from individual returns**: The IRS does **not** offer free online fillable forms for Form 941 the way it does for Form 1040 (FFFF). Employer 941 e-filing requires an IRS authorized e-file provider — either a paid payroll software (Gusto, ADP, Paychex, QuickBooks Payroll, Patriot, OnPay, etc.) or a third-party tax-preparation service (Drake, ATX, ProSeries, etc.). Self-filers can also paper-mail the return.

---

## Channel decision tree

```
Does the user already use a payroll provider (Gusto, ADP, QuickBooks Payroll, etc.)?
  → Provider files 941 automatically
    Browser automation: provider-specific dashboards (often pre-filed by the provider).
    Use Section 2 — verify the filing, don't refile.

Does the user have a CPA or payroll bureau handling employment taxes?
  → CPA files 941 via professional tax software
    Browser automation: not applicable — hand the draft to the CPA.
    Use Section 4 — handoff package.

Does the user file 941 themselves?
  → Three options:
    a) Authorized IRS e-file provider (small-business focus: TaxBandits, Yearli, eFile4Biz, Track1099, etc.)
       Browser automation: feasible per provider. Use Section 1.
    b) Free option does NOT exist for Form 941 (no FFFF equivalent). Self-filers must use paid e-file or paper.
    c) Paper-mail Form 941 + Schedule B (if applicable). Use Section 3.
```

---

## Section 1 — IRS authorized e-file provider (third-party)

Examples (not endorsements, just stable patterns): TaxBandits.com, Yearli.com, eFile4Biz.com, Track1099.com. Each charges a fee per filing (~$5–$15). Each is registered with the IRS as an Electronic Return Originator (ERO).

### Pre-flight

Agent must have:

- The user's permission to log in / register on the provider's site
- Employer EIN, legal name, trade name, address (matching IRS records)
- Signing officer's name, title, phone, email
- The completed Form 941 draft from `SKILL.md`
- Schedule B detail (if semi-weekly depositor)
- Bank account routing and account number **only if** the provider supports EFW (Electronic Funds Withdrawal) for the balance due. Otherwise the user pays via EFTPS separately.
- The user's current-year IRS PIN or 94x Online Signature PIN (filed via Form 8655 + Form 8453-EMP)

### Browser flow (generic — works for most providers)

The agent navigates and interacts deterministically. Selectors will differ per provider; rely on label text rather than DOM IDs.

1. **Navigate** to the provider's home page
2. **Sign in** (or register if first time)
3. **Pick the form**: search "941" or pick from form list
4. **Pick the tax year and quarter**
5. **Enter business info**:
   - EIN (no spaces or hyphens; provider re-formats)
   - Legal name (must match SS-4)
   - Trade name (optional)
   - Address (matches IRS records)
6. **Fill Form 941 from the draft** — field-by-field map:

| Form 941 line | Provider field label (typical) | Source (in draft) |
|---------------|-------------------------------|-------------------|
| Header — EIN | "EIN" | Header EIN |
| Header — Name | "Legal Business Name" | Header legal name |
| Header — Trade name | "Doing Business As (DBA)" | Header trade name |
| Header — Address | "Address" | Header address |
| Quarter checkbox | "Reporting Quarter" dropdown | Quarter |
| 1 | "Number of Employees" | Line 1 |
| 2 | "Total Wages, Tips, Compensation" | Line 2 |
| 3 | "Federal Income Tax Withheld" | Line 3 |
| 4 | "Wages NOT subject to SS/Medicare" checkbox | Line 4 |
| 5a col 1 | "Taxable Social Security Wages" | Line 5a col 1 |
| 5a col 2 | (auto-computed, verify) | Line 5a col 2 |
| 5a(i) | "Qualified sick leave wages" | $0 default |
| 5a(ii) | "Qualified family leave wages" | $0 default |
| 5b col 1 | "Taxable Social Security Tips" | Line 5b col 1 |
| 5c col 1 | "Taxable Medicare Wages" | Line 5c col 1 |
| 5d col 1 | "Wages subject to Additional Medicare" | Line 5d col 1 |
| 5e | (auto-computed) | (verify against draft) |
| 5f | "§3121(q) Notice and Demand" | $0 default |
| 6 | (auto-computed) | (verify) |
| 7 | "Fractions of cents adjustment" | Line 7 |
| 8 | "Sick pay third-party adjustment" | Line 8 |
| 9 | "Tips/group-term life adjustment" | Line 9 |
| 10 | (auto-computed) | (verify) |
| 11a | "R&D Payroll Credit (Form 8974)" | Line 11a |
| 11b–f | (residual COVID) | $0 default |
| 11g | (auto-computed) | (verify) |
| 12 | (auto-computed) | (verify) |
| 13a | "Total Deposits Made" | Line 13a |
| 14 | "Balance Due" (auto) | (verify) |
| 15 | "Overpayment" (auto) | (verify) |

7. **Pick deposit schedule (Line 16)**:
   - Box 1 / Box 2 / Box 3 radio
   - If Box 2: three monthly amounts
   - If Box 3: open Schedule B sub-form, enter daily liability for each pay date

8. **Final-return / seasonal check** (Lines 17, 18) if applicable

9. **Sign** with 94x Online Signature PIN (10-digit) OR by uploading Form 8453-EMP (PDF signature page). The provider integrates with the IRS PIN system.

10. **Pay**:
   - If balance due: choose EFW (provider debits bank), or pay separately via EFTPS, or include check by mail
   - If overpayment: elect refund or apply-to-next-quarter

11. **Submit**:
   - Provider runs validation (math, missing fields)
   - Resolve flags
   - Confirm — provider sends to IRS Modernized e-File (MeF)

12. **Capture the submission ID** that the provider displays. Save the screenshot.

13. **Wait 24–72 hours** for IRS acceptance. Provider emails an acknowledgment. Reject codes are documented at https://www.irs.gov/e-file-providers/business-rules-for-modernized-e-file. Common: R0000-905-01 (EIN/name mismatch), R0000-194 (duplicate filing).

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 11
- Do not bypass provider validation (step 11) even if it looks like a false positive
- Do not file 941 if a payroll provider has already filed (would create duplicate-filing flag)
- Do not store the user's EIN + bank account details together in any log
- Do not fabricate an Online Signature PIN — it must be applied for via Form 8655 (reporting agent) or generated by the IRS upon e-file registration

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "EIN/Name mismatch" (R0000-905-01) | Legal name typo or recent name change | Verify with IRS via 1-800-829-4933 or letter CP 575 |
| "Duplicate filing" (R0000-194) | 941 already filed (often by payroll provider) | Check with provider; if true, file 941-X for any corrections instead |
| "Signature PIN invalid" | Wrong 94x PIN | Re-apply via IRS — 45-day wait |
| "Balance due not paid by due date" | EFW failed | Pay via EFTPS within 24 hours to avoid late deposit penalty |
| "Schedule B totals don't match Line 12" | Daily entries off | Recompute daily; verify that month-end totals sum |

---

## Section 2 — Payroll provider already files 941

If the user uses Gusto, ADP, Paychex, QuickBooks Payroll, Patriot, OnPay, Rippling, Justworks, or similar full-service payroll, the provider files 941 automatically each quarter. The agent's role:

1. **Verify** the provider has the correct quarter on file
2. **Pull the filed 941 PDF** from the provider dashboard (usually under "Tax Documents", "Tax Filings", or "Compliance")
3. **Cross-check** against the draft from `SKILL.md`. Surface any disagreements.
4. **Do NOT refile** if the provider already filed — would create duplicate-filing rejection
5. If the provider's filing is wrong, **file 941-X** to correct (separate workflow — see [`references/941-x-corrections.md`](./references/941-x-corrections.md))

Common provider URLs (for the agent's reference, subject to change):

- Gusto: app.gusto.com → Taxes & filings → Quarterly tax filings
- ADP RUN: runpayroll.adp.com → Reports → Tax & wage summary
- QuickBooks Payroll: quickbooks.intuit.com → Taxes → Payroll tax → Filings
- Paychex: paychexflex.com → Reports → Tax filings
- Patriot: my.patriotsoftware.com → Reports → Tax filings

---

## Section 3 — Paper filing

Sometimes paper is the right answer (provider doesn't support form, identity-theft concerns, prior-year amendment).

### Assemble the return

Order top-to-bottom:

1. **Form 941** (signed by an authorized officer)
2. **Schedule B (Form 941)** if Line 16 Box 3
3. **Form 8974** if Line 11a > 0
4. **Form 945-A** if monthly liability summary doesn't reconcile

Do not staple. Use a single paperclip in the upper-left if needed. Each form printed full-size on letter paper, single-sided.

### Mailing addresses (verify each year)

The IRS mailing address for paper Form 941 differs **with payment vs. without** and varies by state. Look up the current address at:

https://www.irs.gov/filing/where-to-file-your-taxes-for-form-941

The agent must look up the current address by:

1. Whether a payment is enclosed
2. Filer's principal place of business state

Do not hardcode addresses — they shift between years.

### If paying with the return

- Use **Form 941-V (Payment Voucher)** — included on page 5 of the Form 941 PDF
- Make check or money order payable to **"United States Treasury"**
- Write on the check memo: EIN, "Form 941", and the quarter (e.g., "Q1 2026")
- Do NOT staple check to the return
- Mail by the due date (postmark counts under IRC §7502 — timely mailing is timely filing)

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing
- Postmark by the quarter's due date (April 30, July 31, October 31, January 31). If the date falls on a weekend or federal holiday, the next business day applies.
- Keep a complete photocopy of the entire return + check
- Save the certified-mail receipt for at least 4 years (IRS retention recommendation)

### Producing the printable PDF

1. Download the latest revision of Form 941 from https://www.irs.gov/pub/irs-pdf/f941.pdf (re-fetch each tax year)
2. Open in a PDF tool that supports form filling (Adobe Acrobat, PDF.js, pypdf)
3. Map draft values to PDF field names (stable on IRS forms — `f1_3`, `f1_4`, etc.)
4. Save as flattened PDF for printing

The agent should fetch the field list once per tax year and cache.

---

## Section 4 — CPA / payroll-bureau handoff

If the user has a CPA or payroll bureau handling 941, the agent's role is to produce a clean handoff package:

1. **The completed draft** from `SKILL.md` (markdown or PDF)
2. **The supporting payroll data**: per-employee table with gross wages, FIT withheld, FICA wages, deposits made
3. **EFTPS deposit confirmations** (PDF or CSV)
4. **Any anomalies flagged** during validation (Section 4 of `SKILL.md`)
5. **Authorization** to discuss with IRS if needed (Form 2848 or 8821)

Send the package securely (encrypted email, password-protected PDF, or via the CPA's portal — never plain email with EIN + employee SSN).

---

## Section 5 — Submission state machine

After filing (any channel), the return moves through:

1. **Submitted** — sent to IRS (provider dashboard or postal receipt)
2. **Accepted** — IRS acknowledges receipt and basic validation passed (e-file: 24–72 hours; paper: 4–8 weeks)
3. **Processed** — IRS has fully ingested the return (e-file: 1–2 weeks after acceptance; paper: 6–10 weeks)
4. **Notice issued** OR **No further action**

Possible IRS notices on a 941:

- **CP136** — Annual deposit-frequency change notice (informational)
- **CP207 / CP207L** — Schedule B mismatch or missing
- **CP276** — Underpayment of estimated deposits (FTD penalty assessed)
- **CP504** — Final notice of intent to levy if balance remains unpaid

Status checks:

- E-file: provider dashboard usually shows status
- Paper: call IRS Practitioner Priority Service at 1-866-860-4259 (with POA) or general business line 1-800-829-4933
- Account transcript: pull via IRS e-Services or Form 4506-T

The agent should set a follow-up reminder 7 days after submission (e-file) or 10 weeks (paper) to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 941 for Q[N] [YYYY] right now" must be captured.
2. **Never store EIN + bank account + Online Signature PIN together** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If the IRS or provider asks for proof, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures, duplicate-filing rejection), **stop and surface the issue**. Don't retry blindly.
6. **Never store employee SSNs.** Form 941 itself doesn't ask for SSNs (those are on W-2s), but per-employee payroll data passed in by the user may include them. Strip before logging.
7. **Pre-submission diff**: show the user a side-by-side of the draft vs. what's about to be submitted. Get explicit OK before clicking submit.
