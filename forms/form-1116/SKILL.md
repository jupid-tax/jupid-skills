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
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f1116.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1116.pdf
---

# Form 1116 — Foreign Tax Credit (Individual, Estate, or Trust)

This skill produces an audit-grade draft of Form 1116 from the user's foreign income, foreign taxes paid or accrued, and US tax facts. It walks the form line by line, applies the IRC §904 limitation per category (basket), validates the result, and emits a deliverable the filer can transcribe to a paper or e-file form.

The math is mechanical. The judgment is in (1) whether the user even needs Form 1116 vs. the de-minimis $300/$600 election, (2) which basket each income item belongs in, (3) how to allocate deductions between foreign- and US-source income, and (4) whether the FTC or a Schedule A deduction yields a better result.

This skill optimizes for "ask, don't guess." Foreign tax facts are highly user-specific; the agent must collect inputs, not invent them.

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
- The user is a corporation → use Form 1118, not Form 1116.
- The user took the FEIE on the same income → no FTC on the excluded portion (see `references/coordination-with-2555.md`).

If the user's situation is ambiguous (e.g., they're an expat with both wages and dividends, or they're choosing between exclusion and credit), pause and route to the right skill — running both in parallel is normal and the agent should be ready to invoke `form-2555` after this draft if the user wants the comparison.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. 1116 thresholds, exchange rates, and limitation math are year-specific.
2. **Filer's legal name and SSN/ITIN** (or trust EIN for Form 1041 attachments). Used in the form header.
3. **Filer's status**: individual (Form 1040), nonresident alien (Form 1040-NR), or estate/trust (Form 1041). Determines which return Form 1116 attaches to and which deductions allocate.
4. **Resident country** for the tax year (Line i — country code on the form). Ask if the filer changed residence mid-year.
5. **Foreign income items**, structured as a list. For each: source country, US-dollar amount, category/basket (passive / general / §901(j) / re-sourced by treaty / lump-sum distributions), and the foreign currency and exchange method used (spot rate on the income date, or yearly average — the IRS allows either, but it must be consistent within a category).
6. **Foreign income tax** paid OR accrued (the user picks one method and uses it for all foreign taxes that year — IRC §905(a)). For each tax: country, amount in foreign currency, USD amount, date paid or accrued, and which income category it relates to.
7. **The election method** for taxes: cash basis (paid) or accrual basis (accrued). Default for individuals is cash. Once the accrual election is made, it's binding for all future years.
8. **Whether the user qualifies for the de-minimis exception** ($300 single / $600 MFJ — see Step 1). If yes, the answer is "no Form 1116 — just Schedule 3 Line 1," and the skill can short-circuit.
9. **US tax before credits** (Form 1040 Line 16, or Form 1041 equivalent). Needed for the §904 limitation denominator.
10. **Total taxable income before personal exemption** (Line 18 denominator). For Form 1040 filers, this is the amount used in Line 18 of Form 1116.
11. **Any prior-year unused FTC carryovers**, by category (basket). Carryback 1 + carryforward 10 per IRC §904(c).

For each foreign income item, also collect:

- **Allocable deductions** (definitely related to the foreign income — e.g., investment expenses tied to foreign dividends, business expenses tied to foreign self-employment)
- **Pro-rata share of "not definitely related" deductions** — standard deduction or itemized deductions that aren't tied to specific income (allocated by ratio)

If the user can't produce category-by-category foreign income or doesn't know which basket a 1099 belongs to, **ASK** — see [`references/baskets.md`](./references/baskets.md) for the routing rules.

---

## Workflow

Execute these steps in order.

### Step 1 — Test the de-minimis exception (no Form 1116 needed)

The filer can skip Form 1116 entirely (and just put the foreign tax on Schedule 3 Line 1) if **all** of these are true (per Form 1040 instructions and IRC §904(k)):

- Total creditable foreign taxes ≤ **$300** (single, HoH, MFS, qualifying surviving spouse) OR ≤ **$600** (MFJ)
- All foreign income is **passive category** income (interest, dividends, capital gains)
- All foreign income and foreign tax are reported on a **qualified payee statement** (1099-DIV, 1099-INT, Schedule K-1, K-3, or substitute statement)
- The filer is not filing Form 4563 and is not a bona fide resident of Puerto Rico
- The filer elects this treatment (just by claiming the credit on Schedule 3 Line 1 without 1116)

If ALL true, **stop here** — emit a one-line deliverable: "Schedule 3 Line 1: $X. No Form 1116 required (IRC §904(k) de-minimis election)." Skip the rest of this skill.

If ANY are false, continue to Step 2.

### Step 2 — Sort foreign income into categories (baskets)

Each Form 1116 covers exactly one category. The user files a separate 1116 per category they have. The categories are:

- **(a) Section 951A category** — GILTI inclusion (rare for individuals; mostly CFC shareholders)
- **(b) Foreign branch category** — foreign branch income (post-TCJA; mostly business filers)
- **(c) Passive category income** — interest, dividends, royalties, rents, net gain from property held for investment, annuities (most 1099-DIV/INT box 7 income)
- **(d) General category income** — wages, self-employment income, business income, anything not in another basket
- **(e) Section 901(j) category** — income from sanctioned countries (currently Iran, North Korea, Sudan; verify against current §901(j) list)
- **(f) Income re-sourced by treaty** — income that a US treaty reclassifies as foreign-source (treaty-specific)
- **(g) Lump-sum distributions** — qualified retirement distribution

Walk through each item and assign a basket using [`references/baskets.md`](./references/baskets.md). When ambiguous, **ASK**.

If the user has income in more than one basket, prepare one Form 1116 per basket. The drafts share inputs but compute the §904 limitation independently per basket.

### Step 3 — Convert foreign currency to USD

Foreign income and foreign tax are reported in USD on Form 1116. The filer must translate from foreign currency.

- Wages / salary / SE income (one-time accrual): use the spot rate on the day the income was received OR a yearly average rate
- Recurring passive income (1099-DIV/INT already in USD): no translation — broker did it
- Foreign tax paid in cash: use spot rate on the day paid
- Foreign tax accrued: use yearly average for the year of accrual (IRS Yearly Average Currency Exchange Rates page)

The user should pick a consistent method. See [`references/currency.md`](./references/currency.md) for IRS rate sources and worked examples.

### Step 4 — Fill Part I (Foreign-Source Taxable Income, per category)

For the chosen basket on this 1116:

- **Line 1a** — Gross income from foreign sources (in this category), per country, USD
- **Line 2** — Allocable deductions definitely related to the foreign income
- **Line 3a–3g** — Pro-rata deductions (standard deduction, itemized deductions not definitely related, interest expense allocation per Reg. §1.861-9)
- **Line 4a/4b** — Home mortgage interest allocation if applicable
- **Line 5** — Losses from foreign sources
- **Line 6** — Total deductions (sum)
- **Line 7** — Foreign-source taxable income (Line 1a − Line 6)

See [`references/line-by-line.md`](./references/line-by-line.md) for line-level detail. Allocation of Line 3 is the most error-prone area; see [`references/deduction-allocation.md`](./references/deduction-allocation.md).

### Step 5 — Fill Part II (Foreign Taxes Paid or Accrued)

For each country:

- **Line A/B/C columns** — country letter + name
- Foreign currency / USD columns for taxes withheld at source (interest, dividends, royalties, etc.) and other foreign taxes
- **Line 8** — Total foreign taxes paid or accrued (in USD), this category

The user must check the box for **paid** OR **accrued** (Line h) — once accrued is elected, it's binding for all future years.

### Step 6 — Compute Part III §904 limitation

This is the math that often surprises filers. The credit is **limited** so it can only offset US tax on foreign-source income, not US tax on US-source income.

```
Line 9  = Line 8 (foreign tax this category)
Line 10 = Carryback / carryforward of prior unused FTC for this category
Line 11 = Line 9 + Line 10 (total available)
Line 14 = Line 7 (foreign-source taxable income, this category)
Line 15 = Adjustments (e.g., qualified dividend rate differential — IRC §904(b)(2)(B))
Line 17 = Line 14 − Line 15 (net foreign-source taxable income, adjusted)
Line 18 = Total taxable income (Form 1040 Line 15, with adjustments)
Line 19 = Line 17 ÷ Line 18 (limitation fraction; max 1.0)
Line 20 = Line 19 × Form 1040 tax (before credits) (Line 16, with adjustments)
Line 21 = Lesser of Line 11 or Line 20 (this is the FTC for this category)
```

The qualified-dividend / capital-gain rate adjustment on Line 15 prevents double-counting the rate benefit; it's required when the user has qualified dividends or LTCG taxed at preferential rates. See [`references/qualified-dividend-adjustment.md`](./references/qualified-dividend-adjustment.md).

If Line 11 > Line 20: the user has **unused** FTC. The excess carries back 1 year (file an amended return) and forward up to 10 years (IRC §904(c)). Track it.

### Step 7 — Sum Part IV (combine all baskets)

If the user has multiple baskets, fill one Form 1116 per basket (Steps 4-6 each). Then on **one summary 1116** (or in tax software, automatic), Part IV combines:

- **Line 33** — Total credit (sum of Line 21 across all categories)
- **Line 35** — Smaller of Line 33 or US tax before credits — final FTC

This goes on Schedule 3 Line 1 of Form 1040.

### Step 8 — Compare credit vs. deduction

The user can elect to take the foreign tax as a Schedule A itemized deduction instead of an FTC (IRC §164). The credit is almost always better (dollar-for-dollar reduction vs. fractional benefit at marginal rate), but exceptions exist:

- High-bracket filer with very limited foreign-source income (limitation severely caps FTC)
- Significant unused carryovers expiring soon
- Filer wants to avoid the qualified-dividend rate adjustment

Compute both, surface the difference. Default recommendation: credit. If the deduction is higher, surface that and let the user choose.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms / actions:

- **Form 1116 Line 35** → Schedule 3 (Form 1040) Line 1 → Form 1040 Line 20
- **Unused FTC** → track carryover schedule for next year (IRS recommends keeping a running schedule by category)
- **If filer also has FEIE** → see `form-2555` skill; coordinate so excluded income and its allocable taxes don't appear on 1116
- **If accrual method elected this year for the first time** → note it's binding for future years
- **If foreign-source income includes wages that could be excluded under §911** → consider whether 2555 yields a better result; run that skill in parallel for comparison

### Step 12 — File the return

Hand off to [`filing.md`](./filing.md) for filing channel selection (e-file via tax software, FFFF, paper). Form 1116 is supported on most major e-file platforms but has channel-specific quirks.

---

## Line-by-line guidance

Full reference in [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **i** — Resident country code (use IRS country code list; if the filer is a US resident with foreign-source income, the answer is "United States")
- **a/b/c/d/e/f/g** — Category (basket) checkbox; only one per 1116
- **h** — Paid or accrued (binding once "accrued" elected)

### Part I — Taxable income from sources outside the US

- **Line 1a** — Gross foreign-source income, by country column. Includes all income in this basket from this country. Does NOT include US-source income.
- **Line 2** — Definitely related deductions: business expenses tied to foreign SE income, investment expenses tied to foreign dividends, etc.
- **Line 3a-3g** — Pro-rata deductions:
  - 3a: Itemized deductions or standard deduction (the not-definitely-related portion)
  - 3b: Other deductions (e.g., charitable contributions if itemizing)
  - 3c: Sum
  - 3d: Gross foreign-source income (this category, all countries)
  - 3e: Gross income from all sources (worldwide)
  - 3f: 3d ÷ 3e (allocation ratio)
  - 3g: 3c × 3f (foreign share of pro-rata deductions)
- **Line 4a/4b** — Home mortgage interest (if itemizing): allocate per Reg. §1.861-9 (usually based on average asset value)
- **Line 5** — Losses (foreign-source losses reduce this basket's income; net losses recharacterize to other baskets per IRC §904(f))
- **Line 6** — 2 + 3g + 4b + 5
- **Line 7** — 1a − 6 (taxable income from sources outside the US, this basket)

### Part II — Foreign taxes paid or accrued

Two-block table (taxes withheld vs. other) by country letter. Sum to Line 8.

- The user checks **paid** (cash) or **accrued** (book) at top of Part II. **Once accrued is elected, it's binding for all future years (IRC §905(a)).**
- Foreign taxes ineligible for credit (penalties, interest, withholding on US-source income, taxes voluntarily paid above legal liability) do NOT go here. See [`references/non-creditable-taxes.md`](./references/non-creditable-taxes.md).

### Part III — Computing the credit (the §904 limitation)

- **Line 9** = Line 8 (this year's foreign tax, this basket)
- **Line 10** = Carryback / carryforward from prior years, this basket
- **Line 11** = 9 + 10
- **Line 12** = Reduction for international boycott operations (rare)
- **Line 13** = 11 − 12
- **Line 14** = Line 7 (foreign-source taxable income, this basket)
- **Line 15** = Adjustments for qualified-dividend / cap-gain rate differential (line 18 of the Qualified Dividends and Capital Gain Tax Worksheet differential calculation)
- **Line 17** = 14 − 15
- **Line 18** = Total taxable income from all sources (Form 1040 Line 15, with §904(b) adjustments)
- **Line 19** = 17 ÷ 18 (the limitation ratio; cap at 1.000000 if higher)
- **Line 20** = US tax before credits × Line 19
- **Line 21** = Lesser of 13 or 20 (FTC for this basket this year)

### Part IV — Summary of credits from separate Parts III

Used when the filer has multiple baskets. Sum Line 21 from each basket's 1116 onto Lines 22-32, then Line 33 = total. Line 35 = smaller of Line 33 or US tax — final FTC to Schedule 3 Line 1.

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] Line 6 = Line 2 + Line 3g + Line 4b + Line 5
- [ ] Line 7 = Line 1a − Line 6
- [ ] Line 8 = sum of Part II rows
- [ ] Line 11 = Line 9 + Line 10
- [ ] Line 13 = Line 11 − Line 12
- [ ] Line 17 = Line 14 − Line 15
- [ ] Line 19 = Line 17 ÷ Line 18 (rounded to 6 decimals; capped at 1.000000)
- [ ] Line 20 = Line 19 × the user's Form 1040 tax before credits
- [ ] Line 21 = lesser of Line 13 or Line 20
- [ ] If multiple baskets: Line 33 = sum of Line 21 across all 1116s
- [ ] Line 35 ≤ user's Form 1040 tax before credits (FTC can never exceed pre-credit US tax)

### Sanity checks

Surface a warning, do not block:

- [ ] Foreign tax > 50% of foreign income → unusual; check whether the user is paying both source-country and resident-country tax (treaty relief might apply)
- [ ] Line 19 = 1.000000 → all income is foreign-source; verify the user has no US-source items hiding on the return
- [ ] Foreign tax in passive basket but income source is wages → mis-classification; wages go in general basket
- [ ] User reports foreign tax on US-source dividends → not creditable; remove from Form 1116 and pursue treaty refund
- [ ] User has FEIE on Form 2555 AND foreign tax on the same wages → cannot credit foreign tax on excluded income (must allocate)
- [ ] Line 20 is low because Line 18 (total taxable income) is high relative to Line 17 → expected; flag carryforward
- [ ] Line 11 > Line 20 by a large margin → significant unused FTC; track carryover; consider whether deduction is better
- [ ] Filer elects accrued for the first time → confirm filer understands binding nature
- [ ] Single basket, total foreign tax < $300/$600, all passive, all on qualified payee statement → user should have used the de-minimis election in Step 1; back up and verify

### Cross-form checks

- [ ] If FEIE used (Form 2555): exclude that wage income from Line 1a AND the foreign tax allocable to it from Line 8
- [ ] If user has 1099-DIV Box 7: confirm the broker reported the foreign tax, not US backup withholding (Box 4)
- [ ] If foreign-source losses occurred: apply §904(f) recharacterization rules (out of scope; CPA referral if material)
- [ ] Country list on Part I matches country list on Part II (or document the mismatch)

---

## Output format

```markdown
# Form 1116 — DRAFT for tax year YYYY (Category: <basket>)

## Header
Filer name: <name>
SSN/ITIN: <id>
Resident country (Line i): <country>
Category (a-g): <one box checked>
Paid or accrued (h): Paid | Accrued

## Part I — Foreign-source taxable income
Country column A: <country>
Country column B: <country>  (if applicable)
Country column C: <country>  (if applicable)

1a. Gross foreign-source income (per country):
    A: $X,XXX
    B: $X,XXX
    Total: $X,XXX
1b. Compensation included on Line 1a from US payer for services performed
    abroad (if applicable): $X,XXX
2.  Definitely-related deductions:           $X,XXX
3a. Pro-rata: itemized/standard deduction:   $X,XXX
3b. Pro-rata: other deductions:              $X,XXX
3c. 3a + 3b:                                  $X,XXX
3d. Gross foreign-source income (this basket): $X,XXX
3e. Gross income from all sources:            $X,XXX
3f. 3d ÷ 3e:                                  0.XXXXXX
3g. 3c × 3f:                                  $X,XXX
4a. Home mortgage interest:                   $X,XXX
4b. Allocated to foreign:                     $X,XXX
5.  Losses from foreign sources:              $X,XXX
6.  2 + 3g + 4b + 5:                          $X,XXX
7.  1a − 6 (foreign-source taxable income):   $X,XXX

## Part II — Foreign taxes paid or accrued (this basket)
| Country | Foreign currency | USD amount | Date paid/accrued |
|---------|------------------|-----------|-------------------|
| ...     | ...              | ...        | ...               |
8. Total foreign tax (USD):                   $X,XXX

## Part III — §904 limitation
9.  = Line 8:                                 $X,XXX
10. Prior-year carryover (this basket):       $X,XXX
11. 9 + 10:                                   $X,XXX
12. Boycott reduction:                        $0
13. 11 − 12:                                  $X,XXX
14. = Line 7:                                 $X,XXX
15. QD/LTCG adjustment:                       $X,XXX
17. 14 − 15:                                  $X,XXX
18. Total taxable income:                     $X,XXX
19. 17 ÷ 18:                                  0.XXXXXX
20. Line 19 × US tax before credits:          $X,XXX
21. Lesser of 13 or 20 (FTC, this basket):    $X,XXX

## Part IV (only on the summary 1116, if multiple baskets)
22-32. Credits from separate Parts III:       $X,XXX (sum)
33. Total credit:                             $X,XXX
35. Final FTC (Schedule 3 Line 1):            $X,XXX

## Carryover tracking
Unused FTC this year (Line 13 − Line 21), this basket: $X,XXX
  - Carryback: 1 year (consider amending prior year)
  - Carryforward: 10 years (IRC §904(c))

## Required attachments
- [ ] One Form 1116 per basket (separate forms)
- [ ] Schedule B detail for foreign interest/dividends (if applicable)
- [ ] Form 8938 (specified foreign financial assets, if threshold met — separate skill)
- [ ] FBAR / FinCEN 114 (if foreign account aggregate > $10,000 — separate filing)

## Validation summary
- Math: <pass | list failures>
- Sanity: <list any warnings>
- Next steps: <handoff>

## Sources cited in this draft
- IRS Form 1116, Rev. <date>
- IRS Instructions for Form 1116, Rev. <date>
- IRC §901 (foreign tax credit), §904 (limitation), §905 (election timing)
- IRC §904(c) (1-year carryback, 10-year carryforward)
- IRC §904(j)/(k) (de-minimis no-1116 exception)
- Pub. 514 — Foreign Tax Credit for Individuals
- Reg. §1.861-9 (interest expense allocation)
- (any other authority used)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on Form 1116 with examples and edge cases
- [`references/baskets.md`](./references/baskets.md) — How to assign income to passive / general / §901(j) / re-sourced categories
- [`references/coordination-with-2555.md`](./references/coordination-with-2555.md) — When to use credit (1116) vs. exclusion (2555); coordination when using both
- [`references/deduction-allocation.md`](./references/deduction-allocation.md) — Allocating itemized/standard deductions and interest expense to foreign-source income
- [`references/qualified-dividend-adjustment.md`](./references/qualified-dividend-adjustment.md) — Line 15 adjustment for QD/LTCG rate differential
- [`references/non-creditable-taxes.md`](./references/non-creditable-taxes.md) — Foreign taxes that don't qualify for FTC
- [`references/currency.md`](./references/currency.md) — Foreign currency translation methods and IRS rate sources
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Audit-tripping mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for filing the completed Form 1116

## Examples

End-to-end worked drafts. Use as patterns when the user's situation is similar.

- [`examples/de-minimis-investor.md`](./examples/de-minimis-investor.md) — US investor with $1,800 foreign tax in 1099-DIV Box 7 — qualifies for $300 election, no 1116 filed
- [`examples/expat-germany-wages.md`](./examples/expat-germany-wages.md) — US citizen in Germany with $120K wages and $45K German tax — full Form 1116 general basket
- [`examples/multi-basket-investor.md`](./examples/multi-basket-investor.md) — Investor with both passive (foreign dividends) and general (foreign consulting) income, two separate Form 1116s

## Sources

Re-verify each year — the IRS revises forms and instructions each cycle.

- [Form 1116 (latest)](https://www.irs.gov/pub/irs-pdf/f1116.pdf)
- [Instructions for Form 1116 (latest)](https://www.irs.gov/pub/irs-pdf/i1116.pdf)
- [About Form 1116](https://www.irs.gov/forms-pubs/about-form-1116)
- [Publication 514](https://www.irs.gov/publications/p514) — Foreign Tax Credit for Individuals
- [Yearly Average Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates) — for translation
- IRC §901 (allowance of credit), §902 (deemed-paid for corps — out of scope here), §903 (in-lieu-of taxes), §904 (limitation), §904(c) (carryback/carryforward), §904(f) (recharacterization of foreign losses), §904(j)/(k) (de-minimis exception), §905 (election timing)
- Reg. §1.861-8 / §1.861-9 (allocation and apportionment of deductions)
- Rev. Rul. 84-143, Rev. Rul. 70-263 (foreign tax creditability tests)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. International tax has many edge cases (treaty overrides, dual-resident filers, §904(f) recharacterization, §951A inclusions); for material amounts or unusual fact patterns, route the user to a CPA or EA with international expertise.
