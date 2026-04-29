# California Federal-to-State Adjustments

California does not fully conform to federal tax law. Several federal items must be adjusted on Form 568 (and Schedule K-1 (568) per member). This reference catalogs the most common adjustments.

The agent's job: take the federal Schedule K (from federal Form 1065 or the federal Schedule C/E for SMLLCs), apply the California-specific adjustments, and report the adjusted numbers on Form 568 Schedule K (568) and the member K-1s.

---

## Depreciation and §179

### Bonus depreciation (§168(k))

| Federal | California |
|---------|-----------|
| 100% bonus depreciation made permanent under OBBBA 2025 (verify effective date for assets placed in service) | **California does NOT conform** to §168(k). Full add-back required. |

Mechanic: federal Form 4562 may show, e.g., $50,000 of 100% bonus depreciation on a $50,000 piece of equipment. On California, the LLC depreciates the same equipment under MACRS at the regular recovery period (5- or 7-year for most equipment). Year 1 California deduction is much smaller — first-year MACRS half-year convention on a 5-year asset is 20%, so $10,000 instead of $50,000.

The $40,000 difference becomes an **adjustment** on Schedule K (568) — added back to California taxable income.

In subsequent years, California allows MACRS depreciation while federal has already deducted everything → California gets a deduction federal doesn't.

### Section 179

| Federal | California |
|---------|-----------|
| 2025 limit: $1,250,000 (Rev. Proc. 2024-40); 2026 set by inflation indexing | **California limit: $25,000** (R&TC §17255 / §24356) |

If the federal §179 deduction exceeds $25,000, the excess must be depreciated under MACRS for California purposes.

Example. LLC bought $100,000 of equipment, elected federal §179 = $100,000. California §179 limit = $25,000. The remaining $75,000 must be depreciated under MACRS for California — at 5-year, 20% Year 1, $15,000. So California deduction Year 1 = $25,000 + $15,000 = $40,000, vs. federal $100,000.

Add-back on Schedule K (568) = $100,000 − $40,000 = **$60,000**.

### Phaseout

The federal §179 phaseout starts at $3,130,000 (2025; verify 2026). California's phaseout starts at $200,000 — much lower.

---

## QBI Deduction (§199A)

| Federal | California |
|---------|-----------|
| 20% of qualified business income, made permanent under OBBBA 2025 | **California does NOT conform** to §199A. Members report their full distributable share without §199A reduction. |

The QBI deduction is taken at the member (1040) level federally; nothing changes on Form 568 directly. But the K-1 (568) reports California-source income without the federal §199A treatment, so members claiming §199A on federal must reconcile on California Schedule CA(540).

---

## State Tax Refunds

| Federal | California |
|---------|-----------|
| State tax refunds are taxable to the extent the prior-year deduction provided a federal tax benefit (tax benefit rule) | **California does not tax California state-tax refunds** (R&TC §17131.6 — refund of CA tax not income). California **does** tax other states' tax refunds. |

Adjustment: subtract any California state tax refund from federal income; add back any other state's refund if not in federal income.

---

## Domestic Production Activities Deduction (DPAD, §199 — repealed federally 2017 but legacy applicable in some states)

| Federal | California |
|---------|-----------|
| Repealed 2018 (TCJA) | California never conformed; no adjustment needed for current returns |

---

## Charitable Contributions

| Federal | California |
|---------|-----------|
| Mostly conforms; AGI-based limits | Mostly conforms; some §170(p) provisions don't apply |

Generally minor; for most LLCs the federal and California charitable amounts match.

---

## NOL (Net Operating Loss) carryforwards

| Federal | California |
|---------|-----------|
| 80% of taxable income (post-2017); indefinite carryforward | California suspended NOL deductions for 2024 and 2025 for taxpayers with > $1M income (AB 5/SB 167); 80% limit; up to 20-year carryforward. **Verify current rules** as the suspension may extend or expire. |

If the LLC's federal income includes an NOL deduction, California may not allow it for 2024-2025. Add-back required.

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
| Deduction on Schedule 1 Line 17 (above-the-line) | Conforms |

No adjustment needed at LLC level. (This is at the member's individual level anyway — flows through 1040, not Form 568.)

---

## §163(j) Business Interest Limitation

| Federal | California |
|---------|-----------|
| 30% of ATI limit (with TCJA modifications) | California does NOT conform to §163(j); LLC computes interest deduction without the federal cap |

If federal Form 8990 limited the LLC's interest deduction, California allows the full deduction. Adjustment: add back the federal-limited amount (i.e., California takes more).

---

## Cannabis Businesses (§280E)

| Federal | California |
|---------|-----------|
| §280E disallows ordinary business deductions for trafficking in controlled substances (which under federal law includes cannabis) | California does NOT conform to §280E for licensed cannabis businesses. Deductions allowed (R&TC §17209 / §24436.1). |

This is significant for licensed California cannabis LLCs. Federal Form 1065 may show very high taxable income because §280E disallowed COGS-related expenses; California allows them. Large adjustment.

---

## Loans Forgiven Under PPP / similar federal programs

| Federal | California |
|---------|-----------|
| Loan forgiveness excluded from gross income; expenses paid with PPP funds remain deductible | California conforms to PPP exclusion only for taxpayers meeting certain revenue-decline tests (AB 80) |

For most current returns this is no longer relevant (PPP era ending), but legacy LLCs may still have adjustments.

---

## Quick adjustment template

For the agent producing Form 568 from federal data:

```markdown
## California adjustments to federal income

| Item | Federal amount | California amount | Adjustment |
|------|----------------|---------------------|------------|
| §168(k) bonus depreciation | $X,XXX | $0 | Add back $X,XXX |
| §179 over $25K | $X,XXX (excess) | depreciated under MACRS | Add back excess − MACRS Year 1 |
| §163(j) interest cap | limited | unlimited | Subtract limit difference |
| §199A QBI deduction | (claimed at 1040) | not claimed | n/a at LLC level |
| State tax refund (CA) | included if applicable | not taxed | Subtract |
| State tax refund (other states) | included if applicable | included | n/a |
| §280E (cannabis) | deductions disallowed | deductions allowed | Subtract disallowed amounts |
```

The sum of adjustments → modifies Schedule K (568) line by line, and flows to each member's K-1 (568).

---

## Citation summary

- R&TC §17024 — California conformity to IRC as of a specified date (currently January 1, 2015, with selected updates)
- R&TC §17131.6 — California state tax refund exclusion
- R&TC §17209 — Cannabis business deductions
- R&TC §17255, §24356 — California §179 limits
- AB 5 / SB 167 (2024) — NOL suspension
- AB 80 (2021) — PPP conformity (mostly historical now)

California's general approach: conform to IRC as of a specified date, then update by reference for specific provisions. The legislature decides each year which federal changes to adopt. The FTB's Pub 1001 (Supplemental Guidelines to California Adjustments) is the canonical reference — verify each tax year.
