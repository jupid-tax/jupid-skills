# Example: Two-Member LLC at $401,200 of California Income ($900 LLC Fee Tier)

A two-member California LLC operating a marketing agency, partnership-classified federally. Hits the first non-zero LLC fee tier ($250,000–$499,999 → $900 fee). Both members are California residents (no nonresident complexity), so this is a clean mid-tier example. Line numbers are from the 2025 Form 568 and 2025 Form 1065; math checked in Python.

## The filers

- **LLC name**: Pacific Marketing Partners LLC
- **Members**: Jordan Reyes (60%, CA resident, San Francisco) and Sam Ortiz (40%, CA resident, Los Angeles)
- **Entity**: California-formed LLC, formed January 15, 2022 (its first taxable year fell in the AB 85 window — irrelevant for 2025)
- **California SOS file number**: `202206543210` (placeholder)
- **FEIN**: 87-9876543 (placeholder)
- **Federal classification**: Partnership (default for multi-member; no Form 8832 / 2553 filed)
- **Taxable year**: 2025 (filing in 2026)
- **Federal Form 1065**: drafted; due March 16, 2026

## Inputs gathered

### Income (federal Form 1065)
- Gross receipts: $400,000
- COGS: $0 (service business)
- Interest on the business savings account: $1,200 (portfolio income, federal Schedule K line 5 — not in ordinary income)

### Expenses (federal Form 1065 page 1)
- Contract labor (subcontractors): $90,000
- Office rent: $24,000
- Software subscriptions: $18,000
- Professional fees: $12,000
- Meals (deductible 50% portion): $6,000
- Other operating expenses: $35,000
- Total deductions (Form 1065, line 22): $185,000
- Ordinary business income (Form 1065, line 23): $400,000 − $185,000 = **$215,000**

### Equipment
- Server purchased and placed in service in 2025: $40,000 (5-year property). Federal §179 election = $40,000 (2025 federal limit $2,500,000; 2025 Instructions for Form 4562). §179 is separately stated on federal Schedule K line 12, not deducted in ordinary income.

### California-source: 100% (business wholly within California)

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

Pacific Marketing Partners was formed in California → Form 568 obligation. Multi-member, partnership-classified → Form 568 (not 100/100S).

### Step 2 — Pay or confirm $800 annual tax (FTB 3522)

LLC paid the 2025 $800 with Web Pay on April 10, 2025 (due April 15, 2025). Goes on line 8.

### Step 3 — Determine if the LLC fee applies

Schedule IW (all California):
- Line 1a (Schedule B line 3, gross profit): $400,000
- Line 1b (cost of goods sold): $0
- Line 7 (subtotal): $400,000
- Line 10 (California interest, Schedule K line 5): $1,200
- Line 17 (total California income): **$401,200**

Tier: $250,000–$499,999 → **LLC fee = $900**

(The $1,200 of interest counts toward line 17 but doesn't move the tier.)

### Step 4 — Pay or confirm FTB 3536

The 2024 fee was $900. The LLC paid a $900 estimate with Web Pay on June 13, 2025 (due June 16, 2025, because June 15 fell on a Sunday). The 2025 fee is also $900, so there is no balance and no penalty. Even if the fee had come in higher, paying at least the 2024 fee by the 6th-month date meets the R&TC §17942(d)(2) safe harbor.

### Step 5 — Filing deadline

Partnership-classified → 15th day of the 3rd month → **March 16, 2026** (March 15, 2026 is a Sunday). Automatic 7-month extension to October 15, 2026.

### Step 6 — Schedule K and member K-1s

#### California adjustments to federal amounts

| Item | Federal | California | Adjustment |
|------|---------|------------|------------|
| §179 expense (Schedule K line 12) | $40,000 | $25,000 (2025 FTB 3885L line 1; §179 property $40,000 < $200,000 threshold) | −$15,000 |
| Depreciation on the remaining $15,000 basis | $0 (fully expensed federally) | 5-year MACRS, half-year: 20% × $15,000 = $3,000 on FTB 3885L → Schedule B line 17 | Ordinary income −$3,000 |
| §168(k) bonus depreciation | $0 (not used) | $0 | None |
| §199A | Member level (Form 1040), not on Form 1065 | Not on Form 568 | None |

Net effect on the members' California income compared with federal: +$15,000 (smaller §179) − $3,000 (extra depreciation) = **+$12,000**.

#### Schedule K (568)

| K Line | Item | (b) Federal K (1065) | (c) CA adjustment | (d) California |
|--------|------|------------|------------|-----------|
| 1 | Ordinary income from trade or business | $215,000 | −$3,000 | $212,000 |
| 5 | Interest income | $1,200 | $0 | $1,200 |
| 12 | §179 expense | $40,000 | −$15,000 | $25,000 |
| 21a | Total distributive income/payment items (1 + 5 − 12) | $176,200 | +$12,000 | $188,200 |

#### K-1 (568) per member (column (d), California)

Jordan Reyes (60%):
- Ordinary income: $127,200
- Interest: $720
- §179: $15,000

Sam Ortiz (40%):
- Ordinary income: $84,800
- Interest: $480
- §179: $10,000

### Step 7 — Apportionment

Business wholly within California. Question M(1) "No"; no Schedule R.

### Step 8 — Nonresident members

Both Jordan and Sam are California residents. No FTB 3832, no Schedule T, no withholding.

### Step 9 — Compute the bottom line

```
Line 1  (Total income from Schedule IW):     $401,200
Line 2  (LLC fee, $250K–$499,999 tier):          $900
Line 3  (2025 annual LLC tax):                   $800
Line 4  (PTE elective tax):                        $0
Line 5  (Nonconsenting nonresident tax):           $0
Line 6  (Partnership level tax):               (blank)
Line 7  (Total tax and fee):                   $1,700
Line 8  (Paid with FTB 3522 + 3536):           $1,700
Line 12 (Total payments):                      $1,700
Line 14 (Payments balance):                    $1,700
Line 16 (Tax and fee due):                         $0
Line 17 (Overpayment):                             $0
Line 21 (Total amount due):                        $0
```

### Step 10 — Validation

- ☑ Math: Line 7 = $900 + $800 + $0 + $0 + $0 = $1,700. Line 8 = $800 + $900 = $1,700. Line 16 = $0. Pass.
- ☑ Math: Schedule IW line 17 = $400,000 + $0 + $1,200 = $401,200 → line 1. Pass.
- ☑ Math: K-1 shares sum to Schedule K column (d): ordinary $127,200 + $84,800 = $212,000; interest $720 + $480 = $1,200; §179 $15,000 + $10,000 = $25,000. Two K-1s = Question K (2). Pass.
- ☑ Sanity: $401,200 is $98,800 below the $500,000 boundary (no boundary risk).
- ☑ Sanity: §179 limited to $25,000 and the $15,000 excess depreciated on FTB 3885L.

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for taxable year 2025

## Identification (Side 1)
A. SOS file number:                       202206543210
B. FEIN:                                  87-9876543
E. Accounting method:                     Cash
F. Date business started in CA:           01/15/2022
G. Total assets EOY:                      $58,000 (from Schedule L)
H. Boxes checked:                         none (not initial / final / amended / protective)
I(1)–I(3):                                No / No / No

## Side 1 — Tax, fee, and payments
Line 1.  Total income from Schedule IW:        $401,200
Line 2.  LLC fee:                                 $900
Line 3.  Annual LLC tax:                          $800
Line 4.  PTE elective tax:                          $0
Line 5.  Nonconsenting nonresident tax:             $0
Line 6.  Partnership level tax:                (blank)
Line 7.  Total tax and fee:                     $1,700
Line 8.  Paid with FTB 3537 / 3522 / 3536:      $1,700
Line 9.  PTE elective tax payments:                 $0
Line 10. Prior-year overpayment credited:           $0
Line 11. Withholding:                               $0
Line 12. Total payments:                        $1,700
Line 13. Use tax:                                   $0
Line 14. Payments balance:                      $1,700
Line 15. Use tax balance:                           $0
Line 16. Tax and fee due:                           $0
Line 17. Overpayment:                               $0
Line 18. Credited to 2026:                          $0
Line 19. Refund:                                    $0
Line 20. Penalties and interest:                    $0
Line 21. Total amount due:                          $0

## Questions (Side 2–3)
J. PBA code / activity / product:   541800 / Marketing agency / Brand strategy and digital marketing
K. Maximum members:                 2
M(1) Schedule R:                    No
P(1)/P(2) nonresident members:      No / No
U(1) Disregarded:                   No
GG(2) First year doing business in CA: No

## Schedule IW
1a $400,000 · 1b $0 · 2a–6 $0 · 7 $400,000 · 8a–9c $0 · 10 $1,200 · 11–16 $0
17 $401,200 → Side 1, line 1

## Schedule K (568) summary
| K Line | Item | (b) Federal | (c) CA adjustment | (d) California |
|--------|------|-------------|-------------------|----------------|
| 1 | Ordinary income | $215,000 | −$3,000 (FTB 3885L depreciation on $15,000) | $212,000 |
| 5 | Interest income | $1,200 | $0 | $1,200 |
| 12 | §179 expense | $40,000 | −$15,000 (CA limit $25,000) | $25,000 |

## Schedule K-1 (568) per member
| Member | TIN | % | Ordinary income | Interest | §179 | CA resident | FTB 3832 |
|--------|-----|---|-----------------|----------|------|-------------|----------|
| Jordan Reyes | XXX-XX-XXXX | 60 | $127,200 | $720 | $15,000 | Yes | N/A |
| Sam Ortiz    | XXX-XX-XXXX | 40 | $84,800  | $480 | $10,000 | Yes | N/A |

## Payments and attachments
- [x] 2025 FTB 3522 ($800) — Web Pay, April 10, 2025
- [x] 2025 FTB 3536 ($900) — Web Pay, June 13, 2025
- [ ] FTB 3832 — not applicable (both members CA residents)
- [ ] Form 592-Q / 592-PTE / 592-B — not applicable (no nonresident members)
- [ ] Schedule R — not applicable (100% California)
- [x] FTB 3885L (depreciation and California §179)
- [x] Schedules L, M-1, M-2 and Item G — required: federal Form 1065 Schedule B Question 4a ("total receipts less than $250,000") is "No"

## Validation summary
- Math: all checks passed
- Sanity:
  - §179 limited to $25,000; $15,000 excess depreciated ($3,000 in 2025)
  - All members CA residents → no nonresident complexity
  - Schedule IW within tier ($401,200 < $500,000)
- Next steps:
  - Each member reports the K-1 (568) amounts on their California return (California §179 and depreciation differ from federal)
  - 2026 FTB 3522 ($800) due April 15, 2026
  - 2026 FTB 3536 estimate due June 15, 2026 — paying at least $900 (the 2025 fee) by then avoids the estimate penalty even if 2026 crosses $500,000
  - 2025 Form 568 due March 16, 2026 (October 15, 2026 on extension); 2026 Form 568 due March 15, 2027

## Sources cited in this draft
- 2025 Form 568 and 2025 Form 568 Booklet (General Information E, F; Schedule IW; Schedule L)
- 2025 Form 1065 (lines 22–23; Schedule B Question 4)
- 2025 FTB 3885L (§179 $25,000 / $200,000; no §168(k))
- 2025 Instructions for Form 4562 (federal §179 $2,500,000)
- R&TC §17941, §17942(a)(1), §17942(d)(2), §18567, §18633.5
```

## Why each non-obvious choice

**Why does California allow only $25,000 of §179 instead of the federal $2,500,000?** California does not conform to the enhanced federal §179 expensing; its limit is $25,000 with a $200,000 investment threshold (2025 FTB 3885L; R&TC §17255). The remaining $15,000 of basis is depreciated over the asset's California recovery period.

**Why does ordinary income change by only $3,000?** §179 is not part of ordinary business income; it passes through separately on Schedule K line 12. The ordinary-income difference is only the extra California depreciation on the $15,000 that California would not expense.

**Why is the LLC fee $900 and not $0?** Schedule IW line 17 ($401,200) exceeds $250,000. The tier table jumps from $0 to $900 at $250,000.

**Why is interest income included in Schedule IW?** Schedule IW counts all California-source income items (line 10 is interest), not just operating revenue. For an LLC whose business is wholly within California, everything is assigned to California.

**Why are Schedules L, M-1, M-2 required?** The shortcut applies only if federal Form 1065 Schedule B Questions 4a–4c are all "Yes" and the LLC has 10 or fewer members (2025 booklet, Schedule L). Question 4a requires total receipts under $250,000; this LLC had $400,000.

**What if Jordan moved to Texas mid-year?** Then Jordan is a part-year resident and possibly a nonresident member at year-end, which raises the FTB 3832 / Schedule T question and 7% withholding on distributions after the move. Residency is fact-specific (FTB Pub. 1031) — flag it and refer to a CPA.

**Why no Schedule R?** Single-state operation. Schedule R applies only when income must be apportioned across states.

## Audit defense

The LLC's audit defense:
1. SOS confirms California formation
2. Federal Form 1065 cross-references all income and the §179 election
3. FTB 3885L shows the $25,000 California §179 and the $3,000 depreciation on the $15,000 excess
4. Schedule IW built from gross receipts plus interest
5. Both members CA residents — no FTB 3832 needed
6. FTB 3522 and FTB 3536 timely paid; Form 568 timely filed

This is a clean mid-tier filing. The most fragile piece is the California depreciation schedule — keep FTB 3885L and the asset's California basis for every later year.
