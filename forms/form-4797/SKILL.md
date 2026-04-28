---
name: form-4797
description: >
  Use this skill when a sole proprietor, single-member LLC, S-corp owner, or
  rental real estate investor disposes of property used in a trade or business
  and needs to fill out IRS Form 4797. Triggers on phrases like "sold business
  equipment", "sold rental property", "sold vehicle used for business",
  "depreciation recapture", "Section 1231 gain", "1245 recapture",
  "1250 recapture", "Form 4797", "what tax do I owe on selling my truck",
  "what tax on selling my rental". Do NOT use for personal stock/crypto sales
  (use form-8949 skill), Schedule C ordinary inventory sales (Schedule C
  Line 1 on the schedule-c skill), or like-kind exchanges (Form 8824 — a
  different form that defers gain rather than recognizes it).
form: Form 4797
audience: [solo, llc1, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f4797.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i4797.pdf
---

# Form 4797 — Sales of Business Property

This skill produces an audit-grade draft of Form 4797 from the user's disposition data, prior depreciation history, and 5-year §1231 history. It walks through the form's three (sometimes four) parts in the right order, applies §1231 / §1245 / §1250 / §179 / §280F rules correctly, and emits a deliverable the user can transcribe to a paper or e-file form with confidence.

The math is mechanical once the character of each gain is known. The judgment is in (a) classifying each disposed asset (§1245 vs §1250 vs ordinary), (b) recovering accumulated depreciation history, and (c) remembering the 5-year lookback. This skill optimizes for the latter — the agent should ask, not guess.

**Companion guide for end users:** [Form 4797 + AI Agent Skill: Sales of Business Property Guide 2026](https://jupid.com/blog/form-4797-business-property-sales-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 4797, "Section 1231", "1245 recapture", "1250 recapture", "depreciation recapture", or "unrecaptured §1250 gain"
- The user describes a disposition of business-use property: equipment, vehicle, machinery, livestock, breeding animals, rental real estate, or any asset previously depreciated on Form 4562
- The user is selling a rental property and asks about tax consequences
- The user took §179 or bonus depreciation on an asset and either sold it or had business use drop to ≤50%
- The user sold a business as an asset sale (allocate proceeds across asset classes per Form 8594) and needs to compute gain/loss per asset

Do **not** engage this skill when:

- The user is selling personal stock, ETF, mutual fund, or crypto → use the `form-8949` skill instead
- The user is selling inventory in the ordinary course of business → that is gross receipts on `schedule-c` Line 1 (or Form 1125-A for corporations), not Form 4797
- The user is doing a like-kind exchange of real property → use Form 8824 (deferred gain, different mechanics — no Form 4797 unless boot is received)
- The user is selling a primary residence with full §121 exclusion → no Form 4797 (or Form 8949) required
- The user is selling a partnership interest → that is a Schedule D / Form 8949 transaction with §751 hot-asset adjustment, not Form 4797 directly

If the asset has both business and personal use (e.g., a truck used 70% for business), only the business-use portion of basis, depreciation, and proceeds flows through Form 4797. The personal-use portion goes on Form 8949 / Schedule D as a personal capital asset (with the caveat that personal-use losses are non-deductible).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

### Per disposition

1. **Description of property** (e.g., "2021 Ford F-250", "rental at 123 Maple St", "CNC mill model XYZ")
2. **Date acquired** and **date sold** — together these determine §1231 eligibility (more than 1 year held)
3. **Original cost or other basis** including capitalized improvements
4. **Accumulated depreciation** ("allowed or allowable" — see ask-don't-guess rule below)
5. **Sales price (gross proceeds)**
6. **Selling expenses** (commissions, closing costs, legal fees) — reduce sales price
7. **Business-use percentage** at time of disposition and historically (matters for §179/§280F)
8. **Property character** — §1245 (personal property) or §1250 (real property)? If mixed (e.g., rental sold with appliances), allocate.

### 5-year lookback (REQUIRED for any §1231 gain)

9. **Prior 5 years of Form 4797 Part I results** — was there a net §1231 loss in any of TY-1, TY-2, TY-3, TY-4, TY-5? Specifically, the amount on Line 7 if it was negative (a net loss).
10. **Prior recapture amounts** — has any of that prior loss already been recharacterized as ordinary income in subsequent years?

If the user can't produce the prior 5 years, ask them to pull prior tax returns or note "no prior §1231 losses to my knowledge" — but the agent should warn that an unexamined lookback is the most common audit-trip on Form 4797.

### Ask-don't-guess rules

- **"Allowed or allowable" depreciation.** If the user says they didn't take depreciation in some years, ask: "Did you depreciate this asset every year you owned it?" If no, recommend Form 3115 (§481(a) catch-up) BEFORE filing 4797, because the IRS computes recapture on what they should have claimed regardless.
- **§179 vs MACRS.** If the user took §179 on a vehicle or listed property, ask whether business use ever dropped to 50% or less. If yes, Part IV applies even if they didn't sell the asset.
- **Building components.** If selling rental real estate, ask whether a cost segregation study was done. If yes, separately classify the segregated components as §1245 (full recapture) vs §1250 building (25% cap).
- **Installment sale.** Ask "Are you receiving payments over multiple years?" If yes, coordinate with Form 6252 — gain is recognized pro-rata on each payment.

---

## Workflow

Execute these steps in order. Don't skip ahead.

### Step 1 — Confirm scope

Confirm each disposed asset is property used in a trade or business or for the production of income (rental). If the user describes selling investment stock, redirect to `form-8949`. If selling inventory, redirect to `schedule-c` Line 1.

### Step 2 — Classify each disposition

For each asset, classify into one of these buckets:

| Bucket | Holding period | Character | Form 4797 location |
|--------|----------------|-----------|---------------------|
| §1231 long-term, depreciable | > 1 year | §1245 or §1250 | Part III first → residual to Part I |
| §1231 long-term, non-depreciable | > 1 year | Land, livestock | Part I direct |
| Short-term | ≤ 1 year | Ordinary | Part II Line 10 |
| §179 / §280F business-use drop | n/a | Recapture | Part IV |

### Step 3 — Compute Part III for each depreciable §1231 asset

Lines 19-25 / 26 for each property:

```
Line 20 (Sales price)
−  Line 21 (Cost basis)
=  Line 22 (Depreciation taken)
=  Line 23 (Adjusted basis = 21 − 22)
=  Line 24 (Total gain = 20 − 23)
```

Then compute recapture by character:

**§1245 (personal property — Lines 25a/b):**
```
Line 25a = depreciation allowed (= Line 22 for §1245 property)
Line 25b = lesser of Line 24 (gain) or Line 25a (depreciation)
```

The §1245 recapture amount goes to Line 32 (recapture sent to Part II Line 13). The residual gain (Line 24 − Line 25b) goes back to Part I Line 6 as §1231 gain.

**§1250 (real property post-1986 — Lines 26a-h):**
For straight-line MACRS (the only allowed method for real property post-1986), Line 26g recapture is generally **$0**. The depreciation portion is tracked separately as **unrecaptured §1250 gain** on the Schedule D Unrecaptured §1250 Gain Worksheet at a 25% federal cap.

For pre-1986 property or property with accelerated methods, Line 26 has its own additional-depreciation computation. See [`references/section-1250-recapture.md`](./references/section-1250-recapture.md).

### Step 4 — Roll Part III to Part I and Part II

- **Line 32** (total recapture) → **Part II Line 13** as ordinary
- Residual gain after recapture → **Part I Line 6** as §1231 gain

### Step 5 — Apply §1231 5-year lookback (Line 8)

Pull last 5 years of Form 4797. Sum any net §1231 losses (Part I Line 7 net negative) less any amounts already recharacterized in intervening years. Enter this unrecaptured-loss amount on Line 8.

If current Line 7 is a net §1231 gain, the lookback amount converts gain to ordinary on Line 12 of Part II. Only the excess over the lookback amount remains long-term capital gain on Line 9.

### Step 6 — Compute Part IV if applicable (§179 / §280F recapture)

If business use dropped to ≤50% on a §179 or listed-property asset before the recovery period ends:

```
Line 33 = §179 amount previously taken
Line 34 = recomputed depreciation under MACRS through year of drop
Line 35 = Line 33 − Line 34 (recapture amount)
```

This recapture flows to the form on which the original §179 was deducted (Schedule C Line 6 for sole prop), NOT to Part II of Form 4797. The recaptured amount adds to basis for future depreciation.

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

- **Part I Line 9** (long-term §1231 gain) → **Schedule D Line 11** for individuals
- **Part II Line 18** (ordinary gain/loss) → **Schedule 1 Line 4** → Form 1040 Line 8
- **Part IV Line 35** (§179 recapture) → Schedule C Line 6 (Other income)
- **Unrecaptured §1250 gain** → Schedule D Unrecaptured §1250 Gain Worksheet
- If installment sale → coordinate with **Form 6252**
- If casualty/theft → **Form 4684** first, then conclusions flow to Form 4797

### Step 10 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — §1231 Property Held More Than 1 Year (Lines 1-9)

| Line | What goes here |
|------|----------------|
| 1 | Year and Forms 1099-S info (real estate transactions reported to IRS) |
| 2 | Per-property §1231 gains/losses for non-depreciable property (land, livestock held for breeding, etc.) |
| 3 | Gain from §1231 portion of installment sales (Form 6252 carryover) |
| 4 | §1231 gain from Form 4684 (casualty/theft) |
| 5 | §1231 gain from §1231 property held in like-kind exchanges with boot (Form 8824) |
| 6 | Residual §1231 gain from Part III (after recapture is removed) |
| 7 | Combine Lines 2 through 6 — net §1231 result |
| 8 | 5-year lookback — non-recaptured net §1231 losses from prior 5 years |
| 9 | Excess of Line 7 over Line 8 — flows to Schedule D Line 11 as long-term capital gain |

### Part II — Ordinary Gains and Losses (Lines 10-18)

| Line | What goes here |
|------|----------------|
| 10 | Ordinary gains/losses on property held 1 year or less; pass-through K-1 ordinary items |
| 11 | If Line 7 (Part I) is a net loss, the loss amount is entered here as ordinary |
| 12 | §1231 gain recharacterized as ordinary by the 5-year lookback (= Line 8 if current Line 7 is a gain) |
| 13 | Recapture from Part III Line 32 |
| 14 | Other ordinary gains/losses |
| 15 | Ordinary loss from §1244 small business stock |
| 16 | Ordinary gain from §1244 small business stock recapture (rare) |
| 17 | Combined |
| 18 | Total ordinary — flows to Schedule 1 Line 4 |

### Part III — Recapture Computation (Lines 19-32)

Columns A/B/C/D for up to 4 properties on one page. Lines 19-24 establish the gain. Lines 25-30 compute recapture by section:

- **Line 25** — §1245 recapture (personal property)
- **Line 26** — §1250 recapture (real property)
- **Line 27** — §1252 recapture (farmland soil/water expenses)
- **Line 28** — §1254 recapture (oil, gas, mineral, geothermal)
- **Line 29** — §1255 recapture (cost-share payments)
- **Line 30** — Total per-column recapture
- **Line 31** — Sum across columns
- **Line 32** — Recapture sent to Part II Line 13

### Part IV — §179 and §280F Recapture (Lines 33-35)

| Line | What goes here |
|------|----------------|
| 33 | §179 deduction previously taken |
| 34 | Recomputed depreciation under MACRS |
| 35 | Difference — recapture amount, reported on the form where §179 was originally claimed |

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Each Part III column: Line 23 = Line 21 − Line 22; Line 24 = Line 20 − Line 23
- [ ] §1245 recapture (Line 25b) = lesser of Line 24 or Line 25a
- [ ] §1250 recapture (Line 26g) is appropriately computed (typically $0 for post-1986 SL MACRS)
- [ ] Line 31 = sum of Line 30 across columns
- [ ] Line 32 = Line 31 − any recapture going to other forms (rare)
- [ ] Part II Line 13 = Part III Line 32
- [ ] Part I Line 6 = sum of (Line 24 − recapture) across all §1231 depreciable properties in Part III
- [ ] Part I Line 7 = sum of Lines 2 through 6
- [ ] Part I Line 9 = Line 7 − Line 8 (if Line 7 ≥ Line 8 and both positive)
- [ ] Part II Line 18 = sum of Lines 10 through 17

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Filer claims §1245 property held more than 1 year but no depreciation was taken → "allowed or allowable" trap; recommend Form 3115 catch-up before filing
- [ ] Filer reports a §1231 gain without checking 5-year lookback → ask explicitly about prior §1231 losses
- [ ] Building sold without separating §1245 components (appliances, carpets, removable equipment) → ask if cost segregation was used; if so, Part III must split
- [ ] §179 was taken in a prior year and business use is now ≤50% but Part IV is not completed → recapture required even without sale
- [ ] Sales price + selling expenses don't reconcile with HUD-1 / 1099-S → request settlement statement
- [ ] Holding period is exactly 1 year → not §1231 (§1231 requires more than 1 year); goes to Part II Line 10
- [ ] Asset was inherited — basis is stepped-up under IRC §1014 and recapture clock effectively resets; verify decedent date-of-death FMV
- [ ] Rental property but filer never reported on Schedule E → fact-check whether it was actually held for rental; if personal-use vacation home, different rules apply

### Cross-form checks

- [ ] If Part I Line 9 > 0, ensure Schedule D Line 11 reflects the amount
- [ ] If Part II Line 18 ≠ 0, ensure Schedule 1 Line 4 reflects the amount
- [ ] If Part III contains §1250 property with depreciation, ensure Schedule D Unrecaptured §1250 Gain Worksheet is completed
- [ ] If Part IV §179 recapture, ensure it appears on Schedule C Line 6 (sole prop) or equivalent
- [ ] Form 4562 prior years reconcile to Line 22 depreciation columns
- [ ] Form 6252 (installment) is consistent with Part I Line 3 if applicable

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe. Format:

```markdown
# Form 4797 — DRAFT for tax year YYYY

## Header
Name(s) shown on return: <name>
Identifying number: <SSN/EIN>

## Part I — §1231 (Property Held > 1 Year)
| Line | Description | Acquired | Sold | Sales Price | Depreciation | Cost+Imp | Gain/Loss |
|------|-------------|----------|------|-------------|--------------|----------|-----------|
| 2    | <each property>           |          |      | $           | $            | $        | $         |
| 3    | Installment sale §1231 gain                                                    | $         |
| 4    | Form 4684 §1231 gain                                                           | $         |
| 5    | §1231 boot from like-kind exchange                                             | $         |
| 6    | §1231 gain from Part III                                                       | $         |
| 7    | Combined net §1231 gain/loss                                                   | $         |
| 8    | 5-year lookback (non-recaptured prior §1231 losses)                            | $         |
| 9    | Long-term capital gain to Schedule D Line 11                                   | $         |

## Part II — Ordinary Gains and Losses
| Line | Description                                                                     | Amount    |
| 10   | Ordinary (≤1 year held)                                                         | $         |
| 11   | Net §1231 loss from Part I Line 7 (if loss)                                     | $         |
| 12   | §1231 gain recharacterized by lookback                                          | $         |
| 13   | Recapture from Part III Line 32                                                 | $         |
| 14-17| Other ordinary                                                                  | $         |
| 18   | Total ordinary → Schedule 1 Line 4                                              | $         |

## Part III — Recapture
| Line | A: <prop1> | B: <prop2> | C: <prop3> | D: <prop4> |
|------|-----------|-----------|-----------|-----------|
| 19   | description |
| 20   | sales price |
| 21   | cost basis |
| 22   | depreciation |
| 23   | adjusted basis |
| 24   | total gain |
| 25a  | §1245 dep allowed |
| 25b  | §1245 recapture (lesser of 24 or 25a) |
| 26a-g| §1250 recapture (typically $0 post-1986 SL) |
| 27-29| §1252/§1254/§1255 (rare) |
| 30   | column total |
| 31   | sum of Line 30 |
| 32   | to Part II Line 13 |

## Part IV — §179 / §280F Recapture (if applicable)
| Line | Description | Section 179 | §280F Listed |
| 33   | Section 179 / §280F deduction previously taken | $ | $ |
| 34   | Recomputed depreciation                        | $ | $ |
| 35   | Recapture amount → form where originally claimed | $ | $ |

## Unrecaptured §1250 Gain (for Schedule D Worksheet)
| Property | Depreciation portion | Treatment |
|----------|---------------------|-----------|
| <name>   | $                   | Max 25% rate |

## Required attachments
- [ ] Form 4562 (prior depreciation history reference, not attached but cited)
- [ ] Form 6252 (if installment sale)
- [ ] Form 4684 (if casualty/theft)
- [ ] Form 8824 (if part of like-kind exchange — boot only)
- [ ] Form 8594 (if business asset sale with goodwill allocation)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings>
- Lookback: confirmed prior 5 years at $X non-recaptured §1231 loss
- Next steps: <handoff items from Step 9>

## Sources cited in this draft
- IRS Form 4797 (revision date YYYY-MM-DD)
- IRS Instructions for Form 4797 (revision date YYYY-MM-DD)
- IRC §1231, §1245, §1250, §1(h)(1)(E), §179(d)(10), §280F(b)(2), §1016(a)(2)
- Pub 544, Pub 946
- (any other authority used)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 4797 line with examples
- [`references/section-1245-recapture.md`](./references/section-1245-recapture.md) — Personal property recapture mechanics, §179 interaction
- [`references/section-1250-recapture.md`](./references/section-1250-recapture.md) — Real property recapture, unrecaptured §1250 gain, post-1986 vs pre-1986
- [`references/1231-lookback.md`](./references/1231-lookback.md) — 5-year lookback rule with worked examples
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 10 audit-trip mistakes with fixes
- [`filing.md`](./filing.md) — Browser-automation playbook (loaded only when user authorizes filing)

## Examples

End-to-end worked Form 4797s. Use these as patterns.

- [`examples/landscaper-truck-sale.md`](./examples/landscaper-truck-sale.md) — Sole prop, §1245 truck sale, full ordinary recapture
- [`examples/landlord-rental-sale.md`](./examples/landlord-rental-sale.md) — §1250 rental real estate, unrecaptured §1250 gain at 25%
- [`examples/equipment-and-179-recapture.md`](./examples/equipment-and-179-recapture.md) — §179 recapture in Part IV when business use drops

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [Form 4797 + AI Agent Skill: Sales of Business Property Guide 2026](https://jupid.com/blog/form-4797-business-property-sales-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 4797 (latest)](https://www.irs.gov/pub/irs-pdf/f4797.pdf) — the form itself
- [Instructions for Form 4797 (latest)](https://www.irs.gov/pub/irs-pdf/i4797.pdf) — line-by-line IRS guidance
- [About Form 4797](https://www.irs.gov/forms-pubs/about-form-4797) — IRS landing page with archive of past revisions
- [Publication 544](https://www.irs.gov/publications/p544) — Sales and Other Dispositions of Assets (canonical §1231/§1245/§1250 reference)
- [Publication 946](https://www.irs.gov/publications/p946) — How to Depreciate Property
- [Publication 537](https://www.irs.gov/publications/p537) — Installment Sales
- [Publication 551](https://www.irs.gov/publications/p551) — Basis of Assets
- IRC §1231 (property used in trade or business), §1245 (personal property recapture), §1250 (real property recapture), §1(h)(1)(E) (25% unrecaptured §1250 cap), §179(d)(10) (§179 recapture on business-use drop), §280F(b)(2) (listed-property recapture), §1016(a)(2) (allowed-or-allowable depreciation), §1252/§1254/§1255 (specialty recapture)
- Rev. Proc. 2024-40 — §179 limit for tax year 2025 ($1,250,000)
- IRS Reg. §1.1402(a)-6 — Form 4797 gains excluded from self-employment income

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (cost segregation, partnership/S-corp K-1 §1231 items, installment sales, like-kind exchange boot) warrant a licensed tax professional's review.
