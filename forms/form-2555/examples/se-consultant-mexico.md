# Example — Self-Employed Consultant in Mexico (The SE Tax Trap)

## Facts

- **Filer**: Jordan Reyes, US citizen, single, age 41
- **Tax year**: 2025
- **Occupation**: Independent management consultant; Schedule C business
- **Tax home**: Mexico City, Mexico — established March 1, 2024 on a Mexican Temporary Resident visa (4-year), continuous residence since
- **Tax compliance in Mexico**: Files Mexican RFC and pays Mexican ISR (Impuesto Sobre la Renta) under the "personas físicas con actividad empresarial" regime; treated as a Mexican tax resident
- **Income**: $80,000 USD net SE earnings from Schedule C — all clients are foreign companies (one in Spain, two in Mexico, one in Brazil); all consulting work performed at his home office in Mexico City or at client sites in Latin America
- **Schedule C details**:
  - Gross receipts: $95,000
  - Business expenses: $15,000 (software subscriptions $4K, contractor help $6K, business travel within Latin America $3K, internet/phone $2K)
  - Net SE income: $80,000
- **Foreign housing expenses**: $9,600 rent (paid by Jordan) + $1,200 utilities = $10,800
- **No US-source income**
- **No prior FEIE election** — first year claiming
- **State of domicile**: Florida (no state tax; left New Jersey in 2022)

## Analysis

### Eligibility check

- US citizen — eligible
- Tax home in Mexico City — yes, established 2024 with Temporary Resident visa, RFC, Mexican tax filing
- Abode is NOT in the US
- Not in §901(j) sanctioned country
- Not federal employee

Eligible.

### Test selection — Bona Fide Residence

For tax year 2025, Jordan has been in Mexico continuously since March 2024.

- For 2024: BFR did NOT cover entire tax year (only March-December). Jordan would need to use PPT for 2024 (likely qualifies if he had ≥330 foreign days in some 12-month window).
- For 2025: BFR covers all 365 days (he started BFR in 2024 and continued into 2025). BFR available.

Use Part II (BFR). Jordan files Mexican income tax as resident (Line 14 = Yes), didn't claim non-residence to Mexican authorities (Line 13 = No), holds residence visa, has integrated.

### FEIE cap (2025)

$130,000 (full year — no pro-ration since BFR covers entire 2025).

### Foreign earned income (Schedule C)

- Net Schedule C earnings: $80,000
- All services performed in Mexico (or Latin American client sites — still foreign-source, services performed outside US)
- All income is foreign-earned

**Line 24 (Total FEI): $80,000**

### Foreign earned income exclusion

- Line 37 (max exclusion): $130,000 (full year)
- Line 42 (earned income exclusion = lesser of $80,000 or $130,000): **$80,000**
- Line 45 (total to Schedule 1, before housing): $80,000

### Foreign housing deduction (Part IX — self-employed)

Jordan is **self-employed** (Schedule C). Housing goes through Part IX (housing **deduction**), NOT Part VI (which is for employees with employer-paid housing).

Housing deduction calculation:

- Housing expenses: $10,800
- Maximum housing amount (default; Mexico City is on the IRS high-cost list — verify current year's Notice; typical limit ~$48,000-$54,000 for Mexico City):
  - 2025 default max: 30% × $130,000 = $39,000
  - Mexico City adjusted max (illustrative, verify against current Notice): assume $39,000 (default — Mexico City may or may not be on the high-cost list in a given year)
- Lesser of expenses or max: $10,800
- Base housing amount: 16% × $130,000 = $20,800

Housing deduction = max(0, $10,800 - $20,800) = **$0**

**Jordan's housing expenses do NOT exceed the base amount** — no housing deduction available. Common situation in lower-cost countries where rent is below the 16% base threshold.

### THE SE TAX TRAP

This is the central lesson of this example.

**FEIE excludes income from federal INCOME tax (IRC §911) but does NOT exclude self-employment tax (IRC §1402).**

Schedule SE is computed on the FULL net SE earnings, not the post-FEIE amount.

Schedule SE for Jordan:

- Net SE earnings: $80,000
- Multiply by 0.9235 (the 92.35% adjustment): $80,000 × 0.9235 = **$73,880** (this is the SE tax base)
- Social Security portion (12.4% on first $176,100 for 2025): $73,880 × 0.124 = **$9,161**
- Medicare portion (2.9%): $73,880 × 0.029 = **$2,143**
- **Total SE tax: $11,304**

**Deduction for half SE tax** (Schedule 1 line 15): $11,304 / 2 = **$5,652**

### US-Mexico Totalization Agreement

The US and Mexico have a Totalization Agreement (effective October 1, 2024 — verify status and whether it applies for the 2025 tax year). If in effect:

- If Jordan is contributing to **IMSS** (Mexican social security) or paying social tax under the Mexican self-employment regime, he can obtain a **Certificate of Coverage** from Mexican authorities and become exempt from US SE tax on the same earnings.
- If Jordan is NOT contributing to Mexican social security (some self-employed regimes don't require it), the Totalization Agreement doesn't help — he owes US SE tax on the full $80,000.

For this example: assume the agreement is now in effect but Jordan has not yet obtained a Certificate of Coverage (he's been advised to do so for 2026 going forward). For 2025, he owes the full US SE tax.

**Bottom line: $11,304 of US SE tax, even though $80,000 of income tax was excluded.**

### Income tax computation

- Line 24 FEI: $80,000
- Schedule 1 Line 8d (FEIE negative): -$80,000
- Schedule 1 Line 15 (half SE tax deduction): -$5,652
- Schedule 1 Line 24h (housing deduction): $0
- Federal AGI: $0 - $5,652 = $0 (after standard deduction, $0 taxable income)
- **Federal income tax: $0**

But:
- **Self-employment tax: $11,304** (Schedule 2 Line 4)
- Additional Medicare tax (0.9% on SE earnings over $200K single): $0 (Jordan is below threshold)

**Total federal tax owed: $11,304** (all SE tax, no income tax)

### Mexican income tax

Jordan also pays Mexican ISR on the same $80,000 (or $95,000 gross, depending on the Mexican regime). Mexican ISR rates progress to ~35%; he likely owes $15,000-$20,000 to Mexico.

### Foreign Tax Credit?

Mexican income tax paid on excluded income is NOT creditable (Reg. §1.911-6 allocation). Since 100% of Jordan's SE income is excluded under FEIE, 100% of his Mexican income tax allocates to excluded income → no FTC available on Form 1116.

**Result**: Jordan paid Mexican income tax (~$17,000) AND US SE tax ($11,304) — total ~$28,000 — on the same $80,000 of income. No relief from this double tax burden via Form 1116 because the FEIE election allocates all tax to excluded income.

### Should Jordan have used Form 1116 (FTC) instead?

Alternative scenario: skip FEIE, use Form 1116 for FTC on the Mexican tax paid.

- US income tax on $80,000 (single, after standard deduction $14,600 → taxable $65,400): $9,432
- FTC: lesser of US tax on foreign income ($9,432) or Mexican tax paid (~$17,000) = $9,432
- Net US income tax: $0
- US SE tax: $11,304
- Total US: $11,304
- Mexican tax: $17,000
- **Combined: $28,304** — basically the same.

The FTC carries forward $7,568 of unused foreign tax (Mexican tax paid above the FTC limit). This could be valuable in future years if Jordan has US-taxable income.

**Verdict**: in Jordan's case, FEIE and FTC produce nearly identical 2025 outcomes. FTC has a slight long-term advantage via carryforward. For most SE consultants in higher-tax countries, FTC may be the better long-term choice — but switching from FEIE later triggers the 5-year lock-out.

### State tax (Florida)

No state income tax. No state coordination.

If Jordan were domiciled in California, he'd owe California tax on the full $80,000 (FEIE not honored). Roughly $5,000-$6,000 California tax.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Calle Orizaba 100, Roma Norte, 06700 Ciudad de México, Mexico |
| 2 | Occupation | Management consultant |
| 4d | Type | Self-employed |
| 5 | Last year FEIE claimed | None (first year) |
| 7 | Test used | Bona Fide Residence |
| 9 | Tax home | Mexico City, established 03/01/2024 |
| 10 | BFR start date | 03/01/2024 |
| 13 | Statement to Mexican authorities re non-resident | No |
| 14 | Required to pay Mexican income tax | Yes (Mexican RFC, ISR) |
| 21 | SE income share | $80,000 |
| 24 | Total foreign earned income | $80,000 |
| 27 | = Line 24 | $80,000 |
| 37 | Max exclusion (full year) | $130,000 |
| 42 | Earned income exclusion | $80,000 |
| 45 | Total exclusion to Schedule 1 | $80,000 |
| 51-53 | Housing deduction | $0 (expenses below base) |

## Required attachments

- [x] Form 2555 (this draft) — exclusion of $80,000
- [x] **Schedule SE** — full $80,000 SE tax computation, $11,304 owed (THE TRAP)
- [x] Schedule C — gross receipts $95,000, expenses $15,000, net $80,000
- [x] Schedule 1 — Line 8d: -$80,000 (FEIE); Line 15: -$5,652 (half SE tax deduction)
- [x] Schedule 2 — Line 4: $11,304 (SE tax)
- [ ] Form 1116 — not needed (no creditable foreign tax with full FEIE election)
- [ ] FBAR / FinCEN 114 separately if Mexican bank account aggregate exceeded $10,000

## Lessons

1. **THE SE TAX TRAP**: this is the most critical lesson. FEIE excludes income from income tax — NOT from self-employment tax. Jordan owes $11,304 of US SE tax even though he excluded $80,000 of income. **Always verify Schedule SE is completed on the full SE earnings.** Many tax software packages incorrectly zero out SE tax when FEIE is claimed — manual override may be needed.
2. **Totalization Agreements** are the only way to avoid US SE tax on excluded SE income. Verify the agreement exists for the country, verify the filer is contributing to that country's social security, and obtain a Certificate of Coverage.
3. **Schedule C expenses are deducted BEFORE the FEIE cap is applied**: Line 24 = net SE earnings ($80,000), not gross ($95,000). The §911 disallowance (Part VIII) doesn't double-disallow Schedule C ordinary business expenses — only deductions allocable to excluded income beyond Schedule C/SE business deductions (e.g., personal itemized deductions).
4. **Housing deduction often = $0**: in lower-cost countries, the 16% base amount ($20,800) exceeds typical housing costs. The deduction only kicks in for high-cost cities or expensive housing.
5. **FEIE vs. FTC for SE filers**: in high-tax countries, FTC may be more efficient long-term (carries forward unused credit). FEIE is simpler. The 5-year revocation lock-out (§911(e)(2)) makes switching costly.
6. **Mexican tax + US SE tax double-burdens** the income. Plan cash flow accordingly. The myth of "tax-free expat life" doesn't apply to self-employed expats in normal-tax countries.

## Citations

- IRC §911(a) — exclusion from gross income (income tax only)
- IRC §911(d)(1)(A) — bona fide residence test
- IRC §1401-1402 — self-employment tax (NOT excluded by §911)
- IRC §911(e)(2) — 5-year revocation lock-out
- Reg. §1.911-6 — allocation of deductions
- Rev. Proc. 2024-40 — 2025 FEIE cap $130,000
- Schedule SE instructions — explicit statement that FEIE-excluded SE income remains subject to SE tax
- US-Mexico Totalization Agreement (October 1, 2024 — verify current status)
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
- Pub. 334 — Tax Guide for Small Business
