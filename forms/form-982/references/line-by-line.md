# Form 982 Line-by-Line Reference

Complete lookup for every line on Form 982. Use this when the agent needs to confirm what a line means or where a value goes.

Line map rebuilt from the PDF text of **Form 982 (Rev. March 2018)** and the **Instructions for Form 982 (Rev. December 2021)**, the current revisions as of 2026-10-06 (the About page lists "Recent Developments: None"). Re-check https://www.irs.gov/forms-pubs/about-form-982 before use; a new revision may renumber lines.

The form has 13 numbered lines in Parts I and II plus the Part III corporate consent. There is no line 14 and no total line.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name shown on return | Filer's name as on Form 1040 | Match the 1040 |
| Identifying number | SSN (individuals) or EIN (entities) | |

---

## Part I — General Information

### Line 1 — Amount excluded is due to (check applicable box(es))

The form says "check applicable box(es)": one Form 982 can carry more than one box when one discharge, or several discharges in the same year, fall under different exclusions. Pub. 4681 (2025) shows this: boxes 1b and 1c together (farm debt, insolvency Example 2) and 1b and 1d together (QRPBI Examples 1 and 2).

| Box | Code section | Form text | When to use |
|-----|--------------|-----------|-------------|
| 1a | §108(a)(1)(A) | Discharge of indebtedness in a title 11 case | Under the bankruptcy court's jurisdiction; discharge granted by the court or under a court-approved plan (§108(d)(2); any chapter, e.g. 7, 11, 12, 13) |
| 1b | §108(a)(1)(B) | Discharge of indebtedness to the extent insolvent (not in a title 11 case) | Liabilities exceeded FMV of assets immediately before the discharge (§108(d)(3); Pub. 4681 Insolvency Worksheet) |
| 1c | §108(a)(1)(C) | Discharge of qualified farm indebtedness | Debt incurred directly in operating a farming business; 50% or more of aggregate gross receipts for the 3 preceding tax years from farming; discharged by a qualified person (§108(g)) |
| 1d | §108(a)(1)(D) | Discharge of qualified real property business indebtedness | Taxpayer other than a C corporation; debt incurred or assumed in connection with, and secured by, real property used in a trade or business; pre-1993 debt or qualified acquisition indebtedness (§108(c)(3)); checking the box is the election |
| 1e | §108(a)(1)(E) | Discharge of qualified principal residence indebtedness (form caution: see instructions if discharged after 2017) | Debt to buy, build, or substantially improve the main home and secured by it; only for discharges before Jan. 1, 2026, or under an arrangement entered into and evidenced in writing before Jan. 1, 2026 |

**Coordination rules (§108(a)(2); i982 Lines 1b–1e)**:
- Title 11 first: boxes 1b through 1e don't apply to a discharge in a title 11 case. A title 11 discharge of home mortgage debt goes on 1a, never 1e.
- Insolvency before farm and QRPBI: the farm and QRPBI exclusions don't apply to the extent the taxpayer was insolvent (§108(a)(2)(B)). Apply 1b first, then 1c or 1d to the remainder.
- QPRI before insolvency, unless the taxpayer elects to check 1b instead of 1e (§108(a)(2)(C)).
- QRPBI is elective: the election is made by checking 1d on a timely filed return (including extensions).

### Line 2 — Total amount of discharged indebtedness excluded from gross income

The total excluded under §108 for all boxes checked. Limits (i982 Lines 1b–1e; Pub. 4681):
- Box 1a: no cap in §108(a).
- Box 1b: not more than the amount by which liabilities exceeded the FMV of assets immediately before the discharge (§108(a)(3)).
- Box 1c: not more than the sum of adjusted tax attributes (credits counted at $3 per $1) and the adjusted basis of qualified property held at the beginning of the next tax year (§108(g)(3)).
- Box 1d: not more than (i) outstanding principal immediately before the discharge minus the net FMV of the securing property (reduced by other QRPBI secured by it), and (ii) the aggregate adjusted basis of depreciable real property held immediately before the discharge, other than property acquired in contemplation of the discharge (§108(c)(2)).
- Box 1e: QPRI is acquisition debt up to $750,000 ($375,000 married filing separately) for discharges after 2020 (§108(h)(2)); if only part of a loan is QPRI, the exclusion applies only to the amount discharged in excess of the non-QPRI part (§108(h)(4) ordering rule).

Line 2 never exceeds the debt actually canceled. Box 2 of Form 1099-C may show only part of the canceled debt or include interest (Pub. 4681, "Amount of canceled debt"); reconcile to the actual cancellation.

**Line 2 does not have to equal Part II.** If 1a, 1b, or 1c is checked, line 2 won't necessarily equal the total of lines 5 through 13 (excluding 10b) because the excluded amount may exceed the available tax attributes. If 1e is checked, line 2 won't necessarily equal line 10b (i982 Line 2; Pub. 4681 "Reduction of Tax Attributes").

### Line 3 — Election to treat real property held for sale as depreciable property

Form text: "Do you elect to treat all real property described in section 1221(a)(1), relating to property held for sale to customers in the ordinary course of a trade or business, as if it were depreciable property?" Yes / No.

- Authority: §1017(b)(3)(E). The election lets inventory real estate absorb a line 5 basis reduction (i982 Part II "Basis Reduction") or a farm-debt basis reduction (Pub. 4681).
- It does not apply to the discharge of qualified real property business indebtedness (i982 Line 3; §1017(b)(3)(F)(ii)).
- Made on the return for the year of the discharge; revocable only with IRS consent (§1017(b)(3)(E)(ii)).
- Most individual filers check "No" or leave it blank. Ask before checking "Yes"; it only matters for a dealer in real estate.

Line 3 is **not** the §108(b)(5) election. That election is line 5.

---

## Part II — Reduction of Tax Attributes

Form header: "You must attach a description of any transactions resulting in the reduction in basis under section 1017. See Regulations section 1.1017-1 for basis reduction ordering rules, and, if applicable, required partnership consent statements." Every line in Part II is an **amount excluded from gross income** applied to that attribute ("Enter amount excluded from gross income"). For credit lines, enter the excluded dollars applied; the credit itself drops by 33⅓ cents per dollar (i982 Line 7; §108(b)(3)(B)).

Default order when 1a, 1b, or 1c is checked and no line 5 election is made: lines 6, 7, 8, 9, 10a (or 11a–11c for farm debt), 12, 13 (i982 "Any other debt"; §108(b)(2)). Reductions are made after the tax for the discharge year is figured (§108(b)(4)(A)).

### Line 4 — QRPBI applied to reduce the basis of depreciable real property

Box 1d only. Enter the excluded QRPBI amount; it reduces the basis of depreciable real property (§108(c)(1); §1017(b)(3)(F)). The reduction is made at the beginning of the next tax year, or immediately before disposition if the property is sold first (Pub. 4681 "Qualified Real Property Business Indebtedness"; §1017(b)(3)(F)(iii)). Land is not depreciable real property.

### Line 5 — Election under §108(b)(5) to reduce the basis of depreciable property first

- Available when box 1a, 1b, or 1c is checked (i982 Part II "Basis Reduction"). Completing line 5 is the election; there is no checkbox.
- Enter all or part of the excluded amount; it reduces the basis (under §1017) of depreciable property, including real property elected on line 3. The balance, if any, goes to lines 6 through 13 (excluding 10b).
- Limited to the aggregate adjusted bases of depreciable property held at the beginning of the next tax year (§108(b)(5)(B)). The §1017(b)(2) liabilities limit that applies to line 10a does not apply to line 5 (i982 Line 10a).
- Must be made on a timely filed return (including extensions); revocable only with IRS consent. If the return was timely filed without it, the election can be made on an amended return filed within 6 months of the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2" (i982 "When To File"; §108(d)(9)).
- Basis reduction order under the election (Pub. 4681): (1) depreciable real property used in a trade or business or held for investment that secured the canceled debt; (2) depreciable personal property used in a trade or business or held for investment that secured the canceled debt; (3) other depreciable property used in a trade or business or held for investment; (4) real property held for sale to customers, if elected on line 3.

### Line 6 — Net operating loss

NOL for the tax year of the discharge, then NOL carryovers to that year in order of the years they arose, starting with the earliest (§108(b)(4)(B)). Dollar for dollar. $0 if none.

### Line 7 — General business credit carryover

Carryovers to or from the discharge year (Form 3800). Reduce the carryover by 33⅓ cents for each dollar excluded (i982 Line 7). Enter the excluded dollars applied: absorbing a $1,000 carryover uses $3,000 of excluded amount, so line 7 shows $3,000. $0 if none.

### Line 8 — Minimum tax credit

Minimum tax credit available as of the beginning of the tax year after the discharge year (§108(b)(2)(C)). 33⅓ cents per dollar; enter the excluded dollars applied. $0 if none.

### Line 9 — Net capital loss and capital loss carryovers

Net capital loss for the discharge year, then capital loss carryovers to that year, earliest first (§108(b)(4)(B)). Dollar for dollar. $0 if none.

### Line 10a — Basis of nondepreciable and depreciable property (if not reduced on line 5)

Not for qualified farm indebtedness (form text). Dollar for dollar. Basis is reduced for property held at the beginning of the next tax year (§1017(a)), in this order and, within each category, in proportion to adjusted basis (Pub. 4681 "Basis"):
1. Real property used in a trade or business or held for investment (other than real property held for sale to customers) that secured the canceled debt
2. Personal property used in a trade or business or held for investment (other than inventory and accounts and notes receivable) that secured the canceled debt
3. Any other property used in a trade or business or held for investment (other than inventory, accounts and notes receivable, and real property held for sale)
4. Inventory, accounts receivable, notes receivable, and real property held primarily for sale to customers
5. Personal-use property

**Limit in title 11 and insolvency cases:** the line 10a reduction can't exceed the excess of the aggregate bases of property held immediately after the discharge over the aggregate liabilities immediately after the discharge (§1017(b)(2); i982 Line 10a). In a title 11 case, exempt property is not reduced (§1017(c)(1)).

**Nonbusiness debt with no attributes other than basis of nondepreciable property** (i982 "How To Complete the Form", "A nonbusiness debt"): check 1a or 1b, enter the excluded amount on line 2, and enter on line 10a the **smallest** of:
- (a) the basis of the nondepreciable property,
- (b) the amount of the nonbusiness debt on line 2, or
- (c) the excess of the aggregate bases of property plus money held immediately after the discharge over aggregate liabilities immediately after the discharge.

Compute all three and show them. For an insolvent filer, (c) is often $0, which makes line 10a $0; say so in the draft rather than leaving the line blank. Pub. 4681's repossessed-car example gets $100 for (c) and allocates it 91%/9% between furniture and jewelry by basis.

### Line 10b — Basis of the principal residence

**Only if box 1e is checked** (form text) and only if the taxpayer continues to own the home after the discharge. Enter the smaller of (a) the part of line 2 attributable to the QPRI exclusion or (b) the basis of the main home (i982 Line 10b; §108(h)(1)). If the home was sold, foreclosed, or otherwise disposed of in the transaction (short sale, foreclosure, deed in lieu), line 10b is $0.

### Line 11 — Qualified farm indebtedness: basis reduction

Box 1c only, for amounts not absorbed by lines 6–9 and not reduced on line 5 (i982 Line 1c; §1017(b)(4)):
- **11a** Depreciable property used or held for use in a trade or business or for the production of income, if not reduced on line 5
- **11b** Land used or held for use in a trade or business of farming
- **11c** Other property used or held for use in a trade or business or for the production of income

### Line 12 — Passive activity loss and credit carryovers

Carryovers from the discharge year (Form 8582 / 8582-CR). Losses dollar for dollar; credits 33⅓ cents per dollar (i982 "Any other debt", item 6). $0 if none.

### Line 13 — Foreign tax credit carryover

Carryovers to or from the discharge year (Form 1116). 33⅓ cents per dollar. $0 if none.

### Reconciliation (the math)

```
Line 2 ≥ Line 4 + Line 5 + Lines 6–9 + Line 10a + Lines 11a–11c + Line 12 + Line 13   (for 1a/1b/1c/1d)
Line 2 ≥ Line 10b                                                                      (for 1e)
Each Part II line ≤ the attribute available (credits: excluded dollars ≤ 3 × credit)
```

If the excluded amount exceeds the available attributes, the excess stays excluded and no further reduction is required (Pub. 4681 "Reduction of Tax Attributes": "the total reduction of tax attributes in Part II of Form 982 will be less than the amount on line 2").

---

## Part III — Consent of Corporation to Adjustment of Basis of Its Property Under Section 1082(a)(2)

Corporations only: consent under §1081(b) to adjust basis under §1082(a)(2) (Regulations section 1.1082-3(b)), with a description of the transactions resulting in nonrecognition of gain under §1081. It has nothing to do with the §108(b)(5) election. Leave Part III blank for individual and sole-proprietor filers.

---

## Worksheets and supporting documentation

### Pub. 4681 Insolvency Worksheet

Use when box 1b is checked. Pub. 4681 (2025) worksheet: Part I lines 1–15 (liabilities), Part II lines 16–37 (FMV of assets, including line 28 retirement accounts and line 29 pension plan), Part III line 38 (amount of insolvency). Marked "Keep for Your Records"; it is not attached to the return. See [`insolvency-worksheet.md`](./insolvency-worksheet.md).

### §1017 basis-reduction statement

Required whenever Part II reduces basis (lines 4, 5, 10a, 11a–11c): a description of the transactions resulting in the basis reduction and the property whose basis was reduced (Form 982 Part II header; i982 Part II "Basis Reduction").

### QRPBI election

Made by checking box 1d and completing Form 982 on a timely filed return (Pub. 4681 "How to elect the qualified real property business debt exclusion"). Attach the §1017 statement above for the line 4 reduction.

### Bankruptcy documents

If box 1a is checked, keep the case number, chapter, and discharge order or confirmed plan with the records. Form 982 instructions don't require attaching them.

### Principal residence documentation

If box 1e is checked, keep the mortgage, closing, and refinance documents showing the debt was used to buy, build, or substantially improve the main home and was secured by it, plus any written arrangement dated before Jan. 1, 2026 for a 2026 discharge.

---

## Reconciling with Form 1099-C

```
Canceled debt (1099-C Box 2, corrected to the actual cancellation)   $X,XXX
- Form 982 Line 2 (excluded amount)                                 $X,XXX
= Taxable canceled debt                                              $X,XXX
```

Where the taxable part goes (Pub. 4681 chapter 1): Schedule 1 (Form 1040) line 8c for nonbusiness debt; Schedule C line 6 for a nonfarm sole proprietorship; Schedule E line 3 for nonfarm rental real property; Form 4835 line 6 for farm rental; Schedule F line 8 for farm debt.

Excluding the entire amount when only part qualifies is a common error.

---

## Common edge cases

### Multiple 1099-Cs in the same year

Analyze each debt separately (a different exclusion may apply to each), then report on one Form 982: check every applicable box on line 1 and enter the total excluded on line 2. Debts with no exclusion go to the income line for that debt type.

### 1099-C from a related party

A cancellation that is a gift, bequest, devise, or inheritance generally is not income (Pub. 4681 "Exceptions"); a corporation canceling a stockholder's debt is a constructive distribution (Pub. 4681 "Stockholder Debt"). Investigate before excluding.

### Recourse vs. nonrecourse debt

For nonrecourse debt, a foreclosure or abandonment produces no cancellation-of-debt income: the full debt is the amount realized on the disposition (Pub. 4681 chapter 1, "Sales or Other Dispositions" and "Abandonments"). For recourse debt, the excess of the canceled debt over the property's FMV is cancellation-of-debt income. See Pub. 4681 chapters 2 and 3.

### Discharge timing and bankruptcy

Box 1a applies only if the taxpayer was under the court's jurisdiction and the discharge was granted by the court or under a court-approved plan (§108(d)(2)). A cancellation before the petition or after dismissal is not a title 11 discharge; test insolvency instead. In chapter 7 or 11 cases to which §1398 applies, the bankruptcy estate, not the individual, reduces the attributes (§108(d)(8)); refer these to a CPA (Pub. 908).

### Pass-through entity discharges

Partnerships: §108(a), (b), (c), and (g) are applied at the partner level (§108(d)(6)); each partner files their own Form 982. S corporations: those subsections are applied at the corporate level (§108(d)(7)), so the exclusion and attribute reduction belong to the S corporation, not the shareholder. Out of scope for this skill; refer to a CPA.

### Canceled student loans

§108(f) student loan exclusions are not §108(a) exclusions and are not claimed on Form 982 (i982 "When To File" covers §108(a) exclusions; Pub. 4681 treats student loans under "Exceptions", which apply before the exclusions and don't reduce tax attributes).
- Work-requirement discharges (§108(f)(1)) and the health-care repayment programs (§108(f)(4)) remain.
- The broad §108(f)(5) exclusion enacted by the American Rescue Plan Act covered discharges after Dec. 31, 2020 and before Jan. 1, 2026 (Pub. 4681 "Special rule for student loan discharges for 2021 through 2025").
- For discharges after Dec. 31, 2025, P.L. 119-21 §70119 rewrote §108(f)(5): it excludes only discharges on account of death or total and permanent disability (federal student loans and private education loans), and only if the taxpayer's SSN, valid for employment and issued before the return due date, is on the return (§108(f)(5)(C); Pub. 4681 (2025) "What's New").
- Other student loan discharges after 2025 (not covered by §108(f)(1) or (f)(4)) are income unless a §108(a) exclusion (for example insolvency, on Form 982) applies.
