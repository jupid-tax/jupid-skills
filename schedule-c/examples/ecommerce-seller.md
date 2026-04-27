# Example: E-commerce Seller (Etsy + Shopify with Inventory)

A complete Schedule C for an online seller of handmade products. This is the canonical "Part III applies" pattern — service-business filers should reference the freelance-designer example instead.

## The filer

- **Name**: Priya Patel
- **Business**: Hand-poured candles sold on Etsy + own Shopify store
- **Entity**: Single-member LLC (Delaware, taxed as disregarded entity)
- **First Schedule C year**: No (fourth year)
- **Tax year**: 2025

## Inputs gathered

### Income

Marketplaces and processors send 1099-Ks at lower thresholds in recent years:

| Source | Type | Amount |
|--------|------|--------|
| Etsy 1099-K (gross sales before fees) | 1099-K | $48,200 |
| Shopify Payments 1099-K | 1099-K | $19,400 |
| PayPal 1099-K | 1099-K | $4,800 |
| Wholesale orders to one local boutique (paid by check, no 1099) | check | $3,200 |
| **Line 1 Gross receipts** | | **$75,600** |

Returns and refunds: $1,840 (Etsy refunds for damaged shipping, Shopify customer cancellations). **Line 2 = $1,840**, Line 3 = $73,760.

### Cost of Goods Sold (Part III)

Priya makes candles. She has materials, labor (just herself — not deductible), and finished inventory.

| Line | Item | Amount |
|------|------|--------|
| 33 | Inventory method | Cost |
| 34 | Changed method | No |
| 35 | Beginning inventory (from 2024 Line 41) | $3,400 |
| 36 | Purchases of finished or near-finished candles for resale (none — she makes everything) | $0 |
| 37 | Cost of labor (no employees, owner labor not deductible) | $0 |
| 38 | Materials and supplies (wax, wicks, fragrance oil, glass containers, lids, labels, dyes — all become part of the product) | $14,800 |
| 39 | Other costs (freight-in for raw materials, shop supplies for production like pots and thermometers under $2,500 each that wear out) | $1,650 |
| 40 | Total | $19,850 |
| 41 | Ending inventory (year-end count: ~280 finished candles + raw materials) | $4,200 |
| 42 | Cost of Goods Sold | **$15,650** |

**Line 4 of Part I = $15,650.** Line 5 (Gross profit) = $73,760 − $15,650 = $58,110. Line 6 = $0. **Line 7 = $58,110**.

### Operating expenses (Part II)

| Original transaction | Mapped to | Amount |
|---------------------|-----------|--------|
| Etsy ads + Meta ads | Line 8 (Advertising) | $1,800 |
| Local delivery to one wholesale account (84 miles × $0.70) | Line 9 (Car & truck) | $59 |
| Etsy seller fees + Shopify subscription fee + payment processor fees | Line 10 (Commissions/fees) | $9,750 |
| Bookkeeper (12 months × $150) | Line 11 (Contract labor) | $1,800 |
| Liability + product insurance for candles | Line 15 (Insurance) | $480 |
| Business credit card interest | Line 16b (Interest) | $190 |
| CPA fees + Jupid + Etsy seller's tax tools | Line 17 (Legal & prof) | $720 |
| Office paper, printer ink for shipping labels | Line 18 (Office expense) | $240 |
| Rent for 200 sq ft of dedicated workshop space at the local maker space | Line 20b (Rent — other) | $4,800 |
| Equipment repair (broken candle melter pot replaced) | Line 21 (Repairs) | $180 |
| Shipping supplies (boxes, tape, packing peanuts — NOT inventory because they don't become part of the product) | Line 22 (Supplies) | $1,420 |
| LLC franchise tax (Delaware annual) + state business license | Line 23 (Taxes & licenses) | $310 |
| Outbound shipping costs paid through Etsy (USPS/UPS for orders shipped) | Line 27a (Other) | $5,800 |
| Online courses (candle-making advanced techniques) | Line 27a (Other) | $290 |

### Home office

Priya's "office" for invoicing and customer service is the kitchen table — fails exclusive use. Her actual production happens at the maker space (Line 20b rent, separate location). **Line 30 = $0**.

### Vehicle

Just the 84 business miles (one delivery to a wholesale buyer). Standard mileage 84 × $0.70 = $59 on Line 9. Part IV must still be completed if Line 9 > 0, even for a small amount.

## The completed Schedule C draft

```markdown
# Schedule C — DRAFT for tax year 2025

## Header
A. Principal business: Online sales of handmade candles
B. Business code: 339999 (All other miscellaneous manufacturing) — chosen because Priya makes the products
C. Business name: Priya Patel Candle Co LLC
D. EIN: 88-XXXXXXX
E. Address: Same as Form 1040
F. Accounting method: Cash
G. Material participation: Yes
H. Started this year: No
I. Paid any individual $600+: Yes (bookkeeper $1,800)
J. Will file required 1099-NEC: Yes

## Part I — Income
1.  Gross receipts:                $75,600
2.  Returns and allowances:        $1,840
3.  Subtract line 2 from 1:        $73,760
4.  Cost of goods sold:            $15,650   (from Part III)
5.  Gross profit:                  $58,110
6.  Other income:                  $0
7.  Gross income:                  $58,110

## Part II — Expenses
 8. Advertising:                   $1,800
 9. Car and truck:                 $59       (84 mi × $0.70 — see Part IV)
10. Commissions and fees:          $9,750
11. Contract labor:                $1,800
12. Depletion:                     $0
13. Depreciation + §179:           $0
14. Employee benefit programs:     $0
15. Insurance:                     $480
16a. Mortgage interest:            $0
16b. Other interest:               $190
17. Legal and professional:        $720
18. Office expense:                $240
19. Pension/profit-sharing:        $0
20a. Rent (vehicles, machinery):   $0
20b. Rent (other):                 $4,800   (workshop space)
21. Repairs and maintenance:       $180
22. Supplies:                      $1,420   (shipping supplies)
23. Taxes and licenses:            $310
24a. Travel:                       $0
24b. Deductible meals (50%):       $0
25. Utilities:                     $0       (workshop utilities included in Line 20b lease)
26. Wages:                         $0
27a. Other expenses (Part V):      $6,090
28. Total expenses:                $27,839

## Part II totals
29. Tentative profit:              $30,271
30. Home office:                   $0
31. Net profit:                    $30,271

## Part III — COGS
33. Inventory method: Cost
34. Method changed: No
35. Beginning inventory:           $3,400
36. Purchases:                     $0
37. Cost of labor:                 $0
38. Materials and supplies:        $14,800
39. Other costs:                   $1,650
40. Total:                         $19,850
41. Ending inventory:              $4,200
42. Cost of goods sold:            $15,650 (= Line 4)

## Part IV — Vehicle
43. Date placed in service:        01/01/2025
44a. Business miles:               84
44b. Commuting miles:              0
44c. Other miles:                  6,400
45. Available for personal use:    Yes
46. Another vehicle available:     No
47a. Have evidence:                Yes
47b. Written:                      Yes (single-trip log)

## Part V — Other Expenses (detail of Line 27a)
| Description                                | Amount  |
|---------------------------------------------|---------|
| Outbound shipping (USPS/UPS via Etsy)       | $5,800  |
| Continuing education (candle technique courses) | $290 |
| **Total (Line 48 = Line 27a)**              | $6,090  |

## Required attachments
- [ ] Form 4562 — Not required
- [ ] Form 8829 — Not required (no home office)
- [x] Schedule SE — Required (profit > $400)

## Validation summary
- Math: all checks passed
  - Part III: 19,850 − 4,200 = 15,650 ✓ matches Line 4
  - Line 28 = sum of 8-27a ✓
  - Line 29 = Line 7 − Line 28 ✓
  - Line 31 = Line 29 − Line 30 ✓
- Sanity:
  - COGS ratio: 21% of gross sales — consistent with handmade goods
  - Operating expense ratio: 38% of gross income — typical for inventory-based e-commerce with paid shipping
  - Line 27a is 22% of total expenses — high, but legitimately driven by outbound shipping which has nowhere better to go
  - 1099-NEC required for bookkeeper (over $600)
- Next steps:
  - Schedule SE: 92.35% × $30,271 = $27,955 × 15.3% = $4,277 SE tax
  - Half of SE tax ($2,138) deductible on Schedule 1 Line 15
  - Quarterly estimated taxes for 2026: ~$5,500 federal + state
  - Confirm Etsy/Shopify 1099-Ks reconcile to Etsy/Shopify gross sales reports — discrepancies should be researched

## Sources cited in this draft
- IRS Form 1040 Schedule C, Rev. 2025
- IRC §162, §183 (hobby loss), §263A(i) (UNICAP small biz exemption)
- IRS Pub 334 (Tax Guide for Small Business)
- Notice 2025-5 (2025 standard mileage rate 70¢)
```

## Why each non-obvious choice

**Why is outbound shipping on Line 27a, not COGS?** This one trips up many filers. Inventoriable costs (those that go into Part III) include freight-in (cost to ship raw materials to Priya). Freight-out (shipping finished products to customers) is an operating expense, not COGS. Line 27a is the most common home for outbound shipping — it could also defensibly go on Line 22 (Supplies) if the shipping supplies are negligible. Line 27a keeps it cleanly visible.

**Why are wax and glass jars on Line 38 (Materials), not Line 22 (Supplies)?** They become part of the finished product. That's the COGS test. Shipping boxes don't become part of the candle — they ship the candle — so those go on Line 22 (or Line 27a if pure outbound shipping cost).

**Why Line 39 (Other costs) for shop pots and thermometers?** Items consumed in production that aren't materials per se. Tools costing under $2,500 each that wear out fit here under the de minimis safe harbor.

**Why business code 339999 (manufacturing) instead of 454110 (electronic shopping)?** Priya makes the products. The IRS expects manufacturers to have higher COGS than retailers. Code 339999 aligns the audit benchmark with her actual cost structure. If she were drop-shipping or reselling someone else's candles, 454110 would be correct.

**Why is Etsy's 1099-K $48,200 if she had returns?** 1099-K reports gross transactions, not net of refunds. Refunds go on Line 2 separately. Her Line 1 should match the gross 1099-K total (plus the wholesale check), and refunds reduce the total via Line 2.

**Why no §179 deduction on the candle melter equipment?** The melter pot was replaced for $180 (Line 21 repair, expensed). Her larger original melter cost $1,800 four years ago — under de minimis when bought, expensed in year one, no Form 4562 needed. Smaller production equipment under $2,500 individually didn't trigger §179 either.

**What if Priya had inventory shrinkage (theft or damage during production)?** Document and write off as a Line 39 (Other costs) addition or as a separate inventory adjustment with backup. Year-over-year ending inventory drops without corresponding COGS increases attract IRS attention.

**What about sales tax?** If Priya collects and remits sales tax, that's separate from income tax. Don't include sales tax collected in Line 1 gross receipts (some platforms include it; back it out). Sales tax remitted by Priya goes on Line 23 only if she's the retailer (in most states). Marketplace facilitator laws often shift sales tax collection to Etsy/Shopify — Priya should verify per state.
