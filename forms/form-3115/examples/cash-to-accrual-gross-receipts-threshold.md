# Example — Cash to Accrual on Crossing the §448 Gross Receipts Threshold

A growing service business crosses the $30M three-year-average gross receipts threshold and is forced from cash to accrual under IRC §448. Files Form 3115 with DCN 233 (automatic consent, mandatory change).

---

## Taxpayer facts

- **Entity**: Vertex Engineering Services, Inc. (C-corp, EIN 22-3344556)
- **Business**: engineering consulting services
- **Calendar fiscal year**
- **Current method**: cash basis since incorporation in 2018
- **Gross receipts (3-year average for 2024 testing)**:
  - 2022: $24M
  - 2023: $30M
  - 2024: $36M
  - **3-year average**: ($24M + $30M + $36M) / 3 = **$30M**

For 2025, the 3-year-average test (looking back at 2022-2024) is **$30M**, which **does not exceed** the §448(c) threshold of $30M (2025 amount; verify 2026 inflation adjustment). Vertex remains on cash for 2025.

For 2026 testing (looking back at 2023-2025):
- 2023: $30M
- 2024: $36M
- 2025: $42M (estimated)
- 3-year average: ($30M + $36M + $42M) / 3 = **$36M**

This **exceeds** the §448(c) threshold for 2026. Vertex must convert to accrual for tax year 2026 — it is the **year of change**.

---

## Why DCN 233 (automatic, mandatory)

§448(a) prohibits C-corps and partnerships with C-corp partners from using the cash method when gross receipts exceed the threshold. The exception in §448(c) for "small businesses" no longer applies once the threshold is crossed.

The change from cash to accrual under §448 is covered by **DCN 233** in Rev. Proc. 2024-23 (or successor):
- **Automatic consent** — no user fee
- **Mandatory** — Vertex has no choice; the IRS deems consent granted
- **Filed in duplicate** — original with the 2026 return; duplicate to Ogden

The CFO does NOT need to file a non-automatic application or pay an $11,500 fee. DCN 233 is the standard path for forced §448 conversions.

---

## §481(a) computation

The §481(a) adjustment captures the cumulative net effect of switching methods. Vertex is moving from cash (income on receipt, expenses on payment) to accrual (income when earned, expenses when incurred).

### Items affected as of December 31, 2025 (start of year of change)

| Item | Cash treatment to-date | Accrual treatment | §481(a) effect |
|------|-------------------------|-------------------|-----------------|
| Accounts receivable | Not yet recognized as income | Should have been recognized when earned | +$1,800,000 |
| Accounts payable | Not yet deducted | Should have been deducted when incurred | −$420,000 |
| Accrued payroll | Not yet deducted | Should have been deducted when earned by employees | −$180,000 |
| Prepaid insurance (12-month policy paid in Dec 2025) | Fully deducted on payment | Should have been capitalized and amortized | +$60,000 |
| Customer deposits / unearned revenue | Recognized as income on receipt | Should have been deferred until earned | −$240,000 |
| Inventory items (engineering supplies on hand) | Deducted when purchased | Should have been capitalized | +$90,000 |
| **Net §481(a)** | | | **+$1,110,000** |

### Spread

§481(a) is **positive ≥ $50,000** → mandatory **4-year spread** under default rules.

| Year | §481(a) recognized |
|------|---------------------|
| 2026 (year of change) | $277,500 |
| 2027 | $277,500 |
| 2028 | $277,500 |
| 2029 | $277,500 |
| **Total** | **$1,110,000** |

The §481(a) recognized each year flows to Form 1120 as additional income on the "Other income" line (Line 10) labeled "§481(a) adjustment, accounting method change from cash to accrual under §448, DCN 233".

---

## Form 3115 — Part I (general information)

| Line | Field | Value |
|------|-------|-------|
| 1a | Name of filer | Vertex Engineering Services, Inc. |
| 1b | EIN | 22-3344556 |
| 2 | Tax year of change | January 1, 2026 – December 31, 2026 |
| 3 | Type of return | Form 1120 (C-corp) |
| 4 | Type of accounting method change | Overall method (cash to accrual) |
| 5 | DCN | 233 |
| 6 | Section 481(a) adjustment | +$1,110,000 |
| 7 | Spread | 4-year (mandatory; ≥ $50K positive) |

---

## Form 3115 — Part II (information for automatic change)

Vertex confirms compliance with all DCN 233 conditions:

- [x] Entity is a C-corp (eligible for DCN 233)
- [x] Crossed §448(c) threshold based on 3-year average gross receipts test
- [x] Has used cash method for at least the prior 2 tax years (used cash since 2018)
- [x] Not under IRS examination on a §448 issue
- [x] Not in final year of business
- [x] No method change for the same item in the prior 5 years

The Part II "statement of compliance" is signed by the corporate officer authorized to file the return.

---

## Form 3115 — Part IV (§481(a) adjustment statement)

Attached separately:

```
§481(a) Adjustment Schedule — DCN 233 (Cash to Accrual under §448)
Vertex Engineering Services, Inc., EIN 22-3344556
Tax year of change: January 1, 2026 – December 31, 2026

Item-by-item:

1. Accounts receivable as of 12/31/2025:    +$1,800,000
   - Cumulative correct (accrual): $1,800,000 (would have been recognized as earned)
   - Cumulative actual (cash):     $0 (not yet collected)
   - Per-item §481(a):             +$1,800,000

2. Accounts payable as of 12/31/2025:        −$420,000
   - Cumulative correct (accrual): $420,000 deducted
   - Cumulative actual (cash):     $0
   - Per-item §481(a):             −$420,000

3. Accrued payroll as of 12/31/2025:         −$180,000
   - Cumulative correct: $180,000 deducted
   - Cumulative actual:  $0
   - Per-item §481(a):   −$180,000

4. Prepaid insurance (12-month policy):      +$60,000
   - Cumulative correct: $0 expensed in 2025 (would have been amortized 1/12 in Dec 2025)
   - Cumulative actual:  $60,000 fully expensed in Dec 2025 on payment
   - Per-item §481(a):   +$60,000 (add back the over-deducted amount)

5. Customer deposits / unearned revenue:     −$240,000
   - Cumulative correct: $0 (would have been deferred)
   - Cumulative actual:  $240,000 included in income on receipt
   - Per-item §481(a):   −$240,000 (back out income that wasn't yet earned)

6. Engineering supplies on hand:             +$90,000
   - Cumulative correct: $0 (would have been capitalized as inventory)
   - Cumulative actual:  $90,000 deducted on purchase
   - Per-item §481(a):   +$90,000 (add back the over-deducted amount)

Net §481(a):                                 +$1,110,000

Spread: 4-year (positive ≥ $50,000)
   2026: $277,500
   2027: $277,500
   2028: $277,500
   2029: $277,500
```

---

## Filing logistics

| Task | Date | Detail |
|------|------|--------|
| Year of change begins | January 1, 2026 | Apply accrual from this date forward in books |
| Original Form 3115 prepared | March – Sep 2026 | With 2026 return preparation |
| Duplicate copy mailed to Ogden | Same day or before return filing | Certified mail, return receipt |
| Original attached to Form 1120 | By return filing | Including extensions, latest October 15, 2027 |
| First §481(a) recognized | 2026 return | $277,500 on Form 1120 Line 10 |
| Subsequent §481(a) recognized | 2027, 2028, 2029 | $277,500 each year |

---

## Going forward (2026+)

Starting January 1, 2026, Vertex:
- Records income when **earned** (not when collected)
- Records expenses when **incurred** (not when paid)
- Tracks accounts receivable and accounts payable as balance-sheet items
- Capitalizes inventory and amortizes prepaid items

The internal accounting system (likely QuickBooks, NetSuite, or similar) needs to be configured for accrual reporting. The CFO should run a parallel cash report for management purposes if needed, but tax reporting is accrual.

---

## Common errors avoided

1. **Filing non-automatic instead of DCN 233**: a non-automatic filing would cost $11,500 user fee. DCN 233 is the correct (free) path.
2. **Forgetting the duplicate copy to Ogden**: invalidates the automatic consent.
3. **Missing the §481(a) computation**: the IRS rejects Form 3115 without the cumulative-effect schedule.
4. **Wrong year of change**: the year of change is the FIRST year the threshold is crossed and the change is required (2026 here, not 2025 when the trigger was just emerging).
5. **Spreading negative §481(a) over 4 years**: a positive §481(a) is spread 4 years; if it had been negative (taxpayer-favorable), it would be deducted entirely in the year of change.
6. **Continuing to use cash for management reporting and forgetting to apply accrual on the tax return**: the tax return must be on accrual starting 2026; book-tax differences may emerge if internal management reports stay on cash.

---

## Output for the user

The agent delivers to Vertex's CFO:

1. **Form 3115 draft** (Parts I-IV) ready for signature
2. **§481(a) schedule** (separate attachment) with line-by-line item math and citations
3. **Filing checklist**: Ogden mailing, return attachment, signature block, retention
4. **Multi-year spread tracker**: $277,500 to recognize in each of 2026-2029 with prompts for the next 3 returns
5. **System configuration note**: switch to accrual in the GL effective January 1, 2026
6. **Documentation**: 3-year gross-receipts test math showing the §448(c) threshold was crossed
