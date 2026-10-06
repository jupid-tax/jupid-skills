---
name: ca-form-568
description: >
  Use this skill when a California LLC owner (single-member or multi-member)
  needs to file California Form 568 with the Franchise Tax Board (FTB), pay
  the $800 annual LLC tax, or compute the tiered LLC fee. Triggers on phrases
  like "California LLC tax", "CA Form 568", "$800 California LLC tax",
  "California LLC fee", "Franchise Tax Board LLC", "FTB LLC return", or any
  request to handle California LLC state-level tax obligations.
  Do NOT use for: the federal partnership return (Form 1065 — use form-1065),
  an LLC that elected corporate or S-corporation treatment federally (it files
  California Form 100 or 100S, not Form 568), or California pass-through
  withholding mechanics in isolation (Form 592-Q / 592-PTE / 592-A / 592-F —
  those are referenced from this skill but have their own flow).
form: California Form 568 (Limited Liability Company Return of Income)
audience: [llc1, llcm]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.ftb.ca.gov/forms/2025/2025-568.pdf
official_instructions: https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf
---

# California Form 568 — Limited Liability Company Return of Income

This skill produces an audit-grade draft of California Form 568 and its companion vouchers (FTB 3522 for the $800 annual tax, FTB 3536 for the LLC fee, FTB 3537 for an extension payment of nonconsenting nonresident members' tax) from the user's California LLC facts. Form 568 is filed with the **California Franchise Tax Board** (FTB), not the IRS. Every LLC classified as a partnership or disregarded entity that is organized in, registered in, or doing business in California owes the $800 annual tax and, once total California income reaches $250,000, a tiered LLC fee, regardless of profit. LLCs taxed as corporations file Form 100 or 100S instead and owe no LLC fee.

The math is mechanical. The judgment is in **what counts as "doing business in California"**, **whether the LLC is taxed as a partnership, disregarded entity, or corporation for federal purposes** (which drives which return and schedules apply), and **how much income is assigned to California on Schedule IW** (which sets the fee tier). This skill optimizes for the judgment calls: ask, don't guess.

The line map was verified against the **2025 Form 568 (taxable year 2025, filed in 2026)** and the **2025 Form 568 Booklet**. The 2026 Form 568 had not been released as of 2026-10-06; re-check the next revision at <https://www.ftb.ca.gov/forms/> (search "568") before using this skill for taxable year 2026. In general, California does not conform to the One Big Beautiful Bill Act (2025 booklet, What's New) and conforms to the IRC as of January 1, 2025 (SB 711), so federal 2025 changes do not flow through automatically.

**Companion guide for end users:** [Form 568 Instructions 2026: CA 568 Due Date, Extended Due Date, and Line-by-Line Guide + AI Agent Skill](https://jupid.com/blog/form-568-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 568, "California LLC tax", "$800 LLC tax", "California LLC fee", or "FTB LLC return"
- The user formed an LLC in California or registered an out-of-state LLC with the California Secretary of State
- The user owns an LLC that "does business in California" (organized or commercially domiciled in California, a member or manager acting in California for the LLC, or California sales, property, or payroll above the indexed thresholds — see [`references/doing-business-in-california.md`](./references/doing-business-in-california.md))
- The user asks how the $800 California LLC tax works, or how the tiered LLC fee scales

Do **not** engage this skill when:

- The LLC filed federal Form 2553 (S election) → California treats it as an S corporation automatically (R&TC §23801(a)) → **Form 100S**, not Form 568
- The LLC filed federal Form 8832 to be taxed as a corporation → **Form 100** (see [`../form-8832/SKILL.md`](../form-8832/SKILL.md))
- The user has a **partnership that's not an LLC** (general partnership, LP, LLP) → Form 565, not Form 568
- The user needs the **federal** partnership return → [`../form-1065/SKILL.md`](../form-1065/SKILL.md); this skill uses its numbers but does not draft it
- The LLC is a nonregistered foreign (non-California) LLC that is not doing business in California but has California-source income → Form 565 (2025 booklet, General Information D); a nonregistered foreign single-member LLC that is not doing business in California files neither
- The user's only California issue is **nonresident member withholding** in isolation → Form 592-Q / 592-PTE / 592-A / 592-F (this skill references those but doesn't drive them)

If the user's classification is ambiguous (especially "LLC taxed as S-corp"), ask before proceeding. California follows the federal check-the-box classification and allows no separate state election (2025 booklet, General Information S), so the deciding question is which federal election, if any, the LLC made. See [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Taxable year** the return covers. Form 568 for taxable year 2025 is filed in 2026. The $800 tax (R&TC §17941) and the fee tiers (R&TC §17942(a)) are fixed dollar amounts in the statute, not inflation-indexed; the doing-business thresholds are indexed every year (R&TC §23101(c)).
2. **California SOS file number**, exactly as shown in Secretary of State records — required in Item A.
3. **Federal EIN** of the LLC — required in Item B, including for single-member LLCs (2025 booklet, "Before mailing, make sure entries have been made for... FEIN").
4. **Date the LLC filed with the SOS** (or, for a foreign LLC, the date it was organized in its home state). This sets the first taxable year and the first $800 due date, and decides whether a first-year rule applies (AB 85 for first taxable years 2021–2023; the $400 first-year tax for first taxable years beginning 2027–2029 under SB 122).
5. **Federal tax classification** of the LLC: disregarded entity (single-member default), partnership (multi-member default), or corporation (Form 8832 or 2553 filed; redirect). This drives which schedules are required.
6. **For a single-member LLC: the owner's entity type** (individual, C corporation, pass-through entity, estate or trust, exempt organization). It sets the due date and extension length and fills the Single Member LLC Information and Consent on Side 3.
7. **All members' names, SSN/ITIN/FEIN, addresses, ownership %, and California residency status**. Nonresident members raise two separate issues: the FTB 3832 consent (or Schedule T tax if they don't sign) and 7% withholding on distributions.
8. **California-source income by category** for Schedule IW: gross receipts and cost of goods sold, rents, interest, dividends, royalties, gains. "Total income" for the fee is gross income plus cost of goods sold, assigned to California using the sales-assignment rules of R&TC §§25135–25136 (R&TC §17942(b)(1)). It is **not** profit. See [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md).
9. **Profit/loss data**: for partnership-classified LLCs, the drafted federal Form 1065 (Form 568 Schedule K mirrors federal Schedule K with California adjustments). For single-member LLCs, the owner's federal Schedule C / E / F numbers.
10. **Multi-state facts** if the LLC has activity or customers outside California: where customers receive the benefit of services, where goods are shipped, where property and payroll sit. Schedule IW assigns income item by item; Schedule R apportions business income (2025 booklet, Schedule IW instructions; FTB LLC page).
11. **Has the $800 annual tax been paid via FTB 3522 (or Web Pay)?** Due by the 15th day of the 4th month of the taxable year (April 15, 2025 for calendar 2025). If unpaid, a late-payment penalty and interest accrue (R&TC §19132).
12. **Has the estimated LLC fee been paid via FTB 3536 (or Web Pay), how much, and on what date? What was the total LLC fee for the preceding taxable year?** The estimate is due by the 15th day of the 6th month. If the estimate is less than the fee for the year, the penalty is 10% of the shortfall, unless the amount paid by the due date is at least the preceding year's total fee (R&TC §17942(d)(2)).

For nonresident members, additionally ask:

- Has each nonresident member signed **FTB 3832** (consent to California's jurisdiction to tax their distributive share)? A member who doesn't sign triggers the Schedule T tax paid by the LLC.
- Did the LLC make distributions of California-source income to any domestic nonresident member, and did it withhold 7% and remit on **Form 592-Q**? Any foreign (non-U.S.) members (Form 592-A payments, Form 592-F)?

---

## Workflow

Execute these steps in order. Each step is a discrete decision the agent must make.

### Step 1 — Confirm California nexus and entity classification

Confirm the LLC is organized in California, registered with the California SOS, doing business in California under R&TC §23101, or has California-source income (2025 booklet, General Information D). If the user is unsure, walk through the tests in [`references/doing-business-in-california.md`](./references/doing-business-in-california.md). If none applies, no Form 568 is required.

Then confirm federal classification (disregarded vs. partnership vs. corporation). If the LLC elected to be taxed as a corporation (Form 8832) or as an S corporation (Form 2553), stop: the return is Form 100 or 100S. See [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md).

### Step 2 — Pay or confirm the $800 annual tax (FTB 3522)

The $800 annual LLC tax is owed by every LLC doing business in California or with articles of organization accepted or a certificate of registration issued by the SOS, for every taxable year until the cancellation papers are filed (2025 booklet, General Information F). It is due **by the 15th day of the 4th month after the beginning of the taxable year** (April 15 for calendar-year LLCs). The first taxable year begins when the LLC files with the SOS (FTB 3522 instructions); the FTB's example: an LLC formed June 18 owes its first $800 by September 15 of that year (FTB LLC page).

> **First-year rules.** AB 85 (Stats. 2020, ch. 8) exempted LLCs from the $800 for their first taxable year only for taxable years beginning on or after January 1, 2021, and before January 1, 2024 (FTB LLC page). LLCs whose first taxable year begins in 2024, 2025, or 2026 owe the full $800 in year one. For taxable years beginning on or after January 1, 2027, and before January 1, 2030, the first-year annual tax drops to **$400** (SB 122, 2026 budget trailer bill; FTB "What's new with tax forms"). Confirm the rule for the user's first taxable year before relying on it.

Other exceptions: a first taxable year of 15 days or less with no business in that window (no return, no tax); a short-form cancellation (SOS Form LLC-4/8) filed within 12 months of organizing by an LLC that never did business; the deployed-military exemption for taxable years 2020–2029 (enter $0 on lines 2 and 3); certain tax-exempt title-holding LLCs (2025 booklet, General Information D, F, Q).

If the $800 has not been paid, prepare FTB 3522 (or tell the user to pay with Web Pay) using the voucher for the taxable year being paid; do not send the $800 with Form 568. If late, compute the late-payment penalty (5% of the unpaid tax plus 0.5% for each month or part of a month, up to 40 months, maximum 25%, R&TC §19132) and interest at the FTB's posted rate (7% for July 1, 2025 – December 31, 2026; R&TC §19521; FTB "Interest and estimate penalty rates").

### Step 3 — Determine if the LLC fee applies, and which tier

The LLC fee (R&TC §17942) is **separate from the $800 tax** and applies once total California income (Form 568, Side 1, line 1, from Schedule IW line 17) reaches $250,000. 2025 booklet, General Information F:

| Total California income (Form 568, Side 1, line 1) | LLC fee |
|---|---|
| Less than $250,000 | $0 |
| $250,000 – $499,999 | $900 |
| $500,000 – $999,999 | $2,500 |
| $1,000,000 – $4,999,999 | $6,000 |
| $5,000,000 or more | $11,790 |

Cite: R&TC §17942(a)(1)–(4).

Use [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md) for the "total income" definition (gross income plus cost of goods sold, assigned to California item by item; income already subject to the fee at another LLC is excluded).

### Step 4 — Pay or confirm the estimated LLC fee (FTB 3536)

If the LLC expects to owe a fee, it must pay an **estimated fee** with FTB 3536 (or Web Pay) by the **15th day of the 6th month** of the taxable year (June 16, 2025 for calendar 2025 because June 15 fell on a Sunday; June 15, 2026 for calendar 2026). Any fee not paid as a timely estimate is still due by the **original due date of the return**, also on FTB 3536 (2025 FTB 3536 instructions).

Penalty (R&TC §17942(d)(2)): 10% of (fee for the year − amount paid by the 6th-month date). No penalty if the amount paid by that date is equal to or greater than the LLC's total fee for the **preceding** taxable year. Example: an LLC whose prior-year fee was $900 pays $900 in June and ends the year in the $2,500 tier → no penalty; the $1,600 balance is due by the return's original due date. If the LLC had no preceding taxable year, there is no prior-year amount to compare: tell the user to estimate the current-year fee.

### Step 5 — Determine filing deadline

2025 booklet, General Information E; R&TC §18633.5 (due dates), §18567 (extensions):

| LLC classification | Original due date (calendar year) | Automatic extension |
|---|---|---|
| Partnership (multi-member) | 15th day of 3rd month after year-end (March 16, 2026 for 2025: March 15 fell on a Sunday) | 7 months → October 15, 2026 |
| Single-member LLC owned by a partnership or an LLC taxed as a partnership | 15th day of 3rd month (March 16, 2026) | 7 months → October 15, 2026 |
| Single-member LLC owned by an S corporation | 15th day of 3rd month (March 16, 2026) | 6 months → September 15, 2026 |
| Any other single-member LLC (individual, C corporation, estate or trust owner) | 15th day of 4th month after the close of the owner's taxable year (April 15, 2026) | 6 months → October 15, 2026 |

The extension is automatic for an LLC in good standing (no form; a suspended or forfeited LLC gets none), but it extends filing only. The remaining LLC fee (FTB 3536) and any nonconsenting nonresident members' tax (FTB 3537) are due by the **original** due date; the $800 was due in the 4th month of the taxable year. If the return is not filed by the extended date, the late-filing penalty runs from the original due date (2025 booklet, General Information G).

### Step 6 — Draft Schedule K and member K-1s (if multi-member)

If the LLC is partnership-classified, federal Form 1065 should already be drafted. Form 568 Schedule K has columns (b) amounts from federal K (1065), (c) California adjustments, (d) totals under California law. Common adjustments: California does not conform to §168(k) bonus depreciation, and its §179 limit is $25,000 with a $200,000 investment threshold (2025 FTB 3885L, lines 1 and 3), against the federal 2025 limit of $2,500,000 and threshold of $4,000,000 (2025 Instructions for Form 4562).

The agent should:

1. Pull federal Schedule K line totals
2. Apply California adjustments per [`references/california-adjustments.md`](./references/california-adjustments.md) (depreciation from FTB 3885L)
3. Generate a Schedule K-1 (568) for each member; the number of K-1s must equal Question K
4. Sum member shares = Schedule K column (d) totals (validation)

A disregarded single-member LLC completes Schedules B and K only if Schedule B line 1 or lines 3–11 is $3,000,000 or more, or Schedule K line 21a is $3,000,000 or more or −$3,000,000 or less; it never issues a Schedule K-1 (568) (2025 booklet, Filing Requirements for Disregarded Entities).

### Step 7 — Assign California income (Schedule IW) and apportion if multi-state (Schedule R)

Schedule IW assigns total income to California item by item: services where the customer receives the benefit, intangibles where used, tangible goods by destination, real property and rentals where located (R&TC §§25135–25136; 2025 booklet, Schedule IW instructions). An LLC wholly within California assigns everything to California. If the LLC has income inside and outside California, Schedule R apportions business income using the single-sales-factor formula (R&TC §25128.7) and Question M(1) is "Yes" (FTB LLC page). Out of scope: industry-specific §25137 rules, combined reports, three-factor situations — redirect to a CPA.

### Step 8 — Handle nonresident members (if any)

Two separate obligations (2025 booklet, General Information F and R):

- **Consent / Schedule T.** Every nonresident member should sign **FTB 3832**; attach it to Form 568. For each nonresident member who doesn't sign (or a nonresident single owner who doesn't sign the Side 3 consent), the LLC pays tax on that member's distributive share on **Schedule T** at 12.3% (individual, partnership, LLC, estate, trust), 8.84% (C corporation), or 1.5% (S corporation), reduced by tax already withheld for that member. Due by the original due date; on extension, pay with FTB 3537.
- **Withholding.** The LLC withholds 7% of distributions of California-source income to domestic nonresident members once a member's distributions exceed $1,500 in the calendar year, remits with **Form 592-Q** (payment periods due April 15, June 15, September 15, January 15), files **Form 592-PTE** by January 31 of the following year, and gives each member **Form 592-B** (2025 booklet, General Information R; 2025 Form 592-PTE instructions). Signing FTB 3832 does not remove this obligation.

See [`references/nonresident-members.md`](./references/nonresident-members.md). Out of scope: foreign (non-U.S.) members (R&TC §18666 withholding on allocations, Form 592-A / 592-F, federal §1446) — redirect to a CPA.

### Step 9 — Compute the bottom line

2025 Form 568, Side 1 and Side 2:

```
Line 1   Total income from Schedule IW (line 17)
Line 2   Limited liability company fee (tier table)
Line 3   2025 annual LLC tax ($800; $0 only under the deployed-military exemption)
Line 4   Pass-through entity elective tax (FTB 3804, Part I, line 3; only if elected)
Line 5   Nonconsenting nonresident members' tax (Schedule T total)
Line 6   Partnership level tax (only after an IRS centralized partnership audit; else blank)
Line 7   Total tax and fee = lines 2 + 3 + 4 + 5 + 6
Line 8   Amount paid with FTB 3537, 2025 FTB 3522, and FTB 3536
Line 9   Amounts paid for pass-through entity elective tax (FTB 3893 / electronic)
Line 10  Overpayment from prior year allowed as a credit
Line 11  Withholding (Form 592-B and/or 593) claimed by the LLC
Line 12  Total payments = lines 8 + 9 + 10 + 11
Line 13  Use tax (not a total line)
Line 14  Payments balance = line 12 − line 13, if line 12 is more
Line 15  Use tax balance = line 13 − line 12, if line 13 is more
Line 16  Tax and fee due = line 7 − line 14, if line 7 is more
Line 17  Overpayment = line 14 − line 7, if line 14 is more
Line 18  Amount of line 17 credited to 2026 tax or fee
Line 19  Refund = line 17 − line 18
Line 20  Penalties and interest
Line 21  Total amount due = lines 15 + 16 + 18 + 20 − line 17
```

### Step 10 — Run validation

See **Validation** below. Run every check.

### Step 11 — Produce the deliverable

See **Output format** below.

### Step 12 — Hand off downstream

State the next steps:

- **If multi-member**: each member gets a Schedule K-1 (568) plus the federal Schedule K-1 (1065) for their own returns; nonresident members file Form 540NR (FTB 3832 does not satisfy their filing requirement)
- **If single-member**: the owner reports the LLC's activity on federal Schedule C (or E / F) and on the California return; depreciation differences for an individual owner go on Schedule CA (540) via FTB 3885A
- **Withholding**: Form 592-B goes to each member who was withheld upon; the member attaches it to the California return
- **Next year**: FTB 3522 due by the 15th day of the 4th month (April 15, 2026 for calendar 2026), FTB 3536 estimate by the 15th day of the 6th month (June 15, 2026)

### Step 13 — File the return (optional)

If the agent has browser-automation tooling and the user authorizes filing, follow [`filing.md`](./filing.md). An LLC that prepares Form 568 with tax preparation software must e-file it (R&TC §18621.10; 2025 booklet, What's New "Business e-file"). CalFile does not support Form 568. Paper filing remains for hand-prepared returns or under an FTB waiver.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below (2025 Form 568).

### Side 1 header items

- **A** — California SOS file number
- **B** — FEIN
- **E** — Accounting method: cash, accrual, or other (attach explanation)
- **F** — Date business started in California
- **G** — Total assets at end of year (not required when Schedules L, M-1, M-2 are not required; enter $0 if no assets)
- **H** — Initial return, final return, amended return, or protective claim
- **I(1)–(3)** — Changes in control or ownership of entities owning or leasing California real property; "Yes" to both parts of any question requires the BOE-100-B statement

### Side 1 money lines

- **Line 1** — Schedule IW line 17; never negative. **Not** federal gross receipts or profit.
- **Line 2** — LLC fee from the tier table (Step 3)
- **Line 3** — $800 annual tax for 2025
- **Line 4** — PTE elective tax, if the LLC elected (out of scope beyond the line entry)
- **Line 5** — Schedule T total
- **Line 6** — Partnership level tax; normally blank
- **Lines 7–21** — See Step 9

### Side 2 and Side 3 questions

- **J** — Principal business activity code (six digits from the booklet's PBA code chart), business activity, product or service. "Do not leave blank."
- **K** — Maximum number of members at any time during the year
- **M(1)/(2)** — Using Schedule R? If not, registered with no California-source income (the "SB 1106 Filing" situation)
- **P(1)–(3)** — Foreign or domestic nonresident members; withholding forms filed
- **U(1)–(3)** — Disregarded entity? Credits? California income less than total income?
- **GG(2)** — First year of doing business in California
- **Single Member LLC Information and Consent** (Side 3) — owner's name, TIN, owner entity type, and signed consent. Complete only if the LLC is disregarded.

### Schedule IW — LLC Income Worksheet (Side 7)

California amounts only, income and gains but never losses: lines 1a/1b (Schedule B gross profit plus its cost of goods sold), 2a/2b (a disregarded entity's gross income and cost of goods sold not reported elsewhere, from the owner's federal schedules), 3a–3c (pass-through shares), 4 (farm gross income), 5 (other income), 6 (gains), 7 (subtotal), 8a–8c (rental real estate), 9a–9c (other rentals), 10–16 (interest, dividends, royalties, capital gains, §1231 gains, other portfolio income, other income), 17 (total → Side 1, line 1). Lines 1b, 2b, 3b, 3c, and 17 may not be negative.

For a service-only LLC wholly within California, line 17 ≈ gross receipts plus any interest and other income. For multi-state LLCs, assign item by item (Step 7).

### Schedule K (568) and Schedule K-1 (568)

Mirrors federal K / K-1 with a California-adjustments column. See [`references/california-adjustments.md`](./references/california-adjustments.md) for depreciation, §179, and other federal-to-California differences.

### Schedules L, M-1, M-2

Not required, along with Item G, if the LLC answered "Yes" to federal Form 1065 Schedule B Questions 4a–4c and has 10 or fewer members (2025 booklet, Schedule L). Federal Question 4a requires total receipts under $250,000 and 4b total assets under $1 million (2025 Form 1065). A disregarded single-member LLC is not listed as completing these schedules.

### Schedule T — Nonconsenting Nonresident Members' Tax Liability

Columns (c) distributive share × (d) rate = (e) tax, minus (f) amount withheld by this LLC on Form 592-B = (g) net tax (not below zero). Total goes to Side 1, **line 5** (the Schedule T caption on the 2025 form says "line 4"; the Side 1 label and the booklet's line 5 instruction control — flag it to the user).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 1 = Schedule IW line 17, and line 1 ≥ 0
- [ ] Line 2 matches the tier for line 1 ($0 below $250,000)
- [ ] Line 7 = lines 2 + 3 + 4 + 5 + 6
- [ ] Line 8 = every FTB 3522 (2025), FTB 3536, and FTB 3537 payment for the year, including Web Pay
- [ ] Line 12 = lines 8 + 9 + 10 + 11; lines 14–17 follow the form's either/or rules; line 21 = 15 + 16 + 18 + 20 − 17
- [ ] Schedule T column (g) total = line 5
- [ ] If multi-member: sum of member K-1 (568) shares = Schedule K column (d) for every line; number of K-1s = Question K
- [ ] If Schedule L filed: balance sheet balances (assets = liabilities + capital)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] First taxable year began 2024–2026 but no $800 was paid → AB 85 ended with 2023 first years; the $400 rate starts with 2027 first years
- [ ] Line 1 within a few percent of a tier boundary ($250,000, $500,000, $1,000,000, $5,000,000) → confirm every California-source item and the sourcing records
- [ ] FTB 3536 paid by the 6th-month date < fee for the year **and** < prior-year total fee → 10% penalty under R&TC §17942(d)(2)
- [ ] Nonresident member with no FTB 3832 and no Schedule T entry → consent or Schedule T missing
- [ ] Distributions to a domestic nonresident member above $1,500 with no Form 592-Q / 592-PTE → withholding missed
- [ ] Federal §179 > $25,000, or federal §179 property placed in service > $200,000 → California limit and phase-down apply
- [ ] Federal bonus depreciation (§168(k)) → California does not conform; recompute on FTB 3885L
- [ ] Out-of-state customers or activity but Schedule IW assigns 100% to California, or no Schedule R → confirm sourcing
- [ ] "Final return" checked but no SOS cancellation (LLC-4/7, plus LLC-3 for a domestic LLC) planned within 12 months → the $800 keeps accruing (2025 booklet, General Information Q)

### Cross-form checks

- [ ] If multi-member: federal Form 1065 drafted; Schedule K column (b) ties to federal Schedule K
- [ ] If single-member: owner's federal Schedule C / E / F totals tie to Schedule IW (lines 2a/2b and the income lines)
- [ ] FTB 3832 attached for every consenting nonresident member
- [ ] Form 592-B issued to every member withheld upon
- [ ] Federal tax on Form 1065 / 1040 is separate from this Form 568

---

## Output format

The agent's deliverable is a **filled draft** the user can enter into Form 568-capable tax software or transcribe to the FTB form.

```markdown
# California Form 568 — DRAFT for taxable year YYYY

## Identification (Side 1)
A. SOS file number: XXXXXXXXXXXX
B. FEIN: XX-XXXXXXX
E. Accounting method: [Cash / Accrual / Other]
F. Date business started in CA: MM/DD/YYYY
G. Total assets EOY: $X,XXX,XXX (or "not required")
H. Boxes checked: [Initial / Final / Amended / Protective claim / none]
I(1)–I(3): Yes / No

## Side 1 — Tax, fee, and payments
Line 1.  Total income from Schedule IW:          $X,XXX,XXX
Line 2.  LLC fee:                                 $X,XXX
Line 3.  Annual LLC tax:                          $800
Line 4.  PTE elective tax:                        $0
Line 5.  Nonconsenting nonresident members' tax:  $X,XXX
Line 6.  Partnership level tax:                   (blank)
Line 7.  Total tax and fee (2+3+4+5+6):           $X,XXX
Line 8.  Paid with FTB 3537 / 3522 / 3536:        $X,XXX
Line 9.  PTE elective tax payments:               $0
Line 10. Prior-year overpayment credited:         $0
Line 11. Withholding (592-B / 593):               $0
Line 12. Total payments (8+9+10+11):              $X,XXX
Line 13. Use tax:                                 $0
Line 14. Payments balance:                        $X,XXX
Line 15. Use tax balance:                         $0
Line 16. Tax and fee due:                         $X,XXX
Line 17. Overpayment:                             $0
Line 18. Credited to next year:                   $0
Line 19. Refund:                                  $0
Line 20. Penalties and interest:                  $0
Line 21. Total amount due:                        $X,XXX

## Questions (Side 2–3)
J. PBA code / activity / product: XXXXXX / <activity> / <product>
K. Maximum members: N
M(1) Schedule R: Yes / No    P(1)/P(2) nonresident members: Yes / No
U(1) Disregarded: Yes / No   GG(2) First year doing business in CA: Yes / No
SMLLC owner type (if disregarded): [Individual / C corp / Pass-through / Estate-Trust / Exempt]

## Schedule IW — every line, including zeros
1a ... 17 → Side 1, line 1

## Schedule K (568) (if partnership-classified or $3M SMLLC)
| Line | Item | (b) Federal | (c) CA adjustment | (d) California |

## Schedule K-1 (568) per member
| Member | TIN | Ownership % | Distributive share | Resident? | FTB 3832 signed? | Withheld (592-B) |

## Schedule T (if nonconsenting nonresident members)
| Member | TIN | (c) Share | (d) Rate | (e) Tax | (f) Withheld | (g) Net |

## Payments and attachments
- [ ] FTB 3522 ($800) — paid date / confirmation
- [ ] FTB 3536 (estimate; and any balance by the original due date)
- [ ] FTB 3537 (only if NCNR tax owed and filing on extension)
- [ ] FTB 3832 (each consenting nonresident member)
- [ ] Form 592-Q / 592-PTE / 592-B (withholding on distributions to domestic nonresidents)
- [ ] FTB 3885L (depreciation), Schedule R (if apportioning), federal Form 8832 copy (year of election)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 12>

## Sources cited in this draft
- 2025 Form 568 and 2025 Form 568 Booklet (FTB)
- R&TC §17941, §17942, §18567, §18633.5, §19132, §19172, §23101
- <any other authority used>
```

The draft is **not** the final filed form. The user still has to enter it into software that e-files Form 568 or, for a hand-prepared return, paper-mail it. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line on 2025 Form 568 Side 1, the Side 2–3 questions, Schedule IW, Schedule K, Schedule T, and Schedules L/M-1/M-2
- [`references/llc-fee-tiers.md`](./references/llc-fee-tiers.md) — How "total income" is computed under §17942, tier-boundary edge cases, sourcing for multi-state LLCs, and the estimated-fee penalty
- [`references/doing-business-in-california.md`](./references/doing-business-in-california.md) — R&TC §23101 tests; 2025 thresholds $757,070 sales / $75,707 property / $75,707 payroll
- [`references/california-adjustments.md`](./references/california-adjustments.md) — Depreciation conformity (no §168(k) bonus), §179 limit ($25,000), and other federal-to-California adjustments
- [`references/nonresident-members.md`](./references/nonresident-members.md) — FTB 3832 consent, Schedule T, and the separate 7% withholding on distributions (592-Q / 592-PTE / 592-B)
- [`references/llc-vs-s-corp-classification.md`](./references/llc-vs-s-corp-classification.md) — When an LLC files Form 568 vs. Form 100 / 100S (California follows the federal election)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with citations
- [`filing.md`](./filing.md) — Payment and filing playbook: Web Pay, e-file software, paper, extensions, mailing addresses

## Examples

End-to-end worked Form 568 returns for taxable year 2025. Use these as patterns when the user's situation is similar.

- [`examples/smllc-zero-revenue.md`](./examples/smllc-zero-revenue.md) — First-year single-member LLC with $0 revenue still owes $800 and files Form 568; late first payment with penalty and interest
- [`examples/multi-member-mid-tier.md`](./examples/multi-member-mid-tier.md) — Two-member LLC with $401,200 of California income: $800 + $900 fee, §179 California adjustment
- [`examples/smllc-high-tier.md`](./examples/smllc-high-tier.md) — Single-member LLC with $1,050,000 assigned to California: $800 + $6,000 fee, prior-year safe harbor on the estimate

## Sources

Authoritative sources used by this skill. Re-verify each year against the FTB site for the taxable year being filed.

- [California Form 568 (2025)](https://www.ftb.ca.gov/forms/2025/2025-568.pdf) — the form itself
- [California Form 568 Booklet (2025)](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf) — instructions (General Information D, E, F, G, Q, R, S; Specific Line Instructions; Schedule IW; Schedule T; Schedule L)
- [FTB 3522 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3522.pdf) and [FTB 3522 (2026)](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf) — $800 annual LLC tax voucher
- [FTB 3536 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3536.pdf) and [FTB 3536 (2026)](https://www.ftb.ca.gov/forms/2026/2026-3536.pdf) — estimated fee voucher
- [FTB 3537 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3537.pdf) — payment for automatic extension for LLCs
- [FTB 3832 (2025)](https://www.ftb.ca.gov/forms/2025/2025-3832.pdf) — nonresident members' consent
- [Form 592-Q (2025)](https://www.ftb.ca.gov/forms/2025/2025-592-q.pdf), [Form 592-PTE (2025)](https://www.ftb.ca.gov/forms/2025/2025-592-pte.pdf) and [instructions](https://www.ftb.ca.gov/forms/2025/2025-592-pte-instructions.html), [Form 592-A (2025)](https://www.ftb.ca.gov/forms/2025/2025-592-a.pdf) — withholding vouchers and annual return
- [FTB 3885L (2025)](https://www.ftb.ca.gov/forms/2025/2025-3885l.pdf) — California depreciation; §179 limit $25,000, threshold $200,000
- [FTB Limited Liability Company page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) — first-year due-date example, AB 85 years, fee table
- [FTB Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) — indexed thresholds by year
- [FTB What's new with tax forms](https://www.ftb.ca.gov/forms/whats-new.html) — SB 122 ($400 first-year tax, 2027–2029), SB 711 (IRC conformity date January 1, 2025), SB 132 (PTE elective tax extended)
- [FTB Interest and estimate penalty rates](https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html)
- [FTB Pub. 3556 (LLC MEO)](https://www.ftb.ca.gov/forms/misc/3556.html) — Limited Liability Company Filing Information
- California Revenue and Taxation Code:
  - §17941 — Annual LLC tax ($800)
  - §17942 — LLC fee (tiers; total income definition; 6th-month estimate and 10% penalty)
  - §18567 — Extensions (7 months for partnership-classified LLCs)
  - §18621.10 — Business e-file requirement
  - §18633.5 — LLC return due dates
  - §19131, §19132, §19172 — Late filing, late payment, and per-member filing penalties
  - §19521 — Interest
  - §23101 — Doing business in California
  - §23801 — Federal S election applies for California
  - §25128.7, §25135, §25136 — Single-sales-factor apportionment and sales assignment
- AB 85 (Stats. 2020, ch. 8) — first-year $800 exemption for first taxable years 2021–2023; ended
- [2025 Instructions for Form 4562](https://www.irs.gov/pub/irs-pdf/i4562.pdf) — federal §179 $2,500,000 / $4,000,000; bonus depreciation for property acquired after January 19, 2025

## Disclaimer

This skill encodes procedural guidance based on publicly available California Franchise Tax Board forms and instructions and the California Revenue and Taxation Code. It is not tax advice and does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations — especially those involving multi-state apportionment, nonresident or foreign members, or entity-classification elections — warrant a licensed California tax professional's review.
