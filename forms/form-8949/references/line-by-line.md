# Form 8949 Line-by-Line Reference

Complete lookup for every box, column, and adjustment code on Form 8949. Use this when the agent needs to confirm where a transaction belongs, what a column means, or which code applies.

---

## Header (every page used)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Filer's legal name (matches Form 1040) | |
| SSN/ITIN | Filer's SSN or ITIN | |
| Box checkbox | Exactly one of A/B/C (Part I) or D/E/F (Part II) | One box per page. Use multiple pages if needed. |

If the user has transactions in three different boxes, use three pages (or three sets of pages).

---

## Parts and boxes

Form 8949 has two parts. **Part I** is short-term (held ≤ 1 year). **Part II** is long-term (held > 1 year). Each part has three boxes that depend on how the broker reported the transaction to the IRS.

### Part I — Short-Term (held ≤ 365 days)

| Box | Condition | Common scenarios |
|-----|-----------|------------------|
| **A** | 1099-B received with basis reported to IRS | Most stock sales for shares acquired after Jan 1, 2011 ("covered" securities under IRC §6045(g)) |
| **B** | 1099-B received with basis NOT reported to IRS | Older lots, transferred-in shares without basis history, certain options, debt instruments acquired before 2014 |
| **C** | No 1099-B received | Crypto sales (most US exchanges still don't issue 1099-B), private placements, peer-to-peer asset sales |

### Part II — Long-Term (held > 365 days)

| Box | Condition | Common scenarios |
|-----|-----------|------------------|
| **D** | 1099-B received with basis reported to IRS | Most stock sales for "covered" shares acquired after 2011 |
| **E** | 1099-B received with basis NOT reported to IRS | Mutual fund shares acquired before Jan 1, 2012, transferred lots without basis history, debt instruments acquired before 2014 |
| **F** | No 1099-B received | Long-held crypto, real estate, collectibles |

**The 1099-B itself tells you which box.** Read each 1099-B carefully — it's labeled "Short-term — basis reported to IRS" (Box A), "Short-term — basis not reported" (Box B), "Long-term — basis reported" (Box D), "Long-term — basis not reported" (Box E), or one of several "non-1099-B" labels.

**Cost-basis reporting cutoffs (IRC §6045(g)):**

| Asset type | "Covered" (reported to IRS) starts |
|------------|------------------------------------|
| Most equities | Acquired on or after Jan 1, 2011 |
| Mutual funds and DRIP shares | Acquired on or after Jan 1, 2012 |
| Debt instruments (most) | Acquired on or after Jan 1, 2014 |
| Certain options and other securities | Acquired on or after Jan 1, 2014 |
| Digital assets (Form 1099-DA regime) | Tax year 2025+, phased — verify per the most recent IRS guidance |

Anything outside the covered scope is "non-covered" and lands in Box B or E.

---

## Columns

Each transaction is one row across columns (a) through (h).

### Column (a) — Description of property

What was sold. Be specific enough that an examiner can match it to the 1099-B or exchange record.

| Asset | Format |
|-------|--------|
| Stock | "100 sh AAPL" or "100 shares Apple Inc" |
| ETF | "50 sh VTI" |
| Mutual fund | "1,234.567 sh VTSAX" |
| Crypto | "0.5 BTC" or "1.25 ETH" |
| NFT | "Bored Ape #1234" or contract address + token ID |
| Bond | "$10,000 US Treasury 4.5% due 2030" |
| Real estate | Property address |
| Collectible | Description of item |

### Column (b) — Date acquired

`MM/DD/YYYY` format. Special values:

- **VARIOUS** — when one row aggregates multiple lots with different acquisition dates (allowed when all lots are the same character — short-term or long-term). Often used for crypto where many small buys aggregated to one sale.
- **INHERITED** — for inherited assets, which always count as long-term per IRC §1223(9). Basis is stepped up to FMV on date of death per IRC §1014.

### Column (c) — Date sold or disposed

`MM/DD/YYYY` of the disposition. The trade date (not settlement date) is what counts for holding period.

### Column (d) — Proceeds

Net sale proceeds in USD. If the 1099-B shows gross proceeds, subtract selling commissions (Form 8949 wants net). The 1099-B "Box 1d" is the figure the IRS will reconcile against — use exactly that number for Boxes A and D rows.

For crypto, proceeds = USD value at the moment of disposition. For crypto-to-crypto swaps, proceeds = FMV of the asset received (which equals FMV of the asset given up).

### Column (e) — Cost or other basis

The adjusted basis. Includes:

- Original purchase price
- Commissions, transfer fees, acquisition costs
- Reinvested dividends (DRIP — each reinvestment increases basis)
- Capital improvements (real estate)
- Wash sale adjustments from prior dispositions added to basis

For inherited assets: stepped-up FMV per IRC §1014.
For gifted assets: generally the donor's basis (carryover basis), with special rules if the FMV at gift date is less than basis.
For crypto: original USD cost; for staking rewards / hard fork coins, FMV at time of receipt (already taxed as ordinary income).

**Never enter $0** when basis is unknown. Either pull records or ask the user — defaulting to $0 overstates the gain and is one of the most common 8949 errors.

### Column (f) — Codes

One or two letters that explain why the gain/loss is being adjusted. Multiple codes can stack, separated by no space (e.g., "BO").

### Column (g) — Amount of adjustment

Always entered as a **positive number**. The form's column (h) formula handles the sign automatically:

`(h) = (d) − (e) + (g)`

Wait — that formula always **adds** (g). That's because:

- For wash sale (code W): you're disallowing a loss, so you add back the disallowed amount → makes (h) less negative or zero
- For basis correction upward (code B with broker basis too low): the adjustment is negative, but it's entered as positive in (g) and the instructions tell you when to use a negative sign instead

The instructions table for each code specifies the sign convention. When in doubt, work backwards: compute the gain/loss you want shown in (h), then derive (g) from the formula.

### Column (h) — Gain or (loss)

`(d) − (e) + (g)`. Losses shown in parentheses.

---

## Full adjustment code table (column f)

The IRS Form 8949 instructions list these codes. Here are the ones an agent will encounter most often:

| Code | When to use | What goes in (g) |
|------|-------------|------------------|
| **W** | Wash sale — loss disallowed under IRC §1091. Required when a loss is fully or partially disallowed because a substantially identical security was bought within the 61-day window. | Disallowed loss amount as a positive number. Column (h) will then equal $0 or the small allowed remainder. |
| **B** | Basis on 1099-B is incorrect. Broker reported the wrong basis; you're correcting it. | Difference between your computed basis and the broker's, with sign per instructions. |
| **T** | 1099-B reported the wrong type or holding period. | Adjustment to fix the 8949 row, sign per instructions. |
| **N** | You received a Form 1099-B as a nominee for someone else. | Subtracts the portion that's not yours. |
| **H** | Sold your main home and the gain is partially excluded under §121. | The excluded portion as a negative adjustment. |
| **D** | Accrued market discount on a debt instrument — the discount portion is ordinary income, not capital gain. | Adjustment removing the ordinary-income portion. |
| **Q** | §1202 QSBS (Qualified Small Business Stock) — partial gain excluded. | The excluded portion as a negative adjustment. |
| **X** | §1202 QSBS — full exclusion (100% rule for stock acquired after Sept 27, 2010 held > 5 years). | The excluded amount. |
| **R** | §1244 Section 1244 small business stock loss — ordinary loss treatment up to limit. | The portion treated as ordinary loss. |
| **L** | Nondeductible loss from sale of personal-use property (e.g., personal car, family home below FMV). | Disallowed loss amount. |
| **C** | Collectibles — informs Schedule D that the gain is taxed at the maximum 28% rate. | Often $0; the code is informational for Schedule D Line 18 (28% Rate Gain Worksheet). |
| **S** | Loss from sale to a related party — disallowed under IRC §267. | Disallowed loss. |
| **O** | Other — see instructions. Catch-all for less-common adjustments. | Per instructions. |
| **E** | Selling expenses or option premiums needed adjustment to basis or proceeds. | Per instructions. |
| **M** | Multiple transactions reported on a single row — for summary reporting under Pub 550 Method 2. | Sum of adjustments for the aggregated rows. |

The **full and authoritative code list** is in the IRS Instructions for Form 8949 (Table 1). Always verify against the current-year instructions before filing.

**Multiple codes**: when more than one applies, list them in alphabetical order with no spaces. Example: "BW" means a basis correction on a wash sale.

---

## Page totals

Each Form 8949 page sums column (d), (e), (g), (h) at the bottom row. These page totals are what flow to Schedule D.

---

## Schedule D roll-up

Form 8949 always pairs with Schedule D. Box totals roll up like this:

```
Schedule D Part I — Short-Term Capital Gains and Losses
  Line 1b — Box A totals (proceeds, basis, adjustment, gain/loss)
  Line 2  — Box B totals
  Line 3  — Box C totals
  Line 4  — Short-term gain from Form 6252 (installment sales), 4684 (casualty), 6781 (§1256), 8824 (§1031)
  Line 5  — Net short-term from partnerships, S-corps, estates, trusts (Schedule K-1)
  Line 6  — Short-term capital loss carryover (from prior year worksheet)
  Line 7  — Net short-term capital gain or loss (sum of 1b through 6)

Schedule D Part II — Long-Term Capital Gains and Losses
  Line 8b — Box D totals
  Line 9  — Box E totals
  Line 10 — Box F totals
  Line 11 — Gain from Form 4797 Part I, plus other long-term gains
  Line 12 — Net long-term from partnerships, S-corps, estates, trusts (Schedule K-1)
  Line 13 — Capital gain distributions (from 1099-DIV Box 2a)
  Line 14 — Long-term capital loss carryover
  Line 15 — Net long-term capital gain or loss

Schedule D Part III — Summary
  Line 16 — Total = Line 7 + Line 15  → Form 1040 Line 7
  Line 17 — Are 15 and 16 both gains?  Yes → continue to special rate worksheets
  Line 18 — 28% Rate Gain Worksheet (collectibles, §1202 portion not excluded)
  Line 19 — Unrecaptured §1250 Gain Worksheet (real estate depreciation recapture)
  Line 20 — Use Qualified Dividends and Capital Gain Tax Worksheet or Schedule D Tax Worksheet
  Line 21 — If Line 16 is a loss, enter the smaller of the loss or $3,000 ($1,500 MFS) → Form 1040 Line 7
  Line 22 — Do you have qualified dividends? Yes → use Qualified Div/CG Worksheet
```

If net loss > $3,000 ($1,500 MFS), the excess is carried to next year via the **Capital Loss Carryover Worksheet** in the Schedule D instructions. The carryforward retains its short-term or long-term character.

---

## Special situations

### "VARIOUS" in column (b)

Allowed when multiple lots are aggregated into one row, and all lots are the same character (all short-term or all long-term). Common for crypto where dozens of small buys at different times feed a single sale. The IRS expects you to keep the underlying lot detail in your records.

### "INHERITED" in column (b)

Always long-term per §1223(9), regardless of how soon you sell after inheriting. Basis is stepped up to FMV on date of death (or alternate valuation date if elected) per §1014.

### Gifted assets

- If FMV on gift date ≥ donor's basis → carryover basis (use donor's basis), and donor's holding period tacks on
- If FMV on gift date < donor's basis → "dual basis" rule:
  - If you later sell at a gain: use donor's basis
  - If you later sell at a loss: use FMV at gift date
  - If between: no gain or loss

### Spousal asset transfers

Carryover basis under §1041; no gain or loss on the transfer itself.

### §1244 small business stock

Loss on §1244 stock can be treated as ordinary (not capital), up to $50,000 single / $100,000 MFJ per year. Code "R" in column (f).

### Like-kind exchange (§1031)

Real property only post-TCJA. Goes on **Form 8824**, not 8949. Any boot received may produce gain reportable on 8949.

### §1256 contracts (futures, broad-based index options)

60/40 treatment — 60% long-term, 40% short-term, regardless of holding period. Reported on **Form 6781**, then carried to Schedule D Lines 4 and 11. Not on 8949 directly.

### §1202 QSBS

Gain may be partially or fully excluded depending on acquisition date and holding period. The full gain still appears on 8949 with code Q (partial) or X (full); the excluded portion is the negative adjustment in (g).

### Wash sales — see [`wash-sales.md`](./wash-sales.md)

### Crypto-specific — see [`crypto-reporting.md`](./crypto-reporting.md)
