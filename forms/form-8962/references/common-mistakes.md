# Common Form 8962 Mistakes

The most frequent audit-trip mistakes filers and their software make on Form 8962. Each entry: what went wrong, why, citation, and correction.

## 1. Using current-year FPL instead of prior-year

**The mistake**: For a 2025 return, filer uses 2025 HHS poverty guidelines (e.g., $15,650 for family of 1) on Line 4 instead of 2024 guidelines ($15,060).

**Why it's wrong**: IRC §36B(d)(3)(C) defines FPL as the most recent HHS guidelines published as of the **first day of the open enrollment period** for the plan year. For 2025 plan year, that's November 2024 → use 2024 HHS table.

**Citation**: IRC §36B(d)(3)(C); Pub 974 Chapter 2.

**Correction**: Always use prior-year HHS guidelines. 2025 returns → 2024 FPL; 2026 returns → 2025 FPL.

## 2. Counting non-dependents in tax family size

**The mistake**: Filer lives with their adult child who works and files their own taxes. Filer enters Line 1 = 2 (filer + child).

**Why it's wrong**: Tax family size = filer + spouse + people *claimed as dependents* on Form 1040. An adult child not claimed is in their own tax family.

**Citation**: IRC §36B(d)(1)(B); Pub 974 Chapter 2.

**Correction**: Count only filer + spouse + claimed dependents. Reduce Line 1 accordingly. Reduce Line 4 (FPL) accordingly.

## 3. Including non-required dependent's MAGI on Line 2b

**The mistake**: Filer's 17-year-old dependent worked a part-time job and chose to file a return to claim a small refund of withholding. Filer adds the dependent's MAGI ($4,000) to Line 2b.

**Why it's wrong**: Line 2b includes only dependents who are **required** to file, not those who chose to file optionally. A 17-year-old earning $4,000 in W-2 wages is below the filing requirement threshold (~$15,000 for 2025 single dependents under 65 with only earned income).

**Citation**: IRC §36B(d)(2)(A)(ii); Pub 501 (filing requirements).

**Correction**: Exclude non-required dependent MAGI. Line 2b only includes MAGI of dependents whose income met the filing requirement.

## 4. Filing Form 8962 with all-zero Lines 11 or 12-23

**The mistake**: Filer received a Form 1095-A but didn't enroll in coverage / didn't actually receive APTC; preparer files Form 8962 with all zeros to "be safe".

**Why it's wrong**: Form 8962 with all zeros is not required if no APTC was paid and no PTC is being claimed. It can confuse the IRS processing. Only file Form 8962 if APTC > 0 OR claiming PTC at filing.

**Citation**: Form 8962 Instructions, "Who Must File" section.

**Correction**: Verify Form 1095-A Column C has nonzero APTC. If all zeros (no APTC paid) and not claiming PTC at filing, do not file Form 8962. Retain 1095-A for records.

## 5. Misallocating shared policy between divorced parents

**The mistake**: Two divorced parents share a marketplace policy for their child. Each files Form 8962 independently. Parent A allocates 70/30; Parent B allocates 60/40.

**Why it's wrong**: Both filers must use the **same allocation percentages**. The IRS cross-checks Forms 8962 between the two SSNs and issues notices when they disagree.

**Citation**: Treas. Reg. §1.36B-4(c).

**Correction**: Coordinate the allocation between the parents before either files. Both Forms 8962 must show identical allocation percentages.

## 6. Using annual method when monthly is required

**The mistake**: Filer married mid-year. Pre-marriage and post-marriage SLCSP differ. Filer uses annual method (Line 10 = Yes) and files.

**Why it's wrong**: Annual method requires same SLCSP, family size, and eligibility every month. Marriage changes family size mid-year, forcing monthly method.

**Citation**: IRC §36B(b)(2); Form 8962 Instructions Line 10.

**Correction**: Switch to monthly method (Line 10 = No). Fill Lines 12–23 with month-specific amounts. Consider Part V (alternative calculation for year of marriage) if it produces a more favorable result.

## 7. Missing the repayment limitation cap

**The mistake**: Filer at 250% FPL (single) had $4,200 excess APTC. Preparer enters $4,200 on Schedule 2 Line 2 without checking Line 28.

**Why it's wrong**: Pub 974 Table 5 caps the repayment for filers below 400% FPL. For 2025, single at 250% FPL: cap = $975. The filer should owe $975, not $4,200. Skipping Line 28 overpays by $3,225.

**Citation**: IRC §36B(f)(2)(B); Pub 974 Table 5.

**Correction**: Always compute Line 28 from Pub 974 Table 5. Line 29 = lesser of Line 27 or Line 28.

## 8. Filing Form 1040 without Form 8962 when 1095-A was received

**The mistake**: Filer received Form 1095-A showing APTC paid but did not file Form 8962. The IRS holds the refund and sends Letter 12C requesting Form 8962.

**Why it's wrong**: When the marketplace pays APTC, the filer must reconcile via Form 8962 regardless of whether they're getting a refund or owe tax. Failure to reconcile triggers Letter 12C and delays refund.

**Citation**: IRC §36B(f); Form 8962 Instructions "Who Must File".

**Correction**: Always file Form 8962 if APTC > 0 on Form 1095-A. Failure to reconcile (FTR) status also blocks APTC eligibility for the next plan year.

## 9. Reporting the wrong applicable figure for the year

**The mistake**: For a 2024 return, preparer uses 2024 applicable figure table (with IRA modifications) but for a 2026 return uses the same IRA-modified table.

**Why it's wrong**: IRA modifications expire after tax year 2025 unless extended. For 2026, verify whether IRA was extended. If not, the pre-IRA table applies and the 400% FPL cliff returns.

**Citation**: IRC §36B(b)(3)(A) (statutory base); ARPA §9661 (2021–2022 modification); IRA §12001 (2021–2025 extension); post-IRA legislation (verify).

**Correction**: Always cross-check the applicable figure table against the current-year Pub 974 and Form 8962 instructions. Don't reuse a prior year's table.

## 10. Adding APTC withholding to Form 1040 Line 25c

**The mistake**: Filer treats APTC paid by the marketplace as if it were federal income tax withholding (Form 1040 Line 25c).

**Why it's wrong**: APTC is paid by Treasury directly to the insurer; it is not income tax withholding from the filer's wages. Form 1040 Line 25c is for W-2 Box 2 + 1099 federal withholding, not APTC.

**Citation**: Form 1040 Instructions Line 25c.

**Correction**: APTC reconciles via Form 8962 only. The result lands on Schedule 3 Line 9 (refundable PTC) or Schedule 2 Line 2 (excess APTC repayment). It does not appear on Line 25c.

## 11. Not coordinating SLCSP across multiple 1095-A forms

**The mistake**: Filer had two marketplace policies during the year (changed plans mid-year). Two 1095-A forms received. Preparer averages or sums SLCSP incorrectly.

**Why it's wrong**: Each 1095-A reports the SLCSP for the months that policy was in effect. Form 8962 monthly method needs the SLCSP for each month from the corresponding 1095-A. Don't average; use month-by-month.

**Citation**: Form 8962 Instructions; Pub 974.

**Correction**: For each month, identify which 1095-A applied and use its Column B value. Sum properly across months.

## 12. Filing as MFS without checking the abuse / abandonment exception

**The mistake**: Filer is MFS and claims PTC. The IRS rejects because MFS is generally ineligible.

**Why it's wrong**: IRC §36B(c)(1)(C) generally bars PTC for MFS filers. Exception: domestic abuse or spousal abandonment victims may file MFS and claim PTC if they meet the Pub 974 criteria.

**Citation**: IRC §36B(c)(1)(C); Pub 974 Chapter 1 (MFS exception).

**Correction**: Verify the filer qualifies for the abuse / abandonment exception before claiming PTC on MFS. If qualifying, attach a written statement to the return per Pub 974. If not qualifying, the filer is ineligible for PTC (and may need to repay all APTC, subject to the cap).
