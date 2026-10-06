# Foreign Currency Translation for Form 1116

Form 1116 reports income and tax in US dollars. The user must translate foreign currency to USD using a method that's:

- Consistent within a tax year
- Documented (audit-defensible)
- Aligned with Pub. 514, the 2025 Instructions for Form 1116 ("Foreign Currency Conversion"), and IRC §986(a) for foreign taxes

Attach to Form 1116 a detailed explanation of how each conversion rate was figured (2025 i1116).

## The two acceptable methods

### Method 1: Spot rate on the date of the transaction

For each foreign income receipt and each foreign tax payment, use the foreign-to-USD spot rate on that day. This is the IRS's general rule ("use the exchange rate prevailing, i.e., the spot rate, when you receive, pay or accrue the item") and the required rule for foreign taxes claimed on a paid basis.

**Pros**: most accurate; matches the user's actual experience.
**Cons**: laborious for many small transactions (e.g., monthly salary, frequent dividend distributions).

### Method 2: Yearly average exchange rate

Use the IRS's published yearly average rate for the currency, applied uniformly to income items in that currency for the year. The IRS has no official exchange rate and "generally accepts any posted exchange rate that is used consistently" (IRS yearly-average page). For foreign taxes, the yearly average is the rule only for taxes claimed on an accrued basis (below).

**Pros**: simple; one rate per currency per year.
**Cons**: smooths over within-year variation. May over- or under-state in volatile years.

The IRS publishes yearly average rates at:
**https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates**

The table lists units of foreign currency per US dollar: **divide** the foreign-currency amount by the rate to get dollars. The page is updated each year; verify before filing.

## Which method to use

### For taxes claimed on an accrual basis (Part II box (k) "Accrued")

- Use the **average exchange rate for the tax year to which the taxes relate** (2025 i1116; Pub. 514).
- Exceptions: use the rate on the payment date if the taxes are paid more than 2 years after the close of that tax year, paid before the tax year begins, or denominated in an inflationary currency (cumulative inflation of at least 30% over the 36 months before year-end). Accrued but unpaid inflationary-currency taxes use the rate on the last day of the US tax year.
- Election: an accrual-basis filer can elect to use the payment-date rate for taxes in a nonfunctional currency; the election applies to that year and all later years unless revoked with IRS consent, and is made by a statement on a timely return (including extensions).

### For taxes claimed on a cash basis (Part II box (j) "Paid")

- Use the **rate on the date paid**; for tax withheld, the rate on the date of withholding; for foreign estimated payments, the rate on the payment date (Pub. 514). Monthly payroll withholding means one rate per payday. A refund later received is translated at the rate in effect when the tax was paid.
- For income, use the **spot rate on the date received** OR a consistently used posted rate such as the **yearly average** — the user's choice, applied consistently to all income in that currency that year.

### For 1099-DIV box 7 (already in USD)

The broker already translated. Don't re-translate. Use the USD amount directly.

### For wages from a foreign employer

If the employer pays a fixed foreign-currency salary monthly, the user can translate the **income** either:

- Each paycheck at the spot rate that day, OR
- The annual total at the yearly average rate

The **tax withheld** from those paychecks, on a paid basis, is translated at each payday's rate (a 12-row worksheet), not at the yearly average.

## Where to find rates

### IRS yearly average rates

Pull from https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates. Sample rates from that page, units of foreign currency per US dollar (fetched 2026-10-06; verify before relying):

| Currency | 2025 | 2024 |
|----------|------|------|
| Euro | 0.886 | 0.924 |
| British pound | 0.759 | 0.783 |
| Japanese yen | 149.632 | 151.353 |
| Canadian dollar | 1.398 | 1.370 |
| Singapore dollar | 1.307 | 1.336 |

Divide: €10,000 ÷ 0.886 = $11,287 (2025). **Always pull the IRS page for the actual year being filed**.

### Spot rates

Several acceptable sources:

- US Treasury Reporting Rates of Exchange (https://fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/) — published quarterly
- Federal Reserve H.10 release — daily
- European Central Bank euro reference rates — daily (cross rates for non-euro pairs)
- OANDA, XE.com, Reuters — daily commercial sources, accepted by IRS
- The user's bank or broker statement — if they actually exchanged the currency

The IRS doesn't mandate one source. Pick a reputable one and stick with it for the year.

## Worked examples

### Example 1: Expat in Germany, EUR salary, accrual method

Filer earned €120,000 EUR salary in 2024, paid €38,500 EUR German income tax (withheld monthly), and claims the credit on an **accrued** basis (box (k)); all tax was paid during 2024.

- IRS 2024 yearly average EUR rate: 0.924 euros per dollar
- Income (Line 1a): 120,000 ÷ 0.924 = **$129,870 USD**
- Foreign tax (Line 8): 38,500 ÷ 0.924 = **$41,667 USD** (yearly average allowed because the taxes are accrued and paid within the 24-month window)

On a **paid** basis the same €38,500 would instead be translated at each monthly payday's rate.

### Example 2: Investor with Canadian dividend, cash method

Filer received CAD $5,000 dividend from a Canadian stock on March 15, 2024. Canadian withholding tax was CAD $750 (15% treaty rate). Both translated at the spot rate on March 15, 2024: ECB reference rates that day were USD 1.0892 and CAD 1.4731 per euro, so 1 CAD = 1.0892 ÷ 1.4731 = $0.7394 USD.

- Income (Line 1a): 5,000 × 0.7394 = **$3,697 USD**
- Foreign tax (Line 8): 750 × 0.7394 = **$555 USD**

If the broker (Schwab, Fidelity, etc.) already reported these in USD on the 1099-DIV, use the broker's number — they translated.

### Example 3: Mid-year move — UK to Singapore

Filer moved from UK to Singapore on July 1, 2024.

- Jan-Jun: GBP 35,000 wages, GBP 5,250 UK PAYE tax
- Jul-Dec: SGD 80,000 wages, SGD 6,000 Singapore tax

Translate each currency separately using its IRS 2024 yearly average (the tax figures assume an accrued-basis filer; a paid-basis filer translates each tax payment at its payment-date rate):

- 2024 GBP yearly average 0.783 → £35,000 ÷ 0.783 = $44,700 wages; £5,250 ÷ 0.783 = $6,705 tax
- 2024 SGD yearly average 1.336 → S$80,000 ÷ 1.336 = $59,880 wages; S$6,000 ÷ 1.336 = $4,491 tax

Aggregate: $104,580 wages, $11,196 foreign tax — both flow to general basket Form 1116 with country columns A=UK, B=Singapore.

## What the agent should do

1. **Ask** the user which method they want to use for income — spot or yearly average — and whether foreign taxes are claimed paid or accrued (that choice fixes the tax-translation rule)
2. **Pull** the IRS yearly average rates (and, for paid-basis taxes, the payment-date spot rates) for the relevant currencies and tax year
3. **Translate** each item using the chosen method, document the rate source
4. **Show the math** in the deliverable so a CPA could re-derive

If the user has multiple currencies, translate each separately. Don't aggregate currencies first.

## Edge cases

### Functional currency rules (§985)

A US individual's functional currency is USD (Reg. §1.985-1). All translations are TO USD. Foreign-currency-denominated bank accounts may generate §988 gain or loss when balances move — separate issue, not on Form 1116.

### Accrued tax paid at a different amount or date (Reg. §1.905-3)

On an accrual basis, a foreign tax redetermination occurs when the tax paid differs from the amount accrued, when accrued tax isn't paid within 24 months after the close of the year it relates to, or when it is refunded. For taxes accrued but translated at the payment-date rate, an exchange-rate-only difference needs no redetermination if it is less than the smaller of $10,000 or 2% of the tax initially accrued for that country; the US tax is adjusted in the year paid instead. Otherwise file an amended return with a revised Form 1116 and Schedule C (Form 1116) (2025 i1116, "Foreign Tax Redeterminations").

### Inflationary and hyperinflationary currencies

For accrued foreign taxes, a currency is inflationary if cumulative inflation over the 36 months before year-end is at least 30% (2025 i1116); those taxes use the payment-date rate. Separate functional-currency rules apply to QBUs in hyperinflationary economies (Reg. §1.985-1, §1.985-3). Out of scope for this skill; route to CPA.

### Cryptocurrency-denominated foreign income

If the user is paid in crypto for services performed abroad, treat as a foreign-currency receipt. Use the USD value at the time of receipt (spot price on the day). Source rules still apply — wages are sourced where services are performed.
