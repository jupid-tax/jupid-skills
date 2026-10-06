# Example — Sport Fishing Equipment Importer

A small importer of finished fishing rods reports the §4161(a) manufacturers excise tax on its Q3 2026 Form 720.

**Verified against:** Form 720 (Rev. June 2026), Instructions for Form 720 (Rev. June 2026), Pub. 510 (Rev. Dec. 2025) ch. 5, IRC §§4161, 4162, 4216, on 2026-10-06. Math checked in Python.

---

## Taxpayer facts

- **Entity**: Pelican Tackle LLC (single-member LLC, EIN 88-7654321, disregarded for income tax; it files Form 720 under its own EIN, i720 "Disregarded entities")
- **Owner**: sole member, files Schedule C on personal Form 1040
- **Business**: imports finished fishing rods from Vietnam and resells to US sporting goods retailers
- **Quarter under review**: Q3 2026 (July 1 – September 30, 2026)
- **Sales during Q3**: 8 invoices to unrelated US retailers, 660 rods, totaling **$48,000** in invoiced sale price (excluding separately stated shipping and excluding the federal excise tax itself)
- **Per-rod sale prices**: $65 to $90; no rod sold for $100 or more
- **No related-party sales** in the quarter; no other excise taxes

The owner needs to determine excise liability and file the Q3 2026 Form 720. The due date is October 31, 2026, a Saturday, so the return is timely if filed by Monday, November 2, 2026 (i720 "When To File").

---

## Determining liability

### Is the importer the taxpayer?

Under IRC §4161(a)(1)(A), the tax is imposed on the sale of sport fishing equipment by the **manufacturer, producer, or importer**. An importer is a person who brings a taxable article into the United States (Pub. 510, ch. 5, "Importer").

Pelican imports finished rods and sells them to retailers. **Pelican is the §4161 taxpayer** on its sales.

### Which IRS No. applies?

Fishing rods and poles → **IRS No. 110** (Part II): 10% of the sale price, not more than $10 per article (§4161(a)(1)(B); Form 720 Part II). IRS No. 41 is for sport fishing equipment *other than* rods and poles.

Because every rod sold for less than $100, 10% of each rod's price is under $10 and the cap never applies this quarter. If Pelican sells a rod for $180, the tax on that rod is $10, not $18.

### Sale price exclusions

Per Pub. 510 ch. 5 (price rules under §4216), the sale price excludes the manufacturers excise tax itself, transportation charges pursuant to the sale, and discounts actually granted; it includes charges for containers and packing for shipment. Pelican's $48,000 excludes shipping (billed separately at cost).

---

## Computation

### Sales log (kept in the file; not reported line by line)

| Sale date | Rods | Price per rod | Invoice amount | Tax @ 10% (each rod under the $10 cap) |
|-----------|------|---------------|----------------|-----------|
| Jul 8 | 80 | $65 | $5,200 | $520 |
| Jul 22 | 120 | $65 | $7,800 | $780 |
| Aug 5 | 50 | $90 | $4,500 | $450 |
| Aug 18 | 120 | $75 | $9,000 | $900 |
| Sep 3 | 100 | $65 | $6,500 | $650 |
| Sep 12 | 60 | $80 | $4,800 | $480 |
| Sep 25 | 90 | $80 | $7,200 | $720 |
| Sep 30 | 40 | $75 | $3,000 | $300 |
| **Total** | **660** | | **$48,000** | **$4,800** |

```
Tax = Σ min(10% × price, $10) per rod = $4,800
```

### No Schedule A, no deposits

IRS No. 110 is a Part II tax. Schedule A is completed only for Part I taxes (Form 720 Schedule A note), and Pub. 510 ch. 5 says of sport fishing equipment: "Pay this tax with Form 720. No tax deposits are required." The full $4,800 is paid with the Q3 return.

---

## Form 720 — Part II, IRS No. 110

| Line | Field | Value |
|------|-------|-------|
| Quarter ending | | September 2026 |
| Filer name | | Pelican Tackle LLC |
| EIN | | 88-7654321 |
| Address | | (entity address) |
| Part I line 1 | | $0 (none) |
| IRS No. 110 — Fishing rods and fishing poles | Tax | $4,800.00 |
| Part II line 2 | | $4,800.00 |
| Schedule A | | Not completed (no Part I liability) |
| Schedule C | | Not used (no claims) |

### Part III — totals

| Line | Field | Value |
|------|-------|-------|
| 3 | Total tax (line 1 + line 2) | $4,800.00 |
| 4 | Claims | $0 |
| 5 | Deposits made for the quarter | $0 |
| 6 | Overpayment from previous quarters | $0 |
| 7 | Form 720-X amount included on line 6 | $0 |
| 8 | Line 5 + line 6 | $0 |
| 9 | Line 4 + line 8 | $0 |
| 10 | Balance due | $4,800.00 |

---

## Filing channel

E-filing Form 720 is optional (IRS Form 720 e-file FAQ). Pelican can:
- e-file through a provider on https://www.irs.gov/e-file-providers/720-mef-providers and pay by electronic funds withdrawal, EFTPS, or Direct Pay; or
- mail the paper return to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0009, with Form 720-V and a check payable to "United States Treasury" (i720 "Where To File", Form 720-V).

Let the user choose. Pelican was liable this quarter, so it must keep filing Form 720 each quarter until it files a final return (i720 "Who Must File").

---

## Documentation to retain

- Customs entry documents (CBP Form 7501) for each import shipment
- Sales invoices for all 8 sales with rod counts, per-rod prices, and shipping stated separately
- The sales log above
- Form 720 filing confirmation (e-file) or certified mail receipt, and the payment record
- The §4161(a)(1)(B) and IRS No. 110 citation for the rate and cap

Retention: at least 4 years from the latest of the date the tax became due, the date it was paid, or the date a claim was filed (i720 "Recordkeeping").

---

## Common errors avoided

1. **Using IRS No. 41 for rods**: rods and poles are IRS No. 110, with the $10 per-article cap.
2. **Completing Schedule A or making deposits for a Part II tax**: not required for sport fishing taxes.
3. **Including shipping in sale price**: separately stated transportation pursuant to the sale is excluded; including it overstates tax by 10% × shipping.
4. **Confusing tackle boxes (3%) with rods (10%)**: tackle boxes go on IRS No. 114 at 3%; electric outboard motors on IRS No. 42 at 3%.
5. **Treating the retailer as a "related party"**: unless Pelican and the retailer are related, the invoiced price is the sale price. Related-party sales use a constructive sale price (§4216(b)).
6. **Missing the weekend rule**: October 31, 2026 is a Saturday; the return is timely on November 2, 2026.

---

## Output for the user

The agent delivers to Pelican Tackle:

1. **Filing summary**: Q3 2026 Form 720, IRS No. 110, $4,800.00 owed, timely if filed and paid by November 2, 2026
2. **Sales log**: rods, per-rod price, tax per invoice, cap check
3. **Payment note**: no deposits required; pay with the return
4. **Channel options**: e-file through an IRS-listed 720 MeF provider, or paper to Ogden with Form 720-V
5. **Future-quarter reminder**: watch for rods priced at $100 or more (cap applies) and file each quarter until a final return
