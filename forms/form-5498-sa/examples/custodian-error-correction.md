# Example: Custodian Error and CORRECTED 5498-SA

David, 51, self-only HDHP. Custodian double-counted a transfer. Corrected 5498-SA issued; no Form 1040-X needed.

---

## Background

- **David**, age 51, IT consultant operating as a single-member LLC
- Self-only HDHP via individual marketplace
- HSA at HealthEquity since 2020
- Catch-up contribution eligible (age 55+ rule does NOT apply yet — David is 51)
- For tax year 2025:
  - $4,300 contribution limit (self-only)
  - David contributed exactly $4,300 in three direct ACH transfers
- David filed Form 8889 on March 30, 2026
- On May 28, 2026, David receives Form 5498-SA from HealthEquity — Box 2 reads **$5,150**, which exceeds the contribution limit by $850

## David's documents

### Form 8889 (filed March 30, 2026)

```
Line 1:  Self-only coverage  ✓
Line 2:  Direct HSA contributions:               $4,300
Line 3:  Contribution limit (self-only):         $4,300
Line 8:  Total limit:                            $4,300
Line 9:  Employer contributions:                     $0
Line 12:                                         $4,300
Line 13: HSA deduction:                          $4,300
            → Schedule 1, Line 13
```

### Bank records (David's checking, 2025)

| Date | Description | Amount |
|------|-------------|--------|
| 2025-04-30 | ACH to HealthEquity HSA | $1,433 |
| 2025-08-31 | ACH to HealthEquity HSA | $1,434 |
| 2025-12-15 | ACH to HealthEquity HSA | $1,433 |
| **Total direct contributions** | | **$4,300** |

### Initial Form 5498-SA from HealthEquity (received May 28, 2026)

```
Trustee: HealthEquity
Recipient: David
Account number: ********9012

Box 1: $0
Box 2: $5,150   ← exceeds annual limit by $850!
Box 3: $0
Box 4: $0
Box 5: $26,400
Box 6: HSA  ✓
```

### Apparent problem

```
Form 8889 Line 2:                              $4,300
Form 5498-SA Box 2:                            $5,150
Discrepancy:                                  +$850
```

If the 5498-SA is correct, David has an **excess contribution** of $850 ($5,150 received vs. $4,300 limit). The 6% excise tax would apply unless he withdraws the excess plus earnings by the extended October 15, 2026 deadline.

But David's bank records show only $4,300 in direct contributions. Where did the extra $850 come from?

## Diagnosis

The diagnosis tree (see [`references/reconciliation.md`](../references/reconciliation.md)) walks through causes in order:

1. **Prior-year contribution timing** — David did not make a January-April prior-year-designated contribution. Cause ruled out.
2. **December check timing** — David's December 15, 2025 transfer cleared on December 17, 2025. Cause ruled out.
3. **Custodian clerical error** — Worth investigating.

David logs into HealthEquity's portal and pulls the contribution history for 2025:

| Date | Description | Amount |
|------|-------------|--------|
| 2025-04-30 | ACH from David's checking | $1,433 |
| 2025-04-30 | ACH from David's checking — DUPLICATE | $850 |
| 2025-08-31 | ACH from David's checking | $1,434 |
| 2025-12-15 | ACH from David's checking | $1,433 |
| **HealthEquity total** | | **$5,150** |

There it is. HealthEquity recorded a duplicate transaction on April 30, 2025 — they posted David's $1,433 transfer once at full amount and once at $850 (apparently a partial duplicate from a payment retry).

David's bank statement confirms only **one** transfer on April 30, 2025 for $1,433. The $850 duplicate is not a real deposit — it's a phantom HealthEquity entry.

## Action: contact HealthEquity for CORRECTED 5498-SA

David calls HealthEquity's customer service on May 30, 2026:

> "My 2025 Form 5498-SA Box 2 reads $5,150, but my bank records show only $4,300 in transfers. Looking at your contribution history, there's an entry on April 30, 2025 for $850 that appears to be a duplicate of my $1,433 transfer that day. My bank only shows the $1,433 leaving my account. Can you investigate?"

HealthEquity researches and confirms the duplicate. They:

1. Reverse the phantom $850 entry from David's account
2. Issue a **CORRECTED 5498-SA** with "CORRECTED" box checked at the top
3. File the corrected version with the IRS automatically

David receives the CORRECTED form on June 18, 2026:

```
☑ CORRECTED

Trustee: HealthEquity
Recipient: David
Account number: ********9012

Box 1: $0
Box 2: $4,300   ← corrected!
Box 3: $0
Box 4: $0
Box 5: $25,550   ← also corrected (year-end FMV reduced by $850)
Box 6: HSA  ✓
```

## Reconciliation against CORRECTED form

```
Form 8889 Line 2:                              $4,300
Corrected 5498-SA Box 2:                       $4,300
                                              =======
Match!
```

The original Form 8889 was correct. No Form 1040-X is needed. David files both 5498-SAs (original and CORRECTED) with his 2025 tax records along with a memo documenting the correction.

## Reconciliation report

```markdown
# Form 5498-SA Reconciliation Report — Tax Year 2025

## Custodian and Account
- Custodian: HealthEquity
- Account number: ********9012
- Account holder: David
- Tax year: 2025

## 5498-SA Box Values (CORRECTED form, dated June 18, 2026)
| Box | Label                         | Value     |
|-----|-------------------------------|-----------|
| 1   | Archer MSA contributions      | $0        |
| 2   | Total contributions (cal yr)  | $4,300    |
| 3   | Prior-year contributions      | $0        |
| 4   | Rollover contributions        | $0        |
| 5   | Year-end FMV                  | $25,550   |
| 6   | Account type                  | HSA       |

## Cross-Form Comparison
| Check                                 | 5498-SA   | 8889       | Match? |
|---------------------------------------|-----------|------------|--------|
| Total 2025 contributions              | $4,300    | $4,300     | YES    |
| Direct contributions                  | $4,300    | $4,300     | YES    |
| Year-end FMV vs. Dec custodian stmt   | $25,550   | $25,550    | YES    |

## Reconciliation Status: PASS (after CORRECTED 5498-SA)

## Discrepancies
- Original 5498-SA (May 28, 2026) showed Box 2 = $5,150
- Investigation revealed HealthEquity duplicate entry of $850 on April 30, 2025
- CORRECTED 5498-SA issued June 18, 2026 with Box 2 = $4,300
- Reconciliation now passes against corrected form

## Required Follow-Up Actions
- [x] Filed both original and CORRECTED 5498-SAs with 2025 tax records
- [x] Memo documenting custodian error and correction
- [ ] No Form 1040-X required (original Form 8889 was correct)

## Sources
- Original Form 5498-SA (2025, dated May 28, 2026)
- CORRECTED Form 5498-SA (2025, dated June 18, 2026)
- Form 8889 (filed 2026-03-30)
- David's bank statements (April 2025)
- HealthEquity customer service ticket #HE-2026-XXXXXX (May 30, 2026)
- IRC §223
```

## Key takeaways

- An apparent excess contribution on Form 5498-SA can be a **custodian error**, not a filer error
- Always pull custodian's transaction history and compare against bank records before assuming the worst
- When the custodian made the error, the fix is a **CORRECTED 5498-SA** — not a Form 1040-X
- The CORRECTED form supersedes the original; the IRS receives the corrected version directly
- Document the custodian ticket number, the date of the call, and the dates of both 5498-SAs in your tax records
- Time matters: contact the custodian within 30 days of receiving an erroneous 5498-SA to ensure the correction is processed before any IRS notice goes out
