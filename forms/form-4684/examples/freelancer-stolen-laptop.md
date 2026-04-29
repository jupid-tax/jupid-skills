# Example: Freelancer Whose Business Laptop Was Stolen

A complete walkthrough of Form 4684 Section B for a theft loss to property used 100% in a trade or business. Pattern: small loss, no insurance, no AGI floor, ordinary loss flowing to Form 4797.

## The filer

- **Name**: Priya Shah
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Business**: Freelance technical writing (Schedule C)
- **Event**: Laptop stolen from a coworking space, October 2025
- **Property**: 16-inch MacBook Pro

The laptop was used 100% for Priya's business — she had a separate personal laptop at home. The theft is reported under Section B because the property is trade/business. Section A would not apply even if she wanted (post-TCJA personal-use theft is not deductible at all).

## Why Section B (not Section A)

The most common confusion: "I lost personal property; isn't this Section A?" The classification depends on how the property was **used**, not where it was used.

- Property used 100% in a Schedule C business → **Section B, column (b)(i) trade or business**
- No floors apply
- Loss flows to **Form 4797 Part II Line 14** as an ordinary loss

If the laptop had been mixed-use (60% business, 40% personal), Priya would split:
- 60% to Section B
- 40% to Section A — but Section A is NOT available for theft of personal property post-TCJA, so the 40% is just lost economically

For this example, 100% business use → all Section B.

## Inputs gathered

### AGI

Single, AGI = $74,000 for 2025. (Not relevant to Section B computation, but agent confirmed for completeness.)

### Property

- **Description**: 16" MacBook Pro M3 Pro, purchased Feb 2024
- **Purchase price**: $2,800 (bought for the business)
- **§179 election in 2024**: Priya expensed the full $2,800 under §179 on her 2024 Schedule C / Form 4562
- **Adjusted basis after §179**: $2,800 − $2,800 = **$0**
- **FMV before**: ~$2,500 (used MacBook Pros depreciate; real-world value Oct 2025)
- **FMV after**: $0 (gone)
- **Decline in FMV**: $2,500
- **Insurance**: NONE. Coworking space had a renters/liability policy that excluded theft of customer items. Priya had no business property insurance.
- **Police report**: filed; case # 2025-OCT-1234

### Recapture from §179 — important

When property fully expensed under §179 is disposed of (sold, abandoned, stolen), the original §179 deduction can be subject to recapture if business use drops below 50%. But for theft, §179 recapture rules don't apply in the same way — the property is destroyed/stolen, not converted to personal use.

The mechanic on Form 4684 Section B for §179'd property:
- Adjusted basis = original cost − §179 expensed = $2,800 − $2,800 = $0
- Loss is the smaller of basis ($0) or decline in FMV ($2,500) = **$0**

Wait — this seems wrong. Let me re-examine.

Actually, for fully §179'd property that's stolen, the loss is the adjusted basis (which is $0 because the deduction was already taken). Priya **cannot** claim a second deduction via Form 4684 — she already deducted the laptop's full cost in 2024.

If the laptop had NOT been §179'd (i.e., depreciated under MACRS over 5 years):
- After ~1.7 years of depreciation, accumulated depreciation might be ~$1,400 (illustrative)
- Adjusted basis = $2,800 − $1,400 = $1,400
- Smaller of basis ($1,400) or decline ($2,500) = $1,400
- Loss = $1,400

Or if Priya bought a NEW laptop in 2025 (post-§179'd one) and that new laptop was stolen:
- Purchased June 2025 for $2,800
- Used 100% for business, no §179 yet (planned to claim it on 2025 return — but it was stolen first)
- Adjusted basis = $2,800
- Smaller of basis ($2,800) or decline ($2,500) = $2,500
- Loss = $2,500

For this example, let's assume Priya bought the laptop in **June 2025** (so it hadn't been §179'd yet — the question of §179 vs. casualty deduction comes up at filing time). Adjusted basis = full $2,800.

Updating the inputs:

- **Description**: 16" MacBook Pro M3 Pro, purchased June 2025
- **Purchase price**: $2,800
- **Adjusted basis**: $2,800 (no depreciation taken yet; held < 1 year)
- **FMV before theft**: $2,500
- **FMV after theft**: $0
- **Decline in FMV**: $2,500
- **Smaller of basis or decline**: smaller of $2,800 or $2,500 = **$2,500**
- **Insurance**: $0
- **Loss after insurance**: **$2,500**

This is the actual deduction. Note that Priya is BETTER OFF claiming the casualty/theft loss on Form 4684 than she would be claiming §179 on the laptop and then trying to deduct again — she can't double-dip.

### Holding period

Held < 1 year → short-term for Section B Part II classification.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Priya Shah
Identifying number: XXX-XX-XXXX
FEMA disaster declaration number: N/A (Section A not used)

## Section A — Personal-Use Property
N/A — property used 100% in trade/business

## Section B — Business and Income-Producing Property

### Part I — Per-item gain/loss

| Line | Description | Trade/Business (b)(i) | Income-Producing (b)(ii) |
|------|-------------|----------------------:|-------------------------:|
| 19 | Description | 16" MacBook Pro M3 Pro | N/A |
| 20 | Cost or other basis | $2,800 | — |
| 21 | Insurance/reimbursement | $0 | — |
| 22 | Gain (Line 21 − Line 20 if pos) | $0 | — |
| 23 | FMV before | $2,500 | — |
| 24 | FMV after | $0 | — |
| 25 | Decline (Line 23 − Line 24) | $2,500 | — |
| 26 | Smaller of Line 20 or Line 25 | $2,500 | — |
| 27 | Subtract Line 21 from Line 26 | $2,500 | — |

### Part II — Roll-up to other forms
| 28 | Total losses (sum of Line 27, ≤ 1 yr) | $2,500 |
| 32 | Total gains | $0 |
| 38 | Net business loss → Form 4797 Part II Line 14 | $2,500 |
| 39 | Net income-producing loss → Schedule A Line 16 | $0 |

## Section C — Theft (§1244 / Ponzi safe harbor)
N/A

## Section D — Election to Deduct in Preceding Year
N/A (Section D applies to Section A only)

## Required attachments
- [ ] Schedule A (no Section A loss, no Section B income-producing loss)
- [x] Form 4797 ($2,500 ordinary loss flows to Part II Line 14)
- [ ] Statement with FEMA disaster number (not applicable; theft is not a federal disaster)
- [x] Police report (case #2025-OCT-1234)
- [x] Receipt for laptop purchase (basis substantiation)
- [x] Bank/credit card record showing purchase
- [ ] FEMA registration (not applicable)

## Validation summary
- Math: all checks passed
  - Line 26 = smaller of basis ($2,800) or decline ($2,500) = $2,500
  - No floors applied (Section B has no $100 floor and no AGI floor)
  - Line 38 = $2,500 → flows to Form 4797
- Sanity:
  - 100% business use confirmed (Priya has separate personal laptop)
  - Police report obtained promptly after discovery
  - No insurance claim possible (no business property insurance)
  - Section A not used (theft of business property; personal-use theft would be barred under TCJA anyway)
  - Holding period: short-term (< 1 year)
- Insurance status: no claim filed (no coverage available)
- Next steps:
  - Complete Form 4797 Part II Line 14 with $2,500 ordinary loss
  - Schedule C net profit reduces by $2,500 indirectly through Form 4797 → reduces SE tax base
  - Consider business property insurance for replacement laptop going forward
  - Retain police report, purchase receipt, bank record for at least 3 years

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision
- IRS Pub 547 (Casualties, Disasters, and Thefts) — theft section
- IRS Pub 584-B (Business Casualty/Theft Workbook)
- IRS Form 4797 instructions (Part II ordinary loss)
- IRC §165(c)(1) — losses incurred in trade or business
- Reg. §1.165-7 — casualty losses
- Reg. §1.165-8 — theft losses
```

## Why each non-obvious choice

**Why Section B and not Section A?** The laptop was used 100% for business. Property classification follows USE, not personal/business of the owner. A laptop owned by an individual but used in their Schedule C business is business property → Section B. (And separately, post-TCJA personal-use theft is not deductible at all, so there's no Section A path even if Priya wanted one.)

**Why is the loss $2,500 and not $2,800?** The "smaller of" rule. Adjusted basis is $2,800 (purchase price, no depreciation, no §179 taken yet). Decline in FMV is $2,500 (the laptop was used for ~4 months and lost some value). The smaller is $2,500 → that's the deductible loss.

**Why no insurance reduction?** Priya didn't have business property insurance. The coworking space's policy excluded customer property. There's no "phantom" reimbursement to subtract because there's no policy.

**Why no $100 or 10% AGI floor?** Section B doesn't apply either. Those floors are Section A only (IRC §165(h)).

**Why does the loss flow to Form 4797 instead of directly reducing Schedule C?** This is a TIMING and CHARACTER question. Form 4797 Part II shows ordinary losses from involuntary conversions of property used in a trade/business held ≤ 1 year. The character is ordinary; the amount affects Form 1040 income directly via Schedule 1. Schedule C is for ongoing business income/expenses, not casualty losses on assets. Following the IRS-mandated path (4684 → 4797 → 1040) preserves correct character and trail.

**What if Priya had §179'd the laptop in 2025 already?** Adjusted basis would be $0 (fully expensed). Loss = smaller of $0 or $2,500 = $0. No Form 4684 deduction; the §179 already gave her the full benefit. Priya cannot double-deduct.

**What if Priya had used the laptop 70% business / 30% personal?**
- Business portion (70%): basis = $2,800 × 70% = $1,960; decline = $2,500 × 70% = $1,750; smaller = $1,750 → Section B
- Personal portion (30%): NOT deductible because it's a personal-use theft and post-TCJA personal theft losses are barred (no FEMA disaster could ever apply to a theft anyway)

So the deductible loss would be $1,750 instead of $2,500.

**Documentation Priya retains**:
1. Police report (case # 2025-OCT-1234) — proves the theft, dated and contemporaneous
2. Apple Store receipt or order confirmation showing $2,800 purchase
3. Credit card statement showing the charge (corroborates purchase)
4. Coworking space contract or correspondence (establishes the location of theft)
5. Photos of the laptop's serial number (if any)
6. Email to Apple about theft (sometimes Apple flags devices)
7. Schedule C from prior year showing the laptop was used in business (if depreciated previously)

Retain for at least 3 years post-filing.
