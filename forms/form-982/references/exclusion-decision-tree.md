# §108(a) Exclusion Decision Tree

How to determine which exclusion (if any) applies to the user's canceled debt. Walk through the tests in order — the first one that fits is the exclusion to claim.

The key principle: §108(a)(2) gives bankruptcy priority over all other exclusions. Other exclusions follow conditional priorities described below.

---

## Step 1 — Bankruptcy test (Box 1a)

Ask:
1. Did the user file a bankruptcy petition under Title 11 of the US Code?
2. Did the bankruptcy court grant a DISCHARGE of the debt?
3. Did the discharge occur while the user was IN the bankruptcy proceeding?

If all three: **Box 1a, §108(a)(1)(A)**. STOP. Use bankruptcy exclusively.

The bankruptcy exclusion is the broadest:
- No insolvency requirement (could be solvent and still qualify)
- No cap on excluded amount
- All Title 11 chapters qualify (Chapter 7, 11, 12, 13)
- Court-ordered discharge is the trigger, not the petition filing

Documentation: bankruptcy case number, chapter, date filed, date of discharge order. The discharge order itself should be retained (NOT filed with Form 982).

If user is "in bankruptcy" but the debt was canceled by the creditor BEFORE the petition or AFTER dismissal — Box 1a does NOT apply. Try insolvency.

---

## Step 2 — Qualified principal residence test (Box 1e)

This step comes BEFORE insolvency under §108(a)(2)(C), unless the user elects insolvency instead.

Ask:
1. Was the property the user's PRINCIPAL residence at the time of the discharge?
2. Was the debt acquisition indebtedness (used to BUY, BUILD, or substantially IMPROVE the residence)?
3. Was the debt secured by the residence?
4. Is the qualified principal residence exclusion in effect for the tax year?

Verify item 4 against current legislation:
- Original §108(a)(1)(E) was for discharges 2007-2017
- Multiple extensions: through 2018, 2020, 2021, 2025
- For tax year 2025: in effect (per Inflation Reduction Act + later extensions)
- For tax year 2026+: VERIFY — the most recent extension may have lapsed

If all four: **Box 1e, §108(a)(1)(E)**. Use principal residence exclusion.

Cap: $750K of qualified principal residence indebtedness ($375K MFS) — IRC §108(h)(2). Pre-2018 cap was $2M for many years.

If discharged amount exceeds the cap: only the first $750K is excludable; the excess goes to insolvency or income.

After exclusion: reduce basis of the residence by the excluded amount under §108(h)(1). NOT through Form 982 Part II — recorded in user's home-basis records for future §121 / sale calculation.

User can ELECT insolvency instead of principal residence exclusion if insolvency is bigger or otherwise more advantageous (§108(a)(2)(C)). The election is on a per-discharge basis.

If property was a vacation home, rental, or investment — NOT principal residence. Skip to Step 4.

---

## Step 3 — Insolvency test (Box 1b)

Ask:
1. Was the user insolvent IMMEDIATELY BEFORE the discharge?
2. Insolvency = total liabilities > FMV of total assets (using ALL assets and liabilities, including retirement, including non-recourse debt at FMV).

Use Pub 4681 Worksheet 2 to compute. See [`insolvency-worksheet.md`](./insolvency-worksheet.md).

If user is insolvent: **Box 1b, §108(a)(1)(B)**. Use insolvency exclusion.

Cap: lesser of (canceled debt amount) or (insolvency amount). If user was $20K insolvent and had $30K of debt forgiven, only $20K is excludable; $10K is ordinary income on Schedule 1 Line 8c.

If user is solvent (assets > liabilities), insolvency does NOT apply. Skip to Step 4.

Common confusion: "I have no money in the bank, I'm insolvent." The §108 insolvency test uses ALL assets, including the home, cars, and retirement accounts. A user with $200K in a 401(k) and $60K of credit card debt is NOT insolvent — they have $140K of net worth.

---

## Step 4 — Qualified farm indebtedness test (Box 1c)

Uncommon for general agent use. Ask only if:
1. The debt was incurred in the operation of a farm
2. ≥ 50% of the user's aggregate gross receipts for the prior 3 years came from farming
3. The lender is unrelated (not family, not a controlled entity)

If yes: **Box 1c, §108(a)(1)(C)**. Use farm exclusion.

Cap: complex; see §108(g). Generally limited to aggregate adjusted bases of qualified farm property + tax attributes available for reduction.

This skill primarily targets individual / solo filers. Most won't qualify under (C). If user is a farmer, refer to a CPA.

---

## Step 5 — Qualified real property business indebtedness test (Box 1d)

NON-corporate taxpayers with debt secured by REAL property used in a trade or business.

Ask:
1. Is the user non-corporate (individual, partnership, S-corp shareholder)?
2. Is the debt secured by real property used in a trade or business (NOT personal-use, NOT investment-only)?
3. Was the debt incurred or assumed BEFORE January 1, 1993, OR incurred to acquire/construct/substantially improve such property?
4. Is the user willing to make the §108(c) election?

If yes to all: **Box 1d, §108(c)**. Use QRPBI election.

Cap: lesser of (excess of debt over FMV of property, before discharge) or (basis of depreciable real property used in the business).

After exclusion: reduce basis of the depreciable real property by the excluded amount.

The QRPBI election is irrevocable. Make it deliberately.

QRPBI is somewhat rare. Most real-estate business owners are better off with insolvency or bankruptcy if those apply. Use QRPBI when the user is solvent and not in bankruptcy but has real-estate business debt to discharge.

---

## Step 6 — No exclusion applies

If none of Steps 1-5 fits: there is NO §108 exclusion. The full discharged amount is ordinary income on Schedule 1 Line 8c.

In this case:
- Do NOT file Form 982
- Use the `form-1099-c` skill for reporting on Schedule 1
- Do NOT make up a reason to claim an exclusion that doesn't fit — the IRS audits canceled-debt exclusions

---

## Decision matrix

| User scenario | Likely exclusion |
|---------------|------------------|
| Filed Chapter 7 / 11 / 13; debt discharged by court | Box 1a (bankruptcy) |
| Out of bankruptcy; liabilities > assets including retirement | Box 1b (insolvency) |
| Short sale / foreclosure of primary residence; acquisition debt | Box 1e (principal residence) — verify exclusion still in effect |
| Foreclosure of investment property | Box 1b (insolvency) if applicable; otherwise income |
| Foreclosure of vacation home | Box 1b (insolvency) if applicable; otherwise income |
| Forgiveness on credit card debt while solvent | None — full income on Schedule 1 Line 8c |
| Forgiveness on student loans (non-program) | None unless §108(f) applies |
| Student loans under §108(f)(5) ARP exclusion (2021-2025) | §108(f) automatic; usually no Form 982 needed |
| Public Service Loan Forgiveness | §108(f)(1)(A); generally no Form 982 |
| Farm debt forgiveness, ≥50% farm income last 3 years | Box 1c (qualified farm) |
| Real-estate business debt, solvent, not in bankruptcy | Box 1d (QRPBI) — election needed |
| Debt forgiven by family member | Investigate gift treatment (§102) — possibly not income at all |
| Debt to controlled entity | Investigate — may be constructive distribution |

---

## When multiple exclusions could apply

Per §108(a)(2):

1. **Bankruptcy trumps everything**. If the user is in Title 11, Box 1a applies; other boxes don't.
2. **Principal residence trumps insolvency by default** (§108(a)(2)(C)) — but the user can ELECT insolvency instead. Compare which gives a better tax result.
3. **Farm and QRPBI** are alternative paths — pick whichever fits.
4. **Multiple discharges in same year requiring different exclusions** — file multiple Forms 982, one per exclusion.

---

## Computing under "principal residence vs. insolvency" alternatives

When both could apply (user is insolvent AND the discharge is on principal residence):

| Factor | Principal residence (1e) | Insolvency (1b) |
|--------|--------------------------|-----------------|
| Cap | $750K of qualified PRI | Insolvency amount |
| Attribute reduction (Part II Lines 5-11) | None | All required |
| Basis reduction | Yes — reduce home basis | Default: yes (Line 9), or via §108(b)(5) election |
| Future tax cost | At sale of home (basis reduced → larger gain) | Smaller NOLs / credits / capital losses going forward |
| Complexity | Simple | Worksheet 2 + attribute reduction analysis |

The agent should compute both scenarios when both apply, then explain the trade-off:

> "If you elect principal residence exclusion: $X excluded, your home basis drops to $Y (affects future home sale capital gain). No NOLs reduced.
>
> If you elect insolvency: $Z excluded (capped at insolvency), your $A NOL is reduced to $B and your $C capital loss carryover is reduced to $D. Home basis preserved.
>
> Which is better depends on whether you'll sell the home soon (principal residence is worse) or have NOLs to use against next year's income (insolvency is worse if you lose them)."

The election is **irrevocable** once filed. Get user agreement before filing.
