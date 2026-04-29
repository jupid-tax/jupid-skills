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
- **Wages**: $95,000 paid by Berlin GmbH for services performed during the qualifying period (translated from EUR at IRS yearly average rate)
- **Other income**: $3,200 in dividends from a US brokerage (taxable, not eligible for FEIE)
- **Foreign housing expenses**: $14,400 rent + $1,800 utilities (excluding telephone) = $16,200 total. She paid out of pocket (employer didn't reimburse)
- **State of domicile**: Washington State (no state income tax — left California in 2023, changed driver's license, sold car, etc.)
- **No prior FEIE election history** — first year claiming
- **No foreign tax paid** — Portugal's NHR regime exempts her foreign-source consulting income from Portuguese tax for 10 years

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
- For 2024, she didn't cover the entire tax year (only Oct-Dec) — BFR fails for 2024
- For 2025, BFR requires the entire tax year as a bona fide resident — possible, but she also doesn't file Portuguese tax returns under NHR (she's exempt), and her stays in Bali, Tokyo, and Mexico break "integration into Portuguese community"

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

Pro-ration ratio: 273 / 365 = **0.7479** (74.79%)

### FEIE cap (2025)

Per Rev. Proc. 2024-40: 2025 FEIE cap = **$130,000**

Pro-rated cap = $130,000 × 0.7479 = **$97,232**

### Foreign earned income

Wages from Berlin GmbH for services performed during qualifying period: $95,000

(All services were performed in Lisbon / Bali / Tokyo / Mexico — no services performed in the US during the qualifying period. The 13 days in Seattle were vacation, no work performed.)

### Excludable amount

Excludable FEI = lesser of ($95,000 actual FEI, $97,232 pro-rated cap) = **$95,000**

### Foreign housing exclusion

Maria is **self-employed** (independent contractor; receives 1099-NEC equivalents from Berlin GmbH; files Schedule C). So housing goes through Part IX (housing **deduction**), not Part VI (housing exclusion for employees).

Wait — Berlin GmbH treats her as an independent contractor, not an employee. Confirm with the user. For this example, assume self-employment.

Foreign housing deduction calculation:

- Housing expenses: $16,200
- Maximum housing amount (default; Lisbon is not on the IRS high-cost city list): 30% × $130,000 × 0.7479 = $29,168
- Lesser of expenses or max: $16,200
- Base housing amount: 16% × $130,000 × 0.7479 = $15,556
- Housing deduction = $16,200 - $15,556 = **$644**

Small benefit — but every dollar counts. Housing deduction flows to Schedule 1 Line 24h (verify current line for tax year).

### Total federal income tax exclusion

- Foreign earned income exclusion: $95,000 (Schedule 1 negative adjustment)
- Foreign housing deduction: $644 (Schedule 1 above-the-line deduction)

Combined: $95,644 reduction in federal AGI.

### The SE tax trap — does NOT apply here in full

Self-employment tax (15.3% on net SE earnings) is NOT excluded by §911 — only income tax is excluded. Maria's $95,000 of self-employment income is still subject to SE tax on Schedule SE.

But: **Portugal-US Totalization Agreement** is in effect. If Maria has been paying Portuguese social security ("Segurança Social") and obtained a **Certificate of Coverage** from Portugal, she may be exempt from US SE tax on the same earnings. Under the NHR regime, this is more nuanced — verify her actual social security contribution status in Portugal. If she's NOT contributing to Portuguese social security, she remains subject to US SE tax.

For this example: assume Maria has NOT obtained a Certificate of Coverage (she's only been in Portugal a year, hasn't engaged with social security). She owes US SE tax on the full $95,000.

SE tax on Schedule SE:
- Net SE earnings: $95,000 × 0.9235 = $87,733
- SS portion (12.4% up to wage base $176,100 for 2025): $87,733 × 0.124 = **$10,879**
- Medicare portion (2.9%): $87,733 × 0.029 = **$2,544**
- Total SE tax: **$13,423**
- Deduction for half of SE tax (Schedule 1 line 15): $6,712

### Tax-stacking effect on dividends

The $3,200 in US-source dividends are NOT excluded. Under §911(f) tax-stacking, they're taxed at the rate that would apply if FEIE income were included.

Without stacking: Maria's "taxable income" (after standard deduction) would put her in the 0% qualified dividend bracket (since her excluded wages are removed). Tax on dividends ≈ $0.

With stacking: Maria's tax bracket is computed as if the $95,000 wages were included. With $95,000 + $3,200 = $98,200 taxable income, the qualified dividend rate is 15%. Tax on dividends ≈ $480.

(Ordinary dividends would be even higher — taxed at the marginal ordinary rate.)

### State tax (Washington)

Washington has no state income tax. No state coordination needed.

If Maria were domiciled in California, she'd owe California tax on the full $95,000 + $3,200 = $98,200 (FEIE not honored).

### Coordination with Form 1116

No foreign tax was paid (Portugal NHR exemption). Form 1116 not needed.

If Maria had paid Portuguese tax on the $95,000, she'd need to allocate: tax paid on excluded income is NOT creditable; tax paid on non-excluded income (above the FEIE cap, or other foreign income) can be credited via Form 1116.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Apt 4B, Rua das Janelas Verdes 12, 1200-690 Lisboa, Portugal |
| 2 | Occupation | Software contractor |
| 4a-d | Employer | Berlin GmbH (foreign entity) |
| 5 | Last year FEIE claimed | None (first year) |
| 7 | Test used | Physical Presence |
| 9 | Tax home | Apt 4B, Rua das Janelas Verdes 12, Lisboa; established 10/01/2024 |
| 16 | 12-month qualifying period | 10/01/2024 - 09/30/2025 |
| 17 | Principal country | Portugal |
| 18 | Travel summary | Portugal 255, Indonesia 40, Japan 14, Mexico 43; total 352 |
| 19 | Wages, salary | $95,000 |
| 24 | Total foreign earned income | $95,000 |
| 27 | = Line 24 | $95,000 |
| 37 | Max exclusion (pro-rated) | $97,232 |
| 38 | Qualifying days in tax year | 273 |
| 39 | Tax year days | 365 |
| 40 | Ratio | 0.7479 |
| 42 | Earned income exclusion | $95,000 |
| 45 | Total to Schedule 1 (negative) | $95,000 |

Part IX (housing deduction):
- Lines 51-53: housing deduction $644

## Required attachments

- [x] Form 2555 (this draft)
- [x] Schedule SE (full $95,000 SE tax — common trap)
- [x] Schedule 1 (negative $95,000 from Form 2555 Line 45; $644 above-the-line housing deduction; $6,712 deduction for half SE tax)
- [ ] Form 1116 (not needed — no foreign tax paid)
- [ ] FBAR / FinCEN 114 separately if Portuguese bank account aggregate ever exceeded $10,000 during 2025

## Lessons

1. **Travel days matter**: Maria's 13 US days were under the 35-day buffer she had (35 = 365 - 330). One additional US trip of 25+ days would have killed PPT.
2. **Self-employment vs. employee**: same income exclusion, different mechanic — Part IX deduction vs. Part VI exclusion. Verify worker classification.
3. **SE tax is NOT excluded**: $13,423 of US SE tax owed despite "no income tax". Plan cash flow for this.
4. **Totalization Agreements** can wipe out SE tax — verify whether the filer is contributing to the foreign social security system.
5. **Tax-stacking** keeps the marginal rate on residual income at the rate that would apply without exclusion. The $3,200 of dividends is not "free" — it's taxed at 15%.
6. **Pro-ration** matters for first-year filers using PPT with a 12-month period that crosses the tax year boundary.

## Citations

- IRC §911(b)(2)(D) — annual exclusion cap (2025 $130,000 per Rev. Proc. 2024-40)
- IRC §911(d)(1)(B) — physical presence test
- IRC §911(c) — housing exclusion/deduction
- IRC §911(f) — tax-stacking rule
- IRC §1402 — definition of net earnings from self-employment (SE tax base, no §911 exclusion)
- US-Portugal Totalization Agreement (effective August 1, 1989)
- Rev. Proc. 2024-40 — 2025 inflation-adjusted FEIE cap
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
