# Form 2290 — Worked Example: Hector, Owner-Operator Trucker

End-to-end Form 2290 filing for an owner-operator running a single 75,000-lb truck for the full 2026-2027 tax period (Form 2290 Rev. July 2026).

---

## Persona

**Hector** is an independent owner-operator. He runs a 2022 Peterbilt 579 day cab, hauling general freight for a regional brokerage. He operates as a single-member LLC ("Hector Logistics LLC") taxed as a disregarded entity (he files Schedule C).

- Truck: 2022 Peterbilt 579, taxable gross weight 75,000 lbs (with typical loaded trailer)
- Use: General hauling, non-logging, non-agricultural
- Mileage: ~85,000 miles per year (well over the 5,000-mile suspension threshold)
- First use date for 2026-2027 period: July 8, 2026
- EIN: 12-3456789 (active for 3 years)
- Files Schedule C as a single-member LLC

---

## Filing Inputs

| Field | Value |
|-------|-------|
| Tax period | July 1, 2026 — June 30, 2027 |
| Filer name | Hector Logistics LLC |
| EIN | 12-3456789 |
| Address | (Hector's business address) |
| Boxes checked | None (original return) |
| Vehicle VIN | 1XPXXXXX0XXXXXXXX (sample) |
| Weight category | U (74,001 — 75,000 lbs) |
| Logging? | No |
| Agricultural? | No |
| Month of first use (line 1) | 202607 |
| Suspended? | No |

---

## Tax Computation

**Step 1:** Determine weight category.

- Truck taxable gross weight: 75,000 lbs → Category **U**

**Step 2:** Apply rate.

- Standard annual rate for Category U: $540.00 (Form 2290 page 2, column (1)(a))
- Logging? No → no 25% reduction
- Full period (July first use)? Yes → no proration

**Step 3:** Per-vehicle tax = **$540.00**

---

## Form 2290 — Filled Draft

```markdown
# Form 2290 — DRAFT for tax period July 1, 2026 — June 30, 2027

## Header
Name: Hector Logistics LLC
Address: <Hector's business address>
EIN: 12-3456789
Tax period: July 1, 2026 through June 30, 2027 (Rev. July 2026)
Boxes checked: none

## Part I — Tax Calculation
1. Month of first use:                    202607
2. Tax (from Tax Computation table):      $540.00
3. Additional tax from weight increase:   $0.00
4. Total tax (Line 2 + Line 3):           $540.00
5. Credits:                               $0.00
6. Balance due (Line 4 − Line 5):         $540.00

## Part II — Statement in Support of Suspension
N/A — no suspended vehicles

## Schedule 1 — Vehicles
Month of first use: 202607
### Part I — Summary of Reported Vehicles
a. Total number of reported vehicles:   1
b. Suspended (category W) vehicles:     0
c. Taxable vehicles (a − b):            1

### Part II — Vehicles You Are Reporting
| VIN              | Category |
|------------------|----------|
| 1XPXXXXX0XXXXXXXX | U       |
```

---

## Filing Workflow

1. **August 1, 2026** — Hector receives a reminder to file Form 2290
2. **August 5, 2026** — Hector logs into his 2290 e-file provider account
3. **Provider workflow:**
   - Confirms business name, EIN, address
   - Selects tax period 2026-2027
   - Adds vehicle: VIN, Category U, no logging/agricultural flag, first-use July 2026
   - Reviews tax: $540
   - Selects EFW payment from his business checking
   - Reviews and submits
4. **Within 10 minutes** — IRS accepts; provider returns watermarked Schedule 1 PDF
5. **August 5, 2026 (same day)** — Hector saves the stamped Schedule 1:
   - Cloud storage backup
   - Print copy in cab
   - Email forward to himself
6. **August 7, 2026** — $540 EFW debit clears from business checking
7. **September 2026** — Hector renews Wyoming plates; uploads stamped Schedule 1 to state DMV portal; renewal approved

---

## At Tax Time (Schedule C for Tax Year 2026)

The HVUT payment of $540 made in August 2026 is a deductible business expense for tax year 2026. It goes on **Schedule C Line 23 (Taxes and licenses)**; the Schedule C instructions list "Federal highway use tax" under line 23.

Hector's Schedule C Line 23 itemization:

| Item | Amount |
|------|--------|
| HVUT (Form 2290) | $540 |
| State plate registration (Wyoming + permits) | $178 |
| IFTA fuel tax filing | $30 |
| Business license renewal | $50 |
| **Total Schedule C Line 23** | **$798** |

The $45 fee he paid the 2290 e-file provider is not a tax or license; it belongs on Line 17 (Legal and professional services), not Line 23.

The tax effect of the $540 deduction depends on Hector's whole return (income tax bracket, self-employment tax, the qualified business income deduction). This skill does not compute it; use the [Schedule C](../../schedule-c/SKILL.md) and [Schedule SE](../../schedule-se/SKILL.md) skills for that.

---

## Validation Summary

- **Math:** all checks passed (Line 4 = $540, Line 6 = $540, Schedule 1 has 1 VIN)
- **Sanity:** no warnings (filing on time, EIN active, no suspension, full period)
- **Cross-form:** $540 captured for Schedule C Line 23 deduction; Wyoming DMV renewal scheduled

---

## Lessons This Example Illustrates

1. **July–June tax period, not calendar year** — Hector's filing covers July 2026 to June 2027, due August 31, 2026
2. **EIN required even for sole prop / SMLLC** — Hector files Schedule C with an SSN but Form 2290 with the EIN of his LLC
3. **Full-period tax for vehicles first used in July** — no proration needed
4. **Stamped Schedule 1 is the operational deliverable** — the DMV doesn't care about the dollar amount, only that the vehicle's VIN is on a stamped Schedule 1
5. **HVUT flows to Schedule C Line 23 next spring** — when filing his 2026 tax return in early 2027
