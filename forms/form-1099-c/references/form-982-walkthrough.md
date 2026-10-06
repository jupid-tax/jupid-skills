# Form 982 — Line-by-Line Walkthrough

Form 982 ("Reduction of Tax Attributes Due to Discharge of Indebtedness (and Section 1082 Basis Adjustment)") is the form that documents a §108(a) exclusion. It has three parts; individuals use Parts I and II. Part III is for corporations only.

This file covers the form line by line, the attribute-reduction order, and the §108(b)(5) election.

Form revision in scope: **Form 982 (Rev. March 2018)** with the **Instructions for Form 982 (Rev. December 2021)**, both current on 2026-10-06 (About Form 982: "Recent Developments: None"). Check the [current PDF](https://www.irs.gov/pub/irs-pdf/f982.pdf) and https://www.irs.gov/forms-pubs/about-form-982 for the tax year being filed.

---

## When to file

File Form 982 with the income tax return "for a year a discharge of indebtedness is excluded from your income under section 108(a)" (Form 982 instructions, "When To File"):

- §108(a)(1)(A) bankruptcy → required (box 1a)
- §108(a)(1)(B) insolvency → required (box 1b)
- §108(a)(1)(C) qualified farm indebtedness → required (box 1c)
- §108(a)(1)(D) qualified real property business indebtedness → required (box 1d)
- §108(a)(1)(E) qualified principal residence indebtedness → required (box 1e); only for debt discharged before Jan. 1, 2026 or under a written arrangement entered into before that date
- §108(f) student loan exclusions are not §108(a) exclusions → no Form 982 (Pub. 4681 covers them under "Exceptions")

If no exclusion is claimed and the canceled amount is reportable as income, **do not** file Form 982. Just report the income on Schedule 1 Line 8c (or Schedule C Line 6 for sole-proprietor business debt, Schedule E Line 3 for nonfarm rental real property debt, Schedule F Line 8 for farm debt; Pub. 4681).

The §108(b)(5) election (line 5) and the box 1d election must be made on a timely filed return (including extensions); a missed election can still be made on an amended return filed within 6 months of the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2".

---

## Header

| Field | What goes here |
|-------|----------------|
| Name shown on return | Filer's name as on the 1040 |
| Identifying number | SSN or ITIN (matches 1040) |

If spouses file separately, each completes their own Form 982 and Insolvency Worksheet for their share of a joint debt (Pub. 4681, Insolvency, Example 3). For a joint return, Pub. 4681 gives no separate example; flag how insolvency was measured for a CPA to review.

---

## Part I — General Information

### Lines 1a-1e — Type of discharge

Check the box(es) that match the exclusion claimed (the form says "check applicable box(es)").

| Line | Box | Use this when |
|------|-----|---------------|
| **1a** | Discharge of indebtedness in a title 11 case | §108(a)(1)(A) bankruptcy — the court has jurisdiction and grants the discharge or approves the plan |
| **1b** | Discharge of indebtedness to the extent insolvent (not in a title 11 case) | §108(a)(1)(B) insolvency — liabilities exceeded FMV of assets immediately before the discharge |
| **1c** | Discharge of qualified farm indebtedness | §108(a)(1)(C) — farmer-specific; not in a title 11 case or to the extent insolvent |
| **1d** | Discharge of qualified real property business indebtedness | §108(a)(1)(D) — non-corporate (or S corporation) taxpayer, debt secured by real property used in a trade or business; this is an election |
| **1e** | Discharge of qualified principal residence indebtedness | §108(a)(1)(E) — main-home acquisition debt discharged before 2026 (or under a pre-2026 written arrangement). Not allowed in a title 11 case (use 1a); an insolvent filer may elect 1b instead |

### Line 2 — Total amount of discharged indebtedness excluded from gross income

The dollar amount being excluded.

- **Bankruptcy:** Line 2 = canceled amount discharged in the title 11 case
- **Insolvency:** Line 2 = min(canceled amount, insolvency amount). Cannot exceed insolvency.
- **Qualified principal residence:** Line 2 = the excludable QPRI amount after the ordering rule (only the part of the discharge above the loan's nonqualified part), within the $750,000 ($375,000 MFS) QPRI limit.
- **Multiple boxes checked:** Line 2 = sum of all amounts excluded.

Line 2 "won't necessarily equal" the Part II reductions: when the excluded amount exceeds the filer's tax attributes, the Part II total is smaller (Form 982 instructions, Line 2).

### Line 3 — Election under §1017(b)(3)(E)

Check **Yes** to treat all real property held primarily for sale to customers in the ordinary course of a trade or business as if it were depreciable property (relevant to the line 5 election). It does not apply to qualified real property business indebtedness.

For consumer filers, leave it unchecked.

---

## Part II — Reduction of Tax Attributes

Part II applies the excluded amount against tax attributes. A description of any basis reduction under §1017 must be attached.

**Order of reduction** for boxes 1a and 1b (and 1c), unless the line 5 election is made (Form 982 instructions, "Any other debt"):

1. **Net operating loss** for the year of discharge and NOL carryovers to that year → Line 6 (dollar for dollar)
2. **General business credit** carryovers to or from the year → Line 7 (33⅓ cents per dollar)
3. **Minimum tax credit** as of the start of the next tax year → Line 8 (33⅓ cents per dollar)
4. **Net capital loss** for the year and capital loss carryovers → Line 9 (dollar for dollar)
5. **Basis of property** → Line 10a (farm debt: Lines 11a–11c)
6. **Passive activity loss and credit carryovers** → Line 12 (losses dollar for dollar; credits 33⅓ cents per dollar)
7. **Foreign tax credit carryovers** → Line 13 (33⅓ cents per dollar)

Box 1d (QRPBI) reduces only the basis of depreciable real property (Line 4). Box 1e (QPRI) reduces only the basis of the home (Line 10b), and only if the filer still owns it.

### Line 4 — QRPBI applied to reduce basis of depreciable real property

Only with box 1d. Consumers leave it blank.

### Line 5 — §108(b)(5) election

Amount the filer elects to apply first to reduce the basis of depreciable property (including property elected on line 3), before the line 6–13 order. See "§108(b)(5) election" below. Consumers leave it blank.

### Line 6 — Net operating loss

Reduce the NOL for the year of discharge, then NOL carryovers to that year.

For most consumer filers without business losses, NOL = 0.

### Line 7 — General business credit carryover

Reduce by 33⅓ cents for each dollar excluded (Form 982 instructions, Line 7; see Form 3800).

### Line 8 — Minimum tax credit

Minimum tax credit as of the beginning of the tax year after the discharge year; 33⅓ cents per dollar.

### Line 9 — Net capital loss

Current-year net capital loss and carryovers to the discharge year; dollar for dollar.

### Line 10a — Basis of nondepreciable and depreciable property (if not reduced on line 5)

Not for qualified farm debt. In a title 11 or insolvency case, the basis reduction is limited to the excess of the aggregate basis of the filer's property over aggregate liabilities, both immediately after the discharge (§1017(b)(2); Form 982 instructions, Line 10a). The limit doesn't apply to a line 5 reduction.

**Nonbusiness debt (car loan, credit card) with no attributes other than basis of personal-use property** (Form 982 instructions, "A nonbusiness debt"; Pub. 4681 "Reduction of Tax Attributes"): enter the smallest of

- (a) the basis of nondepreciable property,
- (b) the amount on line 2, or
- (c) the excess of the aggregate bases of property **plus money** held immediately after the discharge over aggregate liabilities immediately after the discharge.

For an insolvent consumer, (c) is usually $0 because liabilities still exceed bases and cash after the discharge. Compute it anyway and show the numbers. The reduction applies to personal-use property held at the beginning of the next year, in proportion to adjusted basis.

§1017 and Treas. Reg. §1.1017-1 govern the order of basis reduction among properties for business and investment property.

### Line 10b — Basis of principal residence (box 1e only)

If box 1e is checked **and the filer continues to own the residence after the discharge**, enter the smaller of the box 1e amount included on line 2 or the basis of the main home (Form 982 instructions, Line 10b). After a foreclosure or short sale, the filer no longer owns the home, so there is no Line 10b entry.

### Lines 11a-11c — Qualified farm indebtedness

Basis reductions for depreciable property, farmland, and other business property when box 1c is checked. Farm filers only.

### Line 12 — Passive activity loss and credit carryovers

Losses dollar for dollar; credits 33⅓ cents per dollar.

### Line 13 — Foreign tax credit carryover

33⅓ cents per dollar.

There is no "total" line on Form 982. If the filer has fewer attributes than the excluded amount, the excess just goes unused: it is not added back to income and not carried forward (Pub. 4681: if line 2 is more than total tax attributes, the Part II total will be less than line 2).

---

## §108(b)(5) election (Line 5)

§108(b)(5) lets the filer elect to reduce **basis of depreciable property first** (line 5), before the §108(b)(2) order. It can preserve NOLs and credits at the cost of lower depreciation or a larger gain later. Only available with boxes 1a–1c.

**When to consider:** significant depreciable property and significant NOLs or credits.

**When not:** no depreciable property or no NOLs to preserve (most consumers). Leave line 5 blank. Refer anyone considering it to a CPA.

---

## Part III — Consent of Corporation to Adjustment of Basis

Used only by a corporation excluding income under §1081(b) and consenting to basis adjustment under §1082(a)(2). Individuals never complete Part III.

---

## Sample completed Form 982 — consumer insolvency case

Jenna's $13,000 credit card cancellation (see `../examples/credit-card-settled-with-insolvency.md`), insolvent by $21,000 immediately before the discharge. Immediately after: liabilities $45,000 (other cards $20,000 + auto loan $25,000); property bases plus money $17,500 (car bought for $17,500; 401(k) has no basis; $0 cash left after paying the $5,000 settlement).

```
Name: Jenna Doe
Identifying number: XXX-XX-XXXX

Part I — General Information
1a. Discharge of indebtedness in a title 11 case ........... ☐
1b. Discharge of indebtedness to the extent insolvent ...... ☑
1c. Discharge of qualified farm indebtedness ............... ☐
1d. Discharge of qualified real property business .......... ☐
1e. Discharge of qualified principal residence ............. ☐
2.  Total amount of discharged indebtedness excluded ....... $13,000
3.  §1017(b)(3)(E) election ................................ (not checked)

Part II — Reduction of Tax Attributes
4.   QRPBI basis reduction ................................. (blank)
5.   §108(b)(5) election ................................... (blank)
6.   NOL ................................................... $0
7.   General business credit ............................... $0
8.   Minimum tax credit .................................... $0
9.   Net capital loss ...................................... $0
10a. Basis of property ..................................... $0
     smallest of (a) basis of nondepreciable property $17,500,
     (b) line 2 $13,000, (c) $17,500 bases + $0 money − $45,000
     liabilities after discharge = $0 → $0
10b. Basis of principal residence .......................... (blank; box 1e not checked)
11a–11c. Farm .............................................. (blank)
12.  Passive activity loss and credit carryovers ........... $0
13.  Foreign tax credit carryover .......................... $0
```

Part II total ($0) is less than line 2 ($13,000) because Jenna has no attributes to reduce. The unreduced excess is not added back to income and not carried forward.

---

## Sample completed Form 982 — principal residence, home still owned

A 2025 loan modification reduced the principal on a married couple's main-home purchase mortgage by $90,000. All of the loan is acquisition debt (well under the $750,000 QPRI limit); they keep the home. Basis before the discharge: $350,000 (purchase $300,000 + $50,000 of improvements).

```
Part I
1e. Discharge of qualified principal residence ............. ☑
2.  Excluded ............................................... $90,000

Part II
10b. Basis of principal residence ........................... $90,000
     (smaller of the $90,000 box 1e amount or the $350,000 basis)

(All other lines blank.)

New basis of home: $350,000 − $90,000 = $260,000
(Carried in the owners' records for a future sale.)
```

Discharges completed after Dec. 31, 2025 don't qualify unless under a written arrangement entered into before Jan. 1, 2026.

---

## Common errors

1. **Using box 1e for a 2026 discharge** — QPRI ended for discharges after 2025 (absent a pre-2026 written arrangement). Test insolvency.
2. **Filing Form 982 when no exclusion applies** — the form is for exclusions, not for reporting income. If reporting income, just put it on Schedule 1 Line 8c.
3. **Entering Line 10b after a foreclosure or short sale** — Line 10b applies only if the filer still owns the home.
4. **Reducing attributes the borrower doesn't have** — Part II should reflect actual attributes; if NOL is 0, write 0.
5. **Skipping the Line 10a computation for a consumer insolvency case** — the instructions require the smallest-of-three amount; it is usually $0 but must be computed.
6. **Skipping Form 982 for §108(a)(1)(B) insolvency** — without it, the IRS sees the 1099-C, no income, and no documented exclusion → likely CP2000.
7. **Filing Form 982 without attaching it to a 1040** — Form 982 is an attachment, not a stand-alone return.
8. **Using Form 982 for a student loan exclusion** — §108(f) exclusions don't go on Form 982.

---

## Sources

- [Form 982 (Rev. March 2018)](https://www.irs.gov/pub/irs-pdf/f982.pdf)
- [Instructions for Form 982 (Rev. December 2021)](https://www.irs.gov/pub/irs-pdf/i982.pdf) — When To File, How To Complete the Form chart, Lines 1b–3, Part II, Lines 7, 10a, 10b
- IRC §108(a)(2) — precedence of exclusions
- IRC §108(b) — attribute reduction order; §108(b)(5) election
- IRC §108(h) — QPRI definitions, $750,000 limit, basis reduction, ordering rule
- IRC §1017 — basis reduction; §1017(b)(2) limit; §1017(b)(3)(E) election
- Treas. Reg. §1.1017-1 — basis-reduction ordering
- [Publication 4681 (2025)](https://www.irs.gov/publications/p4681) — Exclusions, Reduction of Tax Attributes
