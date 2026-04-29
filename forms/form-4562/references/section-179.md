# Section 179 Election — Mechanics and Limits

IRC §179 lets a taxpayer expense the full cost of qualifying business property in the year placed in service, instead of depreciating over multiple years. This file covers the mechanics in depth.

---

## What qualifies for §179

### Qualifying property

- Tangible personal property used >50% for business: computers, equipment, furniture, machinery, vehicles (with caps), tools
- Off-the-shelf software (purchased, not custom-developed)
- Qualified improvement property (QIP): interior improvements to nonresidential real property, post-2017 (IRC §168(e)(6))
- Certain agricultural buildings (single-purpose)
- Storage facilities for petroleum and primary products (limited)

### NOT qualifying

- Real property other than QIP (no §179 on residential rental, office buildings, warehouses, land)
- Property used 50% or less for business
- Inventory (those are deductible as COGS)
- Property bought from a related party (IRC §179(d)(2))
- Property used in a passive trade/business by the taxpayer
- Property used in a tax-exempt trade or business
- Property used outside the U.S. (with limited exceptions)
- Property leased to others (limited; the lessee usually elects, not the lessor)

---

## Annual limits

| Tax year | §179 dollar limit (Line 1) | Phase-out threshold (Line 3) | Heavy SUV §179 cap | Source |
|----------|----------------------------|------------------------------|---------------------|--------|
| 2023 | $1,160,000 | $2,890,000 | $28,900 | Rev. Proc. 2022-38 |
| 2024 | $1,220,000 | $3,050,000 | $30,500 | Rev. Proc. 2023-34 |
| 2025 | $1,250,000 | $3,130,000 | $31,300 | Rev. Proc. 2024-40 |
| 2026 | TBD (announced ~Oct 2025 by IRS) | TBD | TBD | Verify before filing |

**Heavy SUV cap** applies to vehicles >6,000 lbs and ≤14,000 lbs GVWR with a cargo area ≤6 ft (most large SUVs and pickup trucks fall here unless the bed is long enough). The §179 deduction is capped at the heavy-SUV figure even when the taxpayer is well under the dollar limit.

---

## Three limits, applied in order

§179 has **three sequential limits**. Apply in this order:

### Limit 1 — Dollar limit (Line 5)

= Line 1 − max(0, Line 2 − Line 3)

For solo filers, this almost always equals Line 1 because total purchases rarely exceed the phase-out threshold. The phase-out matters for larger businesses.

### Limit 2 — Tentative deduction (Line 9)

= min(Line 5, Line 8)

Where Line 8 = total cost of §179 property elected in Line 6 (column c) + listed property §179 from Line 29.

### Limit 3 — Business income limitation (Line 12)

= min(Line 9 + Line 10 prior carryover, Line 11)

Line 11 — aggregate active business income — is the most-misunderstood limit. It includes:
- Net Schedule C profit (before §179 itself — but after every other expense)
- Net Schedule F profit (farming)
- Net K-1 earned income from active partnerships and S-corps
- W-2 wages (including from unrelated employers)

It does NOT include:
- Net rental income from Schedule E (unless real-estate professional)
- Capital gains from investment activity
- Interest, dividends, royalties from investments
- Pension, retirement income
- Unemployment, social security

So a freelancer with $30,000 of Schedule C profit and a $40,000 W-2 day job has $70,000 of Line 11 income and can §179 up to $70,000.

---

## Carryforward (Line 13)

If Line 9 + Line 10 > Line 11, the excess carries forward. Mechanics:

- Carryover is **per-taxpayer**, aggregated across all activities
- No expiration; carries forward indefinitely
- Subject to the income limit again in each subsequent year
- On next year's Form 4562, enters as Line 10
- The asset's depreciable basis is still reduced by the full elected §179 amount (not just the deductible portion); this is important for later sale/disposition basis calculations

Example:

```
Year 1:
  Asset cost (after bus%):              $50,000
  Elected §179:                         $50,000
  Tentative deduction (Line 9):         $50,000
  Prior carryover (Line 10):            $0
  Business income (Line 11):            $30,000
  §179 deduction (Line 12):             $30,000
  Carryforward (Line 13):               $20,000

Year 2:
  No new §179 election
  Tentative deduction (Line 9):         $0
  Prior carryover (Line 10):            $20,000
  Business income (Line 11):            $80,000
  §179 deduction (Line 12):             $20,000  ← fully recovered
  Carryforward (Line 13):               $0
```

---

## Recapture

§179 recapture under IRC §280F(b)(2) and IRC §179(d)(10) triggers when:

- Business use of a §179'd asset drops to ≤50% in any year before the recovery period ends
- The asset is converted to personal use
- The asset is given away (gifted, abandoned without disposition gain)

The recapture amount = §179 deduction taken − cumulative MACRS depreciation that *would have been* allowed if §179 had not been elected. Reported on **Form 4797 Part IV**, then ordinary income on Form 1040 Line 8 (via Schedule 1).

The recapture year's Form 4562 must show the asset returning to MACRS straight-line over the remaining recovery period.

### Common recapture trigger

Vehicle expensed at 80% business use in year 1. Year 3, business use drops to 40% (life change: new commute, less client travel). Recapture is required immediately — the $X §179 deduction taken in year 1 (less MACRS that would have been allowed in years 1-3) is added back to year-3 ordinary income.

---

## Election mechanics

The §179 election is made on Form 4562 Line 6 by listing the asset and elected cost. There's no separate election form. The election must be on a **timely-filed return** (including extensions). It can be revoked or modified on an amended return within 3 years of the original due date without IRS consent (IRC §179(c)(2)).

---

## Listed-property §179

Listed property (vehicles, computers <100% business) §179 lives in **Part V** (Lines 25–29), not Part I. The total §179 from Part V Line 29 then carries to Part I Line 7 to prevent double-counting.

Heavy SUV (>6,000 lbs GVWR) §179 is capped at the year's heavy-SUV figure ($31,300 for 2025; verify 2026), not the full dollar limit. The remainder of the SUV's basis can take bonus depreciation (which is uncapped for heavy SUVs, post-2018) and then MACRS.

Cars and light trucks (≤6,000 lbs GVWR) are subject to §280F luxury auto caps; §179 amount is then constrained by the luxury cap. See `listed-property.md`.

---

## §179 vs. bonus depreciation — which to elect

Both can fully expense an asset in year one. Differences:

| Factor | §179 | Bonus (§168(k)) |
|--------|------|-----------------|
| Income-limited? | Yes (Line 11) | No |
| Can create a loss? | No | Yes |
| Dollar cap? | Yes ($1.25M for 2025) | No |
| Property limits? | Tangible personal + QIP + off-the-shelf software | Tangible personal + QIP + computer software |
| Heavy SUV cap? | Yes ($31,300) | No (post-2018) |
| Recapture if business use drops? | Yes, §280F(b)(2) | Yes, §280F(b)(2) |
| Election? | Affirmative (Line 6) | Default (must opt out) |
| Reversibility? | Amend within 3 years | Opt-out is irrevocable |

**Default approach for a solo filer**: §179 if income covers it (avoids creating a loss that may have NOL implications), bonus if income is too low, MACRS if neither makes sense.

**For heavy SUVs**: §179 up to the heavy-SUV cap ($31,300 for 2025), then bonus on the remainder.

**For loss situations**: bonus is preferable because it can create a loss; §179 just carries forward.

---

## State conformity

States vary widely on §179:
- Some conform fully (e.g., most states' personal income tax)
- Some have lower §179 limits (e.g., NY for corporations historically)
- Some don't conform at all (e.g., CA on bonus, less so on §179)

The agent should remind the user that the federal §179 deduction may differ from the state's §179 deduction, and the state return may need separate adjustment.

---

## Citations

- IRC §179: https://www.law.cornell.edu/uscode/text/26/179
- IRC §179(b)(1): annual dollar limit
- IRC §179(b)(2): phase-out threshold
- IRC §179(b)(3): business income limitation
- IRC §179(b)(4): married-filing-separately allocation
- IRC §179(b)(5): heavy SUV cap ($25,000 base, indexed for inflation)
- IRC §179(d)(2): related-party exclusion
- IRC §179(d)(10): recapture
- Rev. Proc. 2024-40: 2025 inflation adjustments
- IRS Pub. 946: How to Depreciate Property (Chapter 2 covers §179 in depth)
- Form 4562 Instructions: line-by-line for Part I
