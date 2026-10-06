# Example: Single-Member LLC With $1,050,000 Assigned to California ($6,000 LLC Fee Tier)

A single-member California LLC running a SaaS business with $1.5M of gross receipts, of which $1,050,000 is assigned to California. Hits the $1,000,000–$4,999,999 tier ($6,000 fee). The owner expensed $110,000 of equipment under federal §179, which California limits to $25,000 — an owner-level adjustment, not a Form 568 one. The June estimate was too low for this year's fee but met the prior-year safe harbor.

Line numbers are from the 2025 Form 568; math checked in Python.

## The filer

- **LLC name**: Sundial Software LLC
- **Owner / sole member**: Priya Mehta, California resident, San Diego (an individual)
- **Entity**: California-formed LLC, formed March 16, 2020
- **California SOS file number**: `202032109876` (placeholder)
- **FEIN**: 85-1230000 (placeholder)
- **Federal classification**: Disregarded entity (SMLLC default; no Form 8832 / 2553)
- **Taxable year**: 2025 (filing in 2026)
- **Federal Schedule C**: filed with Priya's 2025 Form 1040

## Inputs gathered

### Income (federal Schedule C, line 1)
- Gross receipts: $1,500,000
- Returns/refunds: $0
- COGS: $0 (SaaS subscriptions)

### Where customers receive the benefit
Priya's customers are in many states. Her billing system shows customers with California billing addresses paid **$1,050,000** (70%); out-of-state customers paid $450,000. She runs the business from San Diego.

### Expenses (federal Schedule C)
- Salaries to W-2 employees: $480,000
- Contract labor: $120,000
- Office rent (San Diego coworking): $36,000
- Software & cloud: $84,000
- Professional fees (legal + CPA): $24,000
- Advertising: $48,000
- Travel: $12,000
- Meals (deductible 50% portion): $6,000

### Equipment placed in service in 2025
- 5 laptops @ $4,000 each = $20,000 (used 100% by employees)
- Server hardware: $90,000 (used 100% in business)
- Total equipment: $110,000 (5-year property)

Federal: Priya's CPA elected §179 = $110,000 (2025 federal limit $2,500,000, threshold $4,000,000; 2025 Instructions for Form 4562). Federal Schedule C line 13 includes the $110,000.

California (owner level): §179 limit $25,000 (§179 property $110,000 < $200,000 threshold; 2025 FTB 3885L lines 1 and 3, and FTB 3885A for an individual owner):
- Excess: $110,000 − $25,000 = $85,000, depreciated under MACRS
- MACRS 5-year, half-year convention, Year 1 = 20% × $85,000 = $17,000
- California §179 + MACRS Year 1 = $25,000 + $17,000 = $42,000
- **California depreciation is $68,000 less than federal** ($110,000 − $42,000) → Priya adds $68,000 on Schedule CA (540)

Because Sundial is a disregarded SMLLC below the $3,000,000 test, it files no Schedule B or K, and the depreciation difference lives on Priya's own California return, not on Form 568.

### Prior-year fee
Sundial's 2024 fee was $2,500 (2024 California income in the $500,000–$999,999 tier).

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

Sundial was formed in California and is commercially domiciled there. SMLLC, disregarded for federal, individual owner. Form 568 applies.

### Step 2 — $800 annual tax (FTB 3522)

Paid with Web Pay on April 11, 2025 (due April 15, 2025). Goes on line 8.

### Step 3 — LLC fee tier

Schedule IW assigns receipts item by item. SaaS subscriptions are services/intangibles: assigned to California to the extent the customer receives the benefit in California (R&TC §25136; R&TC §17942(b)(1)(B); 2025 booklet, Schedule IW instructions). Using billing addresses as the location evidence:

- Line 2a (disregarded entity's gross income assigned to California): $1,050,000
- Line 2b (its cost of goods sold): $0
- Line 7: $1,050,000
- Line 17: **$1,050,000**

Tier: $1,000,000–$4,999,999 → **LLC fee = $6,000**

⚠ Boundary: $1,050,000 is only $50,000 above the $1,000,000 boundary. If the California share were under $1,000,000, the fee would be $2,500. Confirm the sourcing evidence before finalizing.

### Step 4 — FTB 3536 (estimated fee)

Priya paid a $2,500 estimate with Web Pay on June 12, 2025 (due June 16, 2025, because June 15 fell on a Sunday), matching the 2024 fee.

The 2025 fee is $6,000, so $3,500 was not paid as an estimate. But the $2,500 paid by the 6th-month date equals the **2024 total fee**, so the 10% estimated-fee penalty does **not** apply (R&TC §17942(d)(2); 2025 FTB 3536 instructions).

The $3,500 balance is due by the return's original due date, April 15, 2026, on FTB 3536. Priya pays it with Web Pay (estimated LLC fee payment type) on April 10, 2026, before e-filing. Paid on time → no late-payment penalty or interest.

(Had she paid nothing in June, the penalty would have been 10% × $6,000 = $600.)

### Step 5 — Filing deadline

SMLLC owned by an individual → **April 15, 2026**; automatic 6-month extension to October 15, 2026 (the fee balance stays due April 15).

### Step 6 — Schedule B and Schedule K

Not required: Schedule C gross receipts ($1,500,000) are below the $3,000,000 test. Schedules L, M-1, M-2 are not part of a disregarded SMLLC's required sides (Sides 1, 2, 3, 7). No Schedule K-1 (568).

### Step 7 — Schedule R

Sundial has income from customers inside and outside California. The FTB LLC page says to use Schedule R in that situation, so Question M(1) is "Yes" and Schedule R is attached, showing California sales of $1,050,000 of $1,500,000 (70.00%). Schedule R does not change Schedule IW, which already assigned receipts item by item.

### Step 8 — Nonresident members

Priya is the sole member and a California resident; she signs the Single Member LLC Information and Consent on Side 3. No FTB 3832, no Schedule T, no withholding.

### Step 9 — Compute the bottom line

```
Line 1  (Total income from Schedule IW):      $1,050,000
Line 2  (LLC fee, $1M–$4,999,999 tier):           $6,000
Line 3  (2025 annual LLC tax):                       $800
Line 4  (PTE elective tax):                            $0
Line 5  (Nonconsenting nonresident tax):               $0
Line 6  (Partnership level tax):                   (blank)
Line 7  (Total tax and fee):                       $6,800
Line 8  (FTB 3522 $800 + 3536 $2,500 + 3536 $3,500): $6,800
Line 12 (Total payments):                          $6,800
Line 14 (Payments balance):                        $6,800
Line 16 (Tax and fee due):                             $0
Line 17 (Overpayment):                                 $0
Line 20 (Penalties and interest):                      $0
Line 21 (Total amount due):                            $0
```

### Step 10 — Validation

- ☑ Math: Line 7 = $6,000 + $800 + $0 + $0 + $0 = $6,800. Line 8 = $800 + $2,500 + $3,500 = $6,800. Line 16 = $0. Pass.
- ☑ Math: Schedule IW line 17 = $1,050,000 = line 1; $1,050,000 / $1,500,000 = 70.00%. Pass.
- ☑ Sanity: Estimate $2,500 < 2025 fee $6,000, but ≥ 2024 fee $2,500 → no §17942(d)(2) penalty.
- ⚠ Sanity: line 1 within $50,000 of the $1,000,000 boundary → sourcing records must support $1,050,000.
- ☑ Sanity: federal §179 $110,000 > $25,000 → owner-level California adjustment ($68,000) flagged for Schedule CA (540).

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for taxable year 2025

## Identification (Side 1)
A. SOS file number:                     202032109876
B. FEIN:                                85-1230000
E. Accounting method:                   Accrual
F. Date business started in CA:         03/16/2020
G. Total assets EOY:                    not required (disregarded SMLLC below the $3M test)
H. Boxes checked:                       none
I(1)–I(3):                              No / No / No

## Side 1 — Tax, fee, and payments
Line 1.  Total income from Schedule IW:          $1,050,000
Line 2.  LLC fee:                                $6,000
Line 3.  Annual LLC tax:                         $800
Line 4.  PTE elective tax:                       $0
Line 5.  Nonconsenting nonresident tax:          $0
Line 6.  Partnership level tax:                  (blank)
Line 7.  Total tax and fee:                      $6,800
Line 8.  Paid with FTB 3537 / 3522 / 3536:       $6,800
Line 9.  PTE elective tax payments:              $0
Line 10. Prior-year overpayment credited:        $0
Line 11. Withholding:                            $0
Line 12. Total payments:                         $6,800
Line 13. Use tax:                                $0
Line 14. Payments balance:                       $6,800
Line 15. Use tax balance:                        $0
Line 16. Tax and fee due:                        $0
Line 17. Overpayment:                            $0
Line 18. Credited to 2026:                       $0
Line 19. Refund:                                 $0
Line 20. Penalties and interest:                 $0
Line 21. Total amount due:                       $0

## Questions (Side 2–3)
J. PBA code / activity / product:   513210 / Software publishing / B2B SaaS subscriptions
K. Maximum members:                 1
M(1) Schedule R:                    Yes
P(1)/P(2) nonresident members:      No / No
U(1) Disregarded:                   Yes    U(2): No    U(3): Yes ($1,050,000 CA < $1,500,000 total)
GG(2) First year doing business in CA: No
SMLLC owner type:                   Individual (Priya Mehta), consent signed

## Schedule IW
1a $0 · 1b $0 · 2a $1,050,000 · 2b $0 · 3a–6 $0 · 7 $1,050,000 · 8a–16 $0
17 $1,050,000 → Side 1, line 1

## Schedule R (single sales factor)
Total sales (everywhere):       $1,500,000
California sales:               $1,050,000
California factor:              70.00%

## Owner-level California adjustment (Priya's Schedule CA (540), via FTB 3885A — not on Form 568)
| Item | Federal Schedule C | California | Difference |
|------|--------------------|------------|------------|
| §179 + Year 1 MACRS on $110,000 of equipment | $110,000 | $42,000 ($25,000 + 20% × $85,000) | $68,000 less California depreciation |

## Member info (1 member, CA resident)
| Name | TIN | % | CA resident | Consent |
|------|-----|---|-------------|---------|
| Priya Mehta | XXX-XX-XXXX | 100 | Yes | Side 3 SMLLC consent signed |

## Payments and attachments
- [x] 2025 FTB 3522 ($800) — Web Pay, April 11, 2025
- [x] 2025 FTB 3536 ($2,500 estimate) — Web Pay, June 12, 2025 (= 2024 fee; safe harbor met)
- [x] 2025 FTB 3536 ($3,500 balance) — Web Pay, April 10, 2026 (by the original due date)
- [ ] FTB 3832 — not applicable (single-member LLC)
- [ ] Form 592-Q / 592-PTE / 592-B — not applicable
- [x] Schedule R (70% California)

## Validation summary
- Math: all checks passed
- Sanity:
  - Estimate below this year's fee but at least last year's fee → no 10% penalty
  - Line 1 is $50,000 above the $1,000,000 boundary → keep the billing-address report
  - $68,000 California depreciation difference flagged for Priya's own return
- Next steps:
  - 2026 FTB 3522 ($800) due April 15, 2026
  - 2026 FTB 3536 estimate due June 15, 2026 — paying at least $6,000 (the 2025 fee) by then avoids the penalty
  - 2025 Form 568 due April 15, 2026 (October 15, 2026 on extension)

## Sources cited in this draft
- 2025 Form 568 and 2025 Form 568 Booklet (Filing Requirements for Disregarded Entities; Schedule IW instructions; General Information E, F)
- 2025 FTB 3536 instructions; FTB LLC page (Schedule R)
- 2025 FTB 3885L / 3885A (§179 $25,000 / $200,000); 2025 Instructions for Form 4562
- R&TC §17941; §17942(a)(3), (b)(1)(B), (d)(2); §25128.7; §25136
```

## Why each non-obvious choice

**Why is the California depreciation difference $68,000?** Federal allowed the full $110,000 under §179; California allows $25,000 plus 20% MACRS Year 1 on the $85,000 excess = $42,000. Difference: $68,000. For a disregarded SMLLC owned by an individual below the $3,000,000 test, this is reported on the owner's California return (Schedule CA (540), FTB 3885A), not on Form 568.

**Why is line 1 $1,050,000 and not 70% of something?** Schedule IW assigns each receipt to the location where the customer receives the benefit (R&TC §§17942(b)(1)(B), 25136). Here the assigned receipts happen to equal 70% of total receipts; the 70% factor on Schedule R is a result, not the method.

**Why no estimated-fee penalty even though the estimate was $3,500 short?** R&TC §17942(d)(2): no penalty if the amount paid by the 15th day of the 6th month is at least the LLC's total fee for the preceding taxable year. Priya paid $2,500 = the 2024 fee.

**Why pay the $3,500 on FTB 3536 rather than with the return?** The booklet says the LLC uses FTB 3536 to pay, by the return's due date, any fee not paid as a timely estimate. Paying it before filing puts it on line 8; paying it with the return instead would show it on line 16 / 21. Either way it must be paid by April 15, 2026.

**Why no Schedule L?** A disregarded SMLLC completes Sides 1, 2, 3, and 7 (plus Schedules B and K only at $3,000,000); Schedules L, M-1, and M-2 are not in that list (2025 booklet, Filing Requirements for Disregarded Entities).

**What if Priya had a co-investor in Wyoming?** Then the LLC would be multi-member and partnership-classified. The Wyoming member signs FTB 3832, or the LLC pays Schedule T tax at 12.3% on that member's distributive share; separately, distributions of California-source income to that member above $1,500 in a calendar year require 7% withholding (Form 592-Q / 592-PTE / 592-B). See [`nonresident-members.md`](../references/nonresident-members.md).

## Audit defense

Priya's 568 audit defense:
1. SOS confirms LLC formation
2. Federal Schedule C cross-references gross receipts
3. Customer-location records (billing addresses by invoice) support the $1,050,000 assigned to California
4. FTB 3536 payment history shows $2,500 by June 16, 2025 and $3,500 by April 15, 2026
5. The 2024 Form 568 shows the $2,500 prior-year fee behind the safe harbor

The fragile piece is the sourcing — Priya should keep an exportable customer-location report. It is the evidence for line 1, and line 1 sits close to the $1,000,000 boundary between the $2,500 and $6,000 tiers.
