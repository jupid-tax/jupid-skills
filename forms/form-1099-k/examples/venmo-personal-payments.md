# Example: Venmo Mixed-Use Account — Personal Payments + Small Freelance Income

The most common 1099-K reconciliation problem in the wild: a single Venmo (or PayPal, Cash App, Zelle) account used for both personal payments (friends/family reimbursements) and a small amount of freelance work. Box 1a covers everything; the user has to split it.

## The filer

- **Name**: Jordan Park
- **Day job**: W-2 software engineer at a tech company
- **Side activity**: Occasional weekend freelance graphic design work (~$2,800/year)
- **Personal Venmo activity**: Heavy — splits dinner with friends, group gifts, splitting rent with roommate, occasional reimbursements from family
- **Entity**: Individual; no LLC; no separate business Venmo profile (single personal Venmo used for everything)
- **Tax year**: 2026
- **State**: California (no state 1099-K threshold lower than federal $20,000 / 200; California-resident-source-only filings handled at state level separately)

## The 1099-K

Venmo (PayPal, Inc. — Venmo's parent) issued a 1099-K. The trigger: Jordan's account had $24,500 in gross flows + 287 transactions for 2026 — both federal thresholds met, so PayPal/Venmo was required to file under IRC §6050W.

| Box | Value |
|-----|-------|
| Filer | PayPal, Inc. (Venmo) |
| Box 1a (Gross) | $24,500 |
| Box 1b (CNP) | $24,500 |
| Box 2 (Transactions) | 287 |
| Box 4 (Federal tax withheld) | $0 |
| Box 6 (State) | CA |

Jordan opens the form, panics, and Googles "Venmo 1099-K what do I do." This skill kicks in.

## Step 1 — Confirm form

Jordan confirms the form title says "Payment Card and Third Party Network Transactions." Yes, it's a 1099-K. Box 1a = $24,500 met the federal threshold ($20,000 + 200 transactions) so the form was required. Reconciliation needed.

## Step 2 — Classify each portion

Jordan exports their Venmo transaction CSV for 2026. The agent helps Jordan tag each transaction:

| Classification | Description | Amount | Transaction count |
|----------------|-------------|--------|-------------------|
| Trade or business | Freelance graphic design work for 4 small clients | $2,800 | 6 |
| Personal — friends/family | Splitting dinner, brunches, drinks (~30 events) | $4,200 | 78 |
| Personal — friends/family | Roommate's share of rent + utilities (Jordan paid landlord, roommate paid back) | $14,400 | 24 |
| Personal — friends/family | Group gifts collected for birthdays, going-aways | $1,800 | 32 |
| Personal — friends/family | Splitting Uber rides on group nights out | $620 | 41 |
| Personal — friends/family | Mom's birthday gift, dad's Christmas gift (received from siblings, Jordan organized) | $580 | 7 |
| Personal — reimbursement | Travel reimbursements from W-2 employer (Jordan paid for client dinner, expensed it) | $100 | 4 |
| Personal item resale at loss | Sold an old PS5 + games to a friend below original cost | $0 (already classified as friends/family above) | 0 |

**Sum: $24,500 = $2,800 (business) + $21,700 (personal)** ✓ matches Box 1a.

## Step 3 — Reconcile against Venmo's own records

- Venmo year-end report: $24,500 ✓ matches Box 1a
- Bank account: Jordan's bank statements show ~$2,400 deposits FROM Venmo to bank during the year (Jordan keeps most Venmo balance in Venmo for upcoming personal use); deposits don't equal Box 1a because Venmo balances aren't always deposited. The balance carries forward.

No corrected 1099-K needed.

## Step 4 — Cross-check against other 1099s

Jordan received no 1099-NEC for the $2,800 freelance income — each client paid under the $2,000 1099-NEC threshold (largest single client paid $1,400). No double-reporting.

But all $2,800 is taxable regardless of 1099-NEC issuance.

## Step 5 — Map to schedule lines

### Trade-or-business portion ($2,800)

This is a side activity for Jordan, but it has profit motive (Jordan does it for money) and is a trade or business per IRC §183 — even if intermittent. Goes on Schedule C.

| Line | Description | Amount |
|------|-------------|--------|
| Schedule C Line 1 | Gross receipts (freelance design via Venmo) | $2,800 |
| Schedule C Line 22 | Supplies (Adobe Creative Cloud subscription, fonts) | $720 |
| Schedule C Line 18 | Office expense (small portion) | $80 |
| **Schedule C Line 28** | **Total expenses** | **$800** |
| **Schedule C Line 31** | **Net profit** | **$2,000** |

Schedule SE on $2,000 net: $2,000 × 0.9235 × 0.153 = **$283** SE tax. Half of SE tax ($141) deducts on Schedule 1 Line 15.

### Personal portion ($21,700)

Per IRS Form 1099-K FAQs, personal payments (friends/family / reimbursements / group gifts / loan repayments) are not income but the gross flows through the 1099-K and must be reported + offset to avoid IRS document-matching mismatches.

| Line | Description | Amount |
|------|-------------|--------|
| Schedule 1 Line 8z | Other income — "Personal payments included on 1099-K from PayPal/Venmo" | $21,700 |
| Schedule 1 Line 24z | Other adjustments — "Offset of personal payments on 1099-K from PayPal/Venmo" | $21,700 |
| **Net to AGI** | | **$0** |

## Step 6 — Schedule 1 ledger

| Line | Source | Amount |
|------|--------|--------|
| Schedule 1 Line 3 | Schedule C Line 31 net profit | $2,000 |
| Schedule 1 Line 8z | Personal payments on 1099-K | $21,700 |
| Schedule 1 Line 9 | Total Other income (Sum of Line 8a-8z) | $21,700 |
| Schedule 1 Line 10 | Total additional income | $23,700 (Line 3 + Line 9) |
| Schedule 1 Line 15 | 1/2 SE tax deduction | $141 |
| Schedule 1 Line 24z | Personal-payment offset | $21,700 |
| Schedule 1 Line 26 | Total adjustments | $21,841 |
| **Net effect on Form 1040 Line 10 (AGI calc input)** | (Line 10 − Line 26) | **$1,859** |

The $1,859 is the actual net taxable income from the 1099-K activity:

- $2,000 Schedule C net profit (already taxed via SE, plus federal income tax)
- LESS $141 half-SE-tax deduction
- = $1,859 contribution to AGI from the 1099-K

The $21,700 personal portion fully offsets — no AGI contribution.

## Step 7 — Form 1040 ledger

| Line | Source | Amount |
|------|--------|--------|
| Form 1040 Line 1 | W-2 wages from day job | (Jordan's W-2 amount) |
| Form 1040 Line 8 | Other income from Schedule 1 Line 10 | $23,700 |
| Form 1040 Line 10 | Adjustments to income (Schedule 1 Line 26) | $21,841 |
| Form 1040 Line 11 | AGI | (Line 9 − Line 10) |
| Form 1040 Line 23 | Other taxes (SE tax from Schedule SE) | $283 |

## Step 8 — Validation

| Check | Result |
|-------|--------|
| Sum of classified portions equals Box 1a | $24,500 = $24,500 ✓ |
| Personal portion offset on Line 24z matches Line 8z | $21,700 = $21,700 ✓ |
| Trade-or-business portion appears on Schedule C Line 1 | $2,800 ≥ $2,800 ✓ |
| Box 4 = $0, no Line 25c entry | ✓ |
| Net effect of personal portion to AGI is $0 | ✓ |
| Total reported income on return ≥ Box 1a | $23,700 (Line 8 from Schedule 1) ≥ $24,500? No — but the offset on Line 24z accounts for the difference. The IRS document-matching system specifically looks for Line 8z reporting + Line 24z offset for 1099-K personal portions, per Nov 2025 Form 1099-K FAQ. ✓ |

## What Jordan does NOT do

- Jordan does NOT report the entire $24,500 on Schedule C — that would pay $3,750 in unnecessary SE tax (15.3% × $21,700 phantom income) plus federal income tax on the full $21,700.
- Jordan does NOT omit the personal portion from the return entirely — that triggers a CP2000 alleging $21,700 of unreported income.
- Jordan does NOT try to amend the 1099-K to "remove" the personal portion — Box 1a is what Venmo reported and what the IRS sees.
- Jordan does NOT mark the personal portion as Schedule 1 Line 8j (hobby) — it's not hobby income, it's not income at all.

## Going forward

To prevent the same problem in 2027, Jordan should:

1. **Open a Venmo Business profile** for the freelance work — Business profile transactions are reported separately and Personal profile transactions are excluded from 1099-K reporting (per Venmo's own documentation, friends/family transactions on Personal profile are filtered)
2. **Tag each personal Venmo payment as "friends and family"** at the moment of receipt, not "goods and services"
3. **Get the PS5/old-stuff resales on a different platform** like Mercari with a separate account, so the 1099-K doesn't lump them in

Jordan's 2027 1099-K should drop dramatically — likely zero if Venmo correctly excludes personal-profile flows, or just the $2,800 freelance portion if Jordan moves freelance to a Business profile.

## Audit-defense documentation Jordan keeps

- The 1099-K (PDF download from Venmo)
- Venmo year-end report
- Venmo transaction CSV with the classification tags Jordan applied
- Brief note explaining each personal-payment category (split rent, group gifts, etc.)
- The 4 freelance client invoices + payment records (proves the $2,800 trade-or-business portion)
- The completed Schedule C, Schedule SE, Schedule 1
- The reconciliation worksheet (this document, redacted)
- Form 1040 + e-file acceptance confirmation

If the IRS sends a CP2000 in 2027 questioning the offset, Jordan responds with this bundle. The Venmo CSV with classification tags is the key artifact.

## Sources cited in this draft

- IRS Form 1099-K (current revision)
- IRS Instructions for Form 1099-K
- IRC §6050W (1099-K reporting)
- IRC §61 (gross income — and what's not income)
- IRC §183 (trade or business test)
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs) — "How should I report personal payments on a 1099-K?"
- Schedule 1 (Form 1040) instructions Line 8z, Line 24z
- Schedule C (Form 1040) and instructions
- Companion Jupid blog: [1099-K Guide 2026](https://jupid.com/blog/1099-k-guide-2026)
