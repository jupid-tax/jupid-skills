---
name: form-1116
description: >
  Use this skill when an individual, estate, or trust needs to claim the
  Foreign Tax Credit (FTC) on Form 1116 for foreign income taxes paid or
  accrued on foreign-source income. Triggers on phrases like "Foreign Tax
  Credit", "Form 1116", "claim foreign income tax", "double taxation relief
  credit", "1099-DIV foreign tax box 7", "expat tax credit", "foreign tax
  carryforward", "FTC limitation", "passive vs general basket". Do NOT use
  this skill for the Foreign Earned Income Exclusion (use form-2555 instead);
  for foreign tax withheld on US-source income (not creditable as FTC); for
  GILTI deemed-paid credits under §960 (different mechanics, corporate
  shareholders); or for the simple "no Form 1116 needed" $300/$600 election
  when the user qualifies (covered in Step 1 below — answer is just Schedule
  3 Line 1, no 1116 attached).
form: Form 1116 (Foreign Tax Credit — Individual, Estate, or Trust)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1116.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1116.pdf
---

# Form 1116 — Foreign Tax Credit (Individual, Estate, or Trust)

This skill produces an audit-grade draft of Form 1116 from the user's foreign income, foreign taxes paid or accrued, and US tax facts. It walks the form line by line, applies the IRC §904 limitation per category (basket), validates the result, and emits a deliverable the filer can transcribe to a paper or e-file form.

The math is mechanical. The judgment is in (1) whether the user even needs Form 1116 vs. the de-minimis $300/$600 election, (2) which basket each income item belongs in, (3) how to allocate deductions between foreign- and US-source income, and (4) whether the FTC or a Schedule A deduction yields a better result.

This skill optimizes for "ask, don't guess." Foreign tax facts are highly user-specific; the agent must collect inputs, not invent them.

**Companion guide for end users:** [Form 1116 + AI Agent Skill: Foreign Tax Credit Guide 2026](https://jupid.com/blog/form-1116-foreign-tax-credit-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision.** The line map in this skill was verified on 2026-10-06 against the **2025 Form 1116** (created 9/16/25) and the **2025 Instructions for Form 1116** (Dec 23, 2025), filed in 2026, plus Schedule B (Form 1116) Rev. December 2022 and Schedule C (Form 1116) Rev. December 2025. Line numbers shift between revisions (the 2025 form requires Part IV even with a single Form 1116, and line 18 adds back the Schedule 1-A senior deduction). Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1116 before using this skill for a later tax year.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1116, "Foreign Tax Credit", "FTC", "foreign tax carryforward", or "FTC limitation"
- The user has a 1099-DIV with an amount in Box 7 (foreign tax paid) and wants to claim it
- The user paid foreign income tax on wages, self-employment income, dividends, interest, royalties, or capital gains earned outside the US
- The user is a US citizen or resident alien with foreign-source income and wants to avoid double taxation by credit (not by exclusion)
- The user is an estate or trust with foreign-source income reportable on Form 1041

Do **not** engage this skill when:

- The user wants the **Foreign Earned Income Exclusion** instead → use the `form-2555` skill. Most expats with wage income choose between 1116 and 2555; they coordinate, but mechanics differ. See [`references/coordination-with-2555.md`](./references/coordination-with-2555.md) for the choice.
- The user paid foreign tax on **US-source** income (e.g., a foreign country withheld on US-source dividends) → not creditable as FTC; the user should pursue a foreign-country refund or treaty claim.
- The user has a **GILTI** inclusion and is a corporate shareholder → §960 deemed-paid credit, different mechanics, different form.
- The user is a corporation → use Form 1118, not Form 1116. An individual CFC shareholder who made a **§962 election** also claims the credit for the CFC's taxes on Form 1118 (2025 i1116, "Foreign Taxes Eligible for a Credit").
- The user took the FEIE on the same income → no FTC on the excluded portion (see `references/coordination-with-2555.md`).

If the user's situation is ambiguous (e.g., they're an expat with both wages and dividends, or they're choosing between exclusion and credit), pause and route to the right skill — running both in parallel is normal and the agent should be ready to invoke `form-2555` after this draft if the user wants the comparison.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. 1116 thresholds, exchange rates, and limitation math are year-specific.
2. **Filer's legal name and SSN/ITIN** (or trust EIN for Form 1041 attachments). Used in the form header.
3. **Filer's status**: individual (Form 1040), nonresident alien (Form 1040-NR), or estate/trust (Form 1041). Determines which return Form 1116 attaches to and which deductions allocate. A nonresident alien generally can't take the credit; the exceptions are a full-year Puerto Rico resident and foreign tax on foreign-source income effectively connected with a US trade or business (2025 i1116, "Nonresident aliens"; IRC §906). If neither applies, stop.
4. **Resident country** for the tax year (line h above Part I, "Resident of (name of country)"). Ask if the filer changed residence mid-year.
5. **Foreign income items**, structured as a list. For each: source country, US-dollar amount, category/basket (passive / general / §901(j) / re-sourced by treaty / lump-sum distributions), and the foreign currency and exchange rate used. Income: the spot rate when received, or a posted rate such as the IRS yearly average used consistently. Foreign taxes follow the stricter rules in Step 3.
6. **Foreign income tax** paid OR accrued (the user picks one method and uses it for all foreign taxes that year — IRC §905(a)). For each tax: country, amount in foreign currency, USD amount, date paid or accrued, and which income category it relates to.
7. **The election method** for taxes: cash basis (paid) or accrual basis (accrued). Default for individuals is cash. A cash-basis filer elects accrual by checking "Accrued" in Part II on a timely filed original return (not an amended return); once made, it applies to all future years (2025 i1116, Part II).
8. **Whether the user qualifies for the de-minimis exception** ($300 single / $600 MFJ — see Step 1). If yes, the answer is "no Form 1116 — just Schedule 3 Line 1," and the skill can short-circuit.
9. **US tax for line 20**: Form 1040 line 16 plus Schedule 2 line 1z, less any Form 4972 tax included on line 16 (Form 1041 filers: Schedule G lines 1a and 1d). This is the regular tax the limitation fraction multiplies; it excludes SE tax and NIIT (IRC §26(b)).
10. **Taxable income for line 18** (the limitation denominator): Form 1040 line 11b minus line 14, plus Schedule 1-A line 37 (the $6,000 senior deduction is added back for 2025-2028); estates and trusts use taxable income without the exemption deduction (2025 i1116, line 18). If the filer has qualified dividends or capital gains and doesn't qualify for the adjustment exception, line 18 comes from the Worksheet for Line 18 instead.
11. **Any prior-year unused FTC carryovers**, by category (basket), with the prior Schedule B (Form 1116). Carryback 1 + carryforward 10 per IRC §904(c).

For each foreign income item, also collect:

- **Allocable deductions** (definitely related to the foreign income — e.g., investment expenses tied to foreign dividends, business expenses tied to foreign self-employment)
- **Pro-rata share of "not definitely related" deductions** — standard deduction or itemized deductions that aren't tied to specific income (allocated by ratio)

If the user can't produce category-by-category foreign income or doesn't know which basket a 1099 belongs to, **ASK** — see [`references/baskets.md`](./references/baskets.md) for the routing rules.

---

## Workflow

Execute these steps in order.

### Step 1 — Test the de-minimis exception (no Form 1116 needed)

The filer can skip Form 1116 entirely (and just put the foreign tax on Schedule 3 Line 1) if **all** of these are true (IRC §904(j); 2025 i1116, "Election To Claim the Foreign Tax Credit Without Filing Form 1116"; 2025 Form 1040 instructions, Schedule 3 line 1 "Exception"):

- The filer is an individual (the election isn't available to estates or trusts)
- Total creditable foreign taxes ≤ **$300**, or ≤ **$600** on a joint return
- All foreign-source gross income is **passive category** income (the Form 1040 instructions phrase it as interest and dividends)
- All of that income and the foreign tax on it are reported on a **qualified payee statement**: Form 1099-DIV, 1099-INT, Schedule K-1 (Form 1041), Schedule K-3 (Form 1065 or 1120-S), or a substitute statement
- The stock or bonds were held at least 16 days and the filer wasn't obligated to pay the amounts to someone else
- The filer isn't filing Form 4563 or excluding income from sources within Puerto Rico
- The foreign taxes were legally owed, not eligible for a refund or reduced treaty rate, and paid to countries the US recognizes that don't support terrorism
- The filer elects this treatment (by claiming the credit on Schedule 3 line 1 without Form 1116)

If ALL true, **stop here**. The credit is the smaller of total foreign tax or the total of Form 1040 line 16 and Schedule 2 line 1a (2025 Form 1040 instructions, Schedule 3 line 1). Emit a short deliverable: "Schedule 3 Line 1: $X. No Form 1116 required (IRC §904(j) election)." Tell the user that unused foreign tax can't be carried to or from an election year (IRC §904(j)(1)(B)-(C)). Skip the rest of this skill.

If ANY are false, continue to Step 2.

### Step 2 — Sort foreign income into categories (baskets)

Each Form 1116 covers exactly one category. The user files a separate 1116 per category they have. The categories are:

- **(a) Section 951A category** — GILTI inclusion (rare for individuals; mostly CFC shareholders)
- **(b) Foreign branch category** — foreign branch income (post-TCJA; mostly business filers)
- **(c) Passive category income** — interest, dividends, royalties, rents, net gain from property held for investment, annuities (most income behind foreign tax in 1099-DIV box 7 or 1099-INT box 6)
- **(d) General category income** — wages, self-employment income, business income, anything not in another basket
- **(e) Section 901(j) income** — income from sanctioned countries; for 2025 Pub. 514 lists Iran, Libya (Presidential waiver since Dec 10, 2004), North Korea, Sudan, and Syria. No credit is allowed for taxes paid to those countries; a separate Form 1116 per country, generally completed only through line 17. Re-check the list in the current Pub. 514.
- **(f) Certain income re-sourced by treaty** — US-source income that a treaty sourcing rule treats as foreign source when the filer elects the treaty; separate Form 1116 per treaty country (Form 8833 may be required)
- **(g) Lump-sum distributions** — foreign-source lump-sum distribution from a pension plan when the filer figures the tax on Form 4972

Walk through each item and assign a basket using [`references/baskets.md`](./references/baskets.md). When ambiguous, **ASK**.

If the user has income in more than one basket, prepare one Form 1116 per basket. The drafts share inputs but compute the §904 limitation independently per basket.

### Step 3 — Convert foreign currency to USD

Foreign income and foreign tax are reported in USD on Form 1116. The filer must translate from foreign currency.

- Wages / salary / SE income: the general rule is the spot rate when received; the IRS accepts any posted rate used consistently, including its yearly average (divide the foreign amount by the IRS rate)
- Passive income already in USD on a 1099-DIV/INT: no translation; enter "1099 taxes" in Part II column (l)
- Foreign tax claimed on a **paid** basis: the rate on the day paid, or on the day withheld for withholding (2025 i1116, "Foreign Currency Conversion"; Pub. 514). Monthly payroll withholding means one rate per payday, not the yearly average
- Foreign tax claimed on an **accrued** basis: the average rate for the tax year to which the taxes relate, unless paid more than 2 years after that year, paid before it, or denominated in an inflationary currency (then the rate on the payment date)
- Attach a detailed explanation of how each conversion rate was figured

The user should pick a consistent source. See [`references/currency.md`](./references/currency.md) for IRS rate sources and worked examples.

### Step 4 — Fill Part I (Foreign-Source Taxable Income, per category)

For the chosen basket on this 1116:

- **Line i** — Name of each foreign country or US territory (one column per country; "RIC" for mutual-fund pass-through amounts)
- **Line 1a** — Gross income from sources in that country, in this category, USD (excluding income excluded on Form 2555; foreign qualified dividends and capital gains after any rate adjustment)
- **Line 1b** — Checkbox only: employee compensation, total compensation $250,000 or more, alternative sourcing basis used
- **Line 2** — Expenses definitely related to line 1a (no interest expense)
- **Lines 3a–3g** — Pro rata share of other deductions: 3a certain itemized deductions or the standard deduction, 3b other deductions (Schedule 1 Part II adjustments), 3c sum, 3d gross foreign income in this category, 3e gross income from all sources, 3f ratio, 3g share
- **Lines 4a/4b** — Pro rata share of interest expense: 4a home mortgage interest (gross-income worksheet), 4b other interest expense (asset method)
- **Line 5** — Losses from foreign sources
- **Line 6** — Add lines 2, 3g, 4a, 4b, and 5
- **Line 7** — Line 1a − line 6 (carried to line 15)

See [`references/line-by-line.md`](./references/line-by-line.md) for line-level detail. Allocation of Line 3 is the most error-prone area; see [`references/deduction-allocation.md`](./references/deduction-allocation.md).

### Step 5 — Fill Part II (Foreign Taxes Paid or Accrued)

For each country:

- **Lines A/B/C** — one line per country, matching the Part I columns; column (l) date paid or accrued ("1099 taxes" for 1099-reported tax)
- Columns (m)–(p) foreign currency, (q)–(t) US dollars: taxes withheld at source on dividends, rents and royalties, interest; other foreign taxes paid or accrued
- Column (u) — total in US dollars per line
- **Line 8** — Add lines A through C, column (u); carried to line 9

The user checks **(j) Paid** OR **(k) Accrued**. Once accrued is elected, it applies to all future years.

### Step 6 — Compute Part III §904 limitation

This is the math that often surprises filers. The credit is **limited** so it can only offset US tax on foreign-source income, not US tax on US-source income.

```
Line 9  = Line 8 (foreign tax this category)
Line 10 = Carryover from Schedule B (Form 1116) line 3 col. (xiv) + carrybacks (blank for 951A)
Line 11 = Line 9 + Line 10
Line 12 = Reduction in foreign taxes, entered as a negative (Form 2555 excluded income, etc.)
Line 13 = Taxes reclassified under high tax kickout (+/−)
Line 14 = Lines 11 + 12 + 13 (foreign taxes available for credit)
Line 15 = Line 7 (foreign-source taxable income before adjustments)
Line 16 = Adjustments to line 15 (461(l), allocation of foreign/US losses, recaptures)
Line 17 = Line 15 + line 16 (if zero or less, skip 18 and enter 0 on 19)
Line 18 = Form 1040 line 11b − line 14 + Schedule 1-A line 37 (or Worksheet for Line 18)
Line 19 = Line 17 ÷ Line 18 ("1" if line 17 exceeds line 18)
Line 20 = Form 1040 line 16 + Schedule 2 line 1z (less Form 4972 tax)
Line 21 = Line 20 × Line 19 (maximum credit)
Line 22 = Increase in limitation under §960(c) (usually 0)
Line 23 = Line 21 + Line 22
Line 24 = Smaller of Line 14 or Line 23 (credit for this category, to Part IV)
```

Foreign qualified dividends and capital gains are adjusted on **line 1a / line 5** (multiply by 0.4054 at the 15% rate, 0.5405 at 20%, leave out 0%-rate amounts) and worldwide amounts on **line 18** through the Worksheet for Line 18, unless the filer qualifies for and uses the adjustment exception. See [`references/qualified-dividend-adjustment.md`](./references/qualified-dividend-adjustment.md).

If Line 14 > Line 23: the user has **unused** foreign tax. The excess carries back 1 year (amended return with a revised Form 1116) and forward up to 10 years (IRC §904(c)); attach Schedule B (Form 1116) for each category with a carryover. Track it.

### Step 7 — Sum Part IV (combine all baskets)

Starting with the 2025 form, Part IV (lines 25–35) must be completed **even when filing only one Form 1116** (2025 i1116, What's New). With several baskets, fill one Form 1116 per basket (Steps 4-6 each) and complete Part IV only on the form with the largest line 24 (not on a category e or g form unless those are the only two):

- **Lines 25–31** — line 24 credit from each category (25 §951A, 26 foreign branch, 27 passive, 28 general, 29 §901(j), 30 re-sourced by treaty, 31 lump-sum)
- **Line 32** — Add lines 25 through 31
- **Line 33** — Smaller of line 20 or line 32
- **Line 34** — Boycott reduction (when the boycott factor method is used)
- **Line 35** — Line 33 − line 34: the foreign tax credit

Line 35 goes on Schedule 3 (Form 1040) line 1 (Form 1041: Schedule G line 2a).

### Step 8 — Compare credit vs. deduction

The user can elect to take the foreign tax as a Schedule A itemized deduction instead of an FTC (IRC §164). The credit is almost always better (dollar-for-dollar reduction vs. fractional benefit at marginal rate), but exceptions exist:

- High-bracket filer with very limited foreign-source income (limitation severely caps FTC)
- Significant unused carryovers expiring soon
- Taxes that can't be credited but can be deducted (boycott-related, sanctioned-country, holding-period failures; 2025 i1116, "Credit or Deduction")

The deduction goes on Schedule A line 6 (2025 Schedule A instructions). For any one year the choice applies to all foreign income taxes. The filer can switch from deduction to credit within the 10-year period of IRC §6511(d)(3), and from credit to deduction within the normal 3-year period (2025 i1116).

Compute both, surface the difference. Default recommendation: credit. If the deduction is higher, surface that and let the user choose.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms / actions:

- **Form 1116 Line 35** → Schedule 3 (Form 1040) Line 1 → Schedule 3 line 8 → Form 1040 Line 20
- **Unused FTC** → Schedule B (Form 1116) for each category with a carryover, attached this year and each later year it exists
- **Foreign tax refunded or redetermined later** → amended return with revised Form 1116, plus Schedule C (Form 1116) with the current-year return (2025 i1116, "Foreign Tax Redeterminations")
- **If filer also has FEIE** → see [`form-2555`](../form-2555/SKILL.md); excluded income stays off line 1a (it still counts in lines 3d/3e) and the taxes allocable to it come out on line 12
- **If accrual method elected this year for the first time** → note it's binding for future years
- **If foreign-source income includes wages that could be excluded under §911** → consider whether 2555 yields a better result; run that skill in parallel for comparison

### Step 12 — File the return

Hand off to [`filing.md`](./filing.md) for filing channel selection (e-file via tax software, FFFF, paper). Form 1116 is supported on most major e-file platforms but has channel-specific quirks.

---

## Line-by-line guidance

Full reference in [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header (above Part I)

- **a–g** — Category checkbox; only one per Form 1116: a §951A, b foreign branch, c passive, d general, e §901(j), f certain income re-sourced by treaty, g lump-sum distributions
- **h** — "Resident of (name of country)": the filer's country of residence for the year (United States for a US-resident investor)

### Part I — Taxable income or loss from sources outside the US

- **Line i** — Name of each foreign country or US territory, one per column (A, B, C; attach sheets for more). Special labels: "RIC" (mutual-fund pass-through, one column), "863(b)", "951A", "HTKO" (high-taxed passive income), "909 income"
- **Line 1a** — Gross foreign-source income, by country column, in this category. Identify the type on the dotted line. Does NOT include US-source income or earned income excluded on Form 2555
- **Line 1b** — Checkbox, not an amount: check only if line 1a is employee compensation, total compensation from all sources is $250,000 or more, and an alternative basis was used to source it (attach the required statement)
- **Line 2** — Expenses definitely related to line 1a (business expenses of a foreign business, state and local income taxes on foreign-source income); attach a statement; no interest expense
- **Lines 3a–3g** — Pro rata share of deductions not definitely related:
  - 3a: medical expenses, general sales taxes, real estate taxes on the home, personal property taxes from Schedule A; or the standard deduction if not itemizing
  - 3b: other deductions not related to any specific income, e.g., Schedule 1 Part II adjustments; not the Schedule 1-A line 37 senior deduction
  - 3c: 3a + 3b
  - 3d: gross foreign-source income in this category, including Form 2555-excluded income, before any QD/capital gain adjustment
  - 3e: gross income from all sources (same amount on every Form 1116), including Form 2555-excluded income
  - 3f: 3d ÷ 3e, rounded to at least four decimals, not more than 1
  - 3g: 3c × 3f
- **Line 4a** — Home mortgage interest apportioned with the Worksheet for Home Mortgage Interest (gross income method)
- **Line 4b** — Other interest expense (investment, business, student loan, qualified passenger vehicle loan interest), apportioned by the asset method. If gross foreign-source income (including Form 2555-excluded income) is $5,000 or less, all interest can be allocated to US-source income and lines 4a/4b are 0
- **Line 5** — Losses from foreign sources (adjusted foreign capital losses go here)
- **Line 6** — Add lines 2, 3g, 4a, 4b, and 5
- **Line 7** — Line 1a − line 6; also entered on line 15

### Part II — Foreign taxes paid or accrued

One line (A, B, C) per country, matching Part I. Columns (m)–(p) in foreign currency and (q)–(t) in US dollars: withheld at source on dividends, rents and royalties, interest, and other foreign taxes paid or accrued; column (u) total. Line 8 = lines A through C, column (u).

- The user checks **(j) Paid** or **(k) Accrued**. A cash-basis filer can elect accrued only on a timely filed original return, and the election applies to all future years (2025 i1116, Part II).
- Foreign taxes ineligible for credit (penalties, interest, tax not legally owed or refundable, withholding on US-source income, sanctioned-country tax) do NOT go here. See [`references/non-creditable-taxes.md`](./references/non-creditable-taxes.md).

### Part III — Figuring the credit (the §904 limitation)

- **Line 9** = Line 8
- **Line 10** = Carryover from Schedule B (Form 1116) line 3, column (xiv), plus carrybacks to this year; check the box if Schedule B isn't required; blank for §951A
- **Line 11** = 9 + 10
- **Line 12** = Reduction in foreign taxes, as a negative: taxes on Form 2555-excluded income, Puerto Rico exempt income, Form 4563 income, oil and gas, mineral income, Form 5471/8865 failures, specifically attributable boycott taxes, §909 splitter taxes
- **Line 13** = Taxes reclassified under the high tax kickout (negative on the passive form, positive on the other category's form)
- **Line 14** = 11 + 12 + 13 (foreign taxes available for credit)
- **Line 15** = Line 7
- **Line 16** = Adjustments, in the order listed in the instructions: §461(l) disallowed loss, allocation of foreign losses, allocation of US losses, overall foreign loss recapture, separate limitation loss recapture, overall domestic loss recapture (attach computation)
- **Line 17** = 15 + 16 (if zero or less, skip 18 and enter 0 on 19)
- **Line 18** = Form 1040 line 11b − line 14 + Schedule 1-A line 37; Worksheet for Line 18 when QD/capital gain adjustments are required
- **Line 19** = 17 ÷ 18; "1" if line 17 is more than line 18; "0" if line 18 is zero
- **Line 20** = Form 1040 line 16 + Schedule 2 line 1z, less Form 4972 tax (regular tax only; no SE tax, no NIIT)
- **Line 21** = Line 20 × Line 19
- **Line 22** = §960(c) increase in limitation (rare)
- **Line 23** = 21 + 22
- **Line 24** = Smaller of 14 or 23 (credit for this category)

### Part IV — Summary of separate credits from Parts III

Required on every return with Form 1116 for 2025, even with one form. Lines 25–31 take line 24 from each category's form (25 §951A, 26 foreign branch, 27 passive, 28 general, 29 §901(j), 30 re-sourced by treaty, 31 lump-sum). Line 32 = sum; line 33 = smaller of line 20 or line 32; line 34 = boycott reduction; line 35 = 33 − 34, the credit carried to Schedule 3 line 1.

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] Line 3f = Line 3d ÷ Line 3e (at least 4 decimals, not more than 1); Line 3g = Line 3c × Line 3f
- [ ] Line 6 = Line 2 + Line 3g + Line 4a + Line 4b + Line 5
- [ ] Line 7 = Line 1a − Line 6, and Line 15 = Line 7
- [ ] Line 8 = sum of column (u), lines A through C
- [ ] Line 11 = Line 9 + Line 10; Line 14 = Line 11 + Line 12 + Line 13 (line 12 entered as a negative)
- [ ] Line 17 = Line 15 + Line 16
- [ ] Line 18 = Form 1040 line 11b − line 14 + Schedule 1-A line 37 (or Worksheet for Line 18 line 12)
- [ ] Line 19 = Line 17 ÷ Line 18, "1" if line 17 exceeds line 18
- [ ] Line 20 = Form 1040 line 16 + Schedule 2 line 1z (less Form 4972 tax)
- [ ] Line 21 = Line 20 × Line 19; Line 23 = Line 21 + Line 22; Line 24 = smaller of Line 14 or Line 23
- [ ] Part IV completed (required for 2025 even with one Form 1116): Line 32 = sum of lines 25–31; Line 33 = smaller of Line 20 or Line 32; Line 35 = Line 33 − Line 34
- [ ] Line 35 ≤ Line 20 (the credit never exceeds regular tax)

### Sanity checks

Surface a warning, do not block:

- [ ] Foreign tax > 50% of foreign income → unusual; check whether the user is paying both source-country and resident-country tax (treaty relief might apply)
- [ ] Line 19 = 1 → all income is foreign-source; verify the user has no US-source items hiding on the return
- [ ] Foreign tax in passive basket but income source is wages → mis-classification; wages go in general basket
- [ ] User reports foreign tax on US-source dividends → not creditable; remove from Form 1116 and pursue treaty refund
- [ ] Foreign tax withheld on income a treaty exempts at source (e.g., independent services without a fixed base) → refundable, not creditable; ask before entering it
- [ ] User has FEIE on Form 2555 AND foreign tax on the same wages → taxes allocable to excluded income go out on line 12
- [ ] Line 21 is low because Line 18 is high relative to Line 17 → expected; flag carryforward
- [ ] Line 14 > Line 23 by a large margin → significant unused foreign tax; Schedule B; consider whether the deduction is better
- [ ] Filer elects accrued for the first time → confirm filer understands binding nature
- [ ] Single basket, total foreign tax ≤ $300/$600, all passive, all on qualified payee statements → the Step 1 election probably applies; back up and verify

### Cross-form checks

- [ ] If FEIE used (Form 2555): excluded wages are not on line 1a (but are in lines 3d/3e), and the foreign tax allocable to them is removed on line 12
- [ ] If user has 1099-DIV Box 7: confirm the broker reported the foreign tax, not US backup withholding (Box 4)
- [ ] If foreign-source losses or US-source losses occurred: line 16 adjustments and §904(f)/(g) accounts apply (CPA referral if material)
- [ ] Country list on Part I matches country list on Part II (or document the mismatch)
- [ ] Carryover entered on line 10 or excess on line 14 over line 24 → Schedule B (Form 1116) attached for that category

---

## Output format

```markdown
# Form 1116 — DRAFT for tax year YYYY (Category: <basket>)

## Header
Filer name: <name>
SSN/ITIN: <id>
Category (a-g): <one box checked>
h. Resident of: <country>

## Part I — Foreign-source taxable income
i. Country column A: <country>
   Country column B: <country>  (if applicable)
   Country column C: <country>  (if applicable)

1a. Gross foreign-source income (per country):
    A: $X,XXX
    B: $X,XXX
    Total: $X,XXX
1b. Alternative-basis compensation box (≥ $250,000): checked | not checked
2.  Expenses definitely related:              $X,XXX
3a. Certain itemized deductions or std. ded.: $X,XXX
3b. Other deductions:                         $X,XXX
3c. 3a + 3b:                                  $X,XXX
3d. Gross foreign source income:              $X,XXX
3e. Gross income from all sources:            $X,XXX
3f. 3d ÷ 3e:                                  0.XXXX
3g. 3c × 3f:                                  $X,XXX
4a. Home mortgage interest (worksheet):       $X,XXX
4b. Other interest expense:                   $X,XXX
5.  Losses from foreign sources:              $X,XXX
6.  2 + 3g + 4a + 4b + 5:                     $X,XXX
7.  1a − 6:                                   $X,XXX

## Part II — Foreign taxes paid or accrued (this basket)
(j) Paid | (k) Accrued
| Line | Country | (l) Date paid/accrued | Foreign currency (m)-(p) | USD (q)-(t) | (u) Total USD |
|------|---------|----------------------|--------------------------|-------------|---------------|
| A    | ...     | ...                  | ...                      | ...         | ...           |
8. Total foreign tax (USD):                   $X,XXX

## Part III — Figuring the credit
9.  = Line 8:                                 $X,XXX
10. Carryover (Schedule B) + carrybacks:      $X,XXX
11. 9 + 10:                                   $X,XXX
12. Reduction in foreign taxes:               ($X,XXX)
13. High tax kickout reclassification:        $X,XXX
14. 11 + 12 + 13:                             $X,XXX
15. = Line 7:                                 $X,XXX
16. Adjustments to line 15:                   $X,XXX
17. 15 + 16:                                  $X,XXX
18. Taxable income (1040 11b − 14 + 1-A 37):  $X,XXX
19. 17 ÷ 18:                                  0.XXXX
20. 1040 line 16 + Sch. 2 line 1z:            $X,XXX
21. 20 × 19:                                  $X,XXX
22. §960(c) increase:                         $0
23. 21 + 22:                                  $X,XXX
24. Smaller of 14 or 23:                      $X,XXX

## Part IV (on one Form 1116: the one with the largest line 24)
25-31. Line 24 credit by category:            $X,XXX (each)
32. Add lines 25 through 31:                  $X,XXX
33. Smaller of line 20 or line 32:            $X,XXX
34. Boycott reduction:                        $0
35. Foreign tax credit (Schedule 3 line 1):   $X,XXX

## Carryover tracking
Unused foreign tax this year (Line 14 − Line 24), this basket: $X,XXX
  - Carryback: 1 year (amended return with revised Form 1116)
  - Carryforward: 10 years (IRC §904(c))
  - Schedule B (Form 1116) attached for this category

## Required attachments
- [ ] One Form 1116 per basket (separate forms), Part IV on one of them
- [ ] Schedule B (Form 1116) for each category with a carryover
- [ ] Statements: line 2 and line 3a/3b expense lists, currency conversion explanation, line 16 computation (if any)
- [ ] Form 8938 (specified foreign financial assets, if threshold met — separate filing)
- [ ] FBAR / FinCEN 114 (if foreign account aggregate > $10,000 — separate filing)

## Validation summary
- Math: <pass | list failures>
- Sanity: <list any warnings>
- Next steps: <handoff>

## Sources cited in this draft
- IRS Form 1116 (2025), created 9/16/25
- IRS Instructions for Form 1116 (2025), Dec 23, 2025
- IRC §901 (foreign tax credit), §904 (limitation), §905 (accrual election)
- IRC §904(c) (1-year carryback, 10-year carryforward)
- IRC §904(j) (election to claim the credit without Form 1116)
- Pub. 514 — Foreign Tax Credit for Individuals
- Reg. §1.861-8, §1.861-9 (allocation of deductions and interest expense)
- (any other authority used)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on Form 1116 with examples and edge cases
- [`references/baskets.md`](./references/baskets.md) — How to assign income to passive / general / §901(j) / re-sourced categories
- [`references/coordination-with-2555.md`](./references/coordination-with-2555.md) — When to use credit (1116) vs. exclusion (2555); coordination when using both
- [`references/deduction-allocation.md`](./references/deduction-allocation.md) — Allocating itemized/standard deductions and interest expense to foreign-source income
- [`references/qualified-dividend-adjustment.md`](./references/qualified-dividend-adjustment.md) — Line 1a / line 5 and line 18 adjustments for foreign and worldwide QD/capital gains, and the adjustment exception
- [`references/non-creditable-taxes.md`](./references/non-creditable-taxes.md) — Foreign taxes that don't qualify for FTC
- [`references/currency.md`](./references/currency.md) — Foreign currency translation methods and IRS rate sources
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-tripping mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for filing the completed Form 1116

## Examples

End-to-end worked drafts. Use as patterns when the user's situation is similar.

- [`examples/de-minimis-investor.md`](./examples/de-minimis-investor.md) — US investor with $285 foreign tax in 1099-DIV Box 7 — qualifies for the $300 election, no 1116 filed
- [`examples/expat-germany-wages.md`](./examples/expat-germany-wages.md) — US citizen in Germany with €120,000 wages and €40,090 German tax (2025) — full Form 1116 general basket
- [`examples/multi-basket-investor.md`](./examples/multi-basket-investor.md) — Investor with both passive (foreign dividends) and general (foreign consulting) income, two separate Form 1116s

## Sources

Re-verify each year — the IRS revises forms and instructions each cycle.

- [Form 1116 + AI Agent Skill: Foreign Tax Credit Guide 2026](https://jupid.com/blog/form-1116-foreign-tax-credit-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1116 (2025; latest)](https://www.irs.gov/pub/irs-pdf/f1116.pdf)
- [Instructions for Form 1116 (2025; latest)](https://www.irs.gov/pub/irs-pdf/i1116.pdf)
- [Schedule B (Form 1116), Rev. December 2022](https://www.irs.gov/pub/irs-pdf/f1116sb.pdf) and [Schedule C (Form 1116), Rev. December 2025](https://www.irs.gov/pub/irs-pdf/f1116sc.pdf)
- [About Form 1116](https://www.irs.gov/forms-pubs/about-form-1116)
- [Publication 514](https://www.irs.gov/publications/p514) — Foreign Tax Credit for Individuals (2025 sanctioned-country list)
- [Instructions for Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Schedule 3 line 1 "Exception" (no-Form-1116 requirements)
- [Yearly Average Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates) — for translation
- IRC §901 (allowance of credit), §903 (in-lieu-of taxes), §904 (limitation), §904(c) (carryback/carryforward), §904(f) (recharacterization of foreign losses), §904(j) (election to claim the credit without Form 1116), §905 (accrual election), §906 (nonresident aliens), §6511(d)(3) (10-year credit election period)
- Reg. §1.861-8 / §1.861-9 (allocation and apportionment of deductions), Reg. §1.901-2 (creditable foreign income tax)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. International tax has many edge cases (treaty overrides, dual-resident filers, §904(f) recharacterization, §951A inclusions); for material amounts or unusual fact patterns, route the user to a CPA or EA with international expertise.
