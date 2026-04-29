# Example: Small Business Issuing 1099-NEC to a Web Designer

A complete walkthrough of issuing Form 1099-NEC for a $3,500 freelance web design payment that crosses the 2026 $2,000 threshold. This is the canonical "small business hiring an individual contractor" pattern.

## The payer

- **Name**: Bright Roast Coffee LLC (single-member LLC taxed as S-corp)
- **EIN**: 87-2143XXX
- **Address**: 412 Lyon St, Asheville, NC 28801
- **Tax year**: 2026 (filing in early 2027)
- **Filing situation**: 4 1099-NECs total + 1 1099-MISC for landlord rent = 5 information returns. Below the 10-form e-filing threshold, but Bright Roast still chose to e-file via IRIS for simplicity.

## The payee

- **Name**: Sam Patel (individual, sole proprietor doing business as "Patel Studio")
- **W-9 status**: Sam returned a signed W-9 to Bright Roast on May 3, 2026, showing:
  - Line 1: Sam Patel
  - Line 2: Patel Studio (DBA)
  - Line 3: Individual / sole proprietor or single-member LLC
  - Line 4 (TIN): SSN 401-XX-XXXX
  - Line 5: 1227 Charlotte St, Asheville, NC 28801
  - Part II: certified, not subject to backup withholding
- **TIN matching**: Bright Roast verified Sam's name + SSN combo via IRS TIN Matching on May 4, 2026. Match confirmed.

## The transactions

| Date | Invoice description | Amount | Payment method |
|------|---------------------|--------|----------------|
| 2026-05-15 | Website redesign — initial 50% retainer | $1,750 | Direct ACH (Bright Roast bank → Sam bank) |
| 2026-07-01 | Website redesign — final 50% on launch | $1,750 | Direct ACH |
| **Total to Sam Patel in 2026** | | **$3,500** | |

No reimbursable expenses. No goods involved (services only). No backup withholding (W-9 valid).

## Decision: 1099-NEC required?

Per the threshold rules:

- Total paid in 2026: $3,500
- 2026 threshold: $2,000 (OBBBA Section 112201)
- $3,500 ≥ $2,000 → **1099-NEC required**

Per payee classification:

- Sam is an Individual / sole proprietor (per W-9 Line 3) → not a corporation → **subject to 1099-NEC**

Per payment channel:

- Payments were direct ACH (bank-to-bank, no third-party payment network in between) → **payer issues 1099-NEC** (no 1099-K from any platform)

**Conclusion**: Bright Roast issues 1099-NEC to Sam.

## The completed 1099-NEC

```
PAYER's name, address, phone:
  Bright Roast Coffee LLC
  412 Lyon St
  Asheville, NC 28801
  (828) 555-0142

PAYER's TIN: 87-2143XXX

RECIPIENT's TIN: XXX-XX-XXXX (truncated on Copy B; full SSN on Copy A)
RECIPIENT's name: Sam Patel
RECIPIENT's address:
  1227 Charlotte St
  Asheville, NC 28801

Account number: BRIGHT-2026-002 (internal; Bright Roast's contractor ID for Sam)

Box 1 — Nonemployee compensation:        $3,500.00
Box 2 — Direct sales of consumer products ≥ $5,000:  ☐ (unchecked)
Box 3 — (reserved):                       (blank)
Box 4 — Federal income tax withheld:      $0.00
Box 5 — State tax withheld:               $0.00
Box 6 — State / Payer's state no.:        NC / 87-2143XXX
Box 7 — State income:                     $3,500.00
```

## Filing checklist

- [x] Recipient Copy B mailed to Sam by January 31, 2027 (postmarked January 24, 2027)
- [x] Copy A filed with IRS via IRIS by January 31, 2027 (submitted January 25, 2027; IRIS confirmation #2027NEC-XXXXXX)
- [x] State copy: NC is a CF/SF participant; IRIS forwarded to NC Department of Revenue automatically
- [x] Records retained: W-9, TIN match confirmation, ACH transaction records, copy of 1099-NEC, IRIS submission ID
- [x] No Form 945 needed (no backup withholding applied)

## Why each non-obvious choice

**Why ACH instead of Stripe / PayPal?** Bright Roast considered paying through Stripe but Sam preferred direct ACH. The choice matters for 1099 reporting: ACH = direct payment = payer's 1099-NEC obligation. Stripe = third-party network = Stripe issues 1099-K, payer doesn't issue 1099-NEC.

**Why TIN match before paying the second invoice?** Bright Roast's policy is to TIN-match every contractor before the first payment. If Sam's W-9 had failed matching, Bright Roast would have requested a corrected W-9 and applied backup withholding on subsequent payments until resolved. In Sam's case, TIN matched on May 4 (before the May 15 first payment), so no backup withholding needed.

**Why include account number?** It's optional, but Bright Roast uses it to track which recipient + which year. If Sam works again in 2027 or other relationships emerge, the account number distinguishes contracts. The IRS doesn't require it, but it's good practice for the payer's records.

**Why NC in Box 6 / Box 7?** Sam is a NC resident performing services in NC. Box 6 carries Bright Roast's NC state ID (their EIN, which they registered with NC for business purposes). Box 7 = the income attributable to NC ($3,500, all of it).

**Why no backup withholding?** Sam's W-9 was valid, TIN matched IRS records, and Sam certified Part II that they're not subject to backup withholding. None of the §3406 conditions apply.

## What if something had been different

**If Sam had been an S-corp**: Bright Roast would have NOT issued 1099-NEC. Corporations are exempt for services (except medical / legal). Bright Roast would still keep the W-9 on file as proof of corporate status.

**If Sam had paid via Stripe instead of ACH**: Stripe would issue 1099-K to Sam (because Sam earned > $600 via Stripe). Bright Roast would NOT issue 1099-NEC for the same payments — that would be double-reporting.

**If Sam had failed TIN matching**: Bright Roast would have:
1. Sent a B-Notice (first or second depending on history) to Sam
2. Started backup withholding 30 business days after sending the first B-Notice if no response
3. Withheld 24% of each subsequent payment
4. Deposited withheld amounts via EFTPS
5. Filed Form 945 by January 31, 2027 reconciling backup withholding
6. Issued 1099-NEC with Box 4 > 0 (the withheld amount)

**If total paid had been $1,800** (below the 2026 $2,000 threshold): no 1099-NEC required. Sam still has to report the $1,800 as income on Sam's Schedule C (income is taxable regardless of 1099 issuance).

**If Bright Roast had paid 12 contractors $3,500 each** in 2026: total information returns = 12 → above the 10-form threshold → e-filing mandatory under TFA 2019 (IRC §6011(e)(2)). Paper filing would trigger penalty.

## Sources cited
- IRS Form 1099-NEC, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/f1099nec.pdf)
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/i1099mec.pdf)
- IRC §6041, §6041A, §3406
- OBBBA Section 112201 (2026 threshold raised to $2,000)
- Reg. §301.6109-4 (TIN truncation on payee statements)
- W-9 Instructions (Reg. §301.6109-1(d)(2))
