# Form 1099-MISC Box-by-Box Reference

Complete lookup for every box on Form 1099-MISC and the payer/recipient header blocks.

## Header blocks

### Payer (top-left)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Payer's name, address, phone | Payer's legal business name and primary mailing address | Must match payer's IRS records |
| Payer's TIN | Payer's EIN | |

### Recipient (left-center)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Recipient's name | Legal name from W-9 Line 1 | For SMLLC: owner's name. For corporation: corporation's legal name. |
| (Optional) DBA | From W-9 Line 2 | Below legal name |
| Recipient's TIN | SSN, ITIN, or EIN | Truncate on Copy B (last 4); full on Copy A |
| Recipient's address | From W-9 | |
| Account number | Optional internal payer reference | Required if multiple 1099s for same recipient |

### Special header items

- **2nd TIN not.**: check if IRS notified payer 2x in 3 years that recipient TIN is wrong
- **FATCA filing requirement**: rare; for Foreign Account Tax Compliance Act
- **CORRECTED**: filing correction of previously-issued 1099-MISC
- **VOID**: invalidate paper Copy A pre-submission

---

## Box 1 — Rents

**What goes here**: Rent paid to a landlord during the year for business use of property.

Includes:
- Office, warehouse, retail, storage rental paid to property owners (not corporate)
- Equipment rental: forklift, copier, tractor, generator
- Vehicle rental for business use (paid to non-corporate rental company)

Excludes:
- Residential rent paid by a tenant
- Rent paid through a property management company that issues its own 1099-MISC to the landlord
- Rent paid to a corporation (corporate exemption applies to Box 1)

**Threshold**: $600 per payee per year. Verify whether OBBBA changed this for 2026 — as of last verification, $600 still applies.

**Common error**: payer pays a residential landlord for the payer's apartment and treats it as personal rent (no 1099 needed). But if the apartment is used as a home office and the rent is being deducted as a business expense, the *business portion* is reportable as rent — even though it's residential property. Reg. §1.6041-1.

## Box 2 — Royalties

**What goes here**: Royalty payments paid for the use of intellectual property, mineral rights, copyrights, patents, trademarks, or oil/gas leases.

Threshold: **$10** (lowest of any 1099 box).

Common payees:
- Oil/gas lease holders
- Music publishers / songwriters
- Authors (book royalties)
- Patent holders

## Box 3 — Other income

**What goes here**: Catch-all for taxable miscellaneous payments not fitting other boxes.

Includes:
- Prizes and awards (cash or fair market value of merchandise) ≥ $600
- Damages awarded in a lawsuit (excluding personal physical injury — IRC §104)
- Punitive damages
- Settlement payment to plaintiff (the plaintiff's portion when settlement passed through attorney's trust account)
- Deceased employee's wages paid in the year after death (if final wages weren't on W-2)
- Payments by Indian gaming establishments to tribal members (per capita distributions)
- Termination payments to former insurance salespeople
- Survivor benefits paid

Excludes:
- Nonemployee compensation for services (use 1099-NEC)
- Personal injury damages (IRC §104 exclusion — not income)
- Compensatory damages for emotional distress arising from physical injury

Threshold: $600.

## Box 4 — Federal income tax withheld

Backup withholding (24%) under IRC §3406. Same mechanics as 1099-NEC Box 4. Triggered when:
- No TIN on file
- TIN mismatch (B-Notice received)
- Recipient under-reporting (C-Notice)

Reconciles to Form 945 filed by January 31.

## Box 5 — Fishing boat proceeds

**What goes here**: Each crew member's share of catch proceeds from a fishing boat operating with fewer than 10 crew members.

Specific to commercial fishing. See IRS Pub. 595 for industry-specific rules.

Threshold: $600.

## Box 6 — Medical and health-care payments

**What goes here**: Payments to physicians, hospitals, and other healthcare providers for services rendered.

Includes:
- Doctor / physician fees
- Hospital service payments (not premiums)
- Dentist, orthodontist, periodontist
- Laboratory fees
- Nursing services
- Physical therapy, mental health services
- Chiropractor, acupuncturist
- Veterinarian (if for business animals)

Excludes:
- Health insurance premiums (insurance company handles its own reporting)
- Pharmacy / prescription payments (sale of goods, not services)
- Reimbursements to employees under HRA / FSA / cafeteria plans (those are payroll-side, not 1099)

**Special rule**: REPORTABLE EVEN IF PROVIDER IS A CORPORATION. The standard corporate exemption (Reg. §1.6041-3(c)) does NOT apply to Box 6 medical payments. See [`corporate-exception.md`](./corporate-exception.md).

Threshold: $600.

## Box 7 — Direct sales of consumer products ≥ $5,000

**What goes here**: Checkbox for direct-sales / MLM relationships where payer made $5,000+ in cumulative sales of consumer products to recipient on a buy-sell, deposit-commission, or other commission basis.

Common in: Mary Kay, Avon, Tupperware, Amway, etc.

Note: payer can use either 1099-NEC Box 2 OR 1099-MISC Box 7 — NOT both. Pick one form per recipient.

## Box 8 — Substitute payments in lieu of dividends or interest

**What goes here**: Substitute amounts paid in lieu of dividends or tax-exempt interest, typically from securities lending or short-sale arrangements.

Threshold: **$10**.

For brokers: this is paid to a customer whose securities were lent out, in lieu of the dividends those securities would have generated.

## Box 9 — Crop insurance proceeds

**What goes here**: Insurance proceeds paid to farmers under federal crop insurance programs.

Threshold: $600.

Routes to recipient's Schedule F (farm income).

## Box 10 — Gross proceeds paid to an attorney

**What goes here**: TOTAL amount of a settlement that passed through an attorney's trust account, regardless of how much the attorney kept as fee.

This is distinct from the attorney's *fee* (which goes on 1099-NEC Box 1). Box 10 is the **gross proceeds** — the entire settlement amount.

**Special rule**: REPORTABLE EVEN IF ATTORNEY IS A CORPORATION. Reg. §1.6041-1(d)(2). See [`corporate-exception.md`](./corporate-exception.md).

For a $50,000 settlement where the attorney keeps $20,000 and passes $30,000 to the plaintiff:
- 1099-MISC to attorney, Box 10: **$50,000** (gross proceeds)
- 1099-NEC to attorney, Box 1: **$20,000** (attorney's fee for services)
- 1099-MISC to plaintiff, Box 3: **$30,000** (taxable settlement to plaintiff, if not §104 excluded)

The defendant / payor issues all three forms.

Threshold: $600.

## Box 11 — Section 1042-S transactions (fish processor cash purchases)

**What goes here**: Cash purchases of fish (in the amount of $600 or more) for resale, paid to independent fishers.

Specific to fish-processing businesses. Rare.

## Box 12 — Section 409A deferrals

**What goes here**: Deferrals into a nonqualified deferred compensation plan that are taxable currently because the plan failed §409A compliance.

Rare. Routes to Form 1040 with 20% additional tax under §409A(a)(1)(B).

## Box 13 — FATCA filing requirement

Checkbox for Foreign Account Tax Compliance Act reporting. Rare.

## Box 14 — Excess golden parachute payments

**What goes here**: Excess parachute payments under §280G / §4999. The recipient pays a 20% excise tax on the excess.

Rare; typically only relevant in large corporate change-of-control transactions.

## Box 15 — Nonqualified deferred compensation

**What goes here**: Income inclusions under §409A(a)(1)(A) — deferred compensation that becomes currently taxable due to §409A failure.

Distinct from Box 12 (deferrals); Box 15 is income inclusion of previously deferred amounts.

## Boxes 16-18 — State info

| Box | Field |
|-----|-------|
| 16  | State tax withheld |
| 17  | State / Payer's state ID |
| 18  | State income |

The form supports two state rows (each box appears twice). For more states, file multiple forms with different state rows.

---

## Box deadlines and timing

For 1099-MISC forms issued for tax year 2026:

| Action | Deadline |
|--------|----------|
| Recipient Copy B postmarked or e-delivered | February 1, 2027 |
| IRS Copy A — paper | February 28, 2027 |
| IRS Copy A — electronic (IRIS / FIRE) | March 31, 2027 |
| Form 945 (if backup withholding) | January 31, 2027 |
| State filings (varies by state) | Varies; many tie to federal CF/SF |

**Note**: 1099-MISC has later IRS deadlines than 1099-NEC. 1099-NEC IRS deadline is January 31 (same as recipient deadline); 1099-MISC IRS deadline is February 28 paper / March 31 electronic. Don't conflate the two schedules.

## Box matrix: which forms get a 1099-MISC

| Payment to | Box 1 (Rents) | Box 6 (Medical) | Box 10 (Attorney) | Box 3 (Other) |
|------------|--------------|------------------|--------------------|---------------|
| Individual / SMLLC / Partnership | Yes (≥$600) | Yes (≥$600) | Yes (≥$600) | Yes (≥$600) |
| C-Corporation | **No** (exempt) | **YES** (no exemption) | **YES** (no exemption) | **No** (exempt) |
| S-Corporation | **No** (exempt) | **YES** (no exemption) | **YES** (no exemption) | **No** (exempt) |
| Government entity / nonprofit | Generally no (specific exemptions in Reg. §1.6041-3) | Often yes for medical providers | Often yes for legal services | Generally no |

The Box 6 / Box 10 corporate exception is the biggest 1099-MISC trap. See [`corporate-exception.md`](./corporate-exception.md).
