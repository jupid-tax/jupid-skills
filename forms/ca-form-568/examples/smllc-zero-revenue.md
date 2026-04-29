# Example: First-Year SMLLC With $0 Revenue

The most common newbie surprise. A user formed a single-member LLC in California in mid-2024, never landed a client, ended the year with $0 revenue. They think "no revenue = no tax = no return". California disagrees.

This example walks through the minimum-viable Form 568 for an SMLLC that owes only $800.

## The filer

- **Name**: David Park
- **Business**: Freelance management consulting (planned)
- **Entity**: Single-member LLC formed in California, June 12, 2024
- **California SOS file number**: `202412345678`
- **Federal EIN**: 88-1234567
- **Federal classification**: Disregarded entity (no Form 8832, no Form 2553)
- **First Schedule C / Form 568 year**: Yes
- **Tax year**: 2024 (filing in 2025)

## Inputs gathered

### Revenue
- $0. David never invoiced a client. He has the LLC formed and a website but no income.

### Expenses
- $200 in formation fees (Articles of Organization filed with California SOS)
- $90 California Statement of Information filing fee (Form LLC-12)
- $40 logo design (one-time, contracted to a designer)
- $300 cloud subscriptions (Notion, Adobe Express, Google Workspace) — though these are arguably not deductible if no business activity
- Total: $630 in expenses, all of which David will report on federal Schedule C as startup costs / ordinary expenses

### California-source income
- $0 — David lives in California but had no clients, so no income, period.

### Members
- 1 member: David Park (himself), 100% owner, California resident.

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

David formed the LLC with California SOS → automatic Form 568 filing requirement. SMLLC, disregarded for federal → Form 568 (this skill applies, not 100/100S).

### Step 2 — Pay or confirm $800 annual tax (Form 3522)

LLC formed June 12, 2024. First-year tax due **15th day of 4th month after formation** = October 15, 2024 (4th month after June is October).

> **Important**: David's first year was 2024. AB 85 (the first-year exemption) expired after tax year 2023. David **owes the $800** for 2024 — first year, despite zero revenue.

David did **not** pay Form 3522 in October 2024 (he didn't know). It's now January 2025, two months past due.

Calculate penalty + interest:
- Late payment penalty: 5% of $800 = $40, plus 0.5% × 2 months × $800 = $8 → $48 (R&TC §19132)
- Interest: federal short-term rate + 3%, compounded daily on $800 for 2 months → ≈ $11 (verify current rate at <https://www.ftb.ca.gov/pay/penalties-and-interest/index.html>)

David needs to remit $800 + $48 penalty + $11 interest = **~$859** via Web Pay or Form 3522 voucher immediately.

### Step 3 — Determine if the LLC fee applies

Schedule IW Total Income = $0 (no revenue). Tier: < $250,000. **Fee = $0.**

### Step 4 — Pay or confirm Form 3536

Estimated fee is $0 (because expected fee is $0). Form 3536 is not required.

### Step 5 — Filing deadline

SMLLC → Form 568 due **April 15, 2025** for tax year 2024.

### Step 6-7 — Schedule K, Schedule R

Skip. SMLLC is disregarded; no Schedule K. Single-state California-only; no Schedule R.

### Step 8 — Nonresident members

David is the only member and a California resident. No Form 3832, no Form 592 needed.

### Step 9 — Compute the bottom line

```
Form 568 Line 1 (Total income from Schedule IW): $0
Form 568 Line 2 (LLC fee):                       $0
Form 568 Line 3 (annual LLC tax):              $800
Form 568 Line 4 (nonresident tax):               $0
Form 568 Line 5 (partnership-level tax):         $0
Form 568 Line 6 (Total tax and fee):           $800
Form 568 Line 7 (Form 3522 prepayment):        $800 (paid via Web Pay in Jan 2025)
Form 568 Line 8 (Form 3536 prepayment):          $0
Form 568 Line 11 (Total payments):             $800
Form 568 Line 12 (Tax/fee due or overpayment):   $0
```

Net result: $0 owed with the return (the $800 was already paid via Form 3522, plus $59 in penalty + interest paid separately).

### Step 10 — Validation

- ☑ Math: Line 6 = $0 + $800 + $0 + $0 = $800. Line 11 ($800) − Line 6 ($800) = $0. Pass.
- ☑ Sanity: First-year LLC, no AB-85 exemption (formed 2024). No fee tier issue. No nonresident issues.

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for tax year 2024

## LLC identification
A. SOS file number:                     202412345678
B. Federal EIN:                         88-1234567
C. Principal business activity:         Management consulting
D. Principal product/service:           Strategic and operational consulting (start-up phase)
E. Date business started in CA:         06/12/2024
F. Total assets EOY:                    $0
G. Sales:                               $0
H. Boxes checked:                       [X] Initial return, [X] Single-member LLC
I. Number of members:                   1
J. Federal classification election:     N/A (disregarded entity, default)

## Side 1 — Tax and Fee
Line 1.  Total income (from Sched IW):              $0
Line 2.  LLC fee (from tier table):                 $0
Line 3.  2024 annual LLC tax:                       $800
Line 4.  Nonconsenting nonresident tax:             $0
Line 5.  Partnership-level tax:                     $0
Line 6.  Total tax and fee (2+3+4+5):               $800

## Side 1 — Payments
Line 7.  Form 3522 ($800) prepaid:                  $800
Line 8.  Form 3536 (estimated fee) prepaid:         $0
Line 9.  Withholding (Form 592 / 593):              $0
Line 10. Prior-year overpayment applied:            $0
Line 11. Total payments:                            $800
Line 12. Tax/fee due or overpayment:                $0

## Schedule IW — Income Worksheet
IW Line 1. Gross receipts (CA-source):              $0
IW Line 2. Cost of goods sold (CA):                 $0
IW Line 3. (= Line 1 - Line 2):                     $0
IW Line 4-7. Other CA income:                       $0
Total (= Form 568 Line 1):                          $0

## Member info (1 member, David Park, 100%)
| Name       | SSN          | Ownership | CA resident | Form 3832 |
|------------|--------------|-----------|-------------|-----------|
| David Park | XXX-XX-XXXX  | 100%      | Yes         | N/A       |

## Required attachments
- [x] Form 3522 ($800 paid Jan 2025; verify in FTB account history)
- [ ] Form 3536 (not required; fee = $0)
- [ ] Form 3832 (not applicable; David is a CA resident)
- [ ] Federal Schedule C (David reports $0 revenue + $630 expenses on his 1040)

## Validation summary
- Math: all checks passed
- Sanity:
  - First-year LLC, formed 2024 → AB 85 exemption does NOT apply
  - Late $800 payment incurs ~$59 in penalty + interest (paid separately, not on Form 568)
  - $0 revenue but Form 568 still required
- Next steps:
  - Pay Form 3522 for 2025 ($800) by April 15, 2025
  - If revenue picks up to >$250K in 2025, pay Form 3536 estimated fee by June 15, 2025
  - File 2025 Form 568 by April 15, 2026
  - Decision: if David expects no income in 2025 either, he may want to dissolve (Form LLC-3 + LLC-4/7) to stop the $800

## Sources cited in this draft
- California Form 568, Rev. 2024
- R&TC §17941 (annual LLC tax — applies regardless of revenue)
- R&TC §19132 (late-payment penalty)
- R&TC §19521 (interest)
- AB 85 (Stats. 2020, ch. 8) — first-year exemption expired tax year 2023
```

## Why each non-obvious choice

**Why owe $800 with $0 revenue?** R&TC §17941 imposes the tax on every California LLC for every year, regardless of revenue or activity. There is no minimum-revenue threshold. The only exemption was AB 85 (tax years 2021-2023), which has expired.

**Why the late penalty?** David's first $800 was due October 15, 2024 (4th month after June 12 formation). He missed it and is paying in January 2025. R&TC §19132 imposes 5% + 0.5%/month, max 25%, on unpaid balances.

**Why no LLC fee?** R&TC §17942 only applies if Schedule IW Total Income ≥ $250,000. David's was $0. Even at $1, the tier is $0 fee until $250K.

**Why is Schedule R not required?** David has no out-of-state activity. Schedule R is for multi-state apportionment.

**What if David wants to dissolve to stop the $800 going forward?** He must file Form LLC-3 (Dissolution) and Form LLC-4/7 (Cancellation) with California SOS, plus mark "Final Return" on his next Form 568. Until both happen, the $800 keeps accruing.

**What if David had operated under his own name as a sole proprietor instead?** No Form 568, no $800, just federal Schedule C. The LLC adds $800/year in California costs in exchange for limited-liability protection. For a $0-revenue first year, the LLC is "expensive" relative to the protection it provides — but reasonable people decide differently.

## Audit defense (if it came to that)

David's Form 568 audit defense is straightforward:
1. SOS confirms LLC formation date June 12, 2024
2. Bank statements show $0 in business deposits
3. Federal Schedule C shows $0 revenue and $630 in start-up expenses
4. No nonresident members; no withholding obligations

This is the simplest possible Form 568. The mistake to avoid is not filing at all — that triggers the $18/month/member penalty plus the $800 owed plus interest.
