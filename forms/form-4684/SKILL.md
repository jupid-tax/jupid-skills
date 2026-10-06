---
name: form-4684
description: >
  Use this skill when an individual taxpayer or solo business owner needs to
  report a casualty loss, theft loss, or disaster-related property loss on
  IRS Form 4684. Triggers on phrases like "casualty loss", "theft loss",
  "Form 4684", "federally declared disaster deduction", "Hurricane casualty
  deduction", "fire damage tax deduction", "stolen laptop tax write-off",
  "deduct flood damage", or any request to claim a §165 loss on personal-use
  or business property. Do NOT use for: business property SALES (use the
  form-4797 skill); insurance recoveries already received that simply adjust basis with
  no remaining loss; involuntary conversions where the taxpayer is electing
  to defer gain under §1033 (different reporting path).
form: Form 4684 (Casualties and Thefts)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f4684.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i4684.pdf
---

# Form 4684 — Casualties and Thefts

This skill produces an audit-grade Form 4684 from a description of damaged or stolen property. It walks the agent through the four sections (A: personal-use property; B: business and income-producing property; C: Ponzi-type investment scheme theft loss under Rev. Proc. 2009-20; D: election to deduct a federally declared disaster loss in the preceding year), applies the §165 limitation rules (especially the disaster restriction in §165(h)(5) for personal-use property and the qualified disaster loss rules in §165(h)(6)), computes the loss, and emits a deliverable the user can transcribe to a paper or e-file form.

**Form revision.** The line map was verified against the 2025 Form 4684 ("Created 9/26/25") and the 2025 Instructions for Form 4684 (Dec 19, 2025), filed in 2026: Section A lines 1–18, Section B lines 19–39, Section C lines 40–51, Section D lines 52–57. P.L. 119-108 (Sept. 11, 2026) changed the qualified disaster loss definition after those instructions were printed (see Step 2). Re-check the next revision and any post-release changes at https://www.irs.gov/forms-pubs/about-form-4684 before use.

The math is mechanical (smaller of basis or decline-in-FMV, minus reimbursements, minus statutory floors). The judgment is in *whether the loss is deductible at all* — and that turns on facts the user often hasn't volunteered: was the area declared a federal disaster? was the property personal-use, business, or income-producing? was the taxpayer reimbursed (even partially)?

This skill optimizes for the latter — the agent should ask, not guess.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 4684, a "casualty loss", or a "theft loss"
- The user describes property damage from a hurricane, tornado, wildfire, flood, earthquake, vandalism, terrorist action, or other sudden event
- The user describes stolen property (laptop, equipment, vehicle, cash, inventory) and asks about a tax deduction
- The user mentions a federally declared disaster (FEMA-DR or EM number) and asks about claiming losses
- The user is filing an amended return for a prior-year disaster loss (Form 4684 + Form 1040-X)

Do **not** engage this skill when:

- The user is reporting a *sale* of business property (use [`form-4797`](../form-4797/SKILL.md))
- The property was fully reimbursed by insurance with no remaining loss — there's nothing to report on 4684 (basis is already adjusted in the user's records; the gain or loss happens at sale)
- The user has a gain because the insurance proceeds exceeded basis and they're electing §1033 deferral — that's a separate reporting path; consult a CPA
- The loss is from a decline in market value with no sudden event (e.g., a stock dropped) — that's not a casualty under §165(c)(3)
- The loss is a Ponzi-type investment fraud loss and the user has not confirmed they are a "qualified investor" under Rev. Proc. 2009-20 §4.03 (as modified by Rev. Proc. 2011-58). Ask first. If they qualify and choose the safe harbor, Section C (lines 40–51) of this form computes the deduction; recommend a CPA for anything beyond the Section C arithmetic
- The "loss" is normal wear and tear, gradual deterioration, termite damage, or progressive water damage — none qualify as casualties (Pub 547)

If the user's situation is ambiguous, ask before proceeding. The most common trap: for tax years beginning after 2017, individuals can deduct personal-use casualty and theft losses **only** if attributable to a federally declared disaster (IRC §165(h)(5)). P.L. 119-21 §70109 made this permanent and, for tax years beginning after 2025, also allows losses attributable to a State declared disaster. A house fire that wasn't part of a declared disaster is not deductible on Section A, except to offset personal casualty gains (line 14, Worksheet 1-1). Business and income-producing property is unaffected by §165(h)(5).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The disaster restriction in §165(h)(5) applies to tax years beginning after 2017 with no end date (P.L. 119-21 §70109); State declared disasters count for tax years beginning after 2025. This skill's line map is the 2025 form; for a 2026 return, re-check the 2026 Form 4684 and Pub 547.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 4684 header. Do not invent.
3. **Property classification** for each item. The agent must classify each loss as one of:
   - **Personal-use property** (home, household goods, personal vehicle) → Section A
   - **Business property** (used wholly in a trade or business) → Section B
   - **Income-producing property** (rental, investment) used for profit but not in a trade or business → Section B (different line treatment)
   - **Employee property** (used in performing services as an employee) — not deductible. The 2025 instructions (Section B caution) say these losses cannot be deducted or used in the netting process, because miscellaneous itemized deductions are no longer allowed (P.L. 119-21 §70110 made that permanent). Tell the user; do not enter them.
4. **Cause of loss**. One sentence describing the event (hurricane, house fire, theft of laptop). Date of loss. The agent must determine if it qualifies as a "casualty" — sudden, unexpected, or unusual (Pub 547). Gradual losses do not qualify.
5. **Disaster status** (Section A). If the loss is to personal-use property, ask:
   - "Was this loss in a FEMA-declared federal disaster area? Do you have the FEMA DR- or EM- number?"
   - For a 2026 or later tax year, also ask: "Did the Governor declare a State disaster for this event?"
   - If no declaration applies → the loss is deductible only against personal casualty gains (line 14). With no gains, stop and tell the user.
   - If yes → record the number; check the box above line 1, enter the DR- or EM- number, and enter the ZIP code of the most affected property on line 1, Property A.
   - Then ask: "Was it a major disaster declaration (DR), and what is the FEMA incident period?" A DR major disaster can make the loss a **qualified disaster loss** ($500 reduction, no 10% AGI floor, deductible without itemizing). See Step 2.
   - FEMA disaster declarations: https://www.fema.gov/disaster/declarations
6. **Adjusted basis** of each item before the loss. For purchased property, this is cost plus improvements minus depreciation taken. If unknown, ask. Don't guess — guessed basis is the single biggest audit trigger here.
7. **Fair market value** before AND after the casualty. The decline = FMV before − FMV after. For total loss, FMV after = $0. Realtor / appraiser / repair-cost estimates are acceptable evidence. Pub 584 (personal) and Pub 584-B (business) are workbooks listing common items by room or category to help the user estimate.
8. **Insurance reimbursements** received OR expected. Enter coverage whether or not a claim was filed (instructions for line 3). If a claim has a reasonable prospect of recovery, the part that may be reimbursed is not deductible until it is reasonably certain whether it will be paid (Reg. §1.165-1(d)(2)). Ask whether the claim is settled, denied, or pending.
9. **Adjusted Gross Income (AGI)** for the tax year (2025 Form 1040, line 11b). Required for Section A's 10% AGI floor on line 17.

If the user has multiple items damaged in the same event, treat them as one casualty for the $100 floor (one floor per event, not per item — Section A only).

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Classify each loss

For every damaged or stolen item:

1. Classify as personal-use, business, income-producing, or employee.
2. Confirm the event qualifies as a casualty or theft under §165(c) (sudden, unexpected, or unusual).
3. If personal-use: confirm disaster status (Prerequisite 5). If no declaration applies and the user has no personal casualty gains, the loss is not deductible. Do not file Form 4684 for it.

### Step 2 — Decide which sections of Form 4684 are needed

- Any personal-use disaster losses → **Section A** (Lines 1-18). Use a separate Form 4684 through line 12 for each casualty or theft event.
- Any business or income-producing property losses → **Section B** (Part I lines 19-28 per event; one Part II, lines 29-39, for all events)
- Ponzi-type investment scheme theft loss under the Rev. Proc. 2009-20 safe harbor → **Section C** (Lines 40-51), whose line 51 goes to Section B line 28. Most filers will not need Section C; ask before using it.
- Election to deduct a federally declared disaster loss in the preceding tax year (§165(i)) → **Section D** (Lines 52-57), attached to the preceding-year return. See Step 7.

**Qualified disaster losses** are not a separate section. They are personal-use losses reported in Section A with $500 on line 11 and a net amount on line 15 (no 10% AGI floor). Which disasters qualify:
- 2025 instructions as printed: a major disaster declared January 1, 2020 – September 2, 2025, incident period beginning December 28, 2019 – July 4, 2025 and ending no later than August 3, 2025 (plus older listed disasters). Not COVID-19-only declarations.
- P.L. 119-108 (Sept. 11, 2026) added IRC §165(h)(6) for tax years beginning after December 31, 2024: any area with a major disaster declared under Stafford Act §401 whose incident period begins on or after December 28, 2019 and before January 1, 2027. It replaces the printed window for 2025 and later returns. The 2025 form's lines 11 and 15 already carry the mechanics; check https://www.irs.gov/forms-pubs/about-form-4684 and https://www.irs.gov/DisasterTaxRelief for IRS implementing guidance, and tell a user who filed a 2025 return without the qualified treatment that Form 1040-X may apply.
- An emergency declaration (EM) alone, or a State declared disaster, is never a qualified disaster: those losses take $100 and the 10% AGI floor.

### Step 3 — For each Section A casualty: gather the per-item table

Form 4684 Section A has four property columns per casualty event. If more than four items were damaged in the same event, use additional sheets following the format of lines 1 through 9 (instructions, Section A). Build this internal table:

```
Per-event item table (Section A)
| Item | Description       | Cost/basis | FMV before | FMV after | Insurance | Loss   |
|------|-------------------|------------|------------|-----------|-----------|--------|
| A    | Home (whole lot)  | $210,000   | $340,000   | $305,000  | $20,000   | TBD    |
| B    | Personal vehicle  | $18,000    | $14,000    | $0        | $11,000   | TBD    |
```

For personal-use real estate, measure the decline in value of the property as a whole: land, building, trees, and shrubs are one item. Figure other items separately (instructions for lines 5 and 6).

For each item, the **deductible loss before reimbursement** is the smaller of:
- (a) Cost or other basis (Line 2)
- (b) Decline in FMV (Line 7 = Line 5 minus Line 6)

Then subtract insurance reimbursement.

### Step 4 — Apply the per-event floors (Section A only)

Once the per-item losses for the event are summed:
- Subtract **$100 per casualty event** (Line 11) — IRC §165(h)(1). Enter **$500** instead for a qualified disaster loss when line 10 is larger than the total of line 4 on all Forms 4684 (instructions for line 11).
- Subtract **10% of AGI** (Line 17) — IRC §165(h)(2). This applies once across ALL personal-use casualty losses on the return, not per event. It does **not** apply to qualified disaster losses, which exit on line 15.

These floors do **not** apply to Section B (business and income-producing) losses.

### Step 5 — For each Section B item: separate business and income-producing

Section B Part II (lines 29 and 34) has two loss columns:
- **(b)(i) Trade, business, rental, or royalty property**
- **(b)(ii) Income-producing property** (property held for investment: stocks, notes, bonds, gold, silver, vacant lots, works of art)

The reduction rules differ from Section A:
- The loss is the smaller of basis or decline in FMV, minus insurance. If business or income-producing property is **totally destroyed or stolen**, line 26 is the adjusted basis from line 20 (form note on line 26; Reg. §1.165-7(b)(1)).
- **No $100 floor.** **No 10% AGI floor.**
- Held 1 year or less: line 29 → line 30 → line 31 (column (b)(i) plus (c)) goes to Form 4797 line 14; line 32 (column (b)(ii)) goes to Schedule A line 16.
- Held more than 1 year: line 34 → lines 35-37. If losses exceed gains, line 38a goes to Form 4797 line 14 and line 38b to Schedule A line 16. If gains equal or exceed losses, line 39 goes to Form 4797 line 3 (§1231).
- If Form 4797 is not otherwise required, line 31 and line 38a go to Schedule 1 (Form 1040) line 4 with the "4684" box checked (instructions for lines 31 and 38a).

### Step 6 — Reconcile insurance treatment

Three scenarios:

1. **Insurance claim settled, paid in full or part**: subtract the amount received on the appropriate line.
2. **Insurance claim denied**: no reduction; loss is the full amount.
3. **Claim pending**: enter the expected reimbursement. The part that may be reimbursed is not deductible until it is reasonably certain whether it will be paid (Reg. §1.165-1(d)(2)). If the final payment is lower, deduct the shortfall in that later year; if higher, include the excess in income in the year received to the extent the deduction reduced tax. Do not amend (Pub 547, "Reimbursement Received After Deducting Loss").

If insurance reimbursement exceeds basis → that's a **gain**, not a loss. Section A: line 4 → line 13 → line 15 (net gain to Schedule D). Section B: line 22 → line 29 or 34, column (c), or line 33 when depreciation recapture applies (Form 4797 Part III). If the reimbursement arrives in a later year, report the gain in the year received (instructions for line 4). The user may be able to postpone the gain under §1033 by buying similar replacement property within the replacement period: generally 2 years after the close of the first tax year in which any part of the gain is realized; 4 years for a main home or its contents in a federally declared disaster area (Pub. 547, "Replacement Period"). The postponement statement is separate; flag and consult a CPA.

### Step 7 — Consider the disaster-year election (Section D)

For a loss attributable to a federally declared disaster in an area warranting public or individual assistance, the taxpayer may elect to deduct the loss in the year **before** the disaster year (IRC §165(i); Reg. §1.165-11). This is available for business and income-producing disaster losses too, not only Section A. The election is made by:
- Completing Section D, Part I (lines 52-54: disaster name or description, date(s) of loss, property address with city, county, state, ZIP) on the **preceding year's** Form 4684
- Attaching it to the preceding-year original or amended return that claims the loss (Rev. Proc. 2016-53 §3)

Deadline: 6 months after the regular due date (without extensions) of the disaster-year return (Reg. §1.165-11(f)). For a 2025 disaster-year loss of a calendar-year individual, the deadline is **October 15, 2026** (instructions, "Election to deduct loss in the preceding year").

Ask the user: "Do you want to claim this loss on your 2024 return (prior year) instead of 2025? You'd file Form 1040-X for 2024 unless the 2024 return is not yet filed." Compute both years before they decide.

The election is revocable: Section D, Part II (lines 55-57) on an amended preceding-year return, filed within 90 days after the election deadline and before the disaster-year return that claims the loss (Reg. §1.165-11(d), (g)). A §165(i) election moves the loss into the preceding tax year, so that year's qualified-disaster rules apply to it.

### Step 8 — Compute the totals

Section A bottom-line cascade (lines 13-18 on one Form 4684 only):

```
Line 12 = Line 10 - Line 11, per event (each event's own Form 4684)
Line 13 = sum of Line 4 gains on all Forms 4684
Line 14 = sum of Line 12 losses on all Forms 4684 (Worksheet 1-1 if any loss is not disaster-attributable)
Line 15 = if 13 > 14: net gain → Schedule D; if equal: 0;
          if 13 < 14: 0, or with qualified disaster losses the smaller of (14 - 13)
          or line 12 of the qualified-disaster Form 4684 → Schedule A line 16 ("Net Qualified Disaster Loss")
Line 16 = Line 14 - (Line 13 + Line 15)
Line 17 = 10% × AGI (Form 1040 line 11b)
Line 18 = Line 16 - Line 17, not below 0 → Schedule A line 15
```

Line 18 flows to **Schedule A, Line 15** (itemized deduction). If the user takes the standard deduction, a line 18 loss provides no tax benefit. Tell the user this before producing the deliverable. The exception is a **net qualified disaster loss** (line 15): it goes on Schedule A line 16 and can be added to the standard deduction ("Standard Deduction Claimed With Qualified Disaster Loss" on the dotted line; total to Form 1040 line 12e), so it helps non-itemizers. If the user also files Form 6251, follow the instructions' Form 6251 line 2a rule.

Section B bottom-line cascade:

```
Line 28 = Part I loss per event (sum of Line 27, or Section C line 51)
Lines 29-31 = held 1 year or less → Line 31 to Form 4797 line 14; Line 32 to Schedule A line 16
Line 33 = casualty gains from Form 4797 line 32 (recapture cases)
Lines 34-37 = held more than 1 year
Line 38a → Form 4797 line 14; Line 38b → Schedule A line 16 (when losses exceed gains)
Line 39 → Form 4797 line 3 (when gains equal or exceed losses)
```

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms the user will need:

- **Section A line 18 > $0** → Schedule A line 15 (must itemize); compare itemized total vs. standard deduction
- **Section A line 15 net qualified disaster loss** → Schedule A line 16, itemizing or added to the standard deduction
- **Section A line 15 net gain** → Schedule D ([`schedule-d`](../schedule-d/SKILL.md))
- **Section B lines 31 / 38a / 39** → Form 4797 lines 14 / 3 ([`form-4797`](../form-4797/SKILL.md)), or Schedule 1 line 4 if Form 4797 is not otherwise required
- **Section B lines 32 / 38b** → Schedule A Line 16 ([`schedule-a`](../schedule-a/SKILL.md))
- **Disaster-year election** → Section D on the prior-year Form 4684, with the prior-year original return or Form 1040-X ([`form-1040-x`](../form-1040-x/SKILL.md))
- **§1033 deferral on a casualty gain** → out of scope; consult CPA

### Step 12 — File the return (optional)

If filing through the agent, follow [`filing.md`](./filing.md). Form 4684 is supported by IRS Free File Fillable Forms (which closes October 15, 2026 for 2025 returns) and most paid software. IRS Direct File was not offered in the 2026 filing season; do not offer it as a channel.

---

## Line-by-line guidance

For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name(s) shown on return / Identifying number** — copied from Form 1040
- **SECTION A box above line 1** — check it if the loss is attributable to a federally declared disaster
- **FEMA disaster declaration number** — "DR-" or "EM-" plus four digits (instructions example: "DR-4865"). Also enter the ZIP code of the most affected property on line 1, Property A.

### Section A — Personal Use Property (Lines 1-18)

- **Line 1** — Description of properties (each a separate "Property A/B/C/D" within one event)
- **Lines 2-9** — Per-property: 2 cost/basis, 3 insurance, 4 gain (if line 3 > line 2; then skip 5-9), 5 FMV before, 6 FMV after, 7 decline, 8 smaller of line 2 or line 7, 9 line 8 minus line 3
- **Line 10** — Sum of line 9 across columns A-D
- **Line 11** — $100 per event, regardless of number of items ($500 for qualified disaster losses)
- **Line 12** — Subtract Line 11 from Line 10
- **Line 13** — Sum of line 4 gains on all Forms 4684
- **Line 14** — Sum of line 12 losses on all Forms 4684 (Worksheet 1-1 for non-disaster losses)
- **Line 15** — Net gain to Schedule D, or 0, or net qualified disaster loss to Schedule A line 16
- **Line 16** — Line 14 minus (line 13 + line 15)
- **Line 17** — 10% × AGI floor
- **Line 18** — Line 16 minus Line 17 → Schedule A Line 15

### Section B — Business and Income-Producing Property (Lines 19-39)

Section B has two parts:
- **Part I (Lines 19-28)**: one Part I per casualty or theft; four property columns; line 28 is the event's total loss.
- **Part II (Lines 29-39)**: one Part II for all events, split by holding period (lines 29-32: 1 year or less; lines 33-39: more than 1 year).

The loss columns inside Part II:
- **Column (b)(i)** — Trade, business, rental, or royalty property
- **Column (b)(ii)** — Income-producing property (investment property)
- **Column (c)** — Gains includible in income

**No floors apply to Section B.** The full loss (basis − insurance, capped at decline in FMV) is deductible.

### Section C — Theft Loss Deduction for Ponzi-type Investment Fraud

Use only if the user qualifies for the Rev. Proc. 2009-20 safe harbor (as modified by Rev. Proc. 2011-58) and chooses it. Lines 40-45 build the qualified investment (investments plus income reported, minus withdrawals); line 46 is 0.95 with no potential third-party recovery or 0.75 if pursuing one; line 51 goes to Section B line 28, skipping lines 19-27. Part II holds the required declarations. Most filers will not need Section C. Victims of other financial scams use Section B Part I (instructions, "Losses From Financial Scams").

### Section D — Election to Deduct Federally Declared Disaster Loss in Preceding Year

Part I (lines 52-54) is the §165(i) election statement; Part II (lines 55-57) revokes a prior election. It goes on the preceding year's Form 4684, not the disaster-year return. Revocable within the Reg. §1.165-11(g) window. See Step 7.

---

## Validation

Run before declaring the form ready. Surface failures — don't silently fix.

### Math checks

- [ ] For each Section A item: Line 8 = smaller of (Line 2 basis) or (Line 7 = Line 5 - Line 6, decline in FMV)
- [ ] Line 11 ($100, or $500 for a qualified disaster loss) applied only ONCE per casualty event, even if multiple items
- [ ] Line 17 (10% AGI floor) applied only ONCE across all Section A losses on the return, and never to a net qualified disaster loss on line 15
- [ ] Section B: no $100 floor and no 10% AGI floor used
- [ ] Insurance reimbursement subtracted correctly (cannot reduce loss below zero — excess becomes gain)
- [ ] If gains and losses both exist in Section A, gains offset losses before the AGI floor (Lines 13-16)
- [ ] Business or income-producing property totally destroyed or stolen: line 26 = line 20
- [ ] Loss on Schedule A Line 15 = Line 18 of Form 4684 Section A

### Sanity checks

Surface a warning, do not block, if:

- [ ] Section A claimed without a FEMA DR/EM number (or, for 2026 and later, a State declared disaster) → loss is deductible only against personal casualty gains
- [ ] User is taking the standard deduction → a line 18 loss provides no tax benefit; a line 15 net qualified disaster loss still does (added to the standard deduction)
- [ ] FMV-after equals zero but property is described as "damaged" not "destroyed" → confirm
- [ ] Insurance reimbursement > basis → this is a gain, not a loss; flag for §1033 election consideration
- [ ] Multiple items in one event but only one Property column used → consolidate or split
- [ ] Loss > $50,000 from a single event with no insurance claim filed → audit risk; ask why
- [ ] Personal vehicle loss with FMV-before equal to original cost → unusual; vehicles depreciate
- [ ] Theft loss with no police report → audit risk; the IRS expects contemporaneous documentation

### Cross-form checks

- [ ] Section A Line 18 ties to Schedule A Line 15; Line 15 net qualified disaster loss ties to Schedule A Line 16
- [ ] Section B Lines 31 + 38a tie to Form 4797 Line 14 (or Schedule 1 line 4); Line 39 ties to Form 4797 Line 3
- [ ] Section B Lines 32 + 38b tie to Schedule A Line 16
- [ ] Disaster-year election (Section D) is on the prior-year Form 4684, with the prior-year original return or Form 1040-X, by the Reg. §1.165-11(f) deadline
- [ ] FEMA disaster number matches the FEMA database (https://www.fema.gov/disaster/declarations)

---

## Output format

The deliverable is a **filled draft** the user can transcribe to Form 4684. Every line shown, including zeros.

```markdown
# Form 4684 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <filer name>
Identifying number: <SSN/EIN>
FEMA disaster declaration number: DR-XXXX or EM-XXXX (box above line 1; ZIP code of most affected property on line 1, Property A)

## Section A — Personal-Use Property (Federally Declared Disaster)

### Casualty/Theft #1: <description, e.g., "Hurricane, 6/28/2025, DR-XXXX">

| Line | Description | Property A | Property B | Property C | Property D |
|------|-------------|-----------:|-----------:|-----------:|-----------:|
| 1 | Description | <name> | <name> | <name> | <name> |
| 2 | Cost or other basis | $X | $X | $X | $X |
| 3 | Insurance/reimbursement | $X | $X | $X | $X |
| 4 | Gain (Line 3 - Line 2 if positive) | $X | $X | $X | $X |
| 5 | FMV before casualty | $X | $X | $X | $X |
| 6 | FMV after casualty | $X | $X | $X | $X |
| 7 | Decline in FMV (Line 5 - Line 6) | $X | $X | $X | $X |
| 8 | Smaller of Line 2 or Line 7 | $X | $X | $X | $X |
| 9 | Subtract Line 3 from Line 8 (if pos) | $X | $X | $X | $X |
| 10 | Total casualty/theft loss (sum of Line 9) | $X |
| 11 | $100 ($500 if qualified disaster loss) | $X |
| 12 | Subtract Line 11 from Line 10 | $X |

### Roll-up across all Section A events (one Form 4684 only)
| 13 | Total gains (Line 4, all Forms 4684) | $X |
| 14 | Total losses (Line 12, all Forms 4684) | $X |
| 15 | Net gain → Schedule D, or 0, or net qualified disaster loss → Schedule A Line 16 | $X |
| 16 | Line 14 − (Line 13 + Line 15) | $X |
| 17 | 10% × AGI ($X AGI × 0.10) | $X |
| 18 | Line 16 − Line 17 → Schedule A Line 15 | $X |

## Section B — Business and Income-Producing Property
(omit if no business/income-producing losses)

### Part I — Per-item gain/loss (one Part I per event)
| Line | Description | Property A | Property B |
|------|-------------|-----------:|-----------:|
| 19 | Description (type, location, date acquired) | <item> | <item> |
| 20 | Cost or adjusted basis | $X | $X |
| 21 | Insurance/reimbursement | $X | $X |
| 22 | Gain (Line 21 - Line 20 if pos; then skip 23-27) | $X | $X |
| 23 | FMV before | $X | $X |
| 24 | FMV after | $X | $X |
| 25 | Decline (Line 23 - Line 24) | $X | $X |
| 26 | Smaller of Line 20 or Line 25 (Line 20 if totally destroyed/stolen) | $X | $X |
| 27 | Subtract Line 21 from Line 26 | $X | $X |
| 28 | Casualty or theft loss (sum of Line 27) | $X | |

### Part II — Summary (columns: (b)(i) trade/business/rental/royalty, (b)(ii) income-producing, (c) gains)
| 29 | Held 1 year or less, per event | (b)(i) ($X) | (b)(ii) ($X) | (c) $X |
| 30 | Totals of Line 29 | ($X) | ($X) | $X |
| 31 | Line 30 (b)(i) + (c) → Form 4797 Line 14 (or Schedule 1 line 4) | $X |
| 32 | Line 30 (b)(ii) → Schedule A Line 16 | $X |
| 33 | Gains from Form 4797 Line 32 | $X |
| 34 | Held more than 1 year, per event | (b)(i) ($X) | (b)(ii) ($X) | (c) $X |
| 35 | Total losses | ($X) | ($X) | |
| 36 | Total gains (Line 33 + Line 34 col (c)) | $X |
| 37 | Line 35 (b)(i) + (b)(ii) | ($X) |
| 38a | If 37 loss > 36: Line 35 (b)(i) + Line 36 → Form 4797 Line 14 | $X |
| 38b | If 37 loss > 36: Line 35 (b)(ii) → Schedule A Line 16 | $X |
| 39 | If 37 loss ≤ 36: Lines 36 + 37 → Form 4797 Line 3 | $X |

## Section C — Ponzi-type scheme theft loss (Rev. Proc. 2009-20), Lines 40-51
N/A | (filled if applicable; Line 51 → Section B Line 28)

## Section D — Election to Deduct in Preceding Year, Lines 52-57
[ ] Not elected
[ ] Elected: Section D Part I on the <prior year> Form 4684 (disaster, date(s) of loss, property address), filed with the prior-year return or Form 1040-X by <deadline>

## Required attachments
- [ ] Schedule A (if Section A Line 18 or Line 15 loss > 0, or Section B Line 32 / 38b > 0)
- [ ] Form 4797 (if Section B Line 31, 38a, or 39 is not zero and Form 4797 is otherwise required; else Schedule 1 line 4)
- [ ] Statement that Rev. Proc. 2018-08 safe harbor was used, naming the method (only if used; lines 5-6 left blank, decline on line 7)
- [ ] Police report for theft losses
- [ ] Repair estimates / appraisals supporting FMV decline

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Disaster status confirmed: <FEMA-DR number, declaration date>
- Insurance status: <settled / denied / pending>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 4684 (revision date YYYY)
- IRS Instructions for Form 4684 (revision date YYYY)
- IRS Pub 547 (Casualties, Disasters, and Thefts)
- IRS Pub 584 (Casualty/Theft Loss Workbook — Personal Use)
- IRS Pub 584-B (Business Workbook)
- IRC §165(c) (allowable losses)
- IRC §165(h)(1) ($100 floor)
- IRC §165(h)(2) (10% AGI floor)
- IRC §165(h)(5) (disaster requirement for personal-use losses, tax years beginning after 2017; State declared disasters for tax years beginning after 2025)
- IRC §165(h)(6) (qualified disaster losses, if claimed)
- IRC §165(i) and Reg. §1.165-11 (disaster-year election, if made)
- FEMA disaster declaration: <DR/EM number, incident period, link to FEMA page>
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 4684. The deliverable's value is that every line is computed and traceable.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every Form 4684 line in detail
- [`references/personal-vs-business.md`](./references/personal-vs-business.md) — Classifying property; the §165(h)(5) federally-declared-disaster test
- [`references/insurance-and-1033.md`](./references/insurance-and-1033.md) — Pending claims, deferred gains, replacement period rules
- [`references/disaster-year-election.md`](./references/disaster-year-election.md) — §165(i) election mechanics, when to use it, statement language
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes on Form 4684
- [`filing.md`](./filing.md) — Browser-automation playbook for FFFF, paid software, and paper filing

## Examples

End-to-end worked Form 4684 drafts. Use as patterns when situations are similar.

- [`examples/hurricane-homeowner.md`](./examples/hurricane-homeowner.md) — Section A; $80K home damage plus a vehicle in a qualified disaster; $500 reduction, no 10% AGI floor, net qualified disaster loss added to the standard deduction; §165(i) comparison
- [`examples/freelancer-stolen-laptop.md`](./examples/freelancer-stolen-laptop.md) — Section B; $2,800 laptop used 100% for business, stolen (line 26 = basis), Schedule 1 line 4
- [`examples/small-business-fire.md`](./examples/small-business-fire.md) — Section B; $12,500 of equipment destroyed, partial insurance, §1245 recapture gain through Form 4797 Part III, lines 29-38a

## Sources

Authoritative sources used by this skill. Re-verify each year — the IRS revises forms and publications annually.

- [Form 4684](https://www.irs.gov/pub/irs-pdf/f4684.pdf) — the form itself
- [Instructions for Form 4684](https://www.irs.gov/pub/irs-pdf/i4684.pdf) — line-by-line IRS guidance
- [About Form 4684](https://www.irs.gov/forms-pubs/about-form-4684) — IRS landing page with archive
- [Pub 547](https://www.irs.gov/pub/irs-pdf/p547.pdf) — Casualties, Disasters, and Thefts
- [Pub 584](https://www.irs.gov/pub/irs-pdf/p584.pdf) — Casualty, Disaster, and Theft Loss Workbook (Personal-Use Property)
- [Pub 584-B](https://www.irs.gov/pub/irs-pdf/p584b.pdf) — Business Casualty, Disaster, and Theft Loss Workbook
- [FEMA Disaster Declarations](https://www.fema.gov/disaster/declarations) — verify federally declared disaster status
- IRC §165(c) — allowable losses
- IRC §165(h)(1) — $100 per-event floor
- IRC §165(h)(2) — 10% AGI floor
- IRC §165(h)(5) — disaster requirement for personal-use casualty losses (tax years beginning after 2017; made permanent and extended to State declared disasters for tax years beginning after 2025 by P.L. 119-21 §70109)
- IRC §165(h)(6) — qualified net disaster losses, added by P.L. 119-108 (Sept. 11, 2026), effective for tax years beginning after Dec. 31, 2024: https://www.govinfo.gov/content/pkg/PLAW-119publ108/pdf/PLAW-119publ108.pdf
- P.L. 119-21 (One Big Beautiful Bill Act) §§70109, 70110, 70438: https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf
- IRC §165(i) and Reg. §1.165-11 — disaster-year election, due date (f), revocation (g)
- Rev. Proc. 2016-53, 2016-44 I.R.B. 530 — how to make and revoke the §165(i) election
- IRC §1033 — involuntary conversion gain deferral
- Rev. Proc. 2009-20 (modified by Rev. Proc. 2011-58) and Rev. Rul. 2009-9 — Ponzi-scheme theft loss safe harbor
- Rev. Proc. 2018-08 — safe harbor methods for measuring personal-use casualty losses

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex casualty situations (large losses, disputed insurance claims, §1033 elections, Ponzi safe harbor) warrant a licensed tax professional's review.
