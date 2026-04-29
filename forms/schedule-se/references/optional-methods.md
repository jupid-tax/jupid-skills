# Schedule SE Optional Methods (Part II)

The farm optional method (Section A) and non-farm optional method (Section B) let a low-income self-employed filer voluntarily pay SE tax on a higher base than their actual net earnings would dictate. The point: **earn Social Security credits** in a year that would otherwise generate few or none.

You don't elect optional methods for tax savings — they always **increase** SE tax owed. You elect them for SS credit accrual.

---

## Why optional methods exist

To qualify for Social Security retirement, disability, survivor, or Medicare benefits, a worker needs to earn **40 credits over their lifetime** (max 4 per year). One credit in 2025 = $1,810 in covered earnings (verify yearly at https://www.ssa.gov/oact/cola/QC.html). If a self-employed filer has a bad year and net SE earnings are below $1,810 × 4 = $7,240, they earn fewer than 4 credits.

The optional methods let them voluntarily report up to $6,560 (2025) in elective SE earnings to keep the credit accrual going.

**Lifetime maximum**: non-farm optional method may be elected in only **5 tax years total** (IRC §1402(l)(2)). Farm optional method has no lifetime limit.

---

## Section A — Farm Optional Method

### Eligibility (one-of)

- **Gross farm income < $9,840** (2025; verify each year), OR
- **Net farm profit < $7,103** (2025; verify each year)

There is no requirement of prior-year self-employment for the farm method.

### How much you elect

```
Line 14 = min($6,560, 2/3 × gross farm income)
```

The $6,560 cap is the elective amount, not a multiplier on it. Flows to Line 4b.

### When it makes sense

A farmer whose primary income is a "bad crop year" — gross farm income low, net even lower or negative. Reporting $6,560 in SE earnings generates 4 SS credits for the year.

**Tax cost**: $6,560 × 0.9235 × 0.153 = **~$927 in SE tax** (most years; verify with current rates). The filer is paying ~$927 to keep their 40-credit clock ticking.

### Eligibility math example

| Farmer | Gross farm income | Net farm profit | Eligible? |
|--------|-------------------|-----------------|-----------|
| A | $8,000 | $4,000 | Yes (gross < $9,840) |
| B | $12,000 | $5,000 | Yes (net < $7,103) |
| C | $50,000 | $40,000 | No (both above thresholds) |
| D | $0 | −$2,000 (loss) | Yes (gross < $9,840) |

---

## Section B — Non-Farm Optional Method

### Eligibility (all-of)

- **Net non-farm earnings < $7,103** (2025; verify yearly)
- **Net non-farm earnings ≥ $0** (cannot be a loss; also not a hard requirement, but the implied 72.189% rule below means very low gross income disqualifies)
- **2-of-3 prior years** had net SE earnings ≥ $400 (regularity test, IRC §1402(l))
- **Lifetime cap**: not used in 5 prior tax years

The 72.189% rule: net earnings × 100 / gross income ≥ 72.189%. This ensures the filer is genuinely self-employed and not just making a tax-credit play. It comes from the IRS Schedule SE instructions and is implied by the 2/3 multiplier on gross income.

### How much you elect

```
Line 16 = min($6,560, 2/3 × gross non-farm income)
```

The $6,560 cap is the same as farm. Flows to Line 4b.

### When it makes sense

A regular self-employed worker — bookkeeper, freelance writer, consultant — who has a slow year (income drops below $7,103). The optional method keeps them at 4 SS credits for the year.

**Tax cost**: same ~$927 in SE tax for the credit purchase.

### Lifetime cap mechanics

The 5-time lifetime cap is per filer. Track it: ask the user "Have you elected the non-farm optional method in any prior tax year? In how many?" If they don't know, suggest they request a Social Security earnings statement (https://www.ssa.gov/myaccount/) which shows credited SE earnings by year.

If the filer is on their 6th attempt, the election is invalid; remove it and revert to actual net earnings.

### 2-of-3 prior years test

Prior 3 tax years before the current one must include 2 with net SE earnings ≥ $400. Examples for filing tax year 2025 (prior 3 = 2022, 2023, 2024):

| Filer | 2022 SE | 2023 SE | 2024 SE | Eligible? |
|-------|---------|---------|---------|-----------|
| A | $5,000 | $8,000 | $0 | Yes (2022 + 2023) |
| B | $0 | $0 | $5,000 | No (only 1 of 3) |
| C | $401 | $402 | $403 | Yes (all 3 ≥ $400) |
| D | $399 | $0 | $399 | No (none ≥ $400) |

---

## Combined elections (rare)

A filer with **both** farm and non-farm income may elect both methods in the same year. Add Line 14 + Line 16 to Line 4b — but the combined election cannot exceed $6,560 in 2025 (the cap is per filer, not per method).

---

## Tax cost vs. SS credit benefit

The cost-benefit of an optional method election:

- **Cost**: SE tax on the elected amount. For 2025, electing the full $6,560 base produces ~$927 SE tax (subject to wage-base interaction).
- **Benefit**: 4 SS credits for the year, accelerating eligibility for SS retirement / disability / Medicare. Each credit is worth nothing on its own — only the 40-credit lifetime threshold matters.

Decision rules:
- **Filer is < 40 credits and < age 62**: usually worth electing if the year would otherwise generate 0 credits
- **Filer already has 40+ credits**: rarely worth it (extra credits don't increase SS benefit; the benefit calculation uses the highest 35 years of indexed earnings)
- **Filer is in their last few credits before 40**: worth it
- **Filer is on disability**: maintaining recent credits matters for disability eligibility (DIB requires 20 credits in the 40 quarters before disability) — see SSA disability rules

The agent should **not** make this decision. Surface the trade-off to the user and let them decide.

---

## Authority cited

- IRC §1402(l) — non-farm optional method (regularly engaged in SE)
- IRC §1402(a)(15) — farm optional method
- Schedule SE Part II, Section A and Section B
- IRS Schedule SE Instructions — annual thresholds
- SSA Quarter of Coverage announcements — https://www.ssa.gov/oact/cola/QC.html
- SSA Earnings Record (my Social Security) — https://www.ssa.gov/myaccount/

## Verify before filing

- Gross farm income threshold (2025: $9,840)
- Net farm profit threshold (2025: $7,103)
- Net non-farm earnings threshold (2025: $7,103)
- Optional method cap (2025: $6,560)
- One SS credit dollar amount (2025: $1,810)

The IRS sets these in the Schedule SE Instructions each tax year. The 2026 thresholds are typically announced in late 2025 alongside the SSA wage base.
