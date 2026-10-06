# Example: First-Year SMLLC With $0 Revenue

The most common newbie surprise. A user formed a single-member LLC in California in mid-2025, never landed a client, ended the year with $0 revenue. They think "no revenue = no tax = no return". California disagrees.

This example walks through the minimum-viable 2025 Form 568 for an SMLLC that owes only $800, paid late. Line numbers are from the 2025 Form 568; math checked in Python.

## The filer

- **Name**: David Park
- **Business**: Freelance management consulting (planned)
- **Entity**: Single-member LLC formed in California; Articles of Organization filed with the SOS June 12, 2025
- **California SOS file number**: `202512345678` (placeholder)
- **FEIN**: 88-1234567 (placeholder)
- **Federal classification**: Disregarded entity (no Form 8832, no Form 2553); owner is an individual
- **First Schedule C / Form 568 year**: Yes
- **Taxable year**: 2025 (filing in 2026)

## Inputs gathered

### Revenue
- $0. David never invoiced a client. He has the LLC formed and a website but no income.

### Expenses
- $70 Articles of Organization filing fee (SOS Form LLC-1)
- $20 Statement of Information filing fee (SOS Form LLC-12)
- $40 logo design (one-time, contracted to a designer)
- $300 cloud subscriptions (Notion, Adobe Express, Google Workspace) — whether these are deductible or start-up costs before the business begins is a federal Schedule C question
- Total: $430, reported on David's federal Schedule C, not on Form 568

SOS fees: California Secretary of State, LLC forms and fees page (LLC-1 $70, LLC-12 $20).

### California-source income
- $0 — David lives in California but had no clients, so no income, period.

### Members
- 1 member: David Park (himself), 100% owner, California resident.

## Step-by-step workflow execution

### Step 1 — Confirm California nexus and entity classification

David formed the LLC with the California SOS → Form 568 filing requirement (2025 booklet, General Information D). SMLLC, disregarded for federal → Form 568 (this skill applies, not 100/100S).

### Step 2 — Pay or confirm $800 annual tax (FTB 3522)

The first taxable year began June 12, 2025, when the LLC filed with the SOS. The first $800 is due by the 15th day of the 4th month of that taxable year: June is month 1, so the due date is **September 15, 2025** (same pattern as the FTB's example: formed June 18 → due September 15).

> **Important**: David's first taxable year began in 2025. AB 85 covered only first taxable years 2021–2023, and the $400 first-year rate (SB 122) starts with first taxable years beginning in 2027. David **owes the full $800** for 2025 — first year, despite zero revenue.

David did **not** pay in September 2025 (he didn't know). He pays the $800 with Web Pay on **January 14, 2026**, 121 days late.

Penalty and interest:
- Late-payment penalty (R&TC §19132): 5% plus 0.5% for each month or part of a month unpaid. September 15 → January 14 is 4 months or part of a month → 5% + 4 × 0.5% = 7% × $800 = **$56**
- Interest (R&TC §19521): FTB rate 7% for July 1, 2025 – June 30, 2026, compounded daily on $800 for 121 days → **$18.78**

Penalty plus interest ≈ **$75** (rounded to whole dollars for line 20). The FTB computes the final figure; if its notice differs, pay the notice.

### Step 3 — Determine if the LLC fee applies

Schedule IW line 17 = $0 (no revenue). Tier: < $250,000. **Fee = $0.**

### Step 4 — Pay or confirm FTB 3536

Expected fee is $0, so no FTB 3536 ("If the LLC does not owe a fee, do not complete or mail form FTB 3536", 2025 FTB 3536 instructions).

### Step 5 — Filing deadline

SMLLC owned by an individual → 15th day of the 4th month after the close of the owner's taxable year → Form 568 due **April 15, 2026**; automatic 6-month extension to October 15, 2026.

### Step 6-7 — Schedule K, Schedule IW sourcing, Schedule R

Schedule B and Schedule K not required (far below the $3,000,000 test). Schedule IW is still required. Single-state California-only; no Schedule R.

### Step 8 — Nonresident members

David is the only member and a California resident. He signs the Single Member LLC Information and Consent on Side 3. No FTB 3832, no Schedule T, no withholding.

### Step 9 — Compute the bottom line

```
Line 1  (Total income from Schedule IW):          $0
Line 2  (LLC fee):                                $0
Line 3  (2025 annual LLC tax):                  $800
Line 4  (PTE elective tax):                       $0
Line 5  (Nonconsenting nonresident tax):          $0
Line 6  (Partnership level tax):              (blank)
Line 7  (Total tax and fee):                    $800
Line 8  (Paid with FTB 3537 / 3522 / 3536):     $800 (Web Pay, Jan 14, 2026)
Line 12 (Total payments):                       $800
Line 14 (Payments balance):                     $800
Line 16 (Tax and fee due):                        $0
Line 17 (Overpayment):                            $0
Line 20 (Penalties and interest):                $75
Line 21 (Total amount due):                      $75
```

Net result: the $800 is covered; $75 of penalty and interest is due with the return (or on the FTB's notice).

### Step 10 — Validation

- ☑ Math: Line 7 = $0 + $800 + $0 + $0 + $0 = $800. Line 12 = $800. Line 16 = $800 − $800 = $0. Line 21 = $0 + $0 + $0 + $75 − $0 = $75. Pass.
- ☑ Sanity: First taxable year 2025, no AB 85 exemption, $400 rule not yet in effect. No fee tier issue. No nonresident issues.
- ⚠ Late $800: penalty and interest computed; FTB may adjust.

### Step 11 — Deliverable

```markdown
# California Form 568 — DRAFT for taxable year 2025

## Identification (Side 1)
A. SOS file number:                     202512345678
B. FEIN:                                88-1234567
E. Accounting method:                   Cash
F. Date business started in CA:         06/12/2025
G. Total assets EOY:                    $0
H. Boxes checked:                       [X] Initial return
I(1)–I(3):                              No / No / No

## Side 1 — Tax, fee, and payments
Line 1.  Total income from Schedule IW:          $0
Line 2.  LLC fee:                                $0
Line 3.  Annual LLC tax:                         $800
Line 4.  PTE elective tax:                       $0
Line 5.  Nonconsenting nonresident tax:          $0
Line 6.  Partnership level tax:                  (blank)
Line 7.  Total tax and fee:                      $800
Line 8.  Paid with FTB 3537 / 3522 / 3536:       $800
Line 9.  PTE elective tax payments:              $0
Line 10. Prior-year overpayment credited:        $0
Line 11. Withholding:                            $0
Line 12. Total payments:                         $800
Line 13. Use tax:                                $0
Line 14. Payments balance:                       $800
Line 15. Use tax balance:                        $0
Line 16. Tax and fee due:                        $0
Line 17. Overpayment:                            $0
Line 18. Credited to 2026:                       $0
Line 19. Refund:                                 $0
Line 20. Penalties and interest:                 $75
Line 21. Total amount due:                       $75

## Questions (Side 2–3)
J. PBA code / activity / product:   541600 / Management consulting / Strategic and operational consulting
K. Maximum members:                 1
M(1) Schedule R:                    No     M(2) Registered with no CA-source income: Yes
P(1)/P(2) nonresident members:      No / No
U(1) Disregarded:                   Yes    U(2): No    U(3): No
GG(2) First year doing business in CA: Yes
SMLLC owner type:                   Individual (David Park), consent signed

## Schedule IW — every line
1a $0 · 1b $0 · 2a $0 · 2b $0 · 3a $0 · 3b $0 · 3c $0 · 4 $0 · 5 $0 · 6 $0 · 7 $0
8a $0 · 8b $0 · 8c $0 · 9a $0 · 9b $0 · 9c $0 · 10 $0 · 11 $0 · 12 $0 · 13 $0 · 14 $0 · 15 $0 · 16 $0
17 $0 → Side 1, line 1

## Payments and attachments
- [x] 2025 FTB 3522 ($800) — paid by Web Pay January 14, 2026 (due September 15, 2025)
- [ ] FTB 3536 — not required; fee = $0
- [ ] FTB 3832 — not applicable (single-member LLC; consent signed on Side 3)
- [ ] Federal Schedule C — on David's own Form 1040 ($0 revenue, $430 expenses), not attached to Form 568

## Validation summary
- Math: all checks passed
- Sanity:
  - First taxable year 2025 → full $800; AB 85 ended with 2023 first years; $400 first-year rate starts with 2027 first years
  - Late $800 → $56 penalty + $18.78 interest ≈ $75 on line 20
  - $0 revenue but Form 568 still required
- Next steps:
  - 2026 annual tax ($800, 2026 FTB 3522 or Web Pay) due April 15, 2026
  - If 2026 income could reach $250,000, pay the FTB 3536 estimate by June 15, 2026
  - File 2025 Form 568 by April 15, 2026 (or October 15, 2026 on extension)
  - If David will not use the LLC, he can cancel it with the SOS (Form LLC-3 and LLC-4/7, within 12 months of a timely final return) to stop the $800

## Sources cited in this draft
- 2025 Form 568 and 2025 Form 568 Booklet (General Information D, E, F, G, Q; Schedule IW)
- 2025 FTB 3522 and 3536 instructions; FTB LLC page (first-year due-date example)
- R&TC §17941 (annual LLC tax — applies regardless of revenue)
- R&TC §19132 (late-payment penalty); R&TC §19521 and FTB interest rate table (7%)
- AB 85 (Stats. 2020, ch. 8) — first-year exemption for 2021–2023 first years only; SB 122 — $400 first-year tax for 2027–2029
```

## Why each non-obvious choice

**Why owe $800 with $0 revenue?** R&TC §17941 imposes the tax on every LLC organized, registered, or doing business in California for every taxable year until it is cancelled, regardless of revenue or activity. There is no minimum-revenue threshold. AB 85 (first taxable years 2021–2023) has ended.

**Why September 15, not October 15?** The 15th day of the 4th month counts the month the taxable year begins as month 1 (June, July, August, September). The FTB's own example: formed June 18 → due September 15.

**Why the late penalty?** David paid on January 14, 2026, 4 months or part of a month after September 15, 2025. R&TC §19132: 5% + 0.5% per month or part of a month, up to 40 months, max 25%.

**Why no LLC fee?** R&TC §17942 applies only once Schedule IW line 17 reaches $250,000. David's was $0.

**Why is Schedule R not required?** David has no out-of-state activity. Schedule R is for multi-state apportionment.

**Why answer M(2) "Yes"?** M(2) asks, if Schedule R is not used, whether the LLC was registered in California without earning any California-source income during the year. That fits David. Whether to also write "SB 1106 Filing" at the top of Side 1 (booklet, General Information D) is unclear for an LLC organized in California, which is doing business by definition (R&TC §23101(b)(1)); flag it for the user rather than deciding.

**What if David wants to stop the $800 going forward?** He files a timely final Form 568 (Item H(2)), stops doing business in California, and files Form LLC-4/7 (Certificate of Cancellation) plus Form LLC-3 (Certificate of Dissolution) with the SOS within 12 months of that final return (2025 booklet, General Information Q). Had he cancelled within 12 months of organizing without ever doing business, the short form (LLC-4/8) would have avoided the first-year tax.

**What if David had operated under his own name as a sole proprietor instead?** No Form 568, no $800, just federal Schedule C. The LLC adds $800/year in California costs in exchange for the liability protection; whether that trade is worth it is a decision for David and his advisers, not this skill.

## Audit defense (if it came to that)

David's Form 568 audit defense is straightforward:
1. SOS confirms the Articles of Organization filing date, June 12, 2025
2. Bank statements show $0 in business deposits
3. Federal Schedule C shows $0 revenue and $430 in expenses
4. No nonresident members; no withholding obligations

This is the simplest possible Form 568. The mistake to avoid is not filing at all — that triggers the $18 per member per month penalty (R&TC §19172) plus the $800 owed plus interest.
