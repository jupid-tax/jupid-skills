# Foreign Currency Translation for Form 1116

Form 1116 reports income and tax in US dollars. The user must translate foreign currency to USD using a method that's:

- Consistent within a tax year
- Documented (audit-defensible)
- Aligned with IRS rules in Reg. §1.985-3 and Pub 514

## The two acceptable methods

### Method 1: Spot rate on the date of the transaction

For each foreign income receipt and each foreign tax payment, use the foreign-to-USD spot rate on that day.

**Pros**: most accurate; matches the user's actual experience.
**Cons**: laborious for many small transactions (e.g., monthly salary, frequent dividend distributions).

### Method 2: Yearly average exchange rate

Use the IRS's published yearly average rate for the currency, applied uniformly to all transactions in that currency for the year.

**Pros**: simple; one rate per currency per year.
**Cons**: smooths over within-year variation. May over- or under-state in volatile years.

The IRS publishes yearly average rates at:
**https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates**

The page is updated each year (typically January or February of the following year). Verify before filing.

## Which method to use

### For accrual-method tax (Line h "Accrued")

- Use the **yearly average** rate for the year of accrual. This matches Reg. §1.985-3's general rule.
- This applies to both the income side (Line 1a) and the tax side (Line 8).

### For cash-method tax (Line h "Paid")

- Use the **spot rate on the date paid** for each tax payment.
- For income, use the **spot rate on the date received** OR **yearly average**, the user's choice — but use it consistently for all income in that currency that year.

### For 1099-DIV box 7 (already in USD)

The broker already translated. Don't re-translate. Use the USD amount directly.

### For wages from a foreign employer

If the employer pays a fixed foreign-currency salary monthly, the user can either:

- Translate each paycheck at the spot rate that day, OR
- Translate the annual total at the yearly average rate

The yearly average is much simpler and the difference is usually small.

## Where to find rates

### IRS yearly average rates

Pull from https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates. The IRS lists ~50 major currencies. As of recent years, sample rates (verify current year before relying):

- 2024 EUR/USD yearly average: approximately 0.924 (EUR per USD); inverse 1.082 USD per EUR
- 2024 GBP/USD yearly average: approximately 0.783; inverse 1.278
- 2024 JPY/USD yearly average: approximately 152
- 2024 CAD/USD yearly average: approximately 1.370

These are illustrative; **always pull the IRS page for the actual year being filed**.

### Spot rates

Several acceptable sources:

- US Treasury Reporting Rates of Exchange (https://fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/) — published quarterly
- Federal Reserve H.10 release — daily
- OANDA, XE.com, Reuters — daily commercial sources, accepted by IRS
- The user's bank or broker statement — if they actually exchanged the currency

The IRS doesn't mandate one source. Pick a reputable one and stick with it for the year.

## Worked examples

### Example 1: Expat in Germany, EUR salary, accrual method

Filer earned €120,000 EUR salary in 2024, paid €38,500 EUR German income tax (withheld monthly).

- Yearly average EUR rate (illustrative; verify): 1 EUR = $1.082 USD
- Income (Line 1a): 120,000 × 1.082 = **$129,840 USD**
- Foreign tax (Line 8): 38,500 × 1.082 = **$41,657 USD**

### Example 2: Investor with Canadian dividend, cash method

Filer received CAD $5,000 dividend from a Canadian stock on March 15, 2024. Canadian withholding tax was CAD $750 (15% treaty rate). Both translated using the Treasury rate on March 15, 2024 (illustrative): 1 CAD = $0.738 USD.

- Income (Line 1a): 5,000 × 0.738 = **$3,690 USD**
- Foreign tax (Line 8): 750 × 0.738 = **$554 USD**

If the broker (Schwab, Fidelity, etc.) already reported these in USD on the 1099-DIV, use the broker's number — they translated.

### Example 3: Mid-year move — UK to Singapore

Filer moved from UK to Singapore on July 1, 2024.

- Jan-Jun: GBP 35,000 wages, GBP 5,250 UK PAYE tax
- Jul-Dec: SGD 80,000 wages, SGD 6,000 Singapore tax

Translate each currency separately using its yearly average (illustrative):

- 2024 GBP yearly average: 1 GBP = $1.278 → £35,000 × 1.278 = $44,730 wages; £5,250 × 1.278 = $6,710 tax
- 2024 SGD yearly average: 1 SGD = $0.749 → S$80,000 × 0.749 = $59,920 wages; S$6,000 × 0.749 = $4,494 tax

Aggregate: $104,650 wages, $11,204 foreign tax — both flow to general basket Form 1116 with country columns A=UK, B=Singapore.

## What the agent should do

1. **Ask** the user which method they want to use — spot or yearly average
2. **Pull** the IRS yearly average rates for the relevant currencies and tax year
3. **Translate** each item using the chosen method, document the rate source
4. **Show the math** in the deliverable so a CPA could re-derive

If the user has multiple currencies, translate each separately. Don't aggregate currencies first.

## Edge cases

### Functional currency rules (§985)

A US individual's functional currency is USD (Reg. §1.985-1). All translations are TO USD. Foreign-currency-denominated bank accounts may generate §988 gain or loss when balances move — separate issue, not on Form 1116.

### Revaluation of accrued tax (Reg. §1.905-3)

If the user accrues foreign tax at year-end using yearly average, then actually pays it the following year at a different spot rate, the difference is a §988 gain or loss on the tax payment. For most filers, this is immaterial; the agent can ignore unless the foreign tax amount is large or the currency moved >5%.

### Hyperinflationary economies (Reg. §1.985-3)

Special rules for residents of hyperinflationary countries (cumulative inflation > 100% over 3 years). Out of scope for this skill; route to CPA.

### Cryptocurrency-denominated foreign income

If the user is paid in crypto for services performed abroad, treat as a foreign-currency receipt. Use the USD value at the time of receipt (spot price on the day). Source rules still apply — wages are sourced where services are performed.
