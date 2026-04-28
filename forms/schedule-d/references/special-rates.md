# Special Capital Gain Rates — 28%, 25%, and §1202 QSBS

The headline 0/15/20% LTCG rate is the most common, but Schedule D recognizes three special rates that apply to specific asset categories. Getting these right requires both correct categorization on Form 8949 and the right tax-rate worksheet on Schedule D.

---

## 28% rate — Collectibles and §1202 partial exclusion (IRC §1(h)(4))

**Maximum rate:** 28%

The 28% rate applies to:

1. **Collectibles** held more than one year:
   - Works of art
   - Antiques
   - Gold, silver, platinum coins and bullion (with limited exceptions for some bullion ETFs)
   - Gems
   - Stamps and coins (collectible numismatic value)
   - Wine and spirits held as investments
   - Rare books and manuscripts
   - Classic cars held as investments (not used as a vehicle)

2. **§1202 QSBS gain that is not fully excluded** — typically the included portion when the exclusion is partial (e.g., 50% or 75% exclusions for stock acquired in different windows).

### How it appears on Form 8949

- Code **C** in column (f) for collectibles
- Code **Q** in column (f) for §1202 QSBS partial-exclusion gain (with the excluded portion as a negative adjustment in column (g))

The full gain still appears in column (h); the 28% rate is applied later via the Schedule D Tax Worksheet.

### How it appears on Schedule D

The **28% Rate Gain Worksheet** in the Schedule D instructions pulls all collectibles gain (code C) and the included §1202 portion (code Q) into a single bucket. The result populates **Schedule D Line 18**.

Schedule D Line 18 forces the use of the **Schedule D Tax Worksheet** instead of the simpler Qualified Dividends and Capital Gain Tax Worksheet.

### "Maximum 28%" — the actual mechanic

The 28% is a **ceiling**. If the user's ordinary income bracket is below 28%, the gain is taxed at the lower ordinary rate. The Schedule D Tax Worksheet handles this:

- If ordinary bracket = 22% and user has $5,000 collectibles gain: tax = $5,000 × 22% = $1,100 (not $1,400)
- If ordinary bracket = 32% and user has $5,000 collectibles gain: tax = $5,000 × 28% = $1,400 (capped at 28%)

Most middle-income filers with collectibles gains never actually pay 28% because their ordinary bracket is below it. The 28% cap matters most for filers in the 32%, 35%, or 37% ordinary brackets.

---

## 25% rate — Unrecaptured §1250 Gain (IRC §1(h)(6))

**Maximum rate:** 25%

Applies to gain on real estate (or other §1250 property) attributable to **prior depreciation taken**. The depreciation portion of the gain is "unrecaptured" up to the maximum 25% rate. The remainder of the gain (above the depreciation portion) is taxed at the regular 0/15/20% LTCG rate.

### When it applies

- Sale of rental real estate (residential or commercial) with prior depreciation deductions
- Sale of a primary residence with prior rental years (mixed use)
- Sale of farmland or commercial real estate with §168 cost recovery taken
- Section 1250 property with allowable straight-line depreciation

§1250 property specifically excludes §1245 property (machinery, equipment, intangibles), which has its own ordinary-rate recapture treatment under §1245. Those go on Form 4797 Part III.

### Where the math happens

This is a **two-form** computation:

1. **Form 4797 (Sales of Business Property)** — Part III computes "unrecaptured §1250 gain" based on the asset's prior depreciation and the sale price.
2. **Schedule D Line 11** — Receives the **net §1231 gain** from Form 4797 (which includes the §1250 portion).
3. **Unrecaptured §1250 Gain Worksheet** in Schedule D instructions — Pulls the §1250 portion out and routes it to **Schedule D Line 19**.
4. **Schedule D Tax Worksheet** — Applies 25% (or lower ordinary rate) to the Line 19 amount.

### Worked example

Rental property purchased 2010 for $300,000 (building only, ignoring land for simplicity). 27.5-year residential straight-line depreciation. Sold 2025 for $500,000. Total depreciation taken: 15 years × ($300,000 / 27.5) = $163,636.

```
Sale price:                $500,000
Adjusted basis: $300,000 − $163,636 = $136,364
Gain on sale:              $363,636

Of which:
  Unrecaptured §1250 (depreciation taken):  $163,636  → 25% rate (max)
  Remainder ($363,636 − $163,636):          $200,000  → 0/15/20% LTCG rate

If filer is in the 22% ordinary bracket:
  §1250 portion: $163,636 × 22% = $36,000 (capped at ordinary < 25%)
  Remainder: $200,000 × 15% = $30,000
  Total LTCG tax: $66,000

If filer is in the 32% ordinary bracket:
  §1250 portion: $163,636 × 25% = $40,909 (capped at 25%)
  Remainder: $200,000 × 15% = $30,000
  Total LTCG tax: $70,909
```

**Caveat:** The §1250 portion is capped at the actual gain. If the property sold at a price below adjusted basis, no §1250 recapture applies (you can't recapture more than the gain).

### Why this matters

The "wrong worksheet" mistake is most expensive here. A filer using the Qualified Dividends and Capital Gain Tax Worksheet (which has no 25% bucket) for a real estate sale would tax the entire gain at 15%, *underpaying* by $16,364 in the 32%-bracket example above. The IRS catches this via the Form 4797 / Schedule D crosswalk and issues a notice.

---

## §1202 — Qualified Small Business Stock Exclusion

**Exclusion:** Up to 100% of gain (subject to per-issuer cap) excluded from federal income tax, including NIIT.

§1202 is one of the most generous tax provisions in the Code, and one of the most under-used. For founders and angel investors in qualified C-corps, it can mean the difference between paying 23.8% federal tax on a $10M gain and paying $0.

### Eligibility (high level)

For stock to qualify as Qualified Small Business Stock (QSBS):

1. **Issuer must be a domestic C-corp** at the time of issuance (and during substantially all of holding period)
2. **Original issuance** — stock acquired directly from the corporation, not from a secondary buyer
3. **Small business test** — corporation's aggregate gross assets did not exceed $50 million immediately before and after issuance
4. **Active business test** — corporation must use at least 80% of assets in qualified active business (excludes holding companies, certain service businesses, hospitality, finance)
5. **Holding period** — stock held more than 5 years before sale
6. **Acquisition date matters** — exclusion percentages differ:

| Acquisition date | Exclusion % | AMT preference? |
|------------------|--------------|------------------|
| Before Feb 18, 2009 | 50% | Yes |
| Feb 18, 2009 – Sept 27, 2010 | 75% | Yes |
| **After Sept 27, 2010** | **100%** | **No** |

Most modern QSBS sales benefit from the 100% exclusion under the post-September 27, 2010 rule.

### Per-issuer cap (IRC §1202(b))

Excluded gain is limited to the **greater** of:
- $10,000,000 (cumulative across all years), or
- 10× the taxpayer's adjusted basis in the QSBS

If the basis is $100,000, the cap is the greater of $10M or $1M → $10M.
If the basis is $5,000,000, the cap is the greater of $10M or $50M → $50M.

The cap is per-issuer (per company), per-taxpayer.

### How it appears on Form 8949

- Code **Q** for partial exclusion (50% or 75% windows)
- Code **X** for full exclusion (post-September 27, 2010 acquisitions)
- The excluded portion goes in column (g) as a negative adjustment
- Column (h) = (d) − (e) + (g) — typically zero (full exclusion) or a remainder (partial)

### How it appears on Schedule D

For 100% excluded gain (code X): the gain is fully eliminated on Form 8949; Schedule D never sees it. No 28% rate consideration, no NIIT, no state tax (subject to state conformity).

For partially excluded gain (code Q): the included portion appears in column (h), flows to Schedule D Lines 8a/8b/9/10, and the included portion *also* flows to the 28% Rate Gain Worksheet → Line 18. The 28% rate applies to the included portion.

### State conformity

States vary on §1202 conformity:
- **Federal-conforming:** Gain follows federal exclusion. Most states.
- **Non-conforming:** California (does not conform — CA taxes the full gain), Pennsylvania, and a few others.
- **Partial conforming:** Some states cap the exclusion or use different acquisition windows.

For a filer with a $10M federally-excluded QSBS gain in California, state tax is still owed at 13.3% top rate = $1.33M. Plan accordingly.

### Common errors

- **Holding period miscount:** 5 years means more than 5 years (5 years and 1 day). Selling on the 5-year anniversary disqualifies — wait until day 1,827.
- **Section 1045 rollover ignored:** If the user sold QSBS held less than 5 years, they may roll the gain into other QSBS within 60 days under §1045 to preserve eventual exclusion. Many filers miss this option.
- **Stacking strategies:** Gifting QSBS to family members or trusts creates a per-recipient cap, multiplying the $10M exclusion. Aggressive but legal under current rules.
- **State exclusion missed:** Even when federal exclusion is taken, state may not conform. Surface this for state return preparation.

---

## How these interact on Schedule D

A taxpayer can have all three special-rate categories on a single return:

**Example — multi-bucket filer:**
- Stock sale (covered, basis reported): $50,000 long-term gain → Box D → 0/15/20%
- Rare book collection sale: $20,000 long-term gain → Box F + code C → 28% rate
- Rental property sale: $200,000 gain (of which $80,000 §1250) → Form 4797 → Schedule D Line 11
- §1202 QSBS sale: $5,000,000 gain (100% excluded) → Form 8949 + code X → no Schedule D impact

Schedule D Lines 18 and 19 will both be > 0, forcing the **Schedule D Tax Worksheet**. The QSBS gain doesn't appear on Schedule D at all (excluded). The remaining buckets are taxed:

| Bucket | Amount | Rate | Tax |
|--------|--------|------|-----|
| 28% (collectibles) | $20,000 | 28% (or lower ordinary) | varies |
| 25% (§1250) | $80,000 | 25% (or lower ordinary) | varies |
| 0/15/20% (remainder LT) | $170,000 | 15% or 20% based on bracket | varies |

The Schedule D Tax Worksheet computes the layered tax in the right order.

---

## Sources

- [IRC §1(h)](https://www.law.cornell.edu/uscode/text/26/1) — Maximum capital gains rate structure
- [IRC §1202](https://www.law.cornell.edu/uscode/text/26/1202) — Partial / full exclusion for QSBS
- [IRC §1250](https://www.law.cornell.edu/uscode/text/26/1250) — Recapture of depreciation on real estate
- [Schedule D Instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — 28% Rate Gain Worksheet, Unrecaptured §1250 Gain Worksheet, Schedule D Tax Worksheet
- [Form 4797](https://www.irs.gov/pub/irs-pdf/f4797.pdf) — Sales of Business Property
- [Publication 544](https://www.irs.gov/publications/p544) — Sales and Other Dispositions of Assets
- [Publication 550](https://www.irs.gov/publications/p550) — Investment Income and Expenses
