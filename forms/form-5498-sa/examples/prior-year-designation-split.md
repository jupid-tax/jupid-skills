# Example: Prior-Year Designation Split Across Two 5498-SAs

Sarah, 42, self-only HDHP, made a March prior-year contribution. Reconciliation requires both years' 5498-SAs.

---

## Background

- **Sarah**, age 42, self-employed graphic designer
- Self-only HDHP via the individual market
- HSA at Lively
- For tax year 2025, Sarah wanted to max out the $4,300 self-only limit
- During calendar year 2025 she made $3,000 in direct contributions (paid quarterly)
- On March 5, 2026, she made an additional $1,300 contribution and **designated it as a tax-year-2025 contribution** through Lively's online portal
- Sarah filed Form 8889 on April 8, 2026, with $4,300 on Line 2 (the full $3,000 calendar-year contributions plus the $1,300 March prior-year contribution)
- On May 22, 2026, she receives the **2025** Form 5498-SA from Lively

## Sarah's documents at filing time (April 8, 2026)

### Form 8889 (filed April 8, 2026)

```
Line 1:  Self-only coverage  ✓
Line 2:  Direct HSA contributions:               $4,300
Line 3:  Contribution limit (self-only):         $4,300
Line 8:  Total limit:                            $4,300
Line 9:  Employer contributions:                     $0  (self-employed, no W-2)
Line 12: Line 2 + Line 11:                       $4,300
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

## Initial reconciliation against 2025 5498-SA

### 2025 Form 5498-SA from Lively (received May 22, 2026)

```
Trustee: Lively, Inc.
Recipient: Sarah
Account number: ********4421

Box 1 (Archer MSA contributions):              $0
Box 2 (Total HSA contributions for 2025):  $3,000   ← surprise!
Box 3 (Prior-year contributions made 2026):    $0
Box 4 (Rollover contributions):                $0
Box 5 (FMV at year-end 2025):             $18,400
Box 6 (Account type):                          HSA  ✓
```

### Apparent problem

```
Form 8889 Line 2:                              $4,300
Form 5498-SA Box 2:                            $3,000
Discrepancy:                                  −$1,300
```

Sarah panics: "I claimed a $4,300 deduction but Lively reports only $3,000. The IRS will think I over-claimed!"

## Diagnosis

The diagnosis tree (see [`references/reconciliation.md`](../references/reconciliation.md), Cause 1: Prior-year contribution timing) immediately suggests the explanation:

```
Did you make a contribution between January 1 and April 15, 2026,
designated as a tax-year-2025 contribution?
```

Sarah confirms: yes, the March 5, 2026 transfer of $1,300 was designated for 2025.

That contribution will appear on the **2026 Form 5498-SA Box 3** (not the 2025 form). The 2026 5498-SA won't be issued until May 31, 2027 — so Sarah cannot reconcile fully right now.

## What Sarah does

1. **Verify the designation was recorded properly.** Sarah logs into Lively's portal and confirms the March 5, 2026 transfer is tagged "tax year 2025" in the contribution history. Yes, it is.

2. **Pull the Lively account statement** to verify the deposit cleared March 5, 2026 and is shown as a 2025-designated contribution. Yes.

3. **Document the explanation.** Sarah writes a short memo:

   > "Form 8889 Line 2 of $4,300 includes:
   > - $3,000 direct contributions during calendar year 2025 (per 2025 Form 5498-SA Box 2)
   > - $1,300 prior-year-designated contribution made March 5, 2026 (will appear on 2026 Form 5498-SA Box 3, expected May 2027)
   >
   > Lively portal confirms the March 5, 2026 contribution is properly designated for tax year 2025."

4. **File the 2025 5498-SA** with her 2025 tax records along with the memo.

5. **Set a calendar reminder** for late May 2027 to verify the 2026 5498-SA Box 3 contains $1,300.

## When the 2026 Form 5498-SA arrives (May 2027)

Sarah receives the **2026** Form 5498-SA from Lively on May 18, 2027:

```
Box 1: $0
Box 2: $4,500   ← her 2026 calendar-year contributions
Box 3: $1,300   ← the March 5, 2026 prior-year designation for 2025  ✓
Box 4: $0
Box 5: $24,800  ← year-end FMV
Box 6: HSA
```

Sarah confirms Box 3 = $1,300 as expected. The full picture for tax year 2025 is now:

```
2025 Form 5498-SA Box 2:               $3,000
2026 Form 5498-SA Box 3 (Sarah's):   + $1,300
                                     -------
Total 2025 contributions:              $4,300

Form 8889 Line 2:                      $4,300
                                     =======
Match!
```

## Reconciliation report (May 2027 — final)

```markdown
# Form 5498-SA Reconciliation Report — Tax Year 2025

## Custodian and Account
- Custodian: Lively, Inc.
- Account number: ********4421
- Account holder: Sarah
- Tax year: 2025

## 5498-SA Box Values (from BOTH 2025 and 2026 forms)
| Source           | Box | Value   |
|------------------|-----|---------|
| 2025 Form        | 2   | $3,000  |
| 2026 Form        | 3   | $1,300  |
| **Combined for tax year 2025** |  | **$4,300** |

## Cross-Form Comparison
| Check                                 | 5498-SA   | 8889       | Match? |
|---------------------------------------|-----------|------------|--------|
| Total 2025 contributions              | $4,300    | $4,300     | YES    |
| Direct contributions                  | $4,300    | $4,300     | YES    |
| Employer contributions                | N/A       | $0         | YES    |

## Reconciliation Status: PASS

## Discrepancies
None — initial apparent discrepancy was resolved by pulling 2026 5498-SA Box 3 (prior-year designation).

## Sources
- IRS Form 5498-SA (2025 and 2026 revisions)
- Form 8889 (filed 2026-04-08)
- Lively transaction history
- Memo dated 2026-05-22 documenting prior-year designation
- IRC §223(d)(4)(B)
```

## Key takeaways

- The single most common cause of 5498-SA panic is **prior-year contribution timing**: a contribution made between January 1 and April 15 with prior-year designation
- The contribution lands on the **next year's** 5498-SA Box 3, not the current year's Box 2
- **Always pull both years' 5498-SAs** when reconciling a year that included prior-year-designated contributions
- The 1-year delay between the original return and the next year's 5498-SA means Sarah cannot fully reconcile until May 2027 — but she can document the expected outcome immediately
- This is **not a filer error**, **not a custodian error**, and **does not require Form 1040-X**
