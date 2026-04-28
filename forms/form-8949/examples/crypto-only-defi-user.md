# Example: Crypto-Only DeFi User

A filer whose entire capital activity for the year is on-chain — DEX swaps, staking rewards, NFT trades, and a liquidity pool deposit. This is the canonical "DeFi-native" pattern that most general-purpose tax software handles poorly. Reconstruction comes from on-chain data and crypto tax tooling, not 1099s.

## The filer

- **Name**: Marcus Chen
- **Filing status**: Single
- **2025 ordinary income (W-2 software engineer)**: $145,000 → 24% federal marginal bracket
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 2 of workflow)

### Wallets and exchanges

| Source | Form issued | Box implication |
|--------|-------------|------------------|
| Coinbase | 1099-MISC ($1,200 staking) + transaction CSV | C/F for asset sales (no 1099-B); 1099-MISC ordinary income on Schedule 1 |
| MetaMask wallet (self-custody) | None | C/F |
| Phantom wallet (Solana) | None | C/F |
| Uniswap (DEX, on-chain only) | None | C/F (transactions captured via wallet history) |
| OpenSea (NFT marketplace) | None | C/F |

Marcus uses Koinly to ingest data from all wallets and produce a unified 8949 export. The agent verifies Koinly's output against the underlying CSV and on-chain data.

### Transaction inventory

After deduplication and wallet-level reconciliation per Rev. Proc. 2024-28:

| # | Activity | Date | USD value | Notes |
|---|----------|------|-----------|-------|
| 1 | ETH staking rewards (Coinbase) | Throughout 2025 | $1,200 | Ordinary income on Schedule 1 |
| 2 | Sold 2 ETH for USDC on Uniswap | 2025-04-14 | Proceeds $7,000; basis $5,000 | Held 18 months → long-term, Box F |
| 3 | Swapped 5,000 USDC for 50,000 PEPE | 2025-06-22 | Proceeds (USDC) $5,000; basis $5,000 | No gain/loss on USDC (stable). Sets PEPE basis = $5,000. |
| 4 | Sold 50,000 PEPE for ETH | 2025-09-08 | Proceeds $9,500; basis $5,000 | Held 78 days → short-term, Box C, $4,500 gain |
| 5 | Bought NFT (Bored Ape Mutant) for 12 ETH | 2025-07-15 | NFT basis $36,000; ETH disposition | Held ETH 6 months → short-term loss/gain on the ETH side. Original ETH cost: $24,000 (basis); disposed at $36,000 → $12,000 short-term gain on ETH (Box C) |
| 6 | Sold Mutant Ape NFT for 18 ETH | 2025-12-01 | Proceeds $54,000; basis $36,000 | Held 4.5 months → short-term, $18,000 gain. Code "C" if treated as collectible NFT per Notice 2023-27. Box C. |
| 7 | Deposited 10,000 USDC + 5 ETH into Uniswap V3 LP | 2025-08-10 | $10,000 USDC + $20,000 ETH | Conservative treatment: disposition of both. USDC: $0 gain. ETH: basis $13,000 → proceeds $20,000 → $7,000 long-term gain (held 19 months) → Box F |
| 8 | Withdrew LP position | 2025-11-05 | $9,500 USDC + 4.8 ETH (FMV $24,000) | LP token disposition. Basis $30,000; proceeds $33,500. $3,500 short-term gain. Box C. |
| 9 | Hard fork: received 100 NEW from BTC fork | 2025-03-10 | $200 ordinary income at FMV (Rev. Rul. 2019-24) | Schedule 1 ordinary; basis $200 for future sale. Not yet sold in 2025. |
| 10 | Airdrop: received 1,000 ARB tokens | 2025-05-01 | $1,500 ordinary income at FMV (Rev. Rul. 2019-24 by analogy) | Schedule 1 ordinary; basis $1,500 for future sale. Not yet sold. |

## Step 3 — Box classification

All transactions are crypto with no 1099-B → Boxes C (short-term) and F (long-term).

| # | Asset disposed | Holding | Box |
|---|---------------|---------|-----|
| 2 | 2 ETH (long held) | Long-term | F |
| 4 | PEPE | Short-term | C |
| 5 | ETH used to buy NFT | Short-term (this lot) | C |
| 6 | Mutant Ape NFT | Short-term | C (with code C if collectible NFT) |
| 7 | ETH deposited to LP | Long-term | F |
| 8 | LP tokens | Short-term | C |

Items 1, 9, 10 are ordinary income (Schedule 1, not 8949).
Item 3 is a USDC swap with $0 gain — entered on 8949 (Box C) for completeness, since technically it's a disposition.

## Step 4 — Wash sale check

§1091 does not apply to crypto under current 2025 law. No wash sale codes for any of the loss transactions. The agent verifies the rule before relying — confirmed unchanged for tax year 2025.

If Marcus had a loss on ETH and bought ETH back the next day, no §1091 disallowance. (Not applicable to Marcus this year — all his crypto trades produced gains or no gain/loss.)

## Step 5 — Other codes

- **Item 6 (Mutant Ape NFT)**: under proposed Notice 2023-27, NFTs that "look through" to a collectible are taxed at the maximum 28% LT collectibles rate. The Mutant Ape held only 4.5 months is **short-term**, taxed at ordinary rates regardless of collectible status. Code "C" is informational; no rate change applies because it's short-term. The agent uses code "C" to surface the collectible nature for Schedule D Line 18 purposes (which only matters for long-term collectibles).
- No §121, no §1244, no QSBS, no nominees.

## Step 6 — Per-row math

| # | Box | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|---|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 2 | F | 2 ETH | 10/15/23 | 04/14/25 | $7,000 | $5,000 | (none) | $0 | $2,000 |
| 3 | C | 5,000 USDC | VARIOUS | 06/22/25 | $5,000 | $5,000 | (none) | $0 | $0 |
| 4 | C | 50,000 PEPE | 06/22/25 | 09/08/25 | $9,500 | $5,000 | (none) | $0 | $4,500 |
| 5 | C | 12 ETH (lot used to buy NFT) | 01/2025 (VARIOUS) | 07/15/25 | $36,000 | $24,000 | (none) | $0 | $12,000 |
| 6 | C | Mutant Ape #1234 | 07/15/25 | 12/01/25 | $54,000 | $36,000 | C | $0 | $18,000 |
| 7 | F | 5 ETH (deposited to LP) | 01/2024 (VARIOUS) | 08/10/25 | $20,000 | $13,000 | (none) | $0 | $7,000 |
| 8 | C | LP tokens | 08/10/25 | 11/05/25 | $33,500 | $30,000 | (none) | $0 | $3,500 |

## The completed Form 8949 draft

```markdown
# Form 8949 — DRAFT for tax year 2025

## Filer
Name: Marcus Chen
SSN: XXX-XX-XXXX

## Part I — Short-Term Capital Gains and Losses

### Box C — no 1099-B received
| (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 5,000 USDC | VARIOUS | 06/22/25 | $5,000 | $5,000 | (none) | $0 | $0 |
| 50,000 PEPE | 06/22/25 | 09/08/25 | $9,500 | $5,000 | (none) | $0 | $4,500 |
| 12 ETH | VARIOUS | 07/15/25 | $36,000 | $24,000 | (none) | $0 | $12,000 |
| Mutant Ape #1234 | 07/15/25 | 12/01/25 | $54,000 | $36,000 | C | $0 | $18,000 |
| Uniswap V3 LP tokens | 08/10/25 | 11/05/25 | $33,500 | $30,000 | (none) | $0 | $3,500 |
| **Box C totals** | | | $138,000 | $100,000 | | $0 | $38,000 |

## Part II — Long-Term Capital Gains and Losses

### Box F — no 1099-B received
| (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 2 ETH | 10/15/23 | 04/14/25 | $7,000 | $5,000 | (none) | $0 | $2,000 |
| 5 ETH | VARIOUS | 08/10/25 | $20,000 | $13,000 | (none) | $0 | $7,000 |
| **Box F totals** | | | $27,000 | $18,000 | | $0 | $9,000 |

## Roll-up to Schedule D

| Schedule D Line | Source | Amount |
|-----------------|--------|--------|
| 3  — Box C net | | $38,000 |
| 7  — Net short-term capital gain | | $38,000 |
| 10 — Box F net | | $9,000 |
| 15 — Net long-term capital gain | | $9,000 |
| 16 — Total = Line 7 + Line 15 → Form 1040 Line 7 | | $47,000 |
```

## Ordinary income items (separate, NOT on 8949)

These flow to Schedule 1, Line 8z ("Other income"):

| Item | Amount | Source |
|------|--------|--------|
| Coinbase staking rewards (1099-MISC) | $1,200 | Notice 2014-21 |
| Hard fork distribution (NEW from BTC fork) | $200 | Rev. Rul. 2019-24 |
| Airdrop (1,000 ARB) | $1,500 | Conservative interpretation of Rev. Rul. 2019-24 |
| **Total Schedule 1 Line 8z** | **$2,900** | |

## What Marcus owes

```
Ordinary income increase: $145,000 W-2 + $2,900 crypto ordinary = $147,900
Short-term cap gain (taxed as ordinary): $38,000 → effective 24% bracket
Long-term cap gain: $9,000 → 15% LTCG rate

Federal tax estimate (rough):
  Ordinary + ST gain: $147,900 + $38,000 = $185,900 → ~$33,500 federal income tax (using 2025 single brackets)
  LTCG 15%: $9,000 × 15% = $1,350
  NIIT 3.8% on net investment income ($47,000) — but only on the portion above MAGI $200K threshold.
    MAGI ≈ $194,900 → below $200K, but very close. Verify with actual Schedule B and other items.
    If MAGI > $200K, NIIT = lesser of net investment income or (MAGI − $200K) × 3.8%.
```

## Required attachments

- [x] Schedule D (mandatory)
- [x] Schedule 1 (for crypto ordinary income items)
- [ ] Form 8960 — borderline; verify final MAGI before filing
- [ ] Form 1099-DA — Coinbase may issue for tax year 2025 covering proceeds; reconcile if received

## Validation summary

- Wallet-level basis tracking confirmed per Rev. Proc. 2024-28 (each wallet's lots tracked independently in Koinly)
- Every CSV row from Coinbase + every on-chain transaction in MetaMask/Phantom is represented
- DEX swaps (Uniswap PEPE swap) reported as taxable dispositions per Notice 2014-21 — common error filers miss
- LP deposit treated as disposition (conservative); LP withdrawal treated as separate disposition
- NFT purchase reported as disposition of the ETH used to pay
- §1091 wash sale verified inapplicable to crypto for tax year 2025
- Hard fork and airdrop receipts captured as ordinary income with FMV basis for future tracking
- Form 1040 digital asset question: **Yes** (multiple dispositions and receipts) — consistent with reported activity

## Wash sale tracking

None. No §1091 codes applied because crypto is exempt as of 2025.

## Capital loss carryover

None. Net capital gain, no carryforward.

## Step 10 — Hand off

The agent tells Marcus:

> Your crypto activity produced $47,000 of net capital gain ($38K short-term + $9K long-term) and $2,900 of ordinary income (staking + hard fork + airdrop). Total federal additional tax from crypto: roughly **$10,500–$11,000** depending on final MAGI and NIIT applicability.
>
> Three things to track for next year:
> - Hard fork NEW coins: basis $200 (you haven't sold yet)
> - Airdrop ARB tokens: basis $1,500 (you haven't sold yet)
> - LP token withdrawal already reset your ETH and USDC basis — record the new lots in Koinly
>
> If §1091 is extended to crypto in 2026 legislation, your tax-loss-harvesting strategy will need to change. I recommend re-checking the rule next January before doing year-end harvesting.

## Step 11 — File

Marcus has 7 transactions across two boxes (C and F). Volume is below the 100-transaction threshold for Pub 550 Method 2, so detail-level entry is fine on FFFF. Forms in his package: 1040, Schedule 1 (crypto ordinary income), Schedule D, 8949 Box C, 8949 Box F, possibly 8960.

Marcus opts for paid software (FreeTaxUSA) since FFFF doesn't natively import Koinly's TXF export. Agent follows `filing.md` Section 2 generic pattern.
