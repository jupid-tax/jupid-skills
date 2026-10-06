# Example — Multi-Business Aggregation (Property Management + Rental Real Estate)

End-to-end Form 8995-A walkthrough for an owner of two related businesses who elects aggregation under Schedule B. Tax year 2025 (filed in 2026); 2025 Form 8995-A, Schedule B (Rev. December 2022), 2025 instructions.

---

## Persona

**Sarah Whitfield.** Age 51. Married filing jointly. Owns 100% of two related businesses:

1. **Whitfield Property Management LLC** — S-corp election (Form 2553 filed 2018). Manages residential rental properties for outside owners + her own. Has 5 W-2 employees.

2. **Whitfield Rentals (sole proprietorship, Schedule E)** — Owns 12 rental properties in the same metropolitan area. Reports income on Schedule E. Treated as a trade or business under the Rev. Proc. 2019-38 safe harbor (320 hours of rental services logged, contemporaneous records, separate books, statement attached). Rev. Proc. 2019-38 §3.01 allows a safe-harbor enterprise to be aggregated under Treas. Reg. §1.199A-4.

Spouse George works as a public school teacher with $65,000 W-2.

## 2025 Inputs

### Whitfield Property Management LLC (S-corp)

| Item | Amount |
|------|--------|
| K-1 box 1 ordinary income (after Sarah's W-2 deducted) | $30,000 |
| Sarah's reasonable comp from S-corp (W-2) | $80,000 |
| W-2 wages paid by S-corp (Sarah + 5 employees) | $250,000 |
| UBIA | $5,000 (office furniture, computers) |

### Whitfield Rentals (Schedule E)

| Item | Amount |
|------|--------|
| Net rental income (after depreciation, interest, taxes) | $250,000 |
| W-2 wages paid by Whitfield Rentals | $0 (managed by the PM company) |
| UBIA of qualified property | $1,500,000 (cost basis of buildings, excluding land) |

### Personal

| Item | Amount |
|------|--------|
| Sarah's W-2 from PM S-corp | $80,000 |
| George's W-2 (school teacher) | $65,000 |
| Taxable interest (bond portfolio) | $306,500 |
| Joint AGI | computed below |
| Standard deduction (MFJ, 2025) | $31,500 |

## Form 1040 build-up

| Line | Item | Amount |
|------|------|--------|
| 1a | Sarah's + George's W-2s | $145,000 |
| 2b | Taxable interest | $306,500 |
| 8 | Schedule E (rental + S-corp K-1) | $30,000 + $250,000 = $280,000 |
| **9** | **Total income** | **$731,500** |
| 10 | Adjustments | $0 |
| **11a** | **AGI** | **$731,500** |
| 12e | Standard deduction | $31,500 |
| 13b | Schedule 1-A deductions | $0 |
| | **Taxable income before QBI** | **$700,000** |

This puts her above the 2025 MFJ threshold ($394,600) AND above the phase-in top ($494,600) — full W-2/UBIA limit applies, no Part III, no Schedule A (and neither business is SSTB anyway).

---

## SSTB Classification

- Property management: NOT SSTB (real-estate-related management; not in any of the 11 listed categories)
- Rental real estate: NOT SSTB

Both are non-SSTB. Aggregation is potentially allowed.

---

## Aggregation eligibility (Schedule B)

| Test | Status |
|------|--------|
| 1. 50%+ common ownership | Yes — Sarah owns 100% of both |
| 2. Majority of year + last day | Yes |
| 3. Same tax year | Yes (both calendar) |
| 4. None is SSTB | Yes (both non-SSTB) |
| 5. Two of three sharing factors | Yes (see below) |

Factor analysis:
- **Same products/services**: Both relate to residential real estate. Yes.
- **Centralized elements**: Whitfield PM provides accounting and admin for Whitfield Rentals. Yes.
- **Operating coordination**: Whitfield Rentals relies entirely on Whitfield PM for management. Yes.

All three factors met → aggregation is allowed. Sarah elects on Schedule B. (The election is binding for future years.)

---

## Form 8995-A Part I

| (a) Name | (b) SSTB | (c) Aggregation | (d) TIN | (e) Patron |
|----------|----------|-----------------|---------|------------|
| Aggregation 1 | ☐ | ☑ | (blank for an aggregation) | ☐ |

## Form 8995-A Schedule B (Aggregation No. 1)

- Line 1: description of the aggregated property management and rental business and the factors met (same/customarily offered services, shared accounting and administration, operational reliance)
- Line 2: no change from the prior year (first year: explain that the aggregation is new)
- Line 3: Whitfield Property Management LLC — EIN, QBI $30,000, W-2 wages $250,000, UBIA $5,000; Whitfield Rentals — Sarah's SSN, QBI $250,000, W-2 wages $0, UBIA $1,500,000
- Line 4 totals: QBI $280,000, W-2 wages $250,000, UBIA $1,505,000 → Form 8995-A Part II column A

## Form 8995-A Part II — Aggregated computation

| Line | Item | Value |
|------|------|-------|
| 2 | QBI (combined) | $30,000 + $250,000 = **$280,000** |
| 3 | 20% × L2 | $56,000 |
| 4 | W-2 wages (combined) | $250,000 + $0 = **$250,000** |
| 5 | 50% × L4 | $125,000 |
| 6 | 25% × L4 | $62,500 |
| 7 | UBIA (combined) | $5,000 + $1,500,000 = **$1,505,000** |
| 8 | 2.5% × L7 | $37,625 |
| 9 | L6 + L8 | $100,125 |
| 10 | Greater of L5 or L9 | $125,000 |
| 11 | Smaller of L3 or L10 | **$56,000** |
| 12 | Phased-in reduction | $0 (above the phase-in range) |
| 13 | Greater of L11 or L12 | **$56,000** |
| 14 | Patron reduction | $0 |
| 15 | L13 − L14 | $56,000 |
| 16 | Total QBI component | $56,000 |

---

## Comparison: WITHOUT aggregation

If Sarah had reported them separately:

### Whitfield PM separately

| Line | Value |
|------|-------|
| 2 (QBI) | $30,000 |
| 3 (20%×) | $6,000 |
| 4 (W-2) | $250,000 |
| 5 (50% × W-2) | $125,000 |
| 9 (25% W-2 + 2.5% UBIA) | $62,500 + $125 = $62,625 |
| 10 (greater) | $125,000 |
| 11 (lesser of L3, L10) | $6,000 |

### Whitfield Rentals separately

| Line | Value |
|------|-------|
| 2 (QBI) | $250,000 |
| 3 (20%×) | $50,000 |
| 4 (W-2) | $0 |
| 5 (50% × W-2) | $0 |
| 9 (25% W-2 + 2.5% UBIA) | $0 + $37,500 = $37,500 |
| 10 (greater) | $37,500 |
| 11 (lesser of L3, L10) | $37,500 |

**Combined without aggregation: $6,000 + $37,500 = $43,500**

**With aggregation: $56,000**

**Aggregation benefit: $12,500 of additional deduction.** Taxable income after the deduction ($644,000) is in the 35% MFJ bracket for 2025 ($501,050–$751,600, Rev. Proc. 2024-40 Table 1), so about **$4,375 of additional tax savings**.

---

## Form 8995-A Part IV (with aggregation)

| Line | Item | Value |
|------|------|-------|
| 27 | Total QBI component | $56,000 |
| 28-31 | REIT/PTP component | $0 |
| 32 | L27 + L31 | $56,000 |
| 33 | Taxable income before QBI | $700,000 |
| 34 | Net capital gains | $0 |
| 35 | L33 − L34 | $700,000 |
| 36 | 20% × L35 | $140,000 |
| 37 | Smaller of L32 or L36 | **$56,000** |
| 38 | DPAD under §199A(g) | $0 |
| 39 | Total QBI deduction | **$56,000** |
| 40 | REIT/PTP loss carryforward | $0 |

---

## Form 1040 line 13a = $56,000

---

## Planning takeaways

1. **Aggregation is binding.** Sarah must keep reporting the aggregation in later years (Treas. Reg. §1.199A-4(c)(1)) and complete Schedule B each year. If she sells the management business but keeps the rentals, the aggregation breaks (and the rentals must be reported separately again).

2. **The W-2 wages of one entity supporting the QBI of another is the value here.** The PM company's W-2 wages weren't doing much in their own computation (only $30,000 QBI to support); after aggregation, they back the entire $280,000 QBI.

3. **UBIA is also pooled.** The 2.5% UBIA branch went from supporting $37,500 (rentals only) to $37,625 (combined) — virtually identical because the PM's UBIA is small. UBIA matters here mainly because it triggers the 25%-W-2-plus-2.5%-UBIA test as the alternative to 50%-W-2.

4. **Document the aggregation factors at election.** In an audit, the IRS will ask why these two businesses are aggregateable. Sarah should have a memo identifying the centralized accounting + operating coordination + same-services factors.

5. **If Sarah added an SSTB business** (say, a CPA firm she also owns), she could NOT include it in the aggregation. The CPA firm would file its own Part II on Form 8995-A; the aggregation election doesn't dissolve, but the CPA firm sits outside it.

---

## What if she's exactly at the threshold?

If Sarah's taxable income before QBI were $394,000 (just under the 2025 MFJ threshold of $394,600), neither business would face the W-2/UBIA limit. She'd file the simpler Form 8995 and take 20% × $280,000 = $56,000 directly (the income limitation, 20% × $394,000 = $78,800, doesn't bind) — same answer.

So the aggregation election is most valuable when:
- Taxable income is above the threshold AND
- One business has QBI not adequately supported by its own wages/UBIA AND
- A related non-SSTB business has spare wages/UBIA

Below the threshold, aggregation is irrelevant for the deduction (but might still be worth electing to lock it in for future years).
