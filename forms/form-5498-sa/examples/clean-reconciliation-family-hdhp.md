# Example: Clean Reconciliation — Family HDHP

Marcus, 38, family HDHP, cafeteria plan plus direct deposits, all numbers reconcile cleanly.

---

## Background

- **Marcus**, age 38, employed full-time at a tech company
- Married, two kids, family HDHP coverage through his employer
- HSA at Fidelity Investments since 2018
- Cumulative HSA balance approximately $43,200 at year-end 2025
- For tax year 2025, Marcus contributed the full family limit of $8,550, split between:
  - Cafeteria plan via payroll: $6,000 (handled by employer)
  - Direct ACH deposits from his bank: $2,550 (in three installments — March, July, November)
- Marcus filed Form 8889 on April 12, 2026, before the deadline
- On May 18, 2026, he receives Form 5498-SA from Fidelity

## Marcus's documents

### Form 8889 (filed April 12, 2026)

```
Line 1:  Family coverage  ✓
Line 2:  Direct HSA contributions:               $2,550
Line 3:  Contribution limit (family, 12 months): $8,550
Line 4:  Archer MSA:                                 $0
Line 5:  Line 3 − Line 4:                        $8,550
Line 6:  Line 5:                                 $8,550
Line 7:  Catch-up (under 55):                        $0
Line 8:  Total limit:                            $8,550
Line 9:  Employer + cafeteria (W-2 Box 12 W):    $6,000
Line 10: Qualified HSA funding distribution:         $0
Line 11: Line 9 + Line 10:                       $6,000
Line 12: Line 2 + Line 11:                       $8,550
Line 13: HSA deduction:                          $2,550
            → Schedule 1, Line 13
```

Part II is all zeros — Marcus didn't take any distribution. Part III is skipped (no last-month rule).

### Form W-2 (received January 30, 2026)

Box 12 code W: **$6,000**

This represents the cafeteria plan contributions Marcus made through payroll, which the employer treated as employer contributions for tax purposes.

### Form 5498-SA from Fidelity (received May 18, 2026)

```
Trustee: Fidelity Investments
TIN: 04-2647...
Recipient: Marcus
SSN: ***-**-1234
Address: <home address>
Account number: ********7842

Box 1 (Archer MSA contributions):              $0
Box 2 (Total HSA contributions for 2025):  $8,550
Box 3 (Prior-year contributions made 2026):    $0
Box 4 (Rollover contributions):                $0
Box 5 (FMV at year-end 2025):             $43,200
Box 6 (Account type):                          HSA  ✓
```

### Bank records (Marcus's checking account, 2025)

| Date | Description | Amount |
|------|-------------|--------|
| 2025-03-15 | ACH to Fidelity HSA | $850 |
| 2025-07-22 | ACH to Fidelity HSA | $850 |
| 2025-11-30 | ACH to Fidelity HSA | $850 |
| **Total direct contributions** | | **$2,550** |

### December 31, 2025 custodian statement

Total HSA balance: **$43,200** (cash + Fidelity ZERO Total Market Index Fund)

## Step-by-step reconciliation

### Step 1: Verify header

- Name: matches  ✓
- SSN: matches  ✓
- Address: matches  ✓
- Account number: matches Fidelity online portal  ✓

### Step 2: Box-by-box review

```
Box 1: $0    → Marcus has no Archer MSA, expected
Box 2: $8,550 → Total contributions, see reconciliation below
Box 3: $0    → No prior-year-designated contribution made in 2026 for 2025
Box 4: $0    → No rollovers
Box 5: $43,200 → Year-end FMV, matches December custodian statement
Box 6: HSA  ✓ → Account type confirmed
```

### Step 3: Reconcile Box 2 against Form 8889

```
Form 5498-SA Box 2:                            $8,550
Form W-2 Box 12 code W:                       −$6,000  (cafeteria plan)
                                              -------
Direct contributions (derived):                $2,550

Form 8889 Line 2 (as filed):                   $2,550
                                              =======
Match!
```

### Step 4: Reconcile Form 8889 Line 9 against W-2

```
W-2 Box 12 code W:                             $6,000
Form 8889 Line 9 (as filed):                   $6,000
                                              =======
Match!
```

### Step 5: Verify Box 5 against December statement

```
5498-SA Box 5:                                $43,200
December 31, 2025 custodian statement:        $43,200
                                              =======
Match!
```

### Step 6: Cross-check direct contributions against bank records

```
Bank records (3 ACH transfers totaling):       $2,550
Form 8889 Line 2:                              $2,550
                                              =======
Match!
```

## Reconciliation report

```markdown
# Form 5498-SA Reconciliation Report — Tax Year 2025

## Custodian and Account
- Custodian: Fidelity Investments
- Account number: ********7842
- Account holder: Marcus
- Tax year: 2025

## 5498-SA Box Values
| Box | Label                         | Value     |
|-----|-------------------------------|-----------|
| 1   | Archer MSA contributions      | $0        |
| 2   | Total contributions (cal yr)  | $8,550    |
| 3   | Prior-year contributions      | $0        |
| 4   | Rollover contributions        | $0        |
| 5   | Year-end FMV                  | $43,200   |
| 6   | Account type                  | HSA       |

## Cross-Form Comparison
| Check                                 | 5498-SA   | 8889 / W-2 | Match? |
|---------------------------------------|-----------|------------|--------|
| Total contributions for tax year      | $8,550    | $8,550     | YES    |
| Cafeteria/employer portion            | $6,000    | $6,000     | YES    |
| Direct contributions                  | $2,550    | $2,550     | YES    |
| Year-end balance vs. Dec stmt         | $43,200   | $43,200    | YES    |

## Reconciliation Status: PASS

## Discrepancies
None.

## Required Follow-Up Actions
- [x] File 5498-SA with 2025 tax records
- [ ] No further action required

## Sources cited
- IRS Form 5498-SA (2025 revision)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025 revision)
- Form 8889 (filed 2026-04-12)
- Form W-2 (received 2026-01-30)
- Bank records (Marcus's checking, 2025)
- Fidelity December 31, 2025 statement
- IRC §223
```

## Key takeaways

- The reconciliation took 10 minutes and confirmed everything was correct
- The split between cafeteria plan ($6,000 → Line 9) and direct contributions ($2,550 → Line 2) is the most common HSA pattern; the reconciliation requires both Form 5498-SA AND Form W-2
- Box 5 ($43,200) is informational — it doesn't change anything on the return but is a useful baseline for tracking HSA growth as a retirement asset
- Marcus files the 5498-SA in his 2025 tax records folder and moves on

If any number had been off, the diagnosis tree in [`references/reconciliation.md`](../references/reconciliation.md) would walk through the most common causes in order.
