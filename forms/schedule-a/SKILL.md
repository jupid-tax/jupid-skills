---
name: schedule-a
description: >
  Use this skill when an individual filer needs to fill out IRS Schedule A
  (Form 1040) — Itemized Deductions. Triggers on phrases like "should I
  itemize", "fill out Schedule A", "claim mortgage interest deduction",
  "deduct medical expenses", "SALT cap deduction", "charitable contribution
  deduction", "standard vs itemized", or "where do property taxes go on my
  taxes". Do NOT use for: business expenses (Schedule C — use schedule-c),
  educator expenses (Schedule 1 Line 11 — use schedule-1), HSA contributions
  (Form 8889 — use form-8889), self-employed health insurance (Schedule 1
  Line 17 — use schedule-1), QBI deduction (Form 8995 — use form-8995),
  above-the-line student loan interest (Schedule 1 — use schedule-1), or the
  Schedule 1-A deductions for tips, overtime, car loan interest and seniors
  (Form 1040 line 13b — use form-1040).
form: Schedule A (Form 1040)
audience: [individual, solo, freelance]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040sa.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040sca.pdf
---

# Schedule A (Form 1040) — Itemized Deductions

This skill produces an audit-grade draft of Schedule A from the user's medical, tax, mortgage, charitable, and casualty expenses. It collects documents, applies the limits for the tax year (2025: the $40,000 SALT cap with its $500,000 MAGI phase-down; 2026: the $40,400 cap, deductible mortgage insurance premiums, the 0.5% charitable floor and the 2/37 limitation for the 37% bracket), runs the standard-vs-itemized comparison, and emits a deliverable the user can transcribe to a paper or e-file form.

The math is mechanical. The judgment is in the **standard-vs-itemized comparison** and in **knowing which year's rules apply**. The One Big Beautiful Bill Act (P.L. 119-21, July 4, 2025) changed Schedule A in two waves: for 2025 returns, the SALT cap (§70120); for 2026 returns, mortgage insurance premiums (§70108), personal casualty losses from State declared disasters (§70109), educator expenses (§70110), the overall itemized limitation (§70111) and charitable contributions (§§70424–70425).

**Form revision.** The line map in this skill was verified on 2026-10-06 against the **2025 Schedule A (Form 1040)** (Cat. No. 17145C, filed in 2026) and the 2025 Instructions for Schedule A (Dec 8, 2025). 2026-only rules are flagged as such; the 2026 Schedule A had not been released when this skill was verified, so re-check its line numbers (especially the mortgage insurance line and the charitable floor) before preparing a 2026 return: https://www.irs.gov/forms-pubs/about-schedule-a-form-1040.

**Companion guide for end users:** [Schedule A (Form 1040) + AI Agent Skill: Itemized Deductions Guide 2026](https://jupid.com/blog/schedule-a-itemized-deductions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Schedule A, "Form 1040 Schedule A", or "itemized deductions"
- The user asks "should I itemize" or "standard vs itemized"
- The user wants to deduct: mortgage interest, property tax, state income tax, medical expenses, charitable contributions, casualty/theft losses
- The user asks "where do my property taxes go on my taxes"
- The user is a homeowner asking about tax deductions

Do **not** engage this skill when:

- The expense is a business expense — that goes on **Schedule C** (use the [`schedule-c`](../schedule-c/SKILL.md) skill)
- The expense is for educators, jury duty, alimony, IRA contributions — those are **above-the-line** adjustments on Schedule 1 (use [`schedule-1`](../schedule-1/SKILL.md))
- The user has self-employed health insurance — that goes on **Schedule 1 Line 17**, not Schedule A
- The user wants to claim QBI — that's **Form 8995/8995-A** (use [`form-8995`](../form-8995/SKILL.md))
- The user has HSA contributions — that's **Form 8889** (use [`form-8889`](../form-8889/SKILL.md))
- The user wants student loan interest — that's **Schedule 1 Line 21** (above the line)
- The user asks about the deductions for qualified tips, qualified overtime, car loan interest, or the $6,000 senior deduction — those are on **Schedule 1-A**, flow to Form 1040 line 13b, and are allowed whether or not the user itemizes (2025 Schedule A instructions, What's New); use [`form-1040`](../form-1040/SKILL.md)

If the user's situation is borderline (e.g., a freelancer asking about home office property taxes), ask: "Is this a personal residence or a business property?" Personal-residence property tax goes on Schedule A Line 5b; business-property tax goes on Schedule C Line 23 or Form 8829.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Schedule A rules differ between 2024 (old $10K SALT cap, no mortgage insurance deduction, no charity floor), 2025 ($40,000 SALT cap with phase-down, no mortgage insurance deduction, no floor), and 2026 ($40,400 SALT cap, mortgage insurance premiums deductible again, 0.5% charity floor, 2/37 overall limitation, State declared disasters). Numbers depend on this — DO NOT default.
2. **Filing status** — Single / MFJ / MFS / HoH / Qualifying Surviving Spouse. Determines standard deduction and SALT cap.
3. **AGI** — from Form 1040 line 11b (2025 form). Used for medical 7.5% floor, mortgage insurance phase-out (2026+), charity ceilings and 0.5% floor (2026+, on the contribution base), and casualty 10% floor.
4. **MAGI for the SALT phase-down** — AGI plus amounts excluded under IRC §911 (Form 2555), §931 (Form 4563) and §933 (Puerto Rico) (IRC §164(b)(7)(B)(iv); 2025 Schedule A instructions, line 5e worksheet lines 2–4). For most filers it equals AGI.
5. **Ages and blindness** of the user and spouse — for the additional standard deduction in the comparison.

Collect the user's documents and inputs by category:

### Medical (Lines 1-4)
- Total out-of-pocket medical expenses paid in the tax year (NOT reimbursed by insurance, HSA, FSA, or HRA)
- Long-term care insurance premiums (with age-based caps from Pub 502)
- Medical mileage log (21¢ per mile for 2025; for 2026, 20.5¢ for January 1–June 30 and 23.5¢ for July 1–December 31, per [IRS Standard Mileage Rates](https://www.irs.gov/tax-professionals/standard-mileage-rates), IR-2025-128 and IR-2026-29)

### Taxes (Lines 5-7)
- State and local income tax paid (W-2 box 17, 1099 withholding boxes, estimated tax payments, prior-year balance due paid this year) OR sales tax (use IRS optional table or actual receipts)
- Real estate taxes (property tax bill — verify the amount represents value-based ad valorem tax, not special assessments)
- Personal property tax (typically vehicle registration value-based portion)
- Foreign income tax (only if not claimed as a credit on Schedule 3); foreign real property taxes are not deductible

### Interest (Lines 8-10)
- Form 1098 (Rev. April 2025) from each mortgage lender — box 1 interest, box 4 refund of overpaid interest, box 5 mortgage insurance premiums, box 6 points, box 10 other (often real estate taxes), box 11 acquisition date
- Loan origination date (determines $750K vs $1M cap)
- Purpose of any HELOC or home equity loan (must be buy/build/improve)
- Refinance details if applicable
- Investment interest (Form 4952 worksheet)

### Charity (Lines 11-14)
- Cash contributions log with payee, date, amount
- Written acknowledgments for any single gift ≥ $250
- Non-cash contributions log with description and FMV
- Form 8283 if non-cash > $500
- Qualified appraisal if any item or group of similar items is deducted at more than $5,000 (not required for publicly traded securities)
- Carryover from prior year (from prior Form 8283 / Schedule A worksheet)

### Casualty/theft (Line 15)
- Disaster declaration: 2025 — federally declared disasters only (2025 Schedule A instructions, line 15); 2026+ — federally declared or State declared disasters (IRC §165(h)(5) as amended by P.L. 119-21 §70109)
- Form 4684 inputs: adjusted basis, FMV before/after, insurance reimbursement

### Other (Line 16)
- Gambling winnings (Schedule 1) and gambling losses log
- Any IRD federal estate tax, bond premium amortization, claim-of-right repayment

If the user says "I want to itemize" but has no mortgage, no significant medical, no large charity, and no SALT > $10K, **stop and warn**: "Based on what you've shared, your standard deduction will likely beat itemizing. Want me to run the comparison anyway, or skip Schedule A?"

---

## Workflow

Execute these steps in order.

### Step 1 — Determine the tax year and filing status

Confirm tax year (2024, 2025, or 2026) and filing status. State the standard deduction:

| Filing Status | 2025 Standard Deduction | 2026 |
|---|---|---|
| Single / MFS | $15,750 | $16,100 |
| MFJ / QSS | $31,500 | $32,200 |
| HoH | $23,625 | $24,150 |
| Additional, age 65+ or blind (each) — married / unmarried | $1,600 / $2,000 | $1,650 / $2,050 |

Sources: 2025 base amounts from P.L. 119-21 §70102 (IRC §63(c)(7)), printed on the 2025 Form 1040 and in its instructions (What's New); 2025 additional amounts from Rev. Proc. 2024-40 §2.15(3); 2026 amounts from Rev. Proc. 2025-32 §4.14.

### Step 2 — Confirm AGI and MAGI

Pull AGI from Form 1040 line 11b if available. If the user is still computing AGI, ask for it — Schedule A depends on it for the medical floor, charity ceiling/floor, casualty floor, and high-income SALT phase-down. For the SALT phase-down, MAGI = AGI + exclusions under §911 (Form 2555 lines 45 and 50), §931 (Form 4563 line 15) and §933 (Puerto Rico income) (IRC §164(b)(7)(B)(iv)). Ask whether any of those apply.

### Step 3 — Compute Lines 1-4 (Medical)

Apply 7.5% AGI floor per [`references/medical-expenses.md`](./references/medical-expenses.md).

```
Line 1: Total qualified medical expenses
Line 2: AGI (from Form 1040 line 11b)
Line 3: Line 2 × 7.5%
Line 4: max(0, Line 1 − Line 3)
```

### Step 4 — Compute Lines 5-7 (SALT)

Apply the SALT cap per [`references/salt-cap.md`](./references/salt-cap.md).

```
Line 5a: State/local income tax OR general sales tax (user elects one; check the box for sales tax)
Line 5b: Real estate taxes
Line 5c: Personal property taxes
Line 5d: 5a + 5b + 5c

Base cap for the tax year (IRC §164(b)(7)(A); MFS gets half):
  - 2024: $10,000 ($5,000 MFS) — TCJA original
  - 2025: $40,000 ($20,000 MFS)
  - 2026: $40,400 ($20,200 MFS)
  - 2027-2029: 101% of the prior year's amount (IRS will publish the figure)
  - 2030+: $10,000 ($5,000 MFS), no phase-down

Phase-down (2025-2029), from the 2025 State and Local Tax Deduction Worksheet:
  If line 5d ≤ $10,000 ($5,000 MFS): line 5e = line 5d, stop
  Threshold = $500,000 for 2025, $505,000 for 2026 (half for MFS)
  Reduced amount = base cap (the full, not halved, amount) − 30% × max(0, MAGI − threshold)
  Allowed = max(reduced amount, $10,000); MFS: half of that
  (the $10,000 floor is not indexed — IRC §164(b)(7)(B)(iii))

Line 5e: min(Line 5d, allowed amount)
Line 6: Other taxes (foreign income tax, GST on certain income distributions)
Line 7: Line 5e + Line 6
```

### Step 5 — Compute Lines 8-10 (Interest)

Apply mortgage rules per [`references/mortgage-interest.md`](./references/mortgage-interest.md).

- Verify acquisition debt is within cap ($750K post-Dec 15 2017; $1M grandfathered). If exceeded, compute deductible portion using the average-balance method in Pub 936.
- Verify HELOC/home equity loan funds were used to buy/build/improve the home; otherwise interest is not deductible.
- If any home mortgage proceeds were not used to buy, build, or substantially improve the home, check the box on line 8 and figure the deductible interest with Pub 936.
- Mortgage insurance premiums: **not deductible for 2025** (line 8d is "Reserved for future use" on the 2025 form). **For 2026+** they are treated as qualified residence interest again (IRC §163(h)(3)(E), P.L. 119-21 §70108), reduced by 10% for each $1,000 ($500 MFS) of **AGI** over $100,000 ($50,000 MFS), so nothing is deductible above $109,000 ($54,500 MFS); not indexed. Confirm which line the 2026 Schedule A uses.

```
Line 8a: Mortgage interest and points from Form 1098 (deductible portion)
Line 8b: Mortgage interest not on Form 1098 (e.g., seller-financed; name, SSN/EIN, address)
Line 8c: Points not on Form 1098
Line 8d: Reserved for future use (2025)
Line 8e: Sum 8a-8c
Line 9: Investment interest (Form 4952 if required)
Line 10: Line 8e + Line 9
```

### Step 6 — Compute Lines 11-14 (Charity)

Apply charity rules per [`references/charitable-contributions.md`](./references/charitable-contributions.md).

```
Line 11: Cash contributions (60% AGI ceiling for cash to public charities; see Pub 526 if over 30% of AGI)
Line 12: Non-cash contributions (ceilings depend on property type and donee: 30% for capital gain property to public charities, 20% to private foundations; see Pub 526)
Line 13: Carryover from prior year
Line 14: Sum 11-13

If tax year ≥ 2026 (IRC §170(b)(1)(I), P.L. 119-21 §70425):
  Floor = contribution base (AGI figured without any NOL carryback) × 0.5%
  Deductible charity = max(0, total allowed after the percentage ceilings − Floor)
  (the statute applies the floor in a set order across contribution categories; amounts
   lost to the floor carry forward only from years in which a percentage ceiling is
   exceeded — IRC §170(d)(1)(C))

If tax year ≤ 2025: no floor; use Line 14 raw.
```

Verify substantiation for every gift ≥ $250 (contemporaneous written acknowledgment), Form 8283 if non-cash deductions exceed $500, and a qualified appraisal for any item or group of similar items over $5,000 (Form 8283 Section B; publicly traded securities excepted).

2026+ non-itemizers: a user who takes the standard deduction can still deduct up to $1,000 ($2,000 joint) of cash gifts to public charities, not to donor-advised funds or supporting organizations (IRC §170(p) as amended by P.L. 119-21 §70424). It is not a Schedule A item; include it in the Step 10 comparison and confirm where the 2026 Form 1040 reports it.

### Step 7 — Compute Line 15 (Casualty/theft)

Only for a loss attributable to a federally declared disaster (2025) or a federally declared or State declared disaster (2026+, IRC §165(h)(5) as amended). A **net qualified disaster loss** (Form 4684 line 15) goes on line 16, not line 15. See [`references/common-mistakes.md`](./references/common-mistakes.md) for non-disaster cases that don't qualify.

```
For each loss:
  Loss = min(decrease in FMV, adjusted basis) − insurance reimbursement
  After-floor = max(0, Loss − $100)

Sum all after-floor losses
Line 15 = max(0, sum − AGI × 10%)
```

Form 4684 must be attached.

### Step 8 — Compute Line 16 (Other)

Only the items listed in the instructions: gambling losses (capped at gambling winnings reported on Schedule 1 line 8b), casualty and theft losses of income-producing property (Form 4684 lines 32 and 38b, Form 4797 line 18a), federal estate tax on income in respect of a decedent, amortizable bond premium, ordinary loss on contingent payment or inflation-indexed debt instruments, claim-of-right repayments over $3,000, certain unrecovered investment in a pension, impairment-related work expenses, and a net qualified disaster loss. List type and amount.

### Step 9 — Compute Line 17 (Total)

```
Line 17 = Line 4 + Line 7 + Line 10 + Line 14 + Line 15 + Line 16  → Form 1040 line 12e
Line 18 = box: check only if the user elects to itemize although Line 17 is less than the standard deduction
```

2026+: if taxable income (figured before this rule and adding back itemized deductions) exceeds the start of the 37% bracket ($768,700 MFJ/QSS, $640,600 Single/HoH, $384,350 MFS for 2026, Rev. Proc. 2025-32 §4.01), itemized deductions are reduced by 2/37 of the lesser of the itemized total or that excess (IRC §68 as amended by P.L. 119-21 §70111). Check how the 2026 form implements it.

### Step 10 — Run standard-vs-itemized comparison

See [`references/standard-vs-itemized-decision.md`](./references/standard-vs-itemized-decision.md).

```
If Line 17 > standard deduction (including any additional amount for age/blindness):
  → Itemize. Line 17 flows to Form 1040 line 12e.
Else:
  → Take standard deduction. Don't file Schedule A, unless the user elects to itemize
    (line 18 box), e.g., for state purposes, or must itemize because the MFS spouse itemizes.
  → Surface the gap to the user: "Your itemized total of $X is below the standard deduction of $Y; you save $Z by taking the standard."
```

Schedule 1-A deductions (Form 1040 line 13b) apply either way and don't change this comparison. For 2026, add the §170(p) non-itemizer charitable deduction to the standard-deduction side.

For close cases (within $2,000 of standard), suggest bunching strategies — see [`references/standard-vs-itemized-decision.md`](./references/standard-vs-itemized-decision.md).

### Step 11 — Run validation checks

See **Validation** below. Run every check.

### Step 12 — Produce the deliverable

See **Output format** below.

### Step 13 — Hand off downstream

State the next forms the user will need:

- **Itemizing** → Schedule A attaches to Form 1040
- **Form 8283** if non-cash charity > $500
- **Form 4684** if casualty loss claimed
- **Form 4952** if investment interest claimed
- **Form 4868** if filing extension needed past April 15

### Step 14 — File the return (optional)

If browser-automation tooling is available and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (IRS Free File / FFFF / paid software / paper); IRS Direct File was not offered in the 2026 filing season
- Field-by-field mapping from this skill's draft to FFFF Schedule A labels
- Substantiation and record retention (generally 3 years from filing; 6 years if income is underreported by more than 25%; property records until the limitations period for the year of disposition ends)

---

## Line-by-line guidance

For full detail, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Lines 1-4 — Medical and Dental

- Only the amount above 7.5% × AGI is deductible
- See Pub 502 for the qualifying-expense list
- Most common mistakes: deducting cosmetic surgery, OTC drugs without prescription, gym memberships
- Medical mileage is at the IRS medical rate (21¢/mile for 2025; 20.5¢ / 23.5¢ for the two halves of 2026), not the business rate

### Lines 5-7 — SALT

- Pick state/local income OR sales tax for Line 5a, not both
- Real estate tax must be value-based and uniformly assessed
- SALT cap is the largest item to track each year — see year table in Step 4
- High-income phase-down: MAGI over $500,000 (2025) / $505,000 (2026) reduces the cap by 30% of the excess, not below $10,000 (MFS: half)

### Lines 8-10 — Interest

- Form 1098 is the starting point for Line 8a; if more interest was paid than the 1098 shows, enter the larger deductible amount and attach an explanation
- Acquisition debt cap: $750K (post-12/15/2017) or $1M (grandfathered)
- HELOC/equity loan: only deductible if used to buy/build/improve home
- Mortgage insurance: not deductible for 2025 (line 8d reserved); 2026+ deductible with an AGI phase-out from $100K to $109K ($50K–$54.5K MFS)

### Lines 11-14 — Charity

- 60% AGI ceiling for cash to public charities; 50% for ordinary-income property and 30% for capital gain property to public charities; 30%/20% to private foundations (Pub 526)
- 5-year carryforward for excess
- 0.5% floor on the contribution base: tax year 2026+ only (IRC §170(b)(1)(I))
- Substantiation: written acknowledgment for any gift ≥ $250; Form 8283 for non-cash > $500; appraisal for an item or group over $5,000 (not publicly traded securities)
- QCDs from IRA do NOT go on Schedule A (excluded from income: Form 1040 lines 4a/4b with the "QCD" box on line 4c, 2025 form)

### Line 15 — Casualty and Theft

- 2025: federally declared disaster only; 2026+: federally declared or State declared disaster (IRC §165(h)(5) as amended by P.L. 119-21 §70109)
- $100 per casualty floor + 10% AGI floor
- Net qualified disaster loss: line 16, not line 15
- Form 4684 required
- Theft of business property still deductible (not on Schedule A; on Schedule C)

### Line 16 — Other

- Gambling losses (capped at winnings)
- IRD federal estate tax
- Claim-of-right repayment > $3,000
- Bond premium amortization
- TCJA-eliminated 2%-floor miscellaneous deductions remain non-deductible (IRC §67(h), now without a sunset). From 2026, unreimbursed educator expenses are no longer a miscellaneous itemized deduction (IRC §67(b)(13), (g), P.L. 119-21 §70110); confirm the 2026 form's line before using it

---

## Validation

Run these checks before declaring the form ready. Surface failures, don't silently fix.

### Math checks

- [ ] Line 2 = Form 1040 line 11b
- [ ] Line 3 = Line 2 × 0.075
- [ ] Line 4 = max(0, Line 1 − Line 3)
- [ ] Line 5d = Line 5a + Line 5b + Line 5c
- [ ] Line 5e ≤ SALT cap for the year
- [ ] Line 7 = Line 5e + Line 6
- [ ] Line 8e = Line 8a + Line 8b + Line 8c (2025 form; line 8d reserved)
- [ ] Line 10 = Line 8e + Line 9
- [ ] Line 14 raw = Line 11 + Line 12 + Line 13
- [ ] If 2026+: charity reduced by 0.5% × contribution base
- [ ] Line 17 = Line 4 + Line 7 + Line 10 + Line 14 + Line 15 + Line 16 = Form 1040 line 12e

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 17 < standard deduction → itemizing is suboptimal; warn and recommend standard
- [ ] Any mortgage insurance premium on a 2025 return → not deductible for 2025; remove
- [ ] 2026+ mortgage insurance claimed with AGI > $109,000 ($54,500 MFS) → fully phased out; remove
- [ ] Line 5e exactly $10,000 and MAGI ≤ $500K and year ≥ 2025 → likely using outdated cap; recompute
- [ ] Line 8a > $50,000 and no Form 1098 source confirmed → Pub 936 may require average-balance limitation
- [ ] Line 11 + Line 12 > 60% × AGI → confirm AGI ceiling not exceeded; excess carries forward
- [ ] Non-cash item or group of similar items over $5,000 (other than publicly traded securities) with no qualified appraisal → flag substantiation risk
- [ ] Line 15 claimed without a disaster declaration cited → 2025: federally declared only; 2026+: federally or State declared
- [ ] Gambling losses on Line 16 > gambling winnings → cap at winnings
- [ ] Tax year 2026+ and Line 14 raw < AGI × 0.5% → entire charitable deduction wiped out by floor; warn
- [ ] Filer is itemizing only because of large medical bills paid via HSA/FSA → those are NOT deductible (already pre-tax)

### Cross-form checks

- [ ] If Line 12 > $500: Form 8283 required
- [ ] If Line 15 > 0: Form 4684 required
- [ ] If Line 9 > 0: Form 4952 required
- [ ] If Line 17 < standard deduction: don't file Schedule A (unless the line 18 election applies); enter standard deduction on 1040 line 12e

---

## Output format

The deliverable is a **filled draft** the user can transcribe. Format:

```markdown
# Schedule A — DRAFT for tax year YYYY

## Filing context
Filing status: Single | MFJ | MFS | HoH | QSS
AGI (Form 1040 line 11b): $XXX,XXX
MAGI (SALT phase-down): $XXX,XXX
Standard deduction for filing status (incl. age/blind additions): $XX,XXX
SALT cap applicable: $XX,XXX (with phase-down if MAGI > $500K for 2025 / $505K for 2026)

## Lines 1-4 — Medical and Dental
1. Medical and dental expenses:        $X,XXX
2. AGI:                                $XXX,XXX
3. 7.5% × AGI:                         $XX,XXX
4. Deductible medical (Line 1 − Line 3, ≥ 0): $X,XXX

## Lines 5-7 — Taxes
5a. State/local income OR sales tax:   $XX,XXX
5b. Real estate taxes:                 $X,XXX
5c. Personal property taxes:           $XXX
5d. Sum 5a+5b+5c:                      $XX,XXX
5e. SALT capped (smaller of 5d or cap):$XX,XXX
6.  Other taxes:                       $X,XXX
7.  Total taxes:                       $XX,XXX

## Lines 8-10 — Interest
8a. Mortgage interest (Form 1098):     $XX,XXX
8b. Mortgage interest not on 1098:     $X,XXX
8c. Points not on 1098:                $XXX
8d. Reserved for future use (2025 form) — 2026+: mortgage insurance per the 2026 form: $X,XXX
8e. Sum 8a-8c:                         $XX,XXX
9.  Investment interest (Form 4952):   $XXX
10. Total interest:                    $XX,XXX

## Lines 11-14 — Charity
11. Cash contributions:                $X,XXX
12. Non-cash contributions:            $X,XXX
13. Carryover from prior year:         $XXX
14. Total charity:                     $X,XXX
    Raw total: $X,XXX
    0.5% floor on contribution base (2026+): $XXX
    Effective Line 14: $X,XXX

## Line 15 — Casualty and theft
15. Casualty/theft (Form 4684):        $X,XXX
    Disaster declaration: <federal (FEMA DR-/EM- number) or, for 2026+, State>

## Line 16 — Other
16. Other itemized deductions:         $X,XXX
    Description: <gambling losses / IRD estate tax / etc.>

## Line 17 — Total itemized deductions
17. Total: Sum Lines 4+7+10+14+15+16:  $XX,XXX  (→ Form 1040 line 12e)
18. Elect to itemize although less than standard deduction: ☐

## Standard-vs-itemized comparison
Itemized (Line 17):       $XX,XXX
Standard deduction:       $XX,XXX
Recommendation: ITEMIZE | TAKE STANDARD
Difference: $X,XXX

## Required attachments
- [ ] Form 8283 (if Line 12 > $500)
- [ ] Form 4684 (if Line 15 > 0)
- [ ] Form 4952 (if Line 9 > 0)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 13>

## Sources cited in this draft
- IRS Form 1040 Schedule A (revision date YYYY-MM-DD)
- IRS Instructions for Schedule A (revision date YYYY-MM-DD)
- IRC §63 (standard deduction), §68 (2026+ overall limitation), §163(h) (interest), §164(b)(6)–(7) (SALT cap and phase-down), §165(h) (casualty), §170 (charity; §170(b)(1)(I) 0.5% floor for 2026+), §213 (medical)
- Rev. Proc. 2024-40 (2025 inflation adjustments); Rev. Proc. 2025-32 (2026)
- One Big Beautiful Bill Act (P.L. 119-21) §§70102, 70108–70111, 70120, 70424–70425
- Pub 502, 526, 530, 547, 936
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or the paper Schedule A.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Schedule A line with examples and edge cases
- [`references/salt-cap.md`](./references/salt-cap.md) — IRC §164(b)(6)–(7); year-by-year cap; OBBBA changes; high-income phase-down worksheet
- [`references/medical-expenses.md`](./references/medical-expenses.md) — Pub 502 detail; what qualifies; 7.5% AGI floor; medical mileage
- [`references/mortgage-interest.md`](./references/mortgage-interest.md) — Acquisition debt cap; HELOC rules; refinance; mortgage insurance premiums (2026+)
- [`references/charitable-contributions.md`](./references/charitable-contributions.md) — Substantiation; cash vs non-cash; AGI ceilings; 0.5% floor and non-itemizer deduction (2026+); QCDs
- [`references/standard-vs-itemized-decision.md`](./references/standard-vs-itemized-decision.md) — When to itemize; bunching strategies; common breakeven points
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Schedule A via FFFF, paid software, or paper

## Examples

End-to-end worked Schedule As. Use these as patterns when the user's situation is similar.

- [`examples/homeowner-with-mortgage-and-charity.md`](./examples/homeowner-with-mortgage-and-charity.md) — Patricia & Mike, MFJ in CA, $180K AGI; example from the blog
- [`examples/high-income-itemizer.md`](./examples/high-income-itemizer.md) — $400K AGI, large mortgage, large charitable giving
- [`examples/senior-with-medical-expenses.md`](./examples/senior-with-medical-expenses.md) — Retired filer with high out-of-pocket medical (>7.5% AGI)

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed.

- [Schedule A (Form 1040) + AI Agent Skill: Itemized Deductions Guide 2026](https://jupid.com/blog/schedule-a-itemized-deductions-2026) — Jupid's narrative companion to this skill
- [Schedule A (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sa.pdf) — the form
- [Instructions for Schedule A](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) — line-by-line IRS guidance
- [About Schedule A (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-a-form-1040) — IRS landing page
- [Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (For Individuals)
- [Publication 502](https://www.irs.gov/publications/p502) — Medical and Dental Expenses
- [Publication 526](https://www.irs.gov/publications/p526) — Charitable Contributions
- [Publication 530](https://www.irs.gov/publications/p530) — Tax Information for Homeowners
- [Publication 547](https://www.irs.gov/publications/p547) — Casualties, Disasters, and Thefts
- [Publication 936](https://www.irs.gov/publications/p936) — Home Mortgage Interest Deduction
- [Form 4684](https://www.irs.gov/pub/irs-pdf/f4684.pdf) — Casualties and Thefts
- [Form 4952](https://www.irs.gov/pub/irs-pdf/f4952.pdf) — Investment Interest Expense Deduction
- [Form 8283](https://www.irs.gov/pub/irs-pdf/f8283.pdf) — Noncash Charitable Contributions
- IRC §63 (standard deduction), §67(h) (miscellaneous itemized deductions), §68 (overall limitation, 2026+), §163(h) (mortgage and investment interest; §163(h)(3)(E) mortgage insurance), §164(b)(6)–(7) (SALT cap and phase-down), §165(h) (casualty losses), §170 (charitable contributions; §170(b)(1)(I) 0.5% floor and §170(p) non-itemizer deduction, both 2026+), §213 (medical and dental expenses)
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) — 2025 inflation adjustments; [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — 2026 inflation adjustments
- [IRS Standard Mileage Rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) — annual medical mileage
- One Big Beautiful Bill Act, P.L. 119-21 (July 4, 2025) — §70120 SALT cap $40,000 (2025) / $40,400 (2026) with the $500,000 / $505,000 MAGI phase-down; §70102 2025 standard deduction; §70108 permanent $750K acquisition debt cap and mortgage insurance premiums (2026+); §70109 permanent disaster-only casualty rule, extended to State declared disasters (2026+); §70110 miscellaneous itemized deductions; §70111 2/37 limitation (2026+); §70424 non-itemizer charitable deduction (2026+); §70425 0.5% charitable floor (2026+)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications and the One Big Beautiful Bill Act of 2025. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (high income with phaseouts, mortgage refinance with mixed-use proceeds, large non-cash charitable gifts, claim-of-right repayments) warrant a licensed tax professional's review.
