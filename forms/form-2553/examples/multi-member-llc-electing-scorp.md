# Example: Multi-Member LLC Electing S-Corp

End-to-end worked example: 2-member LLC currently taxed as a partnership (Form 1065), both members consenting to S-corp election. Demonstrates the multi-shareholder consent mechanics, the operating-agreement amendment for one-class-of-stock compliance, and the partnership-to-S-corp transition.

---

## Scenario

**Filer**: Riverside Builds, LLC
**Members**:
  - Daniel Wright (50% member)
  - Rachel Adams (50% member)
**State**: Texas LLC, formed 06/01/2024
**EIN**: 99-1122334
**Tax history**: Filed Form 1065 (partnership) for 2024 and 2025
**Combined profit projection 2026**: $260,000
**Goal**: Elect S-corp effective 01/01/2026 for combined SE-tax savings

---

## Step 1 — Eligibility check (extra scrutiny for multi-member)

```
□ Domestic LLC formed under Texas law                  ✓
□ Not bank/insurance/§936/DISC                         ✓
□ Two shareholders (Daniel, Rachel)                    ✓ (well under 100)
□ Both are U.S. citizens                               ✓
□ Operating agreement review:                          REVIEW NEEDED — see Step 2
  - Standard 2-member operating agreement
  - Includes "preferred return" clause? UNKNOWN
□ EIN matches "Riverside Builds, LLC"                  ✓
```

**Multi-member trigger**: in a partnership-taxed LLC, members often negotiate non-pro-rata distribution terms (waterfalls, preferred returns, sweat-equity catch-ups). These violate the one-class-of-stock rule and must be removed before electing S-corp.

---

## Step 2 — Operating agreement audit

The agent reads the existing Riverside Builds operating agreement and finds:

```
Section 6.2 — Distributions
  "Distributions of Available Cash shall be made:
   First, to Members in proportion to their Capital Contributions
   until each has received an 8% annual return on contributions;
   Second, pro rata in accordance with Membership Percentages."

Section 7.1 — Liquidation Preferences
  "Upon liquidation, distributions shall follow Section 6.2 priority."
```

This 8% preferred return + waterfall **violates IRC §1361(b)(1)(D) (one class of stock)**. The current operating agreement is incompatible with S-corp status.

**Required fix before filing Form 2553**: amend the operating agreement to:

```
Section 6.2 — Distributions (AMENDED, effective 01/01/2026)
  "Distributions of cash or property shall be made to Members in proportion
   to their Membership Percentages."

Section 7.1 — Liquidation (AMENDED, effective 01/01/2026)
  "Upon liquidation, after payment of debts and obligations, remaining
   assets shall be distributed to Members in proportion to their
   Membership Percentages."
```

Daniel and Rachel sign the operating agreement amendment with effective date 01/01/2026 — **on or before the S-corp effective date**.

This is the single most-important step for multi-member LLCs. Skipping it voids the S-corp election from day one, with retroactive tax consequences.

---

## Step 3 — Deadline calculation

```
Tax year start:  01/01/2026
Deadline:        03/15/2026
Today:           02/01/2026
Status:          ON TIME (~6 weeks of cushion)
```

Standard election. No Part IV required.

---

## Step 4 — Break-even check

```
Combined net profit 2026: $260,000
50/50 split: each member's K-1 share = $130,000

If Riverside continues as partnership:
  Each member's SE tax on $130K:
    SE base: $130,000 × 0.9235 = $120,055
    SE tax (15.3%): $18,368
  Combined SE tax (both members): $36,737

If Riverside elects S-corp with $80K salary each:
  Each member: $80K W-2 + $50K K-1 distribution
  FICA per member: $80,000 × 15.3% = $12,240
  Combined FICA: $24,480
  Distribution FICA: $0

  Combined SE-tax savings: $36,737 − $24,480 = $12,257

Compliance overhead:
  Payroll software (2 employees):           $1,000
  TX state UI (low-tax state):              $400
  Bookkeeping increment:                    $1,800
  Form 1120-S preparation:                  $2,000
  Total overhead:                           ~$5,200

Net annual benefit:                          $12,257 − $5,200 ≈ $7,000
```

In favor of electing.

---

## Step 5 — Reasonable-salary analysis (per member)

Both Daniel and Rachel are 50/50 owners but perform different roles:

```
Daniel — Field operations / project manager
  BLS SOC: 11-9021 Construction Managers — 2024 median $104,900 (national)
  Texas-adjusted: ~$95,000
  Hours/week: 50 (active operations)
  Documented salary: $80,000 (conservative below BLS)

Rachel — Sales, business development, finance
  BLS SOC: 11-1021 General and Operations Managers — 2024 median $101,280
  Texas-adjusted: ~$92,000
  Hours/week: 45 (mix of office + field)
  Documented salary: $80,000 (parity with Daniel — equal partners equal pay)
```

Both salaries documented in writing, signed by both members. Memo dated 02/01/2026.

---

## Step 6 — Both members consent

S-corp election requires **unanimous shareholder consent**. Both Daniel and Rachel must sign Form 2553 Column K. Both provide SSN in Column N.

```
Daniel — single, lives in Texas. Texas IS a community-property state.
   ⚠ Daniel's spouse (if any) must also sign.
   Daniel is unmarried — no spouse signature needed.

Rachel — married, lives in Texas (community-property state).
   ⚠ Rachel's spouse (Mark Adams) must also sign and provide SSN.
   Rachel and Mark both sign.
```

---

## Step 7 — Form 2553 draft

```
PART I — ELECTION INFORMATION

A. Name of corporation:               Riverside Builds, LLC
B. Address:                           7800 Industrial Way
                                      Austin, TX 78745
C. Employer Identification Number:    99-1122334
D. Date incorporated:                 06/01/2024
E. State of incorporation:            TX
F. Election effective date:           01/01/2026
G. Contact: Daniel Wright, 7800 Industrial Way, Austin, TX 78745, (512) 555-1010
H. Name change:                       (blank)
I. Tax year:
   [X] (1) Calendar year
J. Officer:    Daniel Wright
   Title:      Member-Manager
   Date:       02/01/2026

SHAREHOLDER CONSENT STATEMENT

| # | J. Name & address       | K. Sig.  | L. Date    | M. Ownership          | N. SSN     |
|---|-------------------------|----------|------------|-----------------------|------------|
| 1 | Daniel Wright           | D.Wright | 02/01/2026 | 50% from 06/01/2024   | XXX-XX-1111|
|   | 7800 Industrial Way     |          |            |                       |            |
|   | Austin, TX 78745        |          |            |                       |            |
| 2 | Rachel Adams            | R.Adams  | 02/01/2026 | 50% from 06/01/2024   | XXX-XX-2222|
|   | 1505 Oak Lane           |          |            |                       |            |
|   | Austin, TX 78704        |          |            |                       |            |
| 3 | Mark Adams              | M.Adams  | 02/01/2026 | (community-prop spouse| XXX-XX-3333|
|   | (spouse, Rachel Adams)  |          |            |  consent only — 0%)   |            |
|   | 1505 Oak Lane           |          |            |                       |            |
|   | Austin, TX 78704        |          |            |                       |            |

PART II — Skip (calendar year)
PART III — Skip (no trust shareholder)
PART IV — Skip (on time)

ATTACHMENTS:
  - Operating agreement amendment effective 01/01/2026 (NOT required by IRS but
    kept in user's records as proof of one-class-of-stock compliance)
  - Reasonable-comp memos for both Daniel and Rachel (kept in records)
```

---

## Step 8 — Validation

```
□ Eligibility: PASS (operating agreement amended, all members eligible)
□ Timing: ON TIME
□ Consents: 2 of 2 shareholders + 1 of 1 community-property spouses signed
□ Math: 50% + 50% = 100% ✓
□ Sanity warnings: $80K salary on $130K K-1 income per member = 62% — well above
                  any "underpayment" risk threshold
□ Form completeness: A-J complete, Line I Box 1 checked
```

Ready to file.

---

## Step 9 — Filing

```
Service center:   Ogden, UT (TX is in Ogden zone)
Method:           Fax to 855-214-7520
Date:             02/02/2026, 11:30 AM
Pages:            2
Confirmation:     SUCCESSFUL — saved as PDF
```

No mailing — fax only.

---

## Step 10 — Wait for CP261

```
Day 1   (02/02): Filed via fax
Day 45  (03/19): CP261 received — S-corp effective 01/01/2026 ✓
                  Riverside Builds saves CP261 permanently
```

---

## Step 11 — Partnership-to-S-corp transition

This is the multi-member-specific step. The entity is moving from Form 1065 (partnership) to Form 1120-S (S-corp).

```
Tax year 2025 (final partnership year):
  □ File final Form 1065 marked "Final Return" (due 03/15/2026)
  □ Issue final Schedule K-1s to Daniel and Rachel (50/50 split of 2025 income)
  □ Daniel and Rachel each report 2025 K-1 income on their personal returns

Tax year 2026 (first S-corp year):
  □ File Form 1120-S marked "Initial Return" by 03/15/2027
  □ Issue Schedule K-1s reflecting wages + distributions
  □ Daniel and Rachel each report W-2 wages on Form 1040 Line 1
    AND K-1 income on Schedule E

Payroll setup (effective 01/01/2026 or as soon as CP261 received):
  □ Both Daniel and Rachel set up as W-2 employees of Riverside Builds, LLC
  □ Bi-weekly payroll: $80,000 / 26 = $3,077 each per pay period
  □ Federal income tax withholding (W-4 each)
  □ FICA: 7.65% employer + 7.65% employee = 15.3% combined
  □ FUTA: 0.6% on first $7,000 per employee
  □ TX SUTA: rate ~ 2.7% on first $9,000 (rate set by TX Workforce Commission)
  □ Quarterly Form 941 (employer side) — covering both employees
  □ Annual Form 940 — covering both
  □ W-2 to each employee by Jan 31, 2027
```

---

## Step 12 — State conformity

Texas has no state income tax. The federal S-corp election does not require a separate Texas filing for income tax purposes.

However, Texas has a **franchise tax (margin tax)**:
- Riverside Builds owes franchise tax regardless of federal tax election
- 0.375% retail / 0.75% other rate on net taxable margin (above $1.23M no-tax threshold for 2025)
- 2026 projected revenue likely below the no-tax threshold, but verify annually with TX Comptroller

The S-corp election is **net-positive** in Texas because:
- No state income tax to layer on top
- No state-level S-corp "anti-conformity" tax (unlike CA, NJ, IL, etc.)

---

## Result

```
2026 SE-equivalent tax under partnership:    $36,737 combined
2026 FICA under S-corp:                      $24,480 combined
Compliance overhead:                          $5,200
Net 2026 benefit:                             ~$7,000

Going forward: similar savings annually, scaling with profit
```

---

## Lessons / what went right

1. **Operating agreement amended BEFORE filing** — fixed the preferred-return + waterfall before the S-corp effective date. Without this, the election would have been void from day one.
2. **Both members signed Column K** — unanimous consent is non-negotiable for S-corp election.
3. **Community-property spouse signed** — Texas is community-property; Mark's signature was required.
4. **Reasonable salaries documented per member** — $80K each, BLS-anchored, signed memos.
5. **Final 1065 + initial 1120-S transition planned** — clean handoff between tax forms, no double-reporting.

---

## What could have gone wrong

If Daniel and Rachel had filed Form 2553 without amending the operating agreement first:

- Election would be void from 01/01/2026 (one-class-of-stock violation)
- They would unknowingly file Form 1120-S for 2026 and beyond
- On audit (typically 2-3 years later), the IRS would unwind the S-corp treatment retroactively
- All 2026+ income would be reclassified as partnership income on Form 1065
- Both members would owe back-SE-tax on 100% of profits (no FICA cap benefit)
- Plus penalties for underpayment, failure to file 1065, etc.
- Estimated cost of this error: $40,000-$80,000 in back tax + penalties + interest

The 30 minutes spent amending the operating agreement saved a six-figure mistake.
