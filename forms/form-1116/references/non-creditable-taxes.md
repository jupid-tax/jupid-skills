# Foreign Taxes That Do NOT Qualify for FTC

Not every foreign tax the user paid can go on Form 1116 Line 8. The IRS has specific rules about what qualifies as a "creditable" foreign income tax under IRC §901 and Reg. §1.901-2. A tax that fails these tests is not creditable as FTC, though it may be deductible elsewhere or recoverable from the foreign country.

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

Tax on the value of property is not an income tax. **Not creditable.** Deductible on Schedule A if itemizing (subject to SALT cap), or deductible on Schedule E for rental property.

### Foreign sales tax

Same logic as VAT. **Not creditable.**

### Foreign social security tax (in totalization agreement countries)

If the US has a Totalization Agreement with the foreign country, the user typically pays SS tax in only ONE country (per the "detached worker" rules). The tax paid abroad under such an agreement is the equivalent of US Social Security and Medicare tax — **not creditable as FTC** (it offsets US SE tax instead, via Schedule SE).

Countries with US Totalization Agreements (verify current list at SSA.gov before relying):
Australia, Austria, Belgium, Brazil, Canada, Chile, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Japan, Luxembourg, Netherlands, Norway, Poland, Portugal, Slovak Republic, Slovenia, South Korea, Spain, Sweden, Switzerland, United Kingdom, Uruguay.

If the user worked in a country WITHOUT a Totalization Agreement (e.g., Vietnam, Thailand, most of South America outside Brazil/Chile/Uruguay), the foreign SS-equivalent tax may or may not be creditable depending on whether it's structured as an income tax.

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

Tax that was paid but refunded (or refundable) doesn't count. If a refund is received in a later year, the user must file Form 1116 for the refund year reflecting the recovery (or amend the original year). Reg. §1.905-3.

### Withholding on income from §901(j) sanctioned countries

Tax paid to a sanctioned country (Iran, North Korea, Sudan currently) is creditable only on a separate §901(j) basket Form 1116 with stricter limitation. It does NOT go in the passive or general basket.

## Items that ARE creditable (commonly overlooked)

For contrast, these typically ARE creditable:

- Foreign income tax withheld at source on dividends / interest / royalties (subject to treaty rate maximum)
- Foreign income tax on wages or salary (income tax portion, not SS-equivalent)
- Foreign self-employment income tax (income tax portion)
- Foreign capital gains tax
- Tax computed on a reasonable proxy of net income (some countries use turnover-based or asset-based taxes that qualify under Reg. §1.903-1)
- Tax paid in a country WITHOUT a Totalization Agreement that includes both income and SS portions — the income portion is creditable; the SS portion is NOT creditable but may not have an offset either (the user pays both US SE tax and foreign SS tax; this is the cost of working in a non-Totalization country)

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
- Foreign property tax (personal residence) → Schedule A subject to $10,000 SALT cap (or post-2026 cap as applicable)
- Foreign SS-equivalent tax (Totalization country) → no US deduction; offsets via the agreement
- Foreign SS-equivalent tax (non-Totalization, paid on top of US SE tax) → no US offset; ask CPA about §164 deduction availability for trade/business
