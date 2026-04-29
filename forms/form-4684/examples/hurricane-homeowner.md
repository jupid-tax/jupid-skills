# Example: Homeowner with Hurricane Damage in Federally Declared Zone

A complete walkthrough of Form 4684 Section A for a personal-use casualty in a federally declared disaster area. Pattern: significant loss, partial insurance, $100 + 10% AGI reductions.

## The filer

- **Name**: Carlos Martinez
- **Filing status**: Married filing jointly
- **Tax year**: 2025 (filing in 2026)
- **Event**: Hurricane Helene, late September 2025
- **Disaster**: FEMA-DR-4856-FL (federally declared major disaster, hypothetical illustrative number — verify actual declaration before filing)
- **Property**: Single-family home in Florida + family vehicle

Both items damaged in the same event. Both classify as personal-use. Both fall under Section A because the disaster was federally declared.

## Inputs gathered

### AGI

Carlos and his spouse filed jointly with **AGI = $135,000** for 2025.

### Property A: Home damage

- **Adjusted basis**: $260,000 (purchase price $230,000 + $30,000 of improvements; never rented or used for business)
- **FMV before**: $410,000 (Zillow / appraiser estimate)
- **FMV after**: $330,000 (post-storm appraisal accounting for roof, water damage, structural issues)
- **Decline in FMV**: $410,000 − $330,000 = $80,000
- **Smaller of basis or decline**: smaller of $260,000 or $80,000 = **$80,000**
- **Insurance**: filed claim with homeowners; received $50,000 settlement (deductible + coverage limits applied)
- **Loss after insurance**: $80,000 − $50,000 = **$30,000**

### Property B: Vehicle damage

- Family minivan, used 0% for business
- **Adjusted basis**: $26,000 (purchased 3 years ago for $32,000; no improvements or §179)
- **FMV before**: $19,500 (Kelley Blue Book pre-storm)
- **FMV after**: $4,000 (totaled, salvage value)
- **Decline in FMV**: $19,500 − $4,000 = $15,500
- **Smaller of basis or decline**: smaller of $26,000 or $15,500 = **$15,500**
- **Insurance**: comprehensive coverage paid $11,000
- **Loss after insurance**: $15,500 − $11,000 = **$4,500**

### Per-event totals

- Sum of Property A + Property B losses (after insurance): $30,000 + $4,500 = **$34,500** (Line 10)
- Subtract $100 (one event = one $100): **$34,400** (Line 12)

### Roll-up

- Total Section A loss across all events (only one event): $34,400 (Line 13)
- No casualty gains: Line 14 = $0
- Net loss: $34,400 (Line 16)
- 10% AGI floor: $135,000 × 10% = $13,500 (Line 17)
- Final deductible loss: $34,400 − $13,500 = **$20,900** (Line 18)

This $20,900 flows to **Schedule A Line 15**.

### Standard vs. itemized check

The agent ran the comparison:
- Standard deduction MFJ 2025: $30,000 (illustrative — verify Rev. Proc. 2024-40 / current year)
- Itemized total: SALT $10,000 + mortgage interest $14,200 + charitable $3,500 + casualty $20,900 = **$48,600**
- Itemized > standard by $18,600 → itemize

Carlos saves taxes on the marginal $20,900 (roughly 22% bracket → ~$4,600 federal benefit). The $13,500 absorbed by the AGI floor produces no benefit.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Carlos Martinez and [Spouse]
Identifying number: XXX-XX-XXXX
FEMA disaster declaration number: DR-4856-FL (Hurricane Helene)

## Section A — Personal-Use Property (Federally Declared Disaster)

### Casualty/Theft #1: Hurricane Helene, 9/26/2025

| Line | Description | Property A: Home | Property B: Vehicle |
|------|-------------|-----------------:|--------------------:|
| 1 | Description | SFR, 123 Main St, FL | 2022 Toyota Sienna |
| 2 | Cost or other basis | $260,000 | $26,000 |
| 3 | Insurance/reimbursement | $50,000 | $11,000 |
| 4 | Gain (Line 3 − Line 2 if pos) | $0 | $0 |
| 5 | FMV before casualty | $410,000 | $19,500 |
| 6 | FMV after casualty | $330,000 | $4,000 |
| 7 | Decline in FMV | $80,000 | $15,500 |
| 8 | Smaller of Line 2 or Line 7 | $80,000 | $15,500 |
| 9 | Subtract Line 3 from Line 8 (≥ 0) | $30,000 | $4,500 |
| 10 | Total casualty/theft loss | $34,500 |
| 11 | $100 reduction | $100 |
| 12 | Subtract Line 11 from Line 10 | $34,400 |

### Roll-up across all Section A events
| 13 | Total of Line 12 (all events) | $34,400 |
| 14 | Total gains | $0 |
| 15 | Line 14 − Line 13 (gain) or 0 | $0 |
| 16 | Loss (if Line 14 < Line 13) | $34,400 |
| 17 | 10% × AGI ($135,000 × 0.10) | $13,500 |
| 18 | Line 16 − Line 17 → Schedule A Line 15 | $20,900 |

## Section B — Business and Income-Producing Property
N/A (no business or income-producing losses)

## Section C — Theft (§1244 / Ponzi safe harbor)
N/A

## Section D — Election to Deduct in Preceding Year
[x] Not elected
[ ] Elected for FEMA disaster DR-XXXX-XX

## Required attachments
- [x] Schedule A (casualty loss claimed on Line 15)
- [ ] Form 4797 (no business loss)
- [x] Statement with FEMA disaster number (Hurricane Helene, DR-4856-FL)
- [ ] Police report (not applicable; not a theft)
- [x] Insurance settlement letters (homeowners, auto)
- [x] Pre-storm and post-storm appraisals (home)
- [x] Kelley Blue Book pre-storm valuation (vehicle)
- [x] FEMA registration confirmation

## Validation summary
- Math: all checks passed
  - Line 8 = smaller of basis or decline: confirmed for both properties
  - Line 11 ($100) applied once for the single event
  - Line 17 (10% AGI) = $13,500 = 10% × $135,000
  - Line 18 = $34,400 − $13,500 = $20,900
- Sanity:
  - FEMA disaster number verified at fema.gov: DR-4856-FL declared 9/27/2025
  - Insurance fully resolved before filing (no pending claims)
  - Standard vs. itemized: itemizing saves $18,600+; Form 4684 worth filing
  - 10% AGI floor consumes 39% of the gross loss — common for moderate-AGI households
- Disaster-year election (Section D): NOT elected
  - 2024 AGI was $128,000 (similar to 2025); marginal rate similar
  - Refund timing: filing 2025 normally vs. amending 2024 — Carlos prefers normal filing
- Insurance status: settled (homeowner $50K, auto $11K)
- Next steps:
  - File Schedule A with $20,900 on Line 15
  - Confirm Schedule A itemized total > standard deduction → confirmed
  - Retain FEMA registration, insurance correspondence, appraisals for at least 3 years

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision
- IRS Pub 547 (Casualties, Disasters, and Thefts)
- IRS Pub 584 (Personal-Use Property Workbook)
- IRC §165(c) — allowable losses
- IRC §165(h)(1) — $100 per-event floor
- IRC §165(h)(2) — 10% AGI floor
- IRC §165(h)(5) — federally declared disaster requirement
- FEMA disaster declaration DR-4856-FL (Hurricane Helene, hypothetical illustrative)
```

## Why each non-obvious choice

**Why Section A and not Section B?** Carlos's home and vehicle are 100% personal-use. He doesn't run a business, doesn't rent the home, and doesn't drive the minivan for any business. Both are squarely Section A.

**Why the loss isn't $80,000 + $15,500 = $95,500?** Two reasons:
1. Insurance reimbursement is subtracted before any floor — that's IRC §165(a) requiring loss to be net of compensation.
2. Section A applies a $100 per-event floor and a 10% AGI floor.

The path is: $80,000 + $15,500 (gross losses, FMV decline) → minus $50,000 + $11,000 insurance = $34,500 → minus $100 floor = $34,400 → minus $13,500 AGI floor = $20,900.

**Why didn't Carlos elect the disaster-year (§165(i)) election?** The agent computed both:
- Loss-year (2025): 10% × $135K = $13,500 floor; $20,900 deductible
- Prior-year (2024): 10% × $128K = $12,800 floor; $21,600 deductible (slightly more)

The $700 extra deduction at a 22% marginal rate = ~$154 additional savings. Carlos preferred normal filing over the complexity of amending a return for $154. The agent flagged the option, computed the numbers, and let Carlos decide.

**Why is the $100 floor only applied once?** Hurricane Helene is one casualty event. The $100 floor applies per event, not per damaged item. Even though both home and vehicle were damaged, it's still one event. (If Carlos had also had an unrelated kitchen fire that same year — a separate event — that would be a second Form 4684 with its own $100 floor.)

**Why didn't Carlos use replacement cost?** Replacement cost is irrelevant under Reg. §1.165-7(b)(1). The deductible loss is the smaller of adjusted basis or decline in FMV. For the home, basis ($260K) is far higher than the decline ($80K), so the decline caps the loss.

**What if Hurricane Helene hadn't been federally declared?** Then Section A would not be available (IRC §165(h)(5), through 2025). The $20,900 deduction would disappear. This is why FEMA verification is the FIRST thing to check before filing Section A.

**What documentation does Carlos need to retain?**
1. FEMA registration confirmation (proves he was in the declared zone)
2. Insurance claim correspondence (proves the $50K + $11K were the final settlements)
3. Pre-storm and post-storm appraisals on the home (substantiate FMV figures)
4. Kelley Blue Book pre-storm valuation (substantiate vehicle FMV)
5. Receipts establishing basis: original closing statement + improvement receipts
6. Photos of pre-storm condition (if available) and post-storm damage
7. Repair estimates / contractor invoices (corroborate the FMV decline)

Retain for at least 3 years post-filing. Florida hurricane claims often draw IRS scrutiny — Carlos should be prepared.
