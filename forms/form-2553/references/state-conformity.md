# State S-Corp Conformity

A federal S-corp election (CP261 acceptance) does **not** automatically grant S-corp status for state tax purposes in every state. Some states require a separate state-level election or registration step; others impose entity-level taxes that reduce the federal S-corp benefit.

State rules change. The rows below marked "checked 2026-10-06" were confirmed on the state's own site on that date; confirm everything else with the state revenue department before relying on it.

The agent must address state conformity at the time of federal filing. Forgetting the state election results in default state-level tax treatment (typically C-corp), which can wipe out the federal SE-tax savings.

---

## State conformity matrix

### States with a separate S-corp step

| State | Form / mechanism | Deadline | Notes |
|-------|------------------|----------|-------|
| **California** | No separate election; federal election conforms; entity files Form 100S annually | Annual (Mar 15 due date) | 1.5% franchise tax on S-corp income, $800 minimum |
| **New York** | **Form CT-6** (Election by a Federal S Corporation to be Treated as a New York S Corporation) | Any time during the preceding tax year, or on or before the 15th day of the 3rd month of the tax year (Form CT-6 instructions, checked 2026-10-06) | Without CT-6 the entity is a NY C-corp |
| **New Jersey** | No separate election for privilege periods beginning on or after Dec. 22, 2022 (P.L. 2022, c. 133; TB-105(R), checked 2026-10-06). Register with DORES as a corporation ("1120 filer"), submit the federal acceptance letter (CP261), and complete the Shareholder Jurisdictional Consent (Schedule SJC in CBT-100S) | With registration or the CBT-100S | A federal S corp is a NJ S corp unless 100% of shareholders elect C status; earlier periods need a retroactive NJ election |
| **Arkansas** | **Form AR1103** (Election by Small Business Corporation), with a copy of the IRS acceptance notice | During the first 75 days of the taxable year (AR1103 instructions, checked 2026-10-06) | The AR election is held in suspense until the IRS notice is received |
| **Wisconsin** | No separate election form identified; entity files Form 5S | Annual | Verify with the Wisconsin DOR |

Louisiana: Form R-6980 is the **Pass-Through Entity Tax Election** (checked 2026-10-06), not an S-corp election. Do not file it as one; see the PTE section below.

### States with automatic federal conformity (no extra filing)

The majority of states automatically treat the entity as an S-corp at the state level once the federal CP261 is received:

```
AL, AZ, CO, CT, DE, FL*, GA, HI, ID, IL, IN, IA, KS, KY, ME, MD, MA, MI, MN,
MS, MO, MT, NE, NM, NC, ND, OH*, OK, OR, PA, RI, SC, SD*, TN*, UT, VA, VT, WA*,
WV, WY*

*  No broad state individual income tax, so the federal S election matters mainly
   for entity-level taxes (next table; TN excise and TX franchise tax still apply):
   FL, NV, SD, TN, TX, WA, WY, AK.
   OH has no corporate income tax; it levies the CAT on gross receipts.
```

### States with entity-level S-corp tax (federal election applies, but state still taxes)

Some states grant S-corp pass-through treatment but **also** impose an entity-level tax — meaning S-corp owners pay state tax twice (once at entity level, once on K-1 income).

| State | Tax | Rate (approx.) |
|-------|-----|----------------|
| California | Franchise tax on S-corp net income | 1.5% (min $800) |
| Illinois | Personal property replacement tax | 1.5% |
| Massachusetts | Corporate excise income measure on S corps | 2.00% of net income if total receipts are $6M to under $9M; 3.00% at $9M or more; 8.0% only on built-in gains and passive investment income taxed federally under §§1374/1375 (mass.gov "S Corporations", checked 2026-10-06) |
| New Hampshire | Business profits tax + business enterprise tax | Variable |
| New Jersey | Corporation Business Tax on S-corps | Variable (lower than C-corp rates) |
| New York | Fixed dollar minimum tax | $25-$4,500 based on receipts |
| Ohio | Commercial Activity Tax (CAT) — gross receipts | 0.26% on taxable gross receipts above the annual exclusion, $6 million for 2025 and later (tax.ohio.gov, checked 2026-10-06) |
| Tennessee | Excise tax on S-corp income | 6.5% (state has no individual income tax) |
| Texas | Franchise tax / "margin tax" | 0.375% retail/wholesale, 0.75% other; no tax due at or below $2.47 million total revenue (2024-2025 reports) or $2.65 million (2026 report) (comptroller.texas.gov, checked 2026-10-06) |

For users in these states, the federal SE-tax savings from electing S-corp must be netted against the state-level entity tax. In some cases the federal savings are still worthwhile; in others (especially low-profit S-corps in California or Tennessee), the state tax can erase the benefit.

### States with PTE election (Pass-Through Entity Tax / SALT cap workaround)

Separately from S-corp conformity, many states now offer a Pass-Through Entity tax election that lets the entity pay state income tax at the entity level, deduct it federally, and then give shareholders a state credit. This is a **federal SALT-cap workaround** introduced after the 2017 Tax Cuts and Jobs Act. Louisiana's version is Form R-6980.

PTE elections are voluntary. They matter for users whose state and local taxes exceed the federal SALT cap: $40,000 for 2025 ($20,000 married filing separately), reduced for modified AGI over $500,000, under P.L. 119-21 (2025 Schedule A, line 5e and instructions). Most major states now have a PTE option (list not re-verified on 2026-10-06; confirm with the state):

```
AL, AZ, AR, CA, CO, CT, GA, HI, ID, IL, IN, IA, KS, KY, LA, MD, MA, MI, MN,
MS, MO, MT, NJ, NM, NY, NC, OH, OK, OR, RI, SC, UT, VA, WV, WI
```

The PTE election is **separate from** the S-corp election. The agent should mention PTE availability in states where the user files, but not bundle it into the Form 2553 workflow.

---

## State election workflow

When filing federal Form 2553, the agent should:

1. **Identify the state** where the entity was formed (Form 2553 item C) and every state where it does business
2. **Determine state conformity rule** from the matrix above
3. **If a separate state step is required**, prepare it within the state-specific deadline (Arkansas: first 75 days of the taxable year; New York: by the 15th day of the 3rd month)
4. **Inform the user of state-level entity tax** if applicable (CA franchise tax, NJ CBT, etc.) so they understand the net-of-state savings
5. **Mention PTE availability** as a separate optimization, not part of the S-corp election

### Multi-state operations

If the entity has nexus in multiple states (sales, employees, property), each state's conformity rule applies separately. This is a multi-state-tax problem beyond the scope of this skill — refer to a state-tax-specialist CPA.

---

## Common state-conformity mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| File federal 2553, forget NY CT-6 | Entity is NY C-corp; full corporate tax owed at NY rate | File CT-6 retroactively (NY has its own late-relief procedure) |
| File federal 2553, never register NJ as a corporation filer or file the Shareholder Jurisdictional Consent | NJ cannot accept the CBT-100S | Register with DORES as an 1120 filer, upload the CP261, complete Schedule SJC (TB-105(R)) |
| Move from a non-conforming to a conforming state mid-year | Need to re-file state election in new state | New state filing required for new tax-year start |
| Assume CA auto-conforms (it does) but ignore franchise tax | Surprise $800-$3,000 franchise tax bill at year-end | Budget for it; consider whether election is worthwhile in CA |

---

## Cross-references

- Filing mechanics: [`../filing.md`](../filing.md)
- Common mistakes: [`common-mistakes.md`](./common-mistakes.md)
- Authority sources: NY Form CT-6 instructions (tax.ny.gov); NJ TB-105(R) and https://www.nj.gov/treasury/taxation/cbt/scorpfaq-proceduralchanges.shtml; Arkansas AR1103 instructions (dfa.arkansas.gov); mass.gov "S Corporations"; tax.ohio.gov CAT page; comptroller.texas.gov franchise tax; Louisiana Form R-6980 (revenue.louisiana.gov)
- IRS state-tax landing: https://www.irs.gov/businesses/small-businesses-self-employed/state-government-websites
