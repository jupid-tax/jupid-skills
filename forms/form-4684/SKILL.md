---
name: form-4684
description: >
  Use this skill when an individual taxpayer or solo business owner needs to
  report a casualty loss, theft loss, or disaster-related property loss on
  IRS Form 4684. Triggers on phrases like "casualty loss", "theft loss",
  "Form 4684", "federally declared disaster deduction", "Hurricane casualty
  deduction", "fire damage tax deduction", "stolen laptop tax write-off",
  "deduct flood damage", or any request to claim a §165 loss on personal-use
  or business property. Do NOT use for: business property SALES (use Form
  4797); insurance recoveries already received that simply adjust basis with
  no remaining loss; involuntary conversions where the taxpayer is electing
  to defer gain under §1033 (different reporting path).
form: Form 4684 (Casualties and Thefts)
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f4684.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i4684.pdf
---

# Form 4684 — Casualties and Thefts

This skill produces an audit-grade Form 4684 from a description of damaged or stolen property. It walks the agent through the three sections (A: personal-use; B: business / income-producing; C: theft involving §1244 or income-producing assets), applies the §165 limitation rules (especially the federally-declared-disaster restriction in §165(h)(5) for personal-use property), computes the loss, and emits a deliverable the user can transcribe to a paper or e-file form.

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

- The user is reporting a *sale* of business property (use the forthcoming `form-4797` skill)
- The property was fully reimbursed by insurance with no remaining loss — there's nothing to report on 4684 (basis is already adjusted in the user's records; the gain or loss happens at sale)
- The user has a gain because the insurance proceeds exceeded basis and they're electing §1033 deferral — that's a separate reporting path; consult a CPA
- The loss is from a decline in market value with no sudden event (e.g., a stock dropped) — that's not a casualty under §165(c)(3)
- The loss is a Ponzi-scheme / investment fraud loss — those follow Rev. Proc. 2009-20 safe harbor and are reported differently; consult a CPA
- The "loss" is normal wear and tear, gradual deterioration, termite damage, or progressive water damage — none qualify as casualties (Pub 547)

If the user's situation is ambiguous, ask before proceeding. The most common trap: post-TCJA (tax years 2018-2025), individuals can deduct personal-use casualty losses **only** if attributable to a federally declared disaster (IRC §165(h)(5)). A house fire that wasn't part of a declared disaster is not deductible on Section A. Business and income-producing property is unaffected by §165(h)(5).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** the return covers. The federal-disaster restriction in §165(h)(5) applies through 2025. Numbers (the $100 floor, 10% AGI floor) and rules can be re-extended; verify against the latest Pub 547 before filing for any year past 2025.
2. **Filer's legal name and SSN/ITIN.** Used in the Form 4684 header. Do not invent.
3. **Property classification** for each item. The agent must classify each loss as one of:
   - **Personal-use property** (home, household goods, personal vehicle) → Section A
   - **Business property** (used wholly in a trade or business) → Section B
   - **Income-producing property** (rental, investment) used for profit but not in a trade or business → Section B (different line treatment)
   - **Employee property** (used in employment) — post-TCJA, miscellaneous itemized deduction subject to 2% floor is suspended through 2025; generally not deductible on Schedule A. Confirm with user before claiming anything.
4. **Cause of loss**. One sentence describing the event (Hurricane Helene, house fire, theft of laptop). Date of loss. The agent must determine if it qualifies as a "casualty" — sudden, unexpected, or unusual (Pub 547). Gradual losses do not qualify.
5. **Federally-declared-disaster status** (Section A only). If the loss is to personal-use property and the user is in tax years 2018-2025, ask:
   - "Was this loss in a FEMA-declared federal disaster area? Do you have the FEMA-DR or EM number?"
   - If no → the loss is NOT deductible on Section A. Stop and tell the user.
   - If yes → record the FEMA disaster number; it goes in the header above Section A.
   - FEMA disaster declarations: https://www.fema.gov/disaster/declarations
6. **Adjusted basis** of each item before the loss. For purchased property, this is cost plus improvements minus depreciation taken. If unknown, ask. Don't guess — guessed basis is the single biggest audit trigger here.
7. **Fair market value** before AND after the casualty. The decline = FMV before − FMV after. For total loss, FMV after = $0. Realtor / appraiser / repair-cost estimates are acceptable evidence. Pub 584 (personal) and Pub 584-B (business) are workbooks listing common items by room or category to help the user estimate.
8. **Insurance reimbursements** received OR expected. If the user has filed an insurance claim that's pending, the loss is NOT deductible until the claim is resolved (or a reasonable estimate of recovery can be made). Ask whether the claim is settled, denied, or pending.
9. **Adjusted Gross Income (AGI)** for the tax year. Required for Section A's 10% AGI floor.

If the user has multiple items damaged in the same event, treat them as one casualty for the $100 floor (one floor per event, not per item — Section A only).

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Classify each loss

For every damaged or stolen item:

1. Classify as personal-use, business, income-producing, or employee.
2. Confirm the event qualifies as a casualty or theft under §165(c) (sudden, unexpected, or unusual).
3. If personal-use AND tax year 2018-2025: confirm federally-declared-disaster status. If not declared, the loss is not deductible on Section A. Do not file Form 4684 for it.

### Step 2 — Decide which sections of Form 4684 are needed

- Any personal-use disaster losses → **Section A** (Lines 1-18)
- Any business or income-producing property losses → **Section B** (Lines 19-39)
- Theft of §1244 stock or income-producing assets with special characterization → **Section C** (Lines 40-45). Most filers will not need Section C; ask before using it.
- Qualified disaster losses (specific federally declared disasters Congress has elevated) → **Section D** election. Verify whether the disaster is on the qualified-disaster list before electing; consult Pub 547 for the current list.

### Step 3 — For each Section A casualty: gather the per-item table

Form 4684 Section A handles up to four items per casualty event on a single Form 4684. If more than four, use additional Forms 4684. Build this internal table:

```
Per-event item table (Section A)
| Item | Description       | Cost/basis | FMV before | FMV after | Insurance | Loss   |
|------|-------------------|------------|------------|-----------|-----------|--------|
| A    | Roof              | $35,000    | $35,000    | $5,000    | $20,000   | TBD    |
| B    | Personal vehicle  | $18,000    | $14,000    | $0        | $11,000   | TBD    |
```

For each item, the **deductible loss before reimbursement** is the smaller of:
- (a) Adjusted basis (Line 20 / 23 etc.)
- (b) Decline in FMV (Line 21 minus Line 22)

Then subtract insurance reimbursement.

### Step 4 — Apply the per-event floors (Section A only)

Once the per-item losses for the event are summed:
- Subtract **$100 per casualty event** (Line 11) — IRC §165(h)(1).
- Subtract **10% of AGI** (Line 17) — IRC §165(h)(2). This applies once across ALL personal-use casualty losses on the return, not per event.

These floors do **not** apply to Section B (business) losses.

### Step 5 — For each Section B item: separate business and income-producing

Section B has two columns:
- **Trade or business** (Lines 23 col (b)(i))
- **Income-producing property** (Lines 23 col (b)(ii))

The reduction rules differ from Section A:
- The loss is the smaller of basis or decline in FMV, minus insurance.
- **No $100 floor.** **No 10% AGI floor.**
- Business losses flow to Form 4797 Part II (ordinary loss) via Section B Line 38/39 mapping.
- Income-producing property losses flow to Schedule A Line 16 (other itemized — not subject to 2% miscellaneous floor since this is a §165(c)(2) for-profit-transaction loss, but verify against current instructions).

### Step 6 — Reconcile insurance treatment

Three scenarios:

1. **Insurance claim settled, paid in full or part**: subtract the amount received on the appropriate line.
2. **Insurance claim denied**: no reduction; loss is the full amount.
3. **Claim pending**: estimate reasonable recovery; if no estimate is reasonable, the loss is generally not deductible until the year it's resolved (Pub 547). Tell the user this — they may need to wait a year.

If insurance reimbursement exceeds basis → that's a **gain**, not a loss. Form 4684 has gain reporting (Lines 15-16 Section A; Lines 32-34 Section B). The user may be able to defer the gain under §1033 if they reinvest in similar property within the replacement period (2 years for personal property, generally; 4 years for federally declared disaster). The §1033 election is separate; flag and consult a CPA.

### Step 7 — Compute the disaster-year election (Section A only)

For federally declared disasters, taxpayers may elect to claim the loss in the year **before** the loss year (the "disaster-year election" — IRC §165(i)). The election is made by:
- Filing Form 4684 with the prior-year return (or amending the prior-year return)
- Attaching a statement that includes the FEMA disaster number and election language

Ask the user: "Do you want to claim this loss on your 2024 return (prior year) instead of 2025? You'd amend 2024 with Form 1040-X. This makes sense if your 2024 AGI was lower or your refund matters faster."

This is a one-time election; once made it's irrevocable for that disaster.

### Step 8 — Compute the totals

Section A bottom-line cascade:

```
Line 12 = sum of per-item losses after insurance, after $100 floor
Line 13 = subtotal across all Section A casualties (other forms 4684 too)
Line 14 = total gains (if any)
Line 15 = Line 14 - Line 13 (if negative → keep going to Line 16)
Line 16 = (loss from line 15)
Line 17 = 10% × AGI
Line 18 = Line 16 - Line 17 (final personal-use casualty loss)
```

Line 18 flows to **Schedule A, Line 15** (itemized deduction). If the user takes the standard deduction, a personal casualty loss provides no tax benefit. Tell the user this before producing the deliverable — they may not need to file 4684 at all.

Section B bottom-line cascade:

```
Line 28-31 per item
Line 32-34 gains
Line 35-37 losses
Line 38 = total business loss → Form 4797 Part II Line 14
Line 39 = total income-producing loss → Schedule A Line 16
```

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms the user will need:

- **Section A loss > $0** → Schedule A required (must itemize); compare itemized total vs. standard deduction
- **Section B business loss** → Form 4797 Part II
- **Section B income-producing loss** → Schedule A Line 16
- **Disaster-year election** → Form 1040-X for the prior year
- **§1033 deferral on a casualty gain** → out of scope; consult CPA

### Step 12 — File the return (optional)

If filing through the agent, follow [`filing.md`](./filing.md). Form 4684 is supported by IRS Free File Fillable Forms and most paid software. IRS Direct File (as of early 2026) does NOT support Form 4684; if the user is a Direct File user, redirect to FFFF, paid software, or paper.

---

## Line-by-line guidance

For full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name(s) shown on return / Identifying number** — copied from Form 1040
- **SECTION A box at top** — for personal-use property in a federally declared disaster
- **FEMA disaster declaration number** — required; format like "DR-4856-FL" (FEMA-DR + state). Without this the IRS will reject Section A.

### Section A — Personal Use Property (Lines 1-18)

- **Line 1** — Description of properties (each a separate "Property A/B/C/D" within one event)
- **Lines 2-9** — Per-property: cost/basis, insurance, FMV before, FMV after, decline, smaller of basis/decline, loss before $100
- **Line 10** — Smallest of casualty/theft losses across columns (per item before reductions)
- **Line 11** — $100 reduction ($100 per event, regardless of number of items)
- **Line 12** — Subtract Line 11 from Line 10
- **Lines 13-15** — Roll up multiple events / gains
- **Line 16** — Total of all losses
- **Line 17** — 10% × AGI floor
- **Line 18** — Line 16 minus Line 17 → Schedule A Line 15

### Section B — Business and Income-Producing Property (Lines 19-39)

Section B has two sub-parts and two columns within each:
- **Part I (Lines 19-27)**: Casualty or theft gain/loss for THIS year, separated by holding period.
- **Part II (Lines 28-39)**: Roll-up to Form 4797.

The two columns inside Part I:
- **Column (b)(i)** — Trade or business
- **Column (b)(ii)** — Income-producing / rental / investment

**No floors apply to Section B.** The full loss (basis − insurance, capped at decline in FMV) is deductible.

### Section C — Theft Loss Deduction for Ponzi-type Investment Fraud

Use only if the user qualifies for the Rev. Proc. 2009-20 safe harbor for fraudulent investment schemes. Most filers will not need Section C. If user describes a Madoff-style fraud, flag the safe harbor and consult Pub 547 plus Rev. Proc. 2009-20.

### Section D — Election to Deduct Federally Declared Disaster Loss in Preceding Year

A check-the-box election. Section A only. Once elected, irrevocable. See Step 7.

---

## Validation

Run before declaring the form ready. Surface failures — don't silently fix.

### Math checks

- [ ] For each Section A item: Line 8 = smaller of (Line 2 basis) or (Line 5 - Line 6 = decline in FMV)
- [ ] Line 11 ($100 reduction) applied only ONCE per casualty event, even if multiple items
- [ ] Line 17 (10% AGI floor) applied only ONCE across all Section A losses on the return
- [ ] Section B: no $100 floor and no 10% AGI floor used
- [ ] Insurance reimbursement subtracted correctly (cannot reduce loss below zero — excess becomes gain)
- [ ] If gains and losses both exist in Section A, gains offset losses before the AGI floor (Line 14-16)
- [ ] Loss on Schedule A Line 15 = Line 18 of Form 4684 Section A

### Sanity checks

Surface a warning, do not block, if:

- [ ] Section A claimed without a FEMA disaster number → loss is not deductible (post-TCJA, through 2025)
- [ ] User is taking the standard deduction → personal casualty loss provides no tax benefit; consider whether to bother filing
- [ ] FMV-after equals zero but property is described as "damaged" not "destroyed" → confirm
- [ ] Insurance reimbursement > basis → this is a gain, not a loss; flag for §1033 election consideration
- [ ] Multiple items in one event but only one Property column used → consolidate or split
- [ ] Loss > $50,000 from a single event with no insurance claim filed → audit risk; ask why
- [ ] Personal vehicle loss with FMV-before equal to original cost → unusual; vehicles depreciate
- [ ] Theft loss with no police report → audit risk; the IRS expects contemporaneous documentation

### Cross-form checks

- [ ] Section A Line 18 ties to Schedule A Line 15
- [ ] Section B Line 38 ties to Form 4797 Part II Line 14
- [ ] Section B Line 39 ties to Schedule A Line 16
- [ ] Disaster-year election (Section D) requires amending the prior-year return via Form 1040-X
- [ ] FEMA disaster number matches the FEMA database (https://www.fema.gov/disaster/declarations)

---

## Output format

The deliverable is a **filled draft** the user can transcribe to Form 4684. Every line shown, including zeros.

```markdown
# Form 4684 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <filer name>
Identifying number: <SSN/EIN>
FEMA disaster declaration number: DR-XXXX-XX (Section A only)

## Section A — Personal-Use Property (Federally Declared Disaster)

### Casualty/Theft #1: <description, e.g., "Hurricane Helene, 9/26/2025">

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
| 11 | $100 reduction | $100 |
| 12 | Subtract Line 11 from Line 10 | $X |

### Roll-up across all Section A events
| 13 | Total of Line 12 (all events) | $X |
| 14 | Total gains (Line 4 across events) | $X |
| 15 | Line 14 − Line 13 (gain) or 0 | $X |
| 16 | Loss (if Line 14 < Line 13) | $X |
| 17 | 10% × AGI ($X AGI × 0.10) | $X |
| 18 | Line 16 − Line 17 → Schedule A Line 15 | $X |

## Section B — Business and Income-Producing Property
(omit if no business/income-producing losses)

### Part I — Per-item gain/loss
| Line | Description | Trade/Business (b)(i) | Income-Producing (b)(ii) |
|------|-------------|----------------------:|-------------------------:|
| 19 | Description | <item> | <item> |
| 20 | Cost or other basis | $X | $X |
| 21 | Insurance/reimbursement | $X | $X |
| 22 | Gain (Line 21 - Line 20 if pos) | $X | $X |
| 23 | FMV before | $X | $X |
| 24 | FMV after | $X | $X |
| 25 | Decline (Line 23 - Line 24) | $X | $X |
| 26 | Smaller of Line 20 or Line 25 | $X | $X |
| 27 | Subtract Line 21 from Line 26 | $X | $X |

### Part II — Roll-up to other forms
| 28 | Total losses (Line 27 sum, by holding period) | $X |
| 32 | Total gains | $X |
| 38 | Net business loss → Form 4797 Part II Line 14 | $X |
| 39 | Net income-producing loss → Schedule A Line 16 | $X |

## Section C — Theft (§1244 / Ponzi safe harbor)
N/A | (filled if applicable)

## Section D — Election to Deduct in Preceding Year
[ ] Not elected
[ ] Elected for FEMA disaster DR-XXXX-XX (file with prior-year amended return)

## Required attachments
- [ ] Schedule A (if Section A Line 18 > 0)
- [ ] Form 4797 (if Section B Line 38 > 0)
- [ ] Statement with FEMA disaster number (Section A)
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
- IRC §165(h)(5) (federally declared disaster requirement, personal-use, through 2025)
- IRC §165(i) (disaster-year election)
- FEMA disaster declaration: <DR number, link to FEMA page>
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

- [`examples/hurricane-homeowner.md`](./examples/hurricane-homeowner.md) — Section A; $80K hurricane damage in a federally declared zone; $100 + 10% AGI reductions
- [`examples/freelancer-stolen-laptop.md`](./examples/freelancer-stolen-laptop.md) — Section B; $2,500 laptop used 100% for business
- [`examples/small-business-fire.md`](./examples/small-business-fire.md) — Section B; $15K equipment fire loss with partial insurance recovery

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
- IRC §165(h)(5) — federally declared disaster requirement for personal-use casualty losses (in effect through 2025; verify status for later years)
- IRC §165(i) — disaster-year election
- IRC §1033 — involuntary conversion gain deferral
- Rev. Proc. 2009-20 — Ponzi-scheme theft loss safe harbor

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex casualty situations (large losses, disputed insurance claims, §1033 elections, Ponzi safe harbor) warrant a licensed tax professional's review.
