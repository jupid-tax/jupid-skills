# Classifying 1099-K Transactions — Business vs Hobby vs Personal

The single most important judgment when reconciling a 1099-K is classifying each portion of Box 1a. Different classifications route to different schedules with materially different tax treatments. Use this decision tree.

---

## Top-level classification

For each transaction (or batch of similar transactions) on the 1099-K, classify as one of:

1. **Trade or business income** → Schedule C
2. **Rental of real property** → Schedule E (or Schedule C if substantial services)
3. **Hobby income** → Schedule 1 Line 8j (no expense deduction, IRC §67(g))
4. **Personal payment received** (gift, friends/family) → entry space at the top of Schedule 1 (not income)
5. **Personal item resale at a loss** → entry space at the top of Schedule 1 (not income; IRS FS-2025-08)
6. **Personal item resale at a gain** → Form 8949 + Schedule D (capital gain)

A single 1099-K may contain multiple classifications — common when the user has a single Venmo or PayPal account used for both freelance work and personal payments.

---

## Trade or business vs hobby (the §183 test)

IRC §183 distinguishes a trade or business (profit motive, regular activity) from a hobby (no profit motive, sporadic activity). The distinction matters because:

- **Trade or business**: full expense deduction on Schedule C; subject to self-employment tax (15.3%) on net profit; can generate a Schedule C loss
- **Hobby**: full income reported on Schedule 1 Line 8j; **no expense deduction** (miscellaneous itemized deductions, including hobby expenses, are disallowed under IRC §67(g); P.L. 119-21 §70110 made the disallowance permanent)

The IRS uses the **9-factor test** (Treasury Regulation §1.183-2(b)) to determine profit motive:

1. Manner in which the activity is carried on (businesslike books and records?)
2. Expertise of the taxpayer or advisors
3. Time and effort expended
4. Expectation that assets will appreciate in value
5. Success in similar or dissimilar activities
6. History of income or losses
7. Amount of occasional profits earned
8. Financial status of the taxpayer
9. Elements of personal pleasure or recreation

**Practical heuristic** for the agent: if the user describes the activity with intent to earn money, regular hours, business-like records, and a separate bank account or accounting tool, classify as trade or business. If the user describes it as "I just sell some old stuff sometimes" or "I do this for fun," lean hobby — and confirm with the user before finalizing.

The **safe harbor**: an activity is presumed to be for-profit if it produced a profit in 3 of the last 5 years (2 of 7 for horse-related activities). Below that threshold, the IRS may challenge the profit motive.

---

## Personal payment received (friends/family)

This is the Venmo / Cash App / Zelle / PayPal Friends scenario. The user receives money from a friend or family member that's a:

- Reimbursement (split dinner, share of rent, group gift)
- Repayment of a loan
- Gift (gift tax, if any, is the giver's concern; the 2026 annual exclusion is $19,000 per recipient, Rev. Proc. 2025-32 §4.42)
- Pass-through (user paid for the group, gets reimbursed)

These are **not income** to the user. They never were. Gifts and reimbursements for shared costs are not payments for goods or services and should not be on a 1099-K at all (FS-2025-08, What to do Q2 and Common situations Q3); when they are, the platform classified them wrong.

### How to report

Per IRS FS-2025-08 (What to do Q4) and the 2025 Form 1040 instructions (Schedule 1, "Form(s) 1099-K"):

1. Ask the filer for a corrected 1099-K. If it won't arrive in time, don't wait to file.
2. Enter the amount included in error in the **entry space at the top of Schedule 1** ("enter the amount reported to you on Form(s) 1099-K that was included in error or for personal items sold at a loss"). Combine amounts from several 1099-Ks into one entry.
3. Report the rest of Box 1a where it belongs (Schedule C, Schedule E, Form 8949). The entry-space amount is not added to income; the return shows the full Box 1a split between that entry and the other destinations.

FS-2025-08 example: a $11,000 1099-K for a roommate's share of rent → enter $11,000 in the entry space at the top of Schedule 1.

### What the user should NOT do

- Don't leave the personal portion off the return entirely — use the entry space so the return accounts for all of Box 1a
- Don't report the personal portion as Schedule C business income — pays unnecessary SE tax (15.3%) on what wasn't income
- Don't try to reduce Box 1a on the input side — Box 1a is what the IRS sees

### Going forward

The user should configure the platform to mark friends/family payments as "personal" (Venmo, PayPal Friends and Family, Cash App personal). Those are typically excluded from future 1099-K reporting because the platform can distinguish.

---

## Personal item resale at a loss

A user sells used personal items (old clothing on Poshmark, used furniture on Mercari, used electronics on eBay) below original cost. Most of these are sold at a loss — the user paid $200 for a chair years ago and sells it for $40 today.

**Personal-item losses are NOT deductible** (IRC §165 limits losses to business / investment / casualty). But the gross sale flowing through the 1099-K still appears.

Per IRS FS-2025-08 (What to do Q6; Common situations Q4, Q7) and the 2025 Form 1040 instructions (Schedule 1, "Form(s) 1099-K"):

- The user does NOT include personal-item-loss sales as income
- Enter the sale amount (the Box 1a amount for that item) in the entry space at the top of Schedule 1, same as personal payments
- Alternative per FS-2025-08 (Common situations Q7): report the loss sale on Form 8949, which carries to Schedule D, instead of using the entry space
- IRS example: couch bought for $1,000, sold for $700 → enter $700 in the entry space

### Documentation the user should keep

- Original purchase receipts for the items (where possible)
- A list of items sold with sale price and original cost
- Platform listing details

If audited, the user shows that each sale was at a loss against original cost. The IRS doesn't require itemized cost basis for low-value personal items, but reasonable records help.

---

## Personal item resale at a gain (Form 8949)

If the user sold a personal item ABOVE its original cost — a collectible, art, jewelry, vintage clothing, sports memorabilia — the gain is taxable as a capital gain (IRC §1221).

- Held more than 1 year: long-term capital gain (preferential rates 0%/15%/20%)
- Held 1 year or less: short-term capital gain (ordinary income rates)
- Collectibles: long-term collectibles gain (max 28% rate, IRC §1(h)(4))

### How to report

Each gain is itemized on Form 8949 Part I (short-term) or Part II (long-term), with:

- Description of property
- Date acquired
- Date sold
- Sales price (from 1099-K)
- Cost basis (original purchase price + any selling costs)
- Adjustment (if any)
- Gain or (loss)

Totals flow to Schedule D, then to Form 1040 Line 7a (2025 form).

### Mixed gains and losses on personal items

A user reselling 50 items, 47 at a loss and 3 at a gain, reports:

- Personal-item-loss portion (sale amounts of the 47): entry space at the top of Schedule 1
- Personal-item-gain portion (3 items individually): Form 8949 + Schedule D

The losses do NOT offset the gains (personal-use property losses aren't deductible). IRS example: couch $1,000 cost sold for $700 plus handbag $800 cost sold for $1,200, Box 1a $1,900 → $700 in the entry space, handbag on Form 8949 and Schedule D ($400 gain).

---

## Rental of real property — Schedule E vs Schedule C

If the 1099-K covers Airbnb / VRBO / Turo or other rental income, the question is whether to use Schedule E (passive rental) or Schedule C (active trade/business).

### Default — Schedule E

Passive rental of real property is reported on Schedule E. Income on Line 3, expenses on Lines 5-19. Net flows to Schedule 1 Line 5.

Most short-term rental hosts file Schedule E — the rental of a property without substantial services (no daily cleaning, no concierge, no meals) is a real estate rental, not a hospitality business. See [`examples/airbnb-host.md`](../examples/airbnb-host.md).

### Schedule C — substantial services exception

If the host provides **substantial services** comparable to a hotel, the activity becomes a trade or business and reports on Schedule C. Substantial services include:

- Daily cleaning between guests (not just turnover cleaning)
- Meals or breakfast
- Concierge services
- Linen changes during the stay
- Transportation services

See Treasury Regulation §1.1402(a)-4 and IRS Pub 527. The bar is genuinely high — most Airbnb hosts don't meet it. The financial impact is significant: Schedule C subjects net profit to SE tax (15.3%), Schedule E doesn't.

---

## Decision flow

```
Is the activity a trade or business (profit motive, regular)?
  Yes → Schedule C
    EXCEPT rental of real property without substantial services → Schedule E
  No (hobby) → Schedule 1 Line 8j (full income, no deduction)

Is the receipt a personal payment (gift, friends/family, reimbursement)?
  Yes → entry space at the top of Schedule 1 (not income)

Is the sale of a personal item?
  At a loss → entry space at the top of Schedule 1 (not income)
  At a gain → Form 8949 + Schedule D

Is the receipt rental income?
  Without substantial services → Schedule E
  With substantial services → Schedule C
```

---

## Sources

- IRC §61 (gross income definition)
- IRC §162 (trade or business expenses)
- IRC §183 (activity not engaged in for profit / hobby loss rules)
- IRC §165 (losses; personal-use property losses not deductible)
- IRC §1221 (capital asset definition)
- IRC §1(h)(4) (collectibles 28% rate)
- IRC §67(g) (miscellaneous itemized deductions disallowed; permanent under P.L. 119-21 §70110)
- Treasury Regulation §1.183-2(b) (9-factor profit motive test)
- Treasury Regulation §1.1402(a)-4 (rental real estate; substantial services)
- [IRS Fact Sheet FS-2025-08, Form 1099-K FAQs](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) (Oct. 23, 2025)
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf), Schedule 1 "Form(s) 1099-K"
- Rev. Proc. 2025-32 §4.42 (2026 gift annual exclusion)
- [Pub 525](https://www.irs.gov/publications/p525) — Taxable and Nontaxable Income
- [Pub 527](https://www.irs.gov/publications/p527) — Residential Rental Property
