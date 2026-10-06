# Insolvency Worksheet (Pub. 4681)

How to compute the insolvency amount required for §108(a)(1)(B) exclusion. This is the single most error-prone calculation on Form 982 — users underestimate assets and over-claim insolvency.

Pub. 4681 (2025) calls it the "Insolvency Worksheet" (no number) and marks it "Keep for Your Records". It is NOT filed with Form 982. It must be retained with the user's records and made available on IRS request.

---

## The §108(d)(3) definition

> The term "insolvent" means the excess of liabilities over the fair market value of assets. With respect to any discharge, whether or not the taxpayer is insolvent, and the amount by which the taxpayer is insolvent, shall be determined on the basis of the taxpayer's assets and liabilities **immediately before the discharge**.

Two key phrases:
1. **"Immediately before the discharge"** — snapshot AT the moment of discharge, not before / after / averaged.
2. **"Excess of liabilities over fair market value of assets"** — both must be measured. FMV for assets, face amount (typically) for liabilities.

If liabilities ≤ assets: NOT insolvent. Cannot use §108(a)(1)(B).

---

## The general formula

```
Insolvency amount = Total Liabilities − Total FMV of Assets
                    (immediately before the discharge)
```

If positive → user is insolvent by that amount; exclusion = lesser of (canceled debt) or (insolvency amount).
If zero or negative → user is NOT insolvent; cannot use §108(a)(1)(B).

---

## What counts as a LIABILITY

Include EVERY debt, whether or not secured, whether or not in default. Examples (map each to the Pub. 4681 worksheet line in the template below; don't count a liability twice):

| Category | Examples |
|----------|----------|
| Mortgages | Primary residence, vacation home, rental properties |
| Home equity loans / HELOCs | Both balances |
| Credit cards | All cards, all balances (including the canceled debt itself) |
| Student loans | Federal and private |
| Auto loans | Personal and business vehicles |
| Personal loans | Bank, payday, family loans (if real obligations) |
| Business debt | Business loans, lines of credit, business credit cards |
| Tax debt | Federal, state, and local taxes owed (including back taxes, penalties, interest) |
| Judgments | Court-ordered payments owed |
| Medical bills | Outstanding hospital, doctor, dental bills |
| Unpaid utilities | Past-due electric, gas, water, etc. |
| Accrued interest | Interest accrued but not yet paid |
| Co-signed debts | If user is liable, include the full balance |
| Guarantees | Personal guarantees on business or other debt, only IF the user would be required to pay |
| Lawsuits / settlements | If a judgment is anticipated, include estimated amount |

**Important nuance — nonrecourse debt** (Pub. 4681 "Insolvency"). Liabilities include:
- the entire amount of recourse debt;
- nonrecourse debt up to the FMV of the property securing it; and
- nonrecourse debt in excess of that FMV only to the extent the excess is forgiven.

Ask whether each secured debt is recourse (Form 1099-C box 5 checked) or nonrecourse before entering it.

**INCLUDE the canceled debt itself**: The canceled debt is a liability immediately before the discharge. After discharge it goes away; before, it counts. This is a common error users make.

---

## What counts as an ASSET (FMV)

Include EVERY asset the user owns, at fair market value, including assets that secure debt and assets exempt from creditors such as a pension interest or retirement account (Pub. 4681 "Insolvency"; Carlson v. Commissioner, 116 T.C. 87 (2001), held that assets exempt from creditors under state law count). The valuation sources below are practical suggestions, not IRS-prescribed methods:

| Category | Valuation method |
|----------|------------------|
| Cash and cash equivalents | Face value |
| Bank accounts (checking, savings) | Balance |
| Brokerage / investment accounts | Market value |
| Retirement accounts (401(k), IRA, 403(b), etc.) | **Vested balance** at FMV (this is a common omission) |
| Pensions | Present value of accrued benefit (often hard to estimate; use plan statement) |
| Real estate (home, rentals, land) | FMV (Zillow, recent appraisal, comp sales) |
| Vehicles | Kelley Blue Book / NADA value |
| Boats, RVs, motorcycles | KBB / similar |
| Jewelry, watches, art | Appraised value if material |
| Furniture, appliances, electronics | Garage-sale / used market value (NOT replacement cost) |
| Collectibles (coins, stamps, sports cards) | Auction / market value |
| Life insurance cash surrender value | Statement from insurer |
| Business assets (sole prop / partnership share) | FMV |
| Accounts receivable | Net realizable value |
| Intellectual property | If valuable; usually negligible |
| Cryptocurrency | Market value at time of discharge |
| Trust beneficial interests | Present value if currently distributable |

**Common omissions**:
- Retirement accounts (HUGE — many users with $200K+ in 401(k) think they're "broke")
- Life insurance cash value (often $5K-$50K accumulated)
- Vested employer stock options (count if exercisable / valuable)
- Cryptocurrency holdings
- Inheritance interests in active estates

**EXCLUDE**:
- Property you don't own (rented home, leased car)
- Property held in irrevocable trust where the user has no current beneficial interest

**ASK, don't decide alone**: a pension or annuity interest the user says cannot be cashed out, sold, assigned, or borrowed against. The Tax Court held such an interest was not an asset in Schieber v. Commissioner, T.C. Memo. 2017-32, while Pub. 4681 lists pension interests as assets (worksheet line 29). Include it by default and flag it for a CPA.

---

## Joint debt and joint property

If the canceled debt was JOINT (both spouses jointly and severally liable):
- Each may receive a Form 1099-C for the full amount; how much each reports depends on the facts: state law, who received the loan proceeds, who claimed interest deductions, how basis of co-owned property was allocated (Pub. 4681 "Persons who each receive a Form 1099-C showing the full amount of debt")
- Pub. 4681 Example 3 (separate returns): each spouse takes their share of the canceled debt and completes a separate Insolvency Worksheet
- Pub. 4681 gives no rule for combining spouses' assets and liabilities on a joint return. Ask a CPA rather than assuming

If the canceled debt was the user's INDIVIDUAL debt but they hold property jointly with a spouse (e.g., tenancy by the entirety):
- Whether and how much of the joint property counts is not addressed in Pub. 4681; consult a CPA for state-specific application

For non-married joint owners (e.g., siblings co-owning property): include only the user's share at FMV.

---

## Insolvency Worksheet template

Line numbers and labels follow the Pub. 4681 (2025) Insolvency Worksheet. The canceled debt itself goes in its own category (for example line 1 for a credit card). The steps after line 38 are the agent's, not part of the IRS worksheet.

```
Pub. 4681 Insolvency Worksheet (Keep for Your Records)
Date debt was canceled (mm/dd/yy): ____________  (1099-C Box 1)

Part I. Total liabilities immediately before the cancellation
(don't include the same liability in more than one category)
1.  Credit card debt                                               $________
2.  Mortgage(s) on real property (first and second mortgages and
    home equity loans; main home, additional home, investment or
    business property)                                             $________
3.  Car and other vehicle loans                                    $________
4.  Medical bills owed                                             $________
5.  Student loans                                                  $________
6.  Accrued or past-due mortgage interest                          $________
7.  Accrued or past-due real estate taxes                          $________
8.  Accrued or past-due utilities (water, gas, electric, etc.)     $________
9.  Accrued or past-due childcare costs                            $________
10. Federal or state income taxes remaining due (prior tax years)  $________
11. Judgments                                                      $________
12. Business debts (including those owed as a sole proprietor
    or partner)                                                    $________
13. Margin debt on stocks and other debt to purchase or secured
    by investment assets other than real property                  $________
14. Other liabilities (debts) not included above                   $________
15. Total liabilities. Add lines 1 through 14                      $________

Part II. FMV of assets owned immediately before the cancellation
(don't include the FMV of the same asset in more than one category)
16. Cash and bank account balances                                 $________
17. Real property, including the value of land                     $________
18. Cars and other vehicles                                        $________
19. Computers                                                      $________
20. Household goods and furnishings                                $________
21. Tools                                                          $________
22. Jewelry                                                        $________
23. Clothing                                                       $________
24. Books                                                          $________
25. Stocks and bonds                                               $________
26. Investments in coins, stamps, paintings, or other collectibles $________
27. Firearms, sports, photographic, and other hobby equipment      $________
28. Interest in retirement accounts (IRA, 401(k), and other)       $________
29. Interest in a pension plan                                     $________
30. Interest in education accounts                                 $________
31. Cash value of life insurance                                   $________
32. Security deposits with landlords, utilities, and others        $________
33. Interests in partnerships                                      $________
34. Value of investment in a business                              $________
35. Other investments (annuity contracts, guaranteed investment
    contracts, mutual funds, commodity accounts, hedge funds,
    options)                                                       $________
36. Other assets not included above (e.g., cryptocurrency)         $________
37. FMV of total assets. Add lines 16 through 36                   $________

Part III. Insolvency
38. Amount of insolvency. Subtract line 37 from line 15.
    If zero or less, you aren't insolvent.                         $________

Agent steps after the worksheet:
A. Amount of debt canceled (1099-C Box 2, corrected to the actual
   cancellation)                                                   $________
B. Excluded amount = SMALLER of line 38 or line A (Form 982 Line 2) $________
C. Taxable = line A − line B (Schedule 1 Line 8c for nonbusiness
   debt; Schedule C Line 6 for sole-proprietorship debt)           $________
```

---

## Worked example

Sarah has a 1099-C for $24,000 in canceled credit card debt.

**Liabilities immediately before discharge:**
- Mortgage: $185,000
- Credit cards (all, including the canceled $24K): $42,000
- Auto loan: $8,500
- Student loans: $36,000
- Federal tax debt (back taxes): $4,800
- Total liabilities: **$276,300**

**Assets (FMV):**
- Checking + savings: $1,800
- Real estate (home FMV): $215,000
- Vehicle (KBB): $9,200
- Retirement (vested 401(k)): $52,400
- Furniture / electronics (used value): $3,500
- Life insurance cash value: $4,100
- Total assets: **$286,000**

Insolvency = $276,300 − $286,000 = **−$9,700** (NEGATIVE = NOT INSOLVENT)

Sarah cannot use §108(a)(1)(B). The full $24,000 is ordinary income on Schedule 1 Line 8c.

If Sarah had forgotten the retirement account ($52,400), she might have thought she was insolvent. But the rule includes ALL assets including retirement.

---

## Sarah, version 2

Sarah's situation slightly different — large medical bills + smaller retirement:

**Liabilities:**
- Mortgage: $185,000
- Credit cards (incl. canceled): $42,000
- Auto loan: $8,500
- Student loans: $36,000
- Tax debt: $4,800
- Medical bills outstanding: $35,000
- Total: **$311,300**

**Assets:**
- Checking + savings: $1,800
- Real estate: $215,000
- Vehicle: $9,200
- Retirement: $14,000 (smaller balance)
- Furniture etc.: $3,500
- Life insurance: $4,100
- Total: **$247,600**

Insolvency = $311,300 − $247,600 = **$63,700** (insolvent by $63,700)

Excluded amount = lesser of $24,000 (canceled) or $63,700 (insolvency) = **$24,000**

Form 982 Line 2 = $24,000 (entire canceled amount excluded)
Schedule 1 Line 8c = $0

Sarah must then complete Form 982 Part II. If she has NOLs, credit carryovers, or capital loss carryovers, reduce them first (lines 6–9, 12, 13). If her only attribute is the basis of personal-use property, line 10a is the smallest of (a) that basis, (b) $24,000, or (c) the bases of her property plus money held immediately after the cancellation minus liabilities immediately after ($311,300 − $24,000 = $287,300). With $1,800 of cash, (c) is above $0 only if her property bases exceed $285,500; ask for the bases (cost of the home plus improvements, cost of the car) before entering line 10a (i982 "A nonbusiness debt"; §1017(b)(2)).

---

## Common Insolvency Worksheet mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting retirement accounts | Include vested balance at FMV |
| Forgetting life insurance cash value | Include the cash surrender value |
| Using replacement cost for personal property | Use used / garage-sale value |
| Excluding the canceled debt from liabilities | INCLUDE — it was a liability immediately before |
| Using "immediately AFTER" snapshot | Must be IMMEDIATELY BEFORE the discharge |
| Including future obligations (rent, alimony) | Only include CURRENT obligations |
| Joint property with non-liable spouse | Consult Pub. 4681 + state law; refer to a CPA |
| Estimating "I'm broke" without the worksheet | Always do the math; intuition is wrong here |
| Dropping retirement because it's "untouchable" | Pub. 4681 counts exempt assets, including retirement accounts and pension interests; Carlson v. Commissioner, 116 T.C. 87 (2001). A pension interest that can't be cashed out, sold, assigned, or borrowed against was held not an asset in Schieber v. Commissioner, T.C. Memo. 2017-32: include by default and flag for a CPA |
| Excluding home because it's mortgaged | Include FMV of home as asset; mortgage is separate liability |

---

## When in doubt

The agent should:
1. Walk the user through the worksheet line by line
2. ASK for each asset category — don't assume zero
3. Get a pen-and-paper or spreadsheet version the user can verify
4. Recommend a CPA review if insolvency is close to canceled-debt amount (audit risk)
5. Retain the worksheet with the user's records (NOT filed with Form 982 but required if audited)

If the IRS questions the insolvency claim, the worksheet and its statements are the user's support.
