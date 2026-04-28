---
name: form-2290
description: >
  Use this skill when an owner-operator trucker, fleet operator, leasing company,
  ranch owner with hauling trucks, or any business operating highway vehicles with
  taxable gross weight 55,000 pounds or more needs to file IRS Form 2290 (Heavy
  Highway Vehicle Use Tax Return). Triggers on phrases like "Form 2290",
  "heavy vehicle use tax", "trucker tax filing", "HVUT", "DMV proof of payment
  for truck", "Schedule 1 for truck registration", "stamped Schedule 1",
  "file 2290 for my fleet". Do NOT use for vehicle excise tax on autos under
  55,000 lbs (those use Schedule C standard mileage / actual expense), state-level
  vehicle taxes, intercity bus exemption (different rules apply), or fuel excise
  tax (Form 720).
form: Form 2290 (Heavy Highway Vehicle Use Tax Return)
audience: [solo, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f2290.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2290.pdf
---

# Form 2290 — Heavy Highway Vehicle Use Tax Return

This skill produces an audit-grade Form 2290 filing package for any business or individual operating one or more highway vehicles with a taxable gross weight of 55,000 lbs or more. It walks through weight-class determination, suspension category eligibility (mileage-based), logging-rate reduction, partial-period proration for mid-year first use, and the Schedule 1 VIN list that the state DMV requires for plate registration.

Form 2290 has fewer math traps than most income-tax forms — the tax table on page 2 of the instructions does the work. The judgment lives in **filing-period timing** (federal fiscal year July 1 to June 30, not the calendar year), **EIN requirement** (no SSN allowed, even for sole props), and **suspension category** (file with $0 tax owed, do not skip filing).

**Companion guide for end users:** [Form 2290 + AI Agent Skill: Heavy Highway Vehicle Use Tax Guide 2026](https://jupid.com/blog/form-2290-heavy-vehicle-use-tax-2026) on the Jupid blog. Same rules in narrative form. Point human readers there for the long-form context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2290, "2290", "HVUT", or "heavy vehicle use tax"
- The user owns, operates, or leases one or more vehicles with **taxable gross weight 55,000 lbs or more** used on public highways
- The user mentions needing a "stamped Schedule 1" for the DMV
- The user is a trucker, owner-operator, fleet operator, leasing company, or rancher with hauling trucks
- The user describes a deadline around August 31 for trucking taxes
- The user describes mid-year first use of a heavy truck and asks about filing requirements

Do **not** engage this skill when:

- The vehicle's taxable gross weight is **under 55,000 lbs** → use the Schedule C vehicle expense skill (standard mileage or actual expenses on Line 9)
- The user is asking about state-level vehicle taxes, IFTA fuel tax, or registration fees → those are state matters, not Form 2290
- The user is asking about fuel excise tax (Form 720) or alternative fuel credits
- The user operates intercity buses claiming a different exemption — check Form 2290 instructions Part II, this skill assumes standard heavy-vehicle filers
- The vehicle is owned by a federal, state, or local government, the American Red Cross, or another statutorily exempt operator (no filing required at all in those cases)

If the user's vehicle weight or use is ambiguous, ask before proceeding. The 55,000-lb threshold is **taxable gross weight** (the gross vehicle weight rating combined with maximum loaded trailers commonly used) — not curb weight. A truck-tractor that pulls 80,000-lb GCWR loads has a taxable gross weight in that range even if the bare tractor weighs less.

---

## Prerequisites

Before producing anything, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax period** the filing covers (federal fiscal year July 1 — June 30). For a filing made in summer 2025, the period is July 1, 2025 — June 30, 2026.
2. **Filer's legal business name and EIN.** Form 2290 **cannot** be filed with an SSN. If the user is a sole prop without an EIN, instruct them to apply at [IRS.gov/EIN](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online) at least 2 weeks before filing.
3. **Filer's business address** as registered with the IRS.
4. **Vehicle list**, structured as: VIN, taxable gross weight, date of first use during the period, intended use (regular highway, logging, agricultural), and whether each is expected to drive 5,000 miles or fewer (7,500 if agricultural) during the period.
5. **Logging vs. non-logging classification** for each vehicle. Logging gets a 25% rate reduction (IRC §4483(e)).
6. **Agricultural vs. non-agricultural classification** for each vehicle. Agricultural use raises the suspension threshold from 5,000 miles to 7,500 miles.
7. **Mid-year first-use information** for any vehicle placed in service after July of the period start year. The tax is prorated by the number of months remaining.
8. **Prior-year credit data** if the user is claiming a credit for vehicles sold, destroyed, stolen, or used 5,000/7,500 miles or fewer in the **prior** period (Line 5).

For e-filing readiness, additionally confirm:
- The EIN has been active in IRS systems for **at least 2 weeks** (newly issued EINs are not yet propagated to the 2290 e-file ecosystem).
- The user has selected an [IRS-authorized 2290 e-file provider](https://www.irs.gov/e-file-providers/e-file-form-2290).
- The user has banking info ready for EFW or has an EFTPS enrollment.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filing applicability

Confirm at least one vehicle has taxable gross weight 55,000 lbs or more and is used on public highways. If no such vehicle exists, redirect: vehicles under 55,000 lbs go on Schedule C Line 9, not Form 2290.

### Step 2 — Determine tax period and deadline

Form 2290 covers a federal fiscal year, July 1 — June 30. Default rule:

- If the truck is in service on July 1 of the period start year → file by **August 31** of that year, pay full annual tax.
- If first use is mid-period → file by the **last day of the month following the month of first use**, pay prorated tax.

Compute and state the deadline explicitly to the user.

### Step 3 — Classify each vehicle

For each VIN, determine:

- **Weight category (A through V)** — see [`references/weight-categories.md`](./references/weight-categories.md) for the full table.
- **Standard or logging** — logging vehicles get a 25% rate reduction.
- **Active or suspended (Category W)** — vehicles expected to drive 5,000 miles or fewer (7,500 agricultural) per period are filed but pay $0.
- **Full-period or partial-period** — partial-period vehicles (mid-year first use) pay a prorated tax.

### Step 4 — Compute tax per vehicle

Use [`references/tax-table.md`](./references/tax-table.md):

- Annual rate: $100 base + ($22 × thousands of pounds over 55,000), capped at $550 for 75,000+ lbs.
- Logging rate: 75% of the standard rate.
- Partial-period rate: standard rate × (months remaining in period ÷ 12).
- Suspended: $0.

Sum across all vehicles → Line 2 (Form 2290 Part I).

### Step 5 — Compute Line 3 (Increased weight category)

If any vehicle's taxable gross weight increased during the period (e.g., heavier trailers added to a tractor), additional tax may be owed. Calculate per Form 2290 instructions p. 5. Most filings have $0 here.

### Step 6 — Compute Line 5 (Credits)

Credits available for:

- Vehicles **sold, destroyed, or stolen** during the prior period (prorated refund of the unused months).
- Vehicles that **used 5,000 miles or fewer** (7,500 agricultural) in the prior period when full tax was paid.

Credit is taken on the current period's filing as a reduction on Line 5. Attach a supporting statement with VIN, date of event, and calculation.

### Step 7 — Compute Line 6 (Balance due)

```
Line 4 = Line 2 + Line 3                  (Total tax)
Line 6 = Line 4 − Line 5                  (Balance due)
```

### Step 8 — Build Schedule 1 (VIN list)

Every vehicle on the return goes on Schedule 1 with VIN and weight category. Include suspended (Category W) vehicles. Schedule 1 is filed in duplicate on paper or returned as an electronic stamped PDF when e-filing — **this is what the state DMV requires**.

### Step 9 — Complete Part II if any vehicles are suspended

For each Category W vehicle, list VIN and certify projected usage. Also list vehicles that were suspended in the prior period and stayed under the threshold (no tax owed).

### Step 10 — Run validation checks

See **Validation** below. Run every check.

### Step 11 — Produce the deliverable

See **Output format** below.

### Step 12 — Hand off downstream

State the next steps:

- **Payment method** — EFW (direct debit), EFTPS, card (with convenience fee), or check with Form 2290-V.
- **Stamped Schedule 1** — saved digitally; provide to state DMV for plate registration/renewal.
- **Schedule C Line 23 (or Form 1120 Line 17 for C-corp / Form 1120-S for S-corp)** — the HVUT amount paid is deductible as taxes and licenses on the income tax return for the calendar year in which it was paid.
- **Mileage tracking** for any suspended vehicles — if usage exceeds the threshold mid-year, an Amended Return is required.
- **Next year's reminder** — set August 1 reminder for the next tax period.

### Step 13 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Decision tree to pick a filing channel (IRS-authorized 2290 e-file provider vs. paper)
- Field-by-field mapping from this skill's draft to common e-file provider portals
- EIN propagation pre-check
- Submission state machine (Submitted → IRS Accepted → Schedule 1 Stamped)
- Security rules — never store EIN, banking credentials, or PIN beyond the filing session; require explicit consent before submission

If the user only wants a draft, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Tax period** — Enter "July 1, YYYY through June 30, YYYY+1"
- **Name and address** — As registered with the IRS for the EIN
- **EIN** — Required; SSN not accepted
- **Reason for Filing checkboxes:**
  - **A** — Address Change (if business address differs from prior IRS records)
  - **B** — Amended Return (mileage exceeded; weight increased mid-period)
  - **C** — VIN Correction (correcting a typo from a prior 2290; no tax due)
  - **D** — Final Return (no longer have any qualifying vehicles)

### Part I — Tax Calculation

| Line | What it captures | Notes |
|------|------------------|-------|
| 1 | Date of first use during the period | Most full-year filers enter July of the period start year |
| 2 | Tax from Tax Computation table (page 2) | Sum across all vehicles by weight category, prorated for partial-period |
| 3 | Additional tax from increase in taxable gross weight | Rare; only if a vehicle moved up a weight class mid-period |
| 4 | Total tax | Line 2 + Line 3 |
| 5 | Credits | Sold/destroyed/stolen/under-mileage vehicles from prior period |
| 6 | Balance due | Line 4 − Line 5; this is what you pay |

### Part II — Statement in Support of Suspension

Required only if any vehicle is filed under Category W. Three sub-statements:

- **(a)** Certify listed vehicles will be used 5,000 miles or fewer (7,500 agricultural) during the period
- **(b)** List vehicles sold during the prior period that were under suspension
- **(c)** Certify prior-period suspended vehicles whose usage stayed under the limit (carries forward $0 credit eligibility)

### Schedule 1 — Vehicles for Which Tax Is Reported

- **Part I** — VINs of vehicles being reported on this return (with weight category)
- **Part II** — Total number of taxable vehicles reported, count of suspended vehicles
- File in duplicate on paper; stamped electronically by the IRS for e-filers

### Form 2290-V — Payment Voucher

Used only if paying by check or money order. Detach and include with payment. Mail to the address in the instructions for your state.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 2 = sum of per-vehicle tax across all weight categories on the Tax Computation table
- [ ] Line 4 = Line 2 + Line 3
- [ ] Line 6 = Line 4 − Line 5
- [ ] Logging-vehicle tax = 75% of standard rate (rounded to nearest cent per Form instructions)
- [ ] Partial-period tax = standard rate × (months remaining ÷ 12), per the partial-period table on page 2
- [ ] Schedule 1 VIN count = number of vehicles in Part I + suspended vehicles in Part II

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filing date is **after** the deadline (August 31 for July first-use, or last day of month after first use) → late penalty (4.5% per month, max 25%) applies
- [ ] EIN was issued less than 2 weeks ago → likely e-file rejection due to propagation lag
- [ ] Suspension category claimed but mileage tracking method not stated → audit risk if usage is later challenged
- [ ] Logging-rate claimed but vehicles also used for non-logging hauling → IRS expects exclusive or near-exclusive forestry use
- [ ] Fleet of 25 or more vehicles filed on paper → e-filing is **mandatory** under Reg. §41.6011(a)-1(b)
- [ ] Sold/destroyed/stolen credit claimed without supporting statement → IRS will reject or hold the credit
- [ ] Single vehicle's taxable gross weight = exactly 54,999 lbs or just under 55,000 → confirm the user's weight rating; if true, no Form 2290 is required
- [ ] Vehicle expected to drive precisely 5,001 miles → no margin for error; either pay full tax or file suspension and amend if exceeded

### Cross-form checks

- [ ] HVUT paid amount is captured for the user's income tax return (Schedule C Line 23, or Form 1120 / 1120-S equivalent)
- [ ] State DMV plate renewal is on the user's calendar — they need the stamped Schedule 1
- [ ] If suspension claimed, mileage log method is in place for the period

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 2290 or paste into an e-file provider's portal. Format:

```markdown
# Form 2290 — DRAFT for tax period July 1, YYYY — June 30, YYYY+1

## Header
Name: <legal business name>
Address: <address>
EIN: <EIN — required>
Tax period: July 1, YYYY through June 30, YYYY+1
Reason for filing: [A] Address change | [B] Amended | [C] VIN correction | [D] Final | none

## Part I — Tax Calculation
1. Date of first use:                     MM/YYYY
2. Tax (from Tax Computation table):      $X,XXX.XX
3. Additional tax from weight increase:   $X,XXX.XX
4. Total tax (Line 2 + Line 3):           $X,XXX.XX
5. Credits:                               $X,XXX.XX
6. Balance due (Line 4 − Line 5):         $X,XXX.XX

## Part II — Statement in Support of Suspension (if applicable)
(a) Vehicles certified for suspension this period:
    | VIN | Weight Cat | Use type (regular / agri) |
    | ... | W          | ...                      |
(b) Sold prior-period suspended vehicles: <list or N/A>
(c) Carry-forward suspended vehicles: <list or N/A>

## Schedule 1 — Vehicles
### Part I — Reported Vehicles
| VIN              | Weight Category |
|------------------|-----------------|
| 1XPXXXX...       | U (75,000 lbs)  |
| ...              | ...             |

### Part II — Summary
- Total taxable vehicles: N
- Suspended (Category W) vehicles: N

## Tax Computation Detail
| VIN | Wt | Logging? | Period | Standard Tax | This Filing |
|-----|----|----------|--------|--------------|-------------|
| ... | U  | No       | Full   | $540.00      | $540.00     |
| ... | F  | Yes      | Partial 8mo | $210.00 × 0.75 × 8/12 | $105.00 |

## Form 2290-V (only if paying by check/money order)
Payment voucher detail: <name, EIN, amount, period>

## Required attachments
- [ ] Schedule 1 (in duplicate if paper) with all VINs
- [ ] Supporting statement if Line 5 (Credits) used
- [ ] Form 2290-V if paying by check

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 12>

## Sources cited in this draft
- IRS Form 2290 (revision date YYYY-MM-DD)
- IRS Instructions for Form 2290 (revision date YYYY-MM-DD)
- IRC §4481, §4482, §4483, §4484
- 26 CFR Part 41
```

The draft is **not** the final filed form. The user still has to enter it into a 2290 e-file provider's portal or paper-file it. The deliverable's value is that every line is computed and traceable, and the Schedule 1 is ready to send to the DMV.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 2290 line and Schedule 1 element, with examples and edge cases
- [`references/weight-categories.md`](./references/weight-categories.md) — Full weight category table A through V, plus W (suspended), with annual and logging rates
- [`references/tax-table.md`](./references/tax-table.md) — Annual, partial-period, and logging tax computation with worked examples
- [`references/suspension.md`](./references/suspension.md) — Category W rules: 5,000-mile and 7,500-mile (agricultural) thresholds, mileage tracking, mid-year amendments
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files Form 2290 via an IRS-authorized 2290 e-file provider, paper, or hands off to the user

## Examples

End-to-end worked Form 2290 returns. Use these as patterns when the user's situation is similar.

- [`examples/owner-operator-hector.md`](./examples/owner-operator-hector.md) — Single 75,000-lb truck, full-period, owner-operator
- [`examples/fleet-jenna-30-trucks.md`](./examples/fleet-jenna-30-trucks.md) — 30-truck mixed fleet, mandatory e-file
- [`examples/agricultural-sarah.md`](./examples/agricultural-sarah.md) — Single cattle-hauling truck, suspension category at 7,500-mile agricultural threshold

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax period being filed — the IRS revises forms each cycle.

- [Form 2290 + AI Agent Skill: Heavy Highway Vehicle Use Tax Guide 2026](https://jupid.com/blog/form-2290-heavy-vehicle-use-tax-2026) — Jupid's narrative companion, written for human readers
- [Form 2290 (latest)](https://www.irs.gov/pub/irs-pdf/f2290.pdf) — the form itself
- [Instructions for Form 2290 (latest)](https://www.irs.gov/pub/irs-pdf/i2290.pdf) — line-by-line IRS guidance
- [About Form 2290](https://www.irs.gov/forms-pubs/about-form-2290) — IRS landing page
- [E-file Form 2290 — Authorized Providers](https://www.irs.gov/e-file-providers/e-file-form-2290) — list of approved 2290 e-file software vendors
- IRC §4481 (heavy highway vehicle use tax), §4482 (definitions), §4483 (exemptions including suspension and logging), §4484 (cross references)
- 26 CFR Part 41 — Excise tax on use of certain highway motor vehicles regulations
- IRC §6651 — Failure to file or pay penalty (4.5% per month rule)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (intercity bus exemption, dealer demonstration vehicles, fleet leasing arrangements, partial owner changes mid-period) warrant a licensed tax professional's or 2290 e-file provider's review.
