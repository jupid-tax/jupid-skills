# Form 1116 Baskets (Income Categories)

Each Form 1116 covers exactly one category of foreign-source income. The filer files a separate 1116 per category. Picking the wrong basket is the most common Form 1116 error — the credit gets capped against the wrong limitation, and the IRS may reject or recompute on audit.

## The seven categories (IRC §904(d) and Reg. §1.904-4)

| Box | Category | Typical income |
|-----|----------|---------------|
| a | §951A category (GILTI) | GILTI inclusion of US shareholders of CFCs (an individual who made a §962 election claims the CFC-tax credit on Form 1118 instead) |
| b | Foreign branch category | Business profits attributable to qualified business units (QBUs) in foreign countries |
| c | Passive category | Dividends, interest, royalties, rents, capital gains, annuities |
| d | General category | Wages, SE income, business income — anything not in another box |
| e | §901(j) income | Income from sanctioned countries (no credit for taxes paid to them) |
| f | Certain income re-sourced by treaty | US-source income a treaty treats as foreign source, when the filer elects the treaty |
| g | Lump-sum distributions | Foreign-source pension lump sum when the tax is figured on Form 4972 |

## How to assign income

### 1099-DIV with foreign tax (Box 7)

Box 7 dividends → **passive category (c)** by default.

Exception: if the dividend bears foreign tax at a rate above the highest US tax rate that would apply, the **high-tax kickout (HTK)** moves it to general (d). HTK applies when foreign tax > highest US rate × US-equivalent income (Reg. §1.904-4(c)). For most retail dividend income with 15% foreign withholding, HTK does NOT apply.

### 1099-INT or foreign bank interest

Foreign-source interest → **passive (c)**.

Exception: interest from active financing activities of a foreign branch could move to general (d) under regs.

### Wages / salary from foreign employer (or domestic employer for foreign work)

→ **General (d)**.

Wages are never passive. If the filer is using FEIE (Form 2555) for the same wages, those excluded wages do NOT appear on Form 1116 at all — only the non-excluded portion shows up in general (d).

### Self-employment income from foreign clients

→ **General (d)**.

The income is "earned" in the country where the services are performed, not where the client is located. If the user performed services in Spain for a UK client, the income is Spain-source.

### Foreign rental income

→ **Passive (c)**, usually.

If the rental is part of an active trade or business (real estate dealer, hotel operator), it may move to general.

### Foreign capital gains

→ **Passive (c)**, usually.

Gains on sale of inventory or depreciable business property are general. Gain on a home abroad is foreign-source (real property is sourced where located, Pub. 514 Table 2) and is generally passive category income; ask a CPA before filing a large gain.

### Foreign royalties

→ **Passive (c)** for personal royalties (book royalties, music, etc.). General (d) if part of an active business.

### Foreign annuity / pension income

→ **Passive (c)** typically. Lump-sum distribution taxed using Form 4972 → category (g). Source: the part attributable to contributions is sourced where the services were performed; investment earnings are sourced where the pension trust is located (Pub. 514 Table 2).

### Income re-sourced by US treaty

→ **Category (f)** — Income that is US-source under domestic rules but treated as foreign source by a treaty sourcing rule, when the filer elects to apply the treaty. Use a separate Form 1116 for each treaty country, and Form 8833 may be required. The category does not apply to income re-sourced only by the relief-from-double-taxation article that applies to US citizens resident in the treaty country (2025 i1116, category f; IRC §865(h), §904(d)(6), §904(h)(10)).

This is highly treaty-specific. If the user has unusual cross-border income that they expect to be foreign-source via treaty, route to a CPA — not an automatic agent decision.

### Income from §901(j) sanctioned countries

→ **Category (e)**.

Sanctioned for 2025 per Pub. 514: **Iran, Libya (Presidential waiver for taxes arising after Dec 9, 2004), North Korea, Sudan, Syria**. Cuba's sanction period ended Dec 21, 2015 and Iraq's June 27, 2004 (Pub. 514 Table 1). Re-check the current Pub. 514 before filing. No credit is allowed for tax paid to a sanctioned country. Income from each sanctioned country goes on its own Form 1116 (box e), generally completed only through line 17. A residence-based tax paid to a non-sanctioned country on that income can still be credited (2025 i1116, category e).

### GILTI inclusion (US shareholders of CFCs)

→ **Category (a) §951A** (no carryover allowed; line 10 blank). If the individual made a §962 election, the credit for the CFC's taxes is claimed on Form 1118, not Form 1116.

Out of scope for typical retail filers. If the user is a controlled foreign corporation shareholder, route to a CPA with international expertise.

### Lump-sum retirement distribution

→ **Category (g)** when the filer elects Form 4972 for a foreign-source lump-sum pension distribution. Skip Part I and use the Worksheet for Lump-Sum Distributions for Part III (2025 i1116, category g). Most filers won't see this.

## Multi-basket filers

Common combinations:

- **Investor with US brokerage + foreign-employer wages**: passive (c) for 1099-DIV box 7 + general (d) for wages → 2 separate 1116s
- **Expat freelancer with passive interest + SE income**: passive (c) for interest + general (d) for SE income → 2 separate 1116s
- **Investor with normal foreign dividends + dividends from sanctioned-country shares**: passive (c) + §901(j) (e) → 2 separate 1116s

Each basket has its own §904 limitation. The credits combine on the summary 1116's Part IV.

## Country sourcing rules (where the income is "from")

Income source determines whether it goes on Form 1116 at all. Foreign-source rules (IRC §861-§865):

| Income type | Source rule |
|-------------|-------------|
| Wages | Where services are performed |
| SE income | Where services are performed |
| Interest | Residence of payor |
| Dividends | Country of incorporation of payor |
| Royalties | Where the property is used |
| Rental income | Where the property is located |
| Capital gain on real property | Where the property is located |
| Capital gain on personal property | Seller's tax home (with exceptions, Pub. 514) |
| Pension distributions | Contributions: where the services were performed; investment earnings: location of the pension trust |

If the user is uncertain, ask: "Where were the services performed?" or "Where is the property located?" — those facts drive the source rule.

## Edge cases the agent must surface

- **Working in country A while resident in country B**: income is country A source (services performed). The filer pays tax in country A (creditable) and possibly country B (also creditable, on the same income — possible double credit if both countries genuinely tax). Treaty relief may apply.
- **US-source income with foreign withholding**: not creditable as FTC. Pursue treaty refund from the source country.
- **Foreign income on partnership K-1**: the partnership reports foreign source / basket details on Schedule K-3. Filer aggregates to their personal Form 1116. K-3 gives basket-level breakdown; trust the partnership's classification or escalate to CPA.
- **Foreign mutual fund distributions**: typically passive. Watch for PFIC status (Form 8621) if the fund is a foreign mutual fund — separate filing with QEF or mark-to-market elections, out of scope.
- **Treaty tie-breaker resident**: if the filer is a tax resident of two countries and a treaty resolves the tie to the foreign country, US sourcing rules still apply for FTC; but the filer may also have Form 8833 disclosure requirements.
