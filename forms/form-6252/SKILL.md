---
name: form-6252
description: >
  Use this skill when a taxpayer sold property at a gain and receives at least one
  payment after the year of sale (seller financing, a buyer's note, a land contract,
  a deferred payment in a business or practice sale) and needs IRS Form 6252,
  Installment Sale Income, for the year of sale or any later year of the note.
  Triggers on phrases like "Form 6252", "installment sale", "installment method",
  "seller financing", "seller note", "carrying the note", "sold my rental and the
  buyer pays me monthly", "gross profit percentage", "contract price", "sold land to
  my son on payments", "related party installment sale", "elect out of the
  installment method", "453A interest". Do NOT use for a sale paid in full in the
  year of sale (use form-4797 or form-8949), a sale at a loss (form-4797 or
  form-8949), publicly traded stock or securities (form-8949), inventory or dealer
  property (schedule-c), an IRS payment plan for tax owed (an "installment
  agreement" is form-9465), rental operating income (schedule-e), or a like-kind
  exchange with no note (form-8824).
form: Form 6252 (Installment Sale Income)
audience: [individual, solo, llc1, llcm, scorp, ccorp, partnership]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f6252.pdf
---

# Form 6252 — Installment Sale Income

This skill produces an audit-grade draft of Form 6252 for one installment sale: the year-of-sale computation of gross profit, contract price and gross profit percentage, the yearly installment sale income, the related-party resale computation, and the handoffs to Form 4797, Schedule D and Schedule 2. The arithmetic is short. The judgment concentrates in four places: pulling depreciation recapture out in the year of sale (Form 4797, Part III first), deciding what counts as a payment (assumed debt above basis, amounts withheld at closing, deemed payments), applying the related-party rules, and keeping interest off the form entirely.

The worked flow targets Form 1040 filers. Partnerships, S corporations, C corporations, estates and trusts use the same lines and attach Form 6252 to their own return.

Line map verified against the **2025 Form 6252 (Created 5/28/25), whose instructions are printed on the form itself (pages 2–4), filed in 2026.** There is no separate instructions PDF, so this skill's frontmatter has no `official_instructions` link. A sale that closes in 2026 is reported on the 2026 Form 6252; check the next revision at https://www.irs.gov/forms-pubs/about-form-6252 before using this line map for it.

**Companion guide for end users:** [Form 6252 Instructions 2026: Installment Sale Income Line by Line, Gross Profit Percentage, and Selling a Business on a Seller Note](https://jupid.com/blog/form-6252-installment-sale-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 6252, the installment method, a gross profit percentage, or a contract price.
- The user sold real or personal property at a gain and at least one payment arrives after the close of the tax year of the sale (Pub. 537, "What's an Installment Sale?"; IRC §453(b)(1)).
- The user is receiving principal on a note from a sale made in an earlier year. Form 6252 is filed every year until the final payment, even in a year with no payment (Form 6252 instructions, "Purpose of Form").
- The user sold to a relative or a controlled entity on payments, or the related buyer has resold the property.
- The user asks whether to report the whole gain now ("elect out").

Do **not** engage this skill when:

- The sale produced a loss. The installment method cannot report a loss (Form 6252 instructions, line 24; Rev. Rul. 70-430). Use [`../form-4797/SKILL.md`](../form-4797/SKILL.md) for business property or [`../form-8949/SKILL.md`](../form-8949/SKILL.md) for capital assets.
- All payments arrive in the year of sale. No Form 6252. Use form-4797 or form-8949.
- The property is stock or securities traded on an established securities market. All payments are treated as received in the year of sale (Form 6252 instructions; Pub. 537). Use form-8949.
- The property is inventory or dealer property held for sale to customers (Pub. 537, "What's an Installment Sale?"). Use [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md).
- The user means an IRS payment plan for a tax balance. That is an installment *agreement*, Form 9465: [`../form-9465/SKILL.md`](../form-9465/SKILL.md).
- The question is about rent the property produced before the sale: [`../schedule-e/SKILL.md`](../schedule-e/SKILL.md).
- A like-kind exchange with no installment note: [`../form-8824/SKILL.md`](../form-8824/SKILL.md). If the exchange includes an installment note, this skill applies together with form-8824.

Boundaries with siblings:

- **Form 4797** computes depreciation recapture (Part III) before Form 6252 can be finished, and receives the §1231 portion of line 26 on Form 4797 line 4. See [`../form-4797/SKILL.md`](../form-4797/SKILL.md).
- **Schedule D / Form 8949** receive capital-asset gain from line 26 (Schedule D line 4 short-term, line 11 long-term). See [`../schedule-d/SKILL.md`](../schedule-d/SKILL.md).
- **Schedule 2** line 15 carries the §453A interest on deferred tax. See [`../schedule-2/SKILL.md`](../schedule-2/SKILL.md).
- **Interest** the buyer pays goes to Schedule B and Form 1040 as interest income. Never on Form 6252.
- Entity sellers: [`../form-1065/SKILL.md`](../form-1065/SKILL.md), [`../form-1120-s/SKILL.md`](../form-1120-s/SKILL.md), [`../form-1120/SKILL.md`](../form-1120/SKILL.md).

---

## Prerequisites

Collect every item before computing anything. If an item is missing, ask the tight question shown and **stop until the user answers.** Do not pick defaults.

1. **Tax year being prepared and the year of sale.** "Which tax year is this return for, and in which year did the sale close?" Year of sale and later years use different lines (20, 21, 23).
2. **Property description and type code** (line 1). "Was this a timeshare or residential lot, personal-use property, farm property, or something else?"
3. **Dates** (lines 2a, 2b). "On what date did you acquire the property and on what date did the sale close?" The holding period sets short-term versus long-term on line 26.
4. **Related party** (line 3). "Is the buyer your spouse, child, grandchild, parent, sibling, or an entity or trust you or your family control?" If yes, also ask "Has the buyer sold, given away, or otherwise disposed of the property?" and "Is the property depreciable in the buyer's hands?"
5. **Fixed price** (line 4). "Was the total price fixed at closing, or does any part depend on future profits, earnouts, or other contingencies?"
6. **Selling price and its pieces** (line 5): cash at closing, face of the buyer's note, FMV of any property received, and any of the seller's debt the buyer assumed or took the property subject to. Ask for the closing statement and the note.
7. **Assumed debt versus new financing** (line 6). "Did the buyer take over your existing mortgage, or did the buyer get a new loan and pay yours off at closing?" Only debt the buyer assumed or took subject to goes on line 6 (Form 6252 instructions, line 6).
8. **Basis** (line 8): original cost, improvements, and casualty losses and credits listed in the line 8 instructions.
9. **Depreciation allowed or allowable** (line 9), including any §179 deduction, and the method used. "Did you deduct depreciation every year the property was in service? Which method?" Allowable depreciation counts even if not claimed.
10. **Selling expenses** (line 11): commissions, advertising, legal fees.
11. **Form 4797, Part III recapture** (line 12) for the year of sale, or the facts to compute it with [`../form-4797/SKILL.md`](../form-4797/SKILL.md).
12. **Main home exclusion** (line 15). "Was this your main home? If so, how much gain are you excluding under section 121?" Use Pub. 523.
13. **Payments.** Principal received this year (line 21), separated from interest; amounts withheld at closing to pay the seller's debts or fees; for later years, all principal and deemed payments received in prior years (line 23) and the year-of-sale gross profit percentage (line 19). Ask for the prior-year Forms 6252.
14. **Interest terms.** Stated interest rate, compounding, payment schedule, and the month the binding written contract was signed. Needed for the AFR test in [`references/interest-and-afr.md`](./references/interest-and-afr.md).
15. **Election out.** "Do you want to report the entire gain this year instead of as you are paid?" The election is made by the due date of the return, including extensions (Pub. 537).
16. **Note events.** "Did you pledge the note as security for a loan, sell it, give it away, cancel or forgive any of it, or repossess the property?"
17. **Aggregate notes** (for §453A). "At the end of the year, what was the total face amount of all installment notes from sales during that year with a price over $150,000?"

---

## Workflow

Execute in order.

### Step 1 — Confirm the installment method applies

Check: gain (not loss), at least one payment after the year of sale, not publicly traded securities, not inventory or dealer property, not an escrow that pays the full balance (Pub. 537, "Escrow Account"). If any test fails, redirect per **When to invoke**.

### Step 2 — Settle the election out

If the user elects out, do not prepare Form 6252. Report the full gain in the year of sale on Form 4797, Form 8949, or Schedule D (Form 6252 instructions). A timely filer who did not elect can still elect on an amended return filed within 6 months of the due date, excluding extensions, marked "Filed pursuant to section 301.9100-2" ([`../form-1040-x/SKILL.md`](../form-1040-x/SKILL.md)). Revocation needs IRS approval (Pub. 537). Do not advise whether to elect; present the year-by-year income both ways and refer the decision to a CPA.

### Step 3 — Split a multi-asset sale

For a sale of several assets or a whole business, allocate the price and the year-of-sale payments by asset (Pub. 537, "Single Sale of Several Assets" and "Sale of a Business"). Inventory, assets sold at a loss, and gain that is all recapture come out. For a business sale, the buyer and seller each attach **Form 8594** to the return for the year of sale (Pub. 537, "Reporting requirement"). Use one Form 6252 per sale; when several assets must be reported separately, Pub. 537 allows one Form 6252 with an attached schedule per asset.

### Step 4 — Compute recapture first (year of sale only)

Complete Form 4797, Part III for each depreciable asset. The §1245 and §1250 recapture (including §179 and §291) on Form 4797 line 31 is taxed in full in the year of sale; enter it on Form 6252 line 12 and on Form 4797 line 13. Recapture under §1252, §1254, §1255 goes through line 25 instead. Details: [`references/recapture-and-character.md`](./references/recapture-and-character.md).

### Step 5 — Part I (lines 5–18)

Compute selling price, assumed debt, adjusted basis, installment sale basis (line 13), gross profit (line 16), and contract price (line 18). If line 14 is zero or less, stop: do not file Form 6252; report the whole sale on Form 4797, Form 8949, or Schedule D (line 14 instructions). In later years, copy Part I from the year-of-sale form; it does not change unless the selling price was reduced (Pub. 537, Worksheet B).

### Step 6 — Part II (lines 19–26)

Gross profit percentage to at least 4 decimals. Year-of-sale deemed payment on line 20. Principal received on line 21. Installment sale income on line 24. §1252/§1254/§1255 recapture on line 25. Route line 26 by character.

### Step 7 — Part III (lines 27–37) when the buyer is related

Complete Part III for the year of sale and the 2 years after, unless the final payment came this year. Apply the line 29 exceptions, then lines 30–37. Check §453(g) for depreciable property first. See [`references/related-party-and-special-rules.md`](./references/related-party-and-special-rules.md).

### Step 8 — Special rules check

Pledge rule, §453A interest (Schedule 2 line 15), disposition of the note (§453B), repossession, contingent price, reduced price, like-kind exchange. Each is in [`references/related-party-and-special-rules.md`](./references/related-party-and-special-rules.md).

### Step 9 — Interest

Confirm the note carries adequate stated interest against the applicable federal rate for the right months and term, or flag unstated interest. Report interest on Schedule B. See [`references/interest-and-afr.md`](./references/interest-and-afr.md).

### Step 10 — Validate

Run every check in **Validation**. Surface failures; do not silently fix.

### Step 11 — Produce the deliverable

Use **Output format**, including a multi-year schedule of payments and gain.

### Step 12 — Hand off

- Line 26, trade or business property held more than 1 year → Form 4797 line 4; held 1 year or less or ordinary gain from a noncapital asset → Form 4797 line 10, "From Form 6252" ([`../form-4797/SKILL.md`](../form-4797/SKILL.md)).
- Line 26, capital asset → Schedule D line 4 (short-term) or line 11 (long-term) ([`../schedule-d/SKILL.md`](../schedule-d/SKILL.md)).
- Section 1250 property → Unrecaptured Section 1250 Gain Worksheet, line 4, in the Schedule D instructions.
- Line 25 / line 36 → Form 4797 line 15.
- §453A interest → Schedule 2 line 15 with a computation statement ([`../schedule-2/SKILL.md`](../schedule-2/SKILL.md)).
- Interest received → Schedule B and Form 1040.
- Set a reminder: Form 6252 every year until the final payment; Part III for the 2 years after a related-party sale.

### Step 13 — File

If the user wants the agent to file, follow [`filing.md`](./filing.md). Form 6252 is an attachment to the return, not a standalone filing.

---

## Line-by-line guidance

Full map: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Top of form (lines 1–4)

- **Line 1** — Code and description: 1 timeshare or residential lot; 2 sale by an individual of personal-use property (§1275(b)(3)); 3 property used or produced in farming (§2032A(e)(4) or (5)); 4 all other.
- **Lines 2a / 2b** — Date acquired and date sold, mm/dd/yyyy.
- **Line 3** — Related party. "Yes" means Part III for the year of sale and 2 years after, unless the final payment came this year.
- **Line 4** — "No" if the total selling price cannot be determined by the close of the year of sale (contingent payment sale, Temp. Reg. §15a.453-1(c)). Once "No," always "No."

### Part I — Gross profit and contract price (lines 5–18)

Completed every year with year-of-sale amounts.

```
Line 7  = Line 5 − Line 6
Line 10 = Line 8 − Line 9
Line 13 = Line 10 + Line 11 + Line 12          (installment sale basis)
Line 14 = Line 5 − Line 13                     (≤ 0 → stop, no Form 6252)
Line 16 = Line 14 − Line 15                    (gross profit)
Line 17 = Line 6 − Line 13, not below 0        (assumed debt above basis)
Line 18 = Line 7 + Line 17                     (contract price)
```

- **Line 5** excludes stated interest, unstated interest, amounts recharacterized as interest, and OID. A contingent sale with a stated maximum price uses the maximum.
- **Line 6** is only the seller's debt the buyer assumed or took the property subject to. A new bank loan the buyer takes out is not here.
- **Line 12** is Form 4797 line 31 for this property. Zero for straight-line §1250 property owned by an individual (Form 4797 line 26 says enter -0- on line 26g when straight line was used, except a corporation subject to §291).

### Part II — Installment sale income (lines 19–26)

```
Line 19 = Line 16 ÷ Line 18, decimal rounded to at least 4 digits
          (later years: the year-of-sale percentage)
Line 20 = Line 17 in the year of sale; 0 in later years
Line 22 = Line 20 + Line 21
Line 24 = Line 22 × Line 19, not below 0
Line 26 = Line 24 − Line 25
```

- **Line 21** — money and FMV of property received this year, principal only; includes amounts withheld at closing to pay off the seller's mortgage or broker and legal fees. The buyer's note is not a payment unless payable on demand or readily tradable. Amounts already treated as received under Part III (line 34 in a prior year) go on line 23, not line 21.
- **Line 23** — all prior-year payments, including deemed payments (related-party second disposition, pledge rule, liabilities above basis from the year-of-sale line 20).
- **Line 25** — §1252, §1254, §1255 recapture only, never more than line 24; the excess carries to later years. Not §179 recapture (that was on line 12).

### Part III — Related party (lines 27–37)

```
Line 32 = smaller of Line 30 or Line 31
Line 34 = Line 32 − Line 33, not below 0
Line 35 = Line 34 × year-of-sale gross profit percentage
Line 37 = Line 35 − Line 36
```

Line 33 = lines 22 + 23 (all payments by year end, no interest). Skip lines 30–37 if a box on line 29 applies; box 29e needs an attached explanation.

---

## Validation

### Math checks

- [ ] Line 7 = Line 5 − Line 6; Line 10 = Line 8 − Line 9; Line 13 = Lines 10 + 11 + 12
- [ ] Line 14 = Line 5 − Line 13 and is > 0 (otherwise no Form 6252)
- [ ] Line 16 = Line 14 − Line 15; Line 17 = max(0, Line 6 − Line 13); Line 18 = Line 7 + Line 17
- [ ] Line 19 = Line 16 ÷ Line 18 to at least 4 decimals; in later years it equals the year-of-sale figure (unless Worksheet B applies)
- [ ] Line 20 = Line 17 in the year of sale, 0 otherwise; Line 22 = Line 20 + Line 21; Line 24 = Line 22 × Line 19
- [ ] Line 25 ≤ Line 24; Line 26 = Line 24 − Line 25
- [ ] Line 33 = Lines 22 + 23; Line 32 = min(Line 30, Line 31); Line 35 = Line 34 × year-of-sale Line 19; Line 36 ≤ Line 35
- [ ] Multi-year schedule: total payments (including line 20 and deemed payments) = Line 18; total gain over the note = Line 16

### Sanity checks (warn, do not block)

- [ ] Line 9 is 0 on property that was rented or used in business → depreciation "allowed or allowable" still reduces basis; ask.
- [ ] Depreciable property with line 12 = 0 → confirm Form 4797, Part III was run (straight-line §1250 property legitimately gives 0).
- [ ] Line 21 equals the full payment amount on an interest-bearing note → interest is probably mixed in.
- [ ] Line 6 includes a loan the buyer obtained from a bank → remove it.
- [ ] Stated rate below the test AFR, or no stated interest → unstated interest or OID reduces line 5.
- [ ] Related buyer and depreciable property → §453(g) may bar the installment method.
- [ ] Price over $150,000 and the user borrowed against the note → pledge rule payment.
- [ ] Aggregate year-end notes from the year's sales over $5 million → §453A interest.
- [ ] Line 4 = "No" in an earlier year but "Yes" now → must stay "No."

### Cross-form checks

- [ ] Line 12 = Form 4797 line 31 for this property, and the same amount sits on Form 4797 line 13; Form 4797 line 32 shows no gain for this property ("N/A" if Form 4797 was used only for recapture).
- [ ] Line 26 appears once: Form 4797 line 4 or line 10, or Schedule D line 4 or line 11.
- [ ] Unrecaptured §1250 gain on this year's line 26 is tracked on the Schedule D worksheet line 4.
- [ ] Interest received appears on Schedule B, with the buyer's name, address, and SSN on line 1 when the buyer used the property as a personal residence (Pub. 537, "Seller-financed mortgage").

---

## Output format

```markdown
# Form 6252 — DRAFT for tax year YYYY (sale of <property>; year N of the note)

## Top of form
1.  Code / description:            <1|2|3|4> — <description>
2a. Date acquired:                 MM/DD/YYYY
2b. Date sold:                     MM/DD/YYYY
3.  Sold to related party:         Yes | No
4.  Price determinable by year end: Yes | No

## Part I — Gross Profit and Contract Price (year-of-sale amounts)
5.  Selling price:                 $X
6.  Debt assumed by buyer:         $X
7.  Line 5 − line 6:               $X
8.  Cost or other basis:           $X
9.  Depreciation allowed/allowable: $X
10. Adjusted basis:                $X
11. Selling expenses:              $X
12. Recapture (Form 4797 line 31): $X
13. Lines 10 + 11 + 12:            $X
14. Line 5 − line 13:              $X
15. Excluded gain (main home):     $X
16. Gross profit:                  $X
17. Line 6 − line 13 (≥ 0):        $X
18. Contract price:                $X

## Part II — Installment Sale Income
19. Gross profit percentage:       0.XXXX
20. Year-of-sale line 17 (else 0): $X
21. Payments this year (principal): $X
22. Line 20 + line 21:             $X
23. Payments in prior years:       $X
24. Installment sale income:       $X
25. Ordinary income recapture:     $X
26. Line 24 − line 25:             $X  → <Form 4797 line 4 | line 10 | Schedule D line 4 | line 11>

## Part III — Related Party (or "N/A — buyer not related" / "N/A — final payment received")
27. Related party:                 <name, address, TIN>
28. Second disposition this year:  Yes | No
29. Exception box:                 a | b | c | d | e | none
30. Related party's amount realized: $X
31. Contract price (year of sale): $X
32. Smaller of 30 or 31:           $X
33. Payments by year end:          $X
34. Line 32 − line 33 (≥ 0):       $X
35. Line 34 × year-of-sale GPP:    $X
36. Ordinary income recapture:     $X
37. Line 35 − line 36:             $X  → <same routing as line 26>

## Multi-year schedule
| Year | Principal + deemed payments | Gain (× 0.XXXX) | Of which unrecaptured §1250 | Cumulative payments |
|------|-----------------------------|-----------------|-----------------------------|---------------------|

## Interest (not on Form 6252)
- Stated rate / test AFR (month, term, Rev. Rul.): X% vs Y%
- Interest received this year → Schedule B: $X

## Required attachments and handoffs
- [ ] Form 4797 (Part III in year of sale; line 4, 10, 13, or 15)
- [ ] Schedule D / Form 8949 (capital assets)
- [ ] Schedule 2 line 15 with §453A computation statement (if applicable)
- [ ] Form 8594 (sale of a business's assets, year of sale)
- [ ] Explanation for line 29e (if checked)

## Validation summary
- Math: all checks passed | <failures>
- Sanity: <warnings>
- Open questions for the user or CPA: <list>

## Sources cited in this draft
- Form 6252 (2025), including its instructions
- Pub. 537 (2025), Installment Sales
- <Form 4797 instructions, Schedule D instructions, Rev. Rul. for AFR month, IRC sections used>
```

Show every line, including zeros and N/A. The draft is not the filed form; the user or preparer transcribes it.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of the 2025 Form 6252 with the instruction text that governs it
- [`references/recapture-and-character.md`](./references/recapture-and-character.md) — Form 4797 Part III first, line 12 and line 25, unrecaptured §1250 gain on installment payments, line 26 routing, main home exclusion
- [`references/related-party-and-special-rules.md`](./references/related-party-and-special-rules.md) — Part III two-year rule, §453(g), electing out, pledge rule, §453A interest, dispositions of the note, escrow, contingent and reduced prices, like-kind exchanges, repossession pointer
- [`references/interest-and-afr.md`](./references/interest-and-afr.md) — stated and unstated interest, §483 and §1274, the AFR test rate, inflation-adjusted limits
- [`references/common-mistakes.md`](./references/common-mistakes.md) — errors that misstate installment sale income
- [`filing.md`](./filing.md) — channels, mailing addresses, consent and security rules

## Examples

- [`examples/rental-condo-year-of-sale.md`](./examples/rental-condo-year-of-sale.md) — depreciated rental condo, buyer assumes the mortgage, seller note, unrecaptured §1250 gain reported first
- [`examples/land-note-year-three.md`](./examples/land-note-year-three.md) — third year of a land sale: Part I carried forward, line 20 = 0, line 23 cumulative, a principal prepayment
- [`examples/related-party-resale.md`](./examples/related-party-resale.md) — lot sold to a son who resells within 2 years; Part III accelerates the rest of the gain

## Sources

Re-verify each year; the IRS revises the form and Pub. 537 annually.

- [Form 6252 Instructions 2026: Installment Sale Income Line by Line, Gross Profit Percentage, and Selling a Business on a Seller Note](https://jupid.com/blog/form-6252-installment-sale-2026) — companion guide for human readers
- [Form 6252 (2025), with instructions on pages 2–4](https://www.irs.gov/pub/irs-pdf/f6252.pdf); [About Form 6252](https://www.irs.gov/forms-pubs/about-form-6252)
- [Publication 537 (2025), Installment Sales](https://www.irs.gov/pub/irs-pdf/p537.pdf)
- [Form 4797 (2025)](https://www.irs.gov/pub/irs-pdf/f4797.pdf) and [Instructions](https://www.irs.gov/pub/irs-pdf/i4797.pdf) — Part III, lines 4, 10, 13, 15, 31, 32
- [Instructions for Schedule D (Form 1040) (2025)](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — Unrecaptured Section 1250 Gain Worksheet, line 4
- [Schedule 2 (Form 1040) (2025)](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf), line 15; [Instructions for Form 1040 (2025)](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf), Schedule 2 line 15
- [Publication 523](https://www.irs.gov/pub/irs-pdf/p523.pdf) — main home exclusion
- [Applicable Federal Rates](https://www.irs.gov/applicable-federal-rates) — monthly Rev. Ruls.
- [Quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) — underpayment rate for §453A
- IRC [§453](https://www.law.cornell.edu/uscode/text/26/453), [§453A](https://www.law.cornell.edu/uscode/text/26/453A), §453B, §483, §1274, §1239, §1(h)(1)(E), §6621(a)(2); Temp. Reg. §15a.453-1(c); Reg. §301.9100-2; Rev. Rul. 70-430

## Disclaimer

This skill encodes procedural guidance from public IRS forms and publications. It is not tax advice and does not create a CPA-client relationship. Remind the user that the draft is a starting point; business sales, related-party sales, contingent prices, notes over $5 million, and election-out decisions warrant a licensed tax professional's review.
