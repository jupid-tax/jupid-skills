# Adjusted Qualified Education Expenses (AAQEE) — Coordination Math

How to coordinate a 529/Coverdell distribution with scholarships, employer education assistance, and education tax credits (AOTC, LLC).

The same dollar of qualified expense **cannot** fund a tax-free 529 distribution AND any of the following at the same time:

1. Tax-free scholarship or grant (excluded under IRC §117)
2. Employer-provided educational assistance (excluded under IRC §127)
3. American Opportunity Tax Credit (AOTC, IRC §25A(i))
4. Lifetime Learning Credit (LLC, IRC §25A(b))

The IRS calls the resulting figure **Adjusted Qualified Education Expenses (AAQEE)**. Pub 970 chapter 8 walks through the formula. This file is the agent's worksheet.

---

## The formula

```
AAQEE = Total QHEE
        − Tax-free scholarships and grants
        − Employer-provided education assistance (IRC §127, up to $5,250/year exclusion)
        − Expenses allocated to AOTC
        − Expenses allocated to LLC
        − Other tax-free education benefits used for the same expenses
```

If AAQEE ≥ Box 1 of 1099-Q, the entire 529/Coverdell distribution is **tax-free**.

If AAQEE < Box 1, a portion is non-qualified. Compute taxable earnings:

```
Non-qualified portion = Box 1 − AAQEE
Earnings ratio = Box 2 / Box 1
Taxable earnings = Non-qualified portion × Earnings ratio
```

The taxable earnings amount goes on **Schedule 1 Line 8z**, and may also trigger the 10% additional tax via Form 5329 Part II → Schedule 2 Line 8.

---

## Step-by-step coordination

### Step 1 — Start with Total QHEE

Build the QHEE table (see [`qualified-expenses.md`](./qualified-expenses.md)). Sum to get Total QHEE.

### Step 2 — Subtract tax-free scholarships and grants

Tax-free scholarships are amounts received for tuition, fees, books, supplies, or equipment **required for enrollment** at an eligible educational institution, used for qualified expenses, and not in exchange for services. Excluded from income under IRC §117.

**Subtract from QHEE pool**: scholarship amounts that were applied to expenses also in the QHEE pool. The scholarship recipient gets to choose how to allocate scholarships to expenses if not specified by the grantor — see Pub 970 chapter 1.

**Strategy note**: a scholarship recipient can elect to include the scholarship in income (rather than take it tax-free), which frees up the corresponding expenses for AOTC/LLC or 529 tax-free use. This is the "scholarship inclusion strategy" — it sometimes increases total benefit when AOTC is in play. Out of scope for this skill, but the agent should flag if the user appears to be missing the optimization.

### Step 3 — Subtract employer-provided education assistance

Under IRC §127, up to $5,250/year of employer education assistance is excluded from the employee's income. To the extent employer assistance was used for the same expenses also in the QHEE pool, subtract from QHEE.

If the employer pays directly to the school, the user may not have a clean record. Ask: "Did your or the beneficiary's employer pay any tuition or fees directly?" If yes, get the dollar amount.

### Step 4 — Subtract AOTC expenses

The American Opportunity Tax Credit (AOTC) is computed on Form 8863 Part I. It uses up to $4,000 of qualified expenses per student per year:

- Credit = 100% of first $2,000 + 25% of next $2,000 = max $2,500
- Phase-out: MAGI $80K-$90K single / $160K-$180K MFJ
- Available for first 4 years of post-secondary education
- Must be enrolled at least half-time

If the user (or whoever claims the student as a dependent) is using AOTC, the qualified expenses fueling the credit must be subtracted from the QHEE pool for 529 purposes.

**Common allocation**: reserve $4,000 of tuition + required fees for AOTC (maximizing the credit), then use the remainder for 529 tax-free.

### Step 5 — Subtract LLC expenses

The Lifetime Learning Credit (LLC) is computed on Form 8863 Part II. It uses up to $10,000 of qualified expenses per **return** (not per student) per year:

- Credit = 20% of qualified expenses, max $2,000
- Phase-out: MAGI $80K-$90K single / $160K-$180K MFJ (2025; verify 2026)
- Available for any post-secondary education, no time limit
- Includes courses to acquire or improve job skills (not just degree programs)

If LLC is claimed, subtract those expenses from the QHEE pool.

**Note**: AOTC and LLC cannot be claimed for the **same student in the same year**. They can be claimed for different students on the same return.

### Step 6 — Compute AAQEE

```
AAQEE = Total QHEE − Step 2 amount − Step 3 amount − Step 4 amount − Step 5 amount
```

If AAQEE is negative, it's $0. (The user has more credits/scholarships than QHEE — entire 529 distribution is non-qualified.)

---

## Worked example: Coordination with AOTC

User facts:
- Tuition: $18,000
- Required fees: $1,200
- Required books: $800
- Room and board (half-time+): $11,000
- Computer (primary beneficiary use): $1,500
- **Total QHEE: $32,500**
- Tax-free scholarship: $5,000
- Employer assistance: $0
- AOTC claimed: $4,000 of qualifying expenses (yields $2,500 credit)

```
AAQEE = $32,500 − $5,000 (scholarship) − $4,000 (AOTC) − $0 (LLC, employer)
      = $23,500
```

If 1099-Q Box 1 = $20,000, AAQEE ($23,500) ≥ Box 1 → entirely tax-free.

If 1099-Q Box 1 = $25,000, non-qualified portion = $25,000 − $23,500 = $1,500. With Box 2 = $9,000 and Box 3 = $16,000:

```
Earnings ratio = $9,000 / $25,000 = 0.36
Taxable earnings = $1,500 × 0.36 = $540
```

The user reports $540 on Schedule 1 Line 8z. The 10% additional tax: $54 (unless an exception applies — see below).

---

## Exceptions to the 10% additional tax (IRC §529(c)(6)(B))

Even when there's a taxable earnings portion (Schedule 1 Line 8z reports income), the 10% additional tax does NOT apply to the extent of:

1. **Tax-free scholarship offset** — distribution amount up to the value of a tax-free scholarship received by the beneficiary in the same year. (The earnings portion is still taxable; only the 10% additional tax is waived.)
2. **AOTC / LLC offset** — distribution that is taxable solely because the qualified expenses were used for AOTC or LLC instead.
3. **Beneficiary's death** — distribution to the estate or another beneficiary after the original beneficiary dies.
4. **Beneficiary's disability** — defined under IRC §72(m)(7).
5. **U.S. service academy attendance** — distribution up to costs of attendance at the academy.

Each exception is reported on Form 5329 Part II by reducing Line 6 (distributions exempt from additional tax) by the exception amount. The agent should document which exception applies.

**Common scenario**: user has a $10,000 scholarship + $5,000 non-qualified 529 distribution. The $5,000 is treated as non-qualified for income inclusion purposes, but the 10% additional tax is waived up to $5,000 (the scholarship amount). Result: Schedule 1 Line 8z reports the taxable earnings, Schedule 2 Line 8 reports $0 (additional tax waived).

---

## When the strategy changes the math

Some optimizations require the user to act *before* the year ends (planning, not filing):

- **Allocating expenses to AOTC**: claim the first $4,000 of tuition for AOTC; the rest (and room/board, books beyond the $4K, computer) goes against the 529 distribution.
- **Including scholarship in income**: in some cases, the student elects to *include* a scholarship in income to free up the corresponding expenses for AOTC. This works only if the student's marginal rate is low enough that the AOTC value exceeds the additional tax on the included scholarship.
- **Timing the 529 distribution**: distributions within the same calendar year as the expense; an October distribution against January's spring-semester tuition is OK if both are in the same tax year.

This skill **processes** the user's actual transactions; it does NOT optimize the past. If the user is asking about a planning question, route them to a tax professional.

---

## What the agent must ask

When AAQEE is being computed, the agent must explicitly ASK (don't guess):

1. "Did the beneficiary receive any tax-free scholarship or grant in tax year YYYY?" — if yes, get amount and how it was applied
2. "Did the beneficiary's employer (or your employer for a beneficiary who's a dependent) pay any tuition or fees directly under an education-assistance program?" — if yes, get amount
3. "Are you (or anyone) claiming the American Opportunity Tax Credit or Lifetime Learning Credit for this student this year?" — if yes, get qualifying expenses used for credit
4. "Did the student attend at least half-time?" — controls room and board eligibility
5. "How was room and board calculated?" — at the school's cost of attendance, or actual expenses (capped at COA)?

Without these answers, AAQEE is a guess and the worksheet may understate the taxable amount. The agent must NOT default to "no scholarships, no AOTC" without confirmation.

---

## Cross-check before declaring done

- [ ] AAQEE is non-negative
- [ ] AAQEE ≤ Total QHEE
- [ ] If a scholarship was received, it was subtracted (or the user explicitly elected to include in income)
- [ ] If AOTC is being claimed on Form 8863, the corresponding expenses were subtracted
- [ ] If LLC is being claimed on Form 8863, the corresponding expenses were subtracted
- [ ] The "double-dipping" allocation rule was NOT violated (no expense counted twice)
- [ ] The user retains documentation of the allocation for audit (Form 1098-T, scholarship records, employer assistance records, AOTC/LLC computation)
