# Example: Residential Rental Property — 27.5-Year Straight-Line Depreciation

A complete walkthrough of Form 4562 for a landlord depreciating a residential rental building. This is the canonical Schedule E pattern: real property, mid-month convention, straight-line over 27.5 years.

## The filer

- **Name**: Priya Sharma
- **Activity**: Single-family rental (Schedule E activity)
- **Property**: 3-bed, 2-bath single-family home in Austin, TX
- **Tax year**: 2025 (filing in 2026)
- **Other income**: full-time W-2 employee, $140,000 wages

## The property

- **Purchase**: Closed September 1, 2025
- **Total purchase price (cash + mortgage)**: $390,000
- **Closing costs added to basis**: $8,000 (title insurance, attorney, recording fees)
- **Total basis**: $398,000
- **Land allocation**: $98,000 (per county tax appraiser ratio: ~25% land, 75% improvements)
- **Building basis (depreciable)**: $300,000

The $98,000 land basis is **never depreciated** — land has unlimited useful life. The $300,000 building basis is the depreciable amount.

Priya placed the property in service for rental on October 15, 2025 (after a renovation gap September 1 to October 15, when no rental activity occurred and no rent was advertised — she used the time for repairs and finding a tenant).

**Placed in service**: October 15, 2025 — for 27.5-year residential rental, MM convention, this counts as October.

## Why 27.5-year residential rental

IRC §168(c) and Pub. 946 Chapter 3 give recovery periods:
- **Residential rental property**: 27.5 years SL, mid-month convention
- **Nonresidential real property**: 39 years SL, mid-month convention

Residential = building where ≥80% of gross rental income is from dwelling units (per IRC §168(e)(2)(A)). Single-family homes, duplexes, apartment buildings — all residential rental at 27.5 years.

## The Form 4562 entry (Part III Section A)

```
19h Residential rental property:
   (b) Month/year placed in service: 10/2025
   (c) Basis for depreciation: $300,000
   (d) Recovery period: 27.5 yrs
   (e) Convention: MM (mid-month)
   (f) Method: SL (straight-line)
   (g) Depreciation: $2,425
```

### Mid-month convention math

For real property, mid-month convention treats the asset as placed in service on the 15th of the placement month. So October 15 = exactly mid-month, no rounding.

Months remaining in 2025 from mid-October: 2.5 months (mid-October to end of December = 2.5 months).

```
Annual SL depreciation:        $300,000 / 27.5 = $10,909.09
Monthly:                       $10,909.09 / 12 = $909.09
Year 2025 (2.5 months):        2.5 × $909.09 = $2,272.73 ≈ $2,273
```

Or using the IRS Pub. 946 Table A-6 (residential rental, MM convention) for October placement: 0.758% of basis.

```
Year 2025: 0.758% × $300,000 = $2,274
```

(Slight rounding difference from manual calc; use the IRS table value.)

For 2026 onward (full years until disposition or until basis fully recovered):

```
Year 2026: 3.636% × $300,000 = $10,909
Year 2027: 3.636% × $300,000 = $10,909
... (years 3 through 27 all 3.636%, with rounding)
Year 2053: balance to zero out
```

The full table runs years 1-29 because the first and last years are partial; years 2-28 are full at 3.636%.

## No §179, no bonus

- **§179 not allowed** for real property (other than QIP). Residential rental building doesn't qualify.
- **Bonus depreciation not allowed** for residential rental (recovery period >20 years; not QIP). Building doesn't qualify.

So no Part I (§179) and no Part II (bonus) entries for the building. Only Part III Section A (MACRS).

## What Priya could §179 / bonus on

Even though the building isn't eligible, certain items inside are:

- **Refrigerator, stove, dishwasher** — 5-year MACRS, eligible for §179 and bonus (used in a rental — note: §179 does require the activity to be a "trade or business", which historically meant rental qualifying for §179 was murky; post-TCJA, real estate rentals can elect to be a trade or business under §469(c)(7) for active participants). For passive rentals, §179 isn't available, but bonus typically still is.
- **Carpet** — 5-year MACRS, bonus eligible
- **Window AC unit** — 5-year MACRS
- **Furniture in furnished rental** — 5-year MACRS

If Priya bought $4,000 of new appliances when placing the property in service, those go on Form 4562 separately:

```
19b 5-year (appliances):
   (b) 10/2025
   (c) $4,000
   (d) 5 yrs
   (e) HY
   (f) 200DB → SL
   (g) (depending on §179 / bonus elections)

§179: not available (passive rental)
Bonus: 100% if elected (post-Jan 19, 2025 OBBBA)
```

If Priya elects bonus on the appliances: Year 1 deduction = $4,000.

## Form 4562 Part IV summary (building only — no appliances example)

```
21. Listed property (from Line 28):              $0
22. Total (Lines 12+14+15+16+17+19+20+21):       $2,273  (rounded from table)
23. §263A capitalization:                         $0
```

Line 22 = $2,273 → flows to **Schedule E Line 18** (depreciation expense for this rental property).

## Schedule E year 1 (rough)

```
Schedule E rental income (Oct 15 to Dec 31, 2.5 months × $2,800/month): $7,000
Schedule E expenses:
  Mortgage interest (10/15-12/31):              $4,200
  Property tax (allocated for rental period):    $1,400
  Insurance:                                     $300
  Utilities (during rental period, tenant paid most): $0
  Repairs (after placed in service):              $200
  Depreciation (Form 4562 Line 22):              $2,273
  Total:                                         $8,373

Net rental income/loss:                          ($1,373) loss
```

The $1,373 loss is subject to passive activity rules (IRC §469). For Priya:
- She actively participates (selects tenants, sets rent, approves repairs)
- AGI is $140K W-2 + spouse income; if combined AGI is under $100K, full $25,000 special allowance (loss can offset wages); phases out from $100K-$150K AGI
- Above $150K AGI, the $25K allowance is gone and the loss is suspended (carries forward to offset future passive income or until disposition)

The skill should remind Priya that her depreciation deduction is real and reduces taxable income today (if AGI permits) AND increases her gain on sale via depreciation recapture (§1250) at sale.

## Audit defense

If audited:
1. **Land allocation supported by**: county tax appraiser's land/improvement breakdown (commonly used) or independent appraisal. The $98K / $300K split should match the appraiser's ratio.
2. **Placed-in-service date supported by**: rental listing date, first tenant lease, advertising for rental. October 15 is the date Priya advertised the property as available for rent.
3. **Depreciation calculation supported by**: Pub. 946 Table A-6 percentages applied to depreciable basis.
4. **No §179 attempted**: appropriate, since residential rental is passive.

## Long-term implications

After 27.5 years of depreciation totaling $300,000, the building's adjusted basis is $0 (plus $98K land = $98K total adjusted basis). When sold:

- Sale price (e.g., $600,000) − $98,000 adjusted basis = $502,000 gain
- $300,000 of that gain is **§1250 unrecaptured depreciation** (taxed at max 25%)
- $202,000 is long-term capital gain at the user's LTCG rate

Priya should track depreciation taken every year for the eventual sale-of-property calculation. Pub. 544 has the §1250 recapture mechanics; the sale itself is reported on Form 4797 (separate skill).

## §469 election to treat rentals as a trade or business

If Priya owns multiple rental properties and is a real estate professional (>750 hours/year, >50% of personal services in real property trades), she can elect under §469(c)(7) to treat rentals as non-passive. This unlocks:
- §179 on rental personal property
- Loss deductions against W-2 income without the $25K cap

Most solo landlords don't qualify. Don't claim real estate professional status without the time records.

## Sources cited in this draft

- IRS Form 4562, Rev. 2025
- IRS Instructions for Form 4562, Rev. 2025
- IRC §168 (MACRS recovery periods, conventions)
- IRC §168(c) (recovery period for residential rental)
- IRC §168(e)(2)(A) (definition of residential rental property)
- IRC §469 (passive activity rules for rentals)
- IRC §1250 (recapture on sale)
- IRS Pub. 527 (Residential Rental Property)
- IRS Pub. 946 (How to Depreciate Property; Tables A-6, A-7 for residential rental MM convention)
- IRS Pub. 544 (Sales and Other Dispositions of Assets)
