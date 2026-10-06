# Applicable Figure for Form 8962 Line 7

The applicable figure is the percentage of household income the filer is "expected" to contribute to premiums. It's a sliding scale based on Line 5 (% of FPL). The unique product of the applicable figure × household income = annual contribution amount (Line 8a), which is subtracted from the SLCSP to determine maximum premium assistance.

## Year-aware tables

The applicable figure table in IRC §36B(b)(3)(A) was modified by ARPA (Section 9661) for tax years 2021–2022, then extended by IRA (Section 12001) through 2025 (§36B(b)(3)(A)(iii) applies to taxable years beginning before January 1, 2026). For 2026, the indexed statutory table applies (Rev. Proc. 2025-25); no extension had been enacted as of 2026-10-06.

### 2025 table (under IRA extension — applicable to 2025 returns; Rev. Proc. 2024-35; 2025 Form 8962 instructions Table 2)

| Household income as % of FPL | Initial applicable figure | Final applicable figure |
|------------------------------|---------------------------|--------------------------|
| ≤ 150% | 0.00 | 0.00 |
| 150% – 200% | 0.00 | 0.02 |
| 200% – 250% | 0.02 | 0.04 |
| 250% – 300% | 0.04 | 0.06 |
| 300% – 400% | 0.06 | 0.085 |
| ≥ 400% | 0.085 | 0.085 |

Within each band, the applicable figure interpolates linearly. Formula:

```
applicable_figure = initial + (% FPL − band_start) / (band_end − band_start) × (final − initial)
```

Round to four decimals (IRS form instruction).

### 2026 table (Rev. Proc. 2025-25, section 3.01 — applicable to 2026 returns)

| Household income as % of FPL | Initial | Final |
|------------------------------|---------|-------|
| < 100% | not an applicable taxpayer (§36B(c)(1)(A)) | — |
| less than 133% | 0.0210 | 0.0210 |
| at least 133% but less than 150% | 0.0314 | 0.0419 |
| at least 150% but less than 200% | 0.0419 | 0.0660 |
| at least 200% but less than 250% | 0.0660 | 0.0844 |
| at least 250% but less than 300% | 0.0844 | 0.0996 |
| at least 300% but not more than 400% | 0.0996 | 0.0996 |
| > 400% | not an applicable taxpayer (no PTC; §36B(c)(1)(A)) | — |

The statutory base table is indexed annually under §36B(b)(3)(A)(ii); each year's Rev. Proc. publishes the values. Use the 2026 Form 8962 instructions Table 2 (with whole-percent steps) once released.

### 2026 status — verify before filing

The ARPA/IRA enhanced table and the removal of the 400% ceiling (§36B(b)(3)(A)(iii) and (c)(1)(E)) apply only to taxable years beginning before January 1, 2026. No extension had been enacted as of 2026-10-06. If Congress enacts one later, the IRS will post it at IRS.gov/Form8962.

The agent must check the most recent IRS guidance (Pub 974 and Form 8962 instructions for the tax year being filed) before computing Line 7 for 2026 returns.

## Worked examples

### Example 1: 322% FPL, 2025 table

```
band_start = 300, band_end = 400
initial = 0.06, final = 0.085
applicable_figure = 0.06 + (322 − 300) / (400 − 300) × (0.085 − 0.06)
                  = 0.06 + (22 / 100) × 0.025
                  = 0.06 + 0.0055
                  = 0.0655
```

→ Line 7 = 0.0655

### Example 2: 199% FPL, 2025 table

```
band_start = 150, band_end = 200
initial = 0.00, final = 0.02
applicable_figure = 0.00 + (199 − 150) / (200 − 150) × (0.02 − 0.00)
                  = 0.00 + (49 / 50) × 0.02
                  = 0.0196
```

→ Line 7 = 0.0196

### Example 3: 401% FPL, 2025 table (IRA extension)

For % FPL ≥ 400%, applicable figure caps at 0.085.

→ Line 7 = 0.085

### Example 4: 401% FPL, 2026 rules

For household income above 400% FPL in 2026, the filer is not an applicable taxpayer and gets no PTC. All APTC must be repaid, with no repayment cap (P.L. 119-21 §71305; IRS FS-2025-10, Q31).

→ This is the "cliff" that ARPA / IRA suspended for 2021 through 2025.

## How Line 7 lands on Form 8962

The form provides Table 2 in the instructions with discrete percent steps (1% intervals). Most filers can look up the applicable figure rather than interpolate. The computed and looked-up values should match to 4 decimals.

For e-file software, the applicable figure is computed exactly via the formula above. For paper filing, use the lookup table.

## Common mistakes

1. **Using the wrong year's table**. The applicable figure table changes when ARPA / IRA / post-IRA rules change. Always cross-check against the current-year Form 8962 instructions Table 2.
2. **Interpolating within the wrong band**. 199% is in the 150-200% band, not the 200-250% band. The band boundaries are inclusive on the lower end and exclusive on the upper end (or vice versa per the instructions — verify).
3. **Forgetting Line 5 is rounded down**. A filer with computed % FPL of 199.6% uses Line 5 = 199% and looks up the 199% applicable figure, not the 200% one.
4. **Applying the pre-IRA cliff in a year IRA is in effect**. For 2025 returns, even at 401% FPL the filer gets PTC at the 8.5% cap. Pre-IRA, they'd get nothing.

## Pointer

For each tax year, the authoritative source for the applicable figure is:

- IRS **Pub 974**, year-specific edition
- **Form 8962 Instructions** Table 2, year-specific edition
- IRC §36B(b)(3)(A) for the statutory base (modified by ARPA / IRA through 2025)
- Rev. Proc. 2024-35 (2025 table) and Rev. Proc. 2025-25 (2026 table): https://www.irs.gov/pub/irs-drop/rp-25-25.pdf
