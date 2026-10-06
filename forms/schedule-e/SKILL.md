---
name: schedule-e
description: >
  Use this skill when an individual needs to fill out Schedule E (Form 1040)
  for rental real estate, royalties, or Schedule K-1 income or loss from a
  partnership, S corporation, estate, or trust. Triggers on phrases like
  "fill out schedule e", "schedule e for my rental", "report rental income",
  "rental property taxes", "vacation home rented part of the year",
  "airbnb on schedule e", "passive loss limit on my rental", "$25,000 rental
  loss allowance", "where does my K-1 go", "schedule e part ii",
  "royalty income schedule e". Do NOT use for rentals with significant
  services such as maid service, a personal property rental business, real
  estate dealers, or royalties from your own creative work (use schedule-c);
  the home office deduction (use form-8829); selling a rental (use form-4797,
  and form-6252 for an installment sale); preparing the partnership or
  S corporation return itself (use form-1065 or form-1120-s); or an estate's
  or trust's own Form 1041.
form: Schedule E (Form 1040) (Supplemental Income and Loss)
audience: [individual, llc1, partnership, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040se.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040se.pdf
---

# Schedule E (Form 1040): Supplemental Income and Loss

This skill produces an audit-grade draft of Schedule E: every Part I property column, the Part II–IV K-1 and REMIC rows, the Part V summary, plus the worksheets that decide how much of a loss reaches the return (Worksheet 5-1, Form 8582, basis and at-risk). The arithmetic of lines 3–26 is simple. The judgment sits in four places: counting rental and personal days (§280A), splitting improvements from repairs and land from building, deciding whether an activity is passive, and applying the loss gates in the right order. The agent asks for the facts behind each of these and never fills them with a default.

Line map verified against the **2025 Schedule E (Form 1040)** (Created 5/6/25) and the **2025 Instructions for Schedule E** (Nov 12, 2025), the revision filed in 2026. The next revision must be re-checked line by line before use: https://www.irs.gov/forms-pubs/about-schedule-e-form-1040.

**Companion guide for end users:** [Schedule E Instructions 2026: Rental Income, Royalties, and K-1 Income Line by Line](https://jupid.com/blog/schedule-e-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when any of the following is true:

- The user mentions Schedule E, "supplemental income", or "1040 schedule e"
- The user owns rental real estate (house, condo, apartment, duplex unit, commercial space, land) directly or through a single-member LLC that is disregarded (Instructions, Single-member LLC)
- The user rented out a vacation home, a room, or a basement unit, or rented to a family member
- The user received royalties from oil, gas, or mineral interests, or investment-type copyright, patent, or name-image-likeness (NIL) royalties
- The user received a Schedule K-1 from a partnership, S corporation, estate, or trust and asks where it goes
- The user asks about passive loss limits, the $25,000 rental loss allowance, real estate professional status, or suspended losses

Do **not** engage this skill (redirect instead):

| Situation | Go to |
|---|---|
| Significant services to renters, such as maid service (Instructions, Line 3); business of renting personal property such as equipment or vehicles; real estate dealer rentals of property held for sale; self-employed writer, inventor, or artist royalties | [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md) |
| Home office for a business | [`../form-8829/SKILL.md`](../form-8829/SKILL.md) |
| Selling a rental property or other business property | [`../form-4797/SKILL.md`](../form-4797/SKILL.md); installment sale: [`../form-6252/SKILL.md`](../form-6252/SKILL.md) |
| Preparing the entity return that issues the K-1 | [`../form-1065/SKILL.md`](../form-1065/SKILL.md), [`../form-1120-s/SKILL.md`](../form-1120-s/SKILL.md) |
| Rental not engaged in for profit | Schedule 1 line 8j via [`../schedule-1/SKILL.md`](../schedule-1/SKILL.md) |
| Crop-share farm rental by an individual | Form 4835, which reaches Schedule E only through line 40 |
| Estate or trust filing its own Form 1041 | Out of scope; recommend a fiduciary return preparer |

Boundaries inside a Schedule E job, handed to siblings: depreciation and §179 ([`../form-4562/SKILL.md`](../form-4562/SKILL.md)); personal share of mortgage interest and taxes ([`../schedule-a/SKILL.md`](../schedule-a/SKILL.md)); partnership self-employment income ([`../schedule-se/SKILL.md`](../schedule-se/SKILL.md)); qualified business income ([`../form-8995/SKILL.md`](../form-8995/SKILL.md) or [`../form-8995-a/SKILL.md`](../form-8995-a/SKILL.md)); Forms 1099 the landlord must issue ([`../form-1099-nec/SKILL.md`](../form-1099-nec/SKILL.md), [`../form-1099-misc/SKILL.md`](../form-1099-misc/SKILL.md)); the return itself ([`../form-1040/SKILL.md`](../form-1040/SKILL.md)). Forms 8582, 6198, 7203 and 461 have no skill in this repo: prepare them as labeled worksheets inside the draft and recommend CPA review whenever one of them limits a loss.

If it is unclear whether a rental belongs on Schedule C or Schedule E, ask about services first (see Step 2). Do not decide on the length of stays alone.

---

## Prerequisites

Collect these before computing anything. If an item is missing, ask a tight question and stop until it is answered.

1. **Tax year and filing status.** Schedule E for tax year 2025 is filed in 2026. If married filing separately: "Did you live apart from your spouse for all of 2025?" (changes the special allowance to $12,500 or $0; Pub. 925).
2. **Property list.** For each rental or royalty property: address, type code (1–8), ownership share, how held (individually, jointly with spouse, single-member LLC, multi-member LLC or partnership). A multi-member LLC or spousal partnership is a Form 1065 matter unless the spouses qualify and elect QJV (Instructions, QJV).
3. **Day calendar per dwelling unit.** Days rented at a fair rental price; days available but not rented; personal use days and who used the unit at what rent; full-time repair days; whether the unit was the user's main home before or after renting. Never estimate.
4. **Income records.** Rent ledger or platform payout reports, deposits collected/returned/kept, advance rent, tenant-paid expenses, services or property received as rent, Forms 1099-MISC/1099-K, royalty statements.
5. **Expense records by property.** Form 1098 for each mortgage, property tax bills, insurance declarations, manager statements, receipts. For each repair over a few hundred dollars: what was done (repair vs improvement).
6. **Depreciation history.** For each building: purchase date, placed-in-service month (when available for rent, not when first rented), cost basis, land/building split, prior depreciation (last year's Form 4562 or depreciation schedule), improvements and their dates.
7. **Vehicle use for the rental.** Miles, method used in the vehicle's first rental year, log.
8. **Passive-loss inputs** when any property or K-1 shows a loss: MAGI components (Form 8582 line 6 list), active participation facts (who approves tenants, rents, repairs; ownership at least 10%), real estate professional hours, last year's Form 8582 carryforwards, other passive activities.
9. **Short-term rental facts** (any unit with stays of 30 days or less): number of stays and nights booked (average period of customer use), every service provided during stays and by whom.
10. **Each Schedule K-1** with its supplemental statements, the user's hours and role in each entity, S corporation distributions and loan repayments, basis worksheets or last year's Form 7203, at-risk facts (nonrecourse debt, guarantees), prior-year suspended losses and why they were suspended.

### Ask, don't guess

When one of these facts is missing, ask the question in quotes and wait. Never fill a default.

| Missing fact | Question | Why it matters |
|---|---|---|
| Personal use | "Did you, a co-owner, or any relative stay at the property in 2025, even one night? Did they pay full market rent?" | §280A day counts, line 2 |
| Placed-in-service month | "On what date was the property first ready and listed for rent?" | Year-one depreciation rate (Pub. 527 Table 2-2d) |
| Land/building split | "What does the county assessment show for land and for improvements?" | Land is not depreciable (Instructions, Line 18) |
| Repair vs improvement | "What exactly was done for this $X, and did it replace a whole system or just fix a part?" | Line 14 vs capitalize |
| Services | "During a guest's stay, do you or anyone you pay clean the unit, change linens, or provide meals or other services?" | Schedule C vs E (Instructions, Line 3) |
| Average stay | "How many separate bookings, and how many nights in total?" | 7-day and 30-day rental-activity exceptions (Pub. 925) |
| Active participation | "Who approves tenants, sets the rent, and approves repairs? What share of the property do you own?" | $25,000 allowance; 10% ownership (Pub. 925) |
| MAGI | "Do you have taxable social security, an IRA deduction, student loan interest, or self-employment tax on this return?" | Form 8582 line 6 |
| Prior-year carryovers | "Please share last year's Form 8582, Worksheet 5-1, Form 7203, and Form 6198, if any." | Lines 22, 27–28; carryforwards |
| K-1 character | "Did you work in this business in 2025? About how many hours? Are you a limited partner?" | Passive vs nonpassive columns |

---

## Workflow

### Step 1: Confirm Schedule E is the right form

Check the redirect table. Confirm entity status: a single-member LLC is disregarded unless it elected corporate status ([`../form-8832/SKILL.md`](../form-8832/SKILL.md)).

### Step 2: Classify each property

For each property: type code (line 1b); for short-term rentals, the services question (maid service and similar → Schedule C; Pub. 527 ch. 3 lists regular cleaning, changing linen, or maid service primarily for the tenant's convenience, and excludes heat and light, cleaning of public areas, trash collection). If the services facts are mixed, present both readings and refer the user to a CPA. Record the classification and the reason in the draft.

### Step 3: Count days and run §280A

Load [`references/personal-use-and-vacation-homes.md`](./references/personal-use-and-vacation-homes.md). For each dwelling unit with any personal use: compute the rental percentage, run the "used as a home" test (personal days greater than the larger of 14 days or 10% of fair rental days), and apply the outcome: fewer than 15 rental days and used as a home → off Schedule E entirely; used as a home with 15+ rental days and a loss → Worksheet 5-1.

### Step 4: Build the income lines

Line 3 per property (rent, advance rent, kept deposits, tenant-paid expenses, FMV of services or property received). Line 4 per royalty property (gross, before withheld state tax). Ask about any 1099-MISC or 1099-K amount that does not match the ledger.

### Step 5: Map expenses to lines 5–19

Use [`references/line-by-line.md`](./references/line-by-line.md). Apply the rental percentage from Step 3 where required. Separate repairs (line 14) from improvements (capitalize). Trace interest to rental use (lines 12–13). Apply the 2025 standard mileage rate of 70 cents a mile only if the method rules allow it (Instructions, Line 6).

### Step 6: Depreciation (line 18) and Form 4562

Residential rental buildings: 27.5-year straight line, mid-month convention (Form 4562 line 19i); nonresidential (commercial): 39-year (line 19j). Year-one rate from Pub. 527 Table 2-2d by placed-in-service month (January 3.485% through December 0.152%), later years 3.636%. Determine whether Form 4562 must be attached (property first placed in service in 2025, listed property including any vehicle, §179, amortization beginning in 2025) and hand the computation to [`../form-4562/SKILL.md`](../form-4562/SKILL.md), including 2025 §179 limits ($2,500,000, reduced above $4,000,000) and the 100% special allowance for property acquired after January 19, 2025 (Instructions, What's New). Let the form-4562 skill decide §179 and special-allowance eligibility for each asset.

### Step 7: Compute lines 20–21 per property, then apply the loss gates

Line 20 = lines 5–19; line 21 = line 3 and/or 4 − line 20. For any loss, load [`references/passive-loss-and-at-risk.md`](./references/passive-loss-and-at-risk.md) and apply, in order: at-risk (Form 6198 worksheet), passive (Form 8582 worksheet or the documented exception), then note excess business loss (Form 461) for the return preparer. Line 22 = allowed rental real estate loss; never for royalties.

### Step 8: Part I totals

Lines 23a–23e on one Schedule E only; line 24 positive line 21 amounts; line 25 royalty losses from 21 plus rental losses from 22; line 26.

### Step 9: Parts II–IV

Load [`references/k1-parts-ii-iii.md`](./references/k1-parts-ii-iii.md). For each K-1: passive or nonpassive (material participation), basis gate (Form 7203 worksheet for S corporations; partner basis worksheet), at-risk gate, passive gate. Use separate PYA, UPE, and interest lines. Check columns (e) and (f) when required. Route K-1 (Form 1065) box 14 code A to Schedule SE.

### Step 10: Part V and handoffs

Line 41 → Schedule 1, line 5. Line 43 for real estate professionals. List handoffs: Form 4562, Schedule A (personal share), Schedule SE, Form 8995/8995-A, Form 8960 if net investment income tax may apply (Pub. 527 Reminders), Forms 1099 the user owes.

### Step 11: Validate, produce the draft, then hand off to filing

Run every check in Validation. Produce the Output format. If the user wants the agent to file, follow [`filing.md`](./filing.md); otherwise stop at the draft.

---

## Line-by-line guidance

Full map with sources: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

**Lines A–B.** "Yes" on line A if 2025 payments required any Form 1099 ($600 thresholds for nonemployee compensation and for rents and other amounts in 2025; Instructions, Line A). For payments made after December 31, 2025 the IRC §6041(a) threshold is $2,000 (P.L. 119-21 §70433); the 2026 instructions must be re-checked.

**Lines 1a, 1b, 2.** Address (blank for royalties), type code 1–8 (code 8 needs a statement), fair rental days and personal use days, QJV box only for qualifying spouses. The day counts on line 2 must match the §280A worksheet in the draft.

**Line 3.** Include kept deposits, advance rent, lease cancellation payments, tenant-paid expenses, FMV of services or property received. Exclude deposits to be returned (Pub. 527 ch. 1).

**Line 4.** Gross royalties; $10 or more should come with a Form 1099-MISC (Instructions, Line 4).

**Lines 5–19.** Ordinary and necessary expenses, rental share only. Not your own labor, not improvements, not legal fees to defend title or improve property (Instructions, Lines 5–21, 10, 14). Line 12 only interest paid to banks and other financial institutions; other mortgage interest on line 13 with the required statements. Line 18 from the depreciation computation; land is never depreciable. Line 19 lists everything else (attach the list).

**Lines 20–22.** Line 21 loss with amounts not at risk → Form 6198 amount, "Form 6198" written to the left. Line 22 only for rental real estate: the Form 8582 allowed amount, or the line 21 loss when the property is nonpassive or the exception applies.

**Lines 23a–26.** One Schedule E carries the totals. Line 26 → Schedule 1 line 5 when Parts II–V are unused.

**Part II (27–32).** Line 27 "Yes" triggers separate PYA/UPE lines. Columns (g)–(k) split passive and nonpassive. Column (e): S corporation loss, distribution, stock disposition, or loan repayment → Form 7203. The 2025 instructions' S-corporation paragraph says "Part III, column (e)"; the box is on Part II line 28 column (e) on the form. Use the form.

**Part III (33–37).** K-1 (Form 1041) items; trust estimated tax credited to the beneficiary is written next to line 37, not included in it.

**Part IV (38–39).** REMIC residual holders only; column (c) excess inclusion is not added into line 39.

**Part V (40–43).** Line 41 combines 26, 32, 37, 39, 40 → Schedule 1 line 5. Line 42 farming/fishing reconciliation. Line 43 real estate professionals only.

### Year-dependent values used by this skill (re-check every year)

| Value | 2025 return | Source to re-check |
|---|---|---|
| Standard mileage rate (line 6) | 70 cents a mile | Instructions for Schedule E, Line 6; https://www.irs.gov/tax-professionals/standard-mileage-rates (2026: 72.5 cents Jan. 1–June 30, 76 cents July 1–Dec. 31; IR-2025-128, IR-2026-29) |
| Form 1099 threshold (line A) | $600 for 2025 payments | Instructions for Schedule E, Line A; $2,000 for payments after Dec. 31, 2025 (IRC §6041(a), P.L. 119-21 §70433) |
| §179 limit / phase-out start | $2,500,000 / $4,000,000 | Instructions for Schedule E, What's New; Form 4562 instructions |
| Special depreciation allowance | 100% for qualified property acquired after Jan. 19, 2025 | Instructions for Schedule E, What's New |
| Excess business loss threshold | $313,000 ($626,000 joint) | Instructions for Form 461 (2025) |
| SALT test in Worksheet 5-1 line 2b | $40,000 ($20,000 MFS) | Pub. 527 (2025), Worksheet 5-1 instructions |
| $25,000 allowance and $100,000/$150,000 MAGI range | Statutory, not indexed | Pub. 925; IRC §469(i) |
| 27.5-year residential percentages | Table 2-2d | Pub. 527; Form 4562 line 19i |

---

## Validation

Run every check and report failures. Do not silently fix.

### Math checks

- [ ] For each property column: line 20 = sum of lines 5–19
- [ ] Line 21 = line 3 (and/or line 4) − line 20
- [ ] Line 22 only on rental real estate columns; equals the Form 8582 allowed amount or the line 21 loss (exception documented)
- [ ] 23a = sum of line 3; 23b = sum of line 4; 23c = sum of line 12; 23d = sum of line 18; 23e = sum of line 20
- [ ] Line 24 = sum of positive line 21 amounts; line 25 = royalty line 21 losses + line 22 losses; line 26 = 24 + 25
- [ ] Part II: 29a/29b column totals; line 30 = (h) + (k); line 31 = (g) + (i) + (j); line 32 = 30 + 31
- [ ] Part III: line 35 = (d) + (f); line 36 = (c) + (e); line 37 = 35 + 36
- [ ] Line 39 = columns (d) + (e) only
- [ ] Line 41 = 26 + 32 + 37 + 39 + 40 and equals Schedule 1, line 5
- [ ] Worksheet 5-1 (if used): 2e + 4f + 6e ≤ line 1, carryovers 7a = 4e − 4f, 7b = 6d − 6e
- [ ] Form 8582 (if used): line 8 = 50% × (line 5 − line 6), capped at $25,000; line 9 = min(line 4, line 8); Part VI column (c) total = line 9

### Rule checks

- [ ] Every dwelling unit with personal days has the §280A test written out
- [ ] No unit "used as a home" shows a line 21 loss beyond what Worksheet 5-1 allows
- [ ] Land excluded from every depreciable basis; year-one rate matches the placed-in-service month
- [ ] Form 4562 flagged for every 2025 placed-in-service property, vehicle, §179, or new amortization
- [ ] Form 8582 skip exception, if claimed, documented condition by condition
- [ ] MAGI computed with the Form 8582 line 6 adjustments, not raw AGI
- [ ] S corporation rows with distributions or losses have column (e) checked
- [ ] PYA and UPE amounts on separate lines, never netted

### Cross-form checks

- [ ] Schedule 1 line 5 equals Schedule E line 41 (or line 26 when only Part I is used)
- [ ] When a Form 4562 is filed for a rental activity, its line 22 total equals that property's line 18 (Form 4562 line 22: "Enter here and on the appropriate lines of your return")
- [ ] Form 8582 Part VIII/IX allowed amounts equal line 22 (Part I) and column (g) (Part II)
- [ ] Personal share of mortgage interest and taxes went to Schedule A, not lost and not double counted
- [ ] K-1 (Form 1065) box 14 code A carried to Schedule SE; S corporation income not on Schedule SE
- [ ] Line A "Yes" answered for payments that required Forms 1099, and the user knows whether they were filed

### Sanity warnings (surface, do not block)

- [ ] Repairs (line 14) above 20% of rents on a property: confirm none are improvements
- [ ] Line 2 shows 0 personal days on a type 3 (vacation/short-term) property: confirm
- [ ] Fair rental days plus personal days exceed 365
- [ ] Rent far below local market on a property rented to a relative: personal-use days
- [ ] Average stay 7 days or less: not a "rental activity" under the passive rules, so no $25,000 allowance; material participation decides passive vs nonpassive (Pub. 925; Instructions for Form 8582)
- [ ] Property with personal use that has not shown a profit in at least 3 of the last 5 years: ask about profit motive (Pub. 527, Not Rented for Profit, presumption of profit)
- [ ] K-1 box 14 code A present but no Schedule SE in the handoff list

---

## Output format

```markdown
# Schedule E (Form 1040): DRAFT for tax year YYYY
Revision used: 2025 Schedule E (Created 5/6/25); 2025 Instructions (Nov 12, 2025)

## Part I
Line A  1099s required: Yes | No        Line B  Filed: Yes | No | n/a

| Line | Description | A | B | C |
|---|---|---|---|---|
| 1a | Address | | | |
| 1b | Type code | | | |
| 2 | Fair rental days / personal days / QJV | | | |
| 3 | Rents received | | | |
| 4 | Royalties received | | | |
| 5 | Advertising | | | |
| 6 | Auto and travel | | | |
| 7 | Cleaning and maintenance | | | |
| 8 | Commissions | | | |
| 9 | Insurance | | | |
| 10 | Legal and other professional fees | | | |
| 11 | Management fees | | | |
| 12 | Mortgage interest paid to banks, etc. | | | |
| 13 | Other interest | | | |
| 14 | Repairs | | | |
| 15 | Supplies | | | |
| 16 | Taxes | | | |
| 17 | Utilities | | | |
| 18 | Depreciation expense or depletion | | | |
| 19 | Other (itemized below) | | | |
| 20 | Total expenses | | | |
| 21 | Income or (loss) | | | |
| 22 | Deductible rental real estate loss | | | |

Line 19 detail: <description: amount per property>
23a ___  23b ___  23c ___  23d ___  23e ___
24 ___   25 (___)   26 ___

## §280A worksheet (each dwelling unit with personal use)
Fair rental days N; personal days P; threshold max(14, 10% × N) = T; used as home: Yes | No
Rental percentage = N ÷ (N + P) = ___ ; Worksheet 5-1 lines A–F, 1–7b (if required)

## Part II
27 Yes | No
| Row | (a) Name | (b) P/S | (c) Foreign | (d) EIN | (e) Basis | (f) At risk | (g) | (h) | (i) | (j) | (k) |
29a (h) ___ (k) ___   29b (g) ___ (i) ___ (j) ___
30 ___   31 (___)   32 ___

## Part III
| Row | (a) Name | (b) EIN | (c) | (d) | (e) | (f) |
34a ___ 34b ___  35 ___  36 (___)  37 ___

## Part IV
| (a) Name | (b) EIN | (c) Excess inclusion | (d) | (e) |
39 ___

## Part V
40 ___  41 ___ (→ Schedule 1, line 5)  42 ___  43 ___

## Loss-limit worksheets
- At-risk (Form 6198): <activity, amount at risk, loss allowed, carryover>
- Passive (Form 8582): <Parts I–III lines; Part VI–VIII allocation; MAGI build-up>
- Basis (Form 7203 / partner basis): <beginning, increases, distributions, losses, ending>
- Excess business loss (Form 461): <flag or n/a>

## Required attachments
- [ ] Form 4562 (per activity: placed in service 2025 / vehicle / §179 / amortization)
- [ ] Form 8582        - [ ] Form 6198        - [ ] Form 7203
- [ ] Form 461         - [ ] Form 8990        - [ ] Statements (code 8, line 12/13, §469(c)(7)(A) election)

## Carryforwards to next year
<property or activity: Form 8582 suspended loss; Worksheet 5-1 7a/7b; Form 7203 / 6198 carryovers>

## Validation summary
- Math: all checks passed | <failures>
- Rules: <results>
- Warnings: <list>
- Handoffs: <Schedule 1 line 5; Schedule A; Schedule SE; Form 8995/8995-A; Form 8960; Forms 1099>

## Sources cited in this draft
- 2025 Schedule E (Form 1040) and 2025 Instructions for Schedule E
- <Pub. 527, Pub. 925, Form 8582 instructions, Form 7203 instructions, IRC sections actually used>
```

The draft is not the filed form. Every number must trace to an input, a worksheet line, or a cited rule.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md): every line of the 2025 Schedule E with rules and sources
- [`references/personal-use-and-vacation-homes.md`](./references/personal-use-and-vacation-homes.md): §280A day counting, the 14-day/10% test, fewer than 15 rental days, Worksheet 5-1, part-home rentals, not-for-profit rentals
- [`references/passive-loss-and-at-risk.md`](./references/passive-loss-and-at-risk.md): gate order, rental-activity exceptions (7-day and 30-day average stay), material participation, real estate professionals, the $25,000 allowance and phase-out, Form 8582 mechanics
- [`references/k1-parts-ii-iii.md`](./references/k1-parts-ii-iii.md): Part II columns, PYA/UPE lines, Form 7203 basis order, Parts III–V, REMIC boundary
- [`references/common-mistakes.md`](./references/common-mistakes.md): fifteen recurring errors and the agent's response to each
- [`filing.md`](./filing.md): channel decision tree, FFFF notes, paper assembly order, Form 1040 mailing addresses, consent and security rules

## Examples

- [`examples/two-long-term-rentals-phaseout.md`](./examples/two-long-term-rentals-phaseout.md): two long-term rentals, one placed in service May 2025, single filer with MAGI $134,178, Form 8582 phase-out and Part VI allocation
- [`examples/vacation-cabin-used-as-home.md`](./examples/vacation-cabin-used-as-home.md): cabin with 61 rental and 19 personal days, used as a home, Worksheet 5-1 limits expenses and carries depreciation forward
- [`examples/k1-investor-scorp-and-passive-partnerships.md`](./examples/k1-investor-scorp-and-passive-partnerships.md): S corporation owner-operator with a distribution and a PYA basis loss, two limited partnerships with a Form 8582 limitation

## Sources

Re-verify every source each year; the IRS revises the form, the instructions, and the publications every filing season.

- [Schedule E Instructions 2026: Rental Income, Royalties, and K-1 Income Line by Line](https://jupid.com/blog/schedule-e-instructions-2026): companion guide for human readers
- [Schedule E (Form 1040), 2025](https://www.irs.gov/pub/irs-pdf/f1040se.pdf) and [Instructions for Schedule E, 2025](https://www.irs.gov/pub/irs-pdf/i1040se.pdf)
- [About Schedule E (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-e-form-1040): check here for the next revision
- [Form 8582, 2025](https://www.irs.gov/pub/irs-pdf/f8582.pdf) and [Instructions for Form 8582, 2025](https://www.irs.gov/pub/irs-pdf/i8582.pdf); [About Form 8582](https://www.irs.gov/forms-pubs/about-form-8582)
- [Publication 527 (2025), Residential Rental Property](https://www.irs.gov/publications/p527): rental income, Table 2-2d, ch. 5 and Worksheet 5-1
- [Publication 925 (2025), Passive Activity and At-Risk Rules](https://www.irs.gov/publications/p925)
- [Instructions for Form 7203 (Rev. December 2022)](https://www.irs.gov/pub/irs-pdf/i7203.pdf): basis order and loss-limit order
- [Instructions for Form 461 (2025)](https://www.irs.gov/pub/irs-pdf/i461.pdf): 2025 excess business loss threshold
- [Form 4562 (2025)](https://www.irs.gov/pub/irs-pdf/f4562.pdf) and [Instructions](https://www.irs.gov/pub/irs-pdf/i4562.pdf): line 19i, line 19j, separate form per activity
- [Standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates): 2025 70 cents; 2026 72.5 cents (Jan. 1–June 30) and 76 cents (July 1–Dec. 31)
- [Instructions for Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf): Where Do You File (mailing addresses)
- IRC [§280A](https://www.law.cornell.edu/uscode/text/26/280A) (vacation homes; (c)(5), (d)(1), (g)), [§469](https://www.law.cornell.edu/uscode/text/26/469) (passive activity losses; (c)(7), (i)), §465 (at-risk), §1366(d) (S corporation basis limit), [§6041(a)](https://www.law.cornell.edu/uscode/text/26/6041) as amended by P.L. 119-21 §70433 ($2,000 information-return threshold for payments after 2025)
- Rev. Proc. 2011-34 (late real estate professional aggregation election)

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, and publications. It is not tax advice and does not create a CPA-client relationship. When a draft involves suspended losses, real estate professional status, Schedule C versus Schedule E classification, K-1 basis, or at-risk limits, the agent tells the user that a licensed tax professional should review it before filing.
