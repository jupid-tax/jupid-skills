# Example — Inventory Method Change from LIFO to FIFO

A small retailer that has used LIFO since 2018 wants to go back to FIFO because its lender now requires FIFO financial statements, and LIFO for tax requires LIFO in the financial statements (§472(c)). Files Form 3115 with DCN 56 (automatic consent) and a positive §481(a) adjustment.

(The opposite move, **adopting** LIFO, is not a Form 3115 change: it is made on Form 970 attached to the return for the first LIFO year, Reg. §1.472-3 and the Form 970 instructions. If a user asks for FIFO → LIFO, redirect to Form 970.)

---

## Taxpayer facts

- **Entity**: Granite Hardware Co. (S-corp since formation, EIN 12-7788990)
- **Calendar tax year**
- **Business**: brick-and-mortar hardware retailer with 1 location
- **Current method**: dollar-value LIFO since founding in 2018 (Form 970 filed with the 2018 return), 4 pools (Tools, Plumbing, Electrical, General Hardware)
- **Prior method changes**: none in the last 5 years (Form 3115 line 11a "No")
- **Under examination**: no
- **Beginning-of-year-of-change inventory** (January 1, 2026):

| Pool | LIFO value (present method) | FIFO value (proposed method) |
|------|-----------------------------|------------------------------|
| Tools | $158,000 | $180,000 |
| Plumbing | $86,000 | $95,000 |
| Electrical | $97,500 | $110,000 |
| General Hardware | $120,500 | $135,000 |
| **Total** | **$462,000** | **$520,000** |

The change is for the **2026 tax year** (year of change).

---

## Why DCN 56 (automatic)

Rev. Proc. 2025-23 §23.01 ("Change from the LIFO inventory method") covers a taxpayer changing from LIFO for all its LIFO inventory (or entire dollar-value pools) to a permitted method. Its DCN is **56**.

- **Automatic consent** — no user fee
- **Filed in duplicate** — original with the 2026 Form 1120-S; signed copy to Ogden
- **§481(a) adjustment required** (§23.01(7))
- **Re-electing LIFO later**: not for at least 5 taxable years beginning with 2026 without IRS consent on a non-automatic Form 3115; after that, by Form 970 (§23.01(3))
- **S corporation**: Granite has always been an S corporation, so the §1363(d) LIFO recapture rule for C corporations converting to S does not apply (ASK if the entity was ever a C corporation)

---

## §481(a) computation

Compare beginning inventory for the year of change under the proposed method (FIFO) with beginning inventory under the present method (LIFO), pool by pool (same approach as the Form 3115 instructions, Line 25, Example 1):

```
Pool              FIFO        LIFO        Difference
Tools           $180,000    $158,000     +$22,000
Plumbing         $95,000     $86,000      +$9,000
Electrical      $110,000     $97,500     +$12,500
General Hdw     $135,000    $120,500     +$14,500
Total           $520,000    $462,000     +$58,000
```

Beginning inventory is $58,000 higher under FIFO: prior years' cost of goods sold under LIFO was $58,000 higher than FIFO would have allowed. The §481(a) adjustment is **+$58,000** (increase in income).

### Adjustment period

Positive and $50,000 or more → 4 tax years, ratably (Rev. Proc. 2015-13 §7.03(1)); the de minimis election is unavailable.

| Year | §481(a) included |
|------|------------------|
| 2026 (year of change) | $14,500 |
| 2027 | $14,500 |
| 2028 | $14,500 |
| 2029 | $14,500 |
| **Total** | **$58,000** |

Each year's portion goes on Form 1120-S line 5 (Other income) with a statement giving the total adjustment, the portion included, and a description of the change (2025 Instructions for Form 1120-S). It flows to the shareholders on Schedule K-1.

---

## Form 3115 (Rev. December 2022) — identification, Part I, Part II, Part IV

| Line | Field | Value |
|------|-------|-------|
| Identification | Name of filer / EIN | Granite Hardware Co. / 12-7788990 |
| Identification | Tax year of change | 01/01/2026 – 12/31/2026 |
| Identification | Type of applicant | S corporation |
| Identification | Type of change | Other: inventory, change from LIFO |
| 1a | DCN | 56 |
| 2 | Eligibility rules restrict? | No |
| 3 | All required information provided? | Yes (includes the §23.01(5) statements) |
| 4 | Cease business in 2026? | No |
| 6a | Any return under examination? | No |
| 11a | Change for same item within 5 years? | No |
| 13 | Overall method change? | No |
| 14a–14d | Item / present / proposed / overall method | Inventories in 4 pools / dollar-value LIFO / FIFO at cost / accrual |
| 17 | Proposed method used for books and financial statements? | Yes (FIFO statements for the lender) |
| 19a | Gross receipts for 2025, 2024, 2023 | Enter actual amounts (ASK) |
| 25 | Cut-off basis? | No |
| 26 | §481(a) adjustment | +$58,000 (computation attached) |
| 28 | Election | None ($58,000 is not under $50,000) |

---

## Form 3115 — Schedule D, Part II (inventories)

| Line | Field | Value |
|------|-------|-------|
| 1 | Inventory goods being changed | All merchandise inventory in the 4 LIFO pools |
| 2 | Goods not being changed | None |
| 3a | Subject to §263A? | ASK (a small business taxpayer under §263A(i) is exempt) |
| 4a | Identification method | Present: LIFO; proposed: FIFO |
| 4a | Valuation method | Present: cost; proposed: cost |
| 4b | Value at end of 2025 | Present $462,000; proposed $520,000 |
| 5a | Copies of Form 970 | Attach the 2018 Form 970 |
| 5c | Statement required by the List of Automatic Changes | Attach the §23.01(5) statements (Rev. Proc. 2025-23; the form still says Rev. Proc. 2022-14 "or its successor") |

---

## Filing logistics

| Task | Date | Detail |
|------|------|--------|
| Year of change | 2026 | Calendar tax year |
| Form 3115 prepared | with the 2026 return | DCN 56 |
| Signed copy to Ogden | between 01/01/2026 and the day the return is filed | M/S 6111 by certified mail, or fax 844-249-8134 |
| Original Form 3115 attached to 2026 Form 1120-S | by the return due date | March 15, 2027; September 15, 2027 with extension |
| §481(a) portions | 2026–2029 returns | $14,500 each on Form 1120-S line 5 |

---

## Common errors avoided

1. **Using Form 3115 to adopt LIFO**: adoption is on Form 970; Form 3115 is for changing **from** LIFO or within LIFO (Schedule C).
2. **Citing an old DCN**: DCNs are reassigned between lists; DCN 21 is now removal costs and DCN 22 is UNICAP for resellers in Rev. Proc. 2025-23. The change from LIFO is DCN 56.
3. **Skipping the §481(a) adjustment**: required for a change from LIFO (§23.01(7)).
4. **Wrong sign**: a higher FIFO beginning inventory means an increase in income.
5. **Planning to re-elect LIFO soon**: not for 5 taxable years without a non-automatic request.
6. **Forgetting the signed copy to Ogden**: the automatic change is not properly filed.

---

## Output for the user

The agent delivers to Granite's owner:

1. **Form 3115 draft** (identification, Parts I, II, IV, Schedule D Part II) for DCN 56
2. **§481(a) attachment**: pool-by-pool computation, +$58,000
3. **Adjustment schedule**: $14,500 in each of 2026–2029, with reminders for the next 3 returns
4. **Attachments list**: 2018 Form 970, §23.01(5) statements, gross receipts for line 19a
5. **Filing checklist**: original with the 2026 Form 1120-S, signed copy to Ogden
6. **Flag**: confirm the entity was never a C corporation (§1363(d)) and whether §263A applies
