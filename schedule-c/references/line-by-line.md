# Schedule C Line-by-Line Reference

Complete lookup for every line on Schedule C. Use this when the agent needs to confirm where an expense belongs or what a line means.

## Header (identifies you and the business)

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name | Filer's legal name (not business name) | Even if the user has a DBA |
| (top) | SSN | Filer's SSN | Or ITIN if no SSN |
| A | Principal business or profession | Plain English: "Freelance graphic design", "Online sales of jewelry" | One line, ~50 chars |
| B | Business code | 6-digit NAICS code | See [naics-codes.md](./naics-codes.md) |
| C | Business name | DBA or trade name | Blank if user uses their personal name |
| D | EIN | 9-digit Employer ID Number | Blank → use SSN. Get free at IRS.gov/EIN. |
| E | Business address | Where the business operates | If same as Form 1040 home address: blank, check the box |
| F | Accounting method | Cash / Accrual / Other | Cash for ~99% of solo filers |
| G | Material participation | Yes / No | Yes for owner-operated businesses |
| H | Started this year | Checkbox | Only if first Schedule C for this business |
| I | Paid any individual ≥ $600 | Yes / No | Triggers 1099-NEC obligation |
| J | (If I=Yes) Will file required 1099s | Yes / No | Honest answer; informs the IRS |

---

## Part I — Income

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 1 | Gross receipts or sales | All gross income from the business: 1099-NEC + 1099-K + cash + checks + crypto + barter at FMV | Income reported on other schedules (W-2 wages, partnership K-1 income, rental income on Schedule E) |
| 2 | Returns and allowances | Refunds and price adjustments given to customers | Bad debts (those go on Line 27a if cash basis, or are deducted differently on accrual) |
| 3 | (= Line 1 − Line 2) | Computed |  |
| 4 | Cost of goods sold | From Part III, Line 42. Service businesses: 0 | Day-to-day operating costs (those are Lines 8-27) |
| 5 | (= Line 3 − Line 4) | Computed |  |
| 6 | Other income | Interest on business bank accounts, scrap sales, recovered bad debts, federal/state fuel tax credit, business credit card rewards | Personal income |
| 7 | (= Line 5 + Line 6) | Computed = Gross income |  |

**Critical rule for Line 1**: Report ALL income, regardless of whether a 1099 was issued. The IRS often *catches* under-reporting via 1099 cross-matching. Line 1 should be ≥ the sum of all 1099s the user received. If it's less, that's almost always an error.

---

## Part II — Expenses

### Line 8 — Advertising

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Online ads (Google, Meta, LinkedIn, X, TikTok) | Customer gifts (27a, capped $25/recipient/year per IRC §274(b)) |
| Print advertising | Trade show booth fees if part of travel (24a + 27a split) |
| Business cards, brochures, flyers | Sponsorships of sports teams (sometimes; depends on if it's truly advertising or charitable) |
| Website hosting, domain, design (if not capitalized) | Major website rebuild capitalized as a long-term asset (Line 13 via Form 4562) |
| Promotional materials | |
| Social media management subscriptions | |

### Line 9 — Car and truck expenses

Two options — pick one and stick with it for the year:

**Standard mileage**: business miles × IRS rate.
- 2024 rate: 67 cents/mile
- 2025 rate: 70 cents/mile
- 2026 rate: announced by IRS in late 2025 — verify at https://www.irs.gov/tax-professionals/standard-mileage-rates

If using standard mileage, you can also deduct: parking fees while on business, tolls, business-use portion of vehicle interest (16b) and personal property tax on the vehicle (23). You cannot also deduct gas, repairs, insurance, depreciation, or lease payments — those are bundled into the rate.

**Actual expenses**: total vehicle costs × business-use %. Total = gas + oil + repairs + insurance + registration + depreciation (or lease) + tires.

Switching: you can switch from standard to actual in any year, but if you started with actual and used MACRS depreciation, you must continue with actual. This is mostly a one-way door.

Always require: contemporaneous mileage log with date, destination, business purpose, miles. Without it, the deduction is hard to defend.

If Line 9 > 0, Part IV must be completed.

### Line 10 — Commissions and fees

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Sales commissions paid to agents/brokers | Wages to W-2 sales employees (Line 26) |
| Referral fees | Contract labor for non-sales work (Line 11) |
| Affiliate commissions paid out | |
| Payment processor fees (Stripe, Square, PayPal, Shopify Payments) | |
| Marketplace seller fees (Etsy, Amazon, eBay listing/final-value fees) | |
| Booking platform fees (Airbnb, Vrbo if Schedule C-eligible) | |

### Line 11 — Contract labor

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Bookkeeper / accountant fees if they work *with* the business (not a sale) | CPA who prepares the user's return (Line 17) |
| Subcontracted services (designer, developer, copywriter) | Sales commissions (Line 10) |
| Virtual assistant | Wages to W-2 employees (Line 26) |
| Cleaning services for office | |
| Web developer (one-off project) | |

If the user paid any individual contractor $600+ in the year, they must file Form 1099-NEC for that contractor. Note this on Line I/J of the header.

### Line 12 — Depletion

Only for natural-resource extraction (oil, gas, timber, minerals). Almost never applicable to solo filers. If the user is in this niche, a depletion schedule is required — out of scope for this skill.

### Line 13 — Depreciation and Section 179

The Form 4562 total. See [`depreciation.md`](./depreciation.md) for the year-by-year limits and recapture rules.

Quick rules:
- Items ≤ $2,500: expense under de minimis safe harbor; put on Lines 18, 22, or 27a
- Items > $2,500 with useful life > 1 year: depreciate or §179 via Form 4562
- §179 is limited to taxable business income; excess carries forward
- Listed property (vehicles, computers, cell phones) has stricter substantiation requirements

### Line 14 — Employee benefit programs

For *employees* (W-2), not the owner.
- Health insurance for employees
- Group life insurance
- Dependent care assistance
- Educational assistance up to IRC §127 limits

The owner's own benefits go elsewhere:
- Owner's health insurance: Schedule 1 Line 17 (self-employed health insurance deduction)
- Owner's retirement: Schedule 1 Line 16 (SEP, SIMPLE, solo 401k)

### Line 15 — Insurance (other than health)

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| General liability insurance | Vehicle insurance (already inside Line 9 actual or mileage rate) |
| Professional liability / E&O | Health insurance for self (Schedule 1 Line 17) |
| Business property insurance | Health insurance for employees (Line 14) |
| Business interruption | Personal insurance |
| Workers' compensation premiums | |
| Cyber liability | |
| Surety bonds for the business | |

### Lines 16a / 16b — Mortgage / other interest

- **16a**: Business mortgage interest if the user owns property *separately used by the business*. Not the home office (that flows through Form 8829).
- **16b**: All other business interest:
  - Business loan interest
  - Business credit card interest
  - Equipment financing interest
  - Vehicle loan interest *only if using actual expense method* on Line 9 (otherwise it's bundled in the standard mileage rate)

### Line 17 — Legal and professional services

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Attorney fees for business | Personal legal fees |
| CPA / accountant fees (business portion of return prep) | Personal portion of tax prep |
| Bookkeeping services | |
| Tax software subscription (business use %) | |
| Professional consultants | |
| Trade or professional association dues | |
| Jupid subscription, QuickBooks, FreshBooks | |

### Line 18 — Office expense

Small consumables, ≤ $2,500 individual items. If a single item costs more than $2,500 it goes to Line 13.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Paper, pens, ink, toner | Inventory (Part III) |
| Postage and small shipping supplies | Large shipping for products sold (varies; either Line 22 supplies or COGS) |
| Small electronics under $2,500 | |
| Office cleaning supplies | |
| Coffee and water for office | |

### Line 19 — Pension and profit-sharing plans

For employees only. Owner's contributions to SEP, SIMPLE, or solo 401(k) deduct on **Schedule 1 Line 16**, not here.

### Line 20a / 20b — Rent or lease

- **20a**: Vehicles, machinery, equipment leased for business. Note: if using standard mileage on Line 9, do *not* include vehicle lease payments here (they're inside the mileage rate).
- **20b**: Rent for office space, coworking, storage, studio.

### Line 21 — Repairs and maintenance

Repairs return an asset to *previous* working condition. Improvements that *increase* value or extend useful life are capitalized and depreciated (Line 13, via Form 4562).

| Repair (Line 21) | Improvement (Line 13) |
|------------------|------------------------|
| Fixing a broken laptop screen | Upgrading to a more powerful CPU |
| Patching a hole in office wall | Adding a new room to the office |
| Servicing the printer | Replacing the entire printer with a higher-end model |
| Routine vehicle maintenance (if Line 9 actual) | Engine rebuild |

### Line 22 — Supplies

Materials consumed by the business that aren't inventory.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Project materials (for service businesses with material costs) | Inventory for resale (Part III) |
| Cleaning supplies for non-office areas | Office supplies (Line 18) |
| Safety equipment (PPE) | Major equipment > $2,500 (Line 13) |
| Small tools that wear out | |

### Line 23 — Taxes and licenses

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Business license fees | Federal income tax |
| State and local business taxes (gross receipts tax, B&O tax) | Self-employment tax |
| Property tax on business assets | Personal property tax (unless business-use portion) |
| Employer portion of payroll taxes (FICA, FUTA) | Employee portion (those are inside Line 26 wages) |
| Professional license renewal | |
| Sales tax collected and remitted (if user is the retailer) | |

### Line 24a — Travel

Away-from-home overnight business travel.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Airfare | Local commute |
| Hotel | Personal vacation |
| Rental car | Vehicle use at home (Line 9) |
| Train, bus | |
| Local taxi/Uber while at travel destination | |
| Conference registration fees | |
| Tips and incidentals | |

"Away from home" means the user is gone overnight or long enough to require sleep/rest — not just out of town for the day.

### Line 24b — Deductible meals (50%)

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Meals with clients/prospects (50%) | Meals while *not* traveling and not with clients (not deductible) |
| Meals while traveling for business (50%) | Entertainment (not deductible since TCJA 2018) |
| Conference meals provided by attendee (50%) | Office snacks and coffee (those are typically Line 18) |
| Team meals (50%) if employees attended | |

The 50% limit is in IRC §274(n). Always document: date, place, business purpose, attendees.

### Line 25 — Utilities

For a separate (non-home-office) business location:
- Electric
- Gas / heating
- Water
- Internet (dedicated business line at the business location)
- Phone (dedicated business line)

If the user works from a home office, utilities are inside Line 30 (simplified) or Form 8829 (regular). They do *not* go here.

### Line 26 — Wages

Gross W-2 wages paid to employees. Report before withholding. The employer FICA + FUTA portion goes on Line 23, not here.

If the user has no W-2 employees (solo or only contractors), this is zero.

### Line 27a — Other expenses

Catchall for anything that doesn't fit Lines 8-26. Common items:

- Software subscriptions (Adobe, Notion, Figma, ChatGPT, etc.)
- Professional membership fees (other than trade association on Line 17)
- Education and training directly related to current business
- Bank service charges
- Business portion of cell phone and home internet (with %)
- Uniforms/work clothing if required and unsuitable for everyday wear
- Bad debts (cash basis: deduct when written off; accrual: deduct when included in income but not collected)
- Gifts to clients (capped $25 per recipient per year, IRC §274(b))
- Business publications and subscriptions (NYT for a journalist, Adweek for a marketer, etc.)
- Conference fees (registration, not travel/meals)

Each Line 27a item must be itemized on Part V, Line 48.

### Line 28 — Total expenses

Sum of Lines 8 through 27a.

### Line 29 — Tentative profit or loss

Line 7 − Line 28.

### Line 30 — Business use of home

Either:
- **Simplified**: square footage (capped at 300) × $5. Max $1,500.
- **Regular**: from Form 8829.

This deduction cannot create or deepen a business loss. If Line 29 is negative or smaller than the home office calculation, the deduction is capped at the amount that brings Line 31 to zero. Any excess (regular method only) carries forward to next year.

See [`home-office.md`](./home-office.md).

### Line 31 — Net profit or loss

Line 29 − Line 30. **The bottom line.**

If positive: flows to Schedule 1 Line 3, Schedule SE if > $400, then Form 1040.

If negative: reduces other income on Form 1040, subject to:
- At-risk rules (Line 32)
- Hobby loss rules (IRC §183) if not for profit
- Passive activity rules if applicable (rare for solo)

### Line 32 — Loss limitation

If Line 31 is a loss:
- **32a** — All investment is at risk. Most solo filers (cash, no loans personally guaranteed by others). Loss is fully deductible (subject to other limits).
- **32b** — Some investment is not at risk. Attach Form 6198. Less common.

---

## Part III — Cost of Goods Sold (Lines 33-42)

See [`cogs.md`](./cogs.md).

## Part IV — Vehicle Information (Lines 43-47)

See [`vehicle.md`](./vehicle.md).

## Part V — Other Expenses (Line 48)

Itemized list of everything in Line 27a. Format:

| Description | Amount |
|-------------|--------|
| <name of expense> | <amount> |
| ... | ... |
| **Total** | <Line 27a> |

The IRS doesn't require receipts attached, but the user should retain them. The description should be specific enough to defend in audit ("Adobe Creative Cloud annual subscription" not "software").
