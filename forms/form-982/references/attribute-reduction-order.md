# Attribute Reduction Order (§108(b))

When the user excludes canceled debt under bankruptcy, insolvency, or the farm exclusion, IRC §108(b) requires reducing tax attributes — essentially, deferring the tax cost to future years. This reference explains the order, the conversion factors, and the §108(b)(5) election. Line numbers are from Form 982 (Rev. March 2018) and its Instructions (Rev. December 2021); re-check https://www.irs.gov/forms-pubs/about-form-982 for a newer revision.

---

## Why attribute reduction exists

The §108(a) exclusions (bankruptcy, insolvency) provide an immediate exclusion from gross income — but the IRS doesn't want this to be a free deduction. So §108(b) forces the user to reduce tax attributes (NOLs, credits, basis) by the excluded amount, in a defined order.

The economic effect: the user pays no tax now on the excluded amount, but pays "later" through reduced future deductions, credits, and gain on sale. Over time, the tax cost is roughly recovered.

This applies to (§108(b)(1)):
- §108(a)(1)(A) Bankruptcy
- §108(a)(1)(B) Insolvency
- §108(a)(1)(C) Farm — same order, but basis reductions go only to qualified property on lines 11a–11c instead of line 10a (§1017(b)(4); Pub. 4681)

It does NOT apply to:
- §108(a)(1)(D) QRPBI — basis of depreciable real property only, line 4 (§108(c)(1))
- §108(a)(1)(E) Principal residence — basis of the home only, line 10b, and only if the home is still owned (§108(h)(1); i982 Line 10b)

---

## The default ordering (no §108(b)(5) election)

Reduce in this order (§108(b)(2); i982 "Any other debt"; Pub. 4681 "All other tax attributes"):

| Order | Attribute | Form 982 Line | Conversion |
|-------|-----------|---------------|------------|
| 1 | Net operating loss — discharge year, then carryovers to it | 6 | $1 attribute / $1 excluded |
| 2 | General business credit carryover to or from the discharge year | 7 | 33⅓¢ / $1 excluded |
| 3 | Minimum tax credit available at the start of the next year | 8 | 33⅓¢ / $1 excluded |
| 4 | Net capital loss + capital loss carryovers | 9 | $1 / $1 |
| 5 | Basis of property (farm debt: lines 11a–11c) | 10a | $1 / $1 |
| 6 | Passive activity loss / credit carryovers | 12 | $1 loss / $1; 33⅓¢ credit / $1 |
| 7 | Foreign tax credit carryover | 13 | 33⅓¢ / $1 excluded |

Every Part II line is filled with the **excluded dollars** applied to that attribute (form: "Enter amount excluded from gross income"). The 33⅓¢ conversion: $3 of excluded debt = $1 of credit reduction. So a $30,000 exclusion would reduce general business credits by up to $10,000 (after exhausting NOLs), and line 7 would show $30,000.

NOLs and capital losses: reduce the discharge-year loss first, then carryovers in order of the years they arose, earliest first (§108(b)(4)(B)). Credit carryovers: in the order they are taken into account for the discharge year (§108(b)(4)(C)).

---

## The §108(b)(5) election

Form 982 **Line 5** is where the user elects that **basis of depreciable property is reduced FIRST**, before the NOL (line 6) and other attributes. Completing line 5 with an amount is the election; there is no checkbox. (Line 3 is a different election: treating real property held for sale as depreciable property.)

If elected:
- Available only when box 1a, 1b, or 1c is checked (i982 Part II "Basis Reduction")
- Line 5 captures the basis reduction first; it can be all or part of the excluded amount
- Lines 6–13 (excluding 10b) then absorb any remaining excluded amount
- Limited to the aggregate adjusted bases of depreciable property held at the beginning of the next tax year (§108(b)(5)(B)); the §1017(b)(2) liabilities limit does not apply to line 5 (i982 Line 10a)
- Depreciable property means property whose basis reduction reduces depreciation or amortization for the period right after (§1017(b)(3)(B)); real property held for sale counts only if "Yes" is checked on line 3
- Made on a timely filed return (including extensions); revocable only with IRS consent (§108(d)(9)). If the return was timely filed without it, the election can be made on an amended return within 6 months of the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2" (i982 When To File)

**When the §108(b)(5) election is advantageous**:
- User has substantial NOLs they want to preserve for future years
- User has substantial basis in depreciable property they're willing to "spend"
- The user's depreciable property won't be sold soon (basis reduction has long deferral)
- Future depreciation cost (smaller deductions) is OK to absorb

**When NOT to elect**:
- User has little / no depreciable property
- User has small NOL anyway
- User plans to sell depreciable property soon (basis reduction triggers larger taxable gain)
- User would prefer just to lose NOLs than reduce basis

The elected basis reduction is allocated in this order (Pub. 4681 "Election to reduce the basis of depreciable property"; Treas. Reg. §1.1017-1):
1. Depreciable real property used in a trade or business or held for investment that secured the canceled debt
2. Depreciable personal property used in a trade or business or held for investment that secured the canceled debt
3. Other depreciable property used in a trade or business or held for investment
4. Real property held primarily for sale to customers, if elected on line 3

Cannot reduce basis below zero. A later sale at a gain recaptures the reduction as ordinary income (§1017(d); Pub. 4681 "Recapture of basis reductions").

---

## Conversion math: 33⅓¢ per $1

For Lines 7, 8, 12 (credits portion), and 13, the credit is reduced at a 1:3 ratio (§108(b)(3)(B)):

```
$1 of excluded debt reduces $0.33⅓ of credit
$3 of excluded debt reduces $1.00 of credit
$30 of excluded debt reduces $10.00 of credit
```

The statute sets the 33⅓-cent rate; it reflects that a credit offsets tax dollar for dollar while a deduction is worth only the marginal rate.

For Lines 4, 5, 6, 9, 10a, 10b, 11a–11c, and the passive-loss portion of 12: dollar-for-dollar.

---

## Worked example: Insolvency exclusion of $30,000

User: Tom, sole prop with the following attributes:

| Attribute | Available | Form 982 Line |
|-----------|-----------|---------------|
| Discharge-year (2025) NOL | $4,000 | 6 |
| NOL carryover from 2024 | $9,000 | 6 |
| General business credit carryover | $5,000 | 7 |
| Minimum tax credit | $1,500 | 8 |
| Net capital loss + carryover | $2,000 | 9 |
| Basis of office building (depreciable) | $80,000 | 5 (if elected) or 10a |
| Foreign tax credit carryover | $300 | 13 |

Tom is excluding $30,000 under insolvency (box 1b, line 2 = $30,000). The NOL figures are what remains after the 2025 tax is figured (§108(b)(4)(A)).

### Default order (no §108(b)(5) election)

Every $3 of excluded debt reduces $1 of credit, so a credit's absorption capacity is 3 × the credit.

| Step | Form 982 Line | Available attribute | Excluded absorbed (entered on the line) | Attribute after |
|------|---------------|---------------------|------------------------------------------|-----------------|
| 1 | Line 6 (NOL) | $13,000 NOL ($4,000 2025 NOL first, then the $9,000 2024 carryover) | $13,000 | NOL $0 |
| 2 | Line 7 (general business credit) | $5,000 credit × 3 = $15,000 capacity | min($17,000 remaining, $15,000) = $15,000 | Credit $0 (reduced $5,000) |
| 3 | Line 8 (minimum tax credit) | $1,500 × 3 = $4,500 capacity | min($2,000 remaining, $4,500) = $2,000 | Credit $833.33 (reduced $666.67) |

After Step 3: $30,000 excluded fully absorbed. Lines 9, 10a, 12, 13 = $0. Part II total = $30,000 = line 2 (here the attributes were enough; they need not be, i982 Line 2).

Final attributes:
- NOL: $0 (was $13K)
- General business credit: $0 (was $5K)
- Min tax credit: $833 (was $1,500)
- Net capital loss: $2,000 (untouched — didn't need to)
- Basis of office building: $80,000 (untouched)
- FTC: $300 (untouched)

The $30,000 exclusion cost Tom $13,000 of NOL deductions and $5,666.67 of credits ($5,000 + $666.67). Deductions and credits are different currencies: assuming a 24% marginal rate for illustration, the NOL is worth about $3,120 of future tax and the credits about $5,666.67, roughly $8,787 in total.

### With §108(b)(5) election

If Tom enters $30,000 on Line 5:

| Step | Form 982 Line | Available | Absorbed | Result |
|------|---------------|-----------|----------|--------|
| 1 | Line 5 (§108(b)(5) election) | $80,000 basis of depreciable property held on 1/1/2026 | $30,000 | Building basis → $50,000 as of 1/1/2026 |

All $30,000 absorbed by basis reduction. Lines 6–13 = $0; NOLs and credits preserved entirely.

Cost: lower future depreciation on the office building (over remaining recovery period). If 30 years of recovery remain, depreciation per year drops by $1,000 ($30,000 / 30). At the same assumed 24% rate, that's $240/year of higher tax for 30 years = $7,200 nominal, less in present value. If Tom sells the building at a gain, the $30,000 reduction is recaptured as ordinary income (§1017(d)).

Compare (illustration only):
- Default order: about $8,787 of future tax value given up ($3,120 from the NOL, $5,666.67 of credits), felt as soon as Tom would have used them
- §108(b)(5) election: about $7,200 nominal, spread over 30 years, plus recapture risk on a sale

The decision depends on Tom's specifics (how soon he'll use the NOL and credits, whether he'll sell the building, his actual rates and discount rate). The agent should compute both scenarios when both are realistic, show them, and let the user or a CPA decide; this skill doesn't recommend one.

---

## Special rules by situation

### NOL of the discharge year

The NOL OF THE DISCHARGE YEAR (Line 6) is reduced FIRST among NOLs, before NOL carryovers from prior years (§108(b)(4)(B)). All reductions are made after the tax for the discharge year is determined (§108(b)(4)(A)), so the reduction does not change the discharge-year tax; it shrinks what carries forward.

### Reduction order within Line 6

Within Line 6, reduce in this sub-order:
1. Discharge-year NOL
2. NOL carryovers to the discharge year (after any amount used that year), in order of the years they arose, earliest first

### Basis reduction (§1017)

Default basis reduction on Line 10a applies to property held at the beginning of the next tax year (§1017(a)), in this order (Pub. 4681 "Basis"; Treas. Reg. §1.1017-1):
1. Real property used in a trade or business or held for investment (other than real property held for sale to customers) that secured the canceled debt
2. Personal property used in a trade or business or held for investment (other than inventory and accounts and notes receivable) that secured the canceled debt
3. Any other property used in a trade or business or held for investment (other than inventory, accounts and notes receivable, and real property held for sale)
4. Inventory, accounts receivable, notes receivable, and real property held primarily for sale to customers
5. Personal-use property

Within each category, reduce **in proportion to adjusted basis** (Pub. 4681); the user does not pick which property absorbs it. Cannot reduce basis below zero. In title 11 and insolvency cases, the Line 10a reduction can't exceed the aggregate bases of property held immediately after the discharge minus aggregate liabilities immediately after (§1017(b)(2)); in a title 11 case, exempt property is not reduced (§1017(c)(1)). If the excluded amount exceeds the available basis, the excess stays excluded with no further reduction.

For a nonbusiness debt where basis of nondepreciable property is the only attribute, enter on Line 10a the smallest of (a) that basis, (b) line 2, or (c) the §1017(b)(2) excess (i982 "A nonbusiness debt").

### Bankruptcy estates

In a chapter 7 or 11 case to which §1398 applies, the bankruptcy estate, not the individual, is treated as the taxpayer for the attribute reduction (§108(d)(8)). Refer to a CPA (Pub. 908).

---

## When excluded amount > available attributes

If the user excludes $50K but only has $30K of attributes available across all categories:
- All $30K of attributes are reduced to zero
- The remaining $20K of exclusion is "free" — no further attribute reduction required
- The exclusion still applies; the user just has nothing left to reduce

This is a TIME-VALUE benefit: the user got the immediate $50K exclusion at the cost of only $30K of attributes (NPV). Form 982 shows it: line 2 = $50,000 and Part II totals $30,000 (i982 Line 2).

---

## Effective date of reduction

Per §108(b)(4)(A), reductions are made **after the tax for the discharge year is determined**. Basis reductions apply to property held at the beginning of the following tax year (§1017(a)); the minimum tax credit is measured as of the beginning of the following year (§108(b)(2)(C)).

So a 2025 discharge with attribute reduction → the 2025 tax is figured with the full NOL / credits / basis; what carries into 2026 is reduced, and basis reductions take effect 1/1/2026 (or immediately before an earlier disposition for QRPBI property, §1017(b)(3)(F)(iii)).

The agent should make sure the user's 2025 return reflects the FULL attributes (not yet reduced), and the reduction shows up in 2026 records.

---

## Common attribute-reduction mistakes

| Mistake | Fix |
|---------|-----|
| Reducing attributes against the FULL 1099-C amount instead of just the EXCLUDED amount | Use Form 982 Line 2, not 1099-C Box 2 |
| Forgetting to reduce NOLs (skipping Line 6) | §108(b) requires reduction in order; can't skip |
| Reducing credits dollar-for-dollar instead of 33⅓¢/$1 | Conversion factor matters; recompute |
| Entering the credit reduction instead of the excluded dollars on Lines 7, 8, 12, 13 | Enter excluded dollars applied (3 × the credit absorbed) |
| Reducing basis below zero | Cap at zero; remaining exclusion is "free" |
| Ignoring the §1017(b)(2) limit on Line 10a in an insolvency case | Line 10a ≤ bases + money minus liabilities immediately after the discharge |
| Using the §108(b)(5) election when no depreciable property exists | Election produces nothing; default order is fine |
| Failing to make the §108(b)(5) election when it would help | Compute both scenarios; it must be on a timely return and can be revoked only with IRS consent |
| Applying reduction in the wrong year | After the discharge-year tax is figured; basis as of the start of the next year |
| Forgetting to update next year's records | Reduced NOL / basis must be tracked forward |
