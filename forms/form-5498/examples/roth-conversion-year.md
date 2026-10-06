# Example: Roth Conversion Year — Reconciling Box 3 with Form 8606

A complete walkthrough of reconciling Form 5498 Box 3 (Roth conversion
amount) with the corresponding Form 1099-R and Form 8606 Part II.
Demonstrates the pro-rata rule applied to a partial conversion when the
user has nondeductible basis.

## The filer

- **Name**: Wei Lin
- **Age**: 51
- **Filing status**: Married Filing Jointly
- **Tax year**: 2025 (Form 5498s furnished by June 1, 2026)
- **Accounts**:
  - Traditional IRA at Vanguard (Account A): $80,000 balance 12/31/2024
  - Traditional IRA at Vanguard (Account B): $40,000 balance 12/31/2024
  - Roth IRA at Vanguard: $35,000 balance 12/31/2024 (existing)
- **Basis history**: Wei has $12,000 of nondeductible basis tracked on
  prior Form 8606s (from 2017-2020 contributions when she was over the
  Roth phaseout and made nondeductible traditional IRA contributions
  instead)

## What Wei did during 2025

In November 2025, Wei did a partial Roth conversion: she moved $30,000
from Traditional IRA Account A to her Roth IRA. She wanted to
"strategically use up" some basis and take advantage of a lower-income
year (her spouse was on sabbatical so MAGI was lower than usual,
reducing the conversion's marginal tax cost).

She made no other IRA contributions, no rollovers, no recharacterizations.

## The Forms 5498 received

### From Vanguard for the Roth IRA (May 2026)

```
TRUSTEE'S name: Vanguard Group, Inc.
PARTICIPANT'S name: Wei Lin
PARTICIPANT'S SSN: XXX-XX-XXXX

Box 1  IRA contributions:                  (blank)
Box 2  Rollover contributions:             (blank)
Box 3  Roth IRA conversion amount:         $30,000
Box 4  Recharacterized contributions:      (blank)
Box 5  FMV of account on 12/31/2025:       $69,200
Box 7  IRA type:                           ✓ Roth IRA
Box 10 Roth IRA contributions:             (blank)
Box 11 RMD required for next year:         ☐ (correctly unchecked
                                              — Roth IRAs have no
                                              lifetime RMD for original
                                              owner)
```

### From Vanguard for Traditional IRA Account A (May 2026)

```
Box 1  IRA contributions:                  (blank)
Box 5  FMV of account on 12/31/2025:       $52,800 (was $80K, reduced
                                                    by $30K conversion
                                                    + ~$3K growth)
Box 7  IRA type:                           ✓ IRA (Traditional)
Box 11 RMD required for next year:         ☐ (Wei is 51, not at RMD age)
```

### From Vanguard for Traditional IRA Account B (May 2026)

```
Box 1  IRA contributions:                  (blank)
Box 5  FMV of account on 12/31/2025:       $42,400 (modest growth, no
                                                    activity)
Box 7  IRA type:                           ✓ IRA (Traditional)
Box 11 RMD required for next year:         ☐
```

## The corresponding Form 1099-R received

### From Vanguard for Traditional IRA Account A (January 2026)

```
PAYER: Vanguard Group, Inc.
RECIPIENT: Wei Lin

Box 1  Gross distribution:                 $30,000
Box 2a Taxable amount:                     $30,000 (or blank — let
                                                    8606 compute)
Box 7  Distribution code:                  2 (early distribution,
                                              exception applies — the
                                              1099-R instructions list
                                              "A Roth IRA conversion"
                                              for a participant under 59½)
Box 7 IRA/SEP/SIMPLE checkbox:             ✓
```

## What Wei's 2025 tax return showed

Wei's CPA prepared:

**Form 1040**:
- Line 4a (gross IRA distributions): $30,000
- Line 4b (taxable amount): $27,120 (computed via Form 8606 with
  pro-rata basis applied)

**Form 8606 Part II — Roth Conversions**:
```
Line 16: Net amount converted to Roth IRAs in 2025:    $30,000
Line 17: Basis in amount converted (Part I Line 11):    $2,880
Line 18: Taxable amount (Line 16 − Line 17):          $27,120
```

**Form 8606 Part I — Nondeductible Contributions**:
- No new nondeductible contribution this year
- Updated basis tracking: $12,000 prior basis − $2,880 used in
  conversion = $9,120 remaining basis carrying forward to 2026

### How the $2,880 basis was computed (pro-rata rule)

Per IRC §408(d)(1)–(2) (all traditional IRAs treated as one contract,
valued at year end) and the 2025 Form 8606, Part I:

```
Line 1: 2025 nondeductible contributions:            $0
Line 2: Total basis in traditional IRAs:         $12,000
Line 3 / Line 5 (no 2026 contributions for 2025): $12,000

Line 6: Value of all traditional IRAs on 12/31/2025:
  $52,800 (Account A) + $42,400 (Account B) =      $95,200

Line 7: Distributions other than conversions:          $0

Line 8: Net amount converted to Roth in 2025:     $30,000

Line 9: Line 6 + Line 7 + Line 8:                $125,200

Line 10: Line 5 ÷ Line 9 = 12,000 ÷ 125,200 = 0.0958 → 0.096
  (the form asks for at least 3 decimal places)

Line 11: nontaxable part of the conversion:
  $30,000 × 0.096 = $2,880 (also entered on Line 17)

Line 14: remaining basis:
  $12,000 − $2,880 = $9,120 carrying to 2026
```

(Rounding Line 10 to 4 places instead, 0.0958, gives $2,874 nontaxable and
$27,126 taxable; either is consistent with the form's instruction.)

## Reconciliation walkthrough

### Step 1 — Identify populated boxes on each 5498

- Roth 5498: Box 3 ($30,000), Box 5 ($69,200), Box 7 (Roth IRA)
- Traditional A 5498: Box 5 ($52,800), Box 7 (IRA)
- Traditional B 5498: Box 5 ($42,400), Box 7 (IRA)

No Box 1 / 10 / 8 / 9 contributions this year (Wei contributed nothing
new in 2025; just did the conversion).

### Step 2 — Reconcile Box 3 against Form 1040 Line 4a

| Source | Amount |
|--------|--------|
| Roth 5498 Box 3 | $30,000 |
| 1099-R Box 1 (gross) | $30,000 |
| Form 1040 Line 4a | $30,000 |

✓ Match.

### Step 3 — Reconcile taxable portion on Form 1040 Line 4b

| Source | Amount |
|--------|--------|
| Form 1040 Line 4b | $27,120 |
| Form 8606 Part II Line 18 | $27,120 |
| 1099-R Box 2a | $30,000 (gross — but the actual taxable portion is
                            computed by 8606, not the 1099-R) |

The 1099-R Box 2a doesn't necessarily equal Line 4b. Custodians often
report the gross as taxable in Box 2a because they don't track the
user's basis. The user's Form 8606 is the authoritative computation.

✓ Match between 8606 and 1040.

### Step 4 — Verify aggregate IRA values

For pro-rata calculation:
- Sum of Box 5 across Traditional A + B 5498s = $52,800 + $42,400 =
  $95,200 (this is the year-end aggregate value, Form 8606 Line 6)
- Plus the $30,000 conversion during the year (Line 8) = $125,200
  total for allocation (Line 9)

Form 8606 Line 6 should match $95,200 and Line 9 $125,200.

### Step 5 — Confirm basis carryforward

Wei's prior basis was $12,000. After applying $2,880 to this conversion,
$9,120 of basis remains. Form 8606 Line 14 should show $9,120.

This $9,120 carries to 2026's Form 8606. If Wei does another conversion
in 2026, it'll be applied pro-rata against the 2026 aggregate.

### Step 6 — Verify Box 11 (RMD) is unchecked on all three 5498s

Wei is 51, well below RMD age (75 for someone born in 1974, IRC
§401(a)(9)(C)(v)). All Box 11s should be unchecked. The
Roth 5498's Box 11 should *always* be unchecked for original Roth
owners regardless of age.

## The reconciliation report

```markdown
# Form 5498 Reconciliation — Tax Year 2025

## Custodian
Name: Vanguard Group, Inc.
TIN: 23-XXXXXXX
Multiple accounts:
- Roth IRA #...3914
- Traditional IRA Account A #...7728
- Traditional IRA Account B #...4521

## Account holder
Name: Wei Lin
SSN: XXX-XX-XXXX

## Populated boxes summary

### Roth IRA 5498
| Box | Label | Amount | Reconciled to |
|-----|-------|--------|----------------|
| 3 | Roth conversion amount | $30,000 | 1099-R, Form 1040 Line 4a, Form 8606 Part II Line 16 |
| 5 | FMV 12/31/2025 | $69,200 | (informational; next-year basis tracking) |
| 7 | IRA type | Roth IRA | — |
| 11 | RMD required | ☐ unchecked | ✓ correct (Roth IRA, original owner) |

### Traditional A 5498
| Box | Label | Amount | Reconciled to |
|-----|-------|--------|----------------|
| 5 | FMV 12/31/2025 | $52,800 | Form 8606 Line 6 (aggregate with B) |
| 7 | IRA type | IRA | — |

### Traditional B 5498
| Box | Label | Amount | Reconciled to |
|-----|-------|--------|----------------|
| 5 | FMV 12/31/2025 | $42,400 | Form 8606 Line 6 (aggregate with A) |
| 7 | IRA type | IRA | — |

## Reconciliation status

| Item | Status |
|------|--------|
| Box 3 ($30,000) ↔ 1099-R Box 1 ($30,000) | ✓ Match |
| Box 3 ($30,000) ↔ Form 1040 Line 4a ($30,000) | ✓ Match |
| Form 1040 Line 4b ($27,120) ↔ Form 8606 Part II Line 18 ($27,120) | ✓ Match |
| Aggregate Trad IRA Box 5 ($95,200) ↔ Form 8606 Line 6 | ✓ Match |
| Box 11 unchecked on Roth | ✓ Correct |
| Box 11 unchecked on both Trads | ✓ Correct (Wei is 51) |

## Issues to resolve

None.

## Required actions
- [x] File all three 5498s in 2025 tax records
- [x] Confirm Form 8606 was filed with the 2025 return (Part II
      computed conversion taxable portion; Part I tracked basis
      carryforward)
- [ ] Wei's remaining basis ($9,120) carries to 2026 Form 8606 Line 2
- [ ] If Wei does future conversions, apply pro-rata against the
      future-year aggregate (Box 5 of all traditional IRAs)
- [ ] Continue tracking Box 5 across all IRAs for retirement projection

## Validation summary
- Math: all checks passed
  - $30,000 conversion ✓ matches across 5498, 1099-R, 1040 Line 4a, 8606 Part II Line 16
  - $27,120 taxable portion ✓ computed via pro-rata: $30,000 −
    ($30,000 × 0.096) = $27,120
- Sanity:
  - Roth IRA Box 11 correctly unchecked (Roth no lifetime RMD)
  - Wei's basis history: $12,000 prior − $2,880 used = $9,120 carry to 2026
  - 1099-R distribution code 2 correctly reflects a Roth IRA conversion
    by a participant under 59½ (1099-R instructions, code 2)
- Next steps:
  - Tax owed on $27,120 conversion: ~$5,966 federal at Wei's 22%
    bracket (will appear on her 2025 Form 1040 total tax)
  - Continue annual basis tracking via Form 8606 Line 14

## Sources cited in this reconciliation
- IRS Form 5498 (2025)
- IRS Instructions for Forms 1099-R and 5498 (2025) — 1099-R code 2 for Roth IRA conversions
- IRS Form 8606 (2025) — Nondeductible IRAs, Lines 1–18
- IRS Form 1099-R (2025)
- IRC §408(d)(1)–(2) — IRA distributions taxed under §72 with all IRAs treated as one contract
- IRC §408A(c)(5) — Roth IRA RMD exemption for original owner
- IRS Pub 590-B — Distributions from IRAs
```

## Why each non-obvious choice

**Why does the pro-rata rule pull only $3,000 of basis when Wei has
$12,000 total basis?** The pro-rata rule treats all traditional /
SEP / SIMPLE IRAs as a single pool. Wei's basis of $12,000 is allocated
across her *aggregate* IRA value of $125,200. The conversion of
$30,000 represents about 24% of that total, so she "uses" about 24%
of her basis: $2,880 after the form's rounding. The remaining $9,120 stays
as unused basis pending future conversions or distributions.

**Why is the 1099-R Box 2a $30,000 (the gross) when the actual taxable
amount is $27,120?** The custodian doesn't track the user's basis. Box
2a is the custodian's best guess at the taxable amount, often equal to
Box 1 (the gross). The user's Form 8606 is the authoritative
calculation. The IRS expects this discrepancy when basis exists.

**Why is Box 11 unchecked on the Roth 5498 and what would it mean if
checked?** Original Roth IRA owners have no lifetime RMD requirement
(IRC §408A(c)(5)). If Box 11 were checked on the Roth 5498, it would
be a custodian error — request a corrected 5498. Inherited Roth IRAs
do have distribution rules for the beneficiary, but custodians are not
required to report RMDs for inherited IRAs on Form 5498 (2025
Instructions for Forms 1099-R and 5498, "RMDs").

**Why didn't Wei convert all $80,000 from Account A?** Tax planning.
Converting $80,000 in one year would push significant taxable income
into a higher marginal bracket. Wei chose $30,000 to stay within her
22% bracket. This is a multi-year strategy: she'll convert smaller
amounts each year, gradually drawing down her traditional IRA balance
into Roth.

**Why convert from Account A specifically and not Account B?** From a
pro-rata perspective, it doesn't matter which traditional account you
draw from — the basis is allocated across all of them. Wei chose Account
A simply because that's where the funds were liquid (Account B was in
less-liquid investments she didn't want to sell yet). The pro-rata rule
doesn't care which account the dollars physically came from.

**What records should Wei retain?**

1. All three 2025 Forms 5498
2. The 2025 1099-R from Vanguard for Account A
3. The 2025 Form 1040 + Form 8606 (both Part I tracking and Part II
   conversion)
4. All prior-year Forms 8606 (Wei should keep these forever — the basis
   chain depends on them)
5. Vanguard statements showing Account A balances before and after the
   conversion
6. This reconciliation report

The Form 8606 chain is the most important — without it, Wei (or her
estate) cannot prove basis in future conversions or distributions.
