---
name: form-982
description: >
  Use this skill when an individual taxpayer or solo business owner has
  received a Form 1099-C (Cancellation of Debt) and needs to EXCLUDE the
  canceled-debt income from gross income under IRC §108. Triggers on phrases
  like "exclude canceled debt", "Form 982", "insolvency exclusion",
  "bankruptcy debt forgiveness", "qualified principal residence debt",
  "tax attribute reduction", "1099-C insolvency", "short sale tax", "exclude
  forgiven debt from income". Do NOT use when: the user has a 1099-C and no
  exclusion applies (then report it as ordinary income, e.g. Schedule 1
  Line 8c for nonbusiness debt — use the form-1099-c skill); or the user has a
  business debt restructuring under §61 (different mechanism); or a canceled
  student loan covered by a §108(f) exclusion (not claimed on Form 982; for
  discharges after 2025, §108(f)(5) covers only death or total and permanent
  disability).
form: Form 982 (Reduction of Tax Attributes Due to Discharge of Indebtedness)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f982.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i982.pdf
---

# Form 982 — Reduction of Tax Attributes Due to Discharge of Indebtedness

This skill produces an audit-grade Form 982 from a Form 1099-C and the user's facts. It identifies which §108 exclusion applies (bankruptcy, insolvency, qualified principal residence indebtedness, qualified farm indebtedness, qualified real property business indebtedness), computes the excluded amount, applies the §108(b) attribute-reduction ordering rules, and emits a deliverable the user can transcribe to a paper or e-file form.

The math is a rule-driven computation (insolvency worksheet from Pub 4681; basis reduction caps from §108(c)). The judgment is in *which exclusion the user qualifies for* — and that turns on facts the user may not realize matter: the precise fair market value of all assets vs. all liabilities **immediately before** the discharge; the use of the property securing the debt; whether bankruptcy was Chapter 7 vs. 11 vs. 13.

This skill optimizes for the latter — the agent should ask, not guess.

Line map verified against Form 982 (Rev. March 2018) and Instructions (Rev. December 2021), the current revisions as of 2026-10-06, with Pub. 4681 (2025) for the worksheet and examples. Re-check https://www.irs.gov/forms-pubs/about-form-982 before use; a new revision must be re-verified line by line.

**Companion skill**: [`form-1099-c`](../form-1099-c/SKILL.md) handles the receipt and reporting of Form 1099-C as ordinary income (the default case where no exclusion applies). Form 982 is the EXCLUSION path. Many users will have the 1099-C skill produce Schedule 1 Line 8c income; only those with a qualifying §108 exclusion need this skill.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user has received a Form 1099-C and asks if it can be excluded from income
- The user mentions "insolvency", "bankruptcy", "short sale", "principal residence", "farm debt forgiveness", or "qualified real property business debt" in connection with canceled debt
- The user is in or has emerged from a Chapter 7, 11, or 13 bankruptcy and received forgiveness of debt
- The user filed for bankruptcy and is wondering how to report the forgiven amounts on their return
- The user had debt forgiven on their primary residence (mortgage modification, foreclosure, short sale)
- The user is claiming the §108 exclusion and needs to compute the tax-attribute reduction

Do **not** engage this skill when:

- The user received a 1099-C and no §108 exclusion applies (default: report as ordinary income on Schedule 1 Line 8c — use the `form-1099-c` skill)
- The canceled debt is a student loan covered by a §108(f) exclusion. These are not Form 982 exclusions (Pub. 4681 lists them under "Exceptions"). The broad §108(f)(5) exclusion covered discharges after Dec. 31, 2020 and before Jan. 1, 2026; for discharges after Dec. 31, 2025, P.L. 119-21 §70119 limits §108(f)(5) to discharges on account of death or total and permanent disability and requires the taxpayer's SSN on the return. A student loan discharge that no §108(f) rule covers can still be tested for insolvency on Form 982.
- The user is a corporation, partnership, or estate (this skill is scoped to individual / solo filers; entity-level Form 982 has different rules)
- The user has a §61 debt restructuring (e.g., debt-for-equity exchange, debt modification not constituting cancellation) — different mechanism
- The user has cancellation of debt from a related party that's actually a gift under §102 (not income at all; no Form 982 needed)
- The user wants help filing for bankruptcy itself — out of scope; refer to a bankruptcy attorney

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a user who received a 1099-C and is "broke" may or may not be **insolvent** in the §108 technical sense (liabilities > FMV of assets immediately before the discharge, counting all assets including retirement accounts and pension interests, Pub. 4681 Insolvency Worksheet lines 28–29; nonrecourse debt counts as a liability up to the FMV of the property securing it, plus any excess that is forgiven). The agent must work through the Pub. 4681 Insolvency Worksheet to test, not just take the user's word.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers and the **date of the discharge**. The qualified principal residence indebtedness exclusion under §108(a)(1)(E) applies only to debt discharged before Jan. 1, 2026, or discharged under an arrangement entered into and evidenced in writing before Jan. 1, 2026 (extended through 2025 by P.L. 116-260, div. EE, §114; not extended further as of 2026-10-06; Pub. 4681 (2025) What's New). For a 2026 discharge, ask whether a written arrangement (for example a signed modification or short-sale approval) existed before Jan. 1, 2026; if not, box 1e is unavailable.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 982 header.
3. **The Form 1099-C itself.** Required boxes:
   - Box 1: Date of identifiable event (date of cancellation)
   - Box 2: Amount of debt discharged
   - Box 3: Interest, if included in Box 2
   - Box 4: Description of debt
   - Box 5: Check if borrower personally liable
   - Box 6: Identifiable event code (A through H) — tells the agent why the debt was canceled
   - Box 7: FMV of property (if applicable)
4. **Which exclusion the user is claiming**, from the §108(a) menu:
   - (a)(1)(A) Bankruptcy — Title 11 Discharge
   - (a)(1)(B) Insolvency
   - (a)(1)(C) Qualified Farm Indebtedness
   - (a)(1)(D) Qualified Real Property Business Indebtedness (QRPBI)
   - (a)(1)(E) Qualified Principal Residence Indebtedness (discharges before 2026 or under a pre-2026 written arrangement)
   If user is unsure, the agent walks through each test below.
5. **Tax attributes available for reduction** (required for §108(b)):
   - Net operating loss (NOL) for the year + NOL carryovers
   - General business credit carryovers
   - Minimum tax credit carryovers
   - Net capital loss for the year + capital loss carryovers
   - Basis of depreciable property and other assets
   - Passive activity loss carryovers + credits
   - Foreign tax credit carryovers
6. **For insolvency exclusion (a)(1)(B)**: Pub. 4681 Insolvency Worksheet inputs:
   - FMV of ALL assets immediately before the cancellation (including: home, cars, retirement accounts, jewelry, business assets, life insurance cash value, etc.)
   - Total liabilities immediately before the cancellation (including: mortgage, credit cards, student loans, auto loans, business debt, the canceled debt itself, taxes owed, judgments, etc.)
   - For line 10a: adjusted basis (cost, not FMV) of each asset, cash on hand, and total liabilities immediately after the cancellation
7. **For bankruptcy exclusion (a)(1)(A)**: bankruptcy case number, chapter (7, 11, 12, 13), date filed, date of discharge.
8. **For qualified principal residence (a)(1)(E)**: confirmation the property was the user's principal residence; outstanding mortgage balance at time of discharge; FMV of the home.
9. **For qualified real property business (a)(1)(D)**: details of the real property, the debt (date incurred and use of proceeds), outstanding principal and FMV of the property immediately before the discharge, adjusted basis of all depreciable real property, and confirmation that the user makes the election (checking box 1d on a timely filed return).

---

## Workflow

Execute in order.

### Step 1 — Confirm the 1099-C is real and the user wants to exclude

Verify Box 2 (discharged amount) matches what the user is reporting. If the 1099-C is wrong (creditor sent in error, amount disputed), the user should contact the creditor for a corrected 1099-C *before* filing. Do not file Form 982 to "fix" an incorrect 1099-C.

If the user has no §108 exclusion, redirect to the `form-1099-c` skill. Form 982 is exclusion-only.

### Step 2 — Identify the applicable exclusion

Walk through §108(a)(1) in this order:

#### (A) Bankruptcy (Title 11 Discharge)

> Excludes income from discharge of indebtedness if the discharge occurs in a Title 11 case.

Conditions:
- A bankruptcy case was filed under Title 11 of the US Code
- The user was under the court's jurisdiction and the discharge was granted by the court or is under a court-approved plan (§108(d)(2))

If yes: Form 982, **Box 1a** checked. Exclusion = the debt canceled in the title 11 case (no cap), entered on line 2. Boxes 1b–1e don't apply to a title 11 discharge (§108(a)(2)(A)).

#### (B) Insolvency

> Excludes income to the extent the taxpayer was insolvent immediately before the discharge.

Insolvency = liabilities > FMV of assets, **immediately before** the discharge. Use the Pub. 4681 Insolvency Worksheet.

The exclusion is capped at the amount of insolvency. If the user was $20K insolvent and had $30K of debt forgiven, only $20K is excludable; $10K is ordinary income.

If yes: Form 982, **Box 1b** checked. Exclusion = lesser of (Box 2 of 1099-C) or (insolvency amount).

#### (C) Qualified Farm Indebtedness

> Excludes income if the debt was incurred directly in operating a farming business, 50% or more of the user's aggregate gross receipts for the 3 preceding tax years came from farming, and the discharge was by a qualified person (an unrelated lender actively and regularly lending money, or a government agency) (§108(g); i982 Line 1c).

Uncommon. Doesn't apply in a title 11 case or to the extent the user was insolvent. If yes: Box 1c checked.

#### (D) Qualified Real Property Business Indebtedness (QRPBI) — §108(c)

> For taxpayers other than C corporations (§108(a)(1)(D)), excludes income from discharge of debt secured by real property used in a trade or business, in exchange for reducing the basis of depreciable real property.

Conditions:
- Debt secured by real property used in a trade or business (not personal-use, not investment-only)
- Debt incurred or assumed before 1/1/1993, OR incurred or assumed to acquire/construct/reconstruct/substantially improve such property (or a refinancing of such debt, up to the refinanced amount)
- The user elects by checking box 1d on a timely filed return (including extensions); revocable only with IRS consent. A missed election can be made on an amended return filed within 6 months of the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2" (i982 When To File)

Doesn't apply in a title 11 case or to the extent the user was insolvent. If yes: Box 1d checked. Exclusion = lesser of (outstanding principal over the net FMV of the securing property, immediately before discharge) or (adjusted basis of depreciable real property) (§108(c)(2)).

#### (E) Qualified Principal Residence Indebtedness — §108(a)(1)(E)

> Excludes income from discharge of "qualified principal residence indebtedness" — debt incurred to buy, build, or substantially improve the user's principal residence and secured by it.

Availability (§108(a)(1)(E); i982 Line 1e; Pub. 4681 (2025) What's New):
- Only debt discharged before Jan. 1, 2026, or discharged under an arrangement entered into and evidenced in writing before Jan. 1, 2026
- The exclusion began with discharges on or after Jan. 1, 2007 (P.L. 110-142) and was extended several times, last through 2025 by P.L. 116-260, div. EE, §114; no extension as of 2026-10-06
- Discharge after 2025 without a pre-2026 written arrangement: box 1e is unavailable; test insolvency (1b)

Cap: QPRI is acquisition debt up to $750,000 ($375,000 MFS) for discharges after 2020 (§108(h)(2)); before 2021 the figures were $2,000,000 ($1,000,000).

Conditions:
- The home is the filer's main home ("principal residence" has the §121 meaning, §108(h)(5); i982: the home where you ordinarily live most of the time)
- Debt was used to buy, build, or substantially improve that home and is secured by it; a refinance counts only up to the old mortgage principal just before the refinancing
- The discharge is not for services performed for the lender or another factor not directly related to a decline in the home's value or the filer's financial condition (§108(h)(3))
- If only part of the loan is QPRI, the exclusion applies only to the amount discharged in excess of the non-QPRI part (§108(h)(4); i982 example: $1,000,000 loan, $800,000 QPRI, $300,000 discharged → $100,000 excludable)
- Title 11 discharge: use 1a, not 1e. Insolvent filer: may elect 1b instead of 1e

If yes: Box 1e checked. Line 2 = excluded QPRI. If the filer still owns the home after the discharge, line 10b = smaller of that amount or the home's basis (§108(h)(1); i982 Line 10b). If the home was sold or foreclosed in the same transaction, there is no line 10b reduction.

### Step 3 — Compute the excluded amount

Each exclusion has its own cap:

| Exclusion | Cap on excluded amount |
|-----------|------------------------|
| (A) Bankruptcy | None (entire discharged amount) |
| (B) Insolvency | Amount of insolvency |
| (C) Qualified farm | Adjusted tax attributes (credits × 3) + adjusted basis of qualified property held at the start of the next year (§108(g)(3)) |
| (D) QRPBI | Outstanding principal over net FMV of the securing property (less other QRPBI on it); also limited to adjusted basis of depreciable real property (§108(c)(2)) |
| (E) Qualified principal residence | QPRI up to $750K ($375K MFS) of acquisition debt; ordering rule for partly qualified loans (§108(h)(2), (h)(4)) |

If multiple exclusions apply, §108(a)(2) gives an ORDERING RULE:
1. Title 11 first: if the discharge occurs in a title 11 case, only 1a applies (§108(a)(2)(A)).
2. Qualified principal residence before insolvency, unless the user elects 1b instead of 1e (§108(a)(2)(C)).
3. Insolvency before farm and QRPBI: 1c and 1d apply only to the part of the discharge exceeding the insolvency amount (§108(a)(2)(B)).
4. Check every box that applies on one Form 982; line 2 is the total (Pub. 4681 examples with 1b+1c and 1b+1d).

### Step 4 — Compute attribute reduction (§108(b))

For exclusions (A) Bankruptcy, (B) Insolvency, and (C) Farm, the user must reduce tax attributes by the excluded amount (§108(b)(1)), in this ORDER (Form 982 line in brackets):

```
1. Net operating loss (discharge year, then carryovers) — dollar for dollar     [line 6]
2. General business credit carryover — 33⅓ cents per dollar excluded            [line 7]
3. Minimum tax credit — 33⅓ cents per dollar                                    [line 8]
4. Net capital loss + capital loss carryovers — dollar for dollar               [line 9]
5. Basis of property — dollar for dollar (farm debt: lines 11a–11c instead)     [line 10a]
6. Passive activity loss (dollar) + credit (33⅓ cents) carryovers               [line 12]
7. Foreign tax credit carryover — 33⅓ cents per dollar                          [line 13]
```

Each Part II line holds the excluded dollars applied to that attribute (a $1,000 credit carryover absorbs $3,000). Reductions are made after the tax for the discharge year is figured (§108(b)(4)(A)). If the attributes run out, the rest of line 2 stays excluded (i982 Line 2).

If the user makes the **§108(b)(5) election** (1a, 1b, or 1c only), basis of depreciable property is reduced FIRST (before NOLs), up to the adjusted basis of depreciable property held at the start of the next year (§108(b)(5)(B)). It is made by entering the amount on line 5 of a timely filed return and can be revoked only with IRS consent (§108(d)(9); i982 When To File).

For exclusion (D) QRPBI (real property business): reduce basis of depreciable real property used in the business — Form 982 Line 4.

For exclusion (E) qualified principal residence: if the user still owns the home, line 10b = smaller of the QPRI excluded or the home's basis; if the home is gone, there is nothing to reduce (i982 Line 10b).

For a nonbusiness debt where the user has no attribute other than basis of nondepreciable property (the typical consumer case): line 10a = smallest of (a) that basis, (b) line 2, or (c) aggregate bases plus money held immediately after the discharge minus liabilities immediately after (i982 "A nonbusiness debt"; §1017(b)(2)). Compute all three and show them; (c) is often $0 for an insolvent filer, which makes Part II all zeros.

### Step 5 — Run validation checks

See **Validation** below.

### Step 6 — Produce the deliverable

See **Output format** below.

### Step 7 — Hand off downstream

State the next forms / actions:

- **Form 1099-C amount NOT excluded** → ordinary income on Schedule 1 Line 8c (nonbusiness), Schedule C Line 6 (sole proprietorship), Schedule E Line 3 (rental real property), or Schedule F Line 8 (farm) (Pub. 4681)
- **NOL reduced** → keep new NOL schedule for next year
- **Basis reduced** → update fixed-asset records; affects future depreciation and gain on sale
- **Principal residence basis reduced** → keep records for future home sale (affects §121 exclusion calculation)
- **QRPBI (box 1d)** → the election is made by completing Form 982 on a timely filed return; attach the §1017 basis-reduction description the Part II header requires

### Step 8 — File the return (optional)

If filing through the agent, follow [`filing.md`](./filing.md). Form 982 is on the IRS Free File Fillable Forms list of available forms (FFFF closes Oct. 15, 2026); commercial software and paper are the other channels. IRS Direct File was not offered in the 2026 filing season.

---

## Line-by-line guidance

For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — General Information

- **Line 1a–1e** — "Check applicable box(es)": 1a title 11; 1b insolvency (not in a title 11 case); 1c qualified farm; 1d qualified real property business (checking it is the election); 1e qualified principal residence (discharges before 2026 or under a pre-2026 written arrangement). More than one box can apply on one form (Pub. 4681: 1b+1c, 1b+1d).
- **Line 2** — Total amount of discharged indebtedness excluded from gross income. Cannot exceed the cap for each box used. Need not equal the Part II total (i982 Line 2).
- **Line 3** — Yes/No election under §1017(b)(3)(E) to treat all real property held for sale to customers (§1221(a)(1)) as depreciable property. Doesn't apply to QRPBI. This is **not** the §108(b)(5) election.

### Part II — Reduction of Tax Attributes

Each line is the **amount excluded** applied to that attribute (form: "Enter amount excluded from gross income").

| Line | Attribute | When used |
|------|-----------|-----------|
| 4 | QRPBI applied to reduce basis of depreciable real property | Box 1d |
| 5 | §108(b)(5) election: reduce basis of depreciable property first | Optional; boxes 1a–1c; timely return |
| 6 | NOL of the discharge year + NOL carryovers (dollar for dollar) | 1st in default order |
| 7 | General business credit carryover (33⅓¢ per $1) | 2nd |
| 8 | Minimum tax credit (33⅓¢ per $1) | 3rd |
| 9 | Net capital loss + capital loss carryovers (dollar for dollar) | 4th |
| 10a | Basis of nondepreciable and depreciable property not reduced on line 5 (not for farm debt) | 5th; §1017(b)(2) limit in 1a/1b cases |
| 10b | Basis of principal residence | Only if 1e is checked and the home is still owned |
| 11a–11c | Farm debt: depreciable property, farm land, other business/income property | Box 1c, in place of 10a |
| 12 | Passive activity loss (dollar) and credit (33⅓¢) carryovers | 6th |
| 13 | Foreign tax credit carryover (33⅓¢ per $1) | 7th |

There is no line 14 and no total line. Show every line, including zeros.

### Part III — Consent of Corporation to Adjustment of Basis of Its Property Under Section 1082(a)(2)

Corporations only (§1081(b) exclusion; basis adjusted under §1082(a)(2)). Not the §108(b)(5) election. Leave blank for individual / solo filers.

---

## Validation

Run before declaring the form ready. Surface failures.

### Math checks

- [ ] Line 2 ≤ the debt actually canceled (cannot exclude more than was discharged; reconcile to 1099-C Box 2)
- [ ] Line 2 ≤ cap for each box used (insolvency amount; QPRI after the §108(h)(4) ordering rule, up to $750K / $375K MFS; QRPBI §108(c)(2) limits; farm §108(g)(3) limit)
- [ ] Each Part II line ≤ the attribute available (credit lines: excluded dollars ≤ 3 × the credit); total of lines 4–13 (excluding 10b) ≤ Line 2. It need not equal Line 2 (i982 Line 2)
- [ ] Every attribute the user has was reduced in order before moving to the next line (lines 6, 7, 8, 9, 10a, 12, 13 unless line 5 is elected)
- [ ] Insolvency Worksheet: line 15 − line 37 = line 38 (if zero or less, not insolvent)
- [ ] Nonbusiness-debt line 10a = smallest of (a) basis of nondepreciable property, (b) line 2, (c) bases + money minus liabilities immediately after the discharge; all three shown
- [ ] If §108(b)(5) elected: amount on Line 5 (no checkbox), ≤ adjusted basis of depreciable property at the start of the next year
- [ ] If qualified principal residence and the home is still owned: Line 10b = smaller of the 1e amount on line 2 or the home's basis; otherwise Line 10b = $0
- [ ] If QRPBI: Line 4 = Line 2 amount for box 1d, limited to depreciable real property basis

### Sanity checks

Surface a warning, do not block, if:

- [ ] User claims insolvency but didn't include retirement accounts or a pension interest in the Insolvency Worksheet → they are assets (Pub. 4681 worksheet lines 28–29). If the user says an interest can't be cashed out, sold, assigned, or borrowed against, flag for a CPA (Schieber v. Commissioner, T.C. Memo. 2017-32); don't drop it on your own
- [ ] User claims bankruptcy without case number / discharge date → request documentation
- [ ] User claims principal residence exclusion for a vacation home or rental → not qualifying
- [ ] User claims principal residence exclusion for a discharge after 2025 with no written arrangement entered into before Jan. 1, 2026 → not available
- [ ] Mortgage exceeds $750K ($375K MFS) or part of the loan was not used to buy/build/improve the home → apply the §108(h)(4) ordering rule; the non-QPRI part is treated as discharged first
- [ ] User has substantial NOLs but didn't reduce them → §108(b) requires reduction
- [ ] User has a 1099-C from a related party → may be a gift under §102, not income; investigate
- [ ] User has 1099-C for student loan but didn't check §108(f) eligibility → may not need Form 982 at all

### Cross-form checks

- [ ] Form 1099-C Box 2 amount accounted for: excluded portion on Form 982; remainder on the income line for the debt type (Schedule 1 Line 8c, Schedule C Line 6, Schedule E Line 3, Schedule F Line 8)
- [ ] Reduced NOL flows to next year's NOL schedule
- [ ] Reduced basis of depreciable property updates Form 4562 / fixed-asset records for future years
- [ ] Principal residence basis reduction kept in user's records for §121 exclusion at future sale
- [ ] If multiple 1099-Cs, each debt gets its own analysis; all exclusions go on one Form 982 with every applicable box checked and the total on line 2

---

## Output format

The deliverable is a **filled draft** the user can transcribe to Form 982. Every line shown.

```markdown
# Form 982 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <filer name>
Identifying number: <SSN/EIN>

## Part I — General Information

| Line | Description | Value |
|------|-------------|-------|
| 1a | Discharge in a Title 11 case (bankruptcy) | [ ] / [x] |
| 1b | Discharge to extent insolvent (not Title 11) | [ ] / [x] |
| 1c | Discharge of qualified farm indebtedness | [ ] / [x] |
| 1d | Discharge of qualified real property business indebtedness | [ ] / [x] |
| 1e | Discharge of qualified principal residence indebtedness | [ ] / [x] |
| 2 | Total amount of discharged indebtedness excluded from gross income | $X,XXX |
| 3 | Elect to treat §1221(a)(1) real property held for sale as depreciable property? | Yes [ ] / No [ ] |

## Part II — Reduction of Tax Attributes (amount excluded applied to each attribute)

| Line | Attribute | Amount |
|------|-----------|--------|
| 4 | QRPBI applied to reduce basis of depreciable real property (1d) | $X |
| 5 | §108(b)(5) election: applied first to basis of depreciable property | $X |
| 6 | NOL of the discharge year + carryovers | $X |
| 7 | General business credit carryover (credit falls by 1/3 of this) | $X |
| 8 | Minimum tax credit (credit falls by 1/3 of this) | $X |
| 9 | Net capital loss + carryovers | $X |
| 10a | Basis of nondepreciable and depreciable property not reduced on line 5 | $X |
| 10b | Basis of principal residence (only if 1e checked and home still owned) | $X |
| 11a | Farm debt: depreciable property | $X |
| 11b | Farm debt: land used in farming | $X |
| 11c | Farm debt: other business / income property | $X |
| 12 | Passive activity loss and credit carryovers | $X |
| 13 | Foreign tax credit carryover (credit falls by 1/3 of this) | $X |

Check: lines 4–13 (excl. 10b) ≤ Line 2; may be less when attributes run out (i982 Line 2).

### Line 10a computation (nonbusiness debt, only attribute is basis of nondepreciable property)
| (a) Basis of nondepreciable property | $X |
| (b) Nonbusiness debt on line 2 | $X |
| (c) Bases of property + money immediately after − liabilities immediately after (not below $0) | $X |
| Line 10a = smallest | $X |

## Part III — Consent of Corporation to Adjustment of Basis of Its Property Under Section 1082(a)(2)
Blank (corporations only)

## Insolvency Worksheet (Pub. 4681) — only if Line 1b checked

| Item | Value |
|------|-------|
| **Liabilities immediately before discharge** | |
| - Mortgage | $X |
| - Credit card debt | $X |
| - Student loans | $X |
| - Auto loans | $X |
| - Business debt | $X |
| - Tax debt | $X |
| - The canceled debt itself | $X |
| - Other (judgments, medical bills, etc.) | $X |
| **Total liabilities** | $X |
| **FMV of assets immediately before discharge** | |
| - Cash and bank accounts | $X |
| - Real estate (FMV) | $X |
| - Vehicles | $X |
| - Retirement accounts (vested 401(k), IRA, etc.) | $X |
| - Interest in a pension plan | $X |
| - Investments | $X |
| - Personal property (jewelry, electronics, etc.) | $X |
| - Business assets | $X |
| - Life insurance cash value | $X |
| - Other | $X |
| **Total assets** | $X |
| **Insolvency amount = Liabilities − Assets** | $X |
| **Excluded under (B): lesser of canceled debt or insolvency** | $X |

## Required attachments / off-form items
- [ ] Form 1099-C (kept with records)
- [ ] Insolvency Worksheet (if Line 1b)
- [ ] Bankruptcy discharge order (if Line 1a)
- [ ] §1017 basis-reduction description attached (if Line 4, 5, 10a, or 11a–11c is used; Part II header)
- [ ] Basis reduction schedule by property (Lines 4, 5, 10a, 11a–11c)
- [ ] Updated fixed-asset register (post-reduction)
- [ ] Principal residence basis reduction record (if Line 10b)
- [ ] Income line for any amount NOT excluded (Schedule 1 Line 8c / Schedule C Line 6 / Schedule E Line 3 / Schedule F Line 8)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings>
- Exclusion chosen: <(a)(1)(A) / (B) / (C) / (D) / (E)>
- Excluded amount: $X
- Included as ordinary income (form and line): $X
- Tax attributes reduced: <list, including new carryforward amounts>
- Next steps: <handoff items from Step 7>

## Sources cited in this draft
- IRS Form 982 (Rev. March 2018)
- IRS Instructions for Form 982 (Rev. December 2021)
- IRS Pub. 4681 (2025) (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRC §108(a) — exclusions from gross income
- IRC §108(b) — attribute reduction order
- IRC §108(c) — QRPBI limits and basis reduction
- IRC §108(h) — qualified principal residence indebtedness
- IRC §1017 — basis reduction
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 982. The deliverable's value is that every line is computed and traceable.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every Form 982 line in detail
- [`references/exclusion-decision-tree.md`](./references/exclusion-decision-tree.md) — Walk through §108(a) exclusions in order; choose the correct one
- [`references/insolvency-worksheet.md`](./references/insolvency-worksheet.md) — Pub. 4681 Insolvency Worksheet in detail; what counts as an asset / liability
- [`references/attribute-reduction-order.md`](./references/attribute-reduction-order.md) — §108(b) ordering, §108(b)(5) election, dollar-for-dollar vs. 33⅓¢/$1 conversion
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes on Form 982
- [`filing.md`](./filing.md) — Browser-automation playbook

## Examples

End-to-end worked Form 982 drafts.

- [`examples/insolvent-credit-card.md`](./examples/insolvent-credit-card.md) — Insolvency exclusion of $12,880 of a $13,000 credit card cancellation; Insolvency Worksheet; Box 1b; line 10a smallest-of test gives $0
- [`examples/short-sale-residence.md`](./examples/short-sale-residence.md) — 2025 short sale of the main home; $75K excluded under §108(a)(1)(E); no line 10b because the home was sold; 2026 variant without a pre-2026 written arrangement
- [`examples/qualified-real-property-business-debt.md`](./examples/qualified-real-property-business-debt.md) — Sole proprietor with a $200K commercial mortgage workout; $175K excluded under §108(a)(1)(D); Line 4 basis reduction; $25K to Schedule C Line 6

## Sources

Authoritative sources used by this skill. Re-verify each year.

- [Form 982](https://www.irs.gov/pub/irs-pdf/f982.pdf) — the form itself (Rev. March 2018)
- [Instructions for Form 982](https://www.irs.gov/pub/irs-pdf/i982.pdf) — line-by-line IRS guidance (Rev. December 2021)
- [About Form 982](https://www.irs.gov/forms-pubs/about-form-982) — IRS landing page; re-check for a new revision before use
- [Pub. 4681](https://www.irs.gov/pub/irs-pdf/p4681.pdf) — Canceled Debts, Foreclosures, Repossessions, and Abandonments (2025; includes the Insolvency Worksheet)
- [Pub. 523](https://www.irs.gov/pub/irs-pdf/p523.pdf) — Selling Your Home (gain or loss when the home is sold in a short sale or foreclosure)
- IRC §61(a)(11) — discharge of indebtedness as gross income
- IRC §108(a) — exclusions from gross income
- IRC §108(a)(1)(A) — bankruptcy exclusion
- IRC §108(a)(1)(B) — insolvency exclusion
- IRC §108(a)(1)(C) — qualified farm indebtedness
- IRC §108(a)(1)(D) — qualified real property business indebtedness
- IRC §108(a)(1)(E) — qualified principal residence indebtedness (discharges before 2026 or under a written arrangement entered into before Jan. 1, 2026; P.L. 116-260, div. EE, §114)
- IRC §108(a)(2) — coordination of exclusions
- IRC §108(b) — reduction of tax attributes
- IRC §108(b)(5) — election to apply reduction first to basis
- IRC §108(c) — special rules for QRPBI
- IRC §108(d)(3) — definition of insolvency
- IRC §108(d)(9); Treas. Reg. §301.9100-2 — time for the §108(b)(5) and QRPBI elections; 6-month relief on an amended return
- IRC §108(f) — student loan exclusions (not claimed on Form 982); §108(f)(5) as amended by P.L. 119-21 §70119 for discharges after 2025
- IRC §108(h) — qualified principal residence; $750K cap
- IRC §1017 — discharge of indebtedness, basis reduction allocation; §1017(b)(2) limit for title 11 and insolvency cases
- Treas. Reg. §§1.108-2 through 1.108-9 (§1.108-1 is reserved) and §1.1017-1 (basis reduction ordering)
- Carlson v. Commissioner, 116 T.C. 87 (2001) — assets exempt from creditors count as assets in the insolvency test
- Schieber v. Commissioner, T.C. Memo. 2017-32 — pension interest that could not be cashed out, sold, assigned, or borrowed against was not an asset
- Form 1099-C — Cancellation of Debt (received from creditor)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex discharge situations (bankruptcy, multiple 1099-Cs, partial exclusions, basis-reduction elections, partner-level discharge in pass-through entities) warrant a licensed tax professional's review.
