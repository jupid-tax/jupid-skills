# Example — Self-Employed Consultant in Mexico (The SE Tax Trap)

## Facts

- **Filer**: Jordan Reyes, US citizen, single, age 41
- **Tax year**: 2025
- **Occupation**: Independent management consultant; Schedule C business
- **Tax home**: Mexico City, Mexico — established March 1, 2024 on a Mexican Temporary Resident visa (4-year), continuous residence since
- **Tax compliance in Mexico**: Files Mexican RFC and pays Mexican ISR (Impuesto Sobre la Renta) under the "personas físicas con actividad empresarial" regime; treated as a Mexican tax resident
- **Income**: $80,000 USD net profit from Schedule C — all clients are foreign companies (one in Spain, two in Mexico, one in Brazil); all consulting work performed at his home office in Mexico City or at client sites in Latin America
- **Schedule C details**:
  - Gross receipts: $95,000
  - Business expenses: $15,000 (software subscriptions $4K, contractor help $6K, business travel within Latin America $3K, internet/phone $2K)
  - Net profit (Schedule C line 31): $80,000
- **Foreign housing expenses**: $9,600 rent (paid by Jordan) + $1,200 utilities = $10,800
- **No US-source income**; no days in the United States in 2025 (confirm with the user before using line 14)
- **Mexican income tax**: $17,000 for 2025 (persona assumption; in a real case ask for the ISR shown on the Mexican annual return, converted to USD)
- **No prior FEIE election** — first year claiming
- **State of domicile**: Florida (no state tax; left New Jersey in 2022)

## Analysis

### Eligibility check

- US citizen — eligible
- Tax home in Mexico City — yes, established 2024 with Temporary Resident visa, RFC, Mexican tax filing
- Abode is NOT in the US
- Pay is not from the U.S. Government (IRC §911(b)(1)(B)(ii)); no time in Cuba (IRC §911(d)(8))

Eligible.

### Test selection — Bona Fide Residence

For tax year 2025, Jordan has been in Mexico continuously since March 2024.

- For 2025: his uninterrupted residence includes the entire tax year (January 1–December 31, 2025), so the bona fide residence test is met for all 365 days (IRC §911(d)(1)(A)).
- For 2024: once the residence includes a full tax year, the partial first year also qualifies, limited to the days in the qualifying period (i2555 line 31 example). March 1–December 31, 2024 is 306 of 366 days. Because he filed 2024 without the exclusion, he can claim a prorated 2024 exclusion on Form 1040-X (i2555 "When to claim the exclusion(s)"). Ask whether he wants to; if he amends 2024, line 6a on the 2025 form shows 2024 instead of the line 6b "never filed" box.

Use Part II (BFR). Jordan did not submit a statement of nonresidence to Mexican authorities (line 13a = No) and is required to pay Mexican income tax (line 13b = Yes), so the line 13 disqualifier does not apply. He holds a residence visa and has integrated.

### FEIE cap (2025)

$130,000 (full year — no pro-ration since the qualifying period covers all 365 days of 2025; 2025 Form 2555 line 37; Rev. Proc. 2024-40 §2.39).

### Foreign earned income (Schedule C)

- Consulting is personal services; capital is not a material income-producing factor, so the **entire gross income** of the business is earned income (i2555 line 20). Line 20a = gross receipts, **$95,000**, not the $80,000 net profit
- All services performed in Mexico (or Latin American client sites — still foreign-source, services performed outside US)
- The $15,000 of Schedule C expenses comes back in on line 44 as deductions allocable to the excluded income (i2555 line 44)

**Line 20a: $95,000. Lines 24, 26, 27 (foreign earned income): $95,000**

### Foreign earned income exclusion

- Line 37 (max exclusion): $130,000; line 38: 365; line 39: 1.000; line 40: $130,000
- Line 41 (line 27 − line 36 housing exclusion of $0): $95,000
- Line 42 (smaller of line 40 or line 41): **$95,000**
- Line 43 (line 36 + line 42): $95,000
- Line 44 (deductions allocable to excluded income): all of his foreign earned income is excluded ($95,000 ÷ $95,000), so all definitely related deductions are allocable: Schedule C expenses $15,000 + deductible part of SE tax $5,652 (Schedule SE below) = **$20,652** (i2555 line 44; Pub. 54 ch. 5). Both stay in full on Schedule C and Schedule 1 line 15; line 44 removes them from the exclusion instead
- Line 45 (line 43 − line 44): **$74,348** → Schedule 1 line 8d as a negative amount

### Foreign housing (Part VI test, Part IX deduction)

Jordan is **self-employed** (Schedule C). A self-employed filer still runs the Part VI computation; with all foreign earned income from self-employment, lines 34–35 are skipped, line 36 (exclusion) is $0, and any benefit is a **deduction** figured in Part IX (i2555 line 34).

Housing amount check:

- Line 28 housing expenses: $10,800
- Line 29b limit: Mexico City is listed in Notice 2025-16 at **$47,900** for a full year (line 29a: Mexico City, Mexico)
- Line 30: lesser of $10,800 or $47,900 = $10,800
- Line 32 base: $20,800 (365 days; 2025 Form 2555 line 32)
- Line 33: $10,800 − $20,800 = −$10,000 → zero or less, so the rest of Part VI and all of Part IX are not completed (form text, line 33)

**No housing exclusion or deduction.** Answer "No" to the Part V housing question and go to Part VII. Common situation in lower-cost locations where rent is below the base amount.

### THE SE TAX TRAP

This is the central lesson of this example.

**FEIE excludes income from federal INCOME tax (IRC §911) but does NOT reduce self-employment tax: net earnings from self-employment are computed without the §911 exclusion (IRC §1402(a)(11); 2025 Instructions for Schedule SE: "Foreign earnings from self-employment can't be reduced by your foreign earned income exclusion when computing SE tax").**

Schedule SE is computed on the full net profit, not the post-FEIE amount.

2025 Schedule SE for Jordan:

- Line 2 / line 3: $80,000 (Schedule C line 31)
- Line 4a: $80,000 × 92.35% = **$73,880**; lines 4c and 6: $73,880
- Line 7: $176,100 (2025 maximum); no wages, so line 9 = $176,100
- Line 10 (12.4% of the smaller of line 6 or line 9): $73,880 × 0.124 = **$9,161**
- Line 11 (2.9% of line 6): $73,880 × 0.029 = **$2,143**
- **Line 12, total SE tax: $11,304** → Schedule 2 line 4

**Deduction for half SE tax** (Schedule SE line 13 → Schedule 1 line 15): $11,304 × 50% = **$5,652**

### No US-Mexico Totalization Agreement in force

Mexico is not on the list of countries with a US social security agreement in force: neither in the 2025 Instructions for Schedule SE ("U.S. Citizens or Resident Aliens Living Outside the United States", Exception) nor on SSA's list of agreements and their entry-into-force dates (https://www.ssa.gov/international/agreements_overview.html, checked 2026-10-06). So there is no certificate-of-coverage exemption: Jordan owes US SE tax on the full net profit, whatever he pays into Mexican social security (IMSS).

Re-check the SSA list each year. If an agreement enters into force, the exemption requires a coverage statement from the foreign agency attached to the return in place of Schedule SE, with "Exempt, see attached statement" on Schedule 2 line 4 (2025 Instructions for Schedule SE).

**Bottom line: $11,304 of US SE tax, even though all of his foreign earned income was excluded from income tax.**

### Income tax computation

- Schedule 1 line 3 (Schedule C): $80,000
- Schedule 1 line 8d (Form 2555 line 45, negative): −$74,348 → line 9: −$74,348; line 10: $5,652 → Form 1040 line 8
- Form 1040 line 9 (total income): $5,652
- Schedule 1 line 15 (half SE tax deduction): $5,652 → Form 1040 line 10
- Schedule 1 line 24j (housing deduction): $0
- Form 1040 line 11a (AGI): $5,652 − $5,652 = **$0**
- Line 12e standard deduction $15,750 (2025, single); line 15 taxable income: **$0**
- Foreign Earned Income Tax Worksheet: not completed because line 15 is zero (2025 Instructions for Form 1040, line 16)
- **Federal income tax: $0**

But:
- **Self-employment tax: $11,304** (Schedule 2 line 4 → line 21 → Form 1040 line 23)
- Additional Medicare tax (0.9% on SE earnings over $200K single): $0 (Jordan is below threshold)

**Total federal tax owed: $11,304** (all SE tax, no income tax)

### Mexican income tax

Jordan also pays Mexican ISR on the same consulting income: $17,000 under the persona assumption. Do not estimate Mexican tax; take it from his Mexican return.

### Foreign Tax Credit?

No credit or deduction is allowed for foreign tax on income the filer excludes (Pub. 54 ch. 4, "Foreign tax credit or deduction"; Reg. §1.911-6). Since 100% of Jordan's foreign earned income is excluded, all of his Mexican income tax relates to excluded income → no FTC available on Form 1116.

**Result**: Jordan paid Mexican income tax ($17,000 assumed) AND US SE tax ($11,304) — total $28,304 — on the same consulting income. No relief from this double tax burden via Form 1116 because the FEIE election excludes all of the income the Mexican tax was paid on.

### Should Jordan have used Form 1116 (FTC) instead?

Alternative scenario: skip FEIE, use Form 1116 for FTC on the Mexican tax paid (2025 single figures).

- AGI: $80,000 − $5,652 (half SE tax) = $74,348
- Taxable income: $74,348 − $15,750 standard deduction = $58,598 (no qualified business income deduction: the business is conducted in Mexico, and QBI excludes income not effectively connected with a US trade or business, Reg. §1.199A-3(b)(1))
- US income tax: $7,801 (2025 Tax Table, single, $58,550–$58,600 row)
- FTC: all of his income is foreign source, so the limit is the full US tax; credit = lesser of $7,801 or $17,000 Mexican tax = $7,801
- Net US income tax: $0
- US SE tax: $11,304 (same as above; the FTC does not reduce SE tax)
- Total US: $11,304
- Mexican tax: $17,000
- **Combined: $28,304** — the same as with the FEIE.

The FTC route leaves $9,199 of unused foreign tax ($17,000 − $7,801), which carries back 1 year and forward 10 years (IRC §904(c)). This could be valuable in future years if Jordan has US-taxable income in the same category.

**Verdict**: in Jordan's case, FEIE and FTC produce identical 2025 outcomes. FTC has a long-term advantage via the carryover. For SE consultants in countries that tax at or above US rates, FTC may be the better long-term choice — but once the FEIE is elected, claiming the FTC in a later year is treated as revoking it, which triggers the 5-year re-election lock-out (Pub. 54, "Effect of Revoking the Exclusions"; IRC §911(e)(2)). Present both computations to the user and route the choice to a CPA.

### State tax (Florida)

No state income tax. No state coordination.

If Jordan were domiciled in California, California would add the excluded income back and tax it; see [`../references/state-tax-coordination.md`](../references/state-tax-coordination.md). Compute California tax from the current Form 540 instructions rather than estimating.

## Form 2555 draft (key lines)

| Line | Field | Value |
|------|-------|-------|
| 1 | Foreign address | Calle Orizaba 100, Roma Norte, 06700 Ciudad de México, Mexico |
| 2 | Occupation | Management consultant |
| 3 | Employer's name | Self |
| 4a / 4b | Employer's U.S. / foreign address | N/A |
| 5 | Employer is | c Self |
| 6a / 6b | Last year filed / never filed | 6b checked (first year; changes if 2024 is amended) |
| 6c | Ever revoked either exclusion | No |
| 7 | Country of citizenship | United States |
| 8a | Separate foreign residence for family | No |
| 9 | Tax home and date established | Mexico City, Mexico, 03/01/2024 |
| 10 | Bona fide residence began / ended | 03/01/2024 / Continues |
| 11 | Living quarters | b Rented house or apartment |
| 12a | Family lived with you abroad | No |
| 13a | Statement of nonresidence submitted to Mexican authorities | No |
| 13b | Required to pay income tax to Mexico | Yes (Mexican RFC, ISR) |
| 14 | U.S. presence table | None (no U.S. days in 2025; confirm) |
| 15a | Contractual terms on length of employment | N/A (self-employed) |
| 15b | Visa type | Mexican Temporary Resident |
| 15c | Visa limited stay or employment | Ask; if Yes (4-year temporary residence), attach explanation |
| 15d | Maintained a US home | No (confirm; a US home bears on abode and residence) |
| 20a | Personal services in a business or profession | $95,000 |
| 24 / 26 | Total / foreign earned income | $95,000 |
| 27 | Amount from line 26 | $95,000 |
| Part V | Claiming housing exclusion or deduction | No (line 33 would be −$10,000) |
| 37 | Maximum exclusion | $130,000 |
| 38 / 39 | Days / ratio | 365 / 1.000 |
| 40 | Line 37 × line 39 | $130,000 |
| 41 | Line 27 − line 36 | $95,000 |
| 42 | Foreign earned income exclusion | $95,000 |
| 43 | Lines 36 + 42 | $95,000 |
| 44 | Deductions allocable to excluded income | $20,652 (Schedule C expenses $15,000 + half SE tax $5,652; computation attached) |
| 45 | To Schedule 1 line 8d (negative) | $74,348 |
| 46–50 | Part IX | Not completed (no housing amount) |

## Required attachments

- [x] Form 2555 (this draft) — line 45 $74,348, with the line 44 computation
- [x] **Schedule SE** — full $80,000 net profit, $11,304 SE tax owed (THE TRAP)
- [x] Schedule C — gross receipts $95,000, expenses $15,000, net $80,000
- [x] Schedule 1 — line 3: $80,000; line 8d: −$74,348 (Form 2555 line 45); line 15: $5,652 (half SE tax deduction)
- [x] Schedule 2 — line 4: $11,304 (SE tax)
- [ ] Statement for the June 15 automatic extension, if he files after April 15 (i2555 "When To File")
- [ ] Form 1116 — not needed (no creditable foreign tax with full FEIE election)
- [ ] FBAR / FinCEN 114 separately if Mexican bank account aggregate exceeded $10,000

## Lessons

1. **THE SE TAX TRAP**: this is the most critical lesson. FEIE excludes income from income tax — NOT from self-employment tax. Jordan owes $11,304 of US SE tax even though all of his foreign earned income was excluded. **Always verify Schedule SE is completed on the full net profit**, and check that the software has not dropped Schedule SE because the exclusion zeroed out taxable income.
2. **Totalization Agreements** are the only way to avoid US SE tax on excluded SE income. Verify the agreement is in force for the country (SSA list; Schedule SE instructions), verify the filer is covered by that country's social security under the agreement's rules, and obtain a certificate of coverage. Mexico has none.
3. **Self-employed FEI is gross income, not net profit**: when capital is not a material income-producing factor, line 20a is the entire gross income ($95,000), and the Schedule C expenses and the deductible part of SE tax allocable to the excluded income go on line 44 (i2555 lines 20 and 44). The result (line 45 $74,348 plus the $5,652 SE deduction) still removes exactly the $80,000 net profit from AGI.
4. **Housing deduction often = $0**: in lower-cost locations, the base amount ($20,800 for 2025) exceeds typical housing costs, and a higher location limit (Mexico City $47,900) does not help when expenses are below the base. The deduction only kicks in for expensive housing.
5. **FEIE vs. FTC for SE filers**: in countries that tax at or above US rates, FTC may be more efficient long-term (unused credit carries back 1 year and forward 10). FEIE is simpler. The 5-year re-election lock-out after a revocation (§911(e)(2)) makes switching costly.
6. **Mexican tax + US SE tax double-burdens** the income. Plan cash flow accordingly. The myth of "tax-free expat life" doesn't apply to self-employed expats in normal-tax countries.

## Citations

- IRC §911(a) — exclusion from gross income (income tax only)
- IRC §911(b)(1)(B)(ii), §911(d)(8) — U.S. Government pay; Cuba
- IRC §911(d)(1)(A) — bona fide residence test
- IRC §911(d)(6) — no deduction allocable to excluded income (line 44)
- IRC §1401-1402; §1402(a)(11) — self-employment tax (NOT reduced by §911)
- IRC §911(e)(2) — 5-year re-election lock-out after revocation
- IRC §904(c) — foreign tax credit carryback (1 year) and carryforward (10 years)
- Reg. §1.911-6 — disallowance of deductions, exclusions and credits allocable to excluded income
- Reg. §1.199A-3(b)(1) — QBI excludes income not effectively connected with a US trade or business
- 2025 Form 2555 and Instructions (lines 13a–13b, 20, 31 example, 32, 33, 34, 37–45; "When to claim the exclusion(s)")
- Rev. Proc. 2024-40 §2.39 — 2025 FEIE cap $130,000
- Notice 2025-16 — 2025 housing limit for Mexico City, $47,900
- 2025 Schedule SE (lines 4a, 7, 10–13) and Instructions — $176,100 wage base; FEIE does not reduce SE earnings; list of social security agreements
- 2025 Instructions for Form 1040 — $15,750 single standard deduction; Tax Table; Foreign Earned Income Tax Worksheet
- SSA, U.S. International Social Security Agreements (https://www.ssa.gov/international/agreements_overview.html) — Mexico not listed
- Pub. 54 (Rev. December 2025) — Tax Guide for U.S. Citizens and Resident Aliens Abroad (ch. 4 foreign tax credit and revocation; ch. 5 items related to excluded income)
- Pub. 334 — Tax Guide for Small Business
