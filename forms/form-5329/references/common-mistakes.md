# Form 5329 — Common Mistakes

The 10 highest-frequency mistakes filers make on Form 5329, with examples
and fixes. Drawn from IRS audit guides, Pub 590-A/B, and practitioner
literature.

---

## 1. Treating a 401(k)-to-IRA rollover as if the rule of 55 still applies

**The mistake**: A 56-year-old separated from service from their employer,
rolled the 401(k) to a traditional IRA, then took a $30,000 distribution.
They claimed code 01 (separation after 55) on Form 5329 Line 2.

**Why it's wrong**: Code 01 applies only to distributions from qualified
plans (401(k), 403(b), governmental 457(b)). Once rolled to an IRA, the
account is no longer a qualified plan and the rule of 55 doesn't apply.
The distribution is subject to the full 10% under §72(t).

**Fix**: Don't roll a 401(k) to an IRA before age 59½ if there's any
chance of needing distributions. Take the early distribution from the
401(k) directly. If the rollover already happened, code 01 is gone.

**Citation**: IRC §72(t)(2)(A)(v); IRS Pub 575.

---

## 2. Forgetting that Roth IRA basis comes out tax- and penalty-free

**The mistake**: A 32-year-old took $15,000 from a Roth IRA where they had
contributed $25,000 over the years (no conversions). They reported
$15,000 on Form 5329 Line 1, computed a $1,500 Part I additional tax.

**Why it's wrong**: Roth IRA distributions are governed by the ordering
rules of §408A. Regular Roth contributions come out first, tax-free and
penalty-free regardless of age or 5-year rule. The user's $15,000 was
entirely basis. Form 5329 isn't required at all.

**Fix**: Apply Roth ordering rules before computing Line 1. If basis
covers the distribution, Line 1 = 0 and Form 5329 isn't filed.

**Citation**: IRC §408A; IRS Pub 590-B Roth IRA distribution ordering
rules.

---

## 3. Conflating "code 2" on a 1099-R with no penalty owed

**The mistake**: User's 1099-R shows code 2 in Box 7 ("early distribution,
exception applies"). They assume the custodian has already handled the
exception and don't file Form 5329 at all.

**Why it's wrong**: Code 2 means the *custodian* believed an exception
applied (e.g., disability, SoSEPP setup). The IRS still requires the user
to claim the exception on Form 5329 Part I, Line 2 with the appropriate
exception code. If the user doesn't, the IRS may assess the 10% based on
gross distribution without the exception.

**Fix**: Always file Form 5329 Part I when there's any early
distribution, even when Box 7 is code 2. Claim the exception with the
correct code on Line 2.

**Citation**: Instructions for Form 5329, Part I.

---

## 4. Missing the SIMPLE-IRA 25% rate in the first 2 years

**The mistake**: A 40-year-old took a $10,000 distribution from their
SIMPLE IRA, where they had been participating for 14 months. They computed
Part I Line 4 as $10,000 × 10% = $1,000.

**Why it's wrong**: For SIMPLE IRA distributions taken within 2 years of
the date the user first participated in the SIMPLE plan, the rate is **25%**,
not 10%. Form 5329 Part I has a separate computation for this case.

**Fix**: Identify the SIMPLE-plan first-participation date and check
whether 2 years have elapsed. If not, the rate is 25%, computed as a
separate amount on Part I.

**Citation**: IRC §72(t)(6); IRS Pub 590-B.

---

## 5. Recharacterizing a Roth conversion (no longer allowed)

**The mistake**: A user converted $50,000 from traditional to Roth in
March, then in October realized the tax bill was unaffordable. They
asked the custodian to "recharacterize" the conversion back to
traditional.

**Why it's wrong**: TCJA (effective 2018) repealed the ability to
recharacterize Roth *conversions*. Only Roth *contributions* can still
be recharacterized.

**Fix**: There is no fix once the conversion is done. The user owes the
income tax on the conversion. Plan conversion timing more carefully in
future years (consider a smaller conversion or one closer to year-end
when income picture is clearer).

**Citation**: IRC §408A(d)(6) as amended by TCJA §13611; IRS Notice
2018-74.

---

## 6. Not realizing excess contributions compound 6% annually

**The mistake**: User had a $5,000 Roth excess in 2021 and never
corrected it. They didn't file Form 5329 for 2021 or 2022. In 2023 they
realized and asked, "What's the damage?"

**Why it's wrong**: The 6% tax under §4973 applies *each year* the
excess remains. Three years of uncorrected excess = $300 + $300 + $300
= $900 in cumulative tax (assuming the account value supported it). Plus
interest and possibly failure-to-file penalties on the omitted Forms
5329.

**Fix**: File Forms 5329 for each year of excess (a separate 5329 per
year). Withdraw the excess + NIA now to stop the compounding. Consider
filing amended returns if the prior-year 5329s should have included
other items.

**Citation**: IRC §4973; Pub 590-A.

---

## 7. Believing a missed RMD is a 50% catastrophe

**The mistake**: A user missed an RMD and thinks the penalty is 50% (the
pre-2023 rate). They panic, take excessive corrective action, or seek
expensive professional intervention.

**Why it's wrong**: SECURE 2.0 §302 dropped the rate from 50% to 25%
effective for tax years beginning after 12/31/2022. And it can drop to
10% if the user takes the missed distribution within 2 years. And it can
drop to 0 with a reasonable-cause waiver — which the IRS approves
liberally in practice.

**Fix**: Compute the 25% (or 10% with SECURE 2.0 reduction). Most users
should request a waiver; it's a short statement and approval is the
common outcome. See [`missed-rmd.md`](./missed-rmd.md).

**Citation**: SECURE 2.0 Act §302; IRC §4974(d), §4974(e).

---

## 8. Paying the 6% on Roth excess when correction was still possible

**The mistake**: User had a $4,000 Roth excess. By the time they realized,
their custodian was too slow to process a return-of-excess before the tax
filing deadline. They paid the 6% × $4,000 = $240.

**Why it's wrong**: The deadline is the tax filing deadline *including
extensions* (typically October 15). If the user files Form 4868 for an
extension (free, no reason needed), the correction window extends 6 months.
Plenty of time for any custodian.

**Fix**: When discovering an excess close to April 15, file Form 4868 for
an extension first, then have the custodian process the return-of-excess.
Then file the return.

**Citation**: IRC §408(d)(4); IRS Pub 590-A.

---

## 9. Forgetting Part IV when filing MFS

**The mistake**: A married couple files MFS. Wife contributed $7,000 to a
Roth IRA. They had MAGI of $40,000. They didn't think Roth phaseout was a
concern at $40K MAGI.

**Why it's wrong**: For MFS filers, the Roth IRA phaseout is **$0 to
$10,000 MAGI** (yes, ten thousand, not the $150K+ for single filers). Any
MFS filer with MAGI above $10,000 is fully phased out of Roth
contributions. The wife's $7,000 contribution is entirely excess.

**Fix**: MFS filers should not contribute to Roth IRAs unless their MAGI
is genuinely below $10,000 (rare). The wife should withdraw the $7,000 +
NIA before the deadline, or recharacterize to a traditional IRA, or pay
the 6%.

**Citation**: IRC §408A(c)(3); IRS Pub 590-A.

---

## 10. Filing Form 5329 standalone using the wrong signature

**The mistake**: User filed standalone Form 5329 (no 1040 required) but
left the signature line at the bottom of Form 5329 blank. They figured
since they "always" don't sign Form 5329 (because it's normally attached
to the signed 1040), no signature was needed.

**Why it's wrong**: When Form 5329 is filed standalone, there's a separate
signature block at the bottom of the form that *is* required. Without it
the IRS treats the filing as incomplete, may not process the return, and
the underlying tax remains assessed.

**Fix**: When filing standalone, sign the bottom of Form 5329 in ink.
When attaching to a 1040, leave the standalone signature block blank
(the 1040 signature covers the attachment).

**Citation**: Instructions for Form 5329 — "Filing Form 5329 by itself"
section.

---

## Bonus pitfall — Mixing taxable IRA distribution amounts

When computing Part I Line 1, the user enters only the **taxable** portion
of the early distribution. For traditional IRAs with no basis (no
nondeductible contributions ever made), the entire distribution is
taxable. For traditional IRAs with basis (Form 8606 in play), only the
non-basis portion is taxable. Don't include basis in Line 1.

For Roth IRAs: only earnings (the portion *above* contributions and
qualifying conversions) is potentially taxable, and only when the Roth
distribution is non-qualified.

---

## How to spot these mistakes in someone else's return

When reviewing a Form 5329 (CPA review, prior-year amend, etc.), check:

1. Is there a 1099-R with code 1 or 2 *and* no Form 5329 Part I? → Possible
   missed filing.
2. Is there a 1099-R with code 2 and Form 5329 Part I Line 2 = 0? → User
   didn't claim the exception code.
3. Did the user contribute to a Roth and the prior-year MAGI was at the
   phaseout? → Check Part IV.
4. Did the user turn 73, 74, 75, etc. and take *no* distribution? →
   Possible missed RMD.
5. Is the user's prior-year 5329 Part III/IV Line 16 / Line 24 non-zero
   and the current-year 5329 missing? → Carryforward not reported.
