# Related Party Rules for Form 5472

Determining who is a "related party" for Form 5472 reporting is the
threshold question after entity classification. The rules combine
**§6038A** (the statutory authority for 5472) with the related-party
definitions in **§267(b)** and **§707(b)(1)**, as modified by the
constructive ownership rules of **§318** with §6038A-specific
modifications.

## The basic rule

For a US C-corp or foreign corp filing Form 5472, "related party" means:

1. **Any 25%+ direct foreign shareholder** of the reporting corporation
2. **Any 25%+ indirect foreign shareholder** through ownership chains
3. **Any other person related to the reporting corporation** under IRC
   §267(b) or §707(b)(1)

For a foreign-owned US DE filing Form 5472, "related party" includes:

1. **The foreign owner** of the DE (always, by definition)
2. **Any other person related to the foreign owner** under §267(b) /
   §707(b)(1)

A separate Form 5472 is filed for each related party. If the DE has
transactions only with its foreign owner, that's one 5472. If the DE
also paid management fees to the foreign owner's brother (related
under §267(b)), that's a second 5472 for the brother.

## §267(b) related parties

IRC §267(b) lists 13 categories of "related persons" for tax purposes.
The categories most relevant for Form 5472:

- **§267(b)(1)** — Members of a family. For an individual: spouse,
  ancestors (parents, grandparents), lineal descendants (children,
  grandchildren), and brothers/sisters (whole or half).
- **§267(b)(2)** — An individual and a corporation more than 50% owned
  (directly or indirectly) by such individual.
- **§267(b)(3)** — Two corporations that are members of the same
  controlled group.
- **§267(b)(4)** — A grantor and a fiduciary of any trust.
- **§267(b)(5)** — A fiduciary of a trust and a fiduciary of another
  trust if the same person is the grantor of both.
- **§267(b)(6)** — A fiduciary of a trust and a beneficiary of such
  trust.
- **§267(b)(7)** — A fiduciary of a trust and a beneficiary of another
  trust if the same person is the grantor of both trusts.
- **§267(b)(8)** — A fiduciary of a trust and a corporation more than
  50% owned by the trust or by the trust's grantor.
- **§267(b)(10)** — A corporation and a partnership if the same persons
  own more than 50% of each.
- **§267(b)(11)** — An S corporation and another S corporation if the
  same persons own more than 50% of each.
- **§267(b)(12)** — An S corporation and a C corporation if the same
  persons own more than 50% of each.

For a typical foreign-owned DE: the DE is owned by a foreign
individual. Related parties include the individual's family members
(spouse, parents, siblings, children) AND any foreign corporation /
partnership / trust the individual controls > 50%.

## §707(b)(1) — Partnership-related parties

Similar to §267(b) but tailored to partnerships:

- **§707(b)(1)(A)** — A partnership and a partner who owns (directly or
  indirectly) more than 50% of the capital or profits interest.
- **§707(b)(1)(B)** — Two partnerships if the same persons own more
  than 50% of each.

## Constructive ownership under §318 (modified by §6038A)

For determining 25%+ ownership, IRC §6038A(c)(5) applies the
constructive ownership rules of §318 with specific modifications. Key
points:

- **Family attribution** — A person is treated as owning stock owned
  by their spouse, children, grandchildren, and parents (but NOT
  siblings under §318, unlike §267(b)(1) which DOES include siblings)
- **Entity attribution** — Stock owned by a corporation is attributed
  to a 50%+ shareholder; stock owned by a partnership is attributed
  proportionally to partners; stock owned by a trust is attributed
  to beneficiaries proportionally to actuarial interest.
- **Modifications under §6038A**:
  - Family attribution applies broader (includes siblings for §6038A)
  - Entity attribution applies broader (lower thresholds in some
    cases)

Practical effect: in determining 25% foreign ownership of a US corp,
you must trace through corporate, partnership, and trust intermediaries
AND through families.

## Examples of related-party identification

### Example A — Simple foreign-owned DE

**Structure**: Hans (German individual) owns 100% of Delaware LLC.

**Related parties**:
- Hans (the foreign owner, always related)
- Hans's wife (family attribution under §267(b)(1))
- Hans's children (family attribution)
- Hans's parents (family attribution)
- Hans's siblings (under §267(b)(1) but not §318 — in 5472, treated as
  related)
- Any corporation Hans owns > 50% (e.g., his German GmbH if any)
- Any trust Hans is grantor or beneficiary of (>50% interest)

**5472s required**: only for related parties with whom the DE actually
transacts. If Hans's wife never transacts with the DE, no 5472 for her
even though she's a related party.

In practice: most DEs file ONE 5472 for the foreign owner, occasionally
ADDITIONAL 5472s if the DE transacted with another family member's
business or another entity in the foreign owner's structure.

### Example B — Two-tier ownership

**Structure**: Italian individual owns 100% of Italian Srl, which owns
100% of Delaware LLC.

**Related parties**:
- Italian individual (ultimate 25%+ foreign shareholder, indirect)
- Italian Srl (direct foreign shareholder, 100%)
- Italian individual's family
- Any other entities owned by Italian individual or Srl

**5472s required**: at least two — one for the Srl (Part III names the
Srl as direct owner), one for the ultimate Italian individual (Part II
names the individual; Part III names the Srl as intermediate). Plus any
sister entities the DE transacted with.

### Example C — US C-corp with foreign parent and foreign sister

**Structure**: German GmbH owns 100% of US C-corp (filing 1120). The
GmbH also owns 100% of a French SAS. The US C-corp paid royalties to
the French SAS during the year.

**Related parties of the US C-corp**:
- German GmbH (25%+ foreign owner, directly)
- German GmbH's ultimate individual owner if any (constructive)
- French SAS (sister-corporation under common control >50%, related
  under §267(b)(3))

**5472s required**: at least two — one for the GmbH, one for the SAS.
The US C-corp's transactions with the SAS are reportable even though
the SAS is not a shareholder of the US C-corp directly; they're
reportable because the SAS is a "related person" under §267(b)(3).

### Example D — Foreign trust as owner

**Structure**: A Cayman trust owns 100% of a Delaware LLC. The trust's
beneficiaries are a US individual and various foreign individuals.

**Related parties of the DE (Delaware LLC)**:
- The Cayman trust (foreign owner, 100%)
- The trustee (related under §267(b) trust rules)
- The grantor (related under §267(b)(4))
- The beneficiaries (related under §267(b)(6) for fiduciary-beneficiary
  relationships)

This pattern gets complex fast. Multiple related parties; multiple
5472s; possible Form 3520 issues for any US beneficiary; possible
1040-NR issues for foreign beneficiaries.

The skill should flag this and recommend a practitioner.

## Indirect ownership tracing

When determining whether a foreign person owns 25%+ of a US C-corp
through intermediaries, trace through:

- **Corporations**: ownership is proportional. If foreign person owns
  60% of foreign holding, and foreign holding owns 50% of US sub, then
  foreign person indirectly owns 30% of US sub (60% × 50%) — meets the
  25% threshold.
- **Partnerships**: same proportional tracing.
- **Trusts**: actuarial interest of beneficiaries; if foreign person
  is the sole beneficiary of a trust that owns 100% of US sub, foreign
  person owns 100% indirectly.

§6038A(c)(5) and the regs at §1.6038A-1(d) specify the ownership
attribution rules. When in doubt, trace conservatively (assume more
attribution rather than less) to ensure the right related parties are
identified.

## What "transactions" trigger 5472 with each related party

For each identified related party, Form 5472 is required only if the
reporting corp had **reportable transactions** with that party during
the year. Categories:

- Sales/purchases of goods or services
- Loans (any change in balance)
- Interest, royalty, rent, license fees
- Capital contributions or distributions (always for Type 3 DEs)
- Cost-sharing arrangements
- Reimbursements
- Other monetary or non-monetary transfers

If the DE never transacted with the foreign owner's brother, no 5472
for the brother — even though he's a related party.

For Type 3 DEs specifically: the formation contribution from the
foreign owner is always a reportable transaction, so Year 1 always
requires a 5472 for the owner. Subsequent years require a 5472 for
the owner if any contributions, distributions, loans, or other
transactions occurred — and the IRS expects Type 3 DEs to file
annually even if Part V is all zeros.

## Documentation to retain

For each related party identified, the user should keep:

- Documentation of the relationship (cap table, ownership chain
  diagram, family tree if relevant)
- Copies of intercompany agreements (loan agreements, service
  agreements, license agreements, distribution agreements)
- Transfer-pricing documentation if the relationship involves
  significant flows (IRC §6662(e))
- Records of all transactions (invoices, wire confirmations, contract
  terms)

The IRS requires these records to be available for examination on
request. Failure to provide records on request triggers a separate
penalty under §6038A(d)(2) and may result in IRS-determined transfer
prices replacing the corp's reported amounts.
