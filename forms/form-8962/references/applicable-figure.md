# Applicable Figure for Form 8962 Line 7

The applicable figure is the percentage of household income the filer is "expected" to contribute to premiums. It's a sliding scale based on Line 5 (% of FPL). The unique product of the applicable figure × household income = annual contribution amount (Line 8a), which is subtracted from the SLCSP to determine maximum premium assistance.

## Year-aware tables

The applicable figure table in IRC §36B(b)(3)(A) was modified by ARPA (Section 9661) for tax years 2021–2022, then extended by IRA (Section 12001) through 2025. For 2026+, the table reverts unless Congress extends.

### 2025 table (under IRA extension — applicable to 2025 returns)

| Household income as % of FPL | Initial applicable figure | Final applicable figure |
|------------------------------|---------------------------|--------------------------|
| < 150% | 0.00 | 0.00 |
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

### Pre-IRA / pre-ARPA table (would apply to 2026+ if IRA not extended)

| Household income as % of FPL | Initial | Final |
|------------------------------|---------|-------|
| < 100% | not eligible | not eligible |
| 100% – 133% | 0.0210 | 0.0210 |
| 133% – 150% | 0.0312 | 0.0417 |
| 150% – 200% | 0.0417 | 0.0658 |
| 200% – 250% | 0.0658 | 0.0843 |
| 250% – 300% | 0.0843 | 0.0980 |
| 300% – 400% | 0.0980 | 0.0980 |
| ≥ 400% | not eligible (cliff) | — |

Pre-IRA values are also indexed annually for inflation per §36B(b)(3)(A)(ii). Verify the exact figures against the Form 8962 instructions for the tax year.

### 2026 status — verify before filing

As of early 2026, the IRA extension expires after tax year 2025 unless renewed. Possible scenarios:

- **Congress extends ARPA/IRA modifications** → 2025 table continues
- **Congress lets IRA expire** → pre-IRA table returns; 400% FPL cliff resumes
- **Congress passes a new modification** → new table applies

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

### Example 4: 401% FPL, hypothetical pre-IRA table

For % FPL ≥ 400% under pre-IRA rules, filer is not eligible for PTC. Line 5 = 401% means no PTC; full APTC must be repaid (subject to repayment cap).

→ This is the "cliff" that ARPA / IRA suspended through 2025.

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
