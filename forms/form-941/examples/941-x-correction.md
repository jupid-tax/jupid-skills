# Example: Employer Files 941-X to Add Misclassified Wages (Correcting Q2 2025)

A complete walkthrough of Form 941-X for an employer who discovers in November 2025 that a "1099 contractor" paid $18,000 in Q2 2025 was actually a W-2 employee under common-law factors. The employer must add the wages to Q2 2025 retroactively and pay back-FICA + FIT.

## The filer

- **Business name**: Aspen Studio LLC
- **EIN**: 91-XXXXXXX
- **Entity**: Multi-member LLC, taxed as partnership
- **Original Q2 2025 941**: Filed July 28, 2025; reported $42,000 wages, $5,800 FIT, $5,208 FICA
- **Issue discovered**: November 14, 2025
- **Worker reclassified**: Jordan Reyes, paid $18,000 across April 15 – June 30, 2025 as a "1099 contractor"
- **Quarter being corrected**: Q2 2025
- **Filing date for 941-X**: Late November 2025 (well within statute of limitations)

## The reclassification analysis

The CFO discovered during an internal review that Jordan worked exclusively for Aspen, used Aspen's equipment, followed Aspen's schedule, was supervised daily, and had no separate business. Under the IRS common-law test (behavioral control + financial control + relationship), Jordan is an employee, not a contractor.

The CFO consulted with a CPA who recommended:

1. File 941-X for Q2 2025 to add Jordan's wages
2. File 941-X for Q3 2025 (similar issue likely persisted)
3. Issue corrected W-2 / W-2c for 2025
4. The 1099-NEC originally issued to Jordan should not be filed (or if already filed, file a corrected 1099-NEC with $0 to nullify)
5. Use **Section 3509 reduced rates** since this is a voluntary employer reclassification (not IRS reclassification — IRS reclassification triggers higher rates)

### Section 3509 reduced rates

When the employer voluntarily reclassifies (not by IRS audit), and meets statutory requirements (no intentional disregard, prior 1099 was filed):

| Tax | Standard combined rate | §3509 reduced rate |
|-----|----------------------|---------------------|
| FIT withholding | Variable (W-4 driven) | 1.5% of wages |
| Employee SS | 6.2% | 20% × 6.2% = 1.24% |
| Employee Medicare | 1.45% | 20% × 1.45% = 0.29% |
| Employer SS | 6.2% (full) | 6.2% (full) |
| Employer Medicare | 1.45% (full) | 1.45% (full) |

If the prior 1099-NEC was **not** filed (intentional disregard), §3509 reduced rates do NOT apply — full rates do. Aspen filed the 1099-NEC for Jordan in January 2026, so reduced rates apply.

## The corrections to Q2 2025

### Original Q2 2025 941 (as filed)

```
Line 1: 8 employees
Line 2: $42,000.00
Line 3: $5,800.00
Line 5a col 1: $42,000.00 ; col 2: $5,208.00
Line 5c col 1: $42,000.00 ; col 2: $1,218.00
Line 5d: $0
Line 5e: $6,426.00
Line 6: $12,226.00
Line 7-9: $0
Line 10: $12,226.00
Line 11g: $0
Line 12: $12,226.00
Line 13a: $12,226.00 (deposits matched)
Line 14: $0
```

### Corrected Q2 2025 amounts (with Jordan added)

Adding Jordan's $18,000 wages with §3509 reduced rates:

| Item | Calculation | Amount |
|------|-------------|--------|
| Additional Line 2 wages | $18,000 | $18,000.00 |
| Additional FIT withholding (Line 3) | $18,000 × 1.5% | $270.00 |
| Additional SS wages (Line 5a col 1) | $18,000 | $18,000.00 |
| Additional SS tax (Line 5a col 2) | $18,000 × (6.2% employer + 1.24% employee §3509) = $18,000 × 7.44% | $1,339.20 |
| Additional Medicare wages (Line 5c col 1) | $18,000 | $18,000.00 |
| Additional Medicare tax (Line 5c col 2) | $18,000 × (1.45% employer + 0.29% employee §3509) = $18,000 × 1.74% | $313.20 |
| Total additional Line 5e | $1,339.20 + $313.20 | $1,652.40 |
| Total additional Line 6 / Line 10 / Line 12 | $270.00 + $1,652.40 | $1,922.40 |

Plus interest from the original due date (July 31, 2025) to the date 941-X is filed (~late November 2025) — about 4 months at the IRS short-term rate (~8% federal short-term + 3% per IRC §6621). If filed and paid before the IRS examines, this becomes interest-free under IRC §6205 — see "Interest-free adjustment" below.

## The completed Form 941-X draft

```markdown
# Form 941-X — DRAFT for Q2 2025 (filed late November 2025)

## Header
Employer name (legal):       Aspen Studio LLC
EIN:                         91-XXXXXXX
Address:                     789 Pine St, Denver, CO 80202

## Part 1
Quarter being corrected:     Q2 2025
Date original 941 filed:     July 28, 2025
Date error discovered:       November 14, 2025

Question 1: This is a CORRECTION to a previously-filed 941
Question 2 (path):
  [X] Box 1 — Adjusted employment tax return (under-reported tax; pay with the form)
  [ ] Box 2 — Claim (refund / abatement)

## Part 2 — Certifications

Question 3 — applies for under-reported tax:
  [X] I certify that this 941-X reports under-reported tax and I have paid
      (or will pay with this form) the additional tax owed.

Question 4 — applies for over-reported FICA (N/A here, this is under-reported)

Question 5 — applies for over-reported FIT withholding (N/A)

## Part 3 — Reason

Question 6 — Reason for correction:
  [X] Reclassification of workers (Section 3509 rates apply)

## Part 4 — Detailed corrections

Each line shows: Column 1 (corrected), Column 2 (originally reported), Column 3 (difference), Column 4 (tax).

| Line | Col 1 (corrected) | Col 2 (original) | Col 3 (diff) | Col 4 (tax adj) |
|------|------------------|-----------------|--------------|----------------|
| 6 (Line 2 wages) | $60,000.00 | $42,000.00 | $18,000.00 | (no tax in col 4 for line 6 — wages only) |
| 7 (Line 3 FIT) | $6,070.00 | $5,800.00 | $270.00 | $270.00 |
| 8 (Line 5a SS wages) | $60,000.00 | $42,000.00 | $18,000.00 | (use line 9 for tax) |
| 9 (Line 5a SS tax) | (compute from 5a col 2 corrected) | (original) | | $1,339.20 (§3509 rate) |
| 10 (Line 5c Medicare wages) | $60,000.00 | $42,000.00 | $18,000.00 | |
| 11 (Line 5c Medicare tax) | (compute from 5c col 2 corrected) | (original) | | $313.20 (§3509 rate) |

(Note: actual 941-X line numbering differs slightly from 941. Use Form 941-X line numbers for the filing; the table above is conceptual.)

## Part 5 — Total adjustment

Line 23 (Total) — sum of all Column 4 amounts:
  $270.00 + $1,339.20 + $313.20 = $1,922.40

Sign indication: Positive (under-reported tax — owe more)

## Part 6 — Detailed explanation (REQUIRED)

  In November 2025, internal review identified that Jordan Reyes — paid $18,000
  across April 15 through June 30, 2025 as a "1099 contractor" — was in fact
  a common-law employee under IRS Reg. §31.3121(d)-1(c) factors. Jordan worked
  exclusively for Aspen Studio LLC, used company equipment, followed company
  schedules, and had no independent business.

  The original 1099-NEC issued to Jordan in January 2026 will be corrected to
  $0 (1099-NEC with corrected box checked). Jordan will be issued W-2 for the
  full 2025 wages.

  Section 3509 reduced rates apply because:
  (a) Reclassification is voluntary by the employer, not IRS-initiated
  (b) Original 1099-NEC was filed in good faith
  (c) No intentional disregard

  Computation of Q2 2025 corrections:
   - Additional Line 2 wages: $18,000
   - Additional Line 3 FIT (1.5% per §3509): $270.00
   - Additional Line 5a SS (6.2% employer + 1.24% employee §3509 = 7.44%): $1,339.20
   - Additional Line 5c Medicare (1.45% employer + 0.29% employee §3509 = 1.74%): $313.20
   - Total Q2 correction: $1,922.40

  Q3 2025 also affected (Jordan continued working through year-end);
  separate 941-X for Q3 2025 will be filed concurrently.

## Part 7 — Sign here

Title: Managing Member
Phone: 720-555-0118
Date: November 22, 2025
Signature: __________

## Required attachments
- [X] Detailed explanation in Part 6
- [ ] Form 8974 — N/A
- [ ] Q3 2025 941-X — separate filing, also being prepared
- [ ] Form W-2 for Jordan — separate filing via SSA BSO before January 31, 2026
- [ ] Corrected 1099-NEC ($0) for Jordan — separate filing

## Validation summary
- Math: all checks passed
  - $18,000 × 1.5% = $270 (FIT under §3509) ✓
  - $18,000 × 7.44% = $1,339.20 (SS under §3509) ✓
  - $18,000 × 1.74% = $313.20 (Medicare under §3509) ✓
  - Sum = $1,922.40 ✓
- Sanity:
  - §3509 election certified — must show prior 1099 was filed (Aspen did file 1099-NEC in good faith)
  - Statute of limitations: original Q2 941 deemed filed July 31, 2025 → 3 years to assess = July 31, 2028; ample window
  - Interest-free adjustment available under IRC §6205 since employer self-discovered before IRS examination
  - Q3 2025 941-X needed for the same worker — file concurrently
  - W-2 must be issued (or W-2c if W-2 already issued at $0 wages); employee FICA cannot be retroactively withheld from already-paid wages, so the §3509 employee-share reduction is by law absorbed by the employer
- Next steps:
  - File 941-X for Q3 2025 (similar computation)
  - File 2025 W-2 for Jordan via SSA BSO (Box 1 = sum of Q2+Q3 wages = $36,000 estimated)
  - File 2025 W-2c if a W-2 was already issued (wasn't — Jordan got a 1099)
  - File corrected 1099-NEC ($0) to nullify the original
  - Pay the $1,922.40 (plus equivalent Q3 amount) via EFTPS at time of filing
  - State unemployment / state withholding implications — consult CO state DOL
  - Review remaining 1099 contractors for similar misclassification risk
  - Update worker classification policy and onboarding to apply common-law test

## Sources cited in this draft
- IRS Form 941-X (Rev. April 2025)
- IRS Instructions for Form 941-X (Rev. April 2025)
- IRC §3509 (reclassified worker reduced rates)
- IRC §6205 (interest-free adjustment for employment taxes)
- IRS Reg. §31.3121(d)-1(c) (common-law employee factors)
- IRS Reg. §31.3509-1 (Section 3509 mechanics)
- IRC §6511 (statute of limitations for refund claims — not applicable here, this is under-payment)
- IRC §6501 (statute of limitations for IRS assessment — 3 years; window open)
- Pub. 15-A (Employer's Supplemental Tax Guide), 2025 edition — worker classification
```

## Why each non-obvious choice

**Why §3509 reduced rates and not full rates?** Aspen filed the 1099-NEC in good faith for Jordan. Under IRC §3509, when the employer voluntarily reclassifies (not IRS-reclassified) AND the prior 1099 was filed (no intentional disregard), the reduced rates apply. If Aspen had not filed the 1099-NEC, full FICA + FIT-table rates would apply, and the bill would be roughly 2.5× larger.

**Why is the employee FICA portion reduced (1.24% / 0.29%) rather than the full 6.2% / 1.45%?** Section 3509 grants the reclassifying employer a reduced *employee*-share rate to recognize that the employer can't realistically recover FICA from already-paid wages (the employee got the gross amount). The employer effectively absorbs the employee's share; §3509 reduces what they have to pay.

**Why use Box 1 (Adjustment) and not Box 2 (Claim)?** Box 1 is for under-reported tax (Aspen owes more). Box 2 is for over-reported tax (refund). This is unambiguously under-reported.

**Why does the 1099-NEC need to be nullified?** If Jordan now has a W-2 for the same wages, an outstanding 1099-NEC would double-report income. Issue a corrected 1099-NEC marked "Corrected" with $0 in Box 1 to remove from IRS records. Otherwise, the IRS sees both a 1099 and a W-2 for Jordan and starts a CP2000 inquiry on Jordan's personal return.

**Why isn't this filed electronically?** Form 941-X is paper-only (no e-file path). Mail with payment to the address listed in Form 941-X instructions for the filer's state. USPS Certified Mail recommended.

**What about Q1 2025?** The agent should ask: did Jordan also work in Q1 2025? If yes, separate Q1 2025 941-X also needed. The user confirmed Jordan started April 15, 2025, so Q1 is unaffected.

**Audit defense for the 941-X:**
1. Worker classification analysis with common-law factors documented
2. Engagement records showing Jordan's exclusive work, equipment, schedule
3. Original 1099-NEC filing (proof for §3509 eligibility)
4. CPA opinion supporting reclassification
5. Corporate minute book entry recording the decision
6. Computations showing §3509 application
