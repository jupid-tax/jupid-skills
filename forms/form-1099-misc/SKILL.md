---
name: form-1099-misc
description: >
  Use this skill when a US business needs to issue Form 1099-MISC for
  miscellaneous payments (rent, royalties, prizes, fishing-boat proceeds,
  medical/health-care payments, gross proceeds to attorneys, crop insurance,
  etc.) OR when a recipient receives a Form 1099-MISC and needs to report
  it on the correct schedule. Triggers on phrases like "Form 1099-MISC",
  "report rent payment", "report royalties", "1099 for landlord",
  "attorney 1099-MISC Box 10", "prize/award reporting", "medical
  payments 1099", "fishing boat proceeds 1099", "received 1099-MISC".
  Do NOT use for: nonemployee compensation for services (use
  `form-1099-nec` — different form, different deadline); third-party
  payment network platform payments (use `form-1099-k` — Stripe, PayPal,
  Venmo, etc.); interest (1099-INT); dividends (1099-DIV); state /
  local tax refunds (1099-G); cancellation of debt (1099-C); broker /
  exchange transactions (1099-B); digital-asset broker proceeds (1099-DA).
form: Form 1099-MISC (Miscellaneous Information)
audience: [solo, employer, llc1]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1099msc.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099mec.pdf
---

# Form 1099-MISC — Miscellaneous Information

This skill produces an audit-grade plan for Form 1099-MISC, on either side:

- **Payor side**: determine whether 1099-MISC applies for each payment type, allocate amounts to the correct box, file with the IRS, and deliver Copy B to recipients.
- **Recipient side**: reconcile a received 1099-MISC and route each box to the correct line on the recipient's federal return (Schedule E for rents, Schedule C for trade-or-business income, Schedule 1 for prizes / awards / one-off items, Form 1040 Line 25b for withholding).

The 1099-MISC was renamed "Miscellaneous Information" (from "Miscellaneous Income") in 2020 when nonemployee compensation moved to Form 1099-NEC. Today, 1099-MISC reports rent, royalties, prizes/awards, medical and health-care services, attorney legal fees, fishing-boat proceeds, crop insurance, substitute payments, and a few other categories under IRC §6041 and §6041A.

The judgment lives in **(a)** picking the right box for each payment (rents / royalties / Box 3 other income / medical / attorney are different boxes with different rules), **(b)** applying the corporate-exemption exceptions correctly (medical and attorney payments are reportable even to corporations — a special rule), and **(c)** routing recipient income to the right schedule.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1099-MISC, "1099-MISC", or "1099 MISC"
- A business owner asks about reporting **rent** paid to a landlord (commercial real estate, equipment rental — different from residential rent paid by a tenant)
- A business owner asks about reporting **royalties** (oil/gas, mineral, copyright, patent royalty payments)
- A business owner pays **legal fees from a settlement** to an attorney (split between Box 10 attorney portion and Box 14 plaintiff portion)
- A business owner pays **medical or health-care providers** (Box 6 — even if provider is a corporation)
- A business owner gives a **prize or award** to a non-employee
- A recipient asks "I got a 1099-MISC, where do I report each box?"
- The user mentions **fishing boat proceeds** (Box 5) or **crop insurance** (Box 9)

Do **not** engage this skill when:

- The payment is **nonemployee compensation** for services (use `form-1099-nec` — different form, $2,000 threshold for 2026, January 31 IRS deadline)
- The payment was made through a **third-party payment network** (use `form-1099-k`)
- The payment is **interest** (use 1099-INT)
- The payment is **dividends** (use 1099-DIV)
- The payment is **state or local tax refunds, unemployment, or government grants** (use 1099-G)
- The payment is **cancellation of debt** (use `form-1099-c`)
- The payment is **broker / barter exchange transactions** (use 1099-B)
- The payment is **digital-asset broker proceeds** (use forthcoming `form-1099-da`)
- The payment is **wages to W-2 employees** (use W-2)

For the related nonemployee compensation form, see [`form-1099-nec/`](../form-1099-nec/SKILL.md). For platform-mediated payments, see [`form-1099-k/`](../form-1099-k/SKILL.md). The combined IRS instructions cover both 1099-NEC and 1099-MISC: https://www.irs.gov/pub/irs-pdf/i1099mec.pdf.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

### Payor side

1. **Payor's legal name, EIN, and address** — for the form's payer block.
2. **Tax year** the 1099-MISCs cover.
3. **List of every payment** that may be 1099-MISC reportable, categorized by box:
   - **Box 1 (Rents)**: rent paid to landlord for office, equipment, or other business property
   - **Box 2 (Royalties)**: royalties paid for use of intellectual property, mineral rights, etc.
   - **Box 3 (Other income)**: prizes, awards, taxable damages, deceased employee wages paid to estate
   - **Box 4 (Federal income tax withheld)**: backup withholding amounts
   - **Box 5 (Fishing boat proceeds)**: share paid to crew members
   - **Box 6 (Medical / health-care payments)**: payments to physicians, hospitals, health-care providers — **even if corporation**
   - **Box 7 (Direct sales of consumer products ≥ $5,000)**: checkbox for buy-sell-resale arrangements
   - **Box 8 (Substitute payments in lieu of dividends or interest)**: from securities lending
   - **Box 9 (Crop insurance proceeds)**: paid to farmers
   - **Box 10 (Gross proceeds paid to an attorney)**: settlement / legal fees — **even if attorney is corporation**
   - **Box 11 (Section 1042-S transactions filer fish processor)**: cash purchases of fish
   - **Box 12 (Section 409A deferrals)**: deferred compensation
   - **Box 13 (FATCA filing requirement)**: checkbox
   - **Box 14 (Excess golden parachute payments)**: rare
   - **Box 15 (Nonqualified deferred compensation)**: §409A income inclusions
4. **Payee data** — for each: legal name, TIN (SSN/EIN), address (from W-9)
5. **Filing channel** — IRS IRIS, FIRE, or third-party service. Mandatory e-filing if 10+ information returns total.
6. **State filing requirements** — most states piggyback on CF/SF; verify.

### Recipient side

1. **Filer's legal name and SSN/ITIN** — for routing.
2. **Form copy** with all populated boxes.
3. **Underlying activity classification**:
   - Rent received → Schedule E (real property) or Schedule C (real estate dealer / equipment rental as a trade or business)
   - Royalties → Schedule E (typical) or Schedule C (in the business of creating intellectual property)
   - Prize/award → Schedule 1 Line 8 (other income)
   - Medical payments (for the recipient: a healthcare provider) → Schedule C (their business income)
   - Attorney fees received → Schedule C (their business income)
4. **Recipient's records** — does the box amount match expectations?
5. **Box 4 federal withholding** — applies if backup withholding occurred.

---

## Workflow

### Payor side workflow

#### Step 1 — Categorize each potentially-reportable payment

Walk through every business payment and ask: which 1099-MISC box does this fit? Use [`references/box-by-box.md`](./references/box-by-box.md) as the lookup. Most payments don't fit *any* box and aren't 1099-MISC reportable.

#### Step 2 — Apply per-box thresholds

Each box has its own threshold (verify current at https://www.irs.gov/pub/irs-pdf/i1099mec.pdf):

| Box | 2026 Threshold | Notes |
|-----|---------------|-------|
| Box 1 (Rents) | $600 | Verify: OBBBA may or may not have changed this; check guidance |
| Box 2 (Royalties) | $10 | Lowest threshold of any 1099 box |
| Box 3 (Other income) | $600 | Includes prizes, awards |
| Box 5 (Fishing boat proceeds) | $600 | |
| Box 6 (Medical / health-care payments) | $600 | Reportable to corporations too |
| Box 8 (Substitute payments) | $10 | |
| Box 9 (Crop insurance proceeds) | $600 | |
| Box 10 (Gross proceeds to attorney) | $600 | Reportable to corporations too |

The **$2,000 threshold raise from OBBBA Section 112201** specifically applies to nonemployee compensation under §6041A (Form 1099-NEC). Whether OBBBA also raised the §6041 threshold for some 1099-MISC categories (notably Box 1 rents and Box 3 other income) requires verification against current IRS guidance — check before applying. As of last verification (2026-04-28), assume **$600 still applies** to 1099-MISC unless the IRS has issued contrary guidance.

If backup withholding was applied to any payment, issue 1099-MISC regardless of whether the threshold is met.

#### Step 3 — Verify W-9 data

Same as 1099-NEC: every payee crossing a threshold needs a current W-9. TIN-match before filing.

For **Box 6 (medical) and Box 10 (attorney)**, the corporate exemption does NOT apply — issue 1099-MISC even to corporations. This is the most-missed special rule. See [`references/corporate-exception.md`](./references/corporate-exception.md).

#### Step 4 — Allocate amounts to boxes

Many 1099-MISC scenarios involve splitting one transaction across multiple boxes:

- **Settlement payment to plaintiff via attorney's trust account**:
  - Plaintiff's portion → Box 3 (other income, taxable settlement)
  - Attorney's gross proceeds (entire amount that passed through attorney) → Box 10
  - Attorney's fee portion (the cut the attorney kept) → 1099-NEC Box 1 (NOT 1099-MISC)
- **Rent + commission combined**: rent → Box 1; commission → 1099-NEC

See [`references/settlement-allocation.md`](./references/settlement-allocation.md) for the allocation playbook.

#### Step 5 — Populate header and boxes

Per [`references/box-by-box.md`](./references/box-by-box.md). Use truncated TIN on Copy B (recipient), full TIN on Copy A (IRS).

#### Step 6 — Distribute copies

- **Copy A** (IRS): paper deadline February 28; electronic deadline March 31 (note: this is **later** than 1099-NEC, which is January 31)
- **Copy B** (recipient): deadline February 1 (slightly later than 1099-NEC's January 31, but only by one day) — verify each year's calendar

If filing 10+ information returns total across all types, electronic filing is mandatory.

#### Step 7 — Hand off to filing.md

For browser-driven filing, see [`filing.md`](./filing.md).

### Recipient side workflow

#### Step R1 — Identify each populated box

Don't assume "1099-MISC = Schedule C." Each box routes differently. Use [`references/recipient-routing.md`](./references/recipient-routing.md) as the lookup.

#### Step R2 — Route each box

| Box | Default destination | Alternative |
|-----|---------------------|-------------|
| Box 1 (Rents) | Schedule E (rental real property) | Schedule C (if real estate dealer or equipment rental as trade or business) |
| Box 2 (Royalties) | Schedule E Part I | Schedule C (if creating IP as a trade or business) |
| Box 3 (Other income) | Schedule 1 Line 8z (or 8 generic) | Schedule C if the prize / award is part of a trade or business |
| Box 4 (Fed withholding) | Form 1040 Line 25b | (always Form 1040, regardless of which box source) |
| Box 5 (Fishing boat) | Schedule C | (commercial fishing as a trade or business) |
| Box 6 (Medical) | Schedule C | (healthcare provider's business income) |
| Box 8 (Substitute) | Schedule B Part I (interest) or Schedule 1 Line 8 | Depends on underlying nature |
| Box 9 (Crop insurance) | Schedule F (farming) | |
| Box 10 (Attorney gross proceeds) | Schedule C (the attorney's law practice) | Or, for the plaintiff's portion already in Box 3 — not Box 10 |
| Box 12 (§409A deferrals) | Form 1040 Line 8t (with 20% additional tax under §409A(a)(1)(B)) | |
| Box 14 (Excess golden parachute) | Form 1040 Line 1h or other applicable line | Plus 20% excise tax under §4999 |

#### Step R3 — Reconcile against records

Recipient's records should match the box amount within rounding. Discrepancies → investigate before filing.

#### Step R4 — Validate and produce deliverable

See **Validation** below.

---

## Line-by-line guidance

For the full reference, load [`references/box-by-box.md`](./references/box-by-box.md). High-level summary below.

### Header

Same as 1099-NEC: payer block, recipient block, account number, TIN truncation rules. See [`references/box-by-box.md`](./references/box-by-box.md) for details.

### Box 1 — Rents

Rent paid to landlord for business use of real property (office, warehouse, retail, storage) or for machinery / equipment lease.

Common scenarios:
- Business office rent paid directly to a property owner (not via a property management company that issues its own 1099)
- Equipment lease (forklift, tractor, copier) paid to an equipment rental company
- Vehicle rental for business use (paid to non-corporate rental company)

Excludes:
- Residential rent paid by a tenant (the tenant doesn't issue 1099-MISC for personal residential rent)
- Rent paid through a property manager who collects on landlord's behalf (the property manager files 1099-MISC to the landlord; the tenant doesn't)
- Rent paid to a corporation (corporate exemption applies for Box 1)

### Box 2 — Royalties

Royalties paid for the use of intellectual property (copyrights, patents, trademarks, mineral rights, oil/gas leases). Threshold: **$10**.

### Box 3 — Other income

Catch-all for taxable miscellaneous payments not fitting elsewhere:
- Prizes and awards (cash or fair market value of merchandise)
- Damages awarded in a lawsuit (unless personal physical injury, which is excluded under IRC §104)
- Deceased employee's wages paid in a year after death
- Punitive damages
- Settlement payment to plaintiff (the plaintiff's share of a settlement, where the payment passed through an attorney's trust account)

Threshold: $600.

### Box 4 — Federal income tax withheld

Backup withholding under IRC §3406 (24%). Same mechanics as 1099-NEC Box 4. See [`references/backup-withholding.md`](./references/backup-withholding.md).

### Box 5 — Fishing boat proceeds

Share of the catch paid to crew members on a fishing vessel. Specific to the commercial fishing industry. Threshold: $600.

### Box 6 — Medical and health-care payments

Payments made to physicians, hospitals, and other healthcare providers for services. **Reportable even if the provider is a corporation** — this is one of two corporate-exemption exceptions (the other is Box 10 attorney fees).

Includes: doctors' fees, lab fees, hospital payments for services rendered, payments to nurses, dentists, psychologists.

Excludes: insurance premiums (those go through the insurance company), pharmacy payments for prescriptions (those are sales of goods).

Threshold: $600.

### Box 7 — Direct sales of consumer products ≥ $5,000

Same as 1099-NEC Box 2 — checkbox for direct-sales / MLM relationships. The payer can use either form (1099-NEC Box 2 or 1099-MISC Box 7) but not both.

### Box 8 — Substitute payments in lieu of dividends or interest

For securities lending arrangements where the borrower pays the lender a substitute amount for the dividend / interest the lender would have received. Threshold: $10.

### Box 9 — Crop insurance proceeds

Paid to farmers under federal crop insurance programs. Threshold: $600.

### Box 10 — Gross proceeds paid to an attorney

The TOTAL amount of a settlement that passed through an attorney's trust account, regardless of how much the attorney kept as fee. **Reportable even if the attorney is a corporation** — second corporate-exemption exception.

This is distinct from Box 1 of 1099-NEC, which reports the *attorney's fee* (the cut the attorney kept). Box 10 of 1099-MISC reports the *gross proceeds* (the entire settlement amount).

For a $50,000 settlement where the attorney keeps $20,000 and passes $30,000 to the plaintiff:
- 1099-MISC to attorney, Box 10: $50,000 (gross proceeds)
- 1099-NEC to attorney, Box 1: $20,000 (attorney's fee for services)
- 1099-MISC to plaintiff, Box 3: $30,000 (taxable settlement to plaintiff, if not §104 excluded)

This split is the most-confused area of 1099-MISC reporting. See [`references/settlement-allocation.md`](./references/settlement-allocation.md).

### Box 11 — Section 1042-S fish processor cash purchases

Specific to fish processors purchasing from independent fishers. Rare.

### Box 12 — Section 409A deferrals

Reports deferrals into a nonqualified deferred compensation plan that are taxable currently due to §409A non-compliance.

### Box 13 — FATCA filing requirement

Checkbox if filing under Foreign Account Tax Compliance Act.

### Box 14 — Excess golden parachute payments

Excess parachute payments under §280G / §4999 (20% excise tax to recipient on the excess).

### Box 15 — Nonqualified deferred compensation

Income inclusions under §409A(a)(1)(A) (failure to comply with §409A rules — currently includes deferrals plus 20% additional tax + interest).

### Boxes 16-18 — State info

State tax withheld, state / payer's state ID, state income.

---

## Validation

### Math checks (payor side)

- [ ] Sum of all Box 1 (rents) issued matches GL total of rent paid to non-corporate landlords
- [ ] Sum of Box 6 (medical) matches total paid to medical providers regardless of entity type
- [ ] Sum of Box 10 (attorney gross proceeds) matches total of settlement disbursements through attorney trust accounts
- [ ] Sum of all Box 4 (backup withholding) matches Form 945 reconciliation
- [ ] Number of forms filed reported on Form 1096 matches actual count

### Sanity checks (payor side)

- [ ] Any Box 6 or Box 10 payment to a corporation → confirm it's NOT excluded (corporate exemption doesn't apply for these boxes)
- [ ] Any nonemployee compensation accidentally placed on 1099-MISC Box 3 instead of 1099-NEC Box 1 → fix
- [ ] Any payment via Stripe / PayPal / Venmo Business / Square → exclude (1099-K applies)
- [ ] Total information returns ≥ 10 → e-file mandatory

### Math checks (recipient side)

- [ ] Each box amount routed to the correct schedule
- [ ] Sum of Box 4 across all 1099s → Form 1040 Line 25b
- [ ] Recipient's records match each populated box

### Sanity checks (recipient side)

- [ ] Box 1 (rents) recipient has Schedule E (or Schedule C if dealer) — not just Schedule 1
- [ ] Box 3 (other income) recipient correctly identifying whether the income is one-off (Schedule 1) or trade-or-business (Schedule C)
- [ ] Box 10 (attorney gross proceeds) reconciled — the recipient is the attorney; the gross is income to the attorney's law practice (Schedule C), not all of which is profit (the portion paid to the plaintiff is an expense)

---

## Output format

### Payor-side deliverable: 1099-MISC issuance plan

```markdown
# Form 1099-MISC — Issuance Plan for tax year YYYY
Payer: <Legal Name> (EIN: XX-XXXXXXX)

## 1099-MISC by box

### Box 1 — Rents
| Payee | TIN (last 4) | Address | Box 1 Amount |
|-------|--------------|---------|--------------|
| ...   | XXX-XX-1234  | ...     | $X,XXX        |

### Box 2 — Royalties
| Payee | TIN | Address | Box 2 Amount |
| ...   | ... | ...     | $X,XXX       |

### Box 3 — Other income
| Payee | TIN | Address | Box 3 Amount | Description |
| ...   | ... | ...     | $X,XXX       | Prize / award / settlement |

### Box 6 — Medical / health-care payments (CORPORATIONS INCLUDED)
| Payee | TIN | Entity Type | Box 6 Amount |
| ...   | ... | C-Corp / S-Corp / etc. | $X,XXX |

### Box 10 — Gross proceeds to attorney (CORPORATIONS INCLUDED)
| Payee | TIN | Entity Type | Box 10 Amount |
| ...   | ... | C-Corp / S-Corp | $X,XXX |

### Box 4 — Federal tax withheld
Total backup withholding remitted via Form 945: $X,XXX

## Excluded (with reason)
| Payee | Reason for exclusion |
|-------|----------------------|
| Acme Properties Inc. | Corporation, Box 1 rent — exempt |
| ... | Paid via Stripe — covered by 1099-K |

## Filing checklist

- [ ] Recipient copies (Copy B) postmarked or e-delivered by **February 1**
- [ ] IRS Copy A: filed **paper by February 28** OR **electronic by March 31** (1099-MISC has later IRS deadline than 1099-NEC)
- [ ] State copies filed (if state not in CF/SF)
- [ ] Form 945 filed if any backup withholding remitted (deadline January 31)
- [ ] Records retained ≥ 4 years

## Sources cited
- IRS Form 1099-MISC, Rev. <year>
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. <year>
- IRC §6041, §6041A, §3406
- Reg. §1.6041-3(c) (corporate exemption)
- Reg. §1.6041-1(d)(2) (attorney special rule)
```

### Recipient-side deliverable: reconciliation summary

```markdown
# Form 1099-MISC — Recipient Reconciliation for tax year YYYY
Recipient: <Legal Name> (TIN: XXX-XX-XXXX)
Payer: <Legal Name> (EIN: XX-XXXXXXX)

## Boxes populated and routing
| Box | Field | Amount | Routes to |
|-----|-------|--------|-----------|
| 1   | Rents | $X,XXX | Schedule E Line 3 (or Schedule C if dealer) |
| 2   | Royalties | $X,XXX | Schedule E Line 4 (or Schedule C) |
| 3   | Other income | $X,XXX | Schedule 1 Line 8z |
| 4   | Federal tax withheld | $X,XXX | Form 1040 Line 25b |
| 6   | Medical / health-care | $X,XXX | Schedule C Line 1 (provider's business) |
| 10  | Gross proceeds to attorney | $X,XXX | Schedule C Line 1 (attorney's law practice; offset by amount disbursed to client as expense) |

## Reconciliation
Per recipient records: <details>
Per 1099-MISC: <details>
Discrepancies: <if any>

## Validation summary
- Math: passed | <list failures>
- Sanity: <warnings>
- Next steps: <Schedule E / Schedule C / Schedule 1>

## Sources cited
- IRS Form 1099-MISC, Rev. <year>
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. <year>
- IRC §6041, §1402, §61
```

---

## References

- [`references/box-by-box.md`](./references/box-by-box.md) — Complete box-by-box reference for Form 1099-MISC
- [`references/corporate-exception.md`](./references/corporate-exception.md) — Special rules for Box 6 (medical) and Box 10 (attorney) — corporate exemption does NOT apply
- [`references/settlement-allocation.md`](./references/settlement-allocation.md) — How to split a settlement across Boxes 3 + 10 + 1099-NEC for plaintiff and attorney
- [`references/recipient-routing.md`](./references/recipient-routing.md) — Routing each box to the right schedule on the recipient's return
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer errors with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing 1099-MISC via IRIS, FIRE, or paper

## Examples

- [`examples/payor-rent-to-landlord.md`](./examples/payor-rent-to-landlord.md) — Small business issuing 1099-MISC Box 1 for $14,400 commercial office rent paid to an individual landlord
- [`examples/payor-attorney-settlement.md`](./examples/payor-attorney-settlement.md) — Law firm paying $3,500 settlement through an attorney's trust account, splitting Box 10 (attorney gross) + Box 3 (plaintiff portion)
- [`examples/payor-medical-payment.md`](./examples/payor-medical-payment.md) — Business paying medical reimbursement of $1,200 directly to a provider (Box 6), illustrating that the corporate exemption does NOT apply

## Sources

- [Form 1099-MISC (latest)](https://www.irs.gov/pub/irs-pdf/f1099msc.pdf) — the form itself
- [Instructions for Forms 1099-MISC and 1099-NEC (latest)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) — combined IRS instructions
- [About Form 1099-MISC](https://www.irs.gov/forms-pubs/about-form-1099-misc) — IRS landing page
- [Publication 1220](https://www.irs.gov/pub/irs-pdf/p1220.pdf) — Specifications for Electronic Filing of Information Returns
- [Information Returns Intake System (IRIS)](https://www.irs.gov/filing/e-file-information-returns) — IRS free e-file portal
- [Form 945](https://www.irs.gov/forms-pubs/about-form-945) — Annual Return of Withheld Federal Income Tax
- IRC §6041 (general info-return obligation), §6041A (services), §6045(f) (gross proceeds paid to attorneys), §3406 (backup withholding), §6011(e) (mandatory e-file), §61 (gross income), §104 (exclusions for personal physical injury), §409A (deferred compensation)
- Reg. §1.6041-3(c) (corporate exemption from 1099 reporting)
- Reg. §1.6041-1(d)(2) — special rule for attorney legal services (corporate exemption does not apply)
- Reg. §1.6041-1(a)(1)(i) — definition of "in the course of trade or business"
- OBBBA Section 112201 (raised 1099-NEC threshold to $2,000; verify whether also affected 1099-MISC thresholds)
- Notice 2024-85 (transition guidance for §6050W and related; verify applicability to 1099-MISC)
- Reg. §301.6109-4 (TIN truncation on payee statements)
- Taxpayer First Act of 2019, codified at IRC §6011(e)(2) — 10-return e-file threshold

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Complex situations — particularly settlement allocations splitting attorney / plaintiff portions, multi-box scenarios, §409A failures, and prize / award characterization — warrant a licensed tax professional's review.
