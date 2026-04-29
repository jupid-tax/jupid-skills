# Form 8832 Eligibility Reference

Who can and cannot file Form 8832. Walk this checklist before any other workflow step. If the entity is not eligible, Form 8832 cannot be filed regardless of how strong the reasons for wanting to elect.

Source: 26 CFR §301.7701-1, §301.7701-2, §301.7701-3.

---

## The "eligible entity" concept

26 CFR §301.7701-3(a) defines an "eligible entity" as a business entity that is **not** classified as a corporation by §301.7701-2(b). In short, an entity is eligible if it has classification flexibility. Entities that are classified as corporations by definition cannot elect.

---

## Who CAN file Form 8832

### Domestic eligible entities

- **Single-member LLC (SMLLC)** formed under state LLC statute. Default = disregarded. Can elect: association (C-corp).
- **Multi-member LLC** formed under state LLC statute. Default = partnership. Can elect: association (C-corp).
- **Domestic partnership not formed as a corporation**. Default = partnership. Can elect: association.
- **Domestic association** (entity formed under non-corporate state statute that has not previously elected). Default depends on state-law form; if the entity has classification flexibility, it can elect.

### Foreign eligible entities

- **Foreign LLC equivalents** (e.g., UK LLP, Irish LP, certain Cayman entities) that are NOT on the per-se corporation list. Default depends on liability of members per §301.7701-3(b)(2)(i):
  - All members have limited liability → default association (C-corp)
  - At least one member has unlimited liability → default partnership (or disregarded if single owner)
- Foreign entities can elect any of the three classifications: association, partnership, or disregarded (subject to single-vs-multi-owner rules)

---

## Who CANNOT file Form 8832

### Domestic state-law corporations

If the entity was formed as a corporation under state law (filed Articles of Incorporation, designated as "Inc.", "Corp.", "Corporation", "Incorporated", or equivalent), it is **automatically a corporation** under §301.7701-2(b)(1). No election required and no election available — it is permanently classified.

These entities default to C-corporation for federal tax purposes. To become an S-corporation, file Form 2553 (NOT Form 8832).

### Foreign per-se corporations (26 CFR §301.7701-2(b)(8))

Certain foreign entities are classified as corporations by regulation regardless of how they would otherwise be classified. They CANNOT elect down to partnership or disregarded status.

The list is country-specific. Examples (incomplete — verify against the current Treasury regulation):

| Country | Per-se corporation type |
|---------|--------------------------|
| Australia | Public Limited Company |
| Austria | Aktiengesellschaft (AG) |
| Belgium | Société Anonyme (SA) |
| Brazil | Sociedade Anônima |
| Canada | Corporation, Company |
| China | Gufen Youxian Gongsi |
| Czech Republic | Akciová Společnost |
| Denmark | Aktieselskab |
| Finland | Julkinen Osakeyhtiö |
| France | Société Anonyme (SA) |
| Germany | Aktiengesellschaft (AG) |
| Greece | Anonymos Etairia |
| Hong Kong | Public Limited Company |
| Hungary | Részvénytársaság |
| India | Public Limited Company |
| Indonesia | Perseroan Terbuka |
| Ireland | Public Limited Company |
| Israel | Public Limited Company |
| Italy | Società per Azioni (SpA) |
| Japan | Kabushiki Kaisha (KK) |
| Korea (South) | Chusik Hoesa |
| Luxembourg | Société Anonyme (SA) |
| Malaysia | Berhad |
| Mexico | Sociedad Anónima (SA) |
| Netherlands | Naamloze Vennootschap (NV) |
| New Zealand | Limited Company |
| Norway | Allment Aksjeselskap |
| Pakistan | Public Limited Company |
| Peru | Sociedad Anónima |
| Philippines | Stock Corporation |
| Poland | Spółka Akcyjna (SA) |
| Portugal | Sociedade Anônima |
| Russia | Otkrytoye Aktsionernoy Obshchestvo |
| Saudi Arabia | Sharikat Al-Mossahamah |
| Singapore | Public Limited Company |
| South Africa | Public Limited Company |
| Spain | Sociedad Anónima (SA) |
| Sweden | Publika Aktiebolag |
| Switzerland | Aktiengesellschaft (AG) |
| Thailand | Bristat Mahachon Chamkad |
| Turkey | Anonim Şirket |
| Ukraine | Vidkrite Aktsionerne Tovaristvo |
| United Kingdom | Public Limited Company (PLC) |
| Venezuela | Sociedad Anónima |

**Always re-verify the current per-se list at 26 CFR §301.7701-2(b)(8)(i)** before declaring a foreign entity per-se. The list is updated periodically.

If the entity is on the list, the agent must stop and tell the user the entity cannot elect.

### Trusts, estates, REITs, RICs, and statutory exceptions

Per §301.7701-3(a), the following are NOT eligible entities:

- Trusts (governed by §301.7701-4)
- Estates
- Real Estate Investment Trusts (REITs) — IRC §856
- Regulated Investment Companies (RICs) — IRC §851
- Real Estate Mortgage Investment Conduits (REMICs)
- Insurance companies
- State-chartered banks insured by the FDIC
- Joint-stock companies / associations (per §301.7701-2(b)(3)–(7))

If the entity is in any of these categories, Form 8832 is not the right form.

---

## Default classifications without Form 8832

| Entity type | Default classification |
|-------------|------------------------|
| Domestic state-law corporation | C-corporation (Form 1120) |
| Domestic SMLLC | Disregarded (Schedule C if owner is individual; consolidated with parent if owner is corp) |
| Domestic multi-member LLC | Partnership (Form 1065) |
| Foreign entity, all members limited liability | Association (C-corp) |
| Foreign entity, at least one unlimited-liability member | Partnership (or disregarded if single owner) |
| Foreign entity on per-se list | Corporation; cannot elect |
| Domestic GP, LP, LLP, LLLP (multi-member) | Partnership (subject to state-law form) |

---

## The 60-month limitation snapshot

If the entity has filed a Form 8832 within the last 60 months and the prior election was NOT a "newly-formed entity initial classification" election, a new election is generally blocked. See [`sixty-month-rule.md`](./sixty-month-rule.md).

Two exceptions:
- **>50% ownership change**: IRS may waive on showing of more than 50% change in ownership since the prior effective date. Discretionary; requires explanation.
- **First-election exception**: a prior election by a newly-formed entity effective on the date of formation does not count as a "change" — Line 2b on Form 8832.

---

## Eligibility decision tree

```
Is the entity formed as a corporation under state law?
├── Yes → CANNOT elect via Form 8832; entity is a corporation by definition.
│         To become S-corp, file Form 2553.
└── No → Continue

Is the entity a foreign entity on the per-se list (§301.7701-2(b)(8))?
├── Yes → CANNOT elect via Form 8832; entity is a corporation by definition.
└── No → Continue

Is the entity a trust, estate, REIT, RIC, REMIC, insurance company, or
FDIC-insured bank?
├── Yes → CANNOT elect via Form 8832; different rules govern.
└── No → Continue

Has the entity filed a Form 8832 in the last 60 months?
├── No → ELIGIBLE. Proceed to Line 1 box (a) initial classification.
└── Yes → Was that prior election the "newly-formed entity initial
          classification" election (Line 2b)?
          ├── Yes → ELIGIBLE; the prior election does not count.
          │          Proceed to Line 1 box (b) change.
          └── No → 60-month rule blocks unless 50%-ownership-change
                    exception applies. See sixty-month-rule.md.
```

---

## Special cases

### Spouses owning a multi-member LLC in a community-property state

Per Rev. Proc. 2002-69, a "qualified entity" that is an LLC owned solely by spouses in a community-property state can be treated as a single-owner entity (disregarded). If the spouses elect this treatment, Box 6(c) (single-owner disregarded) is available; otherwise Box 6(b) (partnership) is the default.

### Husband-wife unincorporated business in non-community-property state

Without an LLC, this is a qualified joint venture under IRC §761(f) — each spouse files Schedule C as if a sole proprietor. Form 8832 doesn't apply because there's no entity to classify.

### Recently-formed entity with no first-year activity

An eligible entity that has been formed but has not yet started business is still eligible to file Form 8832. The election can be effective on the date of formation if filed within the 75-day window.

### Series LLC

A Series LLC (Delaware, Nevada, etc.) and its protected series are each treated as a separate entity for federal tax classification under proposed regs (Prop. Reg. §301.7701-1(a)(5), 75 Fed. Reg. 55,699 (Sept. 14, 2010)). Each series can have its own classification. If the user is filing Form 8832 for a series LLC, confirm whether they're electing for the master LLC, a specific series, or all of them — each requires a separate Form 8832.

The proposed regulations have not been finalized as of 2026-04-29; verify against the current regulatory status before filing.

### Disregarded entity electing to be regarded for excise tax / employment tax

A SMLLC is regarded for federal employment tax and certain excise tax purposes by default (Reg §301.7701-2(c)(2)(iv) and (v)). This does not change the entity's classification for income tax — it remains disregarded for income tax until Form 8832 elects otherwise. Filers sometimes confuse "regarded for employment tax" with "regarded for income tax"; they are distinct rules.
