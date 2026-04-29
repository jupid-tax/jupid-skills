# Repayment Limitation (Form 8962 Line 28, Pub 974 Table 5)

When a filer's actual entitlement to PTC is *less* than the APTC they received, IRC §36B(f)(2)(B) caps the repayment based on household income as a percentage of FPL. The cap protects filers below 400% FPL from a punitive repayment when income ends up higher than estimated.

## Year-aware cap structure

The cap amounts are set annually in Pub 974 Table 5. They differ for single filers vs. all other filing statuses (MFJ, MFS, HoH, QSS).

### 2025 Pub 974 Table 5 (used for 2025 returns)

| Household income as % of FPL | Single | All other filing statuses |
|------------------------------|-------:|--------------------------:|
| Less than 200% | $375 | $750 |
| At least 200% but less than 300% | $975 | $1,950 |
| At least 300% but less than 400% | $1,625 | $3,250 |
| 400% or more (under IRA) | (subject to current rules) | (subject to current rules) |

**For 2025 under IRA modification**: there is no cliff at 400% FPL; filers above 400% are still subject to a cap-equivalent because the applicable figure is capped at 8.5%, which limits how much PTC could differ from APTC. Verify current Pub 974 Table 5 for the exact 400%+ row.

### 2026 Pub 974 Table 5 (use for 2026 returns)

The cap amounts inflate annually. **Verify against the 2026 Pub 974 (published early 2026) before filing.** Approximate inflation factor on 2025 values yields the 2026 caps, but the IRS publishes discrete values, not formula-derived values.

If the IRA extension expires for 2026, the pre-IRA structure returns:

| Household income as % of FPL | Single | All other |
|------------------------------|-------:|----------:|
| Less than 200% | $X | $Y |
| 200% – 300% | $X | $Y |
| 300% – 400% | $X | $Y |
| 400% or more | **No cap; full excess owed** (cliff) | **No cap; full excess owed** (cliff) |

The pre-IRA cliff is the single biggest driver of large APTC repayments — verify whether the cliff applies for the tax year being filed.

## How the cap works

1. Compute Form 8962 Line 27 = Line 25 (total APTC) − Line 24 (total PTC entitled). This is the *raw* excess.
2. Look up Line 28 from Pub 974 Table 5 based on Line 5 (% FPL) and filing status.
3. Line 29 = lesser of Line 27 or Line 28.

If Line 27 < Line 28, the cap is non-binding (filer pays full excess). If Line 27 > Line 28, the cap saves the filer money — they pay only the cap amount and the rest is forgiven.

## Worked examples

### Example A: 322% FPL single, $1,197 excess

- Line 27 (excess) = $1,197
- Line 5 = 322%, single → Pub 974 Table 5 row "300%–400% single" = $1,625
- Line 28 = $1,625
- Line 29 = lesser of $1,197 or $1,625 = **$1,197**

Cap is non-binding; filer owes the full excess.

### Example B: 250% FPL MFJ, $4,200 excess

- Line 27 = $4,200
- Line 5 = 250%, MFJ → Table 5 row "200%–300% other" = $1,950
- Line 28 = $1,950
- Line 29 = lesser of $4,200 or $1,950 = **$1,950**

Cap saves the filer $2,250 ($4,200 − $1,950). The forgone amount is not added back as income; it is statutorily forgiven under IRC §36B(f)(2)(B).

### Example C: 410% FPL single, $6,800 excess (under IRA, 2025)

For 2025 under IRA modification, Pub 974 Table 5 may have a "400% or more" row with a cap, OR the 8.5% applicable figure cap effectively limits the excess. Verify Table 5 for 2025 specifically.

If Table 5 has a 400%+ row at, say, $1,500/$3,000:
- Line 28 = $1,500
- Line 29 = lesser of $6,800 or $1,500 = **$1,500**

If Table 5 reverts to "no cap" at 400%+ (pre-IRA cliff):
- Line 28 = (none / not applicable)
- Line 29 = $6,800 (full excess)

The agent must verify the current-year Pub 974 Table 5 row for 400%+.

## Special case: < 100% FPL

If Line 5 < 100% FPL, the filer was generally Medicaid-eligible (in expansion states) or was below the lower bound for marketplace PTC. In some cases the filer can still claim PTC under the "alien lawfully present" rule (IRC §36B(c)(1)(B)). Repayment for such filers is limited per Table 5 row "less than 200% single/other".

## Special case: Failure to reconcile

If the filer received APTC and **does not file Form 8962** to reconcile, the IRS treats them as ineligible for APTC in subsequent years. They will be flagged in the marketplace's federal data services for "FTR" (failure to reconcile) and lose APTC eligibility for the next plan year until reconciliation is completed.

## Citation

- IRC §36B(f)(2)(B) — repayment limitation
- Treas. Reg. §1.36B-4(a)(3) — repayment computation
- IRS Pub 974, Table 5 — year-specific cap amounts
- Form 8962 Instructions — Line 28 worksheet

## Pointer

Always pull the current-year Pub 974 from https://www.irs.gov/pub/irs-pdf/p974.pdf and confirm Table 5 values before computing Line 28. The values change annually for inflation.
