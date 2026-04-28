# Form 982 — Line-by-Line Walkthrough

Form 982 ("Reduction of Tax Attributes Due to Discharge of Indebtedness") is the single form that turns a 1099-C from a tax bill into a wash. It has three parts; most consumer filers only touch Part I and write zeros across Part II.

This file covers the form line by line, the attribute-reduction order, and the §108(b)(5) election.

Form revision in scope: 2018-revision form (used for tax years 2018 forward; check the [current PDF](https://www.irs.gov/pub/irs-pdf/f982.pdf) for the tax year being filed).

---

## When to file

File Form 982 with Form 1040 (attach to the return) when the borrower is claiming any §108 exclusion that **requires** the form:

- §108(a)(1)(A) bankruptcy → required
- §108(a)(1)(B) insolvency → required
- §108(a)(1)(C) qualified farm indebtedness → required
- §108(a)(1)(D) qualified real property business indebtedness → required
- §108(a)(1)(E) qualified principal residence indebtedness → required
- §108(f) student loan discharges → not required for permanent §108(f)(1)-(4) sub-rules; conservative practice for §108(f)(5) ARPA broad exclusion (verify per current Form 982 instructions)

If no exclusion is claimed and the canceled amount is reportable as income, **do not** file Form 982. Just report the income on Schedule 1 Line 8c (or Schedule C Line 6 for business debt).

---

## Header

| Field | What goes here |
|-------|----------------|
| Name | Filer's legal name (matches 1040) |
| Identifying number | SSN or ITIN (matches 1040) |

For joint returns, the form is filed under the spouse whose 1099-C and exclusion is being claimed. If both spouses have separate 1099-Cs, file two Forms 982.

---

## Part I — General Information

### Lines 1a-1e — Type of discharge

Check the box that matches the exclusion claimed. Exactly one box is checked per Form 982 (per discharge); if multiple exclusions apply to a single discharge, prioritize the highest-coverage exclusion.

| Line | Box | Use this when |
|------|-----|---------------|
| **1a** | Discharge of indebtedness in a title 11 case | §108(a)(1)(A) bankruptcy — Title 11 discharge order entered |
| **1b** | Discharge of indebtedness to the extent insolvent (not in a title 11 case) | §108(a)(1)(B) insolvency — borrower was insolvent immediately before discharge, not in bankruptcy |
| **1c** | Discharge of qualified farm indebtedness | §108(a)(1)(C) qualified farm indebtedness — farmer-specific |
| **1d** | Discharge of qualified real property business indebtedness | §108(a)(1)(D) qualified real property business indebtedness — non-corporate, depreciable real property used in trade/business |
| **1e** | Discharge of qualified principal residence indebtedness | §108(a)(1)(E) — main home mortgage acquisition debt (verify year-status) |

If multiple discharges occurred in the same year with different exclusions (e.g., one credit card excluded under insolvency, one mortgage excluded under principal residence), the IRS allows a single Form 982 with multiple boxes checked **and** the total on Line 2 — but practice varies. Conservative approach: file two Forms 982, one per exclusion category. Check current Form 982 instructions for the tax year.

### Line 2 — Total amount of discharged indebtedness excluded from gross income

The dollar amount being excluded.

- **Bankruptcy:** Line 2 = canceled amount (no cap from §108(a)(1)(A) itself)
- **Insolvency:** Line 2 = min(canceled amount, insolvency amount). Cannot exceed insolvency.
- **Qualified principal residence:** Line 2 = min(canceled QPRI, $750,000) ($375,000 if MFS).
- **Multiple boxes checked:** Line 2 = sum of all amounts excluded.

This line **must equal or exceed** the sum of basis reductions in Part II Lines 10a-10b and any attribute reductions in Part II Lines 6-12 — see Part II below.

### Line 3 — Election under §108(c)(3)(C) (qualified real property business indebtedness)

Check **Yes** if applying the qualified real property business indebtedness exclusion under §108(a)(1)(D) **and** electing to apply the basis reduction first to the depreciable real property that secured the discharged debt.

For most consumer filers, leave **No**.

---

## Part II — Reduction of Tax Attributes

This is where §108(b) attribute reduction is computed. The borrower reduces tax attributes by the excluded amount, in a fixed order. Each attribute reduction is reported on a specific line.

**Order of reduction** (mandatory under §108(b)(2) unless §108(b)(5) election made):

1. **Net operating loss (NOL)** for the year of discharge → Line 6
2. **General business credit carryovers** → Line 7
3. **Minimum tax credits** → Line 8
4. **Capital loss carryovers** for the year of discharge → Line 9
5. **Basis of property** → Lines 10a / 10b
6. **Passive activity losses and credits** → Line 11
7. **Foreign tax credit carryovers** → Line 12

Each $1 of exclusion reduces $1 of attribute (with a 33⅓¢ ratio for credits — Lines 7, 8, 12).

The total reduced (Lines 6 + 7 ÷ 3 + 8 ÷ 3 + 9 + 10a + 10b + 11 + 12 ÷ 3) **must equal the excluded amount on Line 2**, **subject to the cap**: the borrower can never reduce attributes below zero, and basis reduction is capped at total liabilities minus total asset basis.

### Line 4 — Reduction of credit carryovers under §1374(f)

Special rule for S-corp built-in gains. Almost never applies to consumer 1099-Cs. Leave 0.

### Line 5 — Reduction of credit carryovers under §1502 (consolidated returns)

Consolidated-return rule. Almost never applies. Leave 0.

### Line 6 — Net operating loss

Reduce the NOL for the year of discharge **first**, then NOL carryovers from prior years (in chronological order, oldest first).

For most consumer filers without business losses, NOL = 0. Enter 0 on Line 6.

### Line 7 — General business credits (§38)

Reduce general business credit carryovers (§38 carryovers, including R&D credit, work opportunity credit, etc.). $3 of credit reduces $1 of exclusion.

For most consumer filers, general business credits = 0.

### Line 8 — Minimum tax credits (§53)

Reduce MTC carryovers from §53 (alternative minimum tax credits). $3 of MTC reduces $1 of exclusion.

For most consumer filers, MTC = 0.

### Line 9 — Net capital loss

Reduce current-year net capital loss + capital loss carryovers (§1212). $1 of capital loss reduces $1 of exclusion.

For most consumer filers, capital losses = 0 unless they have a stock-loss history.

### Line 10a — Basis of property (other than principal residence)

Reduce basis of property held by the borrower at the start of the tax year following the discharge. Cap: total liabilities (immediately after discharge) minus total asset basis (immediately after discharge).

§1017 governs the order of basis reduction within a category — Treas. Reg. §1.1017-1 and Pub 4681 Chapter 1 cover the order:

1. Real property used in a trade or business or held for investment (other than principal residence)
2. Personal property used in a trade or business or held for investment
3. Other property used in a trade or business or held for investment
4. Inventory, accounts receivable, notes receivable
5. Other property

For each category, basis is reduced before the next category is touched.

For most consumer filers, basis reduction is irrelevant — they have no business or investment property.

### Line 10b — Basis of principal residence (only for §108(a)(1)(E))

If Line 1e is checked, reduce the basis of the principal residence by the excluded amount on Line 10b. **Mandatory** for §108(a)(1)(E) — see [`qualified-principal-residence.md`](./qualified-principal-residence.md).

This is reported separately because the basis reduction is required regardless of attribute reduction order — it's tied directly to the discharged debt.

### Line 11 — Passive activity losses and credits

Reduce passive activity loss and credit carryovers under §469. $1 PAL reduces $1; $3 passive credit reduces $1.

For most consumer filers, PAL = 0.

### Line 12 — Foreign tax credit carryovers

Reduce FTC carryovers under §27 / §901. $3 of FTC reduces $1 of exclusion.

For most consumer filers, FTC = 0.

### Line 13 — Total

Sum of attribute reductions (in dollar-equivalent terms after the credit ratios). Should equal Line 2.

If the borrower has fewer attributes than the exclusion amount, the excess is **forgiven** — there's nothing more to reduce, and the borrower doesn't owe tax on the excess. This is the case for most consumer filers: the excluded amount exceeds the available attributes (typically zero), so attribute reduction is a non-event.

---

## Part III — Election to Reduce Basis of Depreciable Property First (§108(b)(5))

§108(b)(5) lets the borrower elect to reduce **basis of depreciable property first**, before applying the standard §108(b)(2) attribute order. This is a strategic election: it preserves NOLs, credits, and capital loss carryovers at the cost of immediately reducing depreciable basis.

### Line 14 — Election to apply §108(b)(5)

Check Yes if making the election. Then list the depreciable property and the basis reductions.

**When to elect:**

- Borrower has significant depreciable property and significant NOLs/credits
- Borrower wants to preserve NOLs for future income years
- Trade-off: reduced depreciation deductions in future years vs. preserved NOL for offsetting future income

**When NOT to elect:**

- Borrower has no depreciable property (most consumers)
- Borrower has no NOLs to preserve (most consumers)

For consumer filers, leave Line 14 blank (no election).

---

## Sample completed Form 982 — consumer insolvency case

Jenna's $13,000 credit card cancellation (from the blog example), with Jenna insolvent by $21,000:

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

3.  Election under §108(c)(3)(C) (qualified RP biz) ........ No

Part II — Reduction of Tax Attributes
4.  Reduction under §1374(f) ............................... $0
5.  Reduction under §1502 .................................. $0
6.  NOL .................................................... $0
7.  General business credits ............................... $0
8.  Minimum tax credits .................................... $0
9.  Capital loss carryover ................................. $0
10a. Basis of property (other than principal residence) .... $0
10b. Basis of principal residence ........................... $0
11. Passive activity losses and credits .................... $0
12. Foreign tax credit carryovers .......................... $0
13. Total .................................................. $0

(Note: Total Line 13 < Line 2 because Jenna has no tax attributes
 to reduce. The unreduced excess is permanent — not added back to
 income, not carried forward to future years.)

Part III — §108(b)(5) Election
14. Election to apply §108(b)(5) ........................... No
```

This is the typical consumer pattern: Line 1b checked, Line 2 = excluded amount, Part II all zeros, no election.

---

## Sample completed Form 982 — principal residence case

Borrower had $200,000 of mortgage debt forgiven on principal residence, all qualifying as acquisition indebtedness, basis pre-reduction was $350,000 (purchase $300,000 + $50,000 of capital improvements):

```
Part I
1e. Discharge of qualified principal residence ............. ☑
2.  Excluded ............................................... $200,000

Part II
10b. Basis of principal residence reduction ................. $200,000

(All other lines zero.)

New basis of home: $350,000 − $200,000 = $150,000
(Carried in borrower's records for future sale.)
```

---

## Common errors

1. **Checking multiple boxes 1a-1e on a single Form 982 without splitting Line 2** — IRS prefers each exclusion category have its own Form 982 (or at least clear allocation in Line 2).
2. **Filing Form 982 when no exclusion applies** — the form is for exclusions, not for reporting income. If reporting income, just put it on Schedule 1 Line 8c.
3. **Forgetting Line 10b** for principal residence cases — the basis reduction is mandatory, not optional.
4. **Reducing attributes the borrower doesn't have** — Part II should reflect actual attributes; if NOL is 0, write 0, don't fabricate a reduction.
5. **Sum of Part II ≠ Line 2** — a math error if the borrower has enough attributes; otherwise (consumer case) it's expected — Line 13 < Line 2 when attributes are insufficient.
6. **Skipping Form 982 for §108(a)(1)(B) insolvency** — required by IRC §108(d)(6) and Form 982 instructions; without it, the IRS sees no income reported and no exclusion documented → CP2000.
7. **Filing Form 982 without attaching it to a 1040** — Form 982 is an attachment, not a stand-alone return.

---

## Sources

- [Form 982 (PDF)](https://www.irs.gov/pub/irs-pdf/f982.pdf) — current revision
- [Instructions for Form 982 (PDF)](https://www.irs.gov/pub/irs-pdf/i982.pdf) — line-by-line IRS guidance
- IRC §108(b) — attribute reduction order
- IRC §108(b)(5) — depreciable property basis-first election
- IRC §108(d)(6) — Form 982 filing requirement
- IRC §1017 — basis-reduction ordering rules
- Treas. Reg. §1.1017-1 — basis-reduction rules within a property category
- [Publication 4681](https://www.irs.gov/publications/p4681) — Chapters 1 and 4
