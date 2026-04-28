# Example: Real Estate Sale with §1250 Unrecaptured Gain — David

A landlord who sold a rental property in 2025. Demonstrates the Form 4797 → Schedule D Line 11 routing, the Unrecaptured §1250 Gain Worksheet, and the Schedule D Tax Worksheet.

---

## Filer profile

- **Name:** David ___
- **Filing status:** Married Filing Jointly
- **Tax year:** 2025
- **Wages (combined):** $190,000
- **Standard deduction:** $30,000 (MFJ, 2025)
- **Other income:** $0
- **Qualified dividends:** $4,200
- **Capital gain distributions (1099-DIV Box 2a):** $1,800
- **Prior-year capital loss carryover:** $0

## Property facts

- **Acquired:** January 2010 for $400,000 (allocate $80,000 to land, $320,000 to building per appraisal)
- **Use:** Held as a rental property for 16 years
- **Depreciation method:** 27.5-year residential straight-line on the $320,000 building portion
- **Total depreciation taken (2010–2025):** Approximately $174,545 (16 × $320,000 / 27.5 = $186,182, less partial-year proration in 2010 and 2025)
   For this example, use $174,545 for clean math
- **Sold:** July 2025 for $700,000 (closing costs $42,000)
- **Net proceeds:** $658,000
- **Adjusted basis at sale:** $400,000 − $174,545 = $225,455

## Gain computation

```
Gross gain on sale:        $658,000 − $225,455 = $432,545

Of which:
  Unrecaptured §1250 (depreciation taken portion):  $174,545
  Pure appreciation (remainder):                    $258,000
```

This is a §1231 gain (business-use property held more than 1 year) with §1250 depreciation recapture treatment.

---

## Form 4797 walkthrough

David first completes Form 4797 (Sales of Business Property). This is the gateway form for any business-use disposition.

- **Form 4797 Part I:** Section 1231 sales. Property held more than 1 year used in trade or business.
- **Form 4797 Part III:** Recapture under §§1245, 1250. The §1250 depreciation portion is computed here.

For §1250 residential real estate using straight-line depreciation, **none of the depreciation is recaptured as ordinary income** under §1250(b) — straight-line depreciation is exempt from §1250 ordinary recapture. Instead, the depreciation portion becomes "unrecaptured §1250 gain" and is taxed at the **maximum 25% capital gain rate** under IRC §1(h)(6).

(If David had used accelerated depreciation, the excess over straight-line would have been §1250 ordinary recapture. He didn't.)

Net §1231 gain from Form 4797: **$432,545** → Schedule D Line 11.

---

## Schedule D walkthrough

### Part I — Short-Term

David has no short-term capital activity.

| Line | Amount |
|------|--------|
| 7 | $0 |

### Part II — Long-Term

| Line | Description | Amount |
|------|-------------|--------|
| 8b | Box D 8949 | $0 |
| 9 | Box E 8949 | $0 |
| 10 | Box F 8949 | $0 |
| 11 | **Form 4797 §1231 net gain** | **$432,545** |
| 12 | K-1 LT | $0 |
| 13 | 1099-DIV Box 2a | $1,800 |
| 14 | Prior-year LT carryover | $0 |
| **15** | **Net long-term** | **$434,345** |

### Part III — Summary

| Line | Calculation | Amount |
|------|-------------|--------|
| 16 | Line 7 + Line 15 = $0 + $434,345 | **$434,345** |
| 17 | Both Lines 15 and 16 are gains? | Yes |
| 18 | 28% Rate Gain Worksheet (no collectibles, no §1202) | $0 |
| 19 | **Unrecaptured §1250 Gain Worksheet** | **$174,545** |
| 20 | Line 19 > 0 → use **Schedule D Tax Worksheet** | Yes |

→ Form 1040 Line 7: **$434,345**

---

## Schedule D Tax Worksheet computation

Because Line 19 > 0, David must use the Schedule D Tax Worksheet (not the simpler Qualified Dividends and Capital Gain Tax Worksheet).

David's taxable income:
```
Wages:                            $190,000
LT gain (Line 16):                $434,345
Qualified dividends:                $4,200
AGI:                              $628,545
Standard deduction:               ($30,000)
Taxable income (Form 1040 Line 15): $598,545
```

**Schedule D Tax Worksheet — bucket allocation:**

```
Step 1: Bucket amounts.
   Ordinary income (excluding LT gain and qualified dividends):
       $598,545 − $434,345 − $4,200 = $160,000

   §1250 unrecaptured gain bucket:    $174,545  (max 25%)
   28% rate gain bucket:                   $0
   Remaining LT gain + qualified div: $434,345 + $4,200 − $174,545 = $264,000  (0/15/20%)

Step 2: Ordinary tax on $160,000 (MFJ 2025) ≈ $26,440
   (taxable income $90,750–$201,050 = 22% bracket portion; below $96,700 = 12%, etc.)

Step 3: Layer the special-rate buckets on top.

   Layer 1: 0/15/20% bucket — $264,000 stacked on top of ordinary $160,000.
      Position: $160,000 → $424,000.
      MFJ LTCG brackets: 0% up to $96,700, 15% to $600,050, 20% above.
      Already past 0% bracket. Entire $264,000 in 15% bracket.
      Tax: $264,000 × 15% = $39,600

   Layer 2: §1250 unrecaptured bucket — $174,545 stacked on top of $424,000.
      Position: $424,000 → $598,545.
      Maximum rate 25%. Worksheet applies 25% (since ordinary bracket at this position is 35%, well above 25%).
      Tax: $174,545 × 25% = $43,636

Step 4: Total tax = $26,440 + $39,600 + $43,636 = $109,676
```

**Compare to the wrong worksheet path** — if David used the Qualified Dividends and Capital Gain Tax Worksheet (which has no 25% bucket), the §1250 portion would land in the 15% LTCG bracket:

```
Wrong path: ($264,000 + $174,545) × 15% = $65,782 LTCG tax
Total: $26,440 + $65,782 = $92,222

Underpayment: $109,676 − $92,222 = $17,454
```

The IRS catches this via the Form 4797 / Schedule D crosswalk — Form 4797 reports the §1250 portion, and the IRS recomputes Schedule D using the correct rate. Notice with interest follows.

---

## NIIT — Form 8960

David's MAGI is $628,545, well above the MFJ $250,000 threshold.

```
Net Investment Income:
   Net capital gain (Line 16):     $434,345
   Qualified dividends:               $4,200
   1099-DIV Box 2a:                   (already in cap gain)
   Investment interest expense:      ($0 assumed)
   Total NII:                       $438,545

MAGI excess: $628,545 − $250,000 = $378,545

NIIT base: MIN($438,545, $378,545) = $378,545
NIIT: $378,545 × 3.8% = $14,385

→ Schedule 2 Line 12 → Form 1040 Line 23
```

The MAGI excess is the binding constraint here, not NII — David's MAGI is high enough that the NII is fully exposed up to the $378,545 cap.

---

## Total federal tax on the property sale

```
Schedule D Tax Worksheet result:    $109,676 (regular tax)
   of which on the property sale:    $83,236 (excludes ordinary on wages portion)
NIIT:                                $14,385
Total federal:                       $124,061 attributable to capital gain (rough allocation)
```

Plus state tax (varies by state). For a California filer, add roughly $434,345 × 9.3% = $40,394 state tax. Total all-in tax on the $432,545 gain: roughly $164,000 — about 38% effective rate.

---

## Validation checks

- [x] Form 4797 completed first; §1231 net gain = $432,545
- [x] Schedule D Line 11 = Form 4797 §1231 gain = $432,545
- [x] Line 15 = $434,345 (Line 11 + Line 13)
- [x] Line 16 = $434,345
- [x] Line 19 (§1250) = $174,545 (depreciation taken, capped at gain — $174,545 < $432,545 ✓)
- [x] Line 19 > 0 → Schedule D Tax Worksheet (not Qualified Dividends and Capital Gain Tax Worksheet)
- [x] MAGI > $250K MFJ → Form 8960 required
- [x] Net §1231 gain (not §1231 loss) — converts to LT capital, not ordinary

---

## What David should know

1. **Depreciation recapture is the price of the depreciation deductions.** David got 16 years of $11,200/year depreciation deductions (about $179K of total deductions), saving roughly $40K to $50K in income tax over the holding period. The $43,636 of §1250 recapture is the deferred bill on those deductions — paid at the lower 25% capital rate, not the higher ordinary rates. This is still a net win.

2. **§1031 deferral was an option.** David could have rolled the gain into another rental property within 45/180 days under IRC §1031, deferring the full tax bill until the replacement property is eventually sold. Step-up basis at death (§1014) can wipe out the deferred gain entirely if held until death.

3. **State conformity matters.** California taxes the entire $434,345 at ordinary rates (no preferential capital gain treatment). State tax stacks on top.

4. **Estimated tax payments.** David should have made 2025 quarterly estimated payments to cover the federal tax on the sale; otherwise an underpayment penalty applies at year-end. If the sale was in July, the Q3 payment due September 15 should have included the gain.

---

## Hand-off downstream

- [x] **Form 4797** — Part I and Part III completed
- [x] **Form 8949** — not required for this transaction (it's §1231, not capital, until the conversion at Schedule D Line 11)
- [x] **Schedule D** — Line 11 receives Form 4797 net §1231; Line 19 from Unrecaptured §1250 Gain Worksheet; Schedule D Tax Worksheet computes tax
- [x] **Form 8960** — NIIT $14,385
- [ ] **Form 1040 Line 7** — enter $434,345
- [ ] **Form 1040 Line 16** — enter $109,676 from Schedule D Tax Worksheet
- [ ] **Schedule 2 Line 12** — enter $14,385 NIIT
- [x] **State return** — flag full ordinary-rate treatment in CA / NY / NJ / etc.

---

## Sources

- [Form 4797](https://www.irs.gov/pub/irs-pdf/f4797.pdf) — Sales of Business Property
- [Instructions for Form 4797](https://www.irs.gov/pub/irs-pdf/i4797.pdf)
- [Schedule D (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sd.pdf)
- [Instructions for Schedule D](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — contains Unrecaptured §1250 Gain Worksheet and Schedule D Tax Worksheet
- [Form 8960](https://www.irs.gov/pub/irs-pdf/f8960.pdf)
- [Publication 544](https://www.irs.gov/publications/p544) — Sales and Other Dispositions of Assets
- [Publication 946](https://www.irs.gov/publications/p946) — How to Depreciate Property
- IRC §1(h)(6) (25% rate cap), §1231 (business property), §1250 (depreciation recapture), §1411 (NIIT)
