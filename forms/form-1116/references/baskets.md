# Form 1116 Baskets (Income Categories)

Each Form 1116 covers exactly one category of foreign-source income. The filer files a separate 1116 per category. Picking the wrong basket is the most common Form 1116 error — the credit gets capped against the wrong limitation, and the IRS may reject or recompute on audit.

## The seven categories (IRC §904(d) and Reg. §1.904-4)

| Box | Category | Typical income |
|-----|----------|---------------|
| a | §951A category (GILTI) | GILTI inclusion — CFC shareholders, individual electing §962 |
| b | Foreign branch category | Income of a foreign branch of a US business (post-TCJA) |
| c | Passive category | Dividends, interest, royalties, rents, capital gains, annuities |
| d | General category | Wages, SE income, business income — anything not in another box |
| e | §901(j) category | Income from sanctioned countries |
| f | Income re-sourced by treaty | Treaty reclassifies the income source |
| g | Lump-sum distributions | Qualified retirement lump-sum distribution |

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

Gains on sale of inventory or business assets are general. Gains on personal-use property are personal (no FTC at all).

### Foreign royalties

→ **Passive (c)** for personal royalties (book royalties, music, etc.). General (d) if part of an active business.

### Foreign annuity / pension income

→ **Passive (c)** typically. Lump-sum qualified retirement distribution → category (g).

### Income re-sourced by US treaty

→ **Category (f)** — Income that is technically US-source under domestic rules but re-sourced as foreign under a US tax treaty (e.g., gain on disposition of US real estate by a non-resident under certain treaties).

This is highly treaty-specific. If the user has unusual cross-border income that they expect to be foreign-source via treaty, route to a CPA — not an automatic agent decision.

### Income from §901(j) sanctioned countries

→ **Category (e)**.

Currently sanctioned (verify against the latest IRS list before filing): **Iran, North Korea, Sudan**. Cuba was on the list and was removed; the list changes by Executive Order. Foreign tax paid to a §901(j) country is NOT creditable as a normal FTC; it goes on category (e) with stricter limitation.

### GILTI inclusion (CFC shareholders electing §962)

→ **Category (a) §951A**.

Out of scope for typical retail filers. If the user is a controlled foreign corporation shareholder, route to a CPA with international expertise.

### Lump-sum retirement distribution

→ **Category (g)**.

Special rules apply for certain pre-1974 distributions. Most filers won't see this.

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
| Capital gain on personal property | Residence of seller (with exceptions) |
| Pension / annuity | Where services were performed (for the underlying employment) |

If the user is uncertain, ask: "Where were the services performed?" or "Where is the property located?" — those facts drive the source rule.

## Edge cases the agent must surface

- **Working in country A while resident in country B**: income is country A source (services performed). The filer pays tax in country A (creditable) and possibly country B (also creditable, on the same income — possible double credit if both countries genuinely tax). Treaty relief may apply.
- **US-source income with foreign withholding**: not creditable as FTC. Pursue treaty refund from the source country.
- **Foreign income on partnership K-1**: the partnership reports foreign source / basket details on Schedule K-3. Filer aggregates to their personal Form 1116. K-3 gives basket-level breakdown; trust the partnership's classification or escalate to CPA.
- **Foreign mutual fund distributions**: typically passive. Watch for PFIC status (Form 8621) if the fund is a foreign mutual fund — separate filing with QEF or mark-to-market elections, out of scope.
- **Treaty tie-breaker resident**: if the filer is a tax resident of two countries and a treaty resolves the tie to the foreign country, US sourcing rules still apply for FTC; but the filer may also have Form 8833 disclosure requirements.
