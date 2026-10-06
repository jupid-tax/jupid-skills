---
name: form-656
description: >
  Use this skill when an individual, sole proprietor, or business entity wants to
  settle an IRS tax debt for less than the full balance through an offer in
  compromise based on doubt as to collectibility or effective tax administration,
  and needs Form 656 prepared together with Form 433-A (OIC) or Form 433-B (OIC).
  Triggers on phrases like "offer in compromise", "Form 656", "OIC", "settle my
  tax debt", "pay less than I owe the IRS", "433-A OIC", "433-B OIC", "reasonable
  collection potential", "minimum offer amount", "lump sum offer", "periodic
  payment offer", "OIC low-income certification", "$205 offer fee", "can the IRS
  take less". Do NOT use for: disputing whether the tax is owed at all (doubt as
  to liability is Form 656-L; this skill only routes it, and the 433-A (OIC) math
  does not apply); paying the full balance over time — use form-9465; removing
  penalties — use form-843; a taxpayer in an open bankruptcy proceeding (not
  eligible); state tax settlements (each state runs its own program).
form: Form 656 (Offer in Compromise), with Form 433-A (OIC) and Form 433-B (OIC)
audience: [individual, solo, freelance, llc1, llcm, scorp, ccorp, partnership]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f656b.pdf
---

# Form 656 — Offer in Compromise (with Form 433-A (OIC) and Form 433-B (OIC))

This skill produces an audit-grade draft of an offer in compromise package: an eligibility screen, the Form 433-A (OIC) or Form 433-B (OIC) financial statement computed line by line, the minimum offer amount, and a filled Form 656 with payment terms. The arithmetic is short. The judgment concentrates in three places: whether the taxpayer is eligible at all, whether the taxpayer could pay in full (in which case the IRS generally will not accept an offer), and which allowable-expense figures belong in Box E, which must come from the IRS Collection Financial Standards tables, never from estimates.

There are no separate instructions: the Form 656-B booklet carries the instructions and the forms. This line map was verified against the **Form 656-B booklet (Rev. 4-2026)**, which contains **Form 656 (Rev. 4-2026)**, **Form 433-A (OIC) (Rev. 4-2026)** and **Form 433-B (OIC) (Rev. 4-2026)**, plus the separate **Form 656-L (Rev. 7-2026)**. The IRS revises these forms and their dollar allowances; re-check the current revision at https://www.irs.gov/forms-pubs/about-form-656 before every use.

**Companion guide for end users:** [IRS Offer in Compromise 2026: Form 656 Step by Step, the $205 Fee, and How the IRS Calculates Your Minimum Offer](https://jupid.com/blog/offer-in-compromise-form-656-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## Hard rule: ask, never estimate

Every asset value, loan balance, account balance, income figure, and expense amount on Form 433-A (OIC) or Form 433-B (OIC) comes from the user and the user's documents. Ask for each one. Do not fill a figure from a typical value, a prior conversation, or a guess.

Allowable living expenses are the place agents most often invent numbers. Lines (39) and (45) of Form 433-A (OIC) take the full IRS standard amount, and lines (40) through (43) are capped in practice at the local standard. Those amounts live only in the IRS Collection Financial Standards tables at https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards (standards effective June 29, 2026, per that page). If you cannot read the current table for the user's household size, county, and region, stop and tell the user that Box E cannot be finished until the table values are in hand. Never estimate them.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions an offer in compromise, Form 656, Form 433-A (OIC), Form 433-B (OIC), or "settling" with the IRS
- The user owes federal tax, has filed the returns, has received a bill, and says they cannot pay the full balance before the IRS collection period ends
- The user has a balance-due notice and asks whether the IRS will accept less
- The user wants to check eligibility before paying a tax-resolution firm
- The user has a business entity (corporation, partnership, LLC) with federal tax debt it cannot pay

Do **not** engage this skill when:

- The user disputes that the tax is owed. That is doubt as to liability on **Form 656-L**, with no fee and no payment (Form 656-L (Rev. 7-2026), page 2). See [`references/eligibility-and-alternatives.md`](./references/eligibility-and-alternatives.md) for routing; the 433-A (OIC) calculation does not apply to a 656-L offer.
- The user can pay the full balance over time. Route to [`../form-9465/SKILL.md`](../form-9465/SKILL.md) (installment agreement). The Form 656-B booklet, page 1, says the IRS generally will not accept an offer if the debt can be paid in full through an installment agreement and/or equity in assets.
- The user wants penalties removed. Route to [`../form-843/SKILL.md`](../form-843/SKILL.md). Abatement is often worth trying first, since it shrinks the balance an offer must address.
- The user or the business is in an open bankruptcy proceeding (Form 656-B, page 1: not eligible).
- The debt is a state tax. State programs use their own forms.
- The user needs an account transcript to find assessment dates and balances. Use [`../form-4506-t/SKILL.md`](../form-4506-t/SKILL.md) or the IRS online account first, then return here.

Sibling skills the offer depends on: current-year estimated payments ([`../form-1040-es/SKILL.md`](../form-1040-es/SKILL.md)), current-quarter employment tax deposits for employers ([`../form-941/SKILL.md`](../form-941/SKILL.md)), and business income figures for Form 433-A (OIC) Section 6 ([`../schedule-c/SKILL.md`](../schedule-c/SKILL.md)).

---

## Prerequisites

Collect these before producing anything. If any item is missing, ask for it with a tight question and stop until the user answers.

1. **Who owes.** Individual, joint spouses, sole proprietor, or entity (corporation, partnership, LLC). Ask whether either spouse also owes a separate liability (for example a trust fund recovery penalty); that requires two Forms 656 (Form 656-B, page 4).
2. **Every tax period owed** with balance and assessment date, from an IRS account transcript or notices: form type (1040, 941, 940, TFRP, other) and period end date. Ask for the transcript if the user only has a rough total.
3. **Eligibility facts** (Form 656-B, page 1): all required returns filed; a bill received for at least one listed debt; current-year estimated tax payments made; for employers, federal tax deposits made for the current quarter and the two preceding quarters; no open bankruptcy; no open audit or innocent spouse claim; ITIN not deactivated.
4. **Household.** County of residence, state, household size, ages (65 or older matters for the health care standard), dependents claimed, who contributes to household income, and whether the user lived in AZ, CA, ID, LA, NM, NV, TX, WA or WI while married in the last ten years (Form 433-A (OIC), Section 1 checkbox).
5. **Every asset**, domestic and foreign: bank accounts (most recent statement balance), investment and digital asset accounts, retirement accounts, life insurance cash value, real property, vehicles, valuables, furniture and personal effects, and for the self-employed, business bank accounts, equipment, receivables. For each: current market value and loan balance, with the document it came from.
6. **Monthly income** for every household member who contributes: gross wages, Social Security, pensions, other income, interest, distributions, net rental income, net business income, child support, alimony. Ask for the averaging period for self-employment income (Form 433-A (OIC), Section 6 allows 6 to 12 months).
7. **Monthly expenses, actual amounts**, for lines (40) through (51), with proof the user is actually paying them (IRM 5.8.5.22.4: unsubstantiated court-ordered payments, child care, life insurance, other secured debt, and other expenses are treated as not paid).
8. **Collection Financial Standards lookups** for lines (39) and (45), and the local housing and transportation standards to compare against lines (40) to (42). See the hard rule above.
9. **Payment option the user can fund**: lump sum (20% with the offer, rest in 5 or fewer payments within 5 months of acceptance) or periodic (6 to 24 months), and the source of the money (Form 656, Section 6).
10. **Low-Income Certification facts**: adjusted gross income from the most recently filed Form 1040, household size, and state (48 states/DC/territories, Alaska, or Hawaii) (Form 656, Section 1).

---

## Workflow

Execute in order. Do not skip ahead to the offer amount.

### Step 1 — Classify the request

Ask: "Do you agree that you owe this tax, and the problem is paying it?" If no, route to Form 656-L (doubt as to liability) and stop the 433-A (OIC) workflow. Form 656-L, page 4: a DATL offer and a DATC offer cannot be pending at the same time; if both are sent, the Form 656 offer is returned and any payment is kept.

### Step 2 — Run the eligibility screen

Use [`references/eligibility-and-alternatives.md`](./references/eligibility-and-alternatives.md). Any failed item ends the workflow with a to-do list (file the missing return, make the estimated payment, wait for the bill, finish the bankruptcy). Tell the user plainly what happens if they submit anyway: the IRS applies the initial payment to the debt and returns the offer and the application fee, with no appeal (Form 656-B, page 1).

### Step 3 — Decide which forms and how many

- Individual, sole proprietor, TFRP, individual excise liability, or estate of a deceased individual: Form 433-A (OIC).
- Corporation, partnership, or LLC: Form 433-B (OIC), and the business files its own Form 656 (Section 2).
- Individual and business debts together: two separate Form 656 packages, each with its own fee and payment (Form 656-B, page 4).
- Joint debt plus a separate debt of one spouse: two Forms 656. Legally separated and living apart, or divorced: no joint offer; each spouse files separately (Form 656-B, page 4).

### Step 4 — Build Section 3 of Form 433-A (OIC): personal assets

Apply the form's arithmetic exactly. Full map in [`references/collection-information-statements.md`](./references/collection-information-statements.md). Key rules from Form 433-A (OIC) (Rev. 4-2026), Section 3:

- Line (1) bank accounts: total minus $1,000.
- Lines (2a) to (2d) investment and digital assets: current market value minus loan balance (no 0.8 factor on the form).
- Line (3) retirement accounts: current market value × .8 minus loan balance. The form notes the reduction may be larger because of tax consequences and withdrawal penalties; ask the user for an estimate of those if they want a larger reduction, and attach the support.
- Line (4) life insurance cash value minus loan balance.
- Line (5) real property: current market value × .8 minus loan balance.
- Line (6) vehicles: market value × .8 minus loan; subtract $3,450 on line (6b); subtract $3,450 on line (6d) only if this is a joint offer; leased vehicles are 0.
- Line (7) valuables and remaining furniture and personal effects: × .8 minus loan, then minus $11,980 for the total.
- Box A = lines (1) through (7). Never enter a negative number on any line.

Those allowances ($1,000, $3,450) are applied only after the IRS determines the taxpayer cannot full pay (Form 656-B, page 1; IRM 5.8.5.7 and 5.8.5.12). Use them for the offer computation, and recompute without them for the full-pay screen in Step 8.

### Step 5 — Sections 4 to 6 if self-employed

Complete Section 4 (business information), Section 5 (business assets: line (8) bank accounts, line (9) other assets at × .8 minus loan, with 0 entered for leased assets and assets used in the production of income, line (10) tools of trade deduction, line (11)), Box B, and Section 6 (monthly business income lines (12) to (17), expenses lines (18) to (29), Box C). Non-cash expenses such as depreciation are not allowed (Form 433-A (OIC), line (36)). If the user has an interest in an entity other than a sole proprietorship, Form 433-B (OIC) is also required (Form 433-A (OIC), Sections 2 and 4).

Line (10) is blank on the printed form. See [`references/collection-information-statements.md`](./references/collection-information-statements.md) for how to treat it; never fill it silently.

### Step 6 — Section 7: household income and allowable expenses

Box D is gross monthly household income, lines (30) through (38). Box E is lines (39) through (51). Look up lines (39) and (45) in the current Collection Financial Standards and enter the full standard even if the user spends less (Form 433-A (OIC), Section 7 note). Enter actual amounts on the other lines, and compare lines (40) to (42) with the local standards: the IRS generally allows the lesser of actual or standard (Collection Financial Standards page; IRM 5.8.5.22.2 and 5.8.5.22.3). Flag every line where actual exceeds the standard; the user must document why. Box F = Box D minus Box E, never below 0. Detail in [`references/rcp-calculation.md`](./references/rcp-calculation.md).

### Step 7 — Section 8: minimum offer

- Box G = Box F × 12 for a lump-sum offer (5 or fewer payments within 5 months).
- Box H = Box F × 24 for a periodic offer (6 to 24 months).
- Offer amount = Box A + Box B (if applicable) + Box G or Box H; must be more than $0, whole dollars.

For business entities, Form 433-B (OIC) Section 5: Box A + Box E (× 12) or Box F (× 24).

If fewer than 12 or 24 months remain on the collection statute for **all** tax periods in the offer, IRM 5.8.5.25 uses the remaining months instead. Compute the collection statute expiration date (CSED) for each period from the assessment dates; see [`references/rcp-calculation.md`](./references/rcp-calculation.md).

### Step 8 — Full-pay screen

Compare the balance with what the user could pay before the CSEDs from equity (computed without the $1,000 and $3,450 allowances) plus monthly remaining income. If the user can full pay, stop: the IRS generally will not accept the offer (Form 656-B, page 1). Explain, then route to [`../form-9465/SKILL.md`](../form-9465/SKILL.md). Recommend the user confirm with the IRS Offer in Compromise Pre-Qualifier (IRS.gov/OICtool) or the Individual Online Account eligibility check (Form 656-B, cover page).

### Step 9 — Choose payment terms and check Low-Income Certification

Compare the lump-sum and periodic offer amounts with the cash the user can raise and when. Check Low-Income Certification against the table in Form 656, Section 1 (see [`references/line-by-line.md`](./references/line-by-line.md)). If the user qualifies, no application fee and no payments are sent while the offer is considered; the first payment is due 30 calendar days after acceptance (Form 656-B, page 3).

### Step 10 — Fill Form 656

Section by section per [`references/line-by-line.md`](./references/line-by-line.md): Section 1 or 2 (never both), Section 3 (one box), Section 4 (one payment option), Section 5 (designation and EFTPS numbers), Section 6 (source of funds and compliance checkboxes), Section 8 signatures, Section 9 if a paid preparer prepared it.

### Step 11 — Validate and produce the deliverable

Run **Validation** below. Produce the **Output format** draft.

### Step 12 — Filing handoff

Follow [`filing.md`](./filing.md): Individual Online Account submission for individuals, or mail to the Memphis or Brookhaven Centralized Offer in Compromise unit by state, with the $205 fee and initial payment paid separately (unless Low-Income Certification applies).

---

## Line-by-line guidance

Full Form 656 map: [`references/line-by-line.md`](./references/line-by-line.md). Full Form 433-A (OIC) and Form 433-B (OIC) maps: [`references/collection-information-statements.md`](./references/collection-information-statements.md). Rules that cause most errors:

| Item | Rule | Source |
|------|------|--------|
| Form 656, top | Answer whether the IRS Pre-Qualifier or IOLA eligibility check was used. Optional but recommended. | Form 656 (Rev. 4-2026), page 1 |
| Section 1 vs 2 | Fill one, never both. Individuals, sole proprietors, TFRP, partnership-liable individuals use Section 1. | Form 656, page 1 |
| Tax periods | List every period owed in the formats shown (Form 1040 as 12-31-YYYY; quarters as 03-31-YYYY). The IRS may add assessed periods you missed and remove periods with no balance (Section 7(a), 7(b)). | Form 656, pages 1, 4 |
| Low-Income Certification | Check one of the two boxes only if AGI (latest Form 1040) or household gross monthly income × 12 is at or below the table amount. Not available to entities other than sole proprietors or to a deceased individual's offer. | Form 656, page 2 |
| Section 3 | Exactly one box: doubt as to collectibility, ETA economic hardship (individuals only), or ETA public policy/equity. | Form 656, page 3 |
| Section 4 lump sum | 20% initial payment with the offer; remaining balance in up to 5 payments within 5 months of acceptance. | Form 656, page 3; IRC §7122(c)(1)(A) |
| Section 4 periodic | First payment with the offer; payments on a chosen day 1 to 28; total term no more than 24 months; keep paying while the offer is pending or it is returned without appeal rights. | Form 656, page 3; IRC §7122(c)(1)(B) |
| Section 5 | EFTPS or IOLA payments: list the 15-digit electronic funds transfer number and date; electronic fee and initial payment must be made the same date the offer is mailed or filed. | Form 656, page 4 |
| Section 6 | Source of funds, plus filing and tax-payment checkboxes. Include a complete copy of any return filed within 10 weeks of the offer submission. | Form 656, page 4 |
| Section 8 | Taxpayer and spouse (joint) or corporate officer sign under penalties of perjury. | Form 656, page 7 |

### Form 433-A (OIC) lines that carry the math

| Line / box | Formula printed on the form | Most common error |
|---|---|---|
| (1) | Bank accounts (1a)+(1b)+(1c) − $1,000 | Applying the $1,000 to business accounts on line (8) |
| (2) | Investments and digital assets at market value − loans | Applying × .8 (the form does not) |
| (3) | Retirement × .8 − loans | Leaving out an IRA because "it is for retirement" |
| (4) | Life insurance cash value − loans | Listing term policies (no cash value) |
| (5) | Real property × .8 − loans | Using the tax-assessed value without asking |
| (6b), (6d) | Vehicle equity − $3,450; second vehicle only on a joint offer | Two allowances on a single offer |
| (7) | (7a)+(7b)+(7c) − $11,980 | Subtracting $11,980 from (7a) only |
| (9) | Business assets × .8 − loans; 0 if leased or used in the production of income | Leaving out the asset description and value when entering 0 |
| (10) | Tools-of-trade deduction; no amount printed | Filling it silently |
| Box C | Business income − expenses; no depreciation | Keeping Schedule C depreciation |
| (39), (45) | Full Collection Financial Standards amount | Entering actual spending or an estimate |
| (40)–(43) | Actual amounts; IRS generally allows the lesser of actual or local standard | Not flagging amounts above the standard |
| Box F | Box D − Box E, not below 0 | Carrying a negative number into Box G or H |
| Box G / H | Box F × 12 / × 24 (fewer months if the CSED is closer for all periods) | Using × 24 with a lump-sum payment schedule |

For Form 433-B (OIC): Box A (lines 1 to 5) + Box D × 12 (Box E) or × 24 (Box F); equity in income-producing assets other than real estate may be excluded (Form 433-B (OIC), Section 5 footnote).

### Questions to ask, in this order

1. "Do you agree you owe the tax, and the issue is paying it?" (DATL vs DATC)
2. "Can you send me your IRS account transcript, or the notices for every year you owe?" (periods, balances, assessment dates)
3. "Have you filed every required return, and are this year's estimated payments current?" (eligibility)
4. "Who lives with you, how old are they, and who contributes to the household's bills?" (household size, standards, shared expenses)
5. "Which county do you live in?" (housing and transportation standards)
6. Each asset category in Section 3, one at a time, with "none" recorded explicitly.
7. Each income source, then each expense line with the amount actually paid and proof.
8. "If the IRS accepted an offer, where would the money come from, and how fast?" (payment option, source of funds)

---

## Validation

Run every check. Report failures; do not silently fix.

### Math checks

- [ ] Line (1) = (1a) + (1b) + (1c) − $1,000, floored at 0
- [ ] Each × .8 line = market value × 0.8 − loan balance, floored at 0; leased vehicles and income-producing business assets entered as 0
- [ ] Line (6b) = (6a) − $3,450, floored at 0; line (6d) subtracts $3,450 only on a joint offer
- [ ] Line (7) = (7a) + (7b) + (7c) − $11,980, floored at 0
- [ ] Box A = lines (1) through (7); lettered lines are not added directly
- [ ] Box B = lines (8) + (11); line (11) = (9) − (10), floored at 0
- [ ] Line (17) = (12) through (16); line (29) = (18) through (28); Box C = (17) − (29), floored at 0
- [ ] Box D = lines (30) through (38); Box E = lines (39) through (51); Box F = D − E, floored at 0
- [ ] Box G = F × 12 or Box H = F × 24 (or months remaining on the CSED when IRM 5.8.5.25 applies)
- [ ] Offer = Box A + Box B + G or H; whole dollars; more than $0
- [ ] Lump sum: initial payment ≥ 20% of the offer; initial + listed payments = offer; no payment later than 5 months after acceptance; no more than 5 payments after acceptance
- [ ] Periodic: first + monthly × count + final = offer; total months ≤ 24; payment day between 1 and 28

### Eligibility and sanity checks

- [ ] Every required return filed; a bill received for at least one listed period; current-year estimates paid; employer deposits current for this quarter and the two prior
- [ ] No open bankruptcy, open audit, or innocent spouse claim; no DATL offer pending
- [ ] Full-pay screen run without the $1,000 and $3,450 allowances; result stated
- [ ] Lines (39) and (45) equal the current Collection Financial Standards for the household; source table and date cited; no estimated standard anywhere
- [ ] Every actual expense above a local standard is flagged for documentation
- [ ] Unsecured debt payments, private school or college tuition, charitable contributions, and voluntary retirement contributions not counted as expenses (Form 656-B, page 5; IRM 5.8.5.22.4, 5.8.5.23)
- [ ] Depreciation added back to self-employment income (Form 433-A (OIC), line (36))
- [ ] Offer below the calculated minimum only with a written special-circumstances explanation in Section 3 and supporting documents (Form 656-B, page 29 checklist)
- [ ] Line (10) treatment disclosed to the user if line (9) is above 0
- [ ] Low-Income Certification checked only if the table test is met; if checked, no money in the package
- [ ] Separate packages for individual and business debts; separate offers where spouses owe separate liabilities

---

## Output format

```markdown
# Offer in Compromise — DRAFT (Form 656 Rev. 4-2026, Form 433-A (OIC) Rev. 4-2026)

## Eligibility screen
| Check | Status | Evidence |
|---|---|---|
| All required returns filed | Yes/No | <source> |
| Bill received for at least one period | Yes/No | <notice> |
| Current-year estimated payments made | Yes/No/Not required | <source> |
| Employer deposits, current + 2 prior quarters | Yes/No/Not required | <source> |
| Open bankruptcy / audit / innocent spouse | None | <source> |

## Periods in the offer
| Form | Period end | Assessment date | Balance | CSED |
|---|---|---|---|---|

## Form 433-A (OIC) — every line (enter 0 where none)
### Section 3 — personal assets
(1a) Bank account 1:                     $
(1b) Bank account 2:                     $
(1c) Accounts from attachment:           $
(1)  (1a)+(1b)+(1c) − $1,000:            $
(2a)–(2d) Investments, digital assets:   $  (market value − loans)
(2)  Total:                              $
(3a)–(3b) Retirement × .8 − loans:       $
(3)  Total:                              $
(4)  Life insurance cash value − loans:  $
(5a)–(5c) Real property × .8 − loans:    $
(5)  Total:                              $
(6a) Vehicle 1 × .8 − loan:              $
(6b) (6a) − $3,450:                      $
(6c) Vehicle 2 × .8 − loan:              $
(6d) Joint offer: (6c) − $3,450; else (6c): $
(6e) Vehicles from attachment:           $
(6)  (6b)+(6d)+(6e):                     $
(7a) Valuables × .8 − loans:             $
(7b) Furniture/personal effects × .8:    $
(7c) From attachment:                    $
(7)  (7a)+(7b)+(7c) − $11,980:           $
Box A (1) through (7):                   $

### Sections 4–6 — self-employed (or "N/A — not self-employed")
(8)  Business cash (8a)–(8d):            $
(9a)–(9c) Other business assets:         $  (0 if leased or income-producing; list values anyway)
(9)  Total:                              $
(10) Tools-of-trade deduction:           $  [derived; disclosed to user: yes/no]
(11) (9) − (10):                         $
Box B (8)+(11):                          $
(12)–(16) Business income, (17) total:   $
(18)–(28) Business expenses, (29) total: $
Box C (17) − (29):                       $

### Section 7 — household income and expenses
(30) Primary taxpayer income:            $
(31) Spouse income:                      $
(32)–(35) Other sources, interest, distributions, rental: $
(36) Net business income (Box C):        $
(37)–(38) Child support, alimony:        $
Box D:                                   $
(39) Food/clothing/misc. — STANDARD:     $  [table, household size, effective date]
(40) Housing/utilities — actual:         $  [local standard: $ ; over? flag]
(41) Vehicle ownership — actual:         $  [standard: $ ]
(42) Vehicle operating — actual:         $  [standard: $ ]
(43) Public transportation — actual:     $
(44) Health insurance premiums:          $
(45) Out-of-pocket health — STANDARD:    $  [table, persons by age group]
(46) Court-ordered payments:             $
(47) Child/dependent care:               $
(48) Life insurance premiums:            $
(49) Current monthly taxes:              $
(50) Secured debts/other:                $
(51) Delinquent state/local tax payment: $
Box E (39) through (51):                 $
Box F Box D − Box E (not below 0):       $

### Section 8 — minimum offer
Box G = Box F × 12 (or months left on CSED): $
Box H = Box F × 24 (or months left on CSED): $
Offer = Box A + Box B + Box G or Box H:  $

## Full-pay screen
Equity without allowances: $ | Months to latest CSED: | Box F × months: $ | Total vs balance: $ vs $ → <cannot full pay | can full pay → route to form-9465>

## Form 656
Section 1/2: <names, TINs, addresses, periods>
Low-Income Certification: <box checked or "does not qualify">
Section 3: <one box>
Section 4: <lump sum: offer, 20% initial, schedule | periodic: first, monthly, day, months, final>
Section 5: <designation; EFTPS/IOLA EFT numbers and dates or "paying by check">
Section 6: <source of funds; filing and payment checkboxes>

## Payments due with the package
Application fee: $205 or $0 (Low-Income Certification) | Initial payment: $

## Validation summary
- Math: <pass | failures>
- Flags: <list>
- Open questions for the user: <list>

## Sources cited in this draft
- Form 656-B booklet (Rev. 4-2026); Form 656, 433-A (OIC), 433-B (OIC) (Rev. 4-2026)
- IRS Collection Financial Standards (effective June 29, 2026)
- IRM 5.8.5 (effective 04-23-2026); IRC §7122, §6331(k), §6502
```

Show every line, including zeros. The draft is for the user (or their CPA, EA, or attorney) to review and sign; the agent does not sign.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Form 656 (Rev. 4-2026) section by section, including the Low-Income Certification table and the Section 7 terms
- [`references/collection-information-statements.md`](./references/collection-information-statements.md) — Form 433-A (OIC) and Form 433-B (OIC) (Rev. 4-2026) line maps with every multiplier and allowance
- [`references/rcp-calculation.md`](./references/rcp-calculation.md) — reasonable collection potential, quick sale value, allowable expenses and the Collection Financial Standards, CSED limits, the full-pay screen
- [`references/eligibility-and-alternatives.md`](./references/eligibility-and-alternatives.md) — pre-checks, the three Form 656 grounds, doubt as to liability on Form 656-L, when to route to an installment agreement, separate-offer rules
- [`references/common-mistakes.md`](./references/common-mistakes.md) — errors that get offers returned or rejected
- [`filing.md`](./filing.md) — online and mail channels, payment mechanics, what happens after submission, consent and security rules

## Examples

- [`examples/self-employed-lump-sum.md`](./examples/self-employed-lump-sum.md) — sole proprietor HVAC technician, Sections 4 to 6 completed, lump-sum offer, income-producing assets and line (10) flagged
- [`examples/low-income-retiree-periodic.md`](./examples/low-income-retiree-periodic.md) — retiree on Social Security, Box F negative, Low-Income Certification, periodic offer with no money sent
- [`examples/w2-can-full-pay.md`](./examples/w2-can-full-pay.md) — wage earner whose equity and income cover the debt; the agent stops and routes to an installment agreement

## Sources

Re-verify each year; the allowances, the low-income table, and the standards change.

- [IRS Offer in Compromise 2026: Form 656 Step by Step, the $205 Fee, and How the IRS Calculates Your Minimum Offer](https://jupid.com/blog/offer-in-compromise-form-656-2026) — companion guide for human readers
- [Form 656-B, Offer in Compromise Booklet (Rev. 4-2026)](https://www.irs.gov/pub/irs-pdf/f656b.pdf) — instructions, Form 656, Form 433-A (OIC), Form 433-B (OIC), mailing addresses (page 29)
- [Form 656-L, Offer in Compromise (Doubt as to Liability) (Rev. 7-2026)](https://www.irs.gov/pub/irs-pdf/f656l.pdf)
- [About Form 656](https://www.irs.gov/forms-pubs/about-form-656) — current revisions
- [IRS: Offer in compromise](https://www.irs.gov/payments/offer-in-compromise) — eligibility summary, Form 13711 appeal within 30 days
- [IRS Collection Financial Standards](https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards) — national and local standards, effective June 29, 2026
- [IRM 5.8.5, Financial Analysis (effective 04-23-2026)](https://www.irs.gov/irm/part5/irm_05-008-005r) — net realizable equity, quick sale value, allowable expenses, future income
- [Offer in Compromise Pre-Qualifier](https://irs.treasury.gov/oic_pre_qualifier/) — IRS eligibility and preliminary offer tool
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf), §3.49 — 2026 levy exemptions under §6334(a)(2) ($11,980) and §6334(a)(3) ($5,990)
- IRC §7122 (compromises: 20% lump-sum payment, periodic payments, low-income exception, 24-month deemed acceptance), §6331(k)(1) (no levy while an offer is pending), §6502 (10-year collection period), §6334 (property exempt from levy)

## Disclaimer

This skill encodes procedural guidance from IRS forms, the Internal Revenue Manual, and the Internal Revenue Code. It is not tax or legal advice and does not create a client relationship. Whether to offer less than the calculated minimum, whether an effective tax administration claim is supportable, and how to fund an offer are judgment calls for a CPA, enrolled agent, attorney, or Low Income Taxpayer Clinic. Remind the user that the draft must be reviewed before it is signed under penalties of perjury.
