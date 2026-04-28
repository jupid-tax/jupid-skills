# Example: David and Sarah, Divorced Parents — Shared Policy Allocation

## Persona

- David (40) and Sarah (38), divorced 2023
- One child (age 10) — Sarah claims as dependent on her tax return per their divorce decree
- Marketplace policy is in David's name (he had the better employer offer at one point and kept the plan); covers David, Sarah, and the daughter for 2025
- Both file separately as Single filers
- David's AGI: $58,000
- Sarah's AGI: $34,000
- Resident state: California (uses California Marketplace + Form 3849 state-level reconciliation; for this example we focus on federal Form 8962)

## Form 1095-A Received

David receives the 1095-A in his name. Sarah requests a copy from David (she needs it to file her own Form 8962).

### Part I — Recipient Information
- Recipient: David
- Policy issuer: Blue Shield of California

### Part II — Covered Individuals
- David
- Sarah (ex-spouse, NOT on David's return)
- Daughter (NOT on David's return — claimed by Sarah)

Anyone other than David is NOT on David's tax return → shared policy allocation REQUIRED.

### Part III — Coverage Information

Family-of-3 silver plan, identical all 12 months:

| Month | Col A | Col B | Col C |
|-------|-------|-------|-------|
| Jan–Dec | $1,400 | $1,300 | $750 |
| **Annual** | **$16,800** | **$15,600** | **$9,000** |

## Allocation Agreement

Before filing, David and Sarah agree (in writing):

- David takes 33.3% of premium and SLCSP (covers his share of the policy)
- Sarah takes 66.7% (covers her share + daughter's share)
- APTC allocation: 33.3% David, 66.7% Sarah

Both agree to use these percentages on their respective Form 8962s.

## David's Form 8962

### Part I

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 1 (David only) |
| 2a | Modified AGI | $58,000 |
| 3 | Household income | $58,000 |
| 4 | FPL (HH of 1, 2024 FPL) | $15,060 |
| 5 | Income % FPL | 385% |
| 7 | Applicable Figure (interpolating 300%→400% under ARPA/IRA: 0.0600 + (85/100) × 0.0250) | 0.0813 (8.13%) |
| 8a | Annual contribution | $4,715 |
| 8b | Monthly contribution | $393 |

### Part IV — Allocation (Line 30)

| Field | Value |
|-------|-------|
| (a) Policy number | XYZ-12345 |
| (b) Other taxpayer SSN | Sarah's SSN |
| (c) Start month | 01 |
| (d) Stop month | 12 |
| (e) Premium % | 33.3% (his share) |
| (f) SLCSP % | 33.3% |
| (g) APTC % | 33.3% |

### Part II — Annual Calculation (Line 11)

Apply 33.3% to each annual amount before entering on Line 11:

| Line | Calculation | Amount |
|------|-------------|--------|
| 11(a) | $16,800 × 33.3% | $5,594 |
| 11(b) | $15,600 × 33.3% | $5,195 |
| 11(c) | Annual contribution | $4,715 |
| 11(d) | max(0, 5,195 − 4,715) | $480 |
| 11(e) | lesser of 5,594 or 480 | $480 |
| 11(f) | $9,000 × 33.3% | $2,997 |
| 24 | Total PTC | $480 |
| 25 | Total APTC | $2,997 |
| 27 | Excess APTC = 2,997 − 480 | $2,517 |
| 28 | Repayment limit (Single, 300–400% FPL, 2025 Pub 974 Table 5) | $1,625 |
| 29 | Excess APTC repayment | $1,625 |

**David owes back $1,625** (capped from $2,517 excess) → Schedule 2 Line 1a.

## Sarah's Form 8962

### Part I

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 2 (Sarah + daughter) |
| 2a | Modified AGI | $34,000 |
| 3 | Household income | $34,000 |
| 4 | FPL (HH of 2, 2024 FPL) | $20,440 |
| 5 | Income % FPL | 166% |
| 7 | Applicable Figure (under 200%, ARPA/IRA: between 0.0000 at 150% and 0.0200 at 200%; interpolate: 0.0064) | 0.0064 (0.64%) |
| 8a | Annual contribution | $218 |
| 8b | Monthly contribution | $18 |

### Part IV — Allocation (Line 30)

| Field | Value |
|-------|-------|
| (a) Policy number | XYZ-12345 |
| (b) Other taxpayer SSN | David's SSN |
| (c) Start month | 01 |
| (d) Stop month | 12 |
| (e) Premium % | 66.7% |
| (f) SLCSP % | 66.7% |
| (g) APTC % | 66.7% |

### Part II — Annual Calculation (Line 11)

Apply 66.7% to each annual amount:

| Line | Calculation | Amount |
|------|-------------|--------|
| 11(a) | $16,800 × 66.7% | $11,206 |
| 11(b) | $15,600 × 66.7% | $10,405 |
| 11(c) | Annual contribution | $218 |
| 11(d) | max(0, 10,405 − 218) | $10,187 |
| 11(e) | lesser of 11,206 or 10,187 | $10,187 |
| 11(f) | $9,000 × 66.7% | $6,003 |
| 24 | Total PTC | $10,187 |
| 25 | Total APTC | $6,003 |
| 26 | Net PTC = 10,187 − 6,003 | $4,184 |

**Sarah is owed an additional $4,184 in Net PTC** → Schedule 3 Line 9 (refundable).

## Combined Outcome

- David repays $1,625 (capped excess APTC)
- Sarah receives $4,184 net PTC refund
- Net benefit to former couple: $2,559

## Validation

- [x] Allocation totals: 33.3% + 66.7% = 100% across all three columns
- [x] Both filers used matching allocation percentages on Part IV
- [x] Sum of David's 11(a) + Sarah's 11(a) = $16,800 (matches 1095-A Column A annual)
- [x] Sum of David's 11(f) + Sarah's 11(f) = $9,000 (matches 1095-A Column C annual)

## Key Lesson

Without allocation, each former spouse claiming the full 1095-A would have looked like double-counting and triggered IRS rejection of both returns. With agreed allocation, both returns flow cleanly and the IRS reconciles the totals back to the original 1095-A.

The PTC is structured to be **portable across tax households** — a single Marketplace policy can support multiple tax returns, as long as the allocations are documented and consistent.

Best practice for any shared-policy situation: document the agreement in writing (signed by both parties), specify the percentages for each column (premium / SLCSP / APTC), and have both parties confirm the percentages before either files. Mismatches between returns generate IRS notices that take months to resolve.
