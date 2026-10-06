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
employer plans (401(k), 403(b)), never IRAs (2025 Instructions for Form
5329, Line 2). Once rolled to an IRA, the
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

**Fix**: Apply Roth ordering rules (Form 8606 Part III) before computing
Line 1. If basis covers the distribution, Form 8606 line 25c = 0, Line 1 =
0 and Form 5329 isn't filed; Form 8606 Part III is still filed for the
nonqualified distribution.

**Citation**: IRC §408A; IRS Pub 590-B Roth IRA distribution ordering
rules.

---

## 3. Filing Part I when the 1099-R already shows the exception, or skipping it when it doesn't

**The mistake**: User's 1099-R shows code 1 in Box 7 but the user
qualifies for an exception, and they skip Form 5329; or the user files
Part I for a code 2, 3, or 4 distribution the custodian already coded
correctly.

**Why it's wrong**: Form 5329 Part I is required when a distribution is
subject to the 10% tax and box 7 does not show the exception, or the
exception does not cover the whole distribution. When box 7 correctly shows
an exception for the full amount, Form 5329 is not required. When box 7 is
code 1 and the user owes the 10% on the full amount, the tax can go
straight on Schedule 2 (Form 1040), line 8 without Form 5329 (2025
Instructions for Form 5329, "Who Must File").

**Fix**: Check that the box 7 code matches the facts. File Part I with the
right exception number on Line 2 when the code is 1, J, or S and an
exception applies (number 12 only if the user was 59½ or older).

**Citation**: 2025 Instructions for Form 5329, "Who Must File" and Line 2.

---

## 4. Missing the SIMPLE-IRA 25% rate in the first 2 years

**The mistake**: A 40-year-old took a $10,000 distribution from their
SIMPLE IRA, where they had been participating for 14 months. They computed
Part I Line 4 as $10,000 × 10% = $1,000.

**Why it's wrong**: For SIMPLE IRA distributions taken within 2 years of
the date the user first participated in the SIMPLE plan, the rate is **25%**,
not 10% (Form 5329 Line 4 caution; 1099-R box 7 code S).

**Fix**: Identify the SIMPLE-plan first-participation date and check
whether 2 years have elapsed. If not, include 25% of that amount on Line 4
instead of 10% ($10,000 × 25% = $2,500 here).

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

**Citation**: IRC §408A(d)(6)(B)(iii) as amended by TCJA §13611; Pub.
590-A (Recharacterizations).

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
effective for tax years beginning after 12/31/2022. And it drops to 10% if
the user takes the missed distribution and files during the correction
window. And it can drop to 0 with a reasonable-cause waiver under
§4974(d).

**Fix**: Compute the tax on Lines 54a/54b (10% / 25%). If the shortfall was
due to reasonable error, request a waiver with "RC" next to Line 54a/54b
and a short statement. See [`missed-rmd.md`](./missed-rmd.md).

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

**Why it's wrong**: For MFS filers who lived with their spouse at any time
during the year, the Roth IRA phaseout is **$0 to $10,000 MAGI** (yes, ten
thousand, not the $150K+ for single filers; 2025 Instructions for Form
5329, Line 19). Such a filer with MAGI above $10,000 is fully phased out of
Roth contributions. The wife's $7,000 contribution is entirely excess. (MFS
filers who did not live with their spouse at any time in the year use the
single range.)

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

**Fix**: When filing standalone, include the address on page 1 and sign
and date page 3 of Form 5329 in ink; a standalone Form 5329 cannot be filed
electronically. When attaching to a 1040, leave the standalone signature
block blank (the 1040 signature covers the attachment).

**Citation**: 2025 Instructions for Form 5329, "When and Where To File".

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
2. Is there a 1099-R with code 1 and an exception the user qualifies for,
   but no Form 5329 Line 2 amount? → User didn't claim the exception.
3. Did the user contribute to a Roth and the prior-year MAGI was at the
   phaseout? → Check Part IV.
4. Did the user turn 73, 74, 75, etc. and take *no* distribution? →
   Possible missed RMD.
5. Is the user's prior-year 5329 Part III/IV Line 16 / Line 24 non-zero
   and the current-year 5329 missing? → Carryforward not reported.
