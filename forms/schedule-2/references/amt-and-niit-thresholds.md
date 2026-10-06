# AMT, NIIT, and Additional Medicare Tax Thresholds

Schedule 2 routes results from three major income-driven taxes whose thresholds matter to the agent: AMT (Form 6251 → Schedule 2 Line 2), Net Investment Income Tax (Form 8960 → Schedule 2 Line 12), and Additional Medicare Tax (Form 8959 → Schedule 2 Line 11). This file lists thresholds, citations, and verification pointers.

## Alternative Minimum Tax (AMT) — IRC §55, §59

AMT is a parallel tax computation. The filer pays the *higher* of regular tax or AMT.

### AMT exemption amounts (2025)

Per Rev. Proc. 2024-40:

| Filing status | 2025 exemption | Phaseout begins | Phaseout complete |
|--------------|---------------:|----------------:|------------------:|
| Single / HoH | $88,100 | $626,350 | $978,750 |
| MFJ / QSS | $137,000 | $1,252,700 | $1,800,700 |
| MFS | $68,500 | $626,350 | $900,350 |
| Estate / Trust | $30,700 | $102,500 | $225,300 |

For 2025 the exemption phases out at 25 cents per dollar of AMTI above the phaseout threshold.

### AMT exemption amounts (2026)

Per Rev. Proc. 2025-32 §4.10 (reflecting P.L. 119-21):

| Filing status | 2026 exemption | Phaseout begins | Phaseout complete |
|--------------|---------------:|----------------:|------------------:|
| Single / HoH | $90,100 | $500,000 | $680,200 |
| MFJ / QSS | $140,200 | $1,000,000 | $1,280,400 |
| MFS | $70,100 | $500,000 | $640,200 |
| Estate / Trust | $31,400 | $104,800 | $167,600 |

From 2026 the exemption phases out at 50 cents per dollar of AMTI above the threshold (P.L. 119-21; the complete-phaseout amounts above reflect it).

### AMT rates

- 26% on the first $239,100 of Form 6251 line 6 for 2025 ($119,550 MFS); $244,500 for 2026 ($122,250 MFS)
- 28% above that amount

The 26%/28% break point is indexed annually under IRC §55(b)(1)(A); the rates themselves are statutory.

### Common AMT preference items (IRC §57) and adjustments (IRC §56)

Add back / preference for AMT:

- State and local taxes deducted on Schedule A, or the standard deduction if the filer didn't itemize (Form 6251 line 2a). For 2025, P.L. 119-21 raised the regular-tax SALT cap to $40,000 ($20,000 MFS), reduced when Form 1040 line 11b exceeds $500,000 (2025 Schedule A line 5e), so larger SALT add-backs are possible again
- Bargain element on ISO exercise (FMV at exercise − strike price), if held past year-end
- Private activity bond interest issued 2009–2010 (excluded under ARRA / TCJA in some cases — verify)
- Depreciation differences (regular MACRS vs AMT depreciation)
- Long-term contract income (different methods for AMT)
- Pre-TCJA: misc itemized deductions, personal exemptions — most are no longer relevant under TCJA

### OBBBA AMT changes

P.L. 119-21 made the higher TCJA exemption permanent, reset the 2026 phaseout thresholds to $500,000 / $1,000,000, and doubled the phaseout rate to 50% from 2026 (Rev. Proc. 2025-32). For 2025, Form 6251 line 1 was split into 1a/1b so the Schedule 1-A senior deduction is added back (2025 Instructions for Form 6251, What's New).

---

## Net Investment Income Tax (NIIT) — IRC §1411

3.8% surtax on the lesser of:

1. Net investment income, OR
2. Modified AGI minus threshold

### NIIT thresholds (statutory, NOT indexed for inflation)

| Filing status | Threshold |
|--------------|----------:|
| Single / HoH | $200,000 |
| MFJ / QSS | $250,000 |
| MFS | $125,000 |
| Estate / Trust | start of the top income tax bracket: $15,650 for 2025 (Rev. Proc. 2024-40), $16,000 for 2026 (Rev. Proc. 2025-32) |

These thresholds have NOT been indexed since enactment (2013), so more filers cross into NIIT each year via wage growth.

### Net investment income (NII) — what's in

- Interest (taxable and tax-exempt is excluded)
- Dividends (qualified and ordinary)
- Capital gains (net of capital losses)
- Rental and royalty income from passive activities
- Non-qualified annuities
- Income from passive trades or businesses
- Income from trading in financial instruments / commodities

### NII — what's NOT in

- Wages and salaries (W-2 income)
- Self-employment earnings (Schedule SE income from active trade)
- Distributions from qualified retirement plans (§401(a), §403(a), §403(b), §408, §408A, §457(b))
- Tax-exempt interest (§103 muni bonds)
- Social Security benefits
- Income from active business operations
- Gain from sale of an active business

### MAGI for NIIT

MAGI = AGI + foreign earned income exclusion (§911) + certain other foreign-source amounts. For most domestic filers, MAGI = AGI.

---

## Additional Medicare Tax — IRC §3101(b)(2), §1401(b)(2)

0.9% surtax on wages + RRTA + self-employment earnings above the filing-status threshold.

### Additional Medicare Tax thresholds (statutory, NOT indexed)

| Filing status | Threshold |
|--------------|----------:|
| Single / HoH / QSS | $200,000 |
| MFJ | $250,000 |
| MFS | $125,000 |

Same dollar amounts as NIIT except a qualifying surviving spouse uses $200,000 here and $250,000 for NIIT. Not indexed for inflation.

### Calculation

Form 8959 computes:

1. **Wages portion**: 0.9% × (Medicare wages above threshold for filing status, treating spouses combined for MFJ)
2. **SE portion**: 0.9% × (SE earnings above [threshold − Medicare wages])
3. **RRTA portion**: 0.9% × RRTA compensation above threshold

Sum → Form 8959 Line 18 → Schedule 2 Line 11.

### Employer withholding

Employers withhold 0.9% on Medicare wages > $200,000 paid to a single employee, regardless of filing status. The employer doesn't know the filer's filing status; this can result in:

- Over-withholding (single filer with $250K+ wages: employer withholds correctly; MFJ filer with one spouse earning $250K: employer withheld but the couple's threshold is $250K combined — refund via Form 8959)
- Under-withholding (MFJ with both spouses each earning $150K: no employer withholds, but combined wages > $250K threshold; couple owes via Form 8959)

The reconciliation is the entire purpose of Form 8959.

---

## Premium Tax Credit (PTC) — IRC §36B

Federal Poverty Level (FPL) thresholds drive PTC eligibility. PTC reconciliation flows to Schedule 2 Line 1a (excess APTC repayment) or Schedule 3 Line 9 (net PTC).

### FPL bands

PTC eligibility historically required AGI between 100% and 400% FPL. The American Rescue Plan Act (ARPA) and Inflation Reduction Act (IRA) extended eligibility above 400% FPL through 2025 with an 8.5% applicable percentage cap.

For 2026: the IRS Premium Tax Credit Q&A (Q7, updated Feb. 19, 2026) describes the expansion above 400% FPL as applying to tax years 2021 through 2025, so the 100%–400% FPL limit applies again for 2026 unless later legislation changes it. **Re-check the Q&A before producing 2026 PTC computations.**

### FPL tables

The PTC uses prior-year FPL:

- 2025 returns use 2024 FPL (HHS 2024 poverty guidelines)
- 2026 returns use 2025 FPL (HHS 2025 poverty guidelines)

Tables in IRS Pub 974, Table 1.

### Repayment limitation

If a filer received APTC and reconciliation shows they were entitled to less, repayment for 2025 is capped per Table 5 of the 2025 Form 8962 instructions IF household income is below 400% FPL ($375 / $750 under 200%; $975 / $1,950 at 200%–under 300%; $1,625 / $3,250 at 300%–under 400%, single / other). At 400% FPL or more, the entire excess is owed.

For tax years after 2025 there is no repayment cap at any income: P.L. 119-21 removed it (IRS Premium Tax Credit Q&A, Q31).

---

## Year-aware verification pointers

Before producing a final draft, the agent should re-verify:

| Number | 2025 source | 2026 source |
|--------|-------------|-------------|
| AMT exemption (single) | Rev. Proc. 2024-40 ($88,100) | Rev. Proc. 2025-32 ($90,100) |
| AMT exemption (MFJ) | Rev. Proc. 2024-40 ($137,000) | Rev. Proc. 2025-32 ($140,200) |
| AMT phaseout start (single / MFJ) | $626,350 / $1,252,700 | $500,000 / $1,000,000 (50% rate) |
| AMT rate break (26%/28%) | Indexed in Rev. Proc. 2024-40 ($239,100) | Rev. Proc. 2025-32 ($244,500) |
| NIIT thresholds | Statutory $200K/$250K/$125K | Same (not indexed) |
| Additional Medicare Tax thresholds | Statutory $200K/$250K/$125K | Same (not indexed) |
| SE tax — SS wage base | $176,100 (SSA) | $184,500 (SSA) |
| FPL tables for PTC | 2024 HHS guidelines (used on 2025 returns) | 2025 HHS guidelines (used on 2026 returns) |
| PTC 400% FPL cliff status | Suspended through 2025 (IRA) | Applies again (IRS PTC Q&A Q7, Feb. 19, 2026); re-check |
| Excess APTC repayment cap | Form 8962 instructions Table 5 | None (P.L. 119-21; IRS PTC Q&A Q31) |
| Section 179 limit (for SE income) | $2,500,000 (P.L. 119-21; 2025 Instructions for Form 4562) | $2,560,000 (Rev. Proc. 2025-32 §4.24) |

Sources:

- IRS Rev. Proc. 2024-40 (annual inflation adjustments for 2025) and Rev. Proc. 2025-32 (2026)
- IRS Questions and answers on the Premium Tax Credit: https://www.irs.gov/affordable-care-act/individuals-and-families/questions-and-answers-on-the-premium-tax-credit
- SSA annual fact sheet (SS wage base)
- HHS Poverty Guidelines (annual)
- IRS Pub 974 (Premium Tax Credit detail tables)
- IRC §55, §59, §1411, §3101(b)(2), §36B
