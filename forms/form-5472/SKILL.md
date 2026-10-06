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
last_verified: 2026-10-06
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
  Form 5472 attached. On the pro-forma 1120 only the DE's name and
  address and items B and E are completed (Instructions for Form 5472,
  When and Where To File); the DE has no US income tax liability of its
  own. It exists solely as a vehicle for Form 5472. This is the most
  common 5472 scenario and the one most often missed.

The math is light (mostly transaction totals). The judgment is in
(a) determining who the "related parties" are (25% direct or indirect
ownership; "related" under IRC §§267(b) / 707(b)(1)), (b) classifying
each transaction into the 5472 categories, and (c) documenting transfer
pricing where amounts are large or unconventional.

The skill instructs the agent to ASK rather than guess on each of these.

**Companion guide for end users:** [Form 5472 (2026): The $25,000 Mistake Foreign-Owned LLCs Make + AI Agent Skill](https://jupid.com/blog/form-5472-foreign-owned-llc-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Revision verified:** the line map in this skill was verified against
Form 5472 (Rev. December 2023) and the Instructions for Form 5472 (Rev.
December 2024), the current revisions on 2026-10-06. Form 5472 is not
revised every year. Before use, check
https://www.irs.gov/forms-pubs/about-form-5472 and re-check the line
numbers if a newer revision exists.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 5472, "25% foreign-owned",
  "foreign-owned LLC", or "DE LLC tax filing"
- The user is a foreign individual (or foreign entity) who owns 100% of a
  US single-member LLC that hasn't elected to be taxed as a corporation
  → this is a foreign-owned DE under Treas. Reg. §301.7701-2(c)(2)(vi)
  (tax years beginning on or after January 1, 2017, and ending on or
  after December 13, 2017) and must file pro-forma 1120 + 5472 for any
  year with a reportable transaction (owner contributions and
  distributions count), even with $0 US-source income
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
     no US income — Form SS-4 line 9a "Other: Foreign-owned U.S.
     disregarded entity-Form 5472" and line 10 "Other: Foreign-owned U.S.
     disregarded entity filing Form 5472" per the Instructions for Form
     SS-4; see [`form-ss-4`](../form-ss-4/SKILL.md))
   - State of organization (e.g., Delaware, Wyoming, Nevada)
   - Date of incorporation/formation
   - Business activity and the 6-digit principal business activity
     code from the list in the Instructions for Form 1120
   - Total assets at year-end (line 1c; for a DE, ask for the year-end
     balance sheet or bank balance)
   - Country or countries where business is conducted (line 1o)
   - Total US-source gross income for the year (not a Form 5472 line;
     needed only to route the owner's own return, e.g.
     [`form-1040-nr`](../form-1040-nr/SKILL.md))
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
   - Loans (beginning and ending balances, or the monthly average)
   - Capital contributions / distributions (Part V, foreign-owned DEs
     only)
   - Cost-sharing arrangements
   - Any other amounts paid or received between the parties
7. For each transaction category, the **monetary total in USD** for the
   year (gross — don't net a sale against a purchase; the form has
   separate received lines 9–21 and paid lines 23–35)
8. **Currency translation method** for any transactions denominated in
   foreign currency. Ask which rates the books use; the instructions
   require a schedule showing the exchange rates used (Instructions for
   Form 5472, Part IV)
9. For a foreign-owned DE: the owner's foreign taxpayer identification
   number (FTIN), or confirmation that there is none (line 4b(3) must
   show the FTIN or "None")

For foreign-owned DEs specifically:
- The **owner's contribution at formation** is a reportable transaction
  in the formation year, and any contributions/distributions in later
  years are reportable too (Treas. Reg. §1.6038A-2(b)(3)(xi); Part V)
- Owner-paid LLC expenses (state annual fee, registered agent) are
  transactions between the owner and the DE; ask about them
- If truly nothing happened in a year (no contribution, no
  distribution, no owner-paid expense, no payment either way), the
  instructions say Form 5472 is not required (Instructions for Form
  5472, Exceptions from filing, item 1; Treas. Reg. §1.6038A-2(e)(1)).
  "We did nothing" is rarely literal: walk the bank statements and the
  owner's card statements with the user before accepting it, and if the
  user or CPA wants to file anyway, note that it is a voluntary filing

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
- US partnership (Form 1065) with foreign partners → no 5472 (Form 5472
  is filed by corporations and foreign-owned DEs). If the partnership
  has effectively connected income allocable to foreign partners, it
  may have §1446 withholding and Forms 8804, 8805, and 8813
  (Instructions for Form 1065 (2025)); route to a CPA

### Step 2 — Determine if reportable transactions exist

For Type 1 and Type 2 reporters, Form 5472 is required only if the
corporation had **reportable transactions** with at least one foreign
related party during the year. "Reportable transaction" is broadly
defined and includes any monetary or non-monetary transaction, but in
practice:

- Sales of goods/services with the related party
- Loans (outstanding balances; new loans and repayments change them)
- Interest, royalty, rent payments
- Reimbursements, cost-sharing, license fees
- Capital contributions / distributions: Part V captures these for Type
  3 DEs only. Part IV has no contribution or dividend line; lines 21 and
  35 ("other amounts") take only amounts "taken into account in
  determining the taxable income" (Instructions for Form 5472, Lines 21
  and 35). For a Type 1/2 corporation, ask the CPA how contributions
  and dividends are handled

If a Type 1/2 reporter had zero reportable transactions with all
related parties in the year, no Form 5472 filing is required. Document
the determination in the corporation's records anyway.

For **Type 3 (foreign-owned DE)**, the rules are stricter:
- Capital contributions, distributions, and any transactions between
  the DE and its foreign owner ARE reportable (Treas. Reg.
  §1.6038A-2(b)(3)(xi))
- Even formation contributions are reportable (in the formation year)
- A Type 3 DE that had ZERO reportable transactions (Parts IV, V, and VI)
  in the year is not required to file (Instructions for Form 5472,
  Exceptions from filing, item 1; Treas. Reg. §1.6038A-2(e)(1)). Exceptions
  2, 3, and 6 in the instructions do not apply to foreign-owned DEs.
  Confirm a "zero" year line by line with the user before relying on it

### Step 3 — Identify all related parties

For each related party, a **separate Form 5472** is filed (multiple 5472s
attached to one 1120 / 1120-F / pro-forma 1120). Build the related-party
list:

1. Each 25%+ direct foreign shareholder
2. Each 25%+ indirect foreign shareholder (through ownership chains)
3. Each person related to the reporting corporation or to a foreign
   shareholder under §267(b) / §707(b)(1) — siblings, parents, children,
   controlled corps, sister-corps under common control, trusts
4. Any other person related to the reporting corporation under §482
   (IRC §6038A(c)(2))

The "ultimate indirect 25% foreign shareholder" (the 25% foreign
shareholder whose ownership is not attributed to another 25% foreign
shareholder) is listed in Part II lines 6a–7e of every Form 5472, with
an attached explanation of the attribution. That listing does not by
itself create a separate Form 5472.

Each related party **with which the reporting corporation had a
reportable transaction** gets its own Form 5472 (Part III names it).
Related parties with no transactions in the year get no form
(Instructions for Form 5472, Line 1g).

### Step 4 — Classify transactions per related party

For each (related party, transaction-category) pair, sum the year's USD
total. Form 5472 (Rev. December 2023) puts amounts received on lines
9–21 (total line 22) and amounts paid on lines 23–35 (total line 36):

| Received line | Paid line | Category | Examples |
|---------------|-----------|----------|----------|
| 9  | 23  | Stock in trade (inventory) sold / purchased | Inventory bought from the foreign parent → line 23 |
| 10 | 24  | Tangible property other than stock in trade | Equipment sold or bought |
| 11 | 25  | Platform contribution transaction payments | CSA platform contributions |
| 12 | 26  | Cost sharing transaction payments | CSA cost shares |
| 13a | 27a | Rents (for other than intangible property rights) | Equipment or office lease |
| 13b | 27b | Royalties (for other than intangible property rights) | |
| 14 | 28  | Sales, leases, licenses, etc., of intangible property rights | Trademark or software license royalties, patent sale |
| 15 | 29  | Technical, managerial, engineering, construction, scientific, or like services | Management fees, seconded engineers |
| 16 | 30  | Commissions | Sales agent commissions |
| 17a/17b | 31a/31b | Amounts borrowed / loaned: beginning and ending balance, or monthly average on line b | Intercompany loan balances |
| 18 | 32  | Interest | Intercompany loan interest |
| 19 | 33  | Insurance or reinsurance premiums | Captive arrangements |
| 20 | 34  | Loan guarantee fees | Parent guarantee fee |
| 21 | 35  | Other amounts, to the extent taken into account in determining taxable income | Reimbursements |
| Part V (DE only) | | Formation, dissolution, contributions, distributions (Treas. Reg. §1.482-1(i)(7)) | Owner's capital wire; owner draw |

The full list with exact line numbers is in
[`references/line-by-line.md`](./references/line-by-line.md).

### Step 5 — Prepare each Form 5472

For each related party, fill out:
- Part I — Reporting corporation identification (lines 1a–1o, 2, 3;
  same on every 5472 except line 1f)
- Part II — 25% foreign shareholders: direct (lines 4–5) and ultimate
  indirect (lines 6–7). For a DE, the foreign owner
- Part III — The related party this form is about (lines 8a–8g; all
  filers complete it, even if the party is also in Part II)
- Part IV — Monetary transactions with a foreign related party (lines
  9–36; required when Part III "foreign person" is checked)
- Part V — Checkbox plus attached statement for a foreign-owned DE's
  formation, dissolution, contribution, and distribution transactions
- Part VI — Checkbox plus attached schedule for nonmonetary and
  less-than-full-consideration transactions
- Part VII — Lines 37–43 (all filers; a DE skips 43a–43b)
- Part VIII — One per cost sharing arrangement (lines 44–49)
- Part IX — Base erosion payments (lines 50–52). Required from an
  "applicable taxpayer" under §59A (Treas. Reg. §1.6038A-2(b)(7));
  otherwise ask the CPA whether to complete it

For a small foreign-owned DE filing pro-forma 1120, the typical 5472
fills in:
- Part I (reporting DE identification; line 3 checked)
- Part II (foreign owner on lines 4a–4e, FTIN or "None" on 4b(3))
- Part III (the foreign owner again, "foreign person" checked, 8e "25%
  foreign shareholder")
- Part IV (any monetary transactions such as loans, fees, or
  reimbursements; totals on lines 22 and 36)
- Part V (checkbox and statement: contributions, distributions,
  formation or dissolution amounts)
- Part VII (lines 37–42 answered)
- Parts VI, VIII, IX only if facts call for them

### Step 6 — For Type 3 DE, prepare pro-forma 1120

A foreign-owned US DE files a "pro-forma" Form 1120 as a vehicle for
the Form 5472. The pro-forma 1120 has:

- Name and address of the DE
- Item B: the DE's employer identification number
- Item E: the applicable boxes (initial return, final return, name
  change, address change)
- "Foreign-owned U.S. DE" written across the top of the Form 1120
- Nothing else: "The only information required to be completed on Form
  1120 is the name and address of the foreign-owned U.S. DE and items B
  and E on the first page" (Instructions for Form 5472, When and Where
  To File). Leave income, deduction, and tax lines blank. Income (if
  any) belongs to the foreign owner, who files Form 1040-NR (if
  individual) or Form 1120-F (if corporation) for any ECI
- Attachments: the Form 5472(s) and the Part V statement

The pro-forma 1120 itself does not generate tax; it's purely the
chassis for 5472. Don't try to compute tax on it.

### Step 7 — Currency translation

Translate foreign currency totals to USD using a documented method and
attach a schedule showing the exchange rates used (Instructions for Form
5472, Part IV). Ask which method the books use (for example a yearly
average rate for recurring flows, the spot rate for a one-time
contribution) and apply it consistently.

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
  (a corporation with a fiscal year ending June 30 files by the 15th
  day of the 3rd month, per the Instructions for Form 1120 (2025),
  When To File)
- For Type 2 (foreign corp with US ECI): attach to Form 1120-F due the
  15th day of the 4th month after fiscal year-end (or 6th month if no
  US office), extendable 6 months via Form 7004
- For Type 3 (foreign-owned DE): attach to pro-forma 1120 due **April
  15** for a calendar year (the due date of Form 1120, including
  extensions). The DE uses its owner's U.S. tax year or, if none, the
  calendar year. Extendable via Form 7004, faxed or mailed to the same
  dedicated unit with "Foreign-owned U.S. DE" across the top and the
  Form 1120 code on Part I, line 1 (Instructions for Form 5472).
- **E-filing**: Form 1120 with Form 5472 attached can be e-filed for
  Type 1. A foreign-owned DE "cannot file Form 5472 electronically"
  (Instructions for Form 5472, Electronic Filing of Form 5472): the
  pro-forma 1120 + 5472 goes by **fax to 855-887-7737 (300 DPI or
  higher) or by mail to Internal Revenue Service, 1973 Rulon White
  Blvd, M/S 6112 Attn: PIN Unit, Ogden, UT 84201** (Instructions for
  Form 5472, Dedicated mailing address). See [`filing.md`](./filing.md).
- **Penalty for failure to file**: **$25,000 for each taxable year**
  under IRC §6038A(d)(1) (raised from $10,000 by Pub. L. 115-97,
  §14401(b)(2), for 2018 and later years). Treas. Reg. §1.6038A-4(a)(3)
  applies it once per related party per year, so a corp that fails to
  file for 5 related foreign parties faces up to $125,000 for that
  year. If the failure continues more than 90 days after IRS notice, an
  additional $25,000 per 30-day period (or part) applies
  (§6038A(d)(2)). A substantially incomplete Form 5472 counts as a
  failure to file (Instructions for Form 5472, Penalties).

### Step 11 — File the return

Follow [`filing.md`](./filing.md). For Type 3 DEs, this is a paper/fax
flow. For Type 1/2 with e-fileable 1120 / 1120-F, follow standard
corporate e-file procedures; Form 5472 is included in the e-filed
return.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md).
High-level rules below.

### Part I — Reporting corporation

- **Lines 1a–1b** — Name, address, EIN of the reporting corporation
- **Line 1c** — Total assets (Form 1120 item D for a domestic
  corporation; Form 1120-F Schedule L line 17 column (d) for a foreign
  one)
- **Lines 1d–1e** — Principal business activity and its 6-digit code
  from the Instructions for Form 1120 / 1120-F list
- **Line 1f** — Total value on THIS form: line 22 + line 36 + Part VI
  FMV (+ Part V items for a DE). Blank for a U.S. related party
- **Line 1g** — Number of Forms 5472 filed for the year (one per related
  party with reportable transactions)
- **Line 1h** — Total of line 1f across all Forms 5472
- **Lines 1i–1k** — Consolidated filing box; initial-year box; number of
  Parts VIII attached
- **Lines 1l–1o** — Country and date of incorporation; countries where
  it files as a resident; principal countries of business (never
  "worldwide")
- **Line 2** — Check if a foreign person owned at least 50% (vote or
  value) at any time in the year
- **Line 3** — Check if a foreign-owned U.S. DE

### Part II — 25% foreign shareholder

- **Lines 4a–4e / 5a–5e** — The two largest direct 25% foreign
  shareholders: name and address; U.S. ID (4b(1)); reference ID if no
  U.S. ID (4b(2)); FTIN (4b(3), mandatory "FTIN or None" for a DE);
  countries of business, citizenship/organization, and tax residence
- **Lines 6a–6e / 7a–7e** — The two largest ultimate indirect 25%
  foreign shareholders, with an attached explanation of the attribution
- More shareholders: attach a sheet. Listing a shareholder in Part II
  does not create a separate Form 5472; transactions do

### Part III — Related party

All filers complete Part III for the one related party the form covers,
even if it also appears in Part II. Check "foreign person" or "U.S.
person"; lines 8a–8g give name, IDs, business activity, relationship
boxes (8e), and countries. "Foreign person" checked → Part IV required.

### Part IV — Monetary transactions between reporting corporation and foreign related party

The core of the form. Received amounts go on lines 9–21 (total line
22); paid amounts go on lines 23–35 (total line 36). Each category has
its own line in each direction (for example, inventory sold on line 9,
inventory purchased on line 23). Loans are reported as balances on
lines 17a/17b (borrowed) and 31a/31b (loaned), or as a monthly average
on 17b/31b. Interest limited by §163(j) is reported at the allowed
amount (line 32). Amounts of $50,000 or less may be reported as
"$50,000 or less"; reasonable estimates (75%–125% of actual) are
allowed with the estimates box checked.

Don't net. Show gross amounts on each line.

### Part V — Reportable transactions of a Type 3 DE

Part V is a checkbox. A foreign-owned DE checks it and attaches a
statement describing any other transaction under Treas. Reg.
§1.482-1(i)(7) not already in Part IV: amounts paid or received in
connection with the formation, dissolution, acquisition, and
disposition of the entity, including contributions to and
distributions from the entity. List each item with date and USD
amount.

A foreign-owned DE whose owner wired a $1,000 capital contribution at
formation checks Part V and describes that contribution, even if
nothing else happened that year.

### Part VI — Nonmonetary and less-than-full-consideration transactions

A checkbox plus an attached schedule, foreign related party only. Use
it for any transaction where part of the consideration was not money,
or less than full consideration was paid or received. Examples:

- Equipment transferred for less than FMV
- IP transferred without compensation
- Services performed by foreign parent for US sub without billing

The schedule describes property and services each way and gives a
reasonable FMV estimate. These are flagged for transfer-pricing
scrutiny. The user should be prepared to defend the valuation.

### Part VII — Additional information

All filers answer lines 37–43: imports from the related party and
customs value (37–38c), CSA participation (39), §267A disallowed
interest or royalties (40a–40b), FDII deduction amounts (41a–41d),
loans inside or outside the 100%–130% AFR safe-haven range (42a–42b),
and §385 covered debt (43a–43b; not completed by a foreign-owned DE).
Ask each question; do not default to "No".

### Part VIII — Cost-sharing arrangements

If the reporting corporation participates in a CSA, complete one Part
VIII per CSA (lines 44–49: description, RAB share, stock-based
compensation, intangible development costs) and count them on line 1k.

### Part IX — Base Erosion Payments (BEAT)

Lines 50–52: base erosion payments, base erosion tax benefits, and
qualified derivative payments. §6038A(b)(2) and Treas. Reg.
§1.6038A-2(b)(7) require this information from an "applicable
taxpayer": a corporation with **average annual gross receipts of $500
million or more** over the prior 3 years AND a base erosion percentage
of 3% or more (2% for groups with a bank or registered securities
dealer) (IRC §59A(e)). The line instructions say "(if any)" without
repeating that limit, so for any other corporation ask the CPA whether
to complete Part IX and record the decision in the draft.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that
fails — don't silently fix.

### Math and structural checks

- [ ] Reporting corporation's EIN appears on every Form 5472 (one per
      related party) and on the 1120/1120-F/pro-forma 1120
- [ ] Number of Form 5472s matches number of related parties with
      reportable transactions, and equals line 1g on every form
- [ ] Each Form 5472 has Part I, Part III, and Part VII completed (all
      filers); Part II for 25% foreign-owned corporations and DEs;
      Part IV whenever Part III "foreign person" is checked; Part V box
      and statement for a DE with formation, contribution, or
      distribution items
- [ ] Line 22 = sum of lines 9–21 and line 36 = sum of lines 23–35
      (only 17b/31b sit in the amount column; state the convention
      used for the loan balances)
- [ ] Line 1f = line 22 + line 36 + Part VI FMV (+ Part V items for a
      DE); line 1h = sum of line 1f on all Forms 5472
- [ ] Type 3 DE: pro-forma 1120 has "Foreign-owned U.S. DE" notation at
      top of the form
- [ ] All transaction amounts are in USD with documented exchange-rate
      source for foreign-denominated underlying transactions
- [ ] Line 4b(3) shows the owner's FTIN or "None" (DE); line 4b(2)
      reference ID present wherever 4b(1) is blank, and the same
      reference ID is used on line 8b(2) and in prior years

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Type 3 DE reports zero transactions of any kind for any year
      after formation — confirm: is this truly inactive, or are the
      formation contributions / distributions / owner-paid fees being
      missed? (A true zero year has no filing requirement; see Step 2)
- [ ] Reporting corp has substantial sales / purchases with related
      foreign party but reports nothing on Part VI (nonmonetary /
      less-than-FMV) — likely fine if all transactions were arm's
      length, but confirm transfer-pricing documentation exists
- [ ] Reporting corp has loans outstanding to/from related party but
      no interest income/expense reported — confirm interest is being
      charged at AFR or applicable foreign equivalent (otherwise IRC
      §482 / §7872 imputed interest applies)
- [ ] Large royalties paid to the foreign parent for IP licensing
      (lines 27b/28) relative to the US sub's revenue — ensure §482
      documentation supports the rate (this skill sets no numeric
      threshold; the CPA judges materiality)
- [ ] Type 1 corp has 25% foreign shareholder but reports no
      dividends, no management fees, no service charges — possible
      that everything was non-cash; confirm this is consistent with
      books
- [ ] Reporting corp's average annual gross receipts ≥ $500M but
      Part IX is blank — it is likely an applicable taxpayer that must
      complete Part IX (Treas. Reg. §1.6038A-2(b)(7)) and Form 8991

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
Form revision: Form 5472 (Rev. December 2023); Instructions (Rev. December 2024)
Tax year: beginning <date>, ending <date>

## Part I — Reporting corporation (same on every 5472 except 1f)
1a. Name and address: <name>, <street, suite>, <city, state, ZIP>
1b. EIN: <EIN>
1c. Total assets: $X,XXX
1d. Principal business activity: <description>
1e. Principal business activity code: <6-digit code from Form 1120 instructions>
1f. Total value of gross payments on THIS form: $X,XXX  (line 22 + line 36 + Part VI FMV + Part V items if DE)
1g. Total number of Forms 5472 filed for the year: M
1h. Total value on ALL Forms 5472: $X,XXX
1i. Consolidated filing: [ ]
1j. Initial year: [ ] / [x]
1k. Number of Parts VIII attached: 0
1l. Country of incorporation: <country>
1m. Date of incorporation: <date>
1n. Country(ies) where it files an income tax return as a resident: <list or ASK>
1o. Principal country(ies) where business is conducted: <list>
2.  Foreign person owned ≥ 50%: [ ] / [x]
3.  Foreign-owned U.S. DE: [ ] / [x]

## Part II — 25% foreign shareholders
Surrogate foreign corporation box: [ ]
4a. Direct 25% foreign shareholder (largest): <name, address>
4b(1) U.S. ID: <SSN/ITIN/EIN or blank>  4b(2) Reference ID: <ID or blank>  4b(3) FTIN: <FTIN or "None">
4c. Principal country(ies) of business: <>  4d. Citizenship/organization: <>  4e. Tax residence: <>
5a–5e. Second direct 25% foreign shareholder: <details or "None">
6a–6e. Ultimate indirect 25% foreign shareholder (largest): <details or "None">; attribution explanation attached: [ ]
7a–7e. Second ultimate indirect: <details or "None">

## Part III — Related party
[ ] foreign person  [ ] U.S. person
8a. Name and address: <>
8b(1) U.S. ID: <>  8b(2) Reference ID: <>  8b(3) FTIN: <>
8c. Principal business activity: <>  8d. Code: <>
8e. Relationship: [ ] related to reporting corp  [ ] related to 25% foreign shareholder  [ ] 25% foreign shareholder
8f. Principal country(ies) of business: <>  8g. Tax residence: <>

## Part IV — Monetary transactions (foreign related party)
Estimates used: [ ]
| Line | Received                                    | Amount   | Line | Paid                                        | Amount   |
|------|---------------------------------------------|----------|------|---------------------------------------------|----------|
| 9    | Sales of stock in trade                     | $0       | 23   | Purchases of stock in trade                 | $0       |
| 10   | Sales of other tangible property            | $0       | 24   | Purchases of other tangible property        | $0       |
| 11   | Platform contribution payments received     | $0       | 25   | Platform contribution payments paid         | $0       |
| 12   | Cost sharing payments received              | $0       | 26   | Cost sharing payments paid                  | $0       |
| 13a  | Rents received                              | $0       | 27a  | Rents paid                                  | $0       |
| 13b  | Royalties received                          | $0       | 27b  | Royalties paid                              | $0       |
| 14   | Intangible property rights sold/licensed    | $0       | 28   | Intangible property rights bought/licensed  | $0       |
| 15   | Services income                             | $0       | 29   | Services paid                               | $0       |
| 16   | Commissions received                        | $0       | 30   | Commissions paid                            | $0       |
| 17a  | Amounts borrowed: beginning balance         | $0       | 31a  | Amounts loaned: beginning balance           | $0       |
| 17b  | Amounts borrowed: ending balance / mo. avg. | $0       | 31b  | Amounts loaned: ending balance / mo. avg.   | $0       |
| 18   | Interest received                           | $0       | 32   | Interest paid                               | $0       |
| 19   | Insurance premiums received                 | $0       | 33   | Insurance premiums paid                     | $0       |
| 20   | Loan guarantee fees received                | $0       | 34   | Loan guarantee fees paid                    | $0       |
| 21   | Other amounts received                      | $0       | 35   | Other amounts paid                          | $0       |
| 22   | Total received                              | $0       | 36   | Total paid                                  | $0       |
Line 17/31 balances included in totals: <yes/no, per preparer convention>

## Part V — Foreign-owned U.S. DE transactions
Box checked: [ ] / [x]  Attached statement:
| Date | Description (contribution / distribution / formation / dissolution / owner-paid expense) | USD |
|------|------------------------------------------------------------------------------------------|-----|

## Part VI — Nonmonetary / less-than-full-consideration transactions
Box checked: [ ]  Attached schedule: <property and services each way, FMV estimate> | N/A

## Part VII — Additional information
37. Imports goods from the foreign related party: Yes / No
38a–38c. <if 37 is Yes>
39. Foreign parent in a CSA: Yes / No
40a/40b. §267A disallowed interest or royalty: Yes / No; $
41a–41d. FDII deduction for transactions with this party: Yes / No; $
42a. Loan inside 100%–130% AFR safe-haven range: Yes / No
42b. Loan outside the range: Yes / No
43a/43b. §385 covered debt: Yes / No; $ (not completed by a foreign-owned DE)

## Part VIII — Cost sharing arrangement
N/A | <lines 44–49>

## Part IX — Base erosion payments
50. $  51. $  52. $
Applicable taxpayer under §59A: Yes / No; if No, CPA decision on completing Part IX: <>

## Currency translation
Source: <rates used, by transaction or period>; exchange-rate schedule attached: [ ]

## Required attachments / coordination
- [ ] Attached to Form 1120 (Type 1) | Form 1120-F (Type 2) |
      pro-forma Form 1120 (Type 3)
- [ ] If Type 3: pro-forma 1120 shows name, address, item B (EIN),
      item E, and "Foreign-owned U.S. DE" across the top; nothing else
- [ ] Part V statement, Part VI schedule, Part II attribution
      explanation, exchange-rate schedule (as applicable)
- [ ] Form 8832 election (if relevant) attached separately
- [ ] Transfer-pricing documentation (IRC §6662(e)) — kept with
      taxpayer records, available on IRS request

## Filing channel
| Type | Filing |
|------|--------|
| Type 1 (1120) | E-file with the 1120, or paper per the Instructions for Form 1120 |
| Type 2 (1120-F) | E-file with the 1120-F, or paper per the Instructions for Form 1120-F |
| Type 3 (pro-forma 1120 + 5472) | Not e-fileable. Fax (300 DPI or higher) to 855-887-7737, or mail to Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112 Attn: PIN Unit, Ogden, UT 84201 (Instructions for Form 5472, Rev. December 2024) |

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Cross-form: <reconciliation with 1120/1120-F if applicable>
- Open questions for the user or CPA: <list>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 5472 (Rev. December 2023)
- IRS Instructions for Form 5472 (Rev. December 2024)
- IRC §6038A (information returns by 25%-foreign-owned corps)
- IRC §6038C (foreign corps engaged in US business)
- IRC §6038A(d) ($25,000 penalty per taxable year; Treas. Reg.
  §1.6038A-4(a)(3): per related party)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned DE rules)
- Treas. Reg. §1.6038A-2 (contents of Form 5472; (b)(3)(xi) DE
  transactions; (e)(1) no-reportable-transaction exception)
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
forms and instructions from time to time (re-verify each year).

- [Form 5472 (2026): The $25,000 Mistake Foreign-Owned LLCs Make + AI Agent Skill](https://jupid.com/blog/form-5472-foreign-owned-llc-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 5472 (Rev. December 2023)](https://www.irs.gov/pub/irs-pdf/f5472.pdf) — the form itself (current revision on 2026-10-06)
- [Instructions for Form 5472 (Rev. December 2024)](https://www.irs.gov/pub/irs-pdf/i5472.pdf) — line-by-line IRS guidance; Exceptions from filing; When and Where To File (dedicated fax and mailing address); Penalties
- [About Form 5472](https://www.irs.gov/forms-pubs/about-form-5472) — IRS landing page with archive
- [Form 1120 (latest)](https://www.irs.gov/pub/irs-pdf/f1120.pdf) — required vehicle for Type 1 and Type 3; [Instructions for Form 1120 (2025)](https://www.irs.gov/pub/irs-pdf/i1120.pdf) — When To File, principal business activity codes, foreign-owned domestic DEs
- [Form 1120-F](https://www.irs.gov/forms-pubs/about-form-1120-f) — required vehicle for Type 2
- [Form SS-4](https://www.irs.gov/forms-pubs/about-form-ss-4) — to obtain US EIN for foreign-owned DE; [Instructions for Form SS-4 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/iss4.pdf) — Disregarded entities, Line 10, Apply by telephone / fax / mail
- [Form 7004](https://www.irs.gov/forms-pubs/about-form-7004) — automatic 6-month extension for 1120 and 1120-F
- [Form 8832](https://www.irs.gov/forms-pubs/about-form-8832) — entity classification election
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038C (information returns by foreign corporations engaged in US business)
- IRC §6038A(d) and §6038C(c) — $25,000 penalties; §6038A(d)(2) continuation penalty; §6038A(d)(3) reasonable cause
- IRC §6501(c)(8) — assessment period stays open until 3 years after the information is furnished
- IRC §267(b), §707(b)(1) (related-party definitions)
- IRC §482 (allocation of income among controlled taxpayers)
- IRC §59A (BEAT)
- IRC §6662(e) (transfer-pricing penalty / contemporaneous documentation)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned US DE; T.D. 9796,
  tax years beginning on or after Jan 1, 2017, and ending on or after
  Dec 13, 2017)
- Treas. Reg. §1.6038A-1 through §1.6038A-7 (Form 5472 mechanics);
  §1.6038A-2(b)(3)(xi) (DE formation, contribution, distribution
  transactions), §1.6038A-2(b)(7) (base erosion information from
  applicable taxpayers), §1.6038A-2(e)(1) (no reportable transactions,
  no filing), §1.6038A-3(g) (record retention), §1.6038A-4(a)(3)
  (penalty once per related party per year)
- [IRM 20.1.1.3.3.2.1, First Time Abate](https://www.irs.gov/irm/part20/irm_20-001-001) — lists Form 5472 among returns where FTA does not apply
- [Delinquent international information return submission procedures](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures) — IRS page for late international information returns

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. It does not establish a
CPA-client relationship. The $25,000 penalty per related party per
year makes Form 5472 unforgiving of small mistakes; any user with a
non-trivial cross-border structure (multiple related parties, large
intercompany flows, BEAT exposure) should have a licensed international
tax practitioner (CPA, EA, or attorney) review the draft before filing.
For transfer-pricing-heavy structures, a transfer-pricing economist or
specialist firm is standard.
