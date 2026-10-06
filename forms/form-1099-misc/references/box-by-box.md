# Form 1099-MISC Box-by-Box Reference

Complete lookup for every box on Form 1099-MISC and the payer/recipient header blocks. Verified against Form 1099-MISC Rev. December 2026 (2026 payments) and Rev. April 2025 (2025 payments) and the Instructions for Forms 1099-MISC and 1099-NEC of the same revisions. Thresholds: the §6041 boxes are $600 for 2025 payments and $2,000 for 2026 payments (P.L. 119-21 §70433). Re-check https://www.irs.gov/forms-pubs/about-form-1099-misc for a newer revision.

## Header blocks

### Payer (top-left)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Payer's name, address, phone | Payer's legal business name and primary mailing address | Must match payer's IRS records |
| Payer's TIN | Payer's EIN | |

### Recipient (left-center)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Recipient's name | Legal name from W-9 Line 1 | For a disregarded SMLLC: owner's name (W-9 line 1). For corporation: corporation's legal name. |
| (Optional) DBA | From W-9 Line 2 | Below legal name |
| Recipient's TIN | SSN, ITIN, or EIN | Truncate on Copy B (last 4); full on Copy A |
| Recipient's address | From W-9 lines 5–6 | Rev. December 2026 splits street, apt., city, state, country, ZIP into separate boxes |
| Account number | Optional internal payer reference | Required if multiple 1099s for same recipient |

### Special header items

- **2nd TIN not.**: check if IRS notified payer 2x in 3 years that recipient TIN is wrong
- **FATCA filing requirement**: rare; for Foreign Account Tax Compliance Act (Box 13 on Rev. April 2025; unnumbered checkbox on Rev. December 2026). Account number required if checked
- **CORRECTED**: filing correction of previously-issued 1099-MISC
- **VOID**: invalidate paper Copy A pre-submission

---

## Box 1 — Rents

**What goes here**: Rent paid to a landlord during the year for business use of property.

Includes:
- Office, warehouse, retail, storage rental paid to property owners (not corporate)
- Machine / equipment rental: forklift, copier, bulldozer, generator. If the rental includes an operator, prorate: machine rent in Box 1, operator's charge on 1099-NEC box 1a
- Pasture rental; coin-operated amusement space or machine leases
- Vehicle rental for business use (paid to non-corporate rental company)

Excludes:
- Residential rent paid by a tenant
- Rent paid to a real estate agent or property manager (the agent or manager reports the rent paid over to the owner; Reg. §1.6041-3(d))
- Rent paid to a corporation (corporate exemption applies to Box 1; Reg. §1.6041-3(p)(1))

**Threshold**: $600 per payee for 2025 payments; $2,000 for 2026 payments (Instructions, Box 1).

**Common error**: payer pays a residential landlord for the payer's apartment and treats it as personal rent (no 1099 needed). But if the apartment is used as a home office and the rent is being deducted as a business expense, the *business portion* may be reportable as rent if paid in the course of the trade or business — even though it's residential property. Reg. §1.6041-1(a). Ask the user; this is a judgment call.

## Box 2 — Royalties

**What goes here**: Royalty payments paid for the use of intellectual property, mineral rights, copyrights, patents, trademarks, or oil/gas leases.

Threshold: **$10** (shared with Box 8). Report gross royalties before fees or commissions; oil, gas, and mineral royalties before severance taxes. Working-interest payments go on 1099-NEC box 1a; timber pay-as-cut royalties on 1099-S.

Common payees:
- Oil/gas lease holders
- Music publishers / songwriters
- Authors (book royalties)
- Patent holders

## Box 3 — Other income

**What goes here**: Catch-all for taxable miscellaneous payments not fitting other boxes.

Includes:
- Prizes and awards not for services (cash or fair market value of merchandise); sweepstakes without a wager
- Punitive damages (even when they relate to physical injury), damages for nonphysical injuries (discrimination, defamation), ADEA liquidated damages, and other taxable damages
- Taxable damages paid to a claimant through the claimant's attorney: the full amount, not net of fees (Reg. §1.6045-5(f), Example 3)
- Deceased employee's wages and accrued pay paid to the estate or beneficiary, whether in the year of death or later (W-2 also shows Social Security / Medicare wages if paid in the year of death)
- Indian gaming profits paid to tribal members
- Payments for participating in medical research studies
- Termination payments to former insurance salespeople meeting all six conditions in the instructions
- NQDC / §457 death benefits paid to the estate or beneficiary

Excludes:
- Nonemployee compensation for services (use 1099-NEC), including awards for services
- Damages (other than punitive) for personal physical injury or physical sickness (IRC §104(a)(2)), including emotional distress due to physical injury
- Damages for replacement of capital

Threshold: $600 (2025 payments); $2,000 (2026 payments).

## Box 4 — Federal income tax withheld

Backup withholding (24%) under IRC §3406, plus income tax withheld from Indian gaming profits paid to tribal members. Same mechanics as 1099-NEC Box 4. Triggered when:
- No TIN on file
- TIN mismatch (B-Notice received)

For §6041 payments (rents, other income, medical, crop insurance), backup withholding applies only once the year's payments to the payee reach the §6041(a) amount ($600 for 2025, $2,000 for 2026; IRC §3406(b)(6) as amended by P.L. 119-21 §70433(d)). Reconciles to Form 945 (line 2) filed by January 31.

## Box 5 — Fishing boat proceeds

**What goes here**: Each crew member's share of all proceeds from the sale of a catch (or FMV of a distribution in kind) on boats normally with fewer than 10 crew members (average over the preceding 4 calendar quarters), plus cash of up to $100 per trip for additional duties.

Specific to commercial fishing. See IRS Pub. 595 for industry-specific rules.

Threshold: none; report any amount.

## Box 6 — Medical and health-care payments

**What goes here**: Payments to physicians, hospitals, and other healthcare providers for services rendered.

Includes:
- Doctor / physician fees
- Hospital service payments (not premiums), except as excluded below
- Dentist, orthodontist, periodontist
- Laboratory fees
- Nursing services
- Physical therapy, mental health services
- Chiropractor, acupuncturist
- Payments by health insurers under health, accident, and sickness programs
- Provider charges that include injections, drugs, dentures (report the entire payment)

Excludes:
- Health insurance premiums
- Payments to pharmacies for prescription drugs
- Payments to tax-exempt (501(c)(3)) or government-owned hospitals and extended care facilities
- Payments under a health FSA or HRA

**Special rule**: REPORTABLE EVEN IF PROVIDER IS A CORPORATION, including professional corporations. The standard corporate exemption (Reg. §1.6041-3(p)(1)) carves out medical and health-care providers. See [`corporate-exception.md`](./corporate-exception.md).

Threshold: $600 (2025 payments); $2,000 (2026 payments).

## Box 7 — Direct sales of consumer products ≥ $5,000

**What goes here**: Checkbox for direct-sales / MLM relationships where payer made $5,000+ in cumulative sales of consumer products to recipient on a buy-sell, deposit-commission, or other commission basis.

Common in: Mary Kay, Avon, Tupperware, Amway, etc.

Note: payer can use either 1099-NEC Box 2 OR 1099-MISC Box 7 — NOT both. Pick one form per recipient.

## Box 8 — Substitute payments in lieu of dividends or interest

**What goes here**: Substitute payments received by a broker for a customer in lieu of dividends or tax-exempt interest because the customer's securities were on loan.

Threshold: **$10**. Reportable to corporations too. Copy B due February 15.

For brokers: this is paid to a customer whose securities were lent out, in lieu of the dividends those securities would have generated.

## Box 9 — Crop insurance proceeds

**What goes here**: Crop insurance proceeds paid to farmers by insurance companies, unless the farmer told the insurer that expenses were capitalized under §278, 263A, or 447.

Threshold: $600 (2025 payments); $2,000 (2026 payments).

Routes to recipient's Schedule F (farm income).

## Box 10 — Gross proceeds paid to an attorney

**What goes here**: Gross proceeds paid to an attorney in connection with legal services but not for the attorney's services to the payer — e.g., a settlement check paid to the claimant's attorney — regardless of how much the attorney keeps (IRC §6045(f); Reg. §1.6045-5).

This is distinct from fees the payer pays its own attorney for legal services, which go on 1099-NEC box 1a ($2,000 for 2026 payments; also reportable to corporations). The payer does **not** report the claimant's attorney's fees.

**Special rule**: REPORTABLE EVEN IF ATTORNEY IS A CORPORATION (Instructions, "Payments to corporations for legal services"; Reg. §1.6041-3(p)(1)). See [`corporate-exception.md`](./corporate-exception.md).

For a $50,000 settlement of a taxable claim paid to the claimant's attorney, who keeps $20,000 and passes $30,000 to the claimant:
- 1099-MISC to attorney, Box 10: **$50,000** (gross proceeds)
- 1099-MISC to claimant, Box 3: **$50,000** (full taxable damages, not the $30,000 net)
- No 1099-NEC for the attorney's $20,000

If the damages are for personal physical injury (no punitive part): Box 10 to the attorney only.

Threshold: $600 for both 2025 and 2026 payments. Copy B due February 15.

## Box 11 — Fish purchased for resale

**What goes here**: Total cash payments of $600 or more paid during the year by a buyer in the business of purchasing fish for resale to a person in the business of catching fish (IRC §6050R). "Cash" means currency, cashier's checks, bank drafts, traveler's checks, money orders; not checks drawn on the buyer's own account. Reportable to corporations too.

Specific to fish-buying businesses. Rare.

## Box 12 — Section 409A deferrals

**What goes here**: Optional (Notice 2008-115). Total deferrals for the year for the nonemployee under all nonqualified plans, including earnings on current and prior deferrals; at least $600 (2025) / $2,000 (2026) if completed.

Informational for the recipient; any currently taxable amount is also in Box 15.

## Box 13 (2025) / Boxes 13a–13b (2026)

- Rev. April 2025: Box 13 = FATCA filing requirement checkbox.
- Rev. December 2026: Box 13a = cash tips included in Box 3; Box 13b = up to two Treasury Tipped Occupation Codes ("000" if any tips came from a nonqualifying occupation). P.L. 119-21 §70201. The FATCA checkbox remains, unnumbered.

## Box 14 — Reserved (2025) / Overtime compensation (2026)

- Rev. April 2025: reserved for future use. Excess golden parachute payments are no longer on 1099-MISC; they go on 1099-NEC box 3.
- Rev. December 2026: qualified overtime compensation included in Box 3 (only the premium part, e.g. the "half" of time-and-a-half). P.L. 119-21 §70202.

## Box 15 — Nonqualified deferred compensation

**What goes here**: All amounts deferred (including earnings) that are includible in income under §409A because the NQDC plan fails §409A, at least $600 (2025) / $2,000 (2026). Don't include amounts reported for a prior year or still subject to a substantial risk of forfeiture.

Distinct from Box 12 (deferrals); Box 15 is the income inclusion. The recipient also owes the 20% additional tax plus interest (Schedule 2 line 17h).

## Boxes 16-18 — State info

| Box | Field |
|-----|-------|
| 16  | State tax withheld |
| 17  | State / Payer's state ID |
| 18  | State income |

The form supports two state rows (each box appears twice). For more states, file multiple forms with different state rows.

---

## Box deadlines and timing

For 1099-MISC forms issued for tax year 2026 (statutory dates January 31, February 15, February 28, March 31; next business day when a date falls on a weekend or legal holiday):

| Action | Deadline |
|--------|----------|
| Recipient Copy B furnished (no Box 8 / 10 amounts) | February 1, 2027 (January 31 is a Sunday) |
| Recipient Copy B furnished (Box 8 or 10 amounts) | February 16, 2027 (February 15 is Presidents' Day) |
| IRS Copy A — paper | March 1, 2027 (February 28 is a Sunday) |
| IRS Copy A — electronic (IRIS; FIRE is retired) | March 31, 2027 |
| Form 945 (if backup withholding) | February 1, 2027 |
| State filings (varies by state) | Varies; some CF/SF states still require direct filing (e.g., Massachusetts) |

**Note**: 1099-MISC has later IRS deadlines than 1099-NEC. 1099-NEC IRS deadline is January 31 (same as recipient deadline); 1099-MISC IRS deadline is February 28 paper / March 31 electronic. Don't conflate the two schedules.

## Box matrix: which forms get a 1099-MISC

| Payment to | Box 1 (Rents) | Box 6 (Medical) | Box 10 (Attorney) | Box 3 (Other) |
|------------|--------------|------------------|--------------------|---------------|
| Individual / SMLLC / Partnership | Yes (≥ threshold) | Yes (≥ threshold) | Yes (≥$600) | Yes (≥ threshold) |
| C-Corporation | **No** (exempt) | **YES** (no exemption) | **YES** (no exemption) | **No** (exempt) |
| S-Corporation | **No** (exempt) | **YES** (no exemption) | **YES** (no exemption) | **No** (exempt) |
| Tax-exempt organization / government | No (Reg. §1.6041-3(p)(2)–(5)) | No for tax-exempt or government hospitals; ask for other providers | Ask; check Reg. §1.6041-3(p) | No |

"Threshold" = $600 for 2025 payments, $2,000 for 2026 payments.

The Box 6 / Box 10 corporate exception (plus Boxes 8 and 11) is the biggest 1099-MISC trap. See [`corporate-exception.md`](./corporate-exception.md).
