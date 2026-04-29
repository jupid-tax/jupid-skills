# Example — Sport Fishing Equipment Importer

A small importer of finished fishing rods from overseas reports the §4161(a)(1) manufacturer's excise tax on Q3 Form 720.

---

## Taxpayer facts

- **Entity**: Pelican Tackle LLC (single-member LLC, EIN 88-7654321, treated as disregarded entity)
- **Owner**: sole member, files Schedule C on personal Form 1040
- **Business**: imports finished fishing rods from Vietnam and resells to US sporting goods retailers
- **Quarter under review**: Q3 2026 (July 1 – September 30, 2026)
- **Sales during Q3**: 8 transactions to unrelated US retailers, totaling **$48,000** in invoiced sales price (excluding shipping and excluding the federal excise tax itself)
- **No related-party sales** in the quarter

The owner needs to determine excise liability and file Q3 2026 Form 720 by **October 31, 2026**.

---

## Determining liability

### Is the importer the taxpayer?

Per IRC §4161(a)(1) and Reg. §48.4161-1, the manufacturer's excise tax on sport fishing equipment is paid by the **manufacturer, producer, or importer** at the **first sale to an unrelated party**. An importer of finished goods from overseas is treated as the manufacturer for §4161 purposes.

Pelican Tackle imports finished rods (no further assembly in the US) and sells direct to retailers. The first sale to an unrelated US party is Pelican's invoice to the retailer. **Pelican is the §4161 taxpayer.**

### Which IRS Number applies?

Sport fishing rods → **IRS No. 41** (10% of sales price). See `references/sport-fishing-archery.md` for the full catalog.

### Sales price exclusions

Per §4161(b) and Reg. §48.4161-1(c), the "sales price" excludes:
- The §4161 tax itself
- Separately stated and reasonable transportation charges
- Separately stated warranty / installation charges

Pelican's $48,000 figure is the invoiced sales price excluding shipping (which it bills separately at actual cost). No §4161 tax was previously embedded — Pelican is the first US seller.

---

## Computation

### Tax owed

```
Tax = $48,000 × 10% = $4,800
```

### Schedule A — semi-monthly liability dates

Sport fishing manufacturer's tax is subject to **semi-monthly liability reporting** on Schedule A. The agent must populate Schedule A with the tax accrued in each semi-monthly period.

Pelican's Q3 2026 sales by date:

| Sale date | Invoice amount | Tax @ 10% |
|-----------|----------------|-----------|
| Jul 8 | $5,200 | $520 |
| Jul 22 | $7,800 | $780 |
| Aug 5 | $4,500 | $450 |
| Aug 18 | $9,000 | $900 |
| Sep 3 | $6,500 | $650 |
| Sep 12 | $4,800 | $480 |
| Sep 25 | $7,200 | $720 |
| Sep 30 | $3,000 | $300 |
| **Total** | **$48,000** | **$4,800** |

Aggregating to the semi-monthly periods of Q3:

| Period | Date range | Tax accrued |
|--------|-----------|-------------|
| 1 | Jul 1 – Jul 15 | $520 |
| 2 | Jul 16 – Jul 31 | $780 |
| 3 | Aug 1 – Aug 15 | $450 |
| 4 | Aug 16 – Aug 31 | $900 |
| 5 | Sep 1 – Sep 15 | $1,130 ($650 + $480) |
| 6 | Sep 16 – Sep 30 | $1,020 ($720 + $300) |
| **Total** | | **$4,800** |

---

## Form 720 — Part I, IRS No. 41

| Line | Field | Value |
|------|-------|-------|
| Quarter | 3 | Q3 2026 |
| Filer name | | Pelican Tackle LLC |
| EIN | | 88-7654321 |
| Address | | (entity address) |
| IRS No. 41 — Sport fishing equipment | Sales price | $48,000 |
| IRS No. 41 — Rate | | 10% |
| IRS No. 41 — Tax | | $4,800 |
| Schedule A | | Populated per period table above |
| Schedule C | | N/A (no credits) |

### Part III — totals

| Line | Field | Value |
|------|-------|-------|
| Total tax (Part I) | | $4,800 |
| Less Schedule C credits | | $0 |
| Balance due | | $4,800 |

---

## Filing channel

Pelican exceeded $2,500 in prior-quarter aggregate excise tax (assumed from prior quarters in this scenario), so it must:
- File **electronically** via an IRS-authorized MeF provider for Form 720
- Pay via **EFTPS** with semi-monthly deposits if the threshold for semi-monthly deposit applies

### Semi-monthly deposit rule

If Pelican's net excise tax for any month is > $2,500 in aggregate, the IRS requires **semi-monthly deposits** via EFTPS:

- First semi-monthly period: deposit by the **9th of the following month**
- Second semi-monthly period: deposit by the **24th** of the following month
- "Safe harbor" rule: deposit at least 95% of the actual liability for the period, OR 1/6 of the prior quarter's net tax

Pelican's monthly accruals:
- July: $1,300 — under $2,500, no semi-monthly deposit required for July
- August: $1,350 — under $2,500
- September: $2,150 — under $2,500

Since none of the months individually exceed $2,500, Pelican does NOT need semi-monthly deposits for Q3 2026. The full $4,800 can be paid with the Q3 Form 720 filing by October 31.

(If the monthly aggregate were higher, semi-monthly deposits would be mandatory. Verify the threshold each year — see `references/line-by-line.md`.)

---

## Documentation to retain

- Customs entry documents (Form 7501) for each import shipment showing duty paid and quantities
- Sales invoices for all 8 transactions with sales price clearly broken out from shipping
- Schedule A worksheet showing per-date sales and per-period aggregation
- Form 720 filing confirmation (e-file) or certified mail receipt
- EFTPS deposit confirmations (none for Q3 in this scenario)
- The §4161(a)(1) and IRS No. 41 citation for the rate

Retention: 4 years past the filing (some practitioners keep 7 for state-tax cross-reference).

---

## Common errors avoided

1. **Forgetting Schedule A**: importers / manufacturers under §4161 MUST populate Schedule A. Skipping it triggers IRS correspondence and possible deposit-penalty assessment.
2. **Including shipping in sales price**: shipping (separately stated, reasonable) is excluded. Including it overstates tax by 10% × shipping amount.
3. **Confusing tackle boxes (3%) with rods (10%)**: tackle boxes use IRS No. 42 at 3%, not IRS No. 41. If Pelican sold tackle boxes, those would go on a separate IRS Number line.
4. **Treating the wholesale buyer as a "related party"**: unless Pelican has a controlling interest in the retailer, the sale is at arm's length and the invoiced price is the sales price. Related-party sales use a constructive sales price.
5. **Filing on Q3 calendar deadline (Sep 30) instead of Q3 form deadline (Oct 31)**: the filing is due by the **last day of the month following the end of the quarter**.
6. **Missing the EFTPS enrollment**: e-filers must have an active EFTPS account to make deposits. Enrollment takes ~10 days; first-time filers should enroll well before the deadline.

---

## Output for the user

The agent delivers to Pelican Tackle:

1. **Filing summary**: Q3 2026 Form 720, IRS No. 41, $4,800 owed, due October 31, 2026
2. **Schedule A worksheet**: per-period accruals across 6 semi-monthly periods
3. **Deposit analysis**: no semi-monthly deposits required for Q3 (monthly aggregate < $2,500)
4. **Provider recommendation**: use an IRS-authorized MeF provider supporting Form 720 manufacturer's excise (e.g., TaxBandits, ExpressTaxFilings)
5. **Future-quarter reminder**: monitor monthly aggregate; if any month crosses $2,500, semi-monthly deposits become mandatory
