---
name: form-720
description: >
  Use this skill when a business needs to file IRS Form 720, the Quarterly
  Federal Excise Tax Return. Triggers on phrases like "Form 720", "PCORI fee",
  "federal excise tax return", "quarterly excise tax", "sport fishing
  manufacturer tax", "self-insured health plan tax", "indoor tanning tax",
  "fuel tax credit", "ozone-depleting chemicals tax", "Schedule A excise",
  "Schedule C excise". Do NOT use for: state excise tax (state DOR forms);
  state sales/use tax; Heavy Highway Vehicle Use Tax (Form 2290 — different);
  ACA employer mandate reporting (Form 1094-C / 1095-C); air-transport tax
  filed only by airlines under separate sub-procedures.
form: Form 720 (Quarterly Federal Excise Tax Return)
audience: [scorp, ccorp]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f720.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i720.pdf
---

# Form 720 — Quarterly Federal Excise Tax Return

This skill produces an audit-grade draft of Form 720 covering the federal excise taxes a business is liable for in a given quarter. Most filers only owe one or two specific taxes (PCORI fee for self-insured health plans being the most common), so the skill spends 80% of its time on the handful of common categories and provides pointers for the rest.

The math is per-line mechanical. The judgment is in **identifying which IRS Numbers (the 100+ line items in Parts I and II) apply to the filer's business** and **distinguishing Form 720 obligations from adjacent forms (Form 2290, Form 11-C, state excise)**. When liability is unclear, the agent must ASK rather than guess — wrongly omitting an excise tax produces compounding penalties under §6651.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 720, "quarterly excise tax", "Schedule A excise", "Schedule C excise"
- The user has a **self-insured group health plan** and asks about the **PCORI fee** (Patient-Centered Outcomes Research Institute fee under IRC §4375/§4376)
- The user manufactures, produces, or imports **sport fishing equipment, archery equipment, fishing tackle boxes, fishing rods**, or other items subject to manufacturer's excise tax (IRC §4161)
- The user operates **indoor tanning services** (IRC §5000B — verify status; the tax has been subject to repeal proposals)
- The user has **fuel tax** issues: gasoline, diesel, kerosene, alternative fuels, blender's credits (IRC §4081, §4041, §6426)
- The user imports **ozone-depleting chemicals (ODC)** (IRC §4681)
- The user is a **foreign insurance issuer** subject to §4371 excise tax on policies covering US risks
- The user operates **passenger ships** or charges **air transportation** tickets (limited applicability)
- The user has **HVUT (Form 2290) credits** to reconcile on Form 720 — note: HVUT itself is reported on Form 2290, not Form 720, but credits/refunds may flow

Do **not** engage this skill when:

- The user owes **state** excise tax (different forms; varies by state — gasoline tax, alcohol tax, tobacco tax at state level)
- The user owes **Heavy Highway Vehicle Use Tax** for tractor-trailers ≥ 55,000 lbs gross weight → use the `form-2290` skill (separate skill, separate filing schedule, payable annually not quarterly)
- The user is filing **occupational tax on wagering** → use Form 11-C
- The user is filing **wagering excise** → use Form 730
- The user is reporting the **ACA employer mandate** (1094-C / 1095-C) — that's not Form 720
- The user is a small business asking about general sales tax — sales tax is state, not federal

If the user is unsure which excise taxes apply to their industry, the agent walks the IRS Number list (see `references/irs-number-catalog.md`) and asks targeted yes/no questions.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Filing entity name and EIN.** Form 720 is filed by businesses, not individuals. Sole proprietors with excise liability still use their EIN if assigned, otherwise their SSN — but most excise filers are entities with EINs.
2. **Quarter being filed.** Form 720 is quarterly:
   - Q1 = Jan, Feb, Mar; due **April 30**
   - Q2 = Apr, May, Jun; due **July 31**
   - Q3 = Jul, Aug, Sep; due **October 31**
   - Q4 = Oct, Nov, Dec; due **January 31** (next year)
   - **PCORI fee is annual on the Q2 form, due July 31.**
3. **Business address** — street, city, state, ZIP. Used in the Form 720 header.
4. **Final return flag** — is this the last Form 720 the entity will file? (Triggers a "Final return" checkbox.)
5. **Address change flag** — has the address changed since the last filing?
6. **Excise tax categories** — which IRS Numbers apply? See `references/irs-number-catalog.md`. Common ones:
   - **133** — PCORI fee (annual, on Q2 form)
   - **41/42** — Sport fishing equipment (manufacturer's tax)
   - **44** — Archery equipment
   - **140** — Indoor tanning services (status unclear in 2026 — verify before filing)
   - **104** — Foreign insurance
   - **125** — Ozone-depleting chemicals (ODC) tax
   - **62/79** — Gasoline / Diesel manufacturer
7. **For PCORI specifically** — the agent needs:
   - Plan year ending date (determines applicable rate)
   - Average number of covered lives during the plan year
   - Method used to count covered lives (actual count, snapshot, Form 5500, NAIC) — IRC Reg. §46.4376-1(c)(2)
8. **For fuel taxes** — the agent needs gallons by category and use; coordinate with Schedule C credits.
9. **For sport fishing / archery** — the agent needs total sales price (or constructive sale price for related-party transfers) and category of equipment.
10. **Prior credits / overpayments** carried from previous quarters (Schedule C of Form 720).

For first-time filers, ask whether the entity has previously filed Form 720; if not, an EIN is required and a registration may be needed for certain fuel-related activities (Form 637 — separate registration).

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm Form 720 is the right form

Walk through the anti-trigger list. If the user describes:
- Tractor-trailer use → Form 2290
- Wagering / gambling business → Form 11-C / 730
- State excise → state DOR
- ACA reporting → Forms 1094-C / 1095-C
- Sales tax → state DOR

…redirect.

### Step 2 — Identify applicable IRS Numbers

Open `references/irs-number-catalog.md`. Walk the categories with the user. Most filers only have 1–2 IRS Numbers. The most common pattern is a single PCORI-fee filing on the Q2 form.

The IRS Number is a 2-3 digit code identifying each excise tax. It appears in column (b) of Part I/Part II of Form 720. Each line on the form corresponds to one IRS Number.

### Step 3 — Compute the tax for each applicable IRS Number

Use `references/line-by-line.md` for the canonical computation per category. Common patterns:

- **PCORI (133)**: `covered_lives × applicable_rate`. Rate set by IRS notice each year. For plan years ending Oct 1, 2024 – Sep 30, 2025: $3.22/covered life (Notice 2024-83). For plan years ending Oct 1, 2025 – Sep 30, 2026: verify against IRS notice issued late 2025/early 2026.
- **Sport fishing equipment (41)**: 10% of sales price (3% for tackle boxes, electric outboard motors). IRC §4161(a).
- **Archery equipment (44)**: 11% of sales price for bows of draw weight ≥ 30 lbs and arrows; quivers, broadheads, and arrow shafts taxed separately. IRC §4161(b).
- **Indoor tanning (140)**: 10% of amount paid for indoor tanning services. IRC §5000B. (Status note: subject to repeal proposals — verify still in effect for the quarter being filed.)
- **Fuel taxes (62, 79, etc.)**: rate per gallon × taxable gallons. Rates change with statute; check Pub. 510.

### Step 4 — Complete Schedule A (excise tax liability per semi-monthly period)

Schedule A reports the **dates of liability** within the quarter for **most non-PCORI** environmental and fuel taxes. The IRS uses Schedule A to verify deposit timing (deposits required twice monthly for filers above thresholds).

PCORI does NOT require Schedule A.

### Step 5 — Complete Schedule C (claims, including HVUT credit)

Schedule C reports refundable claims:
- Fuel used for nontaxable purposes (off-highway, farming, exempt entities)
- HVUT credits (Form 2290 prorated refunds)
- Biodiesel and alternative fuel credits
- Section 6426 alternative fuel mixture credit

If the user has a HVUT credit from a sold-mid-year tractor (Form 2290 prorated), the credit appears here.

### Step 6 — Complete Schedule T (terminals — large fuel filers only)

Schedule T applies to terminal operators in the position-holding distribution chain. Most Form 720 filers will not use Schedule T.

### Step 7 — Compute total tax (Part III)

```
Part III Line 3 = sum of Part I + Part II totals (excise tax owed)
Part III Line 4 = Schedule C credits / claims
Part III Line 5 = Part III Line 3 − Line 4 (net tax)
Part III Line 6 = Deposits made during the quarter (semi-monthly EFTPS deposits)
Part III Line 7 = Overpayment from prior quarter (if any)
Part III Line 10 = Balance due (Line 5 − Line 6 − Line 7) if positive
Part III Line 11 = Overpayment if Line 6 + Line 7 > Line 5
```

### Step 8 — Verify deposit requirements

Form 720 has a semi-monthly deposit requirement for taxpayers with > $2,500 in liability per quarter for certain categories (gasoline, alcohol, tobacco — see Pub. 510). PCORI-only filers and small-volume filers can pay with the return.

If deposits were required and not made on time, a §6656 deposit penalty applies in addition to any §6651 late-filing penalty. Surface this in the validation summary.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- **Mandatory e-file via authorized provider** for many filers (IRS prefers electronic Form 720). See `filing.md` for channel decision.
- **Pay any balance due** via EFTPS (electronic), required for most business federal tax payments per Treasury Reg. §31.6302-1.
- **Set up calendar reminders** for the next quarterly deadline.
- **For PCORI**: this is the only excise tax for many filers; reminder for next year (Q2 / July 31).
- **Form 637 registration** required if the user enters a category needing IRS pre-approval (alternative fuel mixers, etc.) — coordinate with `references/registrations.md`.

### Step 12 — File (optional)

If the agent has IRS-authorized e-file tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). Form 720 e-filing is done through IRS-authorized e-file providers (not Direct File, not FFFF) — the list of providers is at https://www.irs.gov/e-file-providers/modernized-e-file-mef-forms.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level structure of Form 720:

### Header

- Quarter (Q1/Q2/Q3/Q4) and year
- Name, address, EIN
- Final return checkbox
- Address change checkbox

### Part I — Excise taxes paid by the filer

Multiple categories, each with a numbered IRS Number and a line. Examples:

| IRS No. | Category | Tax base | Rate |
|---------|----------|----------|------|
| 22 | Air transportation of persons | Amount paid | 7.5% + segment fee |
| 26 | Air transportation of property | Amount paid | 6.25% |
| 28 | Use of international air travel facilities | Per passenger | $22.20 (2025; verify 2026) |
| 29 | Transportation by water | Per passenger | $5.00 |
| 41 | Sport fishing equipment | Sales price | 10% |
| 42 | Fishing tackle boxes | Sales price | 3% |
| 44 | Archery equipment (bows ≥30# draw, arrows) | Sales price | 11% / per arrow |
| 62 | Gasoline | Per gallon | $0.184 (varies — verify Pub. 510) |
| 79 | Diesel | Per gallon | $0.244 (varies) |
| 104 | Foreign insurance | Premium | 1% / 4% / 1% by type |
| 125 | Ozone-depleting chemicals | Per pound | varies by chemical |
| 140 | Indoor tanning services | Amount paid | 10% (verify status) |

### Part II — Other excise taxes (Patient-Centered fees, special taxes)

| IRS No. | Category | Notes |
|---------|----------|-------|
| 133 | PCORI fee | Annual, on Q2 form (July 31). $3.22/covered life for plan years ending Oct 1, 2024 – Sep 30, 2025 (verify next year). |
| 64 | Inland waterways fuel tax | Per gallon |
| 51 | LUST tax (Leaking Underground Storage Tank) | Per gallon |

### Part III — Totals and balance due

Summary of Parts I and II, deposits, claims, and net tax.

### Schedule A — Excise tax liability by semi-monthly period

For applicable categories, report the date liability was incurred. Used by IRS to verify deposit timing.

### Schedule C — Claims

Refundable credits for nontaxable fuel use, alternative fuel mixtures, HVUT, etc. Each claim has a specific IRS Number and required CRN (Claim Reference Number).

### Schedule T — Terminal operations

For licensed terminal operators in the fuel distribution chain.

---

## Validation

Run these checks before declaring the form ready. Surface any failure — don't silently fix.

### Math checks

- [ ] Each IRS Number's tax = (base × rate) per the published rate for the year
- [ ] Part I subtotal = sum of all Part I IRS Numbers' tax columns
- [ ] Part II subtotal = sum of all Part II IRS Numbers' tax columns
- [ ] Part III Line 3 = Part I total + Part II total
- [ ] Part III Line 5 = Part III Line 3 − Part III Line 4
- [ ] Part III Line 10 (balance due) or Line 11 (overpayment) computed correctly
- [ ] Schedule A semi-monthly entries sum to Part I/II liabilities for tracked categories
- [ ] Schedule C claims have correct CRNs and supporting documentation reference

### Sanity checks (warn, don't block)

- [ ] PCORI rate matches the IRS notice for the relevant plan-year-ending range (verify each year)
- [ ] PCORI is filed on the **Q2 form (July 31)** — if user is filing Q1/Q3/Q4 and only PCORI applies, that's wrong; redirect to Q2 form.
- [ ] Indoor tanning IRS No. 140 — verify the tax is still in effect; subject to repeal proposals.
- [ ] Sport fishing 10% rate covers most equipment; tackle boxes and electric outboard motors are 3% — confirm classification.
- [ ] Archery: bows < 30 lbs draw weight are NOT subject to §4161(b); confirm bow specs.
- [ ] Fuel tax rates: verify against Pub. 510 for the quarter being filed; rates can change mid-year by statute.
- [ ] Deposits required for liability > $2,500/quarter for fuel/alcohol/tobacco categories — if user didn't deposit, surface §6656 risk.
- [ ] First-time filer: confirm EIN is on file with the IRS; if not, file Form SS-4 first.

### Cross-form checks

- [ ] If user has Schedule C HVUT claim, ensure they previously filed Form 2290 and the credit corresponds to a sold/destroyed/stolen vehicle.
- [ ] If user has fuel-related excise + Schedule C alternative fuel mixture credits → confirm Form 637 registration is current.
- [ ] If Form 720 reports inland waterways fuel tax (IRS No. 64) → user should verify Pub. 510 for current rate ($0.29 + LUST in 2025; verify 2026).

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to Form 720 (paper) or paste into IRS-authorized e-file software. Format:

```markdown
# Form 720 — DRAFT for Quarter [Q1/Q2/Q3/Q4] of YYYY

## Header
Name: <legal name>
EIN: <9-digit EIN>
Address: <street, city, state, ZIP>
Quarter ending: MM/DD/YYYY
Final return: [ ] Yes  [x] No
Address change: [ ] Yes  [x] No

## Part I — Excise taxes
| IRS No. | Category | Base | Rate | Tax |
|---------|----------|------|------|-----|
| <NN>    | <name>   | $X,XXX | X% | $X,XXX |
| ...     | ...      | ...    | ... | ... |
| **Subtotal Part I** | | | | $X,XXX |

## Part II — Other excise taxes (PCORI, LUST, etc.)
| IRS No. | Category | Base | Rate | Tax |
|---------|----------|------|------|-----|
| 133     | PCORI fee | <covered lives> | $X.XX | $X,XXX |
| ...     | ...       | ...              | ...    | ...    |
| **Subtotal Part II** | | | | $X,XXX |

## Part III — Totals
3.  Total tax (Part I + Part II): $X,XXX
4.  Total claims (Schedule C):    $X,XXX
5.  Net tax (Line 3 − Line 4):    $X,XXX
6.  Total deposits this quarter:  $X,XXX
7.  Overpayment from prior quarter: $X,XXX
8.  Balance due / overpayment:    $X,XXX

## Schedule A — Excise tax liability by semi-monthly period
[Only for applicable IRS Numbers — typically not used for PCORI-only filers]

| Date range | IRS No. | Liability |
|------------|---------|-----------|
| MM/01-15   | ...     | $X,XXX    |
| MM/16-end  | ...     | $X,XXX    |
| ...        | ...     | ...       |

## Schedule C — Claims (if any)
| CRN | Type of claim | Period | Amount |
|-----|---------------|--------|--------|
| 360 | Nontaxable use of gasoline | <period> | $X,XXX |
| ... | ...                        | ...      | ...    |

## Schedule T — Terminal operations (if applicable)
[Only for licensed terminal operators]

## Required attachments / next steps
- [ ] EFTPS deposit required (if liability > $2,500 for tracked categories)
- [ ] Form 637 registration current (for alternative fuel claims)
- [ ] Form 8453-EX (e-file signature) if filing electronically through MeF
- [ ] Pay any balance due via EFTPS by the quarter's due date

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings>
- Year-aware notes:
  - PCORI rate verified against Notice YYYY-XX (or flagged TBD)
  - Fuel tax rates verified against Pub. 510 (or flagged TBD)
  - Indoor tanning tax status verified (or flagged TBD)

## Sources cited in this draft
- IRS Form 720 (revision date YYYY-MM)
- IRS Instructions for Form 720 (revision date YYYY-MM)
- IRC §§4161, 4371, 4375-4377, 4661, 4671, 4681, 4701, 5000B (as applicable)
- Notice YYYY-XX (PCORI rate, if applicable)
- IRS Pub. 510 (Excise Taxes)
```

The draft is **not** the final filed form. The user (or agent, with consent) submits via IRS-authorized e-file or paper.

---

## References

Loaded on demand based on the user's category.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete walkthrough of Form 720 header, Parts I–III, and Schedules A/C/T
- [`references/irs-number-catalog.md`](./references/irs-number-catalog.md) — Lookup table of every IRS Number on Form 720 with rate, base, and statutory citation
- [`references/pcori-fee.md`](./references/pcori-fee.md) — PCORI fee deep dive: covered-lives counting methods, rate history, plan-year-end mapping, deadline (Q2 / July 31)
- [`references/fuel-taxes.md`](./references/fuel-taxes.md) — Gasoline, diesel, kerosene, alternative fuels — rates and Schedule C claim mechanics
- [`references/sport-fishing-archery.md`](./references/sport-fishing-archery.md) — Manufacturer's tax computation under §4161; sales price, constructive sale price, exemptions
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes that trigger §6651/§6656 penalties on Form 720
- [`filing.md`](./filing.md) — Browser-automation playbook: Form 720 e-file via IRS-authorized providers, paper backup

## Examples

End-to-end worked Form 720s. Use these as patterns when the user's situation is similar.

- [`examples/small-employer-pcori.md`](./examples/small-employer-pcori.md) — Small business with self-insured health plan computing PCORI fee for Q2 filing
- [`examples/sport-fishing-importer.md`](./examples/sport-fishing-importer.md) — Sport fishing equipment importer reporting §4161 manufacturer's tax with Schedule A
- [`examples/trucking-hvut-credit.md`](./examples/trucking-hvut-credit.md) — Trucking company reconciling a Form 2290 HVUT credit on Schedule C of Form 720

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the quarter being filed — rates and notices update each year.

- [Form 720 (latest)](https://www.irs.gov/pub/irs-pdf/f720.pdf) — the form itself
- [Instructions for Form 720 (latest)](https://www.irs.gov/pub/irs-pdf/i720.pdf) — line-by-line IRS guidance
- [About Form 720](https://www.irs.gov/forms-pubs/about-form-720) — IRS landing page with archive of past revisions
- [Publication 510](https://www.irs.gov/pub/irs-pdf/p510.pdf) — Excise Taxes (the deep authority)
- [Notice 2024-83](https://www.irs.gov/pub/irs-drop/n-24-83.pdf) — PCORI fee rate $3.22 for plan years ending Oct 1, 2024 – Sep 30, 2025 (verify successor notice for 2025-2026)
- IRC Subtitle D (Miscellaneous Excise Taxes) — chapters 31–36 cover Form 720 categories
- IRC §4161 — sport fishing and archery equipment manufacturer's tax
- IRC §4371 — foreign insurance excise tax
- IRC §4375 / §4376 — PCORI fee
- IRC §4661 / §4671 — chemical excise (Superfund)
- IRC §4681 — ozone-depleting chemicals
- IRC §4701 — small issue bond tax
- IRC §5000B — indoor tanning services tax (verify status)
- IRC §6651 — late-filing penalty
- IRC §6656 — failure to deposit penalty
- IRC §7503 — timely-mailing-as-timely-filing rule

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Federal excise tax has narrow industry-specific rules; complex situations (multi-jurisdiction fuel distribution, large-volume manufacturer credits, foreign-insurance treaties) warrant a licensed tax professional or excise-tax specialist.
