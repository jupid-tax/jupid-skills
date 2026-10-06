# Example — Digital Nomad Meeting Physical Presence Test

## Facts

- **Filer**: Maria Chen, US citizen, single, age 32
- **Tax year**: 2025
- **Occupation**: Independent software contractor; works remotely for a Berlin-based GmbH
- **Tax home**: She maintains her tax home in Lisbon, Portugal — long-term Airbnb (12-month lease executed in October 2024), Portuguese bank account, NIF (Portuguese tax ID)
- **Travel pattern during the qualifying 12-month period**:
  - October 1, 2024 → June 12, 2025: Lisbon, Portugal (255 days)
  - June 13, 2025 → July 22, 2025: Bali, Indonesia (40 days)
  - July 23, 2025 → August 5, 2025: Tokyo, Japan (14 days)
  - August 6, 2025 → August 18, 2025: visiting parents in Seattle, WA, USA (13 US days)
  - August 19, 2025 → September 30, 2025: Mexico City, Mexico (43 days)
- **Contractor fees**: $95,000 paid by Berlin GmbH for services performed during the qualifying period (gross receipts; no business expenses; translated from EUR at the exchange rates in effect when received, per the Form 2555 Part IV note)
- **Other income**: $3,200 in dividends from a US brokerage (taxable, not eligible for FEIE)
- **Foreign housing expenses**: $14,400 rent + $1,800 utilities (excluding telephone) = $16,200 total. She paid out of pocket (employer didn't reimburse)
- **State of domicile**: Washington State (no state income tax — left California in 2023, changed driver's license, sold car, etc.)
- **No prior FEIE election history** — first year claiming
- **No foreign income tax paid on this income in 2025** (persona assumption; in a real case ask, since a Portuguese tax resident normally owes Portuguese tax on work performed in Portugal)

## Analysis

### Eligibility check

- US citizen — eligible for FEIE
- Tax home in Lisbon (Portugal) — yes, established October 2024 with long-term lease, NIF, bank account, regular presence
- Abode is NOT in the US — she has no US residence; her home is Lisbon
- Not in a §901(j) sanctioned country
- Not a federal employee

Eligible.

### Test selection — Physical Presence Test

Maria can't use Bona Fide Residence for tax year 2025 because:
- She established Lisbon residence in October 2024
- October–December 2024 would count under BFR only if her residence went on to include all of 2025 (Pub. 54; i2555 line 31 example), which turns on the next point
- For 2025, BFR requires an uninterrupted period that includes the entire tax year as a bona fide resident — doubtful, since she files no Portuguese tax return and spent most of the summer in Bali, Tokyo, and Mexico City

Physical Presence Test (PPT) is the cleaner path — she just needs 330 full days outside the US in any 12-month window.

### Counting full days

12-month qualifying period: **October 1, 2024 → September 30, 2025** (365 days total).

- Oct 1, 2024 - June 12, 2025 in Lisbon: 255 full days abroad
- June 13 - July 22 in Bali: 40 full days abroad
- July 23 - Aug 5 in Tokyo: 14 full days abroad
- Aug 6 - Aug 18 in Seattle: **13 US days** (NOT counted abroad)
- Aug 19 - Sept 30 in Mexico: 43 full days abroad

Foreign full days: 255 + 40 + 14 + 43 = **352 full days outside the US**

Travel transition days: arrival/departure days are typically partial. To be conservative, drop one day at each transition (5 transitions × 1 day = 5 days). Even with that conservative adjustment: 347 days. Both well above the 330-day threshold.

**Result**: PPT passes by a comfortable margin.

### Pro-rated qualifying days in tax year 2025

Qualifying period: Oct 1, 2024 - Sept 30, 2025
Days of qualifying period that fall within tax year 2025: **Jan 1, 2025 - Sept 30, 2025 = 273 days**

Pro-ration ratio (line 39, rounded to three places): 273 / 365 = **0.748**

### FEIE cap (2025)

Per Rev. Proc. 2024-40: 2025 FEIE cap = **$130,000**

Pro-rated cap (line 40) = $130,000 × 0.748 = **$97,240**

Ask what happened after September 30, 2025: if she stayed abroad, a later 12-month window (for example one ending in 2026) may cover more of 2025 and raise the cap. This example keeps the window above.

### Foreign earned income

Contractor fees from Berlin GmbH for services performed during the qualifying period: $95,000 (Form 2555 line 20a: personal services, capital not a material income-producing factor, so the entire gross income is earned income — i2555 line 20)

(All services were performed in Lisbon / Bali / Tokyo / Mexico — no services performed in the US during the qualifying period. The 13 days in Seattle were vacation, no work performed.)

### Excludable amount

Excludable FEI (line 42) = lesser of ($97,240 pro-rated cap, $95,000 line 41) = **$95,000**

### Foreign housing exclusion

Maria is **self-employed** (independent contractor for Berlin GmbH; files Schedule C). Confirm the worker classification with the user; this example assumes self-employment. All of her foreign earned income is SE income, so lines 34–35 are skipped and line 36 (housing exclusion) is $0; any benefit would come through Part IX (housing **deduction**).

Part VI calculation (2025 form):

- Line 28 housing expenses: $16,200 (confirm they cover only the qualifying period)
- Line 29a: Lisbon, Portugal (listed in Notice 2025-16)
- Line 29b limit: Lisbon daily limit $109.59 × 273 days = $29,918 (Limit on Housing Expenses Worksheet; Notice 2025-16). Under the Notice 2026-25 §4 election it would be $122.74 × 273 = $33,508; it makes no difference here
- Line 30: lesser of $16,200 or $29,918 = $16,200
- Line 31: 273 days
- Line 32 base: $56.99 × 273 = $15,558
- Line 33 housing amount: $16,200 − $15,558 = **$642**
- Line 36: $0 (all SE income)

Part IX is completed only if line 27 is more than line 43. Line 43 is $95,000 (the FEIE excludes all of her foreign earned income), equal to line 27, so there is **no 2025 housing deduction** (IRC §911(c)(4)(B): the deduction can't exceed foreign earned income left after the exclusions). Flag the $642 for the CPA as a possible 1-year carryover question; the 2026 carryover worksheet starts from 2025 lines 46 and 48, which stay blank here.

### Total federal income tax exclusion

- Line 42 foreign earned income exclusion: $95,000
- Line 44 deductions allocable to excluded income: the deductible half of SE tax, $6,712. All of her SE income is excluded, so all of it is allocable (Pub. 54 ch. 5: "the deduction for self-employment tax is" allocable; i2555 line 44)
- Line 45: $95,000 − $6,712 = **$88,288** → Schedule 1 line 8d as a negative amount
- Housing deduction: $0

AGI: $95,000 Schedule C + $3,200 dividends − $88,288 (line 8d) − $6,712 (half SE tax, Schedule 1 line 15, reported in full) = **$3,200**.

### The SE tax trap — does NOT apply here in full

Self-employment tax (15.3% on net SE earnings) is NOT excluded by §911 — only income tax is excluded. Maria's $95,000 of self-employment income is still subject to SE tax on Schedule SE.

But: **Portugal-US Totalization Agreement** is in effect. If Maria has been paying Portuguese social security ("Segurança Social") and obtained a **Certificate of Coverage** from Portugal, she may be exempt from US SE tax on the same earnings. Verify her actual social security contribution status in Portugal. If she's NOT contributing to Portuguese social security, she remains subject to US SE tax.

For this example: assume Maria has NOT obtained a Certificate of Coverage (she's only been in Portugal a year, hasn't engaged with social security). She owes US SE tax on the full $95,000.

SE tax on Schedule SE:
- Net SE earnings: $95,000 × 0.9235 = $87,733
- SS portion (12.4% up to wage base $176,100 for 2025): $87,733 × 0.124 = **$10,879**
- Medicare portion (2.9%): $87,733 × 0.029 = **$2,544**
- Total SE tax: **$13,423**
- Deduction for half of SE tax (Schedule 1 line 15): $6,712

### Tax-stacking effect on dividends

The $3,200 in US-source dividends are NOT excluded. Under §911(f), the Foreign Earned Income Tax Worksheet taxes non-excluded income at the rates that would apply if the excluded income were included.

Here it does not bite: AGI is $3,200, below the $15,750 2025 standard deduction for a single filer, so Form 1040 line 15 (taxable income) is $0 and the worksheet instructions say not to complete it (2025 Instructions for Form 1040, line 16 worksheet). Federal income tax: **$0**.

Stacking matters once taxable income is above zero: if her dividends were $20,000, taxable income would be $4,250 and that $4,250 would be taxed as if it sat on top of the $88,288 on line 45, not from the bottom of the brackets.

### State tax (Washington)

Washington has no state income tax. No state coordination needed.

If Maria were domiciled in California, California would tax the income the FEIE excludes federally (see `../references/state-tax-coordination.md`).

### Coordination with Form 1116

No foreign income tax was paid (persona assumption). Form 1116 not needed.

If Maria had paid Portuguese tax on the $95,000, she'd need to allocate: tax paid on excluded income is NOT creditable; tax paid on non-excluded income (above the FEIE cap, or other foreign income) can be credited via Form 1116.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Apt 4B, Rua das Janelas Verdes 12, 1200-690 Lisboa, Portugal |
| 2 | Occupation | Software contractor |
| 3 | Employer's name | Self (contractor to Berlin GmbH) |
| 5 | Employer is | c Self |
| 6b | Never filed Form 2555 | Checked (first year) |
| 7 | Citizenship | United States |
| 8a | Separate foreign residence for family | No |
| 9 | Tax home | Lisbon, Portugal; established 10/01/2024 |
| 16 | 12-month period | 10/01/2024 through 09/30/2025 |
| 17 | Principal country of employment | Portugal |
| 18 | Travel table | Portugal 10/01/2024–06/12/2025; Indonesia 06/13–07/22/2025; Japan 07/23–08/05/2025; United States 08/06–08/18/2025 (no business days, $0); Mexico 08/19–09/30/2025. Full foreign days ≥ 347 (352 before dropping transition days) |
| 20a | Personal services in a business | $95,000 |
| 24 | Total | $95,000 |
| 26 / 27 | Foreign earned income | $95,000 |
| 28 | Qualified housing expenses | $16,200 |
| 29a / 29b | Location / limit | Lisbon, Portugal / $29,918 |
| 30 | Smaller of 28 or 29b | $16,200 |
| 31 | Qualifying days in 2025 | 273 |
| 32 | $56.99 × 273 | $15,558 |
| 33 | Housing amount | $642 |
| 34–35 | Employer-provided amounts / ratio | Skipped (all SE income) |
| 36 | Housing exclusion | $0 |
| 37 | Maximum exclusion | $130,000 |
| 38 | Days | 273 |
| 39 | Ratio | 0.748 |
| 40 | Prorated maximum | $97,240 |
| 41 | Line 27 − line 36 | $95,000 |
| 42 | Foreign earned income exclusion | $95,000 |
| 43 | Lines 36 + 42 | $95,000 |
| 44 | Deductions allocable to excluded income (half SE tax) | $6,712 |
| 45 | To Schedule 1 line 8d (negative) | $88,288 |
| 46–50 | Part IX | Not completed (line 27 is not more than line 43) |

## Required attachments

- [x] Form 2555 (this draft), with the line 44 computation
- [x] Schedule C (gross receipts $95,000) and Schedule SE (full $95,000 — SE tax $13,423, common trap)
- [x] Schedule 1 (line 8d −$88,288; line 15 $6,712 deduction for half SE tax)
- [ ] Form 1116 (not needed — no foreign tax paid)
- [ ] FBAR / FinCEN 114 separately if Portuguese bank account aggregate ever exceeded $10,000 during 2025

## Lessons

1. **Travel days matter**: Maria's 13 US days were under the 35-day buffer she had (35 = 365 - 330). One additional US trip of 25+ days would have killed PPT.
2. **Self-employment vs. employee**: same income exclusion, different housing mechanic — Part IX deduction vs. Part VI exclusion — and the deduction is capped at foreign earned income left after the FEIE, which here is $0. Verify worker classification.
3. **SE tax is NOT excluded**: $13,423 of US SE tax owed despite "no income tax". Plan cash flow for this.
4. **Totalization Agreements** can wipe out SE tax — verify whether the filer is contributing to the foreign social security system.
5. **Tax-stacking** applies only when Form 1040 line 15 is above zero. Here the standard deduction absorbs the $3,200 of dividends; with more non-excluded income, the stacking worksheet would tax it at the rates that apply on top of the excluded amount.
6. **Pro-ration** matters for first-year filers using PPT with a 12-month period that crosses the tax year boundary.

## Citations

- IRC §911(b)(2)(D) — annual exclusion cap (2025 $130,000 per Rev. Proc. 2024-40)
- IRC §911(d)(1)(B) — physical presence test
- IRC §911(c)(4)(B) — housing deduction limited to foreign earned income not excluded
- IRC §911(d)(6) — no deduction allocable to excluded income (line 44)
- IRC §911(f) — tax-stacking rule
- IRC §1402 — definition of net earnings from self-employment (SE tax base, no §911 exclusion)
- US-Portugal Totalization Agreement (effective August 1, 1989)
- Rev. Proc. 2024-40 — 2025 inflation-adjusted FEIE cap
- Notice 2025-16 — 2025 Lisbon housing limit ($40,000 / $109.59 per day); Notice 2026-25 §4 election
- 2025 Form 2555 and Instructions (lines 20, 29b, 32, 34, 39, 44; Part IX header)
- 2025 Instructions for Form 1040 — Foreign Earned Income Tax Worksheet
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
