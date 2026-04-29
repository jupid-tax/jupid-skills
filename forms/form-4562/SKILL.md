---
name: form-4562
description: >
  Use this skill when a taxpayer needs to fill out IRS Form 4562 (Depreciation
  and Amortization) — required whenever Section 179, bonus depreciation,
  MACRS depreciation, listed property (vehicles, computers used >50% personally),
  or amortization of intangibles is claimed in the current year. Triggers on
  phrases like "Form 4562", "depreciation", "Section 179", "bonus depreciation",
  "amortization", "listed property", "vehicle depreciation", "rental property
  depreciation", "depreciate equipment", "expense a truck under §179". Do NOT
  use for: cost-of-goods-sold inventory writedowns (Schedule C Part III, not
  Form 4562); §1245/§1250 depreciation recapture on the sale of an asset (Form
  4797); business-use-of-home depreciation (Form 8829 — separate skill);
  changing a depreciation method on a prior-year asset (Form 3115 with §481(a)
  adjustment).
form: Form 4562 (Depreciation and Amortization)
audience: [solo, freelance, llc1, llcm, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f4562.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i4562.pdf
---

# Form 4562 — Depreciation and Amortization

This skill produces an audit-grade Form 4562 from the user's asset purchases, business-use percentages, and election preferences. The form has six parts; the agent walks each part in order, applies the IRC limits at each step, validates the result, and emits a deliverable the user can transcribe to a paper or e-file form.

The judgment in this form lives in three places: (1) which assets qualify for which deduction (§179 vs. bonus vs. straight MACRS), (2) the taxable-income limit on §179 and how excess carries forward, (3) listed-property substantiation rules. The agent must ASK when business-use percentages or income limits aren't established — never default.

**Companion guide for end users:** [Section 179 Deduction Guide 2026](https://jupid.com/blog/section-179-depreciation-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 4562, "depreciation", "Section 179", "§179", "bonus depreciation", "amortization", or "MACRS"
- The user describes buying a business asset costing more than $2,500 with a useful life over one year (vehicle, computer, machinery, furniture, equipment, software, building improvements)
- The user describes a rental property they want to depreciate (residential 27.5-year SL or commercial 39-year SL)
- The user is amortizing intangibles: §197 goodwill, customer lists, covenants not to compete, start-up costs (§195), organizational costs (§248), patents, copyrights
- The user has "listed property" — a vehicle, a computer used partly personally, or other property with mixed business/personal use that triggers §280F substantiation

Do **not** engage this skill when:

- The user is writing down inventory on Schedule C — that's Part III of Schedule C, not Form 4562
- The user is selling a previously depreciated asset and recapturing depreciation — that's **Form 4797** (Sales of Business Property), a separate skill
- The user is depreciating their home office — that's **Form 8829** (Expenses for Business Use of Your Home), a separate skill
- The user wants to change the method of depreciation on a previously placed-in-service asset — that's **Form 3115** with a §481(a) adjustment (see the `form-3115` skill)
- The asset cost ≤$2,500 per item — use the de minimis safe harbor under Reg. §1.263(a)-1(f); expense it on Schedule C Lines 18, 22, or 27a; no Form 4562 needed

If the user has multiple asset purchases and only wants the easy ones expensed under de minimis, confirm that explicitly before producing a Form 4562 with fewer entries than they listed.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer. Do not infer a percentage or a date.

1. **Tax year** the form covers. 2025 (filed 2026) and 2026 (filed 2027) have different §179 and §280F luxury auto limits. Check which year before computing.
2. **Filer's legal name and identifying number** (SSN for sole props/SMLLCs; EIN for partnerships, S-corps, C-corps). Goes in the header.
3. **Business activity** the form attaches to. Form 4562 is filed *per business activity*; if the user has both a Schedule C and a Schedule E rental, that's two Form 4562s.
4. **Asset list**, structured as: description, date placed in service, cost basis, business-use %, election preference (§179, bonus, MACRS, or amortization), recovery period if known.
5. **Total asset purchases for the tax year** — needed for the §179 phase-out calculation (Line 3) even if the user is well under the threshold.
6. **Taxable business income before §179** — Schedule C Line 31 before Line 13, plus W-2 wages, plus any other earned income. This is the §179 income limitation under IRC §179(b)(3).
7. **Prior-year §179 carryover** (Form 4562 Line 10) and **prior-year bonus depreciation election** (whether the user opted out under §168(k)(7) in any prior year for an asset class).
8. **For listed property** (vehicles, computers used <100% for business): contemporaneous mileage log or usage log, total miles driven, business miles, commuting miles, personal miles. No log → the deduction is hard to defend; document that gap.

For each vehicle, additionally ask:
- Year/make/model and gross vehicle weight rating (GVWR) — determines whether §280F luxury auto caps apply (cars ≤6,000 lbs) or the heavy SUV cap applies (>6,000 lbs and <14,000 lbs)
- Whether the vehicle is owned, financed, or leased
- Date the vehicle was first **placed in service for business** (not the purchase date)

For amortization (Part VI), additionally ask:
- Type of intangible (§197 acquired-business goodwill, §195 start-up costs, §248 organizational costs, patent, copyright, other)
- Date amortization began
- Total cost basis being amortized

---

## Workflow

Execute these steps in order. Each part of Form 4562 has a different qualifying rule — don't blend them.

### Step 1 — Confirm scope

Ask: which parts apply this year?
- **Part I** — Section 179 election
- **Part II** — Special (bonus) depreciation allowance for assets placed in service this year
- **Part III** — MACRS depreciation: §A for current-year assets, §B for prior-year assets
- **Part IV** — Summary of Parts I–III plus listed-property §179 from Part V
- **Part V** — Listed property: vehicles, computers used <100% for business, certain other property
- **Part VI** — Amortization (§197, §195, §248, etc.)

If only Part VI applies (e.g., a 15-year goodwill amortization continuing from a prior year with no current-year assets), the agent fills only Part VI plus Part IV summary. Don't pad the form.

### Step 2 — Inventory all assets

Build an internal table:

```
| # | Description     | Date in service | Cost   | Bus % | Class    | Election | Notes        |
|---|-----------------|-----------------|--------|-------|----------|----------|--------------|
| 1 | Ford F-150      | 2025-03-15      | 80,000 | 90%   | 5-yr (HSUV) | §179   | >6,000 lb GVWR |
| 2 | Office building | 2025-09-01      | 300,000| 100%  | 39-yr SL | MACRS   | Nonresidential |
| 3 | Goodwill        | 2025-06-01      | 50,000 | 100%  | §197 15-yr | Amort  | Customer list  |
```

This becomes the source of truth for every later step. Confirm each row with the user before computing.

### Step 3 — Apply de minimis filter

For each asset, ask: did this single item cost ≤$2,500? If yes (and the user has no AFS), expense under the de minimis safe harbor (Reg. §1.263(a)-1(f)) on the appropriate Schedule C/E line — do **not** include it on Form 4562. Removing these from the table early avoids cluttering the form.

The threshold is **$2,500 per item, not per invoice**. Ten $1,000 keyboards on one invoice are ten separate items, all under the threshold.

### Step 4 — Section 179 election (Part I)

For each remaining tangible personal property asset used >50% for business:

1. Compute Line 1: maximum dollar limit. **2025: $1,250,000** (Rev. Proc. 2024-40). **2026: verify with the most recent Revenue Procedure** — typically announced October–November of the prior year.
2. Compute Line 2: total cost of §179 property placed in service this year (sum of all eligible assets at full cost).
3. Compute Line 3: phase-out threshold. **2025: $3,130,000** (Rev. Proc. 2024-40). **2026: verify**.
4. Line 4 = Line 2 − Line 3 if positive; else 0. Reduces Line 5.
5. Line 5 = Line 1 − Line 4. If zero, no §179 available this year.
6. Line 6: list each asset (description, cost, elected §179 amount). Cost on Line 6 must be reduced by personal-use portion (if a $40,000 truck is 80% business, Line 6 cost is $32,000).
7. Line 7: listed-property §179 from Part V Line 29. Prevents double-counting.
8. Line 8 = sum of Line 6 elected §179 + Line 7.
9. Line 9 = smaller of Line 5 or Line 8 (tentative deduction).
10. Line 10: carryover from prior year (Form 4562 Line 13 from prior year).
11. Line 11: business income limit. **§179 is limited to the user's aggregate active business income** (Schedule C profit + W-2 wages + active partnership/S-corp earnings). Look this up from the user's other returns.
12. Line 12 = smaller of (Line 9 + Line 10) or Line 11. **This is the deductible §179 for the year.**
13. Line 13 = (Line 9 + Line 10) − Line 12. Carries forward to next year.

If Line 12 < (Line 9 + Line 10), the agent must tell the user: "Your §179 election exceeds your business income; $X carries forward to next year. You can avoid the carryforward by reducing the elected amount on Line 6 to fit within Line 11."

### Step 5 — Special (bonus) depreciation (Part II)

Bonus depreciation under IRC §168(k) lets the user deduct a percentage of the asset's cost in year one **after** §179 reduces basis. Bonus is *not* income-limited (unlike §179) — it can create a loss.

**2025 bonus rate: 100%** (OBBBA 2025 made bonus permanent at 100% for property placed in service after January 19, 2025; a 40% TCJA rate applied to assets placed in service before that date in 2025 — verify the cutoff for the specific asset). **2026 rate: 100% under OBBBA, but verify** — bonus rates are politically volatile; check the latest IRS Notice or Revenue Procedure for the current year.

Line 14: amount of special depreciation for current-year qualified property. Apply only to property eligible (most new and used tangible personal property with recovery period ≤20 years; not real estate ≥27.5-year unless qualified improvement property).

Line 15: amount for property used in farming.

Line 16: bonus depreciation for listed property (computed in Part V Line 25, copied here).

**Election to opt out**: a user can elect *out* of bonus depreciation for an entire asset class (under §168(k)(7)) by attaching a statement to the timely-filed return. Opt-outs are by class (3-year, 5-year, 7-year, etc.), not asset by asset. Once made, the election is irrevocable without IRS consent. If the user wants to opt out, document it on the deliverable.

### Step 6 — MACRS depreciation (Part III)

For assets not fully expensed via §179 + bonus, depreciate the remaining basis under MACRS.

#### Part III Section A — current-year assets

Line 17: MACRS deduction for assets placed in service in tax years prior to current year (carries forward calculations from prior year's Form 4562 — separate Section B).

Line 18: election to group all current-year assets into one general asset account (rare; most filers don't elect this).

Line 19a–19i: current-year assets organized by recovery period (3-year, 5-year, 7-year, 10-year, 15-year, 20-year, 25-year, 27.5-year residential rental, 39-year nonresidential). For each row, list:
- Cost or other basis (after §179 + bonus reduction)
- Recovery period
- Convention (HY half-year, MQ mid-quarter, MM mid-month for real estate)
- Method (200% DB, 150% DB, SL)
- Depreciation deduction for the year

#### Part III Section B — Alternative Depreciation System (ADS)

Lines 20a–20d: assets the user *elects* to depreciate under ADS instead of GDS, or assets *required* to use ADS (listed property used ≤50% for business, certain tax-exempt-use property, foreign-use property). ADS uses straight-line over a longer recovery period.

#### Section 168(g) elections

If the user elected ADS for an asset class in a prior year, that election binds future years for that class. Check prior returns.

### Step 7 — Listed property (Part V)

Listed property under IRC §280F:
- Passenger vehicles (any auto under 6,000 lbs GVWR)
- Trucks and vans under 6,000 lbs GVWR (subject to similar caps)
- Property used for entertainment/recreation/amusement (rare for solo filers)
- Computers (only if not used at a regular business establishment >50% of the time)

For each piece of listed property:
- **>50% business use required** in the first year and throughout the recovery period to use §179, bonus, or accelerated MACRS. If business use is ≤50%, the asset must use straight-line ADS over the full recovery period and gets no §179 or bonus.
- **Substantiation**: contemporaneous log of business and total use. No log → deduction is at audit risk.
- **§280F luxury auto caps** for passenger autos placed in service in 2025 (§280F(a) as adjusted by Rev. Proc. 2024-40 — verify):
  - Year 1 with bonus: ~$20,400 max depreciation (verify exact 2025 figure)
  - Year 1 without bonus: ~$12,400
  - Year 2: ~$19,800
  - Year 3: ~$11,900
  - Year 4 and after: ~$7,160
  These caps reduce the depreciation otherwise allowable. They apply *after* §179 and bonus.
- **Heavy SUV exception** (>6,000 lbs and <14,000 lbs GVWR, with cargo bed length, etc.): §280F caps don't apply, but §179 is capped at **$30,500 for 2025** (IRC §179(b)(5), Rev. Proc. 2024-40). Bonus depreciation can apply to remaining basis.

### Step 8 — Amortization (Part VI)

For intangible assets being amortized:

| Intangible | IRC § | Period |
|------------|-------|--------|
| Goodwill, going concern, customer lists, workforce in place, covenants not to compete, etc. (acquired with a business) | §197 | 15-year SL |
| Start-up costs (≤$5,000 deducted, excess amortized) | §195 | 180 months (15 years) |
| Organizational costs of corporation/partnership (≤$5,000 deducted, excess amortized) | §248/§709 | 180 months |
| Research expenditures (post-TCJA, post-2021) | §174 | 5 years (domestic) / 15 years (foreign) — verify current rules |
| Patents, copyrights | §167 | Useful life or §197 if acquired with a business |
| Software (purchased separately, not §197) | §167 | 36 months SL |

Line 42: amortization of costs that begin during the current year. Each row: description, date amortization begins, amount amortized, IRC code section, amortization period, current-year deduction.

Line 43: amortization of costs that began before the current year (continuing from prior years).

Line 44 = Line 42 + Line 43, total amortization. Flows to the appropriate income tax return line (Schedule C Line 27a as "Amortization", Schedule E Line 18, or the corporate equivalent).

### Step 9 — Summary (Part IV)

- Line 21: listed-property depreciation from Part V Line 28
- Line 22 = sum of Lines 12 + 14 + 15 + 16 + 17 + 19 + 20 + 21 (total depreciation)
- Line 23: portion of Line 22 attributable to assets where §263A capitalization applies (UNICAP — usually inventory-related; check)

Line 22 is the number that flows to:
- Schedule C Line 13 (sole prop / SMLLC)
- Schedule E Line 18 (rental real estate)
- Schedule F Line 14 (farm)
- Form 1120 Line 20, Form 1120-S Line 14, Form 1065 Line 16a (entities)

### Step 10 — Validation checks

See **Validation** below. Run every check.

### Step 11 — Produce the deliverable

See **Output format** below.

### Step 12 — Hand off downstream

State next steps:
- **§179 carryover** — note Line 13 carryforward; remind user to track it for next year's Form 4562 Line 10
- **Recapture risk** — if any §179'd or bonus-depreciated asset has business use ≤50% in any year before the recovery period ends, recapture under §280F(b)(2) is reported on Form 4797
- **§280F caps applied** — note any luxury auto cap reductions; the disallowed amount is recovered post-recovery period via straight-line
- **Bonus opt-out elections** — if any class election was made, attach a written statement to the return
- **Form 4797** — required when the asset is later sold; depreciation taken reduces basis and may trigger §1245/§1250 ordinary-income recapture

### Step 13 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). Form 4562 is filed *with* the income tax return — it does not file standalone.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- Name(s) shown on return — match the related income tax return exactly
- Identifying number — SSN or EIN
- Business or activity — name of the trade or business this Form 4562 attaches to (one Form 4562 per activity)

### Part I — Election To Expense Certain Property Under Section 179

Lines 1–13. Calculation of the §179 deduction with phase-out and income limits (see Step 4 above and [`references/section-179.md`](./references/section-179.md)).

### Part II — Special Depreciation Allowance and Other Depreciation

Lines 14–16. Bonus depreciation under §168(k) (see [`references/bonus-and-macrs.md`](./references/bonus-and-macrs.md)).

### Part III — MACRS Depreciation

Section A: Lines 17–18. Section B: Lines 19a–19i (GDS), Lines 20a–20d (ADS).

### Part IV — Summary

Lines 21–23. Sum of all depreciation; flows to income tax return.

### Part V — Listed Property

Lines 24–30 for §179, bonus, and depreciation for listed property. Lines 31–36 for vehicle-specific reporting (business, commuting, other miles for each vehicle). Lines 37–41 for "questions for employers who provide vehicles for use by their employees" (rare; ignore for solo filers).

See [`references/listed-property.md`](./references/listed-property.md) for the full vehicle-specific rules and §280F caps.

### Part VI — Amortization

Lines 42–44. Amortization of intangibles (see [`references/amortization.md`](./references/amortization.md)).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 4 = max(0, Line 2 − Line 3)
- [ ] Line 5 = max(0, Line 1 − Line 4)
- [ ] Line 8 = (sum of Line 6 column (c) elected amounts) + Line 7
- [ ] Line 9 = min(Line 5, Line 8)
- [ ] Line 12 = min(Line 9 + Line 10, Line 11)
- [ ] Line 13 = (Line 9 + Line 10) − Line 12
- [ ] Line 22 = Lines 12 + 14 + 15 + 16 + 17 + (sum of Line 19) + (sum of Line 20) + Line 21
- [ ] Line 28 (Part V) reconciles to listed-property depreciation included in Line 21
- [ ] Line 29 (Part V) reconciles to listed-property §179 included in Line 7
- [ ] Part VI Line 44 = Line 42 + Line 43
- [ ] For each Line 6 / Line 19 row: cost basis × business-use % is the figure used (not raw cost)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Sum of Line 6 elected §179 + Line 7 > Line 5 → user attempted to elect more §179 than the dollar limit allows
- [ ] Line 12 < Line 8 + Line 10 → carryforward exists; confirm user is aware
- [ ] Listed-property business use ≤50% but §179, bonus, or accelerated MACRS claimed → not allowed; force ADS
- [ ] Vehicle ≤6,000 lbs GVWR with first-year depreciation > §280F luxury cap → cap reduces; verify
- [ ] Heavy SUV §179 > $30,500 → exceeds §179(b)(5) cap; reduce
- [ ] Bonus depreciation taken on real property other than QIP → real property over 20-year class isn't bonus-eligible
- [ ] Amortization of §197 intangible over period other than 15 years → §197 is fixed at 15-year SL
- [ ] No mileage log claimed for vehicle on Part V → audit risk; user should be informed

### Cross-form checks

- [ ] Line 22 matches Schedule C Line 13 / Schedule E Line 18 / etc. on the related return
- [ ] Section 179 carryforward on Line 13 matches what user will track for next year
- [ ] If §280F caps reduced depreciation, the disallowed amount is tracked separately for post-recovery-period catch-up
- [ ] If bonus opt-out elected, the written statement is being attached to the return

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 4562 or paste into tax software. Format:

```markdown
# Form 4562 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <name>
Identifying number: <SSN or EIN>
Business or activity to which this form relates: <activity>

## Part I — Section 179
1.  Maximum amount:                   $1,250,000  (2025; verify 2026)
2.  Total cost of §179 property:      $X,XXX
3.  Threshold cost of §179 property:  $3,130,000  (2025; verify 2026)
4.  Reduction in limit:               $X,XXX
5.  Dollar limit (Line 1 − Line 4):   $X,XXX
6.  (a) Description / (b) Cost / (c) Elected cost
    | (a) Description    | (b) Cost (after bus%) | (c) Elected §179 |
    |--------------------|----------------------|------------------|
    | <asset 1>          | $X,XXX               | $X,XXX           |
    | <asset 2>          | $X,XXX               | $X,XXX           |
7.  Listed property §179 (from Line 29): $X,XXX
8.  Total elected §179 (Line 6 + Line 7): $X,XXX
9.  Tentative deduction (smaller of 5 or 8): $X,XXX
10. Carryover from prior year:        $X,XXX
11. Business income limit:            $X,XXX
12. §179 deduction (smaller of 9+10 or 11): $X,XXX
13. Carryover to next year:           $X,XXX

## Part II — Special Depreciation
14. Special depreciation allowance (current-year qualified property): $X,XXX
15. Property used in farming (50% bonus): $X,XXX
16. Other depreciation (including ACRS): $X,XXX

## Part III — MACRS Depreciation
17. MACRS deduction for prior-year assets: $X,XXX
18. General asset account election: [ ] Check if elected

### Section A (GDS)
| (a) Class | (b) Month/yr placed | (c) Basis | (d) Recovery | (e) Convention | (f) Method | (g) Deduction |
|-----------|---------------------|-----------|--------------|----------------|------------|---------------|
| 19a 3-year |                     |           |              |                |            |               |
| 19b 5-year | 03/2025             | $X,XXX    | 5 yrs        | HY             | 200DB      | $X,XXX        |
| 19c 7-year |                     |           |              |                |            |               |
| 19d 10-year |                    |           |              |                |            |               |
| 19e 15-year |                    |           |              |                |            |               |
| 19f 20-year |                    |           |              |                |            |               |
| 19g 25-year |                    |           |              |                |            |               |
| 19h 27.5-yr residential | 09/2025  | $X,XXX | 27.5 yrs    | MM             | SL         | $X,XXX        |
| 19i 39-yr nonresidential |         |           |              | MM             | SL         |               |

### Section B (ADS)
| (a) | (b) | (c) | (d) | (e) | (f) | (g) |
|-----|-----|-----|-----|-----|-----|-----|
| 20a Class life |   |   |   |   | SL |   |
| 20b 12-year    |   |   |   |   | SL |   |
| 20c 30-year    |   |   |   |   | SL |   |
| 20d 40-year    |   |   |   |   | SL |   |

## Part IV — Summary
21. Listed property (from Line 28):   $X,XXX
22. Total (Lines 12+14+15+16+17+19+20+21): $X,XXX
23. §263A capitalized portion of Line 22: $X,XXX

## Part V — Listed Property
24a. Have evidence to support business use? Yes/No
24b. Is the evidence written? Yes/No

| Item | Date in service | Bus% | Cost | Bus basis | Recovery | Method | Bonus | §179 | MACRS |
|------|-----------------|------|------|-----------|----------|--------|-------|------|-------|
| Vehicle 1 | MM/DD/YYYY | XX% | $X,XXX | $X,XXX | 5 yrs | 200DB/HY | $X,XXX | $X,XXX | $X,XXX |
25. Bonus depreciation for listed property: $X,XXX
26. Listed property used >50% business — depreciation: $X,XXX
27. Listed property used ≤50% — ADS depreciation: $X,XXX
28. Total (Lines 25+26+27) → Line 21: $X,XXX
29. §179 cost for listed property → Line 7: $X,XXX

### Vehicle mileage (per vehicle)
30a. Total business miles:        X,XXX
30b. Total commuting miles:       X,XXX
30c. Total other personal miles:  X,XXX
30d. Total miles driven:          X,XXX  (= 30a+30b+30c)
31. Was vehicle available for personal use during off-duty hours? Yes/No
32. Was vehicle used primarily by a more-than-5% owner? Yes/No
33. Is another vehicle available for personal use? Yes/No

## Part VI — Amortization
| (a) Description | (b) Date begins | (c) Cost | (d) IRC § | (e) Period | (f) Current-year amortization |
|-----------------|-----------------|----------|-----------|------------|-------------------------------|
| <intangible 1>  | MM/DD/YYYY      | $X,XXX   | §197      | 180 mo     | $X,XXX                        |
42. Total Line 42 amortization (current year):  $X,XXX
43. Amortization of costs that began before current year: $X,XXX
44. Total amortization (Line 42 + Line 43):     $X,XXX

## Required attachments and elections
- [ ] Statement of bonus depreciation opt-out election (if elected, by class)
- [ ] Form 4797 if asset disposed during year (separate skill)
- [ ] §179 carryforward tracker (note Line 13 amount)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 12>

## Sources cited in this draft
- IRS Form 4562 (revision date YYYY)
- IRS Instructions for Form 4562 (revision date YYYY)
- IRC §168 (MACRS), §168(k) (bonus), §179, §197 (amortization), §263A (UNICAP), §280F (listed property)
- Rev. Proc. 2024-40 (2025 §179 limit, phase-out, §280F luxury caps)
- IRS Pub. 946 (How to Depreciate Property)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 / 1120 / 1120-S / 1065 e-file software or paper Form 4562.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 4562 line with examples and edge cases
- [`references/section-179.md`](./references/section-179.md) — §179 election mechanics, dollar/phase-out limits, income limit, carryforward, recapture
- [`references/bonus-and-macrs.md`](./references/bonus-and-macrs.md) — §168(k) bonus depreciation rates, MACRS recovery periods and conventions, GDS vs. ADS
- [`references/listed-property.md`](./references/listed-property.md) — §280F vehicles, computers, mixed-use rules, luxury auto caps, heavy SUV exception
- [`references/amortization.md`](./references/amortization.md) — §197 intangibles, §195 start-up costs, §248 organizational costs, software amortization
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 4562 with Form 1040 / 1120 / 1120-S / 1065 via IRS Free File Fillable Forms or paper

## Examples

End-to-end worked Form 4562 filings.

- [`examples/contractor-truck-179.md`](./examples/contractor-truck-179.md) — Sole-prop contractor buys an $80,000 truck; comparison of §179 full expensing vs. 5-year MACRS; vehicle GVWR matters
- [`examples/rental-property-275.md`](./examples/rental-property-275.md) — Rental property owner depreciating a $300,000 residential building over 27.5 years SL with mid-month convention
- [`examples/saas-amortization-197.md`](./examples/saas-amortization-197.md) — SaaS startup amortizing $50,000 of acquired customer-list intangibles over 15 years under §197

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed.

- [Section 179 Deduction Guide 2026](https://jupid.com/blog/section-179-depreciation-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 4562 (latest)](https://www.irs.gov/pub/irs-pdf/f4562.pdf) — the form itself
- [Instructions for Form 4562 (latest)](https://www.irs.gov/pub/irs-pdf/i4562.pdf) — line-by-line IRS guidance
- [About Form 4562](https://www.irs.gov/forms-pubs/about-form-4562) — IRS landing page with archive of prior revisions
- [Publication 946](https://www.irs.gov/publications/p946) — How to Depreciate Property (full MACRS tables, conventions, examples)
- [Publication 463](https://www.irs.gov/publications/p463) — Travel, Gift, and Car Expenses (vehicle substantiation rules)
- IRC §168 (MACRS), §168(k) (bonus depreciation), §179 (election to expense), §197 (15-year amortization of intangibles), §195 (start-up costs), §248 (organizational costs), §263A (UNICAP), §280F (listed property and luxury auto limits)
- Rev. Proc. 2024-40 — inflation adjustments for tax year 2025: §179 limit $1,250,000; phase-out $3,130,000; heavy SUV §179 cap $30,500; §280F luxury auto first-year cap with bonus
- Rev. Proc. (TBD) 2025 — 2026 inflation adjustments; verify October–November 2025

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. The agent invoking this skill should remind the user, when producing a draft, that depreciation choices interact with future-year tax planning and that complex situations (cost segregation studies, multiple §179 carryforwards, bonus opt-outs, §1245/§1250 recapture on later sales) warrant a licensed tax professional's review.
