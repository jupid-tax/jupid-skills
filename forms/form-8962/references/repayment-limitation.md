# Repayment Limitation (Form 8962 Line 28, Instructions Table 5)

When a filer's actual entitlement to PTC is *less* than the APTC they received, IRC §36B(f)(2)(B) caps the repayment based on household income as a percentage of FPL. The cap protects filers below 400% FPL from a punitive repayment when income ends up higher than estimated. It applies to tax years beginning before January 1, 2026 only: P.L. 119-21 §71305 struck §36B(f)(2)(B) for tax years beginning after December 31, 2025.

## Year-aware cap structure

The cap amounts are set annually in Table 5 of the Form 8962 instructions (Pub 974 refers to that table). They differ for single filers vs. all other filing statuses (MFJ, MFS, HoH, QSS).

### 2025 Form 8962 instructions Table 5 (used for 2025 returns)

| Household income as % of FPL | Single | All other filing statuses |
|------------------------------|-------:|--------------------------:|
| Less than 200% | $375 | $750 |
| At least 200% but less than 300% | $975 | $1,950 |
| At least 300% but less than 400% | $1,625 | $3,250 |
| 400% or more | Leave Line 28 blank; no limitation | Leave Line 28 blank; no limitation |

**For 2025**: a filer above 400% FPL can still have a PTC (applicable figure 0.0850), but there is no repayment limitation: "If your entry on Form 8962, line 5, is 400 or more, there is no repayment limitation. You must repay the amount shown on line 27" (2025 Form 8962 instructions, Line 28). If married at year end and filing separately, each spouse uses Table 5 based on the household income on their own return.

### 2026 returns: no repayment limitation

For tax years beginning after December 31, 2025, there is no repayment cap at any income level. All excess APTC is repaid (P.L. 119-21 §71305; IRS Fact Sheet FS-2025-10, Q31: "There is no repayment cap for tax years after 2025"). Above 400% FPL there is also no PTC (§36B(c)(1)(A); the 2021–2025 exception in §36B(c)(1)(E) expired), so every dollar of APTC is repaid.

The 400% cliff and the removed cap are the biggest drivers of large APTC repayments on 2026 returns. Re-check IRS.gov/Form8962 in case later legislation changes this.

## How the cap works

1. Compute Form 8962 Line 27 = Line 25 (total APTC) − Line 24 (total PTC entitled). This is the *raw* excess.
2. Look up Line 28 from the instructions' Table 5 based on Line 5 (% FPL) and filing status (2025 and earlier).
3. Line 29 = lesser of Line 27 or Line 28; if Line 28 is blank, Line 29 = Line 27.

If Line 27 < Line 28, the cap is non-binding (filer pays full excess). If Line 27 > Line 28, the cap saves the filer money — they pay only the cap amount and the rest is forgiven.

## Worked examples

### Example A: 322% FPL single, $1,197 excess (2025)

- Line 27 (excess) = $1,197
- Line 5 = 322%, single → Table 5 row "300%–400% single" = $1,625
- Line 28 = $1,625
- Line 29 = lesser of $1,197 or $1,625 = **$1,197**

Cap is non-binding; filer owes the full excess.

### Example B: 250% FPL MFJ, $4,200 excess (2025)

- Line 27 = $4,200
- Line 5 = 250%, MFJ → Table 5 row "200%–300% other" = $1,950
- Line 28 = $1,950
- Line 29 = lesser of $4,200 or $1,950 = **$1,950**

Cap saves the filer $2,250 ($4,200 − $1,950). The forgone amount is not added back as income; it is statutorily forgiven under IRC §36B(f)(2)(B).

### Example C: 410% FPL single, $6,800 excess (2025)

The 2025 Table 5 row for "400 or more" says to leave Line 28 blank:
- Line 28 = (blank)
- Line 29 = $6,800 (full excess)

### Example D: 250% FPL MFJ, $4,200 excess (2026)

No repayment limitation exists for 2026 (P.L. 119-21 §71305):
- Line 29 = $4,200 (full excess)

## Special case: < 100% FPL

If Line 5 < 100% FPL, the filer was generally Medicaid-eligible (in expansion states) or was below the lower bound for marketplace PTC. For 2025, the filer can still claim PTC if the Marketplace estimated household income of at least 100% FPL and APTC was paid, or under the "alien lawfully present" rule (IRC §36B(c)(1)(B)) (2025 instructions, Line 5). P.L. 119-21 §71302 repealed §36B(c)(1)(B) for tax years beginning after December 31, 2025. Repayment for 2025 filers below 200% is limited per the Table 5 row "less than 200".

## Special case: Failure to reconcile

If the filer received APTC and **does not file Form 8962** to reconcile, the Marketplace can find them ineligible for APTC for a later plan year ("failure to reconcile", FTR) until they file and reconcile (2025 Form 8962 instructions and IRS FS-2025-10 describe the filing requirement; the Marketplace applies the FTR rule).

## Citation

- IRC §36B(f)(2)(B) — repayment limitation (tax years before 2026)
- P.L. 119-21 §71305 — limitation removed for tax years beginning after December 31, 2025
- Treas. Reg. §1.36B-4(a)(3) — repayment computation
- Form 8962 Instructions, Line 28 and Table 5 — year-specific cap amounts
- IRS Fact Sheet FS-2025-10 (Dec. 2025), Q31 — https://www.irs.gov/pub/taxpros/fs-2025-10.pdf

## Pointer

Always pull the current-year Form 8962 instructions from https://www.irs.gov/pub/irs-pdf/i8962.pdf and confirm Table 5 values before computing Line 28 for 2025 or earlier years. The values change annually for inflation.
