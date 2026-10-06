# Example — Cash to Accrual on Crossing the §448 Gross Receipts Threshold

A growing C corporation's three-year-average gross receipts exceed the 2026 §448(c) threshold ($32,000,000), so it must leave the cash method under IRC §448. Files Form 3115 with DCN 257 (automatic consent, change made in the mandatory §448 year).

---

## Taxpayer facts

- **Entity**: Vertex Engineering Services, Inc. (C-corp, EIN 22-3344556)
- **Business**: engineering consulting services
- **Ownership**: 70% held by outside investors who do not work for the company, so Vertex is **not** a qualified personal service corporation (a QPSC, §448(d)(2), could stay on cash regardless of gross receipts; ASK about ownership and activities before applying §448)
- **Calendar tax year**
- **Current method**: cash basis since incorporation in 2018
- **Gross receipts (3-year average for 2024 testing)**:
  - 2022: $24M
  - 2023: $30M
  - 2024: $36M
  - **3-year average**: ($24M + $30M + $36M) / 3 = **$30M**

For 2025, the 3-year-average test (looking back at 2022-2024) is **$30M**, which **does not exceed** the §448(c) threshold of $31,000,000 for tax years beginning in 2025 (Rev. Proc. 2024-40 §2.31). Vertex remains on cash for 2025.

For 2026 testing (looking back at 2023-2025):
- 2023: $30M
- 2024: $36M
- 2025: $42M (estimated)
- 3-year average: ($30M + $36M + $42M) / 3 = **$36M**

This **exceeds** the §448(c) threshold of $32,000,000 for tax years beginning in 2026 (Rev. Proc. 2025-32 §4.30). Vertex must convert to accrual for tax year 2026 — it is the **year of change** and its mandatory §448 year. (Before filing, replace the 2025 estimate with actual gross receipts; the test uses the 3 tax years ending with 2025.)

---

## Why DCN 257 (automatic, mandatory)

§448(a) prohibits C-corps and partnerships with C-corp partners from using the cash method when gross receipts exceed the threshold. The exception in §448(c) for "small businesses" no longer applies once the threshold is crossed.

The change from cash to accrual is section 15.01 of Rev. Proc. 2025-23; when made in the mandatory §448 year its DCN is **257** (§15.01(6)(a)). DCN 122 covers other cash-to-accrual changes; DCN 233 is the opposite change (a small business taxpayer moving **to** cash):
- **Automatic consent** — no user fee
- **Mandatory** — Vertex has no choice; consent is granted under the automatic procedures when properly filed
- **Filed in duplicate** — original with the 2026 return; signed copy to Ogden

The CFO does NOT need to file a non-automatic application or pay the $13,225 non-automatic user fee (Rev. Proc. 2026-1, Appendix A). DCN 257 is the standard path for forced §448 conversions.

---

## §481(a) computation

The §481(a) adjustment captures the cumulative net effect of switching methods. Vertex is moving from cash (income on receipt, expenses on payment) to accrual (income when earned, expenses when incurred).

### Items affected as of December 31, 2025 (start of year of change)

| Item | Cash treatment to-date | Accrual treatment | §481(a) effect |
|------|-------------------------|-------------------|-----------------|
| Accounts receivable | Not yet recognized as income | Should have been recognized when earned | +$1,800,000 |
| Accounts payable | Not yet deducted | Should have been deducted when incurred | −$420,000 |
| Accrued payroll | Not yet deducted | Should have been deducted when earned by employees | −$180,000 |
| Prepaid insurance (12-month policy paid in Dec 2025, coverage starting 1/1/2026) | Fully deducted on payment | Not deductible in 2025 under accrual (ASK whether the 12-month rule of Reg. §1.263(a)-4(f) applies; if it does, this line is $0) | +$60,000 |
| Customer deposits / unearned revenue | Recognized as income on receipt | Deferred until earned, only if Vertex also adopts the advance-payment deferral method (Reg. §1.451-8(c)); otherwise included on receipt and this line is $0 — ASK | −$240,000 |
| Engineering supplies on hand | Deducted when purchased | Deductible when used or consumed (Reg. §1.162-3) | +$90,000 |
| **Net §481(a)** | | | **+$1,110,000** |

### Spread

§481(a) is **positive ≥ $50,000** → **4-year adjustment period**, ratably (Rev. Proc. 2015-13 §7.03(1)); the de minimis election is unavailable. (If Vertex were under examination without a line 7b window, the period would be 2 years.)

| Year | §481(a) recognized |
|------|---------------------|
| 2026 (year of change) | $277,500 |
| 2027 | $277,500 |
| 2028 | $277,500 |
| 2029 | $277,500 |
| **Total** | **$1,110,000** |

The §481(a) recognized each year flows to Form 1120 as additional income on the "Other income" line (line 10, with a statement) labeled "§481(a) adjustment, accounting method change from cash to accrual under §448, DCN 257".

---

## Form 3115 (Rev. December 2022) — identification and Part I

| Line | Field | Value |
|------|-------|-------|
| Identification | Name of filer / EIN | Vertex Engineering Services, Inc. / 22-3344556 |
| Identification | Tax year of change | 01/01/2026 – 12/31/2026 |
| Identification | Type of applicant | Corporation |
| Identification | Type of change | Other: overall method, cash to accrual |
| 1a | DCN | 257 |
| 2 | Eligibility rules restrict? | No |
| 3 | All required information provided? | Yes |

## Form 3115 — Part II, Schedule A, Part IV

| Line | Field | Value |
|------|-------|-------|
| 4 | Cease business / terminate in 2026? | No |
| 6a | Any return under examination? | No |
| 7a / 7b | Audit protection applies? | Yes / Not under exam |
| 11a | Change for same item or overall method change within 5 years? | No (cash method since 2018) |
| 12 | Pending requests? | No |
| 13 | Overall method change? | Yes → Schedule A |
| 15a | Trade or business description | Attached |
| 19a | Gross receipts: 2025 / 2024 / 2023 | $42,000,000 / $36,000,000 / $30,000,000 |
| Sch. A line 1 | Present / proposed | Cash / Accrual |
| Sch. A line 2a | Income accrued but not received | +$1,800,000 |
| Sch. A line 2b | Income received before earned | −$240,000 (only with the deferral method; see above) |
| Sch. A line 2c | Expenses accrued but not paid (AP $420,000 + payroll $180,000) | −$600,000 |
| Sch. A line 2d | Prepaid expenses previously deducted | +$60,000 |
| Sch. A line 2e | Supplies on hand previously deducted | +$90,000 |
| Sch. A line 2h / Part IV line 26 | Net §481(a) adjustment | +$1,110,000 |
| Part IV line 25 | Cut-off basis? | No |
| Part IV line 28 | Election | None (≥ $50,000) |

The signature at the bottom of page 1 is by the corporate officer with authority to bind Vertex; the signed copy goes to Ogden.

---

## Form 3115 — Part IV (§481(a) adjustment statement)

Attached separately:

```
§481(a) Adjustment Schedule — DCN 257 (Cash to Accrual in the mandatory §448 year)
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
   - Cumulative correct: $0 expensed in 2025 (coverage starts 01/01/2026; 12-month rule not applied)
   - Cumulative actual:  $60,000 fully expensed in Dec 2025 on payment
   - Per-item §481(a):   +$60,000 (add back the over-deducted amount)

5. Customer deposits / unearned revenue:     −$240,000
   - Cumulative correct: $0 (would have been deferred)
   - Cumulative actual:  $240,000 included in income on receipt
   - Per-item §481(a):   −$240,000 (back out income that wasn't yet earned)

6. Engineering supplies on hand:             +$90,000
   - Cumulative correct: $0 (deductible when used or consumed)
   - Cumulative actual:  $90,000 deducted on purchase
   - Per-item §481(a):   +$90,000 (add back the over-deducted amount)

Net §481(a):                                 +$1,110,000

Adjustment period: 4 years (positive ≥ $50,000; Rev. Proc. 2015-13 §7.03(1))
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
| Signed copy to Ogden | Between 01/01/2026 and the day the return is filed | M/S 6111 by certified mail, or fax 844-249-8134 |
| Original attached to Form 1120 | By return filing | Including extensions, latest October 15, 2027 |
| First §481(a) recognized | 2026 return | $277,500 on Form 1120 line 10 |
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

1. **Filing non-automatic instead of DCN 257**: a non-automatic filing would cost the $13,225 user fee. DCN 257 is the correct (free) path. **Citing DCN 233** would also be wrong: that DCN is a change to the cash method.
2. **Forgetting the signed copy to Ogden**: the automatic change is not properly filed.
3. **Missing the §481(a) computation**: Form 3115 line 26 requires the computation summary.
4. **Wrong year of change**: the year of change is the FIRST year the threshold is crossed and the change is required (2026 here, not 2025 when the trigger was just emerging).
5. **Spreading negative §481(a) over 4 years**: a positive §481(a) is spread over 4 years; if it had been negative (taxpayer-favorable), it would be deducted entirely in the year of change.
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
