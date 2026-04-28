# Filing 1099-K-Derived Income (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) takes a completed 1099-K reconciliation worksheet and enters the derived figures into the user's tax software. The 1099-K itself is **not filed by the recipient** — the PSE files it with the IRS. This file covers the recipient-side workflow: turning Box 1a (and adjacent boxes) into entries on Schedule C, Schedule 1, Schedule E, Form 8949, and Form 1040.

The agent must produce a complete `SKILL.md`-format reconciliation *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Why "filing" is misleading for 1099-K

Three properties make 1099-K different from W-9, Schedule C, and most other forms in this skill library:

1. **No standalone return.** The 1099-K is an information return that drives entries on other forms. The recipient never "files a 1099-K" — they file Form 1040 with whichever schedules the underlying activity requires (Schedule C / Schedule 1 / Schedule E / Form 8949).
2. **Document-matching exposure.** The IRS receives the PSE's copy of the 1099-K and runs document matching against the recipient's return. If Schedule C Line 1 is below the trade/business portion of Box 1a, the IRS sends a CP2000 notice. The reconciliation worksheet from `SKILL.md` is the audit-defense artifact.
3. **Mixed personal/business is the default state.** Most 1099-K filers have personal payments mixed with business income on the same platform. The reconciliation is what separates them.

---

## Channel decision tree

The user picks the tax-software channel. If they don't know, default to **IRS Direct File** for simple cases (W-2 wages + a single small Schedule C) or **FreeTaxUSA** for everything else.

```
User has Schedule C activity + multiple 1099s + state return needed?
  → FreeTaxUSA or TurboTax Self-Employed (Section 1)
    Best fit: handles Schedule C, Schedule 1 reconciliation, Form 8949, Schedule E.

User has only personal payments on 1099-K (no business)?
  → IRS Direct File or IRS Free File (Section 2)
    Direct File supports Schedule 1 Line 8z + Line 24z for personal-item / friends-family.

User has Schedule E (passive rental real estate)?
  → FreeTaxUSA or TaxSlayer (Section 1)
    IRS Direct File doesn't support Schedule E in 2026.

User has both Schedule C + Schedule E + Form 8949?
  → TurboTax Self-Employed or FreeTaxUSA Deluxe (Section 1)
    Multi-schedule cases benefit from a paid product's review pass.

User received CP2000 notice for under-reported 1099-K?
  → Respond by mail or fax with the reconciliation worksheet (Section 3)
    Do NOT amend until the IRS asks; CP2000 is a proposed adjustment, not a bill.
```

---

## Section 1 — TurboTax Self-Employed / FreeTaxUSA / TaxSlayer

These are the canonical channels for Schedule C filers in 2026. Workflow is similar across products.

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
   - Click "Add income" → "Form 1099-K" (TurboTax has a dedicated 1099-K entry screen as of tax year 2026)
   - Payer name: from worksheet
   - Box 1a (Gross): from worksheet
   - Box 1b, Box 2: from worksheet (Box 2 informational; TurboTax doesn't use it for the tax calculation)
   - Box 4 (federal tax withheld): from worksheet — TurboTax routes this to Form 1040 Line 25c
   - State boxes: from worksheet
   - Confirm "All of this 1099-K is for my business" or "Some of this 1099-K is personal" — the latter opens the personal-portion adjustment screen
4. **Enter the personal-portion adjustment** (if applicable):
   - When prompted, enter the personal portion (friends/family + personal-item-loss)
   - TurboTax routes this to Schedule 1 Line 8z + Line 24z automatically
   - Add the explanation: "Personal payments included on 1099-K from <PSE>" (this becomes the Schedule 1 description text)
5. **Enter Schedule C expenses**:
   - Line 2 (Returns and allowances): from worksheet
   - Line 9 (Car and truck): from worksheet — for mileage, TurboTax asks miles + standard or actual; standard rate is auto-applied
   - Line 10 (Commissions and fees): from worksheet — includes platform processing fees
   - Line 22 (Supplies): from worksheet
   - Line 27a (Other expenses): from worksheet, with each labeled category as a sub-row
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
4. For mixed: enter business portion (drives Schedule C Line 1) and personal portion (drives Schedule 1 Line 8z + Line 24z).
5. Navigate to Schedule C section, enter expenses by line.
6. Run the e-file review.

FreeTaxUSA is materially cheaper than TurboTax (free federal, $14.99 state) and handles 1099-K mixed-use cases as a first-class flow.

### Browser flow — TaxSlayer Self-Employed

Similar to FreeTaxUSA. TaxSlayer exposes a "Personal Items Sold at a Loss" line directly in the Schedule 1 Line 8z entry, which is a nice match for IRS Notice 2023-74's guidance.

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
| Schedule 1 Line 8z and Line 24z don't net to $0 | User mistyped the offset | Tell the user; do not silently fix |
| TurboTax classifies Etsy as "Hobby" | User answered "casual seller" on the activity-classification screen | Re-walk the trade-or-business test from `references/personal-vs-business.md`; profit motive + regularity = business |
| 1099-K shows withholding (Box 4 > 0) but no Line 25c credit appearing | Software routed Box 4 to wrong line | Manually verify Form 1040 Line 25c includes the Box 4 amount |

---

## Section 2 — IRS Direct File / IRS Free File

For users with simple returns (W-2 + small Schedule C OR personal-only 1099-K), free IRS-provided options work for tax year 2026.

### Pre-flight

- Confirm the user's state participates in Direct File (expanded to ~25 states for tax year 2026)
- Confirm the user's tax situation is in scope: Direct File supports Schedule 1 (additional income), Schedule C (limited), Form 1040 standard. Direct File does NOT support Schedule E (rentals) or Form 8949 in 2026.
- The user's IRS.gov account credentials (the agent MUST NOT create a new account)

### Browser flow — IRS Direct File

1. Sign in to IRS.gov → Direct File.
2. Step through the guided flow until the Income section.
3. **Personal-only 1099-K** (no business activity):
   - On the "Other income" screen, choose "Personal payments included on a 1099-K"
   - Enter the personal amount (Box 1a, since 100% is personal)
   - Direct File routes this to Schedule 1 Line 8z with the explanation
   - On the next "Adjustments" screen, choose "Offset of personal payments on 1099-K" and enter the same amount → routes to Schedule 1 Line 24z
   - Net effect: $0 to AGI
4. **Mixed business + personal**: Direct File supports limited Schedule C in 2026. If Schedule C activity is straightforward (one platform, simple expenses), proceed; otherwise, switch to a paid product.
5. **Backup withholding** (Box 4): Direct File auto-routes to Form 1040 Line 25c.
6. Run Direct File's review pass. Submit electronically.

### Browser flow — IRS Free File / FFFF (Free File Fillable Forms)

Use FFFF if the user's AGI is above the Free File income limit (about $84,000 in 2026) but they want a free option. FFFF is unguided — the user must know which lines to fill. This is appropriate when the agent can drive the entries.

1. Sign in to FFFF (https://www.freefilefillableforms.com)
2. Open Schedule C and fill from the worksheet, line by line
3. Open Schedule 1 and add the personal portion to Line 8z + offset on Line 24z
4. Open Form 1040, verify Line 8 (Other income from Schedule 1), Line 25c (federal tax withheld)
5. Submit electronically

### What the agent should NOT do

- Do not submit Direct File if the user's state isn't supported — it'll fail and the user has to re-enter elsewhere
- Do not use FFFF for users who need significant guidance; it has zero hand-holding and validation is shallow
- Do not export Direct File / FFFF entries outside the IRS system without explicit consent

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
   - The IRS is wrong and the user reported correctly with a personal-portion adjustment → disagree, attach the reconciliation worksheet showing Schedule 1 Line 8z + Line 24z offset
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
4. Wait 4-6 weeks for the corrected form (Form 1099-K with the "CORRECTED" box checked)
5. **Do not file with the wrong 1099-K and "fix it later."** Filing with the wrong number sets up an automatic CP2000.

If the deadline approaches and the corrected form hasn't arrived, the user can:
- File an extension (Form 4868) — buys until October 15
- File with the corrected number based on the user's own records and attach a written explanation; this is unusual but defensible if records are clean

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

After filing, advise the user to keep for at least 6 years:

- The 1099-K(s) (paper or PDF copy)
- The reconciliation worksheet (from `SKILL.md`)
- The completed Schedule C, Schedule 1, Schedule E, Form 8949 (whichever apply)
- The Form 1040 + e-file acceptance confirmation
- All other 1099s for the year
- Platform year-end gross-payments reports (PayPal, Stripe, Etsy, etc. all expose these)
- Bank statements for the business account showing gross deposits matching the 1099-K

This bundle is the audit-defense artifact. If the IRS sends a CP2000 in 2027 about the 2026 return, the user has everything needed to respond in one folder.
