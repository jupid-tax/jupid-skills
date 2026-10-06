# Form 2290 — Filing Playbook (Agent Browser Automation)

This document is loaded only when the user explicitly authorizes the agent to **file** Form 2290 on their behalf. If the user only wants a draft, do not load this file.

Addresses, phone numbers, and channel rules below are from the Instructions for Form 2290 (Rev. July 2026) and irs.gov pages checked 2026-10-06. Re-check them in each new July revision.

---

## Decision tree — pick a filing channel

```
Does this return report and pay tax on 25 or more vehicles?
(count categories A–V only; suspended category W vehicles don't count)
├── YES → E-file is MANDATORY (IRC §4481(e); Reg. §41.6011(a)-1(c)(1))
│         → Skip to "E-file via IRS-authorized provider"
└── NO  → E-file is OPTIONAL; the IRS encourages it
          (e-file returns a watermarked Schedule 1, usually within minutes of
          acceptance; paper returns get the stamped copy back by mail)

Does the user have an IRS-approved 2290 e-file provider account?
├── YES → Confirm it is on the current IRS list, then use it (skip to "E-file workflow")
└── NO  → Let the user pick one from the IRS list for the current tax year:
          https://www.irs.gov/e-file-providers/2290-mef-providers
          Form 2290 can't be e-filed on IRS.gov. The IRS does not endorse
          providers; services and fees differ by provider.

Was the EIN assigned at least four weeks ago?
├── YES → Proceed
└── NO  → BLOCK e-file. The IRS says to allow four weeks for a new EIN's name
          control to be established; an earlier e-file "might be rejected".
          Either wait, or paper-file this return if it reports tax on 24 or
          fewer vehicles.

Is the user OK with paper filing (stamped Schedule 1 returned by mail)?
├── YES + 24 or fewer taxed vehicles + no DMV deadline pressure → Paper file (see "Paper-file workflow")
└── NO → E-file
```

---

## Pre-flight checklist (before any submission)

The agent must confirm all of these before clicking submit:

- [ ] EIN is correct, active, and assigned **at least four weeks ago** (for e-file)
- [ ] Business name and address match IRS records
- [ ] Correct revision for the period (Rev. July 2026 = July 1, 2026 — June 30, 2027) and line 1 month as YYYYMM
- [ ] One return per first-use month (vehicles first used in different months go on separate returns)
- [ ] All VINs are 17 characters, no typos (compare against vehicle registration)
- [ ] Weight categories are correct for each vehicle (verified against vehicle registration / weight ticket)
- [ ] Logging vehicles use column (1)(b) / Table II amounts
- [ ] Suspended vehicles are listed under Category W with Part II line 7 completed
- [ ] Mid-year first-use dates are correct (proration calculation matches)
- [ ] Line 5 credits are supported by an attached statement
- [ ] Total balance due (Line 6) is verified against the math
- [ ] Payment method is selected and prepared (EFW bank info, EFTPS enrollment, card, or check/money order with Form 2290-V)
- [ ] User has reviewed and explicitly authorized the submission

**Critical:** Corrections after acceptance are limited. The IRS lets you e-file corrections to weight, mileage, and VIN; other errors on an e-filed and accepted return are corrected on a paper Form 2290 mailed to the instructions' address (FAQs for truckers who e-file). Overpayments from a mistake are claimed on Form 8849, Schedule 6 (instructions "Line 5"). Get it right the first time.

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
| "Check if applicable" boxes (Address Change, Amended Return, VIN Correction, Final Return) | "Filing Type" or similar (Original / Amended / VIN Correction / Final) |

### Step 3 — Tax period and first-use month

Map:

| This skill's field | Provider field |
|--------------------|----------------|
| Tax period | "Tax Year" or "Period" dropdown (e.g., "2026-2027") |
| Line 1 — Month of first use (YYYYMM, e.g., 202607) | "First Used Month" dropdown (e.g., "July 2026") |

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

If claiming credits for vehicles sold, destroyed, or stolen before June 1, or used within the mileage limit in the prior period:

- Enter VIN, category, date of event, and credit amount (line 5 can't exceed line 4)
- Attach the explanation and credit worksheet; for a sold vehicle include the purchaser's name and address

### Step 6 — Review tax calculation

The provider's tax calculation should match this skill's Line 4 / Line 6 to the cent. If there's a discrepancy:

- Check weight category (most common cause)
- Check logging status (column (1)(b) / Table II)
- Check first-use month (Table I / Table II column)
- Check suspension status

Do **not** submit if there's a discrepancy — re-run this skill's computation and reconcile.

### Step 7 — Payment method

| Method | Provider workflow |
|--------|-------------------|
| EFW (Electronic Funds Withdrawal) | Bank routing + account; available only when e-filing; agent enters but does not store |
| EFTPS | Pre-enrollment required (allow 5-7 business days); payment submitted by 8:00 p.m. ET the day before the due date; check the EFTPS box on line 6; user enters PIN themselves; agent does not handle |
| Credit/Debit card | Through IRS.gov/PayByCard processors; convenience fee charged by the processor; check the card box on line 6; user authorizes |
| Check / Money order | Payable to "United States Treasury"; Form 2290-V with payment to Internal Revenue Service, P.O. Box 932500, Louisville, KY 40293-2500 (for an e-filed return, send only the voucher and payment) |

### Step 8 — Submit and capture stamped Schedule 1

After submission, the provider returns:

- IRS submission ID
- IRS acceptance status (usually within minutes)
- **Watermarked Schedule 1 PDF** (this is the deliverable). Check that the watermark is legible when printed; the IRS suggests reprinting if it isn't

Save the stamped Schedule 1 to the user's records. Provide a copy to the user. Recommend they:

- Email it to themselves
- Save to cloud storage
- Print a copy for the truck cab
- Forward to their state DMV portal for plate renewal

### Step 9 — Confirm payment cleared

If EFW was used, monitor the user's bank account for the debit. If it doesn't clear, the return is still filed but the tax is unpaid: pay it another way right away to limit the failure-to-pay penalty and interest (IRC §6651(a)(2)).

---

## Paper-file workflow

Paper filing is allowed only for returns reporting tax on 24 or fewer vehicles (category W vehicles aren't counted). The IRS stamps the second copy of Schedule 1 and mails it back.

### Steps

1. Print Form 2290 (the revision for the period being filed; current revision at [irs.gov/pub/irs-pdf/f2290.pdf](https://www.irs.gov/pub/irs-pdf/f2290.pdf); earlier periods at irs.gov/Form2290)
2. Print **both copies** of Schedule 1 — both must accompany the filing (the return may be rejected without Schedule 1)
3. Print Form 2290-V if paying by check
4. Fill out by hand or with PDF tools (do not use a plain typewriter — use the IRS fillable PDF for cleanest results)
5. Sign and date
6. Mail to the address that matches the payment situation (below). The address does not depend on the filer's state.

### Mailing addresses (Instructions for Form 2290, Rev. July 2026, "Where To File"; re-verify each revision)

| Situation | Address |
|-----------|---------|
| Form 2290 with full payment, not drawn on an international financial institution | Internal Revenue Service, P.O. Box 932500, Louisville, KY 40293-2500 |
| Form 2290 without payment due, or paid through EFTPS or by credit/debit card | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0031 |
| Form 2290 with a check or money order drawn on an international financial institution | Internal Revenue Service, International Accounts, 1973 Rulon White Blvd., Ogden, UT 84201-0038 |

Private delivery services can't deliver to P.O. boxes; for a PDS, use the Ogden street address at IRS.gov/PDSstreetAddresses and a designated service from IRS.gov/PDS.

### What to expect

- IRS receives and processes the return (the instructions give no processing time)
- IRS stamps your Schedule 1 copy and returns it by mail
- Keep the stamped Schedule 1 for DMV registration; until it arrives, a photocopy of the filed Form 2290 with Schedule 1 plus both sides of the canceled check is accepted as proof of payment
- If the stamped Schedule 1 doesn't arrive, call the Form 2290 call site: 866-699-4096 (toll free, U.S.) or 859-320-3581 (Canada or Mexico), Monday–Friday, 8:00 a.m. to 6:00 p.m. Eastern

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

- **EIN not in IRS systems / name control mismatch** → new EIN: wait four weeks from assignment; otherwise the e-file name must match the EIN name (Form 8822-B updates the responsible party or mailing address, not the name)
- **Duplicate filing** (same EIN, period, VIN or category already filed) → list only new vehicles on the new return (FAQs for truckers who e-file)
- **Math error** → tax calculation doesn't match the table (very rare with provider software)
- **Missing required field** → fill it and re-submit

---

## Security rules

The agent **must**:

1. **Never persist the EIN** beyond the filing session. Treat it like an SSN.
2. **Never store banking credentials, EFTPS PIN, or card data**. Pass through to the provider's secure form; do not log.
3. **Show a diff** between this skill's draft and the provider's review screen before allowing the user to submit. Highlight any field where the provider's value disagrees with the draft.
4. **Require explicit user consent** for the final submission step. A button click is not enough — the agent surfaces a summary ("You are about to submit Form 2290 for [business name], EIN [last 4], for tax period [period], with [N] vehicles, total balance due $[amount]. Type 'submit' to authorize.") and waits for the user's response.
5. **Never submit an e-file without verifying** the EIN was assigned at least four weeks ago (earlier e-files "might be rejected" per the IRS trucker FAQ).
6. **Capture and securely deliver** the stamped Schedule 1 to the user. Do not retain a copy in agent state beyond the session.

---

## After filing — operational handoffs

Once the stamped Schedule 1 is in hand:

1. **State DMV registration** — Provide the stamped Schedule 1 to each state where vehicles are registered. Most state DMV portals accept a PDF upload.
2. **Income tax return** — Record the HVUT amount paid as a deductible expense:
   - Sole prop / SMLLC → Schedule C Line 23 (Taxes and licenses)
   - Partnership → Form 1065 Line 14 (Taxes and licenses)
   - S-corp → Form 1120-S Line 12 (Taxes and licenses)
   - C-corp → Form 1120 Line 17 (Taxes and licenses)
   - Farmer → Schedule F Line 29 (Taxes)
3. **Mileage log** for any suspended vehicles — confirm the user has a tracking method (paper log, ELD, fleet management software). If usage exceeds 5,000 miles (7,500 agricultural), file Form 2290 with the Amended Return box checked by the last day of the month following the month the limit was exceeded.
4. **Next year's reminder** — set August 1 reminder for the next tax period.

---

## Edge cases

### Mid-year first use

A truck first used after July → file by the last day of the month following first use (next business day after a weekend or legal holiday). Tax is prorated. Use a separate return for each first-use month.

Example: First use January 14, 2027. Due date: February 28, 2027 is a Sunday, so **March 1, 2027** (instructions chart). Line 1 = 202701. Tax = Table I (or Table II for logging) amount in the JAN (6) column (Jan–Jun = 6 months).

Use the Partial-Period Tax Tables at the end of the instructions, not your own math — Table II amounts can differ from the formula by $0.01.

### Vehicle sold mid-period

If the vehicle was sold before June 1 and not used again by the seller, the seller may claim a credit on the next Form 2290 filed (or a refund on Form 8849, Schedule 6) for the months after the sale, including the purchaser's name and address. A buyer who first uses the vehicle in the month of sale, from a seller who paid this period's tax, owes tax from the first day of the next month, enters that month on line 1, and keeps the normal due date (instructions "Used vehicles").

### Weight category increase mid-period

If a tractor that filed at Category K (65,000 lbs) starts customarily carrying heavier loads and its taxable gross weight is now 75,000 lbs (Category U), file Form 2290:

- Check the Amended Return box and write the month of the increase next to it
- Line 3 = Partial-Period Tax Table amount for the new category minus the amount for the old category, both in the month-of-increase column (Line 3 worksheet, attached)
- List the VIN on Schedule 1 under the new category
- Due by the last day of the month following the month of the increase

### VIN typo

File Form 2290 for the period being corrected with the **VIN Correction** box checked (not the Amended Return box), list the corrected VIN on Schedule 1, and attach an explanation. It can be e-filed. The corrected Schedule 1 comes back stamped.

### Final return

If you no longer have taxable vehicles to report (sold the entire fleet, exited trucking), file a final return: check the Final Return box, sign, and file.

---

## Provider-specific notes

Provider portals differ (bulk VIN upload, fleet vs. single-vehicle flows, extra compliance upsells). Read the chosen provider's own help pages before automating; do not assume a workflow from another provider.

The IRS lists approved providers by tax year at [2290 MeF providers](https://www.irs.gov/e-file-providers/2290-mef-providers) and says the list "does not mean that a software package includes every possible schedule or attachment". The agent should not recommend a specific provider. Surface the current IRS list and let the user choose.
