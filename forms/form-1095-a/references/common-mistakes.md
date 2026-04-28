# Common Mistakes on Form 1095-A and Form 8962

The ten most-flunked items, with citation and fix.

---

## 1. Filing without Form 8962 when 1095-A was received

**Problem**: Filer received Form 1095-A but skips Form 8962 because they "didn't get APTC" or "had Marketplace coverage but want to skip the math."

**Impact**: IRS rejection of e-filed return. Future APTC eligibility blocked until reconciliation is filed. Forfeit any net PTC the user qualified for.

**Citation**: IRC §36B(g); Form 8962 instructions ("Who Must File").

**Fix**: Always file Form 8962 if 1095-A was received, even with zero APTC. Form 8962 establishes whether net PTC is owed to the user.

---

## 2. Using the wrong year's FPL table

**Problem**: Filer uses 2025 FPL for tax year 2025 instead of 2024 FPL.

**Impact**: Wrong Line 5 percentage, wrong applicable figure, wrong PTC.

**Citation**: Form 8962 instructions ("Federal Poverty Line"); IRC §36B(d)(3)(B) (uses "the most recently published poverty line as of the first day of the regular enrollment period").

**Fix**: For tax year YYYY, use the FPL released in January of year YYYY (i.e., the prior calendar year's FPL).

---

## 3. Column B is $0 in some months

**Problem**: 1095-A Part III Column B (SLCSP) is missing for one or more months. Filer enters $0 on Form 8962 and skips ahead.

**Impact**: PTC = lesser of premium or (SLCSP − contribution). If SLCSP = 0, max premium assistance = max(0, 0 − contribution) = 0. PTC = 0 for that month. User loses the credit they actually qualify for.

**Citation**: Form 8962 instructions; IRS Notice 2015-87.

**Fix**: Use the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or state Marketplace tool to look up the correct SLCSP. Enter the looked-up value on Form 8962, even if 1095-A Column B is $0.

---

## 4. Filing MFS without a qualifying exception

**Problem**: Married filer files separately from spouse and claims PTC.

**Impact**: PTC denied entirely (MFS-status filers are not "applicable taxpayers" except in narrow circumstances). Excess APTC repayment is uncapped. Return rejected or assessed.

**Citation**: IRC §36B(c)(1)(C); Form 8962 instructions ("Married Filing Separately").

**Fix**: File MFJ if at all possible. The MFS exception applies only if:
- The filer is a victim of domestic abuse, OR
- The filer is a victim of spousal abandonment

Both require the filer to check the exception box on Form 8962. If neither applies, switching to MFJ is the only way to claim PTC.

---

## 5. Not allocating shared policy amounts

**Problem**: Two unmarried parents share a policy covering their child. One parent claims the child as dependent. The other parent has the 1095-A. Both file Form 8962 using the full 1095-A amounts.

**Impact**: IRS receives duplicate amounts. Both returns flagged. Refunds delayed. CP2000 notices issued.

**Citation**: IRC §36B(d)(2); Pub 974 Chapter 4; Form 8962 Part IV.

**Fix**: Agree on allocation percentages with the other taxpayer. Both file Form 8962 Part IV with matching allocations. Default 50/50 if no agreement.

---

## 6. Including non-tax-family members in Line 1

**Problem**: Filer counts all 1095-A Part II covered individuals on Line 1 (Tax family size), including a child claimed as dependent by an ex-spouse.

**Impact**: Wrong family size, wrong FPL, wrong PTC.

**Citation**: Form 8962 instructions ("Tax family size").

**Fix**: Line 1 = filer + spouse (if MFJ) + dependents on the return. Anyone on 1095-A Part II who isn't on the return is excluded from Line 1 and triggers Part IV allocation instead.

---

## 7. Forgetting to add tax-exempt interest, foreign earned income, and non-taxable Social Security to AGI

**Problem**: Filer enters AGI from Form 1040 Line 11 directly on Form 8962 Line 2a without adding modifications.

**Impact**: Modified AGI under-stated. Line 5 percentage too low. PTC over-claimed. CP2000 notice with adjustment.

**Citation**: IRC §36B(d)(2)(B); Form 8962 instructions, Line 2a.

**Fix**: Modified AGI = AGI + tax-exempt interest (Form 1040 Line 2a) + excluded foreign earned income (Form 2555) + non-taxable Social Security benefits. Use the Modified AGI Worksheet in Form 8962 instructions.

---

## 8. Ignoring a corrected 1095-A

**Problem**: Filer files using original 1095-A. Marketplace mails corrected version in March or April. Filer doesn't amend.

**Impact**: Original Form 8962 has wrong amounts. IRS receives corrected 1095-A from Marketplace, compares to filed return, issues CP2000 with proposed adjustment plus interest.

**Citation**: Form 1095-A instructions ("Corrected Form").

**Fix**: File Form 1040-X amended return with corrected Form 8962. Note "1095-A corrected" in Part III explanation. Doing it proactively avoids penalty interest accrual.

---

## 9. Using the wrong applicable figure (pre-ARPA vs. ARPA/IRA)

**Problem**: Filer uses pre-ARPA applicable figure table (e.g., 9.86% at 400% FPL) for tax year 2024.

**Impact**: Contribution amount over-stated, PTC under-claimed. Net PTC owed to filer is missed.

**Citation**: IRC §36B(b)(3)(A) as amended by ARPA and IRA; Rev. Proc. 2024-36 (2025 figures).

**Fix**: For tax years 2021–2025, use ARPA/IRA-extended applicable figures (lower percentages, no upper cap). For 2026+, verify whether the expansion was extended.

---

## 10. Missing the Net PTC refund flow

**Problem**: Filer correctly calculates Form 8962 Line 26 (Net PTC = $1,500) but forgets to enter it on Schedule 3 Line 9.

**Impact**: PTC not actually claimed on the tax return. User loses refundable credit.

**Citation**: Form 1040 instructions; Schedule 3 instructions.

**Fix**: Form 8962 Line 26 → Schedule 3 Line 9 → Form 1040 Line 31 (Total of Schedule 3 → reduces tax owed or increases refund).

Conversely, Form 8962 Line 29 → Schedule 2 Line 1a → Form 1040 Line 23 (Total of Schedule 2 → adds to tax owed).

---

## Source

- IRS Publication 974 (Premium Tax Credit) — comprehensive guide
- Form 8962 instructions (annual revision)
- Form 1095-A instructions (annual revision)
- IRC §36B and §6055
- Pub 974 Table 5 (repayment limits)
