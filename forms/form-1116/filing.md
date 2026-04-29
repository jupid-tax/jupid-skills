# Filing Form 1116 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Browserbase, Selenium) takes a completed Form 1116 draft and files it. Form 1116 attaches to Form 1040 (individuals) or Form 1041 (estates/trusts) — it is never filed standalone.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute the channel-specific steps.

---

## Channel decision tree

```
User qualifies for the de-minimis $300/$600 exception?
  → No Form 1116 needed. Just put the foreign tax on Schedule 3 Line 1.
    Use the user's normal 1040 channel (FFFF, paid software, paper).
    Done.

User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Most partners support Form 1116. Check the partner's form list before relying.
    Browser flow is provider-specific; do not write deterministic flows.

User wants to fill the form directly?
  → IRS Free File Fillable Forms (FFFF)
    FFFF supports Form 1116 in most years. Verify on the current year's form list.
    Use Section 1.

User has paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct)?
  → Use the software's "foreign tax credit" / "Form 1116" wizard.
    Use Section 2 (generic pattern).

User wants paper?
  → Print Form 1040 + Form 1116 (one per basket) + supporting schedules.
    Use Section 3.

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Form 1116 in most scopes.
    Verify current scope at https://www.irs.gov/filing/irs-direct-file before
    relying. If unsupported, redirect to FFFF or paper.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October. Each tax year is a separate FFFF account (no credentials carry over).

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 1116 draft from `SKILL.md` — one per basket if multi-basket
- Form 1040 inputs (filing status, dependents, W-2s, 1099s, etc.) — Form 1116 doesn't stand alone
- Foreign income / foreign tax detail per country in USD
- Prior-year unused FTC by basket, if any
- An email address the user controls

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → FFFF launchpad
3. **Sign in / Register** (current tax year only)
4. **Identity verification**: prior-year AGI or self-select PIN
5. **Start a new return** → Form 1040 landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Fill 1040 income lines** including any foreign-source income on the standard lines (wages on Line 1a, dividends on 3b, etc.) — Form 1116 doesn't replace these; it computes a credit
8. **Add Form 1116** for the first basket:
   - Click "Add a Form / Schedule" → search "1116"
   - Select the category checkbox (one of a-g)
   - Fill the resident country (Line i)
   - Check "Paid" or "Accrued" (Line h) — once "Accrued" elected, binding for future years
9. **Fill Part I (Foreign-source taxable income)** — field-by-field map:

| Form 1116 line | FFFF field | Source (in draft) |
|----------------|-----------|-------------------|
| Country column header | "Country A/B/C" text | Draft Part I header |
| 1a | "Gross income from sources outside the US" per column | Draft Line 1a per country |
| 1b | "Compensation for services performed abroad" | Draft Line 1b |
| 2 | "Expenses definitely related" | Draft Line 2 |
| 3a | "Pro-rata: itemized/standard deduction" | Draft Line 3a |
| 3b | "Pro-rata: other deductions" | Draft Line 3b |
| 3c | (auto from 3a + 3b) | Verify |
| 3d | "Gross foreign-source income, this category" | Draft Line 3d |
| 3e | "Gross income from all sources" | Draft Line 3e |
| 3f | (auto from 3d/3e) | Verify |
| 3g | (auto from 3c × 3f) | Verify |
| 4a | "Home mortgage interest" | Draft Line 4a |
| 4b | "Allocated to foreign" | Draft Line 4b |
| 5 | "Losses from foreign sources" | Draft Line 5 |
| 6 | (auto from 2 + 3g + 4b + 5) | Verify |
| 7 | (auto from 1a − 6) | Verify |

10. **Fill Part II (Foreign taxes)** — for each country row:
    - Country letter + name
    - Date paid OR accrued
    - Foreign currency amount (informational; FFFF may auto-translate or require USD only)
    - USD amount per type (taxes withheld at source on income types A-D; other foreign taxes paid)
    - Line 8 auto-sums

11. **Fill Part III (§904 limitation)**:
    - Line 9 = Line 8 (auto)
    - Line 10 = Carryover from prior years (manual entry; FFFF doesn't track across years)
    - Line 11 = auto
    - Line 12 = boycott reduction (usually 0)
    - Line 13 = auto
    - Line 14 = Line 7 (auto)
    - Line 15 = QD/LTCG adjustment — manual entry; FFFF may not auto-compute
    - Line 17 = auto (14 − 15)
    - Line 18 = total taxable income (auto if 1040 already filled, else manual)
    - Line 19 = auto (17/18)
    - Line 20 = auto (19 × tax before credits)
    - Line 21 = auto (lesser of 13 or 20)

12. **If multiple baskets**: repeat Steps 8-11 with another Form 1116 instance (different category checkbox). FFFF allows multiple 1116s in one return; one is designated as the "summary" 1116 for Part IV.

13. **Fill Part IV (summary 1116 only)**:
    - Lines 22-32: enter Line 21 from each basket's 1116
    - Line 33 = sum (auto)
    - Line 35 = lesser of Line 33 or US tax before credits (auto)

14. **Verify Schedule 3 Line 1** auto-populates with Line 35

15. **Run FFFF's "Check Form" / "Verify"** — resolve every flag

16. **Cross-check** every auto-computed field against the draft. If FFFF disagrees with the draft, **stop**. Don't override blindly.

17. **Save the return** (FFFF stores progress server-side)

18. **Submit** when 1116(s), 1040, and any other schedules are complete:
    - Click "E-file Now"
    - Sign with Self-Select PIN + prior-year AGI
    - Submit

19. **Capture the submission ID** — save the screenshot

20. **Wait 24-48 hours**, log back in to confirm IRS acceptance. On rejection, read the rejection code and fix.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 18
- Do not bypass the QD/LTCG adjustment on Line 15 if the user has qualified dividends or LTCG taxed at preferential rates — this is a common audit issue
- Do not file with an "Accrued" election unless the user explicitly understands it's binding for future years
- Do not store SSN, DOB, or PIN in any log

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 1116 not yet supported" | Filing too early in the season | Wait until late January |
| "Math error on Line 19" | Line 17 > Line 18 (impossible) | Recompute; usually a mis-allocated deduction |
| "Identity verification failed" | Wrong prior-year AGI | Get IRS transcript |
| FFFF won't accept multiple 1116 | Some years FFFF allows only 1 1116 in the form set | File on paper or use paid software |
| Schedule 3 Line 1 doesn't populate | Form 1116 missing the summary designation | Mark one 1116 as the summary in FFFF |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software:

1. Sign in → start or resume return
2. Navigate to "Foreign tax credit" / "Form 1116" / "International" section
3. Wizard typically asks:
   - "Did you receive a 1099-DIV with foreign tax (Box 7)?" → maps to passive basket
   - "Did you work or live abroad and pay foreign tax on wages?" → general basket
   - "Are you taking the FEIE on Form 2555?" → coordination needed
4. The software computes Line 19 limitation automatically. **Verify** against the draft — they sometimes mis-allocate Line 3a or skip the Line 15 QD adjustment.
5. After the wizard, find a "Form 1116 summary" or "International credits" review screen. Compare every line to the draft. Override anything that disagrees.
6. Continue Form 1040 review.
7. E-file.

Provider-specific notes:

- **TurboTax**: handles the de-minimis $300 election automatically based on 1099-DIV imports. For full 1116, the wizard works but the user must override Line 15 QD adjustment manually if it doesn't apply correctly.
- **FreeTaxUSA**: solid 1116 support; wizard explicitly asks the basket question.
- **H&R Block**: good for passive basket, weaker for general basket with FEIE coordination.
- **TaxSlayer**: requires manual entry of carryover from prior years.

---

## Section 3 — Paper filing

### Assemble the return

Order (top to bottom):

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in order
3. **Schedule A** if itemizing (or attached Schedule B for interest/dividends)
4. **Form 1116** — one per basket; the summary 1116 has Part IV filled
5. **Form 2555** if also using FEIE (coordinate first)
6. **Form 8938** if specified foreign financial assets exceed reporting threshold
7. **Other schedules and forms** in attachment-sequence order
8. **W-2s and 1099s** with federal withholding stapled to front of 1040

Single staple, upper-left corner. No paperclips. No double-sided.

### Mailing addresses

Look up at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment by:
1. Form (1040)
2. Payment vs. no payment
3. State (or "Foreign country" for filers abroad)

Filers abroad mail to the Austin, Texas service center (verify the current address each year).

### Mailing best practices

- USPS Certified Mail with Return Receipt (or international equivalent) for proof of timely filing under IRC §7502
- Postmark by April 15 (June 15 for filers abroad with auto-extension; further extension via Form 4868)
- Photocopy the entire return for the user's records
- If paying, attach Form 1040-V with check made to "United States Treasury", with SSN + "Form 1040" + tax year on the memo line

### Producing the printable PDF

1. Download the latest revision of Form 1116 from https://www.irs.gov/pub/irs-pdf/f1116.pdf
2. Open in a fillable-PDF tool (Adobe, Preview on macOS, pdftk)
3. Map draft values to PDF field names — they're stable on IRS forms
4. Save as flattened PDF for printing

Form 1116 has multiple page-2 sections; ensure all pages print and the basket checkbox is visible.

---

## Section 4 — Submission state machine

After filing:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (24-48 hours e-file; 4-8 weeks paper)
3. **Processed** — fully ingested
4. **Refund / balance due / notice** — IRS may send CP2000 if foreign income/tax mismatches third-party reports

Follow-up checks:

- **E-file**: status via tax software or IRS "Where's My Refund"
- **Account transcript**: https://www.irs.gov/individuals/get-transcript
- **CP2000 notice for foreign tax**: usually triggered when the user's reported FTC differs from broker-reported 1099-DIV Box 7. Respond with substantiation (foreign tax payment receipts).

The agent should set a 7-day post-submission reminder.

---

## Security and consent rules

Non-negotiable:

1. **Never file without explicit consent** at the moment of submission
2. **Never store SSN, DOB, PIN, or prior-year AGI** in agent logs or transcripts
3. **Never bypass identity verification or CAPTCHA**
4. **Always capture submission confirmations** as screenshots stored under the user's account
5. **If anything looks wrong** — math disagreement, FFFF reject, unexpected screen — **stop and surface the issue**. Don't retry blindly.
6. **Foreign tax substantiation**: keep the user's foreign tax payment receipts (or foreign return) for at least 10 years, given the 10-year FTC carryforward — the IRS may audit a carryforward year and ask for substantiation of the originating year's tax payment.
