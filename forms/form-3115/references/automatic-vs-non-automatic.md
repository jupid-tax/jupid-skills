# Automatic vs Non-Automatic Filing Logistics

A practical filing logistics companion to the conceptual treatment in `automatic-vs-nonautomatic.md`. This file answers the operational questions: *Where do I send the duplicate? What is the year-end deadline mechanically? How is the §481(a) spread chosen? What does the user fee actually buy?*

Use this when the agent has already classified the change (automatic vs non-automatic via DCN matching) and now needs to execute the filing.

---

## The duplicate-filing rule (automatic only)

Automatic-consent Form 3115 is filed **in duplicate**:

1. **Original** — attached to the timely filed (including extensions) federal income tax return for the year of change.
2. **Signed copy (duplicate)** — filed separately with the IRS in Ogden, Utah (Rev. Proc. 2026-1 §9.06; Instructions for Form 3115, Address Chart):

```
Mail:                      Internal Revenue Service
                           Ogden, UT 84201
                           M/S 6111
Private delivery service:  Internal Revenue Service
                           1973 N. Rulon White Blvd.
                           Ogden, UT 84201
                           Attn: M/S 6111
Fax:                       844-249-8134 (with a cover sheet)
```

The signed copy must be filed **no earlier than** the first day of the year of change and **no later than** the date the original is filed with the return (Rev. Proc. 2015-13 §6.03(1)(a)(i)(B)). It may be a photocopy; the original attached to the return does not need to be signed (i3115). The IRS does not acknowledge receipt, so keep the certified mail receipt or fax confirmation.

**Common error**: filing only the original with the return. The Ogden copy is a filing requirement of the automatic change procedures; without it, the change is not properly filed under those procedures.

For non-automatic filings the duplicate-copy rule does not apply; a single copy goes to the IRS National Office in Washington DC.

---

## Year-end deadline mechanics

### Automatic consent

Deadline = **due date of the return for the year of change, including extensions**.

| Filer | Year-of-change return | Earliest filing | Latest filing (with extension) |
|-------|------------------------|-----------------|-------------------------------|
| Calendar-year individual / sole prop | 2025 Form 1040 | Mid-January 2026 | October 15, 2026 |
| Calendar-year S-corp | 2025 Form 1120-S | Late January 2026 | September 15, 2026 |
| Calendar-year C-corp | 2025 Form 1120 | Late January 2026 | October 15, 2026 |
| Fiscal-year filer | Year-of-change return | First day of next year | 6 months after due date |

The Form 3115 must be **attached to** the return and the duplicate copy mailed **before or simultaneously with** the return filing.

### Non-automatic (advance consent)

Deadline = **during the year of change** (on or before its last day) for most changes (Rev. Proc. 2015-13 §6.03(2)).

For calendar-year 2026 changes, the non-automatic Form 3115 must be filed at the IRS National Office by **December 31, 2026** — not by the return due date. This is the trap: by the time the taxpayer is preparing the return in spring 2027, the non-automatic deadline has already passed.

**No general grace period.** A late non-automatic Form 3115 is accepted only in unusual and compelling circumstances, through a letter ruling request under Reg. §301.9100-3 with its own user fee (i3115, "Late Application"). For automatic changes, an automatic 6-month extension from the unextended return due date may be available (Rev. Proc. 2015-13 §6.03(4)(a); Reg. §301.9100-2).

---

## User fee — what $13,225 actually buys

The user fee for a non-automatic Form 3115 (Rev. Proc. 2026-1, Appendix A; a successor is published each January):

| Filer category | Fee (requests received in 2026) |
|----------------|----------------------------------|
| Standard non-automatic Form 3115 | $13,225 ((A)(3)(b)(i)) |
| Gross income of $400,000 or more but under $10 million | $9,775 ((A)(4)(b)) |
| Gross income under $400,000 | $3,450 ((A)(4)(a)) |
| Letter ruling for an extension of time to file Form 3115 (§301.9100-3) | $13,900 ((A)(3)(b)(ii)); reduced fees per (A)(4) |

Pay the full fee through www.pay.gov before submitting and include the receipt (Rev. Proc. 2026-1 §9.05). Reduced fees need the certification in Appendix A (B)(1). **No fee** for automatic-consent filings.

What the fee buys:
- IRS Branch reviews the application and may request additional information (typically 1-3 rounds of correspondence)
- Branch issues a **letter ruling** consenting to (or denying) the change
- The letter is binding on the IRS for the specific facts
- Audit protection for prior years (within Rev. Proc. limits)

What the fee does **not** buy:
- A guarantee of approval — the IRS can deny
- A specific timeline — processing can take many months
- Retroactive consent for years before the year of change

The fee is **not refundable** if the application is withdrawn, denied, or returned incomplete.

---

## §481(a) spread — automatic decision rules

The §481(a) adjustment is the cumulative net effect of changing methods (see `section-481-adjustment.md` for computation). Once computed, the spread rules determine when the income (or deduction) hits the return.

### Default spread

```
if §481(a) is negative (taxpayer-favorable, i.e., deduction):
    → 1-year spread (entire deduction in year of change)

elif §481(a) is positive AND amount < $50,000:
    → 4-year spread (default), OR 1-year de minimis election (Form 3115 line 28)

elif §481(a) is positive AND amount ≥ $50,000:
    → 4-year spread: 1/4 in year of change + 1/4 each of next 3 years
      (1-year only with the eligible acquisition transaction election)

if the taxpayer is under examination (positive adjustment):
    → 2-year spread unless a Form 3115 line 7b window category applies
```

Source: Rev. Proc. 2015-13 §7.03(1), (3)(c)–(d); i3115, Lines 25 and 28.

### Why the rules are asymmetric

The asymmetry is intentional:
- **Negative §481(a)** = taxpayer overpaid in prior years (under old method) → IRS allows immediate full deduction (no benefit to the IRS in spreading a refund-like deduction)
- **Positive §481(a)** = taxpayer underpaid in prior years → IRS spreads the income over 4 years to avoid bunching tax in one year (revenue-positive for the government, taxpayer-friendly relative to a 1-year recognition)

### When the 1-year election is favorable

Election to recognize positive §481(a) in 1 year (instead of 4) makes sense when:
- The taxpayer expects to be in a lower tax bracket in the year of change than in succeeding years (e.g., low-income year, retirement transition)
- The taxpayer is using NOLs that would otherwise expire
- The §481(a) is small enough that bracket-creep isn't an issue

The election is made on the Form 3115 itself (Part IV, line 28).

### Acceleration — the cessation rule

Any remaining §481(a) is taken into account in the year the taxpayer ceases to engage in the trade or business (Rev. Proc. 2015-13 §7.03(4)(a)). Cessation includes terminating existence, ceasing operation, or transferring substantially all the assets, for example incorporating the business, a §1060 sale, a taxable liquidation, or contributing the assets to a partnership (§3.04).

Example: positive §481(a) of $60,000 spread over 4 years ($15,000/year). Year 1 done; in year 2, the business closes. Remaining $45,000 is recognized in year 2 (the year-2 portion plus the two unused future portions).

This rule is why method changes near the end of a business's life are often unfavorable — there's no time to spread the gain.

---

## DCN-specific spread overrides

Some Designated Change Numbers override the default spread. Verify against current Rev. Proc.:

| DCN | Change | Adjustment rule |
|-----|--------|-----------------|
| 7 | Impermissible to permissible depreciation (§6.01) | Default periods |
| 8 | Permissible to permissible depreciation (§6.02) | No §481(a) adjustment (neither required nor permitted) |
| 122 / 257 | Cash to accrual (§15.01) | Default periods; read §15.01 for concurrent changes |
| 233 | Small business taxpayer to cash (§15.17) | Read §15.17; some variants are cut-off |
| 56 | Change from LIFO (§23.01) | §481(a) adjustment required (§23.01(7)) |

When in doubt, the DCN's section in Rev. Proc. 2025-23 (or a later list) governs.

---

## Filing checklist — automatic

- [ ] DCN identified and verified against current Rev. Proc.
- [ ] Rev. Proc. 2015-13 §5.01(1) eligibility rules checked (5-year rules, final year, §381 transaction, exam limits)
- [ ] §481(a) computed and documented on attached schedule
- [ ] Adjustment period determined (default, or line 28 election for positive < $50K)
- [ ] Original Form 3115 attached to return (signature not required on the original)
- [ ] Signed copy prepared (photocopy acceptable)
- [ ] Signed copy mailed to Ogden (certified mail) or faxed to 844-249-8134 by the date the return is filed
- [ ] Information and statements required by the DCN section attached (Part I, line 3)
- [ ] Copy retained for records (recommended retention: 7 years past final spread year)

## Filing checklist — non-automatic

- [ ] No DCN matches OR DCN-conditions fail OR an eligibility rule applies
- [ ] User fee determined ($13,225 standard; $9,775 / $3,450 reduced)
- [ ] Application prepared per Rev. Proc. 2015-13 and Rev. Proc. 2026-1
- [ ] Filed with IRS National Office in Washington DC during the year of change
- [ ] User fee paid on pay.gov, receipt enclosed
- [ ] §481(a) computed and documented (provisionally — IRS may require revisions)
- [ ] Continue using OLD method until letter ruling received
- [ ] Upon letter ruling, apply NEW method retroactively to year of change

---

## Common filing errors

1. **Filing only the original (no duplicate to Ogden)** — invalidates automatic consent.
2. **Filing automatic Form 3115 after the return due date** — too late; the change isn't valid for the intended year of change.
3. **Filing non-automatic Form 3115 after the last day of the year of change** — the change isn't available for that year without §301.9100-3 relief.
4. **Wrong DCN cited** — the application is treated as for the cited DCN; if the cited DCN doesn't actually cover the change, consent isn't granted.
5. **Missing §481(a) schedule** — line 26 requires a summary of the computation and methodology.
6. **Same item changed within the 5 tax years ending with the year of change** — automatic consent generally isn't available unless waived; file non-automatic with user fee.
7. **Using the wrong Rev. Proc. version** — DCNs are renumbered periodically; an outdated DCN reference can invalidate the filing.

---

## Citations

- Rev. Proc. 2025-23 (as modified by Rev. Proc. 2025-28) — current DCN list
- Rev. Proc. 2015-13 — general procedural rules for accounting method changes
- Rev. Proc. 2026-1, Appendix A and §§9.05–9.06 — user fees and addresses
- IRC §446(e) — IRS consent required for method changes
- IRC §481(a) — cumulative adjustment rule
- Reg. §§301.9100-2, 301.9100-3 — extensions of time
- Reg. §1.481-1 through -5 — §481(a) computation and spread rules
- Form 3115 instructions (current year)
- IRS Pub. 538 — Accounting Periods and Methods
