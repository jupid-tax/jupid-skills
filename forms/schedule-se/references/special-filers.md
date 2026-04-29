# Special Filers on Schedule SE

Edge cases the standard workflow does not cover cleanly. The agent should detect these situations from the user's prerequisites and apply the rules below.

---

## Partners in a partnership (Form 1065 K-1)

### General partner / LLC manager-member

Schedule K-1 (Form 1065) Box 14 Code A reports **net earnings from self-employment** allocated to the partner. This flows to Schedule SE Line 2 alongside any Schedule C income.

For an LLC taxed as a partnership: the manager-member's share is SE earnings. If the LLC has multiple managers all materially participating, each member's K-1 Box 14 Code A is their SE share.

### Limited partner (or non-managing LLC member)

IRC §1402(a)(13) **excludes** limited partner distributive share from SE earnings — the partner is treated as a passive investor. The K-1 will typically show $0 or no entry in Box 14 Code A for a true limited partner.

Exception: **guaranteed payments** to a limited partner for services rendered (K-1 Box 4a) ARE SE earnings, regardless of partner status. If the K-1 has Box 4a > 0, that amount is SE-eligible.

### LLC manager-member: the IRS audit issue

There is ongoing IRS litigation over whether LLC manager-members are treated as general partners (SE-eligible) or limited partners (not SE-eligible). The IRS's position (proposed regulations, never finalized) is that LLC members who *materially participate* are treated as general partners; passive members get the limited-partner exclusion. The Tax Court has aligned with this in Renkemeyer (2011) and similar cases.

The agent should **not** make the call on the user's behalf. Ask: "Are you materially participating in the partnership/LLC operations?" If yes, treat Box 14 Code A as SE. If no, ask whether the K-1 issuer treated the user as a limited partner (Box 14 should be 0).

### Multiple partnerships

A filer can have K-1s from several partnerships. Sum all SE-eligible Box 14 Code A amounts for Line 2. Each K-1 is independent; one being limited-partner status doesn't affect another.

---

## Foreign earned income exclusion (Form 2555)

A US citizen or resident working abroad can exclude up to **$130,000** (2025; verify 2026) of foreign earned income from regular income tax via Form 2555. **However:**

> The Form 2555 exclusion does NOT reduce SE tax. — IRC §911(d)(4)

If the filer has foreign-earned SE income (e.g., a freelance consultant living in Berlin earning USD from US clients), the gross SE earnings flow to Schedule C → Schedule SE Line 2 *unreduced* by the Form 2555 exclusion. The filer pays SE tax on the full amount even though they pay no income tax on it.

Exception: **totalization agreement coverage**. If the filer obtains a Certificate of Coverage from the foreign country's social security agency showing they are covered by that country's system, the income is excluded from US SE tax. The certificate goes in the filer's records (the IRS may request it on audit).

US has totalization agreements with about 30 countries — full list at https://www.ssa.gov/international/agreements_overview.html

### How to handle on Schedule SE

If the filer has Form 2555 income but **no totalization certificate**: report SE income normally on Line 2 and pay SE tax. Note in the deliverable: "Form 2555 income included in SE base per IRC §911(d)(4)."

If the filer has a **totalization certificate**: exclude the covered SE income from Line 2. Note in the deliverable: "Foreign SE income excluded under [country] totalization agreement, certificate dated [date] retained in filer records."

---

## Statutory employees

Form W-2 Box 13 has a "Statutory employee" checkbox. When checked, the worker is treated as an employee for FICA (employer withholds Social Security and Medicare) but as self-employed for income tax (deducts business expenses on Schedule C).

Common statutory employees:
- Full-time life insurance agents
- Agent or commission drivers (delivering food, beverages, laundry)
- Traveling or city salespeople (under exclusive contract)
- Home workers performing work according to specifications

### Schedule SE treatment

Because FICA is withheld at the W-2 stage, statutory employee income is **not subject to SE tax**. The Schedule C net profit derived from statutory employee earnings should NOT flow to Schedule SE Line 2.

If the filer has a Schedule C with only statutory-employee income, no Schedule SE is required for that Schedule C. If they have additional non-statutory SE income (a side gig), only that flows to Line 2.

The agent should ask: "Is your Schedule C income from a Form W-2 with the 'Statutory employee' box checked?" If yes, exclude that Schedule C's net profit from Line 2.

---

## Notary public fees

Notary public fees received for performing notarial acts are **exempt from SE tax** under IRC §1402(c)(1). They remain in Schedule C gross income but get backed out of the SE base.

### How to handle

On Schedule SE Line 2, enter the Schedule C net profit *minus* the notary fees portion. Most filers include a written explanation: "Schedule C Line 31 = $X,XXX. Notary public fees of $Y,YYY excluded from SE earnings under IRC §1402(c)(1). Net SE earnings = $X,XXX − $Y,YYY = $Z,ZZZ."

The IRS form does not have a dedicated line for this — attach a statement.

---

## Clergy with Form 4361 exemption

Ministers, members of religious orders, and Christian Science practitioners can file **Form 4361** within 2 years of starting their ministry to claim exemption from SE tax on ministerial earnings (IRC §1402(e)). Once approved, the exemption is **irrevocable** — there is no way to opt back in to Social Security on those earnings.

### Schedule SE treatment

Approved Form 4361 holders **do not file Schedule SE** for their ministerial earnings. They may still file Schedule SE if they have non-ministerial SE income.

This is a complex area (parsonage allowance, church-employer FICA elections, dual-status ministers); refer the user to **Pub 517** and a tax professional. Out of scope for this skill.

---

## Amish and Mennonite (Form 4029 exemption)

Members of recognized religious sects opposed to receiving public insurance (Old Order Amish, certain Mennonite groups) can file **Form 4029** for total exemption from FICA and SE tax (IRC §1402(g)). Approved holders do not file Schedule SE on covered earnings.

Like Form 4361, this is irrevocable. Out of scope; refer to Form 4029 instructions and Pub 517.

---

## State self-employment / city-level SE-equivalents

**Federal SE tax (Schedule SE)** is the only tax computed on this form. Several states and cities impose SE-equivalent taxes that are NOT reported on Schedule SE:

- **NYC Unincorporated Business Tax (UBT)** — 4% on unincorporated business income above thresholds. Filed on NYC-202.
- **California — none** at the state level for SE tax (the state taxes SE income via regular state income tax).
- **Self-Employment Contributions Act (SECA) state mirrors** — most states do not have a separate SE tax.
- **Local Earnings Taxes** — Philadelphia (BIRT/NPT), Pittsburgh (LST), Cleveland (CCA) — apply to SE earnings independently of federal SE tax.

The agent should remind the user: "Schedule SE handles only federal Social Security and Medicare tax on your SE earnings. Your state and city may have additional taxes — check your state revenue department and local rules."

---

## Joint returns with SE income from both spouses

A married-filing-jointly couple where both spouses have SE income files **two separate Schedule SEs** — one in each spouse's name. The wage base, optional method elections, and W-2 wage offsets apply per spouse.

Common mistake: combining both spouses' SE earnings on one Schedule SE. The IRS rejects this; the SS wage base is per-individual, not per-couple.

If only one spouse has SE income, only that spouse files a Schedule SE.

---

## Multi-state filers

SE tax is federal. The filer's state of residence does not affect the Schedule SE computation. However:

- The **state income tax** treatment of the §164(f) deductible half of SE tax (Schedule 1 Line 15) depends on whether the state conforms to federal AGI. Most states do; California has its own conformity quirks.
- If the filer operates a Schedule C across multiple states, each state may require its own state return reporting the apportioned business income — but Schedule SE is computed once on the federal aggregate.

---

## Authority cited

- IRC §1402(a)(13) — limited partner exclusion
- IRC §1402(c)(1) — notary public exemption
- IRC §1402(e) — ministers' Form 4361 exemption
- IRC §1402(g) — religious sect Form 4029 exemption
- IRC §911(d)(4) — Form 2555 does not reduce SE tax
- IRC §3121(d)(3) — statutory employees
- Tax Court decisions on LLC manager-member SE treatment: Renkemeyer (2011), Castigliola (2017)
- Pub 517 — Social Security and Other Information for Members of the Clergy
- SSA Totalization Agreements — https://www.ssa.gov/international/agreements_overview.html

## Verify before filing

- Form 2555 exclusion amount for current year (2025: $130,000)
- Active totalization agreements (no major changes recently, but verify if exotic country)
- State-level SE / unincorporated business tax for the filer's jurisdiction
