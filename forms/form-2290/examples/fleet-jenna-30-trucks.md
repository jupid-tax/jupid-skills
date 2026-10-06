# Form 2290 — Worked Example: Jenna, 30-Truck Fleet Operator

End-to-end Form 2290 filing for a small fleet operator with 30 mixed vehicles, 2026-2027 period (Form 2290 Rev. July 2026). Mandatory e-file applies because the return reports tax on 25 or more vehicles.

---

## Persona

**Jenna** runs **Jenna Logistics LLC**, an S-corp with 30 trucks doing regional and dedicated freight in the Southeast. Her bookkeeper handles annual compliance filings.

- Fleet: 30 vehicles (mixed — day cabs, sleepers, single-axle straights)
- Use: General hauling, non-logging, non-agricultural
- All vehicles first used in July 2026 for the full 2026-2027 period (none placed in service mid-year)
- EIN: 98-7654321
- Tax election: S-corp (Form 2553 filed in 2018)
- Income tax return: Form 1120-S

---

## Fleet Composition

| Vehicle Type | Count | Taxable Gross Weight | Category | Annual Tax (each) |
|-------------|-------|---------------------|----------|-------------------|
| Day cabs | 18 | 75,000 lbs | U | $540 |
| Sleepers | 8 | over 75,000 lbs | V | $550 |
| Single-axle straight | 4 | 60,000 lbs | F | $210 |
| **Total** | **30** | | | |

---

## Tax Computation

| Vehicle Group | Count | Tax Each | Subtotal |
|--------------|-------|----------|----------|
| Day cabs (Category U) | 18 | $540 | $9,720 |
| Sleepers (Category V) | 8 | $550 | $4,400 |
| Single-axle straights (Category F) | 4 | $210 | $840 |
| **Total fleet HVUT (Line 2 / Line 4 / Line 6)** | **30** | | **$14,960** |

No vehicles are logging, agricultural, or suspended. No mid-year first-use. No prior-period credits. Line 5 = $0.

---

## E-File Mandate

Because the return reports tax on 30 vehicles (≥ 25), e-filing is **mandatory** (IRC §4481(e); Reg. §41.6011(a)-1(c)(1)). Suspended category W vehicles would not count toward the 25: if 6 of the 30 trucks were suspended, the return would report tax on 24 and paper filing would be allowed. Jenna's bookkeeper uses an IRS-approved 2290 e-file provider that supports CSV bulk VIN upload.

---

## Form 2290 — Filled Draft

```markdown
# Form 2290 — DRAFT for tax period July 1, 2026 — June 30, 2027

## Header
Name: Jenna Logistics LLC
Address: <business address>
EIN: 98-7654321
Tax period: July 1, 2026 through June 30, 2027 (Rev. July 2026)
Boxes checked: none

## Part I — Tax Calculation
1. Month of first use:                    202607
2. Tax (from Tax Computation table):      $14,960.00
3. Additional tax from weight increase:   $0.00
4. Total tax (Line 2 + Line 3):           $14,960.00
5. Credits:                               $0.00
6. Balance due (Line 4 − Line 5):         $14,960.00

## Part II — Statement in Support of Suspension
N/A — no suspended vehicles

## Page 2 — Tax Computation (column (1)(a) × column (3)(a) = column (4))
F: $210.00 × 4  = $840.00
U: $540.00 × 18 = $9,720.00
V: $550.00 × 8  = $4,400.00
Total vehicles (3): 30        Total tax (4): $14,960.00 → line 2

## Schedule 1 — Vehicles
Month of first use: 202607
### Part I — Summary of Reported Vehicles
a. Total number of reported vehicles:   30
b. Suspended (category W) vehicles:     0
c. Taxable vehicles (a − b):            30

### Part II — Vehicles You Are Reporting
[All 30 VINs listed with category]
| VIN              | Category |
|------------------|----------|
| 1XPDC001000000001 | U |
| 1XPDC002000000002 | U |
| ... (16 more day cabs) | U |
| 1XPSL001000000001 | V |
| ... (7 more sleepers) | V |
| 1NPSA001000000001 | F |
| ... (3 more straights) | F |
```

---

## Filing Workflow

1. **July 15, 2026** — Bookkeeper opens 2026-2027 filing with the e-file provider
2. **Bulk VIN upload:** CSV file with 30 rows (VIN, weight category) uploaded to provider
3. **Provider validates** all VINs are 17 characters
4. **Tax review:** Provider's tax calculation matches the bookkeeper's: $14,960
5. **Payment:** EFW from S-corp operating account; bank routing + account entered for one-time debit
6. **Submission:** August 4, 2026 (27 days before the August 31, 2026 deadline)
7. **IRS acceptance:** within 15 minutes
8. **Watermarked Schedule 1 PDF:** received as a single PDF listing all 30 VINs
9. **DMV distribution:** Bookkeeper forwards stamped Schedule 1 to each state DMV portal where vehicles are registered (FL, GA, AL — three states)
10. **Bank debit clears:** August 6, 2026

---

## At Tax Time (Form 1120-S for Tax Year 2026)

The $14,960 HVUT paid in 2026 is a deductible business expense on the S-corp's 2026 income tax return.

It goes on **Form 1120-S, Line 12 (Taxes and licenses)**, alongside:

| Item | Amount |
|------|--------|
| HVUT (Form 2290) | $14,960 |
| State plate registrations (30 trucks) | $5,400 |
| IFTA quarterly fuel tax | $1,200 |
| State business income tax | $3,800 |
| Federal payroll taxes (employer share) | $24,500 |
| **Total Line 12** | **$49,860** |

The $14,960 reduces the S-corp's ordinary business income, which flows through to Jenna and any other shareholders on Schedule K-1.

---

## Validation Summary

- **Math:** all checks passed (Line 4 = $14,960; Schedule 1 Part II has 30 VINs = Part I line a; line c = 30 = page 2 column (3) total)
- **Sanity:** no warnings (e-file required and used, EIN active, all vehicles full-period)
- **Cross-form:** $14,960 captured for Form 1120-S Line 12; stamped Schedule 1 distributed to FL/GA/AL DMVs

---

## Lessons This Example Illustrates

1. **Tax reported on 25+ vehicles = mandatory e-file** (IRC §4481(e); Reg. §41.6011(a)-1(c)(1)); category W vehicles don't count
2. **Bulk VIN upload via CSV** is offered by some providers (confirm with the chosen one) — much faster than entering 30 vehicles by hand
3. **Single Schedule 1 PDF** lists all VINs — distributed to multiple state DMVs as needed
4. **S-corp deduction goes on Form 1120-S Line 12**, not Schedule C (which is for sole props/SMLLCs)
5. **Filing 3+ weeks before deadline** is good practice for fleets — gives time to fix any rejected submissions
