# Filing California Form 568 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 568 draft and actually file it with the California Franchise Tax Board (FTB). This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

California's e-file landscape is narrower than federal because **CalFile (the FTB's free filing tool) does not support Form 568** — it's an individual-only tool. Form 568 must be filed via FTB-approved third-party software, paper, or the limited Web Pay channel for the $800 tax and LLC fee vouchers (Forms 3522 / 3536) only.

```
User wants to make voucher payments only ($800 tax via 3522, estimated fee via 3536)?
  → Use FTB Web Pay (free, FTB-hosted, supports business entity logins)
    Browser automation: feasible, deterministic.
    Use Section 1 below.

User wants to e-file the full Form 568?
  → Use FTB-approved business e-file software
    Browser automation: provider-specific. Common options:
      - Lacerte / ProSeries (Intuit Pro)
      - Drake Tax
      - TaxAct Business
      - FreeTaxUSA (limited Form 568 support — verify)
      - TurboTax Business (Windows only, supports CA)
    Skip — proprietary flows change too often for deterministic automation.
    Use Section 2 (generic pattern).

User wants to file Form 568 on paper?
  → Print, sign, mail to FTB
    "Browser automation": prepare PDF, give address.
    Use Section 3.

User missed the deadline and needs the automatic 7-month extension?
  → No form needed (CA grants extension to FILE automatically)
    BUT: the $800 tax + LLC fee + nonresident withholding are still due by
    the original deadline. Pay via Form 3537 voucher and Web Pay.
    Use Section 4.
```

---

## Section 1 — FTB Web Pay (Form 3522 + Form 3536 only)

URL: <https://www.ftb.ca.gov/pay/index.html>

**Scope**: Web Pay handles the **$800 annual LLC tax** (Form 3522) and the **estimated LLC fee** (Form 3536). It does **not** file Form 568 itself — only the payments. For the return, see Section 2 (e-file software) or Section 3 (paper).

**Availability**: Web Pay is available year-round, 24/7.

### Pre-flight

Agent must have:

- The user's permission to authorize an electronic payment from the LLC's bank account
- LLC's California Secretary of State (SOS) file number (12 digits, starts with `2`)
- LLC's federal EIN
- LLC's exact legal name as registered with FTB
- LLC's bank account routing and account numbers (single-use; do **not** store)
- Tax year the payment applies to
- Form being paid (3522 for $800 tax, 3536 for estimated fee)

### Browser flow — Form 3522 ($800 annual tax)

1. **Navigate** to <https://www.ftb.ca.gov/pay/bank-account/index.html>
2. **Select** "Make a Payment" → "Limited Liability Company" → "Annual Tax (Form 3522)"
3. **Enter LLC identification**:
   - SOS file number
   - Federal EIN
   - LLC legal name
4. **Enter payment details**:
   - Tax year (the year the $800 covers)
   - Amount: $800.00
   - Routing and account numbers
   - Account type (checking / savings)
5. **Review and submit**
6. **Capture the confirmation number**. FTB displays a confirmation page with the confirmation number — screenshot it. The agent should also save the user's email confirmation if FTB sends one.
7. **Wait 1-2 business days** for FTB to process. The payment will then appear in the LLC's account history at <https://www.ftb.ca.gov/login/login-as-a-business-representative.html>.

### Browser flow — Form 3536 (estimated LLC fee)

Same flow as 3522, but at step 2 select "Estimated Fee (Form 3536)" instead. The amount is the user's estimate of the LLC fee from the tier table:

- $0 if expected total income < $250,000
- $900 if $250,000 - $499,999
- $2,500 if $500,000 - $999,999
- $6,000 if $1M - $4,999,999
- $11,790 if $5M+

**Underestimation penalty**: if Form 3536 payment is less than the actual fee owed by more than 10%, a 10% penalty applies under R&TC §17942(d). The agent should ask the user to estimate at the high end of their expected revenue range.

### What the agent should NOT do

- Do not submit a Web Pay transaction without the user's explicit go-ahead at step 5
- Do not store the user's bank account numbers in any log or transcript — pull at filing time, use, discard
- Do not use Web Pay for the actual Form 568 return (it doesn't support it)
- Do not pay $800 from the wrong tax year — Web Pay accepts payments for current and prior years; pick the right one

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Entity not found" | Wrong SOS file number or EIN combination | Verify both with the user; SOS file number must match FTB records |
| "LLC is not in good standing" | LLC has prior unpaid $800 or fee | Pay prior years first, then current |
| Payment rejected by bank | Wrong routing/account, or insufficient funds | Re-enter or use alternative bank account |
| Confirmation page didn't load | Browser timeout | Check FTB account history before retrying — duplicate payments are not auto-reversed |

---

## Section 2 — Generic business-tax-software pattern

For users with paid software supporting California Form 568 (Lacerte, ProSeries, Drake, TaxAct Business, FreeTaxUSA, TurboTax Business), the flow is:

1. Sign in → start or resume a California business return
2. Navigate to "California Form 568" or "California LLC return" section
3. The software typically asks:
   - "Is this LLC's first year?" → Header H box
   - "Final return?" → Header H box
   - "Single-member or multi-member?" → drives whether Schedule K appears
   - "Total California-source income?" → Schedule IW
4. Enter Schedule IW line-by-line from the draft
5. Enter Schedule K lines from the draft (multi-member only); software typically pulls federal K and prompts for California adjustments
6. Enter member information (K-1 568): name, SSN/ITIN/EIN, address, %, residency
7. Mark each nonresident member's Form 3832 status; software generates Schedule T if applicable
8. Review the computed Form 568 — verify each line against the draft. **Override anything that disagrees** with the draft and investigate the discrepancy.
9. E-file. The software handles transmission to FTB. Record the FTB acceptance number.

**Why this section is generic**: provider-specific selectors and screens change every tax year. An agent should rely on label text (visible to the user) and human-readable navigation rather than DOM IDs.

**Common gotcha**: TurboTax (consumer / Online editions) does **not** support Form 568. TurboTax Business (Windows-only desktop) does. If the user is on TurboTax Online or TurboTax Self-Employed, redirect to a different product or to paper filing.

---

## Section 3 — Paper filing

Sometimes paper is the right answer (software doesn't support, complex multi-state apportionment, user preference).

### Assemble the return

Order matters. Stack from top to bottom:

1. **Form 568** (signed by managing member or authorized representative)
2. **Schedule IW** (Income Worksheet)
3. **Schedule K (568)** (if multi-member)
4. **Schedule K-1 (568)** for each member (kept by LLC and given to members; copies attached to Form 568)
5. **Schedule L, M-1, M-2** (if total receipts ≥ $250K or assets ≥ $1M)
6. **Schedule T** (if nonconsenting nonresident members)
7. **Schedule R** (if multi-state apportionment)
8. **Form 3832** (consent of nonresident members) — one per consenting nonresident
9. **Federal Form 1065 + Schedules K-1** (federal copy attached if multi-member)
10. **Federal Schedule C / E / F** (attached if SMLLC; copy from owner's 1040)

Use a single staple in the upper-left corner. Print at full size on letter paper. Don't paperclip.

### Mailing addresses

Form 568 mailing addresses depend on whether a payment is enclosed:

**Without payment** (e.g., $800 already paid via Form 3522, fee paid via Form 3536, and no balance due):

```
Franchise Tax Board
PO Box 942857
Sacramento, CA 94257-0501
```

**With payment** (a balance is owed with the return):

```
Franchise Tax Board
PO Box 942857
Sacramento, CA 94257-0531
```

Verify current addresses at <https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html> — addresses occasionally change. Do not hardcode.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt** for proof of timely filing
- Postmark by the original due date (March 15 for partnership-classified, April 15 for SMLLC), even if using the automatic 7-month extension to file
- Keep a complete photocopy of the entire return for the user's records
- If paying by check, make payable to "Franchise Tax Board"; write the SOS file number, EIN, tax year, and "Form 568" on the memo line

### Producing the printable PDF

If the agent has access to FTB fillable PDFs, the deterministic flow is:

1. Download the latest revision of Form 568 from <https://www.ftb.ca.gov/forms/>
2. Open in a PDF tool that supports form filling (Adobe Acrobat, Preview on macOS supports field input, `pypdf` for scripted)
3. Map draft values to PDF field names
4. Save as flattened PDF for printing
5. Print, sign, mail

FTB form-field names are stable within a tax year but renumber across years. Cache the field list once per tax year.

---

## Section 4 — Automatic 7-month extension

If the LLC misses the original filing deadline, **California grants an automatic 7-month extension to FILE** with no form required. New deadlines:

- Partnership-classified: March 15 → September 15
- SMLLC: April 15 → October 15
- Calendar-year only; fiscal-year LLCs adjust by month

**Extension to FILE is not extension to PAY.** The $800 annual tax (Form 3522), the LLC fee (Form 3536 / final reconciliation), and any nonconsenting nonresident withholding are all still due by the original deadline. If unpaid by the original deadline:

- Late-payment penalty: 5% of unpaid tax + 0.5%/month, max 25% (R&TC §19132)
- Interest: federal short-term rate + 3%, compounded daily (R&TC §19521)
- Estimated-fee penalty: 10% of underpayment (R&TC §17942(d))

To pay the balance owed during extension period, use **Form 3537** (Automatic Extension Payment for LLCs) via Web Pay or paper voucher.

---

## Section 5 — Submission state machine

After filing (any channel), the LLC's return moves through:

1. **Submitted** — sent to FTB
2. **Accepted** — FTB acknowledges receipt and basic validation passed
3. **Processed** — FTB has fully ingested the return
4. **Refund issued** OR **Balance due notice (FTB 4963 / 4961 / 7275)** OR **Audit notice**

Status checks:

- E-file: usually Accepted within 3-5 business days
- Paper: 6-12 weeks for Acceptance acknowledgment
- Account history (requires login): <https://www.ftb.ca.gov/login/login-as-a-business-representative.html>

The agent should set a follow-up reminder 30 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file or pay without explicit user consent** at the moment of submission. "I authorize you to file Form 568 / pay $X to FTB on the LLC's behalf right now" must be captured.
2. **Never store SSN, ITIN, EIN, bank routing/account numbers, or FTB MyFTB credentials** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If FTB asks for identity proof, pause and let the user respond directly.
4. **Always capture submission/payment confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Never submit duplicate Web Pay transactions** if the first one's confirmation page didn't load — check the LLC's account history before retrying. FTB will collect both payments and the user has to request a refund.
