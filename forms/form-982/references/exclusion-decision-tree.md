# §108(a) Exclusion Decision Tree

How to determine which exclusion (if any) applies to the user's canceled debt. Walk through the tests in order — the first one that fits is the exclusion to claim.

The key principle: §108(a)(2) gives bankruptcy priority over all other exclusions. Other exclusions follow conditional priorities described below. Sources: IRC §108 (law.cornell.edu), Instructions for Form 982 (Rev. December 2021), Pub. 4681 (2025).

---

## Step 1 — Bankruptcy test (Box 1a)

Ask:
1. Did the user file a bankruptcy petition under Title 11 of the US Code?
2. Was the user under the court's jurisdiction in the case?
3. Was the discharge granted by the court, or does it occur under a plan approved by the court (§108(d)(2))?

If all three: **Box 1a, §108(a)(1)(A)**. STOP. Use bankruptcy exclusively; boxes 1b–1e don't apply to a title 11 discharge (§108(a)(2)(A)).

The bankruptcy exclusion is the broadest:
- No insolvency requirement (could be solvent and still qualify)
- No cap on excluded amount
- All Title 11 chapters qualify (Chapter 7, 11, 12, 13)
- Court-granted discharge (or a court-approved plan) is the trigger, not the petition filing

Documentation: bankruptcy case number, chapter, date filed, date of discharge order. The discharge order itself should be retained (NOT filed with Form 982).

If user is "in bankruptcy" but the debt was canceled by the creditor BEFORE the petition or AFTER dismissal — Box 1a does NOT apply. Try insolvency.

---

## Step 2 — Qualified principal residence test (Box 1e)

This step comes BEFORE insolvency under §108(a)(2)(C), unless the user elects insolvency instead.

Ask:
1. Was the property the user's main home (principal residence, §108(h)(5): where the user ordinarily lives most of the time)?
2. Was the debt used to BUY, BUILD, or substantially IMPROVE that home (a refinance counts only up to the old mortgage principal just before the refinancing)?
3. Was the debt secured by the home?
4. When was the debt discharged? The exclusion covers only discharges before Jan. 1, 2026, or discharges under an arrangement entered into and evidenced in writing before Jan. 1, 2026.
5. Was the discharge tied to a decline in the home's value or the user's financial condition (not to services for the lender or another unrelated factor, §108(h)(3))?

Item 4 status as of 2026-10-06 (§108(a)(1)(E); i982 Line 1e; Pub. 4681 (2025) What's New):
- The exclusion began with discharges on or after Jan. 1, 2007 (P.L. 110-142) and was extended several times
- The last extension (P.L. 116-260, div. EE, §114) runs through Dec. 31, 2025
- No extension for 2026 discharges. For a 2026 discharge, ask for a written arrangement (signed modification, short-sale approval, settlement letter) dated before Jan. 1, 2026; without one, box 1e is unavailable

If all five: **Box 1e, §108(a)(1)(E)**. Use principal residence exclusion.

Cap: QPRI is acquisition debt up to $750K ($375K MFS) for discharges after 2020 (IRC §108(h)(2)); before 2021 the figures were $2M ($1M MFS).

If only part of the loan is QPRI (debt above the cap, or cash-out not used on the home): the exclusion applies only to the amount discharged in excess of the non-QPRI part (§108(h)(4)). The i982 example: $1M loan, $800K QPRI, $300K discharged → $100K excludable; the other $200K may qualify for another exclusion such as insolvency.

After exclusion: if the user still owns the home, Form 982 line 10b = smaller of the excluded QPRI or the home's basis (§108(h)(1); i982 Line 10b). If the home was sold or foreclosed in the same transaction, there is no line 10b reduction. Keep the record for a future sale (Pub. 523 basis adjustments).

User can ELECT insolvency instead of principal residence exclusion by checking box 1b instead of 1e (§108(a)(2)(C); i982 Line 1e).

If property was a vacation home, rental, or investment — NOT principal residence. Go to Step 3 (insolvency).

---

## Step 3 — Insolvency test (Box 1b)

Ask:
1. Was the user insolvent IMMEDIATELY BEFORE the discharge?
2. Insolvency = total liabilities > FMV of total assets (all assets, including exempt assets such as retirement accounts and pension interests; nonrecourse debt counts up to the FMV of the property securing it, plus any excess that is forgiven) (Pub. 4681 "Insolvency").

Use the Pub. 4681 Insolvency Worksheet to compute. See [`insolvency-worksheet.md`](./insolvency-worksheet.md).

If user is insolvent: **Box 1b, §108(a)(1)(B)**. Use insolvency exclusion.

Cap: lesser of (canceled debt amount) or (insolvency amount). If user was $20K insolvent and had $30K of debt forgiven, only $20K is excludable; $10K is ordinary income on Schedule 1 Line 8c.

If user is solvent (assets > liabilities), insolvency does NOT apply. Skip to Step 4.

Common confusion: "I have no money in the bank, I'm insolvent." The §108 insolvency test uses ALL assets, including the home, cars, and retirement accounts. A user with $200K in a 401(k) and $60K of credit card debt is NOT insolvent — they have $140K of net worth.

---

## Step 4 — Qualified farm indebtedness test (Box 1c)

Uncommon for general agent use. Ask only if:
1. The debt was incurred directly in connection with the operation of a farming business
2. ≥ 50% of the user's aggregate gross receipts for the 3 tax years before the discharge year came from farming
3. The discharge was made by a qualified person: someone actively and regularly engaged in lending money who is not related to the user, not the seller of the property, and not paid a fee on the user's investment in it, or a federal, state, or local government or agency (§108(g)(1); i982 Line 1c)

If yes: **Box 1c, §108(a)(1)(C)**, but only for the part of the discharge beyond any insolvency amount (§108(a)(2)(B)).

Cap: the sum of adjusted tax attributes (credits counted at $3 per $1) and the adjusted basis of qualified property held at the beginning of the next tax year (§108(g)(3); Pub. 4681 "Exclusion limit").

This skill primarily targets individual / solo filers. Most won't qualify under (C). If user is a farmer, refer to a CPA.

---

## Step 5 — Qualified real property business indebtedness test (Box 1d)

Taxpayers other than C corporations with debt secured by REAL property used in a trade or business.

Ask:
1. Is the taxpayer other than a C corporation (§108(a)(1)(D))? For this skill: an individual or sole proprietor. (Partnerships apply §108 at the partner level, S corporations at the corporate level, §108(d)(6)–(7).)
2. Was the debt incurred or assumed in connection with real property used in a trade or business, and is it secured by that property? (Not real property held primarily for sale to customers; residential rental property generally qualifies unless the user also uses the dwelling as a home, Pub. 4681.)
3. Was the debt incurred or assumed BEFORE January 1, 1993, OR is it qualified acquisition indebtedness (to acquire, construct, reconstruct, or substantially improve the property), or a refinancing of either up to the refinanced amount (§108(c)(3)–(4))?
4. Does the user want to make the election (checking box 1d on a timely filed return, including extensions)?

If yes to all: **Box 1d, §108(a)(1)(D) and §108(c)**, but only for the part of the discharge beyond any insolvency amount (§108(a)(2)(B)).

Cap: lesser of (outstanding principal immediately before the discharge over the FMV of the securing property, reduced by other QRPBI secured by it) or (aggregate adjusted basis of depreciable real property held immediately before the discharge, other than property acquired in contemplation of it) (§108(c)(2)).

After exclusion: reduce basis of the depreciable real property by the excluded amount (Form 982 line 4).

The QRPBI election can be revoked only with IRS consent (§108(d)(9)(B); i982 When To File). A missed election can be made on an amended return within 6 months of the due date (excluding extensions) marked "Filed pursuant to section 301.9100-2". Make it deliberately.

QRPBI is somewhat rare. It doesn't apply in a title 11 case or to the extent the user was insolvent; those exclusions come first. Use QRPBI for the solvent part of a real-estate business debt discharge outside bankruptcy.

---

## Step 6 — No exclusion applies

If none of Steps 1-5 fits: there is NO §108 exclusion. The full discharged amount is ordinary income: Schedule 1 Line 8c for nonbusiness debt, Schedule C Line 6 for a sole proprietorship, Schedule E Line 3 for rental real property, Schedule F Line 8 for farm debt (Pub. 4681).

In this case:
- Do NOT file Form 982
- Use the `form-1099-c` skill for reporting the income
- Do NOT make up a reason to claim an exclusion that doesn't fit — the IRS audits canceled-debt exclusions

---

## Decision matrix

| User scenario | Likely exclusion |
|---------------|------------------|
| Filed Chapter 7 / 11 / 13; debt discharged by court | Box 1a (bankruptcy) |
| Out of bankruptcy; liabilities > assets including retirement | Box 1b (insolvency) |
| Short sale / foreclosure of primary residence; acquisition debt | Box 1e (principal residence) if discharged before 2026 or under a pre-2026 written arrangement; otherwise test 1b |
| Foreclosure of investment property | Box 1b (insolvency) if applicable; otherwise income |
| Foreclosure of vacation home | Box 1b (insolvency) if applicable; otherwise income |
| Forgiveness on credit card debt while solvent | None — full income on Schedule 1 Line 8c |
| Forgiveness on student loans (non-program) | None unless §108(f) applies; test insolvency (1b) |
| Student loans discharged after 2020 and before 2026 (ARPA §108(f)(5)) | §108(f) exclusion; no Form 982 |
| Student loans discharged after 2025 on account of death or total and permanent disability | §108(f)(5) as amended by P.L. 119-21 §70119; SSN required on the return; no Form 982 |
| Discharge for working a set period in certain professions | §108(f)(1); no Form 982 |
| Farm debt forgiveness, ≥50% of gross receipts from farming in the 3 prior years | Box 1c (qualified farm), after any insolvency amount |
| Real-estate business debt, solvent, not in bankruptcy | Box 1d (QRPBI) — election needed |
| Debt forgiven by family member | Investigate gift treatment (§102) — possibly not income at all |
| Debt to controlled entity | Investigate — may be constructive distribution |

---

## When multiple exclusions could apply

Per §108(a)(2):

1. **Bankruptcy trumps everything** (§108(a)(2)(A)). If the discharge occurs in a title 11 case, Box 1a applies; other boxes don't.
2. **Principal residence trumps insolvency by default** (§108(a)(2)(C)) — but the user can ELECT insolvency (box 1b instead of 1e). Compare which gives a better tax result.
3. **Insolvency comes before farm and QRPBI** (§108(a)(2)(B)): those exclusions apply only to the part of the discharge beyond the insolvency amount. QRPBI excludes qualified farm indebtedness (§108(c)(3)).
4. **Multiple discharges or exclusions in the same year** — one Form 982: check every applicable box and enter the total on line 2 (form: "check applicable box(es)"; Pub. 4681 examples check 1b and 1c, and 1b and 1d).

---

## Computing under "principal residence vs. insolvency" alternatives

When both could apply (user is insolvent AND the discharge is on principal residence):

| Factor | Principal residence (1e) | Insolvency (1b) |
|--------|--------------------------|-----------------|
| Cap | $750K of qualified PRI | Insolvency amount |
| Attribute reduction (Part II lines 6–13) | None | Required, in order |
| Basis reduction | Line 10b, only if the home is still owned | Line 10a (limited by §1017(b)(2)), or line 5 via §108(b)(5) election |
| Future tax cost | At sale of home (basis reduced → larger gain) | Smaller NOLs / credits / capital losses going forward |
| Complexity | Simple | Insolvency Worksheet + attribute reduction analysis |

The agent should compute both scenarios when both apply, then explain the trade-off:

> "If you elect principal residence exclusion: $X excluded, your home basis drops to $Y (affects future home sale capital gain). No NOLs reduced.
>
> If you elect insolvency: $Z excluded (capped at insolvency), your $A NOL is reduced to $B and your $C capital loss carryover is reduced to $D. Home basis is reduced only through line 10a, which is often $0 for an insolvent filer.
>
> Which is better depends on whether you'll sell the home soon (principal residence is worse) or have NOLs to use against next year's income (insolvency is worse if you lose them)."

The instructions don't say whether this choice can be changed after filing; get user agreement before filing.
