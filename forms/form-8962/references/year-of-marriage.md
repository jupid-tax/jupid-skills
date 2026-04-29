# Alternative Calculation for Year of Marriage (Form 8962 Part V)

When two filers marry during a tax year and one or both had marketplace coverage *before* the marriage, the standard calculation uses combined household income for the entire year — which inflates the income used to compute pre-marriage applicable figure and reduces PTC retroactively. Part V offers an alternative that treats pre-marriage and post-marriage months separately.

## When Part V applies

All three must be true:

1. Filer married during the tax year (filing status MFJ on the return)
2. At least one spouse had marketplace coverage before the marriage date
3. Using the alternative calculation produces a more favorable result than the standard calculation

The alternative calculation is **elective**. Filers can choose to use it or stick with the standard monthly method. Part V is filled only if the filer elects.

## How the alternative calculation works

Per IRC §36B(c)(2)(D)(ii) and Treas. Reg. §1.36B-4(b)(3):

For pre-marriage months:
- Use a **modified household income** = (each spouse's pre-marriage MAGI / their family size at that time) × 12 / pre-marriage months
- Use **modified family size** = the spouse's pre-marriage family size

For post-marriage months:
- Use combined household income and combined family size as in the standard calculation

The "modification" is essentially: prorate each spouse's pre-marriage income as if it had been earned over the full year given their pre-marriage family size, then apply the applicable figure to that pro-rated amount.

The exact formula is:

```
alternative_taxpayer_FPL_pct = (taxpayer_pre-marriage_MAGI × 12 / pre-marriage_months) / pre-marriage_FPL × 100
alternative_spouse_FPL_pct   = (spouse_pre-marriage_MAGI × 12 / pre-marriage_months) / pre-marriage_FPL × 100
```

For each pre-marriage month, the appropriate spouse's alternative %FPL is used to derive their alternative applicable figure and alternative monthly contribution.

## Worked example

### The filer

- Alex married Jordan on July 15, 2025
- Filing status: MFJ
- Tax year: 2025

### Pre-marriage facts

- Alex (Jan–June): single, family size 1, MAGI $24,000 for full year (assume earned $12,000 Jan–June, $12,000 Jul–Dec)
- Jordan (Jan–June): single, family size 1, MAGI $40,000 for full year (assume earned $20,000 Jan–June, $20,000 Jul–Dec)
- Both had separate marketplace coverage Jan–June

### Post-marriage facts

- MFJ filing, family size 2, combined MAGI $64,000 for full year
- Joined Alex's marketplace policy July 15 (ongoing)

### Standard calculation (no Part V)

- Combined household income: $64,000
- Family size: 2
- 2024 FPL for size 2: $20,440
- Line 5 = ($64,000 / $20,440) × 100 = 313% FPL
- Applicable figure (2025 table, 313%): 0.06 + (13/100) × 0.025 = 0.06325
- Annual contribution: $64,000 × 0.06325 = $4,048
- Monthly contribution: $337

For pre-marriage months, this $337 monthly contribution is used to compute PTC against each spouse's pre-marriage policy SLCSP. Result: small or zero PTC for pre-marriage months because monthly contribution ($337) approaches or exceeds the SLCSP for a single-person policy.

### Alternative calculation (Part V)

Pre-marriage months (Jan–June):

For Alex:
- Pre-marriage MAGI: $12,000 (Jan–June portion)
- Annualized: $12,000 × 12 / 6 = $24,000
- Pre-marriage family size: 1, FPL $15,060
- Alternative %FPL: ($24,000 / $15,060) × 100 = 159% FPL
- Alternative applicable figure (159%, 2025 table): 0.00 + (9/50) × 0.02 = 0.0036
- Alternative monthly contribution: $24,000 × 0.0036 / 12 = $7.20

For Jordan:
- Pre-marriage MAGI: $20,000
- Annualized: $20,000 × 12 / 6 = $40,000
- Alternative %FPL: ($40,000 / $15,060) × 100 = 265% FPL
- Alternative applicable figure (265%, 2025 table): 0.04 + (15/50) × 0.02 = 0.046
- Alternative monthly contribution: $40,000 × 0.046 / 12 = $153

Pre-marriage months use these alternative monthly contributions to compute PTC for each spouse's separate policy.

Post-marriage months (Jul–Dec) use the standard combined calculation.

### Result comparison

The alternative calculation produces:

- **Higher PTC for Alex's pre-marriage months** ($7.20/month contribution vs $337/month) — Alex's PTC is dramatically larger
- **Slightly higher PTC for Jordan's pre-marriage months** ($153/month contribution vs $337/month)
- Same PTC for post-marriage months

If the increase exceeds zero, Part V is favorable and the filer should elect.

## How Part V is filled

| Line | Detail |
|------|--------|
| 34 | Alternative family size (typically pre-marriage size = 1 for each spouse) |
| 35 | Alternative monthly contribution amount and pre-marriage months for the **taxpayer** (primary filer) |
| 36 | Alternative monthly contribution amount and pre-marriage months for the **spouse** |

Then Lines 12–23 are completed using:
- Alternative monthly contribution for pre-marriage months (different for each spouse)
- Standard combined monthly contribution (Line 8b) for post-marriage months

This requires careful month-by-month bookkeeping and is best done with worksheet reference.

## Pitfalls

1. **Forgetting that Part V is elective** — filers must affirmatively elect on the form
2. **Mixing pre/post marriage months** — pre-marriage months use alternative; post-marriage use standard. The break point is the marriage date.
3. **Using pre-marriage tax family size that's wrong** — pre-marriage size is the spouse's *pre-marriage* family size, including any dependents the spouse claimed pre-marriage. If a spouse had no dependents pre-marriage, family size = 1.
4. **Annualizing income wrong** — divide pre-marriage MAGI by pre-marriage months, multiply by 12. Don't use full-year MAGI directly.
5. **Not running both calculations** — the agent should compute both standard and alternative and only elect Part V if the alternative produces more favorable PTC. Sometimes alternative is worse (rare but possible).

## Citation

- IRC §36B(c)(2)(D)(ii)
- Treas. Reg. §1.36B-4(b)(3)
- Form 8962 Instructions Part V worksheet
- IRS Pub 974 Chapter on year-of-marriage calculation

## Pointer

Always run both calculations side-by-side before choosing. The alternative is often (but not always) better. The IRS does not penalize filers for choosing standard when alternative would be better — it's a missed opportunity, not a mistake.
