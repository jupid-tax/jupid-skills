# Tax Rate Worksheets — Picking the Right One

Schedule D Lines 17–22 don't compute the tax. They tell you which **worksheet** computes it. Picking the wrong worksheet is the most common Schedule D mistake and often costs filers thousands.

There are two preferential-rate worksheets and the regular tax tables.

---

## Worksheet A — Qualified Dividends and Capital Gain Tax Worksheet

**Location:** Form 1040 Instructions (not Schedule D's instructions).

**When to use:**

- Schedule D Line 18 = 0 **and** Line 19 = 0 (no collectibles, no §1250 unrecaptured gain, no §1202 partial-exclusion gain), **and**
- The user has either: a net long-term capital gain (Schedule D Line 15 > 0 leading to Line 16 > 0), or qualified dividends on Form 1040 Line 3a, or both

**Logic:**

1. Compute taxable income (Form 1040 Line 15).
2. Subtract long-term gain + qualified dividends → "ordinary income only" base.
3. Compute regular tax on the ordinary base using the tax tables.
4. Stack the long-term gain + qualified dividends on top, in 0%/15%/20% brackets:
   - Portion within the 0% LTCG bracket: 0% tax
   - Portion within the 15% LTCG bracket: 15% tax
   - Portion in the 20% LTCG bracket: 20% tax
5. Total tax = ordinary tax + LTCG tax.

**2025 LTCG bracket cutoffs (Rev. Proc. 2024-40):**

| Filing status | 0% bracket top | 15% bracket top | 20% starts above |
|---------------|-----------------|------------------|-------------------|
| Single | $48,350 | $533,400 | $533,400 |
| MFJ / QSS | $96,700 | $600,050 | $600,050 |
| HoH | $64,750 | $566,700 | $566,700 |
| MFS | $48,350 | $300,000 | $300,000 |
| Estates / Trusts | $3,250 | $15,900 | $15,900 |

**2026 figures:** Indexed for inflation; published by IRS in October–November 2025. Verify against the most recent Revenue Procedure before filing a 2026 return.

**Worked example:**

```
Single filer, 2025:
  Wages (ordinary income):        $90,000
  Long-term capital gain:         $15,000
  Qualified dividends:             $2,000
  Total income:                  $107,000
  Standard deduction:            ($15,000) [single 2025]
  Taxable income (Line 15):       $92,000

Step 1: Ordinary base = $92,000 − $15,000 − $2,000 = $75,000
Step 2: Regular tax on $75,000 (single, 2025 tables) ≈ $11,825
Step 3: LTCG layer — $17,000 stacked on top of $75,000:
  - Portion within 0% bracket (cutoff $48,350): $0 (already past it)
  - Portion within 15% bracket: $17,000 × 15% = $2,550
  - Portion above $533,400: $0
Step 4: Total tax = $11,825 + $2,550 = $14,375

Compare to "wrong worksheet" path:
  Regular tax on $92,000 ≈ $15,571
  Difference: $1,196 overpayment if the user used regular tables
```

---

## Worksheet B — Schedule D Tax Worksheet

**Location:** Schedule D Instructions.

**When to use:**

- Schedule D Line 18 > 0 (28% rate gain — collectibles or §1202 partial exclusion), **or**
- Schedule D Line 19 > 0 (unrecaptured §1250 gain — real estate depreciation)

**Logic:** Layers four rate buckets:

1. **Ordinary income** at regular rates (10%–37%)
2. **§1250 unrecaptured gain (Line 19)** at maximum 25%
3. **28% rate gain (Line 18)** at maximum 28%
4. **Remaining net long-term gain + qualified dividends** at 0/15/20%

The "maximum 25%" / "maximum 28%" language matters: if the user's ordinary bracket is below those rates, they pay the lower ordinary rate on the §1250 / collectibles bucket.

**Worked example — rental real estate sale:**

```
Single filer, 2025:
  Wages:                          $80,000
  Rental sale gain (LT):         $100,000
    of which §1250 unrecaptured:  $30,000 (depreciation taken)
    of which §1231 capital:       $70,000 (appreciation)
  Total income:                  $180,000
  Standard deduction:            ($15,000)
  Taxable income:                $165,000

Schedule D entries:
  Line 11 (§1231 from Form 4797): $100,000
  Line 15 (Net LT):                $100,000
  Line 16:                         $100,000
  Line 19 (Unrecaptured §1250):    $30,000

Schedule D Tax Worksheet:
  Bucket 1 — ordinary on $65,000 (taxable − LT gain) ≈ $9,200
  Bucket 2 — §1250 unrecaptured: $30,000 × 25% = $7,500
  Bucket 3 — 28% rate (none): $0
  Bucket 4 — remaining LT $70,000 × 15% = $10,500
  Total tax: $27,200

Compare to "wrong worksheet" (Qualified Dividends and Capital Gain Tax Worksheet):
  This worksheet doesn't have a 25% bucket — it would route the
  full $30,000 §1250 gain at 15%, saving $3,000. Filers sometimes
  *accidentally* use the wrong worksheet and underpay; the IRS
  catches it via the Form 4797 / Schedule D crosswalk.
```

---

## Worksheet C — Regular Tax Tables / Tax Computation Worksheet

**Location:** Form 1040 Instructions.

**When to use:**

- Schedule D Line 16 ≤ 0 (net loss or zero gain), **and**
- No qualified dividends

This is the default. Tax is computed solely on ordinary income.

If you have qualified dividends but Line 16 is zero or a loss, use **Worksheet A** to capture the dividend portion at preferential rates.

---

## Decision tree

```
Schedule D Line 18 > 0 OR Line 19 > 0?
├── YES → Schedule D Tax Worksheet (Worksheet B)
└── NO  → Continue
    │
Schedule D Line 16 > 0 OR Form 1040 Line 3a (qualified dividends) > 0?
├── YES → Qualified Dividends and Capital Gain Tax Worksheet (Worksheet A)
└── NO  → Regular tax tables (Worksheet C)
```

---

## Common errors and IRS detection

### Error: Using regular tables when long-term gain qualifies for preferential rate

**Pattern:** DIY filer on paper, no software. Computes "regular tax" on Form 1040 Line 24 using the tables, ignores the LTCG bracket.

**IRS detection:** Doesn't catch — the IRS computer accepts the higher tax as long as it's not lower than the correct amount. The filer overpays and never gets the difference back automatically.

**Fix:** Amend with Form 1040-X within 3 years.

### Error: Using Qualified Dividends and Capital Gain Tax Worksheet when Schedule D Tax Worksheet was required

**Pattern:** Real estate sale with depreciation; Line 19 > 0; filer uses the simpler worksheet.

**IRS detection:** Often catches — the Form 4797 / Schedule D crosswalk on the IRS side identifies the §1250 component and recomputes the tax. Underpayment notice with interest.

**Fix:** Recompute using Schedule D Tax Worksheet. If the difference is large, an amended return is preferable to waiting for a notice.

### Error: Carryover from prior year not applied

**Pattern:** $20,000 net loss in 2024; only $3,000 used; $17,000 carried forward. Filer forgets to enter on Schedule D Line 6 / 14 in 2025.

**IRS detection:** Doesn't catch — the IRS doesn't track carryovers. The filer overpays and the carryover is permanently lost (unless amended within 3 years).

**Fix:** Save the prior-year Capital Loss Carryover Worksheet every year. If using software, carry the same software (or import) year over year.

---

## State considerations

Most states do **not** have a preferential capital gain rate — capital gains are taxed at the ordinary state income rate. Notable exceptions:

- **Hawaii** — 7.25% maximum on long-term capital gains (lower than the 11% top ordinary rate)
- **Some states** — exemptions for specific asset categories (e.g., Wisconsin's 30% LT exclusion)

Some states have different capital loss carryover rules:

- **California** — net loss limit is $3,000 (matches federal), but carryover rules can differ; state uses its own AGI definitions
- **New Jersey** — does not allow capital loss carryover at all; net losses lost permanently in the year incurred

When preparing a state return, do not assume federal Schedule D figures transfer cleanly. Each state has its own capital gain schedule (CA Schedule D, NY IT-201 attachment, etc.).

---

## Sources

- [Form 1040 Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — contains Qualified Dividends and Capital Gain Tax Worksheet
- [Schedule D Instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — contains Schedule D Tax Worksheet, 28% Rate Gain Worksheet, Unrecaptured §1250 Gain Worksheet
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) — 2025 inflation-adjusted brackets
- IRC §1(h) — capital gain rate structure
