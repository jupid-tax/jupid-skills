# Example: Prior-Year Designation Read Across Box 2 and Box 3

Sarah, 42, self-only HDHP, made a March prior-year contribution. Reconciliation needs Box 3 of the 2025 form, and next year it needs that same Box 3 again to read the 2026 form correctly.

Rules used (2025 Instructions for Forms 1099-SA and 5498-SA): Box 2 = total contributions **made in** the calendar year, including contributions made in that year for the prior year; Box 3 = contributions made in the following year (by April 15) **for** the year on the form.

---

## Background

- **Sarah**, age 42, self-employed graphic designer
- Self-only HDHP via the individual market
- HSA at Lively
- For tax year 2025, Sarah wanted to max out the $4,300 self-only limit (Rev. Proc. 2024-25)
- During calendar year 2025 she made $3,000 in direct contributions (paid quarterly); none of it was designated for 2024
- On March 5, 2026, she made an additional $1,300 contribution and **designated it as a tax-year-2025 contribution** through Lively's online portal
- Sarah filed Form 8889 on April 8, 2026, with $4,300 on Line 2 (the $3,000 made in 2025 plus the $1,300 March prior-year contribution)
- On May 22, 2026, she receives the **2025** Form 5498-SA from Lively

## Sarah's documents at filing time (April 8, 2026)

### Form 8889 (filed April 8, 2026)

```
Line 1:  Self-only coverage  ✓
Line 2:  Direct HSA contributions:               $4,300
Line 3:  Contribution limit (self-only):         $4,300
Line 8:  Total limit:                            $4,300
Line 9:  Employer contributions:                     $0  (self-employed, no W-2)
Line 12: Line 8 − Line 11:                       $4,300
Line 13: HSA deduction:                          $4,300
            → Schedule 1, Line 13
```

### Bank records (Sarah's business checking, 2025 + early 2026)

| Date | Description | Amount |
|------|-------------|--------|
| 2025-04-15 | Transfer to Lively HSA | $750 |
| 2025-07-15 | Transfer to Lively HSA | $750 |
| 2025-10-15 | Transfer to Lively HSA | $750 |
| 2025-12-15 | Transfer to Lively HSA | $750 |
| **2025 total** | | **$3,000** |
| 2026-03-05 | Transfer to Lively HSA — **designated for 2025** | $1,300 |
| **2025 effective total (with March prior-year)** | | **$4,300** |

## Reconciliation against the 2025 5498-SA

### 2025 Form 5498-SA from Lively (received May 22, 2026)

```
Trustee: Lively
Recipient: Sarah
Account number: ********4421

Box 1 (Archer MSA contributions):                   $0
Box 2 (Total contributions made in 2025):       $3,000   ← looks short
Box 3 (Contributions made in 2026 for 2025):    $1,300
Box 4 (Rollover contributions):                     $0
Box 5 (FMV at year-end 2025):                  $18,400
Box 6 (Account type):                              HSA  ✓
```

### Apparent problem

Sarah reads Box 2 only:

```
Form 8889 Line 2:                              $4,300
Form 5498-SA Box 2:                            $3,000
Discrepancy:                                  −$1,300
```

Sarah panics: "I claimed a $4,300 deduction but Lively reports only $3,000. The IRS will think I over-claimed!"

## Diagnosis

The diagnosis tree (see [`references/reconciliation.md`](../references/reconciliation.md), Cause 1: Prior-year contribution timing) asks:

```
Did you make a contribution between January 1 and April 15, 2026,
designated as a tax-year-2025 contribution?
```

Sarah confirms: yes, the March 5, 2026 transfer of $1,300 was designated for 2025. It is in **Box 3 of the same 2025 form**. Box 2 counts only money received in 2025.

```
2025 Form 5498-SA Box 2:                 $3,000
− 2024 Form 5498-SA Box 3:              −    $0   (no 2025 money designated for 2024)
+ 2025 Form 5498-SA Box 3:              + $1,300
                                        -------
Contributions for 2025:                  $4,300

Form 8889 Line 2 + Line 9 + Line 10:     $4,300 + $0 + $0 = $4,300
                                        =======
Match!
```

## What Sarah does

1. **Confirm the designation in the portal.** The March 5, 2026 transfer is tagged "tax year 2025" in Lively's contribution history, matching Box 3.
2. **File the 2025 5498-SA** with her 2025 tax records. No memo, custodian call, or amendment is needed.
3. **Note the carry-over for next year.** The same $1,300 was received in 2026, so it will also be in Box 2 of her 2026 Form 5498-SA.

## Next year: the 2026 Form 5498-SA (received in May 2027)

In 2026 Sarah contributes $4,400 for 2026 (the 2026 self-only limit, Rev. Proc. 2025-19) and makes no 2027 contribution designated for 2026. Her 2026 Form 5498-SA (continuous-use Rev. December 2026) shows:

```
Box 1: $0
Box 2: $5,700   ← $1,300 (made in 2026 for 2025) + $4,400 (for 2026)
Box 3: $0
Box 4: $0
Box 5: <year-end FMV>
Box 6: HSA
```

Reconciling the 2026 Form 8889:

```
2026 Box 2:                              $5,700
− 2025 Box 3:                           − $1,300
+ 2026 Box 3:                           +     $0
                                        -------
Contributions for 2026:                  $4,400   = 2026 Form 8889 Line 2
```

Without subtracting the 2025 Box 3, Sarah would think Lively over-reported her 2026 contributions by $1,300, or that she had a $1,300 excess.

## Reconciliation report (May 2026)

```markdown
# Form 5498-SA Reconciliation Report — Tax Year 2025

## Custodian and Account
- Custodian: Lively
- Account number: ********4421
- Account holder: Sarah
- Tax year: 2025

## 5498-SA Box Values
| Source           | Box | Value   |
|------------------|-----|---------|
| 2025 Form        | 2   | $3,000  |
| 2024 Form        | 3   | $0      |
| 2025 Form        | 3   | $1,300  |
| **Contributions for tax year 2025** |  | **$4,300** |

## Cross-Form Comparison
| Check                                 | 5498-SA   | 8889       | Match? |
|---------------------------------------|-----------|------------|--------|
| Total 2025 contributions              | $4,300    | $4,300     | YES    |
| Direct contributions                  | $4,300    | $4,300     | YES    |
| Employer contributions                | N/A       | $0         | YES    |

## Reconciliation Status: PASS

## Discrepancies
None — the apparent $1,300 gap was the March 2026 contribution shown in Box 3 of the 2025 form.

## Required Follow-Up Actions
- [x] File 2025 5498-SA with 2025 tax records
- [ ] Next year: subtract the 2025 Box 3 ($1,300) from the 2026 Box 2

## Sources
- IRS Form 5498-SA (2025) and Instructions for Forms 1099-SA and 5498-SA (2025), Boxes 2 and 3
- Form 8889 (filed 2026-04-08)
- Lively transaction history
- IRC §223(d)(4)(B) (applies §219(f)(3): contributions by the unextended due date count for the prior year)
- Rev. Proc. 2024-25 (2025 limit $4,300); Rev. Proc. 2025-19 (2026 limit $4,400)
```

## Key takeaways

- The single most common cause of 5498-SA panic is **prior-year contribution timing**: a contribution made between January 1 and April 15 with prior-year designation
- That contribution shows in **Box 3 of the form for the year it was designated for**, and again in **Box 2 of the next year's form** because it was received that year
- Contributions for a year = that year's Box 2 − the prior year's Box 3 + that year's Box 3
- Sarah can reconcile 2025 in full as soon as the 2025 5498-SA arrives; the Box 3 amount matters again when she reads the 2026 form
- This is **not a filer error**, **not a custodian error**, and **does not require Form 1040-X**
