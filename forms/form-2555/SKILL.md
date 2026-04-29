---
name: form-2555
description: >
  Use this skill when a US citizen or resident alien working abroad needs to
  elect the Foreign Earned Income Exclusion (FEIE) and/or the Foreign
  Housing Exclusion or Deduction on Form 2555. Triggers on phrases like
  "Foreign Earned Income Exclusion", "FEIE", "Form 2555", "expat income
  exclusion", "330-day test", "bona fide residence", "physical presence
  test", "expat housing exclusion", "exclude foreign salary", "$120k expat
  exclusion". Do NOT use this skill for foreign passive/investment income
  (interest, dividends, capital gains — those are not eligible for FEIE;
  use form-1116 for FTC instead); for state tax (most states do NOT honor
  FEIE — California especially); for FBAR / FinCEN 114 reporting (separate
  filing for foreign accounts > $10,000); or for Form 8938 specified foreign
  financial assets (separate form). Coordinate with form-1116 when foreign
  earned income exceeds the FEIE cap or when the user has both wages and
  passive income.
form: Form 2555 (Foreign Earned Income)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f2555.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2555.pdf
---

# Form 2555 — Foreign Earned Income (Exclusion + Housing)

This skill produces an audit-grade draft of Form 2555 for a US citizen or resident alien claiming the Foreign Earned Income Exclusion (FEIE) and, if applicable, the Foreign Housing Exclusion or Deduction. It walks the form line by line, applies the qualification tests (bona fide residence or physical presence), computes the exclusion and housing amounts, validates the result, and emits a deliverable.

The judgment in Form 2555 is mostly in (1) qualification — does the user meet the bona fide residence or physical presence test, (2) what counts as "foreign earned income" vs. ineligible income, (3) housing-amount calculation when the country has a city-specific high-cost adjustment, and (4) coordination with FTC (Form 1116) when income exceeds the FEIE cap.

This skill optimizes for "ask, don't guess." Qualification and income classification are highly user-specific.

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
- The user is a **non-resident alien** filing Form 1040-NR — FEIE is for US citizens / resident aliens only
- The user wants to compare credit vs. exclusion → use `form-1116` skill alongside this one and run the comparison in [`references/coordination-with-1116.md`](./references/coordination-with-1116.md)
- The user has a US-source income concern — FEIE only applies to FOREIGN-source earned income
- The user asks about FBAR / FinCEN 114 (foreign accounts > $10,000) — separate filing, separate form
- The user asks about Form 8938 (specified foreign financial assets) — separate form, separate skill
- The user is in Puerto Rico — different rules (§933, not §911)
- The user is a US military member abroad — military pay is treated specially; the §911 abode-in-the-US disqualifier may apply

If the user's situation is mixed (foreign wages + foreign passive income, or foreign wages exceeding the FEIE cap), produce a Form 2555 draft for the qualifying earned income AND use `form-1116` for the rest. Coordinate per [`references/coordination-with-1116.md`](./references/coordination-with-1116.md).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The FEIE cap and housing thresholds change annually.
2. **Filer's legal name and SSN/ITIN.** Used in the form header.
3. **Filer's tax home country and city** for the year. The city matters for housing exclusion (some cities have higher housing caps).
4. **Qualification test the user is using**: bona fide residence (Part II) OR physical presence (Part III). Ask if unsure; the rules differ.
5. **Travel dates** if using the physical presence test: a list of every entry/exit between the US and foreign countries during the qualifying 12-month period. The agent must verify 330 full days outside the US.
6. **Date qualification began** if using bona fide residence: the date the filer became a bona fide resident of the foreign country. Bona fide residence requires being a resident for an **entire tax year**, not just any 12-month period.
7. **Foreign earned income**: a structured list of wages, salary, SE income, bonuses, allowances, and noncash compensation earned in the foreign country during the qualifying period. By source and amount in USD.
8. **Foreign housing expenses** if claiming housing exclusion/deduction: rent, utilities (other than telephone), property insurance, repairs, residential parking, etc. Itemized.
9. **Employer-provided housing** vs. **self-paid housing**: determines whether the user takes the housing **exclusion** (employer-provided) or the housing **deduction** (self-employed pays themselves). Different lines on Form 2555.
10. **Days in qualifying period during the tax year**. If the user qualified for less than the full tax year (e.g., started bona fide residence in March, or qualified physical presence period was March-following-March), the FEIE and housing limits are pro-rated.
11. **Whether the user has previously made and revoked a §911 election**. If so, the 5-year wait under IRC §911(e)(2) may block re-election.
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
- Their abode is in the United States (e.g., they spent the year on remote work from home in Texas while their employer is in Germany — abode is the US)
- They're a federal employee whose service abroad qualifies (some restrictions)
- They're working in a §901(j) sanctioned country (Iran, North Korea, Sudan currently) — FEIE not allowed

If ineligible, stop and route to `form-1116` instead (FTC may apply on the same income).

### Step 2 — Determine which qualifying test applies

**Bona Fide Residence Test (Part II of Form 2555)**:
- The filer is a bona fide resident of a foreign country (or countries) for an **entire tax year** (Jan 1 to Dec 31, no exceptions)
- Subjective test: based on intent, integration into local community, length of stay, type of quarters, family ties, etc.
- US citizens only (resident aliens cannot use this test unless they're treaty residents of a country with a US tax treaty)
- More flexible on US visits — bona fide residents can return to the US for vacation, business, or family without losing the qualification, as long as foreign tax home is maintained

**Physical Presence Test (Part III of Form 2555)**:
- The filer is physically present in foreign countries for **at least 330 full days during any 12 consecutive months**
- Objective test: count days
- Available to US citizens AND resident aliens
- Strict on travel: a single day counted toward US presence breaks a "full day" abroad. Travel days (in transit between US and abroad over international airspace/waters) do NOT count as foreign days

The 12-month period for physical presence does NOT have to be the calendar tax year. The user picks any 12-month window that contains 330+ foreign days. The exclusion is then pro-rated to the portion of the tax year covered.

See [`references/qualifying-tests.md`](./references/qualifying-tests.md) for detailed application.

### Step 3 — Compute foreign earned income (FEI)

Foreign earned income includes (per IRC §911(b) and Reg. §1.911-3):

- Wages, salaries, professional fees for services performed in a foreign country
- SE income from services performed in a foreign country
- Bonuses, commissions, allowances, noncash compensation (housing, meals, lodging, car) at fair market value
- Differential pay
- Royalties earned for services (e.g., author advances on services performed abroad)

Foreign earned income does NOT include:

- Pension, annuity, deferred compensation
- Investment income (interest, dividends, capital gains)
- Income from working in international waters or airspace (depends on facts)
- Income earned while the abode was in the US
- Income earned in a §901(j) sanctioned country
- US government pay or pay from a US-based employer for work physically performed in the US

Compute the total FEI. This is the amount eligible for exclusion (capped at the annual limit).

### Step 4 — Apply the FEIE cap

The FEIE cap is set annually by IRC §911(b)(2)(D). Recent figures (verify the current year against the most recent IRS Rev. Proc.):

- 2024: $126,500
- 2025: $130,000
- **2026: announced by IRS in fall 2025 — verify Rev. Proc. before relying**

If the user qualified for the entire tax year, exclude up to the cap. If the user qualified for less than the full year (Step 2), pro-rate:

```
Pro-rated cap = Annual cap × (qualifying days in tax year / 365)
```

Excludable FEI = lesser of (Total FEI, Pro-rated cap).

### Step 5 — Compute the foreign housing exclusion or deduction

If the user has foreign housing costs above a base amount AND meets either qualifying test, they can also exclude (or deduct, if SE) housing costs.

**Base housing amount** = 16% of FEIE cap × (qualifying days / 365)
- 2025 base: 16% × $130,000 = $20,800 (if qualified full year)
- 2026 base: 16% × 2026 FEIE cap (TBD)

**Maximum housing amount** = 30% of FEIE cap × (qualifying days / 365), with city-specific high-cost adjustment that can raise this cap significantly for places like London, Hong Kong, Tokyo, Geneva, etc.
- 2025 default max: 30% × $130,000 = $39,000 (if qualified full year)
- See city-specific table in IRS Notice updated annually (e.g., Notice 2024-XX for 2024; check current year)

**Housing exclusion amount** = Housing expenses (capped at max) − Base amount.

For **employees** (employer pays or reimburses housing): housing **exclusion** (Form 2555 Part VI). Reduces taxable income.

For **self-employed** (SE pays own housing): housing **deduction** (Form 2555 Part IX). Above-the-line deduction on Schedule 1 Line 24h or similar (verify current line).

See [`references/housing.md`](./references/housing.md) for detailed mechanics, city tables, and worked examples.

### Step 6 — Run the FEIE election

The election is made by **filing Form 2555 attached to the return** for the year of election. Once made, it applies to all subsequent years until revoked. To revoke, file a return without claiming FEIE and attach a statement of revocation.

**5-year re-election lock-out**: once revoked, the filer cannot re-elect FEIE for 5 years without IRS consent (IRC §911(e)(2); Rev. Rul. 90-77). This trips up filers who switch to FTC and later want to switch back.

### Step 7 — Compute the tax-stacking effect

The exclusion does NOT mean the filer pays $0 US tax. The non-excluded income (passive income, US-source income, FEI above the cap) is taxed at the rates that would apply if the excluded income WAS included. This is the "stacking rule" of IRC §911(f).

Mechanic: the IRS Foreign Earned Income Tax Worksheet (in the 1040 instructions) applies. The tax on (taxable income + excluded income) is computed; then the tax on (excluded income alone) is subtracted; the difference is the actual tax. Because tax brackets are progressive, this effectively keeps the marginal rate applicable to the residual income.

For an expat with $130,000 wages all excluded and $30,000 of dividends:
- Without stacking: dividends taxed at low rates (12% bracket)
- With stacking: dividends "stack on top" of the excluded $130K — taxed at the 22% / 24% marginal rate

This rule prevents double benefit. Tax software handles it automatically. Manual filers must use the Form 1040 instructions worksheet.

### Step 8 — Coordinate with Form 1116 (if applicable)

If foreign earned income exceeds the FEIE cap, the EXCESS is not excluded. Foreign tax allocable to that excess (and to passive foreign income) can be credited via Form 1116. See [`references/coordination-with-1116.md`](./references/coordination-with-1116.md).

If the user has foreign passive income (dividends from a foreign brokerage), FEIE does NOT apply; use Form 1116 for that income.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms / actions:

- **Form 2555 Part VII (excluded foreign earned income)** → reduces Form 1040 wages on Line 1z (or other appropriate line; include negative adjustment)
- **Form 2555 housing exclusion** → also reduces wages
- **Foreign Earned Income Tax Worksheet** → computes Form 1040 Line 16 with stacking
- **Self-employment tax** → STILL OWED on excluded SE income (FEIE only excludes income tax, not SE tax — common trap)
- **Form 1116** if there's foreign tax to credit on non-excluded portions or passive income
- **State tax** — most states do NOT recognize FEIE; California, New York, etc. tax full income (unless filer is a non-resident of the state)
- **FBAR / FinCEN 114** — separate filing if foreign account aggregate exceeds $10,000
- **Form 8938** — separate form if specified foreign financial assets exceed thresholds

### Step 12 — File the return

Hand off to [`filing.md`](./filing.md) for filing channel selection. Form 2555 is supported on most major e-file platforms.

---

## Line-by-line guidance

Full reference in [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — General Information

- **Lines 1-3** — Foreign address and occupation
- **Line 4a-c** — Employer name, US address, foreign address, type
- **Lines 5-7** — Last year FEIE was claimed; type of test used; revocation history (5-year lock-out check)
- **Line 8** — Family members in the foreign country
- **Line 9** — Tax home address and date established

### Part II — Bona Fide Residence Test

- **Line 10** — Date bona fide residence began (must cover an entire tax year)
- **Line 11** — Type of living quarters
- **Line 12a/b** — Family lived with filer (yes/no)
- **Line 13a/b** — Statement to foreign authorities re non-resident
- **Line 14** — Required to pay foreign country income tax
- **Line 15a-d** — Other contractual or factual ties to the country

### Part III — Physical Presence Test

- **Line 16** — 12-month qualifying period (start date, end date)
- **Line 17** — Principal country of employment
- **Line 18** — Travel summary table: every period of physical presence by country, with dates and full-day counts. Sum to ≥ 330 full days outside the US

### Part IV — All Filers

- **Lines 19-23** — Foreign earned income breakdown by type (salary, allowances, SE, noncash, etc.)
- **Line 24** — Total foreign earned income
- **Lines 25-26** — Compensation paid by US employer for services performed abroad (informational)

### Part V — All Filers

- **Line 27** — FEIE allowable
- **Lines 28a-c** — Foreign earned income exclusion amount (Pro-rated cap × qualifying days / total days)

### Part VI — Foreign Housing Exclusion (Employees)

- **Lines 28-36** — Housing expense computation, base amount, exclusion limit
- **Line 36** = housing exclusion (subtracted from wages)

### Part VII — Foreign Earned Income Exclusion

- **Line 37** — Maximum exclusion (annual cap, pro-rated if partial year)
- **Lines 38-43** — Excluded amount = lesser of (FEI − housing exclusion, max exclusion)
- **Line 45** — Total exclusion amount = housing + earned income, flows to Schedule 1 Line 8d (negative)

### Part VIII — Taxpayers Claiming Foreign Earned Income Exclusion

- **Lines 46-50** — Reconciliation: deductions allocable to excluded income (NOT deductible against any income — IRC §911 disallowance)

### Part IX — Foreign Housing Deduction (Self-Employed Only)

- **Lines 51-53** — Housing deduction limit and amount; flows to Schedule 1 Line 24h or similar

---

## Validation

Run every check before declaring ready.

### Math checks

- [ ] Line 24 (Total foreign earned income) = sum of Lines 19-23
- [ ] Line 27 = Line 24 (or capped at FEIE max if pro-rating doesn't apply)
- [ ] Line 36 (housing exclusion) = housing expenses (Line 32) − base amount (Line 33), capped at max (Line 35)
- [ ] Line 37 (max exclusion) = annual cap × (qualifying days / total days)
- [ ] Line 42 (excluded earned income) = lesser of (Line 24 − Line 36, Line 37)
- [ ] Line 45 (total exclusion to Schedule 1) = Line 36 + Line 42
- [ ] If physical presence test: sum of full days outside the US in the 12-month period ≥ 330
- [ ] If bona fide residence test: Line 10 covers an entire tax year (Jan 1 – Dec 31)

### Sanity checks

Surface a warning, do not block:

- [ ] Filer claims abode in the US (working remotely from Texas) → FEIE disqualified; route to FTC
- [ ] Travel dates show > 35 days in the US during the qualifying 12-month period → physical presence test fails (need ≥ 330 foreign full days)
- [ ] Foreign earned income includes pension or investment income → ineligible portion; revise Line 24
- [ ] User claims FEIE but plans to take FTC on the same wages → cannot double dip; allocate
- [ ] User claims housing exclusion > 30% of FEIE cap without a city-specific high-cost designation → over-claim; verify city table
- [ ] User SE income excluded but didn't compute SE tax on Schedule SE → SE tax STILL OWED on excluded SE income; common trap
- [ ] User changed countries mid-year → bona fide residence may break; verify continuous foreign tax home
- [ ] User previously revoked FEIE within last 5 years → 5-year lock-out under §911(e)(2); cannot re-elect without IRS consent
- [ ] State of residence is California / Massachusetts / New York → state likely doesn't honor FEIE; warn user

### Cross-form checks

- [ ] If FEIE used: ensure deductions allocable to excluded income are NOT also on Schedule A or Schedule C (IRC §911 disallowance)
- [ ] If foreign tax paid on excluded income: do NOT credit on Form 1116 (allocation per Reg. §1.911-6)
- [ ] If foreign earned income > FEIE cap: surface that residual is taxable; coordinate with Form 1116 if foreign tax was paid on it
- [ ] SE income excluded under FEIE: confirm Schedule SE is filed for SE tax (not excluded by §911)
- [ ] If foreign housing is employer-provided: housing FMV is included in Line 24 (Foreign earned income includes noncash housing compensation), AND the exclusion is taken in Part VI

---

## Output format

```markdown
# Form 2555 — DRAFT for tax year YYYY

## Header
Filer name: <name>
SSN/ITIN: <id>
Foreign address (Line 1): <address>
Occupation (Line 2): <occupation>
Employer (Line 4a): <name>
Type (Line 4d): <Foreign entity / US company / Self / etc.>

## Part I — General
5. Last year claimed FEIE: YYYY (or "Never")
6. Qualifying test: Bona Fide Residence | Physical Presence
7. Revocation history (5-year lock-out): None | <details>
8. Family members in foreign country: <list>
9. Tax home: <address>, established <date>

## Part II — Bona Fide Residence (only if using BFR test)
10. Date bona fide residence began: MM/DD/YYYY
11. Living quarters: <Rented house, leased apartment, etc.>
12-15. (See line-by-line)

## Part III — Physical Presence (only if using PPT)
16. 12-month qualifying period: MM/DD/YYYY to MM/DD/YYYY
17. Principal country: <country>
18. Travel summary:
| Country | Date entered | Date left | Full days outside US |
|---------|--------------|-----------|---------------------|
| <c>     | MM/DD/YYYY   | MM/DD/YYYY | XXX                |
| ...     | ...          | ...       | ...                 |
| **Total full days outside US** | | | **≥ 330** |

## Part IV — Foreign earned income (all filers)
19. Wages, salary, bonuses, commissions:    $XX,XXX
20. Allowances, reimbursements, noncash:    $X,XXX
21. Allowable share of income for personal services in business if both personal services and capital are material income-producing factors: $X,XXX
22. Noncash income (housing FMV, meals, etc.): $X,XXX
23. Other foreign earned income:             $X,XXX
24. Total foreign earned income:             $XX,XXX
25-26. Compensation from US employer:        $X,XXX (informational)

## Part V — All filers
27. = Line 24 (or apportionment for PFP):    $XX,XXX
28a-c. (mechanical sub-allocation)

## Part VI — Housing Exclusion (employees)
28. Foreign housing expenses (rent, utilities, etc.): $X,XXX
    - Itemize:
      | Type | Amount |
      |------|--------|
      | Rent | $X,XXX |
      | Utilities (excl phone) | $X,XXX |
      | Property insurance | $X,XXX |
      | ... | ... |
29-30. (See line-by-line)
31. Limit on housing expenses (30% × FEIE cap × days/365 + city adjustment): $X,XXX
32. Lesser of 28 or 31:                      $X,XXX
33. Base housing amount (16% × FEIE cap × days/365): $X,XXX
34. 32 − 33:                                  $X,XXX
35. Housing expenses paid by employer (allowance + employer-provided): $X,XXX
36. Housing exclusion = lesser of 34 or 35:  $X,XXX

## Part VII — Foreign Earned Income Exclusion
37. Maximum exclusion (annual cap, pro-rated if partial): $XXX,XXX
38. Total qualifying days in tax year:       XXX
39. Tax year days:                            365 (or 366 leap year)
40. 38 ÷ 39:                                  0.XXXXXX
41. Pro-rated max:                            $XXX,XXX
42. Earned income exclusion = lesser of (24 − 36) or 41: $XXX,XXX
43. Total exclusion (housing + earned):       $XXX,XXX
44. (worksheet line for tax-stacking)
45. Total exclusion to Schedule 1:            $XXX,XXX (negative on Sched 1)

## Part VIII — Disallowed Deductions
46-50. Deductions allocable to excluded income (NOT deductible): $X,XXX

## Part IX — Foreign Housing Deduction (self-employed only, if applicable)
51-53. Housing deduction (above-the-line):   $X,XXX

## Required attachments
- [x] Form 2555 (this draft)
- [ ] Form 1116 if foreign tax to credit on non-excluded portions (separate skill)
- [ ] Schedule SE if SE income excluded — SE TAX STILL OWED (common trap)
- [ ] Form 8938 if specified foreign financial assets exceed threshold
- [ ] FBAR / FinCEN 114 separately (not attached) if foreign account aggregate > $10,000

## Validation summary
- Math: <pass | list failures>
- Sanity: <list any warnings>
- Tax-stacking note: residual income (passive, US-source, or FEI above cap) is taxed at the rate that would apply if FEI were NOT excluded. Use the Foreign Earned Income Tax Worksheet.
- Next steps: <handoff>

## Sources cited in this draft
- IRS Form 2555, Rev. <date>
- IRS Instructions for Form 2555, Rev. <date>
- IRC §911 (FEIE + housing exclusion/deduction)
- IRC §911(b)(2)(D) (annual exclusion cap)
- IRC §911(c) (housing exclusion/deduction)
- IRC §911(e)(2) (5-year revocation lock-out)
- IRC §911(d)(3) (tax home and abode)
- IRC §911(f) (tax-stacking rule)
- Pub. 54 — Tax Guide for U.S. Citizens and Resident Aliens Abroad
- Reg. §1.911-2 (definitions)
- Rev. Proc. — current-year FEIE cap
- Notice — current-year city-specific housing limits
- (any other authority used)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on Form 2555 with examples and edge cases
- [`references/qualifying-tests.md`](./references/qualifying-tests.md) — Bona fide residence vs. physical presence; how to verify; tie-breakers
- [`references/housing.md`](./references/housing.md) — Housing exclusion/deduction mechanics, base/max amounts, city-specific high-cost adjustments
- [`references/coordination-with-1116.md`](./references/coordination-with-1116.md) — When to use exclusion vs. credit; coordination when using both
- [`references/se-tax-trap.md`](./references/se-tax-trap.md) — FEIE excludes income tax NOT SE tax; Totalization Agreements; common SE income mistakes
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 12 audit-tripping mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for filing the completed Form 2555

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
- [Publication 54](https://www.irs.gov/publications/p54) — Tax Guide for U.S. Citizens and Resident Aliens Abroad
- IRC §911 (foreign earned income exclusion + housing)
- IRC §911(b)(2)(D) (annual exclusion cap, indexed)
- IRC §911(c)(1)/(2) (housing amount and high-cost areas)
- IRC §911(d)(1) (qualified individual; bona fide residence and physical presence tests)
- IRC §911(d)(3) (tax home and "abode" rule)
- IRC §911(e)(1)/(2) (election; 5-year revocation lock-out)
- IRC §911(f) (tax-stacking rule)
- Reg. §1.911-1 through §1.911-7 (mechanics)
- Rev. Proc. 2024-40 (2025 FEIE cap $130,000)
- Rev. Proc. (year) — annual indexed FEIE cap; verify current year
- IRS Notice (year) — annual high-cost city housing table; verify current year
- US Totalization Agreements list (SSA.gov) — for SE tax interactions

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. International tax has many edge cases (treaty overrides, dual-resident filers, mid-year residency changes, partial-year qualification); for material amounts or unusual fact patterns, route the user to a CPA or EA with international expertise.
