# Recapture and Character on Form 6252

How depreciation recapture, unrecaptured §1250 gain, and the character of installment gain interact with Form 6252. Sources: 2025 Form 6252 and its instructions (https://www.irs.gov/pub/irs-pdf/f6252.pdf), 2025 Form 4797 and instructions, Pub. 537 (2025) "Depreciation Recapture Income," and the 2025 Instructions for Schedule D, Unrecaptured Section 1250 Gain Worksheet.

## Rule 1 — Recapture is taxed in the year of sale, before any installment computation

Pub. 537: "If you sell property for which you claimed or could have claimed a depreciation deduction, you must report any depreciation recapture income in the year of sale, whether or not an installment payment was received that year." Form 6252 instructions, line 12: ordinary income recapture under §1245 or §1250 (including §179 and §291) "is fully taxable in the year of sale even if no payments were received."

Order of work in the year of sale:

1. Complete **Form 4797, Part III** for the property (lines 19–29b). For individuals and pass-through owners the recapture components are line 25b (§1245) and line 26g (§1250).
2. Form 4797 **line 31** for this property = Form 6252 **line 12**. Enter the same amount on Form 4797 **line 13** (ordinary gain in Part II).
3. Do not enter gain for this property on Form 4797 line 32. If Form 4797 was used only to figure line 12, write "N/A" on Form 4797 line 32.
4. Line 12 joins line 13 (installment sale basis), so recapture is excluded from gross profit and is not taxed a second time as payments arrive (Pub. 537: "The recapture income reported in the year of sale is included in your installment sale basis in determining your gross profit").

Never ask whether to defer recapture. It is not optional.

### Straight-line §1250 property owned by an individual

Form 4797 line 26 text: "If straight line depreciation was used, enter -0- on line 26g, except for a corporation subject to section 291." Residential rental and nonresidential real property placed in service after 1986 is depreciated straight line under MACRS, so line 12 is usually **0** for an individual's rental building. The depreciation does not disappear: it becomes **unrecaptured §1250 gain** (Rule 3). Pub. 537's "Sale of a Business" example states the same: the building "is section 1250 property. There's no depreciation recapture income because the building was depreciated using the straight line method."

A corporation subject to §291 has a §291 amount on Form 4797 line 26f; route that through [`../../form-1120/SKILL.md`](../../form-1120/SKILL.md).

### When all of the gain is recapture

If recapture equals the whole gain, line 14 is zero and Form 6252 is not filed (line 14 instructions). The entire sale goes on Form 4797 in the year of sale even if the buyer pays over several years.

Worked check (non-round numbers):

```
Equipment cost $18,640, fully expensed under §179 → depreciation allowed $18,640
Sold for $6,215; selling expenses $310

Form 4797 Part III: line 20 = 6,215; line 21 = 18,640 + 310 = 18,950;
  line 22 = 18,640; line 23 = 310; line 24 = 5,905; line 25a = 18,640; line 25b = 5,905
Form 6252: line 10 = 0; line 11 = 310; line 12 = 5,905; line 13 = 6,215;
  line 14 = 6,215 − 6,215 = 0  → no Form 6252
```

### When gain exceeds recapture

```
Truck cost $41,300; depreciation allowed $27,730; sold for $44,950; selling expenses $1,120

Form 4797 Part III: line 21 = 42,420; line 23 = 14,690; line 24 = 30,260;
  line 25b = smaller of 30,260 or 27,730 = 27,730 (recapture, year of sale)
Form 6252: line 10 = 13,570; line 11 = 1,120; line 12 = 27,730; line 13 = 42,420;
  line 14 = 2,530 (= 30,260 − 27,730); with no assumed debt line 18 = 44,950;
  line 19 = 2,530 ÷ 44,950 = 0.05628 → 0.0563
```

Only $2,530 is spread over the payments; $27,730 is ordinary income in the year of sale. Make sure the user can pay tax on recapture in a year when little cash may have arrived.

## Rule 2 — Line 25 is for §1252, §1254, §1255 recapture, limited each year

Form 6252 instructions, line 25: enter (and on Form 4797 line 15) ordinary income recapture on §1252 (farmland soil, water, land clearing), §1254 (intangible drilling, mine development, depletion), or §1255 (excluded cost-sharing payments) property "for the year of sale or all remaining recapture from a prior year sale." In the year of sale, the recapture amount comes from Form 4797 line 27c, 28b, or 29b; do not enter gain for this property on Form 4797 line 31 or 32 ("N/A" on both if Form 4797 was only used for this).

Limit: "Don't enter on line 25 more than the amount shown on line 24. Any excess must be reported in future years on Form 6252 up to the taxable part of the installment sale until all of the recapture has been reported." So this recapture follows the payments, unlike §1245/§1250 recapture on line 12. Never put §179 ordinary income on line 25.

Line 25 also carries remaining recapture on §1245 or §1250 property sold before June 7, 1984. Line 36 follows the same rules for Part III.

## Rule 3 — Unrecaptured §1250 gain on installment payments is reported first

For §1250 property held more than 1 year, the portion of each year's line 26 that is unrecaptured §1250 gain is figured on the **Unrecaptured Section 1250 Gain Worksheet, line 4**, in the 2025 Instructions for Schedule D:

- **Step 1.** The smaller of (a) depreciation allowed or allowable or (b) the total gain for the sale. "This is the smaller of line 22 or line 24 of your 2025 Form 4797 (or the comparable lines of Form 4797 for the year of sale)."
- **Step 2.** Reduce by §1250 ordinary income recapture (Form 4797 line 26g). The result is the total unrecaptured §1250 gain to allocate to the installment payments.
- **Step 3.** "Generally, the entire amount of gain from the sale of trade or business property included in each installment payment is treated as unrecaptured section 1250 gain until the total unrecaptured section 1250 gain figured in Step 2 has been used in full." Each year's amount is the smaller of that year's Form 6252 line 26 (or line 37) or the unrecaptured §1250 gain remaining.

Track the running balance in the multi-year schedule of the deliverable. Unrecaptured §1250 gain is taxed at a maximum rate of 25% (IRC §1(h)(1)(E)); the Schedule D worksheet result goes to Schedule D line 19. Gain reported after the balance is used up is the remaining §1231 gain, still flowing through Form 4797 line 4 and Part I.

An installment sale of §1250 property for which the year-of-sale return had no Form 4797 Part I entry uses worksheet line 12 instead (Schedule D instructions, "Line 12. ... Installment sales"); apply the same three steps.

This matches the sibling skill's treatment of §1250 property: [`../../form-4797/references/section-1250-recapture.md`](../../form-4797/references/section-1250-recapture.md).

## Rule 4 — Character follows the property, every year

Pub. 537 ("Other forms"): "If your gain from the installment sale qualifies for long-term capital gain treatment in the year of sale, it will continue to qualify in later tax years. Your gain is long term if you owned the property for more than 1 year when you sold it."

Routing of line 26 (and line 37):

| Property | Holding period | Destination |
|----------|----------------|-------------|
| Trade or business property (including rental property) | More than 1 year | Form 4797 line 4 (§1231 gain from installment sales) |
| Trade or business property, or ordinary gain from a noncapital asset | 1 year or less (or any period, for ordinary gain) | Form 4797 line 10, "From Form 6252" |
| Capital asset (investment land, personal-use property, stock not publicly traded) | More than 1 year | Schedule D line 11 |
| Capital asset | 1 year or less | Schedule D line 4 |

A §1231 gain arriving on Form 4797 line 4 is netted with the year's other §1231 items and the 5-year lookback on Form 4797 line 8 in the year the payment is received (handled by [`../../form-4797/SKILL.md`](../../form-4797/SKILL.md)).

Interest is never part of this character analysis: it is ordinary interest income on Schedule B in the year received or accrued (Pub. 537, "Interest Income").

## Rule 5 — Main home sold on installments

Line 15 takes the §121 exclusion. Pub. 537 ("Sale of your home"): "If the sale is an installment sale, any gain you exclude isn't included in gross profit when figuring your gross profit percentage." Compute the excludable amount with Pub. 523 (https://www.irs.gov/pub/irs-pdf/p523.pdf) and ask the user for the ownership and use facts; do not assume the exclusion applies. If part of the home was used for business or rental after May 6, 1997, Pub. 523 says gain equal to that depreciation cannot be excluded; flag it for the CPA.

When the buyer of a main home is an individual paying on a seller-financed mortgage, the seller enters the buyer's name, address, and SSN on Schedule B line 1 when reporting the interest (Pub. 537, "Seller-financed mortgage").

## Rule 6 — Partnerships and S corporations

The Form 6252 line 12 instructions send partnerships, S corporations, and their partners and shareholders to the Instructions for Form 4797 for how recapture on an installment sale is handled. A partner or shareholder whose K-1 reports an installment sale uses the K-1 information; route the entity-level work to [`../../form-1065/SKILL.md`](../../form-1065/SKILL.md) or [`../../form-1120-s/SKILL.md`](../../form-1120-s/SKILL.md).

Sale of a partnership interest: gain allocable to unrealized receivables and inventory cannot be reported on the installment method; the rest can (Pub. 537, "Sale of Partnership Interest"). Ask the partnership for the §751 allocation before building Form 6252.
