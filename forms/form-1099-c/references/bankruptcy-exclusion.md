# Bankruptcy Exclusion — IRC §108(a)(1)(A)

The bankruptcy exclusion is the strongest exclusion available under §108. If the canceled debt was discharged in a Title 11 case and the discharge order has been entered by the bankruptcy court, the **entire** canceled amount is excluded from income — no caps, no income test, no insolvency calculation.

This file covers the requirements, the timing rules, the documentation the agent should obtain, and the trade-off (attribute reduction).

---

## The rule

**IRC §108(a)(1)(A):** Gross income does not include any amount that would otherwise be includable in gross income by reason of the discharge of indebtedness if the discharge occurs **in a Title 11 case**.

**Title 11** of the United States Code is the federal bankruptcy code. It includes:

- **Chapter 7** — liquidation (most common consumer bankruptcy)
- **Chapter 11** — reorganization (typical for businesses; rarely consumer)
- **Chapter 12** — family farmer/fisherman reorganization
- **Chapter 13** — wage earner reorganization (consumer with regular income)

State-law debt-relief proceedings (state insolvency laws, assignments for the benefit of creditors, state receiverships) are **not** Title 11. The §108(a)(1)(A) exclusion does not apply to those — analyze under insolvency or other exclusions.

---

## Two requirements

### Requirement 1 — Title 11 case

The debt must be discharged in a case **under** Title 11. Confirm:

- The borrower filed a bankruptcy petition with a U.S. Bankruptcy Court (not a state court)
- The case is under Chapter 7, 11, 12, or 13
- The case was not dismissed (a dismissed case has no discharge)

### Requirement 2 — Discharge order entered

The bankruptcy court must have **entered a discharge order** that includes the canceled debt. Pre-discharge cancellations are not §108(a)(1)(A) eligible:

- A debt the borrower negotiated and settled with a creditor *before* filing bankruptcy → not under §108(a)(1)(A) (test §108(a)(1)(B) insolvency or other exclusions)
- A debt the trustee abandoned during the case but that wasn't part of the discharge → analyze case-by-case
- A debt the creditor charged off after filing but before the discharge order → typically picked up by the discharge order if scheduled in the petition

**Get the discharge order date and a copy from the borrower** before relying on this exclusion. The discharge order is an official document from the bankruptcy court (Form B 318 in Chapter 7 cases). Without it, the agent should treat the debt as not yet discharged.

---

## Timing

The exclusion applies when the **discharge occurs**, which is the date the discharge order is entered.

- If Box 1 of the 1099-C is **before** the discharge order date, the §108(a)(1)(A) exclusion may not apply to that creditor's cancellation — the creditor canceled before the discharge. Test other exclusions.
- If Box 1 is **after** the discharge order date, but the creditor is reporting cancellation of a debt that was actually discharged by the bankruptcy court, the §108(a)(1)(A) exclusion applies — the creditor may be late in filing the 1099-C.
- The tax year of reporting follows Box 1, but the exclusion's authority (the discharge order) is established by the order date.

**Common timing scenario:** Borrower's Chapter 7 discharge entered 2024-11-20. Creditor sends 1099-C with Box 1 = 2025-02-10 (creditor's internal write-off date) and Box 6 = G (decision to discontinue collection). The cancellation is post-discharge → debt was already discharged in the 2024 Title 11 case. The 1099-C arguably should not have been issued (the debt was already gone), but if it was, claim the §108(a)(1)(A) exclusion on the 2025 return because Box 1 = 2025.

---

## How to claim

**Form 982** is required.

1. Check **Box 1a** (Discharge of indebtedness in a title 11 case)
2. Enter the excluded amount on **Line 2**
3. Apply attribute reduction in Part II — see below
4. Attach Form 982 to the 1040

The borrower does **not** report the canceled amount on Schedule 1 Line 8c (or anywhere else as income) when the exclusion applies fully.

---

## Attribute reduction (the trade-off)

§108(a)(1)(A) is paired with **§108(b)**, which requires the borrower to **reduce tax attributes** by the excluded amount. The reduction is mandatory and follows a fixed order:

1. **NOLs** — net operating loss for the year of discharge, then NOL carryovers
2. **General business credits** — IRC §38 credit carryovers
3. **Minimum tax credits** — alternative minimum tax credits
4. **Capital loss carryovers** — current-year capital loss + carryovers
5. **Basis of property** — reduce basis of all property held at the start of the year following discharge (subject to a limit equal to total liabilities minus total asset basis)
6. **Passive activity losses and credits** — IRC §469 carryovers
7. **Foreign tax credit carryovers** — IRC §27 / §901 carryovers

Each $1 of exclusion reduces $1 of attribute (with a 33⅓¢ ratio for credits — a $1 exclusion reduces $1/3 of credit dollars in categories 2, 3, and 7).

**For most consumer bankruptcies, the borrower has no tax attributes to reduce.** No NOLs, no business credits, no capital loss carryovers, minimal property basis. In that case, attribute reduction is a non-event — Part II of Form 982 is filled with zeros and a "no attributes to reduce" note.

For borrowers with significant attributes (active business, capital loss carryovers, NOLs from prior years), the reduction is the price of the exclusion. The attribute reduction is timing — the borrower pays tax later when those attributes would have offset income — rather than absolute. But it can be material.

**Election to reduce basis of depreciable property first (§108(b)(5)):** A borrower can elect to apply the reduction to depreciable property basis **before** the standard attribute order. This is sometimes useful for borrowers with both NOLs and depreciable property; it preserves the NOLs for future use at the cost of reducing basis (which becomes recapture on sale or smaller depreciation deductions). The election is made on Form 982 Part III Line 14.

---

## Documentation checklist

- [ ] Bankruptcy petition (or chapter 7 statement of financial affairs)
- [ ] Schedule of debts filed with the petition (showing the canceled debt was scheduled)
- [ ] **Discharge order** from the bankruptcy court (the load-bearing document)
- [ ] Notice from the trustee or court showing case status (closed vs. open)
- [ ] The 1099-C(s) at issue
- [ ] If multiple creditors canceled discharged debts: a list of all 1099-Cs and confirmation each one was scheduled in the petition

If the borrower didn't schedule the debt in the petition, the discharge may not have covered it (depending on the chapter and circumstances). In Chapter 7, unscheduled debts can sometimes still be discharged if the creditor had notice; in Chapter 13, unscheduled debts are typically excluded from discharge. When in doubt, refer the borrower to bankruptcy counsel.

---

## Edge cases

### Pending bankruptcy

If the borrower has filed but the discharge has not yet been entered, **do not** claim §108(a)(1)(A). Wait for the discharge order. Until then:

- Test §108(a)(1)(B) insolvency for any current-year cancellation (filing bankruptcy is itself strong evidence of insolvency)
- Or extend the borrower's return until the discharge is entered, if the filing deadline allows

### Dismissed case

A dismissed case (the case is closed without a discharge) does **not** discharge debts. The §108(a)(1)(A) exclusion does not apply. Test other exclusions; insolvency is the most likely path.

### Hardship discharge in Chapter 13

A Chapter 13 hardship discharge (under 11 U.S.C. §1328(b)) does discharge debts but with limitations. For §108 purposes, it is still a Title 11 discharge — claim §108(a)(1)(A) for amounts discharged.

### Student loans in bankruptcy

Student loans are generally **not dischargeable** in bankruptcy unless the borrower obtains an "undue hardship" finding (Brunner test or its equivalent in the circuit). If a student loan was *not* discharged in the bankruptcy and a creditor later sends a 1099-C, the §108(a)(1)(A) exclusion does not apply to that loan. Test §108(f) student loan exclusions instead.

### Tax debt in bankruptcy

Some federal income tax debts are dischargeable in Chapter 7 (older taxes meeting the 3-2-240 day rules), most are not. If a tax debt was discharged, §108(a)(1)(A) applies; if it was merely "uncollectible" (CNC status), it's not discharged and other exclusions may apply.

---

## Sources

- IRC §108(a)(1)(A) — bankruptcy exclusion
- IRC §108(b) — attribute reduction order
- IRC §108(b)(5) — election to reduce basis of depreciable property first
- IRC §108(d)(2) — Title 11 case definition
- 11 U.S.C. §727 — Chapter 7 discharge
- 11 U.S.C. §1141 — Chapter 11 discharge
- 11 U.S.C. §1228 — Chapter 12 discharge
- 11 U.S.C. §1328 — Chapter 13 discharge
- [Publication 4681](https://www.irs.gov/publications/p4681) — Chapter 1 walks through the exclusion
- [Form 982](https://www.irs.gov/pub/irs-pdf/f982.pdf) and [Instructions](https://www.irs.gov/pub/irs-pdf/i982.pdf)
