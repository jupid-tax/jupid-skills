# Form 8949 Line-by-Line Reference

Complete lookup for every box, column, and adjustment code on Form 8949. Use this when the agent needs to confirm where a transaction belongs, what a column means, or which code applies.

---

## Header (every page used)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name | Filer's legal name (matches Form 1040) | |
| SSN/ITIN | Filer's SSN or ITIN | |
| Box checkbox | Exactly one of A/B/C/G/H/I (Part I) or D/E/F/J/K/L (Part II) | One box per page. Use multiple pages if needed. |

If the user has transactions in three different boxes, use three pages (or three sets of pages).

---

## Parts and boxes

Form 8949 has two parts. **Part I** is short-term (held ≤ 1 year). **Part II** is long-term (held > 1 year). Each part has six boxes that depend on how the broker reported the transaction to the IRS: three for transactions other than digital assets (A/B/C, D/E/F) and three for digital assets (G/H/I, J/K/L). Boxes G–L are new on the 2025 form; the 2025 instructions say not to use Box C or F for digital asset transactions (Instructions for Form 8949 (2025), pp. 1 and 3).

### Part I — Short-Term (held ≤ 365 days)

| Box | Condition | Common scenarios |
|-----|-----------|------------------|
| **A** | 1099-B received with basis reported to IRS | Most stock sales for shares acquired after Jan 1, 2011 ("covered" securities under IRC §6045(g)) |
| **B** | 1099-B received with basis NOT reported to IRS | Older lots, transferred-in shares without basis history, certain options, debt instruments acquired before 2014 |
| **C** | No 1099-B or 1099-DA received, not a digital asset | Private placements, peer-to-peer asset sales. Never a digital asset (use Box I). |
| **G** | 1099-DA received with basis reported to IRS (box 2 checked) | For 2025 sales, only where the broker chose to report basis (voluntary for 2025) |
| **H** | 1099-DA received with basis NOT reported to IRS | 2025 crypto sales on a U.S. custodial exchange that issued a proceeds-only 1099-DA |
| **I** | Digital asset, no 1099-DA or 1099-B received | Self-custody wallet trades, DEX swaps, foreign exchanges, NFT sales between wallets |

### Part II — Long-Term (held > 365 days)

| Box | Condition | Common scenarios |
|-----|-----------|------------------|
| **D** | 1099-B received with basis reported to IRS | Most stock sales for "covered" shares acquired after 2011 |
| **E** | 1099-B received with basis NOT reported to IRS | Mutual fund shares acquired before Jan 1, 2012, transferred lots without basis history, debt instruments acquired before 2014 |
| **F** | No 1099-B or 1099-DA received, not a digital asset | Real estate, collectibles. Never a digital asset (use Box L). |
| **J** | 1099-DA received with basis reported to IRS (box 2 checked) | Same as G, held more than 1 year |
| **K** | 1099-DA received with basis NOT reported to IRS | Same as H, held more than 1 year |
| **L** | Digital asset, no 1099-DA or 1099-B received | Same as I, held more than 1 year |

**The 1099-B itself tells you which box.** Read each 1099-B carefully — it's labeled "Short-term — basis reported to IRS" (Box A), "Short-term — basis not reported" (Box B), "Long-term — basis reported" (Box D), "Long-term — basis not reported" (Box E), or one of several "non-1099-B" labels.

**Form 1099-DA works the same way.** Its "Applicable checkbox on Form 8949" field carries code G, H, J, or K. Code Y means the broker does not know the holding period, so the agent decides between H and K from the user's records (2025 Instructions for Form 1099-DA, p. 7). The matching code on a Form 1099-B is X, meaning the broker cannot choose between Box B and Box E (2025 Instructions for Form 1099-B, p. 8). The Form 8949 instructions (2025, p. 2) mention only code X, for both forms: the 2025 revision added Form 1099-DA to the 2024 sentence about Form 1099-B without adding code Y. Read Y on a 1099-DA, and X on a 1099-B, as "holding period unknown: use your own records". For 2025 sales, brokers had to report gross proceeds but not basis, and a broker that left basis out used code Y (2025 Instructions for Form 1099-DA, pp. 1 and 4). Unless box 2 is checked, a 2025 sale on a 1099-DA goes in Box H or K.

**Digital asset on a Form 1099-B.** A few digital assets reach the user on a 1099-B instead (for 2025 only, a broker could report a tokenized asset sold for cash on either form; assets that are digital only because they settle on a limited-access regulated network stay on 1099-B) (2025 Instructions for Form 1099-DA, pp. 4–5). Follow the 1099-B into Box A/B/D/E: the Schedule D instructions tie the box to the form received (Instructions for Schedule D (2025), p. 4, Example 2), and Box I/L by its own text covers only digital assets not reported on a 1099-DA or 1099-B. Section 1256 contracts on digital assets reported in aggregate on a 1099-B go to Form 6781, not Form 8949.

**Cost-basis reporting cutoffs (IRC §6045(g)):**

| Asset type | "Covered" (reported to IRS) starts |
|------------|------------------------------------|
| Most equities | Acquired on or after Jan 1, 2011 |
| Mutual funds and DRIP shares | Acquired on or after Jan 1, 2012 |
| Debt instruments (most) | Acquired on or after Jan 1, 2014 |
| Certain options and other securities | Acquired on or after Jan 1, 2014 |
| Digital assets (Form 1099-DA) | Acquired after 2025 in a custodial account and held there until the sale (Instructions for Form 8949 (2025), p. 7; 2025 Instructions for Form 1099-DA, p. 2). Mandatory basis reporting starts with sales in 2026, on 1099-DAs furnished in 2027 (basis was voluntary for 2025 sales). |

Anything outside the covered scope is "non-covered" and lands in Box B or E (Box H or K for a digital asset on a 1099-DA).

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

Net sale proceeds in USD. If the 1099-B shows gross proceeds, subtract selling commissions (Form 8949 wants net). The 1099-B "Box 1d" is the figure the IRS will reconcile against — use exactly that number for Boxes A and D rows. For Boxes G, H, J, and K, use exactly 1099-DA box 1f, which the broker has already reduced by digital asset transaction costs (2025 Instructions for Form 1099-DA, p. 7). Costs the form does not reflect go in column (g) with code E (Instructions for Form 8949 (2025), p. 9).

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

One or more letters that explain why the gain/loss is being adjusted. Multiple codes stack in alphabetical order with no space or comma (e.g., "BOQ") (Instructions for Form 8949 (2025), pp. 7–8).

### Column (g) — Amount of adjustment

Column (g) is a **signed** amount. "Enter negative amounts in parentheses" (Instructions for Form 8949 (2025), p. 8). Column (h) is (d) − (e), then combined with (g) (same instructions, p. 11):

`(h) = (d) − (e) + (g)`, where (g) carries its own sign.

The sign depends on the code (instructions table, pp. 8–11):

- **Positive (raises gain / shrinks loss):** W (disallowed wash sale loss), L (other nondeductible loss), S (the ordinary loss claimed on Form 4797 for §1244 stock), Y (previously deferred QOF gain now recognized), N when the nominee row shows a loss, E for an option premium received, B when the reported basis is higher than the correct basis (Worksheet for Basis Adjustments, line 4).
- **Negative, in parentheses (lowers gain):** H (excluded home-sale gain), Q (§1202 exclusion), X (DC Zone / qualified community asset exclusion), R (postponed rollover gain), Z (deferred gain invested in a QOF), D (ordinary-income market discount, Worksheet line 5), E for selling expenses, digital asset transaction costs, or option premiums paid, N when the nominee row shows a gain, B when the correct basis is higher than the reported basis (Worksheet line 3).
- **Zero (-0-):** C (collectibles), M (multiple transactions on one row) unless another code needs an amount, T (wrong type of gain) unless another code needs an amount, B on a Box B/E/H/K row (put the correct basis in column (e) instead).
- **More than one code on a row:** enter the net (e.g., $5,000 and ($1,000) → $4,000) (p. 8).

When in doubt, compute the gain or loss the row must show in (h), then derive the signed (g) from the formula.

### Column (h) — Gain or (loss)

`(d) − (e) + (g)`. Losses shown in parentheses.

---

## Full adjustment code table (column f)

The IRS Form 8949 instructions list these codes. Checked letter by letter against the 2025 table "How To Complete Form 8949, Columns (f) and (g)" (Instructions for Form 8949 (2025), pp. 8–11):

| Code | When to use | What goes in (g) |
|------|-------------|------------------|
| **W** | Wash sale — loss disallowed under IRC §1091. Required when a loss is fully or partially disallowed because a substantially identical security was bought within the 61-day window. | Disallowed loss amount as a positive number. Column (h) will then equal $0 or the small allowed remainder. If the 1099-B box 1g / 1099-DA box 1i amount is wrong, enter the correct amount; attach a statement if yours is smaller. -0- if no part is a wash sale loss. |
| **B** | Basis on 1099-B (box 1e) or 1099-DA (box 1g) is incorrect. | Box B/E/H/K row: correct basis in (e), -0- in (g). Box A/D/G/J row: reported basis in (e), then (g) = reported basis − correct basis: positive if the reported basis is too high, negative in parentheses if too low (Worksheet for Basis Adjustments, p. 11). |
| **T** | The type of gain or loss in 1099-B box 2 / 1099-DA box 6 (short-term, long-term, ordinary) is incorrect. | Report on the correct Part; -0- unless another code needs an amount. |
| **N** | You received a 1099-B, 1099-DA, or 1099-S as a nominee for the actual owner. | Any resulting gain as a negative number, any loss as a positive number, so (h) = 0. |
| **H** | Sold your main home at a gain, must report it on Part II, and can exclude some or all of the gain under §121. | Excluded gain as a negative number (in parentheses). |
| **D** | 1099-B box 1f / 1099-DA box 1h shows accrued market discount — the discount portion is ordinary income, not capital gain. | Worksheet for Accrued Market Discount, line 5, as a negative number; -0- if you included market discount in income currently; partial principal payment: smaller of accrued discount or proceeds. |
| **Q** | §1202 QSBS (Qualified Small Business Stock) exclusion — any exclusion percentage, including 100% (Instructions for Schedule D (2025), p. 8). | The excluded gain as a negative number (in parentheses). |
| **X** | Exclusion of gain on DC Zone assets or qualified community assets (not QSBS). | The exclusion as a negative number (in parentheses). |
| **R** | You elect to postpone all or part of a gain under a rollover rule (e.g., rollover of gain from QSB stock). | The postponed gain as a negative number (in parentheses). |
| **L** | Nondeductible loss other than a wash sale (e.g., loss on a sale to a related party, or loss on personal-use property reported on a 1099-K or 1099-S). | Nondeductible loss as a positive number. |
| **C** | Collectibles — informs Schedule D that the gain is taxed at the maximum 28% rate. | -0-. The code feeds Schedule D Line 18 (28% Rate Gain Worksheet). |
| **S** | Loss on §1244 small business stock larger than the ordinary-loss limit ($50,000; $100,000 joint). The ordinary part goes on Form 4797; this row reports the capital part (Instructions for Schedule D (2025), pp. 6–7). | The loss claimed on Form 4797 as a positive number. |
| **O** | Adjustment not explained by any other code; also contingent payment debt instruments (worksheet on p. 12). | The appropriate amount; CPDI worksheet: ordinary gain negative, ordinary loss positive. |
| **E** | Selling expenses, option premiums, or digital asset transaction costs not reflected on the 1099-B, 1099-DA, or 1099-S. | Expenses, transaction costs, and premiums paid as a negative number; option premium received as a positive number. |
| **M** | Multiple transactions on a single row under Exception 2 or the special provision for certain entities. | -0- unless another code needs an amount. |
| **P** | Nonresident alien individual, foreign trust or estate, or foreign corporation that sold an interest in a partnership engaged in a U.S. trade or business. | Any adjustment under Regulations section 1.864(c)(8)-1(b) and (c). |
| **Y** | Recognizing gain from a QOF investment that was deferred in a prior year. | The previously deferred gain as a positive number (p. 13). |
| **Z** | Electing to defer eligible gain by investing in a QOF. | The deferred gain as a negative number (in parentheses), on its own row (p. 12). |

If none of these situations applies, leave columns (f) and (g) blank. Always verify against the current-year instructions before filing.

**Multiple codes**: when more than one applies, list them in alphabetical order with no spaces, and enter the net adjustment in (g). Example: "BW" means a basis correction on a wash sale.

---

## Page totals

Each Form 8949 page sums column (d), (e), (g), (h) at the bottom row. These page totals are what flow to Schedule D.

---

## Schedule D roll-up

Form 8949 always pairs with Schedule D. Box totals roll up like this:

```
Schedule D Part I — Short-Term Capital Gains and Losses
  Line 1a — Aggregate of 1099-B or 1099-DA basis-reported, no-adjustment transactions (optional; skips Form 8949)
  Line 1b — Box A and Box G totals (proceeds, basis, adjustment, gain/loss)
  Line 2  — Box B and Box H totals
  Line 3  — Box C and Box I totals
  Line 4  — Short-term gain from Form 6252 (installment sales), 4684 (casualty), 6781 (§1256), 8824 (§1031)
  Line 5  — Net short-term from partnerships, S-corps, estates, trusts (Schedule K-1)
  Line 6  — Short-term capital loss carryover (from prior year worksheet)
  Line 7  — Net short-term capital gain or loss (sum of 1a through 6)

Schedule D Part II — Long-Term Capital Gains and Losses
  Line 8a — Long-term counterpart of Line 1a (optional)
  Line 8b — Box D and Box J totals
  Line 9  — Box E and Box K totals
  Line 10 — Box F and Box L totals
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

Loss on §1244 stock can be treated as ordinary (not capital), up to $50,000 single / $100,000 MFJ per year. The ordinary part goes on Form 4797. Only a loss above the limit also goes on Form 8949: code "S" in column (f), the Form 4797 loss as a positive number in (g) (Instructions for Schedule D (2025), pp. 6–7).

### Like-kind exchange (§1031)

Real property only post-TCJA. Goes on **Form 8824**, not 8949. Any boot received may produce gain reportable on 8949.

### §1256 contracts (futures, broad-based index options)

60/40 treatment — 60% long-term, 40% short-term, regardless of holding period. Reported on **Form 6781**, then carried to Schedule D Lines 4 and 11. Not on 8949 directly.

### §1202 QSBS

Gain may be partially or fully excluded depending on acquisition date and holding period. The full gain still appears on 8949 with code Q, whether the exclusion is partial or 100%; the excluded portion is the negative adjustment in (g) (Instructions for Schedule D (2025), p. 8). Code X is for DC Zone / qualified community assets, not QSBS.

### Wash sales — see [`wash-sales.md`](./wash-sales.md)

### Crypto-specific — see [`crypto-reporting.md`](./crypto-reporting.md)

---

## Sources

- [Form 8949 (2025)](https://www.irs.gov/pub/irs-pdf/f8949.pdf) and [Instructions for Form 8949 (2025)](https://www.irs.gov/pub/irs-pdf/i8949.pdf) — boxes A–L, columns, codes
- [Instructions for Schedule D (2025)](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — box-to-line map, Example 2 on p. 4
- [Instructions for Form 1099-DA (2025)](https://www.irs.gov/pub/irs-prior/i1099da--2025.pdf) — 2025 proceeds-only reporting, Applicable checkbox codes, 1099-B carve-outs
- [Instructions for Form 1099-B (2025)](https://www.irs.gov/pub/irs-prior/i1099b--2025.pdf), p. 8 — code X (holding period unknown on a 1099-B)
