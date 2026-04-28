# Holding Period

The holding period determines whether a gain or loss is short-term (taxed at ordinary rates) or long-term (preferential rates: 0/15/20%). Counting rules are precise — one day off and the entire tax treatment flips.

---

## The basic rule

> The holding period begins the **day after** the asset is acquired and ends on the **day** the asset is sold or disposed of.

Practical implications:

- **Long-term** = held **more than one year** (i.e., one year and one day)
- **Short-term** = held **one year or less**

The cutoff is exactly **one year and one day** of holding.

```
Buy on January 15, 2025.
Holding period starts January 16, 2025.

Sell on January 15, 2026 → holding period = 365 days → SHORT-TERM
Sell on January 16, 2026 → holding period = 366 days → LONG-TERM
```

The trade date (not settlement date) is what counts. For a stock that trades T+1 or T+2, the trade date is the date the order was executed, even though cash and shares change hands later.

---

## Why one day matters

```
$50,000 gain — single filer with $200K ordinary income (32% bracket)

Sold day 365: short-term @ 32% = $16,000 federal tax
Sold day 366: long-term  @ 15% = $7,500 federal tax

Difference: $8,500
```

The agent must verify holding period dates carefully. A common error: filers buy on Day X and assume "next year same day" qualifies as long-term — it doesn't. They need Day X + 1 year + 1 day, minimum.

---

## Special holding period rules

### Inherited assets (§1223(9))

**Always long-term**, regardless of how soon you sell after inheriting. Even if you inherit on March 1 and sell on March 2, it's long-term.

Basis is stepped up to FMV on date of death (or alternate valuation date if elected by the executor) under IRC §1014.

On Form 8949, column (b) shows "INHERITED" instead of a date.

### Gifted assets (§1223(2))

The donor's holding period **tacks on** to the donee's. If the donor held for 8 months and gives the asset, the donee starts at month 8 — a sale 5 months later would still be long-term (8 + 5 = 13 months).

Two exceptions:

- If FMV on gift date < donor's basis AND the donee later sells at a loss: the donee's holding period **starts on the gift date** (no tacking)
- If FMV on gift date < donor's basis AND the donee later sells at a price between FMV and donor's basis: no gain or loss; holding period is irrelevant

### Wash sale replacement lots

When a wash sale disallows a loss, the disallowed amount adds to the basis of the replacement lot, AND **the holding period of the original (sold) lot tacks back** to the replacement lot.

```
Buy 100 SPY on Nov 1, 2024.
Sell 100 SPY at a loss on Dec 15, 2025 (held 13.5 months — long-term).
Buy 100 SPY on Dec 28, 2025 (within 30 days → wash sale).

The Dec 28 lot's holding period starts Nov 1, 2024 (tacks back).
If sold any time after Dec 28, 2025, it's automatically long-term.
```

This is one of the few wash-sale "benefits" — the deferred loss is preserved AND the holding period continues.

### Like-kind exchanges (§1031)

The holding period of the relinquished property tacks on to the replacement property. Real estate only post-TCJA.

### Spousal transfers (§1041)

Carryover basis and **carryover holding period**. The transferee picks up where the transferor left off.

### Stock splits and stock dividends

The new shares share the holding period of the original shares. If you held the original for 3 years, the split shares are also long-term immediately.

### Mutual fund shares acquired via reinvested dividends (DRIP)

Each reinvestment is a **separate lot** with a **separate holding period** starting the day after reinvestment. This is why DRIP shares often produce a mix of short-term and long-term gains at sale.

### §1233 short positions

If you close a short at a gain, the gain is short-term unless the short was held for more than one year, regardless of how long the security itself was held. (The asset acquired to close the short is what matters.)

### §1256 contracts

60/40 rule — 60% long-term, 40% short-term, regardless of actual holding period. Reported on Form 6781, not 8949.

---

## Holding period during corporate actions

| Action | Effect on holding period |
|--------|--------------------------|
| Stock split | New shares share original holding period |
| Reverse stock split | Combined shares share original holding period |
| Stock dividend (taxable) | New shares have a new holding period from the distribution date |
| Stock dividend (non-taxable, §305) | New shares share original holding period |
| Spin-off (§355 tax-free) | New entity's shares share original holding period |
| Merger / reorganization (§368 tax-free) | New entity's shares share original holding period |
| Cash merger (taxable) | Old shares' holding period applies for gain/loss recognition; new cash isn't a holding-period asset |

---

## Counting tricks the agent must avoid

### Off-by-one errors

- "I bought on Jan 15 last year and I'm selling today (Jan 15) — that's one year, so long-term, right?"
- **No.** That's exactly one year. Long-term requires more than one year. Sell on Jan 16 or later.

### Trade date vs settlement date confusion

- The trade date is what counts. If the user's broker statement shows "Trade date: Aug 12; Settlement date: Aug 14", use Aug 12.
- Holding period uses trade dates at both ends (acquisition and disposition).

### Crypto block timestamp vs receipt time

- Holding period for crypto starts the day after the block timestamp when the wallet receives the coin
- For exchange purchases, this is typically nearly instant; for staking rewards, the block timestamp of the reward block is the acquisition date
- For airdrops and hard forks, the date dominion and control begins is the start

### "Various" aggregations

- When column (b) says "VARIOUS", all aggregated lots must be the **same character** (all short-term or all long-term)
- A row aggregating both short-term and long-term lots is incorrect — split into two rows

### Gifted-asset tacking

- The donor's holding period tacks on (in most cases) — agents must obtain the donor's acquisition date when basis-checking gifted assets
- For inherited assets, this doesn't apply — inherited is always long-term regardless

---

## What the agent must verify

For every transaction:

1. **Date acquired** — actual trade date or "INHERITED" or "VARIOUS"
2. **Date sold** — actual trade date
3. **Holding period** — (Date sold) − (Date acquired + 1)
4. **Box selection (Part I or Part II)** — based on holding period, not on the user's belief about it
5. **For inherited**: column (b) is "INHERITED"; row goes in Part II (long-term) regardless
6. **For gifted**: confirm donor's holding period and tack on
7. **For wash sale replacements**: confirm tacked-back holding period
8. **For DRIP shares**: verify each reinvested lot has its own holding period

---

## Sources

- **IRC §1222** — Holding period definitions
- **IRC §1223** — Holding period rules for various transactions (gifts §1223(2), inheritance §1223(9), like-kind §1223(1), wash sale §1223(3))
- **IRC §1233** — Short-position holding period
- **IRC §1256** — 60/40 contracts
- **IRC §1014** — Basis for inherited property
- **IRC §1015** — Basis for gifts
- **IRS Publication 550** — Investment Income and Expenses (holding period chapter)
- **IRS Publication 551** — Basis of Assets
