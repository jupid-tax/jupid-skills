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
  exclusion applies (then just report on Schedule 1 Line 8c as ordinary
  income — see the form-1099-c skill); or the user has a business debt
  restructuring under §61 (different mechanism); or canceled student loan
  debt qualifying for the §108(f) exclusion automatically without Form 982
  (verify against current §108(f) scope).
form: Form 982 (Reduction of Tax Attributes Due to Discharge of Indebtedness)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f982.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i982.pdf
---

# Form 982 — Reduction of Tax Attributes Due to Discharge of Indebtedness

This skill produces an audit-grade Form 982 from a Form 1099-C and the user's facts. It identifies which §108 exclusion applies (bankruptcy, insolvency, qualified principal residence indebtedness, qualified farm indebtedness, qualified real property business indebtedness), computes the excluded amount, applies the §108(b) attribute-reduction ordering rules, and emits a deliverable the user can transcribe to a paper or e-file form.

The math is a rule-driven computation (insolvency worksheet from Pub 4681; basis reduction caps from §108(c)). The judgment is in *which exclusion the user qualifies for* — and that turns on facts the user may not realize matter: the precise fair market value of all assets vs. all liabilities **immediately before** the discharge; the use of the property securing the debt; whether bankruptcy was Chapter 7 vs. 11 vs. 13.

This skill optimizes for the latter — the agent should ask, not guess.

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
- The canceled debt is a student loan qualifying for the §108(f) exclusion (most §108(f) discharges do NOT require Form 982, but the rules differ by program — verify against current §108(f) scope; the temporary §108(f)(5) broader exclusion was scheduled to sunset after 2025)
- The user is a corporation, partnership, or estate (this skill is scoped to individual / solo filers; entity-level Form 982 has different rules)
- The user has a §61 debt restructuring (e.g., debt-for-equity exchange, debt modification not constituting cancellation) — different mechanism
- The user has cancellation of debt from a related party that's actually a gift under §102 (not income at all; no Form 982 needed)
- The user wants help filing for bankruptcy itself — out of scope; refer to a bankruptcy attorney

If the user's situation is ambiguous, ask before proceeding. The most common confusion: a user who received a 1099-C and is "broke" may or may not be **insolvent** in the §108 technical sense (which requires liabilities > assets immediately before the discharge, computed using ALL assets including retirement, including non-recourse debt at FMV). The agent must work through Pub 4681 Worksheet 2 to test, not just take the user's word.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The qualified principal residence indebtedness exclusion under §108(a)(1)(E) was extended through tax year 2025 (Consolidated Appropriations Act 2021 + Inflation Reduction Act + later extensions). Verify status for any year 2026+. If extension expires, that exclusion is unavailable.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 982 header.
3. **The Form 1099-C itself.** Required boxes:
   - Box 1: Date of identifiable event (date of cancellation)
   - Box 2: Amount of debt discharged
   - Box 3: Interest, if included in Box 2
   - Box 4: Description of debt
   - Box 5: Check if borrower personally liable
   - Box 6: Identifiable event code (A through I) — tells the agent why the debt was canceled
   - Box 7: FMV of property (if applicable)
4. **Which exclusion the user is claiming**, from the §108(a) menu:
   - (a)(1)(A) Bankruptcy — Title 11 Discharge
   - (a)(1)(B) Insolvency
   - (a)(1)(C) Qualified Farm Indebtedness
   - (a)(1)(D) Qualified Real Property Business Indebtedness (QRPBI)
   - (a)(1)(E) Qualified Principal Residence Indebtedness (verify availability for the tax year)
   If user is unsure, the agent walks through each test below.
5. **Tax attributes available for reduction** (required for §108(b)):
   - Net operating loss (NOL) for the year + NOL carryovers
   - General business credit carryovers
   - Minimum tax credit carryovers
   - Net capital loss for the year + capital loss carryovers
   - Basis of depreciable property and other assets
   - Passive activity loss carryovers + credits
   - Foreign tax credit carryovers
6. **For insolvency exclusion (a)(1)(B)**: Pub 4681 Worksheet 2 inputs:
   - FMV of ALL assets immediately before the cancellation (including: home, cars, retirement accounts, jewelry, business assets, life insurance cash value, etc.)
   - Total liabilities immediately before the cancellation (including: mortgage, credit cards, student loans, auto loans, business debt, the canceled debt itself, taxes owed, judgments, etc.)
7. **For bankruptcy exclusion (a)(1)(A)**: bankruptcy case number, chapter (7, 11, 12, 13), date filed, date of discharge.
8. **For qualified principal residence (a)(1)(E)**: confirmation the property was the user's principal residence; outstanding mortgage balance at time of discharge; FMV of the home.
9. **For qualified real property business (a)(1)(D)**: details of the real property, the debt, election under §108(c).

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
- The discharge was granted by the bankruptcy court
- The discharge occurred during the bankruptcy proceeding

If yes: Form 982, **Box 1a** checked. Exclusion = Box 2 (line 2 of Form 982).

#### (B) Insolvency

> Excludes income to the extent the taxpayer was insolvent immediately before the discharge.

Insolvency = liabilities > FMV of assets, **immediately before** the discharge. Uses Pub 4681 Worksheet 2.

The exclusion is capped at the amount of insolvency. If the user was $20K insolvent and had $30K of debt forgiven, only $20K is excludable; $10K is ordinary income.

If yes: Form 982, **Box 1b** checked. Exclusion = lesser of (Box 2 of 1099-C) or (insolvency amount).

#### (C) Qualified Farm Indebtedness

> Excludes income if the debt was incurred in operating a farm and most of the user's income for the prior 3 years came from farming, and the lender is unrelated.

Uncommon. If yes: Box 1c checked.

#### (D) Qualified Real Property Business Indebtedness (QRPBI) — §108(c)

> For NON-corporate taxpayers, excludes income from discharge of debt secured by real property used in a trade or business, in exchange for reducing the basis of the property.

Conditions:
- Debt secured by real property used in a trade or business (not personal-use, not investment-only)
- Debt incurred or assumed before 1/1/1993, OR incurred or assumed to acquire/construct/substantially improve such property
- Election made under §108(c)

If yes: Box 1d checked. Exclusion = lesser of (excess of debt over property's FMV, before discharge) or (basis of depreciable real property).

#### (E) Qualified Principal Residence Indebtedness — §108(a)(1)(E)

> Excludes income from discharge of "qualified principal residence indebtedness" — debt incurred to buy, build, or substantially improve the user's principal residence and secured by it.

Verify availability:
- TCJA originally limited the exclusion to discharges before 2018
- Extended multiple times by various acts
- Currently in effect through tax year 2025 (verify against most recent extension legislation for any year past 2025)
- If extension lapsed, exclusion not available

Cap: $750K of qualified principal residence debt ($375K MFS) per §108(h)(2). Pre-2018 cap was $2M.

Conditions:
- Property was filer's principal residence
- Debt was acquisition indebtedness (used to buy/build/improve, not refinance for unrelated purposes)
- Discharge occurred while the property was filer's principal residence

If yes: Box 1e checked. Exclusion = qualified principal residence indebtedness portion of discharged debt, capped at $750K. Then reduce basis of the residence by the excluded amount under §108(h)(1).

### Step 3 — Compute the excluded amount

Each exclusion has its own cap:

| Exclusion | Cap on excluded amount |
|-----------|------------------------|
| (A) Bankruptcy | None (entire discharged amount) |
| (B) Insolvency | Amount of insolvency |
| (C) Qualified farm | Aggregate adjusted bases of qualified property + cap on tax attributes |
| (D) QRPBI | Excess of debt over FMV (also limited to basis of depreciable real property) |
| (E) Qualified principal residence | $750K ($375K MFS) of acquisition indebtedness |

If multiple exclusions apply, §108(a)(2) gives an ORDERING RULE:
1. Bankruptcy is checked FIRST — if applicable, use bankruptcy exclusively.
2. If not bankruptcy: insolvency is checked.
3. Qualified farm and QRPBI are alternative paths.
4. Qualified principal residence exclusion has special priority — it's checked BEFORE insolvency unless the user elects insolvency instead (§108(a)(2)(C)).

### Step 4 — Compute attribute reduction (§108(b))

For exclusions (A) Bankruptcy and (B) Insolvency, the user must reduce tax attributes by the excluded amount, in this ORDER:

```
1. Net Operating Losses (current year + carryovers) — dollar-for-dollar
2. General Business Credits — 33⅓ cents per dollar of excluded income
3. Minimum Tax Credit (AMT credit) — 33⅓ cents per dollar
4. Net Capital Loss + capital loss carryovers — dollar-for-dollar
5. Basis of property (including non-depreciable) — dollar-for-dollar (with §1017 election option)
6. Passive Activity Loss + credit carryovers — dollar-for-dollar / 33⅓ cents
7. Foreign Tax Credit carryovers — 33⅓ cents per dollar
```

Lines 5-13 of Form 982 capture the per-attribute reductions.

If the user makes the **§108(b)(5) election**, basis reduction comes FIRST (before NOLs). This can preserve NOLs for future years. The election is irrevocable and made by checking the box on Form 982 Line 5.

For exclusion (D) QRPBI (real property business): reduce basis of depreciable real property used in the business — Form 982 Line 4.

For exclusion (E) qualified principal residence: reduce basis of the principal residence — but only up to the amount of basis. Once basis is zero, no further reduction is needed.

### Step 5 — Run validation checks

See **Validation** below.

### Step 6 — Produce the deliverable

See **Output format** below.

### Step 7 — Hand off downstream

State the next forms / actions:

- **Form 1099-C amount NOT excluded** → Schedule 1 Line 8c as ordinary income
- **NOL reduced** → keep new NOL schedule for next year
- **Basis reduced** → update fixed-asset records; affects future depreciation and gain on sale
- **Principal residence basis reduced** → keep records for future home sale (affects §121 exclusion calculation)
- **§108(c) QRPBI election** → attach election statement and basis-reduction schedule

### Step 8 — File the return (optional)

If filing through the agent, follow [`filing.md`](./filing.md). Form 982 is supported by IRS Free File Fillable Forms and most paid software. IRS Direct File (as of early 2026) does NOT support Form 982; redirect to FFFF, paid software, or paper.

---

## Line-by-line guidance

For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — General Information

- **Line 1a-1e** — Check ONE box (the applicable §108 exclusion). For (E), the discharge year must be a year the exclusion is available.
- **Line 2** — Total amount of discharged indebtedness excluded from gross income. This is the dollar amount being excluded. Cannot exceed cap for the chosen exclusion.
- **Line 3** — Check if applying §108(b)(5) election (basis reduction first, before NOLs). Irrevocable.

### Part II — Reduction of Tax Attributes (for (a)(1)(A) Bankruptcy and (a)(1)(B) Insolvency)

| Line | Attribute reduced | Order |
|------|-------------------|-------|
| 4 | Reduction of basis under §108(b)(5) election (or QRPBI Line 1d) | If §108(b)(5) elected, basis goes here first |
| 5 | NOL for the year + NOL carryovers | First in default order |
| 6 | General business credit carryovers | Second; converted at 33⅓¢/$1 |
| 7 | Minimum tax credit | Third |
| 8 | Net capital loss + carryovers | Fourth |
| 9 | Other basis (non-§108(b)(5)) | Fifth, default |
| 10 | Passive activity loss + credit | Sixth |
| 11 | Foreign tax credit carryovers | Seventh |

The total of Lines 4-11 must equal Line 2 (excluded amount).

### Part III — Consent of Corporation to Adjustment of Basis

Not applicable for individual / solo filers. Skip.

---

## Validation

Run before declaring the form ready. Surface failures.

### Math checks

- [ ] Line 2 ≤ amount on Form 1099-C Box 2 (cannot exclude more than was discharged)
- [ ] Line 2 ≤ cap for the chosen exclusion (e.g., insolvency amount; $750K for principal residence)
- [ ] Sum of Lines 4-11 = Line 2 (every dollar excluded must be applied to attribute reduction, except for QRPBI and principal residence which have alternative paths)
- [ ] Insolvency Worksheet 2: liabilities − assets = insolvency amount (cannot be negative)
- [ ] If §108(b)(5) elected: Line 3 box checked; Line 4 has the basis reduction
- [ ] If qualified principal residence: basis reduction recorded for the home (off-form, in user's records)
- [ ] If QRPBI: basis reduction limited to depreciable real property basis

### Sanity checks

Surface a warning, do not block, if:

- [ ] User claims insolvency but didn't include retirement accounts in Worksheet 2 → retirement IS an asset (Pub 4681)
- [ ] User claims bankruptcy without case number / discharge date → request documentation
- [ ] User claims principal residence exclusion for a vacation home or rental → not qualifying
- [ ] User claims principal residence exclusion in a year where the exclusion has lapsed → not available
- [ ] Discharged debt exceeds $750K under principal residence → only first $750K excludable
- [ ] User has substantial NOLs but didn't reduce them → §108(b) requires reduction
- [ ] User has a 1099-C from a related party → may be a gift under §102, not income; investigate
- [ ] User has 1099-C for student loan but didn't check §108(f) eligibility → may not need Form 982 at all

### Cross-form checks

- [ ] Form 1099-C Box 2 amount accounted for: excluded portion on Form 982; remainder on Schedule 1 Line 8c
- [ ] Reduced NOL flows to next year's NOL schedule
- [ ] Reduced basis of depreciable property updates Form 4562 / fixed-asset records for future years
- [ ] Principal residence basis reduction kept in user's records for §121 exclusion at future sale
- [ ] If multiple 1099-Cs, each gets its own analysis (or aggregated per Pub 4681 if same exclusion)

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
| 3 | Election under §108(b)(5) to apply reduction first to basis | [ ] / [x] |

## Part II — Reduction of Tax Attributes (only for (a)(1)(A) and (a)(1)(B))

| Line | Attribute | Amount reduced |
|------|-----------|----------------|
| 4 | Basis under §108(b)(5) election OR §108(c) QRPBI | $X |
| 5 | NOL (current + carryover) | $X |
| 6 | General business credit | $X |
| 7 | Minimum tax credit | $X |
| 8 | Net capital loss + carryover | $X |
| 9 | Basis of other property (default ordering) | $X |
| 10 | Passive activity loss + credit | $X |
| 11 | Foreign tax credit carryover | $X |
| | **Total Line 4 through 11** | **$X (must equal Line 2)** |

## Part III — Consent of Corporation to Adjustment of Basis
N/A (individual filer)

## Insolvency Worksheet (Pub 4681 Worksheet 2) — only if Line 1b checked

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
- [ ] §108(c) QRPBI election statement (if Line 1d)
- [ ] Basis reduction schedule (Lines 4 / 9)
- [ ] Updated fixed-asset register (post-reduction)
- [ ] Principal residence basis reduction record (if Line 1e)
- [ ] Schedule 1 Line 8c (if any 1099-C amount NOT excluded)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings>
- Exclusion chosen: <(a)(1)(A) / (B) / (C) / (D) / (E)>
- Excluded amount: $X
- Included as ordinary income (Schedule 1 Line 8c): $X
- Tax attributes reduced: <list, including new carryforward amounts>
- Next steps: <handoff items from Step 7>

## Sources cited in this draft
- IRS Form 982 (revision date YYYY)
- IRS Instructions for Form 982 (revision date YYYY)
- IRS Pub 4681 (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRC §108(a) — exclusions from gross income
- IRC §108(b) — attribute reduction order
- IRC §108(c) — basis reduction election (QRPBI)
- IRC §108(h) — qualified principal residence indebtedness
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 982. The deliverable's value is that every line is computed and traceable.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every Form 982 line in detail
- [`references/exclusion-decision-tree.md`](./references/exclusion-decision-tree.md) — Walk through §108(a) exclusions in order; choose the correct one
- [`references/insolvency-worksheet.md`](./references/insolvency-worksheet.md) — Pub 4681 Worksheet 2 in detail; what counts as an asset / liability
- [`references/attribute-reduction-order.md`](./references/attribute-reduction-order.md) — §108(b) ordering, §108(b)(5) election, dollar-for-dollar vs. 33⅓¢/$1 conversion
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes on Form 982
- [`filing.md`](./filing.md) — Browser-automation playbook

## Examples

End-to-end worked Form 982 drafts.

- [`examples/insolvent-credit-card.md`](./examples/insolvent-credit-card.md) — Section A insolvency exclusion of $13K credit card debt; Worksheet 2; Box 1b
- [`examples/short-sale-residence.md`](./examples/short-sale-residence.md) — Short sale of primary residence; $75K excluded under §108(a)(1)(E); basis reduction
- [`examples/qualified-real-property-business-debt.md`](./examples/qualified-real-property-business-debt.md) — Sole proprietor with $200K commercial mortgage workout; §108(a)(1)(D) QRPBI exclusion; basis reduction of depreciable real property; Box 1d

## Sources

Authoritative sources used by this skill. Re-verify each year.

- [Form 982](https://www.irs.gov/pub/irs-pdf/f982.pdf) — the form itself
- [Instructions for Form 982](https://www.irs.gov/pub/irs-pdf/i982.pdf) — line-by-line IRS guidance
- [About Form 982](https://www.irs.gov/forms-pubs/about-form-982) — IRS landing page
- [Pub 4681](https://www.irs.gov/pub/irs-pdf/p4681.pdf) — Canceled Debts, Foreclosures, Repossessions, and Abandonments (the canonical reference, includes Worksheet 2)
- IRC §61(a)(11) — discharge of indebtedness as gross income
- IRC §108(a) — exclusions from gross income
- IRC §108(a)(1)(A) — bankruptcy exclusion
- IRC §108(a)(1)(B) — insolvency exclusion
- IRC §108(a)(1)(C) — qualified farm indebtedness
- IRC §108(a)(1)(D) — qualified real property business indebtedness
- IRC §108(a)(1)(E) — qualified principal residence indebtedness (verify extension status for current tax year)
- IRC §108(b) — reduction of tax attributes
- IRC §108(b)(5) — election to apply reduction first to basis
- IRC §108(c) — special rules for QRPBI
- IRC §108(d)(3) — definition of insolvency
- IRC §108(f) — student loan exclusion
- IRC §108(h) — qualified principal residence; $750K cap
- IRC §1017 — discharge of indebtedness, basis reduction allocation
- Reg. §1.108-1 through §1.108-9
- Form 1099-C — Cancellation of Debt (received from creditor)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex discharge situations (bankruptcy, multiple 1099-Cs, partial exclusions, basis-reduction elections, partner-level discharge in pass-through entities) warrant a licensed tax professional's review.
