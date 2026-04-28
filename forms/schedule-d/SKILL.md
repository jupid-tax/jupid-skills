---
name: schedule-d
description: >
  Use this skill when an individual filer needs to aggregate capital gains and
  losses for the tax year and produce IRS Schedule D (Form 1040). Triggers on
  phrases like "fill out Schedule D", "capital gains tax", "report stock
  sales", "long-term vs short-term capital gains", "capital loss carryover",
  "net capital gain", "capital gain rate 0/15/20%", "$3,000 loss limit",
  "NIIT 3.8%", "carry forward capital loss".
  Do NOT use for: an individual transaction (use form-8949 — that detail feeds
  INTO Schedule D); business asset sale (use Form 4797 — different form for
  §1231 property used in a trade or business); rental real estate (Schedule E
  for ongoing operations; sale of rental real estate is Form 4797 → §1231 →
  Schedule D Line 11); like-kind exchange of real property (Form 8824); §1256
  contracts marked-to-market (Form 6781); a primary residence sale fully
  excluded under §121 ($250k single / $500k MFJ); activity inside an IRA,
  401(k), HSA, or 529 (no recognition).
form: Schedule D (Form 1040)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1040sd.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040sd.pdf
---

# Schedule D (Form 1040) — Capital Gains and Losses

This skill produces an audit-grade draft of Schedule D from the user's Form 8949 totals, prior-year carryovers, and any K-1 / 1099-DIV capital gain distributions. It computes Part I (short-term), Part II (long-term), and Part III (summary), applies the IRC §1211 loss limit, builds the Capital Loss Carryover Worksheet for next year, and routes the result to the correct tax computation worksheet (Qualified Dividends and Capital Gain Tax Worksheet vs Schedule D Tax Worksheet).

The math is mechanical. The judgment is in **picking the right tax worksheet**, **classifying §1231 vs capital gain correctly**, **tracking carryover by short/long character**, and **flagging NIIT exposure**. The skill optimizes for these — when a fact is missing, the agent asks rather than guesses.

**Companion guide for end users:** [Schedule D (Form 1040) + AI Agent Skill: Capital Gains and Losses Guide 2026](https://jupid.com/blog/schedule-d-capital-gains-losses-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user has just produced or has Form 8949 totals to roll up (Box A through F)
- The user has 1099-DIV Box 2a (capital gain distributions) — even with no Form 8949 entries, those flow to Schedule D Line 13
- The user has a prior-year capital loss carryover and needs to apply it
- The user has K-1 capital gain pass-through from a partnership, S-corp, estate, or trust
- The user is asking how to compute capital gains tax at the 0/15/20% rates, or how to handle §1250 unrecaptured gain or 28% collectibles gain
- The user is asking about the $3,000 loss limit, capital loss carryforward, or NIIT 3.8%
- The user mentions Schedule D, "capital gain summary form", "1040 capital gains", or "report my net gain"

Do **not** engage this skill when:

- The user is itemizing individual transactions and has not yet completed Form 8949 → run [`forms/form-8949`](../form-8949/SKILL.md) first; come back to this skill once they have totals
- The user sold business-use property (e.g., equipment from a Schedule C operation) → that goes on Form 4797 first; only the net §1231 gain after recapture flows to Schedule D Line 11
- The user is reporting rental real estate operations → Schedule E
- The user is reporting like-kind exchange of real property → Form 8824
- The user has §1256 contracts (futures, broad-based index options) → Form 6781 first, then 60% long-term / 40% short-term to Schedule D
- The user's only capital gain is a primary residence sale fully excluded under §121
- The user is a partnership, S-corp, or C-corp at the entity level (capital gains pass through differently)

If the user mentions Form 8949 detail and Schedule D summary in the same conversation, run the 8949 skill first to produce totals, then this skill to summarize.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop.

1. **Tax year** the return covers. Affects which inflation-adjusted LTCG brackets apply (0/15/20% thresholds change yearly per Rev. Proc.).
2. **Filer's legal name and SSN/ITIN.** Used in the Schedule D header.
3. **Filing status** — single, MFJ, MFS, HoH, qualifying surviving spouse. Determines LTCG bracket cutoffs and the loss limit ($3,000 vs $1,500 MFS).
4. **Form 8949 totals by box** — for each of Boxes A, B, C (Part I) and Boxes D, E, F (Part II): column (d) proceeds total, column (e) basis total, column (g) adjustment total, column (h) net gain/loss total.
5. **1099-DIV Box 2a totals** — capital gain distributions from mutual funds and REITs. Always treated as long-term regardless of fund holding period; flow to Schedule D Line 13.
6. **K-1 capital gain boxes** — short-term and long-term capital gain pass-through from partnerships (Form 1065 K-1 Box 8/9a), S-corps (Form 1120-S K-1 Box 7/8a), estates and trusts (Form 1041 K-1 Box 3/4a). Lines 5 and 12 of Schedule D.
7. **Prior-year capital loss carryover** if any. Ask: "Did you have a net capital loss last year that you couldn't fully use against ordinary income (limit $3,000 / $1,500 MFS)? If yes, what was the short-term carryforward and the long-term carryforward from last year's Capital Loss Carryover Worksheet?"
8. **§1231 net gain from Form 4797**, if any — converted to long-term capital gain and lands on Schedule D Line 11.
9. **§1256 contract result from Form 6781** — 60% long-term, 40% short-term split; flows to Schedule D Lines 4 and 11.
10. **§1250 unrecaptured gain** — if real estate with prior depreciation was sold, the depreciation portion routes through the Unrecaptured §1250 Gain Worksheet to Line 19 (taxed at 25% max).
11. **28% rate gain** — collectibles (8949 code "C") and §1202 QSBS gain not fully excluded; routes through 28% Rate Gain Worksheet to Line 18 (taxed at 28% max).
12. **Modified AGI** — needed to determine NIIT exposure ($200K single / $250K MFJ threshold). If MAGI is at or near threshold, Form 8960 is also in scope.
13. **Qualified dividends** from Form 1099-DIV Box 1b — needed only for the tax-rate computation worksheet, but materially affects which worksheet is used.

For each input the user can't produce, **stop and ask** — Schedule D's accuracy depends entirely on the upstream detail.

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm filing scope

Confirm the user is filing as an individual reporting personal capital gain and loss activity. Redirect partnership/S-corp/C-corp scenarios.

Confirm the activity is *not* exclusively inside tax-advantaged accounts (IRA, 401(k), HSA, 529).

Confirm Form 8949 has been completed (or is being completed in parallel) — Schedule D is the summary; Form 8949 is the detail.

### Step 2 — Inventory all inputs

Build an internal table of every source feeding Schedule D:

```
| Source                          | Schedule D Line | ST/LT |
|---------------------------------|-----------------|-------|
| Form 8949 Box A net (h)         | 1b              | ST    |
| Form 8949 Box B net (h)         | 2               | ST    |
| Form 8949 Box C net (h)         | 3               | ST    |
| Form 6252 ST installment        | 4               | ST    |
| Form 6781 ST portion (40%)      | 4               | ST    |
| K-1 Box 8 ST cap gain           | 5               | ST    |
| Prior-year ST loss carryover    | 6               | ST    |
| Form 8949 Box D net (h)         | 8b              | LT    |
| Form 8949 Box E net (h)         | 9               | LT    |
| Form 8949 Box F net (h)         | 10              | LT    |
| Form 4797 §1231 net gain        | 11              | LT    |
| Form 6252 LT installment        | 11              | LT    |
| Form 6781 LT portion (60%)      | 11              | LT    |
| Form 8824 like-kind boot        | 11              | LT    |
| K-1 Box 9a / 4a LT cap gain     | 12              | LT    |
| 1099-DIV Box 2a distributions   | 13              | LT    |
| Prior-year LT loss carryover    | 14              | LT    |
```

If the user can't produce any input that should exist, stop and ask.

### Step 3 — Compute Part I (Short-Term)

Sum Lines 1a through 6 to produce **Line 7** (Net short-term capital gain or loss).

Decision: If the user has Box A transactions with **no adjustments** (no wash sale, no basis correction), they may aggregate on Line 1a instead of Line 1b. Otherwise itemize on Form 8949 → Line 1b.

### Step 4 — Compute Part II (Long-Term)

Sum Lines 8a through 14 to produce **Line 15** (Net long-term capital gain or loss).

Same Line 8a aggregation rule for Box D transactions with no adjustments.

### Step 5 — Compute Part III (Summary)

```
Line 16 = Line 7 + Line 15
```

**Branch A — Both Lines 15 and 16 are gains (Line 17 = Yes):**

- Compute **Line 18** (28% Rate Gain Worksheet result) from any collectibles gain (8949 code "C") or §1202 partial-exclusion gain (8949 code "Q"). If none, Line 18 = 0.
- Compute **Line 19** (Unrecaptured §1250 Gain Worksheet result) from any real estate depreciation recapture. If none, Line 19 = 0.
- If Line 18 > 0 or Line 19 > 0 → use **Schedule D Tax Worksheet** (in Schedule D instructions).
- If Line 18 = 0 and Line 19 = 0 → use **Qualified Dividends and Capital Gain Tax Worksheet** (in Form 1040 instructions). Most retail filers land here.

**Branch B — Line 16 is a loss:**

- Apply the **IRC §1211 limit** at Line 21: enter the smaller of (a) Line 16 as a positive number, or (b) $3,000 ($1,500 MFS).
- The capped amount lands on Form 1040 Line 7 as a negative number (reducing ordinary income).
- The remainder flows to the Capital Loss Carryover Worksheet for next year, retaining short-term and long-term character.

**Branch C — Line 16 is zero or Line 15 is a loss but Line 16 is positive (rare):**

- Use the regular tax tables or Qualified Dividends and Capital Gain Tax Worksheet depending on whether qualified dividends exist.

### Step 6 — Run the appropriate tax-rate worksheet

The agent should compute the worksheet result, not just point to it.

**Qualified Dividends and Capital Gain Tax Worksheet** (Form 1040 instructions): Stacks long-term gain + qualified dividends on top of ordinary income. The portion within the 0% LTCG bracket is taxed at 0%; portion in the 15% bracket at 15%; portion in the 20% bracket at 20%. Ordinary income is taxed at regular rates.

**Schedule D Tax Worksheet** (Schedule D instructions): Layers four rate buckets — ordinary, 25% (Line 19 §1250), 28% (Line 18 collectibles), and 0/15/20% (remaining net gain). Used only when Line 18 or 19 is positive.

Use [`references/tax-rate-worksheets.md`](./references/tax-rate-worksheets.md) for the step-by-step.

### Step 7 — Compute NIIT exposure (Form 8960)

If MAGI exceeds $200,000 single / $250,000 MFJ / $125,000 MFS:

```
NIIT base = MIN(Net Investment Income, MAGI − threshold)
NIIT     = NIIT base × 3.8%
```

Net Investment Income includes net capital gain (Schedule D Line 16, capped at zero — a net loss does not produce a negative NIIT base). Form 8960 is required and routes the NIIT to Schedule 2 → Form 1040.

The thresholds are not indexed for inflation under IRC §1411 — verify they remain the statutory $200K / $250K / $125K.

### Step 8 — Build the Capital Loss Carryover Worksheet (if Line 16 is a loss)

The worksheet (in Schedule D instructions) computes:
- **Short-term carryforward** to next year = unused short-term loss after offsetting long-term gain and the $3,000 ordinary-income deduction
- **Long-term carryforward** to next year = unused long-term loss after offsetting short-term gain and the $3,000 ordinary-income deduction

Order of absorption: short-term loss first absorbs $3,000 ordinary-income limit; remainder of short-term offsets long-term gain. Long-term loss does the inverse.

See [`references/loss-carryover.md`](./references/loss-carryover.md) for full mechanics.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms the user will need:

- **Form 1040 Line 7** — Schedule D Line 16 (if positive) or Line 21 (if loss, capped)
- **Form 8960** — Net Investment Income Tax (3.8%) if MAGI exceeds the threshold
- **Capital Loss Carryover Worksheet** — save with this year's records for use next year
- **Form 4797** — if any business-use property was sold, must be completed before Schedule D Line 11
- **Form 6781** — if any §1256 contracts traded
- **Form 8824** — if any §1031 like-kind exchange
- **State return** — most states tax capital gain at the ordinary income rate (no preferential federal-style rate). Carryforward rules differ from federal in some states (e.g., California, New Jersey).

### Step 12 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md) for the browser-automation playbook covering FFFF, IRS Direct File, paid software, and paper-filing options.

---

## Line-by-line guidance

For full detail, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name and SSN** — must match Form 1040 exactly
- Schedule D is identified by tax year; ensure the form revision corresponds to the year being filed

### Part I — Short-Term (Lines 1a-7)

| Line | Source | Notes |
|------|--------|-------|
| 1a | Box A 1099-B aggregate | Optional; only if no adjustments |
| 1b | 8949 Box A totals | (d), (e), (g), (h) |
| 2  | 8949 Box B totals | Basis NOT reported |
| 3  | 8949 Box C totals | No 1099-B |
| 4  | Forms 6252, 6781 (40%), 8824, etc. | Short-term portion |
| 5  | K-1 short-term cap gain | Schedule K-1 |
| 6  | Prior-year ST carryover | Negative number |
| 7  | Net short-term | Sum |

### Part II — Long-Term (Lines 8a-15)

| Line | Source | Notes |
|------|--------|-------|
| 8a | Box D 1099-B aggregate | Optional; only if no adjustments |
| 8b | 8949 Box D totals | (d), (e), (g), (h) |
| 9  | 8949 Box E totals | Basis NOT reported |
| 10 | 8949 Box F totals | No 1099-B |
| 11 | Forms 4797 §1231, 6252 LT, 6781 (60%), 8824 LT | Long-term portion |
| 12 | K-1 long-term cap gain | Schedule K-1 |
| 13 | 1099-DIV Box 2a | Always long-term |
| 14 | Prior-year LT carryover | Negative number |
| 15 | Net long-term | Sum |

### Part III — Summary (Lines 16-22)

| Line | Calculation | Notes |
|------|-------------|-------|
| 16 | Line 7 + Line 15 | Total |
| 17 | Are 15 and 16 both gains? | Yes/No branch |
| 18 | 28% Rate Gain Worksheet | Collectibles, §1202 partial |
| 19 | Unrecaptured §1250 Gain Worksheet | Real estate depreciation |
| 20 | Use which worksheet? | Branch on Line 18/19 |
| 21 | Loss limit ($3,000 / $1,500 MFS) | Only if Line 16 < 0 |
| 22 | Qualified dividends consideration | Routes to right worksheet |

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] Line 1b column (h) = sum of Box A pages on Form 8949
- [ ] Line 2 column (h) = sum of Box B pages
- [ ] Line 3 column (h) = sum of Box C pages
- [ ] Line 7 = Line 1a (h) + Line 1b (h) + Line 2 (h) + Line 3 (h) + Line 4 + Line 5 + Line 6
- [ ] Line 8b column (h) = sum of Box D pages
- [ ] Line 9 column (h) = sum of Box E pages
- [ ] Line 10 column (h) = sum of Box F pages
- [ ] Line 15 = Line 8a (h) + Line 8b (h) + Line 9 (h) + Line 10 (h) + Line 11 + Line 12 + Line 13 + Line 14
- [ ] Line 16 = Line 7 + Line 15
- [ ] If Line 16 < 0: Line 21 = MIN(absolute value of Line 16, $3,000 or $1,500 MFS)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 16 is a loss greater than $3,000 ($1,500 MFS) → confirm Capital Loss Carryover Worksheet has been built and saved
- [ ] Filing status MFS but Line 21 = $3,000 → should be $1,500
- [ ] Line 13 (capital gain distributions) > 0 but no 1099-DIV Box 2a in user's records → reconcile
- [ ] Line 6 or Line 14 is positive → carryovers are always negative; positive value indicates a sign error
- [ ] Prior-year carryover entered without a corresponding prior-year worksheet → ask user to produce the worksheet
- [ ] Line 18 (28% rate) > 0 but no Form 8949 entry with code "C" or "Q" → reconcile
- [ ] Line 19 (§1250) > 0 but no real estate sale on Form 8949 / 4797 → reconcile
- [ ] Line 18 or 19 > 0 and the agent used the Qualified Dividends and Capital Gain Tax Worksheet → must use Schedule D Tax Worksheet instead
- [ ] MAGI > $200K single / $250K MFJ but Form 8960 is not on the to-do list → add NIIT
- [ ] §1231 gain on Line 11 but no Form 4797 in attachments → must attach 4797
- [ ] Long-term loss > 0 and short-term gain > 0 → losses absorb gains *within* the same character first; verify Line 7 and Line 15 reflect the right netting per the form's literal addition (the netting happens at Line 16, but ordering matters for worksheet computation)

### Cross-form checks

- [ ] Schedule D Line 16 reconciles to Form 1040 Line 7 (gain) or Form 1040 Line 7 reflecting Line 21 (loss capped)
- [ ] If Form 8949 has any entry, Schedule D must be filed
- [ ] If §1256 contracts on Form 6781, the 60/40 split flows to Lines 4 (40% ST) and 11 (60% LT)
- [ ] If QSBS exclusion claimed on 8949 (code Q or X), the excluded portion is in column (g); only the included portion (if any) flows to Schedule D
- [ ] If state return is California or New Jersey, capital loss carryforward rules differ from federal — flag for state-return preparation

---

## Output format

The deliverable is a **filled draft** the user can transcribe to paper Schedule D or paste into tax software.

```markdown
# Schedule D (Form 1040) — DRAFT for tax year YYYY

## Filer
Name: <legal name>
SSN: <SSN>
Filing status: <single | MFJ | MFS | HoH | QSS>

## Part I — Short-Term Capital Gains and Losses

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 1a   | Box A aggregate | $X | $X |  | $X |
| 1b   | Box A 8949 totals | $X | $X | $X | $X |
| 2    | Box B 8949 totals | $X | $X | $X | $X |
| 3    | Box C 8949 totals | $X | $X | $X | $X |
| 4    | Forms 6252 / 6781 / 8824 ST |   |   |   | $X |
| 5    | K-1 short-term cap gain |   |   |   | $X |
| 6    | Prior-year ST loss carryover |   |   |   | ($X) |
| **7**| **Net short-term gain/loss** |   |   |   | **$X** |

## Part II — Long-Term Capital Gains and Losses

| Line | Description | (d) Proceeds | (e) Basis | (g) Adj | (h) Gain/Loss |
|------|-------------|--------------|-----------|---------|---------------|
| 8a   | Box D aggregate | $X | $X |  | $X |
| 8b   | Box D 8949 totals | $X | $X | $X | $X |
| 9    | Box E 8949 totals | $X | $X | $X | $X |
| 10   | Box F 8949 totals | $X | $X | $X | $X |
| 11   | Forms 4797 §1231 / 6252 / 6781 / 8824 LT |   |   |   | $X |
| 12   | K-1 long-term cap gain |   |   |   | $X |
| 13   | Capital gain distributions (1099-DIV 2a) |   |   |   | $X |
| 14   | Prior-year LT loss carryover |   |   |   | ($X) |
| **15**| **Net long-term gain/loss** |   |   |   | **$X** |

## Part III — Summary

| Line | Description | Amount |
|------|-------------|--------|
| 16 | Line 7 + Line 15 | $X |
| 17 | Both Lines 15 and 16 are gains? | Yes / No |
| 18 | 28% rate gain (worksheet result) | $X |
| 19 | Unrecaptured §1250 gain (worksheet result) | $X |
| 20 | Use Schedule D Tax Worksheet? | Yes / No |
| 21 | Capital loss limitation (if Line 16 < 0) | ($X) [max $3,000 / $1,500 MFS] |

→ Form 1040 Line 7: $X (or capped loss from Line 21)

## Tax-rate computation

Using: <Qualified Dividends and Capital Gain Tax Worksheet | Schedule D Tax Worksheet | Tax tables>

| Component | Amount | Rate | Tax |
|-----------|--------|------|-----|
| Long-term gain in 0% bracket | $X | 0% | $0 |
| Long-term gain in 15% bracket | $X | 15% | $X |
| Long-term gain in 20% bracket | $X | 20% | $X |
| 28% rate gain (Line 18) | $X | 28% | $X |
| §1250 unrecaptured (Line 19) | $X | 25% | $X |
| Ordinary income | $X | <bracket> | $X |
| **Total federal tax** | | | **$X** |

## NIIT (Form 8960) — if applicable

MAGI: $X
NIIT threshold (filing status): $X
Net Investment Income: $X
NIIT base: MIN(NII, MAGI − threshold) = $X
NIIT (3.8%): $X
→ Schedule 2 Line 12

## Capital Loss Carryover Worksheet (if Line 16 < 0)

| Carryforward to next year | Amount |
|---------------------------|--------|
| Short-term carryforward | ($X) |
| Long-term carryforward | ($X) |

## Required attachments and downstream forms

- [ ] Form 8949 (all pages, all boxes used)
- [ ] Form 8960 (if MAGI > NIIT threshold)
- [ ] Form 6781 (if §1256 contracts)
- [ ] Form 4797 (if §1231 business property)
- [ ] Form 8824 (if §1031 like-kind exchange)
- [ ] Capital Loss Carryover Worksheet (saved for next year)

## Validation summary

- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Worksheet used: <name>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft

- IRS Schedule D (Form 1040) (revision date YYYY-MM-DD)
- IRS Instructions for Schedule D (revision date YYYY-MM-DD)
- IRC §1(h) (capital gain rate structure), §1211 (loss limit), §1212 (carryover), §1411 (NIIT), §1202 (QSBS), §1231 (business property), §1250 (real estate recapture)
- Rev. Proc. 2024-40 (2025 inflation-adjusted brackets — verify 2026 against most recent Revenue Procedure)
- Pub 550 (Investment Income and Expenses)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Schedule D. The deliverable's value is that every line is computed and traceable, with the right tax worksheet selected.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every Schedule D line: Part I (1a–7), Part II (8a–15), Part III (16–22) with examples
- [`references/tax-rate-worksheets.md`](./references/tax-rate-worksheets.md) — Qualified Dividends and Capital Gain Tax Worksheet vs Schedule D Tax Worksheet: when to use each, step-by-step
- [`references/loss-carryover.md`](./references/loss-carryover.md) — IRC §1211 / §1212: $3,000 limit, indefinite carryforward, Capital Loss Carryover Worksheet mechanics, character preservation
- [`references/niit.md`](./references/niit.md) — IRC §1411: 3.8% NIIT computation on Form 8960, MAGI thresholds, what counts as net investment income
- [`references/special-rates.md`](./references/special-rates.md) — 28% collectibles rate, 25% §1250 unrecaptured gain, §1202 QSBS exclusion mechanics
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 8-10 mistakes filers make and how the skill avoids them
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Schedule D + Form 8949 via FFFF, IRS Direct File, paid software, or paper

## Examples

- [`examples/day-trader-with-stocks-and-crypto.md`](./examples/day-trader-with-stocks-and-crypto.md) — Sam from the blog: net ST loss + net LT gain, 15% LTCG bracket, NIIT exposure
- [`examples/big-loss-year-with-carryover.md`](./examples/big-loss-year-with-carryover.md) — Investor with $25,000 net loss; $3,000 absorbed against ordinary income; $22,000 carryover by character
- [`examples/real-estate-sale-with-1250.md`](./examples/real-estate-sale-with-1250.md) — Rental property sold; depreciation recapture at 25%; remainder at 0/15/20%; uses Schedule D Tax Worksheet

## Sources

- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [About Schedule D (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-d-form-1040)
- [Form 8949](https://www.irs.gov/pub/irs-pdf/f8949.pdf) — feeds Schedule D
- [Form 8960](https://www.irs.gov/pub/irs-pdf/f8960.pdf) — Net Investment Income Tax
- [Form 4797](https://www.irs.gov/pub/irs-pdf/f4797.pdf) — Sales of Business Property
- [Form 6781](https://www.irs.gov/pub/irs-pdf/f6781.pdf) — §1256 Contracts and Straddles
- [Form 8824](https://www.irs.gov/pub/irs-pdf/f8824.pdf) — Like-Kind Exchanges
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
- [Publication 544](https://www.irs.gov/publications/p544) — Sales and Other Dispositions of Assets
- [Publication 551](https://www.irs.gov/publications/p551) — Basis of Assets
- IRC §1(h), §1211, §1212, §1411, §1202, §1231, §1250
- Rev. Proc. 2024-40 — 2025 inflation adjustments (verify 2026 against the most recent Revenue Procedure)
- [Schedule D Capital Gains Guide on Jupid](https://jupid.com/blog/schedule-d-capital-gains-losses-2026) — narrative companion

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. The agent invoking this skill should remind the user that the output is a draft and that complex situations — particularly involving §1202 QSBS exclusion, §1250 real estate, large carryovers, or NIIT planning — warrant a licensed tax professional's review.
