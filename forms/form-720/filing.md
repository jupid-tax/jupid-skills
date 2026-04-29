# Filing Form 720 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser) can take a completed Form 720 draft and file it. This file is complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below.

---

## Channel decision tree

```
User has gross excise liability requiring electronic filing per IRS regs?
  → Mandatory e-file via IRS-authorized provider (MeF — Modernized e-File)
    Use Section 1.

User is a small filer below mandatory threshold and prefers paper?
  → Paper filing to IRS Cincinnati or Ogden (varies by state and form type)
    Use Section 2.

User has only a PCORI fee and wants the simplest filing?
  → Most authorized e-file providers support PCORI-only Form 720 with simple
    plan-year + covered-lives input. Use Section 1.
```

**Note**: The IRS does NOT provide a free direct e-file portal for Form 720 (unlike Form 1040's Free File Fillable Forms). All e-filing goes through IRS-authorized third-party providers. The agent picks one.

---

## Section 1 — IRS-authorized e-file providers (MeF)

The IRS publishes the list of providers approved for Form 720 MeF at https://www.irs.gov/e-file-providers/modernized-e-file-mef-forms. Common providers include:

- **Tax720.com** (PCORI-focused)
- **ExpressTaxFilings / ExpressTruckTax** (covers Form 720 + Form 2290)
- **Simple720** (PCORI-focused)
- **Drake Tax** (professional tax prep software)
- **CCH Axcess** (professional)
- **TaxBandits** (multi-form)

**The list and pricing change each year. Always verify against the IRS-published list before filing.**

### Pre-flight

Agent must have:

- The user's permission to log in / register on the chosen provider on their behalf
- Filing entity name, EIN, address
- The completed Form 720 draft from `SKILL.md`
- For paid providers: payment method (the agent should NOT pay without explicit consent)
- An EFTPS account for paying the balance due (separate from the e-file provider — the IRS does not accept payment through MeF for Form 720; payment is via EFTPS)
- Form 8453-EX e-file signature authorization OR an electronic-return-originator (ERO) PIN if the provider supports paperless signatures

### Generic provider browser flow

The exact selectors vary by provider. Use label text and human-readable navigation rather than DOM IDs. The pattern is:

1. **Navigate** to the provider's Form 720 entry page
2. **Sign in** or register with email + password
3. **Start a new return**:
   - Select tax form: "Form 720"
   - Select quarter: Q1 / Q2 / Q3 / Q4
   - Select tax year: e.g., 2026
4. **Enter business information**:
   - Name, EIN, address from header
   - Final return / address change checkboxes
5. **Enter Part I IRS Numbers**:
   - For each applicable IRS Number, enter the base, rate (often pre-filled by the provider), and tax
   - The provider may use a wizard ("Do you have indoor tanning income?" → "Do you have foreign insurance?") rather than presenting all 30+ IRS Numbers at once
6. **Enter Part II IRS Numbers**:
   - Most relevant for PCORI (IRS No. 133): enter plan-year-end date, average covered lives, counting method
   - Provider auto-applies the PCORI rate ($3.22 for plan years ending Oct 1, 2024 – Sep 30, 2025; verify next-year rate)
7. **Enter Schedule A** (semi-monthly liability dates) — only if applicable; PCORI-only filers skip this
8. **Enter Schedule C** (claims) — if any HVUT credits, fuel-use claims, etc.
9. **Review the auto-generated summary** — the provider computes Part III totals
10. **Cross-check** every line against the draft. If the provider's numbers disagree with the draft, **stop**; one is wrong.
11. **Sign electronically**:
    - Form 8453-EX upload (paper signature scanned), OR
    - ERO PIN (if user is registered as ERO), OR
    - Self-Select PIN (provider-specific)
12. **Submit** when verified
13. **Capture the e-file confirmation / submission ID** from the provider
14. **Pay the balance due via EFTPS** in a separate session (see Section 3 below) — most providers do NOT route payment to IRS

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "EIN not found" | EIN is new / not yet in IRS records | Wait 2 weeks after Form SS-4, or call IRS |
| "Form 720 not yet supported for this quarter" | Filing too early | Wait until form is available (typically a few days after quarter end) |
| "PCORI rate validation failed" | Wrong rate for the plan-year-end date | Check Notice (e.g., 2024-83 for plan years ending Oct 1 2024 – Sep 30 2025) |
| "MeF rejection R0000-XXX" | IRS-side validation error | Read rejection code; common ones: duplicate filing, EIN mismatch, signature missing |
| Provider charges unexpected fee | Pricing change | Confirm with user before paying |

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 12
- Do not bypass the provider's validation tools
- Do not file Form 720 if the user has already filed for that quarter (creates duplicate-filing rejection — though MeF generally rejects automatically)
- Do not store the user's EFTPS PIN, EIN, or e-file authorization in any log or transcript
- Do not pay the provider's fee without explicit user authorization

---

## Section 2 — Paper filing

Some filers prefer or require paper. As of 2026, paper Form 720 is still accepted but mandatory e-file applies for some categories — verify the current Form 720 instructions for the threshold.

### Assemble the return

1. Print Form 720 (latest revision from https://www.irs.gov/pub/irs-pdf/f720.pdf)
2. Fill in all applicable lines per the SKILL.md draft
3. Sign and date the return (signed by an officer or authorized representative)
4. Print supporting schedules (Schedule A, C, T as applicable)
5. Print Form 8453-EX if e-filing requires a paper signature (not applicable for paper return — Form 720 is signed in ink)

### Mailing addresses (verify each year)

The IRS publishes Form 720 mailing addresses in the form instructions. As of 2025, paper Form 720 with payment goes to:

```
Internal Revenue Service
P.O. Box 932500
Louisville, KY 40293-2500
```

Without payment:

```
Department of the Treasury
Internal Revenue Service
Cincinnati, OH 45999-0009
```

(These addresses change between years and processing reorganizations. Always verify against the latest i720.pdf before mailing.)

### Mailing best practices

- USPS Certified Mail with Return Receipt for proof of timely filing under IRC §7502
- Postmark on or before the quarter's due date (Apr 30 / Jul 31 / Oct 31 / Jan 31)
- Keep a complete photocopy of the entire return
- Pay the balance due via EFTPS, NOT by check — most business excise tax payments must be electronic per Treasury Reg. §31.6302-1 (for taxpayers above $200K threshold; below that, check is OK)

---

## Section 3 — Paying the balance due (EFTPS)

Form 720 e-file does NOT include a payment mechanism. The user must pay separately via EFTPS.

### Pre-flight

- EFTPS enrollment (5–7 business days lead time for new enrollees)
- EFTPS PIN and Internet Password
- Bank routing + account number
- The balance due from Part III Line 10 of the draft

### EFTPS payment flow

1. Navigate to https://www.eftps.gov
2. Sign in with EIN + PIN + Internet Password
3. Click "Make a Payment"
4. Select tax form: "720"
5. Select tax period: the quarter and year being filed (e.g., "2026 Q2")
6. Enter payment amount = Part III Line 10 (balance due)
7. Select effective date (typically same day or next business day)
8. Confirm bank info
9. Submit → confirmation number issued
10. Capture the EFT acknowledgment number

### Semi-monthly deposits (if applicable)

For some Form 720 categories (gasoline, diesel, alcohol, tobacco) with > $2,500 quarterly liability, semi-monthly deposits are required during the quarter — not just at filing. Deposit periods:

| Period | Deposit due |
|--------|-------------|
| 1st – 15th of month | 14 days after period end (i.e., 29th–30th of same month) |
| 16th – end of month | 14 days after period end (i.e., 14th of next month) |

A taxpayer who incurs liability and fails to deposit by the due date owes a §6656 penalty (2% / 5% / 10% / 15% by lateness). The agent must surface deposit-timing requirements when computing the draft.

PCORI does NOT require semi-monthly deposits — payment is annual with the Q2 return.

---

## Section 4 — Submission state machine

After filing (any channel), Form 720 moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS validates basic structure (e-file: 24–48 hours; paper: 4–6 weeks)
3. **Posted** — IRS account credited; visible on IRS Online Account
4. **Closed** — quarter is finalized; any refund issued or balance applied

Status checks:

- E-file: provider's portal shows acceptance/rejection within 1–2 business days
- Paper: 4–6 weeks for IRS to acknowledge; verify via IRS Online Account or call PPS line
- IRS Online Account (business account separate from individual): https://www.irs.gov/payments/online-account

The agent should set a follow-up reminder 14 days post-submission to verify acceptance.

---

## Section 5 — Security and consent rules for the agent

These are non-negotiable:

1. **Never file or submit a payment without explicit user consent at the moment of action.** "I authorize you to file Form 720 for [quarter] [year] and pay $[amount] via EFTPS right now" must be captured.
2. **Never store EIN, EFTPS PIN, e-file PIN, or bank account information** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs** on provider sites or EFTPS.
4. **Always capture submission IDs and EFTPS confirmation numbers** as the user's records.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), stop and surface the issue. Don't retry blindly — repeated failed attempts can lock EFTPS PINs.
6. **Verify the quarter and tax year** one last time before submitting. Wrong quarter on Form 720 routes the payment to the wrong period and is painful to unwind.
7. **For PCORI specifically**: verify the Q2 form is being used (PCORI is filed annually on the Q2 form, NOT on Q1/Q3/Q4 even if the plan year ends in those quarters). The plan-year-end date determines the rate; the filing quarter is always Q2 (July 31).
