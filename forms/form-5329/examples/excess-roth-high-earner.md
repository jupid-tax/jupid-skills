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
~$10,000 bonus, putting him in the Roth phaseout but historically below
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

NIA formula (per Treas. Reg. §1.408-11; the adjusted opening balance
includes the contribution being returned):
```
Adjusted opening balance = $112,400 + $7,000 = $119,400
Adjusted closing balance = $124,800
NIA = $7,000 × (($124,800 − $119,400) / $119,400)
    = $7,000 × ($5,400 / $119,400)
    = $7,000 × 0.04523
    = $316.58 → $317
```

Fidelity distributes $7,000 + $317 = $7,317.

Tax effects (in 2025, the year of the original contribution, Pub. 590-A):
- $7,000 principal: tax-free, penalty-free (Roth basis)
- $317 earnings: taxable on Marcus's 2025 Form 1040 Line 4b
- Marcus is 38 (under 59½): the $317 goes on Form 5329 Part I Line 1 and
  Line 2 with exception 21, so the 10% additional tax is $0 (corrective
  distributions on or after December 29, 2022; 2025 Instructions for Form
  5329, Line 23)

**No Part IV tax**. Total cost: about $76 in income tax on the earnings
($317 × 24%; 2025 taxable income $208,000 − $15,750 = $192,250 is in the
24% bracket, Rev. Proc. 2024-40).

### Option B — Recharacterize to Traditional IRA before October 15, 2026

Marcus contacts Fidelity and requests recharacterization. The $7,000 +
NIA ($317) moves to a traditional IRA. The contribution is treated as
having been made to the traditional IRA from the start.

Tax effects:
- Marcus has an active 401(k) at work and is a high earner. The
  traditional IRA deduction phaseout for an active participant in an
  employer plan, single filer, in 2025 is $79,000-$89,000 MAGI (Notice
  2024-80). Marcus's $208,000 MAGI is well above. So
  the recharacterized $7,000 is a **nondeductible** traditional
  contribution.
- $7,000 nondeductible basis is added to Form 8606 (nondeductible
  contributions tracking).
- $317 earnings stay in the traditional IRA (not currently taxed).

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

1. **Cheapest option in dollars** — ~$76 vs. $420 for the 6% (and the
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

Since Marcus withdrew the excess + NIA before the deadline, the excess is
treated as not contributed, so Part IV is not needed. Form 5329 still has
Part I activity because the instructions route the $317 earnings (under
59½) to Line 1 and Line 2 with exception 21.

```markdown
# Form 5329 — DRAFT for tax year 2025

## Header
Name: Marcus Chen
SSN: XXX-XX-XXXX
Filing standalone? No (attaching to Form 1040)

## Part I — Additional Tax on Early Distributions
1.  Early distributions includible in income:        $317
    ($317 NIA on returned excess; Fidelity 1099-R box 7 codes P and J
     if paid in 2026 for 2025, or 8 and J if paid in 2025)
2.  Exception amount + number:                       $317 (21)
    (Corrective distribution of income on an excess contribution
     made by the due date including extensions)
3.  Amount subject to additional tax (Line 1 − 2):   $0
4.  Additional tax (Line 3 × 10%):                   $0

## Parts II-IX
N/A (Part IV: no prior-year excess, and the 2025 excess was withdrawn
with earnings by the due date, so Line 23 = $0)

## Total additional tax flowing to Schedule 2 Line 8: $0

## Required attachments
- [ ] Form 1040 (5329 attaches)
- [ ] Form 8606 N/A (Marcus chose Option A, not recharacterization)
- Keep (not attached): Fidelity 1099-R for the return-of-excess (issued in
  January 2027 for a 2026 distribution, or January 2026 if processed in
  2025)

## Validation summary
- Math: all checks passed
- Sanity:
  - 2025 single Roth phaseout: $150,000-$165,000 MAGI per Notice 2024-80
  - Marcus's MAGI $208,000 > $165,000 → contribution fully ineligible
  - Excess $7,000 withdrawn with NIA $317 before October 15, 2026
    deadline → no Part IV 6% tax
  - $317 earnings reported as taxable on Form 1040 Line 4b
  - No 10% tax on the $317 (exception 21), even though Marcus is 38
- Next steps:
  - File Form 1040 reporting $317 taxable on Line 4b
  - Schedule 2 Line 8: $0 from Form 5329
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
- IRC §72(t), §72(t)(2)(A)(ix) — early distribution additional tax; corrective-distribution earnings exception
- IRC §408(d)(4) — return of excess contribution before due date
- Treas. Reg. §1.408-11 — net income attributable (NIA) computation
- Notice 2024-80 — 2025 Roth IRA phaseout limits ($150K-$165K single)
- IRS Pub 590-A — contributions to IRAs (excess contribution correction)
```

## Why each non-obvious choice

**Why does Part I appear even though no tax is due?** Return-of-excess
preserves the *principal* tax-and-penalty-free character (it was Roth
basis), but the *earnings* (NIA) on the excess are taxable in the year of
the original contribution. For corrective distributions made on or after
December 29, 2022, the earnings are not subject to the 10% tax (IRC
§72(t)(2)(A)(ix), SECURE 2.0 §333). The instructions still route them
through Part I: Line 1 and Line 2 with exception 21 (2025 Instructions for
Form 5329, Line 23).

**Why exception 21 rather than another exception?** Exception 21 is the
specific number for corrective distributions of the income on excess
contributions made by the due date including extensions (2025
Instructions for Form 5329, Line 2). If the earnings were the only Part I
item, no other number is needed.

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
linearly reduced (Pub. 590-A (2025), Worksheet 2-2). Calculation:
```
Line 5: ($155,000 − $150,000) / $15,000 = 0.333
Line 7: $7,000 × 0.333 = $2,331
Line 8: $7,000 − $2,331 = $4,669 → rounded up to the nearest $10 = $4,670
Excess = $7,000 − $4,670 = $2,330
```
He'd correct only the $2,330 excess, not the full $7,000.

**What records should Marcus retain?**

1. Fidelity statements showing the original $7,000 contribution in
   January 2025
2. Fidelity statement of the return-of-excess (showing $7,000 + $317)
3. Fidelity 1099-R for the return-of-excess (when issued)
4. Marcus's 2025 final pay stubs and W-2 supporting MAGI calculation
5. Marcus's 2025 1099-B and brokerage statements supporting MAGI
6. NIA computation worksheet from Fidelity
7. Copy of the filed Form 5329 with Part I and Part IV
