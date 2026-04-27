# Vehicle Expenses (Schedule C Line 9 + Part IV)

Two methods for vehicle deductions on Schedule C: standard mileage and actual expenses. Pick one per vehicle per year.

## Standard mileage rate

Multiply business miles × IRS rate. The rate bundles gas, depreciation, repairs, insurance, and maintenance. Annual rates:

| Year | Business rate (per mile) | Source |
|------|--------------------------|--------|
| 2023 | 65.5 cents | Notice 2023-3 |
| 2024 | 67 cents | Notice 2024-8 |
| 2025 | 70 cents | Notice 2025-5 |
| 2026 | TBD (announced ~Dec 2025) | Verify at https://www.irs.gov/tax-professionals/standard-mileage-rates |

In addition to the per-mile rate, the user can also deduct (with standard mileage):
- Parking fees while on business trips (not at the regular workplace)
- Tolls
- Personal property tax on the vehicle (Line 23)
- Business-use % of vehicle loan interest (Line 16b)

What's *inside* the standard mileage rate (don't deduct separately):
- Gas and oil
- Repairs and maintenance
- Insurance
- Registration
- Depreciation (or lease payments)
- Tires

### Eligibility for standard mileage

The user can use standard mileage only if **all** of:

- They own or lease the vehicle (they're not depreciating it under MACRS already)
- It's not used for hire (rideshare drivers can use it; delivery drivers can use it)
- They didn't take §179 or bonus depreciation on the vehicle in any prior year (one-way door)
- They're not operating five or more cars simultaneously (fleet — rare for solo)

Once the user starts a vehicle on actual expenses with MACRS, they're locked into actual for that vehicle's life. So the choice in year one matters.

## Actual expenses method

Total vehicle costs × business-use percentage.

### Eligible costs

- Gas and oil
- Repairs and maintenance
- Insurance
- Registration and title fees
- Depreciation (MACRS or §179 — see [`depreciation.md`](./depreciation.md) for vehicle-specific caps)
- Lease payments (if leased)
- Tires
- Car washes (business portion)
- Garage rent (if separate from home)

### Business-use percentage

```
Business % = business miles / total miles
```

Both numerator and denominator should match Part IV Line 44 totals.

### Example

```
Total miles: 18,000
Business miles: 8,000
Business %: 8,000 / 18,000 = 44.4%

Total vehicle costs:
  Gas               $2,400
  Insurance         $1,800
  Repairs             $850
  Registration        $200
  Depreciation      $3,200  (MACRS year 2 of a 5-year vehicle)
  Total           $8,450

Deduction = $8,450 × 44.4% = $3,752
```

## Standard vs. actual — which is better?

It depends on:

| Factor | Favors standard | Favors actual |
|--------|-----------------|---------------|
| New vehicle | Year 1 only | After year 1 (depreciation falls off) |
| Old vehicle (paid off, low value) | Yes (per-mile rate beats minimal actual costs) | No |
| Heavy expense year (major repair, accident) | No | Yes |
| Long-haul driver (high mileage) | Often yes | Often yes (depends on costs) |
| Rideshare with high gas spend | Maybe | Often actual wins on calculator |
| First-year filer | Standard (preserves option to switch later) | Actual locks in |

**Rule of thumb**: compute both and take the larger. Document the comparison even if the user picks one in tax software — it's defensible if audited.

## Vehicles with §179 or bonus depreciation

If the user expensed a vehicle under §179 or bonus depreciation in a prior year, they cannot switch to standard mileage. They're stuck on actual. This is the most common locked-in scenario.

Also, §179 and bonus on vehicles are subject to the IRC §280F luxury auto caps:

| Tax year | Year 1 cap with bonus | Year 1 cap without bonus | Year 2 | Year 3 | Year 4+ |
|----------|------------------------|---------------------------|--------|--------|---------|
| 2024 | $20,400 | $12,400 | $19,800 | $11,900 | $7,160 |
| 2025 | (verify Rev. Proc. 2024-44 or successor) | | | | |

The cap is reduced for vehicles used less than 100% for business (proportional).

Heavy SUVs (>6,000 lbs GVWR, less than 14,000 lbs) escape the §280F caps but have their own §179 cap of $30,500 for 2025.

## Recordkeeping — the audit Achilles heel

Vehicle deductions are the single most common audit trigger for Schedule C filers. The IRS expects a contemporaneous mileage log with:

- **Date** of trip
- **Destination** (address or business name)
- **Business purpose** (one line: "Met with client X to discuss project Y")
- **Miles** for the trip

Apps that capture this automatically (Jupid, MileIQ, Hurdlr) are far better than a "I'll reconstruct it from my calendar at year-end" approach. Reconstruction logs are accepted but viewed skeptically.

Without a log, courts have allowed approximate deductions in some cases (Cohan rule), but the IRS often disallows the full Line 9 amount in audit. Don't claim Line 9 if there's no log.

## Part IV — Vehicle Information

Required if Line 9 has a vehicle expense.

### Line 43 — Date placed in service

When the vehicle was first used for business — not when bought. If the user bought a car in March and started using it for business in June, the date is in June.

### Line 44 — Miles

Three categories that should sum to total annual miles:

- **44a** — Business miles (from the mileage log)
- **44b** — Commuting miles (home to regular workplace; never deductible)
- **44c** — Other miles (personal: errands, trips, family use)

If the user works from home and meets clients at various locations, all those trips are business miles, not commuting. Commuting only applies if the user has a regular non-home workplace.

### Lines 45-46 — Personal use questions

- **45**: Was the vehicle available for personal use during off-hours? Almost everyone answers Yes. A No is only credible if the user has a separate personal vehicle and never drives the business vehicle off-duty.
- **46**: Is another vehicle available for personal use? Answering Yes here strengthens the case that the business vehicle is genuinely a business vehicle.

### Line 47 — Evidence

- **47a**: Do you have evidence to support the deduction? **Yes** if the user kept logs/receipts.
- **47b**: Is the evidence written? **Yes** if it's a written log (digital counts).

A No on 47b makes the deduction nearly indefensible in audit.

## Multiple vehicles

If the user has more than one business vehicle, each is reported separately (additional Schedule C if needed, or supplemental statement). The standard vs. actual choice is made per vehicle.

## Two-business households

If both spouses run separate Schedule C businesses and share a vehicle, the business mileage must be allocated between them. Each files their own Schedule C with their share. This is rare but worth flagging.

## Switching vehicles mid-year

If the user replaces the business vehicle mid-year, each vehicle gets its own Part IV (or a supplemental schedule). Don't combine.
