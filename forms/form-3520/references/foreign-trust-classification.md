# Foreign Trust Classification

Whether an entity is a "foreign trust" for US tax purposes is the
threshold question for Form 3520. Misclassification produces a correctly
filed wrong form. This reference walks through the rules and the common
edge cases.

## The two-part test

An entity is a **trust** for US tax purposes if it meets the test in
**Treas. Reg. §301.7701-4(a)**:

> The term "trust" refers to an arrangement created either by a will or
> by an inter vivos declaration whereby trustees take title to property
> for the purpose of protecting or conserving it for the beneficiaries
> under the ordinary rules applied in chancery or probate courts.

In plain language: someone (settlor / grantor) transfers property to a
fiduciary (trustee) who holds it for beneficiaries under fiduciary duty.
The trustee has no economic interest of their own.

A trust is **foreign** if it fails either prong of the **two-part test in
IRC §7701(a)(30)(E) and §7701(a)(31)(B)**:

1. **Court test** — A US court can exercise primary supervision over the
   administration of the trust
2. **Control test** — One or more US persons have authority to control all
   substantial decisions of the trust

If the trust **fails either** test, it is foreign. Both must be passed for
domestic status.

The IRS specifies "substantial decisions" in Treas. Reg. §301.7701-7(d):
distribution timing, beneficiary identification, allocation of receipts to
income or corpus, investment decisions, choice of trustee, choice of
governing law. If any single substantial decision rests with a non-US
person, the trust fails the control test.

## Common entities and how they classify

### Clear foreign trusts

- **Trust formed under foreign law with foreign trustee and foreign
  governing law** — failed both court and control test → foreign trust.
  Example: UK family trust under English law with a UK solicitor as
  trustee.

- **Offshore trust in Bahamas, Cayman, Jersey, Liechtenstein** —
  classic foreign trust. Always a 3520 trigger if the user is the
  grantor or beneficiary.

### Clear NOT-trusts

- **Foreign corporation** — entity-level legal personality, owners hold
  shares not beneficial interests. Use Form 5471 (CFC) reporting instead.
- **Foreign partnership** — pass-through with partner equity. Use Form
  8865.
- **Foreign individual's bank account or brokerage account** — not a
  trust. FBAR + Form 8938 if thresholds met.
- **Mutual fund / ETF in a foreign country** — typically a corporation
  (PFIC); not a trust. Form 8621.

### Hard cases — ASK the user

#### Liechtenstein Stiftung (foundation)

A Liechtenstein **Stiftung** is a hybrid: it has separate legal
personality (like a corporation) but operates with a fiduciary purpose
(like a trust). The IRS often treats family Stiftungen as foreign trusts,
especially when the founder retains beneficiary-like rights. Ask:

- Does the Stiftung have separate legal personality under Liechtenstein
  law? (Yes for Stiftung; this would suggest corporation)
- What is the founder's role? (If the founder retains substantial control
  via "Mandate Agreement" or letter of wishes, IRS may treat as trust)
- Are there beneficiaries with vested or contingent interests? (Yes →
  trust-like)

If the answer leans trust, file Form 3520. If it leans corporation, file
Form 5471 (or 8938 for PFIC). When in doubt, the safer position is to
file BOTH 3520 and 5471 with cross-referencing statements; over-reporting
is not penalized, under-reporting is.

#### Panamanian / Liechtenstein Anstalt

An **Anstalt** is similar to a Stiftung — a hybrid entity. Same analysis.
Often treated as a foreign corporation but can be a trust depending on
governing documents.

#### Mexican Fideicomiso

A **Fideicomiso** is the Mexican equivalent of a trust, used commonly to
hold real estate in restricted zones for foreign buyers. Generally a
foreign trust for US tax purposes. The US person who is the beneficiary
of the Fideicomiso files Form 3520 if the trust holds real estate, even
though the substance feels more like an ownership arrangement.

The IRS issued **Rev. Rul. 2013-14** clarifying treatment of certain
Mexican land trusts (fideicomisos that hold real estate in the restricted
zone for residential use); these may NOT be trusts for US tax purposes if
the beneficiary holds the bundle of ownership rights — but the safe
harbor is narrow. Read the ruling and confirm with the user.

#### Hong Kong / Singapore family office structures

Often involve nested corporations and trusts. Each entity in the chain
needs its own classification. Ask for the org chart.

#### "Foundations" in Panama, Curacao, Netherlands

Same hybrid analysis as Stiftung. Often used for asset protection. Ask
for the founding charter and analyze the substantial decisions.

#### Foreign retirement accounts

Most foreign retirement accounts (UK SIPP, Australian Super, Canadian
RRSP) are **trusts** under §7701. Without a treaty exemption, the US
person owner files Form 3520 and 3520-A annually.

- **Canadian RRSP / RRIF**: Rev. Proc. 2014-55 grants automatic exemption
  from 3520 / 3520-A (the user files only Form 8938 and reports income
  per the US-Canada treaty election on Form 1040). This is a major
  simplification.
- **UK SIPP**: No equivalent exemption. Treated as foreign trust → 3520
  required. Some practitioners argue that "tax-deferred" treatment under
  the US-UK treaty obviates 3520 reporting; the IRS has never explicitly
  agreed. Conservative position: file 3520 + 3520-A.
- **Australian Super**: Similar to UK SIPP. The IRS has not issued
  guidance carving Super out of 3520. Conservative position: file.
- **EU pension plans**: Country-by-country analysis. Some treaties have
  specific carveouts; many do not.

#### Foreign LLCs treated as disregarded entities

A foreign LLC owned 100% by a US person, treated as a disregarded entity
under "check the box" rules, is **not a trust**. The user reports the
LLC's activities directly on their Form 1040. However:

- If the foreign LLC is treated as a corporation (default for many
  foreign entity types under Treas. Reg. §301.7701-3), Form 5471 applies
- If it's a foreign partnership, Form 8865 applies
- If it holds financial accounts, FBAR + 8938 apply

The check-the-box election (Form 8832) determines classification. Ask
the user if they made a CTB election.

#### Trusts established by a foreign person for US beneficiaries

If a foreign grantor (e.g., a parent abroad) established a foreign trust
for the benefit of a US beneficiary, the trust is a **foreign trust** but
the US beneficiary is **not the grantor**. Under §679, US grantor trust
status doesn't apply (the grantor is foreign).

The US beneficiary's Form 3520 obligation arises only when:
- They receive a distribution → Part III
- The grantor dies and the trust converts (special rules)

Until distribution, no 3520 is required from the US beneficiary.

## When in doubt, ask the practitioner

Foreign entity classification is the area most likely to be wrong on a
self-prepared 3520. The skill should:

1. Ask the user for the entity's full legal name, country of formation,
   and a copy of the charter/trust deed if available
2. Walk the §7701 court and control tests with the user
3. If the answer is genuinely unclear (Stiftung, Anstalt, hybrid), advise
   the user to consult an international tax practitioner before filing,
   AND offer to file conservatively (both Form 3520 and Form 5471) with
   cross-references

The cost of over-reporting is duplicate paperwork. The cost of
under-reporting is penalties up to 35% of the asset value or 25% of the
unreported gift.
