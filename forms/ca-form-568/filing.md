# Filing California Form 568 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 568 draft and actually file it with the California Franchise Tax Board (FTB). This file describes deterministic flows the agent can follow; it's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

California's e-file landscape is narrower than federal because **CalFile (the FTB's free filing tool) does not support Form 568** — it's an individual-only tool. Form 568 is filed through tax software that supports California business e-file, or on paper. **An LLC that prepares an original or amended return with tax preparation software must e-file it** (R&TC §18621.10; FTB "e-file for Business" page, updated 03/23/2026); the FTB may grant a waiver for technology constraints, undue financial burden, or reasonable cause. Payments (FTB 3522, 3536, 3537, and balances due) can be made separately with Web Pay, credit card, electronic funds withdrawal through the software, or a paper voucher.

Mailing addresses, extension lengths, and due dates below are from the 2025 Form 568 Booklet, General Information E (https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf) and the 2025 FTB 3522 / 3536 / 3537 vouchers. Re-check them in the next year's booklet.

```
User wants to make payments only ($800 tax via 3522, estimated fee or fee
balance via 3536, NCNR members' tax on extension via 3537)?
  → Use FTB Web Pay for Businesses (free, FTB-hosted)
    Browser automation: feasible; labels change, read the screen.
    Use Section 1 below.

User prepared (or will prepare) Form 568 in tax software?
  → E-file is required (R&TC §18621.10)
    Browser automation: provider-specific. Ask the user which product they
    use and confirm it lists California Form 568 business e-file.
    Skip — proprietary flows change too often for deterministic automation.
    Use Section 2 (generic pattern).

User is hand-preparing Form 568 (no software) or has an FTB e-file waiver?
  → Print, sign, mail to FTB
    "Browser automation": prepare PDF, give address.
    Use Section 3.

User can't file by the original due date?
  → No form needed (automatic extension to FILE for an LLC in good standing:
    7 months for partnership-classified LLCs and SMLLCs owned by a
    partnership; 6 months for other SMLLCs)
    BUT: the LLC fee balance (FTB 3536) and nonconsenting nonresident
    members' tax (FTB 3537) are still due by the original due date.
    Use Section 4.
```

---

## Section 1 — FTB Web Pay (payments only)

URL: <https://www.ftb.ca.gov/pay/index.html> (business bank-account payments: <https://www.ftb.ca.gov/pay/bank-account/index.asp>)

**Scope**: Web Pay handles the **$800 annual LLC tax** (the FTB 3522 payment), the **estimated LLC fee and any fee balance** (FTB 3536), the **extension payment** for nonconsenting nonresident members' tax (FTB 3537), and balances due with the return. It does **not** file Form 568 itself. LLCs can pay immediately or schedule payments up to a year in advance (2025 FTB 3522 / 3536 / 3537 instructions). When paying by Web Pay, do not also mail the paper voucher.

### Pre-flight

Agent must have:

- The user's permission to authorize an electronic payment from the LLC's bank account
- LLC's California Secretary of State (SOS) file number, exactly as in SOS records
- LLC's federal EIN
- LLC's exact legal name as registered with FTB
- LLC's bank account routing and account numbers (single-use; do **not** store)
- Tax year the payment applies to
- Form being paid (3522 for $800 tax, 3536 for estimated fee)

### Browser flow — Form 3522 ($800 annual tax)

1. **Navigate** to <https://www.ftb.ca.gov/pay/bank-account/index.html>
2. **Select** the business entity / LLC path and the annual-tax payment type (labels change; read the screen and match the payment to "annual tax" for the correct taxable year)
3. **Enter LLC identification**:
   - SOS file number
   - Federal EIN
   - LLC legal name
4. **Enter payment details**:
   - Taxable year (the year the $800 covers — the $800 paid in April 2026 is the 2026 annual tax)
   - Amount: $800.00
   - Routing and account numbers
   - Account type (checking / savings)
5. **Review and submit**
6. **Capture the confirmation number**. FTB displays a confirmation page with the confirmation number — screenshot it. The agent should also save the user's email confirmation if FTB sends one.
7. **Check the payment later** in the LLC's MyFTB account (<https://www.ftb.ca.gov/myftb/index.asp>) before relying on it for Form 568, line 8.

### Browser flow — Form 3536 (estimated LLC fee)

Same flow as 3522, but at step 2 select the estimated LLC fee payment type instead. The amount is the user's estimate of the LLC fee from the tier table (2025 Form 568 Booklet, General Information F):

- $0 if expected total income < $250,000
- $900 if $250,000 - $499,999
- $2,500 if $500,000 - $999,999
- $6,000 if $1M - $4,999,999
- $11,790 if $5M+

**Underestimation penalty**: if the amount paid by the 15th day of the 6th month is less than the fee for the year, a penalty of 10% of the shortfall applies — unless the amount paid is at least the LLC's total fee for the preceding taxable year (R&TC §17942(d)(2); 2025 FTB 3536 instructions). Ask the user for the prior-year fee; paying at least that amount by the 6th-month date avoids the penalty. Any remaining fee is paid with FTB 3536 by the return's original due date.

### What the agent should NOT do

- Do not submit a Web Pay transaction without the user's explicit go-ahead at step 5
- Do not store the user's bank account numbers in any log or transcript — pull at filing time, use, discard
- Do not use Web Pay for the actual Form 568 return (it doesn't support it)
- Do not pay $800 for the wrong taxable year — a late prior-year $800 goes to that year (the booklet says to use that year's FTB 3522, not the next year's)

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Entity not found" | Wrong SOS file number or EIN combination | Verify both with the user; SOS file number must match FTB records |
| "LLC is not in good standing" | LLC has prior unpaid $800 or fee | Pay prior years first, then current |
| Payment rejected by bank | Wrong routing/account, or insufficient funds | Re-enter or use alternative bank account |
| Confirmation page didn't load | Browser timeout | Check FTB account history before retrying — duplicate payments are not auto-reversed |

---

## Section 2 — Generic business-tax-software pattern

For users with tax software that supports California Form 568 business e-file (ask the user which product; confirm Form 568 is on the product's supported-forms list), the flow is:

1. Sign in → start or resume a California business return
2. Navigate to "California Form 568" or "California LLC return" section
3. The software typically asks:
   - "Initial / final / amended?" → Item H
   - "Single-member or multi-member?" → Question U(1), Question K, and whether Schedule K appears
   - "Owner type (SMLLC)?" → Single Member LLC Information on Side 3; also sets the due date
   - "Total California-source income?" → Schedule IW
4. Enter Schedule IW line-by-line from the draft
5. Enter Schedule K lines from the draft (multi-member only); software typically pulls federal K and prompts for California adjustments
6. Enter member information (K-1 568): name, SSN/ITIN/EIN, address, %, residency
7. Mark each nonresident member's Form 3832 status; software generates Schedule T if applicable
8. Review the computed Form 568 — verify each line against the draft. **Override anything that disagrees** with the draft and investigate the discrepancy.
9. Sign the California e-file authorization (FTB 8453-LLC) as the software instructs, then e-file. The software handles transmission to the FTB. Record the acknowledgment. A balance due on an e-filed return is paid by Web Pay, credit card, EFW, or FTB 3588 mailed to the address in Section 3.

**Why this section is generic**: provider-specific selectors and screens change every tax year. An agent should rely on label text (visible to the user) and human-readable navigation rather than DOM IDs.

**Common gotcha**: consumer individual-return products often do not include the business Form 568. If the user's product does not list Form 568, the LLC needs a product that does; paper is allowed only for a return not prepared with software or under an FTB e-file waiver.

---

## Section 3 — Paper filing

Paper is for a hand-prepared return (not prepared with tax software) or a return covered by an FTB e-file waiver (R&TC §18621.10).

### Assemble the return

Include, in form order:

1. **Form 568, Sides 1–7** as required (Side 3 signed by an authorized member or manager; a single-member LLC completes Sides 1, 2, 3, and 7, plus Schedules B and K only if the $3,000,000 test is met)
2. **Schedule K-1 (568)** for each member of a multi-member LLC (the count must equal Question K)
3. **Schedules L, M-1, M-2** unless federal Form 1065 Schedule B Questions 4a–4c are all "Yes" and there are 10 or fewer members
4. **Schedule T** (if nonconsenting nonresident members) — it is on Side 4
5. **Schedule R** (if apportioning), **FTB 3885L** (depreciation), **Schedule D (568)** / **Schedule EO** if used
6. **FTB 3832** (nonresident members' consent)
7. **Form 592-B / 593** at the front lower portion if the LLC claims withholding on line 11
8. Copies of federal **Form 8832** (election year) and **Form 8886** (reportable transactions) when applicable

Do not attach copies of federal Schedule K-1 (1065) (2025 booklet, Question V instructions). Enclose, but do not staple, any payment (2025 Form 568, Side 1). Do not send the $800 annual tax with Form 568; it is paid on FTB 3522.

### Mailing addresses

Form 568 mailing addresses depend on whether a payment is enclosed (2025 Form 568 Booklet, General Information E):

**With payment** (a balance is owed with the return):

```
FRANCHISE TAX BOARD
PO BOX 942857
SACRAMENTO CA 94257-0501
```

**Without payment, paid electronically, or requesting a refund:**

```
FRANCHISE TAX BOARD
PO BOX 942857
SACRAMENTO CA 94257-0500
```

**Payment for an e-filed return** (FTB 3588), and the **FTB 3522, 3536, and 3537 vouchers** (per each 2025 voucher):

```
FRANCHISE TAX BOARD
PO BOX 942857
SACRAMENTO CA 94257-0531
```

**Private delivery service** (cannot deliver to a PO box): FRANCHISE TAX BOARD, SACRAMENTO CA 95827.

The FTB LLC web page (updated 03/05/2026) lists 94257-0631 for mailed FTB 3522 payments, which conflicts with the 94257-0531 printed on the 2025 and 2026 FTB 3522. Use the address printed on the voucher for the year and tell the user about the conflict. Re-check addresses each year in the booklet; do not hardcode them across years.

### Mailing best practices

- Send via **USPS Certified Mail with Return Receipt**, or a designated private delivery service, for proof of timely filing (California follows the federal timely-mailing rules; 2025 booklet, General Information E)
- Postmark the return by the original due date, or by the extended due date if filing under the automatic extension; any fee balance and NCNR tax must still be paid by the original due date
- Keep a complete copy of the entire return for the user's records
- If paying by check, use black or blue ink, make it payable to "Franchise Tax Board", and write the SOS file number, FEIN, and "2025 Form 568" on the check (2025 booklet, General Information E)

### Producing the printable PDF

If the agent has access to FTB fillable PDFs, the deterministic flow is:

1. Download the latest revision of Form 568 from <https://www.ftb.ca.gov/forms/>
2. Open in a PDF tool that supports form filling (Adobe Acrobat, Preview on macOS supports field input, `pypdf` for scripted)
3. Map draft values to PDF field names
4. Save as flattened PDF for printing
5. Print, sign, mail

FTB form-field names are stable within a tax year but renumber across years. Cache the field list once per tax year.

---

## Section 4 — Automatic extension

If the LLC in good standing cannot file by the original due date, **California grants an automatic extension to FILE** with no form required (2025 booklet, General Information E; R&TC §18567; 2025 FTB 3537). A suspended or forfeited LLC gets none. For calendar 2025:

| LLC | Original due date | Extension | Extended due date |
|-----|-------------------|-----------|-------------------|
| Partnership-classified | March 16, 2026 (March 15 was a Sunday) | 7 months | October 15, 2026 |
| SMLLC owned by a partnership or partnership-classified LLC | March 16, 2026 | 7 months | October 15, 2026 |
| SMLLC owned by an S corporation | March 16, 2026 | 6 months | September 15, 2026 |
| Other SMLLC (individual, C corporation, estate or trust owner) | April 15, 2026 | 6 months | October 15, 2026 |

Fiscal-year LLCs count the same number of months from their own due date.

**Extension to FILE is not extension to PAY.** The LLC fee not paid as a timely estimate (pay with **FTB 3536**) and any nonconsenting nonresident members' tax (pay with **FTB 3537**) are due by the original due date; the $800 annual tax was due by the 15th day of the 4th month of the taxable year. Use FTB 3537 only if NCNR tax is owed and the return will be filed on extension (2025 FTB 3537). If unpaid by the due date:

- Late-payment penalty: 5% of the unpaid amount plus 0.5% for each month or part of a month, up to 40 months, maximum 25% (R&TC §19132); each item is computed separately from its own due date
- Interest from the original due date at the FTB's posted rate (7% for July 1, 2025 – December 31, 2026; R&TC §19521)
- Estimated-fee penalty: 10% of the shortfall unless the 6th-month payment was at least the prior-year fee (R&TC §17942(d)(2))
- If the return is not filed by the extended date, the extension does not apply and the late-filing penalty (5% per month, max 25%, R&TC §19131) runs from the original due date, plus $18 per member per month (up to 12 months, R&TC §19172)

---

## Section 5 — Submission state machine

After filing (any channel), the LLC's return moves through:

1. **Submitted** — sent to FTB
2. **Accepted** — for e-file, the software reports the FTB acknowledgment
3. **Processed** — FTB has fully ingested the return
4. **Refund issued** OR **balance-due notice** OR **examination notice**

Status checks:

- E-file: check the acknowledgment in the software
- Paper: no acknowledgment is sent; check the account
- Account history (requires login): MyFTB, <https://www.ftb.ca.gov/myftb/index.asp>

The agent should set a follow-up reminder 30 days post-submission to check status.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file or pay without explicit user consent** at the moment of submission. "I authorize you to file Form 568 / pay $X to FTB on the LLC's behalf right now" must be captured.
2. **Never store SSN, ITIN, FEIN, bank routing/account numbers, or MyFTB credentials** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If FTB asks for identity proof, pause and let the user respond directly.
4. **Always capture submission/payment confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures), **stop and surface the issue**. Don't retry blindly.
6. **Never submit duplicate Web Pay transactions** if the first one's confirmation page didn't load — check the LLC's account history before retrying. FTB will collect both payments and the user has to request a refund.
