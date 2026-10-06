# Allocating Deductions to Foreign-Source Income (Form 1116 Lines 2-5)

The §904 limitation requires foreign-source taxable income — not gross. So deductions must be allocated and apportioned between US-source and foreign-source income. This is the most error-prone area of Form 1116 because the rules are scattered across Reg. §1.861-8 through §1.861-17.

For Form 1116 individual filers, the practical mechanics simplify to three buckets:

1. **Definitely-related deductions (Line 2)** — tied to specific income; allocate fully to that income's basket
2. **Pro-rata deductions (Line 3)** — not tied to specific income; apportion by gross-income ratio
3. **Interest expense (Lines 4a/4b)** — home mortgage interest by a gross-income worksheet (4a), other interest by the asset method (4b)

Line numbers follow the 2025 Form 1116 and its instructions (Dec 23, 2025).

## Bucket 1 — Definitely related (Line 2)

A deduction is "definitely related" when it has a direct, identifiable factual connection to a specific income source.

Examples:

- Investment custody fees on a foreign brokerage account → definitely related to foreign passive income
- Professional services billed to a specific foreign engagement → definitely related to that foreign SE income
- Depreciation on equipment used only for foreign-sourced consulting → definitely related
- Foreign business expenses on Schedule C if the SE income is foreign-source → definitely related
- State and local income taxes related to foreign-source income → line 2 (2025 i1116, Line 2)

Allocation: 100% to the related basket. Interest expense never goes on line 2. If a definitely related deduction relates to a class of income that spans more than one category (or a category and US-source income), apportion it within that class, for example by gross income (Pub. 514, "Class of gross income that includes more than one separate limit category"). Attach a statement listing the line 2 expenses.

## Bucket 2 — Pro-rata (not definitely related) (Line 3)

Deductions that aren't tied to specific income get apportioned by a gross-income ratio.

### Certain itemized deductions or standard deduction (Line 3a)

- If standard deduction: enter the full standard deduction amount on Line 3a
- If itemizing: enter only these Schedule A items: medical expenses (line 4), general sales taxes, real estate taxes for the home, and state and local personal property taxes. Don't include more state and local tax than Schedule A line 5e allows (2025 i1116, Lines 3a and 3b; Pub. 514)

### Other deductions (Line 3b)

Other deductions that don't definitely relate to any specific type of income, for example Schedule 1 (Form 1040) Part II adjustments to income (such as the deductible part of self-employment tax). Do not include the Schedule 1-A line 37 senior deduction; the Schedule 1-A line 30 car loan interest deduction goes on line 4b. Attach a statement listing the line 3a and 3b items.

### Gross income for lines 3d and 3e

Gross receipts less cost of goods sold, gains before losses, and other income before deductions. Both lines include foreign earned income excluded on Form 2555 but no other exempt income, and both use qualified dividends and capital gains before any rate adjustment. Line 3e is the same on every Form 1116.

### The allocation ratio (Line 3f)

```
Line 3f = Line 3d / Line 3e   (round to at least 4 decimals; not more than 1)
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
- Standard deduction (2025 single, as amended by P.L. 119-21): $15,750
- Total gross income: $135,000

For simplicity this example leaves out the deductible part of SE tax; in a real return it goes on line 3b of both forms.

For the **general basket** Form 1116 (German SE income):

- Line 3a = $15,750 (standard deduction)
- Line 3b = $0
- Line 3c = $15,750
- Line 3d = $50,000 (foreign general-basket gross income)
- Line 3e = $135,000
- Line 3f = 50,000 / 135,000 = 0.3704
- Line 3g = $15,750 × 0.3704 = $5,834

So $5,834 of standard deduction allocates to foreign general basket.

For the **passive basket** Form 1116 (foreign dividends):

- Line 3a = $15,750
- Line 3b = $0
- Line 3c = $15,750
- Line 3d = $5,000 (foreign passive gross income)
- Line 3e = $135,000
- Line 3f = 5,000 / 135,000 = 0.0370
- Line 3g = $15,750 × 0.0370 = $583

So $583 allocates to foreign passive basket.

The remaining $15,750 − $5,834 − $583 = $9,333 stays with US-source income (not on either Form 1116).

## Bucket 3 — Interest expense (Lines 4a and 4b)

**Threshold first.** If gross foreign-source income (including income excluded on Form 2555) is $5,000 or less, a US citizen, resident alien, or domestic estate can allocate all interest expense to US-source income; lines 4a and 4b are then 0 (2025 i1116, Lines 4a and 4b).

**Line 4a — home mortgage interest: gross income method.** Use the Worksheet for Home Mortgage Interest in the instructions:

1. Gross foreign-source income of the type shown on this Form 1116 (don't include Form 2555-excluded income)
2. Gross income from all sources (don't include Form 2555-excluded income)
3. Line 1 ÷ line 2, at least four decimals
4. Deductible home mortgage interest (Schedule A line 8e)
5. Line 4 × line 3 → Form 1116 line 4a

Complete a separate worksheet for each country if the form has more than one country column.

**Line 4b — other interest expense: asset method.** Investment interest, trade or business interest, passive activity interest, student loan interest, and qualified passenger vehicle loan interest are apportioned by the adjusted basis of the assets that produce foreign vs. US income, each type separately (Pub. 514, "Interest expense"; Reg. §1.861-9).

### Worked example — home mortgage interest (line 4a)

Filer has (2025, itemizing):
- Home mortgage interest (Schedule A line 8e): $18,000
- Gross rents from a Spanish rental apartment (passive, foreign): $24,000
- Gross income from all sources: $180,000; no Form 2555 exclusion

Worksheet: $24,000 ÷ $180,000 = 0.1333; $18,000 × 0.1333 = **$2,399 → line 4a** of the passive basket Form 1116.

### Worked example — investment interest (line 4b)

From the 2025 instructions: $2,000 of investment interest; assets of $100,000 adjusted basis, $40,000 producing US-source income and $60,000 producing foreign-source income. 60% of $2,000 = **$1,200 → line 4b**; the $800 apportioned to US-source income goes on no line of Part I.

## Special situations

### Self-employed filer with foreign SE income

Schedule C deductions definitely related to the foreign engagement are Line 2 items, not pro-rata. This is a big advantage — they reduce foreign income directly without going through the pro-rata ratio (which would dilute them across all income).

Example: a filer with $50,000 German consulting revenue and $15,000 of expenses tied entirely to that engagement (travel to client site, project supplies, contractor payments for the project) puts $15,000 on Line 2. Foreign-source income on Line 1a is $50,000; after Line 2 only, it's $35,000. The standard deduction or itemized still pro-rata-apportions on Line 3.

### Filer with home office on Schedule C

If the home office serves both US-source and foreign-source SE work, the home office deduction is allocated by the proportion of the work. Most agents simplify by allocating based on revenue split. Document the methodology.

### Filer using FEIE (Form 2555)

Deductions allocable to the **excluded** income are not allowed (IRC §911(d)(6)), and the instructions say not to include deductions related to excluded income on lines 2 through 5. The agent must:

1. Identify deductions definitely related to the FEIE-excluded income
2. Leave them off lines 2 through 5 (and off the return where §911(d)(6) disallows them)
3. Still include the excluded income in the line 3d and 3e gross-income amounts, and leave it out of the line 4a worksheet

See [`coordination-with-2555.md`](./coordination-with-2555.md).

### Mortgage interest deduction with home office

If the filer has a home office that's used for foreign-source SE work, AND home mortgage interest, the home office portion of the interest is on Schedule C / Form 8829. On Form 1116 it is still interest expense: it never goes on line 2, and it is apportioned on line 4b (trade or business interest, asset method). The remaining personal-use portion is on Schedule A and goes through the line 4a worksheet.

## What the agent should do

1. **Sort each deduction** into one of the three buckets based on the user's facts
2. **Apply the formulas** for each bucket
3. **Document the methodology** for each pro-rata or asset-method allocation (the user should keep records)
4. **Show the math** in the deliverable so a CPA could re-derive it

The agent should NOT:

- Default to "no allocation" — the IRS will recompute and assess additional tax if Line 7 is too high (because deductions weren't allocated)
- Default to "allocate everything pro-rata" — definitely related deductions allocate fully, not pro-rata
- Treat home mortgage interest like other interest: it uses the line 4a gross-income worksheet, while other interest uses the line 4b asset method
