# Foreign Taxes That Do NOT Qualify for FTC

Not every foreign tax the user paid can go on Form 1116 Line 8 (Part II). The 2025 Instructions for Form 1116 list the main exclusions under "Foreign Taxes Not Eligible for a Credit." The IRS has specific rules about what qualifies as a "creditable" foreign income tax under IRC §901 and Reg. §1.901-2. A tax that fails these tests is not creditable as FTC, though it may be deductible elsewhere or recoverable from the foreign country.

## The §901 creditability tests

A foreign tax is creditable only if it is:

1. **A tax** (compulsory payment under foreign law, not a fee for services)
2. **An income tax in the US sense** (computed on net income or a reasonable proxy)
3. **Paid to a foreign country** (not to a US state or political subdivision)
4. **The legal liability of the US filer** (not someone else's tax the filer happened to pay)

A tax that fails any of these is NOT creditable. The foreign-tax-paid number on Line 8 should exclude all of the following.

## Common non-creditable items

### Foreign Value-Added Tax (VAT) / Goods and Services Tax (GST)

VAT and GST are consumption taxes, not income taxes. **Not creditable.** They can be expensed as part of business expenses on Schedule C if the underlying purchase is deductible.

Examples: UK VAT (20%), German Mehrwertsteuer (19%), Canadian HST/GST.

### Foreign property tax

Tax on the value of property is not an income tax. **Not creditable.** Foreign real and personal property taxes are not deductible on Schedule A (2025 Schedule A instructions, "Taxes You Can't Deduct"); property tax on a foreign rental property is a rental expense on Schedule E.

### Foreign sales tax

Same logic as VAT. **Not creditable.**

### Foreign social security tax (in totalization agreement countries)

If the US has a social security (totalization) agreement with the foreign country, the user generally pays social security tax to only one country. **No credit or deduction is allowed** for social security taxes paid or accrued to a country with which the US has such an agreement (Pub. 514, "Pension, unemployment, and disability fund payments"). The agreement prevents dual coverage; it does not create an offset on Schedule SE.

Countries with US social security agreements (list from the 2025 Instructions for Schedule SE; verify current list at SSA.gov before relying):
Australia, Austria, Belgium, Brazil, Canada, Chile, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Japan, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Slovenia, South Korea, Spain, Sweden, Switzerland, United Kingdom, Uruguay.

If the user worked in a country WITHOUT an agreement (e.g., Vietnam, Thailand, most of South America outside Brazil/Chile/Uruguay), a foreign tax that funds retirement, unemployment, illness, or disability benefits is not treated as payment for a specific economic benefit if the amount doesn't depend on the individual's age or life expectancy (Pub. 514). It is creditable only if it also meets the net income tax requirements of Reg. §1.901-2. ASK for the foreign payslip or assessment and treat it as a CPA question if material.

### Foreign penalties and interest

Late-filing penalties, interest on tax assessments — **not creditable.** They're not "tax" under IRC §901.

### Withholding on US-source income

If a foreign country withheld tax on income that is US-source under US sourcing rules (e.g., a foreign country withheld on a dividend from a US corporation), that withholding is NOT creditable. The user must pursue a refund from the foreign country (often via tax treaty mechanism — Form 8233 equivalent in the foreign country).

### Voluntary tax (over-withholding the user could refund)

If the user could have claimed a treaty rate (typically 15% on dividends) but took the higher statutory rate (often 30%) by not filing the right form abroad, the excess is NOT creditable. The user is expected to claim the treaty benefit at source. Per Reg. §1.901-2(e)(5).

Example: filer holds Spanish dividend stock. Spain's statutory withholding is 19%; the US-Spain treaty rate is 15%. If the broker withheld 19% because the user didn't file the treaty residence certificate, only 15% is creditable. The 4% excess must be refunded by Spain (Form 210 or treaty claim) or written off.

### Soak-up taxes

Per Reg. §1.901-2(c), a soak-up tax is one whose liability depends on the availability of an FTC in the user's home country. Some countries have provisions that effectively shift tax burden depending on whether the foreign country credits — these are NOT creditable. Rare for individual filers.

### Foreign tax on income excluded under §911 (FEIE)

If the user excluded wages under FEIE (Form 2555), the foreign tax allocable to the EXCLUDED portion is NOT creditable. See [`coordination-with-2555.md`](./coordination-with-2555.md) for the allocation formula.

### Refunded or refundable foreign tax

Tax that was paid but refunded (or refundable) doesn't count. If a refund is received in a later year, that is a foreign tax redetermination: the user files an amended return (Form 1040-X) with a revised Form 1116 for the year the credit was claimed, plus Schedule C (Form 1116) with the current-year return (2025 i1116, "Foreign Tax Redeterminations"; Reg. §1.905-3).

### Withholding on income from §901(j) sanctioned countries

Tax paid to a sanctioned country (2025 Pub. 514 list: Iran, Libya with a Presidential waiver since Dec 10, 2004, North Korea, Sudan, Syria) is **not creditable at all**. The income from that country goes on a separate category e Form 1116, generally completed only through line 17. The tax may be deductible instead (2025 i1116, "Credit or Deduction").

### Short holding period or related payments

Foreign tax withheld on a dividend is not creditable if the stock wasn't held at least 16 days within the 31-day period that begins 15 days before the ex-dividend date (longer for certain preferred stock), or to the extent the user must make related payments on substantially similar property. The same 16-day rule applies to withholding on other income from property (IRC §901(k), §901(l); 2025 i1116, items 5-8). These taxes can be deducted instead.

## Items that ARE creditable (commonly overlooked)

For contrast, these typically ARE creditable:

- Foreign income tax withheld at source on dividends / interest / royalties (subject to treaty rate maximum)
- Foreign income tax on wages or salary (income tax portion, not SS-equivalent)
- Foreign self-employment income tax (income tax portion)
- Foreign capital gains tax
- Tax computed on a reasonable proxy of net income (some countries use turnover-based or asset-based taxes that qualify under Reg. §1.903-1)
- Tax paid in a country WITHOUT a social security agreement that includes both income and social-insurance portions — the income portion is creditable; the social-insurance portion is creditable only if it meets the Reg. §1.901-2 net income tax requirements (Pub. 514)

## What the agent should do

When the user reports a foreign tax amount, ASK:

1. "What kind of tax is it? Income tax, VAT, social security, property tax?"
2. "Is the source income US-source or foreign-source?" (foreign country may have withheld on US-source income)
3. "Was any portion refunded or refundable?"
4. "Did you claim treaty-rate withholding, or the statutory rate?" (excess over treaty rate is non-creditable)
5. "Does the country have a US Totalization Agreement?" (for SS-equivalent)
6. "Was any portion related to FEIE-excluded income?" (allocate out)

Document the answers. Only the creditable income-tax portion goes on Form 1116 Line 8.

## Documentation the user must retain

For audit defense (FTC carryforwards last 10 years; the IRS may audit any open year):

- Foreign tax payment receipts or foreign tax return
- Translation to USD with the rate source documented (yearly average vs. spot)
- Allocation memos if the user split tax between excluded and non-excluded income
- Treaty residence certificates if they claimed reduced withholding

## Where non-creditable taxes go instead

- VAT / GST on business purchases → Schedule C as part of the cost
- Foreign property tax (rental) → Schedule E
- Foreign property tax (personal residence) → not deductible (2025 Schedule A instructions list foreign personal or real property taxes under "Taxes You Can't Deduct")
- Foreign social security tax (agreement country) → no credit and no deduction (Pub. 514)
- Foreign social security tax (non-agreement country) that fails the net income tax test → ask a CPA whether any deduction is available
- Creditable foreign income taxes the user chooses to deduct instead → Schedule A line 6 (all-or-nothing for the year)
