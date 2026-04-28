# Example: Late S-Corp Election with Rev. Proc. 2013-30 Relief

End-to-end worked example: LLC formed in 2024 that missed the original S-corp election deadline. User discovers the omission in 2026 while preparing taxes. Demonstrates Rev. Proc. 2013-30 mechanics — Part IV completion, reasonable-cause statement, and combined filing with first Form 1120-S.

---

## Scenario

**Filer**: Aisha Patel, freelance marketing consultant
**Entity**: Patel Strategic, LLC (California single-member LLC, formed 04/12/2024)
**EIN**: 88-7654321
**Tax history**: Filed Schedule C on 2024 Form 1040 (single-member LLC default)
**Profit history**: 2024 net profit $95,000 (Schedule C); 2025 net profit $185,000 (Schedule C)
**Discovery**: In April 2026, a CPA pointed out Aisha could have elected S-corp for 2024 or 2025
**Goal**: Elect S-corp retroactive to 01/01/2025, recapture SE-tax savings for 2025

---

## Step 1 — Eligibility check

```
□ Domestic LLC formed under California law           ✓
□ Not bank/insurance/§936/DISC                       ✓
□ Single shareholder (Aisha, U.S. citizen)           ✓
□ Aisha is U.S. citizen                              ✓
□ Single-member LLC, one class of stock              ✓
□ Operating agreement: standard pro-rata template     ✓
□ EIN matches "Patel Strategic, LLC"                  ✓
```

All eligibility checks pass.

---

## Step 2 — Deadline analysis

```
Intended effective date:  01/01/2025
Original deadline:        01/01/2025 + 2 months 15 days = 03/15/2025
Current date:             04/20/2026
Time past deadline:       ~13 months
Rev. Proc. 2013-30 window:
  Opens:                  01/01/2025
  Closes:                 01/01/2025 + 3 years 75 days = 03/17/2028
  Status:                 Within the 3-year-75-day window ✓

Late relief AVAILABLE under Rev. Proc. 2013-30.
```

---

## Step 3 — Rev. Proc. 2013-30 eligibility check

```
1. Entity intended S-corp from effective date (01/01/2025)?
   Aisha confirms she intended to operate as an S-corp from 2025;
   she just didn't know about the form.                                ✓

2. Entity failed to qualify SOLELY due to late filing (not eligibility)?
   All eligibility met (Step 1). Failure is purely procedural.          ✓

3. Reasonable cause for late filing?
   Aisha was unaware of the requirement to file Form 2553 within
   2 months 15 days. She believed Schedule C was the right path.
   She learned of the requirement from her new CPA on 04/15/2026.
   She is filing immediately upon discovery.                            ✓

4. Within 3 years 75 days of intended effective date?
   01/01/2025 + 3 years 75 days = 03/17/2028. Today is 04/20/2026.      ✓

5. Income reported consistent with S-corp treatment from 01/01/2025?
   Issue: Aisha already filed 2025 Form 1040 with Schedule C reporting
   $185K of LLC income. Rev. Proc. 2013-30 still permits relief, but
   Aisha must AMEND her 2025 Form 1040 to:
     - Remove Schedule C
     - Report $185K via Form 1120-S → Schedule K-1 → Form 1040 Schedule E
     - Compute reasonable salary retroactively for 2025
     - Pay back FICA on the salary portion (entity owes employer share)
     - Pay shortfall (or get refund) on the SE-tax-vs-FICA differential

   Aisha decides this is worth doing because the SE-tax savings
   on $185K profit are substantial (~$13K).                              ✓ (with amendment)
```

All five conditions met. Proceed with Rev. Proc. 2013-30 filing.

---

## Step 4 — Reasonable-cause statement

Aisha and the agent draft this statement. 2-4 sentences, factual:

> "Patel Strategic, LLC was formed on April 12, 2024, and the sole member intended at all times to operate the entity as an S-corporation effective January 1, 2025. The sole member was unaware that Form 2553 was required to be filed within 2 months and 15 days of the intended effective date and erroneously believed that filing Schedule C was the correct procedure. Upon being advised by her certified public accountant on April 15, 2026, of the requirement and of Rev. Proc. 2013-30 relief, the sole member promptly prepared and is filing this Form 2553 along with a corrected Form 1120-S for tax year 2025 and amended Form 1040-X to report income consistent with S-corp treatment."

This statement is attached as a separate page to Form 2553. Aisha signs and dates it.

---

## Step 5 — Reasonable-salary analysis (retroactive for 2025)

For the 2025 amendment, Aisha must compute a retroactive reasonable salary.

```
Role:           Marketing consultant / fractional CMO
BLS SOC code:   13-1161 (Market Research Analysts and Marketing Specialists)
2024 BLS median (national): $76,080  → adjusted up for senior level
Geographic:     California Bay Area — upward adjustment of ~25%
Hours/week:     ~40
Documented final 2025 salary: $90,000

Distribution:   $185,000 − $90,000 = $95,000

2025 retroactive payroll catch-up:
  W-2 wages reclassified from distributions:    $90,000
  Employer FICA (7.65%):                         $6,885
  Employee FICA (7.65%):                         $6,885
  FUTA (0.6% on first $7,000):                   $42
  CA SUTA (~3.4% on first $7,000):               $238

  Total catch-up payroll cost:                   ~$14,000 employer side

  Original 2025 SE tax paid (sole prop):         ~$26,142 (15.3% × 0.9235 × $185K capped)
  New 2025 FICA (employer + employee on $90K):  ~$13,770
  Net 2025 SE-tax savings:                       ~$12,372
                                                  (less penalties for late payroll deposits,
                                                   which can be abated with reasonable cause)
```

Even with retroactive payroll catch-up costs, Aisha nets ~$10K of savings on the 2025 amendment.

---

## Step 6 — Form 2553 draft

```
HEADER: write across top of page 1:

    FILED PURSUANT TO REV. PROC. 2013-30

PART I — ELECTION INFORMATION

A. Name of corporation:               Patel Strategic, LLC
B. Address:                           500 Howard St, Suite 100
                                      San Francisco, CA 94105
C. Employer Identification Number:    88-7654321
D. Date incorporated:                 04/12/2024
E. State of incorporation:            CA
F. Election effective date:           01/01/2025
G. Contact: Aisha Patel, 500 Howard St, Suite 100, SF, CA 94105, (415) 555-9876
H. Name change:                       (blank)
I. Tax year:
   [X] (1) Calendar year
   [ ] (2-4)

J. Officer signature:  Aisha Patel
   Title:              Sole Member
   Date:               04/20/2026

SHAREHOLDER CONSENT

| # | J. Name & address    | K. Sig. | L. Date    | M. Ownership            | N. SSN     |
|---|----------------------|---------|------------|-------------------------|------------|
| 1 | Aisha Patel          | A.Patel | 04/20/2026 | 100% from 04/12/2024    | XXX-XX-5678|
|   | 500 Howard St, #100  |         |            |                         |            |
|   | San Francisco, CA    |         |            |                         |            |

(Aisha is single — not in community-property state issue regardless,
 since CA community property only kicks in for married filers.)

PART II — Skip (calendar year)
PART III — Skip (no trust shareholder)

PART IV — LATE ELECTION RELIEF (REQUIRED)

[X] (1) The corporation intended to be classified as an S corporation as of
        the effective date entered on Line E.

[X] (2) The corporation has reasonable cause for its failure to make the
        timely election.

[X] (3) The corporation and all of its shareholders have reported their
        income for the period since the effective date in a manner consistent
        with S corporation status, OR will do so via amended returns.

ATTACHMENT: Reasonable-cause statement (separate page, Step 4 above), signed
            and dated by Aisha Patel.
```

---

## Step 7 — Filing channel decision

Because Aisha is filing late and also needs to file her first Form 1120-S for 2025, the cleanest approach is:

```
Mail Form 2553 ATTACHED to Form 1120-S for tax year 2025.

Service center: Ogden, UT (CA is in Ogden zone)
Address: Department of the Treasury
         IRS Service Center
         Ogden, UT 84201

Method: USPS Certified Mail with Return Receipt

Packet contents:
  1. Form 2553 (with "FILED PURSUANT TO REV. PROC. 2013-30" across top)
  2. Reasonable-cause statement
  3. Form 1120-S for tax year 2025 (with Aisha's Schedule K-1)
  4. Cover letter referencing both filings
```

Aisha mails on 04/22/2026. Certified Mail receipt postmarked 04/22/2026 — preserved as proof.

---

## Step 8 — Amend 2025 Form 1040

Separately, Aisha files **Form 1040-X** to:

- Remove Schedule C reporting $185K of LLC income
- Add Schedule E reporting Schedule K-1 from Form 1120-S
- Recompute SE tax (now $0 since income is via K-1, not Schedule C)
- Compute additional FICA owed on the $90K salary portion
- Net effect: refund approximately $5,000-$10,000 (less amendments processing)

Form 1040-X is filed via Aisha's tax software or paper. Wait time for processing: 12-16 weeks.

---

## Step 9 — California state conformity

California auto-conforms to federal S-corp election. Aisha files **Form 100S** (CA S-corp return) for 2025 instead of relying on Schedule C in her CA return.

CA also imposes 1.5% franchise tax on S-corp net income (minimum $800):
```
2025 CA franchise tax: max($800, $185,000 × 1.5%) = max($800, $2,775) = $2,775
```

This $2,775 is the cost of CA conformity — netted against the federal SE-tax savings.

```
Net 2025 benefit (federal − CA franchise):
  Federal SE-tax savings:    ~$12,372
  CA franchise tax cost:     − $2,775
  Net:                       ~$9,597
```

Still positive. Aisha proceeds.

---

## Step 10 — Wait for CP261

```
Day 1   (04/22): Mailed packet via Certified Mail
Day 7   (04/29): USPS Form 3811 returned showing IRS receipt
Day 65  (06/26): CP261 acknowledgment letter received
                  S-corp effective 01/01/2025 ✓
                  Aisha saves CP261 permanently — proof of S-corp from 2025
```

---

## Step 11 — Forward-looking compliance

For tax year 2026 (current year):
```
□ Continue $90K salary (or re-run analysis for 2026 increase)
□ Quarterly Form 941 (already starting Q2 2026 with retroactive payroll)
□ Annual Form 940 for 2026
□ CA Form 100S for 2026 (March 15, 2027 deadline)
□ Federal Form 1120-S for 2026 (March 15, 2027 deadline)
```

---

## Result

```
Permanent change to S-corp status from 01/01/2025
Recovered ~$10K of 2025 SE-tax savings via Rev. Proc. 2013-30 + 1040-X
Going forward: ~$12-15K/year SE-tax savings on $185K-ish profit
                 less ~$3K compliance + $2.8K CA franchise = ~$8-10K net annual benefit
```

---

## Lessons / what went right

1. **Caught the missed deadline within Rev. Proc. 2013-30 window** (13 months past, well within 3 years 75 days)
2. **Reasonable-cause statement was clean and factual** — "unaware of requirement, learned on [date], filing immediately"
3. **Combined filing with Form 1120-S** — simplest path; one packet, one service center
4. **2025 Form 1040-X amendment was budgeted into the decision** — Aisha understood the full picture before committing
5. **California conformity addressed at the same time** — Form 100S filed instead of doubling-up Schedule C and CA C-corp by accident
6. **CP261 received within 65 days** — confirms relief was granted; Aisha now has permanent S-corp status proof

---

## What could have gone wrong

If Aisha had discovered the omission in **2029** instead of 2026, the 3-year-75-day window for a 01/01/2025 effective date would already have closed (closes 03/17/2028). Her remaining option would be a **Private Letter Ruling under Reg. §301.9100-3**:
- $12,600 IRS user fee
- 6-12 month wait
- ~$10,000 tax attorney to prepare
- Discretionary — IRS may deny

This is why early discovery matters. The agent should always check the 3-year-75-day window first.
