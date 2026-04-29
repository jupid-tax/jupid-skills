# California Form 568 Line-by-Line Reference

Complete lookup for every line on Form 568, Schedule IW, Schedule K (568), Schedule T, and the supporting schedules. Use this when the agent needs to confirm where a value belongs or what a line means. Line numbers below are from the 2024 Form 568 booklet; verify against the 2025 booklet at <https://www.ftb.ca.gov/forms/> before filing.

---

## Form 568 Side 1 — Header (LLC identification)

| Field | What goes here | Notes |
|-------|----------------|-------|
| (top, left) | LLC legal name | Exactly as registered with California SOS — abbreviations matter |
| (top, right) | Federal EIN | 9 digits with dash (XX-XXXXXXX) |
| A | California SOS file number | 12 digits, starts with `2` for LLCs (e.g., `201234567890`). LP / GP entities have different prefixes. |
| B | (printed) Federal EIN field | Same as top-right |
| C | Principal business activity (PBA) | Plain English: "Real estate rental", "Software consulting", "Cannabis cultivation" |
| D | Principal product/service | Specific: "Residential rental properties", "SaaS subscription software" |
| E | Date business started in California | First date the LLC had California nexus, not necessarily formation date |
| F | Total assets at end of year | From federal Schedule L, Line 14 (column d), if Schedule L is filed; otherwise leave blank |
| G | (printed) Sales | From federal Schedule K Line 1c (gross receipts less returns) |
| H | Boxes — check applicable | Initial return / Final return / Amended return / Single-member LLC / Protective claim / Election to be taxed as corporation in CA |
| I | Number of members | 1 for SMLLC, 2+ for multi-member |
| J | Effective date of federal classification election | Only if the LLC filed federal Form 8832 to elect a non-default classification |

Critical: if the user marks "Final return" but has not filed **Form LLC-3 (Certificate of Dissolution)** and **Form LLC-4/7 (Certificate of Cancellation)** with the California Secretary of State, the LLC remains "active" with SOS and will accrue another $800 annual tax next year. Check this before declaring final.

---

## Form 568 Side 1 — Tax and Fee

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 1 | Total income from Schedule IW | Schedule IW total — California-source gross receipts | Federal gross receipts (those are on Schedule K Line 1c) |
| 2 | Limited liability company fee | LLC fee from §17942 tier table; see [`llc-fee-tiers.md`](./llc-fee-tiers.md) | The $800 (that's Line 3) |
| 3 | 2024 (or 2025) annual LLC tax | $800 — fixed per §17941 | The fee (that's Line 2) |
| 4 | Nonconsenting nonresident members' tax | From Schedule T; see [`nonresident-members.md`](./nonresident-members.md) | Withholding for consenting nonresidents (no withholding owed if Form 3832 signed) |
| 5 | Partnership level tax (PLT) | Rare; only if FTB assessed a partnership-level tax in a prior audit | Standard income tax (LLCs are pass-through, not corporate) |
| 6 | Total tax and fee | Line 2 + 3 + 4 + 5 | |
| 7 | Form 3522 (annual tax) prepayment | The $800 already paid via Form 3522 voucher in 4th month | Form 3536 (that's Line 8) |
| 8 | Form 3536 (estimated fee) prepayment | The estimated fee paid in 6th month | Form 3522 (that's Line 7) |
| 9 | Withholding | California source withholding (from Forms 592-B / 593) | Federal withholding |
| 10 | 2024 overpayment applied to 2025 | Refund from prior year's 568 the user elected to apply | New payments |
| 11 | Total payments | Sum of Lines 7-10 | |
| 12 | Tax/fee due (or overpayment) | Line 6 − Line 11 | |
| 13-17 | Penalty, interest, refund mechanics | Late filing / late payment / underestimation | |

**Critical rule for Line 1**: Schedule IW Total Income is **not** the same as federal Line 1c. It includes specific California-source items per §17942 — see [`llc-fee-tiers.md`](./llc-fee-tiers.md). For single-state, single-source LLCs, they often coincide; for multi-state LLCs, Schedule IW reflects only California's apportioned share.

---

## Schedule IW — Limited Liability Company Income Worksheet

This worksheet computes Form 568 Line 1 (Total Income) for the LLC fee. It is California-specific.

| Line | Field | What goes here |
|------|-------|----------------|
| 1 | Total gross receipts | All revenue from CA-source business activity, before any deductions |
| 2 | Cost of goods sold | CA-source COGS (mirrors federal Schedule A of 1065 or the equivalent Schedule C COGS) |
| 3 | Subtract Line 2 from Line 1 | Gross profit |
| 4 | Other income | Interest, dividends, rents, royalties from CA sources; gains from disposition of CA-source assets |
| 5-6 | Adjustments | Specific California-source income or losses |
| 7 | Total income | Sum → flows to Form 568 Line 1 |

For SMLLCs that are single-state, single-source: Schedule IW Line 1 typically equals federal Schedule C Line 1 (Gross receipts). For multi-state LLCs, apply Schedule R apportionment first and use the California share.

**Common error**: Including out-of-state income in Schedule IW. Only California-source income counts toward the LLC fee tier. A delivery business that hauls goods through 5 states only counts the California portion.

---

## Schedule K (568) — Partners' Distributive Share Items

Required for multi-member LLCs (partnership-classified). Mirrors federal Form 1065 Schedule K with California adjustments. Line numbers parallel federal.

Key California adjustments versus federal:

| Federal item | California adjustment |
|--------------|----------------------|
| §168(k) bonus depreciation | California does not conform; full add-back required |
| §179 deduction | California cap is $25,000 (not federal's $1.25M); excess is depreciated under MACRS |
| State tax refunds from other states | Generally taxable in California (no state-tax-refund exclusion) |
| Charitable contributions | Mostly conforms; some limits differ |
| §199A QBI deduction | California does not conform; LLC reports as if §199A didn't exist |
| Domestic production activities | California has different rules |

For full California adjustments, see [`california-adjustments.md`](./california-adjustments.md).

---

## Schedule K-1 (568) — Member's Share of Income, Deductions, Credits

One per member. Each shows that member's distributable share of every Schedule K (568) line, plus their California-source share if the LLC has out-of-state activity.

Required member info on the K-1:
- Name
- SSN / ITIN / EIN (depending on member type — individual / single-member LLC / corporation)
- Address
- Ownership % at end of year
- Profit/loss/capital % (if different)
- California residency status
- Whether Form 3832 was signed (drives nonresident withholding)

---

## Schedule L — Balance Sheet

Required if **total receipts ≥ $250,000** OR **total assets ≥ $1,000,000** at year-end. Mirrors federal Schedule L.

For smaller LLCs, leave blank — it's not required.

---

## Schedule M-1 — Reconciliation of Income (Loss) per Books With Income (Loss) per Return

Required with Schedule L. Reconciles book income to taxable income, accounting for items deducted on books but not on the return (M&E nondeductible portion, federal income tax on books, etc.).

---

## Schedule M-2 — Analysis of Members' Capital Accounts

Required with Schedule L. Tracks each member's capital account: beginning balance + contributions + share of income − distributions − share of loss = ending balance.

---

## Schedule T — Nonconsenting Nonresident Members' Tax

For each nonresident member who did **not** sign Form 3832 (consent to California jurisdiction). The LLC computes tax on their distributable California-source income.

| Column | What goes here |
|--------|----------------|
| Member name | |
| Tax ID | SSN / ITIN / EIN |
| Distributable CA-source share | From Schedule K-1 (568) |
| Rate | 12.3% (individual) or 8.84% (corporation) |
| Tax | Share × rate |

Sum of Schedule T total → Form 568 Line 4.

This is a **liability of the LLC**, not the member. The LLC pays it directly. The member can claim a credit for it on their California nonresident return (Form 540NR).

---

## Schedule R — Apportionment

For multi-state LLCs only. California uses a single-sales-factor formula post-2013 (R&TC §25128.7):

```
California apportionment % = California sales / Total sales (everywhere)
```

Apply this percentage to:
- Form 568 Line 1 (Total Income) — but only the California-source portion counts
- Schedule K-1 (568) per member — California-source share

For LLCs with both California and non-California members, this gets complex; see [`apportionment.md`](./apportionment.md). Out of scope for this skill: complex multistate situations with three-factor election or non-standard sourcing — redirect to a CPA.

---

## Side 6 — Schedule O (Amounts from Liquidation, etc.)

Used for the year an LLC dissolves. Reports gain/loss from liquidating distributions. Out of scope unless user is dissolving the LLC.

---

## Where common items go (quick lookup)

| Item | Where on Form 568 |
|------|-------------------|
| $800 annual LLC tax owed | Line 3 |
| LLC fee owed (tiered) | Line 2 |
| $800 already paid via Form 3522 | Line 7 (credit) |
| Estimated fee paid via Form 3536 | Line 8 (credit) |
| Nonresident member tax (didn't sign 3832) | Line 4 (via Schedule T) |
| Federal §168(k) bonus depreciation | Schedule K + add-back line (CA does not conform) |
| Federal §179 over $25K | Schedule K + add-back; rest depreciated under MACRS |
| Member's CA-source share | Schedule K-1 (568) per member |
| Nonresident member who signed Form 3832 | Attach Form 3832; no withholding |
| Multi-state apportionment | Schedule R |
| LLC fee tier boundary issue | Recompute Schedule IW carefully |
