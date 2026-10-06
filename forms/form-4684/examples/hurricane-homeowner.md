# Example: Homeowner with Hurricane Damage in Federally Declared Zone

A complete walkthrough of Form 4684 Section A for a personal-use casualty in a federally declared disaster area. Pattern: significant loss, partial insurance, a major disaster that counts as a **qualified disaster** ($500 reduction, no 10% AGI floor, claimed on top of the standard deduction).

## The filer

- **Name**: Carlos Martinez
- **Filing status**: Married filing jointly
- **Tax year**: 2025 (filing in 2026)
- **Event**: hurricane, landfall June 28, 2025 (hypothetical event for this example)
- **Disaster**: FEMA major disaster declaration (DR) issued July 2025; FEMA incident period June 27 – July 2, 2025. The number is shown here as DR-XXXX; look up the real number and incident period at https://www.fema.gov/disaster/declarations before filing.
- **Property**: Single-family home in Florida + family vehicle

Both items damaged in the same event. Both classify as personal-use. Both fall under Section A because the disaster was federally declared.

## Is it a qualified disaster?

The agent checked both definitions, because P.L. 119-108 changed the rule after the 2025 instructions were printed:
- 2025 Instructions for Form 4684: major disaster declared January 1, 2020 – September 2, 2025, incident period beginning December 28, 2019 – July 4, 2025 and ending by August 3, 2025. Declared July 2025, incident period June 27 – July 2, 2025 → **qualifies**.
- IRC §165(h)(6) as added by P.L. 119-108 (Sept. 11, 2026), for tax years beginning after December 31, 2024: Stafford Act §401 major disaster with incident period beginning on or after December 28, 2019 and before January 1, 2027 → **qualifies**.

So the loss is a qualified disaster loss under either rule: $500 on line 11 instead of $100, no 10% AGI floor, and the net loss can be added to the standard deduction.

## Inputs gathered

### AGI

Carlos and his spouse filed jointly with **AGI = $135,000** for 2025 (Form 1040 line 11a).

### Property A: Home damage

- **Adjusted basis**: $260,000 (purchase price $230,000 + $30,000 of improvements; never rented or used for business)
- **FMV before**: $410,000 (appraiser estimate)
- **FMV after**: $330,000 (post-storm appraisal accounting for roof, water damage, structural issues; whole property, land and building as one item)
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
- Line 11: total of line 4 on all Forms 4684 is $0, smaller than line 10, so enter **$500** (qualified disaster loss; one event = one reduction)
- Line 12: $34,500 − $500 = **$34,000**

### Roll-up

- Line 13 (gains, line 4 of all Forms 4684): $0
- Line 14 (losses, line 12 of all Forms 4684): $34,000
- Line 15: line 13 is less than line 14 and the loss is a qualified disaster loss: smaller of ($34,000 − $0) or line 12 of this form ($34,000) = **$34,000 net qualified disaster loss** → Schedule A line 16
- All of Carlos's losses are qualified disaster losses, so lines 16–18 are not completed (no 10% AGI floor)

### Standard vs. itemized check

The agent ran the comparison:
- Itemized: state and local taxes paid $10,000 (property and sales tax; under the 2025 $40,000 cap) + mortgage interest $14,200 + charitable $3,500 + net qualified disaster loss $34,000 = **$61,700**
- Increased standard deduction: 2025 standard deduction MFJ $31,500 (2025 Form 1040) + net qualified disaster loss $34,000 = **$65,500**
- $65,500 > $61,700 → claim the increased standard deduction through Schedule A line 16

Schedule A line 16 dotted line: "Net Qualified Disaster Loss $34,000" and "Standard Deduction Claimed With Qualified Disaster Loss $31,500"; total $65,500 on Schedule A line 16 and Form 1040 line 12e (2025 Instructions for Form 4684, "Increased standard deduction reporting").

Tax effect (2025 MFJ Tax Table / Tax Computation Worksheet): taxable income $103,500 without the loss (tax $12,598) vs. $69,500 with it (tax $7,866) → about **$4,732** less federal tax.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Carlos Martinez and [Spouse]
Identifying number: XXX-XX-XXXX
Federally declared disaster box: checked; FEMA disaster declaration number: DR-XXXX (look up)

## Section A — Personal-Use Property (Federally Declared Disaster)

### Casualty/Theft #1: hurricane, 6/28/2025 (qualified disaster)

| Line | Description | Property A: Home | Property B: Vehicle |
|------|-------------|-----------------:|--------------------:|
| 1 | Description | Single-family home, [city], FL [ZIP of most affected property], acquired [date] | 2022 Toyota Sienna, [city], FL, acquired [date] |
| 2 | Cost or other basis | $260,000 | $26,000 |
| 3 | Insurance/reimbursement | $50,000 | $11,000 |
| 4 | Gain (Line 3 − Line 2 if pos) | $0 | $0 |
| 5 | FMV before casualty | $410,000 | $19,500 |
| 6 | FMV after casualty | $330,000 | $4,000 |
| 7 | Decline in FMV | $80,000 | $15,500 |
| 8 | Smaller of Line 2 or Line 7 | $80,000 | $15,500 |
| 9 | Subtract Line 3 from Line 8 (≥ 0) | $30,000 | $4,500 |
| 10 | Total casualty/theft loss | $34,500 |
| 11 | $500 (qualified disaster loss) | $500 |
| 12 | Subtract Line 11 from Line 10 | $34,000 |

### Roll-up across all Section A events
| 13 | Total gains (Line 4, all Forms 4684) | $0 |
| 14 | Total losses (Line 12, all Forms 4684) | $34,000 |
| 15 | Net qualified disaster loss → Schedule A Line 16 | $34,000 |
| 16 | Not completed (all losses are qualified disaster losses) | — |
| 17 | Not completed | — |
| 18 | Not completed | — |

## Section B — Business and Income-Producing Property
N/A (no business or income-producing losses)

## Section C — Ponzi-type scheme theft loss (Rev. Proc. 2009-20), Lines 40-51
N/A

## Section D — Election to Deduct in Preceding Year, Lines 52-57
[x] Not elected
[ ] Elected

## Required attachments
- [x] Schedule A (line 16: net qualified disaster loss $34,000 + standard deduction $31,500 = $65,500)
- [ ] Form 4797 (no business loss)
- [ ] Rev. Proc. 2018-08 safe-harbor statement (not used; FMV from appraisal and KBB)
- [ ] Police report (not applicable; not a theft)

Kept in the file, not attached: insurance settlement letters (homeowners, auto); pre-storm and post-storm appraisals (home); Kelley Blue Book pre-storm valuation (vehicle); FEMA registration confirmation.

## Validation summary
- Math: all checks passed
  - Line 8 = smaller of basis or decline: confirmed for both properties
  - Line 11 ($500) applied once for the single event; line 10 ($34,500) > total line 4 ($0)
  - Line 15 = smaller of (line 14 − line 13) or line 12 = $34,000
  - No 10% AGI floor (qualified disaster loss)
- Sanity:
  - FEMA declaration: major disaster (DR); incident period June 27 – July 2, 2025 falls inside both qualified-disaster definitions. Verify the actual number and dates at fema.gov.
  - Insurance fully resolved before filing (no pending claims)
  - Standard vs. itemized: increased standard deduction $65,500 beats itemizing $61,700
- Disaster-year election (Section D): NOT elected
  - 2025 benefit ≈ $4,732 vs. 2024 benefit ≈ $4,533 (see below)
- Insurance status: settled (homeowner $50K, auto $11K)
- Next steps:
  - Schedule A line 16 with both dotted-line entries; Form 1040 line 12e = $65,500
  - If the couple also files Form 6251, follow the instructions' rule for Form 6251 line 2a
  - Retain FEMA registration, insurance correspondence, appraisals for at least 3 years

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision (Qualified disaster loss; Increased standard deduction reporting; lines 11 and 15)
- IRS Pub 547 (Casualties, Disasters, and Thefts)
- IRS Pub 584 (Personal-Use Property Workbook)
- IRC §165(c)(3) — allowable personal casualty losses
- IRC §165(h)(1) — $100 per casualty, $500 for qualified disaster-related personal casualty losses
- IRC §165(h)(5) — federally declared disaster requirement
- IRC §165(h)(6) and §63(b)(8) — qualified net disaster loss, added by P.L. 119-108
- FEMA disaster declaration DR-XXXX (placeholder; look up)
```

## Why each non-obvious choice

**Why Section A and not Section B?** Carlos's home and vehicle are 100% personal-use. He doesn't run a business, doesn't rent the home, and doesn't drive the minivan for any business. Both are squarely Section A.

**Why the loss isn't $80,000 + $15,500 = $95,500?** Two reasons:
1. Insurance reimbursement is subtracted before any reduction — the loss must be net of compensation by insurance (IRC §165(a)).
2. Section A applies a per-event reduction, here $500 because it is a qualified disaster loss.

The path is: $80,000 + $15,500 (FMV decline, each smaller than basis) → minus $50,000 + $11,000 insurance = $34,500 → minus $500 = $34,000 → no 10% AGI floor.

**What if the disaster had not been a qualified disaster?** For example, an emergency declaration (EM) only. Then line 11 would be $100 (line 12 = $34,400), line 15 = $0, line 16 = $34,400, line 17 = 10% × $135,000 = $13,500, and line 18 = $20,900 to Schedule A line 15. Itemized total would be $10,000 + $14,200 + $3,500 + $20,900 = $48,600, still above the $31,500 standard deduction, but the tax saving would fall to about $2,704.

**Why didn't Carlos elect the disaster-year (§165(i)) election?** The agent computed both:
- Loss year (2025): $34,000 net qualified disaster loss on top of the $31,500 standard deduction; tax saving ≈ $4,732
- Prior year (2024): the hurricane also fits the qualified window that governs 2024 (declared by September 2, 2025; incident period began by July 4, 2025 and ended by August 3, 2025), so the same $34,000 would sit on top of the 2024 MFJ standard deduction of $29,200 with 2024 AGI of $128,000; tax saving ≈ $4,533

Claiming in 2025 saves about $199 more and avoids an amended return. The election deadline for this 2025 disaster-year loss is October 15, 2026. The agent flagged the option, computed the numbers, and let Carlos decide.

**Why is the reduction only applied once?** The hurricane is one casualty event. The reduction applies per event, not per damaged item. Even though both home and vehicle were damaged, it's still one event. (If Carlos had also had an unrelated kitchen fire that same year — a separate event — that would be a separate Form 4684 through line 12, and as a non-disaster loss it would be deductible only against personal casualty gains.)

**Why didn't Carlos use replacement cost?** Replacement cost is irrelevant under Reg. §1.165-7(b)(1). The deductible loss is the smaller of adjusted basis or decline in FMV. For the home, basis ($260K) is far higher than the decline ($80K), so the decline caps the loss.

**What if the hurricane hadn't been federally declared?** Then the loss would be deductible only to the extent of personal casualty gains (IRC §165(h)(5); Worksheet 1-1). Carlos has none, so the deduction would disappear. This is why FEMA verification is the FIRST thing to check before filing Section A.

**What documentation does Carlos need to retain?**
1. FEMA registration confirmation (proves he was in the declared zone)
2. Insurance claim correspondence (proves the $50K + $11K were the final settlements)
3. Pre-storm and post-storm appraisals on the home (substantiate FMV figures)
4. Kelley Blue Book pre-storm valuation (substantiate vehicle FMV)
5. Receipts establishing basis: original closing statement + improvement receipts
6. Photos of pre-storm condition (if available) and post-storm damage
7. Repair estimates / contractor invoices (corroborate the FMV decline)

Retain for at least 3 years post-filing.
