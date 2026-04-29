# Bonus Depreciation (§168(k)) and MACRS

The default depreciation regime for assets that aren't fully expensed under §179. Bonus depreciation is a layer on top of MACRS that lets the taxpayer deduct a percentage of basis in year one before MACRS starts.

---

## Bonus depreciation rates

IRC §168(k) lets a taxpayer deduct a percentage of an asset's adjusted basis in the year placed in service. The rate has changed multiple times under TCJA and OBBBA.

| Year placed in service | TCJA original | OBBBA 2025 modification |
|------------------------|----------------|--------------------------|
| 2017 (Q4 only, post-Sept 27) | 50% / 100% (new vs. used) | n/a |
| 2018–2022 | 100% | n/a |
| 2023 | 80% | n/a |
| 2024 | 60% | n/a |
| 2025 (pre-Jan 19) | 40% | 40% (no OBBBA effect) |
| 2025 (post-Jan 19) | n/a | **100% (OBBBA)** |
| 2026 | 20% (TCJA) | **100% (OBBBA — verify)** |
| 2027+ | 0% (TCJA) | TBD |

**OBBBA 2025** (One Big Beautiful Bill Act) made bonus depreciation permanent at 100% for property placed in service after January 19, 2025. **Verify the current-year rate** at https://www.irs.gov/businesses/small-businesses-self-employed/depreciation-and-amortization-cost-recovery before filing — legislative changes can recur.

---

## What qualifies for bonus

- Tangible personal property with MACRS recovery period ≤20 years
- Off-the-shelf computer software
- Qualified improvement property (QIP) — interior improvements to nonresidential real property after the building was placed in service (post-2017 fix corrected QIP from 39-year to 15-year)
- Certain plants bearing fruits/nuts (specific to farming)
- Used property qualifies (post-TCJA), provided the taxpayer didn't previously use it

What does NOT qualify:
- Real property over 20-year class (residential rental at 27.5 years, nonresidential at 39 years — except QIP)
- Property that must use ADS (e.g., listed property used ≤50% business)
- Property that's been owned by the taxpayer or related party before
- Property used in a tax-exempt trade or business

---

## Bonus mechanics

1. Apply §179 first (if elected) — this reduces the asset's depreciable basis
2. Apply bonus depreciation: rate × (cost − §179 elected)
3. Apply MACRS to the remaining basis: (cost − §179 − bonus) depreciated over the recovery period

Example for a $50,000 5-year asset placed in service in 2025 (post-Jan 19):

```
Cost:                                  $50,000
§179 elected:                          $30,000  ← user choice
Adjusted basis after §179:             $20,000
Bonus rate (100%):                    × 100%
Bonus depreciation:                    $20,000  ← all remaining basis
Adjusted basis after bonus:            $0
MACRS year 1 deduction:                $0
Total year 1 deduction:                $50,000
```

If the user opts out of bonus for the 5-year class, bonus = 0 and MACRS applies to the full post-§179 basis.

---

## Opt-out election

A taxpayer can elect *out* of bonus depreciation for an entire asset class under IRC §168(k)(7). The election:

- Is made on a written statement attached to the timely-filed return
- Identifies the class of property (3-year, 5-year, 7-year, 10-year, 15-year, 20-year, QIP, or any other class)
- Applies to **all** assets in that class placed in service in the tax year — can't pick and choose individual assets
- Is irrevocable without IRS consent (the consent process is via Form 3115)

**Why opt out**: a taxpayer expecting to be in a much higher tax bracket later (or with state-conformity issues) may prefer slower depreciation. Solo filers rarely opt out.

---

## MACRS — Modified Accelerated Cost Recovery System

After §179 and bonus reduce basis, the remaining amount is depreciated over the asset's MACRS recovery period.

### General Depreciation System (GDS) recovery periods

| Class | Period | Method | Common assets |
|-------|--------|--------|---------------|
| 3-year | 3 yrs | 200DB → SL | Special handling tools, race horses, qualified rent-to-own property |
| 5-year | 5 yrs | 200DB → SL | Cars, light trucks, computers, copiers, office machines, appliances in residential rental, R&D property |
| 7-year | 7 yrs | 200DB → SL | Office furniture, fixtures, agricultural machinery, most equipment without a more-specific class |
| 10-year | 10 yrs | 200DB → SL | Vessels, single-purpose agricultural structures, fruit/nut trees |
| 15-year | 15 yrs | 150DB → SL | QIP, fences, roads, certain land improvements |
| 20-year | 20 yrs | 150DB → SL | Farm buildings other than single-purpose, certain utility property |
| 25-year | 25 yrs | SL | Water utility property |
| 27.5-year residential rental | 27.5 yrs | SL | Apartment buildings, single-family rentals (≥80% gross rents from dwelling units) |
| 39-year nonresidential | 39 yrs | SL | Office buildings, warehouses, retail (placed in service after May 12, 1993) |

Methods:
- **200DB (200% declining balance) → SL**: doubles the SL rate; switches to SL when SL would give a larger deduction. For 5-year and 7-year classes.
- **150DB → SL**: 1.5× SL rate; for 15-year and 20-year classes.
- **SL (straight-line)**: equal annual deductions; required for real property and 25-year class.

### Conventions

| Convention | When applies | Effect on year 1 |
|------------|--------------|------------------|
| Half-year (HY) | Personal property, default | Treats all assets as placed mid-year → ½ year of depreciation |
| Mid-quarter (MQ) | When >40% of total annual personal-property purchases happened in Q4 | Treats each asset as placed mid-quarter; later-quarter assets get less first-year depreciation |
| Mid-month (MM) | All real property | Treats asset as placed mid-month of actual placement month |

The MQ trigger is per-tax-year: compute total cost (after §179) of all personal property placed in service. If Q4 placements > 40% of the total, MQ applies to ALL personal property placed that year, not just Q4. This catches solo filers who buy a lot of equipment late in the year.

### Sample MACRS percentages

For 5-year property, half-year convention, 200DB:

| Year | Percentage | Cumulative |
|------|-----------|------------|
| 1 | 20.00% | 20.00% |
| 2 | 32.00% | 52.00% |
| 3 | 19.20% | 71.20% |
| 4 | 11.52% | 82.72% |
| 5 | 11.52% | 94.24% |
| 6 | 5.76% | 100.00% |

For 7-year property, half-year, 200DB:

| Year | Percentage |
|------|-----------|
| 1 | 14.29% |
| 2 | 24.49% |
| 3 | 17.49% |
| 4 | 12.49% |
| 5 | 8.93% |
| 6 | 8.92% |
| 7 | 8.93% |
| 8 | 4.46% |

For 27.5-year residential rental, mid-month, SL: divide by 27.5; first and last years prorated by month placed in service.

For 39-year nonresidential, mid-month, SL: divide by 39; same proration.

Full tables in IRS Pub. 946 Appendix A.

---

## Alternative Depreciation System (ADS)

ADS uses straight-line over a longer recovery period. Required when:

- Listed property used ≤50% for business (cannot use GDS, §179, or bonus)
- Property used predominantly outside the U.S.
- Tax-exempt bond-financed property
- Tax-exempt-use property
- Property imported from a discriminating foreign country (rare)

ADS recovery periods are generally longer than GDS:

| GDS class | ADS class | Difference |
|-----------|-----------|------------|
| 5-year | 5 yrs | Same |
| 7-year | 10 yrs | +3 |
| 15-year | 20 yrs | +5 |
| 27.5-year residential rental | 30 yrs (post-2017) | +2.5 |
| 39-year nonresidential | 40 yrs | +1 |

ADS can be **elected** (irrevocable for that class in that year) or **required**. The election is rare for solo filers.

---

## Bonus on listed property

Listed property used >50% for business qualifies for bonus depreciation, subject to §280F luxury auto caps (for cars/light trucks). The bonus computation appears on Part V Line 25 and is then carried to Part II Line 16.

For heavy SUVs (>6,000 lbs GVWR), bonus is uncapped post-2018 — the §280F luxury auto limits don't apply. This is why heavy SUVs are tax-favored: §179 up to $31,300 (2025), then 100% bonus on the remainder, can fully expense a $80,000 truck in year 1.

---

## Election interactions

The order matters:

1. **§179 election** (per asset, made on Line 6) — reduces basis
2. **Bonus depreciation** (default; class-level opt-out election) — applies to remaining basis
3. **MACRS** — applies to residual basis

If the user opts out of bonus for an asset's class but elected §179, the asset gets §179 then MACRS (no bonus). If the user opts out of bonus AND doesn't elect §179, the asset gets pure MACRS.

---

## Citations

- IRC §168 (MACRS)
- IRC §168(k) (bonus depreciation)
- IRC §168(g) (ADS)
- OBBBA 2025 (One Big Beautiful Bill Act) — bonus depreciation permanence
- TCJA 2017 — original bonus phase-down schedule
- IRS Pub. 946: How to Depreciate Property (Chapters 3–4 for MACRS, conventions, tables)
- Form 4562 Instructions Part II and Part III
