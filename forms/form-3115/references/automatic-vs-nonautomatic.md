# Automatic vs. Non-Automatic Consent

The single most consequential decision in filing Form 3115. Get it right and the change is deemed-consented and free. Get it wrong and the IRS rejects, and the change requires advance consent with an $11,500+ user fee and 6-12 months of waiting.

---

## The two paths

| Aspect | Automatic consent | Non-automatic (advance consent) |
|--------|-------------------|----------------------------------|
| Procedure | Rev. Proc. 2024-23 (or successor) | Rev. Proc. 2015-13 (general procedural) |
| Filing deadline | Return due date including extensions | Last day of year of change (with 6-month grace under Reg. §1.446-1(e)(3)(i) for some) |
| Where filed | Original with return + duplicate to Ogden | Single copy to IRS national office (Washington DC area) |
| User fee | None | ~$11,500 (Rev. Proc. 2025-1; verify 2026) |
| IRS review | None — consent deemed granted | Branch reviews, may request more info, can deny |
| Time to consent | Immediate (filed = consented) | 6-12+ months for letter ruling |
| Audit protection | Yes (subject to exceptions) | Yes |
| Reversibility | The change is committed once filed | The change requires the consent letter before being effective |

---

## The automatic-consent decision tree

```
Step 1 — Does the change have a DCN in the current Rev. Proc.?

  Look up the change in Rev. Proc. 2024-23 (or successor). Match by:
    - Type of change (overall method, depreciation, inventory, etc.)
    - Specific item (the affected asset/account/category)
    - Direction of change (cash → accrual, FIFO → LIFO, etc.)

  If no DCN matches: → NON-AUTOMATIC (Section 2)

  If a DCN matches: → continue to Step 2

Step 2 — Are any "Section 5" exclusions present?

  Per Rev. Proc. 2015-13 Section 5, automatic consent is NOT available if:

  a) The change is for the same item that was previously changed within
     the 5 prior tax years (the "5-year rule")
  b) The taxpayer is currently under IRS examination, and the change is to
     an item under exam
  c) The taxpayer's prior return is before Appeals or in federal court for
     the same issue
  d) The taxpayer is a "tax shelter" (Code §448(d)(3))
  e) The taxpayer is in the final year of business
  f) Other specific exclusions per Rev. Proc.

  If any apply: → NON-AUTOMATIC

  If none apply: → AUTOMATIC (Section 1)

Step 3 — Verify the DCN's specific conditions

  Each DCN in Rev. Proc. has its own conditions. Examples:
    - DCN 7 (impermissible to permissible depreciation): requires that the
      taxpayer is changing for an asset placed in service before the year
      of change
    - DCN 32 (cash to accrual, voluntary): the taxpayer must have used cash
      method for at least 2 years
    - DCN 233 (cash to accrual, §448): mandatory for entities crossing the
      $30M 3-year average gross receipts threshold

  If conditions fail: → NON-AUTOMATIC (or change can't be made)

  If conditions met: → File AUTOMATIC
```

---

## Common DCN coverage

These are the most common method changes for small businesses (verify in current Rev. Proc.):

### Overall method changes (Schedule A)

| DCN | Description |
|-----|-------------|
| 32 | Cash to accrual, voluntary (small business) |
| 33 | Accrual to cash, small business under §448(c) thresholds |
| 233 | Cash to accrual, mandatory for entities crossing §448 limits |
| 235 | Cash to accrual for personal service corporations |

### Inventory changes (Schedule D)

| DCN | Description |
|-----|-------------|
| 21 | LIFO method (multiple sub-DCNs depending on direction and sub-method) |
| 22 | UNICAP §263A adoption |
| 23 | UNICAP allocation method change |

### Depreciation changes (Schedule E)

| DCN | Description |
|-----|-------------|
| 7 | Impermissible to permissible depreciation method (most common) |
| 88 | Late §168(g) election (ADS) |
| 89 | Late §168(k) opt-out election |

### Specific item changes

| DCN | Description |
|-----|-------------|
| 14 | Bad debt method (specific charge-off vs. reserve) |
| 16 | Long-term contract method |
| 184 | UNICAP exempt small business under §263A(i) |

**Verify the specific DCN number in the current Rev. Proc. before filing.** DCN renumbering happens periodically (Rev. Proc. 2018-31, then 2019-43, then 2022-14, then 2024-23 — each version may add, remove, or renumber DCNs).

---

## Section 5 exclusions in detail

### The 5-year rule

If the taxpayer made a method change for the same item within the 5 prior tax years, automatic consent is not available for another change to that item.

Same item interpretation:
- Same asset (for depreciation changes)
- Same revenue or expense category (for overall method changes)
- Same inventory (for inventory changes)

Example: in 2022, the taxpayer changed the inventory method from FIFO to specific identification. In 2025, the taxpayer wants to change to LIFO. Same item (inventory). 2025 is within 5 years of 2022 → automatic consent not available; must file non-automatic.

### Under examination

If the IRS is currently auditing the taxpayer, and the issue under audit relates to the method being changed, automatic consent is not available. The taxpayer must:

1. Obtain consent from the IRS area office (often via the audit team)
2. File Form 3115 within 30 days of the audit team's consent (or 90 days, depending on the change)
3. Include the area office's consent letter with the Form 3115 filing

If the IRS is auditing unrelated issues, automatic consent is generally still available — but the taxpayer must:
- Disclose the audit on Line 9 of Part II
- Verify under Rev. Proc. 2015-13 that the specific change being made is not affected

### Tax shelter

A "tax shelter" under IRC §448(d)(3) is excluded from many automatic consent procedures. Definition includes:
- Partnership / S-corp where >35% of losses are allocated to non-active limited partners / shareholders
- Reportable transactions
- Specific types of entities

Most solo filers are NOT tax shelters; the rule mainly affects investor-driven partnerships.

### Final year of business

If the year of change is also the final year of business, the entire §481(a) adjustment is recognized in that year (acceleration rule). Some DCNs are still available; others aren't. Verify per the specific DCN.

---

## Non-automatic filing — when it's the only option

Common scenarios:

1. **No matching DCN** for the change. Example: a niche industry-specific accounting method not in Rev. Proc.
2. **5-year rule excludes** automatic consent. The taxpayer changed the same item recently.
3. **Under exam** for the issue.
4. **Specific change requires advance consent** per Rev. Proc. (some changes are designated non-automatic by the IRS).

Non-automatic filings:
- Filed by year-end of the year of change (or grace period)
- $11,500+ user fee per Rev. Proc. 2025-1 (verify 2026 — typically published in January)
- IRS National Office in Washington DC processes
- Taxpayer waits for letter ruling (6-12+ months typical)
- Until the ruling is received, taxpayer continues using the OLD method
- After ruling, taxpayer applies new method retroactively to year of change via §481(a)

---

## Cost-benefit analysis

For most small-business changes:
- Automatic consent costs: time to research DCN + duplicate copy mailing
- Non-automatic costs: $11,500 user fee + tax professional fees + 6-12 months of uncertainty

Solo filers and small businesses should almost always use automatic consent if available. The exceptions are typically driven by exam status or the 5-year rule.

If the change isn't on the automatic list, the alternative is often to **delay** the change to a future year when:
- The 5-year rule no longer applies
- The taxpayer is no longer under exam
- The IRS adds the DCN in a future Rev. Proc.

But delay isn't always possible — for §448 cash-method limits, the change is mandatory in the year the threshold is crossed.

---

## Citations

- Rev. Proc. 2024-23: comprehensive list of automatic accounting method changes (verify successor for current year)
- Rev. Proc. 2015-13: general procedural rules for method changes (still controlling, with periodic modifications)
- Rev. Proc. 2025-1: annual user fee schedule (verify 2026 successor)
- IRC §446: general rule for accounting methods
- IRC §448: cash method limitation
- IRC §263A: UNICAP rules
- IRC §481: adjustments required by changes
- Reg. §1.446-1(e)(3)(i): 6-month grace period for some non-automatic changes
- IRS Pub. 538: Accounting Periods and Methods
