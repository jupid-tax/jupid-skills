# Insolvency Worksheet (Pub 4681 Worksheet 2)

How to compute the insolvency amount required for §108(a)(1)(B) exclusion. This is the single most error-prone calculation on Form 982 — users underestimate assets and over-claim insolvency.

The Worksheet 2 itself is NOT filed with Form 982. It must be retained with the user's records and made available on IRS request.

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

Include EVERY debt, whether or not secured, whether or not in default. The full list per Pub 4681:

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

**Important nuance — non-recourse debt**: For non-recourse debt, the IRS position (per Pub 4681 and Rev. Rul. 92-53) is that the debt is included in liabilities at the FMV of the secured property — but ONLY if the discharge is of the same non-recourse debt. The full mechanics are subtle; for personal-use property in a typical 1099-C scenario, include the full face amount.

**INCLUDE the canceled debt itself**: The canceled debt is a liability immediately before the discharge. After discharge it goes away; before, it counts. This is a common error users make.

---

## What counts as an ASSET (FMV)

Include EVERY asset the user owns, at fair market value. The full list per Pub 4681:

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

**Common omissions** (each has caused IRS audit disputes):
- Retirement accounts (HUGE — many users with $200K+ in 401(k) think they're "broke")
- Life insurance cash value (often $5K-$50K accumulated)
- Vested employer stock options (count if exercisable / valuable)
- Cryptocurrency holdings
- Inheritance interests in active estates

**EXCLUDE**:
- Property you don't own (rented home, leased car)
- Joint property where only one spouse is liable for the canceled debt — see "tenancy by entirety" rules below
- Property held in irrevocable trust where the user has no current beneficial interest

---

## Joint debt and joint property

If the canceled debt was JOINT (both spouses liable):
- Each spouse's insolvency is computed separately if filing separately
- If filing jointly, generally aggregate assets and liabilities

If the canceled debt was the user's INDIVIDUAL debt but they hold property jointly with a spouse (e.g., tenancy by entirety):
- Special rules apply; some states protect joint property from individual creditors
- See Pub 4681 examples; consult a CPA for state-specific application

For non-married joint owners (e.g., siblings co-owning property): include only the user's share at FMV.

---

## Worksheet 2 template

```
Pub 4681 Worksheet 2 — Insolvency
Filer: ________________________
Date of debt discharge (1099-C Box 1): ____________
"Immediately before" date: ____________ (same as Box 1 for snapshot)

LIABILITIES IMMEDIATELY BEFORE DISCHARGE:
1. Mortgage(s) on primary residence              $________
2. Mortgage(s) / loans on other real estate      $________
3. Home equity loans / HELOCs                    $________
4. Credit card balances (all cards)              $________
5. Student loans (federal + private)             $________
6. Auto loans                                    $________
7. Personal loans (bank, family, etc.)           $________
8. Business loans / lines of credit              $________
9. Business credit cards                         $________
10. Tax debt (federal / state / local)           $________
11. Judgments                                    $________
12. Medical bills outstanding                    $________
13. Past-due utilities / other consumer          $________
14. The canceled debt itself (per 1099-C Box 2)  $________
15. Other liabilities (specify): _______________ $________
16. **TOTAL LIABILITIES**                        $________

ASSETS (FMV) IMMEDIATELY BEFORE DISCHARGE:
17. Cash on hand                                 $________
18. Checking / savings account balances           $________
19. Money market / CDs                           $________
20. Investment / brokerage accounts (FMV)        $________
21. Retirement accounts (401(k), IRA — vested)   $________
22. Pension benefits (present value)             $________
23. Real estate (FMV of home + others)           $________
24. Vehicles (KBB / NADA)                        $________
25. Boats / RVs / motorcycles                    $________
26. Jewelry / watches / art (if material)        $________
27. Furniture / appliances (used value)          $________
28. Collectibles / antiques                      $________
29. Life insurance cash value                    $________
30. Business assets (sole prop, partnership)     $________
31. Cryptocurrency / digital assets              $________
32. Other assets (specify): ___________________ $________
33. **TOTAL ASSETS**                             $________

INSOLVENCY:
34. Insolvency = Line 16 − Line 33               $________
   (If zero or negative: NOT insolvent; cannot exclude under §108(a)(1)(B))

CANCELED DEBT (FROM 1099-C):
35. Amount of debt canceled (1099-C Box 2)       $________

EXCLUSION:
36. Excluded amount = LESSER of Line 34 or Line 35  $________
    (This is Form 982 Line 2)

INCLUDED IN INCOME:
37. Schedule 1 Line 8c amount = Line 35 − Line 36   $________
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

Sarah must then reduce tax attributes per §108(b) for the $24,000 (Form 982 Part II Lines 5-11).

---

## Common Worksheet 2 mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting retirement accounts | Include vested balance at FMV |
| Forgetting life insurance cash value | Include the cash surrender value |
| Using replacement cost for personal property | Use used / garage-sale value |
| Excluding the canceled debt from liabilities | INCLUDE — it was a liability immediately before |
| Using "immediately AFTER" snapshot | Must be IMMEDIATELY BEFORE the discharge |
| Including future obligations (rent, alimony) | Only include CURRENT obligations |
| Joint property with non-liable spouse | Consult Pub 4681 + state law |
| Estimating "I'm broke" without the worksheet | Always do the math; intuition is wrong here |
| Dropping retirement because it's "untouchable" | §108(d)(3) doesn't have a "touchability" test — include it |
| Excluding home because it's mortgaged | Include FMV of home as asset; mortgage is separate liability |

---

## When in doubt

The agent should:
1. Walk the user through the worksheet line by line
2. ASK for each asset category — don't assume zero
3. Get a pen-and-paper or spreadsheet version the user can verify
4. Recommend a CPA review if insolvency is close to canceled-debt amount (audit risk)
5. Retain the worksheet with the user's records (NOT filed with Form 982 but required if audited)

The IRS frequently disputes insolvency claims, especially for users with substantial retirement balances. The worksheet is the user's defense.
