# Example: Small Business Issuing 1099-MISC Box 1 for Office Rent

A complete walkthrough of issuing Form 1099-MISC Box 1 for $14,400 paid to an individual landlord for commercial office rent in 2026. This is the canonical "small business renting office space directly from an individual landlord" pattern.

## The payer

- **Name**: Cedar & Cloth Apparel LLC (multi-member LLC taxed as partnership)
- **EIN**: 84-2901XXX
- **Address**: 38 Mill St, Burlington, VT 05401
- **Business**: Boutique apparel design and online sales
- **Tax year**: 2026

## The landlord (payee)

- **Name**: Helena Boucher (individual, owns the office building personally)
- **W-9 status** (Form W-9 Rev. March 2024): returned January 12, 2026 (before lease started):
  - Line 1: Helena Boucher
  - Line 2: blank (no DBA)
  - Line 3a: Individual/sole proprietor
  - Lines 5–6: 412 Pearl St, Burlington, VT 05401
  - Part I: SSN 058-XX-XXXX
  - Part II: certified, not subject to backup withholding
- **TIN matching**: payer ran TIN match on January 13, 2026; matched.

## The transaction

- Lease: 12 months starting February 1, 2026
- Monthly rent: $1,200
- Annual rent paid in 2026: $1,200 × 12 = **$14,400** (full year — landlord required first month + last month upfront in February, then monthly thereafter; all paid by check)
- Payment method: check (direct payor → landlord)

## Decision: 1099-MISC Box 1 required?

**Threshold**: $2,000 for Box 1 rent paid in 2026 (P.L. 119-21 §70433; Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026, Box 1). It was $600 for 2025 payments.

$14,400 ≥ $2,000 → **threshold met**.

**Entity classification**: Helena is an individual (W-9 Line 3a) → not a corporation → **subject to 1099-MISC Box 1**.

**Payment channel**: paid by check, no third-party payment network → **payer issues 1099-MISC**.

**Trade or business**: Cedar & Cloth Apparel is a trade-or-business; the rent is paid in the course of that business → reportable.

**Conclusion**: Cedar & Cloth issues 1099-MISC to Helena.

## The completed 1099-MISC

```
FORM 1099-MISC (Rev. December 2026), calendar year 2026

PAYER: Cedar & Cloth Apparel LLC
  EIN: 84-2901XXX
  38 Mill St
  Burlington, VT 05401
  (802) 555-0177

RECIPIENT: Helena Boucher
  TIN (truncated on Copy B): XXX-XX-XXXX
  Address: 412 Pearl St, Burlington, VT 05401

Account number: CC-LEASE-2026

Box 1 — Rents:                            $14,400.00
Box 2 — Royalties:                        $0
Box 3 — Other income:                     $0
Box 4 — Federal income tax withheld:      $0
Box 5 — Fishing boat proceeds:            $0
Box 6 — Medical / health-care:            $0
Box 7 — Direct sales ≥$5,000:             ☐
Box 8 — Substitute payments:              $0
Box 9 — Crop insurance:                   $0
Box 10 — Gross proceeds to attorney:      $0
Box 11 — Fish purchased for resale:       $0
(Boxes 12, 13a, 13b, 14, 15 left blank; FATCA box unchecked)
Box 16 — State tax withheld:              $0
Box 17 — State / Payer's state no.:       VT / <Vermont-assigned payer ID, not the EIN>
Box 18 — State income:                    $14,400
```

## Filing checklist

- [x] Recipient Copy B mailed to Helena by **February 1, 2027** (January 31 is a Sunday; postmarked January 28, 2027)
- [x] Copy A filed with IRS via IRIS by **March 31, 2027** (electronic deadline; the paper deadline would be March 1, 2027 because February 28 is a Sunday)
- [x] State copy: ask whether Vermont needs a direct filing; check tax.vermont.gov (1099 e-filing specifications) instead of assuming IRIS CF/SF forwarding covers it
- [x] Records retained: signed W-9, TIN match confirmation, lease agreement, rent payment ledger, copies of canceled checks, 1099-MISC, IRIS submission ID
- [x] No Form 945 needed (no backup withholding)

## Helena's side: where does she report this?

Helena is an individual landlord — **not a real estate dealer, no substantial services**. Her rental activity is passive rental real estate.

She reports on **Schedule E Part I**:
- Property A (1 column): line 1a "38 Mill St, Burlington, VT 05401"; line 1b type 4 (Commercial)
- Line 3 (Rents received): $14,400
- Lines 5-19 (expenses): mortgage interest, property tax, insurance, utilities (if she pays), repairs, depreciation
- Line 21: net rental income or loss
- Net flows to Schedule 1 Line 5

If Helena has multiple rental properties, each gets its own column (A, B, C) in Schedule E Part I.

**Why not Schedule C?** Helena holds the property as an investment and doesn't provide significant services to the tenant. Copy B, Box 1: report rents from real estate on Schedule E unless you provided significant services to the tenant, sold real estate as a business, or rented personal property as a business. Rental activity is generally passive (IRC §469(c)(2)) unless an exception applies.

## Why each non-obvious choice

**Why is this Box 1 (rent) and not 1099-NEC (services)?** Helena is renting property to Cedar & Cloth, not providing services. The payment is for property use, not for personal services.

**What if Helena's office building were owned by an LLC taxed as S-corp?** Then the corporate exemption (Reg. §1.6041-3(p)(1)) would apply to Box 1, and Cedar & Cloth would NOT issue 1099-MISC. Verify entity type from W-9 every year — landlords sometimes change their entity election.

**What if Cedar & Cloth paid Helena by card or through a payment app?** Those payments are reported on Form 1099-K by the payment settlement entity, not on 1099-MISC (Instructions, "Form 1099-K"), so Cedar & Cloth leaves them off its 1099-MISC whether or not a 1099-K is actually issued.

**What if Cedar & Cloth used a property management company that collects rent and remits to Helena?** Rent paid to a real estate agent or property manager is not reportable by the tenant; the manager reports the rent paid over to Helena on 1099-MISC (Reg. §1.6041-3(d); Instructions, Box 1).

**Why include account number "CC-LEASE-2026"?** Optional. Useful for the payer's records; useful if Cedar & Cloth had multiple recipient relationships with Helena (e.g., separate sublease for storage).

**What if Helena were a non-resident alien?** Then the payer would need a W-8BEN, not a W-9. The payment may be subject to chapter 3 withholding (typically 30% on US-source rental income, subject to treaty), reported on **Form 1042-S**, not 1099-MISC. Out of scope for this example — but the agent should always check W-9 vs. W-8BEN (a Helena who is a US citizen / resident is W-9; a non-resident alien is W-8BEN).

## What if backup withholding had applied

Suppose Helena never returned a W-9. Cedar & Cloth would:
1. Apply 24% backup withholding on each $1,200 rent payment → $288 withheld
2. Pay Helena $912 net per month, deposit $288 with IRS via EFTPS
3. Annual: $14,400 × 24% = $3,456 withheld
4. File Form 945 by February 1, 2027 (January 31 is a Sunday) reporting $3,456 backup withholding on line 2
5. Issue 1099-MISC with Box 1 = $14,400, Box 4 = $3,456
6. Helena reports $14,400 gross rent on Schedule E Line 3, claims $3,456 credit on Form 1040 Line 25b

## Sources cited
- IRS Form 1099-MISC, Rev. December 2026 (https://www.irs.gov/pub/irs-pdf/f1099msc.pdf)
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026 (https://www.irs.gov/pub/irs-pdf/i1099mec.pdf)
- IRC §6041 (as amended by P.L. 119-21 §70433), §3406, §469(c)(2)
- Reg. §1.6041-3(p)(1) (corporate exemption), §1.6041-3(d) (rental agents)
- Form W-9 (Rev. March 2024)
- IRS Schedule E Part I (Form 1040)
