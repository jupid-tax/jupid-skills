# Form 2290 — Suspension Category (W) Reference

Suspension is the most-misunderstood part of Form 2290. The agent must understand it well to avoid two common mistakes:

1. **Skipping the filing** because the vehicle won't drive much (wrong — file with $0 tax)
2. **Filing under suspension** without a mileage tracking method (wrong — set up tracking before period start)

---

## What Is Suspension?

A vehicle is **suspended** (Category W) for a tax period if it is **expected to be used** on public highways:

- **5,000 miles or fewer** during the period (general rule), OR
- **7,500 miles or fewer** if used for **agricultural purposes**

Suspension means **$0 tax owed**, but the filing still happens.

**Legal Basis:** IRC §4483(d). The IRS calls this "vehicles used for less than 5,000 miles" (or 7,500 for agricultural).

---

## What Counts as Agricultural Use?

A vehicle qualifies for the 7,500-mile agricultural threshold if:

1. The vehicle is **used primarily** for farming purposes during the period — meaning at least 50% of the vehicle's use during the period is for farming
2. The vehicle is **registered** as a "highway motor vehicle used for farming purposes" under state law (state designations vary)

**Farming purposes include:**

- Transporting any agricultural commodity to or from the farm
- Transporting any item used in agricultural production (feed, seed, fertilizer, equipment) to the farm
- Direct use in farming operations (e.g., a feed truck running between barns and fields)

**Farming does NOT include:**

- Long-haul trucking of agricultural products by a non-farmer (a contract trucker hauling cattle for a ranch is not farming use, even though the cargo is agricultural — they don't qualify for the 7,500 threshold)
- Transporting agricultural products from the farm to processing plants more than ~150 miles away (the IRS scrutinizes this)

If the user is a rancher with their own truck that they drive themselves to haul their own cattle, that's clear agricultural use. If they're a contract trucker hired by ranchers, it's not.

---

## Why You Still File a Suspended Vehicle

Three reasons the suspension category is filed (not skipped):

1. **Schedule 1 for DMV plate registration** — Even a $0-tax suspended vehicle gets a stamped Schedule 1, which the state DMV requires
2. **Audit trail** — The IRS knows the vehicle exists; if you don't file at all, they may eventually inquire
3. **Penalty avoidance** — Failure to file is its own penalty (IRC §6651), independent of tax owed

---

## Filing a Suspended Vehicle — Required Steps

### On Form 2290

- List the VIN on Schedule 1 with **Category W**
- Complete Part II (Statement in Support of Suspension)
  - Statement (a): Certify the vehicle will be used 5,000 miles or fewer (or 7,500 if agricultural)
  - User signs the statement (sworn certification)
- Line 2 (tax) excludes this vehicle's contribution
- Line 6 (balance due) reflects $0 for this vehicle

### After Filing

- Save the stamped Schedule 1 — provide to state DMV
- **Begin or continue mileage tracking** for the vehicle
  - Paper logbook (date, route, miles)
  - ELD (electronic logging device, common in commercial trucking)
  - Fleet management software (Motive, Samsara, etc.)
- Set a personal threshold alert at 4,500 miles (or 7,000 agricultural) — gives time to amend before crossing

---

## What Happens If Mileage Exceeds the Threshold

If a suspended vehicle drives **more than 5,000 miles** (or **more than 7,500 if agricultural**) during the period, the suspension is voided and the user owes the **full annual tax** for that vehicle (or the partial-period tax if first use was mid-year).

### Required Action

1. **File an Amended Return** (Form 2290 with Box B checked) within the month following when the threshold was crossed
2. Pay the tax owed (the full annual or partial-period rate based on the vehicle's first-use month)
3. Receive an updated stamped Schedule 1 reflecting the correct category (A-V instead of W)

### Worked Example

Sarah filed her cattle hauler under Category W (agricultural, 7,500-mile threshold) on August 1, 2025. By April 15, 2026, the truck has driven 7,400 miles. She thinks usage will stay under 7,500 for the remaining 2.5 months.

Then in late April she takes a one-time long haul, putting the truck at 8,200 miles by April 30.

**She must:**
- File an Amended Return by **May 31, 2026** (last day of month following when threshold was crossed)
- Pay the full annual tax for the truck (Category C if 56,000 lbs taxable gross weight = $144)
- Receive an updated Schedule 1 with Category C
- Forward the new Schedule 1 to the state DMV

If she doesn't amend, the IRS can later reconcile her records and assess the tax plus failure-to-file and failure-to-pay penalties.

---

## Mileage Tracking Methods

The agent should ask the user how they're tracking miles. Acceptable methods:

| Method | Pros | Cons |
|--------|------|------|
| Paper logbook | Simple, low-tech | Easy to forget; hard to audit |
| Spreadsheet (Excel, Google Sheets) | Searchable; backup-able | Requires manual entry |
| ELD (Electronic Logging Device) | Automatic; FMCSA-required for many commercial vehicles | Cost; may not include personal trips |
| Fleet management software | Best for fleets; integrates with maintenance, fuel | Cost; setup time |
| Odometer photos | Verifiable; timestamped | Tedious; gaps if not done regularly |

For suspended vehicles, the agent should recommend:

- **Daily** odometer log (date + miles driven)
- **Monthly** total summary
- **Periodic** photo of odometer for proof

Records should be kept for at least 3 years (the standard IRS audit window).

---

## Edge Cases

### Edge Case 1: Vehicle Suspended in Prior Period, Stayed Under Threshold

If a vehicle was Category W last period and finished the period under the mileage threshold:

- Current period filing: continue Category W if expected use is still under threshold
- Complete Part II Statement (c) — Carry-Forward Suspended Vehicles
- No tax owed, no credit needed (no tax was paid in the prior period)

### Edge Case 2: Vehicle Suspended in Prior Period, Sold During Prior Period

- Current period: do NOT include the vehicle on Schedule 1 (it's no longer the user's)
- Complete Part II Statement (b) — Sold Prior-Period Suspended Vehicles
- Lists the VIN and date of sale to close the IRS expectation

### Edge Case 3: Vehicle Originally Filed at Active Category, Stayed Under Threshold

- The user paid full tax but should have suspended
- Current period filing: claim the prior-period tax as a credit on Line 5 (Scenario 3 in [`tax-table.md`](./tax-table.md))
- File the current vehicle either as suspended (W) or active (A-V) based on expected use

### Edge Case 4: Mid-Year Fleet Sale

If the user sells the entire fleet mid-period:

- The buyer files Form 2290 for first use as of the date of sale (mid-year first-use rules)
- The seller may claim a credit on next year's filing (or via Form 8849) for the unused months on each vehicle
- The seller files Form 2290 with Box D (Final Return) on the next 2290 they would have filed (or sooner, if confident the sale is permanent)

---

## Penalty Math for Failure to File or Pay

If the user misses the deadline (didn't file at all, or filed but didn't pay):

```
Failure-to-file penalty = 4.5% of unpaid tax per month (max 25%)
Failure-to-pay penalty   = 0.5% of unpaid tax per month (max 25%)
Interest                 = federal short-term rate + 3%, compounded daily
```

Both failure-to-file and failure-to-pay can apply concurrently in some cases — see IRC §6651.

The minimum penalty for late filing (when the return is more than 60 days late) is the **lesser** of $485 (2025 figure) or the full unpaid tax. This figure adjusts for inflation; verify current amount in IRS Notice or instructions.

---

## When in Doubt — File and Pay, Then Amend

If the user is genuinely unsure whether the truck will stay under the mileage threshold (e.g., new owner-operator who doesn't yet have a usage pattern), the **safer** approach is:

1. File at the active category (A-V) and pay the full tax
2. Track mileage rigorously
3. If usage stays under the threshold, claim a credit on next year's Line 5 (or via Form 8849 for a refund)

The downside is paying tax that may be refunded later. The upside is no risk of failure-to-pay penalty if usage exceeds the threshold.

For users with established low-mileage patterns (the rancher who's hauled cattle for 20 years and never come close to 7,500 miles), filing under suspension is appropriate from the start.
