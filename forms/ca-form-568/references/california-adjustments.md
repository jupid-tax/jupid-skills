# California Federal-to-State Adjustments

California does not fully conform to federal tax law. For taxable years beginning on or after January 1, 2025, California conforms to the IRC as of January 1, 2025, with modifications (SB 711), and in general does not conform to the One Big Beautiful Bill Act (2025 Form 568 Booklet, What's New and General Information A). Several federal items must be adjusted on Form 568 (and Schedule K-1 (568) per member). This reference catalogs the most common adjustments.

The agent's job: take the federal Schedule K (from federal Form 1065 or the federal Schedule C/E for SMLLCs), apply the California-specific adjustments, and report the adjusted numbers on Form 568 Schedule K (568) and the member K-1s.

---

## Depreciation and §179

### Bonus depreciation (§168(k))

| Federal | California |
|---------|-----------|
| 100% bonus depreciation for qualified property acquired after January 19, 2025 (OBBBA; 2025 Instructions for Form 4562) | **California does NOT conform** to §168(k) (2025 FTB 3885L). Recompute depreciation on FTB 3885L. |

Mechanic: federal Form 4562 may show, e.g., $50,000 of 100% bonus depreciation on a $50,000 piece of equipment. On California, the LLC depreciates the same equipment under MACRS at the regular recovery period (5- or 7-year for most equipment). Year 1 California deduction is much smaller — first-year MACRS half-year convention on a 5-year asset is 20%, so $10,000 instead of $50,000.

The $40,000 difference becomes an **adjustment** on Schedule K (568) — added back to California taxable income.

In subsequent years, California allows MACRS depreciation while federal has already deducted everything → California gets a deduction federal doesn't.

### Section 179

| Federal | California |
|---------|-----------|
| 2025 limit: $2,500,000, reduced above $4,000,000 of §179 property (OBBBA; 2025 Instructions for Form 4562) | **California limit: $25,000**, reduced above $200,000 (2025 FTB 3885L, lines 1 and 3; R&TC §17255) |

If the federal §179 deduction exceeds $25,000, the excess must be depreciated under MACRS for California purposes.

Example. LLC bought $100,000 of equipment, elected federal §179 = $100,000. California §179 limit = $25,000. The remaining $75,000 must be depreciated under MACRS for California — at 5-year, 20% Year 1, $15,000. So California deduction Year 1 = $25,000 + $15,000 = $40,000, vs. federal $100,000.

Add-back on Schedule K (568) = $100,000 − $40,000 = **$60,000**.

### Phaseout

The federal §179 phaseout starts at $4,000,000 for 2025 (2025 Instructions for Form 4562; re-check the 2026 figure there). California's phaseout starts at $200,000 (2025 FTB 3885L, line 3).

---

## QBI Deduction (§199A)

| Federal | California |
|---------|-----------|
| 20% of qualified business income, made permanent under OBBBA | **California does NOT conform** to §199A. Members report their full distributive share without §199A reduction. |

The QBI deduction is taken at the member (1040) level federally; nothing changes on Form 568 directly. But the K-1 (568) reports California-source income without the federal §199A treatment, so members claiming §199A on federal must reconcile on California Schedule CA(540).

---

## State Tax Refunds

| Federal | California |
|---------|-----------|
| State tax refunds are taxable to the extent the prior-year deduction provided a federal tax benefit (tax benefit rule) | Treated at the member level on Schedule CA (540 / 540NR), not on Form 568. |

No Form 568 adjustment. Refunds of state income tax are a member's individual-return item; leave them to the member's California return.

---

## Domestic Production Activities Deduction (DPAD, §199 — repealed federally 2017 but legacy applicable in some states)

| Federal | California |
|---------|-----------|
| Repealed 2018 (TCJA) | California never conformed; no adjustment needed for current returns |

---

## Charitable Contributions

| Federal | California |
|---------|-----------|
| Separately stated on Schedule K; limits apply at the member level | Separately stated on Schedule K (568) lines 13a–13b; limits apply at the member level |

Generally minor at the LLC level; differences, if any, arise on the members' California returns.

---

## NOL (Net Operating Loss) carryforwards

| Federal | California |
|---------|-----------|
| Member-level deduction | Member-level deduction: "an LLC is not allowed the deduction" (2025 Form 568 Booklet, General Information on federal/state differences). California limits NOL deductions for some high-income taxpayers (2025 FTB 3805V, line 1 refers to net business income and modified AGI of $1,000,000 or more). |

No Form 568 adjustment: an LLC classified as a partnership does not take an NOL deduction. NOL limits are a member-level question; out of scope here.

---

## Meals & Entertainment

| Federal | California |
|---------|-----------|
| Meals 50% deductible (post-TCJA); entertainment not deductible | Conforms; same rules |

No adjustment needed.

---

## Health Insurance for Self-Employed

| Federal | California |
|---------|-----------|
| Deduction on Schedule 1 (Form 1040), line 17 (above-the-line) | Member-level item |

No adjustment needed at LLC level. (This is at the member's individual level anyway — flows through 1040, not Form 568.)

---

## §163(j) Business Interest Limitation

| Federal | California |
|---------|-----------|
| 30% of ATI limit (with TCJA modifications) | Historically California did not conform to the TCJA version of §163(j). After SB 711 moved the conformity date to January 1, 2025, confirm the current treatment in FTB Pub. 1001 for the taxable year before making an adjustment; ask a CPA if the federal limit applied. |

If federal Form 8990 limited the LLC's interest deduction, do not assume a California adjustment either way until confirmed.

---

## Cannabis Businesses (§280E)

| Federal | California |
|---------|-----------|
| §280E disallows ordinary business deductions for trafficking in controlled substances (which under federal law includes cannabis) | California allows the deductions for commercial cannabis activity licensed under MAUCRSA (R&TC §17209). The LLC attaches a schedule to each K-1 (568) showing the member's share of cannabis-related deductions and credits for FTB 4197 reporting (2025 booklet, Special Reporting for R&TC Section 41). |

This is significant for licensed California cannabis LLCs. Federal Form 1065 may show very high taxable income because §280E disallowed COGS-related expenses; California allows them. Large adjustment.

---

## Loans Forgiven Under PPP / similar federal programs

| Federal | California |
|---------|-----------|
| Loan forgiveness excluded from gross income; expenses paid with forgiven or grant funds remain deductible (CAA, 2021) | California conforms with modifications: an ineligible entity that deducted those expenses federally enters them as a California adjustment (2025 booklet, General Information on federal/state differences) |

For most current returns this is no longer relevant, but legacy LLCs may still have adjustments.

---

## Quick adjustment template

For the agent producing Form 568 from federal data:

```markdown
## California adjustments to federal income

| Item | Federal amount | California amount | Adjustment |
|------|----------------|---------------------|------------|
| §168(k) bonus depreciation | $X,XXX | $0 | Add back $X,XXX |
| §179 over $25K | $X,XXX (excess) | depreciated under MACRS | Add back excess − MACRS Year 1 |
| §163(j) interest cap | limited | confirm for the year (Pub. 1001) | Only after confirming |
| §199A QBI deduction | (claimed at 1040) | not claimed | n/a at LLC level |
| §280E (cannabis) | deductions disallowed | deductions allowed | Subtract disallowed amounts |
```

The sum of adjustments → modifies Schedule K (568) line by line, and flows to each member's K-1 (568).

---

## Citation summary

- R&TC §17024.5 — California conformity to the IRC as of a specified date (January 1, 2025, for taxable years beginning on or after January 1, 2025, under SB 711; FTB "What's new with tax forms")
- R&TC §17209 — Cannabis business deductions
- R&TC §17255, §24356 — California §179 limits
- 2025 FTB 3885L — California depreciation and §179 ($25,000 / $200,000; no §168(k))
- 2025 Instructions for Form 4562 — federal §179 $2,500,000 / $4,000,000 and bonus depreciation after January 19, 2025
- 2025 Form 568 Booklet — What's New (OBBBA nonconformity), federal/state differences (§174, NOL, CAA 2021 grants)

California's general approach: conform to IRC as of a specified date, then update by reference for specific provisions. The legislature decides each year which federal changes to adopt. The FTB's Pub 1001 (Supplemental Guidelines to California Adjustments) is the canonical reference — verify each tax year.
