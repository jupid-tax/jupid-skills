# Filing Form 720 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser) can take a completed Form 720 draft and file it. This file is complementary to `SKILL.md`, which produces the draft.

**Verified against:** Instructions for Form 720 (Rev. June 2026) "Where To File", "How To File", "Making a Payment", "Payment of Taxes"; IRS Form 720 e-file FAQ; IRS 720 MeF provider page; Form 8453-EX (Rev. Dec. 2011), on 2026-10-06. Re-check the current instructions before each filing.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below.

---

## Channel decision tree

```
Does the user want electronic filing (faster acknowledgment, electronic funds withdrawal)?
  → E-file through an IRS-approved 720 Modernized e-File (MeF) provider.
    Use Section 1.

Does the user prefer paper?
  → Paper Form 720 is still accepted. Mail to Ogden, UT (Section 2).

User has only a PCORI fee?
  → Either channel works. File the Q2 return only; no Q1, Q3, Q4 returns
    are required for a PCORI-only filer (i720 "How To File").
```

E-filing Form 720 is **optional** for every filer; the IRS still accepts paper Forms 720 (IRS Form 720 e-file FAQ). The IRS does NOT provide a free direct e-file portal for Form 720; all e-filing goes through approved providers, which charge a fee.

---

## Section 1 — IRS-authorized e-file providers (MeF)

The IRS publishes the list of providers that passed testing for Form 720 MeF, by tax year, at https://www.irs.gov/e-file-providers/720-mef-providers (linked from https://www.irs.gov/etec). The IRS does not endorse any provider and a listing doesn't mean the software supports every schedule.

**Pick the provider from the current IRS list, not from memory.** Confirm with the user that the provider supports the IRS Nos. and schedules in the draft (e.g., Schedule A, Schedule C, Form 6627 attachments) before entering data.

### Pre-flight

Agent must have:

- The user's permission to log in / register on the chosen provider on their behalf
- Filing entity name, EIN, address
- The completed Form 720 draft from `SKILL.md`
- For paid providers: payment method (the agent should NOT pay without explicit consent)
- The payment method for any balance due: electronic funds withdrawal (EFW) through the e-file return, EFTPS, or IRS Direct Pay (i720 "Part III, Line 10"; "Making a Payment")
- Form 8453-EX (Excise Tax Declaration for an IRS e-file Return) if the provider requires it; it carries the taxpayer declaration and the EFW authorization (Form 8453-EX Part II)

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
   - The provider may use a wizard ("Do you have indoor tanning income?" → "Do you have foreign insurance?") rather than presenting all of the roughly 60 IRS Nos. at once
6. **Enter Part II IRS Numbers**:
   - Most relevant for PCORI (IRS No. 133): enter plan-year-end date and average covered lives on the right row ($3.47 for plan years ending Oct 1, 2024 – Sep 30, 2025; $3.84 for Oct 1, 2025 – Sep 30, 2026; Notices 2024-83, 2025-61)
   - Check that the provider applied the rate for the plan year end, not the filing year
7. **Enter Schedule A** (semimonthly net liability) only if Part I shows a liability; Part II-only filers (PCORI, sport fishing, archery, tanning) skip it
8. **Enter Schedule C** (claims) only if the return reports a Part I or II liability: fuel nontaxable-use claims, ultimate vendor claims, tire credits. There is no HVUT claim on Form 720.
9. **Review the auto-generated summary** — the provider computes Part III totals
10. **Cross-check** every line against the draft. If the provider's numbers disagree with the draft, **stop**; one is wrong.
11. **Sign electronically**:
    - Form 8453-EX upload (paper signature scanned), OR
    - ERO PIN (if user is registered as ERO), OR
    - Self-Select PIN (provider-specific)
12. **Submit** when verified
13. **Capture the e-file confirmation / submission ID** from the provider
14. **Pay the balance due**: either EFW selected inside the e-file return (step 4b of Form 8453-EX), or EFTPS / Direct Pay in a separate session (Section 3). Don't file Form 720-V when paying electronically.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "EIN not found" | EIN is new or name/EIN mismatch | Confirm the EIN and legal name with the user; call the IRS Business and Specialty Tax Line, 800-829-4933 (i720 "Employer Identification Number") |
| "Form 720 not yet supported for this quarter" | Filing too early | Wait until form is available (typically a few days after quarter end) |
| "PCORI rate validation failed" | Wrong rate or row for the plan-year-end date | Notice 2024-83 ($3.47, plan years ending Oct 1, 2024 – Sep 30, 2025); Notice 2025-61 ($3.84, Oct 1, 2025 – Sep 30, 2026) |
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

Paper Form 720 is accepted for every filer; there is no e-file mandate for Form 720 (IRS Form 720 e-file FAQ).

### Assemble the return

1. Print Form 720 (current revision from https://www.irs.gov/pub/irs-pdf/f720.pdf; Rev. June 2026 on 2026-10-06)
2. Fill in all applicable lines per the SKILL.md draft
3. Sign and date the return (signed by a person authorized by the entity to sign it)
4. Complete Schedule A, C, or T only as applicable, and attach Form 6627, 6197, or 7208 when an IRS No. requires it
5. If additional sheets are attached, put the name and EIN on each sheet
6. If paying by check or money order, complete Form 720-V and enclose it loose (don't staple)

### Mailing address

The Instructions for Form 720 (Rev. June 2026), "Where To File", list one address:

```
Department of the Treasury
Internal Revenue Service
Ogden, UT 84201-0009
```

Private delivery services can't deliver to IRS P.O. boxes; for a designated PDS, use the street address listed at https://www.irs.gov/PDSStreetAddresses. The communications and air transportation uncollected tax report is mailed separately to Cincinnati, OH 45999, not with the return; a first taxpayer's report is filed with Form 720 and a separate copy goes to Cincinnati, OH 45999-0555 (i720 "Uncollected Tax Report", "First taxpayer's report"). Re-check the address in the current instructions before mailing.

### Mailing best practices

- USPS Certified Mail with Return Receipt, or a designated PDS, for proof of timely filing under IRC §7502
- Postmark on or before the quarter's due date (Apr 30 / Jul 31 / Oct 31 / Jan 31; next business day if the date falls on a weekend or legal holiday)
- Keep a complete copy of the entire return
- The balance due on line 10 may be paid by check or money order payable to "United States Treasury" with Form 720-V; write the EIN, "Form 720", and the tax period on it (Form 720-V instructions). Required semimonthly deposits are a different matter: they must be made by electronic funds transfer (i720 "Electronic deposit requirement").

---

## Section 3 — Paying the balance due (EFTPS)

Payment options for line 10 (i720 "Making a Payment"): EFW with an e-filed return, EFTPS, IRS Direct Pay, debit/credit card or digital wallet (provider fee), same-day wire, or check/money order with Form 720-V. EFTPS is also the channel for required semimonthly deposits.

### Pre-flight

- EFTPS enrollment (a new EIN is automatically enrolled; activate it from the separate EFTPS mailing, i720 "Tip"), so start early
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

Semimonthly deposits are required for Part I taxes unless the quarter's Part I net liability is $2,500 or less (i720 "Payment of Taxes"). Regular method deposit periods:

| Period | Deposit due |
|--------|-------------|
| 1st – 15th of month | 14th day after period end (generally the 29th of the same month) |
| 16th – end of month | 14th day after period end (generally the 14th of the next month) |

A due date on a Saturday, Sunday, or legal holiday moves to the preceding business day. EFTPS deposits must be initiated by 8:00 p.m. Eastern the day before the due date. September has an additional deposit (in 2026, liability for Sept. 16–26 due Sept. 29). A taxpayer who fails to deposit on time owes the §6656 penalty (2% / 5% / 10% / 15% by lateness). The agent must surface deposit-timing requirements when computing the draft.

PCORI and other Part II taxes (except the ODC floor stocks tax) do NOT require deposits; payment is made with the return.

---

## Section 4 — Submission state machine

After filing (any channel), Form 720 moves through:

1. **Submitted** — sent to IRS
2. **Accepted or rejected** — e-file: the provider shows the IRS acknowledgment; paper: no acknowledgment is sent
3. **Posted** — the return and payment post to the business's IRS account
4. **Closed** — any refund issued or overpayment applied to the next quarter (line 11b)

Status checks:

- E-file: the provider's portal shows acceptance or the rejection code
- Paper: check the IRS business tax account (https://www.irs.gov/businesses/business-tax-account) or call the Business and Specialty Tax Line, 800-829-4933
- Keep the EFTPS acknowledgment number or bank record for every payment

The agent should set a follow-up reminder to verify acceptance and posting.

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
