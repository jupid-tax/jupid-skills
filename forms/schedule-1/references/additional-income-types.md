# Schedule 1 Line 8 — Additional Income Types (Deep Reference)

Line 8 is where every income item that doesn't fit Lines 1-7 of Schedule 1 lands. The 2025 form (carrying into 2026) has 22 sub-lines plus an "8z list type and amount" catchall. This file is the agent's deep reference for each type — when it applies, how to compute the amount, what's *not* included, and which authority controls.

When in doubt about which sub-line an item belongs on, default to **8z with a clear label** rather than guessing. The IRS would rather see "8z — Settlement payment for emotional distress" than the same dollar mis-classified onto a wrong sub-line.

---

## 1099-K and personal items sold at a loss

Before Line 8, there is a dedicated above-Part-I row for 1099-K amounts that are not taxable income. Two qualifying situations:

1. **Personal items sold at a loss** — used couch on Marketplace, used phone on eBay, concert tickets resold via PayPal G&S for less than face. The user bought it for $X, sold for less than $X, no gain. The 1099-K still reports the gross. Enter the gross 1099-K amount in this row to reconcile.
2. **1099-K issued in error** — wrong taxpayer, duplicate, or non-business activity that doesn't fit any income category. Enter the erroneous amount and disregard.

If the 1099-K is for a real trade or business (regular Etsy sales, rideshare, freelance), it belongs on **Schedule C** — not on the 1099-K reconciliation row, not on Line 8.

If a 1099-K covers personal items sold at a **gain** (e.g., a watch the user bought for $200 and sold for $500), the gain goes on Schedule D / Form 8949 (capital gain on personal property), not on Schedule 1.

---

## 8a — Net operating loss (NOL)

Reported as a **negative** number. NOL carryforward from a prior year, computed on Form 1045 Schedule A or Pub 536 worksheet.

Post-TCJA NOLs (arising in tax years after 2017):
- Carry forward indefinitely (no 20-year limit)
- Cannot be carried back (with limited exceptions for farming and casualty losses)
- Limited to **80%** of taxable income before the NOL deduction

Pre-TCJA NOLs follow the prior 2-back/20-forward rules and are not subject to the 80% cap.

**Source**: IRC §172.

---

## 8b — Gambling winnings

**All gambling winnings are taxable**, whether or not a W-2G was issued. Report **gross winnings** on Line 8b. Losses do **not** offset winnings on Line 8b.

W-2G is issued for:
- $1,200+ on bingo or slots
- $1,500+ on keno (net)
- $5,000+ on poker tournaments (net of buy-in)
- $600+ and 300:1 odds on other gambling (horse racing, sweepstakes, lotteries)

**Losses**: deductible only as an itemized deduction on Schedule A, **only up to the amount of winnings**. Filers who take the standard deduction get no offset for losses.

**Sports betting / DFS**: same rules. The platform issues a W-2G when thresholds are met; under-threshold winnings are still taxable.

**Common error**: netting winnings and losses on Line 8b. Always report gross.

**Source**: IRC §165(d); IRS Publication 529.

---

## 8c — Cancellation of debt

Forgiven debt is income (IRC §61(a)(11)) unless an exception applies. Lender reports on Form 1099-C.

**Exceptions** (full or partial exclusion, computed on Form 982):
- **Insolvency** — taxpayer's liabilities exceeded assets immediately before discharge (most common solo-filer exclusion)
- **Bankruptcy** — debt discharged in Title 11 case
- **Qualified principal residence indebtedness** — up to $750,000 ($375,000 MFS) for primary residence acquisition debt forgiven
- **Qualified farm indebtedness**
- **Qualified real property business indebtedness**
- **Student loan discharge** — certain types are excluded under IRC §108(f); American Rescue Plan Act discharges through 2025 are non-taxable federally

If an exception applies, attach Form 982 and reduce tax attributes per IRC §108(b).

**Source**: IRC §§61(a)(11), 108; IRS Publication 4681.

---

## 8d — Foreign earned income exclusion

Reported as a **negative**. From Form 2555 Line 45. Reduces income for U.S. citizens / resident aliens working abroad who meet the bona fide residence or physical presence test.

2025 exclusion: $130,000. 2026: announced fall 2025.

If excluding via 2555, the housing exclusion goes on Line 8d as well; the housing **deduction** (for self-employed) goes on Line 24j.

**Source**: IRC §911.

---

## 8e — Income from Form 8853

Distributions from an Archer MSA or Medicare Advantage MSA used for non-qualifying medical expenses, plus taxable LTC contract distributions. Form 8853 computes the amount.

---

## 8f — Income from Form 8889

Distributions from an HSA used for non-qualifying medical expenses. Subject to 20% additional tax on Schedule 2 (unless user is 65+, disabled, or deceased). Form 8889 computes the amount.

**Source**: IRC §223(f).

---

## 8g — Alaska Permanent Fund dividends

Annual Alaska Permanent Fund Dividend received by Alaska residents. Reported on a 1099-MISC by the State of Alaska. Fully taxable federally.

A child's PFD income reported on the child's return; if the child has only PFD and limited investment income, see the IRS rules on the kiddie tax (Form 8615).

---

## 8h — Jury duty pay

Pay received for serving on a jury (federal, state, or local court). Always taxable.

If the user's **employer paid them their regular wages during jury service** and required them to turn over the jury pay, the user reports the jury pay on **Line 8h** and takes an offsetting adjustment on **Line 24a** for the amount turned over. Net effect: zero on AGI. Without the employer-payment circumstance, Line 24a doesn't apply.

---

## 8i — Prizes and awards

Game show winnings, raffle prizes (Publishers Clearing House, charity raffles), contest winnings, scientific or scholastic awards (unless excluded under IRC §74(b) for a transfer-to-charity election), employer-given non-cash awards over the de minimis threshold.

Report **fair market value**, even for non-cash prizes (a $30,000 car won on a game show = $30,000 of income; the IRS doesn't accept "I'd never pay sticker price" arguments).

**Source**: IRC §74.

---

## 8j — Activity not engaged in for profit (hobby)

Hobby income — gross receipts from an activity not engaged in for profit. Report **gross income only**.

Under TCJA (2018-2025; verify status for 2026), hobby expenses are **not deductible** as miscellaneous itemized deductions. Filers cannot net expenses against hobby income on Line 8j.

**Hobby vs. business** (IRC §183): the IRS uses 9 factors to determine for-profit intent (manner conducted, expertise, time and effort, expectation of asset appreciation, success in similar activities, history of income/loss, occasional profits, financial status, personal pleasure). If the activity is genuinely operating for profit, it's a Schedule C business — file Schedule C, not Line 8j.

**Common audit pattern**: a "side gig" with consistent losses. The IRS reclassifies as a hobby, disallows the loss, and assesses tax + penalty. The fix is honest classification upfront.

**Source**: IRC §183; Treas. Reg. §1.183-2(b).

---

## 8k — Stock options

Non-statutory stock option income that wasn't reported on a W-2. Most NSO income lands on a W-2 because the employer captures it in payroll; this line catches edge cases (former employer, foreign exercise, contractor option grants).

ISO disqualifying dispositions are typically captured on the user's W-2. ISO AMT adjustments go on Form 6251 (separate AMT preference item), not on Line 8k.

---

## 8l — Income from rental of personal property (not a business)

Rare. Occasional rental of personal property (not real estate) when the activity is **not a trade or business** — e.g., one-time rental of a piece of equipment or a costume.

Trade-or-business rental of personal property → Schedule C. Real-estate rental → Schedule E → Schedule 1 Line 5.

Deductible expenses related to this Line 8l rental go on Line 24b.

---

## 8m — Olympic and Paralympic medals and USOC prize money

USOC pays cash prizes and medals receive a fair-market value. Both are reportable on 8m. **Offset**: if the user's AGI was $1,000,000 or less ($500,000 MFS), an offsetting Line 24c adjustment makes the income non-taxable per IRC §74(d).

---

## 8n — Section 951(a) inclusion

Subpart F income from a controlled foreign corporation. International tax provision; rare for solo filers.

---

## 8o — Section 951A(a) inclusion

GILTI (Global Intangible Low-Taxed Income). International tax provision; rare for solo filers.

---

## 8p — Section 461(l) excess business loss adjustment

Add-back if the user's aggregate business losses exceeded the §461(l) threshold ($305,000 single / $610,000 MFJ for 2025). The disallowed amount carries forward as an NOL.

**Source**: IRC §461(l).

---

## 8q — Taxable distributions from an ABLE account

Distributions from a §529A ABLE account used for non-qualified disability expenses, plus the proportional share of earnings. Form 1099-QA reports.

---

## 8r — Scholarship and fellowship grants not on W-2

Taxable portion of scholarships not used for qualified tuition and required fees (e.g., room and board, optional fees). Tax-free portion (qualified tuition and required fees for a degree candidate at an eligible institution) is not reported anywhere.

**Source**: IRC §117; IRS Publication 970.

---

## 8s — Nontaxable amount of Medicaid waiver payments

Reported as a **negative**. Medicaid waiver payments to a care provider for caring for an eligible person in their home (Notice 2014-7) are excludable from income. If the payer issued a W-2 including these payments, the user reports the W-2 wages on Form 1040 Line 1a and offsets here on 8s with a negative.

---

## 8t — Pension or annuity from nonqualified deferred comp / nongovt §457 plan

Distributions from a nonqualified deferred compensation plan or a non-governmental §457 plan that aren't reported on W-2 (rare; most are W-2'd).

---

## 8u — Wages earned while incarcerated

Income earned while incarcerated. The IRS excludes this from earned income for EITC purposes but it remains taxable income.

---

## 8v — Digital assets received as ordinary income

The 8v line was added to capture digital asset (crypto, NFT, token) income received as **ordinary income**, when the activity is not a trade or business (which would belong on Schedule C).

Common 8v scenarios:
- **Receiving crypto as payment** for goods or services as an individual (not a business) — FMV at receipt
- **NFT royalties** received from secondary-market resales
- **Staking rewards** when the activity is passive holding, not a Schedule C business
- **Mining rewards** when small-scale and non-business
- **Airdrops and forks** — FMV at the time of dominion and control
- **Hard fork tokens** — per Rev. Rul. 2019-24

If the activity is regular and for-profit (an active mining operation, NFT-creation business, professional staking validator), it's a Schedule C business — not Line 8v.

**Capital gains** from selling crypto held as an investment go on Form 8949 / Schedule D, not Line 8v.

**Source**: Notice 2014-21; Rev. Rul. 2019-24; IRS digital asset FAQs.

---

## 8z — Other income (list type and amount)

Catchall. Use when the income doesn't fit any pre-printed sub-line. Always include a clear, specific label.

Common 8z entries:
- **Settlement / lawsuit proceeds** — taxable portion (lost wages, punitive damages, interest); excluded portion (physical injury) goes nowhere
- **Recovery of a prior-year deduction** (other than state refund — that's Line 1)
- **Director's fees** (if filer is a non-employee corporate director) — could also be Schedule C if it's a regular activity
- **Forgiven student loan debt** under a non-§108(f) employer-arrangement
- **Accident insurance benefits in excess of medical expenses** when employer paid premiums
- **Foreign social security received** (not U.S. Social Security — that's its own Form 1040 line)
- **Alimony from a foreign decree** that doesn't fit Line 2a

Format: "Description — $amount". Multiple items: list each on its own row, sum to the entered total.

---

## When in doubt — ask, don't guess

For any income item not obviously matching a sub-line, the agent must ask the user:
1. What's the source?
2. Was a 1099 issued? Which kind?
3. Is the activity a regular trade or business (Schedule C) or one-off?
4. Is any portion excludable from gross income?

The cost of asking is one extra prompt; the cost of guessing wrong is a CP2000 notice for the user.

---

## Sources

- IRS Schedule 1 (Form 1040), 2025 revision and instructions
- IRC §§61, 74, 108, 111, 117, 165(d), 172, 183, 461(l), 911
- IRS Publication 525 (Taxable and Nontaxable Income)
- IRS Publication 529 (Miscellaneous Deductions)
- IRS Publication 970 (Tax Benefits for Education)
- IRS Publication 4681 (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- Notice 2014-7 (Medicaid waiver payments)
- Notice 2014-21 (digital assets initial guidance)
- Rev. Rul. 2019-24 (digital asset hard forks)
