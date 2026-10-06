# Example: Small Business with Equipment Fire Loss

A complete walkthrough of Form 4684 Section B for a casualty loss to business property with partial insurance recovery. Pattern: medium loss, partial insurance, depreciation history affecting basis, one item with a gain that is depreciation recapture, ordinary loss to Form 4797.

## The filer

- **Name**: Marcus Chen
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Business**: Photography studio LLC (single-member, taxed as disregarded entity → Schedule C)
- **Event**: Electrical fire in studio space, October 2025; not part of a federally declared disaster
- **Property**: Three pieces of equipment, all totally destroyed

The fire was not a federally declared disaster — just a localized electrical fire. A personal-use loss from it would not be deductible (§165(h)(5)). Section B doesn't have that restriction; business casualty losses are deductible regardless of disaster status.

## Inputs gathered

### AGI

Single, AGI = $89,000 for 2025 (not relevant to Section B math but agent recorded for completeness).

### The destroyed equipment

Depreciation: MACRS 5-year GDS, 200% declining balance, half-year convention, no §179, and Marcus elected out of the special depreciation allowance for 2023 and 2024 (from his prior Forms 4562). In the year of disposition the half-year convention allows half a year of depreciation. Property placed in service and disposed of in the same year gets no depreciation (2025 Instructions for Form 4562).

| Item | Description | Original cost | Placed in service | Depreciation allowed through disposition | Adjusted basis (line 20) | FMV before | FMV after |
|------|-------------|---------------|-------------------|------------------------------------------|--------------------------|------------|-----------|
| A | Sony A1 + lenses | $9,000 | Jan 2023 | 2023 $1,800 + 2024 $2,880 + 2025 $864 (½ × 19.2%) = $5,544 | $3,456 | $5,500 | $0 |
| B | Lighting kit (4 strobes, modifiers) | $4,500 | Mar 2024 | 2024 $900 + 2025 $720 (½ × 32%) = $1,620 | $2,880 | $3,800 | $0 |
| C | Studio computer + accessories | $3,500 | Aug 2025 | $0 (placed in service and disposed of in 2025) | $3,500 | $3,200 | $0 |

Total FMV before = $5,500 + $3,800 + $3,200 = $12,500. All three items were totally destroyed, so the decline in FMV equals FMV before.

### Insurance

- Marcus had a Business Owner's Policy (BOP) covering equipment up to $20,000 with a $1,000 deductible
- Filed claim; insurer settled for **$8,500** total (after deductible), paid December 2025
- Lump-sum reimbursement is divided among the assets by the FMV of each at the time of the loss (instructions for line 3, "Lump-sum reimbursement"):
  - Camera: $5,500 / $12,500 × $8,500 = $3,740
  - Lighting: $3,800 / $12,500 × $8,500 = $2,584
  - Computer: $3,200 / $12,500 × $8,500 = $2,176

Total reimbursement: $8,500 (rounding-checked)

### Per-item computation (Section B Part I)

**Item A (Camera)**:
- Line 20 basis $3,456; line 21 insurance $3,740
- Line 21 > line 20 → **gain of $284** on line 22; skip lines 23-27 for this column

**Item B (Lighting)**:
- Line 21 $2,584 < line 20 $2,880 → no gain
- Totally destroyed → line 26 = line 20 = $2,880 (also the smaller of $2,880 or the $3,800 decline)
- Line 27: $2,880 − $2,584 = **$296** loss

**Item C (Computer)**:
- Line 21 $2,176 < line 20 $3,500 → no gain
- Totally destroyed → line 26 = line 20 = $3,500, even though the $3,200 decline is smaller (form note on line 26; Reg. §1.165-7(b)(1))
- Line 27: $3,500 − $2,176 = **$1,324** loss

**Line 28**: $296 + $1,324 = **$1,620**, allocated by holding period: computer $1,324 (held 1 year or less) to line 29, lighting $296 (more than 1 year) to line 34.

### The camera gain is depreciation recapture

The camera is §1245 property held more than 1 year, and its $284 gain is smaller than the $5,544 of depreciation taken. Recapture applies, so the instructions for line 33 send it through Form 4797 Part III instead of Form 4684 line 34:
- Form 4797 line 20 (gross sales price = insurance) $3,740; line 21 cost $9,000; line 22 depreciation $5,544; line 23 adjusted basis $3,456; line 24 gain $284; line 25a $5,544; line 25b $284
- Form 4797 line 30 $284; line 31 $284 → Form 4797 line 13 (ordinary); line 32 $0 → Form 4684 line 33 = $0

### Section B Part II roll-up

- Held 1 year or less: line 29 (b)(i) ($1,324) → line 30 → line 31 ($1,324) → Form 4797 line 14
- Held more than 1 year: line 34 (b)(i) ($296); line 35 ($296); line 36 gains $0 (line 33 $0 + line 34 column (c) $0); line 37 ($296)
- Line 37 loss is more than line 36 gain → line 38a = line 35 (b)(i) + line 36 = ($296) → Form 4797 line 14
- Line 38b $0; line 39 not used

Form 4797: line 13 $284 (recapture) + line 14 ($1,620) = **net ordinary loss of $1,336** (line 17, then line 18b → Schedule 1 line 4).

### Why the loss is so much smaller than $12,500

Marcus lost equipment worth $12,500 before the fire. But:

1. **Adjusted basis caps the loss**. Depreciation had already reduced basis to $3,456 + $2,880 + $3,500 = $9,836.
2. **Insurance recovery was substantial**. $8,500 of the $9,836 was recovered.
3. **One item (camera) showed a gain** because insurance exceeded its depreciated basis, and that gain is ordinary recapture.

Net of all: $1,620 ordinary casualty loss − $284 ordinary recapture = $1,336 net ordinary loss.

### §1033 deferral on the camera gain?

Marcus has a $284 gain on the camera. He's planning to buy a replacement camera with insurance proceeds + savings. He could choose §1033 postponement by buying similar replacement property by December 31, 2027 (2 years after the close of 2025, the year the gain was realized; Pub. 547 "Replacement Period").

Practical note: $284 deferral isn't worth the paperwork and basis tracking. Recognize and move on. (If the gain were $5,000+, §1033 would matter more.) Agent flags this and lets Marcus decide.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Marcus Chen
Identifying number: XXX-XX-XXXX
Federally declared disaster box: not checked (no declared disaster; Section A not used)

## Section A — Personal-Use Property
N/A (no personal-use casualty loss)

## Section B — Business and Income-Producing Property

### Part I — Studio fire, October 2025

| Line | Description | Property A | Property B | Property C |
|------|-------------|-----------:|-----------:|-----------:|
| 19 | Description | Sony A1 + lenses, [city, state], acquired 01/2023 | Lighting kit, [city, state], acquired 03/2024 | Studio computer, [city, state], acquired 08/2025 |
| 20 | Cost or adjusted basis | $3,456 | $2,880 | $3,500 |
| 21 | Insurance/reimbursement | $3,740 | $2,584 | $2,176 |
| 22 | Gain (Line 21 − Line 20 if pos) | $284 | $0 | $0 |
| 23 | FMV before | (skip) | $3,800 | $3,200 |
| 24 | FMV after | (skip) | $0 | $0 |
| 25 | Decline (Line 23 − Line 24) | (skip) | $3,800 | $3,200 |
| 26 | Totally destroyed: Line 20 amount | (skip) | $2,880 | $3,500 |
| 27 | Subtract Line 21 from Line 26 (≥0) | (skip) | $296 | $1,324 |
| 28 | Casualty or theft loss | $1,620 | | |

### Part II — Summary of Gains and Losses
| Line | (a) Casualty | (b)(i) Trade/business | (b)(ii) Income-producing | (c) Gains |
|------|--------------|----------------------:|-------------------------:|----------:|
| 29 | Studio fire 10/2025 (computer, held ≤ 1 yr) | ($1,324) | $0 | $0 |
| 30 | Totals | ($1,324) | $0 | $0 |
| 31 | Line 30 (b)(i) + (c) → Form 4797 line 14 | ($1,324) | | |
| 32 | Line 30 (b)(ii) → Schedule A line 16 | | $0 | |
| 33 | Casualty gains from Form 4797 line 32 | | | $0 |
| 34 | Studio fire 10/2025 (lighting, held > 1 yr) | ($296) | $0 | $0 |
| 35 | Total losses | ($296) | $0 | |
| 36 | Total gains (Line 33 + Line 34 (c)) | | | $0 |
| 37 | Line 35 (b)(i) + (b)(ii) | ($296) | | |
| 38a | Line 35 (b)(i) + Line 36 → Form 4797 line 14 | ($296) | | |
| 38b | Line 35 (b)(ii) → Schedule A line 16 | | $0 | |
| 39 | Not used (loss on 37 exceeds gain on 36) | | | |

## Section C — Ponzi-type scheme theft loss, Lines 40-51
N/A

## Section D — Election to Deduct in Preceding Year, Lines 52-57
N/A (no federally declared disaster)

## Required attachments
- [ ] Schedule A (no Section A or income-producing loss)
- [x] Form 4797 (Part III recapture for the camera: line 31 $284 → line 13; line 14 ($1,620) from Form 4684 lines 31 and 38a)
- [ ] Rev. Proc. 2018-08 statement (not applicable)

Kept in the file, not attached: fire department report, insurance settlement letter showing $8,500 and the FMV allocation, prior-year Forms 4562 (substantiating depreciation), original purchase receipts, photos of damaged equipment.

## Validation summary
- Math: all checks passed
  - Item A (camera): insurance $3,740 > basis $3,456 → gain of $284 on line 22; lines 23-27 skipped
  - Item B (lighting): totally destroyed → line 26 = basis $2,880; loss $296
  - Item C (computer): totally destroyed → line 26 = basis $3,500 (not the $3,200 decline); loss $1,324
  - Line 28 = $1,620 = $1,324 (line 29) + $296 (line 34)
  - Insurance allocation sums to $8,500
  - No floors applied (Section B has no $100 reduction and no AGI floor)
- Sanity:
  - All three items used 100% in business (no personal use)
  - Insurance settlement paid December 2025, so the camera gain is a 2025 item (a reimbursement received in a later year is reported in the year received; instructions for line 4)
  - Computer placed in service and destroyed in 2025: no depreciation claimed for it
  - Camera gain is §1245 recapture → Form 4797 Part III, Form 4684 line 33 = $0
  - §1033 deferral on $284 gain: available, not worth the paperwork at this size
  - No federally declared disaster → Section A not used; Section D not available
- Insurance status: settled (December 2025 settlement of $8,500 with FMV allocation)
- Depreciation history: substantiated by Forms 4562 from 2023 and 2024 returns; 2025 disposition-year depreciation ($864 camera, $720 lighting) on the 2025 Form 4562
- Next steps:
  - Complete Form 4797: line 13 $284, line 14 ($1,620), line 17 ($1,336) → line 18b → Schedule 1 line 4
  - The loss does not reduce Schedule C net profit or self-employment tax (IRC §1402(a)(3)(C))
  - Remove the destroyed items from the depreciation schedule going forward
  - Retain all documentation 3+ years post-filing

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision (lines 3, 4, 26, 28, 31, 33, 38a)
- IRS Form 4797, 2025 revision (Part III lines 20-32; Part II lines 13, 14, 17, 18b)
- IRS Instructions for Form 4562, 2025 (same-year disposition; conventions)
- IRS Pub 547 (Casualties, Disasters, and Thefts)
- IRS Pub 584-B (Business Casualty/Theft Workbook)
- IRC §165(c)(1) — trade or business losses
- IRC §1245 — depreciation recapture
- IRC §1033 — involuntary conversion deferral (flagged but not elected)
- IRC §1402(a)(3)(C) — involuntary conversions excluded from self-employment income
- Reg. §1.165-7 — casualty losses
```

## Why each non-obvious choice

**Why Section B and not Section A?** All three items were used 100% in Marcus's photography business. Section B handles trade/business and income-producing property. The fire was NOT a federally declared disaster, which matters only for personal-use property.

**Why is the deductible loss so much smaller than the $12,500 of equipment destroyed?**

Three layers of reduction:
1. **Adjusted basis caps the loss**. The camera and lighting had been depreciated; their basis was below FMV.
2. **Insurance recovered $8,500** of the $9,836 total basis.
3. **One item (camera) had insurance > basis**, creating a $284 gain instead of a loss.

The user-perceived loss ($12,500 of equipment destroyed) doesn't match the tax-deductible amount ($1,336 net ordinary loss). This is normal — depreciation already gave Marcus a tax benefit on the camera and lighting in earlier years.

**Why use basis, not the smaller decline, for the computer?** The computer was totally destroyed. For business property that is totally destroyed, the loss is the adjusted basis when FMV before is lower than basis (form note on line 26; Reg. §1.165-7(b)(1)). For partial damage, the "smaller of" rule would apply.

**Why does the $284 gain matter?**

Insurance in excess of basis is a recognized gain unless the user elects §1033 deferral. For tax purposes, this is treated as if Marcus disposed of the camera for $3,740 with $3,456 basis = $284 gain. Because depreciation on the camera ($5,544) exceeds the gain, the whole gain is ordinary §1245 recapture, reported through Form 4797 Part III and not on Form 4684 line 34.

For $284, §1033 isn't worth the trouble. Recognize and move on.

**Why does Form 4797 matter?**

Form 4684 Section B doesn't directly reduce Schedule C. The flow is:
1. Form 4684 Section B Part I computes the per-item losses (and gains)
2. Line 31 (held 1 year or less) and line 38a (more than 1 year, losses exceeding gains) go to Form 4797 line 14 as ordinary amounts
3. The recapture gain goes through Form 4797 Part III to line 13
4. Form 4797 line 17 → line 18b → Schedule 1 line 4 → Form 1040

If gains on property held more than 1 year had exceeded losses, line 39 would have gone to Form 4797 line 3 for §1231 netting instead.

**What if Marcus had no insurance?**

Each item is totally destroyed, so each loss is its basis: $3,456 + $2,880 + $3,500 = $9,836 (computer $3,500 on line 29; camera and lighting $6,336 on line 34, then line 38a). All ordinary. Much bigger deduction, but Marcus would be out-of-pocket for replacement. Insurance is almost always the better economic choice even with a smaller tax deduction.

**What documentation does Marcus retain?**
1. Fire department incident report (date, cause, scope)
2. Insurance claim file (initial filing, adjuster reports, settlement letter, allocation)
3. Photos of damaged equipment
4. Original purchase receipts for all three items
5. Depreciation schedules from prior-year Form 4562s (substantiates adjusted basis)
6. Schedule C and Form 4562 from prior years showing the items
7. Replacement-cost estimates (corroborate FMV before)

Retain at least 3 years post-filing.
