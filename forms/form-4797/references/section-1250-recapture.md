# §1250 Recapture and Unrecaptured §1250 Gain

§1250 property is depreciable real property — buildings, structural components, and real property improvements with a recovery period over 15 years. The §1250 recapture rules are MORE generous than §1245 because real property has historically been required (or strongly favored) to use straight-line depreciation, which doesn't produce "excess" depreciation to recapture.

For most filers selling rental real estate placed in service after 1986, the **statutory §1250 recapture is $0**, but the depreciation portion of the gain is still taxed at a special rate — the **unrecaptured §1250 gain** rate, capped at 25% federal under IRC §1(h)(1)(E).

---

## What is §1250 property?

IRC §1250(c) defines §1250 property as **any depreciable real property** (real property subject to depreciation) that is NOT §1245 property.

Examples:
- Residential rental buildings (27.5-year MACRS)
- Commercial buildings (39-year MACRS, 31.5-year for property placed in service before 5/13/1993)
- Building structural components: walls, floors, roofs, plumbing, electrical, HVAC central systems
- Land improvements that are inherently permanent (sidewalks, foundations)

NOT §1250 property:
- Land itself (not depreciable, not subject to recapture)
- Personal property (§1245)
- Cost-segregated components reclassified to short MACRS lives (those are §1245)

---

## The §1250 recapture formula (post-1986 MACRS)

For real property placed in service after 1986 under MACRS:

```
Statutory §1250 recapture = excess of accelerated depreciation over straight-line × applicable %

For MACRS straight-line property:
  Accelerated depreciation = Straight-line depreciation
  Excess = $0
  Statutory §1250 recapture = $0
```

Because MACRS requires straight-line for real property post-1986 (residential rental: 27.5-year SL; commercial: 39-year SL), there is no "excess" depreciation, so Line 26g recapture is generally $0.

---

## Unrecaptured §1250 gain (the 25% rate)

Even though §1250 recapture is $0 for most filers, the depreciation portion of the gain is NOT taxed at the regular long-term capital gain rate (0/15/20%). Under IRC §1(h)(1)(E), it is taxed at a maximum federal rate of **25%**.

```
Total §1231 gain on real property:        $X
  ├── Unrecaptured §1250 gain (≤ depreciation taken): taxed at max 25%
  └── Pure capital gain (excess over basis): taxed at 0/15/20%
```

The unrecaptured §1250 gain is **not** ordinary income. It still flows through Form 4797 Part I → Schedule D Line 11 as long-term capital gain. The 25% cap is applied on the **Unrecaptured §1250 Gain Worksheet** in the Schedule D instructions, which feeds Schedule D Line 19 and the tax computation worksheets.

### Worked example

```
Rental property:
  Original cost basis (excluding land):    $200,000
  Accumulated depreciation:                $50,000
  Adjusted basis:                         $150,000
  Sales price (allocated to building):    $250,000
  Realized gain:                          $100,000

§1250 statutory recapture (Line 26g):     $0  (straight-line MACRS)
Unrecaptured §1250 gain:                  $50,000  ← taxed at max 25%
Pure long-term capital gain:              $50,000  ← taxed at 0/15/20%

Total long-term capital gain:            $100,000  → Schedule D Line 11
                                                    Line 19 = $50,000 (worksheet)
```

If the filer is in the 24% ordinary bracket (so 15% LTCG bracket):
- $50,000 × min(25%, 24%) = $50,000 × 24% = $12,000 (capped at filer's ordinary rate, not 25%)
- $50,000 × 15% = $7,500
- Total: $19,500 (vs. $25,000 if all ordinary)

For higher-bracket filers (32%+), the 25% cap on unrecaptured §1250 gain matters more:
- $50,000 × 25% = $12,500 (capped vs. 32% ordinary)
- $50,000 × 15% = $7,500
- Total: $20,000 (vs. $32,000 if all ordinary)

---

## §1250 recapture for pre-1986 property and accelerated methods

If real property was placed in service before 1986 and used ACRS (or earlier method) accelerated depreciation, OR if a filer used a non-straight-line method, then "additional depreciation" exists:

```
Additional depreciation = Accelerated depreciation taken − What straight-line would have been
```

This additional depreciation IS recaptured as ordinary §1250 gain (Line 26g), with applicable percentages depending on the year placed in service:

- **Pre-1970 property** — applicable % declines based on holding period (full recapture only in early years)
- **1970-1975 property** — 100% recapture
- **1976-1980 property** — 100% recapture (residential rental 1976-1980 is 100%)
- **Post-1986 property under MACRS** — statutory recapture = $0 (always SL)

In practice, you only see Line 26g > $0 today for very old rental properties or commercial real estate where accelerated methods were elected (rare).

---

## §291 — Corporate additional 20% recapture

For C-corporations (NOT S-corps, partnerships, or individuals), IRC §291(a)(1) imposes an additional 20% recapture on §1250 property:

```
§291 additional recapture = 20% × (amount that would have been §1245 recapture if the property were §1245 − amount actually recaptured under §1250)
```

This is reported on Line 26f. Most Form 4797 filers (sole props, LLCs, S-corps, partnerships) do NOT have §291 recapture — only true C-corps.

---

## Cost segregation reverses the §1250 advantage

If a filer used **cost segregation** to accelerate depreciation by reclassifying building components into 5-, 7-, or 15-year MACRS lives:

- The reclassified components become §1245 property
- At sale, §1245 (full ordinary recapture) applies to those components
- The pure-real-property residual stays §1250 with the 25% cap

Trade-off:
- Cost seg gives faster deductions during ownership (NPV benefit)
- At sale, cost-seg components produce ordinary recapture instead of 25%-cap unrecaptured §1250 gain

For long-hold properties (>10 years) the time value of accelerated deductions usually beats the recapture penalty. For short-hold properties, the math is much closer.

---

## Land vs building allocation

Land is not depreciable. At purchase, the filer must allocate basis between land (non-depreciable) and building (depreciable). The IRS expects this allocation to match the property tax assessor's land/improvement ratio, or a reasonable substitute.

At sale, the allocation matters because:
- Gain on land = pure §1231 (no depreciation, no recapture)
- Gain on building = §1231 with unrecaptured §1250 gain layer

If the filer allocated 20% to land at purchase, they should allocate roughly 20% of the sale proceeds to land at disposition (unless the relative values have shifted meaningfully).

---

## §1250 traps

1. **Treating cost-segregated components as pure §1250.** If you accelerated $400K of a $2M rental via cost seg, that $400K is §1245 with full ordinary recapture, not 25% cap.

2. **Forgetting the unrecaptured §1250 gain when §1250 recapture is $0.** Filers see Line 26g = $0 and think the whole gain is regular LTCG. Wrong — the depreciation portion is still capped at 25%, not 15%.

3. **Land allocation drift.** Filer allocated 30% to land at purchase but at sale claimed a 50% land allocation to dodge depreciation recapture. The IRS will challenge inconsistent allocations.

4. **Improvements after acquisition.** Filer added a $50K HVAC replacement in year 4 that they capitalized and depreciated. At sale they forgot to add it to basis or include its depreciation in the recapture computation. Both basis and depreciation must reflect ALL capitalized improvements.

5. **Rental that was once a primary residence.** §121 exclusion and §1250 recapture interact awkwardly. The §121 exclusion can shelter the gain ABOVE the depreciation portion, but post-May 6, 1997 depreciation is NOT excludable under §121(d)(6) — it remains as unrecaptured §1250 gain at 25%.
