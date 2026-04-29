# Automatic vs Non-Automatic Filing Logistics

A practical filing logistics companion to the conceptual treatment in `automatic-vs-nonautomatic.md`. This file answers the operational questions: *Where do I send the duplicate? What is the year-end deadline mechanically? How is the §481(a) spread chosen? What does the user fee actually buy?*

Use this when the agent has already classified the change (automatic vs non-automatic via DCN matching) and now needs to execute the filing.

---

## The duplicate-filing rule (automatic only)

Automatic-consent Form 3115 is filed **in duplicate**:

1. **Original** — attached to the timely filed (including extensions) federal income tax return for the year of change.
2. **Duplicate copy** — mailed separately to the IRS National Office in Ogden, Utah:

```
Internal Revenue Service
Ogden, UT 84201-0010
ATTN: Ogden Submission Processing — M/S 6111
```

The duplicate copy must be sent **no earlier than** the first day of the year of change and **no later than** the date the original return is filed (including extensions). Most practitioners mail the duplicate the same week the return is filed, using certified mail with return receipt for proof.

**Common error**: filing only the original with the return. Without the duplicate copy, the IRS treats the consent as **not granted** — the change is invalid and the taxpayer remains on the old method.

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

Deadline = **last day of the year of change** for most changes.

For calendar-year 2025 changes, the non-automatic Form 3115 must be filed at the IRS National Office by **December 31, 2025** — not by the return due date. This is the trap: by the time the taxpayer is preparing the return in spring 2026, the non-automatic deadline has already passed.

**Reg. §1.446-1(e)(3)(i) grace period**: a 6-month extension is available for some (not all) non-automatic changes if the taxpayer files Form 3115 within 6 months of the original deadline AND the taxpayer's failure was due to "reasonable cause" (a high bar). Verify the specific change qualifies.

---

## User fee — what $11K actually buys

The user fee (Rev. Proc. 2025-1, Appendix A — verify 2026 successor) is **~$11,500** for most non-automatic accounting method changes, with reduced fees for:

| Filer category | Fee (2025; verify 2026) |
|----------------|--------------------------|
| Standard non-automatic Form 3115 | $11,500 |
| Small business (gross income < $1M, 3-year average) | $2,800 |
| Sub-small business (gross income < $250K) | $1,140 |

The fee is paid by check or via Pay.gov when the application is filed. **No fee** for automatic-consent filings.

What the fee buys:
- IRS Branch reviews the application and may request additional information (typically 1-3 rounds of correspondence)
- Branch issues a **letter ruling** consenting to (or denying) the change
- The letter is binding on the IRS for the specific facts
- Audit protection for prior years (within Rev. Proc. limits)

What the fee does **not** buy:
- A guarantee of approval — the IRS can deny
- A specific timeline — typical processing is 6-12 months, sometimes longer
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
    → 4-year spread (default), OR 1-year election available

elif §481(a) is positive AND amount ≥ $50,000:
    → 4-year spread (mandatory): 1/4 in year of change + 1/4 each of next 3 years
```

### Why the rules are asymmetric

The asymmetry is intentional:
- **Negative §481(a)** = taxpayer overpaid in prior years (under old method) → IRS allows immediate full deduction (no benefit to the IRS in spreading a refund-like deduction)
- **Positive §481(a)** = taxpayer underpaid in prior years → IRS spreads the income over 4 years to avoid bunching tax in one year (revenue-positive for the government, taxpayer-friendly relative to a 1-year recognition)

### When the 1-year election is favorable

Election to recognize positive §481(a) in 1 year (instead of 4) makes sense when:
- The taxpayer expects to be in a lower tax bracket in the year of change than in succeeding years (e.g., low-income year, retirement transition)
- The taxpayer is using NOLs that would otherwise expire
- The §481(a) is small enough that bracket-creep isn't an issue

The election is made on the Form 3115 itself (Part IV) and is **irrevocable** once filed.

### Acceleration — the cessation rule

Any remaining §481(a) is fully recognized in the year of:
- Cessation of the trade or business (sale, closure)
- Death of the taxpayer (sole prop)
- Liquidation of the entity
- Bankruptcy filing
- Cancellation of the method change

Example: positive §481(a) of $40,000 spread over 4 years ($10,000/year). Year 1 done; in year 2, the business closes. Remaining $30,000 ($10,000 × 3 years) all recognized in year 2.

This rule is why method changes near the end of a business's life are often unfavorable — there's no time to spread the gain.

---

## DCN-specific spread overrides

Some Designated Change Numbers override the default spread. Verify against current Rev. Proc.:

| DCN | Change | Spread rule |
|-----|--------|-------------|
| 7 | Impermissible to permissible depreciation | Default (4-year for positive ≥ $50K) |
| 32 | Cash to accrual (small business voluntary) | Default |
| 184 | UNICAP exempt small business | Default |
| 233 | Cash to accrual (mandatory under §448) | Default, but special transition rules — verify |
| 21 (LIFO family) | Inventory method changes | Layer-by-layer treatment, complex |
| 16 | Long-term contract method | Contract-by-contract, not aggregated |

When in doubt, the DCN's section in Rev. Proc. 2024-23 (or successor) governs.

---

## Filing checklist — automatic

- [ ] DCN identified and verified against current Rev. Proc.
- [ ] Section 5 exclusions checked (5-year rule, exam status, tax shelter, final year)
- [ ] §481(a) computed and documented on attached schedule
- [ ] Spread elected (default or 1-year for positive < $50K)
- [ ] Original Form 3115 attached to return
- [ ] Duplicate copy prepared with cover letter
- [ ] Duplicate mailed to Ogden via certified mail with return receipt
- [ ] Statement of compliance with all DCN conditions (Part IV)
- [ ] Signature on Form 3115 by taxpayer or authorized representative
- [ ] Copy retained for records (recommended retention: 7 years past final spread year)

## Filing checklist — non-automatic

- [ ] No DCN matches OR DCN-conditions fail OR Section 5 exclusion present
- [ ] User fee determined ($11,500 standard; reduced for small business)
- [ ] Application prepared per Rev. Proc. 2015-13 and Rev. Proc. 2025-1
- [ ] Filed with IRS National Office in Washington DC by year-end
- [ ] User fee paid (check or Pay.gov)
- [ ] §481(a) computed and documented (provisionally — IRS may require revisions)
- [ ] Continue using OLD method until letter ruling received
- [ ] Upon letter ruling, apply NEW method retroactively to year of change

---

## Common filing errors

1. **Filing only the original (no duplicate to Ogden)** — invalidates automatic consent.
2. **Filing automatic Form 3115 after the return due date** — too late; the change isn't valid for the intended year of change.
3. **Filing non-automatic Form 3115 after December 31** — same issue; the change isn't valid for the year.
4. **Wrong DCN cited** — the application is treated as for the cited DCN; if the cited DCN doesn't actually cover the change, consent isn't granted.
5. **Missing §481(a) schedule** — the IRS rejects applications without the cumulative computation.
6. **Same item changed twice within 5 years** — automatic consent isn't available; must file non-automatic with user fee.
7. **Using the wrong Rev. Proc. version** — DCNs are renumbered periodically; an outdated DCN reference can invalidate the filing.

---

## Citations

- Rev. Proc. 2024-23 (or successor) — automatic consent procedures and DCN list
- Rev. Proc. 2015-13 — general procedural rules for accounting method changes
- Rev. Proc. 2025-1, Appendix A — annual user fee schedule
- IRC §446(e) — IRS consent required for method changes
- IRC §481(a) — cumulative adjustment rule
- Reg. §1.446-1(e)(3)(i) — six-month grace period for non-automatic
- Reg. §1.481-1 through -5 — §481(a) computation and spread rules
- Form 3115 instructions (current year)
- IRS Pub. 538 — Accounting Periods and Methods
