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

User has AGI ≤ $89,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners; $89,000 AGI limit for the
    2026 filing season, https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free)
    Each partner sets its own eligibility rules and form list. Check the
    partner's form list for Form 1116 before relying.
    Browser flow is provider-specific; do not write deterministic flows.

User wants to fill the form directly?
  → IRS Free File Fillable Forms (FFFF), any income level, closes Oct. 15, 2026
    The 2026-season forms list includes Form 1116 and Schedule B (Form 1116).
    FFFF needs a 10-digit U.S. cell phone number (SMS) and accepts no
    attachments beyond the forms it offers; if Form 1116 statements (currency
    conversion, line 2/3b lists) must be attached, use another e-file provider
    or paper. Use Section 1.

User has paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct)?
  → Use the software's "foreign tax credit" / "Form 1116" wizard.
    Use Section 2 (generic pattern).

User wants paper?
  → Print Form 1040 + Form 1116 (one per basket) + supporting schedules.
    Use Section 3.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: forms available Jan. 26, 2026 for the 2026 season (tax year 2025); the program closes Oct. 15, 2026. Create a new account for the current filing year even if the user had one before (no credentials carry over). The account requires a 10-digit U.S. cell phone number that receives SMS, which many filers abroad don't have; if so, use another channel.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, DOB, mailing address, prior-year AGI (for IRS identity verification)
- The completed Form 1116 draft from `SKILL.md` — one per basket if multi-basket
- Form 1040 inputs (filing status, dependents, W-2s, 1099s, etc.) — Form 1116 doesn't stand alone
- Foreign income / foreign tax detail per country in USD
- Prior-year unused FTC by basket, if any
- An email address the user controls and a 10-digit U.S. cell phone number that receives SMS

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
   - Fill line h, "Resident of (name of country)", and the country names on line i (one column per country)
   - Check (j) "Paid" or (k) "Accrued" in Part II — once "Accrued" elected, binding for future years
9. **Fill Part I (Foreign-source taxable income)** — field-by-field map:

FFFF shows the IRS form itself; the captions below are the 2025 form's line captions.

| Form 1116 line | Form caption | Source (in draft) |
|----------------|-------------|-------------------|
| i | "Enter the name of the foreign country or U.S. territory" (columns A/B/C) | Draft line i |
| 1a | "Gross income from sources within country shown above and of the type checked above" per column | Draft Line 1a per country |
| 1b | Checkbox: employee compensation, total compensation $250,000 or more, alternative sourcing basis | Draft Line 1b |
| 2 | "Expenses definitely related to the income on line 1a" | Draft Line 2 |
| 3a | "Certain itemized deductions or standard deduction" | Draft Line 3a |
| 3b | "Other deductions" | Draft Line 3b |
| 3c | 3a + 3b | Verify |
| 3d | "Gross foreign source income" | Draft Line 3d |
| 3e | "Gross income from all sources" | Draft Line 3e |
| 3f | 3d ÷ 3e | Verify |
| 3g | 3c × 3f | Verify |
| 4a | "Home mortgage interest" | Draft Line 4a |
| 4b | "Other interest expense" | Draft Line 4b |
| 5 | "Losses from foreign sources" | Draft Line 5 |
| 6 | 2 + 3g + 4a + 4b + 5 | Verify |
| 7 | 1a − 6 | Verify |

10. **Fill Part II (Foreign taxes)** — for each country row:
    - Country letter + name
    - Column (l): date paid or accrued ("1099 taxes" for taxes reported on a 1099)
    - Columns (m)–(p): foreign currency amounts (taxes withheld at source on dividends, rents and royalties, interest; other foreign taxes)
    - Columns (q)–(t): the same amounts in USD; column (u) total
    - Line 8 = lines A through C, column (u)

11. **Fill Part III (§904 limitation)** (FFFF does only basic calculations; verify every line):
    - Line 9 = Line 8
    - Line 10 = Carryover from Schedule B (Form 1116) line 3, column (xiv), plus carrybacks (manual entry; FFFF doesn't track across years). Add Schedule B (Form 1116) from the Form 1116 when the instructions require it
    - Line 11 = 9 + 10
    - Line 12 = Reduction in foreign taxes (e.g., taxes on Form 2555-excluded income), entered with a minus sign
    - Line 13 = Taxes reclassified under high tax kickout (usually 0)
    - Line 14 = 11 + 12 + 13
    - Line 15 = Line 7; Line 16 = adjustments (usually 0); Line 17 = 15 + 16
    - Line 18 = Form 1040 line 11b − line 14 + Schedule 1-A line 37, or the Worksheet for Line 18 result when the QD/capital gain adjustment applies (manual entry)
    - Line 19 = 17 ÷ 18 ("1" if line 17 is more than line 18)
    - Line 20 = Form 1040 line 16 + Schedule 2 line 1z
    - Line 21 = 20 × 19; Line 22 = §960(c) increase (usually 0); Line 23 = 21 + 22
    - Line 24 = smaller of line 14 or line 23

12. **If multiple baskets**: repeat Steps 8-11 with another Form 1116 instance (different category checkbox).

13. **Fill Part IV** (required for 2025 even with one Form 1116; with several, only on the form with the largest line 24):
    - Lines 25-31: line 24 from each category's Form 1116
    - Line 32 = sum of lines 25-31
    - Line 33 = smaller of line 20 or line 32
    - Line 34 = boycott reduction (usually 0)
    - Line 35 = 33 − 34

14. **Enter Schedule 3 line 1 directly** with Form 1116 line 35: FFFF does not transfer line 35 to Schedule 3 line 1 (FFFF known limitations, Form 1116)

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
- Do not bypass the QD/LTCG adjustment (lines 1a and 18) if the user has qualified dividends or LTCG taxed at preferential rates and doesn't qualify for the adjustment exception — this is a common audit issue
- Do not file with an "Accrued" election unless the user explicitly understands it's binding for future years
- Do not store SSN, DOB, or PIN in any log

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Form 1116 not yet supported" | Filing before the form's availability date | Check the FFFF forms list (01/26/2026 this season); the program closes Oct. 15, 2026 |
| Line 19 above 1 | Line 17 > Line 18 | Enter "1" (form instruction); then check for US-source items or a mis-allocated deduction |
| "Identity verification failed" | Wrong prior-year AGI | Get IRS transcript |
| FFFF won't accept multiple 1116 | A copy limit on the current FFFF forms list (none listed for Form 1116 in the 2026 season) | File on paper or use paid software |
| Schedule 3 Line 1 doesn't populate | FFFF doesn't transfer line 35 (known limitation) | Enter line 35 on Schedule 3 line 1 directly |
| Can't create the account | No 10-digit U.S. cell phone number | Use another e-file provider or paper |
| Required statement can't be attached | FFFF accepts only the forms it offers | Use another e-file provider or paper |

---

## Section 2 — Generic tax-software pattern

For users with paid tax software:

1. Sign in → start or resume return
2. Navigate to "Foreign tax credit" / "Form 1116" / "International" section
3. Wizard typically asks:
   - "Did you receive a 1099-DIV with foreign tax (Box 7)?" → maps to passive basket
   - "Did you work or live abroad and pay foreign tax on wages?" → general basket
   - "Are you taking the FEIE on Form 2555?" → coordination needed
4. The software computes the line 19-24 limitation automatically. **Verify** against the draft — check the Line 3a allocation and the line 1a / line 18 QD adjustment.
5. After the wizard, find a "Form 1116 summary" or "International credits" review screen. Compare every line to the draft. Override anything that disagrees.
6. Continue Form 1040 review.
7. E-file.

Provider behavior changes each season. Before relying on a product, check its current help pages for: Form 1116 support for each category the user needs, the $300/$600 no-Form-1116 election, Schedule B (Form 1116) carryovers, and Form 2555 coordination.

---

## Section 3 — Paper filing

### Assemble the return

Order (top to bottom):

1. **Form 1040** (signed in ink)
2. **Schedule 1, 2, 3** in order
3. **Schedule A** if itemizing (or attached Schedule B for interest/dividends)
4. **Form 1116** — one per basket; the one with the largest line 24 has Part IV filled
5. **Form 2555** if also using FEIE (coordinate first)
6. **Form 8938** if specified foreign financial assets exceed reporting threshold
7. **Other schedules and forms** in attachment-sequence order; supporting statements (currency conversion, line 2/3b lists) last, in the same order as the forms they support
8. **Forms W-2** (and W-2G / 1099-R if tax was withheld) attached to Form 1040 (2025 Form 1040 instructions, "Assemble Your Return")

Single staple, upper-left corner. No paperclips. No double-sided.

### Mailing addresses

Look up at https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment by:
1. Form (1040)
2. Payment vs. no payment
3. State (or "Foreign country" for filers abroad)

From the 2025 Form 1040 instructions ("Where Do You File?"), for filers who live in a foreign country or U.S. territory, use an APO/FPO address, file Form 2555 or 4563, or are dual-status aliens:

- No payment enclosed: Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215
- Check or money order enclosed: Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303

A US-resident filer who attaches Form 1116 without Form 2555 uses the address for their state in the same table. Re-check the table each year.

### Mailing best practices

- USPS Certified Mail with Return Receipt (or international equivalent) for proof of timely filing under IRC §7502
- Postmark by April 15, 2026 (June 15, 2026 for US citizens and residents living abroad under the automatic 2-month extension, with a statement attached explaining the qualifying situation; Form 4868 filed by June 15 extends filing to Oct. 15; interest runs from April 15) (Pub. 54, ch. 1)
- Photocopy the entire return for the user's records
- If paying by check, put the check and Form 1040-V loose in the envelope (don't staple or attach them to the return); make the check payable to "United States Treasury" and write name, address, daytime phone, SSN, and "2025 Form 1040" on it (Form 1040-V instructions)

### Producing the printable PDF

1. Download the latest revision of Form 1116 from https://www.irs.gov/pub/irs-pdf/f1116.pdf
2. Open in a fillable-PDF tool (Adobe, Preview on macOS, pdftk)
3. Map draft values to PDF field names — they're stable on IRS forms
4. Save as flattened PDF for printing

Form 1116 is two pages (Parts III and IV on page 2); ensure both pages of every copy print and the category checkbox is visible.

---

## Section 4 — Submission state machine

After filing:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (allow 24-48 hours after e-file per the FFFF page; for paper, refund status appears about 4 weeks after mailing per IRS Free File / Where's My Refund)
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
