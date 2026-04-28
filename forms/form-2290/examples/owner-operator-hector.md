# Form 2290 — Worked Example: Hector, Owner-Operator Trucker

End-to-end Form 2290 filing for an owner-operator running a single 75,000-lb truck for the full 2025-2026 tax period.

---

## Persona

**Hector** is an independent owner-operator. He runs a 2022 Peterbilt 579 day cab, hauling general freight for a regional brokerage. He operates as a single-member LLC ("Hector Logistics LLC") taxed as a disregarded entity (he files Schedule C).

- Truck: 2022 Peterbilt 579, taxable gross weight 75,000 lbs (with typical loaded trailer)
- Use: General hauling, non-logging, non-agricultural
- Mileage: ~85,000 miles per year (well over the 5,000-mile suspension threshold)
- First use date for 2025-2026 period: July 8, 2025
- EIN: 12-3456789 (active for 3 years)
- Files Schedule C as a single-member LLC

---

## Filing Inputs

| Field | Value |
|-------|-------|
| Tax period | July 1, 2025 — June 30, 2026 |
| Filer name | Hector Logistics LLC |
| EIN | 12-3456789 |
| Address | (Hector's business address) |
| Reason for filing | None (standard original filing) |
| Vehicle VIN | 1XPXXXXX0XXXXXXXX (sample) |
| Weight category | U (74,001 — 75,000 lbs) |
| Logging? | No |
| Agricultural? | No |
| First use date | 07/2025 |
| Suspended? | No |

---

## Tax Computation

**Step 1:** Determine weight category.

- Truck taxable gross weight: 75,000 lbs → Category **U**

**Step 2:** Apply rate.

- Standard annual rate for Category U: $540.00
- Logging? No → no 25% reduction
- Full period (July first use)? Yes → no proration

**Step 3:** Per-vehicle tax = **$540.00**

---

## Form 2290 — Filled Draft

```markdown
# Form 2290 — DRAFT for tax period July 1, 2025 — June 30, 2026

## Header
Name: Hector Logistics LLC
Address: <Hector's business address>
EIN: 12-3456789
Tax period: July 1, 2025 through June 30, 2026
Reason for filing: none (standard)

## Part I — Tax Calculation
1. Date of first use:                     07/2025
2. Tax (from Tax Computation table):      $540.00
3. Additional tax from weight increase:   $0.00
4. Total tax (Line 2 + Line 3):           $540.00
5. Credits:                               $0.00
6. Balance due (Line 4 − Line 5):         $540.00

## Part II — Statement in Support of Suspension
N/A — no suspended vehicles

## Schedule 1 — Vehicles
### Part I — Reported Vehicles
| VIN              | Weight Category |
|------------------|-----------------|
| 1XPXXXXX0XXXXXXXX | U (75,000 lbs) |

### Part II — Summary
- Total taxable vehicles: 1
- Suspended (Category W) vehicles: 0
```

---

## Filing Workflow

1. **August 1, 2025** — Hector receives a reminder to file Form 2290
2. **August 5, 2025** — Hector logs into his 2290 e-file provider account
3. **Provider workflow:**
   - Confirms business name, EIN, address
   - Selects tax period 2025-2026
   - Adds vehicle: VIN, Category U, no logging/agricultural flag, first-use July 2025
   - Reviews tax: $540
   - Selects EFW payment from his business checking
   - Reviews and submits
4. **Within 10 minutes** — IRS accepts; provider returns watermarked stamped Schedule 1 PDF
5. **August 5, 2025 (same day)** — Hector saves the stamped Schedule 1:
   - Cloud storage backup
   - Print copy in cab
   - Email forward to himself
6. **August 7, 2025** — $540 EFW debit clears from business checking
7. **September 2025** — Hector renews Wyoming plates; uploads stamped Schedule 1 to state DMV portal; renewal approved

---

## At Tax Time (Schedule C for Tax Year 2025)

The HVUT payment of $540 made in August 2025 is a deductible business expense for tax year 2025. It goes on **Schedule C Line 23 (Taxes and Licenses)**.

Hector's Schedule C Line 23 itemization:

| Item | Amount |
|------|--------|
| HVUT (Form 2290) | $540 |
| State plate registration (Wyoming + permits) | $178 |
| IFTA fuel tax filing | $30 |
| Federal heavy-vehicle preparer fee | $45 (alternatively goes to Line 17) |
| Business license renewal | $50 |
| **Total Schedule C Line 23** | **$843** |

**Tax savings calculation:**

- Hector's marginal federal income tax rate: 22%
- His self-employment tax rate (effective on net SE income): 14.13% (15.3% × 92.35%)
- Combined marginal rate: ~36.13%
- Tax savings from $540 HVUT deduction: $540 × 36.13% ≈ **$195**

So his net out-of-pocket cost for the HVUT, after the federal tax deduction, is roughly $345.

---

## Validation Summary

- **Math:** all checks passed (Line 4 = $540, Line 6 = $540, Schedule 1 has 1 VIN)
- **Sanity:** no warnings (filing on time, EIN active, no suspension, full period)
- **Cross-form:** $540 captured for Schedule C Line 23 deduction; mileage tracking active via ELD; Wyoming DMV renewal scheduled

---

## Lessons This Example Illustrates

1. **Federal fiscal year, not calendar year** — Hector's filing covers July 2025 to June 2026, due August 31, 2025
2. **EIN required even for sole prop / SMLLC** — Hector files Schedule C with an SSN but Form 2290 with the EIN of his LLC
3. **Full-period tax for vehicles in service on July 1** — no proration needed
4. **Stamped Schedule 1 is the operational deliverable** — the DMV doesn't care about the dollar amount, only that the vehicle's VIN is on a stamped Schedule 1
5. **HVUT flows to Schedule C Line 23 next April** — when filing his 2025 tax return in early 2026
