# Example: Airbnb Host — Schedule E vs Schedule C Decision Tree

Short-term rental hosts (Airbnb, VRBO, Vrbo, Turo) often receive a 1099-K and immediately ask: Schedule E or Schedule C? The financial impact is significant — Schedule C net profit is subject to 15.3% SE tax, Schedule E is not. Get the classification right.

## The filer

- **Name**: Riley Thompson
- **Property**: Two-bedroom guesthouse behind their primary residence in Asheville, NC
- **Rental activity**: Listed on Airbnb year-round; ~150 guest-nights in 2026
- **Services provided**: Riley does turnover cleaning between guests (or hires a cleaner), provides linens and towels at check-in, leaves a welcome basket. Does NOT provide daily cleaning, meals, transportation, or concierge services.
- **Other rental properties**: None
- **Tax year**: 2026
- **State**: North Carolina (state 1099-K threshold is $600, so Riley would receive a 1099-K from Airbnb regardless of federal threshold)

## The 1099-K

Airbnb Payments, Inc. issued a 1099-K showing:

| Box | Value |
|-----|-------|
| Filer | Airbnb Payments, Inc. |
| Box 1a (Gross) | $32,400 |
| Box 1b (CNP) | $32,400 |
| Box 2 (Transactions) | 87 (one per booking) |
| Box 4 (Federal tax withheld) | $0 |
| Box 6 (State) | NC |

Box 1a includes Airbnb's gross collection — nightly rates + Airbnb cleaning fees + Airbnb service fees + state/local lodging taxes Airbnb collected and remitted.

## Step 1 — Confirm form

Riley confirms the form title says "Payment Card and Third Party Network Transactions." Yes, it's a 1099-K. Box 1a = $32,400 met both federal thresholds ($20,000 + 200... wait, only 87 transactions). Riley would still receive a 1099-K because of NC's $600 state threshold OR because Airbnb voluntarily issues at $20,000 regardless of transaction count for some host categories. Reconciliation needed either way.

## Step 2 — Schedule E vs Schedule C decision tree

The key question: does Riley provide **substantial services** comparable to a hotel?

Per Treasury Regulation §1.1402(a)-4 and IRS Pub 527, "substantial services" include:

- Daily cleaning during the guest's stay (NOT just turnover between guests)
- Meals or breakfast
- Linen changes during the stay (not just initial provision)
- Concierge services
- Transportation to/from airport
- Other hotel-like services

What Riley provides:
- Turnover cleaning (between guests, not during) — NOT substantial
- Linens at check-in (one-time, not changed during stay) — NOT substantial
- Welcome basket (snacks, water) — NOT substantial
- Standard listing maintenance — NOT substantial

**Verdict: Riley does NOT provide substantial services.** This is a passive rental of real property. **Schedule E.**

The substantial-services bar is genuinely high. Most Airbnb hosts file Schedule E. The exception is people running boutique hotels / B&Bs with real hospitality services. Even "luxury" Airbnbs typically don't meet it without daily housekeeping or meals.

## Step 3 — Reconcile against Airbnb records

Riley pulls the Airbnb host dashboard year-end summary:

| Source | Amount |
|--------|--------|
| Gross from guests (nightly rates) | $24,800 |
| Airbnb cleaning fees passed to host | $4,200 |
| Airbnb service fees (host portion) | -$1,400 (deducted before payout) |
| Lodging taxes collected and remitted by Airbnb | $4,800 |
| **1099-K Box 1a total** | **$32,400** ✓ |

The 1099-K reports gross **before** Airbnb's host service fees and **including** the lodging taxes Airbnb collected and remitted to the state.

## Step 4 — Cross-check against other 1099s

Riley received no 1099-NEC from individual guests (guests aren't reporting). No double-reporting.

Riley also collected $1,200 in cash for one guest who paid by check after a platform issue — that $1,200 is not on the 1099-K but is still rental income.

## Step 5 — Map to Schedule E lines

| Line | Description | Amount |
|------|-------------|--------|
| Line 1a | Property location | "Asheville, NC — guesthouse" |
| Line 2 | Type of property | "2 — Multi-Family Residence" |
| Line 3 | Rents received | $32,400 + $1,200 = **$33,600** (1099-K Box 1a + cash) |
| Line 5 | Advertising (Airbnb-internal listing boosts Riley paid for) | $180 |
| Line 6 | Auto and travel (mileage to property for maintenance) | $94 |
| Line 7 | Cleaning and maintenance (paid cleaner $35/turnover × 87 turnovers) | $3,045 |
| Line 8 | Commissions (Airbnb host service fee — the $1,400 deducted from Riley's payouts) | $1,400 |
| Line 9 | Insurance (rental dwelling insurance allocated to guesthouse) | $620 |
| Line 11 | Management fees (none) | $0 |
| Line 12 | Mortgage interest (allocated to guesthouse, if Riley has a mortgage) | $0 (paid off) |
| Line 14 | Repairs (water heater repair, gutter cleaning) | $480 |
| Line 15 | Supplies (toilet paper, soap, snacks for welcome basket) | $215 |
| Line 16 | Taxes (lodging taxes Airbnb collected and remitted on host's behalf — pass-through) | $4,800 |
| Line 17 | Utilities (allocated portion of electric, water, internet) | $1,800 |
| Line 18 | Depreciation (residential rental, 27.5 years straight-line, allocated) | $2,400 |
| Line 19 | Other (linens replacement, welcome basket items) | $310 |
| **Line 20** | **Total expenses** | **$15,344** |
| **Line 21** | **Income or loss** (Line 3 − Line 20) | **$18,256** |

Line 21 net flows to Schedule E Line 26 (Total rental real estate income), then to **Schedule 1 Line 5 (Rental real estate, royalties, partnerships, S corporations, trusts, etc.)**.

## Step 6 — NO Schedule SE

Because this is Schedule E (passive rental, no substantial services), the $18,256 net rental income is **NOT subject to self-employment tax**. Riley saves 15.3% × $18,256 = **$2,793** compared to Schedule C treatment.

This is the entire reason the Schedule E vs Schedule C classification matters financially.

## Step 7 — Form 1040 ledger

| Line | Source | Amount |
|------|--------|--------|
| Schedule 1 Line 5 | Schedule E net rental income | $18,256 |
| Form 1040 Line 8 | Other income from Schedule 1 | $18,256 |
| Form 1040 Line 23 | Other taxes (no SE tax for Schedule E) | $0 |

## Step 8 — Validation

| Check | Result |
|-------|--------|
| Sum of classified portions equals Box 1a | $32,400 = $32,400 ✓ |
| Activity classified as rental real estate without substantial services | ✓ |
| Schedule E Line 3 ≥ trade-or-business portion of Box 1a | $33,600 ≥ $32,400 ✓ (extra is non-1099 cash) |
| No Schedule C filed for this activity | ✓ (no substantial services) |
| Box 4 = $0, no Line 25c entry | ✓ |
| Lodging taxes reported on Line 3 (gross) and deducted on Line 16 (pass-through) | ✓ |

## What Riley does NOT do

- Riley does NOT file Schedule C — that would unnecessarily impose 15.3% SE tax on the $18,256 net.
- Riley does NOT subtract Airbnb's service fee or lodging taxes from Box 1a before reporting Line 3. Gross stays $33,600 (with the cash addition); service fees deduct on Line 8, lodging taxes on Line 16.
- Riley does NOT exclude the $1,200 cash payment from Line 3. All rental income is reportable.
- Riley does NOT depreciate the entire building — only the allocated portion attributable to the guesthouse (separate structure used 100% for rental).

## When Riley WOULD file Schedule C

If Riley's rental business changed to include substantial services — say, Riley converted the guesthouse to a B&B with daily cleaning, breakfast, and concierge services — the activity would become a trade or business per Treas. Reg. §1.1402(a)-4. Then:

- Schedule C, not Schedule E
- Net profit subject to SE tax (15.3%)
- Different depreciation rules (depending on the §168 property class)
- Eligibility for QBI deduction under IRC §199A (which Schedule E rentals can also access via the §199A safe harbor for rentals, but the test differs)

The financial trade-off: substantial services usually allow higher nightly rates, but the SE tax cost is meaningful. Most Airbnb hosts find the no-services Schedule E path more profitable.

## What if Riley was renting only part of their primary residence?

If Riley rented out a spare bedroom in their main house (not a separate guesthouse), the analysis would add a "personal-use vs rental-use days" allocation per IRC §280A:

- **Rented less than 15 days/year**: Rental income excluded from gross income; no expense deduction. (IRC §280A(g) — the "Augusta rule")
- **Rented more than 14 days, personal use exceeds 14 days or 10% of rental days**: Mixed-use; expenses must be allocated; loss limited to rental income.
- **Rented more than 14 days, personal use ≤ 14 days or 10%**: Treated as a rental property; full Schedule E.

Riley's case (separate guesthouse, no personal use) avoids §280A entirely.

## Going forward

Riley should:

1. Keep careful records of which expenses are allocated to the guesthouse vs primary residence
2. Track the 27.5-year depreciation schedule across years (year 2026 partial-year depreciation differs from full-year)
3. Track guest-nights vs vacant-nights for occupancy reporting
4. If considering substantial services, model the SE-tax cost first

## Audit-defense documentation Riley keeps

- The 1099-K (PDF download from Airbnb)
- Airbnb host year-end statement (with breakdown of nightly rates, fees, lodging taxes)
- Airbnb transaction CSV
- Receipts for cleaning expenses, supplies, repairs, insurance, utilities (allocated)
- Depreciation schedule + Form 4562
- Calendar showing rental nights vs vacant nights
- Photos of the guesthouse (proves it's a separate structure)
- The completed Schedule E, Schedule 1
- The reconciliation worksheet (this document, redacted)
- Form 1040 + e-file acceptance confirmation

## Sources cited in this draft

- IRS Form 1099-K (current revision)
- IRS Instructions for Form 1099-K
- IRC §6050W (1099-K reporting)
- IRC §1402(a)(1) (rental real estate excluded from SE tax)
- IRC §280A (personal use of dwelling unit)
- Treasury Regulation §1.1402(a)-4 (substantial services / hotel-like definition)
- Schedule E (Form 1040) and instructions
- [IRS Pub 527 — Residential Rental Property](https://www.irs.gov/publications/p527)
- IRS Topic No. 414 — Rental Income and Expenses
- Companion Jupid blog: [1099-K Guide 2026](https://jupid.com/blog/1099-k-guide-2026)
