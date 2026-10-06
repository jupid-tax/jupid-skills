# Filing 1099-K-Derived Income (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) takes a completed 1099-K reconciliation worksheet and enters the derived figures into the user's tax software. The 1099-K itself is **not filed by the recipient** — the PSE files it with the IRS. This file covers the recipient-side workflow: turning Box 1a (and adjacent boxes) into entries on Schedule C, Schedule 1, Schedule E, Form 8949, and Form 1040.

The agent must produce a complete `SKILL.md`-format reconciliation *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Why "filing" is misleading for 1099-K

Three properties make 1099-K different from W-9, Schedule C, and most other forms in this skill library:

1. **No standalone return.** The 1099-K is an information return that drives entries on other forms. The recipient never "files a 1099-K" — they file Form 1040 with whichever schedules the underlying activity requires (Schedule C / Schedule 1 / Schedule E / Form 8949).
2. **Document-matching exposure.** The IRS receives the PSE's copy of the 1099-K and runs document matching against the recipient's return. If the return doesn't account for Box 1a (Schedule C / Schedule E / Form 8949 plus the 1099-K entry space at the top of Schedule 1), the IRS can send a CP2000 notice. The reconciliation worksheet from `SKILL.md` is the audit-defense artifact.
3. **Mixed personal/business is the default state.** Most 1099-K filers have personal payments mixed with business income on the same platform. The reconciliation is what separates them.

---

## Channel decision tree

The user picks the tax-software channel. If they don't know, use **IRS Free File guided software** when AGI is $89,000 or less (https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free), **Free File Fillable Forms** for any income level if the user is comfortable with bare forms, or a commercial product. IRS Direct File was not offered in the 2026 filing season; do not route users to it.

```
User has Schedule C activity + multiple 1099s + state return needed?
  → FreeTaxUSA or TurboTax Self-Employed (Section 1)
    Best fit: handles Schedule C, the Schedule 1 1099-K entry space, Form 8949, Schedule E.

User has only personal payments on 1099-K (no business)?
  → IRS Free File (AGI ≤ $89,000) or Free File Fillable Forms (Section 2)
    Only entry needed: the amount in the entry space at the top of Schedule 1.

User has Schedule E (rental real estate)?
  → FreeTaxUSA or TaxSlayer (Section 1), or FFFF if the user knows the forms

User has both Schedule C + Schedule E + Form 8949?
  → TurboTax Self-Employed or FreeTaxUSA Deluxe (Section 1)
    Multi-schedule cases benefit from a paid product's review pass.

User received CP2000 notice for under-reported 1099-K?
  → Respond by mail or fax with the reconciliation worksheet (Section 3)
    Do NOT amend until the IRS asks; CP2000 is a proposed adjustment, not a bill.
```

---

## Section 1 — TurboTax Self-Employed / FreeTaxUSA / TaxSlayer

These are common channels for Schedule C filers. Menu names change each season; confirm each screen against the line the worksheet names.

### Pre-flight

Agent must have:

- The user's permission to enter data on their behalf
- The completed 1099-K reconciliation worksheet from `SKILL.md`
- Other 1099s (1099-NEC, 1099-MISC) the user received
- W-2s if the user also has wage income
- The user's tax-software credentials (the agent MUST NOT create a new account)
- Two-factor authentication available (the agent pauses for the user)

### Browser flow — TurboTax Self-Employed

1. **Sign in** to TurboTax. Accept the latest e-records and signatures disclosure.
2. **Navigate** to the Self-Employment section: Income → Self-Employment → Edit/Add.
3. **Enter the Schedule C trade/business portion**:
   - Click "Add income" → "Form 1099-K"
   - Payer name: from worksheet
   - Box 1a (Gross): from worksheet
   - Box 1b, Box 2 (MCC), Box 3 (transactions): from worksheet (informational; not used in the tax calculation)
   - Box 4 (federal tax withheld): from worksheet — must land on Form 1040 Line 25b
   - State boxes: from worksheet
   - Confirm "All of this 1099-K is for my business" or "Some of this 1099-K is personal" — the latter opens the personal-portion adjustment screen
4. **Enter the personal-portion adjustment** (if applicable):
   - When prompted, enter the personal portion (friends/family + personal-item-loss)
   - Check the Schedule 1 preview: the amount should appear in the entry space at the top of Schedule 1, not on Line 8z / 24z (those were the 2022–2023 method) and not inside Schedule C
5. **Enter Schedule C expenses**:
   - Line 2 (Returns and allowances): from worksheet
   - Line 9 (Car and truck): from worksheet — for mileage, TurboTax asks miles + standard or actual; standard rate is auto-applied
   - Line 10 (Commissions and fees): from worksheet — includes platform processing fees
   - Line 22 (Supplies): from worksheet
   - Part V Other expenses: from worksheet, one labeled row per category; total flows to Line 27b
   - Part III COGS (if marketplace seller): step through beginning inventory, purchases, ending inventory
6. **Validate Schedule C Line 31 (Net profit)** against the reconciliation worksheet. If TurboTax computes a different net, find the discrepancy before continuing.
7. **Hobby income** (if applicable): TurboTax routes this through "Less Common Income" → "Hobby Income"; goes to Schedule 1 Line 8j with no deduction.
8. **Schedule E** (if applicable): TurboTax has a separate Rental Properties section. Confirm the 1099-K rental portion goes to Schedule E Line 3.
9. **Form 8949** (if personal-item gain): TurboTax → Investments → "Sold or traded property other than securities" → enter each gain individually with cost basis.
10. **Run TurboTax's review pass**. Document-matching warnings about 1099-K should resolve to clean — flag any remaining red exclamation as a discrepancy.

### Browser flow — FreeTaxUSA

Same logical pattern with different navigation:

1. Sign in. Navigate to Income → 1099-K.
2. Enter PSE name, Box 1a, Box 4, state info from worksheet.
3. Choose "Business income" / "Personal payments" / "Mixed" radio button.
4. For mixed: enter business portion (drives Schedule C Line 1) and personal portion (must land in the entry space at the top of Schedule 1).
5. Navigate to Schedule C section, enter expenses by line.
6. Run the e-file review.

Check the product's current pricing and whether it supports the Schedule 1 1099-K entry space before starting.

### Browser flow — TaxSlayer Self-Employed

Similar to FreeTaxUSA. Confirm on the Schedule 1 preview that personal items sold at a loss land in the entry space at the top of Schedule 1.

### What the agent should NOT do

- Do not enter Box 1a directly on Schedule C Line 1 if any portion is personal — split it first
- Do not deduct platform fees from Box 1a before entry; enter gross, deduct fees on Line 10
- Do not skip the personal-portion adjustment for the friends/family Venmo case; the IRS will flag it
- Do not log SSN, EIN, DOB, or full account numbers in agent transcripts or telemetry

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| TurboTax shows "Mismatch with IRS records on 1099-K" | User's name/TIN on tax return doesn't match the 1099-K | Verify recipient identity boxes; if 1099-K is wrong, request corrected form before filing |
| Schedule C Line 31 differs from worksheet | One of the expense lines was entered wrong, or Box 1a was netted | Re-walk Schedule C entries against the worksheet |
| Schedule 1 entry-space amount differs from the worksheet's personal portion | User mistyped it, or software put it on Line 8z / 24z | Tell the user; do not silently fix |
| TurboTax classifies Etsy as "Hobby" | User answered "casual seller" on the activity-classification screen | Re-walk the trade-or-business test from `references/personal-vs-business.md`; profit motive + regularity = business |
| 1099-K shows withholding (Box 4 > 0) but no Line 25b credit appearing | Software routed Box 4 to wrong line | Manually verify Form 1040 Line 25b includes the Box 4 amount |

---

## Section 2 — IRS Free File / Free File Fillable Forms

For users with simple returns (W-2 + small Schedule C OR personal-only 1099-K). IRS Direct File was not offered in the 2026 filing season (no IRS Direct File page; the IRS free-filing options page lists Free File and Free File Fillable Forms). Do not send users there.

### Pre-flight

- **IRS Free File guided software**: AGI of $89,000 or less, age and state limits set by each partner (https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free). Start at IRS.gov/FreeFile, not the partner's own site.
- **Free File Fillable Forms (FFFF)**: any income level; no interview, basic math, federal return only, no state return. Requires an email address and a 10-digit U.S. cell phone number. FFFF for the 2025 return closes **Oct. 15, 2026** (https://www.irs.gov/e-file-providers/free-file-fillable-forms).
- The user's credentials (the agent MUST NOT create a new account without the user present for the SMS step)

### Browser flow — IRS Free File guided software

1. Start at IRS.gov/FreeFile and let the user pick a partner that accepts their AGI, age, and state.
2. Enter the 1099-K in the partner's 1099-K screen; enter the personal portion where the software asks for 1099-K amounts included in error or personal items sold at a loss.
3. Check the Schedule 1 preview: personal portion in the entry space at the top; business portion on Schedule C Line 1.
4. Backup withholding (Box 4) must land on Form 1040 Line 25b.
5. Run the software's review pass. Submit only with the user's explicit consent.

### Browser flow — Free File Fillable Forms

FFFF is unguided — the user must know which lines to fill. This is appropriate when the agent can drive the entries.

1. Sign in to FFFF (start from https://www.irs.gov/e-file-providers/free-file-fillable-forms)
2. Open Schedule C and fill from the worksheet, line by line
3. Open Schedule 1 and enter the personal portion in the entry space above Part I ("amount reported to you on Form(s) 1099-K that was included in error or for personal items sold at a loss")
4. Open Form 1040, verify Line 8 (Schedule 1 Line 10) and Line 25b (federal tax withheld on Forms 1099)
5. Submit electronically with the user's consent

### What the agent should NOT do

- Do not route anyone to IRS Direct File for the 2026 filing season
- Do not use FFFF for users who need significant guidance; it has zero hand-holding and validation is shallow
- Do not export FFFF entries outside the IRS system without explicit consent

---

## Section 3 — CP2000 response (notice handling)

If the user receives a CP2000 notice claiming under-reported 1099-K income, the response workflow is:

### Pre-flight

- The user's CP2000 notice (paper letter from IRS)
- The 1099-K reconciliation worksheet (from `SKILL.md`) for the year in question
- All other 1099s, bank records, and platform reports for the year

### Workflow

1. **Read the CP2000 carefully.** It identifies the discrepancy (e.g., "PSE reported Box 1a of $25,000; we found $18,000 in your Schedule C Line 1"). It is a **proposed** adjustment, not a final assessment.
2. **Reconcile** by determining if:
   - The IRS is correct and the user under-reported → agree, sign the notice, pay the additional tax
   - The IRS is wrong and the user reported correctly with a personal-portion adjustment → disagree, attach the reconciliation worksheet showing the Schedule 1 entry-space amount and where the rest of Box 1a was reported
   - The IRS is partially correct → partially agree, attach a corrected breakdown
3. **Respond by the deadline** (usually 30 days from notice date) by:
   - Mail to the address on the CP2000 (not the regular IRS address)
   - Include: signed CP2000 response page, reconciliation worksheet, copies of relevant 1099s, brief cover letter explaining the discrepancy
4. **Do not amend** the original return until the IRS asks. CP2000 is its own resolution channel.
5. **Keep copies** of everything mailed; certified mail with return receipt is recommended.

The reconciliation worksheet from `SKILL.md` is designed to be the audit-defense artifact for exactly this scenario — it shows that the user identified each portion of Box 1a, classified it correctly, and routed each portion to the right schedule. Submit it as-is with the CP2000 response.

---

## Section 4 — Corrected 1099-K from the PSE

If the user determines that the 1099-K itself is wrong (gross amount different from the platform's own dashboard, refunds not netted in correctly, multiple-account issue), request a corrected form before filing.

### Workflow

1. Identify the issue clearly (with screenshots from the platform dashboard)
2. Contact the PSE's tax support team — most platforms have a dedicated 1099-K correction request form in their help center
3. Provide: tax year, account ID, Box 1a as reported, Box 1a as expected, supporting documentation
4. Wait for the corrected form (Form 1099-K with the "CORRECTED" box checked). The IRS can't correct a 1099-K (FS-2025-08, What to do Q4).
5. **Do not report the wrong number as income.**

If the deadline approaches and the corrected form hasn't arrived, don't wait (FS-2025-08, What to do Q4):
- File with the correct amounts from the user's own records and enter the amount included in error in the entry space at the top of Schedule 1; keep the platform records that prove it
- Or file an extension (Form 4868) — extends time to file until October 15, not time to pay

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never enter or submit a tax return without explicit user consent** at the moment of submission. "I authorize you to e-file my <return> through <software> right now" must be captured.
2. **Never store SSN, EIN, DOB, or full bank/account numbers** in agent logs, vector stores, or transcripts. Pull at entry time, use, discard.
3. **Never bypass the tax-software MFA / KBA challenge.** If the platform asks the user to verify identity, pause and let the user respond directly.
4. **Always capture e-file confirmations** as PDFs stored under the user's account, not the agent's.
5. **If the 1099-K appears wrong**, surface to the user before filing — do not silently override or "round" to a different number.

---

## Archival and recordkeeping

After filing, advise the user to keep the following at least 3 years after filing, and 6 years if income they should have reported was more than 25% of the gross income shown (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records):

- The 1099-K(s) (paper or PDF copy)
- The reconciliation worksheet (from `SKILL.md`)
- The completed Schedule C, Schedule 1, Schedule E, Form 8949 (whichever apply)
- The Form 1040 + e-file acceptance confirmation
- All other 1099s for the year
- Platform year-end gross-payments reports (PayPal, Stripe, Etsy, etc. all expose these)
- Bank statements for the business account showing gross deposits matching the 1099-K

This bundle is the audit-defense artifact. If the IRS sends a CP2000 in 2027 about the 2026 return, the user has everything needed to respond in one folder.
