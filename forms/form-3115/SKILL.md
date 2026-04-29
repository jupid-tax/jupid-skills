---
name: form-3115
description: >
  Use this skill when a taxpayer needs to file IRS Form 3115 to request consent
  to change an accounting method — e.g., changing from cash to accrual,
  correcting a prior-year depreciation error, switching inventory methods (FIFO
  to LIFO), or adopting a UNICAP capitalization method. Triggers on phrases
  like "change accounting method", "Form 3115", "cash to accrual", "DCN
  automatic change", "fix prior depreciation error", "change inventory method",
  "§481 adjustment". Most accounting method changes are AUTOMATIC under the
  current Rev. Proc. and require Form 3115 filed in duplicate (with the return
  + a copy to IRS Ogden) with no user fee. Non-automatic changes require an
  advance consent filing by year-end with a user fee. Do NOT use for: choosing
  an accounting method in the first year of business (pick a method, no change
  needed); changing tax year (Form 1128 — different); correcting an error
  within the statute of limitations on a single prior year (Form 1040-X
  amendment is the right tool); changing entity classification (Form 8832).
form: Form 3115 (Application for Change in Accounting Method)
audience: [solo, llc1, scorp]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f3115.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i3115.pdf
---

# Form 3115 — Application for Change in Accounting Method

This skill produces an audit-grade Form 3115 from the user's facts about their current method, the desired method, the change reason, and the §481(a) adjustment computation. Form 3115 is filed when the taxpayer wants the IRS to consent to a change in accounting method — broadly defined to include overall methods (cash vs. accrual), depreciation methods, inventory methods, and many specific items.

The complexity in Form 3115 lives in three places: (1) classifying the change as **automatic** (DCN-listed, no user fee, deemed consent) or **non-automatic** (advance-consent filing required, user fee, IRS reviews), (2) computing the **§481(a) adjustment** (cumulative income/expense effect of the change, spread over multiple years), and (3) **filing logistics** (duplicate copy to Ogden, timing, statement of compliance).

The agent must ASK when the change reason is unclear or when the §481 adjustment computation depends on facts the user hasn't supplied — never default.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 3115, "change accounting method", "method change", "§481", "DCN", "Rev. Proc. 2024-23" (or successor)
- The user describes crossing the $30M (3-year average) gross receipts threshold and being forced from cash to accrual under IRC §448
- The user describes discovering a prior-year depreciation error (wrong recovery period, wrong method, missed asset entirely) where the error spans 2+ years
- The user wants to change an inventory method (FIFO ↔ LIFO ↔ specific identification ↔ retail inventory method)
- The user wants to adopt UNICAP §263A or change UNICAP allocation method
- The user wants to change from impermissible to permissible method (e.g., was using cash above $30M threshold and needs to fix)
- The user wants to change overall method on a Schedule C, Schedule F, or entity return

Do **not** engage this skill when:

- The user is in their first year of business and just needs to pick an accounting method — that's a method *adoption*, not a *change*. No Form 3115 needed; just file consistently from year 1.
- The user wants to fix a single-year error within the 3-year statute of limitations — that's a **Form 1040-X** amendment, not Form 3115. Form 3115 is for changes spanning multiple years or going forward.
- The user wants to change tax year (calendar to fiscal or vice versa) — that's **Form 1128** (Application to Adopt, Change, or Retain a Tax Year), not Form 3115.
- The user wants to change entity classification (e.g., LLC default to S-corp election) — that's **Form 8832** (Entity Classification Election) and/or **Form 2553** (S-corp election), not Form 3115.
- The user is changing depreciation method on **only the current year's new asset** — that's just an election on Form 4562 in the year placed in service. Form 3115 is for changing methods on **previously placed-in-service** assets.

If the user's situation is ambiguous (e.g., "I think I've been depreciating my rental wrong for 3 years"), confirm: how many years has the wrong method been used? If 1 year, it's a 1040-X. If 2+ years, it's Form 3115 with §481(a) adjustment.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** of the change. Form 3115 has a "year of change" — the first tax year in which the new method is used.
2. **Filer's legal name and identifying number** (SSN for sole props, EIN for entities).
3. **Type of return** the change relates to (Form 1040 with Schedule C/E/F, Form 1120, Form 1120-S, Form 1065).
4. **Description of the present (current) method** — what method has been used in prior years (e.g., "cash method overall", "MACRS 39-year SL on residential rental property mistakenly treated as nonresidential").
5. **Description of the proposed (new) method** — what the taxpayer wants to use going forward (e.g., "accrual method overall", "MACRS 27.5-year SL on residential rental").
6. **Reason for the change** — voluntary improvement, mandatory under IRC threshold (e.g., §448 cash-basis disallowance for C-corps with >$30M 3-year avg gross receipts), correction of impermissible method.
7. **DCN (Designated Change Number)** if claiming automatic consent — look up in the current Rev. Proc. (Rev. Proc. 2024-23 published the most recent comprehensive list as of early 2026; verify the latest update). If no DCN matches the change, the change is non-automatic.
8. **§481(a) adjustment computation** — the cumulative net income/expense effect of using the new method since inception of the affected items, as if the new method had always been used. Positive = increases income (unfavorable to taxpayer); negative = decreases income (favorable).
9. **Spread period** for the §481(a) adjustment:
   - Positive (income-increasing): default 4-year spread over the year of change and 3 succeeding years
   - Negative (income-decreasing): generally 1-year (full deduction in year of change)
10. **Prior method changes** in the past 5 years — if yes, the new change may be ineligible for automatic consent (Section 5 of Rev. Proc. 2015-13 prior-change limitations).

---

## Workflow

### Step 1 — Confirm this is actually a method change

Ask: "Has the method been used for at least 2 consecutive years?" The IRS treats a method as "established" only after 2+ years of consistent use. A 1-year inconsistency is an error, not an established method, and is corrected via Form 1040-X (or amended entity return), not Form 3115.

Also confirm: the change is to an **accounting method**, not a tax election, classification, or entity-level change. Common confusions:
- §179 election: no Form 3115; revoke via amended return within 3 years
- §168(k) bonus opt-out: no Form 3115 to *make* the election; Form 3115 only if revoking after the year of election (and only with IRS consent)
- Tax year change: Form 1128, not 3115
- Entity classification: Form 8832 / 2553, not 3115

### Step 2 — Classify automatic vs. non-automatic

The current Rev. Proc. listing automatic accounting method changes is **Rev. Proc. 2024-23** (verify current version — may be superseded by 2025-X). It contains 200+ DCNs covering most common changes.

Common automatic-consent DCNs:

| DCN | Change | Citation in Rev. Proc. |
|-----|--------|------------------------|
| 7 | Impermissible to permissible depreciation method | Section 6.01 |
| 21 | Change in inventory cost method (LIFO to FIFO, etc.) | Section 22 |
| 31 | Cash to accrual under IRC §448 | Section 15 |
| 233 | Cash to accrual (small business §448(c) exception lost) | (verify in current Rev. Proc.) |
| 32 | Accrual to cash (small business) | Section 15 |

**Look up the DCN in the latest Rev. Proc.** before claiming automatic consent. The list updates annually with new DCNs added and old ones removed.

If no DCN matches the change → **non-automatic** filing required:
- Filed by the **last day of the year of change** (or extended due date for e-file submissions in some cases — verify current rules)
- Requires user fee (~$11,500 for non-automatic for 2025; verify 2026)
- IRS reviews case-by-case; consent not deemed
- Significantly more risk: the IRS could deny, charge interest on §481(a) adjustment, or impose conditions

### Step 3 — Compute the §481(a) adjustment

The §481(a) adjustment is the cumulative income/expense effect of switching to the new method, as if the new method had always been used since inception of the affected item.

**Positive adjustment (favorable to government, unfavorable to taxpayer)**:
- Indicates the old method under-reported income or over-reported expenses
- Typically deferred over 4 years (1/4 in year of change, 1/4 each in next 3 years)
- Exception: if positive < $50,000, may elect 1-year inclusion (small adjustment)

**Negative adjustment (favorable to taxpayer)**:
- Old method over-reported income or under-reported expenses
- Generally deductible in full in the year of change (1-year)
- Some specific changes have different spreads; consult Rev. Proc.

### Cash-to-accrual example

Cash-basis user has $80,000 of accounts receivable and $30,000 of accounts payable at the end of year prior to change. New method (accrual) would have already recognized:

- AR as income: +$80,000
- AP as expense: −$30,000
- Net §481(a) adjustment: +$50,000 (positive — taxpayer recognizes additional income over the spread period)

Spread: $50,000 / 4 years = $12,500 per year for 4 years (year of change + 3 succeeding).

### Depreciation correction example

User mistakenly used 39-year SL nonresidential method on a residential rental placed in service in 2022 ($300,000 building basis, $3,846 instead of $10,909 annual depreciation). 3 years of error (2022, 2023, 2024). Now changing to correct 27.5-year SL in 2025.

- Correct depreciation 2022-2024: 3 × $10,909 = $32,727 (with first-year proration ignored for example)
- Actual depreciation taken 2022-2024: 3 × $3,846 = $11,538
- §481(a) adjustment: $32,727 − $11,538 = **−$21,189 (negative)** — taxpayer gets a deduction equal to the under-claimed depreciation.

Because negative, full deduction in year of change (2025): −$21,189 reduces income.

### Step 4 — Identify the correct DCN

Cross-reference with Rev. Proc. 2024-23 (or current). The DCN goes on **Form 3115 Page 1, Part I, Line 1(a)** if automatic.

For depreciation method/recovery period changes, the most common DCN is **DCN 7** (Section 6.01 of Rev. Proc. 2024-23): "change from an impermissible method of accounting for depreciation to a permissible method" for assets placed in service in tax years prior to the year of change. Works when:
- The asset has been depreciated for 2+ years using the wrong method
- The user is not a "tax shelter"
- No prior method change for the same item in the past 5 years

For cash-to-accrual, common DCNs include:
- **DCN 32**: cash to accrual when not required by §448 (voluntary)
- **DCN 233**: cash to accrual when required by §448 (small business gross receipts threshold crossed)
- (Verify current numbers — DCNs occasionally renumber)

### Step 5 — Fill Form 3115 Parts I–IV

Form 3115 has four parts plus several schedules:

- **Part I**: Information about the applicant (name, ID, type of entity, year of change, present and proposed methods, DCN, prior method changes)
- **Part II**: Information for all requests (description of present/proposed methods, business reasons, §481(a) computation summary)
- **Part III**: Information for advance consent requests only (NOT used for automatic-consent filings)
- **Part IV**: §481(a) adjustment details

Schedules attached as applicable:
- **Schedule A**: Change in overall method of accounting (cash↔accrual)
- **Schedule B**: Change to deferral method for advance payments
- **Schedule C**: Change in long-term contract method
- **Schedule D**: Change in inventory method (LIFO, FIFO, retail, lower-of-cost-or-market)
- **Schedule E**: Change in depreciation or amortization method (most common for solo filers)
- **Schedule F**: Change involving financial institutions (rare for solo)

For depreciation correction (DCN 7), **Schedule E** is filled out per asset. Includes asset description, date placed in service, original method, proposed method, basis, depreciation taken to date, §481(a) adjustment per asset.

### Step 6 — Compute and document the §481(a) adjustment

Show the work explicitly. The IRS expects a detailed schedule showing:
- For each affected item: cumulative income/deduction under old method vs. new method, year by year
- Net adjustment per item
- Sum of adjustments
- Spread schedule (4-year for positive, 1-year for negative usually)

Attach the schedule to Form 3115 as a separate statement labeled "§481(a) Adjustment Schedule".

### Step 7 — File logistics

#### Automatic-consent filing

1. Attach Form 3115 to the **current-year tax return** (the year of change)
2. File a **duplicate copy** of Form 3115 (separately from the return) with the **IRS Ogden Service Center**:
   - Address (verify each year): Internal Revenue Service, Ogden, UT 84201-0054 (for automatic consent)
3. Both copies must be filed by the **return's filing due date including extensions**
4. No user fee for automatic consent
5. Consent is **deemed granted** upon filing

#### Non-automatic (advance consent) filing

1. File Form 3115 with the IRS **before the year of change ends** (must be filed by the last day of the year of change, with limited grace periods)
2. **User fee**: ~$11,500 for non-automatic (verify 2026 schedule in Rev. Proc. 2025-1 or successor — fee schedule updates annually)
3. IRS reviews case-by-case; can take 6-12+ months
4. Consent comes via a **letter ruling**; only after receiving the ruling can the taxpayer use the new method
5. Mail to the address in the current Rev. Proc. (typically Ogden or Covington — verify)

### Step 8 — Validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next steps:
- Track the §481(a) adjustment **across the spread period** (4 years if positive). Each year, include the appropriate fraction in income.
- Update the user's books to reflect the new method going forward.
- Retain the filed Form 3115 + duplicate confirmation + §481(a) schedule for at least 6 years (longer than the 3-year SOL because the §481 adjustment spans multiple years).
- For depreciation method changes (DCN 7): update the depreciation schedule going forward; file Form 4562 each year reflecting the corrected method.
- Be aware: **5-year prior-change limitation** — once a method change is made, the same item generally cannot have another method change for 5 years (Rev. Proc. 2015-13 Section 5.01). Plan accordingly.

### Step 11 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes, follow [`filing.md`](./filing.md). Form 3115 has its own filing rules (duplicate copy to Ogden + with return) that differ from typical e-filed schedules.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Information

- **Line 1**: Type of change request — automatic (1a, with DCN) or advance consent (1b, no DCN)
- **Line 2**: Tax year of change (year of change is the first year using the new method)
- **Line 3**: Type of return (1040, 1120, 1120-S, 1065, etc.)
- **Line 4**: Description of present method
- **Line 5**: Description of proposed method
- **Line 6**: Brief description of business activity, NAICS code

### Part II — Information for all requests

- **Lines 7–14**: Yes/No questions about prior method changes, IRS examination status, etc. **Most common pitfall**: Line 12 asks about prior method changes; if yes within 5 years for the same item, automatic consent may be unavailable.

### Part III — Information for advance consent requests only

- Skipped entirely if filing for automatic consent.

### Part IV — §481(a) Adjustment

- **Line 25**: Net §481(a) adjustment (positive or negative)
- **Line 26**: How spread (1-year for negative, 4-year for positive default, etc.)
- **Line 27**: Year-by-year spread schedule

### Schedule E — Depreciation/Amortization (most common)

For each asset, separate row with:
- Description
- Date placed in service
- Cost or basis
- Method used (impermissible)
- Method changing to (permissible)
- §481(a) adjustment per asset

---

## Validation

Before declaring the form ready, run these checks.

### Math checks

- [ ] §481(a) adjustment per item = (cumulative correct amount) − (cumulative actual amount)
- [ ] Sum of per-item §481(a) adjustments = total §481(a) on Line 25
- [ ] If positive and ≥$50,000: 4-year spread = Line 25 / 4 each year
- [ ] If negative: 1-year inclusion = full Line 25 in year of change (deduction)
- [ ] If positive and <$50,000: user may elect 1-year (deduction increase) — confirm election

### Sanity checks

Surface a warning if:
- [ ] DCN claimed but the change description doesn't match the DCN's coverage in current Rev. Proc.
- [ ] Method was used for <2 years → it's an error, not an established method; redirect to Form 1040-X
- [ ] Prior method change in past 5 years for same item → automatic consent unavailable per Section 5 of Rev. Proc. 2015-13
- [ ] Filing for non-automatic but no user fee budgeted (~$11,500)
- [ ] Filing for automatic but missing duplicate copy to Ogden
- [ ] §481(a) adjustment > 5% of taxpayer's gross income → high-magnitude change; consider professional review
- [ ] Yes on Line 12 (prior changes) without explanation attached
- [ ] Yes on Line 11 (under IRS examination) — Rev. Proc. 2015-13 has special rules for taxpayers under exam; method change may not be available without IRS consent

### Cross-form checks

- [ ] If depreciation change (Schedule E): Form 4562 for the year of change reflects the new method
- [ ] If overall method change (Schedule A, cash↔accrual): Schedule C or entity return reflects the new method going forward
- [ ] If inventory change (Schedule D): Schedule C Part III COGS reflects the new method

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 3115, with attached schedules. Format:

```markdown
# Form 3115 — DRAFT for tax year YYYY (Year of Change)

## Header
Name of filer: <name>
Identifying number: <SSN or EIN>
Principal business activity code: <NAICS>
Tax year of change begins: <date>
Tax year of change ends: <date>

## Part I — Information
1a. Automatic change. DCN: <number>
    OR
1b. Non-automatic (advance consent) change. (Then Part III applies.)
2.  (covered in dates above)
3.  Type of return: Form 1040 (Schedule C) | Form 1120 | Form 1120-S | Form 1065
4.  Present method: <description>
5.  Proposed method: <description>
6.  Business activity: <description and NAICS>

## Part II — Information for all requests
7.  Has the applicant filed a federal return for the immediately preceding year? Yes/No
8.  Has the applicant requested a similar change in any prior year? Yes/No (if Yes, attach explanation)
9.  Is the applicant under IRS exam? Yes/No (if Yes, special rules apply)
10. Is the applicant a member of an affiliated group? Yes/No
11. List any item NOT being changed that requires a similar method analysis. (Usually N/A)
12. Has the applicant made a method change for the same item within 5 prior years? Yes/No
13. Other tax-shelter / partnership-level questions: Yes/No each
14. Description of present method, proposed method, and business reason: (attach detailed statement)

## Part III — (Advance consent only — skipped for automatic)

## Part IV — §481(a) Adjustment
25. Net §481(a) adjustment: $X,XXX  (positive = +; negative = −)
26. Spread:
    [ ] 1-year (year of change only) — for negative or elected small positive
    [ ] 4-year (default for positive ≥$50K)
    [ ] Other (specify)
27. Year-by-year:
    Year of change (YYYY):    $X,XXX
    Succeeding year 1:         $X,XXX
    Succeeding year 2:         $X,XXX
    Succeeding year 3:         $X,XXX

## Schedule E — Change in Depreciation or Amortization (if applicable)
| Asset | Date in service | Cost basis | Old method | New method | §481(a) adj |
|-------|-----------------|-----------|------------|-----------|-------------|
| <asset 1> | YYYY-MM-DD | $X,XXX | <old> | <new> | $X,XXX |
| <asset 2> | YYYY-MM-DD | $X,XXX | <old> | <new> | $X,XXX |

(or Schedule A, Schedule D, etc., as applicable)

## §481(a) Adjustment Schedule (attached statement)
For each affected item, show:
- Cumulative correct amount under new method (from inception)
- Cumulative actual amount under old method (from inception)
- Difference (= §481(a) for that item)
Sum of differences = Line 25.

## Filing details
[ ] Original Form 3115 attached to current-year tax return
[ ] Duplicate Form 3115 mailed separately to IRS Ogden (address in Rev. Proc. 2024-23 or successor)
[ ] User fee: $0 (automatic) | $11,500 (non-automatic, verify 2026 schedule in Rev. Proc.)
[ ] Filing deadline: return due date including extensions

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Spread schedule confirmed
- DCN verified against latest Rev. Proc.
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 3115 (revision date YYYY)
- IRS Instructions for Form 3115 (revision date YYYY)
- Rev. Proc. 2024-23 (or successor): list of automatic accounting method changes
- Rev. Proc. 2015-13: general procedural rules for method changes
- Rev. Proc. 2025-1 (or successor): user fee schedule
- IRC §446 (general rule), §481 (adjustments), §448 (cash method limits for entities)
```

The draft is **not** the final filed form. The user (or their CPA) still must transcribe to the IRS Form 3115 PDF, sign, and file two copies (one with return, one to Ogden).

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 3115 line with examples
- [`references/automatic-vs-nonautomatic.md`](./references/automatic-vs-nonautomatic.md) — Decision tree for automatic vs. advance consent
- [`references/section-481-adjustment.md`](./references/section-481-adjustment.md) — §481(a) computation in depth, spread rules, examples
- [`references/dcn-catalog.md`](./references/dcn-catalog.md) — Catalog of common DCN numbers and what they cover (per Rev. Proc. 2024-23)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Filing playbook: dual-copy submission, Ogden mailing, user fees, timing

## Examples

End-to-end worked Form 3115 filings.

- [`examples/cash-to-accrual-448.md`](./examples/cash-to-accrual-448.md) — Cash-method consultant crossing $30M gross receipts (3-year average), forced to accrual under IRC §448. Automatic DCN 233.
- [`examples/depreciation-correction-dcn7.md`](./examples/depreciation-correction-dcn7.md) — Rental property owner who used 39-year SL on residential rental for 3 years; corrects to 27.5-year SL with §481(a) negative adjustment. Automatic DCN 7.
- [`examples/inventory-fifo-to-lifo.md`](./examples/inventory-fifo-to-lifo.md) — E-commerce business switching from FIFO to LIFO. Automatic DCN listed in Rev. Proc.

## Sources

- [Form 3115 (latest)](https://www.irs.gov/pub/irs-pdf/f3115.pdf) — the form itself
- [Instructions for Form 3115 (latest)](https://www.irs.gov/pub/irs-pdf/i3115.pdf)
- [About Form 3115](https://www.irs.gov/forms-pubs/about-form-3115)
- **Rev. Proc. 2024-23** (and any successor for the year of change) — comprehensive list of automatic accounting method changes with DCNs
- **Rev. Proc. 2015-13** — general procedural rules for method changes (still controlling, with periodic modifications)
- **Rev. Proc. 2025-1** (or successor) — annual user fee schedule for non-automatic consent
- IRC §446 — general rule for accounting methods
- IRC §448 — limitation on cash method of accounting (entities)
- IRC §481 — adjustments required by changes in method of accounting
- IRC §263A — UNICAP capitalization rules
- IRS Pub. 538 — Accounting Periods and Methods

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and procedures. It is not tax advice. Method changes interact with state-tax conformity, prior IRS determinations, NOL carryforwards, AMT, and many other facts. The agent invoking this skill should remind the user that a Form 3115 filing — especially non-automatic — warrants a licensed tax professional's review before submission.
