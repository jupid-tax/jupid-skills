# Form 2290 — Filing Playbook (Agent Browser Automation)

This document is loaded only when the user explicitly authorizes the agent to **file** Form 2290 on their behalf. If the user only wants a draft, do not load this file.

---

## Decision tree — pick a filing channel

```
Is the fleet 25 or more vehicles?
├── YES → E-file is MANDATORY (Reg. §41.6011(a)-1(b))
│         → Skip to "E-file via IRS-authorized provider"
└── NO  → E-file is OPTIONAL but strongly recommended
          (paper takes 4-6 weeks for stamped Schedule 1; e-file takes minutes)

Does the user have an IRS-authorized 2290 e-file provider account?
├── YES → Use that provider (skip to "E-file workflow")
└── NO  → Help them pick one from
          https://www.irs.gov/e-file-providers/e-file-form-2290
          Common providers: ExpressTruckTax, eForm2290, J.J. Keller, TaxBandits,
          Simple Trucking Tax. Provider choice doesn't affect the IRS submission;
          fees range from ~$10 (single vehicle) to ~$30 (fleet).

Is the EIN at least 2 weeks old in IRS systems?
├── YES → Proceed
└── NO  → BLOCK. Newly issued EINs are not yet propagated to the 2290 e-file
          ecosystem. Either wait, or paper-file this period (and e-file next).

Is the user OK with paper filing (4-6 week wait for Schedule 1)?
├── YES + low fleet count + no DMV deadline pressure → Paper file (see "Paper-file workflow")
└── NO → E-file
```

---

## Pre-flight checklist (before any submission)

The agent must confirm all of these before clicking submit:

- [ ] EIN is correct, active, and **at least 2 weeks old**
- [ ] Business name and address match IRS records
- [ ] Tax period is correctly stated (July 1, YYYY — June 30, YYYY+1)
- [ ] All VINs are 17 characters, no typos (compare against vehicle registration)
- [ ] Weight categories are correct for each vehicle (verified against vehicle registration / weight ticket)
- [ ] Logging vehicles are flagged with the 25% reduction
- [ ] Suspended vehicles are listed under Category W with Part II completed
- [ ] Mid-year first-use dates are correct (proration calculation matches)
- [ ] Line 5 credits are supported by an attached statement
- [ ] Total balance due (Line 6) is verified against the math
- [ ] Payment method is selected and prepared (EFW bank info, EFTPS PIN, card, or check)
- [ ] User has reviewed and explicitly authorized the submission

**Critical:** Any change after submission requires an Amended Return. Some changes (VIN correction) are easy; others (weight category) involve repaying tax. Get it right the first time.

---

## E-file via IRS-authorized provider

### Step 1 — Provider login

Most providers use email + password authentication. Some support SSO. The agent uses [`agent-browser`] tooling to log in but **does not store credentials beyond the filing session**.

### Step 2 — Business / EIN entry

Map this skill's header data to the provider's "Business" form:

| This skill's field | Common provider field labels |
|--------------------|------------------------------|
| Legal business name | "Business Name" / "Company Name" |
| EIN | "EIN" / "Employer ID" (no SSN allowed) |
| Address | "Business Address" (street, city, state, ZIP) |
| Reason for Filing checkboxes | "Filing Type" radio (Original / Amended / VIN Correction / Final) |

### Step 3 — Tax period and first-use month

Map:

| This skill's field | Provider field |
|--------------------|----------------|
| Tax period | "Tax Year" or "Period" dropdown (e.g., "2025-2026") |
| Line 1 — Date of first use | "First Used Month" dropdown (e.g., "July") |

### Step 4 — Vehicle entry (Schedule 1)

For each vehicle, enter:

| This skill's field | Provider field |
|--------------------|----------------|
| VIN | "VIN" (17 chars) |
| Weight category (A-V or W) | "Taxable Gross Weight" dropdown |
| Logging flag | "Logging Vehicle?" checkbox |
| Agricultural flag | "Agricultural Vehicle?" checkbox |
| Suspension flag (Category W) | "Suspended Vehicle?" checkbox |
| Date of first use (if mid-year) | "First Used Date" |

### Step 5 — Credits (Line 5)

If claiming credits for prior-period sold/destroyed/stolen/under-mileage vehicles:

- Enter VIN, date of event, and credit amount
- Upload supporting statement (PDF) if the provider requires it

### Step 6 — Review tax calculation

The provider's tax calculation should match this skill's Line 4 / Line 6 to the cent. If there's a discrepancy:

- Check weight category (most common cause)
- Check logging flag (25% reduction)
- Check first-use month (proration)
- Check suspension status

Do **not** submit if there's a discrepancy — re-run this skill's computation and reconcile.

### Step 7 — Payment method

| Method | Provider workflow |
|--------|-------------------|
| EFW (Electronic Funds Withdrawal) | Bank routing + account; agent enters but does not store |
| EFTPS | User enters PIN themselves; agent does not handle |
| Credit/Debit card | Convenience fee applies; user authorizes |
| Check / Money order | Print Form 2290-V; mail with check; provider gives address |

### Step 8 — Submit and capture stamped Schedule 1

After submission, the provider returns:

- IRS submission ID
- IRS acceptance status (usually within minutes)
- **Stamped Schedule 1 PDF** (this is the deliverable)

Save the stamped Schedule 1 to the user's records. Provide a copy to the user. Recommend they:

- Email it to themselves
- Save to cloud storage
- Print a copy for the truck cab
- Forward to their state DMV portal for plate renewal

### Step 9 — Confirm payment cleared

If EFW was used, monitor the user's bank account 1-3 business days post-filing for the debit. If it doesn't clear, the IRS may not consider the filing complete.

---

## Paper-file workflow

Paper filing is acceptable for fleets of 24 or fewer vehicles. It takes 4-6 weeks to receive the stamped Schedule 1.

### Steps

1. Print Form 2290 (latest revision from [irs.gov/pub/irs-pdf/f2290.pdf](https://www.irs.gov/pub/irs-pdf/f2290.pdf))
2. Print Schedule 1 **in duplicate** — both copies must accompany the filing
3. Print Form 2290-V if paying by check
4. Fill out by hand or with PDF tools (do not use a plain typewriter — use the IRS fillable PDF for cleanest results)
5. Sign and date
6. Mail to the IRS address listed in the Form 2290 instructions for your state (varies by state and whether you're paying by check or expecting a refund)

### Mailing addresses (verify in current instructions)

The IRS publishes specific addresses depending on:
- Whether payment is enclosed
- The filer's state

See **page 12 of the [Form 2290 instructions](https://www.irs.gov/pub/irs-pdf/i2290.pdf)** for the current address table. Do not hard-code addresses — they change.

### What to expect

- IRS receives and processes (4-6 weeks typically)
- IRS stamps your Schedule 1 copy and returns it by mail
- Keep the stamped Schedule 1 for DMV registration
- If you don't receive the stamped Schedule 1 within 6 weeks, call the IRS at the number in the instructions

---

## Submission state machine

```
DRAFT
  ↓ (user authorizes submission)
SUBMITTED (provider confirms receipt)
  ↓ (provider transmits to IRS, usually within minutes)
IRS_ACCEPTED (IRS validates and accepts the filing)
  ↓ (IRS processes, applies stamp)
SCHEDULE_1_STAMPED (deliverable available)
  ↓ (payment clears, if EFW)
PAYMENT_CLEARED (filing fully complete)

OR at any e-file step:
IRS_REJECTED (with reason code)
  ↓ (agent surfaces reason, user fixes, re-submits)
```

Common IRS rejection reasons:

- **EIN not in IRS systems** → wait for propagation, retry
- **Name/EIN mismatch** → user must reconcile with IRS records (Form 8822-B for address changes)
- **VIN already filed for this period** → another return already exists for that vehicle; check for duplicate
- **Math error** → tax calculation doesn't match the table (very rare with provider software)
- **Missing required field** → fill it and re-submit

---

## Security rules

The agent **must**:

1. **Never persist the EIN** beyond the filing session. Treat it like an SSN.
2. **Never store banking credentials, EFTPS PIN, or card data**. Pass through to the provider's secure form; do not log.
3. **Show a diff** between this skill's draft and the provider's review screen before allowing the user to submit. Highlight any field where the provider's value disagrees with the draft.
4. **Require explicit user consent** for the final submission step. A button click is not enough — the agent surfaces a summary ("You are about to submit Form 2290 for [business name], EIN [last 4], for tax period [period], with [N] vehicles, total balance due $[amount]. Type 'submit' to authorize.") and waits for the user's response.
5. **Never submit without verifying** the EIN is at least 2 weeks old (the most common e-file rejection cause for new businesses).
6. **Capture and securely deliver** the stamped Schedule 1 to the user. Do not retain a copy in agent state beyond the session.

---

## After filing — operational handoffs

Once the stamped Schedule 1 is in hand:

1. **State DMV registration** — Provide the stamped Schedule 1 to each state where vehicles are registered. Most state DMV portals accept a PDF upload.
2. **Income tax return** — Record the HVUT amount paid as a deductible expense:
   - Sole prop / SMLLC → Schedule C Line 23 (Taxes and licenses)
   - Partnership → Form 1065 deductions
   - S-corp → Form 1120-S Line 12 (Taxes and licenses)
   - C-corp → Form 1120 Line 17 (Taxes and licenses)
3. **Mileage log** for any suspended vehicles — confirm the user has a tracking method (paper log, ELD, fleet management software). If usage exceeds 5,000 miles (7,500 agricultural), file an Amended Return immediately.
4. **Next year's reminder** — set August 1 reminder for the next tax period.

---

## Edge cases

### Mid-year first use

A truck placed in service after July → file by the last day of the month following first use. Tax is prorated.

Example: First use January 14, 2026. File by February 28, 2026. Tax = standard annual rate × 6/12 (Jan, Feb, Mar, Apr, May, Jun = 6 months remaining in the period).

Use the partial-period table on page 2 of the instructions, not your own math — the IRS rounds in specific ways.

### Vehicle sold mid-period

The seller may claim a credit on next year's filing for the unused months. The buyer becomes responsible for filing 2290 for their first month of use forward (mid-year first use rules).

### Weight category increase mid-period

If a tractor that filed at Category K (65,000 lbs) starts pulling heavier trailers and now operates at Category U (75,000 lbs), file an Amended Return:

- Check Box B (Amended Return)
- Pay the difference between the new tax and the originally-paid tax for the remaining months
- Update Schedule 1

### VIN typo

File an Amended Return with Box C checked (VIN Correction). No additional tax is due — this is a clerical correction. You'll receive a corrected stamped Schedule 1.

### Final return

If you no longer have any qualifying vehicles (sold the entire fleet, exited trucking), check Box D (Final Return) on the next 2290 you would have filed. This signals to the IRS to stop expecting future filings.

---

## Provider-specific notes

The agent should look up provider-specific quirks before automating. Common patterns:

- **ExpressTruckTax** — supports bulk VIN upload via CSV; useful for fleets
- **eForm2290** — separate workflows for "single vehicle" vs. "fleet"; don't mix
- **J.J. Keller** — bundles 2290 with broader compliance services; UI may have extra steps
- **TaxBandits** — supports SSO with QuickBooks for fleet account import
- **Simple Trucking Tax** — minimal UI; faster for single-vehicle owner-operators

The agent should not recommend a specific provider unless the user asks. Surface the IRS-authorized list and let the user choose.
