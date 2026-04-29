# Example: 73-Year-Old Verifying Box 11 RMD Indicator and Reconciling Box 12

A complete walkthrough of using Form 5498 to verify RMD compliance for a
new RMD-age filer with multiple IRAs. Demonstrates aggregation rules,
Box 5 / Box 11 / Box 12 interactions, and reconciliation against the
1099-R for the actual distribution.

## The filer

- **Name**: Robert Tanaka
- **Age**: 73 (turned 73 on August 22, 2025)
- **Filing status**: Married Filing Jointly
- **Tax year**: 2025 (Form 5498s received May 2026)
- **Spouse**: Same age, no impact on Robert's RMD (Robert's spouse has
  her own IRAs and is computing her own RMD)
- **Accounts**:
  - Traditional IRA at Fidelity: $310,000 12/31/2024 balance
  - Traditional IRA at Schwab: $185,000 12/31/2024 balance
  - SEP-IRA at Schwab: $42,000 12/31/2024 balance (from his pre-
    retirement self-employment)

## What Robert did during 2025

This is Robert's first RMD year. He turned 73 in August 2025, triggering
the RMD requirement starting with tax year 2025.

He has two options for the first-year RMD timing:
1. Take the 2025 RMD by **December 31, 2025** (most common)
2. Delay the 2025 RMD to **April 1, 2026** (the "required beginning
   date" for first-year RMDs only) — but then must also take the 2026
   RMD by 12/31/2026, doubling up

Robert chose Option 1 — take the 2025 RMD in 2025 to avoid the doubling
up.

## Computing the 2025 RMD

Aggregate traditional / SEP IRA value on 12/31/2024 (the prior-year
balance is what drives the current-year RMD):

```
Fidelity Traditional IRA:  $310,000
Schwab Traditional IRA:    $185,000
Schwab SEP-IRA:             $42,000
                           ─────────
Aggregate:                 $537,000
```

Distribution period factor (Uniform Lifetime Table, age 73): **26.5**
(per IRS Pub 590-B Appendix B, 2022 update; verify current Pub).

```
2025 RMD = $537,000 ÷ 26.5 = $20,264
```

Robert took $20,400 from his Fidelity Traditional IRA on November 15,
2025 (rounding up slightly for safety). He took nothing from Schwab.

## The Forms 5498 received in May 2026

### Fidelity Traditional IRA 5498

```
TRUSTEE'S name: Fidelity Investments
PARTICIPANT'S name: Robert Tanaka
PARTICIPANT'S SSN: XXX-XX-XXXX
Account number: ...8841

Box 1   IRA contributions:                  (blank)
Box 2   Rollover contributions:             (blank)
Box 3   Roth conversion amount:             (blank)
Box 5   FMV of account on 12/31/2025:       $295,400 (after $20,400
                                                      distribution
                                                      and ~$5,800 growth)
Box 7   IRA type:                           ✓ IRA
Box 11  RMD required for next year:         ✓
Box 12a RMD date:                           12/31/2026
Box 12b RMD amount:                         $11,592 (Fidelity's
                                                     calculation:
                                                     $295,400 ÷ 25.5
                                                     factor for age 74)
```

### Schwab Traditional IRA 5498

```
TRUSTEE'S name: Charles Schwab
PARTICIPANT'S name: Robert Tanaka
PARTICIPANT'S SSN: XXX-XX-XXXX
Account number: ...3392

Box 1   IRA contributions:                  (blank)
Box 5   FMV of account on 12/31/2025:       $193,800 (modest growth,
                                                      no distributions)
Box 7   IRA type:                           ✓ IRA
Box 11  RMD required for next year:         ✓
Box 12a RMD date:                           12/31/2026
Box 12b RMD amount:                         $7,600 (Schwab's
                                                    calculation:
                                                    $193,800 ÷ 25.5)
```

### Schwab SEP-IRA 5498

```
TRUSTEE'S name: Charles Schwab
PARTICIPANT'S name: Robert Tanaka
PARTICIPANT'S SSN: XXX-XX-XXXX
Account number: ...7158

Box 1   IRA contributions:                  (blank)
Box 5   FMV of account on 12/31/2025:       $44,100 (modest growth)
Box 7   IRA type:                           ✓ SEP
Box 8   SEP contributions:                  (blank — Robert is
                                              retired, no SEP
                                              contributions)
Box 11  RMD required for next year:         ✓
Box 12a RMD date:                           12/31/2026
Box 12b RMD amount:                         $1,729 (Schwab's
                                                    calculation:
                                                    $44,100 ÷ 25.5)
```

## The corresponding Form 1099-R received

Issued by Fidelity in January 2026 for the November 2025 distribution:

```
PAYER: Fidelity Investments
RECIPIENT: Robert Tanaka

Box 1   Gross distribution:                 $20,400
Box 2a  Taxable amount:                     $20,400
Box 4   Federal income tax withheld:        $4,080 (20% withholding;
                                                    Robert can elect
                                                    or decline)
Box 7   Distribution code:                  7 (normal distribution
                                                — Robert is 73)
IRA/SEP/SIMPLE checkbox:                    ✓
```

## What Robert's 2025 tax return showed

**Form 1040**:
- Line 4a (gross IRA distributions): $20,400
- Line 4b (taxable amount): $20,400
- Line 25b (federal income tax withheld from 1099): $4,080

No Form 8606 (no nondeductible basis to track).
No Form 5329 (RMD was satisfied; no penalty).

## Reconciliation walkthrough

### Step 1 — Identify populated boxes across all three 5498s

- Fidelity: Box 5, Box 7 (IRA), Box 11 ✓, Box 12a, Box 12b
- Schwab Trad: Box 5, Box 7 (IRA), Box 11 ✓, Box 12a, Box 12b
- Schwab SEP: Box 5, Box 7 (SEP), Box 11 ✓, Box 12a, Box 12b

No contribution boxes (1, 8, 9, 10) populated — Robert is retired.

### Step 2 — Verify Box 11 is correctly checked

Robert is 73. RMD applies to all his traditional / SEP IRAs. All three
Box 11s should be ✓. ✓ Correct on all three.

### Step 3 — Compute aggregate 2025 RMD using prior-year balances

Wait — the 5498 reflects 2025 activity, but the 2025 RMD is based on the
**12/31/2024** balances (already happened). For verification of the 2025
RMD that was already taken, we need:

- Fidelity 12/31/2024 balance: $310,000 (from prior year's 5498 Box 5)
- Schwab Trad 12/31/2024 balance: $185,000 (from prior year's 5498 Box 5)
- Schwab SEP 12/31/2024 balance: $42,000 (from prior year's 5498 Box 5)
- Aggregate: $537,000
- Factor (age 73): 26.5
- 2025 RMD: $537,000 ÷ 26.5 = $20,264

Robert took $20,400. ✓ Within $1 of computed RMD; satisfied. (Slight
overage gives a small buffer against custodian-recordkeeping
differences.)

### Step 4 — Reconcile actual distribution against 1099-R and 1040

| Source | Amount |
|--------|--------|
| Fidelity 1099-R Box 1 | $20,400 |
| Form 1040 Line 4a | $20,400 |
| Form 1040 Line 4b | $20,400 |
| 2025 RMD requirement | $20,264 (aggregate) |

✓ Match. RMD satisfied. Slight surplus of $136 (Robert's safety margin)
is fine.

### Step 5 — Verify the 2026 RMD computation using 2025 5498 Box 5

For 2026 RMD planning:
- Aggregate Box 5 (12/31/2025): $295,400 + $193,800 + $44,100 = $533,300
- Factor (age 74, Uniform Lifetime Table): 25.5
- 2026 RMD: $533,300 ÷ 25.5 = $20,914

Sum of all three Box 12b values: $11,592 + $7,600 + $1,729 = $20,921

These differ slightly from the agent's $20,914 calculation. The
custodian's amounts in Box 12b are computed using each custodian's
slightly different rounding. Total is close enough; Robert can take
$20,914 (his agent-computed aggregate) or $20,921 (custodian sum) and
either is fine.

### Step 6 — Aggregation rule check

For 2026, Robert's aggregate RMD is ~$20,914 from his three IRAs. Per
IRA aggregation rules, he can take this from any one or any
combination of the three accounts. Rule:

- Traditional IRAs aggregate with each other AND with SEP/SIMPLE for RMD
  purposes (all "IRA-type" accounts aggregate)
- 401(k) and other qualified plans do NOT aggregate with IRAs (Robert
  has none of these, so no issue)

Robert can take all $20,914 from Fidelity (most convenient), or split.

### Step 7 — Confirm no missed RMD

For 2025, Robert took $20,400 against a $20,264 requirement. ✓ No
shortfall. No Form 5329 Part IX needed.

## The reconciliation report

```markdown
# Form 5498 Reconciliation — Tax Year 2025

## Custodians (multiple)
1. Fidelity Investments — Traditional IRA #...8841
2. Charles Schwab — Traditional IRA #...3392
3. Charles Schwab — SEP-IRA #...7158

## Account holder
Name: Robert Tanaka
SSN: XXX-XX-XXXX
Age: 73 (turned 73 on 08/22/2025; first RMD year)

## Populated boxes summary (per account)

### Fidelity Traditional
| Box | Label | Amount |
|-----|-------|--------|
| 5 | FMV 12/31/2025 | $295,400 |
| 7 | IRA type | IRA |
| 11 | RMD required next year | ✓ |
| 12a | RMD date | 12/31/2026 |
| 12b | RMD amount | $11,592 |

### Schwab Traditional
| Box | Label | Amount |
|-----|-------|--------|
| 5 | FMV 12/31/2025 | $193,800 |
| 7 | IRA type | IRA |
| 11 | RMD required next year | ✓ |
| 12a | RMD date | 12/31/2026 |
| 12b | RMD amount | $7,600 |

### Schwab SEP
| Box | Label | Amount |
|-----|-------|--------|
| 5 | FMV 12/31/2025 | $44,100 |
| 7 | IRA type | SEP |
| 11 | RMD required next year | ✓ |
| 12a | RMD date | 12/31/2026 |
| 12b | RMD amount | $1,729 |

## 2025 RMD verification

| Item | Amount |
|------|--------|
| Aggregate 12/31/2024 balance (from prior 5498s) | $537,000 |
| Distribution period factor (age 73, Uniform Lifetime Table) | 26.5 |
| Required 2025 RMD | $20,264 |
| Distribution actually taken (Fidelity, 11/15/2025) | $20,400 |
| Status | ✓ Satisfied (with $136 buffer) |

## Reconciliation status

| Item | Status |
|------|--------|
| 1099-R Box 1 ($20,400) ↔ Form 1040 Line 4a ($20,400) | ✓ Match |
| 1099-R Box 2a ($20,400) ↔ Form 1040 Line 4b ($20,400) | ✓ Match |
| 2025 RMD requirement ($20,264) ↔ Distribution ($20,400) | ✓ Satisfied |
| Box 11 ✓ on all three 5498s | ✓ Correct (Robert is 73, IRA-type accounts) |

## 2026 RMD planning

| Item | Amount |
|------|--------|
| Aggregate 12/31/2025 Box 5 (sum across all 5498s) | $533,300 |
| Distribution period factor (age 74) | 25.5 |
| Computed 2026 RMD (aggregate) | $20,914 |
| Sum of custodian Box 12b values | $20,921 |
| Difference (rounding) | $7 (immaterial) |

Robert should plan to take ~$20,914 in 2026 from any one or combination
of the three accounts before 12/31/2026.

## Issues to resolve

None.

## Required actions
- [x] File all three 2025 Forms 5498 in tax records
- [x] Confirm 2025 RMD satisfied (✓)
- [ ] Set up Fidelity / Schwab automated RMD distribution for 2026
      (helps avoid missed-RMD risk)
- [ ] In 2026, monitor custodian-computed Box 12b values; if Robert
      changes accounts, recompute aggregate
- [ ] Continue annual reconciliation for as long as Robert has IRAs

## Validation summary
- Math: all checks passed
  - Aggregate 2025 RMD: $537,000 ÷ 26.5 = $20,264 ✓
  - Distribution: $20,400 ≥ $20,264 ✓
  - 2026 projection: $533,300 ÷ 25.5 = $20,914 (matches sum of custodian
    Box 12b within rounding)
- Sanity:
  - Robert's first RMD year — he correctly chose to take it in 2025 (vs.
    delaying to April 1, 2026 which would have doubled up with the 2026
    RMD)
  - Box 11 correctly checked on all three accounts (all are IRA-type
    requiring RMDs)
  - No SEP contributions in 2025 (Robert is retired) — Box 8 correctly
    blank on the SEP 5498
  - Distribution code 7 on 1099-R (normal distribution, not early)
- Next steps:
  - $20,400 RMD reported on 2025 Form 1040 Line 4a/4b ✓
  - Federal withholding $4,080 credited on Form 1040 Line 25b ✓
  - Robert continues annual RMDs; consider automating

## Sources cited in this reconciliation
- IRS Form 5498, Rev. 2025
- IRS Instructions for Form 5498, Rev. 2025
- IRC §401(a)(9) — RMD rules
- IRC §408(a)(6) — IRA RMD application
- SECURE 2.0 Act §107 — RMD age 73 (applies to those reaching 73 in
  2023-2032)
- IRS Pub 590-B — Distributions from IRAs (Uniform Lifetime Table,
  Appendix B)
- Robert's 2024 Forms 5498 (for 12/31/2024 balances used in 2025 RMD)
- 2025 Form 1099-R from Fidelity
- 2025 Form 1040
```

## Why each non-obvious choice

**Why does the aggregation rule allow Robert to take the entire RMD
from Fidelity?** Because traditional IRAs (and SEP-IRAs and SIMPLE-IRAs)
aggregate for RMD purposes under IRC §408(a)(6) and Treasury Reg.
§1.408-8. The user can take the total RMD from any one or any
combination of the aggregating accounts.

If Robert had a 401(k) or 403(b), that would NOT aggregate — the RMD
from a 401(k) must come from the 401(k) itself. Each plan stands alone
except for IRA-type accounts.

**Why did Robert take the 2025 RMD in November rather than waiting until
April 1, 2026?** Because waiting until April 1 would mean two RMDs in
2026 (the delayed 2025 RMD plus the regular 2026 RMD), nearly doubling
2026 taxable income. Taking the 2025 RMD in 2025 levels the income
between the years.

**Why does the distribution period factor change from 26.5 (age 73) to
25.5 (age 74)?** Each year the user gets one year older, the factor
decreases (you're projected to live fewer years), so the RMD is a
larger fraction of the account. The IRS Uniform Lifetime Table
publishes the factor for each age.

**Why is custodian-computed Box 12b ($20,921 sum) close to but not
exactly matching the agent's computation ($20,914)?** Custodians
compute using their internal records; the agent computes from Box 5.
These should match, but rounding (typically to the nearest cent or
dollar) and intra-day timing of the year-end value can create small
differences. For amounts under ~$50, this is normal and not worth
investigating.

**Why no Form 8606?** Robert has no nondeductible basis. All his IRA
contributions over the years (when he was working) were either
deductible traditional contributions or SEP-IRA contributions —
neither generates basis. Form 8606 is only needed when there's
nondeductible basis.

**What if Robert had missed his 2025 RMD?** He'd be subject to Form 5329
Part IX. The penalty would be 25% of the shortfall (or 10% if corrected
within 2 years per SECURE 2.0 §302). A waiver request under §4974(d)
would likely be approved given Robert is a first-year RMD filer who
might reasonably have been confused about the requirement. See the
form-5329 skill `examples/missed-rmd-waiver.md` for that walkthrough.

**What records should Robert retain?**

1. All three 2025 Forms 5498
2. Prior-year (2024) Forms 5498 — needed to document 12/31/2024
   balances used in the 2025 RMD computation
3. The 2025 1099-R from Fidelity
4. The 2025 Form 1040
5. This reconciliation report
6. RMD calculation worksheet showing aggregate balance ÷ factor
7. Custodian statements showing the November 2025 distribution
8. Going forward: every year's 5498s, 1099-Rs, 1040, and a fresh
   reconciliation
