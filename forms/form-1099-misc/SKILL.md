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
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1099msc.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099mec.pdf
---

# Form 1099-MISC — Miscellaneous Information

This skill produces an audit-grade plan for Form 1099-MISC, on either side:

- **Payor side**: determine whether 1099-MISC applies for each payment type, allocate amounts to the correct box, file with the IRS, and deliver Copy B to recipients.
- **Recipient side**: reconcile a received 1099-MISC and route each box to the correct line on the recipient's federal return (Schedule E for rents, Schedule C for trade-or-business income, Schedule 1 for prizes / awards / one-off items, Form 1040 Line 25b for withholding).

The 1099-MISC was renamed "Miscellaneous Information" (from "Miscellaneous Income") in 2020 when nonemployee compensation moved to Form 1099-NEC. Today, 1099-MISC reports rent, royalties, prizes/awards and other income, medical and health-care payments, gross proceeds paid to attorneys, fishing-boat proceeds, crop insurance, substitute payments, fish purchased for resale, and §409A amounts, under IRC §6041, §6045(d) and (f), §6050A, §6050N, and §6050R. Fees for legal services provided to the payer are 1099-NEC, not 1099-MISC.

Box map and thresholds verified against **Form 1099-MISC (Rev. December 2026)** and the Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026, June 25 2026), used for 2026 payments filed in early 2027, and against the **Rev. April 2025** form and instructions used for 2025 payments. The $600 thresholds became **$2,000** for payments made after December 31, 2025 (P.L. 119-21 §70433, amending IRC §6041(a); indexed for inflation from 2027 under §6041(h)). Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1099-misc before use.

**Companion guide for end users:** [1099-MISC vs 1099-NEC (2026): Which Form You File and When + AI Agent Skill](https://jupid.com/blog/1099-misc-vs-1099-nec-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

The judgment lives in **(a)** picking the right box for each payment (rents / royalties / Box 3 other income / medical / attorney are different boxes with different rules), **(b)** applying the corporate-exemption exceptions correctly (medical, attorney gross proceeds, substitute payments, and fish purchases are reportable even to corporations), and **(c)** routing recipient income to the right schedule.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1099-MISC, "1099-MISC", or "1099 MISC"
- A business owner asks about reporting **rent** paid to a landlord (commercial real estate, equipment rental — different from residential rent paid by a tenant)
- A business owner asks about reporting **royalties** (oil/gas, mineral, copyright, patent royalty payments)
- A business pays a **settlement through the claimant's attorney** (Box 10 gross proceeds to the attorney; Box 3 to the claimant for the full taxable amount)
- A business owner pays **medical or health-care providers** (Box 6 — even if provider is a corporation)
- A business owner gives a **prize or award** to a non-employee
- A recipient asks "I got a 1099-MISC, where do I report each box?"
- The user mentions **fishing boat proceeds** (Box 5) or **crop insurance** (Box 9)

Do **not** engage this skill when:

- The payment is **nonemployee compensation** for services, including attorneys' fees for legal services provided to the payer (use `form-1099-nec` — different form, $2,000 threshold for 2026, January 31 IRS deadline)
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
   - **Box 3 (Other income)**: prizes, awards, taxable damages, deceased employee's wages paid to the estate or beneficiary
   - **Box 4 (Federal income tax withheld)**: backup withholding amounts
   - **Box 5 (Fishing boat proceeds)**: crew members' shares on boats normally with fewer than 10 crew — any amount
   - **Box 6 (Medical / health-care payments)**: payments to physicians and other medical or health-care providers — **even if corporation** (not tax-exempt or government hospitals)
   - **Box 7 (Direct sales of consumer products ≥ $5,000)**: checkbox for buy-sell-resale arrangements
   - **Box 8 (Substitute payments in lieu of dividends or tax-exempt interest)**: from securities lending — **even if corporation**
   - **Box 9 (Crop insurance proceeds)**: paid to farmers
   - **Box 10 (Gross proceeds paid to an attorney)**: e.g., settlement money paid to a claimant's attorney — **even if attorney is corporation**. Not fees for legal services provided to the payer (1099-NEC box 1a)
   - **Box 11 (Fish purchased for resale)**: cash payments to persons in the business of catching fish — **even if corporation**
   - **Box 12 (Section 409A deferrals)**: optional box
   - **Rev. April 2025 (2025 payments)**: Box 13 = FATCA filing requirement checkbox; Box 14 = reserved (excess golden parachute payments moved to 1099-NEC box 3)
   - **Rev. December 2026 (2026 payments)**: Box 13a = cash tips included in Box 3; Box 13b = Treasury Tipped Occupation Code; Box 14 = qualified overtime compensation included in Box 3; FATCA checkbox unnumbered
   - **Box 15 (Nonqualified deferred compensation)**: amounts includible under §409A because the plan fails §409A
4. **Payee data** — for each: legal name, TIN (SSN/EIN), address (from W-9)
5. **Filing channel** — IRS IRIS, paper, or third-party service. FIRE is retired after 2026; for 2026 forms (filed in 2027) IRIS is the only IRS intake system (Pub. 1099 (2026), What's New). Mandatory e-filing if 10+ information returns total.
6. **State filing requirements** — most states piggyback on CF/SF; verify.

### Recipient side

1. **Filer's legal name and SSN/ITIN** — for routing.
2. **Form copy** with all populated boxes.
3. **Underlying activity classification**:
   - Rent received → Schedule E (real property) or Schedule C (real estate dealer / equipment rental as a trade or business)
   - Royalties → Schedule E (typical) or Schedule C (in the business of creating intellectual property)
   - Prize/award → Schedule 1 Line 8i (prizes and awards); other Box 3 income → Schedule 1 Line 8z
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

Each box has its own threshold. Ask which calendar year the payments were made in; the year decides the threshold (Instructions for Forms 1099-MISC and 1099-NEC, Rev. April 2025 and Rev. December 2026, "Specific Instructions for Form 1099-MISC"):

| Box | 2025 payments | 2026 payments | Notes |
|-----|---------------|---------------|-------|
| Box 1 (Rents) | $600 | $2,000 | |
| Box 2 (Royalties) | $10 | $10 | §6050N |
| Box 3 (Other income, prizes, awards) | $600 | $2,000 | |
| Box 5 (Fishing boat proceeds) | "Any fishing boat proceeds" | Any amount | §6050A |
| Box 6 (Medical / health-care payments) | $600 | $2,000 | Reportable to corporations too |
| Box 8 (Substitute payments) | $10 | $10 | Reportable to corporations too |
| Box 9 (Crop insurance proceeds) | $600 | $2,000 | |
| Box 10 (Gross proceeds to attorney) | $600 | $600 | §6045(f); reportable to corporations too |
| Box 11 (Fish purchased for resale, cash) | $600 | $600 | §6050R; reportable to corporations too |
| Box 12 / Box 15 (§409A) | $600 | $2,000 | Box 12 is optional |

P.L. 119-21 §70433 replaced the $600 in IRC §6041(a) with $2,000 for payments made after December 31, 2025, indexed for inflation in $100 steps from 2027 (IRC §6041(h)); the Rev. December 2026 instructions apply it to every §6041 box above. Royalties, substitute payments, attorney gross proceeds, and fish purchases have their own sections and did not change. Read the current indexed figure at the About Form 1099-MISC page before filing 2027 payments.

If backup withholding was applied to any payment, issue 1099-MISC regardless of whether the threshold is met.

#### Step 3 — Verify W-9 data

Same as 1099-NEC: every payee crossing a threshold needs a current W-9. TIN-match before filing.

For **Box 6 (medical), Box 8 (substitute payments), Box 10 (attorney gross proceeds), and Box 11 (fish purchases)**, the corporate exemption does NOT apply — issue 1099-MISC even to corporations (Instructions, "Reportable payments to corporations"; Reg. §1.6041-3(p)(1)). This is the most-missed special rule. See [`references/corporate-exception.md`](./references/corporate-exception.md).

#### Step 4 — Allocate amounts to boxes

Many 1099-MISC scenarios involve splitting one transaction across multiple boxes:

- **Settlement paid to the claimant's attorney**:
  - Attorney → Box 10, the gross amount paid to the attorney
  - Claimant → Box 3, the **full** taxable damages (not net of the attorney's fee), if taxable
  - The payer does **not** report the claimant's attorney's fees on a 1099-NEC (Instructions, "Gross proceeds paid to attorneys"; Reg. §1.6045-5(f), Examples 2–3)
  - Damages (other than punitive) for personal physical injury or physical sickness: no Box 3 to the claimant; Box 10 to the attorney still applies
- **Machine rental with an operator**: prorate — machine rent → Box 1; operator's charge → 1099-NEC box 1a (Instructions, Box 1)

See [`references/settlement-allocation.md`](./references/settlement-allocation.md) for the allocation playbook.

#### Step 5 — Populate header and boxes

Per [`references/box-by-box.md`](./references/box-by-box.md). Use truncated TIN on Copy B (recipient), full TIN on Copy A (IRS).

#### Step 6 — Distribute copies

- **Copy A** (IRS): paper deadline February 28; electronic deadline March 31 (note: this is **later** than 1099-NEC, which is January 31)
- **Copy B** (recipient): January 31; February 15 if any amount is in Box 8 or Box 10 (Pub. 1099 (2026), Reminders)
- A date on a Saturday, Sunday, or legal holiday moves to the next business day. 2025 forms: recipients Feb 2, 2026 (Feb 17, 2026 with Box 8/10), IRS Mar 2, 2026 paper / Mar 31, 2026 electronic. 2026 forms: recipients Feb 1, 2027 (Feb 16, 2027 with Box 8/10), IRS Mar 1, 2027 paper / Mar 31, 2027 electronic.

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
| Box 3 (Other income) | Schedule 1 Line 8i (prizes and awards) or Line 8z (other) | Schedule C or F if it is trade or business income (Copy B, Box 3) |
| Box 4 (Fed withholding) | Form 1040 Line 25b | (always Form 1040, regardless of which box source) |
| Box 5 (Fishing boat) | Schedule C | (commercial fishing as a trade or business) |
| Box 6 (Medical) | Schedule C | (healthcare provider's business income) |
| Box 8 (Substitute) | Schedule 1 "Other income" line (8z) | Copy B, Box 8 |
| Box 9 (Crop insurance) | Schedule F (farming) | |
| Box 10 (Attorney gross proceeds) | Attorney's Schedule C: only the taxable part (the fee) is income | Copy B: "Report only the taxable part as income" |
| Box 12 (§409A deferrals) | Informational; nothing to report from Box 12 alone | Any currently taxable amount is also in Box 15 |
| Box 13a / 13b, 14 (2026 forms) | Cash tips / TTOC / overtime, all already included in Box 3 | Used for Schedule 1-A deductions; outside this skill |
| Box 15 (NQDC, §409A failure) | Report as income on the return | Plus 20% additional tax and interest on Schedule 2 line 17h |

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
- Rent paid to a corporation (corporate exemption applies for Box 1, Reg. §1.6041-3(p)(1))

Threshold: $600 (2025 payments), $2,000 (2026 payments).

### Box 2 — Royalties

Royalties paid for the use of intellectual property (copyrights, patents, trademarks, mineral rights, oil/gas leases). Threshold: **$10**.

### Box 3 — Other income

Catch-all for taxable miscellaneous payments not fitting elsewhere:
- Prizes and awards not for services (cash or fair market value of merchandise)
- Taxable damages: punitive damages (even when they relate to physical injury), damages for nonphysical injuries such as discrimination or defamation. Not reported: damages (other than punitive) for personal physical injury or physical sickness, IRC §104(a)(2)
- Deceased employee's wages and accrued pay paid to the estate or beneficiary, whether paid in the year of death or later
- Taxable damages paid to a claimant through the claimant's attorney: the full amount, not net of the attorney's fee

Threshold: $600 (2025 payments), $2,000 (2026 payments).

### Box 4 — Federal income tax withheld

Backup withholding under IRC §3406 (24%), plus withholding on Indian gaming profits paid to tribal members. Same mechanics as 1099-NEC Box 4. See [`../form-1099-nec/references/backup-withholding.md`](../form-1099-nec/references/backup-withholding.md).

### Box 5 — Fishing boat proceeds

Each crew member's share of catch proceeds (or FMV of a distribution in kind) on boats normally with fewer than 10 crew members, plus up to $100 per trip for additional duties. Specific to the commercial fishing industry. Threshold: none; report any amount.

### Box 6 — Medical and health-care payments

Payments made to physicians and other suppliers or providers of medical or health-care services, including payments by health insurers under health, accident, and sickness programs. **Reportable even if the provider is a corporation**, including professional corporations (other corporate-exemption exceptions: Boxes 8, 10, 11).

Includes: doctors' fees, lab fees, hospital payments for services rendered, payments to nurses, dentists, psychologists. When the provider's charge includes injections, drugs, or dentures, report the entire payment.

Excludes: insurance premiums, payments to pharmacies for prescription drugs, payments to tax-exempt (501(c)(3)) or government-owned hospitals and extended care facilities, and payments under a health FSA or HRA (Instructions, Box 6; Reg. §1.6041-3(p)(1)).

Threshold: $600 (2025 payments), $2,000 (2026 payments).

### Box 7 — Direct sales of consumer products ≥ $5,000

Same as 1099-NEC Box 2 — checkbox for direct-sales / MLM relationships. The payer can use either form (1099-NEC Box 2 or 1099-MISC Box 7) but not both.

### Box 8 — Substitute payments in lieu of dividends or interest

Substitute payments of at least $10 received by a broker for a customer in lieu of dividends or tax-exempt interest because the customer's securities were on loan. Reportable to corporations too.

### Box 9 — Crop insurance proceeds

Crop insurance proceeds paid to farmers by insurance companies, unless the farmer told the insurer that expenses were capitalized under §278, 263A, or 447. Threshold: $600 (2025 payments), $2,000 (2026 payments).

### Box 10 — Gross proceeds paid to an attorney

Gross proceeds of $600 or more paid to an attorney in connection with legal services but not for the attorney's services to the payer, e.g., a settlement check paid to the claimant's attorney (IRC §6045(f)). Report the full amount paid to the attorney, regardless of how much the attorney keeps. **Reportable even if the attorney is a corporation.**

This is distinct from 1099-NEC box 1a, which reports fees the payer pays an attorney for legal services provided to the payer ($2,000 for 2026 payments; also reportable to corporations).

For a $50,000 settlement of a taxable (non-physical-injury) claim paid to the claimant's attorney, who keeps $20,000 and passes $30,000 to the claimant:
- 1099-MISC to attorney, Box 10: $50,000 (gross proceeds)
- 1099-MISC to claimant, Box 3: $50,000 (the full taxable damages, not the $30,000 net)
- No 1099-NEC from the payer for the attorney's $20,000 fee (the payer does not report the claimant's attorney's fees)

If the $50,000 were damages for personal physical injury (no punitive part): Box 10 $50,000 to the attorney and nothing to the claimant (Reg. §1.6045-5(f), Example 2).

This split is the most-confused area of 1099-MISC reporting. See [`references/settlement-allocation.md`](./references/settlement-allocation.md).

### Box 11 — Fish purchased for resale

Total cash payments of $600 or more by a buyer in the business of purchasing fish for resale to a person in the business of catching fish. "Cash" excludes checks drawn on the buyer's account. Reportable to corporations too. Rare.

### Box 12 — Section 409A deferrals

Optional box (Notice 2008-115). If completed: total deferrals for the year under all nonqualified plans for the nonemployee, including earnings, of at least $600 (2025) / $2,000 (2026).

### Box 13 / 13a / 13b — FATCA checkbox or cash tips

Rev. April 2025: Box 13 is the FATCA filing requirement checkbox. Rev. December 2026: Box 13a is cash tips included in Box 3 and Box 13b is the Treasury Tipped Occupation Code (P.L. 119-21 §70201); the FATCA checkbox stays on the form unnumbered.

### Box 14 — Reserved (2025) / Overtime compensation (2026)

Rev. April 2025: reserved; excess golden parachute payments are no longer reported on 1099-MISC (now 1099-NEC box 3). Rev. December 2026: qualified overtime compensation included in Box 3 (only the premium part, e.g. the "half" of time-and-a-half; P.L. 119-21 §70202).

### Box 15 — Nonqualified deferred compensation

Amounts (including earnings) includible in income under §409A because the NQDC plan fails §409A, at least $600 (2025) / $2,000 (2026). The recipient owes a 20% additional tax plus interest (Schedule 2 line 17h).

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

- [ ] Any Box 6, 8, 10, or 11 payment to a corporation → confirm it's NOT excluded (corporate exemption doesn't apply for these boxes)
- [ ] Threshold applied for the right payment year ($600 for 2025, $2,000 for 2026 for the §6041 boxes)
- [ ] No 1099-NEC issued for a claimant's attorney's fee out of a settlement the payer paid
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
- [ ] Box 10 (attorney gross proceeds) reconciled — the recipient is the attorney; only the taxable part (the fee) is the attorney's income; amounts passed to the client are not income (Copy B, Box 10)

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

### Box 6 — Medical / health-care payments (CORPORATIONS INCLUDED, except tax-exempt / government hospitals)
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
| ... | Paid by card or via Stripe / PayPal — covered by 1099-K |
| ... | Below the threshold for the payment year |

## Filing checklist

- [ ] Recipient copies (Copy B) furnished by **January 31** (**February 15** if Box 8 or Box 10 has an amount); next business day if a weekend or holiday
- [ ] IRS Copy A: filed **paper by February 28** OR **electronic by March 31** (1099-MISC has later IRS deadline than 1099-NEC)
- [ ] State copies filed (state rules vary; some CF/SF states still require direct filing)
- [ ] Form 945 filed if any backup withholding remitted (deadline January 31; next business day if a weekend)
- [ ] Copies kept at least 3 years from the due date (4 years if backup withholding was imposed) (Pub. 1099 (2026))

## Sources cited
- IRS Form 1099-MISC, Rev. <year>
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. <year>
- IRC §6041 (as amended by P.L. 119-21 §70433), §6045(f), §3406
- Reg. §1.6041-3(p)(1) (corporate exemption and its medical / attorney exceptions)
- Reg. §1.6045-5 (gross proceeds paid to attorneys)
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
| 3   | Other income | $X,XXX | Schedule 1 Line 8i (prizes, awards) or 8z (other); Schedule C if trade or business |
| 4   | Federal tax withheld | $X,XXX | Form 1040 Line 25b |
| 6   | Medical / health-care | $X,XXX | Schedule C Line 1 (provider's business) |
| 10  | Gross proceeds to attorney | $X,XXX | Attorney's Schedule C: only the fee is income; amounts passed to the client are not |

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
- [`references/corporate-exception.md`](./references/corporate-exception.md) — Special rules for Boxes 6, 8, 10, 11 — corporate exemption does NOT apply
- [`references/settlement-allocation.md`](./references/settlement-allocation.md) — How to report a settlement paid through the claimant's attorney (Box 10 to the attorney, Box 3 to the claimant)
- [`references/recipient-routing.md`](./references/recipient-routing.md) — Routing each box to the right schedule on the recipient's return
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer errors with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing 1099-MISC via IRIS or paper

## Examples

- [`examples/payor-rent-to-landlord.md`](./examples/payor-rent-to-landlord.md) — Small business issuing 1099-MISC Box 1 for $14,400 commercial office rent paid to an individual landlord
- [`examples/payor-attorney-settlement.md`](./examples/payor-attorney-settlement.md) — Business paying a $3,500 settlement to the claimant's attorney: Box 10 to the attorney and Box 3 for the full $3,500 to the claimant; no 1099-NEC for the fee
- [`examples/payor-medical-payment.md`](./examples/payor-medical-payment.md) — Business paying $2,450 directly to a corporate medical provider (Box 6), illustrating that the corporate exemption does NOT apply and the 2026 $2,000 threshold

## Sources

- [1099-MISC vs 1099-NEC (2026): Which Form You File and When + AI Agent Skill](https://jupid.com/blog/1099-misc-vs-1099-nec-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1099-MISC (Rev. December 2026)](https://www.irs.gov/pub/irs-pdf/f1099msc.pdf) — the form for 2026 payments; Rev. April 2025 for 2025 payments (https://www.irs.gov/pub/irs-prior/f1099msc--2025.pdf)
- [Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) — combined IRS instructions
- [About Form 1099-MISC](https://www.irs.gov/forms-pubs/about-form-1099-misc) — IRS landing page
- [Publication 1099 (2026)](https://www.irs.gov/pub/irs-pdf/p1099.pdf) — General Instructions for Certain Information Returns (due dates, corrections, FIRE retirement, record retention)
- [Form 1096 (2026)](https://www.irs.gov/pub/irs-pdf/f1096.pdf) — paper transmittal; type code 95; mailing addresses
- [Information Returns Intake System (IRIS)](https://www.irs.gov/filing/e-file-information-returns) — IRS free e-file portal
- [Form 945](https://www.irs.gov/forms-pubs/about-form-945) — Annual Return of Withheld Federal Income Tax
- IRC §6041 (general info-return obligation; $2,000 for payments after 2025, §6041(h) indexing), §6041A (services), §6045(d) (substitute payments), §6045(f) (gross proceeds paid to attorneys), §6050A (fishing boat proceeds), §6050N (royalties), §6050R (fish purchases), §3406 (backup withholding), §6011(e) (mandatory e-file), §61 (gross income), §104 (exclusions for personal physical injury), §409A (deferred compensation)
- P.L. 119-21 §70433 (One Big Beautiful Bill Act: $600 → $2,000 in §6041(a) for payments after Dec. 31, 2025); §§70201–70202 (cash tips and overtime boxes)
- Reg. §1.6041-3(p)(1) (corporate exemption, with exceptions for attorneys' fees and medical and health-care providers)
- Reg. §1.6041-1(f) and §1.6045-5 (payments to attorneys and claimants; Examples)
- Reg. §1.6041-1(a)(1)(i) — definition of "in the course of trade or business"
- Reg. §301.6109-4 (TIN truncation on payee statements)
- Taxpayer First Act of 2019, codified at IRC §6011(e)(2) — 10-return e-file threshold

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Complex situations — particularly settlement allocations splitting attorney / plaintiff portions, multi-box scenarios, §409A failures, and prize / award characterization — warrant a licensed tax professional's review.
