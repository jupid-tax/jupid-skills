# Schedule E Parts II–V: K-1 Income, Estates and Trusts, REMICs, Summary

Load this file when the user has a Schedule K-1 from a partnership (Form 1065), S corporation (Form 1120-S), or estate or trust (Form 1041), or a Schedule Q from a REMIC. Sources: 2025 Schedule E page 2 and 2025 Instructions for Schedule E (Parts II, III, IV, V); Instructions for Form 7203 (Rev. Dec. 2022); Instructions for Form 8582 (2025).

The K-1 and its own instructions say where each box goes. This skill places only the items the K-1 instructions send to Schedule E. Never attach the K-1 to the return; keep it (Instructions, Part II and Part III).

## Part II: Partnerships and S corporations

### Columns of line 28

| Column | Content | Put here |
|--------|---------|----------|
| (a) | Name | Entity name; separate lines labeled "PYA", "UPE", "business interest", "passive interest", "investment interest", or a related-item description (e.g., "depletion") |
| (b) | P or S | P = partnership, S = S corporation |
| (c) | Foreign partnership | Check if foreign; Form 8865 may be required (controlled, ≥10% interest while U.S. persons control, certain acquisitions, dispositions or contributions; contributions over $100,000 in a 12-month period) |
| (d) | EIN | From the K-1 |
| (e) | Basis computation required | S corporation: loss, distribution, stock disposition, or loan repayment. Attach Form 7203 |
| (f) | Any amount not at risk | Attach Form 6198 |
| (g) | Passive loss allowed | From Form 8582 Part VIII or IX, or the loss itself when the rental-real-estate exception lets you skip Form 8582 (general partner or S shareholder in a rental real estate activity meeting every condition) |
| (h) | Passive income from Schedule K-1 | Passive income items |
| (i) | Nonpassive loss allowed | After basis and at-risk; Form 6198 deductible loss for nonpassive at-risk activities |
| (j) | Section 179 expense deduction from Form 4562 | Pass-through §179 after your own Form 4562 limit; route to `../../form-4562/SKILL.md` |
| (k) | Nonpassive income from Schedule K-1 | Nonpassive income items |

Report the current-year ordinary income or loss on one line, then each related item that must go on Schedule E on its own following line with a description in column (a) (Instructions, Line 28). If Form 8582 is required, follow its instructions first.

### Passive or nonpassive

Character depends on your participation in that entity's activity, not on whether it is a partnership or S corporation. Use the seven material participation tests in `passive-loss-and-at-risk.md`. Limited partners: generally not material participants. Ask the user for hours and role for each K-1; do not infer from ownership percentage.

### Line 27 and the separate-line rules

Answer line 27 "Yes" if you are reporting any of: a loss not allowed in a prior year due to at-risk or basis limits, a prior-year unallowed passive loss not reported on Form 8582, or unreimbursed partnership expenses (UPE). Then (Instructions, Line 27):

- **Prior-year basis or at-risk losses now deductible**: total on a separate line in column (i); write "PYA" in column (a). Never net against current-year amounts.
- **Prior-year unallowed passive losses not reported on Form 8582** (for example, now deductible because there is no overall passive loss, or because the entire interest was disposed of in a fully taxable transaction): separate line in column (g); "PYA" in column (a).
- **UPE**: deductible only if the partnership agreement required you to pay them and they are §162 expenses. Nonpassive: separate line in column (i). Passive and no Form 8582 required: separate line in column (g). Passive and Form 8582 required: do not report separately (they go through Form 8582). Write "UPE" in column (a).

Skipping these rules produces IRS mismatch notices because Schedule E will not agree with the K-1 (Instructions, Line 27).

### Debt-financed acquisitions

If loan proceeds bought an interest in, or funded a capital contribution to, a partnership or S corporation, allocate the loan and interest among the entity's assets by any reasonable method (Instructions, Line 28):

- Trade or business assets: separate line, "business interest" and entity name in (a), amount in (i).
- Passive activity use: through Form 8582; deductible amount on a separate line, "passive interest" in (a), amount in (g).
- Investment use: Form 4952; amount allocated to royalties on a separate line, "investment interest" in (a), column (i); the balance to Schedule A line 9.
- Personal use: generally not deductible.

### Basis (Form 7203 for S corporations)

Stock basis is adjusted at year end in this order unless the user has made the Treas. Reg. §1.1367-1(g) election (Instructions for Form 7203):

1. Increase by all income items (including tax-exempt income) on the K-1.
2. Decrease (not below zero) by distributions (K-1 box 16, code D), less the part in excess of stock basis.
3. Decrease (not below zero) by nondeductible expenses and certain oil and gas depletion.
4. Decrease (not below zero) by losses and deductions.

Losses blocked by basis carry forward indefinitely. Distributions in excess of basis are reported as gain per Form 7203 (route to `../../form-8949/SKILL.md` or `../../schedule-d/SKILL.md`). Partnership basis: use the partner's basis worksheet in the Partner's Instructions for Schedule K-1 (Form 1065) and Pub. 541.

Ask for last year's Form 7203 or basis schedule. If the user has never tracked basis, stop and recommend a CPA before claiming any K-1 loss.

### Other Part II rules from the instructions

- Partnership income may be net earnings from self-employment: K-1 (Form 1065) box 14, code A goes to Schedule SE after reducing by allowable expenses (route to `../../schedule-se/SKILL.md`). Schedule E itself does not compute SE tax.
- S corporation net income is not subject to self-employment tax.
- S corporation distributions of prior-year accumulated earnings and profits are dividends on Form 1040 line 3b, not Schedule E.
- Fuel tax credit claimed on the 2024 return from partnership information: include as income in column (h) or (k) for 2025.
- Partnership gambling: winnings in column (k), losses in column (i), limited to total winnings on the return.
- AMT preference items from K-1s go to Form 6251.
- If you treat any item differently from the K-1, Form 8082 may be required.
- Excess business loss: figured on Form 461 after Schedule E; not reflected on Schedule E.

## Part III: Estates and trusts

Report your share of income (even if not received) or loss from Schedule K-1 (Form 1041) in line 33 columns (c)–(f), split passive/nonpassive like Part II. Totals: line 34a (d, f), 34b (c, e), line 35, line 36, line 37 (Instructions, Part III; form).

Trust estimated tax credited to you (K-1 (Form 1041) box 13, code A): write "ES payment claimed" and the amount on the dotted line next to line 37, exclude it from line 37, and claim it on Form 1040 line 26 (Instructions, Part III).

Foreign trusts: Schedule B Part III and possibly Form 3520; a U.S. transferor may be taxed under §679. These are outside this skill; flag for CPA review.

## Part IV: REMIC residual holders (boundary)

Use only for a residual interest; regular-interest income goes on Form 1040 line 2b (Instructions, Part IV). Enter Schedule Q (Form 1066) amounts: column (c) line 2c (excess inclusion), (d) line 1b, (e) line 3b. Line 39 combines (d) and (e) only. Column (c) is not included in line 39; it is the floor for taxable income on Form 1040 line 15 and for AMTI on Form 6251 line 4 (write "Sch Q" next to the entry). REMIC income or loss is not passive. Almost no individual filer has this; if the user does, prepare the column entries and recommend CPA review.

## Part V: Summary

- Line 40: net farm rental income or (loss) from Form 4835; also complete line 42.
- Line 41: combine lines 26, 32, 37, 39, 40 → Schedule 1 (Form 1040), line 5.
- Line 42: gross farming and fishing income from Form 4835 line 7; K-1 (Form 1065) box 14 code B; K-1 (Form 1120-S) box 17 code AN; K-1 (Form 1041) box 14 code F. Relevant to the farmer/fisher estimated tax exception (gross farming or fishing income at least two-thirds of gross income for 2024 or 2025, and file and pay by March 2, 2026) (Instructions, Line 42).
- Line 43: real estate professionals only; net income or loss from all rental real estate activities with material participation, wherever reported on the return.

## Questions to ask for each K-1

1. "Send the K-1 and the K-1 instructions page or supplemental statement."
2. "Did you work in this business in 2025? Roughly how many hours, and in what role? Are you a limited partner?"
3. "For an S corporation: did you receive any distributions or loan repayments, or sell stock? Do you have last year's Form 7203?"
4. "For a partnership: do you have a basis worksheet? Any nonrecourse debt or guarantees?"
5. "Any losses from this entity that were not allowed in earlier years? Why (basis, at-risk, passive)?"
6. "Did the partnership agreement require you to pay any partnership expenses yourself?"
7. "Did you borrow money to buy this interest or to contribute capital?"
