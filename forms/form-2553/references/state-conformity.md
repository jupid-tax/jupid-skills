# State S-Corp Conformity

A federal S-corp election (CP261 acceptance) does **not** automatically grant S-corp status for state tax purposes in every state. About 8 states require either a separate state-level election or impose entity-level taxes that effectively negate the federal S-corp benefit.

The agent must address state conformity at the time of federal filing. Forgetting the state election results in default state-level tax treatment (typically C-corp), which can wipe out the federal SE-tax savings.

---

## State conformity matrix

### States requiring separate S-corp election

| State | Form / mechanism | Deadline | Notes |
|-------|------------------|----------|-------|
| **California** | Federal election conforms automatically; entity files Form 100S annually | Annual (Mar 15 due date) | But: 1.5% franchise tax on S-corp income, $800 minimum |
| **New York** | **Form CT-6** (Election by a Federal S Corporation to be Treated as a New York S Corporation) | Within 2.5 months of effective date OR any time during preceding tax year | NY does not auto-conform; without CT-6 the entity is a NY C-corp (full corporate tax) |
| **New Jersey** | **Form CBT-2553** (New Jersey S Corporation or New Jersey QSSS Election) | Within 1 month after effective date of federal election | NJ also imposes entity-level tax on S-corps; CBT-100S is the annual return |
| **Arkansas** | **Form AR1103** (Election by Small Business Corporation) | Within 75 days of federal effective date | Or Arkansas defaults to C-corp treatment |
| **Louisiana** | **Form R-6980** (Tax Election for Pass-Through Entity) | Within 30 days of federal acknowledgment | Recently changed; verify with LA Department of Revenue |
| **Wisconsin** | Federal election conforms but S-corps owe separate annual fee; check Form 5S instructions | Annual | No separate election form |

### States with automatic federal conformity (no extra filing)

The majority of states automatically treat the entity as an S-corp at the state level once the federal CP261 is received:

```
AL, AZ, CO, CT, DE, FL*, GA, HI, ID, IL, IN, IA, KS, KY, ME, MD, MA, MI, MN,
MS, MO, MT, NE, NM, NC, ND, OH*, OK, OR, PA, RI, SC, SD*, TN*, UT, VA, VT, WA*,
WV, WY*

*  No state income tax — S-corp election is moot for state purposes:
   FL, NV (no income tax), SD, TN, TX, WA, WY (no income tax),
   OH (replaced corp tax with CAT — gross receipts based)
   AK (no broad income tax)
```

### States with entity-level S-corp tax (federal election applies, but state still taxes)

Some states grant S-corp pass-through treatment but **also** impose an entity-level tax — meaning S-corp owners pay state tax twice (once at entity level, once on K-1 income).

| State | Tax | Rate (approx.) |
|-------|-----|----------------|
| California | Franchise tax on S-corp net income | 1.5% (min $800) |
| Illinois | Personal property replacement tax | 1.5% |
| Massachusetts | Excise tax on S-corp income | 8.0% on net income (with thresholds) |
| New Hampshire | Business profits tax + business enterprise tax | Variable |
| New Jersey | Corporation Business Tax on S-corps | Variable (lower than C-corp rates) |
| New York | Fixed dollar minimum tax | $25-$4,500 based on receipts |
| Ohio | Commercial Activity Tax (CAT) — gross receipts | 0.26% on receipts > $1M |
| Tennessee | Excise tax on S-corp income | 6.5% (state has no individual income tax) |
| Texas | Franchise tax / "margin tax" | 0.375% retail, 0.75% other (above threshold) |

For users in these states, the federal SE-tax savings from electing S-corp must be netted against the state-level entity tax. In some cases the federal savings are still worthwhile; in others (especially low-profit S-corps in California or Tennessee), the state tax can erase the benefit.

### States with PTE election (Pass-Through Entity Tax / SALT cap workaround)

Separately from S-corp conformity, many states now offer a Pass-Through Entity tax election that lets the entity pay state income tax at the entity level, deduct it federally, and then give shareholders a state credit. This is a **federal SALT-cap workaround** introduced after the 2017 Tax Cuts and Jobs Act.

PTE elections are voluntary. They benefit users with state income tax > $10,000/year on K-1 income who are otherwise capped on SALT deductions. Most major states now have a PTE option:

```
AL, AZ, AR, CA, CO, CT, GA, HI, ID, IL, IN, IA, KS, KY, LA, MD, MA, MI, MN,
MS, MO, MT, NJ, NM, NY, NC, OH, OK, OR, RI, SC, UT, VA, WV, WI
```

The PTE election is **separate from** the S-corp election. The agent should mention PTE availability in states where the user files, but not bundle it into the Form 2553 workflow.

---

## State election workflow

When filing federal Form 2553, the agent should:

1. **Identify the state** where the entity does business (Line E of Form 2553)
2. **Determine state conformity rule** from the matrix above
3. **If a separate state election is required**, prepare and file the state form within the state-specific deadline (which can be tighter than the federal deadline — NJ's 1-month deadline is the most common trap)
4. **Inform the user of state-level entity tax** if applicable (CA franchise tax, NJ CBT, etc.) so they understand the net-of-state savings
5. **Mention PTE availability** as a separate optimization, not part of the S-corp election

### Multi-state operations

If the entity has nexus in multiple states (sales, employees, property), each state's conformity rule applies separately. This is a multi-state-tax problem beyond the scope of this skill — refer to a state-tax-specialist CPA.

---

## Common state-conformity mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| File federal 2553, forget NY CT-6 | Entity is NY C-corp; full corporate tax owed at NY rate | File CT-6 retroactively (NY has its own late-relief procedure) |
| File federal 2553, forget NJ CBT-2553 | NJ doesn't recognize S-corp; CBT-100 owed | File CBT-2553 with reasonable cause; NJ generally accepts late filings |
| Move from a non-conforming to a conforming state mid-year | Need to re-file state election in new state | New state filing required for new tax-year start |
| Assume CA auto-conforms (it does) but ignore franchise tax | Surprise $800-$3,000 franchise tax bill at year-end | Budget for it; consider whether election is worthwhile in CA |

---

## Cross-references

- Filing mechanics: [`../filing.md`](../filing.md)
- Common mistakes: [`common-mistakes.md`](./common-mistakes.md)
- Authority sources: state revenue department instructions for each state listed
- IRS state-tax landing: https://www.irs.gov/businesses/small-businesses-self-employed/state-government-websites
