# Cost Basis Methods

Choosing a basis method determines which lot is treated as sold when the user has multiple lots of the same asset. The right method can shift thousands of dollars of gain between long-term (preferential rate) and short-term (ordinary rate), or accelerate/defer recognition. Most filers use the broker default; aware filers use specific identification to optimize.

---

## The methods

### FIFO — First In, First Out

The default at most US brokers and the IRS default if no method is elected.

- Shares acquired first are treated as sold first
- Predictable; no record-keeping burden
- Often produces long-term gains (older lots have older acquisition dates)
- Sub-optimal in rising markets — sells the lowest-basis (highest-gain) shares first

```
Buy 100 sh XYZ at $50 on Jan 5, 2020 (lot 1: $5,000 basis)
Buy 100 sh XYZ at $80 on Jun 10, 2024 (lot 2: $8,000 basis)
Sell 100 sh XYZ at $120 on Aug 15, 2025

FIFO: lot 1 sold. Gain = $7,000 long-term.
```

### Specific Identification

The user (or the broker on instruction from the user) identifies the specific lot at the time of trade.

- **Maximum tax flexibility** — pick the highest-basis lot to minimize gain, or pick a long-term lot over short-term
- Must be elected **at or before settlement** of the trade. Cannot be reconstructed after.
- Most brokers allow specific-ID by checking a box at trade entry, or via a custom default ("Loss Gain Harvester", "Tax Lot Optimizer", etc.)
- Documentation required: trade confirmation showing the specific lot identified

```
Same lots as above.
Specific-ID at sale: pick lot 2 (the $80 lot).
Gain = $4,000 short-term (held 14 months) → wait, that's long-term too.
Gain = $4,000 long-term.

vs. FIFO's $7,000 long-term.
Saves the user $450 at the 15% LT rate.
```

### Average Cost

Available **only for mutual funds** (and ETFs at brokers that offer it — Vanguard, Schwab, Fidelity, etc.).

- All shares of the same fund pool into one weighted average basis
- Once elected for a particular fund, the user must continue using average cost for that fund (with prior-year revocation rules — see Treas. Reg. §1.1012-1(e))
- Simplest for funds with frequent reinvested dividends
- Cannot be used for individual stocks or crypto

```
Buy 100 sh VTSAX at $100 (basis $10,000)
Buy 100 sh VTSAX at $130 (basis $13,000)
Average basis: $115/share

Sell 50 sh VTSAX at $150
Gain = (50 × $150) − (50 × $115) = $1,750
```

### HIFO — Highest In, First Out

A form of specific identification: the user identifies the highest-basis lot at the time of trade.

- Minimizes current-year gain (or maximizes current-year loss)
- Common in **crypto** because crypto basis tracking has historically been done by the user, not the exchange
- Must satisfy specific-ID requirements: identify the lot at or before disposition
- Some crypto tax tools default to HIFO if the user has not elected another method

### LIFO — Last In, First Out

Last-acquired shares sold first.

- **Not allowed for stocks/securities** under §1012 — the IRS recognizes only FIFO, specific-ID, and average cost (mutual funds)
- Sometimes used in inventory accounting (Schedule C, COGS), but not for capital gain purposes
- Crypto: LIFO is technically a form of specific-ID if the user can prove the last-in lot was specifically identified

---

## Method election rules

### Stocks (covered securities)

Most brokers default to FIFO. To elect specific-ID, the user must:

1. Notify the broker before settlement (typically a checkbox at trade entry, or set a global default)
2. Receive a written confirmation from the broker that the specified lot was sold
3. Keep the confirmation for records

To elect average cost for a particular mutual fund: notify the broker. Once elected, average cost stays in effect for all sales of that fund unless revoked under §1.1012-1(e).

### Mutual funds

Default at most brokers is **average cost**. Filers can elect FIFO or specific-ID before the first sale of the fund. After the first sale under any method, switching is restricted (the IRS treats the method as effectively locked).

### DRIP shares

Each reinvested dividend is a separate lot at the FMV on the reinvestment date. Average cost simplifies; specific-ID is mechanically possible but tedious.

### Crypto

Per **Rev. Proc. 2024-28** (effective Jan 1, 2025), crypto basis must be tracked **by wallet**, not aggregated across wallets. Within a wallet, the user can use:

- FIFO (default)
- Specific-ID (must identify the specific lot at or before the disposition; supported by transaction hash records)
- HIFO as a form of specific-ID

**Cross-wallet aggregation is no longer permitted.** Many crypto tax tools (Koinly, CoinTracker) updated their default behavior in late 2024 to comply.

The user must keep:

- Per-wallet cost basis ledger
- Transaction hashes for each disposition showing the specific lot identified
- Year-end position by wallet

---

## How method choice interacts with holding period

The single most consequential basis-method decision: **picking a long-term lot vs a short-term lot**.

- A short-term lot taxed at 32% federal vs a long-term lot at 15% on a $10,000 gain saves $1,700.
- If the user has both, specific-ID always wins for tax minimization.

Example:

```
Buy 100 sh AAPL at $80 on March 15, 2020 (lot 1: long-term, $8,000 basis)
Buy 50 sh AAPL at $200 on November 5, 2024 (lot 2: short-term, $10,000 basis)
Sell 50 sh AAPL at $230 on August 12, 2025

FIFO: 50 sh of lot 1 sold. Gain = (50 × $230) − (50 × $80) = $7,500 long-term.
Specific-ID picking lot 2: Gain = (50 × $230) − (50 × $200) = $1,500 long-term.
```

Wait — both lots are long-term in this example because Nov 5 to Aug 12 of the next year is over a year. Let me redo:

```
Buy 100 sh AAPL at $80 on March 15, 2020 (long-term)
Buy 50 sh AAPL at $200 on March 15, 2025 (short-term as of August 12, 2025)
Sell 50 sh AAPL at $230 on August 12, 2025

FIFO: lot 1 sold. Gain = $7,500 long-term @ 15% = $1,125 federal.
Specific-ID picking lot 2: Gain = $1,500 short-term @ 32% = $480 federal.

Specific-ID saves $645 in this case.
```

The optimal choice depends on whether short-term is bigger or smaller, and whether ordinary brackets push the user above LTCG breakpoints.

---

## What the agent must do

For each disposition in the draft:

1. **Identify the basis method used** by the broker or by the user
2. **For broker-tracked stocks**: pull the 1099-B basis as authoritative. If the user disagrees, use code "B" with the correction in column (g).
3. **For mutual funds**: confirm whether average cost applies (most common). Once the user has used average cost for a fund, they're typically locked in.
4. **For crypto**: confirm wallet-level tracking is in place per Rev. Proc. 2024-28. Confirm method choice (FIFO, specific-ID, HIFO).
5. **Surface optimization opportunities**: if the user has both long-term and short-term lots and is considering a sale, point out the specific-ID savings.

The agent should not retroactively change a method election. Method changes have notice and consistency requirements; getting them wrong invites IRS challenge.

---

## Sources

- **IRC §1012** — Basis of property
- **Treas. Reg. §1.1012-1** — Basis rules including specific identification and average cost
- **Treas. Reg. §1.1012-1(e)** — Average cost for mutual funds, election and revocation rules
- **Rev. Proc. 2024-28** — Wallet-level crypto basis tracking (effective Jan 1, 2025)
- **IRC §6045(g)** — Cost-basis reporting by brokers (covered vs non-covered)
- **IRS Publication 550** — Investment Income and Expenses (chapters on basis)
- **IRS Publication 551** — Basis of Assets
