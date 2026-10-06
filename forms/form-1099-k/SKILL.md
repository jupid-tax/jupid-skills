---
name: form-1099-k
description: >
  Use this skill when a US person receives a Form 1099-K from a payment
  processor (PayPal, Venmo, Stripe, Square, Etsy, eBay, Uber, Lyft, DoorDash,
  Airbnb, etc.) and needs to reconcile it against their records, classify it
  (business vs hobby vs personal), and report it correctly on Schedule C,
  Schedule 1, or Schedule E. Triggers on phrases like "received 1099-K",
  "PayPal tax form", "Venmo tax", "Etsy 1099-K", "Uber 1099-K", "marketplace
  seller taxes", "1099-K threshold", "third-party network reporting",
  "1099-K from Stripe", "report 1099-K on Schedule C", "1099-K personal
  payments", "1099-K hobby income". Do NOT use for: 1099-NEC (use
  `form-1099-nec` skill — different form, $2,000 threshold, direct
  client payments not platform-mediated); 1099-MISC (use `form-1099-misc`);
  1099-INT or 1099-DIV (interest/dividends — different forms, different
  schedules); 1099-DA (digital-asset broker reporting — new in 2025);
  W-2 wage reporting (use payroll tax skills).
form: Form 1099-K
audience: [solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1099k.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099k.pdf
---

# Form 1099-K — Payment Card and Third Party Network Transactions

This skill walks the agent through reconciling a Form 1099-K and routing the gross-payment amount to the correct line on the recipient's federal return. The 1099-K is an **information return** issued under IRC §6050W by payment settlement entities (PSEs) — credit-card processors and third-party networks — to anyone who received gross payments through their platform.

The 1099-K itself is **not filed by the recipient** — the PSE files it with the IRS and sends a copy to the user. The recipient's job is **reconciliation**: figure out which portion of the reported gross is business income, which is personal payment received in error, which is a hobby, which is a personal-item resale, and route each portion to the right form.

Box map verified against **Form 1099-K (Rev. December 2026)** and the Instructions for Form 1099-K (Rev. December 2026), used for 2026 transactions, and the **Rev. March 2024** form used for 2024 and 2025 transactions (no 2025 revision was issued). Return lines verified against the 2025 Schedule 1, Schedule C, and Form 1040 (filed in 2026); the 2026 drafts keep the same line numbers. Re-check the next revision at https://www.irs.gov/forms-pubs/about-form-1099-k before use.

The judgment is in **(a)** classifying the underlying transactions as business / hobby / personal / personal-item-sale, **(b)** mapping each classification to the correct schedule (Schedule C / Schedule 1 / Schedule E / not reported), and **(c)** producing an explicit reconciliation that handles personal-payment-mixed-with-business 1099-Ks (the most common real-world failure mode).

**Companion guide for end users:** [1099-K Guide 2026: Payment App Reporting Thresholds, Rules, and How to File](https://jupid.com/blog/1099-k-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1099-K, "1099-K", or "1099K"
- The user received a tax document from PayPal, Venmo, Stripe, Square, Cash App, Etsy, eBay, Amazon, Mercari, Poshmark, StubHub, Ticketmaster resale, Uber, Lyft, DoorDash, Instacart, GrubHub, Airbnb, VRBO, Turo, or any other payment processor / third-party network
- The user is reconciling business income reported via a third-party platform
- The user has personal Venmo / PayPal / Cash App payments showing up on a tax form and is unsure how to report them
- The user is a marketplace seller (Etsy, eBay, Amazon, Poshmark) trying to figure out how to report platform sales

Do **not** engage this skill when:

- The user received a **1099-NEC** from a direct client (use `form-1099-nec` — different form, $2,000 threshold, no transaction count)
- The user received a **1099-MISC** for rents, royalties, prizes, or gross proceeds paid to an attorney (different form)
- The user received a **1099-INT** or **1099-DIV** (interest / dividends — different schedules)
- The user received a **1099-DA** for digital asset broker proceeds (new form starting tax year 2025 for crypto brokers; use the forthcoming `form-1099-da` skill)
- The user is a **payor** preparing 1099-K forms to issue (this skill is for recipients; payor-side filing is a different workflow handled by the platform itself)
- The user received a **W-2** for wages (different system entirely)

If the user is unsure which 1099 they have, ask: "What does the form's title say at the top? Look for 'Payment Card and Third Party Network Transactions' (1099-K), 'Nonemployee Compensation' (1099-NEC), or 'Miscellaneous Information' (1099-MISC)."

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Payer (PSE) name** — who issued the 1099-K (e.g., "PayPal," "Stripe," "Etsy," "Uber Technologies, Inc.").
2. **Box 1a (gross payments)** — the total dollar amount on the form. This is gross before any fees, refunds, or chargebacks.
3. **Box 1b (card not present)** — payment card forms only; blank when the "Third party network" checkbox is marked. Informational.
4. **Box 3 (number of payment transactions)** — count of transactions, not including refunds. (Box 2 is the merchant category code; TPSOs leave it blank.)
5. **Checkboxes** — filer type (PSE vs EPF/other third party) and transactions reported (payment card vs third party network). The $20,000 / 200 test applies only to third party network forms.
6. **Box 4 (federal income tax withheld)** — usually $0; non-zero only if the user was subject to backup withholding.
7. **Boxes 5a-5l (monthly breakdown)** — gross by month; useful for spotting timing issues (e.g., December settlements that hit January).
8. **Boxes 6-8 (state info)** — state-level reporting if applicable. On Rev. December 2026 forms (2026 transactions), also **Box 1c (cash tips)** and **Box 1d (Treasury Tipped Occupation Code)**, used for the qualified tips deduction on Schedule 1-A; that deduction is outside this skill.
9. **The user's own records** — what was the underlying activity? Business sales? Selling personal items? Friends-and-family Venmo payments mistakenly classified as business? Rental income?
10. **Other 1099s for the same income** — did a client also issue a 1099-NEC for payments that flowed through the same platform? (Double-reporting check, see `references/reconciliation.md`.)
11. **Activity classification** — for each portion of the gross: business / hobby / personal payment received / personal-item resale. See [`references/personal-vs-business.md`](./references/personal-vs-business.md).

For marketplace sellers and gig workers specifically, also ask:

- Is this a **trade or business** (regular, continuous, profit-motive activity) or a **hobby** (sporadic, no profit motive)? Different reporting + different deduction treatment post-TCJA.
- For rentals: does the activity rise to "trade or business" (Schedule C) or is it passive rental income (Schedule E)? See [`examples/airbnb-host.md`](./examples/airbnb-host.md).
- For "personal item" resellers (selling old furniture, used clothing on Mercari/Poshmark): are most sales **at a loss** (not income; entry space at the top of Schedule 1, IRS FS-2025-08) or **at a gain** (capital gain, Schedule D / Form 8949)?

The single most-common 1099-K failure: a freelancer mixes business and personal Venmo payments on one account, gets a 1099-K covering both, and either (a) reports the entire gross as business income (overpaying SE tax) or (b) reports only the business portion (creating an IRS document-mismatch). The correct path requires explicit reconciliation. See `examples/venmo-personal-payments.md`.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm form and 2026 threshold context

Verify the user has an actual Form 1099-K (not a 1099-NEC, 1099-MISC, or platform-internal sales report). Ask the user to read the title at the top of the form: it must say "Payment Card and Third Party Network Transactions."

Reporting threshold context (IRC §6050W(e) as amended by P.L. 119-21 §70432, the One, Big, Beautiful Bill Act, July 4, 2025): a third party settlement organization (TPSO: payment app or online marketplace) is required to file a 1099-K for third party network transactions only if **both** of these are met:

- Gross payments exceed **$20,000**, AND
- Number of transactions exceeds **200**

**Payment card transactions have no minimum.** A merchant acquirer reports every card payment (FS-2025-08, General information Q2 and Third party filers Q7).

The American Rescue Plan Act of 2021 had lowered the TPSO threshold to over $600 with no transaction minimum. The IRS delayed it (Notices 2023-10, 2023-74) and then announced a phase-in under Notice 2024-85 ($5,000 for 2024, $2,500 for 2025, $600 after 2025). P.L. 119-21 §70432 restored $20,000 / 200 **retroactively** (effective as if included in ARPA §9674), so the phase-in amounts never applied. Sources: Instructions for Form 1099-K (Rev. December 2026), "Exception for de minimis payments"; IRS FS-2025-08 and IR-2025-107 (Oct. 23, 2025).

Important caveats:

- **Voluntary reporting**: PSEs may issue a 1099-K below the federal threshold (some always do). The recipient still has to reconcile and report.
- **State thresholds may be lower**: e.g., Massachusetts and Virginia ($600), Illinois (over $1,000 and 4 or more transactions), Vermont ($2,000). See [`references/phased-thresholds.md`](./references/phased-thresholds.md) for sources; check the user's state for anything not listed.
- **All income is taxable regardless of whether a 1099-K was issued.** The form only changes whether the payor was required to report — the underlying income is taxable either way.

### Step 2 — Classify each portion of the gross

Walk the user through breaking down Box 1a by activity type. Use [`references/personal-vs-business.md`](./references/personal-vs-business.md). For each transaction (or each batch of similar transactions), classify as:

| Classification | What it is | Where it goes |
|----------------|-----------|---------------|
| **Trade or business income** | Regular, profit-motive activity (freelance services, marketplace sales, gig work) | Schedule C, Line 1 |
| **Rental of real property** | Long-term residential rental, commercial rental, or short-term rental without substantial services | Schedule E |
| **Rental + substantial services** | Short-term rental with hotel-like services (cleaning, meals, concierge) | Schedule C |
| **Hobby income** | Sporadic, no profit motive (occasional crafts, casual reselling for fun) | Schedule 1, Line 8j (Activity not engaged in for profit) — full income, NO expense deduction post-TCJA |
| **Personal payment received** | Friends/family reimbursement, gift, splitting dinner | Not income. Enter the amount in the entry space at the top of Schedule 1 ("included in error") |
| **Personal item resale at a loss** | Sold used personal property below original cost (used clothing, furniture, electronics) | Not income; loss not deductible. Enter the sale amount in the entry space at the top of Schedule 1 |
| **Personal item resale at a gain** | Sold collectible / personal property above cost basis | Form 8949 + Schedule D (capital gain) |

If a single 1099-K covers multiple classifications (typical for mixed-use Venmo or PayPal accounts), the gross splits — the agent must produce a reconciliation showing the breakdown.

### Step 3 — Reconcile against payer records

Cross-check Box 1a against the user's own records from the platform:

- Pull the platform's gross payments report for the calendar year (most platforms expose this in their tax/year-end report)
- Compare to Box 1a — they should match exactly. Mismatches usually trace to: chargebacks the platform reversed in early next year, currency conversions, multiple linked accounts, or platform error.
- If the 1099-K is wrong, contact the PSE and request a **corrected 1099-K** (Form 1099-K with the "CORRECTED" box checked). Do not file with a known-wrong number.

Cross-check against any other 1099 forms the user received for the same income:

- If a client paid through PayPal AND issued a 1099-NEC for the same payments → double-reporting. The user reports the income **once** on Schedule C and keeps records to defend against an IRS document-matching notice.
- The general rule: when 1099-K and 1099-NEC overlap, the income is taxable once. Payments made by card or through a third party network are reported on 1099-K, not 1099-NEC (Instructions for Forms 1099-MISC and 1099-NEC). Report the income once on Schedule C. If Forms 1099-NEC box 1 total more than Schedule C line 1, attach a statement explaining the difference (2025 Schedule C instructions, line 1).

See [`references/reconciliation.md`](./references/reconciliation.md) for the full process.

### Step 4 — Map each classification to a return line

For each classified portion from Step 2, fill in the destination line:

| Classification | Form / Schedule | Line | Box on 1099-K traced from |
|---------------|----------------|------|-------------------------|
| Trade or business | Schedule C | Line 1 (Gross receipts) | Box 1a portion |
| Rental real estate (no services) | Schedule E | Line 3 (Rents received) | Box 1a portion |
| Hotel-like rental (substantial services) | Schedule C | Line 1 | Box 1a portion |
| Hobby income | Schedule 1 | Line 8j (Activity not for profit) | Box 1a portion |
| Personal payment received (gift, friends/family) | Schedule 1 | Entry space at the top of Schedule 1 (not added to income) | Box 1a portion |
| Personal item resale at loss | Schedule 1 | Entry space at the top of Schedule 1 (not added to income) | Box 1a portion |
| Personal item resale at gain | Form 8949 → Schedule D | Each sale itemized | Box 1a portion |
| Federal tax withheld (Box 4) | Form 1040 | Line 25b (Form(s) 1099) | Box 4 |

The entry space reads "For 2025, enter the amount reported to you on Form(s) 1099-K that was included in error or for personal items sold at a loss" (2025 Schedule 1; the 2026 draft has the same line). Combine amounts from several 1099-Ks into one entry. Schedule 1 lines 8z / 24z were the method only for 2022 and 2023 (FS-2025-08, Common situations Q6–Q7).

### Step 5 — Itemize Schedule C deductions if business

For the trade-or-business portion, the gross goes on Line 1 — but the user is also entitled to deduct the platform's fees and any other ordinary-and-necessary business expenses against it. Common 1099-K-related deductions:

- **Platform processing fees** — Stripe (2.9% + 30¢), PayPal (~2.9%), Etsy transaction fees (6.5% + listing) → Schedule C Line 10 (Commissions and fees)
- **Refunds and chargebacks** processed in the same tax year → Schedule C Line 2 (Returns and allowances)
- **Cost of goods sold** for marketplace sellers → Schedule C Part III → Line 4
- **Shipping supplies** the seller bought (boxes, mailers, tape) → Schedule C Line 22 (Supplies)
- **Postage** the seller bought (separate from buyer-paid shipping that's a pass-through) → Schedule C Part V, label "Postage", total to Line 27b (Other expenses; Line 27a is the Form 7205 deduction on the 2025 form)
- **Mileage** to the post office, fairs, supplier visits → Schedule C Line 9 (Car and truck) at the standard rate: 70¢ per mile for 2025; for 2026, 72.5¢ for Jan 1 – Jun 30 and 76¢ for Jul 1 – Dec 31 (https://www.irs.gov/tax-professionals/standard-mileage-rates). Ask for miles by half-year when the year is 2026.

NEVER subtract platform fees from Box 1a before reporting Line 1. Report gross on Line 1, deduct fees as separate expenses. Reporting net would create an IRS document-mismatch.

### Step 6 — Validate

Run every check in the **Validation** section. Surface any sanity warnings.

### Step 7 — Produce the deliverable

Use the template in **Output format**.

### Step 8 — Hand off to filing

The 1099-K itself isn't filed by the recipient. The reconciled outputs flow to Schedule C / Schedule 1 / Schedule E / Form 8949, which are part of the user's Form 1040 return. Hand off to [`filing.md`](./filing.md) which covers:

- Mapping the reconciliation to the actual line items on each schedule
- Common e-file software field locations (TurboTax, FreeTaxUSA, IRS Free File / FFFF) for 1099-K entry
- Backup-withholding claim on Form 1040 Line 25b if Box 4 has a non-zero amount
- Handling a CP2000 notice if the IRS document-matching system flags an apparent under-report

### Step 9 — Set the next-year prevention plan

For users who received a 1099-K mixing personal and business payments, advise:

- Open a separate business account on each platform (PayPal Business profile vs personal; Venmo Business profile)
- Tag personal Venmo/Cash App payments at the moment of receipt as "friends and family" (not "goods and services")
- Keep a running monthly reconciliation so January 2027's 1099-K is a confirmation rather than a surprise

---

## Line-by-line guidance

For the full reference, load [`references/boxes-explained.md`](./references/boxes-explained.md). High-level rules below.

### Filer / payer info (top of form)

- **PSE name + address + EIN** — identifies the platform that issued the form. Cross-reference if the user has accounts on multiple platforms with the same parent (e.g., Square / Cash App, both Block Inc.).
- **Filer checkbox** — "Payment settlement entity (PSE)" or "Electronic payment facilitator (EPF)/Other third party". When an EPF files, the PSE's name and phone appear above the account number. Doesn't change recipient reporting.
- **Transactions reported checkbox** — "Payment card" or "Third party network". A payee with both types gets a separate 1099-K for each. Only third party network forms are subject to the $20,000 / 200 test.
- **Filer's name, address, federal ID** — informational.
- **Account number** — platform's internal account ID for the user.

### Recipient info

- **Recipient's TIN** — must match the SSN or EIN the user provided on their W-9 to the platform. Mismatch triggers backup withholding (24%, IRC §3406).
- **Recipient name + address** — must match user's tax-return name. If wrong, request a corrected 1099-K.

### Box 1a — Gross amount of payment card / third party network transactions

The headline number. **Gross before fees, refunds, chargebacks, or any adjustments.** This is what the IRS sees and what document-matching looks for.

### Box 1b — Card not present transactions

Subset of Box 1a where the card was not present or the card number was keyed in (online, phone, catalog sales). Not reported on third party network forms. Informational only.

### Boxes 1c and 1d — Cash tips and TTOC (Rev. December 2026 forms only)

Box 1c is cash tips included in Box 1a; Box 1d is up to two Treasury Tipped Occupation Codes. Used for the qualified tips deduction in Part II of Schedule 1-A. Not on the Rev. March 2024 form used for 2025.

### Box 2 — Merchant category code

Four-digit MCC for payment card transactions. TPSOs leave it blank. Informational.

### Box 3 — Number of payment transactions

Count of transactions, not including refund transactions. Multiple sales to one buyer count as multiple transactions. Used to check the federal $20,000 / 200 test on third party network forms.

### Box 4 — Federal income tax withheld

Backup withholding (24%) only. $0 unless the user failed W-9 / TIN matching at some point. For TPSO payments, backup withholding applies only when the $20,000 / 200 test is met (IRC §3406(b)(8), calendar years after 2024). If non-zero, claim on **Form 1040 Line 25b** (Form(s) 1099) — this is a refundable credit against the user's total tax liability.

### Boxes 5a-5l — Monthly gross

Box 1a broken out by month. Useful for catching timing issues — e.g., a December 30 settlement that hits the user's bank January 2 still counts as 2026 gross because settlement date drives reporting, not deposit date.

### Boxes 6-8 — State info

State name + state ID + state tax withheld. State 1099-K reporting may differ from federal in trigger threshold (see `references/phased-thresholds.md`) but the recipient's reporting on the federal return doesn't change.

---

## Validation

Before declaring the reconciliation ready, run these checks. Surface anything that fails — don't silently fix.

### Identity checks

- [ ] Recipient name on the 1099-K matches the user's tax-return name
- [ ] Recipient TIN on the 1099-K matches the user's SSN or EIN as filed on Form 1040
- [ ] Mismatch on either → tell the user to request a corrected 1099-K from the PSE before filing

### Reconciliation checks

- [ ] Box 1a equals the sum of all classified portions in Step 2 (trade/business + hobby + personal + personal-item-resale)
- [ ] Box 3 (number of transactions) is plausible given the user's described activity (e.g., 3 transactions for a "marketplace seller" is suspicious)
- [ ] If the user's own platform records differ from Box 1a → flagged as needs-corrected-1099-K
- [ ] If another 1099 (1099-NEC, 1099-MISC) covers any of the same payments → double-reporting flag with reconciliation note

### Schedule C checks (if any portion is trade/business)

- [ ] Schedule C Line 1 (Gross receipts) ≥ the trade/business portion of Box 1a
- [ ] Line 1 may be > Box 1a portion if user has additional non-1099 business income (cash sales, sub-threshold clients) — that's correct
- [ ] Platform fees deducted on Line 10, not netted into Line 1
- [ ] No personal payments or personal-item sales inside Schedule C (not on Line 1, not as an "other expense" offset)
- [ ] Refunds / chargebacks on Line 2, not netted into Line 1
- [ ] If user is an Etsy/eBay seller, COGS computed in Part III and flowing to Line 4

### Schedule 1 checks (if any portion is personal or hobby)

- [ ] Personal payments and personal items sold at a loss: combined total entered in the entry space at the top of Schedule 1 (not on Lines 8z / 24z, which applied only to 2022–2023)
- [ ] Hobby income: reported on Line 8j; NO Schedule C; NO expense deduction (IRC §67(g), made permanent by P.L. 119-21 §70110)
- [ ] Classified portions plus the entry-space amount account for all of Box 1a

### Schedule E checks (if portion is rental)

- [ ] Schedule E used only for passive rental real estate (no substantial services)
- [ ] Short-term rental with substantial services → moved to Schedule C, not Schedule E

### Backup withholding check

- [ ] If Box 4 > 0, claim on Form 1040 Line 25b
- [ ] Tell the user why backup withholding was applied (failed W-9, TIN mismatch) and how to fix going forward

### Sanity checks (warn, don't block)

- [ ] User describes a "side hustle" but classifies the entire 1099-K as hobby → confirm; profit motive + regularity usually means business
- [ ] User receives 1099-K below the $20,000 / 200 threshold and assumes it's wrong → not necessarily; payment card forms have no threshold, a TPSO can issue voluntarily, and state thresholds may be lower
- [ ] User wants to subtract platform fees from Box 1a before reporting Line 1 → block; explain the document-mismatch risk
- [ ] User is selling used personal items at a loss but reporting full Box 1a as income → over-reporting; enter the loss-sale amounts in the entry space at the top of Schedule 1 (FS-2025-08, What to do Q6)
- [ ] Multiple 1099-Ks from the same parent company (Square + Cash App both from Block Inc.) → confirm whether activity overlaps

---

## Output format

The deliverable is a **reconciliation worksheet** the user can transcribe into their tax software or hand to a CPA. Format:

```markdown
# Form 1099-K Reconciliation — DRAFT

## Source 1099-K
PSE / Filer:                                   <Platform name + EIN>
Recipient TIN:                                 <SSN or EIN>
Tax year:                                      2026
Box 1a (gross payments):                       $<amount>
Transactions reported:                         <Payment card | Third party network>
Box 1b (card not present):                     $<amount or blank>
Box 3 (transactions):                          <count>
Box 4 (federal tax withheld):                  $<amount>

## Activity classification (Box 1a breakdown)
| Classification | Amount | Destination form / line |
|----------------|--------|-------------------------|
| Trade or business income | $<amount> | Schedule C Line 1 |
| Rental real estate (no services) | $<amount> | Schedule E Line 3 |
| Rental + substantial services | $<amount> | Schedule C Line 1 |
| Hobby income | $<amount> | Schedule 1 Line 8j |
| Personal payments (friends/family) | $<amount> | Schedule 1 entry space (top of form) |
| Personal-item resale at loss | $<amount> | Schedule 1 entry space (top of form) |
| Personal-item resale at gain | $<amount> | Form 8949 → Schedule D |
| **Sum** | **$<should equal Box 1a>** | |

## Schedule C entries (if applicable)
Line 1 (Gross receipts):                       $<incl 1099-K business portion + non-1099 income>
Line 2 (Returns and allowances):               $<refunds + chargebacks>
Line 4 (COGS, from Part III):                  $<for marketplace sellers>
Line 9 (Car and truck):                        $<mileage at standard rate>
Line 10 (Commissions and fees):                $<platform processing fees>
Line 22 (Supplies):                            $<shipping supplies>
Line 27b (Other expenses, from Part V):        $<labeled categories>
Line 31 (Net profit / loss):                   $<flows to Schedule 1 Line 3 + Schedule SE>

## Schedule 1 entries (if personal portion)
Entry space above Part I (1099-K included in error or personal items sold at a loss): $<personal portion>
Effect on income:                              $0 (the entry is informational; it is not added to Part I)

## Form 1040 entries
Line 25b (Federal tax withheld, Form(s) 1099): $<Box 4 amount>

## Other 1099s for the same income (double-reporting check)
| Other form | Issuer | Amount | Status |
|------------|--------|--------|--------|
| 1099-NEC | <Client name> | $<amount> | Already counted in Schedule C Line 1, not double-reported |

## Validation summary
- Identity checks: passed
- Reconciliation checks: passed
- Schedule C checks: passed
- Schedule 1 checks: passed
- Backup withholding check: passed
- Sanity warnings: <list any>

## Sources cited in this draft
- IRS Form 1099-K (current revision)
- IRS Instructions for Form 1099-K
- IRC §6050W (third-party payment reporting)
- IRC §61 (gross income definition)
- IRC §162 (trade or business expenses)
- IRC §183 (hobby loss rules)
- IRS FS-2025-08, Form 1099-K FAQs (Oct. 23, 2025, reflecting P.L. 119-21)
- 2025 Form 1040 instructions, Schedule 1 "Form(s) 1099-K"
- (any others relied on)
```

The reconciliation is **not** a filed form. It is a worksheet that drives the user's actual return entries on Schedule C, Schedule 1, Schedule E, Form 8949, and Form 1040 — see `filing.md`.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/boxes-explained.md`](./references/boxes-explained.md) — Every box on Form 1099-K with examples and edge cases
- [`references/phased-thresholds.md`](./references/phased-thresholds.md) — History of the $600 / $5,000 / $2,500 / $20,000 thresholds, OBBBA reversal, state thresholds, voluntary reporting
- [`references/personal-vs-business.md`](./references/personal-vs-business.md) — Decision tree for classifying transactions: trade-or-business vs hobby vs personal vs personal-item-resale
- [`references/reconciliation.md`](./references/reconciliation.md) — Reconciling 1099-K to Schedule C / Schedule 1 / Schedule E / Form 8949; double-reporting handling; corrected-form workflow
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 1099-K filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: entering 1099-K-derived figures into TurboTax / FreeTaxUSA / IRS Free File / Free File Fillable Forms

## Examples

End-to-end worked 1099-K reconciliations. Use these as patterns when the user's situation is similar.

- [`examples/etsy-seller-business.md`](./examples/etsy-seller-business.md) — Marketplace seller (Etsy) with clear trade-or-business activity. Reconciles 1099-K to Schedule C with COGS, fees, shipping, and a small craft-fair side income. Same pattern as the Maya Chen example in the Jupid blog companion.
- [`examples/venmo-personal-payments.md`](./examples/venmo-personal-payments.md) — Mixed-use Venmo account: 80% friends/family reimbursements + 20% small freelance payments. Reconciles via the entry space at the top of Schedule 1 for the personal portion and Schedule C for the freelance portion.
- [`examples/airbnb-host.md`](./examples/airbnb-host.md) — Short-term rental host. Decision tree for Schedule E (passive rental) vs Schedule C (substantial services). Most STR hosts file Schedule E; the substantial-services exception is rare.

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the current revision — IRS publishes annual updates to Form 1099-K and revises the FAQs as guidance changes.

- [1099-K Guide 2026: Payment App Reporting Thresholds, Rules, and How to File](https://jupid.com/blog/1099-k-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1099-K (latest)](https://www.irs.gov/pub/irs-pdf/f1099k.pdf) — the form itself
- [Instructions for Form 1099-K (latest)](https://www.irs.gov/pub/irs-pdf/i1099k.pdf) — line-by-line IRS guidance
- [About Form 1099-K](https://www.irs.gov/forms-pubs/about-form-1099-k) — IRS landing page with archive of past revisions
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) — web version of FS-2025-08
- [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) — Form 1099-K FAQs revised Oct. 23, 2025 (IR-2025-107): retroactive $20,000 / 200, no minimum for payment cards, Schedule 1 entry space
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Schedule 1 "Form(s) 1099-K" entry-space instructions and examples
- [IRS Notice 2023-74](https://www.irs.gov/pub/irs-drop/n-23-74.pdf) — Calendar year 2023 transition relief
- [IRS Notice 2024-85](https://www.irs.gov/pub/irs-drop/n-24-85.pdf) — Phase-in schedule ($5,000 / $2,500 / $600), superseded retroactively by P.L. 119-21 §70432
- [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) — 2025 70¢; 2026 72.5¢ (Jan–Jun) and 76¢ (Jul–Dec)
- [Schedule C (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-c-form-1040) — Profit or Loss from Business
- [Schedule E (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-e-form-1040) — Supplemental Income and Loss (rentals)
- [Schedule 1 (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-1-form-1040) — Additional Income and Adjustments
- [Form 8949](https://www.irs.gov/forms-pubs/about-form-8949) — Sales and Other Dispositions of Capital Assets
- [Publication 334](https://www.irs.gov/publications/p334) — Tax Guide for Small Business
- [Publication 525](https://www.irs.gov/publications/p525) — Taxable and Nontaxable Income
- IRC §6050W (returns relating to payments made in settlement of payment card and third-party network transactions)
- IRC §61 (gross income defined)
- IRC §162 (trade or business expenses)
- IRC §183 (activity not engaged in for profit / hobby loss rules)
- IRC §3406 (backup withholding requirements, 24% rate; §3406(b)(8) TPSO threshold for backup withholding)
- IRC §67(g) (miscellaneous itemized deductions, including hobby expenses, disallowed; made permanent by P.L. 119-21 §70110)
- P.L. 119-21 §70432 (restoration of $20,000 / 200 threshold for IRC §6050W(e), retroactive to ARPA's effective date)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state activity, mixed business/hobby/rental, large personal-item-resale gains, prior-year corrections) warrant a licensed tax professional's review.
