# Common Schedule 2 Mistakes

The most frequent audit-trip mistakes filers and their software make on Schedule 2. Each entry: what went wrong, why, citation, and correction.

## 1. Putting refundable PTC on Schedule 2 Line 1a instead of Schedule 3 Line 9

**The mistake**: Filer's Form 8962 shows a Net Premium Tax Credit (Line 26 > 0) and the preparer puts it on Schedule 2 Line 1a.

**Why it's wrong**: Schedule 2 Line 1a is *excess APTC repayment* — i.e., when the filer received more APTC than they were entitled to and owes the government back. Form 8962 Line 29 is the source. A net credit (Line 26) is a refundable credit that reduces tax, and it goes on **Schedule 3 Line 9**, not Schedule 2.

**Citation**: Form 8962 instructions (IRS Pub i8962); IRC §36B.

**Correction**: Move the amount from Schedule 2 Line 1a to Schedule 3 Line 9. Recompute Form 1040 Lines 17 and 31.

## 2. Reporting SE tax twice (Schedule 2 Line 4 + Form 1040 Line 23 manual entry)

**The mistake**: Filer enters SE tax on Schedule 2 Line 4 *and* writes the same amount directly on Form 1040 Line 23.

**Why it's wrong**: Form 1040 Line 23 is *populated by* Schedule 2 Line 21. It should not be entered manually if Schedule 2 is attached. Manual entry creates a doubled tax.

**Citation**: Form 1040 instructions (i1040gi).

**Correction**: Schedule 2 Line 21 is the only entry that should populate Form 1040 Line 23. Delete the manual override.

## 3. Not attaching Schedule SE when SE tax appears on Line 4

**The mistake**: Schedule 2 Line 4 has an amount but Schedule SE is missing from the return.

**Why it's wrong**: Schedule SE is required whenever Line 4 > 0. The IRS will reject e-filed returns or send a notice on paper returns.

**Citation**: Form 1040 instructions; Schedule SE instructions.

**Correction**: Compute Schedule SE from Schedule C/F/K-1 self-employment earnings; attach. Verify Schedule SE Line 12 = Schedule 2 Line 4.

## 4. Forgetting that half of SE tax is deductible above-the-line

**The mistake**: Filer reports SE tax correctly on Schedule 2 Line 4 but forgets to claim the **deduction for half of SE tax** on Schedule 1 Line 15.

**Why it's wrong**: IRC §164(f) allows a deduction for half of SE tax. It's not on Schedule 2 — it's on Schedule 1 Line 15 (AGI adjustment).

**Citation**: IRC §164(f); Schedule SE instructions; Schedule 1 instructions.

**Correction**: Add half of Schedule SE Line 12 to Schedule 1 Line 15.

## 5. Putting Additional Medicare Tax withholding on Schedule 2 Line 11

**The mistake**: Filer's W-2 shows Box 6 (Medicare tax) including the 0.9% surtax withheld on wages > $200K, and the filer reports it on Schedule 2 Line 11.

**Why it's wrong**: Schedule 2 Line 11 is the *liability* (Form 8959 Line 18). The amount the employer *withheld* goes on Form 8959 Line 24 and routes to Form 1040 Line 25c (federal income tax withholding) — it's a payment, not a tax.

**Citation**: Form 8959 instructions (i8959); IRC §3101(b)(2).

**Correction**: Run Form 8959 fully. Line 18 (liability) → Schedule 2 Line 11. Line 24 (withheld) → Form 1040 Line 25c.

## 6. Missing AMT when the filer exercised ISOs

**The mistake**: Filer exercised ISOs mid-year and held the shares past 12/31; preparer skips Form 6251 because "ISOs aren't taxable until sold."

**Why it's wrong**: ISOs create an *AMT preference* in the year of exercise equal to (FMV at exercise − strike) × shares. Even though there's no regular-tax income, AMTI is increased and Form 6251 may produce AMT. This is the single most common AMT trigger for tech employees.

**Citation**: IRC §56(b)(3), §57(a)(8); Form 6251 instructions.

**Correction**: Compute Form 6251 with the ISO bargain element added back (Form 6251 line 2i). If Line 11 > 0, Schedule 2 Line 2 reflects AMT.

## 7. Reporting NIIT without checking the MAGI threshold

**The mistake**: Filer with $150,000 AGI and $20,000 in dividends has 3.8% NIIT computed and entered on Schedule 2 Line 12.

**Why it's wrong**: NIIT applies only when MAGI exceeds the threshold ($200K single / $250K MFJ / $125K MFS). At $150K MAGI single, NIIT = 0 even with investment income.

**Citation**: IRC §1411; Form 8960 instructions.

**Correction**: Verify MAGI > threshold before populating Form 8960. If MAGI ≤ threshold, Form 8960 is not required; Schedule 2 Line 12 = 0.

## 8. Reporting full APTC repayment when filer is below 400% FPL (ignoring the limitation)

**The mistake**: Filer received $4,200 in APTC but reconciliation shows they were only entitled to $1,800. Preparer enters $2,400 (full excess) on Schedule 2 Line 1a on a 2025 return.

**Why it's wrong**: For 2025, Table 5 of the Form 8962 instructions caps the repayment for filers below 400% FPL based on household income as a percentage of FPL: $375 (single) / $750 (others) under 200%, $975 / $1,950 at 200%–under 300%, and $1,625 / $3,250 at 300%–under 400%. The filer's actual repayment is capped at the table limit, not the full excess.

**2026 and later**: there is no cap; the full excess is repaid (P.L. 119-21; IRS Premium Tax Credit Q&A, Q31). Applying a 2025 cap to a 2026 return is now the error.

**Citation**: IRC §36B(f)(2)(B) (as in effect for 2025); 2025 Instructions for Form 8962, Table 5.

**Correction**: Run Form 8962 with the repayment limitation table. The Line 29 result already reflects the cap.

## 9. Reporting first-time homebuyer credit repayment after the 15-year window expired

**The mistake**: Filer claims a Line 10 entry for "annual installment of first-time homebuyer credit" in 2025 from a 2008 purchase.

**Why it's wrong**: The 2008 credit (up to $7,500) was repaid via 15 annual installments starting tax year 2010. The final installment was tax year 2024. On the 2025 Schedule 2, Line 10 is "Reserved for future use."

**Citation**: IRC §36(f); Form 5405 (Rev. November 2024); 2025 Schedule 2.

**Correction**: Leave Line 10 blank. If the user believes an amount is still owed, refer them to a CPA.

## 10. Putting non-qualified HSA additional tax on the wrong sub-line

**The mistake**: Filer took a $2,000 non-qualified HSA distribution; preparer enters the 20% additional tax on Schedule 2 Line 8 (Form 5329).

**Why it's wrong**: Form 5329 Part I (10% under §72(t)) is for early IRA / 401(k) distributions, not HSA. The 20% HSA additional tax under §223(f)(4) comes from Form 8889 line 17b and goes on Schedule 2 Line 17c.

**Citation**: IRC §223(f)(4); Form 8889 line 17b; 2025 Schedule 2 instructions, line 17c.

**Correction**: Move from Line 8 to Line 17c. Re-sum Line 18.

## 11. Not aggregating MFJ wages for Additional Medicare Tax

**The mistake**: MFJ couple, each spouse earns $150,000 W-2 wages. Each W-2 shows Medicare wages $150K with no Additional Medicare Tax withheld (since neither alone exceeds $200K). Preparer concludes no Additional Medicare Tax is due.

**Why it's wrong**: For MFJ, the threshold is $250,000 *combined*. Combined wages $300,000 → $50,000 above threshold → 0.9% × $50,000 = $450 Additional Medicare Tax owed via Form 8959, even though no employer withheld.

**Citation**: IRC §3101(b)(2)(B); Form 8959 instructions.

**Correction**: Run Form 8959 with combined Medicare wages. Schedule 2 Line 11 = $450.

## 12. Missing Form 6251 entry for a large SALT add-back

**The mistake**: Filer in a high-tax state (CA, NY, NJ) deducted state income tax + property tax on Schedule A. For 2025 the cap is $40,000 ($20,000 MFS), reduced when income exceeds $500,000 (P.L. 119-21; 2025 Schedule A line 5e). Preparer doesn't run Form 6251.

**Why it's wrong**: The full SALT deduction taken on Schedule A is added back for AMTI on Form 6251 line 2a. With the higher 2025 cap, the add-back can be several times the old $10,000. Combined with other adjustments, AMT may trigger — particularly for filers with depreciation differences or ISO exercises.

**Citation**: IRC §56(b)(1)(A)(ii); 2025 Form 6251 line 2a and instructions.

**Correction**: Always run the Form 6251 worksheet when SALT deduction is claimed; let the math decide whether AMT applies. Don't skip 6251 based on intuition.
