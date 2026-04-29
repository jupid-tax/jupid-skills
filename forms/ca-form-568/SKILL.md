---
name: ca-form-568
description: >
  Use this skill when a California LLC owner (single-member or multi-member)
  needs to file California Form 568 with the Franchise Tax Board (FTB), pay
  the $800 annual LLC tax, or compute the tiered LLC fee. Triggers on phrases
  like "California LLC tax", "CA Form 568", "$800 California LLC tax",
  "California LLC fee", "Franchise Tax Board LLC", "FTB LLC return", or any
  request to handle California LLC state-level tax obligations.
  Do NOT use for: federal partnership return (Form 1065), California S-corp
  (Form 100S — file an SOS LLC-elected-S-corp through that), or California
  nonresident-member withholding mechanics in isolation (Form 592 / 592-A /
  592-Q — those are referenced from this skill but have their own flow).
form: California Form 568 (Limited Liability Company Return of Income)
audience: [llc1, llcm]
tax_year: 2025
last_verified: 2026-04-28
official_form: https://www.ftb.ca.gov/forms/2025/2025-568.pdf
official_instructions: https://www.ftb.ca.gov/forms/2024/2024-568-booklet.pdf
---

# California Form 568 — Limited Liability Company Return of Income

This skill produces an audit-grade draft of California Form 568 and its companion vouchers (Form 3522 for the $800 annual tax, Form 3536 for the estimated LLC fee) from the user's California LLC facts. Form 568 is filed with the **California Franchise Tax Board** (FTB), not the IRS. California treats LLCs differently from federal: every LLC doing business in or registered in California owes the $800 annual tax and, if gross receipts exceed $250,000, a tiered LLC fee — regardless of profit, regardless of federal tax classification (disregarded entity, partnership, or even electing-S-corp LLCs in some cases).

The math is mechanical. The judgment is in **what counts as "doing business in California"**, **whether the LLC is taxed as a partnership / disregarded / corporation for federal purposes** (which drives which schedules to attach), and **the tier the gross receipts fall into**. This skill optimizes for the latter — ask, don't guess.

> **2025-vs-2026 note.** As of 2026-04-28, the 2025 Form 568 is the most recent published form (2026 forms typically post in late 2026). The booklet PDF is published per cycle — the 2024 booklet is the linked instructions; verify the 2025 booklet at `https://www.ftb.ca.gov/forms/` before filing for tax year 2025. **The $800 tax and tiered LLC fee thresholds shown below are the 2024-2025 figures; verify against the 2025 (and later 2026) FTB instructions before filing.**

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 568, "California LLC tax", "$800 LLC tax", "California LLC fee", or "FTB LLC return"
- The user formed an LLC in California or registered an out-of-state LLC with the California Secretary of State
- The user owns an LLC that "does business in California" (has a CA address, has CA customers under specified thresholds, has CA payroll, or has CA property — see [`references/doing-business-in-california.md`](./references/doing-business-in-california.md))
- The user asks how the $800 California LLC tax works, or how the tiered LLC fee scales

Do **not** engage this skill when:

- The user has a **California S-corporation** (entity formed as a corporation, or LLC that filed federal Form 2553 *and* California Form 3520-CT/CC equivalent to elect S-corp at state level) → that's Form 100S, not Form 568
- The user has a **California C-corporation** → Form 100
- The user has a **partnership that's not an LLC** (general partnership, LP, LLP) → Form 565, not Form 568
- The user owns an LLC that has **no California nexus** at all (no CA address, no CA members, no CA customers, no CA registration) → no California return is required
- The user's only California issue is **nonresident member withholding** in isolation → Form 592 / 592-A / 592-Q (this skill references those but doesn't drive them)

If the user's classification is ambiguous (especially "LLC taxed as S-corp"), ask before proceeding. The most common confusion: an LLC that elected S-corp federally still might file Form 568 OR Form 100S depending on whether it elected S-corp at the California level. See [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 568 for tax year 2025 is filed in 2026; for 2024, in 2025. The $800 tax and tiered fee thresholds are set by year (per Rev. & Tax. Code §17941, §17942, with annual indexing only on certain items).
2. **California Secretary of State (SOS) file number** (12-digit, starting with `2` for LLCs) — required on the form header
3. **Federal EIN** of the LLC. Required even for SMLLCs filing Form 568 (because the form needs an EIN line, even though federally the SMLLC may use the owner's SSN on Schedule C).
4. **California LLC formation or registration date** — used to determine whether the first-year exemption applies (it doesn't; AB 85 expired — see workflow Step 2).
5. **Federal tax classification** of the LLC: disregarded entity (SMLLC), partnership (multi-member), or corporation (rare; if so, redirect). This drives which Schedule K, Schedule K-1, and member tables are required.
6. **All members' names, SSN/ITIN/EIN, addresses, ownership %, and California residency status**. Nonresident members trigger withholding on distributable share (Form 592 / 592-A / 592-Q) and may require Form 3832 (nonresident consent).
7. **Total income from all sources** ("Total Income") for the LLC fee calculation. **Important:** California's "Total Income" for the LLC fee is defined per §17942 — it's gross receipts plus other income from California sources, with specific exclusions. It is **not** the same as federal gross receipts. See [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md).
8. **Profit/loss data** for partnership-classified LLCs: federal Form 1065 must be drafted/filed first, because Form 568 Schedule K mirrors federal K with California adjustments. For SMLLCs, federal Schedule C / Schedule E / Schedule F numbers carry over.
9. **California-source apportionment data** if the LLC has out-of-state activity: Schedule R is required to apportion income to California. See [`references/apportionment.md`](./references/apportionment.md).
10. **Has the $800 annual tax been paid this year via Form 3522 (FTB voucher 3522)?** Required by 15th day of 4th month of the tax year. If unpaid, late-payment penalty + interest accrue.
11. **Has the estimated LLC fee been paid via Form 3536 (FTB voucher 3536)?** Required by 15th day of 6th month if expected fee > $0. If underpaid by more than 10%, an estimated-fee penalty (10% of underpayment) applies under §19132.

For nonresident members, additionally ask:

- Is each nonresident member willing to sign **Form 3832** (consent to California jurisdiction)? If yes, the LLC does not have to withhold on that member. If no, the LLC must withhold 7% of distributable California-source income > $1,500 and remit via Form 592.
- Has the LLC already filed any **Form 592 / 592-A / 592-Q** withholding deposits this year?

---

## Workflow

Execute these steps in order. Each step is a discrete decision the agent must make.

### Step 1 — Confirm California nexus and entity classification

Confirm the LLC is registered with California SOS or is "doing business in California" under R&TC §23101. If the user is unsure, walk through the nexus tests in [`references/doing-business-in-california.md`](./references/doing-business-in-california.md). If there's no nexus, no Form 568 is required.

Then confirm federal classification (SMLLC/disregarded vs. partnership vs. corporation). If the LLC elected to be taxed as a corporation federally (Form 8832) or as an S-corp federally (Form 2553), this skill may not apply — see [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md) and consider routing to Form 100 / 100S.

### Step 2 — Pay or confirm the $800 annual tax (Form 3522)

The $800 annual LLC tax is owed by **every** California LLC (with limited exceptions noted below) for **every** taxable year, including the year of formation and the final year of dissolution. It's due **by the 15th day of the 4th month** of the LLC's tax year (April 15 for calendar-year filers).

> **First-year exemption — verify before relying on it.** AB 85 (Stats. 2020, ch. 8) exempted LLCs formed in tax years **2021, 2022, and 2023** from the first-year $800 tax. **AB 85 was not extended; LLCs formed in 2024 and later owe $800 in their first year.** This skill assumes the AB 85 exemption does not apply unless the user is filing for tax year 2021-2023. Confirm against the FTB LLC page before relying on any first-year relief: <https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html>.

If the $800 has not been paid, prepare Form 3522 (Limited Liability Company Tax Voucher) and instruct the user to remit. If overdue, calculate the late-payment penalty (5% of unpaid tax + 0.5% per month, max 25%, per §19132) and interest (federal short-term rate + 3%, compounded daily, per §19521).

### Step 3 — Determine if the LLC fee applies, and which tier

The LLC fee (R&TC §17942) is **separate from the $800 tax** and is owed by LLCs with California-source "total income" of $250,000 or more. As of the 2024-2025 instructions:

| California "total income" (Form 568, Line 1) | LLC fee |
|---|---|
| Less than $250,000 | $0 |
| $250,000 – $499,999 | $900 |
| $500,000 – $999,999 | $2,500 |
| $1,000,000 – $4,999,999 | $6,000 |
| $5,000,000 or more | $11,790 |

These are the figures published in the 2024 booklet (verify current values in the 2025 booklet before filing). Cite: R&TC §17942(a)(1)-(4).

Use [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md) for the exact "total income" definition (it's broader than federal gross receipts in some cases and narrower in others — pay attention to the §17942(b) exclusions and the apportionment for out-of-state LLCs).

### Step 4 — Pay or confirm the estimated LLC fee (Form 3536)

If the LLC expects to owe a fee (Step 3 ≠ $0), it must remit an **estimated fee** via Form 3536 by the **15th day of the 6th month** of the tax year (June 15 for calendar year). The estimate must equal at least the actual fee for the prior year (or the actual current-year fee if known); underpayment > 10% triggers a 10% penalty under §17942(d).

Common pitfall: a fast-growing LLC pays Form 3536 based on prior year ($900 last year) but ends up in a higher tier ($6,000 this year). The penalty is 10% of the underpayment. Have the user re-estimate at month 6 if growth is fast.

### Step 5 — Determine filing deadline

| LLC classification | Deadline (calendar year) |
|---|---|
| Partnership (multi-member, default) | **March 15** (15th day of 3rd month after year-end) |
| Disregarded entity (SMLLC) | **April 15** (15th day of 4th month after year-end) |
| Corporation (rare; redirect) | March 15 / April 15 depending on C/S |

If the LLC misses this deadline, it can get an **automatic 7-month extension** to file (no form needed — California grants the extension automatically), but **the $800 tax and any LLC fee are still due by the original deadline**. An extension to file is not an extension to pay.

> Note on conformity: California's filing deadline for partnership-classified LLCs is March 15, matching federal Form 1065. The disregarded-entity deadline is April 15, matching federal Form 1040.

### Step 6 — Draft Schedule K and member K-1s (if multi-member)

If the LLC is partnership-classified, federal Form 1065 should already be drafted. Form 568 Schedule K mirrors federal Schedule K with California-specific adjustments (different depreciation under §168(k) — California does not conform to bonus depreciation; different §179 limits — California's max is $25,000, not federal's $1.25M; California-specific credits).

The agent should:

1. Pull federal Schedule K line totals
2. Apply California adjustments per [`references/california-adjustments.md`](./references/california-adjustments.md)
3. Generate a Form 568 Schedule K-1 (568) for each member
4. Sum member shares = Schedule K totals (validation)

### Step 7 — Apportion income if multi-state (Schedule R)

If the LLC has activity outside California, attach **Schedule R** to apportion income using California's single-sales-factor formula (post-2013, R&TC §25128.7). Single-member LLCs that are disregarded for federal purposes but have multi-state activity still apportion at the parent level — this skill flags it but the apportionment lives upstream.

### Step 8 — Handle nonresident members (if any)

For each nonresident member:

- If they sign **Form 3832** (Limited Liability Company Nonresident Members' Consent), no withholding is required. Attach Form 3832 to Form 568.
- If they don't sign Form 3832, the LLC withholds **7% of distributable California-source income > $1,500** and remits via **Form 592** (annual reconciliation), **Form 592-A** (foreign-partner deposits, if applicable), and **Form 592-Q** (estimated quarterly deposits). Issue Form 592-B to each nonresident member.

See [`references/nonresident-members.md`](./references/nonresident-members.md). Out of scope for this skill: foreign (non-U.S.) members — they trigger §1446 withholding federally and additional California rules; redirect to a CPA.

### Step 9 — Compute the bottom line

```
Form 568 Side 1, Line 1 — Total income (per §17942 definition)
Form 568 Side 1, Line 2 — Limited liability company fee (from tier table)
Form 568 Side 1, Line 3 — 2024 annual LLC tax ($800)
Form 568 Side 1, Line 4 — Nonconsenting nonresident members' tax (Schedule T)
Form 568 Side 1, Line 5 — Partnership level tax (rare)
Form 568 Side 1, Line 6 — Total tax and fee = Line 2 + 3 + 4 + 5
Form 568 Side 1, Lines 7-12 — Payments / credits (Form 3522, Form 3536, withholding, overpayment from prior year)
Form 568 Side 1, Line 13 — Tax/fee due or overpayment
```

(Verify exact line numbering against the 2025 booklet — line numbers are stable across years but occasionally renumber when new credits or boxes are added.)

### Step 10 — Run validation

See **Validation** below. Run every check.

### Step 11 — Produce the deliverable

See **Output format** below.

### Step 12 — Hand off downstream

State the next steps:

- **If multi-member**: each member needs Form 568 Schedule K-1, plus federal Form 1065 K-1, for their personal returns
- **If SMLLC**: the owner reports the LLC's activity on their federal Schedule C (or E for rentals), and California Schedule CA(540) flows from federal AGI with adjustments
- **Nonresident withholding**: any 592-B issued to members must accompany their California nonresident return (Form 540NR)
- **Next year**: remind the user about Form 3522 due April 15 of the next tax year, and Form 3536 estimate due June 15

### Step 13 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). California offers e-file via FTB-approved software (CalFile does not support Form 568 — it's individual-only). Paper filing is allowed.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Side 1 (Top of form)

- **A** — California SOS file number (12 digits, starts with `2`)
- **B** — Federal EIN
- **C** — Principal business activity (e.g., "Real estate rental", "Software consulting")
- **D** — Principal product or service (NAICS-aligned plain-English description)
- **E** — Date business started in California
- **F** — Total assets at end of year (from federal Schedule L if filed)
- **G** — Sales (from federal Schedule K, Line 1c for partnerships)
- **H** — Check applicable boxes: initial return, final return, amended, single-member LLC, etc.
- **I** — Number of members (1 for SMLLC, 2+ for multi-member)
- **J** — Effective date of LLC's federal classification election (if any Form 8832 filed)

### Side 1 (Tax and Fee)

- **Line 1** — Total income from Schedule IW (Limited Liability Company Income Worksheet), which collects California-source gross receipts. **Not** the federal Line 1.
- **Line 2** — LLC fee from the tier table (Step 3)
- **Line 3** — $800 annual tax
- **Line 4** — Tax on nonconsenting nonresident members (Schedule T) — typically the highest CA marginal rate (12.3% individual / 8.84% corporate) on their share
- **Line 5** — Partnership-level tax (very rare; almost always $0 for solo LLCs)
- **Line 6** — Total tax and fee
- **Lines 7-12** — Payments: Form 3522 ($800 paid earlier), Form 3536 (estimated fee), withholding credits, overpayment from prior year
- **Line 13** — Tax/fee due (or overpayment)

### Schedule IW — Limited Liability Company Income Worksheet

This is **the** worksheet for computing Line 1 (Total income) for the LLC fee. It is California-specific and does not mirror federal. Lines:

- IW Line 1 — Total gross receipts (California-source)
- IW Line 2 — Cost of goods sold (California-source)
- IW Line 3-7 — Various California-source income items
- Sum → Form 568 Line 1

For a service-only single-state LLC, Schedule IW Line 1 ≈ federal gross receipts. For multi-state LLCs, Schedule R apportionment applies.

### Schedule K (568) and Schedule K-1 (568)

Mirrors federal K / K-1 with California adjustments. See [`references/california-adjustments.md`](./references/california-adjustments.md) for the line-by-line California adjustment reference (depreciation, §179, charitable contributions, state tax refunds, etc.).

### Schedule L, M-1, M-2 (Balance sheet)

Required if LLC's total receipts ≥ $250,000 OR total assets ≥ $1,000,000. For smaller LLCs, can omit.

### Schedule T — Nonconsenting Nonresident Members

For each nonresident member who didn't sign Form 3832, compute their share of California-source income × 12.3% (or 8.84% for corporate members).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Form 568 Line 6 = Line 2 + Line 3 + Line 4 + Line 5
- [ ] Form 568 Line 1 = Schedule IW total
- [ ] Schedule IW total ≥ $250,000 → Line 2 (LLC fee) > $0; otherwise Line 2 = $0
- [ ] If multi-member: sum of member K-1 (568) shares = Schedule K (568) totals for every line
- [ ] If Schedule L filed: balance sheet balances (Assets = Liabilities + Capital)
- [ ] Form 3522 ($800) paid by 4th month deadline → credit on Line 7
- [ ] Form 3536 (estimated fee) paid by 6th month deadline → credit on Line 8
- [ ] Schedule T total (nonconsenting nonresident members' tax) = Line 4

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] LLC formed in 2024+ but Form 3522 ($800) not paid → AB 85 expired; no first-year exemption
- [ ] Schedule IW Line 1 close to a tier boundary (e.g., $249,500 or $499,000) → confirm the user has counted all California-source income; one extra invoice could push the LLC into a higher fee bracket
- [ ] Form 3536 estimated fee underpaid by > 10% → 10% penalty under §17942(d) will apply
- [ ] Multi-member LLC with nonresident member but no Form 3832 attached and no Form 592 filed → withholding obligation likely missed
- [ ] §179 deduction on federal Schedule K > $25,000 → California cap applies; California adjustment must reduce
- [ ] Bonus depreciation (§168(k)) on federal → California does not conform; add-back required
- [ ] LLC has out-of-state members or activity but no Schedule R attached → apportionment likely required
- [ ] LLC marked "final return" but did not file Form LLC-3 / LLC-4/7 with SOS → the LLC remains "active" with SOS and accrues another $800 next year

### Cross-form checks

- [ ] If multi-member: federal Form 1065 must be drafted/filed; Form 568 Schedule K mirrors federal K
- [ ] If SMLLC: owner reports activity on federal Schedule C (business) or E (rental); Form 568 is in addition, not in lieu
- [ ] Form 3832 attached for every nonresident member who consented
- [ ] Form 592 / 592-B issued for every nonresident member who didn't consent
- [ ] If LLC owes federal tax to IRS via 1065 / 1040, that's separate from this Form 568

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to the FTB form or paste into California-supporting tax software (Lacerte, ProSeries, Drake, FreeTaxUSA — note: TurboTax supports Form 568 only in higher tiers; CalFile does not support it).

```markdown
# California Form 568 — DRAFT for tax year YYYY

## LLC identification
A. SOS file number: 2XXXXXXXX
B. Federal EIN: XX-XXXXXXX
C. Principal business activity: <description>
D. Principal product/service: <description>
E. Date business started in CA: MM/DD/YYYY
F. Total assets EOY: $X,XXX,XXX
G. Sales (federal Sched K Line 1c): $X,XXX,XXX
H. Boxes checked: [Initial / Final / Amended / SMLLC / etc.]
I. Number of members: N
J. Federal classification election (if any): MM/DD/YYYY

## Side 1 — Tax and Fee
Line 1.  Total income (from Sched IW):         $X,XXX,XXX
Line 2.  LLC fee (from tier table):            $X,XXX
Line 3.  2024/2025 annual LLC tax:             $800
Line 4.  Nonconsenting nonresident tax (T):    $X,XXX
Line 5.  Partnership-level tax:                $0
Line 6.  Total tax and fee (2+3+4+5):          $X,XXX

## Side 1 — Payments
Line 7.  Form 3522 ($800) prepaid:             $800
Line 8.  Form 3536 (estimated fee) prepaid:    $X,XXX
Line 9.  Withholding (Form 592 / 593):         $X,XXX
Line 10. 2024 overpayment applied:             $X,XXX
Line 11. Total payments:                       $X,XXX
Line 12. Tax/fee due or overpayment:           $X,XXX

## Schedule IW — Income Worksheet
IW Line 1. Gross receipts (CA-source):        $X,XXX,XXX
IW Line 2. Cost of goods sold (CA):           $X,XXX,XXX
... (every line, including zeros)
Total → Form 568 Line 1:                       $X,XXX,XXX

## Schedule K (if partnership-classified)
[summary of federal K with CA adjustments — full table in deliverable]

## Schedule K-1 (568) per member
| Member | SSN/ITIN/EIN | Ownership % | Distributable share | Resident/Nonresident | Form 3832 signed? |
|--------|--------------|-------------|---------------------|----------------------|-------------------|
| ...    | ...          | ...         | ...                 | ...                  | Yes / No          |

## Schedule L (if required)
[balance sheet, if total receipts ≥ $250K or total assets ≥ $1M]

## Schedule T (if nonconsenting nonresident members)
| Member | CA-source share | Rate (12.3% / 8.84%) | Tax |
|--------|-----------------|----------------------|-----|
| ...    | ...             | ...                  | ... |

## Required attachments
- [ ] Form 3522 (the actual $800 payment voucher; pay by April 15)
- [ ] Form 3536 (estimated LLC fee voucher; pay by June 15)
- [ ] Form 3832 (for each consenting nonresident member)
- [ ] Form 592 / 592-B (for each non-consenting nonresident member)
- [ ] Schedule R (if multi-state apportionment)
- [ ] Federal Form 1065 (must be filed if multi-member)
- [ ] Federal Schedule C / E / F (if SMLLC, on owner's 1040)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 12>

## Sources cited in this draft
- California Form 568, Rev. 2024 (or 2025 if filed)
- California Form 568 Booklet (2024 — verify against 2025 before filing)
- R&TC §17941 (annual LLC tax)
- R&TC §17942 (LLC fee)
- R&TC §19132 (penalty)
- R&TC §23101 (doing business in California)
- R&TC §25128.7 (single-sales-factor apportionment)
- AB 85 (Stats. 2020, ch. 8) — first-year tax exemption (expired 2024+)
```

The draft is **not** the final filed form. The user still has to enter it into FTB-supporting tax software, paper-mail it, or e-file via an FTB-approved provider. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete reference for every line on Form 568, Schedule IW, Schedule K, and Schedule T
- [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md) — How "Total Income" is computed for §17942, tier-boundary edge cases, and apportionment for multi-state LLCs
- [`references/doing-business-in-california.md`](./references/doing-business-in-california.md) — R&TC §23101 nexus tests; $711K sales / $71K property / $71K payroll thresholds (2024 — verify current)
- [`references/california-adjustments.md`](./references/california-adjustments.md) — Depreciation conformity (no §168(k) bonus), §179 limit ($25K), state tax refunds, and other federal-to-California adjustments
- [`references/nonresident-members.md`](./references/nonresident-members.md) — Form 3832 consent, Form 592 withholding mechanics, and Schedule T computation
- [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md) — When an LLC files Form 568 vs. Form 100S (federal S-corp election does not always carry to California)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with citations
- [`filing.md`](./filing.md) — Browser-automation playbook for FTB e-file or paper filing

## Examples

End-to-end worked Form 568 returns. Use these as patterns when the user's situation is similar.

- [`examples/smllc-zero-revenue.md`](./examples/smllc-zero-revenue.md) — First-year SMLLC with $0 revenue still owes $800 + must file Form 568 (the most common newbie surprise)
- [`examples/multi-member-mid-tier.md`](./examples/multi-member-mid-tier.md) — Two-member LLC with $400K California-source gross receipts: $800 + $900 LLC fee
- [`examples/smllc-high-tier.md`](./examples/smllc-high-tier.md) — Single-member LLC with $1.5M California-source gross receipts: $800 + $6,000 fee, with bonus-depreciation add-back

## Sources

Authoritative sources used by this skill. Re-verify each year against the FTB site for the tax year being filed.

- [California Form 568 (2025 PDF)](https://www.ftb.ca.gov/forms/2025/2025-568.pdf) — the form itself
- [California Form 568 Booklet (2024 PDF)](https://www.ftb.ca.gov/forms/2024/2024-568-booklet.pdf) — instructions; verify 2025 booklet at <https://www.ftb.ca.gov/forms/> before filing
- [California Form 3522 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3522.pdf) — $800 annual LLC tax voucher
- [California Form 3536 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3536.pdf) — estimated LLC fee voucher
- [California Form 3537 (2024)](https://www.ftb.ca.gov/forms/2024/2024-3537.pdf) — automatic extension payment voucher
- [California Form 3832 (2024)](https://www.ftb.ca.gov/forms/2024/2024-3832.pdf) — nonresident member consent
- [California Form 592-A (2024)](https://www.ftb.ca.gov/forms/2024/2024-592-a.pdf) — nonresident withholding voucher
- [California Form 592-Q (2024)](https://www.ftb.ca.gov/forms/2024/2024-592-q.pdf) — quarterly nonresident withholding
- [FTB Limited Liability Company page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) — landing page with current rules and exemptions
- [FTB Pub 3556 (LLC MEO)](https://www.ftb.ca.gov/forms/misc/3556.html) — Limited Liability Company Filing Information
- California Revenue and Taxation Code:
  - §17941 — Annual LLC tax ($800)
  - §17942 — LLC fee (tiered by total income)
  - §19132 — Failure to pay penalty
  - §19521 — Interest on underpayments
  - §23101 — Doing business in California
  - §25128.7 — Single-sales-factor apportionment
- AB 85 (Stats. 2020, ch. 8) — first-year $800 tax exemption for LLCs formed 2021-2023; expired for 2024+

## Disclaimer

This skill encodes procedural guidance based on publicly available California Franchise Tax Board forms and instructions and the California Revenue and Taxation Code. It is not tax advice and does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations — especially those involving multi-state apportionment, nonresident or foreign members, or California-S-corp elections — warrant a licensed California tax professional's review.
