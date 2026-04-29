# AMT, NIIT, and Additional Medicare Tax Thresholds

Schedule 2 routes results from three major income-driven taxes whose thresholds matter to the agent: AMT (Form 6251 → Schedule 2 Line 1), Net Investment Income Tax (Form 8960 → Schedule 2 Line 12), and Additional Medicare Tax (Form 8959 → Schedule 2 Line 11). This file lists thresholds, citations, and verification pointers.

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

The exemption phases out at 25 cents per dollar of AMTI above the phaseout threshold.

### AMT exemption amounts (2026)

Set by inflation adjustment in the fall 2025 Revenue Procedure (typically Rev. Proc. 2025-XX). **Verify before filing 2026 returns.**

### AMT rates (statutory, not indexed)

- 26% on AMTI up to $239,100 (2025 single) / $239,100 (2025 MFJ); same threshold for MFS halved
- 28% on AMTI above that amount

The 26%/28% break point is indexed annually per IRC §55(b)(1)(A) — verify the 2026 amount.

### Common AMT preference items (IRC §57) and adjustments (IRC §56)

Add back / preference for AMT:

- State and local taxes deducted on Schedule A (TCJA capped these regular-tax deductions at $10K, which dampened AMT for many filers post-2018)
- Bargain element on ISO exercise (FMV at exercise − strike price), if held past year-end
- Private activity bond interest issued 2009–2010 (excluded under ARRA / TCJA in some cases — verify)
- Depreciation differences (regular MACRS vs AMT depreciation)
- Long-term contract income (different methods for AMT)
- Pre-TCJA: misc itemized deductions, personal exemptions — most are no longer relevant under TCJA

### OBBBA 2025 AMT changes

OBBBA 2025 made the TCJA AMT exemption increases permanent. Verify exact 2026 phaseout thresholds and rate break points against the post-OBBBA Revenue Procedure.

---

## Net Investment Income Tax (NIIT) — IRC §1411

3.8% surtax on the lesser of:

1. Net investment income, OR
2. Modified AGI minus threshold

### NIIT thresholds (statutory, NOT indexed for inflation)

| Filing status | Threshold |
|--------------|----------:|
| Single / HoH / QSS | $200,000 |
| MFJ / QSS-with-spouse | $250,000 |
| MFS | $125,000 |
| Estate / Trust | varies — top income tax bracket begin ($15,200 for 2024, verify 2025/2026) |

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

Same thresholds as NIIT (deliberate alignment in ACA). Not indexed for inflation.

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

Federal Poverty Level (FPL) thresholds drive PTC eligibility. PTC reconciliation flows to Schedule 2 Line 2 (excess APTC repayment) or Schedule 3 Line 9 (refundable PTC).

### FPL bands

PTC eligibility historically required AGI between 100% and 400% FPL. The American Rescue Plan Act (ARPA) and Inflation Reduction Act (IRA) extended eligibility above 400% FPL through 2025 with an 8.5% applicable percentage cap.

For 2026: the 400% cliff returns unless Congress extends the IRA expansion. **Verify the post-OBBBA / post-IRA status of §36B before producing 2026 PTC computations.** As of early 2026, the cliff status for tax years 2026+ is contingent on legislation.

### FPL tables

The PTC uses prior-year FPL:

- 2025 returns use 2024 FPL (HHS 2024 poverty guidelines)
- 2026 returns use 2025 FPL (HHS 2025 poverty guidelines)

Tables in IRS Pub 974, Table 1.

### Repayment limitation

If a filer received APTC and reconciliation shows they were entitled to less, repayment is capped per Pub 974 Table 5 IF AGI is below 400% FPL. Above 400% FPL, the cap historically did not apply — the entire excess was owed.

For 2026, the cap structure depends on whether the ARPA/IRA above-400%-FPL relief is in effect. Verify before filing.

---

## Year-aware verification pointers

Before producing a final draft, the agent should re-verify:

| Number | 2025 source | 2026 source |
|--------|-------------|-------------|
| AMT exemption (single) | Rev. Proc. 2024-40 ($88,100) | Fall 2025 Rev. Proc. — verify |
| AMT exemption (MFJ) | Rev. Proc. 2024-40 ($137,000) | Fall 2025 Rev. Proc. — verify |
| AMT rate break (26%/28%) | Indexed in Rev. Proc. 2024-40 ($239,100) | Fall 2025 Rev. Proc. — verify |
| NIIT thresholds | Statutory $200K/$250K/$125K | Same (not indexed) |
| Additional Medicare Tax thresholds | Statutory $200K/$250K/$125K | Same (not indexed) |
| SE tax — SS wage base | $176,100 (SSA Oct 2024) | SSA Oct 2025 — verify |
| FPL tables for PTC | 2024 HHS guidelines (used on 2025 returns) | 2025 HHS guidelines (used on 2026 returns) |
| PTC 400% FPL cliff status | Suspended through 2025 (IRA) | Verify legislation for 2026+ |
| Section 179 limit (for SE income) | $1,250,000 (Rev. Proc. 2024-40) | Fall 2025 Rev. Proc. — verify |

Sources:

- IRS Rev. Proc. 2024-40 (annual inflation adjustments for 2025)
- SSA annual fact sheet (SS wage base)
- HHS Poverty Guidelines (annual)
- IRS Pub 974 (Premium Tax Credit detail tables)
- IRC §55, §59, §1411, §3101(b)(2), §36B
