# Example: Single-Member LLC at $1.5M Gross Receipts ($6,000 LLC Fee Tier)

A single-member California LLC running a SaaS-services business with $1.5M in California-source gross receipts. Hits the $1M-$4,999,999 tier ($6,000 fee). The owner used federal §168(k) bonus depreciation, which California doesn't allow → significant add-back.

This example shows how the §168(k) and §179 California adjustments work in practice when the dollar amounts are large enough to matter.

## The filer

- **LLC name**: Sundial Software LLC
- **Owner / sole member**: Priya Mehta, California resident, San Diego
- **Entity**: California-formed LLC, formed March 2020
- **California SOS file number**: `202032109876`
- **Federal EIN**: 85-1230000
- **Federal classification**: Disregarded entity (SMLLC default; no Form 8832 / 2553)
- **Tax year**: 2024 (filing in 2025)
- **Federal Schedule C**: filed with Priya's 1040 by April 15, 2025

## Inputs gathered

### Income (federal Schedule C, Line 1)
- Gross receipts: $1,500,000
- Returns/refunds: $0
- COGS: $0 (SaaS service business)
- Other income (business interest): $4,500

Federal gross income (Schedule C Line 7): $1,504,500

### Expenses (federal Schedule C)
- Salaries to W-2 employees: $480,000
- Subcontractors / contract labor: $120,000
- Office rent (San Diego coworking): $36,000
- Software & cloud (AWS, Stripe, etc.): $84,000
- Professional fees (legal + CPA): $24,000
- Marketing / advertising: $48,000
- Travel: $12,000
- Meals (50%): $6,000

### Equipment purchased in 2024
- 5 high-end MacBooks @ $4,000 each = $20,000 (used 100% by employees)
- Server farm hardware: $90,000 (used 100% in business)
- Total equipment: $110,000

Priya's CPA elected on federal:
- §179: $25,000 (max federal allowed within taxable income limits — actually federal limit is $1.25M, so this is artificially low; revising)

Let's correct that: Priya's CPA elected federal §179 = $110,000 (full amount, since federal §179 cap is $1.25M for 2024 and she's well within it). Federal Schedule C Line 13 = $110,000.

For California:
- §179 cap: $25,000 (R&TC §17255)
- Excess: $110,000 − $25,000 = $85,000
- This $85,000 must be depreciated under MACRS for California purposes
- MACRS 5-year half-year convention Year 1 = 20% × $85,000 = $17,000
- California §179 + MACRS Year 1 on excess = $25,000 + $17,000 = $42,000
- **California §179 add-back** = $110,000 (federal) − $42,000 (California) = **$68,000**

### Additional 2024 expense: Federal §168(k) bonus depreciation

Priya's CPA also elected $0 of bonus depreciation since the §179 already took the full $110K. **Skip add-back.**

But if the CPA had taken §179 = $25,000 + §168(k) bonus = $85,000 (separate strategy), the federal numbers would have been the same but California would still allow only $25K + MACRS on $85K = $42K. Same result, different mechanic.

For this example: federal Schedule C Line 13 = $110,000 (all §179). California Schedule K equivalent = $42,000. Add-back $68,000.

### Federal §163(j) interest cap
Sundial has minimal business interest ($1,200 on a credit card). §163(j) doesn't trigger. No California adjustment.

### California-source: 100%
Priya's customers are global (SaaS), but the business is operated entirely from California. Under R&TC §25136(b) (market-based sourcing for services), customers receive the benefit at their location. So Schedule R apportionment is technically required.

For this example, assume **70% of customers are in California, 30% out-of-state**. Schedule R apportionment:
- California sales: $1,050,000 (70% of $1,500,000)
- Total sales: $1,500,000
- California % = 70%
- Schedule IW Total Income = 70% × $1,504,500 = **$1,053,150**

Tier: $1,000,000-$4,999,999 → **LLC fee = $6,000**

> Note: this assumes Schedule R apportionment applies to a SMLLC with disregarded federal status. In practice, the apportionment is done at the parent level (Priya's 1040 / Schedule C), and the Schedule IW for fee purposes uses California-source revenue. Because Priya is a CA resident, there are nuances about whether her California residency means 100% of the LLC's income is CA-source for personal income tax. For the **fee** computation under §17942, the apportionment to California-source applies. Out of scope for this skill: edge cases around CA-resident sole owners with multi-state-customer SMLLCs — redirect to a CPA for definitive treatment.

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

Sundial formed in California. SMLLC, disregarded for federal. Priya is the only member, CA resident. Form 568 applies.

### Step 2 — $800 annual tax (Form 3522)

Paid April 12, 2024. Record on Line 7.

### Step 3 — LLC fee tier

Schedule IW Total Income = $1,053,150 → tier $1M-$4,999,999 → **LLC fee = $6,000**.

### Step 4 — Form 3536 (estimated fee)

Priya's 2023 fee was $2,500 ($500K-$999K tier). She paid Form 3536 for 2024 = $2,500 by June 14, 2024.

But 2024 actual fee = $6,000. Underpayment = $6,000 − $2,500 = $3,500.

R&TC §17942(d) penalty = 10% × $3,500 = **$350**.

Add to Form 568 as part of penalties (calculated separately, not on Line 6).

### Step 5 — Filing deadline

SMLLC → Form 568 due **April 15, 2025** for tax year 2024.

### Step 6 — Schedule K (not applicable for SMLLC)

SMLLC is disregarded; Schedule K is for partnership-classified LLCs. Skip.

### Step 7 — Apportionment (Schedule R)

Required: 70/30 split (CA / non-CA). Schedule R attached.

### Step 8 — Nonresident members

Priya is the sole member and CA resident. No Form 3832, no Form 592.

### Step 9 — Compute the bottom line

```
Form 568 Line 1 (Total income from Sched IW after R apportionment): $1,053,150
Form 568 Line 2 (LLC fee, $1M-$4.99M tier):                         $6,000
Form 568 Line 3 (2024 annual LLC tax):                                $800
Form 568 Line 4 (nonresident tax):                                      $0
Form 568 Line 5 (partnership-level tax):                                $0
Form 568 Line 6 (Total tax and fee):                                $6,800

Form 568 Line 7 (Form 3522 prepaid):                                  $800
Form 568 Line 8 (Form 3536 prepaid):                                $2,500
Form 568 Line 11 (Total payments):                                  $3,300

Form 568 Line 12 (Balance due before penalty):                      $3,500
Plus §17942(d) underestimation penalty (10% × $3,500):                $350
Plus interest on $3,500 from June 15, 2024 to filing date:           ~$XX
Total amount due with return:                                      ~$3,850+
```

Priya owes ~$3,850 with the Form 568 return on April 15, 2025.

### Step 10 — Validation

- ☑ Math: Line 6 = $0 + $800 + $0 + $0 + $6,000 = $6,800. Pass.
- ☑ Math: Schedule IW = 70% × $1,504,500 = $1,053,150. Pass.
- ☑ Math: Schedule R apportionment 1,050,000 / 1,500,000 = 70%. Pass.
- ☑ Sanity: §179 add-back of $68,000 documented. MACRS Year 1 schedule retained.
- ⚠ Sanity: Form 3536 underestimated → 10% penalty applies. Document.
- ☑ Sanity: Schedule R attached (multi-state apportionment).

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for tax year 2024

## LLC identification
A. SOS file number:                     202032109876
B. Federal EIN:                         85-1230000
C. Principal business activity:         SaaS / software services
D. Principal product/service:           B2B SaaS subscriptions
E. Date business started in CA:         03/15/2020
F. Total assets EOY:                    $290,000
G. Sales:                               $1,500,000
H. Boxes checked:                       [X] Single-member LLC
I. Number of members:                   1
J. Federal classification election:     N/A (disregarded entity, default)

## Side 1 — Tax and Fee
Line 1.  Total income (from Sched IW):                  $1,053,150
Line 2.  LLC fee ($1M-$4.99M tier):                     $6,000
Line 3.  2024 annual LLC tax:                           $800
Line 4.  Nonconsenting nonresident tax:                 $0
Line 5.  Partnership-level tax:                         $0
Line 6.  Total tax and fee:                             $6,800

## Side 1 — Payments
Line 7.  Form 3522 ($800) prepaid:                      $800
Line 8.  Form 3536 prepaid (underestimated):            $2,500
Line 9.  Withholding:                                   $0
Line 10. Prior-year overpayment applied:                $0
Line 11. Total payments:                                $3,300
Line 12. Balance due:                                   $3,500

(Plus $350 §17942(d) underestimation penalty + interest, paid separately)

## Schedule IW — Income Worksheet (after Schedule R apportionment)
IW Line 1. Gross receipts (CA-apportioned):             $1,050,000
IW Line 2. Cost of goods sold (CA):                     $0
IW Line 3. Subtract Line 2 from 1:                      $1,050,000
IW Line 4. Other income (interest, CA-apportioned 70%): $3,150
IW Line 7. Total → Form 568 Line 1:                     $1,053,150

## Schedule R — Apportionment (single-sales-factor)
Total sales (everywhere):                                $1,500,000
California sales:                                        $1,050,000
California apportionment %:                              70.00%

## Federal-to-California adjustments (relevant for Priya's 540 / Schedule CA)
| Item | Federal Schedule C | CA-equivalent | Add-back |
|------|--------------------|---------------| ---------|
| §179 | $110,000 | $42,000 (= $25K cap + 20% MACRS Yr1 on $85K) | $68,000 |
| §168(k) | $0 | $0 | $0 |

## Member info (1 member, sole CA resident)
| Name | SSN | % | CA resident | Form 3832 |
|------|-----|---|-------------|-----------|
| Priya Mehta | XXX-XX-XXXX | 100 | Yes | N/A |

## Required attachments
- [x] Form 3522 ($800 paid April 12, 2024)
- [x] Form 3536 ($2,500 paid June 14, 2024 — UNDERESTIMATED, $350 penalty)
- [ ] Form 3832 (N/A; sole member is CA resident)
- [ ] Form 592 / 592-B (N/A; no nonresident members)
- [x] Schedule R (multi-state apportionment, 70% CA)
- [x] Federal Schedule C (filed with Priya's 1040)
- [x] Schedule L, M-1, M-2 (receipts ≥ $250K → required)

## Validation summary
- Math: all checks passed
- Sanity:
  - §179 add-back of $68,000 documented
  - Schedule R apportionment 70% / 30% based on customer location
  - Form 3536 underestimated → 10% penalty applies (~$350)
  - Schedule L, M-1, M-2 required (receipts ≥ $250K)
- Next steps:
  - Pay $3,500 balance + $350 penalty + interest by April 15, 2025
  - 2025 Form 3522 ($800) due April 15, 2025 — Priya should pay simultaneously
  - 2025 Form 3536 estimate: based on growth, recommend $11,790 (next-tier-up cushion) by June 15, 2025
  - 2025 Form 568 due April 15, 2026
  - On 1040: Priya reports federal Schedule C income; California Schedule CA(540) adjusts for §179 and bonus depreciation differences

## Sources cited in this draft
- California Form 568, Rev. 2024
- California Form 568 Booklet, Rev. 2024
- R&TC §17941 (annual LLC tax)
- R&TC §17942(a)(3) (LLC fee, $1M-$4.99M tier = $6,000)
- R&TC §17942(d) (estimated fee underpayment penalty, 10%)
- R&TC §17255 (California §179 cap = $25,000)
- R&TC §25128.7 (single-sales-factor apportionment)
- R&TC §25136(b) (market-based sourcing for services)
```

## Why each non-obvious choice

**Why is the §179 add-back $68,000 specifically?** Federal allowed full $110K; California allows $25K + MACRS Year 1 on $85K excess = $25K + $17K = $42K. Difference: $68K.

**Why does Schedule R apply to a SMLLC?** Even disregarded entities apportion when they have multi-state customers. The apportionment determines the California-source share for the **§17942 fee** (and ultimately for Priya's California personal income tax).

**Why was the Form 3536 underestimated?** Priya assumed 2024 would track 2023 ($500K-$999K tier, $2,500 fee). Revenue grew faster than expected to $1.5M, pushing into the $1M-$4.99M tier ($6,000 fee). The estimate cushion should have been at the next-tier rate.

**Why is the 10% §17942(d) penalty $350 and not 10% of $6,000?** The penalty is 10% of the **underpayment**, not of the actual fee. Underpayment = $6,000 − $2,500 = $3,500. 10% × $3,500 = $350.

**What if Priya had been more conservative on §179?** If she had taken federal §179 = $25,000 (matching California cap) and MACRS depreciated the rest, federal Schedule C net income would have been higher (worse federally) but no California add-back. Trade-off depends on Priya's federal vs. California marginal rates. The CPA optimized for federal.

**Why no Schedule T?** Priya is the sole member and a CA resident. No nonresident, no consent issue.

**What if Priya had a co-investor in Wyoming?** Then the LLC would be multi-member, partnership-classified, and the Wyoming co-investor would need Form 3832 OR the LLC would withhold 7% per Form 592. Schedule T would compute additional tax for the LLC. See [`nonresident-members.md`](../references/nonresident-members.md).

## Audit defense

Priya's 568 audit defense:
1. SOS confirms LLC formation
2. Federal Schedule C cross-references all income and expense
3. Schedule R apportionment supported by customer-location records (Stripe charge addresses, billing systems)
4. §179 add-back documented with MACRS Year 1 schedule
5. Form 3522 + Form 3536 (with penalty paid) timely
6. Schedule L balance sheet reconciles with bank records

The fragile piece is Schedule R apportionment — Priya should keep an exportable customer-location report showing the 70/30 California / non-California split. Without it, FTB could challenge the apportionment and assess the higher fee on a 100% California basis.
