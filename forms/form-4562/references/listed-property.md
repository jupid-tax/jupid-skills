# Listed Property — IRC §280F Rules

Listed property gets stricter treatment than other assets because it commonly involves mixed business/personal use. The rules in IRC §280F govern: §179, bonus, depreciation method/period, substantiation, and the "luxury auto" annual deduction caps.

---

## What is "listed property"

IRC §280F(d)(4) listed-property classes:

1. **Passenger automobiles** — any 4-wheeled vehicle made for use on public streets, ≤6,000 lbs unloaded GVWR (or ≤6,000 lbs GVWR for trucks/vans)
2. **Other transportation property** — boats, planes, motorcycles (when used for entertainment/recreation context)
3. **Property generally used for entertainment, recreation, or amusement** — rare for solo filers
4. **Computers and peripheral equipment** — unless used at a regular business establishment >50% of the time. (Per TCJA, this listed-property treatment for computers was REMOVED for property placed in service after 2017 — verify current IRS guidance; many practitioners and IRS instructions still treat computers as listed property out of caution).

The rules below apply to listed property for the year placed in service and throughout the recovery period.

---

## The >50% business-use test

**For listed property:**
- **Year 1**: business use must be >50% (more than 50%, not at least 50%) to use §179, bonus, or accelerated MACRS
- **Subsequent years**: if business use drops to ≤50% before end of recovery period, recapture is triggered (IRC §280F(b)(2))
- **Recapture**: §179 + bonus + accelerated MACRS taken minus the SL ADS depreciation that would have been allowable. Reported on Form 4797 in the year of the drop.

**Qualified business use** (the >50% numerator):
- Use in the taxpayer's trade or business
- Excludes: use as a vehicle to commute, use by a >5%-owner-employee or related person other than for business, leasing back to one's own employer
- Investment use does NOT count toward the >50% qualified business use test (though it can be combined for the depreciation deduction itself)

---

## Substantiation

IRC §274(d) and Reg. §1.274-5 require for listed property:

- **Amount** of each business use (e.g., miles for vehicles)
- **Time** of the use (date)
- **Business purpose** of the use
- **Business relationship** if applicable

Requirement: a **contemporaneous written log**. "Contemporaneous" means at or near the time of use; reconstruction after the fact is allowed but viewed skeptically by the IRS.

Methods that meet the bar:
- Mileage tracking app (Jupid, MileIQ, Hurdlr) with date/destination/purpose
- Spreadsheet updated weekly
- Calendar entries with travel notes
- Receipts with notes

Methods that do NOT meet the bar:
- Year-end estimate
- "I drove a lot for business" statement
- Reconstruction with no source data

Form 4562 Part V Lines 24a/24b are the substantiation declaration. Answer truthfully — the IRS uses these answers in audit selection.

---

## §280F luxury auto caps (passenger autos ≤6,000 lbs GVWR)

The IRS publishes annual caps on the maximum first-year depreciation (including §179 + bonus + MACRS) for passenger autos. The caps are inflation-adjusted via Revenue Procedure each year.

Schedule for passenger autos placed in service in 2025 (Rev. Proc. 2024-13 / Rev. Proc. 2024-40 — verify):

| Year | Cap with bonus | Cap without bonus |
|------|----------------|--------------------|
| 1 | ~$20,400 | ~$12,400 |
| 2 | ~$19,800 | ~$19,800 |
| 3 | ~$11,900 | ~$11,900 |
| 4 and after | ~$7,160 | ~$7,160 |

**Verify the exact 2025 figures** in IRS Rev. Proc. 2024-13 (or the equivalent annual updating procedure). 2026 figures will be published late 2025.

The cap is applied **after** computing the un-capped §179 + bonus + MACRS. Excess is carried forward and depreciated post-recovery-period at the year-4-and-after rate until fully recovered.

Worked example: $50,000 passenger sedan placed in service in 2025, 100% business use, taxpayer elects §179 + bonus.

```
Cost basis:                     $50,000
Bus%:                           100%
Adjusted basis:                 $50,000

§179 attempted:                 $50,000  (within dollar limit)
Bonus attempted:                $0       (after §179 fills basis)
MACRS year 1:                   $0

§280F year 1 cap (with bonus):  $20,400
First-year deduction:           $20,400  ← capped
Excess held over:               $29,600  ← recovers post-recovery-period
```

The luxury auto cap is the most-overlooked rule for solo filers buying expensive sedans for business. The vehicle's full cost gets recovered eventually, but spread over many more years than 5.

---

## Heavy SUV exception (>6,000 lbs GVWR)

Vehicles with GVWR >6,000 lbs are NOT passenger autos for §280F purposes. They escape the luxury auto caps. They are still listed property and require >50% business use.

**§179 cap for heavy SUVs**: IRC §179(b)(5) caps §179 at $31,300 for 2025 (verify 2026). This cap applies to:
- Sport utility vehicles
- Vehicles with gross vehicle weight rating >6,000 lbs and ≤14,000 lbs
- Cargo bed ≤6 feet in interior length

Vehicles that are NOT subject to the heavy SUV §179 cap (and can §179 the full cost subject to general dollar limit):
- Vehicles with cargo bed ≥6 feet (long-bed pickups)
- Vehicles >14,000 lbs GVWR (commercial trucks)
- Vehicles with seating for ≥9 passengers behind the driver (transit-style vans)
- Vehicles with cargo area separated from driver compartment, no seats behind driver, no body section protruding more than 30 inches ahead of windshield (delivery vans, ambulances, hearses)

After §179 ($31,300 cap for SUV), the remaining basis can take 100% bonus depreciation (uncapped for heavy SUVs), so a $80,000 heavy SUV at 100% business use can fully expense in year 1:

```
Cost:                           $80,000
Bus%:                           100%
Adjusted basis:                 $80,000

§179 (heavy SUV cap):           $31,300
Adjusted basis after §179:      $48,700
Bonus (100% in 2025 post-Jan 19): $48,700
MACRS year 1:                   $0
Total year 1:                   $80,000
```

This is the "Hummer loophole" / "Section 179 for trucks" pattern. It's legitimate but **only if business use truly exceeds 50%** and is substantiated.

---

## Standard mileage vs. actual expenses for vehicles

A taxpayer using the **standard mileage rate** (Notice annually; 70¢/mile for 2025 per Notice 2025-5; 2026 verify) does NOT report depreciation on Form 4562 for the vehicle. The mileage rate already includes a depreciation component.

A taxpayer using **actual expenses** must:
- Track all vehicle costs (gas, insurance, repairs, lease, etc.) and apply business-use %
- Include depreciation via Form 4562 Part V
- Usually elect §179 / bonus / MACRS through Form 4562

Switching:
- Can switch from standard mileage to actual in any year **if the vehicle was originally placed in service using standard mileage** (then must use SL on the remaining basis)
- Cannot switch from actual back to standard mileage if MACRS was used (one-way door)

---

## Section C — employer-provided vehicles (Lines 37–41)

This section is for entities (S-corp, C-corp, partnership) that provide vehicles to their employees. It asks:

- Does the employer maintain a written policy prohibiting personal use?
- Is the vehicle used >50% in the employer's trade or business?
- Etc.

Solo filers without employees skip this section.

S-corp owners who are also employees of their own S-corp may need to report personal use as wages (added to W-2 income); the company-side reporting flows through Section C.

---

## Common mistakes with listed property

1. **Claiming >50% business use without a log** — audit risk, deduction often disallowed
2. **Claiming 100% business use of a sole vehicle** — IRS skeptical when the household has only one car
3. **Forgetting the §280F cap on a sedan** — taxpayer expects $50,000 deduction, gets $20,400
4. **Forgetting the heavy SUV §179 cap** — taxpayer §179s the full $80,000 truck cost, but §179 capped at $31,300; remainder must be bonus or MACRS
5. **Using §179 + bonus then dropping business use to 40%** — recapture; reported on Form 4797
6. **Combining standard mileage with actual depreciation** — double-counting; mileage rate already includes depreciation
7. **Counting commuting miles as business miles** — not business; Line 30b separates them
8. **Treating a computer used 60% personally as listed property eligible for §179** — fails >50% business use; must use ADS SL

---

## Citations

- IRC §280F: limitations on luxury automobiles and listed property
- IRC §280F(b)(2): recapture when business use drops ≤50%
- IRC §280F(d)(4): definition of listed property
- IRC §179(b)(5): heavy SUV §179 cap
- IRC §274(d): substantiation requirement
- Reg. §1.274-5: substantiation rules
- Reg. §1.280F-2T: passenger auto rules
- Rev. Proc. 2024-13 and Rev. Proc. 2024-40: 2025 inflation adjustments for §280F caps and §179(b)(5) heavy SUV cap
- Notice 2025-5: 2025 standard mileage rate (70¢)
- IRS Pub. 463: Travel, Gift, and Car Expenses (vehicle substantiation)
- IRS Pub. 946: How to Depreciate Property (Chapter 5 covers listed property)
