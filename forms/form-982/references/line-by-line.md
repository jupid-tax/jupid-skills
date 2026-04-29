# Form 982 Line-by-Line Reference

Complete lookup for every line on Form 982. Use this when the agent needs to confirm what a line means or where a value goes.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on return | Filer's name as on Form 1040 | Match the 1040 |
| Identifying number | SSN (individuals) or EIN (entities) | |

---

## Part I — General Information

### Line 1 — Type of discharge (check ONE box)

The exclusion under §108(a) is one of five categories. Check exactly ONE box. Multiple discharges in the same year requiring different exclusions need multiple Forms 982.

| Box | Code | Exclusion | When to use |
|-----|------|-----------|-------------|
| 1a | §108(a)(1)(A) | Discharge in a Title 11 (bankruptcy) case | Court-discharged debt in Chapter 7, 11, 12, or 13 |
| 1b | §108(a)(1)(B) | Discharge to extent insolvent (NOT Title 11) | Outside bankruptcy; user is technically insolvent per Pub 4681 Worksheet 2 |
| 1c | §108(a)(1)(C) | Discharge of qualified farm indebtedness | Farm debt; ≥ 50% of last 3 years' income from farming |
| 1d | §108(a)(1)(D) | Discharge of qualified real property business indebtedness | NON-corporate; debt secured by real property used in trade/business; election under §108(c) |
| 1e | §108(a)(1)(E) | Discharge of qualified principal residence indebtedness | Acquisition indebtedness on principal residence; verify exclusion is in effect for the tax year |

**§108(a)(2) ordering rule**: If multiple exclusions could apply:
- Bankruptcy is checked FIRST — if applicable, use bankruptcy exclusively. Other exclusions don't apply to the bankruptcy discharge.
- Insolvency vs. principal residence: principal residence has priority unless the user elects insolvency instead (§108(a)(2)(C)).
- QRPBI is elective — only applies if the user makes the §108(c) election.

### Line 2 — Total amount of discharged indebtedness excluded from gross income

Dollar amount being excluded under the chosen Box 1 selection.

Caps:
- Box 1a (Bankruptcy): no cap; entire discharge can be excluded
- Box 1b (Insolvency): capped at the amount of insolvency (lesser of canceled debt or insolvency)
- Box 1c (Farm): aggregate adjusted bases of qualified property + tax attributes
- Box 1d (QRPBI): excess of debt over FMV of property (also limited to basis of depreciable real property under §108(c)(2))
- Box 1e (Principal residence): $750,000 ($375K MFS) of qualified principal residence indebtedness

Line 2 cannot exceed the Box 2 amount on the underlying Form 1099-C.

### Line 3 — Election under §108(b)(5)

Checkbox. If checked, the user elects to apply the §108(b) attribute reduction FIRST to the basis of depreciable property, before reducing NOLs.

**When to elect §108(b)(5)**:
- User has substantial NOLs they want to preserve
- User has substantial basis in depreciable property they're willing to reduce
- The basis reduction will produce smaller current-year tax cost than losing the NOL carryforward

**When NOT to elect**:
- User has no significant depreciable property
- User has no NOL or small NOL anyway
- User would prefer to give up the NOL than reduce basis (e.g., basis reduction triggers depreciation recapture concerns at future sale)

The election is **irrevocable**. Once filed, it cannot be undone.

The §108(b)(5) election applies only to bankruptcy and insolvency exclusions. For QRPBI under §108(c), basis reduction is automatic (not elective).

---

## Part II — Reduction of Tax Attributes

Required only if Box 1a (bankruptcy) or Box 1b (insolvency) is checked. The total of Lines 4-11 must equal Line 2.

For Box 1c, 1d, or 1e, Part II works differently:
- Box 1c (farm): see special rules in §108(g) and instructions
- Box 1d (QRPBI): basis reduction goes to Line 4 only
- Box 1e (principal residence): basis reduction is to the residence itself (not on Part II); not on Form 982 directly

### Line 4 — Reduction of basis under §108(b)(5) election OR §108(c) QRPBI

Two uses:
1. If Line 3 (§108(b)(5) election) is checked: amount of basis reduction applied first, before NOLs.
2. If Box 1d (QRPBI): amount of basis reduction in the depreciable real property used in the business.

Cannot exceed the basis of the depreciable property (or principal residence under §108(c)).

### Line 5 — Net operating loss

Reduce CURRENT-YEAR NOL first, then NOL carryovers from prior years (oldest first).

Dollar-for-dollar: $1 of excluded debt → $1 of NOL reduction.

If user has no NOL, Line 5 = $0.

### Line 6 — General business credit carryover

Reduce general business credit (Form 3800) carryovers to/from this year.

**Conversion**: 33⅓ cents per dollar of excluded debt. So $3 of excluded debt = $1 of credit reduction.

If user has no general business credit carryover, Line 6 = $0.

### Line 7 — Minimum tax credit

Reduce minimum tax credit (Form 8801) — i.e., AMT credit from prior years.

**Conversion**: 33⅓ cents per dollar.

If user has no AMT credit, Line 7 = $0.

### Line 8 — Net capital loss + capital loss carryovers

Reduce CURRENT-YEAR net capital loss first, then carryovers (oldest first).

Dollar-for-dollar.

If user has no net capital loss or carryover, Line 8 = $0.

### Line 9 — Other basis (default ordering)

Reduce basis of property — but only if §108(b)(5) election was NOT made.

If §108(b)(5) was elected (Line 4 has the basis reduction), Line 9 may also have additional basis reduction if basis exceeds Line 4 cap and other attributes exist.

Reduction order within Line 9 (per §1017):
1. Basis of real property used in trade/business (depreciable)
2. Basis of personal property used in trade/business (depreciable)
3. Basis of property held for investment (capital assets)
4. Basis of inventory and accounts receivable
5. Basis of personal-use property

Cannot reduce basis below zero.

### Line 10 — Passive activity loss + credit

Reduce passive activity loss (Form 8582) carryovers + passive activity credit carryovers.

PAL: dollar-for-dollar.
PA credits: 33⅓ cents per dollar.

If user has no passive activity carryovers, Line 10 = $0.

### Line 11 — Foreign tax credit

Reduce foreign tax credit (Form 1116) carryovers.

**Conversion**: 33⅓ cents per dollar.

If user has no FTC carryover, Line 11 = $0.

### Reconciliation (the math)

```
Sum(Lines 4-11) = Line 2 (excluded amount)
```

If the user's available attributes don't sum to the full excluded amount (i.e., they have less attributes than excluded debt), the EXCESS is permanently lost — there's no further reduction beyond what's available. The exclusion still applies; the only "cost" was reducing all available attributes.

This is the "tax-attribute reduction" in action — the user gets the exclusion now, and pays it back over time through reduced future deductions / credits / basis.

---

## Part III — Consent of Corporation to Adjustment of Basis

Not applicable for individual filers. For corporate filings only.

---

## Worksheets and supporting documentation

These are NOT lines on Form 982 but are required by the IRS to support the filing.

### Pub 4681 Worksheet 2 — Insolvency Worksheet

Required if Box 1b (insolvency) is checked. Computes the insolvency amount (liabilities minus assets immediately before discharge). The Worksheet 2 itself is NOT filed with Form 982 but must be retained with the user's records.

See [`insolvency-worksheet.md`](./insolvency-worksheet.md).

### §108(b)(5) election statement

If Line 3 is checked, attach a statement identifying:
- The election under IRC §108(b)(5)
- The amount of basis reduction
- The depreciable property to which the reduction applies

### §108(c) QRPBI election statement

If Box 1d is checked, attach a statement identifying:
- The election under §108(c)
- The qualified real property business indebtedness
- The depreciable real property
- The amount of basis reduction

### Bankruptcy discharge order

If Box 1a is checked, retain a copy of the bankruptcy court's discharge order. NOT filed with Form 982 but must be available on IRS request.

### Principal residence acquisition documentation

If Box 1e is checked, retain mortgage statements, closing documents, and any refinance documents establishing the debt was qualified principal residence indebtedness (acquisition / improvement debt, secured by the residence).

---

## Reconciling with Form 1099-C

The Form 1099-C the user received is the trigger for Form 982. The reconciliation:

```
1099-C Box 2 (debt discharged)        $X,XXX
- Form 982 Line 2 (excluded amount)   $X,XXX
= Schedule 1 Line 8c (taxable)        $X,XXX
```

If the entire 1099-C is excluded → Schedule 1 Line 8c = $0
If part is excluded → Schedule 1 Line 8c = remainder

The agent must ensure the user reports the non-excluded portion on Schedule 1. Excluding the entire amount when only part qualifies is a common error.

---

## Common edge cases

### Multiple 1099-Cs in the same year

Each 1099-C may need different treatment:
- One under bankruptcy
- Another under insolvency
- Another not excludable

If the same exclusion applies to multiple 1099-Cs, aggregate them on a single Form 982 (one Box 1 selection, summed Line 2). If different exclusions apply, file multiple Forms 982.

### 1099-C from a related party

If the canceled debt was owed to a related party (family member, controlled entity), it might not be a real cancellation — could be a gift under §102 (not income) or a constructive distribution (different reporting). Investigate before excluding.

### Recourse vs. non-recourse debt

For non-recourse debt secured by property, the cancellation rules differ. The "debt forgiveness" portion (debt > FMV of property) is income; the "FMV of property" portion is a sale (capital gain or loss). See Pub 4681 examples 6-9 for the math.

### Discharge during a bankruptcy proceeding

Box 1a applies if the discharge occurred while the user was IN a Title 11 case. If a creditor canceled debt outside the bankruptcy (before filing or after dismissal), Box 1a doesn't apply — try insolvency instead.

### Pass-through entity discharges (partnerships, S-corps)

For pass-through entity discharges, the §108 exclusions apply at the partner / shareholder level, not the entity level. Each partner / shareholder makes their own §108(a) determination on their share of the discharge. Form 982 is filed by the individual, not the entity.

This skill is scoped to individual / solo filers; pass-through entity coordination is out of scope. Refer to a CPA.

### Cancellation of student loan debt

§108(f) provides exclusions for certain student loan discharges (death, disability, public service forgiveness, certain school closures). Many §108(f) discharges do NOT require Form 982 — the exclusion is automatic.

The temporary §108(f)(5) broad exclusion (American Rescue Plan, 2021-2025) covered most student loan discharges regardless of program. Verify whether this is still in effect for the user's tax year.
