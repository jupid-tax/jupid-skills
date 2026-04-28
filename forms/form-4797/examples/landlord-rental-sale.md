# Example: Linda, Landlord Sells an 8-Year Rental

End-to-end Form 4797 for a §1250 real property disposition with unrecaptured §1250 gain at the 25% cap.

---

## Facts

- **Filer:** Linda, MFJ, owns rental real estate as an individual (Schedule E)
- **Asset:** Single-family rental at 123 Maple St
- **Date acquired:** 06/01/2017
- **Date sold:** 12/15/2025
- **Original total cost:** $300,000
- **Land allocation at purchase:** $60,000 (20%, based on county assessor split)
- **Building basis (depreciable):** $240,000
- **Depreciation method:** Straight-line MACRS, 27.5-year residential rental
- **Accumulated depreciation through 12/15/2025:** $74,182
- **Sales price:** $450,000
- **Selling expenses (commission, closing):** $20,000
- **Net sales price:** $430,000
- **No cost segregation study was performed**
- **Prior 5 years of §1231 history:** No prior §1231 gains or losses
- **Linda's MAGI:** $280,000 (above NIIT threshold $250K MFJ)

---

## Step 1 — Classification

The rental is **§1250 property** (depreciable real property, post-1986 MACRS straight-line). Held more than 1 year (8 years 6 months) → eligible for §1231 treatment. Goes through Part III first; residual lands in Part I via Line 6.

Land ($60K basis) is non-depreciable — its gain portion is pure §1231 with no recapture.

---

## Step 2 — Allocate sale proceeds between land and building

Apply the same 20% / 80% land/building ratio used at purchase:

| Component | Allocation | Original basis | Sale proceeds | Adjusted basis | Gain |
|-----------|-----------|----------------|---------------|----------------|------|
| Land | 20% | $60,000 | $86,000 | $60,000 | $26,000 |
| Building | 80% | $240,000 | $344,000 | $165,818 ($240K − $74,182) | $178,182 |
| **Total** | 100% | $300,000 | $430,000 | $225,818 | **$204,182** |

(Linda allocates the $20,000 selling expenses pro-rata: $4,000 to land reducing land sale to $86,000, $16,000 to building reducing building sale to $344,000.)

---

## Step 3 — Compute Part III for the building

### Part III, Column A: Building portion of 123 Maple St

| Line | Field | Value |
|------|-------|-------|
| 19 | Description | Rental at 123 Maple St (building portion) |
| 20 | Gross sales price | $344,000 |
| 21 | Cost or other basis | $240,000 |
| 22 | Depreciation allowed or allowable | $74,182 |
| 23 | Adjusted basis | $165,818 |
| 24 | Total gain | **$178,182** |

### §1250 recapture computation (Lines 26a-h)

Because Linda used straight-line MACRS (the only allowed method for residential rental real estate placed in service after 1986), there is no excess-over-straight-line depreciation:

| Line | Field | Value |
|------|-------|-------|
| 26a | Additional depreciation after 1975 | $0 |
| 26b | Applicable % × Line 26a | $0 |
| 26c | Subtract Line 26b from Line 26a | $0 |
| 26d | Additional depreciation 1969-1975 | $0 (post-1986 property) |
| 26e | Applicable % × smaller of Line 24 or 26d | $0 |
| 26f | §291 corporate addition | $0 (Linda is an individual, not a C-corp) |
| 26g | **§1250 recapture** | **$0** |
| 26h | Combine | $0 |

### Part III rollup

| Line | Field | Value |
|------|-------|-------|
| 30 | Column A total recapture | $0 |
| 31 | Sum across columns | $0 |
| 32 | To Part II Line 13 | **$0** |

Residual gain after recapture (Line 24 − Line 32) = $178,182 − $0 = **$178,182** flows to Part I Line 6.

---

## Step 4 — Land portion: enter on Part I Line 2 directly

Land is non-depreciable, so it does NOT go through Part III. Enter directly on Part I Line 2:

| Line 2 columns | Value |
|----------------|-------|
| (a) Description | Land at 123 Maple St |
| (b) Date acquired | 06/01/2017 |
| (c) Date sold | 12/15/2025 |
| (d) Gross sales price | $86,000 |
| (e) Depreciation | $0 |
| (f) Cost basis | $60,000 |
| (g) Gain or loss | **$26,000** |

---

## Step 5 — Part I rollup

| Line | Field | Value |
|------|-------|-------|
| 2 | Land portion | $26,000 |
| 6 | §1231 gain from Part III (building residual) | $178,182 |
| 7 | Net §1231 gain | **$204,182** |
| 8 | 5-year lookback | $0 (no prior §1231 losses) |
| 9 | Long-term capital gain → Schedule D Line 11 | **$204,182** |

---

## Step 6 — Part II rollup

| Line | Field | Value |
|------|-------|-------|
| 10-12 | (no entries) | $0 |
| 13 | Recapture from Part III Line 32 | $0 |
| 18 | Total ordinary | **$0** |

No ordinary income from this disposition.

---

## Step 7 — Unrecaptured §1250 Gain Worksheet (Schedule D)

The depreciation portion of the building gain ($74,182) is **unrecaptured §1250 gain** taxed at a maximum 25% federal rate. This is computed on the Unrecaptured §1250 Gain Worksheet in the Schedule D instructions:

```
Line 1: Smaller of (Line 22 depreciation = $74,182) or (Line 24 gain = $178,182):  $74,182
Line 2: Adjustments (none):                                                          $0
Line 3: Net unrecaptured §1250 gain:                                               $74,182
```

Enter $74,182 on **Schedule D Line 19**.

---

## Step 8 — Schedule D rollup and tax computation

| Schedule D Line | Field | Value |
|-----------------|-------|-------|
| 11 | Long-term gain from Form 4797 Part I Line 9 | $204,182 |
| 15 | Net long-term capital gain | $204,182 |
| 16 | Total capital gains (Line 7 + Line 15) | $204,182 |
| 19 | Unrecaptured §1250 gain | $74,182 |

The Schedule D Tax Worksheet (in Schedule D instructions) splits the gain:

```
Pure long-term capital gain (LTCG rate 0/15/20%):  $204,182 − $74,182 = $130,000
Unrecaptured §1250 gain (max 25% rate):                                  $74,182
Total long-term gain:                                                  $204,182
```

---

## Step 9 — Tax impact

Linda's other 2025 income (besides this sale):
- Salary: $200,000
- Other rental net income: $5,000
- Pre-§4797 MAGI: ~$210,000
- Filing status: MFJ
- Bracket pre-sale: 24%

Adding the §1231 gain:
- Total LTCG bracket falls within 15% (taxable income $96,701 − $600,050 for MFJ in 2025)
- Unrecaptured §1250 gain capped at 25% (but since Linda's marginal ordinary rate is 24%, the actual rate for her is min(25%, 24%) = 24%) — wait, the cap is "maximum 25%" meaning unrecaptured §1250 is taxed at the **lesser of 25% or the filer's marginal ordinary rate**. So for Linda the unrecaptured §1250 gain is taxed at 24% (her ordinary rate), not 25%.

Actually, re-checking: IRC §1(h)(1)(E) imposes a 25% maximum, but the rate is the regular rate up to 25% — so it's effectively 25% for filers in 25%+ ordinary brackets, and the ordinary rate for filers below 25%. With the 2025 MFJ brackets, Linda's $210K + $204K gain pushes her to higher brackets — likely 32%+ on the ordinary income. So:

```
Ordinary tax on salary + rental income:        ~$40,000 (existing)
NIIT on existing $5K rental income:                $190 (rental income is investment income for NIIT)

NEW from §4797:
  Unrecaptured §1250 (capped at 25%):    $74,182 × 25%  = $18,545
  Pure LTCG at 15%:                      $130,000 × 15% = $19,500
  NIIT 3.8% on full $204,182:                           = $7,759
  
Total NEW federal tax from this sale:                   = $45,804
```

Compare to alternative — if Linda had wrongly classified everything as ordinary §1245 (it's not, but illustratively): 32% × $204,182 = $65,338. The §1250 / unrecaptured §1250 gain treatment saves Linda about $20K of federal tax compared to ordinary treatment, even after NIIT.

---

## Step 10 — Required attachments and downstream forms

- [x] Schedule D with Line 11 = $204,182, Line 19 = $74,182
- [x] Schedule D Tax Worksheet (computes blended LTCG / unrecaptured §1250 / NIIT)
- [x] Form 8960 (Net Investment Income Tax) — $7,759 on the $204,182 (rental gain is investment income for NIIT)
- [x] Form 4562 — prior-year depreciation history (referenced, not re-attached)
- [ ] Form 6252 — N/A (cash sale)
- [ ] Form 8824 — N/A (not a §1031 exchange)

---

## Lessons from this example

1. **§1250 recapture is usually $0 for post-1986 rentals under MACRS.** But the depreciation portion is still taxed differently (25% cap), which feels like recapture from the filer's perspective.

2. **Land is non-depreciable but still goes on Form 4797.** Land basis and proceeds are allocated separately and the gain is pure §1231 with no recapture layer.

3. **Land/building allocation must be consistent** between purchase and sale. Linda used 20% land at both ends — defensible. Drifting the allocation is an audit flag.

4. **NIIT applies on top of LTCG and unrecaptured §1250 gain.** The 3.8% NIIT on $204K = $7,759 — meaningful additional cost for high-MAGI filers.

5. **§121 exclusion does NOT apply.** Linda has not used this property as a primary residence, so §121 is unavailable. If she had, the depreciation portion ($74K unrecaptured §1250) would still be taxable at 25% even with §121 — only the appreciation portion ($130K) could be excluded up to $250K/$500K.
