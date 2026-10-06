# Automatic vs. Non-Automatic Consent

The single most consequential decision in filing Form 3115. Get it right and the change is deemed-consented and free. Get it wrong and the change may require advance consent with a $13,225 user fee (reduced to $3,450 or $9,775 for gross income under $400,000 or $10 million; Rev. Proc. 2026-1, Appendix A) and a wait for the IRS letter.

---

## The two paths

| Aspect | Automatic consent | Non-automatic (advance consent) |
|--------|-------------------|----------------------------------|
| Procedure | Rev. Proc. 2015-13 + List of Automatic Changes (Rev. Proc. 2025-23, as modified by 2025-28) | Rev. Proc. 2015-13 + Rev. Proc. 2026-1 |
| Filing deadline | Original with the timely filed return (incl. extensions); signed copy to Ogden no later than that | During the year of change (Rev. Proc. 2015-13 §6.03(2)); late only in unusual and compelling circumstances (Reg. §301.9100-3) |
| Where filed | Original with return + signed copy to Ogden (mail or fax) | IRS National Office, Washington DC (mail, secure fax, or encrypted email; Rev. Proc. 2026-1 §9.05) |
| User fee | None | $13,225; $3,450 / $9,775 reduced (Rev. Proc. 2026-1, App. A) |
| IRS review | None — consent deemed granted | Branch reviews, may request more info, can deny |
| Time to consent | Consent deemed on proper filing | After IRS review (can take many months) |
| Audit protection | Yes (subject to exceptions) | Yes |
| Reversibility | The change is committed once filed | The change requires the consent letter before being effective |

---

## The automatic-consent decision tree

```
Step 1 — Does the change have a DCN in the current Rev. Proc.?

  Look up the change in Rev. Proc. 2025-23 (or a later list). Match by:
    - Type of change (overall method, depreciation, inventory, etc.)
    - Specific item (the affected asset/account/category)
    - Direction of change (cash → accrual, LIFO → FIFO, etc.; adopting LIFO is Form 970, not 3115)

  If no DCN matches: → NON-AUTOMATIC (Section 2)

  If a DCN matches: → continue to Step 2

Step 2 — Are any "Section 5" exclusions present?

  Per Rev. Proc. 2015-13 §5.01(1), automatic consent is NOT available if
  (unless the DCN's section waives the rule):

  a) A change for the same item was requested or made within the 5 tax
     years ending with the year of change (§5.01(1)(f), §5.05)
  b) An overall method change was requested or made within those 5 years
     (§5.01(1)(e), §5.04)
  c) The year of change is the final year of the trade or business
     (§5.01(1)(d), §5.03) — waived for DCN 7
  d) A §381(a) liquidation or reorganization occurs in the year of change
     (§5.01(1)(c))
  e) Under examination: automatic changes are generally still available,
     but with limits (§5.01(1)(a); §8.02 audit protection; Form 3115
     lines 6-7) — see "Under examination" below
  f) The DCN section's own conditions are not met

  If any apply: → NON-AUTOMATIC

  If none apply: → AUTOMATIC (Section 1)

Step 3 — Verify the DCN's specific conditions

  Each DCN in Rev. Proc. has its own conditions. Examples:
    - DCN 7 (impermissible to permissible depreciation, §6.01): property
      placed in service before the year of change, impermissible method
      used in the 2 preceding tax years (or 1-year property), not excluded
      by §6.01(1)(c)
    - DCN 122 / 257 (cash to accrual, §15.01): 257 if made in the mandatory
      §448 year (C corporation, partnership with a C corporation partner,
      or tax shelter failing the §448(c) test: $31M for 2025, $32M for
      2026); 122 otherwise
    - DCN 233 (§15.17): small business taxpayer changing TO the cash method

  If conditions fail: → NON-AUTOMATIC (or change can't be made)

  If conditions met: → File AUTOMATIC
```

---

## Common DCN coverage

These are the most common method changes for small businesses (verify in current Rev. Proc.):

### Overall method changes (Schedule A)

| DCN | Description | Rev. Proc. 2025-23 |
|-----|-------------|--------------------|
| 122 | Cash (or accrual-for-inventory/cash hybrid) to an overall accrual method, other than in the mandatory §448 year | §15.01 |
| 257 | Cash to accrual in the mandatory §448 year | §15.01 |
| 233 | Small business taxpayer changing to the overall cash method | §15.17 |
| 259 | Small business taxpayer changing to accrual for inventory and cash for all other items | §15.17 |

### Inventory and UNICAP changes (Schedules C and D)

| DCN | Description | Rev. Proc. 2025-23 |
|-----|-------------|--------------------|
| 137 | Permissible methods of identification and valuation of inventories | §22.10 |
| 230 | From currently deducting inventories to permissible inventory methods | §22.17 |
| 260 / 261 | Small business taxpayer §471(c) inventory methods | §22.18 |
| 56 | Change from the LIFO inventory method | §23.01 |
| 22 / 23 | Certain UNICAP methods used by resellers / producers | §12.01 / §12.02 |
| 234 | Small business taxpayer exception from §263A | §12.16 |

Adopting LIFO is made on Form 970 with the return, not Form 3115 (Form 970 instructions; Reg. §1.472-3).

### Depreciation changes (Schedule E)

| DCN | Description | Rev. Proc. 2025-23 |
|-----|-------------|--------------------|
| 7 | Impermissible to permissible depreciation or amortization (most common) | §6.01 |
| 8 | Permissible to permissible depreciation (no §481(a) adjustment) | §6.02 |
| 245 | Certain late elections under §168 or revocation of certain elections (only those listed) | §6.19 |

### Other common items

| DCN | Description | Rev. Proc. 2025-23 |
|-----|-------------|--------------------|
| 5 | Bad debts: reserve method to specific charge-off method | §4.01 |
| 236 | Small business taxpayer exceptions for certain long-term contracts | §19.01 |
| 223 | Start-up expenditures | §10.01 |
| 265 / 273 / 274 | Research or experimental expenditures (TCJA §174; OBBBA §174A; foreign) | §7.01–7.03 as modified by Rev. Proc. 2025-28 |

**Verify the specific DCN number in the current list before filing.** Each list (Rev. Proc. 2022-14, 2023-24, 2024-23, 2025-23) adds, removes or reassigns DCNs.

---

## Section 5 exclusions in detail

### The 5-year rule

If the taxpayer made a method change for the same item within the 5 prior tax years, automatic consent is not available for another change to that item.

Same item interpretation:
- Same asset (for depreciation changes)
- Same revenue or expense category (for overall method changes)
- Same inventory (for inventory changes)

Example: in 2022, the taxpayer changed the inventory method from FIFO to specific identification. In 2025, the taxpayer wants to change back to FIFO (DCN 137). Same item (inventory). 2022 is within the 5 tax years ending with 2025 → automatic consent not available unless the DCN section waives the rule; otherwise file non-automatic.

### Under examination

A taxpayer under examination can generally still file an automatic change, but (Rev. Proc. 2015-13 §§3.08, 6.03(3), 8.02; i3115 lines 6–8 and 25):

1. Answer Form 3115 lines 6a–6d (and 8a–8d for Appeals/court) and give a copy of the Form 3115 to the examining agent (or Appeals officer / government counsel)
2. Audit protection for prior years may not apply unless a category on line 7b applies (3-month window, 120-day window, method not before the director, negative adjustment, CAP, etc.); if the method is an issue under consideration, the change may not give audit protection
3. A positive §481(a) adjustment is taken into account over 2 tax years instead of 4, unless one of those window categories applies

When the facts are close, refer the user to a CPA: the agent should not decide audit-protection questions.

### Tax shelter

A "tax shelter" under IRC §448(d)(3) is excluded from many automatic consent procedures. Definition includes:
- Partnership / S-corp where >35% of losses are allocated to non-active limited partners / shareholders
- Reportable transactions
- Specific types of entities

Most solo filers are NOT tax shelters; the rule mainly affects investor-driven partnerships.

### Final year of business

Automatic consent is generally not available if the year of change is the final year of the trade or business (Rev. Proc. 2015-13 §5.03), unless the DCN section waives the rule (DCN 7 does). Separately, if the taxpayer ceases the trade or business during an adjustment period, the remaining §481(a) balance is taken into account in the year of cessation (§7.03(4)).

---

## Non-automatic filing — when it's the only option

Common scenarios:

1. **No matching DCN** for the change. Example: a niche industry-specific accounting method not in Rev. Proc.
2. **5-year rule excludes** automatic consent. The taxpayer changed the same item recently.
3. **Under exam** for the issue.
4. **Specific change requires advance consent** per Rev. Proc. (some changes are designated non-automatic by the IRS).

Non-automatic filings:
- Filed during the year of change (Rev. Proc. 2015-13 §6.03(2)); no general grace period
- $13,225 user fee, or $3,450 / $9,775 reduced (Rev. Proc. 2026-1, Appendix A; the annual successor revenue procedure is published each January)
- IRS National Office in Washington DC processes
- Taxpayer waits for the letter / consent agreement
- Until the ruling is received, the taxpayer continues using the OLD method
- After the ruling, the taxpayer implements the new method for the year of change, with the §481(a) adjustment

---

## Cost-benefit analysis

For most small-business changes:
- Automatic consent costs: time to research DCN + duplicate copy mailing
- Non-automatic costs: $13,225 user fee (or reduced fee) + tax professional fees + months of uncertainty

Solo filers and small businesses should almost always use automatic consent if available. The exceptions are typically driven by exam status or the 5-year rule.

If the change isn't on the automatic list, the alternative is often to **delay** the change to a future year when:
- The 5-year rule no longer applies
- The taxpayer is no longer under exam
- The IRS adds the DCN in a future Rev. Proc.

But delay isn't always possible — for §448 cash-method limits, the change is mandatory in the year the threshold is crossed.

---

## Citations

- Rev. Proc. 2025-23 (as modified by Rev. Proc. 2025-28): current list of automatic accounting method changes (check for a successor)
- Rev. Proc. 2015-13: general procedural rules for method changes (still controlling, with periodic modifications)
- Rev. Proc. 2026-1: user fee schedule (Appendix A) and Form 3115 addresses (§§9.05–9.06)
- IRC §446: general rule for accounting methods
- IRC §448: cash method limitation
- IRC §263A: UNICAP rules
- IRC §481: adjustments required by changes
- Reg. §1.446-1(e)(3)(i): consent requirement; Reg. §§301.9100-2, 301.9100-3: extensions of time (automatic 6-month extension for automatic changes; discretionary relief otherwise)
- Form 970 and Reg. §1.472-3: adopting LIFO
- IRS Pub. 538: Accounting Periods and Methods
