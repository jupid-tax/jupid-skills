# Filing Form 5329 (browser automation)

How an agent equipped with browser tooling files a completed Form 5329 draft.
Form 5329 is unusual in that it can either **attach to a Form 1040** (the
common case) or be **filed standalone** (when the user has no other 1040
filing requirement but owes a §72(t)/§4973/§4974 excise tax).

The agent must produce a complete `SKILL.md`-format draft *first*, then pick
a filing channel from the decision tree below, then execute the channel-
specific steps.

---

## Channel decision tree

```
Is the user otherwise required to file Form 1040 for this tax year?
  (Income above the filing threshold, or wants a refund of withholding,
   or has self-employment income, or is filing for any other reason)

  YES → Form 5329 attaches to the 1040
        Channel options:
        - IRS Free File guided software (AGI $89,000 or less for 2025
          returns, https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free) — Section 2 pattern
        - IRS Free File Fillable Forms (FFFF) — Section 1 below (no Part IX
          waiver statement possible; see step 10)
        - Paid tax software (TurboTax, H&R Block, FreeTaxUSA, etc.) — Section 2
        - Paper filing with 1040 — Section 4

  NO  → Form 5329 is filed standalone
        - A Form 5329 filed by itself cannot be filed electronically
          (2025 Instructions for Form 5329, "When and Where To File")
        - The only channel is **paper filing** — Section 5 below
        - The user completes the page 1 address, signs and dates page 3,
          and mails it
```

IRS Direct File was not offered in the 2026 filing season; do not route
users to it.

If the user is unsure whether they need to file a 1040, ask. The most
common ambiguous case: a retiree whose only income is below the standard
deduction but who owes a missed-RMD excise tax. They are technically not
required to file a 1040, but it can simplify the paper trail.

---

## Section 1 — IRS Free File Fillable Forms (FFFF), attached to 1040

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: opens in late January; for 2025 returns the program
closes Oct. 15, 2026 (https://www.irs.gov/e-file-providers/free-file-fillable-forms).

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI
- The completed Form 5329 draft from `SKILL.md`
- The completed Form 1040 inputs (5329 is an attachment)
- Any 1099-R forms with Box 7 distribution codes that triggered a Part I
  early-distribution analysis
- The waiver-request statement text (if Part IX waiver is being requested)

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Sign in** (or register fresh — FFFF accounts don't carry across tax years)
4. **Identity verification** with prior-year AGI or self-select PIN
5. **Open the Form 1040 return** — Form 5329 attaches to it
6. **Fill 1040 header and any other Schedules** (Schedule 1, Schedule 2, etc.)
7. **Add Form 5329**:
   - Click "Add a Form / Schedule"
   - Search "5329" or pick from the additional-tax forms list
   - The form opens with sections labeled by Part
8. **Fill the parts that apply**, leaving inapplicable Parts blank.

   Field-by-field mapping (Parts I, IV, IX shown — others follow same pattern):

| Part / Line | FFFF field label | Source (in draft) |
|-------------|------------------|-------------------|
| Header — Name | "Name of person who must file" | Filer name |
| Header — SSN | "Your social security number" | Filer SSN |
| Part I, Line 1 | "Early distributions includible in income" | Part I Line 1 |
| Part I, Line 2 | "Early distributions included on line 1 that are not subject to the additional tax" + exception number | Part I Line 2 + number |
| Part I, Line 3 | (auto-computed) | (verify Line 1 − Line 2) |
| Part I, Line 4 | "Additional tax — 10% of line 3" (25% part for SIMPLE first 2 years) | Part I Line 4 |
| Part IV, Line 18 | Excess contributions from line 24 of the prior-year 5329 | Part IV Line 18 |
| Part IV, Line 19 | Unused current-year Roth limit | Part IV Line 19 |
| Part IV, Line 20 | Current-year Roth distributions | Part IV Line 20 |
| Part IV, Lines 21-22 | (computed) | (verify) |
| Part IV, Line 23 | Excess contributions for the current year | Part IV Line 23 |
| Part IV, Line 24 | (auto-computed total excess) | (verify) |
| Part IV, Line 25 | "Additional tax — 6%" | Part IV Line 25 |
| Part IX, Lines 52a / 52b | RMD (corrected-in-window plans / all other plans) | Part IX Lines 52a / 52b |
| Part IX, Lines 53a / 53b | Amount distributed during the year | Part IX Lines 53a / 53b |
| Part IX, Lines 54a / 54b | Shortfall × 10% / × 25% | (verify) |
| Part IX, Line 55 | Line 54a + Line 54b | Part IX Line 55 |

9. **For Part I exception numbers**: enter the two-digit number (01–23)
   next to Line 2. If more than one exception applies, enter 99.

10. **For Part IX waiver request**: the instructions require "RC" and the
    waived amount in parentheses next to Line 54a/54b plus an attached
    explanation statement. FFFF does not allow attaching documents other
    than the forms it offers ("Free File Fillable Forms: program
    limitations and available forms",
    https://www.irs.gov/e-file-providers/free-file-fillable-forms-program-limitations-and-available-forms).
    If the waiver statement cannot be attached, use paid software that
    supports it or file on paper (Section 4).

11. **Run FFFF's "Check Form" / "Verify"** — resolve every flag.

12. **Cross-check** auto-computed fields against the draft. If FFFF
    disagrees, stop and recompute.

13. **Confirm Schedule 2 Line 8** picks up the Form 5329 total. FFFF should
    auto-link this; verify visually.

14. **Save the return** (FFFF stores progress server-side).

15. **Submit** with explicit user authorization at the moment of submission:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN + prior-year AGI)
    - Submit

16. **Capture the submission ID and screenshot.**

17. **Wait 24-48 hours**, log back in, confirm acceptance. On rejection,
    read the full rejection message, look it up in the FFFF error search
    tool, correct, and resubmit.

### What the agent should NOT do

- Submit without explicit consent at submission time
- Bypass FFFF's verification flags
- File 5329 standalone via FFFF — FFFF requires a 1040
- Store SSN/DOB/PIN in any log

---

## Section 2 — Paid tax software (generic pattern)

For users with TurboTax / H&R Block / FreeTaxUSA / TaxSlayer / TaxAct /
Cash App Taxes, the flow is:

1. Sign in → start or resume a return
2. Navigate to "Other Tax Situations" / "Additional Taxes" / "Penalties on
   Retirement Accounts" — the section name varies by provider
3. The software typically asks a wizard:
   - "Did you take an early distribution from a retirement account?" → Part I
   - "Did you contribute too much to an IRA / Roth IRA / HSA?" → Parts III-VII
   - "Did you miss a required minimum distribution?" → Part IX
4. The wizard maps user answers to the right Part(s). Use the SKILL draft
   to verify each Part's input matches what the wizard collected.
5. **Critical for waivers**: most software supports a "request a waiver"
   checkbox or text field for Part IX. Enter the waiver text from the
   draft. Some software auto-generates the attachment statement; some
   requires you to upload a PDF.
6. Review the Form 5329 preview / summary screen — verify each line
   against the draft. Override anything that disagrees.
7. Continue through Form 1040 review; software computes Schedule 2 / Line
   23 automatically.
8. Pay software fee; e-file.

**Provider-specific notes**:
- TurboTax: Form 5329 is in "Other Tax Situations" → "Extra tax on early
  retirement withdrawals" / "Extra tax on excess contributions"
- FreeTaxUSA: searchable as "5329"; supports waivers natively
- H&R Block: similar to TurboTax navigation

---

## Section 3 — (removed)

IRS Direct File was not offered in the 2026 filing season. Use Sections 1,
2, 4, or 5.

---

## Section 4 — Paper filing with Form 1040

When attaching to a 1040, the IRS expects this stack from top to bottom:

1. **Form 1040** (signed)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule A, B, C, D, E, etc.** in attachment-sequence order
4. **Form 5329** (no separate signature when attached to 1040)
5. **Waiver-request attachment** (if Part IX waiver) — labeled clearly
6. **Other forms** in attachment-sequence order printed on each form
7. **W-2 Copy B** stapled lower-left of Form 1040
8. **1099-R copies** if federal withholding was reported

Single staple upper-left. Mailing address depends on state and whether
payment is enclosed. Look up at:
https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

USPS Certified Mail with Return Receipt for proof of timely filing.

---

## Section 5 — Standalone Form 5329 (paper only)

When the user is not otherwise required to file a 1040, Form 5329 is filed
standalone. This is the only channel that supports standalone filing.

### Assemble the standalone return

1. **Form 5329** — completed and **signed at the bottom** (the standalone
   signature block; this block is *not* used when 5329 attaches to a 1040)
2. **Waiver-request statement attachment** if Part IX waiver
3. **Payment voucher** if there's an excise tax owed:
   - There is no Form 5329-V; use a check made payable to "United States
     Treasury" with the user's SSN, "Form 5329", and the tax year on the
     memo line
4. **A short cover letter** is helpful but not required, identifying the
   filing as a standalone Form 5329 for tax year YYYY

### Mailing address for standalone Form 5329

The standalone 5329 mails to the same address as Form 1040 *without*
payment for the user's state of residence. The IRS routes by SSN, not by
form type, for standalone filings.

Look up at: https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

If a payment is enclosed, use the *with-payment* address for the user's
state.

### Mailing best practices

- USPS Certified Mail with Return Receipt
- Postmark by April 15 (or extension date) of the year the parent return
  would be due — Form 5329 follows the parent-return deadline even when
  filed standalone
- Keep a complete photocopy

### Producing the printable PDF

1. Download Form 5329 from https://www.irs.gov/pub/irs-pdf/f5329.pdf
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms)
4. If a waiver attachment is needed, generate it as a separate PDF and
   include with the printed package
5. Save as flattened PDF for printing
6. Print, sign in ink at the standalone signature block, mail

---

## Section 6 — Submission state machine

After filing (any channel), the return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (e-file: 24-48 hours; paper:
   4-8 weeks)
3. **Processed** — fully ingested
4. **Result**:
   - Refund issued (if 5329 reduced overall liability somehow — rare;
     usually 5329 only adds tax)
   - Balance due notice (if the user didn't pay the excise tax with the
     return)
   - **Waiver decision** (Part IX) — the IRS reviews the request; if it
     is not granted, the IRS notifies the user of the additional tax owed
     (25% or 10%) (2025 Instructions for Form 5329, Waiver of tax for
     reasonable cause).
   - Audit / CP2000 notice — if a Part I exception is challenged, the
     user receives a CP2000 asking for documentation

Status checks:
- E-file acceptance: usually within 48 hours
- Refund tracking: https://www.irs.gov/refunds
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 30 days post-submission to check
status, especially when a waiver is requested.

---

## Security and consent rules for the agent

Non-negotiable:

1. **Never file without explicit user consent** at the moment of submission.
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs.
3. **Never bypass identity verification** or CAPTCHAs.
4. **Always capture submission confirmations** under the user's account.
5. **Show diff between draft and final** before submission. If FFFF or
   software computed any line differently from the draft, surface that
   diff to the user before clicking submit.
6. **If the user is requesting a waiver**, the waiver narrative must be
   the user's words about the user's situation — not a templated
   pretextual cause. The agent prepares the form; the user owns the
   reasonable-cause statement.
