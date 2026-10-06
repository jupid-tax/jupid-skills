---
name: form-2555
description: >
  Use this skill when a US citizen or resident alien working abroad needs to
  elect the Foreign Earned Income Exclusion (FEIE) and/or the Foreign
  Housing Exclusion or Deduction on Form 2555. Triggers on phrases like
  "Foreign Earned Income Exclusion", "FEIE", "Form 2555", "expat income
  exclusion", "330-day test", "bona fide residence", "physical presence
  test", "expat housing exclusion", "exclude foreign salary", "$130k expat
  exclusion". Do NOT use this skill for foreign passive/investment income
  (interest, dividends, capital gains — those are not eligible for FEIE;
  use form-1116 for FTC instead); for state tax (some states do NOT honor
  FEIE — California especially); for FBAR / FinCEN 114 reporting (separate
  filing for foreign accounts > $10,000); or for Form 8938 specified foreign
  financial assets (separate form). Coordinate with form-1116 when foreign
  earned income exceeds the FEIE cap or when the user has both wages and
  passive income.
form: Form 2555 (Foreign Earned Income)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f2555.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2555.pdf
---

# Form 2555 — Foreign Earned Income (Exclusion + Housing)

This skill produces an audit-grade draft of Form 2555 for a US citizen or resident alien claiming the Foreign Earned Income Exclusion (FEIE) and, if applicable, the Foreign Housing Exclusion or Deduction. It walks the form line by line, applies the qualification tests (bona fide residence or physical presence), computes the exclusion and housing amounts, validates the result, and emits a deliverable.

The judgment in Form 2555 is mostly in (1) qualification — does the user meet the bona fide residence or physical presence test, (2) what counts as "foreign earned income" vs. ineligible income, (3) housing-amount calculation when the country has a city-specific high-cost adjustment, and (4) coordination with FTC (Form 1116) when income exceeds the FEIE cap.

This skill optimizes for "ask, don't guess." Qualification and income classification are highly user-specific.

The line map was verified against the **2025 Form 2555** (created 5/14/25) and the **2025 Instructions for Form 2555** (Sep 17, 2025), filed in 2026. The IRS revises the form every year; re-check the next revision at https://www.irs.gov/forms-pubs/about-form-2555 before using this map for tax year 2026.

**Companion guide for end users:** [Form 2555 + AI Agent Skill: Foreign Earned Income Exclusion Guide 2026](https://jupid.com/blog/form-2555-foreign-earned-income-exclusion-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2555, "Foreign Earned Income Exclusion", "FEIE", or "expat exclusion"
- The user is a US citizen or resident alien who lived abroad and wants to exclude foreign wages or SE income from US tax
- The user mentions the "330-day test", "physical presence", or "bona fide residence test"
- The user is a digital nomad / remote worker abroad asking how to lower US tax
- The user mentions "expat housing exclusion" or "Form 2555 housing"

Do **not** engage this skill when:

- The user has **passive / investment** foreign income (dividends, interest, capital gains, rental) — FEIE doesn't apply; use `form-1116` (FTC)
- The user is a **non-resident alien** filing Form 1040-NR — FEIE is for US citizens / resident aliens only; use [`form-1040-nr`](../form-1040-nr/SKILL.md)
- The user wants to compare credit vs. exclusion → use the [`form-1116`](../form-1116/SKILL.md) skill alongside this one and run the comparison in [`../form-1116/references/coordination-with-2555.md`](../form-1116/references/coordination-with-2555.md)
- The user has a US-source income concern — FEIE only applies to FOREIGN-source earned income
- The user asks about FBAR / FinCEN 114 (foreign accounts > $10,000) — separate filing, separate form
- The user asks about Form 8938 (specified foreign financial assets) — separate form, separate skill
- The user is in Puerto Rico — different rules (§933, not §911)
- The user's pay is from the U.S. Government as its employee (civilian or military) — it is not foreign earned income; don't file Form 2555 for it (i2555 "Who Qualifies" note; IRC §911(b)(1)(B)(ii))

If the user's situation is mixed (foreign wages + foreign passive income, or foreign wages exceeding the FEIE cap), produce a Form 2555 draft for the qualifying earned income AND use `form-1116` for the rest. Coordinate per [`../form-1116/references/coordination-with-2555.md`](../form-1116/references/coordination-with-2555.md).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The FEIE cap and housing thresholds change annually.
2. **Filer's legal name and SSN/ITIN.** Used in the form header.
3. **Filer's tax home country and city** for the year, and the city where housing expenses were incurred. The city matters for the housing limit (locations listed in Notice 2025-16 for 2025 have higher limits).
4. **Qualification test the user is using**: bona fide residence (Part II) OR physical presence (Part III). Ask if unsure; the rules differ.
5. **Travel dates** if using the physical presence test: a list of every entry/exit between the US and foreign countries during the qualifying 12-month period. The agent must verify 330 full days outside the US.
6. **Date qualification began** if using bona fide residence: the date the filer became a bona fide resident of the foreign country. Bona fide residence requires being a resident for an **entire tax year**, not just any 12-month period.
7. **Foreign earned income**: a structured list of wages, salary, SE income, bonuses, allowances, and noncash compensation earned in the foreign country during the qualifying period. By source and amount in USD.
8. **Foreign housing expenses** if claiming housing exclusion/deduction: rent, utilities (other than telephone), property insurance, repairs, residential parking, etc. Itemized.
9. **Employee vs. self-employed income**: the housing **exclusion** applies to the part of the housing amount paid with employer-provided amounts (wages count, so an employee who pays their own rent still excludes it); the housing **deduction** applies to the part paid with self-employment earnings (Pub. 54, "Foreign Housing Exclusion and Deduction"). Different lines on Form 2555 (line 36 vs. Part IX).
10. **Days in qualifying period during the tax year**. If the user qualified for less than the full tax year (e.g., started bona fide residence in March, or qualified physical presence period was March-following-March), the FEIE and housing limits are pro-rated.
11. **Whether the user has previously made and revoked a §911 election** (Form 2555 lines 6a–6d). If so, the 5-year wait under IRC §911(e)(2) may block re-election. Claiming the foreign tax credit, additional child tax credit, or earned income credit in a later year counts as a revocation (Pub. 54, "Effect of Revoking the Exclusions").
12. **Whether the user wants to coordinate with Form 1116**: if foreign earned income exceeds the FEIE cap, or if there's substantial foreign passive income, route to `form-1116` for the residual.

For each foreign earned income item, also collect:

- Whether the income was paid in foreign currency (translation needed)
- The employer (or client) name and country
- Whether the income is for services performed IN the foreign country (FEIE applies) vs. for services performed elsewhere (FEIE does NOT apply, even if paid by foreign employer)

If the user can't provide travel dates for the physical presence test, **ASK**. Don't guess. The 330-day count is exact — one day short disqualifies.

---

## Workflow

Execute these steps in order.

### Step 1 — Verify the user is eligible at all

The user must be:

- A **US citizen** OR **US resident alien** (passes the Substantial Presence Test or Green Card holder)
- Have a **tax home in a foreign country** (Reg. §1.911-2(b))
- Pass either the **bona fide residence test** OR the **physical presence test**

The user is NOT eligible if:

- They're a non-resident alien
- Their abode is in the United States (e.g., they spent the year on remote work from home in Texas while their employer is in Germany — abode is the US). Exception: service in a combat zone in support of the U.S. Armed Forces (IRC §911(d)(3))
- The income is pay to a U.S. Government employee from the U.S. Government or its agencies — not foreign earned income (IRC §911(b)(1)(B)(ii); i2555 "Who Qualifies")
- The time and income are from Cuba in violation of U.S. travel restrictions — those days don't count toward either test and that income isn't foreign earned income (IRC §911(d)(8); i2555 "Travel to Cuba")

If ineligible, stop and route to `form-1116` instead (FTC may apply on the same income).

### Step 2 — Determine which qualifying test applies

**Bona Fide Residence Test (Part II of Form 2555)**:
- The filer is a bona fide resident of a foreign country (or countries) for an uninterrupted period that includes an **entire tax year** (Jan 1 to Dec 31). Once that is met, the partial first and last years also qualify, prorated by days (IRC §911(d)(1)(A); i2555 line 31 example)
- Subjective test: based on intent, integration into local community, length of stay, type of quarters, family ties, etc.
- US citizens, and resident aliens who are citizens or nationals of a country with a US income tax treaty in effect (i2555 Part II)
- More flexible on US visits — bona fide residents can return to the US for vacation, business, or family without losing the qualification, as long as foreign tax home is maintained

**Physical Presence Test (Part III of Form 2555)**:
- The filer is physically present in foreign countries for **at least 330 full days during any 12 consecutive months**
- Objective test: count days
- Available to US citizens AND resident aliens
- Strict on travel: a full day is midnight to midnight in a foreign country. Time on or over international waters when leaving or returning to the US does not count; travel between foreign countries loses days only if the part outside any foreign country takes 24 hours or more (IRS physical presence test page, "Change of location")

The 12-month period for physical presence does NOT have to be the calendar tax year. The user picks any 12-month window that contains 330+ full foreign days (line 16 must show both dates; the period must include part of the tax year). The exclusion is then pro-rated to the days of the qualifying period that fall in the tax year.

See [`references/qualifying-tests.md`](./references/qualifying-tests.md) for detailed application.

### Step 3 — Compute foreign earned income (FEI)

Foreign earned income includes (per IRC §911(b) and Reg. §1.911-3):

- Wages, salaries, professional fees for services performed in a foreign country
- SE income from services performed in a foreign country
- Bonuses, commissions, allowances, noncash compensation (housing, meals, lodging, car) at fair market value
- Differential pay
- Royalties earned for services (e.g., author advances on services performed abroad)

Foreign earned income does NOT include:

- Pensions and annuities (including Social Security); amounts received after the end of the tax year following the year the services were performed; amounts included because of employer contributions to a nonexempt trust or nonqualified annuity (IRC §911(b)(1)(B))
- Investment income (interest, dividends, capital gains), alimony
- Income for work in international waters or airspace (not a foreign country — i2555 "Foreign country")
- Income earned while the abode was in the US
- Income earned in Cuba in violation of U.S. travel restrictions (IRC §911(d)(8))
- US government pay to its employees, or any pay for work physically performed in the US (line 14 column (d) / line 18 column (f))

**Self-employment income (line 20a).** If capital is not a material income-producing factor, the entire gross income of the business is earned income; if both services and capital are material, earned income is a reasonable amount for services, capped at 30% of the filer's share of net profits after the deductible part of SE tax (i2555 line 20). The Schedule C expenses and the deductible part of SE tax that are allocable to the excluded income go on line 44 (i2555 line 44; Pub. 54 ch. 5). Ask for gross receipts and expenses, not only net profit.

Compute the total FEI. This is the amount eligible for exclusion (capped at the annual limit).

### Step 4 — Apply the FEIE cap

The FEIE cap is set annually under IRC §911(b)(2)(D). Year-dependent; re-check the Rev. Proc. at https://www.irs.gov/InflationAdjustment each year:

- 2024: $126,500
- 2025: $130,000 (Rev. Proc. 2024-40 §2.39; 2025 Form 2555 line 37)
- 2026: $132,900 (Rev. Proc. 2025-32 §4.39)

If the user qualified for the entire tax year, exclude up to the cap. If the user qualified for less than the full year (Step 2), pro-rate (Form 2555 lines 38–40):

```
Line 39 = qualifying days in tax year / days in tax year (365, or 366 in a leap year), rounded to at least 3 decimals
Line 40 = Annual cap × line 39
```

Excludable FEI (line 42) = lesser of (line 40, line 27 − housing exclusion on line 36).

### Step 5 — Compute the foreign housing exclusion or deduction

If the user has foreign housing costs above a base amount AND meets either qualifying test, they can also exclude (or deduct, if SE) housing costs.

**Base housing amount** (line 32) = 16% of the FEIE cap, computed per day × qualifying days in the tax year (IRC §911(c)(1)(B))
- 2025: $56.99 × line 31 days; $20,800 if 365 days (2025 Form 2555 line 32)
- 2026: $21,264 for a full year (Notice 2026-25 §2)

**Limit on housing expenses** (line 29b) = 30% of the FEIE cap per day × qualifying days, raised for locations listed in the annual IRS notice (IRC §911(c)(2))
- 2025: $39,000 full year / $106.85 per day for unlisted locations (i2555 line 29b); listed locations per Notice 2025-16 (e.g., London $67,000, Hong Kong $114,300, Mexico City $47,900, Lisbon $40,000)
- 2026: $39,870 full year for unlisted locations; listed locations per Notice 2026-25 (e.g., London $68,600, Lisbon $44,800)
- A filer may elect to apply the 2026 limits to 2025 housing expenses (Notice 2026-25 §4). Ask before using it.

**Housing amount** (line 33) = lesser of (housing expenses, limit) − base amount.

The **exclusion** (Part VI, line 36) covers the share of the housing amount paid with employer-provided amounts: line 33 × (line 34 employer-provided amounts ÷ line 27 foreign earned income). Wages count as employer-provided amounts, so a filer with no self-employment income excludes the whole housing amount even if they pay rent themselves (Pub. 54, "Foreign Housing Exclusion").

The **deduction** (Part IX, line 50) covers the share paid with self-employment earnings, limited to foreign earned income not already excluded (line 47; IRC §911(c)(4)(B)). It goes on Schedule 1 line 24j. Excess carries over one year only (IRC §911(c)(4)(C)).

See [`references/housing.md`](./references/housing.md) for detailed mechanics, city tables, and worked examples.

### Step 6 — Run the FEIE election

The election is made by **filing Form 2555 attached to the return** (Form 1040, 1040-SR, or 1040-X) for the year of election, usually on a timely filed return including extensions (i2555 "Choosing the Exclusion(s)"). Once made, it applies to all subsequent years until revoked. To revoke, attach a statement to the return for the first year the filer doesn't want the exclusion. No revocation is needed for a year with no foreign earned income.

**5-year re-election lock-out**: once revoked, the filer cannot re-elect FEIE for the next 5 tax years without IRS approval, requested as a ruling (IRC §911(e)(2); Pub. 54, "Effect of Revoking the Exclusions"). Claiming the foreign tax credit, additional child tax credit, or earned income credit in a later year is treated as a revocation (Pub. 54, same section). This trips up filers who switch to FTC and later want to switch back.

**First-year timing**: if the filer will not meet either test until after the return's due date (including the June 15 automatic extension), they can file Form 2350 for a special extension or file without the exclusion and amend with Form 1040-X after qualifying (i2555 "When to claim the exclusion(s)").

### Step 7 — Compute the tax-stacking effect

The exclusion does NOT mean the filer pays $0 US tax. The non-excluded income (passive income, US-source income, FEI above the cap) is taxed at the rates that would apply if the excluded income WAS included. This is the "stacking rule" of IRC §911(f).

Mechanic: the Foreign Earned Income Tax Worksheet (2025 Instructions for Form 1040, line 16) applies. The tax on (taxable income + Form 2555 lines 45 and 50) is computed; then the tax on (lines 45 and 50 alone) is subtracted; the difference is the actual tax. If Form 1040 line 15 (taxable income) is zero, the worksheet is skipped. Because tax brackets are progressive, this effectively keeps the marginal rate applicable to the residual income.

For a single 2025 filer with $130,000 wages all excluded and $30,000 of interest income:
- Taxable income = $30,000 − $15,750 standard deduction = $14,250
- Without stacking: taxed in the 10% and 12% brackets
- With stacking: the $14,250 sits on top of the excluded $130,000, inside the 24% bracket ($103,350–$197,300, Rev. Proc. 2024-40 Table 3), so all of it is taxed at 24%

This rule prevents double benefit. Tax software handles it automatically. Manual filers must use the Form 1040 instructions worksheet.

### Step 8 — Coordinate with Form 1116 (if applicable)

If foreign earned income exceeds the FEIE cap, the EXCESS is not excluded. Foreign tax allocable to that excess (and to passive foreign income) can be credited via Form 1116; tax allocable to excluded income cannot (i2555 "Foreign tax credit or deduction"; Pub. 514). See [`../form-1116/references/coordination-with-2555.md`](../form-1116/references/coordination-with-2555.md).

If the user has foreign passive income (dividends from a foreign brokerage), FEIE does NOT apply; use Form 1116 for that income.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms / actions:

- **Form 2555 line 45 (housing exclusion + FEIE − line 44)** → Schedule 1 line 8d as a negative amount → Schedule 1 line 10 → Form 1040 line 8 (i2555 line 45). Form 1040 line 1z wages are not reduced directly
- **Form 2555 line 50 (housing deduction)** → Schedule 1 line 24j
- **Foreign Earned Income Tax Worksheet** → computes Form 1040 line 16 with stacking; for AMT use the worksheet in the Form 6251 instructions
- **Self-employment tax** → STILL OWED on excluded SE income (net earnings from self-employment are computed without the §911 exclusion, IRC §1402(a)(11)) — see [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md)
- **Credits lost**: no earned income credit and no additional child tax credit if either exclusion or the housing deduction is claimed; IRA compensation excludes excluded income (i2555 "Choosing the Exclusion(s)"; Pub. 54 ch. 5)
- **Form 1116** if there's foreign tax to credit on non-excluded portions or passive income
- **State tax** — some states do not follow the exclusion; California is the main one and taxes residents on the full income. See [`references/state-tax-coordination.md`](./references/state-tax-coordination.md)
- **FBAR / FinCEN 114** — separate filing if foreign account aggregate exceeds $10,000
- **Form 8938** — separate form if specified foreign financial assets exceed thresholds

### Step 12 — File the return

Hand off to [`filing.md`](./filing.md) for filing channel selection. Paper returns with Form 2555 go to the special international addresses, not the state-of-residence addresses (i2555 "Where To File").

---

## Line-by-line guidance

Full reference in [`references/line-by-line.md`](./references/line-by-line.md), built from the 2025 form text. High-level rules below.

### Part I — General Information (lines 1–9)

- **Line 1** — Foreign address (full, with country). **Line 2** — Occupation
- **Line 3** — Employer's name; **4a/4b** — employer's U.S. and foreign addresses
- **Line 5** — Employer is: (a) foreign entity, (b) U.S. company, (c) self, (d) foreign affiliate of a U.S. company, (e) other
- **Lines 6a–6d** — Last year Form 2555/2555-EZ was filed; never-filed box; ever revoked either exclusion; type and year of revocation (5-year lock-out check)
- **Line 7** — Country of citizenship/nationality
- **Lines 8a–8b** — Separate foreign residence for family because of adverse conditions at the tax home (second foreign household): city, country, days
- **Line 9** — Tax home(s) and date(s) established

Complete either Part II or Part III, never both.

### Part II — Bona Fide Residence Test (lines 10–15e)

- **Line 10** — Date bona fide residence began and ended ("Continues" if ongoing)
- **Line 11** — Living quarters: purchased house, rented house or apartment, rented room, quarters furnished by employer
- **Lines 12a–12b** — Family lived with the filer abroad; who and when
- **Lines 13a–13b** — Statement of nonresidence to foreign authorities; required to pay that country's income tax. Yes on 13a + No on 13b = not a bona fide resident
- **Line 14** — U.S. presence table: dates arrived/left, days in U.S. on business, income earned in U.S. on business (column (d) stays out of Part IV)
- **Lines 15a–15e** — Employment-length terms, visa type, visa limits, U.S. home maintained and its occupants

### Part III — Physical Presence Test (lines 16–18)

- **Line 16** — 12-month period (both dates; includes part of the tax year)
- **Line 17** — Principal country of employment
- **Line 18** — Travel table: country (including U.S.), date arrived, date left, full days present, days in U.S. on business, income earned in U.S. on business (column (f) stays out of Part IV)

### Part IV — All Taxpayers (lines 19–26)

- **Line 19** — Wages, salaries, bonuses, commissions
- **Lines 20a–20b** — Allowable share of income for personal services in a business/profession or a partnership (self-employment income; 30% cap only when capital is a material income-producing factor)
- **Lines 21a–21d** — Noncash income: home (lodging), meals, car, other (market value; attach statement)
- **Lines 22a–22g** — Allowances: cost of living, family, education, home leave, quarters, other; 22g = total
- **Line 23** — Other foreign earned income
- **Line 24** — Lines 19 through 21d + 22g + 23
- **Line 25** — §119 meals and lodging included on line 24 that are excludable
- **Line 26** — Line 24 − line 25 = foreign earned income

### Part V — All Taxpayers (line 27)

- **Line 27** — Amount from line 26; then answer whether the filer claims the housing exclusion or deduction

### Part VI — Housing Exclusion and/or Deduction (lines 28–36)

- **Line 28** — Qualified housing expenses
- **Lines 29a–29b** — Location (only if listed in Notice 2025-16) and limit on housing expenses ($39,000 full year unlisted; otherwise the Limit on Housing Expenses Worksheet)
- **Line 30** — Smaller of 28 or 29b
- **Line 31** — Days of the qualifying period in the tax year
- **Line 32** — $56.99 × line 31 ($20,800 if 365)
- **Line 33** — Line 30 − line 32 (zero or less: stop Part VI and skip Part IX)
- **Line 34** — Employer-provided amounts (wages count). All-SE filers skip 34–35 and enter 0 on line 36
- **Line 35** — Line 34 ÷ line 27, at least 3 decimals, max 1.000
- **Line 36** — Housing exclusion = line 33 × line 35, not more than line 34

### Part VII — Foreign Earned Income Exclusion (lines 37–42)

- **Line 37** — $130,000 (2025)
- **Line 38** — Days (line 31 if Part VI was completed)
- **Line 39** — 1.000, or line 38 ÷ days in the tax year (at least 3 decimals)
- **Line 40** — Line 37 × line 39
- **Line 41** — Line 27 − line 36
- **Line 42** — Smaller of line 40 or line 41

### Part VIII — Exclusions Total (lines 43–45)

- **Line 43** — Line 36 + line 42
- **Line 44** — AGI deductions allocable to excluded income (e.g., the deductible part of SE tax, Schedule C expenses), attach computation; definitely related items only (IRC §911(d)(6))
- **Line 45** — Line 43 − line 44 → Schedule 1 line 8d (negative)

### Part IX — Housing Deduction (lines 46–50)

Only if line 33 > line 36 AND line 27 > line 43.

- **Line 46** — Line 33 − line 36
- **Line 47** — Line 27 − line 43
- **Line 48** — Smaller of 46 or 47
- **Line 49** — Carryover from 2024 (Housing Deduction Carryover Worksheet)
- **Line 50** — Line 48 + line 49 → Schedule 1 line 24j

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] Line 22g = 22a through 22f; line 24 = lines 19 through 21d + 22g + 23; line 26 = line 24 − line 25; line 27 = line 26
- [ ] Line 30 = smaller of line 28 or line 29b; line 29b = $39,000, or the Notice 2025-16 amount (or worksheet result) for the location and days
- [ ] Line 32 = $56.99 × line 31 ($20,800 if line 31 is 365); line 33 = line 30 − line 32
- [ ] Line 35 = line 34 ÷ line 27, not over 1.000; line 36 = line 33 × line 35, not over line 34 (0 if all income is SE income)
- [ ] Line 38 = line 31 (when Part VI is completed); line 39 = line 38 ÷ days in the tax year, at least 3 decimals; line 40 = $130,000 × line 39
- [ ] Line 41 = line 27 − line 36; line 42 = smaller of line 40 or line 41
- [ ] Line 43 = line 36 + line 42; line 45 = line 43 − line 44, and line 45 equals the negative entry on Schedule 1 line 8d
- [ ] Part IX only if line 33 > line 36 and line 27 > line 43; line 48 = smaller of (line 33 − line 36) and (line 27 − line 43); line 50 = line 48 + line 49 = Schedule 1 line 24j
- [ ] Lines 45 + 50 do not exceed line 27 (IRC §911(d)(7))
- [ ] If physical presence test: sum of full days in foreign countries in the line 16 period ≥ 330
- [ ] If bona fide residence test: the uninterrupted residence on line 10 includes at least one entire tax year

### Sanity checks

Surface a warning, do not block:

- [ ] Filer claims abode in the US (working remotely from Texas) → FEIE disqualified; route to FTC
- [ ] Travel dates show > 35 days in the US during the qualifying 12-month period → physical presence test fails (need ≥ 330 foreign full days)
- [ ] Foreign earned income includes pension or investment income → ineligible portion; revise Line 24
- [ ] User claims FEIE but plans to take FTC on the same wages → cannot double dip; allocate
- [ ] Line 29b above $39,000 (2025 full year) without a location listed in Notice 2025-16 (or Notice 2026-25 under its §4 election) → over-claim; verify the table
- [ ] User SE income excluded but didn't compute SE tax on Schedule SE → SE tax STILL OWED on excluded SE income; common trap
- [ ] User changed countries mid-year → bona fide residence may break; verify continuous foreign tax home
- [ ] User previously revoked FEIE within last 5 years (line 6c Yes), or claimed FTC, ACTC, or EIC in a year after electing → 5-year lock-out under §911(e)(2); cannot re-elect without IRS approval
- [ ] State of residence is California (or another state that does not follow the exclusion) → warn user; see [`references/state-tax-coordination.md`](./references/state-tax-coordination.md)

### Cross-form checks

- [ ] If FEIE used: ensure deductions allocable to excluded income are NOT also on Schedule A or Schedule C (IRC §911 disallowance)
- [ ] If foreign tax paid on excluded income: do NOT credit or deduct it on Form 1116 / Schedule A (i2555 "Foreign tax credit or deduction"; Reg. §1.911-6)
- [ ] If foreign earned income > FEIE cap: surface that residual is taxable; coordinate with Form 1116 if foreign tax was paid on it
- [ ] SE income excluded under FEIE: confirm Schedule SE is filed for SE tax (not excluded by §911)
- [ ] If housing is employer-provided: its fair rental value is on line 21a (or the cash allowance on line 22e) unless excludable under §119 on line 25, and the same value is in line 28 housing expenses
- [ ] No earned income credit or additional child tax credit on the return; IRA contribution compensation excludes the excluded income (i2555; Pub. 54 ch. 5)
- [ ] Form 1040 line 16 tax computed with the Foreign Earned Income Tax Worksheet whenever line 15 is more than zero

---

## Output format

```markdown
# Form 2555 — DRAFT for tax year YYYY

## Header
Filer name: <name>
SSN: <id>

## Part I — General Information
1. Foreign address: <address, country>
2. Occupation: <occupation>
3. Employer's name: <name>
4a. Employer's U.S. address: <address or N/A>
4b. Employer's foreign address: <address or N/A>
5. Employer is: <a foreign entity | b U.S. company | c Self | d foreign affiliate of U.S. company | e Other: ...>
6a. Last year Form 2555/2555-EZ filed: YYYY | 6b. Never filed: [ ]
6c. Ever revoked either exclusion: Yes | No
6d. Type and year of revocation: <...> (5-year lock-out check)
7. Country of citizenship/nationality: <country>
8a. Separate foreign residence for family (adverse conditions): Yes | No
8b. City, country, days: <...>
9. Tax home(s) and date(s) established: <city, country, MM/DD/YYYY>

## Part II — Bona Fide Residence (only if using this test)
10. Began MM/DD/YYYY, ended MM/DD/YYYY | Continues
11. Living quarters: <a | b | c | d>
12a. Family lived with you abroad: Yes | No — 12b. <who, period>
13a. Statement of nonresidence submitted: Yes | No
13b. Required to pay income tax there: Yes | No
14. U.S. presence:
| Date arrived in U.S. | Date left U.S. | Days in U.S. on business | Income earned in U.S. on business |
|----------------------|----------------|--------------------------|-----------------------------------|
15a–15e. <contract terms; visa type; visa limit Yes/No; U.S. home Yes/No; address/occupants>

## Part III — Physical Presence (only if using this test)
16. 12-month period: MM/DD/YYYY through MM/DD/YYYY
17. Principal country of employment: <country>
18. Travel:
| Country (incl. U.S.) | Date arrived | Date left | Full days present | Days in U.S. on business | Income earned in U.S. on business |
|----------------------|--------------|-----------|-------------------|--------------------------|-----------------------------------|
| <c> | MM/DD/YYYY | MM/DD/YYYY | XXX | X | $X |
**Total full days in foreign countries: ≥ 330**

## Part IV — Foreign earned income
19. Wages, salaries, bonuses, commissions:          $XX,XXX
20a. Personal services in a business or profession: $XX,XXX
20b. Partnership share:                              $X
21a. Noncash: home (lodging):                        $X,XXX
21b. Noncash: meals:                                 $X
21c. Noncash: car:                                   $X
21d. Other property or facilities:                   $X
22a–22f. Allowances (COLA, family, education, home leave, quarters, other): $X,XXX
22g. Total allowances:                               $X,XXX
23. Other foreign earned income:                     $X
24. Total (19 through 21d, 22g, 23):                 $XX,XXX
25. Excludable §119 meals and lodging:               $X
26. Foreign earned income (24 − 25):                 $XX,XXX

## Part V
27. Amount from line 26:                             $XX,XXX
Housing exclusion or deduction claimed: Yes | No

## Part VI — Housing (if claimed)
28. Qualified housing expenses:                      $X,XXX
    | Type | Amount |
    |------|--------|
    | Rent | $X,XXX |
    | Utilities (excl. telephone) | $X,XXX |
    | Insurance / parking / repairs / furniture rental | $X,XXX |
29a. Location (only if listed in Notice 2025-16):    <city, country>
29b. Limit on housing expenses:                      $XX,XXX (source: $39,000 default | Notice 2025-16 | Notice 2026-25 §4 election)
30. Smaller of 28 or 29b:                            $X,XXX
31. Qualifying days in tax year:                     XXX
32. $56.99 × line 31 (or $20,800):                   $XX,XXX
33. Line 30 − line 32:                               $X,XXX
34. Employer-provided amounts:                       $XX,XXX (SE only: skip)
35. Line 34 ÷ line 27:                               X.XXX
36. Housing exclusion:                               $X,XXX

## Part VII — Foreign Earned Income Exclusion
37. Maximum exclusion:                               $130,000
38. Days:                                            XXX
39. Ratio:                                           X.XXX
40. Line 37 × line 39:                               $XXX,XXX
41. Line 27 − line 36:                               $XXX,XXX
42. FEIE (smaller of 40 or 41):                      $XXX,XXX

## Part VIII
43. Line 36 + line 42:                               $XXX,XXX
44. Deductions allocable to excluded income:         $X,XXX (computation attached)
45. Line 43 − line 44 → Schedule 1 line 8d:          ($XXX,XXX)

## Part IX — Housing deduction (only if line 33 > line 36 and line 27 > line 43)
46. Line 33 − line 36:                               $X,XXX
47. Line 27 − line 43:                               $X,XXX
48. Smaller of 46 or 47:                             $X,XXX
49. Carryover from prior year:                       $X
50. Housing deduction → Schedule 1 line 24j:         $X,XXX

## Required attachments
- [x] Form 2555 (this draft)
- [ ] Statement for the June 15 automatic extension, if used (i2555 "When To File")
- [ ] Line 44 computation; line 21 noncash valuation statement; line 14(d)/18(f) computation, if any
- [ ] Form 1116 if foreign tax to credit on non-excluded portions (separate skill)
- [ ] Schedule SE if SE income excluded — SE TAX STILL OWED (common trap)
- [ ] Form 8938 if specified foreign financial assets exceed threshold
- [ ] FBAR / FinCEN 114 separately (not attached) if foreign account aggregate > $10,000

## Validation summary
- Math: <pass | list failures>
- Sanity: <list any warnings>
- Tax-stacking note: residual income (passive, US-source, or FEI above cap) is taxed at the rate that would apply if FEI were NOT excluded. Use the Foreign Earned Income Tax Worksheet (skip it if Form 1040 line 15 is zero).
- Next steps: <handoff>

## Sources cited in this draft
- IRS Form 2555 (YYYY)
- IRS Instructions for Form 2555 (YYYY)
- IRC §911 (FEIE + housing exclusion/deduction)
- IRC §911(b)(2)(D) (annual exclusion cap)
- IRC §911(c) (housing exclusion/deduction)
- IRC §911(d)(6) (no double benefit; line 44)
- IRC §911(e)(2) (5-year revocation lock-out)
- IRC §911(d)(3) (tax home and abode)
- IRC §911(f) (tax-stacking rule)
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
- Reg. §1.911-2 (definitions)
- Rev. Proc. — current-year FEIE cap (2025: Rev. Proc. 2024-40; 2026: Rev. Proc. 2025-32)
- Notice — current-year housing limits by location (2025: Notice 2025-16; 2026: Notice 2026-25)
- (any other authority used)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on Form 2555 with examples and edge cases
- [`references/qualifying-tests.md`](./references/qualifying-tests.md) — Bona fide residence vs. physical presence; how to verify; tie-breakers
- [`references/housing.md`](./references/housing.md) — Housing exclusion/deduction mechanics, base/max amounts, city-specific high-cost adjustments
- [`references/state-tax-coordination.md`](./references/state-tax-coordination.md) — States that do not follow the exclusion (California first); domicile questions to ask
- [`../form-1116/references/coordination-with-2555.md`](../form-1116/references/coordination-with-2555.md) — When to use exclusion vs. credit; coordination when using both (lives in the form-1116 skill)
- [`../schedule-se/SKILL.md`](../schedule-se/SKILL.md) — SE tax on excluded SE income (FEIE excludes income tax, not SE tax); the worked trap is in [`examples/se-consultant-mexico.md`](./examples/se-consultant-mexico.md)
- [`filing.md`](./filing.md) — Filing channels, addresses, extensions, and browser-automation steps for the completed return

## Examples

End-to-end worked drafts. Use as patterns when the user's situation is similar.

- [`examples/digital-nomad-330-day.md`](./examples/digital-nomad-330-day.md) — Remote worker meeting physical presence test ($95K excluded)
- [`examples/london-employer-housing.md`](./examples/london-employer-housing.md) — Bona fide resident in London with employer-paid housing (FEIE + housing exclusion)
- [`examples/se-consultant-mexico.md`](./examples/se-consultant-mexico.md) — SE consultant in Mexico (FEIE on SE income, but SE tax still owed — the trap)

## Sources

Re-verify each year — the IRS revises forms, instructions, and FEIE cap each cycle.

- [Form 2555 (latest)](https://www.irs.gov/pub/irs-pdf/f2555.pdf)
- [Instructions for Form 2555 (latest)](https://www.irs.gov/pub/irs-pdf/i2555.pdf)
- [About Form 2555](https://www.irs.gov/forms-pubs/about-form-2555)
- [Form 2555 + AI Agent Skill: Foreign Earned Income Exclusion Guide 2026](https://jupid.com/blog/form-2555-foreign-earned-income-exclusion-2026) — Jupid's narrative companion to this skill, written for human readers
- [Publication 54](https://www.irs.gov/publications/p54) (Rev. December 2025) — Tax Guide for U.S. Citizens and Resident Aliens Abroad
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Foreign Earned Income Tax Worksheet (line 16); Form 2555 filer mailing addresses
- [IRS: Foreign earned income exclusion — physical presence test](https://www.irs.gov/individuals/international-taxpayers/foreign-earned-income-exclusion-physical-presence-test) — full-day and travel rules
- IRC §911 (foreign earned income exclusion + housing)
- IRC §911(b)(2)(D) (annual exclusion cap, indexed)
- IRC §911(c)(1)–(4) (housing cost amount, 16% base, 30% limit and geographic adjustment, housing expenses, deduction and 1-year carryover)
- IRC §911(d)(1) (qualified individual; bona fide residence and physical presence tests)
- IRC §911(d)(3) (tax home and "abode" rule)
- IRC §911(e)(1)/(2) (election; 5-year revocation lock-out)
- IRC §911(d)(4) (waiver for war / civil unrest), §911(d)(6) (no double benefit), §911(d)(8) (restricted countries)
- IRC §911(f) (tax-stacking rule)
- IRC §1402(a)(11) (SE income computed without the §911 exclusion)
- Reg. §1.911-1 through §1.911-7 (mechanics)
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) §3.39 (2025 FEIE cap $130,000)
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §3.39 (2026 FEIE cap $132,900)
- [Notice 2025-16](https://www.irs.gov/pub/irs-drop/n-25-16.pdf) (2025 housing limits by location)
- [Notice 2026-25](https://www.irs.gov/pub/irs-drop/n-26-25.pdf) (2026 housing limits: base $21,264, standard limit $39,870; §4 option to apply them to 2025)
- [Rev. Proc. 2026-16](https://www.irs.gov/pub/irs-drop/rp-26-16.pdf) (countries qualifying for the 2025 waiver of time requirements)
- US Totalization Agreements list (SSA.gov/international; also listed in the Schedule SE instructions) — for SE tax interactions

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. International tax has many edge cases (treaty overrides, dual-resident filers, mid-year residency changes, partial-year qualification); for material amounts or unusual fact patterns, route the user to a CPA or EA with international expertise.
