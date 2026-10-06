---
name: form-3115
description: >
  Use this skill when a taxpayer needs to file IRS Form 3115 to request consent
  to change an accounting method — e.g., changing from cash to accrual,
  correcting a prior-year depreciation error, switching inventory methods (e.g.
  from LIFO to FIFO), or changing a UNICAP capitalization method. Triggers on phrases
  like "change accounting method", "Form 3115", "cash to accrual", "DCN
  automatic change", "fix prior depreciation error", "change inventory method",
  "§481 adjustment". Most accounting method changes are AUTOMATIC under the
  current List of Automatic Changes (Rev. Proc. 2025-23) and require Form 3115
  filed in duplicate (with the return + a signed copy to IRS Ogden) with no user
  fee. Non-automatic changes require an advance consent filing during the year
  of change with a user fee. Do NOT use for: choosing an accounting method in the
  first year of business (pick a method, no change needed); adopting LIFO (Form
  970); changing tax year (Form 1128 — different); correcting an error that is not
  a method (Form 1040-X or amended entity return); changing entity classification
  (Form 8832) or electing S status (use form-2553).
form: Form 3115 (Application for Change in Accounting Method)
audience: [solo, llc1, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f3115.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i3115.pdf
---

# Form 3115 — Application for Change in Accounting Method

This skill produces an audit-grade Form 3115 from the user's facts about their current method, the desired method, the change reason, and the §481(a) adjustment computation. Form 3115 is filed when the taxpayer wants the IRS to consent to a change in accounting method — broadly defined to include overall methods (cash vs. accrual), depreciation methods, inventory methods, and many specific items.

The complexity in Form 3115 lives in three places: (1) classifying the change as **automatic** (DCN-listed, no user fee, deemed consent) or **non-automatic** (advance-consent filing required, user fee, IRS reviews), (2) computing the **§481(a) adjustment** (cumulative income/expense effect of the change, spread over multiple years), and (3) **filing logistics** (duplicate copy to Ogden, timing, statement of compliance).

The agent must ASK when the change reason is unclear or when the §481 adjustment computation depends on facts the user hasn't supplied — never default.

**Form revision:** the line map in this skill was verified on 2026-10-06 against Form 3115 (Rev. December 2022) and the Instructions for Form 3115 (Rev. December 2022), still the current revisions (About Form 3115, updated 30-Mar-2026, lists no newer revision). The instructions still cite Rev. Proc. 2022-14 and Rev. Proc. 2023-1; use the current List of Automatic Changes, **Rev. Proc. 2025-23** (effective for Forms 3115 filed on or after June 9, 2025), as modified by **Rev. Proc. 2025-28** for research or experimental expenditures, and the current user fee and filing-address procedure, **Rev. Proc. 2026-1**. Re-check https://www.irs.gov/forms-pubs/about-form-3115 for a newer form revision or list before each use.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 3115, "change accounting method", "method change", "§481", "DCN", "Rev. Proc. 2025-23" (or successor)
- A C corporation, a partnership with a C corporation partner, or a tax shelter fails the §448(c) gross receipts test (3-year average above $31,000,000 for tax years beginning in 2025, $32,000,000 for 2026; Rev. Proc. 2024-40 §2.31, Rev. Proc. 2025-32 §4.30) and must leave the cash method under IRC §448. Sole proprietors and S corporations are not subject to §448 (unless a tax shelter), but the same test governs the small business exceptions in §§263A(i), 460(e) and 471(c)
- The user wants to deduct domestic research or experimental expenditures under new §174A (P.L. 119-21 §70302) or change a §174 method (Rev. Proc. 2025-28, DCNs 265, 273, 274)
- The user describes discovering a prior-year depreciation error (wrong recovery period, wrong method, missed asset entirely) where the error spans 2+ years
- The user wants to change an inventory method (for example from LIFO to FIFO, among permissible identification/valuation methods, or to a §471(c) small business method). Adopting LIFO is not a Form 3115 change: it is made on Form 970 with the return (Reg. §1.472-3)
- The user wants to adopt UNICAP §263A or change UNICAP allocation method
- The user wants to change from an impermissible to a permissible method (e.g., a C corporation that stayed on cash after failing the §448(c) test)
- The user wants to change overall method on a Schedule C, Schedule F, or entity return

Do **not** engage this skill when:

- The user is in their first year of business and just needs to pick an accounting method — that's a method *adoption*, not a *change*. No Form 3115 needed; just file consistently from year 1.
- The user wants to fix a mathematical or posting error, or an impermissible method used on only one filed return — that's an amended return (**Form 1040-X** or the entity equivalent), not Form 3115. An impermissible method becomes the taxpayer's method once used on two consecutively filed returns (Reg. §1.446-1(e)(2)(ii)(a), (d)(2)). Exception: depreciable property placed in service in the tax year immediately before the year of change may be changed under DCN 7 instead of amending (Rev. Proc. 2025-23 §6.01(1)(b)).
- The user wants to change tax year (calendar to fiscal or vice versa) — that's **Form 1128** (Application to Adopt, Change, or Retain a Tax Year), not Form 3115.
- The user wants to change entity classification (e.g., LLC default to S-corp election) — that's **Form 8832** (Entity Classification Election) and/or **Form 2553** (S-corp election), not Form 3115.
- The user is changing depreciation method on **only the current year's new asset** — that's just an election on Form 4562 in the year placed in service. Form 3115 is for changing methods on **previously placed-in-service** assets.

If the user's situation is ambiguous (e.g., "I think I've been depreciating my rental wrong for 3 years"), confirm: on how many filed returns has the wrong method been used? If one, an amended return (or DCN 7 for property placed in service in the immediately preceding year). If two or more consecutive returns, it's Form 3115 with a §481(a) adjustment.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask explicitly** and stop until you get an answer.

1. **Tax year** of the change. Form 3115 has a "year of change" — the first tax year in which the new method is used.
2. **Filer's legal name and identifying number** (SSN for sole props, EIN for entities).
3. **Type of return** the change relates to (Form 1040 with Schedule C/E/F, Form 1120, Form 1120-S, Form 1065).
4. **Description of the present (current) method** — what method has been used in prior years (e.g., "cash method overall", "MACRS 39-year SL on residential rental property mistakenly treated as nonresidential").
5. **Description of the proposed (new) method** — what the taxpayer wants to use going forward (e.g., "accrual method overall", "MACRS 27.5-year SL on residential rental").
6. **Reason for the change** — voluntary improvement, mandatory (e.g., §448 for a C corporation whose 3-year average gross receipts exceed $31M for 2025 / $32M for 2026), correction of an impermissible method.
7. **DCN (designated automatic accounting method change number)** if claiming automatic consent — look up in the current List of Automatic Changes (Rev. Proc. 2025-23, as modified by Rev. Proc. 2025-28; check for a later list). If no DCN matches the change, the change is non-automatic.
8. **§481(a) adjustment computation** — the cumulative net income/expense effect of using the new method since inception of the affected items, as if the new method had always been used. Positive = increases income (unfavorable to taxpayer); negative = decreases income (favorable).
9. **Adjustment period** for the §481(a) adjustment (Rev. Proc. 2015-13 §7.03):
   - Positive (income-increasing): 4 tax years (year of change and the next 3), ratably; 2 tax years if the taxpayer is under examination, unless a Form 3115 line 7b window applies
   - Negative (income-decreasing): 1 tax year (year of change)
   - Optional 1-year period for a positive adjustment under $50,000 (de minimis election) or with an eligible acquisition transaction (Form 3115 line 28)
10. **Prior method changes** — any change requested or made for the same item, or any overall method change, within the 5 tax years ending with the year of change (Rev. Proc. 2015-13 §5.01(1)(e)–(f); Form 3115 line 11a). These can bar automatic consent unless the DCN section waives the rule.
11. **Examination / Appeals / court status** of any federal return (Form 3115 lines 6a–8d).

---

## Workflow

### Step 1 — Confirm this is actually a method change

Ask: "Has the method been used on at least 2 consecutively filed returns?" An impermissible method is adopted only after use on two consecutive returns (a permissible method is adopted on the first return) (Reg. §1.446-1(e)(2)(ii)(a)). An impermissible treatment used on one return is corrected via Form 1040-X (or amended entity return), not Form 3115 (see the DCN 7 exception above).

Also confirm: the change is to an **accounting method**, not a tax election, classification, or entity-level change. Common confusions:
- §179 election: no Form 3115; revoke via amended return within 3 years
- §168(k) bonus opt-out: no Form 3115 to *make* the election; revoking an election out generally needs a letter ruling, not Form 3115. Form 3115 Schedule E note: do not file Form 3115 for certain late elections and revocations; Rev. Proc. 2025-23 §6.19 (DCN 245) lists the limited late §168 elections/revocations allowed as automatic changes
- Adopting LIFO: Form 970, not 3115
- Tax year change: Form 1128, not 3115
- Entity classification: Form 8832 / 2553, not 3115

### Step 2 — Classify automatic vs. non-automatic

The current List of Automatic Changes is **Rev. Proc. 2025-23** (32 sections, organized by Code section), as modified by **Rev. Proc. 2025-28** (section 7, research or experimental expenditures). The 2025 Schedule C instructions (Line F) point to the same list "and any subsequent revenue procedures modifying" it. Check irs.gov for a later list before relying on a DCN.

Common automatic-consent DCNs (verified in Rev. Proc. 2025-23 / 2025-28):

| DCN | Change | Section of the list |
|-----|--------|---------------------|
| 7 | Impermissible to permissible method of depreciation or amortization | 6.01 |
| 8 | Permissible to permissible method of depreciation (no §481(a) adjustment) | 6.02 |
| 122 | Cash method (or accrual-for-inventory/cash hybrid) to an overall accrual method, all other cases | 15.01 |
| 257 | Cash to accrual made in the mandatory §448 year | 15.01 |
| 233 | Small business taxpayer changing **to** the overall cash method | 15.17 |
| 259 | Small business taxpayer changing to accrual for inventory, cash for everything else | 15.17 |
| 234 | Small business taxpayer exception from §263A capitalization | 12.16 |
| 236 | Small business taxpayer exceptions for certain long-term contracts (§460) | 19.01 |
| 137 | Permissible methods of identification and valuation of inventories | 22.10 |
| 260 / 261 | Small business taxpayer §471(c) inventory methods | 22.18 |
| 56 | Change from the LIFO inventory method | 23.01 |
| 223 | Start-up expenditures (§195) | 10.01 |
| 265 / 273 / 274 | §174 (TCJA) and §174A (OBBBA) research or experimental expenditures | 7.01 / 7.02 / 7.03 (as modified by Rev. Proc. 2025-28) |

**Look up the DCN in the current list** before claiming automatic consent. DCNs are not stable across lists (for example, DCN 21 is now removal costs, §11.03; DCN 31 is multi-year insurance policies, §15.02).

If no DCN matches the change → **non-automatic** filing required:
- Filed during the tax year of change (on or before its last day), unless published guidance provides otherwise (Rev. Proc. 2015-13 §6.03(2); i3115, "Non-automatic change requests"). Late filing is relieved only in unusual and compelling circumstances (Reg. §301.9100-3; i3115, "Late Application")
- User fee $13,225; $3,450 if gross income is under $400,000; $9,775 if under $10 million (Rev. Proc. 2026-1, Appendix A (A)(3)(b)(i), (A)(4)). Pay through pay.gov first and include the receipt (Rev. Proc. 2026-1 §9.05)
- IRS National Office reviews case-by-case; consent is not deemed
- The IRS can deny or impose terms and conditions

### Step 3 — Compute the §481(a) adjustment

The §481(a) adjustment is the cumulative income/expense effect of switching to the new method, as if the new method had always been used since inception of the affected item.

**Positive adjustment (increase in income)**:
- Indicates the old method under-reported income or over-reported expenses
- Taken into account ratably over 4 tax years (year of change and the next 3) (Rev. Proc. 2015-13 §7.03(1)); 2 tax years if under examination unless a line 7b window applies (i3115, Line 25)
- If under $50,000, the taxpayer may elect to take it all into account in the year of change (de minimis election, Rev. Proc. 2015-13 §7.03(3)(c); Form 3115 line 28)

**Negative adjustment (decrease in income)**:
- Old method over-reported income or under-reported expenses
- Taken into account in the year of change (1 tax year)
- Some DCN sections set different rules; read the section for the DCN

### Cash-to-accrual example

Cash-basis user has $80,000 of accounts receivable and $30,000 of accounts payable at the end of year prior to change. New method (accrual) would have already recognized:

- AR as income: +$80,000
- AP as expense: −$30,000
- Net §481(a) adjustment: +$50,000 (positive — taxpayer recognizes additional income over the adjustment period)

Adjustment period: $50,000 / 4 years = $12,500 per year for 4 years (year of change + 3 succeeding). At exactly $50,000 the de minimis election is not available (it requires less than $50,000).

### Depreciation correction example

User mistakenly used 39-year SL nonresidential recovery on a residential rental placed in service in 2022 ($300,000 building basis, $7,692 instead of $10,909 annual depreciation). 3 years of error on filed returns (2022, 2023, 2024). Now changing to the correct 27.5-year SL in 2025.

- Correct depreciation 2022-2024: 3 × $10,909 = $32,727 (with first-year mid-month proration ignored for the example; a real computation uses the mid-month convention)
- Actual depreciation taken 2022-2024: 3 × $7,692 = $23,076
- Under-claimed depreciation: $32,727 − $23,076 = $9,651, so the §481(a) adjustment is **−$9,651 (decrease in income)** — the taxpayer gets a deduction equal to the under-claimed depreciation.

Because negative, it is taken into account in the year of change (2025): −$9,651 reduces income.

### Step 4 — Identify the correct DCN

Cross-reference with Rev. Proc. 2025-23 (or the current list). The DCN goes on **Form 3115 Part I, line 1a** if automatic; an automatic change without a DCN goes on line 1b ("Other", with the citation).

For depreciation method or recovery period corrections, the most common DCN is **DCN 7** (section 6.01 of Rev. Proc. 2025-23): change from an impermissible to a permissible method of determining depreciation for property placed in service before the year of change. Conditions to confirm:
- The impermissible method was used in at least the two tax years immediately preceding the year of change (or the property is 1-year depreciable property under §6.01(1)(b))
- The property is not on the section 6.01(1)(c) exclusion list (read it)
- Not under examination for the issue without the required consent/window (Form 3115 lines 6–7)
- The final-year eligibility rule (Rev. Proc. 2015-13 §5.01(1)(d)) does not apply to DCN 7

For overall cash-to-accrual changes:
- **DCN 257**: change made in the mandatory §448 year (a C corporation, partnership with a C corporation partner, or tax shelter that failed the §448(c) test)
- **DCN 122**: all other cash-to-accrual changes (including voluntary ones)
- **DCN 233**: the reverse direction, a small business taxpayer changing **to** cash

### Step 5 — Fill Form 3115

Form 3115 (Rev. December 2022) has an identification section, four parts, and Schedules A–E:

- **Identification section** (page 1): filer, ID number, principal business activity code, address, tax year of change, contact, applicant(s), type of applicant, type of method change
- **Part I** (lines 1–3): automatic change request — DCN(s), eligibility rules, all information provided
- **Part II** (lines 4–19): information for all requests — cessation, exam/Appeals/court status, audit protection, prior changes within 5 years, pending requests, overall method change, descriptions, legal basis, book conformity, gross receipts for the 3 preceding years
- **Part III** (lines 20–24b): non-automatic requests only — why not automatic, documents, reasons, consolidated group, user fee
- **Part IV** (lines 25–29): §481(a) adjustment — cut-off basis, amount, remaining prior adjustment, de minimis / eligible acquisition transaction election, related-party transactions
- Signature at the bottom of page 1

Schedules attached as applicable:
- **Schedule A**: Change in overall method of accounting (cash/accrual/hybrid; lines 2a–2h build the §481(a) amount)
- **Schedule B**: Advance payments deferral method, cost offset methods, AFS income inclusion rule
- **Schedule C**: Changes within the LIFO inventory method
- **Schedule D**: Long-term contracts (§460), inventories (including a change from LIFO), and §263A cost allocation
- **Schedule E**: Change in depreciation or amortization (most common for small filers)

For depreciation correction (DCN 7), **Schedule E** is completed for each item or class of property: property description and placed-in-service year (line 4a), present treatment (line 5), and for present and proposed methods the Code section, asset class, method, recovery period, convention, and bonus depreciation status (lines 7a–7h). The §481(a) computation goes on a statement attached to Part IV line 26. See [`references/line-by-line.md`](./references/line-by-line.md).

### Step 6 — Compute and document the §481(a) adjustment

Show the work explicitly. Form 3115 line 26 asks for a summary of the computation and an explanation of the methodology, per component if more than one:
- For each affected item: cumulative income/deduction under old method vs. new method
- Net adjustment per item
- Sum of adjustments
- Adjustment period (Step 3)

Attach the schedule to Form 3115 as a separate statement labeled "§481(a) Adjustment Schedule".

### Step 7 — File logistics

#### Automatic-consent filing

1. Attach the original Form 3115 to the **timely filed (including extensions) return for the year of change**. The original does not need to be signed (i3115, "When and Where To File")
2. File a **signed copy** (a photocopy is acceptable) with the IRS in Ogden **no earlier than the first day of the year of change and no later than the date the original is filed with the return** (Rev. Proc. 2015-13 §6.03(1)(a)(i)(B)):
   - Mail: Internal Revenue Service, Ogden, UT 84201, M/S 6111
   - Private delivery service: Internal Revenue Service, 1973 N. Rulon White Blvd., Ogden, UT 84201, Attn: M/S 6111
   - Or fax: 844-249-8134, with a cover sheet (Rev. Proc. 2026-1 §9.06; i3115 Address Chart)
3. No user fee for automatic consent (Rev. Proc. 2026-1, Appendix A note)
4. The IRS does not acknowledge receipt of automatic change requests (i3115)
5. Missed the return deadline: an automatic 6-month extension from the unextended due date may be available (Rev. Proc. 2015-13 §6.03(4)(a); Reg. §301.9100-2)

#### Non-automatic (advance consent) filing

1. File Form 3115 with the IRS National Office **during the year of change** (Rev. Proc. 2015-13 §6.03(2))
2. **User fee**: $13,225, or $3,450 / $9,775 reduced (Rev. Proc. 2026-1, Appendix A); pay through pay.gov first and include the receipt
3. Address (Rev. Proc. 2026-1 §9.05): Internal Revenue Service, Attn: CC:PA:LPD:TSS, P.O. Box 7604, Benjamin Franklin Station, Washington, DC 20044 (private delivery: Room 5336, 1111 Constitution Ave., NW, Washington, DC 20224); or secure fax 877-773-4950; or encrypted email to Userfee@irscounsel.treas.gov with the required MOUs
4. Consent comes in a letter ruling / consent agreement; IRS review can take many months
5. Additional copies go to the examining agent, Appeals, or government counsel if the taxpayer is under exam, before Appeals, or in court (Rev. Proc. 2015-13 §6.03(3))

### Step 8 — Validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next steps:
- Track the §481(a) adjustment **across the adjustment period** (4 years if positive, 2 if under exam). Each year, include the ratable portion (Schedule C line 6; Form 1120-S line 5; Form 1120 line 10, with a statement). If the trade or business ceases (including incorporation or transfer of substantially all assets), take the remaining balance into account in that year (Rev. Proc. 2015-13 §§3.04, 7.03(4)).
- Update the user's books to reflect the new method going forward.
- Retain the filed Form 3115 + duplicate confirmation + §481(a) schedule at least until the period of limitations closes for the last year of the adjustment period (the 3-year limitations period runs separately for each return).
- For depreciation method changes (DCN 7): update the depreciation schedule going forward; file Form 4562 each year reflecting the corrected method.
- Be aware: **5-year prior-change limitation** — a change for the same item (or an overall method change) within the 5 tax years ending with a later year of change generally bars automatic consent for that later change (Rev. Proc. 2015-13 §5.01(1)(e)–(f)), unless the DCN section waives it. Plan accordingly.

### Step 11 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes, follow [`filing.md`](./filing.md). Form 3115 has its own filing rules (signed copy to Ogden + original with return) that differ from typical e-filed schedules.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below (Form 3115, Rev. December 2022).

### Identification section

- Filer name, ID number, principal business activity code, address, tax year of change begins/ends, contact, applicant(s) if different, type of applicant (Individual, Corporation, S corporation, Partnership, etc.), type of change (Depreciation or Amortization / Financial products / Other)

### Part I — Automatic change request

- **Line 1a**: DCN(s) from the current List of Automatic Changes; **line 1b**: "Other" with description and citation if the automatic change has no DCN
- **Line 2**: do any eligibility rules restrict automatic filing? (Rev. Proc. 2015-13 §5.01(1)); "Yes" → explanation
- **Line 3**: all required information and statements provided (including those the DCN section requires)

### Part II — Information for all requests

- **Lines 4–5**: cessation/termination in the year of change; §381 principal method
- **Lines 6a–6d, 8a–8d, 9, 10**: examination, Appeals, federal court status; copies to the examining agent/Appeals
- **Lines 7a–7b**: audit protection and the applicable category (not under exam, 3-month window, 120-day window, method not before director, negative adjustment, CAP, other)
- **Lines 11a–11c**: method changes requested or made within the 5 tax years ending with the year of change — the most common pitfall for automatic eligibility
- **Line 12**: pending letter ruling / method change / technical advice requests
- **Line 13**: overall method change → Schedule A
- **Lines 14a–14d, 15a–15b, 16a–16c**: descriptions of the item, present and proposed methods, the trade or business, and (non-automatic, or where the DCN requires) the legal basis
- **Line 17**: book conformity; **line 18**: conference request; **lines 19a–19b**: gross receipts for the 3 (or 4) preceding years

### Part III — Non-automatic requests only

- **Lines 20–24b**: why not automatic, documents, reasons, consolidated group, user fee amount and reduced-fee certification. Skipped for automatic filings.

### Part IV — §481(a) adjustment

- **Line 25**: cut-off basis? (if "Yes", skip 26–29)
- **Line 26**: the §481(a) amount, + or −, with the computation summary
- **Line 27**: remaining prior §481(a) adjustment required in the year of change
- **Line 28**: $50,000 de minimis or eligible acquisition transaction election (1-year period for a positive adjustment)
- **Line 29**: related-party component
- The form has no "spread" line; the period follows Rev. Proc. 2015-13 §7.03 (Step 3)

### Schedule E — Depreciation/Amortization (most common)

For each item or class of property:
- Lines 1–3: CLADR, capitalization, elections made (§179, §168(f)(1), §168(i)(4), etc.)
- Line 4a: description, type, placed-in-service year, use, credits/basis adjustments; 4b–4c residential rental / public utility
- Lines 5–6: present treatment; support for depreciating if not currently depreciated
- Line 7a–7h: Code section, asset class (Rev. Proc. 87-56), method, recovery period, convention, bonus depreciation claimed or why not, account type — for both present and proposed methods

---

## Validation

Before declaring the form ready, run these checks.

### Math checks

- [ ] §481(a) per item = income under the new method minus income under the old method, cumulative to the start of the year of change (for deduction items: deductions under the old method minus deductions under the new method)
- [ ] Sum of per-item §481(a) adjustments = Part IV line 26 (and Schedule A line 2h for an overall method change)
- [ ] If positive: ratable 4-year amounts (line 26 / 4), or 2-year if under exam without a window, unless line 28 election made
- [ ] If negative: full line 26 in the year of change
- [ ] Line 28 de minimis election only if the positive adjustment is less than $50,000

### Sanity checks

Surface a warning if:
- [ ] DCN claimed but the change description doesn't match the DCN's section in the current list
- [ ] Method used on fewer than 2 consecutive filed returns → likely an amended-return correction, not a method change (DCN 7 1-year property exception)
- [ ] Line 11a "Yes" (change for the same item, or an overall method change, within the 5 tax years ending with the year of change) → check Rev. Proc. 2015-13 §5.01(1)(e)–(f) and any waiver in the DCN section
- [ ] Filing non-automatic but no user fee budgeted ($13,225, or $3,450 / $9,775 reduced; Rev. Proc. 2026-1 App. A)
- [ ] Filing automatic but no signed copy planned for Ogden (mail or fax) by the date the return is filed
- [ ] §481(a) adjustment large relative to the taxpayer's income → high-magnitude change; consider professional review
- [ ] Line 6a or 8a "Yes" (under exam, Appeals, or court) → copies to the agent/Appeals, 2-year period for positive adjustments unless a line 7b window applies, audit protection limits (Rev. Proc. 2015-13 §8)
- [ ] Change to LIFO requested on Form 3115 → wrong form; use Form 970
- [ ] Entity is a sole proprietor or S corporation and the change is described as "required by §448" → §448 does not apply to them (unless a tax shelter); re-check the reason

### Cross-form checks

- [ ] If depreciation change (Schedule E): Form 4562 for the year of change reflects the new method
- [ ] If overall method change (Schedule A, cash↔accrual): Schedule C or entity return reflects the new method going forward
- [ ] If inventory change (Schedule D, Part II): Schedule C Part III COGS (or Form 1125-A) reflects the new method
- [ ] §481(a) ratable portion reported on the right line (Schedule C line 6 or Part V; Form 1120-S line 5 or 20; Form 1120 line 10)

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to a paper Form 3115, with attached schedules. Format:

```markdown
# Form 3115 (Rev. December 2022) — DRAFT, year of change YYYY

## Identification
Name of filer: <name>
Identification number: <SSN or EIN>
Principal business activity code: <code>
Tax year of change begins: MM/DD/YYYY   ends: MM/DD/YYYY
Contact / phone: <name, number>
Type of applicant: <Individual | Corporation | S corporation | Partnership | ...>
Type of change: <Depreciation or Amortization | Other: description>

## Part I — Automatic change request
1a. DCN(s): <number(s)>   (Rev. Proc. 2025-23 §<section>)
1b. Other: <description and citation, if no DCN>
2.  Eligibility rules restrict? Yes/No (explanation if Yes)
3.  All required information and statements provided? Yes/No

## Part II — Information for all requests
4.  Cease trade or business / terminate existence in year of change? Yes/No
5.  §381 principal method change? Yes/No
6a-6d. Under examination? Yes/No (details)
7a-7b. Audit protection applies? Yes/No — category: <...>
8a-8d. Before Appeals / federal court? Yes/No
9-10. Consolidated group / partnership-S corp issue statements: N/A or attached
11a-11c. Change for same item or overall method change within 5 years? Yes/No (attach)
12. Pending ruling/method/technical advice requests? Yes/No
13. Overall method change? Yes/No (Schedule A)
14a-14d. Item, present method, proposed method, present overall method: <attached statement>
15a-15b. Trade or business description: <attached>
16a-16c. Legal basis / authorities / contrary authorities: <attached or "not required for DCN ...">
17. Proposed method used for books and financial statements? Yes/No
18. Conference request (non-automatic): Yes/No
19a. Gross receipts, 3 preceding years: <year: $ / year: $ / year: $>

## Part III — Non-automatic only (skipped for automatic)
24a. User fee: $<13,225 | 9,775 | 3,450>

## Part IV — §481(a) adjustment
25. Cut-off basis? Yes/No
26. §481(a) adjustment: +/−$X,XXX (computation statement attached)
27. Remaining prior §481(a) adjustment: Yes/No ($)
28. Election: [ ] $50,000 de minimis  [ ] eligible acquisition transaction  [ ] none
29. Related-party component? Yes/No

## Adjustment period (Rev. Proc. 2015-13 §7.03; not a form line)
Year of change (YYYY):  $X,XXX
Year +1 / +2 / +3:      $X,XXX each (positive, 4-year)

## Schedule E — Change in Depreciation or Amortization (if applicable)
| Item | Placed in service | Basis | Present method (sec./class/method/period/convention/bonus) | Proposed method (same) | §481(a) |
|------|-------------------|-------|-----------------------------------------------------------|------------------------|---------|
| <asset 1> | MM/YYYY | $X,XXX | <...> | <...> | $X,XXX |

(or Schedule A lines 1-5, Schedule D Part II, etc., as applicable)

## §481(a) Adjustment Schedule (attached statement)
For each affected item: amount under new method, amount under old method, difference, sign.
Sum = line 26.

## Filing details
[ ] Original Form 3115 attached to the year-of-change return (signature not required on the original)
[ ] Signed copy to IRS Ogden, M/S 6111 (mail) or fax 844-249-8134, no earlier than the first day of the year of change and no later than the date the return is filed
[ ] User fee: $0 (automatic) | $13,225 / $9,775 / $3,450 (non-automatic, Rev. Proc. 2026-1)
[ ] Deadline: automatic — timely filed return incl. extensions; non-automatic — during the year of change

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Adjustment period confirmed
- DCN verified against Rev. Proc. 2025-23 (or later list)
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 3115 (Rev. December 2022)
- IRS Instructions for Form 3115 (Rev. December 2022)
- Rev. Proc. 2025-23 (as modified by Rev. Proc. 2025-28): list of automatic changes
- Rev. Proc. 2015-13: general procedures for method changes
- Rev. Proc. 2026-1: user fees and filing addresses
- IRC §446 (general rule), §481 (adjustments), §448 (cash method limits)
```

The draft is **not** the final filed form. The user (or their CPA) still must transcribe to the IRS Form 3115 PDF, sign the copy sent to the IRS, and file two copies (one with the return, one to Ogden).

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every Form 3115 (Rev. December 2022) line and schedule
- [`references/automatic-vs-nonautomatic.md`](./references/automatic-vs-nonautomatic.md) — Decision tree for automatic vs. advance consent, common DCNs
- [`references/automatic-vs-non-automatic.md`](./references/automatic-vs-non-automatic.md) — Filing logistics companion: Ogden copy, deadlines, user fees, adjustment periods
- [`references/section-481-adjustment.md`](./references/section-481-adjustment.md) — §481(a) computation in depth, adjustment periods, examples
- [`filing.md`](./filing.md) — Filing playbook: dual-copy submission, Ogden mailing or fax, user fees, timing

## Examples

End-to-end worked Form 3115 filings.

- [`examples/cash-to-accrual-gross-receipts-threshold.md`](./examples/cash-to-accrual-gross-receipts-threshold.md) — C corporation whose 3-year average gross receipts exceed the 2026 §448(c) threshold ($32M), required to change from cash to accrual. Automatic DCN 257.
- [`examples/depreciation-error-correction.md`](./examples/depreciation-error-correction.md) — S corporation that depreciated a work truck as 7-year property instead of 5-year; corrects with a negative §481(a) adjustment. Automatic DCN 7.
- [`examples/inventory-method-change.md`](./examples/inventory-method-change.md) — S corporation retailer changing from LIFO to FIFO. Automatic DCN 56, positive §481(a) adjustment.

## Sources

- [Form 3115 (Rev. December 2022)](https://www.irs.gov/pub/irs-pdf/f3115.pdf) — the form itself
- [Instructions for Form 3115 (Rev. December 2022)](https://www.irs.gov/pub/irs-pdf/i3115.pdf)
- [About Form 3115](https://www.irs.gov/forms-pubs/about-form-3115)
- [Rev. Proc. 2025-23](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf) — current List of Automatic Changes with DCNs (effective for Forms 3115 filed on or after June 9, 2025); check for a successor
- [Rev. Proc. 2025-28](https://www.irs.gov/pub/irs-drop/rp-25-28.pdf) — OBBBA §174A research or experimental expenditure elections and changes (modifies section 7 of Rev. Proc. 2025-23; DCNs 265, 273, 274)
- [Rev. Proc. 2015-13](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf) — general procedures for method changes (§5 eligibility, §6.03 filing, §7.03 adjustment periods)
- [Rev. Proc. 2026-1](https://www.irs.gov/pub/irs-irbs/irb26-01.pdf) (IRB 2026-1) — user fees (Appendix A) and Form 3115 addresses (§§9.05–9.06)
- Rev. Proc. 2024-40 §2.31 / Rev. Proc. 2025-32 §4.30 — §448(c) gross receipts test: $31,000,000 (2025), $32,000,000 (2026)
- IRC §446 — general rule for accounting methods; Reg. §1.446-1(e)
- IRC §448 — limitation on cash method of accounting (entities)
- IRC §481 — adjustments required by changes in method of accounting
- IRC §263A — UNICAP capitalization rules; IRC §472 and Form 970 — LIFO adoption
- IRS Pub. 538 — Accounting Periods and Methods

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and procedures. It is not tax advice. Method changes interact with state-tax conformity, prior IRS determinations, NOL carryforwards, AMT, and many other facts. The agent invoking this skill should remind the user that a Form 3115 filing — especially non-automatic — warrants a licensed tax professional's review before submission.
