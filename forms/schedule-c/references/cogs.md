# Cost of Goods Sold (Schedule C Part III, Lines 33-42)

For product businesses only. Service businesses skip Part III entirely.

## Who completes Part III

A business completes Part III if any of these is true:
- It maintains inventory
- It manufactures, fabricates, or produces goods for sale
- It buys finished goods to resell

Examples that *do*: Etsy seller of handmade jewelry, Shopify store reselling phone cases, Amazon FBA business, food truck.

Examples that *don't*: graphic designer, consultant, rideshare driver, Airbnb host, freelance writer.

If the user is unsure, ask: "Do you own physical inventory at year-end?" If yes, Part III applies. If no, it doesn't.

## The COGS formula

```
COGS = Beginning Inventory
     + Purchases (Line 36)
     + Cost of Labor (Line 37)
     + Materials and Supplies (Line 38)
     + Other Costs (Line 39)
     − Ending Inventory
```

The total goes on Line 42 and flows back to Line 4 in Part I.

## Line-by-line

### Line 33 — Inventory method

| Method | When to pick |
|--------|--------------|
| Cost | Default for almost all small businesses. What you paid for inventory. |
| Lower of cost or market | Conservative; rarely used by solos |
| Other | Specify; almost never used |

### Line 34 — Did you change methods this year?

Almost always "No". A Yes triggers Form 3115 (Application for Change in Accounting Method).

### Line 35 — Beginning inventory

Carry forward last year's Line 41 (Ending inventory). First-year filers: enter 0.

### Line 36 — Purchases

Total inventory purchases during the year. Subtract any items withdrawn for personal use (e.g., the jewelry maker keeping a piece for herself).

### Line 37 — Cost of labor

Direct production labor for *employees*, not the owner. The owner's own labor on production is never deductible — it's a return on the business.

If the user has no production employees: 0.

### Line 38 — Materials and supplies

Raw materials and supplies that become part of finished products. Examples:
- Sterling silver for a jewelry maker
- Yarn for a knitter
- Ingredients for a bakery
- Components for an electronics assembler

If something is consumed but doesn't become part of the product, it goes on Schedule C Line 22 (Supplies) instead.

### Line 39 — Other costs

Other costs incurred to *produce* goods:
- Freight-in (cost to ship raw materials to you)
- Containers and packaging that become part of the product
- Shop supplies for production
- Manufacturing utilities (separately metered, if any)

Do NOT put here:
- Shipping out to customers (Line 8 advertising/Line 27a Other)
- Storage rent (Line 20b)
- Office supplies (Line 18)

### Line 40 — Total

Sum of Lines 35-39.

### Line 41 — Ending inventory

Value of inventory on hand at year-end. Three valuation choices (must match Line 33):
- **Cost** — what you paid (most common)
- **Lower of cost or market** — write down obsolete or impaired inventory
- **Other** — specify

The user must perform a year-end inventory count or use perpetual inventory records. Estimating is risky in audit.

### Line 42 — Cost of Goods Sold

Line 40 − Line 41. This number flows to Part I, Line 4.

## Worked example: Etsy jewelry seller

Maya makes silver jewelry. Her 2025 Schedule C COGS:

| Line | Item | Amount |
|------|------|--------|
| 33 | Inventory method | Cost |
| 34 | Changed methods | No |
| 35 | Beginning inventory (from last year's Line 41) | $1,200 |
| 36 | Purchases (silver, gemstones bought for resale or for kit-style products) | $4,800 |
| 37 | Cost of labor (Maya has no production employees) | $0 |
| 38 | Materials and supplies (silver wire, clasps, packaging that's part of the product) | $2,300 |
| 39 | Other costs (freight-in for raw silver, manufacturing tools < $2,500 each that wear out) | $450 |
| 40 | Total | $8,750 |
| 41 | Ending inventory (count on Dec 31) | $1,800 |
| 42 | COGS | **$6,950** |

Maya enters $6,950 on Line 4 of Part I.

## What goes in Part III vs Part II

This is the most-confused decision in Schedule C. Rules of thumb:

**Goes in Part III (COGS):**
- Materials that *become part of* the finished product
- Direct labor to *make* the product
- Costs to *bring inventory into existence* (freight-in)

**Goes in Part II (Operating expenses):**
- Costs to *run the business* but not make the product (rent, utilities, advertising)
- Materials *consumed by the business* but not part of the product (cleaning supplies, office paper)
- Shipping *out* to customers (Line 27a is the usual home — though some businesses split: outbound freight on Line 27a, postage stamps for letters on Line 18)
- Selling expenses (commissions on Line 10, marketing on Line 8)

When in doubt, ask: "Would the user have bought this if they made zero sales?" If yes, it's an operating expense (Part II). If the cost only exists because they made the product, it's COGS (Part III).

## UNICAP rules (IRC §263A)

Most small businesses are exempt under the IRC §263A(i) "small business taxpayer" exception (gross receipts ≤ $30M for 2025, indexed annually). Solo filers are virtually always exempt.

If the user has gross receipts > $30M and produces or resells goods, UNICAP rules require capitalizing more costs into inventory (e.g., a portion of indirect costs). That's a CPA-territory situation — don't try to handle it in this skill; flag it and recommend professional help.

## Inventory on hand: the audit risk

The IRS pays attention to ending inventory because it directly affects taxable income. If COGS is overstated, profit is understated, tax is lower. The mechanics:

```
Higher Ending Inventory → Lower COGS → Higher Profit → Higher Tax
Lower Ending Inventory → Higher COGS → Lower Profit → Lower Tax
```

The IRS does not love patterns where ending inventory shrinks year over year while gross receipts stay flat — that suggests inventory write-offs without sales. Year-end physical counts and dated photos are the user's defense.
