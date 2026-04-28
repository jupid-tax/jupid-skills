# Capital Loss Carryover — IRC §1211 and §1212

When net capital losses exceed the allowed annual deduction, the unused portion carries forward indefinitely under IRC §1212. The character (short-term or long-term) is preserved through the carryover.

This reference covers:
1. The annual loss limit (IRC §1211)
2. Order of absorption within a year
3. The Capital Loss Carryover Worksheet
4. Edge cases: death of taxpayer, MFS filings, NOL interaction

---

## The annual loss limit (IRC §1211(b))

Net capital loss deductible against ordinary income each year:

- **Single, MFJ, HoH, QSS:** $3,000
- **Married Filing Separately (MFS):** $1,500

This limit applies to the *net* capital loss — Schedule D Line 16 — not to gross losses. If the user has $20,000 of losses and $5,000 of gains, net loss is $15,000, and the limit applies to that net.

The unused portion carries forward indefinitely under IRC §1212(b). There is no carryback for individuals (corporations have a 3-year carryback, 5-year carryforward, but that's IRC §1212(a) — not relevant for Schedule D).

---

## Order of absorption within the year

Inside a tax year, losses absorb gains in this order:

1. **Short-term losses first offset short-term gains.** If short-term losses < short-term gains, you have net short-term gain (taxed as ordinary income).
2. **Long-term losses first offset long-term gains.** If long-term losses < long-term gains, you have net long-term gain (taxed at preferential rate).
3. **If both Part I and Part II are net losses**, both flow to Line 16 as a combined loss.
4. **If one Part is net gain and the other is net loss**, the net loss reduces the net gain at Line 16.

Schedule D Line 16 = Line 7 + Line 15. The form does this addition mechanically; the netting happens implicitly.

---

## Capital Loss Carryover Worksheet

The worksheet is in the Schedule D instructions. Inputs come from the **prior year's** return:

**Inputs:**
1. Prior-year Form 1040 Line 15 (taxable income)
2. Prior-year Schedule D Line 21 (the $3,000 / $1,500 limited loss used last year)
3. Prior-year Schedule D Line 7 (net short-term)
4. Prior-year Schedule D Line 15 (net long-term)

**Computation (simplified):**

```
Step 1: Compute the loss available to carry over.
   Total prior-year capital loss (Line 16 absolute value)
   Minus the amount used (Line 21)
   = Total carryover

Step 2: Allocate carryover by character.
   If short-term loss > $3,000 absorption:
     ST carryforward = ST loss − amount used against ordinary
     LT carryforward = LT loss in full (none used yet)
   Else (ST loss absorbed by ordinary income):
     ST carryforward = 0
     LT carryforward = remaining loss
```

**The worksheet handles a subtlety:** if your prior-year taxable income was negative or zero, the $3,000 deduction may not have actually reduced tax. In that case, the worksheet recovers the unused portion of the $3,000, increasing the carryover.

This is the so-called "income-based limitation" — you can't have a deduction larger than your taxable income would absorb. The worksheet preserves the unused amount.

---

## Worked example: Multi-year carryover

**Year 2024:**
- Net short-term gain: ($2,000) [loss]
- Net long-term gain: ($8,000) [loss]
- Net capital loss: ($10,000)
- Used against 2024 ordinary income: $3,000 (max)
- Carried forward to 2025:
  - Short-term: $0 (the $2,000 ST loss was absorbed first)
  - Long-term: $7,000

**Year 2025:**
- Schedule D Line 6 (ST carryover): $0
- Schedule D Line 14 (LT carryover): ($7,000)
- Suppose 2025 also produces net ST gain $1,500 and net LT gain $4,000:
  - Line 7 = $1,500 (ST gain offsets nothing)
  - Line 15 = $4,000 + ($7,000) = ($3,000) [LT loss after carryover]
  - Line 16 = $1,500 + ($3,000) = ($1,500)
  - Line 21 = ($1,500) — full deduction (under $3,000 cap)
  - 2026 carryforward:
    - ST: $0
    - LT: $0 (the $7,000 was fully consumed)

**Year 2025 alternative — bigger losses:**
- Schedule D Line 14 (LT carryover): ($7,000)
- 2025 produces no new gains or losses:
  - Line 7 = $0
  - Line 15 = ($7,000)
  - Line 16 = ($7,000)
  - Line 21 = ($3,000) [limit]
  - 2026 carryforward:
    - ST: $0
    - LT: $4,000

The carryover continues year over year until exhausted. There is no expiration.

---

## Edge cases

### Death of taxpayer

Capital loss carryovers **do not survive the taxpayer's death**. If the decedent had $50,000 of unused carryover, the final return absorbs whatever the $3,000 limit allows; the rest is lost.

Important nuance: the surviving spouse on a joint final return can use carryovers attributable to the *decedent's separate property* on that final joint return only — not on subsequent returns.

For estate planning purposes, taxpayers with large carryovers may want to realize gains before death to absorb the carryover.

### MFS to MFJ (or vice versa)

If filing status changes between years, carryovers must be allocated:

- **MFS to MFJ:** The carryover from each spouse's prior MFS return combines on the new joint return.
- **MFJ to MFS:** The prior joint carryover must be allocated. If the loss can be traced to one spouse's separate property, allocate to that spouse; otherwise split equally.

Each year's MFS limit is $1,500, so a former joint $3,000-deduction household may take longer to absorb the carryover after splitting.

### Interaction with NOL

A capital loss carryover is **not** a Net Operating Loss (NOL). They are tracked and computed separately. The capital loss carryover lives on Schedule D Lines 6 / 14; the NOL carryover lives on Schedule 1 Line 8a.

If a year produces both a capital loss and an NOL, both carryovers run independently.

### State carryover rules differ

- **California** — capital loss carryover follows federal mechanics (mostly), but state uses CA-specific AGI definitions
- **New Jersey** — does **not** allow capital loss carryover at all; loss is permanently lost in the year incurred
- **Massachusetts** — has its own capital gain schedule with different netting rules

When the user has a significant carryover, flag the state-side treatment for the state return.

### "$3,000 limit" is per return, not per spouse

If MFJ, the $3,000 is a household limit — not $3,000 per spouse. Two-earner households cannot deduct $6,000.

If MFS, each spouse has a $1,500 limit on their own return. This is one of the reasons MFS often produces a higher combined tax than MFJ.

---

## How Jupid tracks carryover

Jupid's accounting layer keeps year-over-year capital loss carryover automatically:

- After each filing, the prior-year Capital Loss Carryover Worksheet is saved with the user's records.
- The next year's Schedule D import pre-populates Lines 6 and 14 with the carryforward by character.
- Mid-year, when a user asks "What's my carryover?", Jupid reports the inventory of unused short-term and long-term losses available.
- Year-end planning: the user can ask "If I sell MSFT for a $10,000 gain, what's my net taxable gain?" and Jupid computes the answer including absorption from the carryover.

This is the bookkeeping piece that breaks down most often with manual prep — losing track of the prior-year carryover means permanent loss of the deduction.

---

## Sources

- [IRC §1211(b)](https://www.law.cornell.edu/uscode/text/26/1211) — Limitation on capital losses for individuals
- [IRC §1212(b)](https://www.law.cornell.edu/uscode/text/26/1212) — Capital loss carryback and carryforward
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses (definitive on carryover)
- [Schedule D Instructions — Capital Loss Carryover Worksheet](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
