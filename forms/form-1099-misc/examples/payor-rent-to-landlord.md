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
- **W-9 status**: returned January 12, 2026 (before lease started):
  - Line 1: Helena Boucher
  - Line 2: blank (no DBA)
  - Line 3: Individual / sole proprietor or single-member LLC
  - Line 4: SSN 058-XX-XXXX
  - Line 5: 412 Pearl St, Burlington, VT 05401
  - Part II: certified, not subject to backup withholding
- **TIN matching**: payer ran TIN match on January 13, 2026; matched.

## The transaction

- Lease: 12 months starting February 1, 2026
- Monthly rent: $1,200
- Annual rent paid in 2026: $1,200 × 12 = **$14,400** (full year — landlord required first month + last month upfront in February, then monthly thereafter; all paid by check)
- Payment method: check (direct payor → landlord)

## Decision: 1099-MISC Box 1 required?

**Threshold**: $600 for Box 1 rent (current verification — OBBBA's $2,000 raise applies to §6041A nonemployee compensation per IRS guidance; not yet confirmed for §6041 rent payments. Default to $600 unless IRS issues new guidance).

$14,400 ≥ $600 → **threshold met**.

**Entity classification**: Helena is an individual (W-9 Line 3) → not a corporation → **subject to 1099-MISC Box 1**.

**Payment channel**: paid by check, no third-party payment network → **payer issues 1099-MISC**.

**Trade or business**: Cedar & Cloth Apparel is a trade-or-business; the rent is paid in the course of that business → reportable.

**Conclusion**: Cedar & Cloth issues 1099-MISC to Helena.

## The completed 1099-MISC

```
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
(Boxes 12-15 left blank or $0)
Box 16 — State tax withheld:              $0
Box 17 — State / Payer's state no.:       VT / 84-2901XXX
Box 18 — State income:                    $14,400
```

## Filing checklist

- [x] Recipient Copy B mailed to Helena by **February 1, 2027** (postmarked January 28, 2027)
- [x] Copy A filed with IRS via IRIS by **March 31, 2027** (electronic deadline; well before paper Feb 28 deadline since IRIS is e-filing)
- [x] State copy: VT is a CF/SF participant; IRIS forwarded to VT Department of Taxes automatically
- [x] Records retained: signed W-9, TIN match confirmation, lease agreement, rent payment ledger, copies of canceled checks, 1099-MISC, IRIS submission ID
- [x] No Form 945 needed (no backup withholding)

## Helena's side: where does she report this?

Helena is an individual landlord — **not a real estate dealer, no substantial services**. Her rental activity is passive rental real estate.

She reports on **Schedule E Part I**:
- Property A (1 column): "Office Building, 38 Mill St, Burlington VT"
- Line 3 (Rents received): $14,400
- Lines 5-19 (expenses): mortgage interest, property tax, insurance, utilities (if she pays), repairs, depreciation
- Line 21: net rental income or loss
- Net flows to Schedule 1 Line 5

If Helena has multiple rental properties, each gets its own column (A, B, C) in Schedule E Part I.

**Why not Schedule C?** Helena is a passive landlord (she holds the property as an investment, doesn't provide substantial services like daily housekeeping). Per Reg. §1.469-1T(e)(3), rental of real estate is a passive activity unless specific exceptions apply. Schedule C is for real estate dealers (flippers) or hotel-style operations, not passive landlords.

## Why each non-obvious choice

**Why is this Box 1 (rent) and not 1099-NEC (services)?** Helena is renting property to Cedar & Cloth, not providing services. The payment is for property use, not for personal services.

**What if Helena's office building were owned by an LLC taxed as S-corp?** Then the corporate exemption (Reg. §1.6041-3(c)) would apply to Box 1, and Cedar & Cloth would NOT issue 1099-MISC. Verify entity type from W-9 every year — landlords sometimes change their entity election.

**What if Cedar & Cloth paid Helena via Stripe?** Then Stripe issues 1099-K to Helena, and Cedar & Cloth does NOT issue 1099-MISC for the same payments (anti-double-reporting).

**What if Cedar & Cloth used a property management company that collects rent and remits to Helena?** The PMC is the entity that files 1099-MISC to Helena (the principal). Cedar & Cloth does NOT file 1099-MISC to the PMC (because the PMC isn't earning the rental income; the PMC is a conduit). Cedar & Cloth's payment to the PMC is not 1099-MISC reportable for rent purposes (the PMC's services to Cedar & Cloth might be 1099-NEC reportable separately, depending on entity status).

**Why include account number "CC-LEASE-2026"?** Optional. Useful for the payer's records; useful if Cedar & Cloth had multiple recipient relationships with Helena (e.g., separate sublease for storage).

**What if Helena were a non-resident alien?** Then the payer would need a W-8BEN, not a W-9. The payment may be subject to chapter 3 withholding (typically 30% on US-source rental income, subject to treaty), reported on **Form 1042-S**, not 1099-MISC. Out of scope for this example — but the agent should always check W-9 vs. W-8BEN (a Helena who is a US citizen / resident is W-9; a non-resident alien is W-8BEN).

## What if backup withholding had applied

Suppose Helena never returned a W-9. Cedar & Cloth would:
1. Apply 24% backup withholding on each $1,200 rent payment → $288 withheld
2. Pay Helena $912 net per month, deposit $288 with IRS via EFTPS
3. Annual: $14,400 × 24% = $3,456 withheld
4. File Form 945 by January 31, 2027 reporting $3,456 backup withholding
5. Issue 1099-MISC with Box 1 = $14,400, Box 4 = $3,456
6. Helena reports $14,400 gross rent on Schedule E Line 3, claims $3,456 credit on Form 1040 Line 25b

## Sources cited
- IRS Form 1099-MISC, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/f1099msc.pdf)
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/i1099mec.pdf)
- IRC §6041, §3406
- Reg. §1.6041-3(c) (corporate exemption)
- Reg. §1.469-1T(e)(3) (rental real estate as passive activity)
- IRS Schedule E Part I (Form 1040)
