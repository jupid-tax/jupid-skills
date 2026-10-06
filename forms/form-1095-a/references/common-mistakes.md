# Common Mistakes on Form 1095-A and Form 8962

The ten most-flunked items, with citation and fix.

---

## 1. Filing without Form 8962 when 1095-A was received

**Problem**: Filer received Form 1095-A with APTC in Column C but skips Form 8962, or had no APTC and never checks whether a net PTC is available.

**Impact**: With APTC paid: the return cannot be processed correctly without Form 8962, and the Marketplace can find the filer ineligible for APTC in a later year until they reconcile. Without APTC: any net PTC the user qualified for is forfeited.

**Citation**: IRC §36B(f); 2025 Form 1095-A, Instructions for Recipient (Form 8962 is required if any amount other than zero is in Part III, column C, or to take the PTC, whether or not a return is otherwise required); Form 8962 instructions ("Who Must File").

**Fix**: File Form 8962 whenever Column C shows APTC. With zero APTC, compute Form 8962 to see whether net PTC is available and file it if so.

---

## 2. Using the wrong year's FPL table

**Problem**: Filer uses 2025 FPL for tax year 2025 instead of 2024 FPL.

**Impact**: Wrong Line 5 percentage, wrong applicable figure, wrong PTC.

**Citation**: Form 8962 instructions ("Federal Poverty Line"); IRC §36B(d)(3)(B) (uses "the most recently published poverty line as of the first day of the regular enrollment period").

**Fix**: For tax year YYYY, use the HHS guidelines published in January of year YYYY − 1 (e.g., 2024 guidelines for a 2025 return).

---

## 3. Column B is $0 in some months

**Problem**: 1095-A Part III Column B (SLCSP) is missing for one or more months. Filer enters $0 on Form 8962 and skips ahead.

**Impact**: PTC = lesser of premium or (SLCSP − contribution). If SLCSP = 0, max premium assistance = max(0, 0 − contribution) = 0. PTC = 0 for that month. User loses the credit they actually qualify for.

**Citation**: Form 8962 instructions, Lines 11–23 column (b) (applicable SLCSP premium); 2025 Instructions for Form 1095-A, Part III, column B.

**Fix**: First confirm the -0- is not correct (all enrollees joined after the first of the month, or premiums for the month were not paid). Otherwise use the [healthcare.gov Tax Tool](https://www.healthcare.gov/tax-tool/) (federal Marketplace) or state Marketplace tool to look up the correct SLCSP. Enter the looked-up value on Form 8962, even if 1095-A Column B is $0.

---

## 4. Filing MFS without a qualifying exception

**Problem**: Married filer files separately from spouse and claims PTC.

**Impact**: PTC denied entirely (MFS-status filers are not "applicable taxpayers" except in narrow circumstances). All APTC is excess; for 2025 the repayment is limited per Table 5, applied to each spouse separately; for 2026 there is no limit.

**Citation**: IRC §36B(c)(1)(C); Form 8962 instructions ("Married Filing Separately").

**Fix**: File MFJ if at all possible. The MFS exception applies only if:
- The filer is a victim of domestic abuse, OR
- The filer is a victim of spousal abandonment

Both require the filer to check the box on Form 8962 line A (and to meet the other conditions in the instructions, Exception 2). If neither applies, switching to MFJ is the only way to claim PTC.

---

## 5. Not allocating shared policy amounts

**Problem**: Two unmarried parents share a policy covering their child. One parent claims the child as dependent. The other parent has the 1095-A. Both file Form 8962 using the full 1095-A amounts.

**Impact**: IRS receives duplicate amounts. Both returns flagged. Refunds delayed. CP2000 notices issued.

**Citation**: Treas. Reg. §1.36B-4; Form 8962 instructions, Line 9 and Part IV (Allocation Situations 1–4).

**Fix**: Agree on allocation percentages with the other taxpayer (same percentage for premium, SLCSP, and APTC in a month). Both file Form 8962 Part IV with matching allocations and use the monthly calculation. Without an agreement, unmarried parents (Situation 4) use the enrolled-individuals ratio: individuals enrolled by one parent who are in the other's tax family ÷ total enrolled; 50/50 applies only to spouses who divorced during the year or MFS.

---

## 6. Including non-tax-family members in Line 1

**Problem**: Filer counts all 1095-A Part II covered individuals on Line 1 (Tax family size), including a child claimed as dependent by an ex-spouse.

**Impact**: Wrong family size, wrong FPL, wrong PTC.

**Citation**: Form 8962 instructions ("Tax family size").

**Fix**: Line 1 = filer + spouse (if MFJ) + dependents on the return. Anyone on 1095-A Part II who isn't on the return is excluded from Line 1 and triggers Part IV allocation instead.

---

## 7. Forgetting to add tax-exempt interest, foreign earned income, and non-taxable Social Security to AGI

**Problem**: Filer enters AGI from Form 1040 Line 11a directly on Form 8962 Line 2a without adding modifications.

**Impact**: Modified AGI under-stated. Line 5 percentage too low. PTC over-claimed. CP2000 notice with adjustment.

**Citation**: IRC §36B(d)(2)(B); Form 8962 instructions, Line 2a.

**Fix**: Modified AGI = AGI + tax-exempt interest (Form 1040 Line 2a) + excluded foreign earned income and housing (Form 2555, lines 45 and 50) + non-taxable Social Security benefits. Use Worksheet 1-1 in the Form 8962 instructions.

---

## 8. Ignoring a corrected 1095-A

**Problem**: Filer files using original 1095-A. Marketplace mails corrected version in March or April. Filer doesn't amend.

**Impact**: Original Form 8962 has wrong amounts. IRS receives corrected 1095-A from Marketplace, compares to filed return, issues CP2000 with proposed adjustment plus interest.

**Citation**: 2025 Form 1095-A, Instructions for Recipient ("CORRECTED box"); 2025 Instructions for Form 1095-A ("Correction to Information Reported").

**Fix**: File Form 1040-X amended return with corrected Form 8962 ([`form-1040-x`](../../form-1040-x/SKILL.md)). Note "1095-A corrected" in the explanation of changes. Doing it proactively limits interest accrual.

---

## 9. Using the wrong applicable figure (pre-ARPA vs. ARPA/IRA)

**Problem**: Filer uses the wrong year's applicable figure table, e.g., the 2026 table (9.96% at 300–400% FPL) for a 2025 return, or the 2025 table (8.5% above 400%) for a 2026 return.

**Impact**: Contribution amount wrong, PTC wrong. On a 2025 return the net PTC owed to the filer can be missed; on a 2026 return PTC can be overclaimed.

**Citation**: IRC §36B(b)(3)(A) as amended by ARPA and IRA; Rev. Proc. 2024-35 (2025 table); Rev. Proc. 2025-25 (2026 table).

**Fix**: For tax years 2021–2025, use ARPA/IRA-extended applicable figures (lower percentages, no upper cap). For 2026, use the Rev. Proc. 2025-25 table: no PTC above 400% FPL (no extension enacted as of 2026-10-06).

---

## 10. Missing the Net PTC refund flow

**Problem**: Filer correctly calculates Form 8962 Line 26 (Net PTC = $1,500) but forgets to enter it on Schedule 3 Line 9.

**Impact**: PTC not actually claimed on the tax return. User loses refundable credit.

**Citation**: Form 1040 instructions; Schedule 3 instructions.

**Fix**: Form 8962 Line 26 → Schedule 3 Line 9 → Form 1040 Line 31 (Total of Schedule 3 → reduces tax owed or increases refund).

Conversely, Form 8962 Line 29 → Schedule 2 Line 1a → Schedule 2 Line 3 → Form 1040 Line 17 (adds to tax owed).

---

## Source

- IRS Publication 974 (Premium Tax Credit) — comprehensive guide
- Form 8962 instructions (annual revision)
- Form 1095-A instructions (annual revision)
- IRC §36B, including §36B(f)(3) (Form 1095-A reporting)
- Form 8962 instructions, Table 5 (repayment limits, tax years before 2026)
