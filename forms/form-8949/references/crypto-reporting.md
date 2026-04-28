# Crypto Reporting on Form 8949

Cryptocurrency tax rules trip more filers than any other 8949 topic. The IRS treats crypto as **property**, not currency. Every disposition is a taxable event — including swaps, NFT trades, and using crypto to buy goods. Most US exchanges have not historically issued 1099-Bs (Form 1099-DA is phasing in for tax year 2025+), so basis tracking is on the filer. This file covers the full crypto picture.

---

## The foundational rule: Notice 2014-21

**IRS Notice 2014-21** (March 2014) established that virtual currency is treated as property for federal tax purposes. Practical implications:

- Selling crypto for USD: capital gain/loss disposition
- Swapping one crypto for another (e.g., BTC → ETH): a disposition of the BTC at FMV; new ETH basis = USD value at swap
- Buying goods or services with crypto: a disposition of the crypto at the time of purchase
- Mining or staking rewards: ordinary income at FMV on receipt; that FMV becomes the basis for the new coin
- Hard fork distributions: covered separately by Rev. Rul. 2019-24
- Receiving crypto as wages: ordinary income at FMV; W-2 reporting if from an employer
- Receiving crypto as a gift: not a taxable event at receipt (carryover basis from donor)

**Not taxable** (no 8949 entry):

- Buying crypto with USD and holding
- Transferring between your own wallets
- Receiving crypto as a gift (taxable only when later sold)
- Donating crypto to a qualified charity (deductible on Schedule A; no capital gain recognized)

---

## Hard forks and airdrops: Rev. Rul. 2019-24

Issued October 2019. Two scenarios:

### Scenario 1 — Hard fork without airdrop

A hard fork in the protocol creates a new coin (e.g., BCH from BTC, ETC from ETH). If the taxpayer receives the new coin and has **dominion and control** (can transfer, sell, or exchange it), they have **ordinary income** at FMV when dominion and control begins.

That FMV becomes the basis. A subsequent sale of the new coin is reported on 8949.

If the user **never had dominion and control** — for example, the new coin was never credited to their wallet by the exchange — there's no income recognition. The user's records should document the lack of dominion and control.

### Scenario 2 — Hard fork with airdrop

When the new coin is airdropped to the taxpayer's wallet, the same rule: ordinary income at FMV on receipt, with the FMV becoming basis.

The IRS has not extended Rev. Rul. 2019-24 to all airdrops (e.g., promotional airdrops from new tokens). The conservative position is that any airdrop received with dominion and control is ordinary income at FMV. Document FMV at receipt; many tools price airdrops based on the first available DEX trading price.

---

## Staking rewards

Treated as **ordinary income at FMV on receipt**. The basis of the staking reward = FMV when received. A subsequent sale of the staked coin produces capital gain/loss on 8949.

Two open questions in current guidance:

1. **When is income realized — at block reward generation, at unstaking, or at withdrawal?** The IRS has indicated income is realized when the taxpayer has dominion and control. For exchange-staked products, that's typically when the reward credits the account. For self-staking on a node, it's typically when the reward is generated (some debate).

2. **Are staking rewards self-employment income?** The IRS has not taken a definitive position. For passive validators (delegated staking), the conservative position is investment income. For active validator operations (running a node), self-employment treatment may apply.

The Jarrett v. United States case (2022) raised the question of whether self-staked rewards are income at all (the taxpayer argued they were "created property" not income). The IRS refunded the disputed tax without ruling, leaving the rule technically open. The conservative position for now: treat staking rewards as ordinary income.

---

## NFTs

Non-fungible tokens are property, like other crypto. Each NFT is its own asset.

- **Buying an NFT with crypto**: disposition of the crypto used to buy. Capital gain/loss on the crypto.
- **Selling an NFT for crypto or USD**: capital gain/loss on the NFT itself. Basis = USD cost (which itself includes any gain recognized on the crypto used to buy it). Holding period starts the day after acquisition.
- **NFT as collectible**: Notice 2023-27 (proposed) treats NFTs that are "associated with" a collectible (art, etc.) as collectibles for tax purposes — long-term gain taxed at maximum 28% under IRC §1(h)(4). Collectible NFTs use code "C" on 8949 (informational for Schedule D Line 18).
- **Royalties received on resale**: ordinary income.
- **Minting an NFT**: treated similarly to creating property. Cost basis = production costs. Sale produces capital gain/loss (or ordinary income if the user is a dealer).

---

## DeFi (Decentralized Finance)

The IRS has issued no comprehensive guidance for DeFi. The conservative interpretation of Notice 2014-21 (crypto as property) generates many taxable events:

| DeFi action | Tax treatment (conservative) |
|-------------|------------------------------|
| Depositing tokens into a liquidity pool (receiving LP tokens) | Disposition of deposited tokens; new basis in LP tokens at FMV |
| Withdrawing from a liquidity pool (returning LP tokens, receiving underlying) | Disposition of LP tokens; new basis in withdrawn tokens at FMV |
| Wrapping (e.g., ETH → WETH) | Some treat as a non-taxable wrap; conservative treatment is taxable swap |
| Swapping in a DEX (Uniswap, etc.) | Taxable swap, same as exchange-based swap |
| Receiving liquidity-mining rewards | Ordinary income at FMV on receipt |
| Receiving governance tokens from a protocol | Ordinary income at FMV on receipt |
| Lending tokens (Aave, Compound) and receiving aTokens / cTokens | Some treat as a deposit (non-taxable); conservative treatment is taxable disposition |
| Liquidations during borrowing | Disposition of the collateral at the time of liquidation |
| Bridging tokens cross-chain | Ambiguous; many tools treat as non-taxable transfer between user's own assets |

For complex DeFi activity, the agent should recommend:

1. Use a crypto tax tool (Koinly, CoinTracker, ZenLedger, TaxBit) to ingest on-chain data
2. Manually review each DeFi protocol's interactions
3. Consult a crypto-specialized CPA when activity is significant or novel

The agent should not invent rulings. When in doubt, surface the ambiguity to the user.

---

## 1099 reporting for crypto

Historically, US crypto exchanges have issued:

- **1099-MISC** for staking rewards, learn-and-earn, referral bonuses (treated as ordinary income, Schedule 1)
- **1099-K** for users above certain transaction thresholds (treated as gross proceeds, but doesn't affect basis tracking)
- **1099-B** — most exchanges have not issued these, because crypto wasn't formally a covered security under §6045(g)

Starting **tax year 2025**, **Form 1099-DA** ("Digital Asset Proceeds From Broker Transactions") is the new reporting form for digital asset brokers under regulations finalized in 2024. Phased adoption:

- 2025: gross proceeds reporting required for many crypto brokers
- Future years: basis reporting required (date TBD by Treasury)

Until full adoption, the agent should expect crypto sales to land in **Box C or F** (no 1099-B) and require the user to upload the exchange CSV separately.

Even when 1099-DA is issued for proceeds, the agent must verify the CSV-based basis matches what the broker reports — early-year 1099-DAs are likely to have basis errors.

---

## Wash sale rule and crypto

**As of tax year 2025**: IRC §1091 references "stock or securities." Because crypto is treated as property (not stock or securities), §1091 does **not** apply to digital assets. Selling BTC at a loss and rebuying immediately produces an allowed loss with no wash adjustment.

**Risk**: Multiple legislative proposals would extend §1091 to crypto. The agent must verify the rule's scope every January before filing season. See [`wash-sales.md`](./wash-sales.md).

---

## Cost basis methods for crypto

The IRS has not formally limited crypto to a specific basis method. In practice, most users elect:

- **FIFO** (first-in, first-out) — default if no method elected
- **Specific identification** — must be supported by adequate records: which lot, which wallet, which transaction hash. Allows tax-loss harvesting and lot-level optimization.
- **HIFO** (highest-in, first-out) — a form of specific identification; works only if the user can prove they identified specific lots at the time of disposition

The IRS issued **Rev. Proc. 2024-28** (effective Jan 1, 2025) requiring crypto basis to be tracked **by wallet** rather than aggregated across wallets. This means specific-identification users must identify the specific wallet AND specific lot within that wallet. Aggregated FIFO across all wallets (which many crypto tax tools previously offered) is no longer permitted starting 2025.

See [`cost-basis-methods.md`](./cost-basis-methods.md) for details.

---

## Form 1040 digital asset question

Form 1040 has a yes/no question near the top: "At any time during [year], did you (a) receive (as a reward, award, or payment for property or services); or (b) sell, exchange, or otherwise dispose of a digital asset (or a financial interest in a digital asset)?"

- **Yes** if you sold, swapped, spent, received airdrop, received staking reward, received payment in crypto, received NFT, or any disposition
- **No** if you only bought and held, or only transferred between your own wallets

Answering "Yes" without producing a corresponding 8949 entry (or a 1099-MISC entry on Schedule 1) flags the return for review. The agent must reconcile the answer to the underlying activity.

---

## Records the agent must obtain

For every crypto exchange, wallet, and DeFi protocol the user used:

1. **Full transaction CSV export** for the year (and prior years if basis is being reconstructed)
2. **1099-MISC** if issued (for staking, learn-earn, referrals)
3. **1099-DA** if issued (2025+)
4. **1099-K** if issued
5. **Wallet addresses** (public only — never private keys)
6. **Notes on any cross-wallet transfers** so the agent doesn't double-count

Reconstruction from on-chain data is possible (Etherscan, BTCScan, on-chain explorers) but slow. CSV exports from the exchange are the source of truth for basis on coins acquired through the exchange.

---

## What the agent must NOT do

- Never assume basis = $0. Stop and ask the user. A $0 basis on a sold $50,000 BTC creates $50,000 of phantom gain.
- Never invent a wash sale rule for crypto under current law. As of 2025, §1091 does not apply.
- Never invent staking treatment for novel protocols. Surface the ambiguity to the user and recommend a crypto-savvy CPA for material amounts.
- Never store wallet private keys or exchange API keys with write permissions. CSV exports and read-only API tokens only.
- Never paste full wallet addresses or transaction hashes into general-purpose chat tools — these are personally identifying. Use redacted forms in any external communication.

---

## Sources

- **Notice 2014-21** — Virtual Currency Guidance
- **Rev. Rul. 2019-24** — Hard fork and airdrop guidance
- **Rev. Proc. 2024-28** — Wallet-level basis tracking (effective Jan 1, 2025)
- **Form 1099-DA Instructions** — Digital Asset Proceeds From Broker Transactions
- **Treasury Regs §1.6045-1, §1.6045A-1** — Broker reporting rules (extended to digital asset brokers in 2024)
- **IRS FAQs on Virtual Currency Transactions** — https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-virtual-currency-transactions
- **Jarrett v. United States** (2022) — Open question on staking rewards as income vs. created property
- **Notice 2023-27** (proposed) — NFTs as collectibles for §408(m) and §1(h)(4)
- IRC §61 (gross income), §1001 (gain/loss recognition), §1(h)(4) (collectibles 28% rate)
