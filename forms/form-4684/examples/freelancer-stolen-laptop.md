# Example: Freelancer Whose Business Laptop Was Stolen

A complete walkthrough of Form 4684 Section B for a theft loss to property used 100% in a trade or business. Pattern: small loss, no insurance, no AGI floor, ordinary loss flowing to Schedule 1 line 4 (Form 4797 is not otherwise required).

## The filer

- **Name**: Priya Shah
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Business**: Freelance technical writing (Schedule C)
- **Event**: Laptop stolen from a coworking space, discovered October 2025
- **Property**: 16-inch MacBook Pro

The laptop was used 100% for Priya's business — she had a separate personal laptop at home. The theft is reported under Section B because the property is trade/business property. A personal-use theft would not be deductible here: a theft is not attributable to a declared disaster, and she has no personal casualty gains (IRC §165(h)(5)).

## Why Section B (not Section A)

The most common confusion: "I lost personal property; isn't this Section A?" The classification depends on how the property was **used**, not where it was used.

- Property used 100% in a Schedule C business → **Section B**; in Part II it goes in column (b)(i), "trade, business, rental, or royalty property"
- No $100 reduction and no 10% AGI floor
- Held 1 year or less → line 29 → line 31 → Form 4797 line 14, or Schedule 1 line 4 when Form 4797 is not otherwise required (instructions for line 31)

If the laptop had been mixed-use (60% business, 40% personal), Priya would split:
- 60% to Section B
- 40% to Section A — not deductible, because a personal-use theft loss is allowed only if attributable to a declared disaster or against personal casualty gains

For this example, 100% business use → all Section B.

## Inputs gathered

### AGI

Single, AGI = $74,000 for 2025. (Not relevant to Section B computation, but agent confirmed for completeness.)

### Property

- **Description**: 16" MacBook Pro M3 Pro, purchased June 2025 for the business
- **Purchase price**: $2,800
- **Depreciation / §179**: none claimed. No depreciation and no special depreciation allowance is allowed for property placed in service and disposed of in the same tax year (2025 Instructions for Form 4562), so the theft loss is the only deduction for this laptop.
- **Adjusted basis**: **$2,800** (held less than 1 year)
- **FMV before theft**: $2,500 (used MacBook Pros depreciate; real-world value Oct 2025)
- **FMV after theft**: $0 (stolen, not recovered)
- **Decline in FMV**: $2,500
- **Line 26**: the laptop was stolen, so the form note says to enter the line 20 amount: **$2,800** (Reg. §1.165-7(b)(1) and Reg. §1.165-8(c): for business property totally lost, the loss is the adjusted basis)
- **Insurance**: NONE. Coworking space had a renters/liability policy that excluded theft of customer items. Priya had no business property insurance.
- **Loss after insurance**: $2,800 − $0 = **$2,800**
- **Police report**: filed; case # 2025-OCT-1234

### Holding period

Purchased June 2025, stolen October 2025 → held 1 year or less → Section B Part II line 29.

## The completed Form 4684 draft

```markdown
# Form 4684 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Priya Shah
Identifying number: XXX-XX-XXXX
Federally declared disaster box: not checked (Section A not used)

## Section A — Personal-Use Property
N/A — property used 100% in trade/business

## Section B — Business and Income-Producing Property

### Part I — Per-item gain/loss (one event)

| Line | Description | Property A |
|------|-------------|-----------:|
| 19 | Description | 16" MacBook Pro M3 Pro, [city, state], acquired 06/2025 |
| 20 | Cost or adjusted basis | $2,800 |
| 21 | Insurance/reimbursement | $0 |
| 22 | Gain (Line 21 − Line 20 if pos) | $0 |
| 23 | FMV before | $2,500 |
| 24 | FMV after | $0 |
| 25 | Decline (Line 23 − Line 24) | $2,500 |
| 26 | Stolen: enter Line 20 amount | $2,800 |
| 27 | Subtract Line 21 from Line 26 | $2,800 |
| 28 | Casualty or theft loss | $2,800 |

### Part II — Summary
| 29 | Laptop theft (held 1 year or less) | (b)(i) ($2,800) | (b)(ii) $0 | (c) $0 |
| 30 | Totals | ($2,800) | $0 | $0 |
| 31 | Line 30 (b)(i) + (c) → Schedule 1 line 4, "4684" box (Form 4797 not otherwise required) | ($2,800) |
| 32 | Line 30 (b)(ii) → Schedule A Line 16 | $0 |
| 33-39 | Property held more than 1 year | $0 |

## Section C — Ponzi-type scheme theft loss, Lines 40-51
N/A

## Section D — Election to Deduct in Preceding Year, Lines 52-57
N/A (a theft is not a federally declared disaster loss)

## Required attachments
- [ ] Schedule A (no Section A loss, no Section B income-producing loss)
- [ ] Form 4797 (not otherwise required; line 31 goes to Schedule 1 line 4)
- [ ] Rev. Proc. 2018-08 statement (not applicable)

Kept in the file, not attached: police report (case #2025-OCT-1234), receipt for laptop purchase (basis), bank/credit card record showing purchase.

## Validation summary
- Math: all checks passed
  - Line 26 = Line 20 ($2,800) because the property was stolen (form note on line 26)
  - No floors applied (Section B has no $100 reduction and no AGI floor)
  - Line 31 = ($2,800) → Schedule 1 line 4 with the "4684" box checked
- Sanity:
  - 100% business use confirmed (Priya has separate personal laptop)
  - No depreciation or §179 claimed on a laptop placed in service and stolen in 2025 (no double deduction)
  - Police report obtained promptly after discovery
  - No insurance claim possible (no business property insurance)
  - Section A not used (theft of business property)
  - Holding period: 1 year or less
- Insurance status: no claim filed (no coverage available)
- Next steps:
  - Schedule 1 line 4: ($2,800), "4684" box checked
  - The loss does not reduce Schedule C net profit or self-employment tax: losses from an involuntary conversion of business property are excluded from net earnings from self-employment (IRC §1402(a)(3)(C))
  - Consider business property insurance for replacement laptop going forward
  - Retain police report, purchase receipt, bank record for at least 3 years

## Sources cited in this draft
- IRS Form 4684, 2025 revision
- IRS Instructions for Form 4684, 2025 revision (lines 26, 28, 31)
- IRS Instructions for Form 4562, 2025 (property placed in service and disposed of in the same year)
- IRS Pub 547 (Casualties, Disasters, and Thefts) — theft section
- IRS Pub 584-B (Business Casualty/Theft Workbook)
- IRC §165(c)(1) — losses incurred in trade or business
- IRC §1402(a)(3)(C) — involuntary conversions excluded from self-employment income
- Reg. §1.165-7 — casualty losses
- Reg. §1.165-8 — theft losses
```

## Why each non-obvious choice

**Why Section B and not Section A?** The laptop was used 100% for business. Property classification follows USE, not personal/business of the owner. A laptop owned by an individual but used in their Schedule C business is business property → Section B. (A personal-use theft would have no Section A deduction here: no declared disaster, no personal casualty gains.)

**Why is the loss $2,800 and not $2,500?** For business property that is stolen or totally destroyed, line 26 is the adjusted basis from line 20 even when FMV before ($2,500) is lower (form note on line 26; Reg. §1.165-7(b)(1)). For partial damage to business property, the "smaller of" rule would apply instead.

**Why no insurance reduction?** Priya didn't have business property insurance. The coworking space's policy excluded customer property. There's no "phantom" reimbursement to subtract because there's no policy.

**Why no $100 or 10% AGI floor?** Those reductions apply only to personal-use property (IRC §165(h); Pub. 547, "Deduction Limits").

**Why does the loss go to Schedule 1 instead of reducing Schedule C?** Form 4684 line 31 sends a net loss on property held 1 year or less to Form 4797 line 14, or to Schedule 1 line 4 when Form 4797 is not otherwise required. The character is ordinary; the amount reduces AGI through Schedule 1. Schedule C is for ongoing business income and expenses, not casualty losses on assets, and the loss does not reduce self-employment income (IRC §1402(a)(3)(C)).

**What if Priya had bought the laptop in 2024 and claimed §179 for it then?** Adjusted basis would be $0 (fully expensed). Line 26 = $0, so no Form 4684 deduction; the §179 already gave her the full benefit. If it had been depreciated under MACRS instead, line 20 would be cost minus depreciation allowed or allowable, and the holding period would be more than 1 year (line 34).

**What if Priya had used the laptop 70% business / 30% personal?**
- Business portion (70%): basis = $2,800 × 70% = $1,960; stolen business property → line 26 = $1,960 → Section B
- Personal portion (30%): not deductible, because a personal-use theft loss is allowed only if attributable to a declared disaster or against personal casualty gains

So the deductible loss would be $1,960 instead of $2,800.

**Documentation Priya retains**:
1. Police report (case # 2025-OCT-1234) — proves the theft, dated and contemporaneous
2. Apple Store receipt or order confirmation showing $2,800 purchase
3. Credit card statement showing the charge (corroborates purchase)
4. Coworking space contract or correspondence (establishes the location of theft)
5. Photos of the laptop's serial number (if any)
6. Email to Apple about theft (sometimes Apple flags devices)
7. Business records showing the laptop was used only in the business

Retain for at least 3 years post-filing.
