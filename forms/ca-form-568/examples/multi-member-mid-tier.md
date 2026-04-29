# Example: Two-Member LLC at $400K Gross Receipts ($900 LLC Fee Tier)

A two-member California LLC operating a marketing agency, partnership-classified federally. Hits the first non-zero LLC fee tier ($250K-$499,999 → $900 fee). Includes both members as California residents (no nonresident complexity), so this is a clean mid-tier example.

## The filers

- **LLC name**: Pacific Marketing Partners LLC
- **Members**: Jordan Reyes (60%, CA resident, San Francisco) and Sam Ortiz (40%, CA resident, Los Angeles)
- **Entity**: California-formed LLC, formed January 2022 (so AB-85 exemption was used in year 1 — but irrelevant for 2024 filing)
- **California SOS file number**: `202206543210`
- **Federal EIN**: 87-9876543
- **Federal classification**: Partnership (default for multi-member; no Form 8832 / 2553 filed)
- **Tax year**: 2024 (filing in 2025)
- **Federal Form 1065 already filed** by March 15, 2025

## Inputs gathered

### Income (federal Form 1065 already drafted)
- Gross receipts: $400,000
- COGS: $0 (service business)
- Other income (interest on business savings): $1,200
- Total federal income (Form 1065 Line 8): $401,200

### Expenses (federal Form 1065)
- Salaries to subcontractors: $90,000
- Office rent: $24,000
- Software subscriptions: $18,000
- Professional fees: $12,000
- Travel and meals (50% deductible): $6,000
- Equipment depreciation (federal §179 = $40,000 on a $40,000 server purchase, full federal §179): $40,000
- Other operating expenses: $35,000
- Total federal deductions (1065 Line 21): $225,000
- Federal ordinary income (1065 Line 22): $401,200 − $225,000 = $176,200

### California-source: 100% (single-state operation)

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

Pacific Marketing Partners formed in California → automatic Form 568 obligation. Multi-member, partnership-classified → Form 568 (not 100/100S).

### Step 2 — Pay or confirm $800 annual tax (Form 3522)

LLC paid $800 via Form 3522 on April 10, 2024 (timely). Will record on Line 7.

### Step 3 — Determine if the LLC fee applies

Schedule IW Total Income = $400,000 (gross receipts; service business, COGS = $0; plus interest income).

Actually, the §17942 definition is gross receipts + COGS, so:
- Schedule IW Line 1 (gross receipts): $400,000
- Schedule IW Line 2 (COGS): $0
- Schedule IW Line 4 (other income): $1,200
- Total: $401,200

Tier: $250,000-$499,999 → **LLC fee = $900**

(Note: the additional $1,200 in interest income doesn't push the LLC above $500K; tier remains the same.)

### Step 4 — Pay or confirm Form 3536

LLC paid Form 3536 on June 14, 2024 (timely). Estimated fee was $900 (matched 2023 actual). Will record on Line 8.

This estimate happens to be exactly right since 2024 actual fee is also $900 → no underpayment, no penalty.

### Step 5 — Filing deadline

Multi-member, partnership-classified → Form 568 due **March 15, 2025** for tax year 2024 (matches federal Form 1065).

### Step 6 — Schedule K and member K-1s

#### California adjustments to federal income

| Item | Federal | California | Adjustment |
|------|---------|------------|------------|
| Federal ordinary income | $176,200 | -- | -- |
| §179 deduction over $25K cap | $40,000 | $25,000 + ($15,000 × 20% MACRS Year 1 = $3,000) = $28,000 | Add back $40,000 − $28,000 = **$12,000** |
| §168(k) bonus depreciation | $0 (already fully §179'd) | $0 | None |
| §163(j) interest cap | not triggered | -- | -- |
| §199A QBI | (at member level on 1040, not 1065) | -- | -- |

California adjusted ordinary income: $176,200 + $12,000 add-back = **$188,200**

#### Schedule K (568) totals

| K Line | Item | Amount |
|--------|------|--------|
| 1 | Ordinary business income | $188,200 (after CA adjustment) |
| 5 | Interest income | $1,200 |
| ... | (other lines $0) | -- |
| 12 | §179 deduction | $25,000 (CA cap) |
| ... | (other deductions $0) | -- |

#### K-1 (568) per member

Jordan Reyes (60%):
- Ordinary income share: $112,920
- Interest share: $720
- §179 share: $15,000

Sam Ortiz (40%):
- Ordinary income share: $75,280
- Interest share: $480
- §179 share: $10,000

### Step 7 — Apportionment

100% California-source. No Schedule R required.

### Step 8 — Nonresident members

Both Jordan and Sam are California residents. No Form 3832, no Form 592 needed. Schedule T not required.

### Step 9 — Compute the bottom line

```
Form 568 Line 1 (Total income from Schedule IW):  $401,200
Form 568 Line 2 (LLC fee, $250K-$499,999 tier):   $900
Form 568 Line 3 (2024 annual LLC tax):            $800
Form 568 Line 4 (nonresident tax):                $0
Form 568 Line 5 (partnership-level tax):          $0
Form 568 Line 6 (Total tax and fee):              $1,700
Form 568 Line 7 (Form 3522 prepaid):              $800
Form 568 Line 8 (Form 3536 prepaid):              $900
Form 568 Line 11 (Total payments):                $1,700
Form 568 Line 12 (Tax/fee due or overpayment):    $0
```

### Step 10 — Validation

- ☑ Math: Line 6 = $0 + $800 + $0 + $0... wait, Line 2 is $900. So Line 6 = $900 + $800 + $0 + $0 = $1,700. Pass.
- ☑ Math: Schedule IW total = $401,200; flows to Line 1. Pass.
- ☑ Math: Member K-1 shares sum to Schedule K totals. Jordan 60% + Sam 40% = 100%. Ordinary $112,920 + $75,280 = $188,200. Pass.
- ☑ Sanity: Schedule IW total $401,200 is well within $250K-$499K tier (no boundary risk).
- ☑ Sanity: §179 add-back of $12,000 documented; matches MACRS Year 1 calculation.

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for tax year 2024

## LLC identification
A. SOS file number:                       202206543210
B. Federal EIN:                           87-9876543
C. Principal business activity:           Marketing agency
D. Principal product/service:             Brand strategy and digital marketing
E. Date business started in CA:           01/15/2022
F. Total assets EOY:                      $58,000
G. Sales:                                 $400,000
H. Boxes checked:                         [none — not initial / final / amended]
I. Number of members:                     2
J. Federal classification election:       N/A (partnership default)

## Side 1 — Tax and Fee
Line 1.  Total income (from Sched IW):                $401,200
Line 2.  LLC fee ($250K-$499K tier):                    $900
Line 3.  2024 annual LLC tax:                           $800
Line 4.  Nonconsenting nonresident tax:                   $0
Line 5.  Partnership-level tax:                           $0
Line 6.  Total tax and fee:                           $1,700

## Side 1 — Payments
Line 7.  Form 3522 ($800) prepaid:                      $800
Line 8.  Form 3536 prepaid:                             $900
Line 9.  Withholding:                                     $0
Line 10. Prior-year overpayment applied:                  $0
Line 11. Total payments:                              $1,700
Line 12. Tax/fee due or overpayment:                      $0

## Schedule IW — Income Worksheet
IW Line 1. Gross receipts (CA-source):              $400,000
IW Line 2. Cost of goods sold (CA):                       $0
IW Line 3. Subtract Line 2 from 1:                  $400,000
IW Line 4. Other income (interest):                   $1,200
IW Line 7. Total → Form 568 Line 1:                 $401,200

## Schedule K (568) summary
| K Line | Item | Federal | CA Adjustment | CA Total |
|--------|------|---------|---------------|----------|
| 1 | Ordinary business income | $176,200 | +$12,000 (§179 add-back) | $188,200 |
| 5 | Interest income | $1,200 | -- | $1,200 |
| 12 | §179 deduction | $40,000 | -$15,000 (CA cap) | $25,000 |

## Schedule K-1 (568) per member
| Member | SSN | % | Ordinary income | Interest | §179 | CA resident | Form 3832 |
|--------|-----|---|-----------------|----------|------|-------------|-----------|
| Jordan Reyes | XXX-XX-XXXX | 60 | $112,920 | $720 | $15,000 | Yes | N/A |
| Sam Ortiz    | XXX-XX-XXXX | 40 | $75,280  | $480 | $10,000 | Yes | N/A |

## Required attachments
- [x] Form 3522 ($800 paid April 10, 2024)
- [x] Form 3536 ($900 paid June 14, 2024)
- [ ] Form 3832 (not applicable; both members are CA residents)
- [ ] Form 592 / 592-B (not applicable; no nonresident members)
- [ ] Schedule R (not applicable; 100% CA-source)
- [x] Federal Form 1065 + Schedule K-1s (filed by March 15, 2025)
- [ ] Schedule L, M-1, M-2 (not required: receipts ≥ $250K but assets < $1M; verify which threshold applies — under 2024 instructions, receipts ≥ $250K triggers L, so include)

## Validation summary
- Math: all checks passed
- Sanity:
  - §179 add-back of $12,000 documented
  - All members CA residents → no nonresident complexity
  - Schedule IW within tier ($401,200 < $500K boundary)
- Next steps:
  - Each member files California Schedule CA(540) reflecting their K-1 (568) share
  - Members claim §179 deductions per their share on their personal returns
  - 2025 Form 3522 ($800) due April 15, 2025
  - 2025 Form 3536 (estimated fee) due June 15, 2025 — recommend $900 again unless revenue is on a clear growth path
  - 2025 Form 568 due March 15, 2026

## Sources cited in this draft
- California Form 568, Rev. 2024
- California Form 568 Booklet, Rev. 2024
- R&TC §17941 (annual LLC tax)
- R&TC §17942(a)(1) (LLC fee, $250K-$499K tier = $900)
- R&TC §17255 (California §179 cap = $25,000)
- R&TC §17024 (California IRC conformity, including non-conformity to §168(k))
```

## Why each non-obvious choice

**Why does the §179 limit hit $25,000 instead of federal $1,250,000?** California explicitly does not conform to federal §179 expansion. The $25,000 cap has been in place under R&TC §17255 / §24356. The $15,000 excess is depreciated under MACRS over the asset's useful life (5 years for typical equipment).

**Why is the LLC fee $900 and not $0?** Schedule IW Total Income ($401,200) exceeds $250,000. The tier table jumps from $0 to $900 at $250K. Pacific Marketing Partners is squarely in that tier.

**What if Jordan moved to Texas mid-year?** This is the "year of partial residency" complication. Generally, if a member is a California resident at any point during the year and has California-source income, they're treated as a California resident for that income. Mid-year moves require pro-rata allocation between the resident and nonresident period. Out of scope for this skill — flag and consult a CPA.

**Why is interest income $1,200 included in Schedule IW?** Schedule IW captures all California-source income, not just operating revenue. Interest on a business savings account is California-source if the LLC is doing business in California. Add it.

**Why no Schedule R?** Single-state operation. Schedule R applies only when income must be apportioned across states.

## Audit defense

The LLC's audit defense:
1. SOS confirms California formation
2. Federal Form 1065 cross-references all income
3. §179 add-back documented; matches MACRS Year 1 on $15,000 excess
4. Schedule IW computed using gross-receipts-plus-COGS (or equivalent for service business)
5. Both members CA residents — no Form 3832 needed
6. Form 3522 + 3536 timely paid; Form 568 timely filed

This is a clean mid-tier filing. The most fragile piece is the §179 add-back computation — keep the MACRS schedule for Year 1 onwards in the audit file.
