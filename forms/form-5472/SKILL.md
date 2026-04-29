---
name: form-5472
description: >
  Use this skill when a 25%-or-more foreign-owned US corporation, OR a
  foreign corporation engaged in a US trade or business, OR a foreign-owned
  US disregarded entity (single-member LLC owned 100% by a non-US person)
  needs to file Form 5472 to report related-party transactions. Triggers on
  phrases like "Form 5472", "25% foreign-owned LLC", "foreign-owned single-
  member LLC tax filing", "DE LLC for foreign owner", "Delaware LLC foreign
  owner tax", "foreign corp doing business in US", "related-party
  transactions with foreign parent". Do NOT use for: a US-only LLC with no
  foreign owners (no 5472 needed); a foreign corporation that is a CFC
  reporting under Form 5471 (different scope; both 5471 and 5472 may apply
  in some cases — see decision tree); foreign trust reporting (use Form
  3520 / 3520-A); a foreign owner's individual US tax return for ECI (use
  Form 1040-NR).
form: Form 5472 (Information Return of a 25% Foreign-Owned U.S. Corporation or a Foreign Corporation Engaged in a U.S. Trade or Business)
audience: [foreign, ccorp, llc1]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f5472.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i5472.pdf
---

# Form 5472 — Information Return of a 25% Foreign-Owned US Corporation or a Foreign Corporation Engaged in a US Trade or Business

This skill produces an audit-grade draft of Form 5472 for a **reporting
corporation** (the entity required to file) covering each **related party**
with which it had reportable transactions during the tax year. The form is
filed as an attachment to the reporting corporation's income tax return:

- **US C-corporation** (Form 1120) → Form 5472 attached
- **Foreign corporation engaged in US trade/business** (Form 1120-F) →
  Form 5472 attached
- **Foreign-owned US disregarded entity (DE)** (typically a single-member
  LLC owned by a non-US person) → file a **pro-forma Form 1120** with
  Form 5472 attached. The pro-forma 1120 is mostly blank (the DE has no
  US income tax liability of its own; income flows through to the foreign
  owner). It exists solely as a vehicle for Form 5472. This is the most
  common 5472 scenario and the one most often missed.

The math is light (mostly transaction totals). The judgment is in
(a) determining who the "related parties" are (25% direct or indirect
ownership; "related" under IRC §§267(b) / 707(b)(1)), (b) classifying
each transaction into the 5472 categories, and (c) documenting transfer
pricing where amounts are large or unconventional.

The skill instructs the agent to ASK rather than guess on each of these.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 5472, "25% foreign-owned",
  "foreign-owned LLC", or "DE LLC tax filing"
- The user is a foreign individual (or foreign entity) who owns 100% of a
  US single-member LLC that hasn't elected to be taxed as a corporation
  → this is a foreign-owned DE under Treas. Reg. §301.7701-2(c)(2)(vi)
  (effective for tax years beginning on or after January 1, 2017) and
  must file pro-forma 1120 + 5472 even with $0 US-source income
- The user is a US C-corporation with at least one direct or indirect
  25%-or-more foreign shareholder, where the corporation had reportable
  transactions with that shareholder or with another related foreign
  party during the year
- The user is a foreign corporation that has US trade or business income
  (effectively connected income, ECI) reported on Form 1120-F, and had
  reportable transactions with related parties during the year
- The user has a US C-corp with a foreign parent (e.g., Delaware sub of a
  German GmbH) and wants to know "what tax forms do we file"

Do **not** engage this skill when:

- The user's US LLC has only US owners → no Form 5472. (A multi-member
  LLC with US partners files Form 1065; a single-member LLC with US
  owner files Schedule C, Schedule E, or Schedule F on the owner's
  Form 1040.)
- The user owns a foreign corporation as a US person (CFC analysis) →
  use the (forthcoming) `form-5471` skill. Note: a US C-corp that owns
  a foreign sub AND has a foreign parent may need both 5471 (looking
  down) and 5472 (looking up).
- The user is reporting foreign trust transactions → use the
  [`form-3520`](../form-3520/) skill
- The user's foreign owner gave a personal gift to a US person → that's
  Form 3520 Part IV (recipient files), not 5472
- The reporting corporation is a small US corp with NO related-party
  transactions → 5472 isn't required even if 25%+ foreign-owned (the
  filing trigger is **transactions**, not just ownership; see Step 2)

If the user's situation is ambiguous (e.g., a Wyoming LLC owned 60% by a
Canadian individual and 40% by a US individual; or a US C-corp owned 100%
by a foreign trust), ask before proceeding. Ownership chain analysis is
fact-intensive.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are
missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 5472 follows the reporting
   corporation's tax year (calendar year for most DEs and small C-corps;
   fiscal year possible for corporations).
2. **Reporting corporation identity**:
   - Legal name
   - US EIN (mandatory; foreign-owned DEs must obtain a US EIN even with
     no US income — apply via Form SS-4 with "foreign-owned U.S.
     disregarded entity" as the reason)
   - State of organization (e.g., Delaware, Wyoming, Nevada)
   - Date of incorporation/formation
   - Business activity / NAICS code
   - Total assets at year-end (US GAAP or book; rough estimate
     acceptable for a DE with no operations)
   - Total US-source gross income for the year
3. **Type of reporting corporation**:
   - **Type 1**: US C-corp with a 25%+ foreign shareholder
   - **Type 2**: Foreign corp engaged in US trade/business (filing
     1120-F)
   - **Type 3**: Foreign-owned US DE (pro-forma 1120 vehicle)
4. **Ownership chain**:
   - Direct 25%+ shareholders: name, address, country, EIN/TIN if any,
     percentage
   - For each direct shareholder, any 25%+ ownership chains above them
     (constructive ownership under IRC §318 with §6038A modifications)
   - Ultimate parent of the corporation (the entity at the top of the
     ownership chain that is not itself owned 25%+ by another entity)
5. **Related parties** for which separate Form 5472s are needed.
   "Related party" under §6038A includes:
   - Any 25%+ direct or indirect foreign shareholder
   - Any other person related under IRC §267(b) or §707(b)(1) (e.g.,
     siblings of foreign owners, foreign sister-corps under common
     control, foreign trusts in which the foreign owner has a
     beneficial interest)
   - **One Form 5472 per related party** — multiple 5472s attached to a
     single 1120 are normal
6. **Transactions during the year** with each related party, classified
   into the 5472 categories. Common categories:
   - Sales of inventory / tangible property
   - Sales of intangible property (patents, trademarks, software)
   - Services rendered (or received)
   - Interest paid / received
   - Royalties paid / received
   - Rents paid / received
   - Loans (principal increase / decrease in outstanding balance)
   - Capital contributions / distributions / dividends
   - Cost-sharing arrangements
   - Any other amounts paid or received between the parties
7. For each transaction category, the **monetary total in USD** for the
   year (gross — don't net offsetting transactions; the form requires
   gross flows in each direction)
8. **Currency translation method** for any transactions denominated in
   foreign currency (Treasury yearly average rate is standard for
   continuous flows; spot rate for one-time transactions)

For foreign-owned DEs specifically:
- Even if there are NO transactions during the year, a Form 5472 is
  still required reporting the **owner's contribution at formation** as
  a related-party transaction in the formation year, AND any
  contributions/distributions in subsequent years
- If truly nothing happened (no formation, no activity, no
  distributions, no transactions), the DE still files pro-forma 1120 +
  5472 with all-zeros — confirm this with the user; "we did nothing" is
  rarely literal

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the entity is a reporting corporation

Walk the three types:

- **Type 1**: Is the user a US C-corp with at least one 25%+ direct or
  indirect foreign shareholder? Check Articles of Incorporation, cap
  table, parent ownership.
- **Type 2**: Is the user a foreign corp filing Form 1120-F because of
  ECI?
- **Type 3**: Is the user a US LLC with one foreign owner, no
  check-the-box election, no other owners? Then it's a foreign-owned
  US DE (Treas. Reg. §301.7701-2(c)(2)(vi)).

If the entity is none of the three, Form 5472 doesn't apply. Common
non-triggers:
- US LLC with all US owners (no foreign in cap table) → no 5472
- US LLC with foreign owner that ELECTED to be taxed as a corporation
  via Form 8832 → it's a corporation, may still trigger 5472 as Type 1
- US partnership (Form 1065) with foreign partners → no 5472 (Form 8865
  may apply for foreign partners' separate reporting; partnership files
  Schedule K-1s)

### Step 2 — Determine if reportable transactions exist

For Type 1 and Type 2 reporters, Form 5472 is required only if the
corporation had **reportable transactions** with at least one foreign
related party during the year. "Reportable transaction" is broadly
defined and includes any monetary or non-monetary transaction, but in
practice:

- Sales of goods/services with the related party
- Loans (any change in outstanding balance, including new loans or
  repayments)
- Interest, royalty, rent payments
- Reimbursements, cost-sharing, license fees
- Capital contributions / distributions (Type 1 only — these are always
  reportable for Type 3 DEs)

If a Type 1/2 reporter had zero reportable transactions with all
related parties in the year, no Form 5472 filing is required. Document
the determination in the corporation's records anyway.

For **Type 3 (foreign-owned DE)**, the rules are stricter:
- Capital contributions, distributions, and any transactions between
  the DE and its foreign owner ARE reportable
- Even formation contributions are reportable (in the formation year)
- A Type 3 DE that legitimately had ZERO transactions in the year still
  must file pro-forma 1120 + 5472 documenting the lack of transactions
  (per Treas. Reg. §1.6038A-2(b))

### Step 3 — Identify all related parties

For each related party, a **separate Form 5472** is filed (multiple 5472s
attached to one 1120 / 1120-F / pro-forma 1120). Build the related-party
list:

1. Each 25%+ direct foreign shareholder
2. Each 25%+ indirect foreign shareholder (through ownership chains)
3. Each person related to a foreign shareholder under §267(b) /
   §707(b)(1) — siblings, parents, children, controlled corps,
   sister-corps under common control, trusts in which the foreign owner
   has > 50% beneficial interest
4. The "ultimate indirect 25% foreign shareholder" — the person at the
   top of any chain that controls 25% of the reporting corp through
   intermediate entities

Each related party gets its own Form 5472 listing the transactions
between that related party and the reporting corporation.

### Step 4 — Classify transactions per related party

For each (related party, transaction-category) pair, sum the year's USD
total. Standard 5472 transaction categories (Part IV / V):

| Category                                          | Examples                                                    |
|---------------------------------------------------|-------------------------------------------------------------|
| Sales of stock in trade (inventory)               | Inventory sold to foreign parent for resale                 |
| Sales of tangible property other than inventory   | Equipment sold; fixed assets transferred                    |
| Platform contribution transactions                | Cost-sharing platform contributions                         |
| Cost-sharing arrangement amounts                  | Pool of R&D costs shared with foreign sister                |
| Rents and royalties received                      | Royalties received from foreign parent for IP licensed up   |
| Sales of intangible property                      | Patent / trademark / software transferred                   |
| Consideration paid/received for use of property   | Equipment lease, software license                           |
| Commissions received / paid                       | Sales commissions to foreign sales agent                    |
| Amounts borrowed (during year, not balance)       | New loan from foreign parent                                |
| Amounts loaned (during year)                      | New loan to foreign sub                                     |
| Interest received / paid                          | On intercompany loans                                       |
| Premiums received / paid for insurance/reinsurance| Captive insurance arrangements                              |
| Other amounts received / paid                     | Reimbursements, management fees                             |
| Capital contributions received                    | Type 3 formation contribution from foreign owner            |
| Capital distributions paid                        | Type 3 distribution to foreign owner                        |

The full list with exact line numbers is in
[`references/line-by-line.md`](./references/line-by-line.md).

### Step 5 — Prepare each Form 5472

For each related party, fill out:
- Part I — Reporting corporation identification (same on every 5472)
- Part II — 25% foreign shareholder identification (the related party)
- Part III — Direct or indirect 25% foreign shareholder if different
  from Part II
- Part IV — Monetary transactions between reporting corp and the related
  party (this is the core)
- Part V — Reportable transactions of a Type 3 DE (foreign-owned DE
  reporting transactions with its foreign owner)
- Part VI — Nonmonetary and less-than-FMV transactions (any transaction
  not at arm's length)
- Part VII — Additional information about the relationship
- Part VIII — Cost-sharing arrangements
- Part IX — Base Erosion Payments (only if subject to Base Erosion and
  Anti-abuse Tax / BEAT under IRC §59A — applies to large
  corporations with $500M+ average gross receipts)

For a small foreign-owned DE filing pro-forma 1120, typical 5472 fills
in:
- Part I (reporting DE identification)
- Part II (foreign owner)
- Part V (capital contributions, distributions, related-party
  transactions)
- Other parts left blank or N/A

### Step 6 — For Type 3 DE, prepare pro-forma 1120

A foreign-owned US DE files a "pro-forma" Form 1120 as a vehicle for
the Form 5472. The pro-forma 1120 has:

- Top-of-form: name, EIN, address, date incorporated
- Box B (item B): check appropriate box
- Note "Foreign-owned U.S. DE" at the top of the form (handwritten or
  typed) per Form 5472 instructions
- Income, deduction, and tax lines: typically all zeros — the DE has no
  separate US tax obligation; income (if any) flows through to the
  foreign owner who files Form 1040-NR (if individual) or Form 1120-F
  (if corporation) for any ECI
- Schedule attachments: just the Form 5472(s)

The pro-forma 1120 itself does not generate tax; it's purely the
chassis for 5472. Don't try to compute tax on it.

### Step 7 — Currency translation

Translate foreign currency totals to USD using a documented method.
Treasury yearly average is standard for continuous flows (interest,
royalties paid throughout the year). Spot rate is appropriate for
one-time transactions (a capital contribution on a specific date).

The Form 5472 amounts must reconcile to the reporting corporation's
books. If books are kept in foreign currency, translate the books to
USD per ASC 830 (functional currency) before extracting 5472 amounts.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off to filing

State the next steps:

- **Form 5472 is filed AS AN ATTACHMENT** to Form 1120, 1120-F, or
  pro-forma 1120. It is not a standalone form.
- For Type 1 (US C-corp with foreign owner): attach to Form 1120 due
  the 15th day of the 4th month after fiscal year-end (April 15 for
  calendar year), extendable 6 months via Form 7004
- For Type 2 (foreign corp with US ECI): attach to Form 1120-F due the
  15th day of the 4th month after fiscal year-end (or 6th month if no
  US office), extendable 6 months via Form 7004
- For Type 3 (foreign-owned DE): attach to pro-forma 1120 due **April
  15** (15th day of 4th month after end of DE's tax year, which
  defaults to calendar year). Extendable via Form 7004.
- **E-filing**: Form 1120 with Form 5472 attached can be e-filed for
  Type 1. For Type 3 (pro-forma 1120 + 5472), e-filing is generally NOT
  available — the pro-forma 1120 must be **paper filed via fax to the
  IRS Ogden office (855-887-7737 — verify current fax number against
  Form 5472 instructions before sending) OR mailed**. See
  [`filing.md`](./filing.md).
- **Penalty for failure to file**: **$25,000 per related party per
  year** under IRC §6038A(d)(1) (statutory minimum, increased from
  $10,000 by the 2017 TCJA). Continuing $25,000 penalties for each
  30-day period after IRS notice. The penalty is per related party —
  a corp with 5 related foreign parties that fails to file faces
  $125,000 minimum.

### Step 11 — File the return

Follow [`filing.md`](./filing.md). For Type 3 DEs, this is a paper/fax
flow. For Type 1/2 with e-fileable 1120 / 1120-F, follow standard
corporate e-file procedures with attached 5472 PDFs.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md).
High-level rules below.

### Part I — Reporting corporation

- **Lines 1a-1g** — Name, EIN, address, date incorporated, place of
  organization, total assets, total receipts, principal business
  activity
- **Line 1h** — Country(ies) where return is also filed for tax purposes
- **Line 1i** — Total value of gross payments made and received in
  reportable transactions

### Part II — 25% foreign shareholder

- **Lines 2a-2k** — Name, address (foreign), country, US ID# if any,
  reference ID, ownership percentage, principal country of business

If multiple 25%+ shareholders, file a separate Form 5472 for each (or
combine into one 5472 if both are the SAME entity through different
ownership chains — rare).

### Part III — Direct or indirect 25% foreign shareholder

If the Part II shareholder is held through one or more intermediate
entities, Part III identifies the **direct** owner (or the entity at
the next level up). For a simple two-level chain (foreign parent owns
US sub directly), Part II = Part III. For longer chains (foreign
ultimate owner → foreign holding co → US sub), Part III identifies the
intermediate.

### Part IV — Monetary transactions between reporting corporation and foreign related party

The core of the form. Each line represents a transaction category;
fill the dollar amount of transactions of that type with this related
party during the year. Both directions matter:

- "Amounts received from related party" (e.g., Line 8a — sales to
  related party)
- "Amounts paid to related party" (e.g., Line 8b — purchases from
  related party)

Don't net. Show gross flows in each direction.

### Part V — Reportable transactions of a Type 3 DE

For foreign-owned US DEs, Part V captures transactions between the DE
and any related party (most often the foreign owner). Categories:

- Amounts paid to related party
- Amounts received from related party
- Capital contributions received
- Capital distributions made
- Loans (changes in balance)

A foreign-owned DE that received an initial $1,000 capital contribution
from its foreign owner at formation reports this in Part V even if
nothing else happened.

### Part VI — Nonmonetary and less-than-FMV transactions

Any transaction not in cash or that wasn't at arm's length. Examples:

- Equipment transferred for less than FMV
- IP transferred without compensation
- Services performed by foreign parent for US sub without billing

These are flagged for transfer-pricing scrutiny. The user should be
prepared to defend the valuation.

### Part VII — Additional information

Various Yes/No questions about the relationship, the foreign
shareholder's other US entities, etc. Read each carefully against the
current-year instructions.

### Part VIII — Cost-sharing arrangements

If the related parties share R&D, IP development, or platform costs
under a CSA, this part documents the arrangement and the year's
contributions.

### Part IX — Base Erosion Payments (BEAT)

Only filled if the reporting corporation is subject to BEAT under IRC
§59A. BEAT applies to corporations with **average annual gross receipts
of $500 million or more** over the prior 3 years AND a base erosion
percentage of 3% or more (2% for banks/SecDealers). Most filers,
especially Type 3 DEs, leave Part IX blank.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that
fails — don't silently fix.

### Math and structural checks

- [ ] Reporting corporation's EIN appears on every Form 5472 (one per
      related party) and on the 1120/1120-F/pro-forma 1120
- [ ] Number of Form 5472s matches number of related parties identified
- [ ] Each Form 5472 has Part I + Part II + Part IV (or V for DEs)
      filled in at minimum
- [ ] Type 3 DE: pro-forma 1120 has "Foreign-owned U.S. DE" notation at
      top of the form
- [ ] All transaction amounts are in USD with documented exchange-rate
      source for foreign-denominated underlying transactions
- [ ] Aggregated dollar amounts on Line 1i (Part I) reconcile to sum of
      transactions across all related-party 5472s

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Type 3 DE reports zero transactions of any kind for any year
      after formation — confirm: is this truly inactive, or are the
      formation contributions / distributions being missed?
- [ ] Reporting corp has substantial sales / purchases with related
      foreign party but reports nothing on Part VI (nonmonetary /
      less-than-FMV) — likely fine if all transactions were arm's
      length, but confirm transfer-pricing documentation exists
- [ ] Reporting corp has loans outstanding to/from related party but
      no interest income/expense reported — confirm interest is being
      charged at AFR or applicable foreign equivalent (otherwise IRC
      §482 / §7872 imputed interest applies)
- [ ] Royalties paid to foreign parent for IP licensing exceed 5% of
      US sub's gross income — high-royalty arrangements draw IRS
      transfer-pricing scrutiny; ensure §482 documentation supports
      the rate
- [ ] Type 1 corp has 25% foreign shareholder but reports no
      dividends, no management fees, no service charges — possible
      that everything was non-cash; confirm this is consistent with
      books
- [ ] Reporting corp's average annual gross receipts > $500M but
      Part IX (BEAT) is blank — confirm BEAT does not apply or
      complete Part IX

### Cross-form checks

- [ ] Form 5472 amounts on Part IV / V reconcile to corresponding
      lines on Form 1120 / 1120-F (e.g., interest paid to related
      party on 5472 should match a portion of 1120 interest expense)
- [ ] If the reporting corporation also files Form 5471 (controlled
      foreign sub), confirm 5471 transactions don't double-count with
      5472 transactions (5471 reports up the chain to a CFC; 5472
      reports across to a US sub)
- [ ] If FBAR or Form 8938 also applies (the corp has foreign
      financial accounts), separate filing required
- [ ] Form 7004 extension covers the 1120/1120-F/pro-forma 1120 and
      thus the attached 5472(s)

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to
the IRS Form 5472 PDF and attach to the appropriate income tax return.
Format below — produce ONE complete deliverable PER related party.

```markdown
# Form 5472 — DRAFT for tax year YYYY
## (Form 5472 #N of M for reporting corporation [Name])

## Reporting corporation identity (Part I — same on every 5472 attached
## to this return)
1a. Name of reporting corporation: <name>
1b. EIN: <EIN>
1c. Address: <address>
1d. Total assets (book value at year-end): $X,XXX
1e. Principal business activity / NAICS: <description>, <code>
1f. Total US-source gross income: $X,XXX
1g. Total payments / receipts in reportable transactions: $X,XXX
1h. Country(ies) where return also filed: <list>
1i. Type of reporting corporation:
    [ ] Type 1 — US C-corp, 25% foreign-owned
    [ ] Type 2 — Foreign corp engaged in US trade/business
    [x] Type 3 — Foreign-owned US disregarded entity

## Related party (Part II)
2a. Name: <foreign related party name>
2b. Address: <foreign address>
2c. Country: <country>
2d. US ID # (if any): <EIN/ITIN/SSN or "None">
2e. Foreign ID # / reference ID: <if any>
2f. Principal country where business conducted: <country>
2g. Ownership percentage: X% direct | X% indirect | X% total
2h. Principal business activity of related party: <description>

## Direct vs indirect ownership (Part III)
[If different from Part II, identify the direct owner or intermediate
entity]
N/A | <details>

## Part IV — Monetary transactions (Type 1 or Type 2)
| Line | Transaction category                           | Received from RP | Paid to RP   |
|------|------------------------------------------------|------------------|--------------|
| 8    | Sales of stock in trade (inventory)            | $X,XXX           | $X,XXX       |
| 9    | Sales of tangible property                     | $X,XXX           | $X,XXX       |
| 10   | Platform contribution                          | $X,XXX           | $X,XXX       |
| 11   | Cost-sharing arrangement                       | $X,XXX           | $X,XXX       |
| 12   | Rents and royalties                            | $X,XXX           | $X,XXX       |
| 13   | Sales of intangible property                   | $X,XXX           | $X,XXX       |
| 14   | Use of property                                | $X,XXX           | $X,XXX       |
| 15   | Commissions                                    | $X,XXX           | $X,XXX       |
| 16   | Amounts borrowed during year                   | n/a              | $X,XXX       |
| 17   | Amounts loaned during year                     | $X,XXX           | n/a          |
| 18   | Interest                                       | $X,XXX           | $X,XXX       |
| 19   | Premiums received/paid                         | $X,XXX           | $X,XXX       |
| 20   | Other amounts                                  | $X,XXX           | $X,XXX       |

## Part V — Type 3 DE reportable transactions
| Line | Transaction                                    | Amount       |
|------|------------------------------------------------|--------------|
|      | Capital contribution received from foreign owner | $X,XXX     |
|      | Capital distribution paid to foreign owner       | $X,XXX     |
|      | Loans from foreign owner (year-end balance)      | $X,XXX     |
|      | Loans to foreign owner (year-end balance)        | $X,XXX     |
|      | Other reportable transactions                    | $X,XXX     |

## Part VI — Nonmonetary / less-than-FMV transactions
[List each, with description, date, valuation method]
N/A | <details>

## Part VII — Additional information
[Yes/No items per current-year instructions]

## Part VIII — Cost-sharing arrangement
[Only if applicable]
N/A | <details>

## Part IX — Base Erosion Payments (BEAT)
[Only if reporting corp meets §59A thresholds]
N/A — average annual gross receipts < $500M | <details>

## Currency translation
Source: <Treasury yearly average | spot rate | functional currency
        translation per ASC 830>
Notes: <list rates used, special items>

## Required attachments / coordination
- [ ] Attached to Form 1120 (Type 1) | Form 1120-F (Type 2) |
      pro-forma Form 1120 (Type 3)
- [ ] If Type 3: pro-forma 1120 has "Foreign-owned U.S. DE" notation
- [ ] Form 8832 election (if relevant) attached separately
- [ ] Transfer-pricing documentation (IRC §6662(e)) — kept with
      taxpayer records, available on IRS request

## Filing channel
| Type | Filing |
|------|--------|
| Type 1 (1120) | E-file or paper to filer's IRS service center |
| Type 2 (1120-F) | E-file or paper to IRS Ogden / Austin per instructions |
| Type 3 (pro-forma 1120 + 5472) | Paper file via fax to 855-887-7737 OR mail to: Internal Revenue Service, 1973 N Rulon White Blvd., M/S 6112, Attn: PIN Unit, Ogden, UT 84404 (verify against current Form 5472 instructions) |

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Cross-form: <reconciliation with 1120/1120-F if applicable>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 5472 (revision date YYYY-MM-DD)
- IRS Instructions for Form 5472 (revision date YYYY-MM-DD)
- IRC §6038A (information returns by 25%-foreign-owned corps)
- IRC §6038C (foreign corps engaged in US business)
- IRC §6038A(d) ($25,000 per failure penalty)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned DE rules,
  effective 2017)
- Treas. Reg. §1.6038A-2 through §1.6038A-4 (5472 mechanics)
- IRC §59A (BEAT, if applicable)
- IRC §482 (transfer pricing arm's-length rules)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter
the data into the IRS Form 5472 fillable PDF, attach to the
1120/1120-F/pro-forma 1120, and file via the appropriate channel.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete
  walkthrough of Parts I-IX, line by line, with edge cases
- [`references/disregarded-entity.md`](./references/disregarded-entity.md)
  — Foreign-owned US DE rules; Treas. Reg. §301.7701-2(c)(2)(vi);
  pro-forma 1120 mechanics; common DE-only filing pattern (the most
  common 5472 scenario)
- [`references/related-party-rules.md`](./references/related-party-rules.md)
  — Who counts as a "related party" under §6038A and §267(b) /
  §707(b)(1); ownership-chain analysis; constructive ownership rules
- [`references/transfer-pricing.md`](./references/transfer-pricing.md) —
  IRC §482 arm's-length pricing; what documentation to keep; common
  Form 5472 transfer-pricing red flags
- [`references/common-mistakes.md`](./references/common-mistakes.md) —
  Top 5472 mistakes that trigger $25,000 penalties, with fixes
- [`filing.md`](./filing.md) — Filing playbook (e-file for Type 1/2,
  paper/fax for Type 3 pro-forma 1120)

## Examples

End-to-end worked Form 5472s. Use these as patterns when the user's
situation is similar.

- [`examples/foreign-owner-disregarded-llc.md`](./examples/foreign-owner-disregarded-llc.md)
  — French citizen owns 100% of Delaware single-member LLC for e-commerce
  dropshipping; pro-forma 1120 + 5472 even with $0 US-source income
- [`examples/foreign-parent-us-subsidiary.md`](./examples/foreign-parent-us-subsidiary.md)
  — German GmbH owns 100% of Delaware C-corp; full Form 1120 with
  Form 5472 (intercompany inventory, management fee, loan, interest)
- [`examples/joint-venture-with-foreign-partner.md`](./examples/joint-venture-with-foreign-partner.md)
  — 60/40 US-Canadian C-corp joint venture; 40% Canadian shareholder
  triggers Form 5472 with multiple Part IV transactions (royalty,
  services, equipment lease, loan)

## Sources

Authoritative sources used by this skill. Always re-verify these
against the IRS site for the tax year being filed — the IRS revises
forms and instructions each cycle.

- [Form 5472 (latest)](https://www.irs.gov/pub/irs-pdf/f5472.pdf) — the form itself
- [Instructions for Form 5472 (latest)](https://www.irs.gov/pub/irs-pdf/i5472.pdf) — line-by-line IRS guidance
- [About Form 5472](https://www.irs.gov/forms-pubs/about-form-5472) — IRS landing page with archive
- [Form 1120 (latest)](https://www.irs.gov/pub/irs-pdf/f1120.pdf) — required vehicle for Type 1 and Type 3
- [Form 1120-F](https://www.irs.gov/forms-pubs/about-form-1120-f) — required vehicle for Type 2
- [Form SS-4](https://www.irs.gov/forms-pubs/about-form-ss-4) — to obtain US EIN for foreign-owned DE
- [Form 7004](https://www.irs.gov/forms-pubs/about-form-7004) — automatic 6-month extension for 1120 and 1120-F
- [Form 8832](https://www.irs.gov/forms-pubs/about-form-8832) — entity classification election
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038C (information returns by foreign corporations engaged in US business)
- IRC §6038A(d) and §6038C(c) — $25,000 per failure penalties
- IRC §267(b), §707(b)(1) (related-party definitions)
- IRC §482 (allocation of income among controlled taxpayers)
- IRC §59A (BEAT)
- IRC §6662(e) (transfer-pricing penalty / contemporaneous documentation)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned US DE; 2016 final
  regs effective for tax years beginning on or after Jan 1, 2017)
- Treas. Reg. §1.6038A-1 through §1.6038A-7 (Form 5472 mechanics)
- Notice 2017-XX (any updates to 5472 procedures — verify current)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. It does not establish a
CPA-client relationship. The $25,000 statutory minimum penalty per
failure makes Form 5472 unforgiving of small mistakes; any user with a
non-trivial cross-border structure (multiple related parties, large
intercompany flows, BEAT exposure) should have a licensed international
tax practitioner (CPA, EA, or attorney) review the draft before filing.
For transfer-pricing-heavy structures, a transfer-pricing economist or
specialist firm is standard.
