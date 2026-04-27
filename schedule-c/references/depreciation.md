# Depreciation, Section 179, and Bonus Depreciation (Schedule C Line 13)

Three ways to deduct the cost of business assets. The choice matters because it affects current-year tax, future-year tax, and recapture obligations if the asset's use changes.

## The three methods

### 1. De minimis safe harbor (Reg. §1.263(a)-1(f))

If an item costs **$2,500 or less per item**, expense it immediately. No depreciation, no Form 4562, no Section 179. Just put it on the appropriate operating expense line:

- Computer accessories under $2,500 → Line 18 or 27a
- A small printer at $400 → Line 18
- A second monitor at $300 → Line 18
- Hand tools under $2,500 each → Line 22

The $2,500 threshold is per-item, not per-invoice. A user buying ten $1,000 keyboards on one invoice can expense each one under de minimis (total $10,000 expensed). The IRS rule was raised from $500 to $2,500 in 2016 for taxpayers without an Applicable Financial Statement (AFS); it's $5,000 if the user has an AFS, which solo filers almost never do.

**Election required**: technically, the de minimis safe harbor requires an annual election attached to the return. Most tax software handles this automatically. Note it in the user's records.

### 2. Section 179 expense (IRC §179)

For items > $2,500 with useful life > 1 year, Section 179 lets the user deduct up to a per-year limit immediately, instead of depreciating over multiple years.

#### Annual limits (verified)

| Tax year | Section 179 limit | Phase-out begins | Source |
|----------|-------------------|------------------|--------|
| 2024 | $1,160,000 | $2,890,000 | Rev. Proc. 2023-34 |
| 2025 | $1,250,000 | $3,130,000 | Rev. Proc. 2024-40 |
| 2026 | TBD (announced late 2025 by IRS) | TBD | Verify before filing |

The limit is reduced dollar-for-dollar above the phase-out threshold (irrelevant for solo filers in practice). Solo filers almost never hit the limit.

#### What qualifies for §179

- Tangible personal property used >50% for business (computers, equipment, furniture, machinery)
- Off-the-shelf software
- Qualified improvement property (interior improvements to nonresidential buildings, post-2017)
- Certain heavy SUVs (>6,000 lbs GVWR) — limited to $30,500 for 2025; check current year

What does *not* qualify:
- Real property (buildings, land)
- Property used 50% or less for business
- Inventory
- Property bought from a related party

#### The taxable income limit

§179 cannot create or deepen a business loss. The deduction is limited to taxable business income from all sources (Schedule C profit + W-2 wages, etc.). Excess carries forward to next year. Worked example:

```
User has Schedule C net profit before §179 of $40,000 and bought a $50,000 truck.
§179 election: $50,000 (within annual limit and >50% business use)
Limited to: $40,000 (current-year taxable income)
Carryforward: $10,000 (deductible next year if income permits)
```

#### Recapture risk

If business use of a §179'd asset drops to ≤50% at any point during its recovery period, the user must recapture the §179 deduction (add back to income, less depreciation that would have been allowed). This is reported on Form 4797 in the recapture year.

Common recapture trigger: a vehicle expensed at 80% business use that drops to 40% in year two. The IRS will recapture.

### 3. Bonus depreciation + MACRS

The default depreciation regime for assets that aren't expensed under §179.

#### Bonus depreciation rates

Bonus depreciation lets the user deduct a percentage of the asset's cost in year one, beyond §179. The phase-down schedule under TCJA (modified by OBBBA 2025):

| Year placed in service | Bonus rate (TCJA original) | OBBBA 2025 modification |
|------------------------|----------------------------|-------------------------|
| 2024 | 60% | n/a |
| 2025 | 40% | OBBBA: 100% (verify) |
| 2026 | 20% | OBBBA: 100% (verify) |
| 2027 onward | 0% | OBBBA: TBD |

OBBBA 2025 (One Big Beautiful Bill Act) made bonus depreciation permanent at 100% for assets placed in service after Jan 19, 2025. **Always verify the current-year rate at the IRS site or via a CPA before filing**; legislative changes happen mid-year.

#### MACRS recovery periods

After §179 and bonus, the remaining basis is depreciated over MACRS recovery periods. Common solo-relevant categories:

| Asset class | Recovery period | Examples |
|-------------|-----------------|----------|
| 3-year | 3 years | Special tools, race horses |
| 5-year | 5 years | Cars, trucks, computers, copiers, office machines |
| 7-year | 7 years | Office furniture, fixtures, most equipment |
| 15-year | 15 years | Qualified improvement property, fences |
| 27.5-year | 27.5 years | Residential rental real estate (not Schedule C usually) |
| 39-year | 39 years | Nonresidential real estate |

The IRS publishes detailed tables in [Pub 946](https://www.irs.gov/publications/p946). Use the half-year convention for most personal property; mid-quarter convention if >40% of the year's purchases happened in Q4.

## Worked decision: $4,000 laptop in 2025

The user bought a $4,000 laptop on July 1, 2025, used 100% for business.

**Option A — §179**: deduct $4,000 in 2025 (well within $1.25M limit). Done.

**Option B — Bonus depreciation**: at 100% bonus (under OBBBA), deduct $4,000 in 2025. Same outcome.

**Option C — MACRS straight depreciation**: 5-year recovery, half-year convention.
- Year 1 (2025): 20% × $4,000 = $800
- Year 2 (2026): 32% × $4,000 = $1,280
- Year 3 (2027): 19.2% × $4,000 = $768
- Year 4 (2028): 11.52% × $4,000 = $461
- Year 5 (2029): 11.52% × $4,000 = $461
- Year 6 (2030): 5.76% × $4,000 = $230 (half-year convention spreads over 6 calendar years)

For most solo filers, §179 or bonus (immediate full deduction) beats spreading the deduction. Pick MACRS only if:
- Current-year taxable income is too low to absorb the full deduction
- The user expects much higher income in future years and wants larger deductions then
- The asset doesn't qualify for §179 (real estate, related-party purchase)

## Vehicles — special rules

Vehicles are "listed property" (IRC §280F) with stricter rules:

- **Heavy SUVs / pickups** (>6,000 lbs GVWR, less than 14,000 lbs GVWR): §179 capped at $30,500 for 2025 (IRC §179(b)(5)). Bonus depreciation can apply to the rest.
- **Cars and light trucks** (≤6,000 lbs GVWR): annual depreciation caps under IRC §280F (luxury auto limits). For 2025, year 1 cap is around $20,400 with bonus depreciation, $12,400 without. Verify current year.
- **>50% business use required** in the first year and throughout the recovery period.

If the user took §179 or bonus on a vehicle and it drops below 50% business use, recapture applies. This is a real audit risk for solo filers who later use the vehicle more for personal trips.

## Form 4562 mechanics

Whenever the user takes §179, bonus, or MACRS depreciation, attach Form 4562 to the return. The skill should:

1. Compute the deduction using the rules above
2. Note that Form 4562 is required
3. Tell the user the totals to put in each Form 4562 part (Part I §179, Part II bonus, Part III MACRS)

Form 4562 line totals flow to Schedule C Line 13.

## When NOT to take §179 or bonus

Counterintuitive cases where deferring depreciation is smarter:

- **Loss year**: §179 is income-limited; deferring lets the user use depreciation in profitable years
- **NOL carryforward eligibility**: a §179 deduction limited to zero income provides no current benefit and complicates carryforwards
- **Future higher tax bracket**: if the user expects to move from 12% to 24% bracket, $1 of depreciation next year is worth twice as much
- **AMT considerations**: §179 doesn't trigger AMT adjustments; bonus depreciation does (rarely matters for solo filers but verify)

## Summary decision tree

```
Cost ≤ $2,500/item? → Expense as operating cost, no Form 4562 needed
                      (Lines 18, 22, or 27a)

Cost > $2,500/item:
  Useful life ≤ 1 year? → Expense as supplies (Line 22)

  Useful life > 1 year:
    Want immediate full deduction?
      AND current-year taxable income covers it?
        → §179 election on Form 4562 → Line 13

    Need to defer some deduction to future years?
      → MACRS depreciation on Form 4562 → Line 13
      → Optionally combine with bonus depreciation

    Vehicle?
      → Special caps apply; see vehicle.md
```
