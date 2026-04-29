# Attribute Reduction Order (§108(b))

When the user excludes canceled debt under bankruptcy or insolvency, IRC §108(b) requires reducing tax attributes — essentially, deferring the tax cost to future years. This reference explains the order, the conversion factors, and the §108(b)(5) election.

---

## Why attribute reduction exists

The §108(a) exclusions (bankruptcy, insolvency) provide an immediate exclusion from gross income — but the IRS doesn't want this to be a free deduction. So §108(b) forces the user to reduce tax attributes (NOLs, credits, basis) by the excluded amount, in a defined order.

The economic effect: the user pays no tax now on the excluded amount, but pays "later" through reduced future deductions, credits, and gain on sale. Over time, the tax cost is roughly recovered.

This applies to:
- §108(a)(1)(A) Bankruptcy
- §108(a)(1)(B) Insolvency

It does NOT apply to:
- §108(a)(1)(C) Farm — different rules
- §108(a)(1)(D) QRPBI — basis reduction, not full attribute order
- §108(a)(1)(E) Principal residence — basis reduction of the home only

---

## The default ordering (no §108(b)(5) election)

Reduce in this order, dollar-for-dollar (with conversions noted):

| Order | Attribute | Form 982 Line | Conversion | Reason for order |
|-------|-----------|---------------|------------|------------------|
| 1 | Net Operating Loss (NOL) — current year + carryovers | 5 | $1 attribute / $1 excluded | NOLs are most tax-valuable; reduce first |
| 2 | General Business Credit carryover | 6 | 33⅓¢ / $1 excluded | Credits are valuable; reduce next |
| 3 | Minimum Tax Credit | 7 | 33⅓¢ / $1 excluded | AMT credit is also valuable |
| 4 | Net Capital Loss + carryovers | 8 | $1 / $1 | Capital losses; reduce against full amount |
| 5 | Basis of property (default) | 9 | $1 / $1 | Reduce basis last (preserves NOLs etc.) |
| 6 | Passive Activity Loss / Credit | 10 | $1 PAL / $1; 33⅓¢ PA credit / $1 | Passive carryovers reduce |
| 7 | Foreign Tax Credit carryover | 11 | 33⅓¢ / $1 excluded | FTC reduced last |

The 33⅓¢ conversion: $3 of excluded debt = $1 of credit reduction. So a $30,000 exclusion would reduce general business credits by up to $10,000 (after exhausting NOLs).

Within each line, reduce CURRENT-YEAR attribute first, then carryovers (oldest first).

---

## The §108(b)(5) election

Form 982 Line 3 is a checkbox for the user to elect that **basis of depreciable property is reduced FIRST**, before NOLs (Line 5) and other attributes.

If elected:
- Line 4 captures the basis reduction first
- Lines 5-11 then absorb any remaining excluded amount
- The election applies only to depreciable property (real estate used in trade/business, business equipment, etc.)
- The election is **irrevocable**

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

The elected basis reduction is allocated under §1017 within the depreciable property in a specific order (§1017(a)(2)):
1. Real property used in trade/business
2. Personal property used in trade/business
3. Other depreciable property (e.g., property held for income production)

Cannot reduce basis below zero.

---

## Conversion math: 33⅓¢ per $1

For Lines 6, 7, 10 (credits portion), and 11, the reduction is at a 1:3 ratio:

```
$1 of excluded debt reduces $0.33⅓ of credit
$3 of excluded debt reduces $1.00 of credit
$30 of excluded debt reduces $10.00 of credit
```

This is because tax credits are roughly 3x as tax-valuable as deductions (a credit is dollar-for-dollar against tax; a deduction is taxed at marginal rate of ~30%).

For Lines 5, 8, 9, and PAL portion of 10: dollar-for-dollar.

---

## Worked example: Insolvency exclusion of $30,000

User: Tom, sole prop with the following attributes:

| Attribute | Available | Form 982 Line |
|-----------|-----------|---------------|
| Current-year NOL | $4,000 | 5 |
| NOL carryover from 2024 | $9,000 | 5 |
| General business credit carryover | $5,000 | 6 |
| Minimum tax credit | $1,500 | 7 |
| Net capital loss + carryover | $2,000 | 8 |
| Basis of office building (depreciable) | $80,000 | 4 (if elected) or 9 |
| Foreign tax credit carryover | $300 | 11 |

Tom is excluding $30,000 under insolvency.

### Default order (no §108(b)(5) election)

| Step | Apply to | Reduction | Excluded remaining |
|------|----------|-----------|---------------------|
| 1 | Line 5 (NOL) | $13,000 ($4K current + $9K carryover) | $30K − $13K = $17K |
| 2 | Line 6 (gen biz credit) — but converted at 33⅓¢/$1, so $5K credit absorbs $15K of excluded | $5,000 (caps at carryover) | $17K − $15K = $2K |
| 3 | Line 7 (min tax credit) — 33⅓¢/$1, $1,500 absorbs $4,500 (caps at $2K excluded × 3 = $6K, but $2K absorbs $666 credit using inverse) | Wait, let me redo this |

Actually, the logic is: every $3 of excluded reduces $1 of credit. So we need to compute how much excluded can be absorbed by available credits.

Let me redo:

| Step | Form 982 Line | Available attribute | $ Excluded absorbed | Credit reduced |
|------|---------------|---------------------|---------------------|-----------------|
| 1 | Line 5 (NOL) | $13,000 NOL | $13,000 absorbed; NOL → $0 | n/a (dollar-for-dollar) |
| 2 | Line 6 (gen biz credit) | $5,000 credit × 3 = $15,000 absorption capacity | min($17K remaining, $15K capacity) = $15K excluded absorbed; credit → $0 | $5,000 |
| 3 | Line 7 (min tax credit) | $1,500 × 3 = $4,500 absorption capacity | min($2K remaining, $4,500) = $2K absorbed; credit → reduced by $2K/3 = $666.67 | $666.67 (credit becomes $833.33) |

After Step 3: $30K excluded fully absorbed.

Final attributes:
- NOL: $0 (was $13K)
- General business credit: $0 (was $5K)
- Min tax credit: $833 (was $1,500)
- Net capital loss: $2,000 (untouched — didn't need to)
- Basis of office building: $80,000 (untouched)
- FTC: $300 (untouched)

The $30K exclusion cost Tom: $13K NOL + $5K general biz credit + $666 min tax credit = $18,667 of attribute "currency" reduced. That's the deferred tax cost.

### With §108(b)(5) election

If Tom checks Line 3 and elects:

| Step | Form 982 Line | Available | Absorbed | Reduction |
|------|---------------|-----------|----------|-----------|
| 1 | Line 4 (basis under §108(b)(5)) | $80,000 basis | $30,000 | Building basis → $50,000 |

All $30K absorbed by basis reduction. NOLs, credits preserved entirely.

Cost: lower future depreciation on the office building (over remaining life). If building has 30 years of life left, depreciation per year drops by $1,000 ($30K / 30). At marginal rate 24%, that's $240/year of higher tax for 30 years = $7,200 nominal cost.

Compare:
- Default order: $13K NOL + $5K credit + $666 min tax credit lost = ~$18.7K of forgone future tax savings
- §108(b)(5) election: $30K basis reduction = $7,200 nominal future tax cost (less in present value)

For Tom, §108(b)(5) is **better** — preserves NOLs and credits, defers cost over many years.

The decision depends on Tom's specifics (how soon he'll use the NOL, whether he'll sell the building, his discount rate). The agent should compute both scenarios when both are realistic and let the user decide.

---

## Special rules by situation

### NOL of the discharge year

The NOL OF THE DISCHARGE YEAR (Line 5) is reduced FIRST among NOLs, before NOL carryovers from prior years. This affects the user's filing this year — they may have less current-year NOL to apply against this year's other income, increasing this year's tax.

### Reduction order within Line 5

Within Line 5, reduce in this sub-order:
1. Current-year NOL
2. NOL carryovers (oldest first — older carryovers expire eventually)

### Basis reduction (§1017)

Reduction of basis under either §108(b)(5) election or default Line 9 follows §1017's allocation order:
1. Real property used in a trade or business (depreciable)
2. Personal property used in a trade or business (depreciable)
3. Property held for production of income (capital asset)
4. Inventory and accounts receivable
5. Personal-use property

Cannot reduce basis below zero. If excluded amount exceeds total available basis, excess is permanently lost (no further reduction; the excluded amount remains excluded).

Within each category, the user can specify which property to reduce first (good for tax planning).

---

## When excluded amount > available attributes

If the user excludes $50K but only has $30K of attributes available across all categories:
- All $30K of attributes are reduced to zero
- The remaining $20K of exclusion is "free" — no further attribute reduction required
- The exclusion still applies; the user just has nothing left to reduce

This is a TIME-VALUE benefit: the user got the immediate $50K exclusion at the cost of only $30K of attributes (NPV).

---

## Effective date of reduction

Per §108(b)(4), attribute reduction is effective **at the beginning of the tax year FOLLOWING** the year of the discharge.

So a 2025 discharge with attribute reduction → reductions take effect 1/1/2026. The user's 2025 return uses the original NOL / credit / basis for computing 2025 tax; the reduced amounts apply from 2026 forward.

Exception: NOL OF THE DISCHARGE YEAR is reduced first, applies to the year of discharge.

This timing is subtle. The agent should make sure the user's 2025 return reflects the FULL attributes (not yet reduced), and the reduction shows up in 2026 records.

---

## Common attribute-reduction mistakes

| Mistake | Fix |
|---------|-----|
| Reducing attributes against the FULL 1099-C amount instead of just the EXCLUDED amount | Use Form 982 Line 2, not 1099-C Box 2 |
| Forgetting to reduce NOLs (skipping Line 5) | §108(b) requires reduction in order; can't skip |
| Reducing credits dollar-for-dollar instead of 33⅓¢/$1 | Conversion factor matters; recompute |
| Reducing basis below zero | Cap at zero; remaining exclusion is "free" |
| Using the §108(b)(5) election when no depreciable property exists | Election produces nothing; default order is fine |
| Failing to make the §108(b)(5) election when it would help | Compute both scenarios; election is irrevocable |
| Applying reduction in the wrong year | Effective beginning of YEAR FOLLOWING discharge (with current-year NOL exception) |
| Forgetting to update next year's records | Reduced NOL / basis must be tracked forward |
