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
  vehicle taxes, the transit-type bus exemption (IRC §4483(c), different rules
  apply), or fuel excise tax (Form 720).
form: Form 2290 (Heavy Highway Vehicle Use Tax Return)
audience: [solo, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f2290.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2290.pdf
---

# Form 2290 — Heavy Highway Vehicle Use Tax Return

This skill produces an audit-grade Form 2290 filing package for any business or individual operating one or more highway vehicles with a taxable gross weight of 55,000 lbs or more. It walks through weight-class determination, suspension category eligibility (mileage-based), logging-rate reduction, partial-period proration for mid-year first use, and the Schedule 1 VIN list that the state DMV requires for plate registration.

Form 2290 has fewer math traps than most income-tax forms — the Tax Computation table on page 2 of the form and the Partial-Period Tax Tables at the end of the instructions do the work. The judgment lives in **filing-period timing** (federal fiscal year July 1 to June 30, not the calendar year), **EIN requirement** (no SSN allowed, even for sole props), and **suspension category** (file with $0 tax owed, do not skip filing).

**Form revision verified:** Form 2290 (Rev. July 2026, created 4/8/26) and Instructions for Form 2290 (Rev. July 2026, dated April 15, 2026), for the tax period July 1, 2026, through June 30, 2027. The IRS issues a new revision each July; re-check the next revision before using this skill for the period starting July 1, 2027: [About Form 2290](https://www.irs.gov/forms-pubs/about-form-2290).

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
- The user operates transit-type buses claiming the IRC §4483(c) exemption (60% passenger fare revenue test) — this skill assumes standard heavy-vehicle filers; redirect to a CPA
- The vehicle is owned by a federal, state, or local government, the American Red Cross, or another statutorily exempt operator (no filing required at all in those cases)

If the user's vehicle weight or use is ambiguous, ask before proceeding. The 55,000-lb threshold is **taxable gross weight**: the actual unloaded weight of the vehicle fully equipped for service, plus the unloaded weight of trailers customarily used with it, plus the maximum load customarily carried (IRC §4482(b); instructions "Taxable Gross Weight") — not curb weight. If the vehicle is registered in a state that requires a declared gross weight, taxable gross weight can't be less than the highest gross weight declared in any state (instructions "Determining Taxable Gross Weight"). A truck-tractor that pulls 80,000-lb combined loads has a taxable gross weight in that range even if the bare tractor weighs less.

---

## Prerequisites

Before producing anything, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax period** the filing covers (July 1 — June 30). For a filing made in summer 2026, the period is July 1, 2026 — June 30, 2027 (Rev. July 2026 form). A return for an earlier period needs that period's revision from irs.gov/Form2290.
2. **Filer's legal business name and EIN.** Form 2290 **cannot** be filed with an SSN. If the user is a sole prop without an EIN, instruct them to apply at [IRS.gov/EIN](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online); the IRS says to allow four weeks after the EIN is assigned before e-filing Form 2290 ([E-file Form 2290](https://www.irs.gov/e-file-providers/e-file-form-2290)).
3. **Filer's business address** as registered with the IRS.
4. **Vehicle list**, structured as: VIN, taxable gross weight, date of first use during the period, intended use (regular highway, logging, agricultural), and whether each is expected to drive 5,000 miles or fewer (7,500 if agricultural) during the period.
5. **Logging vs. non-logging classification** for each vehicle. Logging gets a 25% rate reduction (IRC §4483(e)).
6. **Agricultural vs. non-agricultural classification** for each vehicle. Agricultural use raises the suspension threshold from 5,000 miles to 7,500 miles.
7. **Mid-year first-use information** for any vehicle placed in service after July of the period start year. The tax is prorated by the number of months remaining. For a used vehicle bought from a private seller who already paid this period's tax, also ask for the sale date and whether the buyer first used it in the month of sale (instructions "Used vehicles").
8. **Credit data** if the user is claiming a credit for tax already paid on vehicles sold, destroyed, or stolen before June 1 and not used for the rest of the period, or used 5,000/7,500 miles or fewer during the **prior** period (Line 5): VIN, category, date of event, tax paid, and the purchaser's name and address for a sold vehicle.

For e-filing readiness, additionally confirm:
- The EIN was assigned **at least four weeks** ago (the IRS says an e-filed return filed earlier "might be rejected" because the name control isn't established yet: [FAQs for truckers who e-file](https://www.irs.gov/businesses/small-businesses-self-employed/faqs-for-truckers-who-e-file)).
- The user has selected an [IRS-authorized 2290 e-file provider](https://www.irs.gov/e-file-providers/e-file-form-2290). Form 2290 cannot be e-filed on IRS.gov.
- The user has banking info ready for EFW or has an EFTPS enrollment.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm filing applicability

Confirm at least one vehicle has taxable gross weight 55,000 lbs or more and is used on public highways. If no such vehicle exists, redirect: vehicles under 55,000 lbs go on Schedule C Line 9, not Form 2290.

### Step 2 — Determine tax period and deadline

Form 2290 covers a federal fiscal year, July 1 — June 30. Default rule:

- If the truck is first used on public highways in July → file by **August 31** of that year, pay full annual tax.
- If first use is mid-period → file by the **last day of the month following the month of first use**, pay prorated tax.
- If the due date falls on a Saturday, Sunday, or legal holiday, file by the next business day. For the 2026-27 period the instructions' chart gives: Sep 2026 first use → Nov 2, 2026; Dec 2026 → Feb 1, 2027; Jan 2027 → Mar 1, 2027; Apr 2027 → Jun 1, 2027; Jun 2027 → Aug 2, 2027 (full chart in [`references/tax-table.md`](./references/tax-table.md)).
- Vehicles first used in different months go on **separate** returns, one per month of first use (instructions "When To File", Example 3).

Compute and state the deadline explicitly to the user.

### Step 3 — Classify each vehicle

For each VIN, determine:

- **Weight category (A through V)** — see [`references/weight-categories.md`](./references/weight-categories.md) for the full table.
- **Standard or logging** — logging vehicles get a 25% rate reduction.
- **Active or suspended (Category W)** — vehicles expected to be used on public highways 5,000 miles or less (7,500 agricultural) during the period are filed but pay $0.
- **Full-period or partial-period** — partial-period vehicles (mid-year first use) pay a prorated tax.

### Step 4 — Compute tax per vehicle

Use [`references/tax-table.md`](./references/tax-table.md):

- Annual rate (column (1)(a)): $100 base + $22 per 1,000 pounds (or fraction) over 55,000, capped at $550 for vehicles over 75,000 lbs.
- Logging rate (column (1)(b)): 75% of the standard rate.
- Partial-period rate (column (2)): take the amount from Table I (Table II for logging) at the end of the instructions; it equals annual × months remaining ÷ 12, but Table II amounts can be $0.01 lower than that formula, so copy the table.
- Suspended: $0.

Sum column (4) across categories A–V → Line 2 (Form 2290 Part I).

### Step 5 — Compute Line 3 (Increased weight category)

If any vehicle's taxable gross weight increased during the period and it moved into a new category (e.g., heavier trailers added to a tractor), additional tax is owed: the Partial-Period Tax Table amount for the new category minus the amount for the old category, both read in the column for the month the weight increased (Line 3 worksheet, instructions p. 6). Check the Amended Return box, write the month of the increase next to it, and file by the last day of the following month. Most filings have $0 here.

### Step 6 — Compute Line 5 (Credits)

Credits available for tax already paid on:

- Vehicles **sold, destroyed, or stolen before June 1** and not used during the rest of the period: credit = tax reported on line 4 for the vehicle minus the partial-period tax for the months of use (first-use month through the month of the event). Claim it on the next Form 2290 filed (same or next period) or as a refund on Form 8849, Schedule 6.
- Vehicles **used 5,000 miles or less** (7,500 agricultural) during the prior period when full tax was paid: credit = the tax paid, claimable only after that period ends, on the first Form 2290 for the next period (or Form 8849).

Line 5 can't exceed line 4; claim any excess on Form 8849 with Schedule 6. Attach an explanation with VIN, category, date of the event, the credit worksheet, and (for a sale) the purchaser's name and address (instructions "Line 5").

### Step 7 — Compute Line 6 (Balance due)

```
Line 4 = Line 2 + Line 3                  (Total tax)
Line 6 = Line 4 − Line 5                  (Balance due)
```

### Step 8 — Build Schedule 1 (VIN list)

Every vehicle on the return goes on Schedule 1, Part II with VIN and weight category. Include suspended (Category W) vehicles. Part I: line a = total vehicles reported, line b = suspended (category W) vehicles, line c = a − b (taxable vehicles; must equal the column (3) total on page 2). Enter the month of first use (same YYYYMM as line 1). Both copies of Schedule 1 are filed on paper (one is stamped and returned), or a watermarked Schedule 1 comes back electronically when e-filing — **this is what the state DMV requires**.

### Step 9 — Complete Part II (lines that apply: current or prior-period suspended vehicles)

- **Line 7:** check the 5,000-mile box, the 7,500-mile agricultural box, or both; the category W vehicles themselves are listed on Schedule 1.
- **Line 8a:** check if vehicles listed as suspended on the prior period's Form 2290 stayed within the mileage limit; **line 8b:** list the VINs of any that exceeded it (their tax goes on a separate Form 2290 for the prior period).
- **Line 9:** list VINs of prior-period suspended vehicles sold or transferred, with the buyer and date.

### Step 10 — Run validation checks

See **Validation** below. Run every check.

### Step 11 — Produce the deliverable

See **Output format** below.

### Step 12 — Hand off downstream

State the next steps:

- **Payment method** — EFW (direct debit, e-filed returns only), EFTPS (enrollment required; submit by 8:00 p.m. ET the day before the due date), credit or debit card (processor convenience fee), or check/money order with Form 2290-V. Tax is paid in full with the return (instructions "How To Pay the Tax").
- **Stamped Schedule 1** — saved digitally; provide to state DMV for plate registration/renewal.
- **Schedule C Line 23 (Form 1120 Line 17 for C-corp, Form 1120-S Line 12 for S-corp, Form 1065 Line 14 for partnership, Schedule F Line 29 for farmers)** — "Federal highway use tax" is a taxes-and-licenses deduction (2025 Schedule C instructions, line 23) on the income tax return for the year in which it was paid.
- **Mileage tracking** for any suspended vehicles — if usage exceeds the limit, an Amended Return is due by the last day of the month following the month the limit was exceeded.
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

- **Tax period** — Printed on the form revision (Rev. July 2026 = July 1, 2026, through June 30, 2027); nothing to enter
- **Name and address** — As registered with the IRS for the EIN
- **EIN** — Required; SSN not accepted
- **"Check if applicable" boxes** (the form does not letter them):
  - **Address Change** — business address differs from prior IRS records
  - **Amended Return** — only for (a) additional tax from an increase in taxable gross weight or (b) suspended vehicles exceeding the mileage use limit; write the month next to the box
  - **VIN Correction** — correcting a VIN on a previously filed Schedule 1; use the Form 2290 revision for the period being corrected, list the corrected VIN on Schedule 1, attach an explanation
  - **Final Return** — no longer have taxable vehicles to report

### Part I — Tax Calculation

| Line | What it captures | Notes |
|------|------------------|-------|
| 1 | Month of first use during the period, as YYYYMM | July first use = 202607 for the 2026-27 period |
| 2 | Tax from Tax Computation table (page 2) | Sum across all vehicles by weight category, prorated for partial-period |
| 3 | Additional tax from increase in taxable gross weight | Rare; only if a vehicle moved up a weight class mid-period |
| 4 | Total tax | Line 2 + Line 3 |
| 5 | Credits | Sold/destroyed/stolen before June 1, or prior-period low-mileage; can't exceed Line 4 |
| 6 | Balance due | Line 4 − Line 5; check the EFTPS or Credit or debit card box if paying that way |

### Part II — Statement in Support of Suspension

Complete the lines that apply:

- **Line 7** — declare that category W vehicles are expected to be used 5,000 miles or less and/or 7,500 miles or less (agricultural) during the period
- **Line 8a / 8b** — declare that vehicles suspended on the prior period's return weren't subject to tax; list on 8b the VINs that exceeded the limit
- **Line 9** — prior-period suspended vehicles sold or transferred: VINs, buyer, date

### Schedule 1 — Schedule of Heavy Highway Vehicles

- **Part I (Summary of Reported Vehicles)** — line a total vehicles reported; line b suspended (category W); line c = a − b taxable vehicles
- **Part II (Vehicles You Are Reporting)** — VIN and category (A–V, or W) for each vehicle
- **Month of first use** box — same YYYYMM as Form 2290 line 1
- Consent to Disclosure of Tax Information (page 2 of Schedule 1) — optional; sign it to let the IRS share VIN and payment verification with DOT, CBP and state DMVs
- File both copies on paper; e-filers receive a watermarked Schedule 1

### Form 2290-V — Payment Voucher

Used only if paying by check or money order (payable to "United States Treasury"). Detach and send with the payment to Internal Revenue Service, P.O. Box 932500, Louisville, KY 40293-2500 (printed on the voucher). Don't file it when paying by EFW, EFTPS, or card.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 2 = sum of per-vehicle tax across all weight categories on the Tax Computation table
- [ ] Line 4 = Line 2 + Line 3
- [ ] Line 6 = Line 4 − Line 5
- [ ] Logging-vehicle annual tax = column (1)(b) amount (75% of the standard rate)
- [ ] Partial-period tax = Table I / Table II amount for the category and first-use month (Partial-Period Tax Tables, end of the instructions)
- [ ] Schedule 1 Part II VIN count = Part I line a; line c = line a − line b = column (3) total on page 2

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filing date is **after** the deadline (August 31 for July first-use, or last day of month after first use) → failure-to-file penalty of 5% of unpaid tax per month or part month (max 25%), reduced by the 0.5% per month failure-to-pay penalty for months both apply, plus interest (IRC §6651(a)(1), (a)(2), (c)(1))
- [ ] EIN was assigned less than four weeks ago → likely e-file rejection (name control not yet established)
- [ ] Suspension category claimed but mileage tracking method not stated → audit risk if usage is later challenged
- [ ] Logging-rate claimed but vehicles also used for non-logging hauling → IRC §4483(e) requires exclusive use for harvested forest products plus state registration as such
- [ ] Return reporting tax on 25 or more vehicles (category W not counted) filed on paper → e-filing is **mandatory** (IRC §4481(e); Reg. §41.6011(a)-1(c)(1))
- [ ] Sold/destroyed/stolen credit claimed without supporting statement → IRS will reject or hold the credit
- [ ] Single vehicle's taxable gross weight = exactly 54,999 lbs or just under 55,000 → confirm the user's weight rating; if true, no Form 2290 is required
- [ ] Vehicle expected to drive precisely 5,001 miles → no margin for error; either pay full tax or file suspension and amend if exceeded
- [ ] Vehicles first used in different months on one return → split into one return per first-use month

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
Boxes checked: Address Change | Amended Return (month: ___) | VIN Correction | Final Return | none

## Part I — Tax Calculation
1. Month of first use:                    YYYYMM
2. Tax (from Tax Computation table):      $X,XXX.XX
3. Additional tax from weight increase:   $X,XXX.XX
4. Total tax (Line 2 + Line 3):           $X,XXX.XX
5. Credits:                               $X,XXX.XX
6. Balance due (Line 4 − Line 5):         $X,XXX.XX

## Part II — Statement in Support of Suspension (if applicable)
7.  Suspended (category W) vehicles: [ ] 5,000 miles or less  [ ] 7,500 miles or less (agricultural)
    | VIN | Weight Cat | Use type (regular / agri) |
    | ... | W          | ...                      |
8a. Prior-period suspended vehicles not subject to tax: [ ] checked / N/A
8b. VINs that exceeded the limit in the prior period: <list or N/A>
9.  Prior-period suspended vehicles sold or transferred: <VINs, buyer, date, or N/A>

## Schedule 1 — Vehicles
Month of first use: YYYYMM
### Part I — Summary of Reported Vehicles
a. Total number of reported vehicles:        N
b. Suspended (category W) vehicles:          N
c. Taxable vehicles (a − b):                 N

### Part II — Vehicles You Are Reporting
| VIN              | Category |
|------------------|----------|
| 1XPXXXX...       | U        |
| ...              | ...      |

## Tax Computation Detail
| VIN | Wt | Logging? | Period | Standard Tax | This Filing |
|-----|----|----------|--------|--------------|-------------|
| ... | U  | No       | Full   | $540.00      | $540.00     |
| ... | F  | Yes      | Partial 8mo (Nov) | Table II, F, NOV (8) | $105.00 |

## Form 2290-V (only if paying by check/money order)
Payment voucher detail: box 1 EIN, box 2 amount (= line 6), box 3 YYYYMM from line 1, box 4 name and address

## Required attachments
- [ ] Schedule 1 (both copies if paper) with all VINs
- [ ] Supporting statement if Line 5 (Credits) used
- [ ] Form 2290-V if paying by check

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 12>

## Sources cited in this draft
- IRS Form 2290 (Rev. July 2026)
- IRS Instructions for Form 2290 (Rev. July 2026), incl. Partial-Period Tax Tables
- IRC §4481, §4482, §4483, §4484
- 26 CFR Part 41
```

The draft is **not** the final filed form. The user still has to enter it into a 2290 e-file provider's portal or paper-file it. The deliverable's value is that every line is computed and traceable, and the Schedule 1 is ready to send to the DMV.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 2290 line and Schedule 1 element, with examples and edge cases
- [`references/weight-categories.md`](./references/weight-categories.md) — Full weight category table A through V (22 taxable categories), plus W (suspended), with annual and logging rates
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
- [E-file Form 2290](https://www.irs.gov/e-file-providers/e-file-form-2290) — e-file steps; four-week wait for a new EIN; payment options
- [2290 MeF providers](https://www.irs.gov/e-file-providers/2290-mef-providers) — IRS list of approved 2290 e-file providers, by tax year
- [FAQs for truckers who e-file](https://www.irs.gov/businesses/small-businesses-self-employed/faqs-for-truckers-who-e-file) — EIN timing, duplicate-filing rejections, e-filed corrections
- IRC §4481 (heavy highway vehicle use tax; (e) e-file for 25+ vehicles), §4482 (definitions; (b) taxable gross weight), §4483 (exemptions: (c) transit-type buses, (d) suspension, (e) logging), §4484 (cross references)
- 26 CFR Part 41 — Excise tax on use of certain highway motor vehicles regulations (§41.6011(a)-1(c) e-file requirement; §41.6071(a)-1 due date)
- IRC §6651 — Failure to file (5% per month, max 25%) and failure to pay (0.5% per month) penalties; §6651(c)(1) offset

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (intercity bus exemption, dealer demonstration vehicles, fleet leasing arrangements, partial owner changes mid-period) warrant a licensed tax professional's or 2290 e-file provider's review.
