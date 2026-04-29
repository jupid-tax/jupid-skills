# LLC Fee Tiers (R&TC §17942)

The California LLC fee is **separate from the $800 annual tax** and is owed in addition to it. The fee is tiered based on the LLC's "Total Income" (a California-specific concept defined in R&TC §17942(b)).

---

## The tier table

From the 2024 Form 568 booklet (verify against 2025 booklet at <https://www.ftb.ca.gov/forms/> before filing):

| Schedule IW Total Income | LLC fee | Code section |
|--------------------------|---------|---------------|
| Less than $250,000 | $0 | §17942(a) |
| $250,000 – $499,999 | $900 | §17942(a)(1) |
| $500,000 – $999,999 | $2,500 | §17942(a)(2) |
| $1,000,000 – $4,999,999 | $6,000 | §17942(a)(3) |
| $5,000,000 or more | $11,790 | §17942(a)(4) |

The fee is **flat within each tier** — an LLC at $499,999 owes $900; at $500,000 it jumps to $2,500. This creates a $1,600 cliff. An LLC near a tier boundary should be careful about Schedule IW computation.

---

## What "Total Income" means under §17942

R&TC §17942(b) defines "Total Income" for the fee as:

> Gross income, plus the cost of goods sold that are paid or incurred in connection with the trade or business of the taxpayer.

In other words: **gross receipts** — *not* gross profit. COGS is **not** subtracted for fee purposes (it's added back in). This is different from the federal definition of "gross income" used for Form 1065.

Example. A reseller has:
- Gross receipts: $480,000
- COGS: $300,000
- Gross profit: $180,000

For federal purposes, gross income on Form 1065 is $180,000.
For California §17942 fee purposes, "Total Income" is $480,000 → puts the LLC in the $250K-$499,999 tier ($900 fee).

If the same LLC had $520,000 gross receipts and $300,000 COGS, "Total Income" is $520,000 → $2,500 fee tier.

---

## Apportionment for multi-state LLCs

If the LLC has activity outside California, only the **California-apportioned share** of total income counts toward the fee tier.

Apportionment formula (post-2013, single-sales-factor, R&TC §25128.7):

```
California % = California sales / Total sales (everywhere)
California Total Income = California % × Total Income
```

Example. An LLC has $1,200,000 total revenue, of which $400,000 is from California customers and $800,000 is from out-of-state.

```
California % = 400,000 / 1,200,000 = 33.3%
California Total Income = 33.3% × 1,200,000 = $400,000
```

Tier: $250K-$499,999 → $900 fee. Even though total revenue is $1.2M, only the California portion drives the fee.

For LLCs with out-of-state services, sourcing rules matter — the California sales factor uses **market-based sourcing** (where the customer receives the benefit) per R&TC §25136(b). For tangible personal property, sourcing is destination-based (where shipped). For services, it's where the customer receives the service.

---

## Exclusions from "Total Income" (§17942(b)(2))

Some income items are **excluded** from Total Income for fee purposes even though they're included for income tax purposes:

- Income from intercompany transactions between the LLC and its members (to prevent double-counting)
- Specific items that would otherwise be double-taxed

This is narrow. For most operating LLCs, it doesn't apply.

---

## Tier boundary edge cases

When an LLC is close to a tier boundary, surface the risk:

| Situation | Risk |
|-----------|------|
| Schedule IW Total = $249,500 | One more invoice in the year pushes into $900 tier |
| Schedule IW Total = $499,800 | One more invoice pushes from $900 to $2,500 ($1,600 jump) |
| Schedule IW Total = $999,500 | One more invoice pushes from $2,500 to $6,000 ($3,500 jump) |
| Schedule IW Total = $4,999,500 | One more invoice pushes from $6,000 to $11,790 ($5,790 jump) |

The LLC fee is an **annual** computation — the tier is based on full-year totals. Mid-year estimates (Form 3536) should err toward the higher tier if the LLC is growing through a boundary.

---

## Estimated fee underpayment penalty (§17942(d))

If the Form 3536 estimated payment is **less than 90% of the actual fee owed** (i.e., underpaid by more than 10%), a penalty applies:

```
Penalty = 10% × (actual fee − amount paid by 6th-month deadline)
```

This is a flat 10%, not a percentage-per-month accumulation. It can be waived in narrow "reasonable cause" situations (rare; documented in §17942(d)(2)).

Example. LLC paid $900 via Form 3536 in June, but actual year-end fee turns out to be $2,500 (LLC crossed $500K). Underpayment = $2,500 − $900 = $1,600. 10% × $1,600 = **$160 penalty**.

To avoid this, when an LLC's growth is uncertain, estimate at the next-higher tier even if it means overpaying. Overpayments are credited on Form 568 Line 8 against the actual fee, and any excess flows through Line 12 as a refund or applied to next year.

---

## When the fee does NOT apply

The fee is **$0** if any of these is true:

- LLC is in its first year and Schedule IW Total Income < $250,000 (the $800 still applies for 2024+; no AB-85 first-year fee waiver beyond the boundary)
- LLC has no California-source activity (then no Form 568 is required at all)
- LLC has elected to be taxed as a corporation federally and California (Form 100 / 100S, not Form 568)
- LLC is a single-member LLC owned by a tax-exempt entity (special rules; rare)

---

## Citation summary

- R&TC §17942(a)(1)-(4) — the tiered fee amounts
- R&TC §17942(b) — definition of "Total Income"
- R&TC §17942(b)(2) — exclusions
- R&TC §17942(d) — underestimation penalty
- R&TC §25128.7 — single-sales-factor apportionment
- R&TC §25136(b) — market-based sourcing for services

The exact fee amounts are set by statute and revised by the legislature, not by inflation indexing. They have been stable since 2007 ($900 / $2,500 / $6,000 / $11,790). If the legislature changes them, the FTB updates the Form 568 booklet.
