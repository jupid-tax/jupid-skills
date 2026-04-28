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
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1099k.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099k.pdf
---

# Form 1099-K — Payment Card and Third Party Network Transactions

This skill walks the agent through reconciling a Form 1099-K and routing the gross-payment amount to the correct line on the recipient's federal return. The 1099-K is an **information return** issued under IRC §6050W by payment settlement entities (PSEs) — credit-card processors and third-party networks — to anyone who received gross payments through their platform.

The 1099-K itself is **not filed by the recipient** — the PSE files it with the IRS and sends a copy to the user. The recipient's job is **reconciliation**: figure out which portion of the reported gross is business income, which is personal payment received in error, which is a hobby, which is a personal-item resale, and route each portion to the right form.

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
- The user received a **1099-MISC** for rents, royalties, prizes, or attorney fees (different form)
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
3. **Box 1b (card-not-present)** — usually equal to or close to Box 1a; informational.
4. **Box 2 (number of transactions)** — count of separate payment transactions.
5. **Box 4 (federal income tax withheld)** — usually $0; non-zero only if the user was subject to backup withholding.
6. **Boxes 5a-5l (monthly breakdown)** — gross by month; useful for spotting timing issues (e.g., December settlements that hit January).
7. **Boxes 6-8 (state info)** — state-level reporting if applicable.
8. **The user's own records** — what was the underlying activity? Business sales? Selling personal items? Friends-and-family Venmo payments mistakenly classified as business? Rental income?
9. **Other 1099s for the same income** — did a client also issue a 1099-NEC for payments that flowed through the same platform? (Double-reporting check, see `references/reconciliation.md`.)
10. **Activity classification** — for each portion of the gross: business / hobby / personal payment received / personal-item resale. See [`references/personal-vs-business.md`](./references/personal-vs-business.md).

For marketplace sellers and gig workers specifically, also ask:

- Is this a **trade or business** (regular, continuous, profit-motive activity) or a **hobby** (sporadic, no profit motive)? Different reporting + different deduction treatment post-TCJA.
- For rentals: does the activity rise to "trade or business" (Schedule C) or is it passive rental income (Schedule E)? See [`examples/airbnb-host.md`](./examples/airbnb-host.md).
- For "personal item" resellers (selling old furniture, used clothing on Mercari/Poshmark): are most sales **at a loss** (excludable, IRS Notice 2023-74) or **at a gain** (capital gain, Schedule D / Form 8949)?

The single most-common 1099-K failure: a freelancer mixes business and personal Venmo payments on one account, gets a 1099-K covering both, and either (a) reports the entire gross as business income (overpaying SE tax) or (b) reports only the business portion (creating an IRS document-mismatch). The correct path requires explicit reconciliation. See `examples/venmo-personal-payments.md`.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm form and 2026 threshold context

Verify the user has an actual Form 1099-K (not a 1099-NEC, 1099-MISC, or platform-internal sales report). Ask the user to read the title at the top of the form: it must say "Payment Card and Third Party Network Transactions."

Reporting threshold context for tax year 2026 (per IRC §6050W as restored by the One, Big, Beautiful Bill Act / OBBBA, July 2025): a third-party settlement organization is required to file a 1099-K only if **both** of these are met:

- Gross payments exceed **$20,000**, AND
- Number of transactions exceeds **200**

The American Rescue Plan Act of 2021 had attempted to lower this to $600 / no transaction minimum. The IRS issued a phased rollout under Notice 2024-85 ($5,000 for 2024, $2,500 for 2025, $600 for 2026). OBBBA superseded the phased rollout and restored $20,000 / 200 permanently. As of the IRS Form 1099-K FAQs updated November 17, 2025, $20,000 / 200 is the operative federal threshold for tax year 2026.

Important caveats:

- **Voluntary reporting**: PSEs may issue a 1099-K below the federal threshold (some always do). The recipient still has to reconcile and report.
- **State thresholds may be lower**: Massachusetts, Maryland, Virginia, Vermont, Montana, North Carolina, DC, New Jersey, and Rhode Island have lower thresholds. See [`references/phased-thresholds.md`](./references/phased-thresholds.md).
- **All income is taxable regardless of whether a 1099-K was issued.** The form only changes whether the payor was required to report — the underlying income is taxable either way.

### Step 2 — Classify each portion of the gross

Walk the user through breaking down Box 1a by activity type. Use [`references/personal-vs-business.md`](./references/personal-vs-business.md). For each transaction (or each batch of similar transactions), classify as:

| Classification | What it is | Where it goes |
|----------------|-----------|---------------|
| **Trade or business income** | Regular, profit-motive activity (freelance services, marketplace sales, gig work) | Schedule C, Line 1 |
| **Rental of real property** | Long-term residential rental, commercial rental, or short-term rental without substantial services | Schedule E |
| **Rental + substantial services** | Short-term rental with hotel-like services (cleaning, meals, concierge) | Schedule C |
| **Hobby income** | Sporadic, no profit motive (occasional crafts, casual reselling for fun) | Schedule 1, Line 8j (Activity not engaged in for profit) — full income, NO expense deduction post-TCJA |
| **Personal payment received** | Friends/family reimbursement, gift, splitting dinner | Schedule 1, Line 8z (Other income) with offsetting Schedule 1, Line 24z adjustment to net to $0 |
| **Personal item resale at a loss** | Sold used personal property below original cost (used clothing, furniture, electronics) | Not reported as income (loss not deductible). Document via Schedule 1, Line 8z $0 with explanation if 1099-K total includes it |
| **Personal item resale at a gain** | Sold collectible / personal property above cost basis | Form 8949 + Schedule D (capital gain) |

If a single 1099-K covers multiple classifications (typical for mixed-use Venmo or PayPal accounts), the gross splits — the agent must produce a reconciliation showing the breakdown.

### Step 3 — Reconcile against payer records

Cross-check Box 1a against the user's own records from the platform:

- Pull the platform's gross payments report for the calendar year (most platforms expose this in their tax/year-end report)
- Compare to Box 1a — they should match exactly. Mismatches usually trace to: chargebacks the platform reversed in early next year, currency conversions, multiple linked accounts, or platform error.
- If the 1099-K is wrong, contact the PSE and request a **corrected 1099-K** (Form 1099-K with the "CORRECTED" box checked). Do not file with a known-wrong number.

Cross-check against any other 1099 forms the user received for the same income:

- If a client paid through PayPal AND issued a 1099-NEC for the same payments → double-reporting. The user reports the income **once** on Schedule C and keeps records to defend against an IRS document-matching notice.
- The general rule: when 1099-K and 1099-NEC overlap, the income is taxable once. Report it on Schedule C and disclose the overlap if needed (some practitioners file a Schedule C-EZ-style disclosure note; others rely on records-on-file).

See [`references/reconciliation.md`](./references/reconciliation.md) for the full process.

### Step 4 — Map each classification to a return line

For each classified portion from Step 2, fill in the destination line:

| Classification | Form / Schedule | Line | Box on 1099-K traced from |
|---------------|----------------|------|-------------------------|
| Trade or business | Schedule C | Line 1 (Gross receipts) | Box 1a portion |
| Rental real estate (no services) | Schedule E | Line 3 (Rents received) | Box 1a portion |
| Hotel-like rental (substantial services) | Schedule C | Line 1 | Box 1a portion |
| Hobby income | Schedule 1 | Line 8j (Activity not for profit) | Box 1a portion |
| Personal payment received (gift, friends/family) | Schedule 1 | Line 8z + Line 24z (offsetting adjustment) | Box 1a portion |
| Personal item resale at loss | Schedule 1 | Line 8z + Line 24z (offsetting adjustment, with explanation) | Box 1a portion |
| Personal item resale at gain | Form 8949 → Schedule D | Each sale itemized | Box 1a portion |
| Federal tax withheld (Box 4) | Form 1040 | Line 25c (Other federal income tax withheld) | Box 4 |

### Step 5 — Itemize Schedule C deductions if business

For the trade-or-business portion, the gross goes on Line 1 — but the user is also entitled to deduct the platform's fees and any other ordinary-and-necessary business expenses against it. Common 1099-K-related deductions:

- **Platform processing fees** — Stripe (2.9% + 30¢), PayPal (~2.9%), Etsy transaction fees (6.5% + listing) → Schedule C Line 10 (Commissions and fees)
- **Refunds and chargebacks** processed in the same tax year → Schedule C Line 2 (Returns and allowances)
- **Cost of goods sold** for marketplace sellers → Schedule C Part III → Line 4
- **Shipping supplies** Maya bought (boxes, mailers, tape) → Schedule C Line 22 (Supplies)
- **Postage** Maya bought (separate from buyer-paid shipping that's a pass-through) → Schedule C Line 27a, label "Postage"
- **Mileage** to the post office, fairs, supplier visits → Schedule C Line 9 (Car and truck) at the standard rate (70¢ per mile for 2025; 2026 rate published by IRS in late 2025)

NEVER subtract platform fees from Box 1a before reporting Line 1. Report gross on Line 1, deduct fees as separate expenses. Reporting net would create an IRS document-mismatch.

### Step 6 — Validate

Run every check in the **Validation** section. Surface any sanity warnings.

### Step 7 — Produce the deliverable

Use the template in **Output format**.

### Step 8 — Hand off to filing

The 1099-K itself isn't filed by the recipient. The reconciled outputs flow to Schedule C / Schedule 1 / Schedule E / Form 8949, which are part of the user's Form 1040 return. Hand off to [`filing.md`](./filing.md) which covers:

- Mapping the reconciliation to the actual line items on each schedule
- Common e-file software field locations (TurboTax, FreeTaxUSA, IRS Direct File, IRS Free File / FFFF) for 1099-K entry
- Backup-withholding claim on Form 1040 Line 25c if Box 4 has a non-zero amount
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
- **PSE / EPF indicator** — "Payment Settlement Entity" (PSE) for direct processors; "Electronic Payment Facilitator" (EPF) for some sub-processors. Doesn't change recipient reporting.
- **Filer's name, address, federal ID** — informational.
- **Account number** — platform's internal account ID for the user.

### Recipient info

- **Recipient's TIN** — must match the SSN or EIN the user provided on their W-9 to the platform. Mismatch triggers backup withholding (24%, IRC §3406).
- **Recipient name + address** — must match user's tax-return name. If wrong, request a corrected 1099-K.

### Box 1a — Gross amount of payment card / third party network transactions

The headline number. **Gross before fees, refunds, chargebacks, or any adjustments.** This is what the IRS sees and what document-matching looks for.

### Box 1b — Card-not-present transactions

Subset of Box 1a where the card wasn't physically swiped (almost always equal to Box 1a for online sellers). Informational only.

### Box 2 — Number of payment transactions

Count of separate transactions, not customer count. Multiple sales to one buyer count as multiple transactions. Used to verify the federal $20,000 / 200 threshold.

### Box 3 — (reserved)

Not used in current revisions.

### Box 4 — Federal income tax withheld

Backup withholding (24%) only. $0 unless the user failed W-9 / TIN matching at some point. If non-zero, claim on **Form 1040 Line 25c** (Other federal income tax withheld) — this is a refundable credit against the user's total tax liability.

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
- [ ] Box 2 (number of transactions) is plausible given the user's described activity (e.g., 3 transactions for a "marketplace seller" is suspicious)
- [ ] If the user's own platform records differ from Box 1a → flagged as needs-corrected-1099-K
- [ ] If another 1099 (1099-NEC, 1099-MISC) covers any of the same payments → double-reporting flag with reconciliation note

### Schedule C checks (if any portion is trade/business)

- [ ] Schedule C Line 1 (Gross receipts) ≥ the trade/business portion of Box 1a
- [ ] Line 1 may be > Box 1a portion if user has additional non-1099 business income (cash sales, sub-threshold clients) — that's correct
- [ ] Platform fees deducted on Line 10, not netted into Line 1
- [ ] Refunds / chargebacks on Line 2, not netted into Line 1
- [ ] If user is an Etsy/eBay seller, COGS computed in Part III and flowing to Line 4

### Schedule 1 checks (if any portion is personal or hobby)

- [ ] Personal payments (gift, friends/family, personal-item loss): reported on Line 8z with offsetting Line 24z adjustment netting to $0
- [ ] Hobby income: reported on Line 8j; NO Schedule C; NO expense deduction (post-TCJA, IRC §67(g))
- [ ] Personal-item-loss explanation references IRS Notice 2023-74 / Form 1099-K FAQs

### Schedule E checks (if portion is rental)

- [ ] Schedule E used only for passive rental real estate (no substantial services)
- [ ] Short-term rental with substantial services → moved to Schedule C, not Schedule E

### Backup withholding check

- [ ] If Box 4 > 0, claim on Form 1040 Line 25c
- [ ] Tell the user why backup withholding was applied (failed W-9, TIN mismatch) and how to fix going forward

### Sanity checks (warn, don't block)

- [ ] User describes a "side hustle" but classifies the entire 1099-K as hobby → confirm; profit motive + regularity usually means business
- [ ] User receives 1099-K below the $20,000 / 200 threshold and assumes it's wrong → not necessarily; PSE can voluntarily issue and state thresholds may be lower
- [ ] User wants to subtract platform fees from Box 1a before reporting Line 1 → block; explain the document-mismatch risk
- [ ] User is selling used personal items at a loss but reporting full Box 1a as income → over-reporting; reroute via Schedule 1 Line 8z with $0 adjustment per IRS Notice 2023-74
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
Box 1b (card-not-present):                     $<amount>
Box 2 (transactions):                          <count>
Box 4 (federal tax withheld):                  $<amount>

## Activity classification (Box 1a breakdown)
| Classification | Amount | Destination form / line |
|----------------|--------|-------------------------|
| Trade or business income | $<amount> | Schedule C Line 1 |
| Rental real estate (no services) | $<amount> | Schedule E Line 3 |
| Rental + substantial services | $<amount> | Schedule C Line 1 |
| Hobby income | $<amount> | Schedule 1 Line 8j |
| Personal payments (friends/family) | $<amount> | Schedule 1 Line 8z + Line 24z (nets to $0) |
| Personal-item resale at loss | $<amount> | Schedule 1 Line 8z + Line 24z (nets to $0) |
| Personal-item resale at gain | $<amount> | Form 8949 → Schedule D |
| **Sum** | **$<should equal Box 1a>** | |

## Schedule C entries (if applicable)
Line 1 (Gross receipts):                       $<incl 1099-K business portion + non-1099 income>
Line 2 (Returns and allowances):               $<refunds + chargebacks>
Line 4 (COGS, from Part III):                  $<for marketplace sellers>
Line 9 (Car and truck):                        $<mileage at standard rate>
Line 10 (Commissions and fees):                $<platform processing fees>
Line 22 (Supplies):                            $<shipping supplies>
Line 27a (Other):                              $<labeled categories>
Line 31 (Net profit / loss):                   $<flows to Schedule 1 Line 3 + Schedule SE>

## Schedule 1 entries (if personal portion)
Line 8z (Other income — describe):             $<personal portion> ("Personal payments included on 1099-K from <PSE>")
Line 24z (Other adjustments — describe):       $<personal portion> ("Offset of personal payments on 1099-K from <PSE>")
Net effect:                                    $0

## Form 1040 entries
Line 25c (Other federal income tax withheld):  $<Box 4 amount>

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
- IRS Notice 2023-74 (personal-item resale guidance for 1099-K)
- IRS Form 1099-K FAQs (Nov 2025 update reflecting OBBBA)
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
- [`filing.md`](./filing.md) — Browser-automation playbook: entering 1099-K-derived figures into TurboTax / FreeTaxUSA / IRS Direct File / IRS Free File

## Examples

End-to-end worked 1099-K reconciliations. Use these as patterns when the user's situation is similar.

- [`examples/etsy-seller-business.md`](./examples/etsy-seller-business.md) — Marketplace seller (Etsy) with clear trade-or-business activity. Reconciles 1099-K to Schedule C with COGS, fees, shipping, and a small craft-fair side income. Same pattern as the Maya Chen example in the Jupid blog companion.
- [`examples/venmo-personal-payments.md`](./examples/venmo-personal-payments.md) — Mixed-use Venmo account: 80% friends/family reimbursements + 20% small freelance payments. Reconciles via Schedule 1 Line 8z + Line 24z for the personal portion and Schedule C for the freelance portion.
- [`examples/airbnb-host.md`](./examples/airbnb-host.md) — Short-term rental host. Decision tree for Schedule E (passive rental) vs Schedule C (substantial services). Most STR hosts file Schedule E; the substantial-services exception is rare.

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the current revision — IRS publishes annual updates to Form 1099-K and revises the FAQs as guidance changes.

- [1099-K Guide 2026: Payment App Reporting Thresholds, Rules, and How to File](https://jupid.com/blog/1099-k-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1099-K (latest)](https://www.irs.gov/pub/irs-pdf/f1099k.pdf) — the form itself
- [Instructions for Form 1099-K (latest)](https://www.irs.gov/pub/irs-pdf/i1099k.pdf) — line-by-line IRS guidance
- [About Form 1099-K](https://www.irs.gov/forms-pubs/about-form-1099-k) — IRS landing page with archive of past revisions
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) — last updated November 17, 2025 reflecting OBBBA threshold restoration
- [IRS Fact Sheet FS-2025-08](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) — Revised 1099-K guidance under OBBBA
- [IRS Notice 2023-74](https://www.irs.gov/pub/irs-drop/n-23-74.pdf) — Transition relief and personal-item resale guidance
- [IRS Notice 2024-85](https://www.irs.gov/pub/irs-drop/n-24-85.pdf) — Phased rollout schedule (superseded by OBBBA July 2025)
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
- IRC §3406 (backup withholding requirements, 24% rate)
- IRC §67(g) (suspension of misc. itemized deductions including hobby expenses, TCJA, through 2025; status for 2026 depends on future legislation)
- OBBBA Section 112202 (restoration of $20,000 / 200 threshold for IRC §6050W)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state activity, mixed business/hobby/rental, large personal-item-resale gains, prior-year corrections) warrant a licensed tax professional's review.
