# Form 2290 — Weight Categories Reference

The IRS uses 23 active weight categories (A through V) plus W for suspended vehicles. Each category corresponds to a 1,000-lb increment of taxable gross weight.

This reference is the input for tax computation on Line 2. For the actual tax amounts (annual, partial-period, logging), see [`tax-table.md`](./tax-table.md).

---

## What Is "Taxable Gross Weight"?

**Taxable gross weight** is not curb weight or empty weight. It's the **total of:**

1. The actual unloaded weight of the vehicle, fully equipped for service
2. The actual unloaded weight of any trailers or semi-trailers, fully equipped for service, customarily used in combination with the vehicle
3. The weight of the maximum load customarily carried on the vehicle and on any trailers or semi-trailers customarily used in combination

This is why a 35,000-lb truck-tractor that pulls 45,000-lb loaded trailers has a taxable gross weight of 80,000 lbs (Category V) — the trailer and load count.

For trucks operated under multiple weight ratings (e.g., loaded for some hauls, empty for others), use the **highest customary** combination.

---

## Category Table

| Category | Taxable Gross Weight (lbs) |
|----------|---------------------------|
| A | 55,000 |
| B | 55,001 — 56,000 |
| C | 56,001 — 57,000 |
| D | 57,001 — 58,000 |
| E | 58,001 — 59,000 |
| F | 59,001 — 60,000 |
| G | 60,001 — 61,000 |
| H | 61,001 — 62,000 |
| I | 62,001 — 63,000 |
| J | 63,001 — 64,000 |
| K | 64,001 — 65,000 |
| L | 65,001 — 66,000 |
| M | 66,001 — 67,000 |
| N | 67,001 — 68,000 |
| O | 68,001 — 69,000 |
| P | 69,001 — 70,000 |
| Q | 70,001 — 71,000 |
| R | 71,001 — 72,000 |
| S | 72,001 — 73,000 |
| T | 73,001 — 74,000 |
| U | 74,001 — 75,000 |
| V | over 75,000 |
| **W** | **Suspended** (5,000 miles or less, or 7,500 if agricultural) |

Note: Category A is exactly 55,000 lbs; Category B is 55,001-56,000. The IRS table on Form 2290 uses these specific 1,000-lb bands.

---

## Annual Tax Formula

```
Tax (standard) = $100 base + ($22 × thousands of lbs over 55,000)
                 capped at $550 for vehicles over 75,000 lbs

Tax (logging)  = Tax (standard) × 0.75
```

| Category | Std Annual | Logging Annual |
|----------|-----------|----------------|
| A | $100.00 | $75.00 |
| B | $122.00 | $91.50 |
| C | $144.00 | $108.00 |
| D | $166.00 | $124.50 |
| E | $188.00 | $141.00 |
| F | $210.00 | $157.50 |
| G | $232.00 | $174.00 |
| H | $254.00 | $190.50 |
| I | $276.00 | $207.00 |
| J | $298.00 | $223.50 |
| K | $320.00 | $240.00 |
| L | $342.00 | $256.50 |
| M | $364.00 | $273.00 |
| N | $386.00 | $289.50 |
| O | $408.00 | $306.00 |
| P | $430.00 | $322.50 |
| Q | $452.00 | $339.00 |
| R | $474.00 | $355.50 |
| S | $496.00 | $372.00 |
| T | $518.00 | $388.50 |
| U | $540.00 | $405.00 |
| V | $550.00 | $412.50 |
| W | $0 | $0 |

The published table on Form 2290 page 2 is the authoritative source. The amounts above match IRC §4481(a) at the time of last verification (2026-04-28). If the IRS publishes a new revision with different amounts, the published table wins.

---

## Logging Vehicles (25% Reduction)

A logging vehicle qualifies for the 25% rate reduction (IRC §4483(e)) if it meets **both**:

1. The vehicle is used **exclusively** for the transportation of products harvested from the forested site, OR for the transportation of the products harvested from the forested site to and from locations on the forested site
2. The vehicle is **registered as a logging vehicle** under the laws of the state in which it is registered

If a vehicle is used for **both** logging and general hauling, it does not qualify for the 25% reduction. The "exclusively" standard is strict.

---

## Suspended Vehicles (Category W)

A vehicle qualifies for suspension if it is **expected to be used** on public highways:

- **5,000 miles or fewer** during the period (general rule)
- **7,500 miles or fewer** during the period if used for agricultural purposes

**Agricultural use** is defined as: the transportation of any agricultural commodity, or any item used in agricultural production, where the vehicle is registered as a "highway motor vehicle used for farming purposes" or similar agricultural designation under state law.

A suspended vehicle still:

- Gets reported on Form 2290 (cannot skip the filing)
- Gets listed on Schedule 1 with Category W
- Receives a stamped Schedule 1 (with $0 tax shown) for DMV registration
- Triggers Part II (Statement in Support of Suspension) certification

If the suspended vehicle exceeds the mileage threshold during the period, the user must file an Amended Return (Box B) within the month following when the threshold was crossed and pay the full annual tax (or partial-period tax based on first use).

---

## Determining the Right Category for a User

When the user gives a vehicle weight, determine the correct category:

1. **Ask if they have the vehicle registration handy** — it lists the gross vehicle weight rating (GVWR) and combined GVWR for tractor-trailer combinations
2. **Confirm the customary load** — a tractor that always runs empty has a different taxable gross weight than one that always pulls loaded trailers
3. **Round up** — taxable gross weight of 64,500 lbs falls in Category K (64,001-65,000)
4. **Verify against weight tickets** — if available, weigh tickets from scales confirm the actual operating weight

For trucks operating in different weight configurations (e.g., logging 4 days, general hauling 1 day per week), use the **highest customary** weight unless the user qualifies for the strict logging exemption.

If the user is unsure, ask:

> "Looking at the heaviest load you typically run — including trailer and cargo — what's the total weight on the road?"

That answer determines the category.
