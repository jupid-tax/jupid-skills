# Schedule SE Line-by-Line Reference

Complete lookup for every line on Schedule SE. Use this when the agent needs to confirm where an input belongs or what a line means.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name of person with self-employment income | Filer's legal name | Even if joint return, name only the spouse with SE income on this Schedule SE |
| Social security number | Filer's SSN | The SE-earner's SSN, not the spouse's |

If both spouses on a joint return have SE income, file two separate Schedule SEs — one per spouse. Do not combine.

---

## Part I — Self-Employment Tax

### Line 1a — Net farm profit or (loss)

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Schedule F (Form 1040) Line 34 | Schedule C net profit (Line 2 below) |
| Farm partnership SE earnings: K-1 (Form 1065) Box 14 Code A allocated as farm | Land rental income (Schedule E) |

If the user has a farm loss, Line 1a is negative. The negative amount can offset positive Schedule C earnings on Line 2 in the Line 3 sum.

### Line 1b — CRP payments excluded from SE

Conservation Reserve Program (CRP) payments received by a farmer who is **already drawing Social Security retirement or disability benefits** are excluded from SE tax under IRC §1402(a)(1). The exclusion only applies to those drawing SS benefits — others include CRP in farm income normally.

For most filers Line 1b = 0.

### Line 2 — Net profit or (loss) from Schedule C

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Schedule C Line 31 (net profit or loss) | Wage income (W-2; not SE) |
| K-1 (Form 1065) Box 14 Code A — general partner / LLC manager-member share | K-1 Box 14 Code A from a limited partnership interest (excluded under IRC §1402(a)(13)) |
| Statutory employee income from Form W-2 Box 13 with "Statutory employee" checked AND Schedule C reported (rare) | S-corp K-1 distributions (no SE tax) |
| Notary public fees (excluded under IRC §1402(c)(1)) — actually NO, exclude these |  |

**Critical**: Notary public fees are exempt from SE tax. If the user's Schedule C profit includes notary fees, subtract them on Line 2 with a note (the form has a write-in line; if not, attach a statement). Same for ministers' housing allowance (Form 4361 exemption) — out of scope here, see Pub 517.

### Line 3 — Combine 1a, 1b, 2

Mechanical: Line 1a + Line 1b + Line 2.

### Line 4a — Line 3 × 0.9235

The 0.9235 factor (= 1 − 0.0765) is the "employer share equivalent" reduction (IRC §1402(a)(12)). It approximates the deduction a W-2 employer takes for the employer portion of FICA when computing wages, giving the self-employed filer parity with W-2 employees on the SE tax base.

Round to the nearest dollar. If Line 4a is **less than $400**, no SE tax is due (IRC §1402(b)) unless the user is using the optional method on Line 4b.

### Line 4b — Optional method amount

Enter the elected amount from Part II Section A (farm) or Section B (non-farm) optional method. Most filers leave Line 4b = 0.

### Line 4c — Combine 4a and 4b

Mechanical sum.

### Line 5a — Church employee income

For W-2 wages from a church or qualified church-controlled organization that has elected out of FICA under IRC §3121(w). The wages are reported on Form W-2 Box 1 with no Social Security or Medicare tax withheld in Boxes 4/6.

This is rare. Most W-2 wages are NOT church employee income.

### Line 5b — Line 5a × 0.9235

Same factor as Line 4a, applied to church employee income.

### Line 6 — Net earnings from SE

Line 4c + Line 5b. This is the base amount on which SE tax is computed.

### Line 7 — Maximum amount subject to Social Security tax

Pre-printed by the IRS each year. This is the SSA's annual contribution and benefit base:

| Tax year | SS wage base |
|----------|--------------|
| 2023 | $160,200 |
| 2024 | $168,600 |
| 2025 | $176,100 |
| 2026 | (verify with SSA — typically announced October of prior year) |

Source: https://www.ssa.gov/oact/cola/cbb.html

**Always read the current year's figure from the printed Schedule SE form**, not from this table — the table can drift.

### Line 8a — Total social security wages (W-2 Box 3)

Sum of Form W-2 Box 3 amounts from all the filer's W-2 jobs in the tax year. This is the wages already subject to Social Security tax via FICA withholding.

If the filer had multiple W-2 jobs and total Box 3 exceeds the wage base, they may have over-withheld Social Security and can claim an excess SS tax credit on Schedule 3 — separate issue, not Schedule SE.

### Line 8b — Unreported tip income subject to SS

From Form 4137 if the filer received tips and didn't report them to the employer. Usually 0.

### Line 8c — Wages from Form 8919

Form 8919 (Uncollected Social Security and Medicare Tax on Wages) is filed when a worker believes they were misclassified as a contractor. The wages flow here so the SE calc doesn't double-count. Usually 0.

### Line 8d — Sum 8a + 8b + 8c

Mechanical.

### Line 9 — Line 7 − Line 8d

Available remaining SS wage base for SE earnings. Floor at 0 (cannot be negative).

If Line 8d ≥ Line 7, Line 9 = 0 → SS portion of SE tax = 0 (the W-2 job already exhausted the wage base).

### Line 10 — SS portion of SE tax

```
Line 10 = min(Line 6, Line 9) × 0.124
```

The 12.4% combines the 6.2% employee + 6.2% employer Social Security rate (IRC §1401(a)). It applies only to the lesser of:
- Total net SE earnings (Line 6), OR
- Remaining wage base after W-2 wages (Line 9)

### Line 11 — Medicare portion of SE tax

```
Line 11 = Line 6 × 0.029
```

The 2.9% combines 1.45% employee + 1.45% employer Medicare (IRC §1401(b)). **No wage base cap.**

High earners with combined wages + SE > $200K (single) / $250K (MFJ) / $125K (MFS) also owe an additional 0.9% Medicare tax on the excess — that's **Form 8959**, not Schedule SE.

### Line 12 — Total self-employment tax

```
Line 12 = Line 10 + Line 11
```

This is the SE tax owed. Flows to Schedule 2 Line 4 → Form 1040 Line 23.

### Line 13 — Deduction for one-half of SE tax

```
Line 13 = Line 12 × 0.5
```

Half of SE tax is deductible above the line as an adjustment to income on Schedule 1 Line 15 (IRC §164(f)). This gives the SE filer parity with W-2 employees, who don't pay tax on the employer's FICA share.

The deduction is "above the line" — it reduces AGI, which can also reduce phase-outs for IRA contributions, education credits, QBI, etc. Worth taking even if the filer takes the standard deduction.

---

## Part II — Optional Methods + Church Employee Income

See [`optional-methods.md`](./optional-methods.md) for thresholds, eligibility, and worked examples.

### Section A — Farm Optional Method

Available if **either** of:
- Gross farm income < $9,840 (2025 — verify yearly); OR
- Net farm profit < $7,103 (2025 — verify yearly)

Election: Line 14 = 2/3 × gross farm income, capped at $6,560 (2025). Flows to Line 4b.

Use case: a farmer with a low-income year wants to keep accruing Social Security credits (4 credits per year, 40 lifetime credits required for retirement benefits).

### Section B — Non-Farm Optional Method

Available if **all** of:
- Net non-farm earnings < $7,103 (2025 — verify yearly)
- Filer is regularly self-employed (net SE earnings ≥ $400 in 2 of the prior 3 years per IRC §1402(l))
- Net non-farm earnings ≥ 72.189% of gross non-farm income (this is the implied floor that makes the optional method economically rational)
- Lifetime cap: 5 elections total

Election: Line 16 = 2/3 × gross non-farm income, capped at $6,560 (2025). Flows to Line 4b.

### Section B (separate from optional method) — Church employee income

Lines 5a/5b in Part I handle this if the filer has W-2 wages from a church that has elected out of FICA. No separate computation needed beyond Lines 5a/5b — the optional methods sections are independent.

---

## Special situations

### Statutory employees

If Form W-2 Box 13 "Statutory employee" is checked, the wages from that W-2 go on Schedule C (not as ordinary wages on Form 1040), and the resulting net profit flows to Schedule SE Line 2 normally. Statutory employees are subject to FICA at the W-2 stage (employer withholds), so they typically do NOT also owe SE tax on the same income — the IRS lists them on Schedule C purely so business expenses can be deducted. In that case, the user reports Schedule C net profit but uses Schedule SE only if they have other (non-statutory-employee) SE earnings.

### Limited partners

Limited partner share of partnership income is **excluded from SE tax** under IRC §1402(a)(13). Only general partner / LLC manager-member share is SE-eligible. If the K-1 Box 14 Code A is for a limited partner, exclude it from Line 2.

### Real estate professionals / rental income

Rental real estate income is reported on Schedule E and is **not subject to SE tax** unless the filer is a real estate dealer (rare) or provides substantial services (operates a hotel / B&B). Most landlords do not owe SE tax.

### Foreign earned income exclusion (FEIE)

Even if the filer excludes foreign earned income from regular income tax via Form 2555, **SE tax still applies** to the gross foreign SE earnings (IRC §911(d)(4)). Don't reduce Line 2 by the FEIE.

### Totalization agreement

If the filer is a US citizen working abroad in a country with a US Social Security totalization agreement, they may be exempt from US SE tax on income covered by the foreign country's SS system. Requires a Certificate of Coverage from the foreign agency. See https://www.ssa.gov/international/agreements_overview.html

### Notary public fees

Notary fees are **exempt from SE tax** (IRC §1402(c)(1)). Subtract notary fees from Line 2 with a note. They still flow to Schedule C Line 1 as gross income; only the SE-tax base is reduced.

### Clergy with Form 4361

Ministers, members of religious orders, and Christian Science practitioners who have filed Form 4361 (and received IRS approval) are exempt from SE tax on ministerial earnings. Different rules apply; see Pub 517. Out of scope for this skill.

---

## Authority cited

- IRC §1401 — SE tax rates (12.4% SS + 2.9% Medicare)
- IRC §1402 — definition of SE earnings
  - §1402(a)(1) — CRP exclusion for SS recipients
  - §1402(a)(12) — 0.9235 factor
  - §1402(a)(13) — limited partner exclusion
  - §1402(b) — $400 threshold
  - §1402(c)(1) — notary exemption
  - §1402(l) — non-farm optional method requirements
- IRC §164(f) — deductible half of SE tax
- IRC §911(d)(4) — FEIE does not reduce SE tax
- IRC §3121(w) — church FICA election
- IRS Schedule SE and Instructions, current revision
- SSA Contribution and Benefit Base announcements
