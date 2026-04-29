# Allocating Deductions to Foreign-Source Income (Form 1116 Lines 2-4)

The §904 limitation requires foreign-source taxable income — not gross. So deductions must be allocated and apportioned between US-source and foreign-source income. This is the most error-prone area of Form 1116 because the rules are scattered across Reg. §1.861-8 through §1.861-17.

For Form 1116 individual filers, the practical mechanics simplify to three buckets:

1. **Definitely-related deductions (Line 2)** — tied to specific income; allocate fully to that income's basket
2. **Pro-rata deductions (Line 3)** — not tied to specific income; apportion by gross-income ratio
3. **Interest expense (Line 4)** — special asset-method allocation

## Bucket 1 — Definitely related (Line 2)

A deduction is "definitely related" when it has a direct, identifiable factual connection to a specific income source.

Examples:

- Investment custody fees on a foreign brokerage account → definitely related to foreign passive income
- Professional services billed to a specific foreign engagement → definitely related to that foreign SE income
- Depreciation on equipment used only for foreign-sourced consulting → definitely related
- Foreign business expenses on Schedule C if the SE income is foreign-source → definitely related

Allocation: 100% to the related basket.

## Bucket 2 — Pro-rata (not definitely related) (Line 3)

Deductions that aren't tied to specific income get apportioned by a gross-income ratio.

### Itemized deduction or standard deduction (Line 3a)

The portion of itemized or standard deduction that isn't definitely related (most of it) is pro-rata.

- If standard deduction: enter the full standard deduction amount on Line 3a
- If itemizing: enter Schedule A total minus items already on Line 2 or Line 4

### Other deductions (Line 3b)

Charitable contributions if itemizing, certain other miscellaneous deductions.

### The allocation ratio (Line 3f)

```
Line 3f = Line 3d / Line 3e
        = Foreign-source gross income (this basket) / Total gross income (worldwide)
```

### The foreign share (Line 3g)

```
Line 3g = Line 3c × Line 3f
        = (Total pro-rata deductions) × (Foreign basket ratio)
```

This is what gets subtracted from foreign-source income.

### Worked example — pro-rata allocation

Filer has:
- US wages: $80,000
- Foreign-source SE income (Germany): $50,000
- Foreign-source dividends (US brokerage holding foreign stock): $5,000
- Standard deduction (2024 single): $14,600
- Total gross income: $135,000

For the **general basket** Form 1116 (German SE income):

- Line 3a = $14,600 (standard deduction)
- Line 3b = $0
- Line 3c = $14,600
- Line 3d = $50,000 (foreign general-basket gross income)
- Line 3e = $135,000
- Line 3f = 50,000 / 135,000 = 0.370370
- Line 3g = $14,600 × 0.370370 = $5,407

So $5,407 of standard deduction allocates to foreign general basket.

For the **passive basket** Form 1116 (foreign dividends):

- Line 3a = $14,600
- Line 3b = $0
- Line 3c = $14,600
- Line 3d = $5,000 (foreign passive gross income)
- Line 3e = $135,000
- Line 3f = 5,000 / 135,000 = 0.037037
- Line 3g = $14,600 × 0.037037 = $541

So $541 allocates to foreign passive basket.

The remaining $14,600 − $5,407 − $541 = $8,652 stays with US-source income (not on either Form 1116).

## Bucket 3 — Interest expense (Line 4)

Interest expense allocation has its own rules under Reg. §1.861-9. Two methods:

- **Asset method**: allocate interest based on adjusted basis of foreign-source vs. US-source assets at year-end (or average)
- **Gross income method**: allocate based on gross income ratio (only available in limited circumstances)

For most individual filers, the **asset method** is required and works like this:

1. Determine total US-source assets at year-end (homes, cars, US bank accounts, US stocks at basis)
2. Determine total foreign-source assets (foreign real estate, foreign stocks at basis)
3. Allocation ratio = foreign assets / total assets
4. Apply to total interest expense

### Worked example — home mortgage interest with foreign assets

Filer has:
- Home mortgage interest: $18,000
- US-source assets (home, US brokerage): $600,000 basis
- Foreign-source assets (Spanish rental property at $200K basis): $200,000

Asset ratio for foreign: $200,000 / $800,000 = 0.25

Foreign allocation of mortgage interest: $18,000 × 0.25 = $4,500 → Line 4b

**This applies to the BASKET to which the foreign assets relate.** The Spanish rental property income is passive basket; so $4,500 allocates to the passive basket Form 1116.

### Practical note

Most individual filers without significant foreign assets have minimal interest expense to allocate. If foreign assets are < 5% of total assets, the allocation is small and often not material. Document the methodology and move on.

## Special situations

### Self-employed filer with foreign SE income

Schedule C deductions definitely related to the foreign engagement are Line 2 items, not pro-rata. This is a big advantage — they reduce foreign income directly without going through the pro-rata ratio (which would dilute them across all income).

Example: a filer with $50,000 German consulting revenue and $15,000 of expenses tied entirely to that engagement (travel to client site, project supplies, contractor payments for the project) puts $15,000 on Line 2. Foreign-source income on Line 1a is $50,000; after Line 2 only, it's $35,000. The standard deduction or itemized still pro-rata-apportions on Line 3.

### Filer with home office on Schedule C

If the home office serves both US-source and foreign-source SE work, the home office deduction is allocated by the proportion of the work. Most agents simplify by allocating based on revenue split. Document the methodology.

### Filer using FEIE (Form 2555)

Deductions allocable to the **excluded** income are NOT deductible at all (against any income). Pub 514 calls this "the §911 disallowance." The agent must:

1. Identify deductions definitely related to the FEIE-excluded income
2. Disallow them entirely (do not put on Line 2 of Form 1116; do not put on Schedule A)

This is automatic in tax software but easy to miss in manual prep. See [`coordination-with-2555.md`](./coordination-with-2555.md).

### Mortgage interest deduction with home office

If the filer has a home office that's used for foreign-source SE work, AND home mortgage interest, the home office portion of the interest is on Schedule C / Form 8829 (definitely related to SE income, hence to the basket of that SE income). The remaining personal-use portion is on Schedule A (pro-rata via Line 3a).

## What the agent should do

1. **Sort each deduction** into one of the three buckets based on the user's facts
2. **Apply the formulas** for each bucket
3. **Document the methodology** for each pro-rata or asset-method allocation (the user should keep records)
4. **Show the math** in the deliverable so a CPA could re-derive it

The agent should NOT:

- Default to "no allocation" — the IRS will recompute and assess additional tax if Line 7 is too high (because deductions weren't allocated)
- Default to "allocate everything pro-rata" — definitely related deductions allocate fully, not pro-rata
- Treat home mortgage interest as pro-rata when it should be asset-method
