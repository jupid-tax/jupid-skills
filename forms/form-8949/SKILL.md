---
name: form-8949
description: >
  Use this skill when an individual filer needs to report sales or dispositions
  of capital assets — stocks, ETFs, mutual funds, bonds, cryptocurrency, NFTs,
  collectibles, or investment real estate — on IRS Form 8949. Triggers on
  phrases like "fill out Form 8949", "report stock sales", "report crypto on
  taxes", "capital gains tax form", "where do I report Bitcoin gains", "wash
  sale", "1099-B reporting", "schedule d 8949", "report NFT sale".
  Do NOT use for: regular dividends or qualified dividends (those go on
  Schedule B); bond interest or savings interest (Schedule B); sales of
  property used in a trade or business (Form 4797 — different skill);
  transactions inside an IRA, 401(k), HSA, or 529 (tax-deferred or tax-free,
  no 8949 required); a primary residence sale that fully qualifies for the
  §121 exclusion ($250k single / $500k MFJ).
form: Form 8949
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f8949.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i8949.pdf
---

# Form 8949 — Sales and Other Dispositions of Capital Assets

This skill produces an audit-grade draft of Form 8949 from the user's brokerage 1099-Bs and crypto exchange records. It groups transactions into the correct Boxes (A/B/C for short-term, D/E/F for long-term), applies wash sale adjustments, computes per-row gain or loss, sums each box, and rolls totals to Schedule D.

The math is mechanical. The judgment is in **box selection**, **wash sale identification across accounts**, and **basis reconstruction for crypto and non-covered shares**. The skill optimizes for the latter — when a fact is missing, the agent asks rather than guesses.

**Companion guide for end users:** [Form 8949 (2026): Capital Gains, Stocks, and Crypto Reporting Guide](https://jupid.com/blog/form-8949-capital-gains-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8949, Schedule D, "capital gains form", or "report my stock sales"
- The user describes a taxable disposition of a capital asset: sold stocks, sold ETF/mutual fund shares, swapped crypto, sold an NFT, sold a rental property
- The user has 1099-B, 1099-DA, or crypto-exchange CSVs and is asking how to report them
- The user is asking about wash sales, holding period (short vs long-term), or capital loss carryover

Do **not** engage this skill when:

- The user is reporting only dividends or interest → use Schedule B (forthcoming `schedule-b` skill)
- The user is reporting business-property sales (e.g., sold a piece of equipment from their Schedule C business) → use Form 4797 (forthcoming `form-4797` skill)
- The user is reporting like-kind exchange (§1031) of real property → that's Form 8824, not 8949
- The user has activity only inside tax-advantaged accounts (IRA, 401(k), HSA, 529) — no 8949 required
- The user sold their primary residence and the gain is below the §121 exclusion — no 8949 required
- The user is a partnership, S-corp, or C-corp — capital gains pass through differently

If the user mentions both 8949-eligible assets and Form 4797 assets in the same conversation, run this skill for the 8949 portion and hand off the 4797 portion.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop.

1. **Tax year** the return covers. Affects which inflation-adjusted brackets apply (long-term capital gain 0/15/20% thresholds change yearly).
2. **Filer's legal name and SSN/ITIN.** Used in the Form 8949 header.
3. **All 1099-B forms** received from brokerages. Each 1099-B itself indicates the box (A/B/D/E based on whether basis was reported to the IRS). Pull from every taxable account, including any closed during the year.
4. **All 1099-DA, 1099-MISC, and exchange CSVs** for crypto activity. CSV exports are the source of truth for basis when no 1099-B was issued.
5. **Transaction-level data**, structured as: per-lot acquired date, sold date, proceeds, basis, asset description, plus any broker-flagged adjustments (wash sale, accrued market discount, etc.).
6. **Wash sale awareness** across accounts. Ask: "Did you take a loss on a security in any account, then buy the same or substantially identical security within 30 days in **any** other account, including IRAs or your spouse's accounts?" Brokers only catch in-account washes.
7. **Prior-year capital loss carryover** if any. Ask: "Did you have a net capital loss last year that you couldn't fully use?" If yes, the prior-year Capital Loss Carryover Worksheet result is the input.

For each transaction, the agent must classify:
- **Short-term or long-term?** Acquired date + 1 day to sold date. >365 days = long-term.
- **Basis reported on 1099-B?** Reported → A or D. Not reported → B or E. No 1099-B issued → C or F.
- **Wash sale applicable?** Loss + replacement purchase within 30 days = code W.
- **Asset type adjustment?** Collectibles get code "C" (28% rate); §1202 QSBS gets code "Q" or "X"; etc. Full code list in [`references/line-by-line.md`](./references/line-by-line.md).

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm filing scope

Confirm the user is filing as an individual reporting personal capital asset dispositions. Redirect partnership/S-corp/C-corp scenarios.

Confirm none of the activity is inside an IRA/401(k)/HSA/529. Those accounts don't generate 8949 entries.

### Step 2 — Gather and inventory all 1099-Bs and exchange records

Ask the user to list every brokerage and crypto exchange they used during the year. For each, pull:
- 1099-B (or 1099-DA, or note "no 1099-B issued")
- Year-end summary or full transaction CSV

Build an internal table:

```
| Source         | Form        | Tax box implication  |
|----------------|-------------|----------------------|
| Schwab         | 1099-B      | A/D for covered       |
| Fidelity       | 1099-B      | A/D for covered       |
| Coinbase       | 1099-MISC + CSV | C/F (no 1099-B)   |
| Kraken         | CSV only    | C/F                  |
```

If the user can't produce records from one source, **stop and ask** — reconstruction from memory is unreliable for capital gains.

### Step 3 — Classify each transaction into a Box

For each transaction, determine:

```
Holding period (acquired+1 → sold):
  ≤ 365 days → Part I (short-term)
  > 365 days → Part II (long-term)

Basis reporting status (from 1099-B or CSV):
  1099-B with basis reported   → Box A (short) or D (long)
  1099-B with basis NOT reported → Box B (short) or E (long)
  No 1099-B issued at all      → Box C (short) or F (long)
```

Produce a working table grouped by box:

```
Box D (long-term, basis reported):
  | Description | Acquired | Sold | Proceeds | Basis | Code | Adj | Gain/Loss |
  | ...         | ...      | ...  | ...      | ...   | ...  | ... | ...       |
```

### Step 4 — Identify and code wash sales

For each loss transaction, check whether the user (or spouse, or any of their accounts including IRAs) bought "substantially identical" security within 30 days before or 30 days after the sale.

If yes:
- Code "W" in column (f)
- Disallowed loss as a positive number in column (g)
- Column (h) = (d) − (e) + (g) — typically zero or a small remainder
- The disallowed amount is added to the basis of the replacement lot. Note this for future-year tracking.

If the wash sale moves the loss into an IRA-purchased replacement, the disallowed loss is **permanently lost** (the IRA has no taxable basis to absorb it). Surface this as a warning to the user.

For crypto wash sales: as of tax year 2025, IRC §1091 has not been extended to digital assets, so wash sale rule does not currently apply to crypto. **Verify the current rule each year before relying on this** — proposals to extend §1091 to crypto have been made multiple times. See [`references/wash-sales.md`](./references/wash-sales.md).

### Step 5 — Apply other column (f) adjustment codes

Common codes the agent may need to apply:

| Code | When to use |
|------|-------------|
| **W** | Wash sale loss disallowed |
| **B** | Basis reported on 1099-B is incorrect (correction needed in column (g)) |
| **T** | 1099-B reported wrong type or holding period (correction in column (g)) |
| **D** | Accrued market discount on a debt instrument (ordinary income carve-out) |
| **L** | Nondeductible loss other than wash sale (e.g., loss on personal-use property) |
| **C** | Collectibles — gain taxed at maximum 28% (informs Schedule D, not 8949 math) |
| **Q** | §1202 QSBS exclusion — partial gain excluded |
| **X** | §1202 QSBS — fully excluded |

Full code table with examples in [`references/line-by-line.md`](./references/line-by-line.md).

### Step 6 — Compute per-row gain/loss and box subtotals

For each row: column (h) = (d) proceeds − (e) basis + (g) adjustment.

For each box: sum the column (h) values. These subtotals carry to Schedule D.

### Step 7 — Roll subtotals to Schedule D

```
Schedule D:
  Line 1b (Box A totals):  __
  Line 2  (Box B totals):  __
  Line 3  (Box C totals):  __
  Line 7  Net short-term capital gain/loss:  __

  Line 8b (Box D totals):  __
  Line 9  (Box E totals):  __
  Line 10 (Box F totals):  __
  Line 15 Net long-term capital gain/loss:   __

  Line 16 Total = Line 7 + Line 15  → Form 1040 Line 7
```

If net loss > $3,000 ($1,500 MFS), apply $3,000 against ordinary income; carry the rest to next year using the Schedule D Capital Loss Carryover Worksheet.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State the next forms the user will need:

- **Schedule D** is mandatory whenever Form 8949 has any entry — the totals roll up there
- **Form 1040 Line 7** — net capital gain/loss from Schedule D Line 16
- **Form 8960** — Net Investment Income Tax (3.8%) if MAGI exceeds $200K single / $250K MFJ
- **Form 6781** — if any §1256 contracts (futures, broad-based index options) were disposed
- **Form 8824** — if any like-kind real estate exchange (§1031) occurred separately
- **Capital Loss Carryover Worksheet** — if net loss exceeds the $3,000 annual limit, save the worksheet for next year
- **State return** — most states tax capital gains at the ordinary income rate (no preferential rate); carryforward rules differ from federal in some states

### Step 11 — File the return (optional)

If the user authorizes filing, follow [`filing.md`](./filing.md) for the browser-automation playbook covering FFFF, paid software, and paper-filing options.

---

## Line-by-line guidance

For full detail, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name and SSN** at the top of every page used
- **Box checkbox** at the top of each Part I and Part II — check exactly one box (A, B, C for Part I; D, E, F for Part II) per page. If you have transactions across multiple boxes, use a separate page (or set of pages) for each box.

### Columns

| Col | Label | What goes here |
|-----|-------|----------------|
| (a) | Description | "100 sh AAPL", "0.5 BTC", "1,000 sh VTSAX" |
| (b) | Date acquired | Mm/dd/yyyy of original purchase. Use "VARIOUS" if multiple lots aggregated. Use "INHERITED" for inherited assets (always long-term). |
| (c) | Date sold | Mm/dd/yyyy |
| (d) | Proceeds | Net sale proceeds (gross minus selling commissions if 1099-B reported gross) |
| (e) | Cost or other basis | Adjusted basis. Crypto: original USD cost + reinvested rewards basis. Inherited: stepped-up FMV per §1014. |
| (f) | Code(s) | Adjustment codes: W, B, T, D, L, C, Q, X, S, N, H, R, etc. (See [`references/line-by-line.md`](./references/line-by-line.md)) |
| (g) | Amount of adjustment | Dollar amount tied to the code in (f). Positive number — the form formula does the sign work. |
| (h) | Gain or (loss) | (d) − (e) + (g). Losses in parentheses. |

### Page totals

Each page sums column (d), (e), (g), (h) at the bottom. The page totals are what flow to Schedule D.

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] For each row: column (h) = (d) − (e) + (g)
- [ ] Each page total in (d), (e), (g), (h) matches the sum of the rows
- [ ] Box A and Box D totals match the corresponding 1099-B Box 1d (proceeds) totals brokerage-by-brokerage. The IRS computer reconciles this.
- [ ] Schedule D Line 7 = sum of Box A, B, C net amounts
- [ ] Schedule D Line 15 = sum of Box D, E, F net amounts
- [ ] Schedule D Line 16 = Line 7 + Line 15

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] A loss reported without code "W" but the user has another account or spouse account where they bought the same security within 30 days → ask about wash sale
- [ ] Crypto disposition reported with no 1099-B and basis = proceeds (i.e., the user "doesn't know" basis and defaulted to a wash) → ask for the original purchase record; CSV from the exchange usually has this
- [ ] Long-term coded but holding period is exactly 365 days or less → that's short-term, recheck dates
- [ ] Box B or E entry where the user *received* a 1099-B with basis reported → that should be Box A or D
- [ ] Box A or D entry where the user did *not* receive a 1099-B → that should be Box C or F
- [ ] Net loss > $3,000 ($1,500 MFS) — confirm carryover to next year is recorded
- [ ] Aggregate proceeds total across all boxes > $1M — encourage the user to file Form 8938 / FBAR if any of the activity was through foreign accounts
- [ ] Date acquired = "INHERITED" but the asset is being reported as short-term → all inherited assets are long-term per §1223(9)
- [ ] Like-kind exchange flagged but reported on 8949 → that goes on Form 8824, not 8949
- [ ] Wash sale disallowed loss applies to a purchase inside an IRA → permanent loss, surface to user

### Cross-form checks

- [ ] If digital asset question on Form 1040 is "Yes" but no Box C/F entries → reconcile (the question is also "Yes" for non-disposing receipt of digital assets, but most "Yes" answers should produce a 8949 entry)
- [ ] If MAGI > $200K single or $250K MFJ and net investment income > 0 → ensure Form 8960 is on the to-do list
- [ ] If §1256 contracts (futures, broad-based index options) traded → those generally go on Form 6781, not 8949
- [ ] If §1202 QSBS exclusion claimed → the gain still appears on 8949 with code Q or X and an adjustment in (g) for the excluded portion

---

## Output format

The deliverable is a **filled draft** the user can transcribe to paper Form 8949 or paste into tax software.

```markdown
# Form 8949 — DRAFT for tax year YYYY

## Filer
Name: <legal name>
SSN: <SSN>

## Part I — Short-Term Capital Gains and Losses (assets held ≤ 1 year)

### Box A — basis reported to IRS on 1099-B
| (a) Description | (b) Acquired | (c) Sold | (d) Proceeds | (e) Basis | (f) Code | (g) Adj | (h) Gain/Loss |
|-----------------|--------------|----------|--------------|-----------|----------|---------|---------------|
| ...             | ...          | ...      | ...          | ...       | ...      | ...     | ...           |
| **Box A totals**|              |          | $X,XXX       | $X,XXX    |          | $X,XXX  | $X,XXX        |

### Box B — basis NOT reported to IRS on 1099-B
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Box B totals** |  |  | $X,XXX | $X,XXX |  | $X,XXX | $X,XXX |

### Box C — no 1099-B received
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Box C totals** |  |  | $X,XXX | $X,XXX |  | $X,XXX | $X,XXX |

## Part II — Long-Term Capital Gains and Losses (assets held > 1 year)

### Box D — basis reported to IRS on 1099-B
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Box D totals** |  |  | $X,XXX | $X,XXX |  | $X,XXX | $X,XXX |

### Box E — basis NOT reported to IRS on 1099-B
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Box E totals** |  |  | $X,XXX | $X,XXX |  | $X,XXX | $X,XXX |

### Box F — no 1099-B received
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Box F totals** |  |  | $X,XXX | $X,XXX |  | $X,XXX | $X,XXX |

## Roll-up to Schedule D

| Schedule D Line | Source | Amount |
|-----------------|--------|--------|
| 1b | Box A net | $X,XXX |
| 2  | Box B net | $X,XXX |
| 3  | Box C net | $X,XXX |
| 7  | Net short-term | $X,XXX |
| 8b | Box D net | $X,XXX |
| 9  | Box E net | $X,XXX |
| 10 | Box F net | $X,XXX |
| 15 | Net long-term | $X,XXX |
| 16 | Total → Form 1040 Line 7 | $X,XXX |

## Wash sale tracking (carry to next year)
| Replacement lot | Original disallowed loss | New basis adjustment |
|-----------------|--------------------------|----------------------|
| ...             | ...                      | ...                  |

## Capital loss carryover (if applicable)
- Short-term carryforward to next year: $X,XXX
- Long-term carryforward to next year:  $X,XXX

## Required attachments and downstream forms
- [ ] Schedule D (always required when 8949 used)
- [ ] Form 8960 (if MAGI > NIIT threshold)
- [ ] Form 6781 (if any §1256 contracts)
- [ ] Form 8824 (if any §1031 like-kind exchange — separate from 8949)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 8949 (revision date YYYY-MM-DD)
- IRS Instructions for Form 8949 (revision date YYYY-MM-DD)
- IRS Schedule D and instructions
- IRC §1001 (gain/loss recognition), §1(h) (capital gain rates), §1091 (wash sales), §1211 (loss limit), §1212 (carryover), §1411 (NIIT)
- Notice 2014-21 (crypto as property), Rev. Rul. 2019-24 (hard forks)
- Rev. Proc. 2024-40 (2025 inflation-adjusted brackets — verify 2026 against most recent Rev. Proc.)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Schedule D + 8949. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Box A/B/C/D/E/F detailed; columns (a) through (h); full adjustment code table
- [`references/wash-sales.md`](./references/wash-sales.md) — IRC §1091 deep dive: substantially identical, 61-day window, cross-account traps, IRA permanent-loss trap
- [`references/crypto-reporting.md`](./references/crypto-reporting.md) — Notice 2014-21, Rev. Rul. 2019-24, hard forks, airdrops, staking, NFTs, DeFi, 1099-DA timing
- [`references/cost-basis-methods.md`](./references/cost-basis-methods.md) — FIFO, specific identification, average cost (mutual funds), HIFO for crypto
- [`references/holding-period.md`](./references/holding-period.md) — counting rules; gifted assets (carryover basis); inherited assets (stepped-up + always long-term)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 8-10 mistakes filers make and how the skill avoids them
- [`filing.md`](./filing.md) — Browser-automation playbook for filing 8949 + Schedule D via FFFF, paid software, or paper

## Examples

- [`examples/day-trader-with-stocks-and-crypto.md`](./examples/day-trader-with-stocks-and-crypto.md) — Sam from the blog: AAPL long-term gain (Box D), BTC long-term gain (Box F), NVDA wash sale (Box B), ETH short-term loss (Box C)
- [`examples/long-term-investor-with-mutual-funds.md`](./examples/long-term-investor-with-mutual-funds.md) — Retiree selling pre-2012 mutual fund shares; Box E reporting; average cost method
- [`examples/crypto-only-defi-user.md`](./examples/crypto-only-defi-user.md) — DeFi user with swaps, staking rewards, NFT trades; all Box C/F; reconstruction from on-chain data

## Sources

- [Form 8949 (latest)](https://www.irs.gov/pub/irs-pdf/f8949.pdf)
- [Instructions for Form 8949 (latest)](https://www.irs.gov/pub/irs-pdf/i8949.pdf)
- [About Form 8949](https://www.irs.gov/forms-pubs/about-form-8949)
- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Form 8960 — Net Investment Income Tax](https://www.irs.gov/pub/irs-pdf/f8960.pdf)
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
- [Publication 544](https://www.irs.gov/publications/p544) — Sales and Other Dispositions of Assets
- [Publication 551](https://www.irs.gov/publications/p551) — Basis of Assets
- [Notice 2014-21](https://www.irs.gov/pub/irs-drop/n-14-21.pdf) — Virtual Currency Guidance
- [Rev. Rul. 2019-24](https://www.irs.gov/pub/irs-drop/rr-19-24.pdf) — Hard fork and airdrop guidance
- IRC §1001, §1(h), §1014, §1091, §1211, §1212, §1411, §6045(g)
- Rev. Proc. 2024-40 — 2025 inflation adjustments (verify 2026 against the most recent Revenue Procedure)
- [Form 8949 Capital Gains Guide on Jupid](https://jupid.com/blog/form-8949-capital-gains-2026) — narrative companion

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. Cryptocurrency tax rules in particular are evolving — verify current guidance against the IRS website before filing. The agent invoking this skill should remind the user that the output is a draft and that complex situations warrant a licensed tax professional's review.
