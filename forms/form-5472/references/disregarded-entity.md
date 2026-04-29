# Foreign-Owned US Disregarded Entity (Type 3 Reporting)

The most common Form 5472 scenario, and the one most often missed: a
foreign individual or foreign entity owns 100% of a US single-member LLC
that is a "disregarded entity" (DE) for federal income tax purposes.
Since 2017, these DEs must file Form 5472 + pro-forma 1120 every year.

## The 2017 rule change

**Treas. Reg. §301.7701-2(c)(2)(vi)** (final regs published 2016,
effective for tax years beginning on or after **January 1, 2017**)
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
   without an election to be taxed as a corporation; or a "qualified
   subchapter S subsidiary"; or any other entity treated as a DE under
   Treas. Reg. §301.7701-3.
2. **US** — formed under the laws of a US state or DC.
3. **Foreign-owned** — wholly owned by one foreign person (foreign
   individual, foreign corporation, foreign partnership, foreign trust,
   foreign estate, or foreign government).

Most common pattern: foreign individual owns 100% of a Delaware,
Wyoming, or Nevada LLC. The LLC was formed for US e-commerce, US
real estate holding, US payment processing (PayPal, Stripe, Amazon
seller account), or asset privacy.

## What's required

Every year, regardless of activity:

1. **Pro-forma Form 1120** — see below
2. **Form 5472** — one per related party (typically just the foreign
   owner)
3. **Mailed or faxed** to a specific Ogden address (NOT the standard
   1120 service center; NOT e-fileable)

Filing deadline: **April 15** for calendar-year DEs (15th day of 4th
month after fiscal year-end). Extension via Form 7004 to October 15.

## What the pro-forma 1120 looks like

A "pro-forma" 1120 is mostly blank. The DE has no separate US tax
liability — its income (if any) flows through to the foreign owner who
files Form 1040-NR (individual) or 1120-F (foreign corp) for any US
ECI. The 1120 exists only as a vehicle for the 5472 attachment.

The pro-forma 1120:

- **Top of form**: name, EIN, address, date incorporated, state of
  organization
- **Item B**: check the box for "Foreign-owned US DE" if available, or
  the closest equivalent (the form changes year to year)
- **"FOREIGN-OWNED U.S. DE" notation**: write or type at the top of
  page 1, per Form 5472 instructions
- **Item D**: total assets at year-end (book value)
- **Income lines (1-11)**: all $0 (the DE doesn't have separate
  income for tax purposes)
- **Deduction lines (12-26)**: all $0
- **Tax lines (29-37)**: all $0
- **Schedule M-1**: not required (no income)
- **Schedule M-2**: not required (no retained earnings)
- **Schedule J**: not required (no tax)
- **Signature**: foreign owner signs as "Member" or "Manager" of the
  LLC

Some software packages have specific "pro-forma 1120 for foreign-owned
DE" mode. If using DIY software, manually fill the 1120 with all-zeros
on the income/tax lines.

## What the Form 5472 looks like for a DE

For a typical foreign-owned DE with one foreign owner:

- **Part I** — DE's identification (Type 3 box checked)
- **Part II** — Foreign owner's identification
- **Part III** — Same as Part II (no intermediate; or fill if there's a
  chain, e.g., owner is a foreign trust whose grantor is the human
  beneficiary)
- **Part IV** — May be all zeros if all transactions are captured in
  Part V instead
- **Part V** — Capital contributions, distributions, loans, services
  between DE and foreign owner
- **Parts VI-IX** — N/A unless special circumstances

## Common DE patterns

### E-commerce LLC

Foreign individual forms Delaware LLC to sell on Amazon, Shopify,
eBay. The LLC has Stripe and a US bank account. Inventory is held by
3PL or drop-shipped. Customers are mostly US-based.

- **Income tax**: depends on whether the LLC has a "fixed place of
  business" in the US (a permanent establishment under treaty terms).
  If no PE, no US ECI, no income tax. If PE (e.g., LLC owns a
  warehouse), ECI exists and the foreign owner files 1040-NR or 1120-F.
- **Form 5472**: required regardless; reports the inflows from
  foreign owner (capital contributions to fund inventory) and
  outflows (distributions of profits to foreign owner)

### Real estate holding LLC

Foreign individual forms Delaware/Florida LLC to hold a US rental
property. Rent collects to LLC bank account. Mortgage on the property.

- **Income tax**: the LLC has US-source ECI (rental income from US
  real property). Foreign owner files 1040-NR with Schedule E and
  pays US tax on net rental income (or 30% gross withholding if no
  net election under IRC §871(d)).
- **Form 5472**: required for the LLC. Reports owner contributions
  (down payment funds) and any management fees paid to the foreign
  owner if applicable.

### Holding LLC (no US activity)

Foreign individual forms Wyoming LLC to hold non-US assets (a foreign
brokerage account, foreign real estate, etc.) for asset protection or
privacy. The LLC has no US-source income.

- **Income tax**: foreign owner has no US filing requirement if no
  US-source income.
- **Form 5472**: required for the LLC. Reports the formation
  contribution and any subsequent contributions/distributions.

The "no US activity" pattern is the most-missed scenario. The owner
assumes "I have no US income, I have no US filing." Wrong — the LLC
itself has the 5472 filing duty.

## EIN for a foreign-owned DE

The DE needs a US EIN even with no US income. The owner applies via
Form SS-4. As a foreign owner, the typical path:

1. Complete Form SS-4 with "Foreign-owned U.S. disregarded entity" as
   the "Reason for applying"
2. Apply by phone: **267-941-1099** (IRS International Tax line for
   foreign filers; 6 AM-11 PM ET, Mon-Fri). The IRS issues an EIN on
   the call.
3. Or by fax: **855-215-1627** (US-based; international fax
   different — see SS-4 instructions)
4. Or by mail (slow): IRS, Cincinnati, OH 45999. 4-5 weeks.

The foreign owner does **not** need an SSN or ITIN to obtain the LLC's
EIN. The SS-4 line for "responsible party" can be filled with the
foreign owner's name and a foreign tax ID (or notation if no ID
available).

## Penalty exposure

**$25,000 per Form 5472 not filed, per year**. For a foreign-owned DE
with a single foreign owner, that's $25,000/year if missed.

Continuing $25,000 per 30-day period if not corrected after IRS notice.

Reasonable cause defense possible under §6038A(d)(3) but the IRS is
unforgiving on first-time foreign filers — the typical "I didn't know"
argument usually fails. Stronger arguments:
- Reliance on a US tax practitioner who failed to advise (must show
  full disclosure of facts to the practitioner)
- The DE was formed believing no US tax filing was required and
  promptly filed upon discovery (within months, not years)
- A formation agent / registered agent service represented that
  filing was not required

The First-Time Abate program does NOT apply.

## Practical workflow for a foreign-owned DE

For a foreign individual who just learned about Form 5472:

1. **Year 1** (formation year):
   - Apply for EIN via SS-4 (if not already done at formation)
   - Form 5472: report formation contribution from foreign owner in
     Part V
   - Pro-forma 1120: all zeros except identifying info
   - File via fax (855-887-7737) by April 15 of year following
     formation
2. **Year 2 onwards**:
   - Form 5472: report any contributions, distributions, loans,
     services between DE and foreign owner during the year
   - Pro-forma 1120: all zeros except identifying info
   - File annually
3. **If LLC has US ECI** (e.g., rental real estate):
   - In addition to 5472, foreign owner files 1040-NR or 1120-F for
     personal US tax
   - The 5472 + pro-forma 1120 is the DE's compliance; the 1040-NR
     is the owner's compliance; both are required
4. **If LLC is dissolved**:
   - File final Form 5472 + pro-forma 1120 marked "FINAL RETURN"
   - Distributions on liquidation reported in Part V
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
