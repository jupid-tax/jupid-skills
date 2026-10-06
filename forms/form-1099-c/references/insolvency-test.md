# Insolvency Test — Pub. 4681 Insolvency Worksheet Walkthrough

The insolvency exclusion under **IRC §108(a)(1)(B)** is the most-used exclusion for consumer 1099-Cs. It allows the borrower to exclude canceled debt from income **up to the amount they were insolvent** immediately before the cancellation.

The IRS's tool for the calculation is the **Insolvency Worksheet** in [Publication 4681 (2025)](https://www.irs.gov/publications/p4681), Chapter 1 (Part I liabilities, lines 1–15; Part II assets at FMV, lines 16–37; Part III line 38, amount of insolvency). This file walks through the worksheet step by step, lists what counts on each side, and surfaces the most common errors.

---

## The formula

```
Insolvency = Total liabilities − Total fair market value of assets
             (immediately before the cancellation)
```

If liabilities > assets, the borrower is insolvent by the difference. The exclusion equals **min(canceled debt, insolvency amount)**.

If liabilities ≤ assets, the borrower is not insolvent for §108 purposes and the exclusion does not apply.

**"Immediately before"** means the moment just before the creditor canceled the debt. The canceled debt itself is included in liabilities at its face value (before cancellation).

---

## Step-by-step walkthrough

### Step 1 — Anchor the date

Use Box 1 of the 1099-C. The borrower's financial position is measured **immediately before** that date. If multiple 1099-Cs were issued in the same year, run a separate worksheet for each cancellation, in chronological order — each later cancellation has a smaller insolvency amount because earlier cancellations reduced the borrower's liability stack.

### Step 2 — List all liabilities at face value immediately before cancellation

Liabilities include both legally enforceable debts and contingent liabilities the IRS has accepted as includable.

**Always-includable:**

| Category | Examples |
|----------|----------|
| Credit card balances | Visa, Mastercard, store cards, charge cards |
| Mortgages | Primary mortgage, second mortgage, HELOC outstanding balance |
| Auto loans | Outstanding loan balance (not the car's value — that's an asset) |
| Student loans | Federal and private, all outstanding balances |
| Personal loans | Bank or family/friends with documented loan |
| Medical bills | Outstanding balances owed |
| Tax debt | Federal, state, local, payroll trust fund recovery, with interest and penalties |
| Other consumer debt | Past-due utilities, rent arrears |
| **The canceled debt itself** | At face value before the creditor wrote it off — see below |

**Also listed on the Pub. 4681 worksheet:**

- Court judgments against the borrower (line 11)
- Accrued or past-due mortgage interest, real estate taxes, utilities, childcare costs (lines 6–9)
- Business debts, including as a sole proprietor or partner (line 12); margin debt (line 13)
- Anything else goes on line 14 (other liabilities); for items such as support arrears, ask whether they are legally owed at the measurement date

**Not includable:**

- Liabilities that have already been discharged in a prior bankruptcy
- Debts that have been formally written off by other creditors before the measurement date (those don't exist anymore)
- Future liabilities that haven't yet been incurred (utility bills not yet billed, credit card charges not yet posted)
- Loan guarantees the borrower made for someone else's debt, unless the borrower has been called on to pay (contingent guarantees don't count)

**Critical inclusion: the canceled debt itself.** The most common borrower error is to leave the canceled debt out of the liability column ("it's about to be canceled, so it's not a liability"). **Wrong.** §108 measures insolvency *immediately before* the cancellation. Include the full pre-cancellation balance of the debt that's about to be canceled. If you exclude it, you understate insolvency and may lose part of the exclusion.

### Step 3 — List all assets at fair market value immediately before cancellation

FMV is what the asset would sell for in an arm's-length sale, not the original cost or insurance value.

**Always-includable:**

| Category | FMV source |
|----------|------------|
| Cash | Face |
| Checking and savings accounts | Balance |
| Investment accounts | Account statement at the measurement date |
| Vehicles | Kelley Blue Book private-party value, NADA, or comparable |
| Real estate | Recent appraisal, Zillow estimate as floor, comp sales |
| Business interests | Reasonable valuation; if no market, book value of equity |
| Jewelry, art, collectibles | Appraisal or recent comparable sales |
| Crypto | Spot price at measurement date |

**Always-includable but commonly missed:**

| Category | Why missed | How to value |
|----------|------------|--------------|
| **Retirement accounts** | Borrowers think "they're protected from creditors" → so not assets. **Wrong.** | Account balance at measurement date |
| Cash value of life insurance | Borrowers think "it's insurance, not asset" | Cash surrender value (not face value) |
| Pension interest | Borrowers think it isn't theirs yet | Value of the interest (worksheet line 29) |
| HSA balances | Borrowers think "it's medical, not financial" | Account balance (line 36, other assets) |
| Education accounts (529, Coverdell) | Even though designated for education | Value of the interest (worksheet line 30) |
| Household goods, clothing, tools, books, hobby equipment | Borrowers forget them | Resale value (worksheet lines 19–24, 27) |

### Retirement accounts — the always-asked question

The Pub. 4681 Insolvency Worksheet lists "Interest in retirement accounts (IRA accounts, 401(k) accounts, and other retirement accounts)" (line 28) and "Interest in a pension plan" (line 29) as assets. So retirement accounts (401(k), 403(b), 457(b), Traditional IRA, Roth IRA, SEP-IRA, SIMPLE IRA) **are** assets in the §108 insolvency test, **regardless of state-law creditor protection**.

The reasoning: insolvency under §108 is a federal income-tax concept measuring the borrower's net worth, not a creditor-protection concept. State laws that shield retirement accounts from creditors don't matter for §108. The account balance counts at face.

Borrowers who exclude retirement accounts as assets typically inflate their insolvency by 5- to 6-figures. In an audit, the IRS recomputes insolvency, reduces the exclusion, and the borrower owes back tax + interest + accuracy penalty.

**Document carefully:** include retirement balances at FMV in the asset column. If the user pushes back, point to Pub. 4681 Insolvency Worksheet lines 28–29.

### Step 4 — Compute insolvency

```
Insolvency = Total liabilities (Step 2) − Total assets (Step 3)
```

If positive: that's the insolvency amount. The exclusion is min(insolvency, canceled debt).

If zero or negative: not insolvent. Exclusion does not apply; the canceled debt is income unless another exclusion applies.

### Step 5 — Compute the exclusion

```
Exclusion amount = min(Canceled debt in Box 2, Insolvency amount)
```

If the canceled debt is fully covered, the entire amount is excluded.

If only partially covered, the excluded portion goes on Form 982 Box 1b Line 2; the remaining portion (canceled − insolvency) is reported as income on the appropriate line (Schedule 1 Line 8c for personal debt, Schedule C Line 6 for business debt).

### Step 6 — Document and retain

Prepare the Pub. 4681 Insolvency Worksheet with the line items, totals, and the resulting insolvency amount (line 38). **Keep this worksheet with the borrower's tax records for at least 3 years** (the general period of limitations) and 6 years if income omitted is more than 25% of the gross income shown (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records). The worksheet is **not** filed with the return; it's the audit defense if the IRS questions the exclusion.

---

## Worked example

Borrower: Carlos. Box 1 date: 2025-08-15. Box 2 amount: $22,000 (credit card settled).

**Liabilities immediately before 2025-08-15:**

| Item | Amount |
|------|--------|
| Credit card being canceled (full $35,000 balance pre-settlement) | $35,000 |
| Other credit cards | $14,000 |
| Auto loan | $18,000 |
| Federal student loan | $32,000 |
| Outstanding medical bill | $4,500 |
| Mortgage | $185,000 |
| **Total liabilities** | **$288,500** |

**Assets immediately before 2025-08-15:**

| Item | FMV |
|------|-----|
| Checking + savings | $3,200 |
| Brokerage account | $8,500 |
| 401(k) balance | $58,000 |
| Roth IRA | $12,300 |
| Car (KBB private-party) | $14,000 |
| Home (Zillow + comps) | $210,000 |
| **Total assets** | **$306,000** |

**Insolvency = $288,500 − $306,000 = −$17,500**

Carlos is **not** insolvent. The §108(a)(1)(B) exclusion does not apply. He must look at other exclusions or report the $22,000 as income on Schedule 1 Line 8c.

If Carlos's home FMV had been $180,000 instead of $210,000, his assets would total $276,000, his insolvency would be $12,500, and his exclusion would be **min($22,000, $12,500) = $12,500**. He would exclude $12,500 via Form 982 Box 1b and report the remaining $9,500 on Schedule 1 Line 8c.

---

## Common errors

1. **Excluding retirement accounts as assets** — overstates insolvency. Include them.
2. **Excluding the canceled debt from liabilities** — understates liabilities. Include the pre-cancellation face value.
3. **Using purchase price instead of FMV for assets** — vehicle and home FMV may be much less than purchase price; use current FMV.
4. **Using account balance instead of FMV for collectibles** — there's no "balance" for jewelry; use a defensible appraisal or comp sales.
5. **Using post-cancellation balances for liabilities** — measure *immediately before* the cancellation, not after.
6. **Mixing measurement dates with multiple 1099-Cs** — each cancellation gets its own measurement date; chronological order matters.
7. **Mishandling a joint debt between spouses** — Pub. 4681 Insolvency Example 3 has each spouse (filing separately) compute insolvency for their own share of the canceled joint debt with their own assets and liabilities. For a joint return, flag the measurement method for a CPA rather than assuming household totals.
8. **Using Zillow estimate as ceiling** — Zillow is a starting point, not an authoritative number. Use comp sales or appraisal if Zillow looks high; document the basis.

---

## Edge cases

### Joint filers

Pub. 4681 (Insolvency, Example 3) shows spouses who file separately each running the worksheet for their own share of a joint canceled debt, using their own liabilities and assets. Pub. 4681 has no joint-return example; do not assume combined household totals without a CPA's review, and document the method used.

### Community property states

In community property states, the rules are more complex. Generally, community debts and community assets count for both spouses. Consult Pub 555 (Community Property) and Pub 4681 if the borrower lives in AZ, CA, ID, LA, NV, NM, TX, WA, or WI and the canceled debt is community.

### Multiple cancellations in the same year

Run the Insolvency Worksheet separately for each cancellation, in chronological order. After cancellation #1, the borrower's liability stack drops by the canceled amount, so cancellation #2's insolvency calculation is smaller. Excluding the same insolvency amount twice for two separate cancellations is the most common multi-1099-C error.

### Asset values that change rapidly

If the borrower owns volatile assets (crypto, growth stocks), use the value on the actual measurement date — not a daily average, not the prior month's value. A spreadsheet of measurement-date prices is acceptable evidence.

---

## Sources

- [Publication 4681 (2025)](https://www.irs.gov/publications/p4681) — Insolvency Worksheet in Chapter 1 (lines 1–38); Example 3 (joint debt, separate returns)
- IRC §108(a)(1)(B) — insolvency exclusion; §108(a)(3) — limited to the amount of insolvency
- IRC §108(d)(3) — definition of insolvency
- Treas. Reg. §1.108-1 — implementation rules
- Pub 555 — Community Property (for community-property-state issues)
