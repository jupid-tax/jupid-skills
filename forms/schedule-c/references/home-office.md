# Home Office Deduction (Schedule C Line 30)

The deduction for the business use of the user's home. Two methods: simplified or regular (Form 8829).

## Eligibility — both methods

The home office must meet **both** of:

1. **Regular and exclusive use** of a specific area for business. "Exclusive" is strict: the IRS does not recognize a home office that doubles as a guest room, gym, or family computer station.
2. **Principal place of business** OR a place where the user meets clients OR a separate structure (detached studio, barn) used for business.

The bar is high. A common failure: a freelancer with a desk in the corner of the living room. The room serves multiple purposes, so it's not exclusive. No deduction.

A laptop on the kitchen table while the rest of the family eats? Definitely not exclusive.

A converted garage used only for the business? Exclusive — qualifies.

## When the home office disqualifies

The user must operate as a sole proprietor or single-member LLC. Employees can no longer deduct home office expenses (TCJA eliminated unreimbursed employee business expenses through 2025; check status for 2026).

Also disqualifying:
- Renting the space *to* the employer (special anti-abuse rules)
- Using the space < 50% of the time on average (not a hard rule, but the IRS gets suspicious)

## Method 1 — Simplified

The fast path. Multiply the square footage of the home office by $5, capped at 300 sq ft.

```
Deduction = min(home_office_sqft, 300) × $5
Maximum   = $1,500
```

Pros:
- One line on Line 30. No Form 8829.
- No depreciation = no recapture risk when the home is sold
- No need to track utility bills, insurance, etc.

Cons:
- Capped at $1,500 even if actual expenses are much higher
- No carryforward if the deduction would create a loss (regular method has carryforward)

When to pick simplified:
- Office < 300 sq ft
- Modest actual expenses
- User wants minimal record-keeping
- User plans to sell the home soon and wants no depreciation recapture

## Method 2 — Regular (Form 8829)

Compute the actual home expenses, multiply by the business-use percentage, deduct.

### Business-use percentage

```
Business % = home_office_sqft / total_home_sqft
```

A 200 sq ft office in a 2,000 sq ft home = 10%.

### Eligible expenses

Direct expenses (only the office area): 100% deductible.
- Painting the home office walls
- Repairs only inside the office

Indirect expenses (whole home): deductible at the business-use %.
- Mortgage interest or rent
- Property tax
- Utilities (electric, gas, water, garbage)
- Homeowners insurance
- Depreciation (homeowners only — see below)
- Whole-home repairs (roof, HVAC service for the entire home)

Unrelated expenses (other parts of the home): 0% deductible.
- Lawn care (unless office is a separate structure)
- Painting a non-office room

### Depreciation — homeowners only

Home depreciation: building basis (excluding land) ÷ 39 years × business-use %.

Example:
- Home cost: $400,000 (basis)
- Land portion: $80,000 (not depreciable)
- Building basis: $320,000
- Business %: 10%
- Annual depreciation: $320,000 × 10% / 39 = $821

Recapture trap: when the user sells the home, the depreciation taken creates Section 1250 unrecaptured gain, taxed at 25%. The exclusion under IRC §121 ($250k single / $500k MFJ) does not cover this depreciation recapture. Many filers take the deduction, then are surprised by the recapture bill at sale.

For renters, no depreciation — just deduct the business-use % of rent.

### The income limit

Like Section 179, the home office deduction (regular method) cannot create or deepen a business loss. Excess carries forward to next year. Form 8829 has a worksheet for this.

Simplified method has no carryforward. If the deduction exceeds Line 29, it's capped at Line 29 and the excess is lost.

### When to pick regular

- Office is large (>300 sq ft makes simplified unattractive)
- Actual expenses are high (high mortgage, high utilities)
- Renter (no depreciation recapture concern)
- User has a multi-year plan and wants carryforward

### Form 8829 mechanics

The skill should produce both: a simplified-method calculation and a regular-method calculation, then let the user pick. If the user already has Form 8829 done, use that number.

Worked simplified example:

```
Home office: 240 sq ft (within the 300 cap)
240 × $5 = $1,200

Schedule C Line 30: $1,200
```

Worked regular example (renter):

```
Office: 200 sq ft / Home: 1,500 sq ft → 13.33% business use

Annual rent: $24,000          → $24,000 × 13.33% = $3,200
Renter's insurance: $300      → $300 × 13.33% = $40
Electric: $1,800              → $1,800 × 13.33% = $240
Internet: $720 (50% biz use)* → $720 × 50% × 13.33% = $48 (* internet is split twice: business % then home-office %)
                                Actually for internet, simpler: deduct business-use % of internet on Line 27a directly,
                                not through Form 8829. Pick one or the other; don't double-count.

Schedule C Line 30: ~$3,480 (rent + insurance + utilities; no depreciation as renter)
```

## Choosing simplified vs regular

| If... | Pick |
|-------|------|
| Office ≤ 300 sq ft and actual expenses < $5/sq ft | Simplified |
| Office > 300 sq ft | Regular |
| User is a homeowner with $100K+ home and actual expenses > $1,500 | Regular (despite recapture) |
| User plans to sell within 2 years and is a homeowner | Simplified (avoid recapture) |
| User is a renter with high rent | Regular |
| User wants minimum paperwork | Simplified |

## Year-to-year switching

The user can switch methods year over year. There's no irrevocability. But:

- Switching from regular to simplified: any prior-year depreciation is "frozen" — it stays in the basis and recaptures at sale, but no current-year impact
- Switching from simplified to regular: ordinary; just compute the new number on Form 8829

## What's NOT inside Line 30

Don't double-count items already inside Line 30 elsewhere:

- Utilities for the home office → inside Line 30 (or Form 8829)
- A separate business location's utilities → Line 25
- Office rent for a separate location (not home) → Line 20b

Also: if the user has employees who work at the home office, that's still fine for the home office deduction (the user owns the business). But the employees' wages and benefits go on the normal Schedule C lines, not Line 30.
