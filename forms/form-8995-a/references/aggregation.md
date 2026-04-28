# Schedule B — Aggregation of Trades or Businesses

Aggregation lets the taxpayer combine multiple trades or businesses for purposes of the W-2 wage / UBIA limit. It's a strategic election, not automatic. This reference covers the eligibility rules, when it makes sense, and the binding-election consequences.

---

## When aggregation helps

Aggregation helps when one business has high QBI but low W-2 wages (would be limited above the threshold) AND another business has low QBI but high W-2 wages (or significant UBIA). Combining lets the wages of the second support the deduction of the first.

**Example:**
- Business A: QBI $400,000, W-2 wages $50,000 → limited to max(50% × 50K, 25% × 50K + 2.5% × UBIA)
- Business B: QBI $50,000, W-2 wages $200,000

Without aggregation, Business A's deduction is constrained by its $50K W-2.
With aggregation, the combined entity has $450,000 QBI and $250,000 W-2 → much higher limit.

---

## Eligibility (Treas. Reg. §1.199A-4(b))

**ALL** five tests must be met:

### Test 1: Common ownership

The same person, or group of persons, must own (directly or by attribution under §267(b) or §707(b)) at least **50%** of each business in the aggregation. Family attribution: spouses, children, grandchildren, parents (§267(c)(4)).

### Test 2: Ownership for the majority of the year

The 50% common ownership must exist for the majority of the tax year, including the last day. Mid-year acquisitions may disqualify aggregation for that year.

### Test 3: Same tax year

All businesses being aggregated must use the same tax year. Most are calendar-year; if any is fiscal-year, aggregation is more restricted.

### Test 4: None is an SSTB

**Critical.** SSTBs cannot be in an aggregation. If any of the businesses is SSTB, the entire aggregation election is invalid.

### Test 5: Two of three sharing factors

The businesses must share at least TWO of the following three:

(a) **Common products or services** — Provide products, property, or services that are the same or customarily offered together (e.g., a restaurant chain; a property management business + the rental properties it manages)

(b) **Centralized business elements** — Share facilities or significant centralized business elements (e.g., personnel, accounting, legal, manufacturing, purchasing, HR, IT)

(c) **Operating coordination** — Operate in coordination with or reliance upon other businesses in the aggregated group (e.g., supply chain integration, exclusive supplier relationships)

---

## How to elect

The election is made on **Schedule B of Form 8995-A** by listing each business and the satisfied factors. There is no separate election form.

The election must be reported on the original return (not amended); failure to report on the original return = no election for that year.

---

## Once elected, binding for future years

Per Treas. Reg. §1.199A-4(c)(1), once you aggregate, you MUST continue aggregating those businesses every year until they no longer qualify (e.g., one is sold, ownership changes, an SSTB is added).

The taxpayer can ADD new businesses to the aggregation in future years, but cannot DISAGGREGATE except for material changes in facts.

---

## Worked Example — Property Manager + Rental Real Estate

**Inputs:**
- Business 1: Property management company (S-corp)
  - QBI: $30,000
  - W-2 wages: $250,000 (employees managing properties)
  - UBIA: $5,000

- Business 2: Rental real estate enterprise (sole prop, qualifying as §162 t/b)
  - QBI: $250,000
  - W-2 wages: $0 (no employees; managed by Business 1)
  - UBIA: $1,500,000 (cost basis of rental buildings, excluding land)

**Owner:** Same individual owns 100% of both. Filing MFJ. Taxable income before QBI: $700,000 (above MFJ threshold $483,900, well above phase-in top — full W-2/UBIA limit applies).

### Without aggregation:

**Business 1 (S-corp PM):**
- 20% × $30,000 = $6,000
- W-2/UBIA limit: max(50% × $250,000, 25% × $250,000 + 2.5% × $5,000) = max($125,000, $62,625) = $125,000
- Adjusted QBI: min($6,000, $125,000) = $6,000

**Business 2 (Rental):**
- 20% × $250,000 = $50,000
- W-2/UBIA limit: max(50% × $0, 25% × $0 + 2.5% × $1,500,000) = max($0, $37,500) = $37,500
- Adjusted QBI: min($50,000, $37,500) = $37,500

**Combined: $6,000 + $37,500 = $43,500**

### With aggregation (Schedule B):

Combined QBI: $30,000 + $250,000 = $280,000
Combined W-2: $250,000 + $0 = $250,000
Combined UBIA: $5,000 + $1,500,000 = $1,505,000

- 20% × $280,000 = $56,000
- W-2/UBIA limit: max(50% × $250,000, 25% × $250,000 + 2.5% × $1,505,000) = max($125,000, $62,500 + $37,625) = max($125,000, $100,125) = $125,000
- Adjusted QBI: min($56,000, $125,000) = **$56,000**

Aggregation gives **$56,000 vs $43,500 = $12,500 more deduction.**

### Eligibility check:

- Test 1 (50%+ common ownership): Yes, 100%
- Test 2 (Majority of year): Yes
- Test 3 (Same tax year): Yes (both calendar year)
- Test 4 (None is SSTB): Yes (property management and rental real estate are not SSTB)
- Test 5 (Two of three factors):
  - Common services: Yes (property management services for the rentals)
  - Centralized elements: Yes (Business 1 provides accounting/HR for Business 2)
  - Operating coordination: Yes (Business 2 relies on Business 1 for management)

All three factors met → aggregation is allowed.

---

## When NOT to aggregate

- One of the businesses is SSTB → cannot aggregate
- The W-2/UBIA limit doesn't bind for any business (under threshold or wages already plenty) → no benefit
- The user might exit one business soon → aggregation locks them in
- The businesses don't actually share enough factors → IRS could disallow aggregation in audit

---

## Common mistakes

1. **Aggregating SSTBs**: A consulting firm + a software firm cannot aggregate because consulting is SSTB. Common confusion when a single owner has mixed-character businesses.

2. **Forgetting to report on Schedule B**: If you don't list it on the form, you didn't elect it. There's no implicit election.

3. **Disaggregating in a later year**: Not allowed except for material changes (sale, ownership change). The election is sticky.

4. **Aggregating businesses with different fiscal years**: Generally requires special procedures; consult the regs and the instructions.

5. **Insufficient documentation of factors**: In audit, the IRS will ask for evidence of the two-of-three factors. Document at the time of election (memo, org chart, accounting structure).
