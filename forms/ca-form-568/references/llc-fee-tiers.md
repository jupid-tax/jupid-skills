# LLC Fee Tiers (R&TC §17942)

The California LLC fee is **separate from the $800 annual tax** and is owed in addition to it. The fee is tiered based on the LLC's "total income from all sources derived from or attributable to this state" (R&TC §17942(b)(1)), computed on Schedule IW and entered on Form 568, Side 1, line 1.

---

## The tier table

From the 2025 Form 568 Booklet, General Information F (https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf), and R&TC §17942(a):

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

R&TC §17942(b)(1)(A) defines "total income from all sources derived from or attributable to this state" as:

> gross income, as defined in Section 24271, plus the cost of goods sold that are paid or incurred in connection with the trade or business of the taxpayer.

In other words: **gross receipts** — *not* gross profit. COGS is **not** subtracted for fee purposes (it's added back in). On Schedule IW this is why line 1a (Schedule B gross profit) is paired with line 1b (cost of goods sold), and line 2a with line 2b.

Example. A reseller has:
- Gross receipts: $480,000
- COGS: $300,000
- Gross profit: $180,000

Gross profit (federal Form 1065, line 3) is $180,000.
For California §17942 fee purposes, "Total Income" is $480,000 → puts the LLC in the $250K-$499,999 tier ($900 fee).

If the same LLC had $520,000 gross receipts and $300,000 COGS, "Total Income" is $520,000 → $2,500 fee tier.

---

## Sourcing for multi-state LLCs

If the LLC has activity or customers outside California, only income **assigned to California** counts toward the fee tier. The assignment is item by item, using the rules for assigning sales under R&TC §§25135 and 25136 (R&TC §17942(b)(1)(B); 2025 booklet, Schedule IW instructions) — not a single apportionment percentage applied to everything:

- Services: California to the extent the purchaser receives the benefit in California (market assignment, R&TC §25136)
- Intangibles: where used; marketable securities: where the customer is
- Tangible personal property: delivered or shipped to a purchaser in California (destination); goods shipped from a California location are also assigned to California unless the seller is taxable in the destination state (2025 booklet, Schedule IW instructions)
- Sale, lease, rental of real property and rental of tangible property: where the property is located
- Industry-specific rules under R&TC §25137 apply where relevant (redirect to a CPA)

Example. A consulting LLC has $1,200,000 of service revenue; customers receiving the benefit in California paid $400,000 and out-of-state customers paid $800,000.

```
Schedule IW receipts assigned to California = $400,000
```

Tier: $250K-$499,999 → $900 fee. Even though total revenue is $1.2M, only the California-assigned receipts drive the fee. (Schedule R, the separate income-apportionment schedule, uses a single sales factor under R&TC §25128.7; it does not replace the item-by-item Schedule IW assignment.)

---

## Exclusions and aggregation (§17942(b))

- **Excluded**: allocations, attributions, or distributions of income or gain an LLC receives as a member of another LLC, to the extent attributable to income already subject to the LLC fee (R&TC §17942(b)(1)(A); booklet: "Do not include any income on the worksheet that has already been subject to the LLC fee").
- **Aggregation**: if the FTB determines that commonly controlled LLCs (same persons owning more than 50% of capital or profits) were formed primarily to reduce the fee, it may compute the fee on the group's combined total income, with joint and several liability (R&TC §17942(b)(2); booklet, General Information F).

The exclusion matters for tiered LLC structures; for most operating LLCs, neither applies.

---

## Tier boundary edge cases

When an LLC is close to a tier boundary, surface the risk:

| Situation | Risk |
|-----------|------|
| Schedule IW Total = $249,500 | One more invoice in the year pushes into $900 tier |
| Schedule IW Total = $499,800 | One more invoice pushes from $900 to $2,500 ($1,600 jump) |
| Schedule IW Total = $999,500 | One more invoice pushes from $2,500 to $6,000 ($3,500 jump) |
| Schedule IW Total = $4,999,500 | One more invoice pushes from $6,000 to $11,790 ($5,790 jump) |

The LLC fee is an **annual** computation — the tier is based on full-year totals. A 6th-month estimate (FTB 3536) at least equal to the prior-year fee avoids the penalty even if the LLC grows through a boundary; the balance is then due by the return's original due date (see below).

---

## Estimated fee underpayment penalty (§17942(d)(2))

The estimate is due by the 15th day of the 6th month of the taxable year (R&TC §17942(d)(1)). If the amount paid by that date is less than the fee for the year:

```
Penalty = 10% × (fee for the year − amount paid by the 6th-month date)
```

**Safe harbor**: no penalty if the amount paid by the 6th-month date is equal to or greater than the LLC's total fee for the **preceding** taxable year (R&TC §17942(d)(2); 2025 FTB 3536 instructions). This is a flat 10%, not a per-month accumulation. Any fee not paid as a timely estimate is still due by the original due date of the return, on FTB 3536; paying it late adds the late-payment penalty and interest from that date.

Example 1. Prior-year fee $900. The LLC paid $900 with FTB 3536 in June; the year ends in the $2,500 tier. Paid ≥ prior-year fee → **no penalty**. The $1,600 balance is due by the return's original due date.

Example 2. Prior-year fee $2,500. The LLC paid $900 in June; the year ends in the $2,500 tier. $900 < $2,500 prior-year fee → penalty = 10% × ($2,500 − $900) = **$160**.

Example 3. The LLC paid nothing in June and its prior-year fee was $900; the year's fee is $2,500 → penalty = 10% × $2,500 = **$250**.

To avoid the penalty, pay at least the prior-year fee by the 6th-month date. If the LLC had no preceding taxable year, there is no prior-year amount to compare; estimate the current-year fee. All fee payments go on Form 568, Side 1, line 8; any excess becomes the line 17 overpayment.

---

## When the fee does NOT apply

The fee is **$0** if any of these is true:

- Schedule IW line 17 is under $250,000, in any year (the $800 annual tax still applies)
- The LLC claims the deployed-military exemption (enter $0 on lines 2 and 3; 2025 booklet, General Information F)
- The LLC is a tax-exempt title-holding company treated as a partnership or disregarded entity (excluded from the LLC definition; 2025 booklet, General Information F)
- The LLC elected to be taxed as a corporation or S corporation federally (it files Form 100 / 100S, not Form 568; California follows the federal election)

---

## Citation summary

- R&TC §17942(a)(1)-(4) — the tiered fee amounts
- R&TC §17942(b)(1)(A) — definition of total income; exclusion of income already subject to the fee
- R&TC §17942(b)(1)(B) — assignment using R&TC §§25135–25136
- R&TC §17942(b)(2) — commonly controlled LLCs
- R&TC §17942(c) — fee due with the return
- R&TC §17942(d) — 6th-month estimate and 10% underpayment penalty with prior-year safe harbor
- R&TC §25128.7 — single-sales-factor apportionment (Schedule R)
- R&TC §25136 — market assignment for services and intangibles

The fee amounts are set by statute (last amended by Stats. 2008, ch. 763), not by inflation indexing. If the legislature changes them, the FTB updates the Form 568 booklet.
