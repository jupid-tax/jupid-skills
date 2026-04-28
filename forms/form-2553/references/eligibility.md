# Eligibility for S-Corporation Status (IRC §1361)

The S-corp election is governed by IRC §1361(b). Every requirement must be met **at the moment of the election effective date and continuously thereafter**. Any single failure voids the election retroactive to the moment of failure, and the entity reverts to C-corp taxation (for corporations) or partnership / sole prop taxation (for LLCs).

This file is the eligibility checklist. Run all six categories before drafting Form 2553.

---

## 1. Entity type

✅ **Eligible**

- Domestic corporation (Inc., Corp.) — formed under U.S. state law
- Domestic LLC — formed under U.S. state law, electing to be taxed as a corporation either via Form 8832 or via the combined-filing path of Rev. Proc. 2013-30 (Form 2553 alone)

❌ **Ineligible**

- Foreign corporations (formed outside the U.S.)
- Sole proprietorships (no entity exists; the owner files Schedule C)
- General or limited partnerships (no entity election possible)
- Multi-member LLCs that haven't elected corporate taxation (taxed as partnership by default)
- Trusts (with narrow exceptions for grantor and qualified trusts holding S-corp stock)

For LLCs: you can skip Form 8832 and file Form 2553 alone. The IRS treats this as a deemed election to corporate status combined with the S-corp election (Rev. Proc. 2013-30). This is the standard path for LLCs electing S-corp.

---

## 2. Ineligible corporation classes

Even an otherwise-qualifying domestic corporation cannot elect S-corp status if it is in any of these classes (IRC §1361(b)(2)):

| Class | Description | Code reference |
|-------|-------------|----------------|
| Bank using reserve method | Banks computing bad-debt reserve under §585 | §1361(b)(2)(A) |
| Insurance company | Subject to Subchapter L | §1361(b)(2)(B) |
| Possessions corporation | Claiming the §936 Puerto Rico / possessions credit | §1361(b)(2)(C) |
| DISC / former DISC | Domestic International Sales Corporation | §1361(b)(2)(D) |

Most small business filers do not fall in any of these classes. Confirm before proceeding only if the user is in finance, insurance, or international sales.

---

## 3. Shareholder count

✅ **≤100 shareholders** at the moment of election and continuously after.

**Aggregation rules** (these reduce the count):

- **Spouses count as one shareholder.** Their estates also count as one with the surviving spouse.
- **Family aggregation** (IRC §1361(c)(1)): all members of a family (six generations from a common ancestor, plus their spouses and estates) can elect to be treated as one shareholder. This is permissive — the family can elect to count as one or as separate.

For most small businesses, the count is far below 100. The 100-cap is rarely the binding constraint.

---

## 4. Shareholder type (the most-violated rule)

Every shareholder, on the effective date and continuously, must be in one of these eligible classes (IRC §1361(b)(1)(B)):

✅ **Eligible shareholders**

| Type | Notes |
|------|-------|
| U.S. citizen (individual) | Always eligible |
| Resident alien (individual) | Eligible — must be a U.S. tax resident; ITIN-holders qualify |
| Estate of a deceased shareholder | Eligible during administration |
| Bankruptcy estate of an individual shareholder | Eligible |
| Grantor trust | Eligible — the grantor is treated as the deemed shareholder |
| Voting trust | Eligible if it meets §1361(c)(2)(A)(iv) requirements |
| Qualified Subchapter S Trust (QSST) | Eligible — must elect under §1361(d); see Part III of Form 2553 |
| Electing Small Business Trust (ESBT) | Eligible — must elect under §1361(e) by separate filing |
| Tax-exempt §501(c)(3) | Eligible — but the S-corp dividends become UBTI |
| Qualified retirement plan trust under §401(a) | Eligible (narrowly) |

❌ **Ineligible shareholders** (any one of these voids the election)

| Type | Notes |
|------|-------|
| C corporation | A C-corp cannot own S-corp stock |
| Partnership | A partnership cannot own S-corp stock |
| Multi-member LLC | Same as partnership — ineligible |
| Non-resident alien | Most common cause of voided elections; ITIN alone is not enough — must be U.S. tax resident |
| Most foreign trusts | Beneficiaries of foreign trusts cannot indirectly hold S-corp stock |
| IRA (with narrow §1361(c)(2)(A)(vi) bank exception) | Almost always ineligible for non-bank S-corps |
| Most non-§501(c)(3) tax-exempt orgs | Generally ineligible |

**Critical for LLCs**: a multi-member LLC cannot itself be a shareholder of an S-corp. If the user has a holding LLC that owns shares of an operating LLC, and they want the operating LLC to be S-corp, the holding LLC must be a single-member LLC (treated as disregarded entity owned by the single eligible shareholder) OR the holding structure must be unwound.

---

## 5. One class of stock (Reg. §1.1361-1(l))

✅ **Eligible**: All outstanding shares confer **identical rights to distributions and liquidation proceeds**.

**Voting differences are allowed.** Voting common and non-voting common are treated as one class for §1361 purposes, even though they have different voting rights.

❌ **Disqualifying**:

- Preferred stock (any class with priority distribution or liquidation rights)
- "Tracking stock" tied to subsidiary performance
- Convertible debt that the IRS recharacterizes as a second class of equity (test: §1361(c)(5) safe harbor — straight debt with fixed interest, fixed maturity, no contingent features)
- Side agreements granting one shareholder priority in distributions
- Disproportionate distributions made in practice (even with single-class stock on paper)

### LLC-specific concern: the operating agreement

This is where most LLC elections fail. Off-the-shelf operating agreements often include:

- **Waterfall distributions**: Investors get returns first, then management catches up, then pro-rata. **Violates one-class-of-stock.**
- **Preferred returns**: Class A members get 8% before Class B receives anything. **Violates one-class-of-stock.**
- **Catch-up provisions**: Same problem.
- **Targeted capital accounts**: Often violates because it adjusts liquidation rights based on performance.

**Before filing Form 2553 for an LLC**: review the operating agreement for any of the above. If found, the operating agreement must be amended to provide pro-rata economic rights, and that amendment must be effective on or before the election effective date. Otherwise the election is void from day one.

A clean S-corp-eligible LLC operating agreement says, in substance:

> "All distributions of cash or property shall be made to Members in proportion to their Percentage Interests. Upon liquidation, after payment of debts and obligations, remaining assets shall be distributed to Members in proportion to their Percentage Interests."

No preferred returns, no waterfalls, no priorities.

---

## 6. State and entity-formation timing

✅ Entity must be **legally formed** under state law before the effective date on Line F.

For new entities: Line F (effective date) cannot be earlier than the date the state accepted the formation filing (Line D — date incorporated).

For existing entities: the entity must have been continuously formed and in good standing.

If state administrative dissolution has occurred (failure to file annual reports, etc.), the entity must reinstate before electing S-corp.

---

## Quick pass/fail checklist

Run this at the start of every Form 2553 engagement. Any "no" stops the election.

```
□ Domestic corporation OR domestic LLC formed under U.S. state law
□ Not a bank using reserve method, insurance co. under Subchapter L,
  §936 possessions corp, or DISC
□ ≤100 shareholders (with spouse / family aggregation)
□ All shareholders are U.S. citizens, resident aliens, eligible trusts,
  estates, or qualifying tax-exempt orgs
□ NO shareholders are: C-corps, partnerships, multi-member LLCs,
  non-resident aliens, most foreign trusts, or IRAs
□ One class of stock confirmed (operating agreement reviewed for LLCs:
  no waterfalls, no preferred returns, pro-rata economic rights)
□ Entity is legally formed and in good standing as of effective date
□ EIN obtained
```

---

## What happens if eligibility is lost mid-year

If the entity loses eligibility after the election (e.g., a shareholder transfers stock to a non-resident alien, or the company issues preferred stock), the S-corp election **terminates automatically** as of the date of the disqualifying event (IRC §1362(d)(2)). The entity must:

1. File two short-period returns: Form 1120-S for the S-corp portion of the year and Form 1120 (C-corp) for the C-corp portion
2. The shareholders may not re-elect S-corp status for **5 years** without IRS consent (IRC §1362(g))

This is a serious consequence. Eligibility must be monitored continuously, especially around stock transfers, marriage/divorce, immigration status changes, and operating-agreement amendments.

---

## Cross-references

- Line-by-line form mechanics: [`line-by-line.md`](./line-by-line.md)
- Deadline calculation and late relief: [`timing-rules.md`](./timing-rules.md)
- Operating agreement red flags (one class of stock for LLCs): [`common-mistakes.md`](./common-mistakes.md)
- Authority sources: IRC §1361, Reg. §1.1361-1, Rev. Proc. 2013-30
