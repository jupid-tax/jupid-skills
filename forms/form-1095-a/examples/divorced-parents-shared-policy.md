# Example: David and Sarah, Divorced Parents — Shared Policy Allocation

## Persona

- David (40) and Sarah (38), divorced 2023
- One child (age 10) — Sarah claims as dependent on her tax return per their divorce decree
- Marketplace policy is in David's name (he kept enrolling the family plan after the divorce); covers David, Sarah, and the daughter for 2025, with APTC paid
- Each files a separate return using Single filing status
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

The policy covered David's tax family (David) and Sarah's tax family (Sarah and the daughter), and David's 1095-A lists people outside his tax family → Form 8962 Line 9 = Yes, shared policy allocation REQUIRED (2025 Form 8962 instructions, Line 9). Because they divorced before 2025, Allocation Situation 4 applies.

### Part III — Coverage Information

Family-of-3 silver plan, identical all 12 months:

| Month | Col A | Col B | Col C |
|-------|-------|-------|-------|
| Jan–Dec | $1,400 | $1,300 | $750 |
| **Annual** | **$16,800** | **$15,600** | **$9,000** |

## Allocation Agreement

Before filing, David and Sarah agree (in writing):

- David takes 0.33 of premium, SLCSP, and APTC (his share of the policy)
- Sarah takes 0.67 (her share + daughter's share)

Allocation Situation 4 requires the same percentage for all three amounts in a month. Their split also equals the default they would have to use without an agreement: individuals David enrolled who are in Sarah's tax family (2) ÷ total enrolled (3) = 67% to Sarah (2025 Form 8962 instructions, Allocation Situation 4). Both agree to use these percentages on their respective Form 8962s.

## David's Form 8962

### Part I

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 1 (David only) |
| 2a | Modified AGI | $58,000 |
| 3 | Household income | $58,000 |
| 4 | FPL (HH of 1, 2024 FPL) | $15,060 |
| 5 | Income % FPL | 385% |
| 7 | Applicable Figure (2025 Table 2 at 385: 0.0600 + (85/100) × 0.0250) | 0.0813 (8.13%) |
| 8a | Annual contribution = 58,000 × 0.0813, rounded | $4,715 |
| 8b | Monthly contribution = 4,715 ÷ 12, rounded | $393 |

### Part IV — Allocation (Line 30)

| Field | Value |
|-------|-------|
| (a) Policy number | XYZ-12345 |
| (b) Other taxpayer SSN | Sarah's SSN |
| (c) Start month | 01 |
| (d) Stop month | 12 |
| (e) Premium % | 0.33 (his share) |
| (f) SLCSP % | 0.33 |
| (g) APTC % | 0.33 |

Line 34 = Yes.

### Part II — Monthly Calculation (Lines 12–23)

Completing Part IV forces Line 10 = No, so David uses the monthly lines. Apply 0.33 to each monthly 1095-A amount; every month is the same:

| Column | Calculation | Each month (Lines 12–23) | 12-month total |
|------|-------------|--------|--------|
| (a) | $1,400 × 0.33 | $462.00 | $5,544 |
| (b) | $1,300 × 0.33 | $429.00 | $5,148 |
| (c) | Line 8b | $393 | $4,716 |
| (d) | max(0, 429 − 393) | $36.00 | $432 |
| (e) | lesser of 462 or 36 | $36.00 | $432 |
| (f) | $750 × 0.33 | $247.50 | $2,970 |

| Line | Description | Amount |
|------|-------------|--------|
| 24 | Total PTC (sum of column (e)) | $432 |
| 25 | Total APTC (sum of column (f)) | $2,970 |
| 26 | Leave blank (Line 25 > Line 24) | — |
| 27 | Excess APTC = 2,970 − 432 | $2,538 |
| 28 | Repayment limit (Single, 300–400% FPL, 2025 Form 8962 instructions Table 5) | $1,625 |
| 29 | Excess APTC repayment | $1,625 |

**David owes back $1,625** (capped from $2,538 excess) → Schedule 2 Line 1a. On a 2026 return there would be no cap (P.L. 119-21 §71305).

## Sarah's Form 8962

### Part I

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 2 (Sarah + daughter) |
| 2a | Modified AGI | $34,000 |
| 3 | Household income | $34,000 |
| 4 | FPL (HH of 2, 2024 FPL) | $20,440 |
| 5 | Income % FPL | 166% |
| 7 | Applicable Figure (2025 Table 2 at 166: between 0.0000 at 150% and 0.0200 at 200%) | 0.0064 (0.64%) |
| 8a | Annual contribution = 34,000 × 0.0064, rounded | $218 |
| 8b | Monthly contribution = 218 ÷ 12, rounded | $18 |

### Part IV — Allocation (Line 30)

| Field | Value |
|-------|-------|
| (a) Policy number | XYZ-12345 |
| (b) Other taxpayer SSN | David's SSN |
| (c) Start month | 01 |
| (d) Stop month | 12 |
| (e) Premium % | 0.67 |
| (f) SLCSP % | 0.67 |
| (g) APTC % | 0.67 |

Line 34 = Yes.

### Part II — Monthly Calculation (Lines 12–23)

Line 10 = No (Part IV completed). Apply 0.67 to each monthly amount; every month is the same:

| Column | Calculation | Each month (Lines 12–23) | 12-month total |
|------|-------------|--------|--------|
| (a) | $1,400 × 0.67 | $938.00 | $11,256 |
| (b) | $1,300 × 0.67 | $871.00 | $10,452 |
| (c) | Line 8b | $18 | $216 |
| (d) | max(0, 871 − 18) | $853.00 | $10,236 |
| (e) | lesser of 938 or 853 | $853.00 | $10,236 |
| (f) | $750 × 0.67 | $502.50 | $6,030 |

| Line | Description | Amount |
|------|-------------|--------|
| 24 | Total PTC | $10,236 |
| 25 | Total APTC | $6,030 |
| 26 | Net PTC = 10,236 − 6,030 | $4,206 |

**Sarah is owed an additional $4,206 in Net PTC** → Schedule 3 Line 9 (refundable).

## Combined Outcome

- David repays $1,625 (capped excess APTC)
- Sarah receives $4,206 net PTC refund
- Net benefit to former couple: $2,581

## Validation

- [x] Allocation totals: 0.33 + 0.67 = 100% across all three columns, same percentage for each amount
- [x] Both filers used matching allocation percentages on Part IV
- [x] Sum of David's column (a) + Sarah's column (a) = $5,544 + $11,256 = $16,800 (matches 1095-A line 33, Column A)
- [x] Sum of David's column (f) + Sarah's column (f) = $2,970 + $6,030 = $9,000 (matches 1095-A line 33, Column C)

## Key Lesson

Without allocation, each former spouse claiming the full 1095-A would have double-counted the policy and invited IRS correspondence on both returns. With agreed allocation, both returns tie back to the original 1095-A.

The PTC is structured to be **portable across tax households** — a single Marketplace policy can support multiple tax returns, as long as the allocations are documented and consistent.

Best practice for any shared-policy situation: document the agreement in writing (signed by both parties), use one percentage for all three columns (premium / SLCSP / APTC) in each month, and have both parties confirm the percentages before either files. Mismatches between returns can lead to IRS notices.
