# Form 1116 Line-by-Line Reference

Complete lookup for every line on Form 1116. Use when the agent needs to confirm where a number belongs or what a line means. One Form 1116 covers exactly one income category (basket); separate forms for each basket the user has.

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name | Filer's legal name | Match Form 1040 |
| (top) | SSN/ITIN | Filer's identifier | Or trust EIN if Form 1041 |
| a | §951A category (GILTI) | Checkbox | Rare for individuals; mostly CFC shareholders |
| b | Foreign branch category | Checkbox | Post-TCJA; mostly business filers |
| c | Passive category income | Checkbox | Most 1099-DIV/INT box 7 income |
| d | General category income | Checkbox | Wages, SE, business income |
| e | §901(j) sanctioned country | Checkbox | Currently Iran, North Korea, Sudan; verify list |
| f | Income re-sourced by treaty | Checkbox | Treaty-specific reclassification |
| g | Lump-sum distributions | Checkbox | Qualified retirement distribution |
| h | Paid OR Accrued | Radio | Accrual election binding for future years (IRC §905(a)) |
| i | Resident country code | 2-letter ISO code | Use IRS country code list |

Only one of a-g is checked per Form 1116. If the filer has income in multiple baskets, file one Form 1116 per basket.

---

## Part I — Foreign-source taxable income (this category)

### Line 1a — Gross income from sources outside the US

Per-country columns (A, B, C). Each column gets the gross foreign-source income from that country, in this category, in USD.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Foreign wages (general basket) | US-source wages even if paid by a foreign employer (treaty-based sourcing rules apply) |
| Foreign dividends, interest (passive) | US-source dividends from a US company (no FTC) |
| Foreign rental net income (passive) | Foreign income excluded under §911 (FEIE — must NOT appear here) |
| Foreign capital gains (passive) | Income re-sourced by treaty (basket f, separate 1116) |
| Foreign royalties (passive, usually) | |
| Foreign SE income (general) | |

**Critical**: If the filer used Form 2555 to exclude wage income, the excluded amount does NOT go on Line 1a. Only the non-excluded portion appears here.

### Line 1b — Compensation for services performed abroad

Subset of Line 1a. Only fill if the filer has wages on Line 1a; this line breaks out the compensation portion.

### Line 2 — Definitely related deductions

Deductions definitely related to the income on Line 1a.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| Investment expenses tied to foreign dividends (custodian fees) | Investment expenses tied to US dividends |
| Foreign business expenses (Schedule C reductions for foreign SE income) | Domestic business expenses |
| Allocable depreciation on foreign-used assets | |

### Line 3a — Itemized or standard deduction (pro-rata portion)

Deductions not definitely related — they get apportioned.

- If itemizing: enter Schedule A total (less items already on Line 2 or Line 4)
- If standard deduction: enter the standard deduction amount

### Line 3b — Other deductions (not definitely related)

Charitable contributions if itemizing; certain above-the-line deductions if not specifically allocable.

### Line 3c — Sum of 3a + 3b

### Line 3d — Gross foreign-source income (this category, all countries)

This is the same as the sum across columns on Line 1a (less any exclusions).

### Line 3e — Gross income from all sources

Worldwide gross income — total income before deductions, US + foreign.

### Line 3f — Allocation ratio = 3d ÷ 3e

Round to 6 decimal places. This is the share of pro-rata deductions allocated to foreign-source income.

### Line 3g — 3c × 3f

The foreign share of pro-rata deductions.

### Line 4a — Home mortgage interest

If itemizing and the user has a home mortgage, the interest is allocated under Reg. §1.861-9. Most individuals use the asset method (not gross income method) — see Pub. 514 for the worked formula.

### Line 4b — Allocated to foreign sources

The foreign-source allocation of Line 4a.

### Line 5 — Losses from foreign sources

Foreign-source losses reduce this basket's income. Net losses across all baskets recharacterize income in later years per IRC §904(f). For most individual filers without complex loss-carryover situations, this line is 0.

### Line 6 — Total deductions

= Line 2 + Line 3g + Line 4b + Line 5

### Line 7 — Foreign-source taxable income

= Line 1a − Line 6

This is the numerator of the §904 limitation fraction.

---

## Part II — Foreign taxes paid or accrued

Two-block structure: foreign taxes withheld at source on (A) dividends, (B) rents/royalties, (C) interest, (D) other; plus a separate "Other foreign taxes paid or accrued" block. By country letter.

| Column | What goes here |
|--------|---------------|
| Country code | Country letter from Part I header |
| Date paid OR accrued | If "Paid" elected: the actual payment date. If "Accrued": the year-end date. |
| Foreign currency | Original currency amount |
| Conversion rate | Spot rate (paid) or yearly average (accrued) |
| In US dollars | The translated USD amount |

### Line 8 — Total foreign taxes

Sum of all USD amounts. This is the total creditable foreign tax for this basket this year.

**Foreign taxes that do NOT go on Line 8**:

- Foreign penalties or interest on tax (not creditable per IRC §901(b))
- Withholding on US-source income (not foreign tax)
- Taxes voluntarily paid above legal liability (over-withholding the user could refund)
- Soak-up taxes that depend on FTC availability (Reg. §1.901-2(c))
- Foreign value-added tax (VAT, GST) on consumption — not an income tax
- Foreign social security tax IF the country has a Totalization Agreement with the US (split between countries)

See [`non-creditable-taxes.md`](./non-creditable-taxes.md) for the full list.

---

## Part III — Computing the credit (the §904 limitation)

### Line 9 — Foreign taxes (= Line 8)

### Line 10 — Carryback / carryforward

Prior-year unused FTC for this basket. Carryback 1 year + carryforward 10 years (IRC §904(c)). The user must track this manually across years; the IRS doesn't compute it.

### Line 11 — Total available

= Line 9 + Line 10

### Line 12 — Reduction in foreign taxes (boycott)

If the filer participated in an international boycott (IRC §999), reduce here. Almost always 0 for individuals.

### Line 13 — Net foreign taxes available

= Line 11 − Line 12

### Line 14 — Foreign-source taxable income (= Line 7)

### Line 15 — Adjustments

The qualified-dividend / long-term capital gain rate adjustment. When the filer has foreign QD or LTCG taxed at preferential US rates (0%/15%/20%), the §904 limitation must be adjusted downward to prevent over-claiming the credit (the foreign income is already getting a US rate benefit).

Mechanics: multiply foreign QD / LTCG by a ratio based on the rate differential, and subtract from Line 14. See [`qualified-dividend-adjustment.md`](./qualified-dividend-adjustment.md) for the worked formula.

If the user has no QD or LTCG (or the de-minimis exemption applies — under $20,000 of foreign QD+LTCG in some years), Line 15 is 0.

### Line 16 — (reserved)

### Line 17 — Adjusted foreign-source taxable income

= Line 14 − Line 15

### Line 18 — Total taxable income

From Form 1040 Line 15 (with adjustments). For 2025/2026, this is the line where the IRS asks for the user's worldwide taxable income before personal exemption (no longer applicable post-TCJA, but the form line still says "before personal exemption" historically).

### Line 19 — Limitation ratio

= Line 17 ÷ Line 18, rounded to 6 decimals, capped at 1.000000.

### Line 20 — Limitation amount

= Line 19 × Form 1040 tax before credits (Line 16 of the 1040, with §904(b)(2) adjustments)

### Line 21 — Foreign tax credit, this category

= Lesser of Line 13 or Line 20.

If Line 13 > Line 20: the user has unused FTC for this basket. The excess carries back 1 year (file an amended return for the prior year if the prior year had limitation room) and carries forward 10 years (IRC §904(c)).

---

## Part IV — Summary (only on the summary 1116 if multiple baskets)

When the user has multiple baskets, each basket's 1116 contains Lines 1-21. ONE of those 1116s is designated the "summary" and contains Part IV.

### Lines 22-32 — Credits from separate Parts III

Enter Line 21 from each basket's 1116 here, by basket.

### Line 33 — Total credit

Sum of Lines 22-32.

### Line 34 — (reduction; rare for individuals)

### Line 35 — Final FTC

= Smaller of Line 33 or US tax before credits (Form 1040 Line 16).

This is the number that goes on **Schedule 3 Line 1** of Form 1040 — the actual FTC the filer claims.

---

## Special situations

### High-tax kickout (HTK)

Income that would normally be passive but bears foreign tax at a high rate is "kicked out" of the passive basket and reclassified as general (IRC §904(d)(2)(F), Reg. §1.904-4(c)). High-tax means foreign tax exceeds the highest US tax rate that would apply to the income. For passive dividends taxed at, say, 30% in source country, this rule may apply.

When HTK applies, the income moves from the passive 1116 to the general 1116. This often surprises filers because their broker categorized it as passive on the 1099. The agent should ask whether any foreign passive income bore foreign tax above the US qualified-dividend rate; if so, evaluate HTK.

### Lookthrough rules for CFC dividends

Dividends from CFCs (§1248) and certain partnerships look through to the underlying basket of the entity's income. Most retail individual filers don't encounter this; route to a CPA.

### §904(f) overall foreign loss recapture

If the filer had a net foreign-source loss in a prior year that reduced US-source income, later foreign-source income gets recharacterized as US-source until the loss is recovered. Track the §904(f) account. Out of scope for this skill; CPA referral.

### Estate / trust filers

Form 1116 attaches to Form 1041 instead of 1040. The §904 limitation uses the trust/estate's taxable income; otherwise mechanics are similar. Distributable net income (DNI) considerations may shift the credit to beneficiaries via Schedule K-1.
