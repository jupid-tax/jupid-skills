# Related Party Rules for Form 5472

Determining who is a "related party" for Form 5472 reporting is the
threshold question after entity classification. The rules combine
**§6038A** (the statutory authority for 5472) with the related-party
definitions in **§267(b)** and **§707(b)(1)**, as modified by the
constructive ownership rules of **§318** with §6038A-specific
modifications.

## The basic rule

For a US C-corp or foreign corp filing Form 5472, "related party" means
(IRC §6038A(c)(2); Instructions for Form 5472, Definitions):

1. **Any 25%+ direct or indirect foreign shareholder** of the reporting
   corporation
2. **Any person related to the reporting corporation, or to a 25%
   foreign shareholder,** under IRC §267(b) or §707(b)(1)
3. **Any other person related to the reporting corporation** under §482

A corporation filing a consolidated return with the reporting
corporation is not a related party.

For a foreign-owned US DE filing Form 5472, the same definition gives:

1. **The foreign owner** of the DE (always, as its 25% foreign
   shareholder)
2. **Any other person related to the DE or to the foreign owner** under
   §267(b) / §707(b)(1) or §482

A separate Form 5472 is filed for each related party with which the
reporting corporation had a reportable transaction. If the DE has
transactions only with its foreign owner, that's one 5472. If the DE
also paid management fees to the foreign owner's brother (related
under §267(b)(1) and §267(c)(4)), that's a second 5472 for the
brother.

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

For determining 25%+ ownership (and for the related-party definition),
IRC §6038A(c)(5) applies the constructive ownership rules of §318 with
two modifications. Key points:

- **Family attribution** — A person is treated as owning stock owned
  by their spouse, children, grandchildren, and parents (but NOT
  siblings under §318, unlike §267(b)(1)/§267(c)(4), which DO include
  siblings for the related-party test)
- **Entity attribution** — Stock owned by a partnership, estate, or
  trust is attributed proportionally to its partners or beneficiaries;
  stock owned by a corporation is attributed proportionally to a
  shareholder who owns 50% or more of it (§318(a)(2)(C))
- **Modifications under §6038A(c)(5)**:
  - "10 percent" replaces "50 percent" in §318(a)(2)(C): a shareholder
    owning 10% or more of a corporation is treated as owning its
    proportionate share of the stock that corporation owns
  - §318(a)(3)(A), (B), and (C) (attribution to an entity from its
    owners) are not applied so as to treat a US person as owning stock
    owned by a foreign person

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

**How the forms look**: every Form 5472 shows the Srl in Part II lines
4a–4e (direct 25% foreign shareholder) and the Italian individual in
lines 6a–6e (ultimate indirect 25% foreign shareholder), with an
attached explanation of the attribution (Instructions for Form 5472,
Lines 6a–6e and 7a–7e). A separate Form 5472 is filed for each related
party the DE transacted with, named in Part III: the Srl if money moved
between the DE and the Srl, the individual if money moved between the
DE and the individual personally, plus any sister entities the DE
transacted with.

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
- The trustee (a fiduciary of a trust that owns more than 50% of the
  DE, §267(b)(8))
- Possibly the grantor and the beneficiaries, through §318/§267(c)
  attribution of the trust's ownership; this is a practitioner
  question

This pattern gets complex fast. Multiple related parties; multiple
5472s; possible Form 3520 issues for any US beneficiary; possible
1040-NR issues for foreign beneficiaries.

The skill should flag this and recommend a practitioner.

## Indirect ownership tracing

When determining whether a foreign person owns 25%+ of a US C-corp
through intermediaries, trace through:

- **Corporations**: ownership is proportional once the 10% threshold
  of the modified §318(a)(2)(C) is met. If foreign person owns 60% of
  foreign holding, and foreign holding owns 50% of US sub, then foreign
  person indirectly owns 30% of US sub (60% × 50%) — meets the 25%
  threshold.
- **Partnerships**: same proportional tracing.
- **Trusts**: actuarial interest of beneficiaries; if foreign person
  is the sole beneficiary of a trust that owns 100% of US sub, foreign
  person owns 100% indirectly.

§6038A(c)(5) and Treas. Reg. §1.6038A-1 specify the ownership
attribution rules (the instructions point to Rev. Proc. 91-55 and
Treas. Reg. §1.6038A-1(e) for ultimate indirect shareholders). When in doubt, trace conservatively (assume more
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
foreign owner is a reportable transaction (Treas. Reg.
§1.6038A-2(b)(3)(xi)), so Year 1 requires a 5472 for the owner.
Subsequent years require a 5472 for the owner if any contributions,
distributions, loans, owner-paid expenses, or other transactions
occurred. A year with no reportable transactions at all has no filing
requirement (Instructions for Form 5472, Exceptions from filing, item
1); confirm such a year line by line before relying on it.

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
request, kept as long as they may be relevant or material and not less
than the assessment period (Treas. Reg. §1.6038A-3(g)). Failure to
maintain records is itself a $25,000 failure (§6038A(d)(1)(B)), and if
a summons for the records is not complied with, the IRS may determine
the deduction and cost amounts for the related-party transactions in
its sole discretion (§6038A(e)(3)).
