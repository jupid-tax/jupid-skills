# Wash Sales — IRC §1091 Deep Dive

The wash sale rule disallows losses when a "substantially identical" security is bought within a 61-day window around the sale that produced the loss. Brokers catch in-account washes; cross-account, cross-spouse, and IRA washes are on the filer. Get this wrong and the IRS reconciles their broker data against your return and sends a notice.

---

## The statute

**IRC §1091** disallows a loss from the sale of "stock or securities" if, within **30 days before or 30 days after** the sale, the taxpayer:

1. Acquires, or
2. Enters into a contract or option to acquire,

substantially identical stock or securities.

The 61-day window includes the sale day itself (day 0), 30 days before, and 30 days after.

```
        ← 30 days before →     SALE     ← 30 days after →
                                 |
   Day -30 ─────────────────  X  ───────────────── Day +30
                                 
       Buying substantially identical anywhere in this 61-day
       window triggers the wash sale rule on the loss.
```

---

## What "substantially identical" means

The IRS has not issued a bright-line definition. Examples from rulings, Publication 550, and case law:

| Likely substantially identical | Likely not substantially identical |
|--------------------------------|-------------------------------------|
| Same stock, same class | Different stocks in the same sector (e.g., AAPL ≠ MSFT) |
| Same stock in different lots / accounts | Bonds of the same issuer with materially different terms |
| Same mutual fund (different share classes ambiguous) | An ETF tracking a different index (e.g., SPY vs. QQQ) |
| Two ETFs tracking the same index — ambiguous; many CPAs treat SPY and IVV as substantially identical because both track S&P 500 | Different mutual funds with different holdings |
| Deep in-the-money call options on the same stock | Out-of-the-money options on the same stock (less clear) |
| Convertible bond and underlying stock — generally yes | Common stock vs. preferred stock of the same issuer (depends on conversion rights and dividend differences) |

When the user is rebuying something close but not identical, document the difference (different index, different holdings, different issuer) in case the IRS asks. The IRS doesn't dispute most ETF-to-different-ETF transactions, but the closer the match, the higher the risk.

---

## How the math works

Three things happen when a wash sale triggers:

1. **Loss disallowed** in the year of sale — entered with code "W" in column (f) and the disallowed amount in column (g) on Form 8949
2. **Basis added** to the replacement lot — the disallowed loss is added to the basis of the shares purchased within the wash window
3. **Holding period extended** — the holding period of the replacement lot includes the holding period of the sold shares (so the loss isn't lost forever; it's deferred until the replacement is sold)

### Worked example

```
Nov 1, 2025:  Buy 100 SPY at $580/share  → basis $58,000
Dec 15, 2025: Sell 100 SPY at $560/share → proceeds $56,000, $2,000 loss
Dec 28, 2025: Buy 100 SPY at $565/share  → original basis $56,500

The Dec 28 buy is within 30 days of the Dec 15 sale.
Wash sale triggered. The $2,000 loss is disallowed in 2025.

Adjusted basis on the Dec 28 lot: $56,500 + $2,000 = $58,500
Holding period for the Dec 28 lot starts Nov 1, 2025 (tacks back to original buy)

Form 8949 entry for the Dec 15 sale:
| (a)      | (b)   acq | (c) sold  | (d) Proc  | (e) Basis | (f) | (g)    | (h)  |
| 100 SPY  | 11/01/25  | 12/15/25  | $56,000   | $58,000   | W   | $2,000 | $0   |

When the Dec 28 lot is later sold, basis = $58,500 (not $56,500).
The deferred $2,000 loss surfaces at that future sale.
```

---

## Cross-account wash sales (the trap)

The 61-day window applies across **all** of the taxpayer's accounts, not just the account where the loss was taken:

- Loss in your taxable account at Schwab + buy in your taxable account at Fidelity → **wash sale**
- Loss in your taxable account + buy in your spouse's taxable account → **wash sale** (under §1091(f), spouse's purchase counts)
- Loss in your taxable account + buy in your IRA → **wash sale** with a worse outcome (see below)
- Loss in your taxable account + buy in a corporation you control → **wash sale**

Brokers' 1099-Bs only flag wash sales **within the same brokerage account**. Cross-account and spousal washes are entirely on the filer to identify and report.

### The IRA trap (permanent loss)

When the wash-sale replacement is bought inside an IRA (yours or your spouse's, traditional or Roth), the disallowed loss is **permanently lost**. Why: the IRA has no taxable basis to absorb the disallowed amount. There's no replacement lot in a taxable account to "hide" the deferred loss in.

This is one of the worst tax outcomes available. The agent must surface this clearly:

> Warning: rebuying [security] inside an IRA within 30 days of selling it at a loss in your taxable account causes the loss to be permanently disallowed under IRC §1091. The disallowed loss does not get added to the IRA's basis (IRAs don't track basis for individual lots) and you cannot recover it.

If the user has already done this, the loss is gone. The fix going forward is to wait at least 31 days between the loss sale and any IRA purchase of the same security, or buy a clearly different security in the IRA.

---

## What does NOT trigger §1091

- **Capital gain** — wash sale rule applies only to losses. A gain is fully recognized regardless.
- **Selling and rebuying outside the 61-day window** — wait at least 31 days.
- **Buying a clearly different security** — different stock, different fund, different index.
- **Selling a security you've never owned at a gain, then buying it later** — no loss triggered the rule.

---

## Crypto and wash sales (as of tax year 2025)

**IRC §1091 references "stock or securities."** Crypto is treated as **property** under Notice 2014-21, not as stock or securities. As a result, the wash sale rule does **not** currently apply to digital assets.

This is a year-by-year question. Multiple proposed amendments (e.g., the Build Back Better Act in 2021, various Senate Finance Committee proposals) would extend §1091 to digital assets, but **none have been enacted as of tax year 2025**. The agent must verify the current rule before relying on this exemption — every January, check whether the rule has changed.

For now (tax year 2025):

- Sell BTC at a $5,000 loss on Dec 15
- Buy BTC back on Dec 16
- The full $5,000 loss is allowed
- No code "W", no adjustment

This makes "tax-loss harvesting" much more aggressive in crypto than in equities. The IRS has expressed concern about this in commentary, which is why proposals to close the gap recur.

**Likely change**: when §1091 is extended to digital assets, the change will be prospective. Existing positions held under the old rule won't be retroactively affected. But agents should set a reminder to re-verify §1091's scope every January before filing season.

---

## Partial wash sales

When the loss-sold quantity exceeds the within-window-purchased quantity, only the loss attributable to the matched portion is disallowed.

```
Dec 15: Sell 200 sh XYZ at a loss of $4,000 ($20/sh loss)
Dec 28: Buy 100 sh XYZ

Matched portion: 100 sh × $20 = $2,000 loss disallowed
Unmatched portion: 100 sh × $20 = $2,000 loss allowed

Form 8949 entries (split into two rows):
Row 1 (matched, wash sale): 100 sh, code W, adjustment $2,000, gain/loss $0
Row 2 (unmatched, allowed):  100 sh, no code, gain/loss ($2,000)
```

---

## Wash sales and short positions

Closing a short position at a loss, then re-shorting (or buying long the same security) within the 61-day window also triggers §1091. Less common in retail filing but applies to active traders.

---

## What the agent must check

For every loss transaction in the draft:

1. **Did the user buy substantially identical security within 61 days (30 before to 30 after the sale)?**
   - In the same account
   - In any other taxable account they hold
   - In any IRA, 401(k), HSA, or 529 they hold
   - In their spouse's accounts (any type)
   - In a corporation, partnership, or trust they control

2. **If yes**:
   - Code "W" in column (f)
   - Disallowed loss in column (g)
   - Surface to the user: replacement lot's basis is adjusted, holding period tacks back
   - If the replacement is in an IRA, surface the permanent-loss warning

3. **If no but the broker flagged a wash sale on the 1099-B**: trust the broker's flag. They saw something. Pull the 1099-B detail to find the matched purchase.

4. **If no and the broker did not flag**: still ask the user about cross-account/spousal/IRA purchases. Brokers cannot see those.

5. **For crypto losses**: confirm current year's §1091 scope. As of tax year 2025, crypto is exempt — no code needed. Reverify in 2026 and beyond.

---

## Sources

- IRC §1091 — Loss from wash sales of stock or securities
- IRS Publication 550 — Investment Income and Expenses (chapter on wash sales)
- IRS Form 8949 Instructions — Code W discussion in Table 1
- Rev. Rul. 56-275 — substantially identical analysis for bonds
- Rev. Rul. 60-195 — wash sales involving short positions
