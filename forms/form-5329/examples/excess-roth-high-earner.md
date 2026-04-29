# Example: High-Earner Over-Contributes to Roth IRA

A complete walkthrough of Form 5329 Part IV for a high-earning filer who
contributed to a Roth IRA in January, then crossed the MAGI phaseout by
year-end. Demonstrates the recharacterization-vs-correction-vs-pay-the-6%
decision and how to compute the 6% tax.

## The filer

- **Name**: Marcus Chen
- **Age**: 38 (DOB 11/02/1987)
- **Filing status**: Single
- **Tax year**: 2025 (filing in 2026)
- **Account**: Roth IRA at Fidelity, opened 2018

## What happened

In January 2025, Marcus contributed the full $7,000 Roth IRA limit. He's
a senior software engineer who normally earns $145,000 base plus a
~$25,000 bonus, putting him in the Roth phaseout but historically below
the upper limit (single phaseout was $146,000-$161,000 for 2024).

For 2025, the phaseout under Notice 2024-80 is $150,000-$165,000 single.

In Q4 2025, Marcus's company paid out an unexpectedly large
performance bonus ($60,000) and a stock-vesting event added $35,000 in
ordinary income. His final 2025 MAGI is **$208,000** — fully above the
$165,000 upper phaseout for single filers.

His allowed Roth contribution: **$0**.
His actual contribution: **$7,000**.
His excess: **$7,000**.

## Three correction options

Marcus discovers the excess in March 2026 while preparing his return.
He has three viable paths:

### Option A — Withdraw excess + earnings before October 15, 2026

Marcus contacts Fidelity and requests a "return of excess contribution."
Fidelity's NIA calculation:

- Roth IRA value just before the 2025 contribution: $112,400
- Roth IRA value at withdrawal request: $124,800
- 2025 Roth contribution: $7,000

NIA formula (per Treas. Reg. §1.408-11):
```
NIA = $7,000 × (($124,800 − $112,400) / $112,400)
    = $7,000 × ($12,400 / $112,400)
    = $7,000 × 0.1103
    = $772
```

Fidelity distributes $7,000 + $772 = $7,772.

Tax effects (in 2025, the year of the original contribution):
- $7,000 principal: tax-free, penalty-free (Roth basis)
- $772 earnings: taxable on Marcus's 2025 Form 1040 Line 4b
- Marcus is 38 (under 59½): the $772 earnings are subject to Form 5329
  Part I 10% additional tax = $77

**No Part IV tax**. Total cost: ~$170 in income tax on the earnings + $77
penalty = ~$247.

### Option B — Recharacterize to Traditional IRA before October 15, 2026

Marcus contacts Fidelity and requests recharacterization. The $7,000 +
NIA ($772) moves to a traditional IRA. The contribution is treated as
having been made to the traditional IRA from the start.

Tax effects:
- Marcus has an active 401(k) at work and is a high earner. The
  traditional IRA deduction phaseout for an active participant in an
  employer plan, single filer, in 2025 is $77,000-$87,000 MAGI (verify
  against Notice 2024-80). Marcus's $208,000 MAGI is well above. So
  the recharacterized $7,000 is a **nondeductible** traditional
  contribution.
- $7,000 nondeductible basis is added to Form 8606 (nondeductible
  contributions tracking).
- $772 earnings stay in the traditional IRA (not currently taxed).

**No 5329 tax**. But Marcus now has $7,000 of basis in his traditional
IRA, which complicates any future Roth conversion (pro-rata rule across
all traditional IRAs).

### Option C — Pay the 6% Part IV tax

Marcus does nothing. The $7,000 stays in the Roth as excess.

Tax effect:
- 6% × min($7,000, account value 12/31) = 6% × $7,000 = **$420**

This recurs every year the excess remains, until corrected.

## The decision

Marcus chooses **Option A** (withdraw excess + earnings) for these
reasons:

1. **Cheapest option in dollars** — ~$247 vs. ~$420 for the 6% (and the
   6% recurs annually until corrected).
2. **No basis tracking complexity** — Option B would add $7,000 of basis
   to his traditional IRA, requiring Form 8606 every year and
   complicating any future Roth conversion strategy via the pro-rata
   rule.
3. **Marcus expects 2026 income to be similarly high** — meaning
   carrying the excess forward (Option C variant) doesn't have a clear
   exit. He might be above the phaseout in 2026 too.
4. **Fidelity's return-of-excess process is fast** — typically 5-7
   business days. Plenty of time before October 15.

## The completed Form 5329 draft (Option A path)

Since Marcus withdrew the excess + NIA before the deadline, the 6% Part
IV tax is **eliminated**. Form 5329 still has Part I activity because
the $772 earnings were a non-qualified Roth distribution (under 59½).

```markdown
# Form 5329 — DRAFT for tax year 2025

## Header
Name: Marcus Chen
SSN: XXX-XX-XXXX
Filing standalone? No (attaching to Form 1040)

## Part I — Additional Tax on Early Distributions
1.  Early distributions includible in income:        $772
    ($772 NIA on returned excess; Box 7 codes 8/P from Fidelity 1099-R)
2.  Exception amount + code:                         $0
    (No exception applies; this is a return-of-excess earnings,
     not a medical / education / homebuyer event)
3.  Amount subject to additional tax (Line 1 − 2):   $772
4.  Additional tax (Line 3 × 10%):                   $77

## Parts II-III, V-IX
N/A

## Part IV — Excess Contributions to Roth IRAs
18. Prior-year excess from prior 5329 Line 24:        $0
19. Current-year excess Roth contribution:            $7,000
20. (Adjustments — distributions of excess)
    Returned excess contribution + NIA before deadline: $7,000
21. Adjusted current-year excess after distribution:  $0
24. Total excess remaining at year-end:               $0
25. Additional tax (6% × min(Line 24, value 12/31)):  $0

## Total additional tax flowing to Schedule 2 Line 8: $77

## Required attachments
- [ ] Form 1040 (5329 attaches)
- [ ] Form 8606 N/A (Marcus chose Option A, not recharacterization)
- [x] Fidelity 1099-R for the return-of-excess (will arrive January
      2027 for the 2026 distribution, OR may be issued for 2025 if
      processed in 2025; verify with Fidelity timing)

## Validation summary
- Math: all checks passed
- Sanity:
  - 2025 single Roth phaseout: $150,000-$165,000 MAGI per Notice 2024-80
  - Marcus's MAGI $208,000 > $165,000 → contribution fully ineligible
  - Excess $7,000 withdrawn with NIA $772 before October 15, 2026
    deadline → no Part IV 6% tax
  - $772 earnings reported as taxable on Form 1040 Line 4b
  - $77 Part I penalty applies because Marcus is 38 (under 59½)
- Next steps:
  - File Form 1040 reporting $772 taxable on Line 4b
  - Schedule 2 Line 8 picks up the $77 Form 5329 Part I tax
  - For 2026: do NOT contribute to Roth IRA early in the year unless
    Marcus is confident MAGI will be below $150,000. If unsure, delay
    contribution to December when MAGI is more visible.
  - Consider Backdoor Roth strategy: nondeductible traditional IRA
    contribution → conversion to Roth. Requires careful pro-rata
    rule analysis if Marcus has any pre-tax traditional IRA balance.

## Sources cited in this draft
- IRS Form 5329, Rev. 2025
- IRS Instructions for Form 5329, Rev. 2025
- IRC §408A(c)(3) — Roth IRA MAGI phaseout
- IRC §4973 — excess contributions excise tax
- IRC §72(t) — early distribution additional tax
- IRC §408(d)(4) — return of excess contribution before due date
- Treas. Reg. §1.408-11 — net income attributable (NIA) computation
- Notice 2024-80 — 2025 Roth IRA phaseout limits ($150K-$165K single)
- IRS Pub 590-A — contributions to IRAs (excess contribution correction)
```

## Why each non-obvious choice

**Why is there still Part I tax even after the excess was withdrawn?**
Return-of-excess preserves the *principal* tax-and-penalty-free
character (it was Roth basis), but the *earnings* (NIA) on the excess
are taxable in the year of the original contribution, and if the user
is under 59½, the earnings are also subject to the 10% penalty under
§72(t). This is one of the surprise costs of Option A.

**Why didn't the medical/disability/etc. exception apply to the $772?**
The §72(t) exceptions don't apply to NIA on returned excess contributions
in the same way they apply to other early distributions. The NIA is
deemed to be a distribution attributable to the year of contribution and
is subject to the 10% additional tax without exception (per IRS Pub
590-A and the regulations). Some practitioners argue an exception could
apply with sufficient documentation, but the conservative approach is
no exception.

**Why is recharacterization (Option B) inferior here?** It would create
$7,000 of nondeductible basis in Marcus's traditional IRA. If Marcus
ever wanted to do a Roth conversion (a common move for high-earners), the
pro-rata rule would distribute the basis across his entire pre-tax
traditional IRA balance. If he has $50,000 in pre-tax traditional IRAs
elsewhere, only $7,000/$57,000 = 12% of any conversion would be tax-
free. The basis becomes a tax-deferred asset rather than a useful one.
Option A keeps Marcus's traditional IRA clean.

**Why didn't Marcus contribute via the "backdoor Roth" strategy in the
first place?** Hindsight question. A high-earner expecting to be above
the Roth phaseout should consider:
1. Skip direct Roth contributions entirely
2. Make a $7,000 nondeductible contribution to a traditional IRA
3. Convert that $7,000 to Roth (the conversion has no income limit)
4. Pay tax only on any growth between contribution and conversion (kept
   minimal by converting immediately)

This works cleanly only if Marcus has *no* pre-tax traditional IRA
balance (the pro-rata rule applies to all traditional IRAs in
aggregate). Marcus would need to verify this before next year's
contribution.

**What if Marcus's bonus had been smaller and his MAGI ended up at
$155,000 (within the phaseout, partial contribution allowed)?** The
allowed contribution at $155,000 MAGI in the $150K-$165K phaseout is
linearly reduced. Calculation:
```
Reduction factor = ($155,000 − $150,000) / ($165,000 − $150,000) = 0.333
Allowed contribution = $7,000 × (1 − 0.333) = $4,669
Excess = $7,000 − $4,669 = $2,331
```
He'd correct only the $2,331 excess, not the full $7,000.

**What records should Marcus retain?**

1. Fidelity statements showing the original $7,000 contribution in
   January 2025
2. Fidelity statement of the return-of-excess (showing $7,000 + $772)
3. Fidelity 1099-R for the return-of-excess (when issued)
4. Marcus's 2025 final pay stubs and W-2 supporting MAGI calculation
5. Marcus's 2025 1099-B and brokerage statements supporting MAGI
6. NIA computation worksheet from Fidelity
7. Copy of the filed Form 5329 with Part I and Part IV
