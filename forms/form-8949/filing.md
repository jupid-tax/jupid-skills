# Filing Form 8949 + Schedule D (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 8949 draft from `SKILL.md` and actually file it. Form 8949 never files alone — it always attaches to Schedule D, which attaches to Form 1040. The three forms move together.

This file is complementary to `SKILL.md`, which produces the draft. The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below.

---

## Channel decision tree

The user picks the channel. If they don't know, default to **IRS Free File Fillable Forms (FFFF)** — it's free, the field labels match the paper form, and the math auto-checks against Schedule D.

```
User has AGI ≤ ~$84,000 and wants free guided software?
  → IRS Free File (Free File Alliance partners)
    Browser automation: provider-specific (FreeTaxUSA, Cash App Taxes, etc.)
    Skip — proprietary flows change too often for deterministic automation.

User wants to fill the form directly themselves with no software help?
  → IRS Free File Fillable Forms (FFFF)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User has > 100 transactions or already paid for tax software (TurboTax, H&R Block, FreeTaxUSA, Koinly, CoinTracker)?
  → That software's "Investments" / "Schedule D" / "Crypto" import flow
    Browser automation: provider-specific.
    Use Section 2 (generic pattern). Don't write provider-specific flows here.

User wants to file on paper?
  → Print Form 1040 + Schedule D + Form 8949 (one or more pages), sign, mail
    Use Section 3.

User wants to use IRS Direct File?
  → Note: as of early 2026, IRS Direct File supports a narrow set of capital-gain
    scenarios. Crypto and complex 1099-B sets typically fall out of scope.
    Check current scope at https://www.irs.gov/filing/irs-direct-file before automating.
```

---

## High-volume rule (Pub 550 Method 2)

If the user has **100+ transactions** or any single brokerage's 1099-B has a long detail attachment (typical for active traders and crypto exchange CSVs):

- Pub 550 permits **summary reporting** on 8949 — one line per box per brokerage with the totals — instead of itemizing every transaction
- The detail must still be attached as a "broker substitute statement" (PDF) when e-filing, or mailed as Form 8453 with the supporting statements when paper-filing the rest electronically
- Use this when itemizing 800+ rows would otherwise blow up the return without changing the math

The agent's draft should flag eligibility for Method 2 and ask the user which path to take. Software like TurboTax and FreeTaxUSA support summary entry natively; FFFF does not — FFFF requires every line entered, so high-volume filers should pick paid software or paper.

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: FFFF is open from late January through mid-October each year. Outside that window, it returns a "season closed" message.

**Account model**: each tax year is a separate FFFF account. Returning users from prior years cannot reuse credentials — the agent must register fresh each year.

### Pre-flight

Agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI
- The completed 8949 draft from `SKILL.md` — every box's transactions plus totals
- The Schedule D roll-up from the draft
- Form 1040 inputs (filing status, dependents, W-2s, etc.) — 8949 doesn't file alone
- An email address the user controls
- An IP address the user is willing to file from

### Browser flow

The agent navigates and interacts deterministically. Stable selectors are listed where known; treat label text as fallback when DOM IDs change between tax years.

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms
2. **Click** "Start Free File Fillable Forms" → redirects to the FFFF launchpad (URL changes per tax year)
3. **Register / Sign in**:
   - First-time: click "Create Account", complete email + password + identity verification
   - Returning: only works for the current tax year's account
4. **Identity verification**: FFFF asks for prior-year AGI or a self-select PIN. If the user doesn't have prior-year AGI handy, retrieve from IRS transcript (Form 4506-T or https://www.irs.gov/individuals/get-transcript) or pause and ask.
5. **Start a new return** → "Form 1040" landing
6. **Fill 1040 header** (name, SSN, filing status, dependents)
7. **Add Form 8949**:
   - Click "Add a Form / Schedule"
   - Search "Form 8949" — or pick from the list
   - FFFF opens **one page per box**. To enter Boxes A and D, you'll create two pages. To enter Boxes A, B, D, E, you'll create four pages. The agent should iterate through every box that has at least one row in the draft.
8. **For each Form 8949 page**:
   - Check the corresponding box at the top (A, B, C in Part I; D, E, F in Part II) — exactly one
   - Enter rows one at a time. FFFF reveals more rows as you fill prior ones.
   - Field-by-field mapping per row:

| Form 8949 column | FFFF field label | Source in draft |
|------------------|------------------|------------------|
| (a) Description | "Description of property" | Draft column (a) |
| (b) Date acquired | "Date acquired" — MM/DD/YYYY (or "VARIOUS" / "INHERITED") | Draft column (b) |
| (c) Date sold | "Date sold" — MM/DD/YYYY | Draft column (c) |
| (d) Proceeds | "Proceeds" | Draft column (d) |
| (e) Cost or other basis | "Cost basis" | Draft column (e) |
| (f) Codes | "Code(s) from instructions" — text | Draft column (f) |
| (g) Amount of adjustment | "Amount of adjustment" — positive number | Draft column (g) |
| (h) Gain/Loss | (auto-computed) | (verify equals draft column (h)) |

9. **Page totals** — FFFF auto-sums each column at the bottom of each 8949 page. Verify the sums match the draft's box totals.
10. **Add Schedule D**:
    - Click "Add a Form / Schedule" → Schedule D
    - Schedule D imports totals from each 8949 page automatically *if* the boxes are checked correctly
    - Verify Lines 1b, 2, 3 (short-term boxes) and Lines 8b, 9, 10 (long-term boxes) match the draft's box totals
    - Lines 7 (net short-term) and 15 (net long-term) compute from the box totals
    - Line 16 (net capital gain/loss) computes; it carries to Form 1040 Line 7
11. **Capital loss carryover** — if Line 16 is a net loss exceeding the $3,000 limit:
    - Schedule D Lines 21–22 hold the limited-deduction calculation
    - The Capital Loss Carryover Worksheet from the Schedule D instructions calculates next year's carryforward — fill it and save it; it doesn't get e-filed but the user needs it for next year's return
12. **Attach related forms** if the draft requires them:
    - Form 8960 (NIIT) if MAGI > $200K single / $250K MFJ
    - Form 6781 if §1256 contracts traded
    - Form 8824 if §1031 like-kind exchange occurred (separate from 8949)
13. **Run FFFF's "Check Form" / "Verify"** — resolves math errors and missing fields. Resolve every flag.
14. **Cross-check** every auto-computed field against the draft. If FFFF's Schedule D Line 7 disagrees with the draft's net short-term, **stop**; one of the two is wrong.
15. **Save the return** (FFFF stores progress server-side).
16. **Submit** when verified, attachments are present, and 1040 is otherwise complete:
    - Click "E-file Now"
    - Sign electronically (Self-Select PIN — usually a 5-digit number, plus prior-year AGI for identity proof)
    - Submit
17. **Capture the submission ID** that FFFF displays. Save the screenshot.
18. **Wait 24–48 hours**, then log back in to confirm IRS acceptance. On rejection, read the rejection code, fix, resubmit.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 16
- Do not bypass FFFF's verification (step 13) even if it looks like a false positive
- Do not enter "0" in column (e) cost basis when basis is unknown — that overstates the gain. Stop and ask the user for the basis.
- Do not store the user's SSN, DOB, PIN, or full account/ID numbers in any log or transcript

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Identity verification failed" | Wrong prior-year AGI | Ask user for IRS transcript |
| "Schedule D total does not match Form 8949" | Box checked on wrong 8949 page | Re-check box selection on each 8949 page |
| "Form not yet supported" | Filing too early in the season | Wait until late January |
| Wash sale code "W" with no adjustment in (g) | Missing adjustment value | Re-enter (g) with disallowed loss as positive number |
| Session timeout | Idle > 30 min | FFFF saves progress; log back in |
| 1099-B totals don't tie to draft | Closed account, transferred lot, or 1099-B correction issued | Pull every 1099-B again before filing |

---

## Section 2 — Generic tax-software pattern (paid software)

For users with paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), or specialized crypto tax software (Koinly, CoinTracker, ZenLedger, TaxBit) which exports 8949 to general filing software:

1. Sign in → start or resume a return
2. Navigate to "Investments" / "Stocks" / "Cryptocurrency" / "Schedule D" section
3. **Import flow** — most software offers direct broker imports:
   - Schwab, Fidelity, Vanguard, Robinhood, E*TRADE: 1099-B import via OAuth or document upload
   - Coinbase, Kraken: CSV upload (formats vary by year)
   - Crypto tax software → general software: 8949 PDF or TXF file import
4. **Manual entry alternative**: same field mapping as Section 1 step 8.
5. **Wash sale**: most software auto-detects within a single broker's data. Cross-broker and cross-account washes are user-supplied. The agent must surface this rule explicitly to the user — the software won't.
6. **Crypto-specific gotcha**: software typically doesn't pull crypto exchange CSVs natively. The user must either upload the CSV or use a crypto tax tool first. Coinbase 1099-MISC (for staking) is *not* a 1099-B and won't import basis. The agent needs to upload the exchange CSV separately.
7. After entry, the software shows a "Schedule D Summary" — verify each line against the draft. Override anything that disagrees.
8. Continue through Form 1040 review; software computes Form 8960 (NIIT) automatically if applicable.
9. Pay the software fee; e-file.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. An agent should rely on label text and human-readable navigation rather than DOM IDs that break each January.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (FFFF closed, complex return with many statement attachments, user preference, identity-theft concerns).

### Assemble the return

Order matters — the IRS expects this stack from top to bottom:

1. **Form 1040** (signed by all filers, in ink)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule D**
4. **Form 8949** — one set of pages per box used (a single page can hold ~14 rows; use as many continuation pages as needed; staple in order)
5. **Form 8960** (if NIIT threshold exceeded)
6. **Form 6781** (if §1256 contracts traded)
7. **Form 4797** (if any business-use asset sales — separate from 8949)
8. **Form 8824** (if §1031 exchange)
9. **All other schedules and forms** in attachment-sequence order printed on each form (top-right corner)
10. **W-2 Copy B** stapled to the front of Form 1040 (lower-left)
11. **1099s with federal withholding** also stapled

Use a single staple in the upper-left corner. Don't paperclip. Don't double-side print. Each form printed at full size on letter paper.

### Substitute statements (Pub 550 Method 2)

If summary-reporting on 8949, the broker substitute statement (the detail not entered line-by-line) must be attached:

- One copy per brokerage, labeled with the brokerage name and tax year
- Stapled behind the 8949 page that summarizes that brokerage's totals
- Each detail page must show: description, date acquired, date sold, proceeds, basis, code, adjustment, gain/loss — same eight columns as 8949

### Mailing addresses (verify each year)

The IRS mailing address differs by state and by whether the return includes a payment. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses — they shift between years and are split by state.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing (IRC §7502 timely-mailing-as-timely-filing rule)
- Postmark by April 15 (or extension date if Form 4868 was filed)
- Keep a complete photocopy of the entire return for the user's records
- If paying, attach Form 1040-V payment voucher with check made out to "United States Treasury"; write SSN + "Form 1040" + tax year on the check memo line

---

## Section 4 — Submission state machine

After filing (any channel), the user's return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — IRS acknowledges receipt and basic validation passed
3. **Processed** — IRS has fully ingested the return
4. **Refund issued** OR **Balance due notice** OR **CP2000 notice** (most common for 8949 mismatches) OR **Audit notice**

The **CP2000** is the 8949-specific risk: the IRS computer matches your Box A/D entries against broker 1099-B totals and sends a CP2000 if anything doesn't tie. Common causes:

- Missed a 1099-B from a closed account
- Used wrong box (A vs B vs C, or D vs E vs F)
- Wash sale loss reported without code "W" while broker reported it with code
- Crypto disposition with basis = $0 because the user didn't have records (CP2000 won't fire on this — but the IRS will assume basis = $0 in their own audit and tax the full proceeds)

Status checks:

- E-file: usually Accepted within 24–48 hours
- Paper: 4–8 weeks for Acceptance acknowledgment
- Refund tracking: https://www.irs.gov/refunds (Where's My Refund tool, requires SSN + filing status + refund amount)
- Account transcript: https://www.irs.gov/individuals/get-transcript (shows all activity once Processed)

The agent should set a follow-up reminder 7 days post-submission to check status, and a separate 9-month reminder to watch for CP2000 notices.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 8949 + Schedule D + Form 1040 through FFFF on my behalf right now" must be captured.
2. **Never store SSN, DOB, PIN, prior-year AGI, full brokerage account numbers, or full crypto exchange API keys** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never email full brokerage account numbers, SSNs, or 1099-B detail** anywhere. If sending the user a confirmation, redact all but the last 4 digits.
4. **Never bypass identity verification or CAPTCHAs.** If the IRS or software asks the user to prove identity, pause and let the user respond directly.
5. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
6. **If anything looks wrong** (Schedule D total disagrees with 8949 totals, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
7. **Crypto exchange CSVs** often contain wallet addresses and transaction hashes — treat these as sensitive. Do not paste raw CSV content into general-purpose chat tools.
