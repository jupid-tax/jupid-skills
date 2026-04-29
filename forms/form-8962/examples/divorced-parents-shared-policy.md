# Example: Divorced Parents Sharing a Marketplace Policy — Part IV Allocation

A complete walkthrough of Form 8962 when a couple held a shared marketplace policy at the start of the year, divorced mid-year, and now files separately. Each ex-spouse must reconcile their allocated share of the policy under Reg. §1.36B-4. Result: Part IV completed, with each filer computing PTC on an agreed allocation percentage.

## The filers

- **Names**: Daniel Park (primary filer for this draft) and Rachel Park (his ex-spouse, files her own return)
- **Filing status this year**: Single (Daniel) and Head of Household (Rachel — she keeps the children)
- **Tax year**: 2025 (filing in 2026)
- **State**: Illinois (48 contiguous + DC group)
- **Coverage**: Family Silver plan covering Daniel, Rachel, and their two children, January–June; Daniel switched to employer coverage in July; Rachel and the children stayed on a separate marketplace policy from July onward (handled on a different 1095-A — out of scope for this allocation example, which is about the Jan–Jun shared policy)

## The shared-policy situation

Daniel and Rachel were married through 2024, divorced June 30, 2025. From January through June, they had one joint marketplace policy covering all four family members. From July onward, they each had their own coverage arrangement.

For the **Jan–Jun joint policy**, the marketplace issued **one Form 1095-A** in Daniel's name (he was the primary subscriber). The form shows Jan–Jun monthly amounts; Jul–Dec are blank because the policy terminated June 30.

Because Daniel and Rachel are now in separate tax families, each must report a portion of that shared policy on their own Form 8962. They negotiated and agreed on a **50/50 allocation** for Jan–Jun. (If they could not agree, the default under Reg. §1.36B-4(a)(1)(ii)(B) would be 50/50 anyway, but having a written agreement avoids dispute.)

## Inputs gathered (Daniel's return)

### Income

- Daniel's W-2 wages: $58,200
- Bank interest: $90
- AGI = $58,200 + $90 = **$58,290**
- Tax-exempt interest: $0; non-taxable SS: $0; foreign income exclusion: $0
- MAGI for PTC = **$58,290**

### Tax family

- Daniel's tax family for 2025: 1 (just himself; the children are claimed by Rachel as HoH per the divorce decree)
- 2024 FPL (48+DC, family size 1) = **$15,060**

### % of FPL

- Line 5 = ($58,290 / $15,060) × 100 = 387.0% → **387%**

### Form 1095-A data (the shared Jan–Jun policy)

Monthly amounts on the 1095-A in Daniel's name:

| Month | Col A (premium) | Col B (SLCSP) | Col C (APTC) |
|-------|----------------|---------------|--------------|
| Jan | $1,520 | $1,440 | $980 |
| Feb | $1,520 | $1,440 | $980 |
| Mar | $1,520 | $1,440 | $980 |
| Apr | $1,520 | $1,440 | $980 |
| May | $1,520 | $1,440 | $980 |
| Jun | $1,520 | $1,440 | $980 |
| Jul–Dec | $0 | $0 | $0 |

Annual totals on the 1095-A as issued: Col A = $9,120; Col B = $8,640; Col C = $5,880.

### Allocation agreement

Daniel and Rachel signed a written allocation agreement: **50% to Daniel, 50% to Rachel** for Jan–Jun premiums, SLCSP, and APTC. Rachel's Form 8962 will show the matching 50% on her own Part IV.

### Method decision

Multiple triggers for **monthly method**:
- Family size changed mid-year (divorce; children moved to Rachel's tax family)
- Coverage on the joint policy ended mid-year (June 30)
- Policy was shared between two tax families for Jan–Jun
- Daniel had no marketplace coverage Jul–Dec

→ **Monthly method (Line 10 = No)**.

## Form 8962 computation (Daniel's return)

### Part I

| Line | Value | Computation |
|------|-------|-------------|
| 1 | 1 | Daniel's tax family size for 2025 |
| 2a | $58,290 | Daniel's MAGI |
| 2b | $0 | No dependents on Daniel's return |
| 3 | $58,290 | Line 2a + Line 2b |
| 4 | $15,060 | 2024 FPL, 48+DC, family size 1 |
| 5 | 387% | (58,290 / 15,060) × 100 = 387.05% → 387% |

### Line 7 — Applicable figure (2025 IRA table, 387% FPL)

Band: 300% – 400%, initial 0.06, final 0.085.

```
applicable_figure = 0.06 + (387 − 300) / (400 − 300) × (0.085 − 0.06)
                  = 0.06 + (87 / 100) × 0.025
                  = 0.06 + 0.02175
                  = 0.08175
```

→ Line 7 = **0.0818** (rounded to 4 decimals)

### Part I continued

| Line | Value | Computation |
|------|-------|-------------|
| 8a | $4,768 | $58,290 × 0.0818 (rounded) |
| 8b | $397 | $4,768 / 12 |

### Part IV — Allocation (Lines 30–33)

Daniel completes one allocation entry for the shared Jan–Jun policy.

| Field | Value |
|-------|-------|
| 30a — Other tax family's SSN | Rachel's SSN |
| 30b — Allocation start month | January |
| 30c — Allocation stop month | June |
| 30d — Premium percentage | 50% |
| 30e — SLCSP percentage | 50% |
| 30f — APTC percentage | 50% |

### Part II — Monthly calculation, applying the allocation

For Jan–Jun, Daniel uses **50% of each 1095-A column**. For Jul–Dec, no marketplace coverage, so the rows are zero.

Daniel's allocated monthly amounts (Jan–Jun):
- Allocated premium: $1,520 × 50% = $760
- Allocated SLCSP: $1,440 × 50% = $720
- Allocated APTC: $980 × 50% = $490
- Monthly contribution (Line 8b): $397

| Month | Col a (prem) | Col b (SLCSP) | Col c (contrib) | Col d (max assist) | Col e (PTC) | Col f (APTC) |
|-------|-------|------|------|------|------|------|
| Jan (12) | $760 | $720 | $397 | $323 | $323 | $490 |
| Feb (13) | $760 | $720 | $397 | $323 | $323 | $490 |
| Mar (14) | $760 | $720 | $397 | $323 | $323 | $490 |
| Apr (15) | $760 | $720 | $397 | $323 | $323 | $490 |
| May (16) | $760 | $720 | $397 | $323 | $323 | $490 |
| Jun (17) | $760 | $720 | $397 | $323 | $323 | $490 |
| Jul–Dec (18–23) | $0 | $0 | $0 | $0 | $0 | $0 |

Each row's Col d = max(0, Col b − Col c) = max(0, 720 − 397) = $323.
Each row's Col e = min(Col a, Col d) = min(760, 323) = $323.

### Reconciliation

| Line | Value | Computation |
|------|-------|-------------|
| 24 | $1,938 | Sum Col e Jan–Jun: 6 × $323 |
| 25 | $2,940 | Sum Col f Jan–Jun: 6 × $490 |
| 26 | — | (skip; Line 25 > Line 24) |
| 27 | $1,002 | Line 25 − Line 24 |
| 28 | $1,625 | Pub 974 Table 5: 387% FPL, Single row (300%–400%) = $1,625 |
| 29 | $1,002 | min($1,002, $1,625) |

→ **Schedule 2 Line 2 = $1,002** (excess APTC repayment, below the cap)

The cap doesn't bind here (raw excess of $1,002 is less than the $1,625 single-filer cap), so Daniel repays the full $1,002.

## The completed Form 8962 draft (Daniel's return)

```markdown
# Form 8962 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Daniel Park
Your social security number: XXX-XX-XXXX

## Part I — Annual and Monthly Contribution Amount
1.  Tax family size:                                      1
2a. Modified AGI of taxpayer:                             $58,290
2b. Dependents' modified AGI:                             $0
3.  Household income:                                     $58,290
4.  Federal poverty line (FPL) for family size:           $15,060
5.  Household income as % of FPL (rounded down):          387 %
6.  (Reserved):                                           —
7.  Applicable figure:                                    0.0818
8a. Annual contribution amount:                           $4,768
8b. Monthly contribution amount:                          $397

## Part II — Premium Tax Credit Claim and Reconciliation of APTC
9.  Did you allocate policy amounts? Yes / No:            Yes
10. Annual calculation? Yes / No:                         No

11. (skip; using monthly method)

12. January     a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
13. February    a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
14. March       a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
15. April       a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
16. May         a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
17. June        a. $760  b. $720  c. $397  d. $323  e. $323  f. $490
18. July        all zeros (no marketplace coverage)
19. August      all zeros
20. September   all zeros
21. October     all zeros
22. November    all zeros
23. December    all zeros

24. Total Premium Tax Credit:                             $1,938
25. Advance payment of PTC:                               $2,940
26. Net Premium Tax Credit:                               $0    (Line 25 > Line 24)
27. Excess APTC (Line 25 − Line 24):                      $1,002
28. Repayment limitation (Pub 974 Table 5,
    Single at 387% FPL → 300%-400%):                      $1,625
29. Excess APTC repayment (lesser of 27 or 28):           $1,002
    → enter on Schedule 2 Line 2

## Part IV — Allocation of Policy Amounts (line 30, first/only entry)
30a. Other tax family SSN:                                Rachel Park's SSN
30b. Allocation start month:                              01
30c. Allocation stop month:                               06
30d. Premium % allocated to taxpayer:                     50%
30e. SLCSP % allocated to taxpayer:                       50%
30f. APTC % allocated to taxpayer:                        50%

## Part V — Year of marriage                              (not applicable)

## Routing
- Line 26 → Schedule 3 Line 9:                            $0
- Line 29 → Schedule 2 Line 2 (excess APTC repayment):    $1,002

## Required attachments
- [x] Form 8962 attached to Form 1040
- [x] Form 1095-A retained in records (not attached)
- [x] Written 50/50 allocation agreement retained (not filed, but supports Part IV)

## Validation summary
- Math:
  - Line 3 = $58,290 + $0 = $58,290 ✓
  - Line 5 = (58,290 / 15,060) × 100 = 387.05% → 387% ✓
  - Line 7 = 0.06 + (87/100) × 0.025 = 0.08175 → 0.0818 ✓
  - Line 8a = 58,290 × 0.0818 = $4,768.12 → $4,768 ✓
  - Each Jan–Jun row: Col d = max(0, 720 − 397) = $323 ✓
  - Each Jan–Jun row: Col e = min(760, 323) = $323 ✓
  - Line 24 = 6 × $323 = $1,938 ✓
  - Line 25 = 6 × $490 = $2,940 ✓
  - Line 27 = $2,940 − $1,938 = $1,002 ✓
  - Line 29 = min($1,002, $1,625) = $1,002 ✓
- Inputs:
  - 2024 HHS FPL (correct for 2025 return)
  - 48+DC table (Illinois)
  - Family size 1 matches Daniel's Form 1040 (children claimed by Rachel)
  - Allocation 50/50 documented in written agreement; matches Rachel's Part IV
- Sanity:
  - Monthly method correctly chosen (multiple triggers: divorce, mid-year coverage end, shared policy)
  - Part IV percentages sum to 100% across both filers (Daniel 50% + Rachel 50%) ✓
  - Cap did not bind (excess $1,002 < $1,625 cap)
  - Lines 26 and 29 mutually exclusive ✓

## Sources cited in this draft
- IRS Form 8962, Rev. 2025
- IRS Instructions for Form 8962, Rev. 2025
- IRS Pub 974, 2025 edition, Tables 1, 2, 5
- HHS 2024 Poverty Guidelines
- IRC §36B (PTC), §36B(b)(3)(A) (applicable figure), §36B(c)(2)(C) (allocation),
  §36B(d)(3)(C) (FPL determination), §36B(f)(2)(B) (repayment limitation)
- Reg. §1.36B-4(a)(1)(ii) (shared-policy allocation rules and 50/50 default)
- IRA 2022 Section 12001 (ARPA modification extended through 2025)
```

## Why each non-obvious choice

**Why must each ex-spouse file their own Form 8962?** Once Daniel and Rachel divorced, they became two separate tax families. Each tax family that had any month of coverage on a shared marketplace policy must complete its own Form 8962, allocate the shared months, and reconcile its allocated APTC. The 1095-A is issued to the policyholder (Daniel) but the tax obligation follows the tax family.

**Why 50/50?** Daniel and Rachel agreed to it. Reg. §1.36B-4(a)(1)(ii)(A) says any percentage from 0% to 100% is allowed if both ex-spouses agree, as long as the percentages sum to 100% across all tax families on the policy. If they could not agree, the default under Reg. §1.36B-4(a)(1)(ii)(B) is 50/50.

**Why does the percentage need to be the same for premiums, SLCSP, and APTC?** Form 8962 Part IV lets the parties pick separate percentages for each of the three columns, but in practice they almost always pick one number for all three. Picking different percentages for different columns invites disputes and IRS scrutiny.

**Why does Rachel's Part IV mirror Daniel's?** They allocated 50/50, so Rachel's Form 8962 will show 50% allocated to her for the same Jan–Jun months. The two filings must be consistent — IRS systems cross-check both returns. If Daniel claims 50% and Rachel claims 70%, both will get correspondence audits.

**Why is the children's coverage on the Jan–Jun policy not split out separately?** The children were dependents of one parent each post-divorce, but for the Jan–Jun policy period (when they were married and one tax family), the policy covered the whole household. The allocation handles the full policy, not per-person. Rachel claims the children on her 2025 return; her allocation captures their share through the 50% split.

**Why does Daniel use the Single (not MFJ) cap?** Daniel files Single for 2025 (divorced as of June 30; the IRS uses marital status on December 31 for the full year). Pub 974 Table 5 cap for Single at 300%–400% FPL is $1,625. The MFJ cap of $3,250 does not apply because they did not file jointly.

**Why is monthly method required?** Annual method requires the same family composition, same SLCSP, and same eligibility for all 12 months. Daniel's family changed (divorced, children left his tax family) and his coverage ended mid-year. Multiple triggers for monthly.

## What if Daniel were audited?

His audit defense would be:

1. Form 1095-A from healthcare.gov for Jan–Jun joint policy
2. Divorce decree dated June 30, 2025, establishing two separate tax families
3. Written 50/50 allocation agreement signed by both ex-spouses
4. Rachel's matching Form 8962 Part IV showing 50% allocation (filed separately, but cross-references)
5. W-2 supporting $58,200 wages and AGI reconciliation
6. Employer coverage offer letter for July showing transition off marketplace
7. Pub 974 Table 5 reference for the $1,625 single-filer cap
