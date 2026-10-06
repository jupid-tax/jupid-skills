# Foreign-Owned US Disregarded Entity (Type 3 Reporting)

The most common Form 5472 scenario, and the one most often missed: a
foreign individual or foreign entity owns 100% of a US single-member LLC
that is a "disregarded entity" (DE) for federal income tax purposes.
Since 2017, these DEs must file Form 5472 + pro-forma 1120 for every
year in which they have a reportable transaction with a related party,
which in practice is most years.

## The 2017 rule change

**Treas. Reg. §301.7701-2(c)(2)(vi)** (T.D. 9796, published December
13, 2016; tax years beginning on or after **January 1, 2017**, and
ending on or after December 13, 2017, per the Instructions for Form
5472)
treats foreign-owned US DEs as **corporations for the limited purpose
of §6038A reporting**. They remain DEs for income tax purposes (income
flows through to the foreign owner; no separate corporate tax) but are
treated as separate entities for Form 5472.

Why the change: before 2017, foreign individuals used Delaware /
Wyoming / Nevada single-member LLCs as anonymous holding vehicles. The
LLCs had no US tax filing requirement (the foreign owner had no US tax
filing if they had no US-source income), so the IRS had no visibility.
Treas. Reg. §301.7701-2(c)(2)(vi) closes that gap by requiring an
annual information return.

## Who is a "foreign-owned US DE"?

All three conditions:

1. **Disregarded entity** under check-the-box rules. Single-member LLC
   without an election to be taxed as a corporation, or any other
   entity disregarded under Treas. Reg. §§301.7701-2 and 301.7701-3.
   (A qualified subchapter S subsidiary cannot be foreign-owned: its
   S corporation parent cannot have a nonresident alien shareholder.)
2. **US** — a domestic entity (formed under the laws of a US state or
   DC).
3. **Foreign-owned** — one foreign person has direct or indirect sole
   ownership (Treas. Reg. §301.7701-2(c)(2)(vi)(A)). "Foreign person"
   covers a nonresident individual, a foreign partnership, company, or
   corporation, a foreign estate or trust, and a foreign government to
   the extent engaged in commercial activity (Instructions for Form
   5472, Definitions).

Most common pattern: foreign individual owns 100% of a Delaware,
Wyoming, or Nevada LLC. The LLC was formed for US e-commerce, US
real estate holding, US payment processing (PayPal, Stripe, Amazon
seller account), or asset privacy.

## What's required

Every year with at least one reportable transaction (Part IV, V, or VI
of Form 5472):

1. **Pro-forma Form 1120** — see below
2. **Form 5472** — one per related party with reportable transactions
   (typically just the foreign owner)
3. **Mailed or faxed** to the dedicated Ogden unit (NOT the standard
   1120 service center; a DE "cannot file Form 5472 electronically")

A year with no reportable transactions at all has no Form 5472
requirement (Instructions for Form 5472, Exceptions from filing, item
1; Treas. Reg. §1.6038A-2(e)(1)). Owner-paid state fees or registered
agent invoices, formation funding, and draws are all reportable, so
confirm a "nothing happened" year line by line.

Filing deadline: the due date (including extensions) of Form 1120,
**April 15** for a calendar-year DE. The DE uses its owner's U.S. tax
year or, if the owner has none, the calendar year (Instructions for
Form 5472, When and Where To File). Extension via Form 7004 to October
15.

## What the pro-forma 1120 looks like

A "pro-forma" 1120 is mostly blank. The DE has no separate US tax
liability — its income (if any) flows through to the foreign owner who
files Form 1040-NR (individual) or 1120-F (foreign corp) for any US
ECI. The 1120 exists only as a vehicle for the 5472 attachment.

"The only information required to be completed on Form 1120 is the
name and address of the foreign-owned U.S. DE and items B and E on the
first page" (Instructions for Form 5472, When and Where To File). On
the 2025 Form 1120:

- **Name and address** of the DE
- **Item B**: the DE's employer identification number
- **Item E**: check (1) Initial return, (2) Final return, (3) Name
  change, or (4) Address change as applicable
- **"Foreign-owned U.S. DE"** written across the top of the Form 1120
- **Everything else** (item C, item D, income, deduction, tax lines,
  schedules): not required; leave blank
- **Signature**: the instructions do not address the signature block.
  ASK the user or CPA; a common practice is for the owner to sign as
  the LLC's member or manager

Commercial software that has no pro forma mode tends to fill zeros or
demand tax computations; prepare the pro forma 1120 on the fillable PDF
instead.

## What the Form 5472 looks like for a DE

For a typical foreign-owned DE with one foreign owner:

- **Part I** — DE's identification (line 3 checked; line 2 checked
  because a foreign person owns 100%)
- **Part II** — Foreign owner on lines 4a–4e; FTIN on 4b(3) or "None";
  reference ID on 4b(2) if the owner has no SSN/ITIN. An ultimate
  indirect owner (for example the individual behind a foreign holding
  company) goes on lines 6a–6e with an attribution statement
- **Part III** — The related party the form covers (usually the foreign
  owner again), "foreign person" checked, line 8e "25% foreign
  shareholder"
- **Part IV** — Monetary transactions such as loans (balances on
  17a/17b or 31a/31b), interest, fees, reimbursements; required when
  Part III "foreign person" is checked
- **Part V** — Checkbox plus attached statement: formation,
  dissolution, contributions, distributions
- **Part VII** — Lines 37–42 answered (a DE does not complete 43a–43b)
- **Parts VI, VIII, IX** — only if the facts call for them

## Common DE patterns

### E-commerce LLC

Foreign individual forms Delaware LLC to sell on Amazon, Shopify,
eBay. The LLC has Stripe and a US bank account. Inventory is held by
3PL or drop-shipped. Customers are mostly US-based.

- **Income tax**: depends on whether the owner has income effectively
  connected with a US trade or business (IRC §864) and, if a treaty
  applies, whether the business profits are attributable to a US
  permanent establishment. That is the owner's question, handled in
  [`form-1040-nr`](../../form-1040-nr/SKILL.md) (individual owner) or
  on Form 1120-F (corporate owner)
- **Form 5472**: required for each year with reportable transactions;
  reports the inflows from the foreign owner (capital contributions to
  fund inventory) and outflows (distributions of profits to foreign
  owner)

### Real estate holding LLC

Foreign individual forms Delaware/Florida LLC to hold a US rental
property. Rent collects to LLC bank account. Mortgage on the property.

- **Income tax**: rent from US real property is US-source income of
  the owner. Without a trade or business it is taxed at 30% of gross;
  the owner can elect under IRC §871(d) to treat it as ECI and pay tax
  on net rental income on Form 1040-NR (see
  [`form-1040-nr`](../../form-1040-nr/SKILL.md)).
- **Form 5472**: required for the LLC. Reports owner contributions
  (down payment funds) and any management fees paid to the foreign
  owner if applicable.

### Holding LLC (no US activity)

Foreign individual forms Wyoming LLC to hold non-US assets (a foreign
brokerage account, foreign real estate, etc.) for asset protection or
privacy. The LLC has no US-source income.

- **Income tax**: foreign owner has no US filing requirement if no
  US-source income.
- **Form 5472**: required for the LLC in each year with a reportable
  transaction. Reports the formation contribution and any subsequent
  contributions/distributions.

The "no US activity" pattern is the most-missed scenario. The owner
assumes "I have no US income, I have no US filing." Wrong — the LLC
itself has the 5472 filing duty whenever money moves between it and
its owner.

## EIN for a foreign-owned DE

The DE needs a US EIN even with no US income. The owner applies via
Form SS-4. As a foreign owner, the typical path:

1. Complete Form SS-4: line 9a "Other" with "Foreign-owned U.S.
   disregarded entity-Form 5472", and line 10 "Other" with
   "Foreign-owned U.S. disregarded entity filing Form 5472"
   (Instructions for Form SS-4, Rev. December 2025)
2. Apply by phone: **267-941-1099** (not toll free; for applicants with
   no legal residence, principal place of business, or principal office
   in the US or US territories; 6:00 a.m. to 11:00 p.m. Eastern,
   Monday through Friday)
3. Or by fax: **855-215-1627** from within the US, **304-707-9471**
   from outside the US (generally within 4 business days)
4. Or by mail: Internal Revenue Service, Attn: EIN International
   Operation, Cincinnati, OH 45999 (EIN by mail in approximately 4
   weeks)

The foreign owner does **not** need an SSN or ITIN to obtain the LLC's
EIN. On line 7b, enter "Foreign" or N/A when the responsible party
does not have and is not eligible for an SSN or ITIN (Instructions for
Form SS-4, Lines 7a–7b). Full walkthrough:
[`form-ss-4`](../../form-ss-4/SKILL.md).

## Penalty exposure

**$25,000 per related party, per year** (IRC §6038A(d)(1); Treas. Reg.
§1.6038A-4(a)(3)). For a foreign-owned DE with a single foreign owner,
that's $25,000/year if missed. A substantially incomplete Form 5472
counts as not filed.

An additional $25,000 per 30-day period (or part) applies if the
failure continues more than 90 days after IRS notice (§6038A(d)(2)).

Reasonable cause defense possible under §6038A(d)(3) and Treas. Reg.
§1.6038A-4(b) (affirmative showing required), but "I didn't know"
alone rarely succeeds. Stronger arguments:
- Reliance on a US tax practitioner who failed to advise (must show
  full disclosure of facts to the practitioner)
- The DE was formed believing no US tax filing was required and
  promptly filed upon discovery (within months, not years)
- A formation agent / registered agent service represented that
  filing was not required

The First-Time Abate program does not apply: IRM 20.1.1.3.3.2.1 lists
Form 5472 among returns where FTA relief is not applicable (it points
to IRM 20.1.9 for an exception; ask the CPA).

## Practical workflow for a foreign-owned DE

For a foreign individual who just learned about Form 5472:

1. **Year 1** (formation year):
   - Apply for EIN via SS-4 (if not already done at formation)
   - Form 5472: check Part V and describe the formation contribution
     from the foreign owner in the attached statement; check line 1j
     (initial year)
   - Pro-forma 1120: name, address, item B, item E (initial return),
     "Foreign-owned U.S. DE" across the top; nothing else
   - File via fax (855-887-7737) or mail (1973 Rulon White Blvd, M/S
     6112 Attn: PIN Unit, Ogden, UT 84201) by April 15 of the year
     following formation
2. **Year 2 onwards**:
   - Form 5472: report any contributions, distributions, loans,
     services between DE and foreign owner during the year
   - Pro-forma 1120: name, address, items B and E only
   - File for every year with a reportable transaction
3. **If LLC has US ECI** (e.g., rental real estate):
   - In addition to 5472, foreign owner files 1040-NR or 1120-F for
     personal US tax
   - The 5472 + pro-forma 1120 is the DE's compliance; the 1040-NR
     is the owner's compliance; both are required
4. **If LLC is dissolved**:
   - File final Form 5472 + pro-forma 1120 with item E(2) "Final
     return" checked
   - Distributions on liquidation described in the Part V statement
   - File state dissolution paperwork separately

## When to consult a practitioner

Always for:
- Multi-tier ownership (DE owned by foreign LLC owned by foreign
  trust owned by foreign individual)
- DE with PE concerns (whether the LLC creates US ECI)
- DE with treaty positions (e.g., asserting treaty residency to
  reduce withholding)
- DE with prior-year filings missed (reasonable cause needed)
- DE involved in transfer pricing (large intercompany flows)

The skill can produce a draft for simple cases (single foreign
individual, single Delaware LLC, simple e-commerce or holding
pattern). For anything more complex, the deliverable should explicitly
say "Have a CPA / EA / international tax attorney review before
filing."
