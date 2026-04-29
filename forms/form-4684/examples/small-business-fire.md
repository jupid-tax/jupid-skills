# Example: Small Business with Equipment Fire Loss

A complete walkthrough of Form 4684 Section B for a casualty loss to business property with partial insurance recovery. Pattern: medium loss, partial insurance, depreciation history affecting basis, ordinary loss to Form 4797.

## The filer

- **Name**: Marcus Chen
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Business**: Photography studio LLC (single-member, taxed as disregarded entity → Schedule C)
- **Event**: Electrical fire in studio space, December 2025; not part of a federally declared disaster
- **Property**: Three pieces of equipment damaged

The fire was not a federally declared disaster — just a localized electrical fire. Section A would be unavailable (post-TCJA §165(h)(5)). But Section B doesn't have that restriction; business casualty losses are deductible regardless of disaster status.

## Inputs gathered

### AGI

Single, AGI = $89,000 for 2025 (not relevant to Section B math but agent recorded for completeness).

### The damaged equipment

| Item | Description | Original cost | Date placed in service | Depreciation method | Accumulated depreciation by Dec 2025 | Adjusted basis |
|------|-------------|---------------|------------------------|---------------------|---------------------------------------|----------------|
| 1 | Sony A1 camera body | $6,500 | Jan 2023 | MACRS 5-yr | $4,225 (~3 yrs) | $2,275 |
| 2 | Pro lighting kit (2× 1500W strobes + softboxes) | $7,800 | Mar 2024 | §179 (full) | $7,800 | $0 |
| 3 | Backdrop printer (large format) | $5,200 | Aug 2025 | §179 (full) | $5,200 | $0 |
| Total | | $19,500 | | | | $2,275 |

Wait — let me re-examine this. The user mentioned "$15K equipment fire loss" so let me adjust the per-item structure to match a $15K loss and make the depreciation realistic.

Adjusting:

| Item | Description | Original cost | Service date | Depreciation method | Accum dep | Adjusted basis | FMV before | FMV after |
|------|-------------|---------------|--------------|---------------------|-----------|----------------|------------|-----------|
| 1 | Sony A1 + lenses | $9,000 | Jan 2023 | MACRS 5-yr (no §179) | $5,400 | $3,600 | $5,500 | $0 |
| 2 | Lighting kit (4 strobes, modifiers) | $4,500 | Mar 2024 | MACRS 5-yr | $1,800 | $2,700 | $3,800 | $0 |
| 3 | Studio computer + accessories | $3,500 | Aug 2025 | MACRS 5-yr (held 4 mo; partial year depreciation) | $350 | $3,150 | $3,200 | $200 |

Total destroyed value (FMV before) = $5,500 + $3,800 + $3,200 = $12,500
Total decline in FMV = $5,500 + $3,800 + $3,000 = $12,300

### Insurance

- Marcus had a Business Owner's Policy (BOP) covering equipment up to $20,000 with a $1,000 deductible
- Filed claim; insurer settled for **$8,500** total (after deductible)
- Settlement received January 2026 (post tax-year, but settlement is reasonably foreseeable for the 2025 return → claim it now per Pub 547)
- Allocate the $8,500 across items proportionally to FMV decline:
  - Camera: $5,500 / $12,300 × $8,500 = $3,801
  - Lighting: $3,800 / $12,300 × $8,500 = $2,626
  - Computer: $3,000 / $12,300 × $8,500 = $2,073

Total reimbursement: $8,500 (rounding-checked)

### Per-item loss calculation (Section B Line 27)

| Item | Adj basis | Decline FMV | Smaller of (Line 26) | Insurance | Loss (Line 27) |
|------|-----------|-------------|----------------------|-----------|----------------|
| Camera | $3,600 | $5,500 | $3,600 | $3,801 | $0 (gain of $201) |
| Lighting | $2,700 | $3,800 | $2,700 | $2,626 | $74 |
| Computer | $3,150 | $3,000 | $3,000 | $2,073 | $927 |

Wait — the camera item shows insurance > smaller-of-basis. That creates a **gain** on that item, not a loss.

Let me recompute precisely:

**Item 1 (Camera)**:
- Smaller of basis or decline: smaller of $3,600 or $5,500 = $3,600
- Insurance: $3,801
- Insurance > smaller-of basis: $3,801 − $3,600 = **gain of $201** (Line 22)
- No loss on Line 27 for this item

**Item 2 (Lighting)**:
- Smaller of $2,700 or $3,800 = $2,700
- Insurance: $2,626
- Loss: $2,700 − $2,626 = $74

**Item 3 (Computer)**:
- Smaller of $3,150 or $3,000 = $3,000
- Insurance: $2,073
- Loss: $3,000 − $2,073 = $927

**Section B Part I totals (Lines 22, 27)**:
- Gain (Line 22): $201
- Loss (Line 27): $74 + $927 = $1,001

**Section B Part II roll-up**:
- Net = $201 gain − $1,001 loss = **net loss of $800**
- Holding period: items 1 & 2 long-term (>1yr), item 3 short-term (<1yr)
- Need to separate by holding period for the gain/loss roll-up — but since the net is a loss flowing to Form 4797 Part II as ordinary loss anyway, the holding-period split mostly affects character of the gain (which is small here)

Net business ordinary loss flowing to Form 4797 Part II Line 14: **$800**

### Why the loss is so much smaller than $15K

Marcus's gross damage was $12,300 in FMV decline. But:

1. **Adjusted basis caps the loss**. Two of three items had basis lower than FMV decline (because depreciation reduced basis). The total "smaller of" was $9,300 not $12,300.
2. **Insurance recovery was substantial**. $8,500 of the $9,300 was recovered.
3. **Some items showed a gain** (camera) because insurance exceeded basis.

Net of all: $800 deductible ordinary loss + $201 gain to recognize. Net Form 4684 effect: small.

### §1033 deferral on the camera gain?

Marcus has a $201 gain on the camera. He's planning to buy a replacement camera with insurance proceeds + savings. He could elect §1033 deferral to avoid recognizing the $201 gain.

Practical note: $201 deferral isn't worth the paperwork. Recognize and move on. (If the gain were $5,000+, §1033 would matter more.) Agent flags this and lets Marcus decide.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Marcus Chen
Identifying number: XXX-XX-XXXX
FEMA disaster declaration number: N/A (no declared disaster; Section A not used)

## Section A — Personal-Use Property
N/A (no personal-use casualty loss; would be barred under §165(h)(5) anyway)

## Section B — Business and Income-Producing Property

### Part I — Per-item gain/loss

| Line | Description | Trade/Business (b)(i) ||| Income-Producing (b)(ii) |
|------|-------------|-------------|-------------|-------------|--------:|
|      | (Item 1)    | (Item 2)    | (Item 3)    |             | |
| 19 | Description | Sony A1 + lenses | Lighting kit | Studio computer | N/A |
| 20 | Cost or other basis | $3,600 | $2,700 | $3,150 | — |
| 21 | Insurance/reimbursement | $3,801 | $2,626 | $2,073 | — |
| 22 | Gain (Line 21 − Line 20 if pos) | $201 | $0 | $0 | — |
| 23 | FMV before | $5,500 | $3,800 | $3,200 | — |
| 24 | FMV after | $0 | $0 | $200 | — |
| 25 | Decline (Line 23 − Line 24) | $5,500 | $3,800 | $3,000 | — |
| 26 | Smaller of Line 20 or Line 25 | $3,600 | $2,700 | $3,000 | — |
| 27 | Subtract Line 21 from Line 26 (≥0) | $0 | $74 | $927 | — |

### Part II — Roll-up

By holding period:
- Long-term (Items 1, 2): gain $201, loss $74 → net loss $0 (gain $201 absorbed; remaining gain = $127); per actual Form 4684 Part II logic: gains and losses from long-term assets net to a $127 long-term gain (held > 1 year)
- Short-term (Item 3): loss $927

Form 4684 actual line entries:

| 28 | Total losses (long-term, Line 27) | $74 |
| 29-31 | Continuation totals | varied |
| 32 | Total gains (long-term, Line 22) | $201 |
| 33-34 | Continuation totals | varied |
| 35-37 | Loss roll-ups | $1,001 |
| 38 | Net loss → Form 4797 Part II Line 14 | $800 |
| 39 | Income-producing loss → Schedule A Line 16 | $0 |

(Note: actual Form 4684 Part II line numbering separates short-term and long-term; the agent fills following the form's exact structure. The bottom-line transfers are $800 ordinary loss to Form 4797 and a $201 gain that may be capital or ordinary depending on §1231 netting.)

## Section C — Theft (§1244 / Ponzi safe harbor)
N/A

## Section D — Election to Deduct in Preceding Year
N/A (no federally declared disaster)

## Required attachments
- [ ] Schedule A (no Section A or income-producing loss)
- [x] Form 4797 (Section B losses + §1231 gain netting)
- [ ] Statement with FEMA disaster number (not applicable)
- [x] Fire department report (insurer requires; agent retains)
- [x] Insurance settlement letter showing $8,500 with allocation
- [x] Asset depreciation schedules from prior years (substantiating adjusted basis)
- [x] Original purchase receipts for all three items
- [x] Photos of damaged equipment

## Validation summary
- Math: all checks passed
  - Item 1 (camera): basis $3,600 < decline $5,500 → smaller is basis $3,600. Insurance $3,801 > basis → gain of $201, NOT a loss.
  - Item 2 (lighting): basis $2,700 < decline $3,800 → smaller is $2,700. Insurance $2,626 < basis → loss $74.
  - Item 3 (computer): basis $3,150 > decline $3,000 → smaller is $3,000. Insurance $2,073 < $3,000 → loss $927.
  - No floors applied (Section B has no $100 floor and no AGI floor)
- Sanity:
  - All three items used 100% in business (no personal use)
  - Insurance settlement was finalized in early Jan 2026 → reasonably foreseeable on 2025 return; included
  - One item (camera) shows a gain because insurance > adjusted basis (depreciation had reduced basis below FMV decline)
  - §1033 deferral on $201 gain: technically available, but not worth the paperwork at this size
  - Long-term items net to a §1231 gain of $127; short-term item is straight ordinary loss; form's Part II logic handles split
  - No federally declared disaster → Section A correctly omitted; would be barred anyway under §165(h)(5)
- Insurance status: settled (Jan 2026 settlement of $8,500 with itemized allocation)
- Depreciation history: substantiated by Form 4562s from 2023, 2024, 2025 returns
- Next steps:
  - Complete Form 4797 with $800 ordinary loss + $201 §1231 gain entries
  - §1231 netting on Form 4797 — gain becomes capital if all §1231 nets to gain; otherwise ordinary
  - Confirm Schedule C asset records remove the destroyed items going forward
  - Retain all documentation 3+ years post-filing

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision
- IRS Pub 547 (Casualties, Disasters, and Thefts)
- IRS Pub 584-B (Business Casualty/Theft Workbook)
- IRS Form 4797 instructions
- IRC §165(c)(1) — trade or business losses
- IRC §1231 — character of business property gains/losses
- IRC §1033 — involuntary conversion deferral (flagged but not elected)
- Reg. §1.165-7 — casualty losses
```

## Why each non-obvious choice

**Why Section B and not Section A?** All three items were used 100% in Marcus's photography business. Section B handles trade/business and income-producing property. The fire was NOT a federally declared disaster — Section A would have been unavailable anyway under §165(h)(5).

**Why is the deductible loss so much smaller than $12,300 of damage?**

Three layers of reduction:
1. **Adjusted basis caps the loss** for two items. Camera and lighting had been depreciated over multiple years; their basis was below FMV decline.
2. **Insurance recovered $8,500** of the $9,300 cap.
3. **One item (camera) had insurance > basis**, creating a $201 gain instead of a loss.

The user-perceived loss ($12,300 of equipment destroyed) doesn't match the tax-deductible loss ($800 net). This is normal — depreciation already gave Marcus tax benefit on the camera and lighting in earlier years.

**Why does the $201 gain matter?**

Insurance in excess of basis is a recognized gain unless the user elects §1033 deferral. For tax purposes, this is treated as if Marcus sold the camera for $3,801 and had $3,600 basis = $201 gain. On Form 4684 Section B Line 22 it shows up; on Form 4797 it nets against the §1231 losses.

For $201, §1033 isn't worth the trouble. Recognize and move on.

**Why does Form 4797 Part II matter?**

Form 4684 Section B doesn't directly reduce Schedule C. The flow is:
1. Form 4684 Section B computes the per-item losses (and gains)
2. Net amounts flow to Form 4797 Part II (ordinary losses) + Form 4797 Part I (§1231 gain netting)
3. §1231 netting determines whether net §1231 amounts are capital or ordinary
4. Final ordinary loss / capital gain flows to Schedule 1 → Form 1040

This trail preserves the character of business losses (ordinary) and gains (capital if net §1231 is gain).

**What if Marcus had no insurance?**

Loss would be the full smaller-of-basis amount: $3,600 + $2,700 + $3,000 = $9,300. Much bigger deduction, but Marcus would be out-of-pocket for replacement. Insurance is almost always the better economic choice even with smaller tax deduction.

**What documentation does Marcus retain?**
1. Fire department incident report (date, cause, scope)
2. Insurance claim file (initial filing, adjuster reports, settlement letter, allocation)
3. Photos of damaged equipment
4. Original purchase receipts for all three items
5. Depreciation schedules from prior-year Form 4562s (substantiates adjusted basis)
6. Schedule C and Form 4562 from prior years showing the items
7. Replacement-cost estimates (corroborate FMV before)

Retain at least 3 years post-filing. Equipment-fire losses with insurance recoveries are common audit topics — the IRS often verifies the insurance allocation matches Form 4684.
