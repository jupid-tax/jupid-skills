# Example — Inventory Method Change from FIFO to LIFO

A small retailer wants to switch inventory accounting from FIFO to LIFO for tax savings during a period of rising costs. Files Form 3115 with DCN 21 (automatic) and Form 970 (LIFO election).

---

## Taxpayer facts

- **Entity**: Granite Hardware Co. (S-corp, EIN 12-7788990)
- **Calendar fiscal year**
- **Business**: brick-and-mortar hardware retailer with 1 location
- **Current method**: FIFO inventory accounting since founding in 2018
- **Inventory pools**: 4 pools (Tools, Plumbing, Electrical, General Hardware)
- **Beginning-of-year-of-change inventory** (January 1, 2026):
  - Tools: $180,000 (FIFO basis)
  - Plumbing: $95,000
  - Electrical: $110,000
  - General Hardware: $135,000
  - **Total**: $520,000

The owner observed inventory replacement costs rising ~6-8% per year over 2022-2025 due to industrial supply chain inflation. Management believes LIFO will produce a closer matching of current costs to current revenues, reducing reported income (and tax).

The change is for the **2026 tax year** (year of change).

---

## Why both Form 3115 AND Form 970

The LIFO election is a **two-document filing**:

1. **Form 970 — Application to Use LIFO Inventory Method** — the formal LIFO election. Filed with the tax return for the year of change.
2. **Form 3115 — DCN 21 (or sub-DCN 22, 23, 24)** — the accounting method change application. Filed in duplicate with the year-of-change return and a copy to Ogden.

A common mistake is filing only Form 970 (the election). Without Form 3115, the §481(a) implications are not addressed and the IRS may treat the change as procedurally invalid.

For a first-time LIFO election (FIFO → LIFO), both forms are required.

---

## DCN selection

Inventory method changes are covered by the **DCN 21 family** in Rev. Proc. 2024-23 (or successor). Sub-DCNs cover specific direction and method:

| Sub-DCN | Description |
|---------|-------------|
| 21 (general) | LIFO method changes |
| 22 | Adoption of LIFO from non-LIFO (the FIFO → LIFO case here) |
| 23 | Change between LIFO sub-methods (dollar-value vs specific-goods) |
| 24 | Termination of LIFO (LIFO → FIFO) |

For Granite (FIFO → LIFO adoption), the applicable sub-DCN is **22**. Verify the exact number against the current Rev. Proc.; the DCN 21 family has been renumbered across versions.

DCN 22 is **automatic consent** — no user fee. Filed in duplicate.

---

## §481(a) — the surprising part of LIFO adoption

For most inventory method changes, §481(a) captures the cumulative effect. **But for FIFO → LIFO adoption, §481(a) is generally ZERO**.

Why: the §481(a) computation compares cumulative correct (LIFO) vs cumulative actual (FIFO). For LIFO adoption, the IRS generally treats the **opening inventory at the start of the year of change as the LIFO base layer**. There is no cumulative recomputation back to inception.

```
LIFO base layer (Jan 1, 2026) = FIFO ending inventory at Dec 31, 2025
                              = $520,000

§481(a) = $0 (no retroactive recomputation)
```

This is the **§472(d) base-year rule**: when adopting LIFO, the prior-method ending inventory becomes the LIFO base layer at base-year prices. There's no §481(a) catch-up because the base-year inventory IS the cumulative-effect anchor.

### Subsequent years — LIFO reserves

After adoption, each year:
- Compute current-year inventory at current prices (current cost)
- Compute current-year inventory at base-year prices (using a price index)
- The difference = LIFO reserve = additional COGS deduction (when prices rise)

The LIFO reserve grows over time as long as prices keep rising. This is the tax benefit of LIFO during inflationary periods.

### Worked example for 2026 (year 1 of LIFO)

Assume year-end 2026:
- Inventory at current cost: $560,000
- Inventory at base-year cost (using BLS Producer Price Index for hardware retailers, applied to base-year items): $530,000
- LIFO reserve at year-end: $560,000 − $530,000 = $30,000
- Compared to year-start LIFO reserve: $0
- LIFO reserve change for 2026: +$30,000

Under FIFO, ending inventory would have been $560,000.
Under LIFO, ending inventory is $530,000.
Difference: $30,000 = additional COGS deduction in 2026 = **$30,000 reduction in 2026 taxable income**.

---

## Form 3115 — Part I

| Line | Field | Value |
|------|-------|-------|
| 1a | Name of filer | Granite Hardware Co. |
| 1b | EIN | 12-7788990 |
| 2 | Tax year of change | January 1, 2026 – December 31, 2026 |
| 3 | Type of return | Form 1120-S |
| 4 | Type of accounting method change | Inventory (FIFO → LIFO adoption) |
| 5 | DCN | 22 (verify in current Rev. Proc.) |
| 6 | Section 481(a) adjustment | $0 (per §472(d) base-year rule) |
| 7 | Spread | N/A (no §481(a) to spread) |

---

## Form 3115 — Schedule D (inventory)

Schedule D of Form 3115 is the inventory-specific schedule. Entries:

| Field | Value |
|-------|-------|
| Old method | FIFO (first-in, first-out) |
| New method | LIFO (dollar-value method, double-extension or link-chain — specify) |
| LIFO sub-method | Dollar-value LIFO |
| Index method | External index (BLS Producer Price Index for hardware retailers) — verify exact PPI table |
| Pools | 4 pools as listed (Tools, Plumbing, Electrical, General Hardware) |
| Base year | 2026 (year of change becomes the LIFO base year) |
| Citation | IRC §472, §473, §474 (LIFO) |

---

## Form 970 — Application to Use LIFO

Form 970 is filed alongside the 2026 return and Form 3115. Required entries:

| Section | Field | Value |
|---------|-------|-------|
| Part I | Type of LIFO method | Dollar-value LIFO |
| | Sub-method | Double-extension method |
| | Index method | External index (PPI by industry) |
| | First year of LIFO | 2026 |
| | Base year | 2026 (the LIFO inventory at the start of the year is the base layer) |
| | LIFO pools | 4 pools as listed |
| Part II | Inventory cost flow | LIFO consistently for all financial reporting (book-tax conformity required under §472(c)) |

The **§472(c) book-tax conformity rule** is critical: a taxpayer using LIFO for tax must also use LIFO for **financial reporting** (audited / reviewed financial statements, lender financial reports, owner financial reports). This is a major commitment — Granite's CFO confirms the company will adopt LIFO for both books and tax.

---

## Filing logistics

| Task | Date | Detail |
|------|------|--------|
| Year of change | 2026 | Calendar tax year |
| Form 970 prepared and signed | with 2026 return | |
| Form 3115 prepared (in duplicate) | with 2026 return | DCN 22 |
| Duplicate Form 3115 to Ogden | before/with return filing | Certified mail with return receipt |
| Original Form 3115 + Form 970 attached to 1120-S 2026 | by return due date | Including extensions, latest September 15, 2027 |
| First LIFO computation done | year-end 2026 | LIFO reserve as of Dec 31, 2026 |
| 2026 income statement uses LIFO | book and tax | §472(c) conformity |

---

## Going forward — annual LIFO maintenance

Each year after adoption:
1. **Compute current-year ending inventory at current cost** (standard valuation)
2. **Compute price index** vs base year (using PPI or internal index — must be consistent year over year)
3. **Compute base-cost equivalent inventory** = current-cost inventory ÷ current price index
4. **Compute LIFO layers**: any incremental quantity in current year vs prior year is added at current-year prices; any decrement removes prior-year layers (LIFO liquidation — risk of reversing tax benefits)
5. **Track LIFO reserve**: difference between FIFO-equivalent and LIFO inventory; disclosed on financial statements per ASC 330

The LIFO reserve grows during inflation and shrinks during deflation or inventory liquidations.

---

## Common errors avoided

1. **Filing only Form 970 without Form 3115**: technically Form 970 is the LIFO election, but the IRS expects Form 3115 (DCN 22) to accompany. Without it, the change may be procedurally questioned.
2. **Missing the §472(c) book-tax conformity**: a LIFO tax election requires LIFO on the books. If the lender or auditor demands FIFO, the LIFO election is invalid for tax.
3. **Computing §481(a) catch-up**: a common error — §481(a) is generally $0 for FIFO → LIFO adoption per the §472(d) base-year rule. The opening inventory at start of year of change IS the LIFO base layer.
4. **Wrong pool definition**: pools should be defined by natural business classification (e.g., 4 product departments here). Re-pooling later is itself a method change requiring Form 3115.
5. **LIFO liquidation in subsequent years**: if Granite reduces inventory below base-year quantity, prior LIFO layers are "liquidated" at low historical costs, releasing low-COGS inventory and triggering income recognition. Watch for this in years when Granite reduces stock or experiences deflation.
6. **Ignoring AMT and state implications**: LIFO is allowed for federal regular tax but is disallowed for several state tax computations (e.g., some states require FIFO for state tax). Track book-tax differences carefully.

---

## When LIFO is a bad idea

Granite should reconsider LIFO if:
- Industry trend is **deflationary** (LIFO produces higher tax than FIFO when prices fall)
- Inventory levels are **shrinking** (LIFO liquidation triggers reversal of prior tax benefits)
- The business is **about to be sold** (LIFO reserves become recapture income at sale)
- Lenders or franchisors **require GAAP-FIFO** financial reporting (§472(c) violation)
- The taxpayer is in a **low-tax-bracket year** (deferred deduction is less valuable)

For Granite with rising costs and stable inventory growth, LIFO is a reasonable choice. Re-evaluate annually.

---

## Output for the user

The agent delivers to Granite's owner:

1. **Form 3115 draft** (Parts I, IV, Schedule D) for DCN 22
2. **Form 970 draft** for the formal LIFO election
3. **§481(a) attachment**: explains why §481(a) = $0 per §472(d) base-year rule
4. **Pool structure**: 4 pools defined with the inventory categorizations
5. **Index methodology**: external PPI source and computation steps
6. **Filing checklist**: dual filing (Form 3115 in duplicate + Form 970 with return)
7. **Annual maintenance plan**: year-end LIFO reserve computation, conformity confirmation, watch for LIFO liquidations
8. **Risk flag**: §472(c) book-tax conformity is mandatory — confirm with banker / auditor before filing
