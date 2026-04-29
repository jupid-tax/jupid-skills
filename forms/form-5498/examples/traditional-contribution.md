# Example: Traditional IRA Contribution Verified Against Schedule 1

A complete walkthrough of reconciling Form 5498 Box 1 (traditional IRA
contribution) against Schedule 1 Line 20 of the user's tax return. The
canonical "no surprises" reconciliation pattern.

## The filer

- **Name**: Sandra Patel
- **Age**: 42
- **Filing status**: Single
- **Tax year**: 2025 (Form 5498 received May 2026)
- **Account**: Traditional IRA at Schwab, opened 2017
- **Employment**: Marketing manager, W-2 income, **not** covered by an
  employer retirement plan (her employer doesn't offer one)

## The Form 5498 received

Sandra received this 5498 from Schwab in May 2026, covering 2025 tax
year contributions:

```
TRUSTEE'S name: Charles Schwab & Co., Inc.
TRUSTEE'S TIN: 94-XXXXXXX
PARTICIPANT'S name: Sandra Patel
PARTICIPANT'S SSN: XXX-XX-XXXX
Account number: ...8472

Box 1  IRA contributions:                  $7,000
Box 2  Rollover contributions:             (blank)
Box 3  Roth IRA conversion amount:         (blank)
Box 4  Recharacterized contributions:      (blank)
Box 5  FMV of account on 12/31/2025:       $54,300
Box 6  Life insurance cost:                (blank)
Box 7  IRA type:                           ✓ IRA
Box 8  SEP contributions:                  (blank)
Box 9  SIMPLE contributions:               (blank)
Box 10 Roth IRA contributions:             (blank)
Box 11 RMD required for next year:         ☐ (unchecked)
Box 12a RMD date:                          (blank)
Box 12b RMD amount:                        (blank)
Box 13a Postponed/late contribution:       (blank)
Box 14a Repayments:                        (blank)
Box 15a FMV of specified assets:           (blank)
```

## What Sandra did during 2025

- **March 2025**: contributed $4,000 to her traditional IRA (designated
  for tax year 2025)
- **December 2025**: contributed an additional $3,000 to her traditional
  IRA (designated for tax year 2025)
- Total 2025 contributions: $7,000 — exactly the 2025 IRA limit per
  Notice 2024-80 (Sandra is under 50, no catch-up)
- No rollovers, conversions, or recharacterizations
- She filed her 2025 tax return on April 1, 2026 (before receiving the
  5498)

## What Sandra's 2025 tax return showed

**Form 1040**:
- Line 1a (W-2 wages): $96,200
- Line 9 (total income): $96,505 (with some interest)
- Line 10 (adjustments to income from Schedule 1): $7,000
- Line 11 (AGI): $89,505

**Schedule 1**:
- Line 20 (IRA deduction): $7,000

**Form 8606**: Not filed (no nondeductible contributions, no Roth
conversions).

## Reconciliation walkthrough

### Step 1 — Identify populated boxes

Populated: Box 1, Box 5, Box 7. Everything else blank.

### Step 2 — Identify IRA type from Box 7

Box 7 = "IRA" (traditional). So the relevant contribution box is Box 1.

### Step 3 — Check deductibility

Sandra is **not** covered by an employer retirement plan. Per IRC §219(g),
the active-participant phaseout doesn't apply to her. She can deduct the
full $7,000 traditional IRA contribution regardless of MAGI.

### Step 4 — Reconcile Box 1 against Schedule 1 Line 20

| Source | Amount |
|--------|--------|
| Form 5498 Box 1 | $7,000 |
| Schedule 1 Line 20 | $7,000 |

✓ Match.

### Step 5 — Verify Box 5 (FMV) for next year's RMD context

Sandra is 42; not yet at RMD age. Box 11 is correctly unchecked. Box 5
is informational for now ($54,300). When Sandra reaches 73 in 2056, the
12/31/2055 Box 5 will drive her first-year RMD computation.

### Step 6 — Surface inconsistencies

None. All boxes reconcile or are appropriately blank.

## The reconciliation report

```markdown
# Form 5498 Reconciliation — Tax Year 2025

## Custodian
Name: Charles Schwab & Co., Inc.
TIN: 94-XXXXXXX
Account #: ...8472

## Account holder
Name: Sandra Patel
SSN: XXX-XX-XXXX
IRA Type (Box 7): IRA (Traditional)

## Populated boxes

| Box | Label | Amount | Reconciled to |
|-----|-------|--------|----------------|
| 1 | IRA contributions | $7,000 | Schedule 1 Line 20 |
| 5 | FMV 12/31/2025 | $54,300 | Informational (next-year RMD input) |
| 7 | IRA type | IRA | — |

All other boxes: blank (no rollover, conversion, recharacterization,
SEP/SIMPLE/Roth contribution; Sandra not yet at RMD age)

## Reconciliation status

| Box | Reconciled to | Status |
|-----|----------------|--------|
| Box 1 ($7,000) | Schedule 1 Line 20 ($7,000) | ✓ Match |
| Box 5 ($54,300) | (informational) | — N/A |
| Box 7 (IRA) | Box 1 populated, consistent | ✓ Match |

## Issues to resolve

None.

## Required actions
- [x] File 5498 in 2025 tax records (no IRS filing required)
- [ ] Check 2026 5498 when received (May 2027) for any 2026 activity
- [ ] No RMD required (Sandra is 42)
- [ ] Continue tracking Box 5 each year for retirement projection

## Validation summary
- Math: all checks passed
- Sanity:
  - Contribution within $7,000 IRA limit (Sandra under 50, no catch-up)
  - Sandra not covered by employer plan; full deduction allowed
  - Account type consistent (Box 7 IRA + Box 1 populated)
- Next steps:
  - File the 5498 in tax records
  - No further action required

## Sources cited in this reconciliation
- IRS Form 5498, Rev. 2025
- IRS Instructions for Form 5498, Rev. 2025
- IRC §219 (IRA deduction); §219(g) (active-participant phaseout)
- IRC §408 (IRA rules)
- Notice 2024-80 — 2025 IRA limit $7,000 ($8,000 age 50+)
- Sandra's 2025 Form 1040, Schedule 1
```

## Why each non-obvious choice

**Why is Sandra's full $7,000 deductible?** Because she's not an active
participant in an employer plan. The §219(g) phaseout only kicks in
when the user (or spouse, in some cases) is covered by an employer
retirement plan. Sandra's W-2 Box 13 "Retirement plan" checkbox should
be unchecked — that's the IRS signal that she's not an active
participant. No phaseout, full deduction.

**Why doesn't Sandra need Form 8606?** Form 8606 is for tracking
nondeductible contributions (basis) and Roth conversions. Sandra's
contribution is fully deductible (no nondeductible portion) and there
was no conversion. So no 8606.

**Why does the contribution split (March $4,000 + December $3,000)
not matter for the 5498?** Box 1 is the *total* contribution for the
tax year. Custodians don't report individual transactions on the 5498;
they report the total. The split matters only for the user's records
and for confirming each transaction landed correctly.

**Why filing in April before the 5498 arrived isn't a problem.** The
IRS designed the 5498 May 31 deadline knowing taxpayers file before
that date. The 5498 confirms what was claimed; if they match, no
discrepancy. If they didn't match, Sandra would need to amend.

**What records should Sandra retain?**

1. Schwab confirmation of the March 2025 $4,000 contribution
2. Schwab confirmation of the December 2025 $3,000 contribution
3. The 2025 Form 5498 (PDF or paper)
4. The 2025 Form 1040 + Schedule 1
5. This reconciliation report

Retain all for at least 7 years after the 2025 return due date (April
15, 2026 + 7 years = April 15, 2033).

**What if Sandra had been covered by an employer plan?** Her 2025 MAGI
of $89,505 would put her above the single-filer active-participant
phaseout upper limit of $89,000 for 2025 (per Notice 2024-80, $79K-$89K
phaseout). Almost no deduction would be allowed. The $7,000 contribution
would still be made, but it would be entirely nondeductible — going on
Form 8606 Line 1 as basis instead of Schedule 1 Line 20 as a deduction.
The 5498 Box 1 would still show $7,000 in either case.
