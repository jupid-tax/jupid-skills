# Example: 67-Year-Old Misses Inherited IRA RMD by Six Months

A complete walkthrough of Form 5329 Part IX with a waiver request. The
user inherited an IRA, did not realize the RMD requirement, and missed
the deadline. Demonstrates the SECURE 2.0 25%/10% rates, the waiver
narrative, and the reasonable-cause statement.

## The filer

- **Name**: Patricia Ng
- **Age**: 67 (DOB 09/22/1958)
- **Tax year**: 2025 (filing in 2026)
- **Account**: Inherited Traditional IRA at Vanguard, account #...4892
- **Decedent**: Patricia's mother, Linda Ng (DOD 03/14/2024)

## What happened

Patricia's mother passed away on 03/14/2024. Her mother was 79 and had
been taking RMDs from a traditional IRA worth $230,000. Patricia, as a
non-spouse beneficiary, inherited the account in May 2024 after probate.

**The two RMD obligations Patricia faced**:

1. **Year-of-death RMD for 2024**: her mother had not yet taken her 2024
   RMD before passing. Under IRC §401(a)(9)(B), the unsatisfied RMD must
   be taken by the beneficiary by 12/31 of the year of death. Patricia
   was unaware of this requirement.

2. **Beneficiary RMDs starting 2025**: under SECURE Act (deaths after
   12/31/2019), most non-spouse beneficiaries are subject to a 10-year
   rule — full distribution by the end of the 10th year. The 2024 final
   regulations clarified that for accounts where the decedent had
   already begun RMDs, annual RMDs within the 10 years are also
   required (Single Life Table).

Patricia satisfied #1 (the 2024 year-of-death RMD) by taking $9,500 in
December 2024 after a CPA flagged it. But for 2025, she was unaware of
the annual RMD requirement and only took $1,200 (an ad hoc withdrawal
to cover a home repair).

## Computing the 2025 RMD

- 12/31/2024 inherited IRA balance: $216,400
- Applicable table: Single Life Table (Patricia is a non-eligible
  designated beneficiary subject to annual RMDs within the 10-year
  window)
- Patricia's age in 2025: 67
- Single Life Table factor at age 67: 19.4 (verify against current Pub
  590-B Appendix B; tables updated effective 2022)

```
RMD = $216,400 ÷ 19.4 = $11,155
```

Patricia took $1,200. The shortfall is $11,155 − $1,200 = $9,955.

## The corrective action and waiver decision

In February 2026, while preparing her 2025 tax return, Patricia's CPA
identified the missed RMD. They acted immediately:

- 02/12/2026: Patricia contacted Vanguard and requested a distribution
  of $9,955 to satisfy the missed 2025 RMD
- 02/14/2026: Vanguard processed the distribution
- 02/15/2026: Patricia set up automatic annual RMD distributions for
  future years through Vanguard's automated RMD service

With the corrective action in hand, Patricia is requesting a waiver of
the 25% additional tax under IRC §4974(d).

The 10% SECURE 2.0 reduction also applies: Patricia took the corrective
distribution well within 2 years of the end of 2025. So if the waiver is
denied, the fallback rate is 10%, not 25%.

## The completed Form 5329 draft

```markdown
# Form 5329 — DRAFT for tax year 2025

## Header
Name: Patricia Ng
SSN: XXX-XX-XXXX
Filing standalone? No (attaching to Form 1040)

## Part I — Additional Tax on Early Distributions
N/A — Patricia is over 59½

## Parts II-VIII
N/A — no other tax-favored account events for the year

## Part IX — Excess Accumulation (Missed RMD)
52. Required minimum distribution:                   $11,155
    (Inherited Traditional IRA, Vanguard #...4892;
     12/31/2024 balance $216,400 ÷ 19.4 Single Life factor)
53. Amount actually distributed in 2025:             $1,200
54. Shortfall (Line 52 − Line 53):                   $9,955
55. Additional tax:                                  $0
    [Waiver requested — see attached statement
     "Form 5329 Line 54 Waiver Request"]

## Total additional tax flowing to Schedule 2 Line 8: $0
(pending IRS waiver decision; if denied, fallback rate is 10%
under SECURE 2.0 §302 corrected-within-2-years reduction =
$9,955 × 10% = $996)

## Required attachments
- [x] Waiver-request statement (see below)
- [x] Form 1040

## Validation summary
- Math: all checks passed
- Sanity:
  - Single Life Table factor verified against IRS Pub 590-B Appendix B
    Table I (Single Life Expectancy)
  - Inherited-IRA RMD requirement is annual under SECURE Act 10-year rule
    when decedent was already in RMD status; verified against Treas. Reg.
    §1.401(a)(9)-5 (final regs issued 7/2024)
  - Corrective distribution of $9,955 processed 02/14/2026, well within
    SECURE 2.0 2-year window
  - Automatic RMD distributions established for future years
- Next steps:
  - The $9,955 corrective distribution will appear on Patricia's 2026
    Form 1099-R and is taxable on her 2026 Form 1040 (year of receipt,
    not year it should have been taken)
  - $1,200 distributed in 2025 is reported on 2025 Form 1040 Line 4b
    as taxable
  - Future-year RMDs will be on autopilot via Vanguard's automated
    RMD program
  - If IRS denies the waiver: Patricia owes $996 (10% × $9,955) plus
    interest; she will receive a CP letter and can pay or appeal

## Sources cited in this draft
- IRS Form 5329, Rev. 2025
- IRS Instructions for Form 5329, Rev. 2025
- IRC §401(a)(9) — RMD rules
- IRC §4974 — excise tax on excess accumulation
- IRC §4974(d) — waiver for reasonable cause
- IRC §4974(e) — corrected-within-2-years 10% rate (SECURE 2.0 §302)
- SECURE Act of 2019 §401 — 10-year rule for non-spouse beneficiaries
- SECURE 2.0 Act of 2022 §302 — RMD penalty reduction
- IRS Pub 590-B, Appendix B Table I (Single Life Expectancy)
- Treasury Regulation §1.401(a)(9)-5 (final regs, July 2024)
```

## The waiver-request statement (attached to Form 5329)

```markdown
# Form 5329 Line 54 — Waiver Request Statement

Filer: Patricia Ng
SSN: XXX-XX-XXXX
Tax Year: 2025

## Account information

Account: Vanguard Inherited Traditional IRA, account #...4892
Decedent: Linda Ng (mother), DOD 03/14/2024
Required minimum distribution for 2025: $11,155
Distribution actually taken in 2025: $1,200
Shortfall: $9,955

## Reasonable cause

I inherited this Traditional IRA from my mother, who passed away on
03/14/2024. As a non-spouse beneficiary, I was unaware that the SECURE
Act's 10-year distribution rule still required annual RMDs in my case
because my mother had already begun her RMDs before her death (she was
79 and in RMD status).

In December 2024, my CPA identified the unsatisfied 2024 year-of-death
RMD, and I took that distribution ($9,500) before 12/31/2024.

In 2025, I took an ad hoc distribution of $1,200 in October 2025 to
cover a home repair, but I did not realize this was below the annual
RMD requirement of $11,155 for 2025. The annual-RMD-within-the-10-year
rule was clarified by Treasury Regulation §1.401(a)(9)-5 (final
regulations issued July 2024), and I did not learn of its application
to my situation until my CPA reviewed my 2025 tax preparation in
February 2026.

## Steps to remedy

I have taken the following corrective actions:

1. On 02/12/2026, I contacted Vanguard and requested a corrective
   distribution of $9,955 to satisfy the missed 2025 RMD. The
   distribution was processed on 02/14/2026.

2. On 02/15/2026, I enrolled in Vanguard's Automated RMD service for
   the inherited IRA. This service will automatically distribute the
   correct annual RMD amount each year, computed using the Single Life
   Table factor for my age, ensuring no future shortfall.

3. I have engaged my CPA to review my retirement account activity
   annually, including verification that all RMDs are satisfied.

The corrective distribution was taken on 02/14/2026, which is within
2 years of the end of the year the RMD was due (12/31/2025). Under IRC
§4974(e) (added by SECURE 2.0 Act §302), if the additional tax is
imposed, it would be at the 10% rate rather than 25%. I am requesting
a full waiver under §4974(d) given the reasonable-cause circumstances
described above.

## Request

I respectfully request that the IRS waive the additional tax under IRC
§4974(d). I have entered $0 on Line 55 of Form 5329 pending review of
this waiver request.

Filer signature: _______________________
Date: __________
```

## Why each non-obvious choice

**Why request a waiver instead of just paying the 10% reduced rate?** A
waiver costs Patricia nothing to request — a one-page statement. The IRS
approves these liberally when reasonable cause is documented and
corrective action has been taken. Both prongs are clearly met here.
Worst case (denial): she pays the 10% = $996 plus interest. Best case
(approval, the common outcome): she pays $0.

**Why is the corrective distribution dated 02/14/2026 reportable on the
2026 Form 1040, not 2025?** The 1099-R is issued in the year the
distribution actually occurs. Patricia received the $9,955 in 2026, so
it's 2026 income. The fact that it was "for" the missed 2025 RMD doesn't
change the timing of taxation.

**Why did the CPA find this in February 2026 and not earlier?** This is
realistic. Inherited-IRA RMD complexity (especially the year-of-death
RMD and the annual-RMD-within-10-year-rule clarified in 2024 final regs)
catches many beneficiaries. The CPA flagged it during 2025 tax prep —
the typical discovery moment.

**Why use Single Life Table (factor 19.4) and not Uniform Lifetime
Table?** Single Life Table applies to beneficiaries of inherited
accounts. Uniform Lifetime applies to living owners of their own
accounts. Patricia inherited from her mother — Single Life is correct.

**Why did Patricia's mother's age (79 at death) matter?** Because she had
already begun taking RMDs (RMDs start at the applicable age — 73 for
post-2022 starters; she had been taking them for years). When the
decedent had already begun RMDs, the post-SECURE-Act 10-year rule still
requires annual RMDs within the 10 years (per the 2024 final
regulations). If the decedent had died *before* RMD age, only the
10-year-empty rule would apply and Patricia could have skipped years.

**What if Vanguard had been slow and the corrective distribution didn't
happen until April 2026 (during return preparation)?** Same waiver
analysis. The 2-year SECURE 2.0 window runs to 12/31/2027 for a 2025
miss; February-April 2026 is well within. The waiver still applies.

**What records should Patricia retain?**

1. Death certificate of Linda Ng
2. Vanguard inherited-IRA account opening documents
3. Vanguard 2024 1099-R for the year-of-death RMD
4. Vanguard 2025 1099-R for the $1,200 ad hoc distribution
5. Vanguard 2026 1099-R (when received) for the $9,955 corrective
   distribution
6. Vanguard confirmation of automated RMD service enrollment (02/15/2026)
7. CPA correspondence flagging the issue (02/2026)
8. Copy of the waiver-request statement and the filed Form 5329
9. IRS response (CP letter) when received — file it with the return

If the waiver is approved: Patricia is done. If denied: she pays the
10% per the SECURE 2.0 reduction and may appeal if she has further
reasonable cause to argue.
