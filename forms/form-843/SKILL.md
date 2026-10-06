---
name: form-843
description: >
  Use this skill when a taxpayer wants the IRS to remove (abate) or refund a
  penalty or addition to tax, remove interest caused by IRS error or delay,
  or claim one of the narrow non-income-tax refunds that only Form 843
  handles (excess social security or Medicare from one employer that will not
  adjust, FICA or RRTA withheld in error, excess tier 2 RRTA). Triggers on
  phrases like "Form 843", "penalty abatement", "first time abate", "FTA
  request", "remove my late filing penalty", "waive the failure to pay
  penalty", "reasonable cause letter", "IRS penalty relief", "refund of a
  penalty I already paid", "abate interest because the IRS delayed",
  "Letter 854C", "net interest rate of zero". Do NOT use for an income tax
  refund or any change to Form 1040 amounts (use form-1040-x); the estimated
  tax penalty under section 6654 (use form-2210); employer corrections of
  FICA or withholding (use the 941-X family, see form-941); refunds of
  installment agreement, offer in compromise, or lien fees (not refundable
  on Form 843); return preparer or promoter penalties (Form 6118); paying a
  balance over time (use form-9465); settling the tax for less (use
  form-656).
form: Form 843 (Claim for Refund and Request for Abatement)
audience: [individual, solo, freelance, llc1, llcm, scorp, ccorp, partnership, employer]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f843.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i843.pdf
---

# Form 843 — Claim for Refund and Request for Abatement

This skill turns an IRS penalty or interest charge into one of three outcomes: a phone script for the number on the notice, a "no action" finding (the charge is not Form 843 material or the IRS should apply relief on its own), or a complete Form 843 draft with a line 8 explanation, a computation of line 2, and an evidence list. The arithmetic is light. The judgment sits in four places: picking the relief ground in the order the IRS applies them (account correction, written advice, AEP, First Time Abate, reasonable cause), splitting requests one period and one tax type per form, checking the IRC §6511 refund window for amounts already paid, and refusing requests that belong on another form.

Line map verified against **Form 843 (Rev. December 2024)** and **Instructions for Form 843 (Rev. December 2024)**, with penalty policy from IRM 20.1.1 (effective 11-25-2025; First Time Abate at IRM 20.1.1.3.3.2.1, 03-29-2023) and the IRS First Time Abate / AEP page (last reviewed 14-Jul-2026). Form 843 is not revised annually; before each use, confirm the revision at https://www.irs.gov/forms-pubs/about-form-843 and re-check the FTA/AEP page, which changed in 2026.

**Companion guide for end users:** [Form 843 (2026): How to Request IRS Penalty Abatement](https://jupid.com/blog/form-843-penalty-abatement-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user names Form 843, penalty abatement, First Time Abate, or penalty relief
- The user has an IRS notice showing a failure-to-file, failure-to-pay, failure-to-deposit, accuracy-related, or similar penalty and wants it removed or refunded
- The user already paid a penalty and wants the money back
- The user says IRS delays (a lost file, a stalled transfer, a late notice of deficiency) ran up interest
- The user received Letter 854C (penalty relief denied) and wants to respond
- An employee had excess social security, Medicare, or RRTA tax withheld by one employer that refuses to fix it

Do **not** engage this skill when:

- The money is overpaid **income tax** or the user wants to change a Form 1040 amount → `../form-1040-x/SKILL.md`
- The penalty is the **estimated tax penalty** (§6654; notice says "underpayment of estimated tax") → `../form-2210/SKILL.md`
- An **employer** wants to correct FICA, RRTA, or income tax withholding → the matching X form (941-X etc.); see `../form-941/SKILL.md`
- The user wants a refund of an **installment agreement, offer in compromise, or lien fee** → not refundable on Form 843 (i843, Purpose of Form)
- The user wants to **pay over time** → `../form-9465/SKILL.md`; **settle for less** → `../form-656/SKILL.md`
- The user disputes that the **tax** itself is owed → IRC §6404(b) bars abatement claims for income, estate, and gift tax; follow the notice, consider audit reconsideration, `../form-1040-x/SKILL.md`, or Form 656-L in `../form-656/SKILL.md`

The full routing table is in [`references/wrong-form-routing.md`](./references/wrong-form-routing.md). If the user's charge is ambiguous, ask them to read the notice heading and the Code section printed next to the penalty before you proceed.

---

## Prerequisites

Before producing anything, get these inputs. If any are missing, **ask for them explicitly** and stop until answered. Never infer a period, an amount, or a Code section.

1. **The notice or transcript.** Notice number (for example CP14, CP161, CP215), notice date, the return address printed on it, and the toll-free number in the top right corner. Without a notice, ask for an IRS account transcript (IRS Online Account or `../form-4506-t/SKILL.md`).
2. **For each charge:** penalty name, IRC section, tax period, assessed amount, and whether any part is paid. Ask: "Please read me each penalty line from the notice: its name, the Code section if shown, the period, and the amount."
3. **Return type and filer identity:** Form 1040, 941, 1120, 1065, 1120-S, and so on; legal name; SSN, ITIN, or EIN; for Form 1040, whether the related return was joint and the spouse's name and SSN.
4. **Payment history** for anything to be refunded: each payment date and amount. Ask: "Did you pay any of this penalty or interest? On which dates and in what amounts?"
5. **Filing date of the related return** (actual date, or "before the due date"). Needed for the §6511 window.
6. **Compliance history** for the same return type in the three prior periods: filed on time? any penalties? any penalty removed, and on what ground? Ask specifically: "Did the IRS remove a penalty for you in the last three years with a letter saying it was a one-time removal for good history?"
7. **What happened**, with dates: start and end of each event, when the taxpayer filed or paid after it ended, and what documents exist.
8. **Prior contact:** did the user already call or write? Any denial letter (Letter 854C) and its date?
9. **Representation:** is a CPA, EA, or attorney acting? If yes, a Form 2848 must be attached.
10. **For interest requests:** date of the first written IRS contact about the deficiency or payment, and the dates of the IRS error or delay.
11. **Signing details:** current address and daytime phone; whether the IRS issued an Identity Protection PIN (taxpayer and spouse). Use the IP PIN only in the draft; do not store it.

---

## Workflow

Execute in order.

### Step 1 — Confirm Form 843 is the vehicle

Run the decision questions in [`references/wrong-form-routing.md`](./references/wrong-form-routing.md). If the request belongs on another form, stop, name the form and sibling skill, and explain in one sentence why.

### Step 2 — Check whether relief should already have happened

- **Account error:** the return was filed or the tax paid on time. Ask for proof (e-file acceptance, certified mail receipt, cancelled check front and back). An account correction is not a penalty waiver.
- **AEP:** for a 2025-or-later annual return or 2026-or-later quarterly return of Forms 1040, 1065, 1120, 940, 941, 943, 944, 945, or CT-1, the IRS applies Automatic Exemption from Penalty at processing when the prior three years (12 quarters) were timely. If a penalty was assessed anyway, the IRS says to contact it. Route to the notice phone number first. See [`references/penalty-relief-paths.md`](./references/penalty-relief-paths.md), section 2.

### Step 3 — Pick the relief ground

In the IRS order (IRM 20.1.1.3.3.2.1: administrative waivers before reasonable cause):

1. Erroneous written advice from the IRS (§6404(f)) → line 7 box b
2. First Time Abate (penalties under §6651(a)(1)–(3), §6698(a)(1), §6699(a)(1), §6656 only) → line 7 box c (see Line 7 below)
3. Reasonable cause → line 7 box c
4. IRS error or delay causing interest (§6404(e)(1)) → line 7 box a
5. Net interest rate of zero (§6621(d)) → no line 7 entry

Fill the FTA lookback worksheet in `penalty-relief-paths.md` section 3 with the user's answers. Report the result as "likely eligible", "not eligible because …", or "unknown, the IRS will check". Never promise approval.

If the user's only reason is on the IRS "generally does not qualify" list (reliance on a preparer, lack of knowledge, a mistake, lack of funds alone), say so before drafting and ask for other facts.

### Step 4 — Pick the channel

| Situation | Channel |
|---|---|
| Notice in hand, likely FTA | Call the toll-free number on the notice; Form 843 if the call cannot approve it |
| Reasonable cause with documents | Call first if the user prefers; otherwise written statement or Form 843 to the notice return address |
| Penalty or interest already paid, refund wanted | Form 843 (a written claim filed inside the §6511 period protects the refund) |
| §6404(e) interest abatement | Form 843 or a signed letter |
| No notice (charge seen only on a transcript) | Form 843 to the service center for the current-year return of that tax |
| Denial letter received | Appeal (see Step 11), not a new Form 843 |

Sources: IRS FTA page; IRS reasonable cause page; IRS interest abatement page; i843 Where To File.

### Step 5 — Check timing

- Paid amounts: run the §6511 worksheet in [`references/refund-and-interest-rules.md`](./references/refund-and-interest-rules.md). A claim must be filed within 3 years from filing the return or 2 years from payment, whichever is later (§6511(a)); the refund is capped by payments inside the lookback (§6511(b)(2)). A return filed early counts as filed on the due date (§6513(a)).
- If a deadline is within 30 days, tell the user to mail by certified mail now.
- Written advice requests: within the collection period, or the refund period if paid (i843).
- Denials: appeal generally within 30 days of the letter (IRS penalty appeal page).

### Step 6 — Split into forms

One Form 843 per tax period and per tax type (i843, Separate Form Required). Exceptions: net interest rate of zero; one IRS act under §6404(e) affecting several years or tax types. Several penalties on the same period and return go on one form; line 2 totals them and line 8 itemizes.

### Step 7 — Fill lines 1–7

Use the rules in **Line-by-line guidance** below and the full map in [`references/line-by-line.md`](./references/line-by-line.md).

### Step 8 — Draft line 8

Structure:

```
Request: [abatement | refund] of [penalty name] under IRC [section] for the period
[MM/DD/YYYY–MM/DD/YYYY], amount $[line 2], [plus any further accruals of the same
penalty for this period].
Ground: [First Time Abate | reasonable cause | erroneous written advice | IRS error
or delay under §6404(e)(1)].
Facts: [event] began [date] and ended [date]. It prevented [filing | payment]
because [mechanism]. The taxpayer [filed | paid] on [date], [N] days after it ended.
Compliance history: [prior three periods, if FTA].
Computation of line 2: [itemized amounts from the notice, or interest estimate
method with rates and dates].
Attachments: [list, each labeled with name and TIN].
```

Keep it factual: dates, mechanism, evidence. No apology paragraphs, no adjectives.

### Step 9 — Validate

Run every check in **Validation**.

### Step 10 — Produce the deliverable

Use **Output format**. Show every line, including blanks.

### Step 11 — Hand off

- Filing: follow [`filing.md`](./filing.md) for the channel, address, signatures, and mailing.
- After a grant: interest on the abated penalty comes off automatically; a refund arrives by check or offset.
- After a denial (usually Letter 854C): appeal within the period in the letter, generally 30 days. Small case request (Form 12203 or brief statement) when tax plus penalties per period is $25,000 or less; formal written protest otherwise (Publication 5).
- Interest denial under §6404(e): note the Tax Court review window under §6404(h) and recommend a tax professional.

---

## Line-by-line guidance

Full map: [`references/line-by-line.md`](./references/line-by-line.md).

### Reason checkbox (top of page 1)

Check exactly one box ("Do not check more than one box," i843). Most requests use the Penalty box "Abatement or refund of a penalty or addition to tax due to reasonable cause or other reason allowed under the law." Interest requests use one of the two Interest boxes. Do not check "Other (specify)" when another form is required.

### Identity block

Name and SSN/ITIN as on the related return; spouse's name and SSN for a joint return; EIN for entities. "Name and address shown on return if different" when either changed.

### Lines 1–7

| Line | Rule |
|---|---|
| 1 | Tax period from the notice, MM/DD/YYYY to MM/DD/YYYY. Blank for net-interest-zero requests |
| 2 | Amount to refund or abate. Penalty: the notice amount (total of all penalties requested for the period). Interest: the computed estimate |
| 3 | Payment dates, only for refunds. Blank for abatement of unpaid amounts |
| 4 | Tax type the penalty or interest relates to: e Income for Form 1040 penalties, a Employment for Form 941 penalties. One box unless an exception applies |
| 5 | Return type. Box i "1040" covers 1040-SR, 1040-NR, 1040 (sp). No 1065 or 1120-S box: use n "Other (specify)" and write the form number (agent's reading; tell the user) |
| 6 | IRC section of the penalty from the notice, for example 6651(a)(1) |
| 7 | a = IRS error or delay (interest); b = erroneous written advice; c = reasonable cause or other reason allowed under the law; d = none of the above |

**Line 7 for First Time Abate.** The instructions do not name FTA. Box c's wording "other reason allowed under the law" is the closest fit for an administrative waiver; some preparers use box d. Choose c unless the user or their CPA prefers d, write "First Time Abate" in line 8 either way, and tell the user the choice is an interpretation. The IRS says taxpayers "don't need to specify FTA" and checks eligibility itself.

### Line 8

Explain, compute line 2, attach evidence, and put the name and TIN on every attached sheet. Situation-specific contents for §6404(e), net interest zero, visual impairment, tier 2 RRTA, and the branded prescription drug fee are in the line-by-line reference.

### Signatures

Both spouses for a joint return. Corporations: an authorized officer with title. Estates and trusts: the fiduciary. Representatives: Form 2848 attached. Decedents: the representative statement or letters testamentary, plus Form 1310. Paid preparers complete their block; the agent never signs.

### Special situations

| Situation | Rule (i843) |
|---|---|
| Excess social security, Medicare, or RRTA from one employer | Attach the employer's statement of amounts repaid or claimed; if unobtainable, the employee's own statement explaining why, plus Form W-2 |
| Excess tier 2 RRTA | Lines 1–2; skip 3; line 4 box a; skip 5–7; line 8 "Excess tier 2 RRTA" with computation; attach all Forms W-2 |
| Trust Fund Recovery Penalty refund | Pay the divisible portion first: one employee's share (employment taxes) or one transaction (excise) for each period |
| Erroneous written advice | Lines 1–4, 6, 7b; attach the written request, the IRS advice, and any adjustment report |
| §6404(e) interest | Lines 1–4, 7a; line 8 five items (type of tax, first written notice date, period, circumstances, why non-abatement is grossly unfair) |
| Net interest rate of zero | Line 1 blank; lines 4–5 (multiple boxes allowed); skip 3, 6, 7; line 8 six items |

---

## Validation

Surface every failure. Do not silently fix.

### Math checks

- [ ] Line 2 equals the sum of the itemized amounts in the line 8 computation
- [ ] Each itemized penalty amount matches the notice or transcript to the cent
- [ ] For a refund: line 2 does not exceed payments dated inside the §6511(b)(2) lookback; the worksheet is shown
- [ ] For partly paid charges: paid part plus unpaid part equals line 2
- [ ] For §6404(e): the delay period's start date is after the first written IRS contact; quarterly rates match https://www.irs.gov/payments/quarterly-interest-rates; the estimate is labeled as an estimate
- [ ] Every date is MM/DD/YYYY and line 1 matches the notice period

### Form checks

- [ ] Exactly one reason box at the top
- [ ] One period and one tax type per form, or a documented exception
- [ ] Line 4 and line 5 have one box each, or a documented exception
- [ ] Line 6 filled for every penalty request (blank for interest-only)
- [ ] Line 7 has one box (none for net-interest-zero, tier 2 RRTA, BPD fee)
- [ ] Joint return: both names, both SSNs, both signature lines
- [ ] Representative: Form 2848 listed as attached
- [ ] Every attachment carries name and TIN

### Sanity checks (warn, do not block)

- [ ] Penalty is §6654 or §6655 → stop; route to form-2210 rules
- [ ] Request is really an income tax refund → stop; form-1040-x
- [ ] FTA requested but a penalty was removed under FTA in the three-year lookback → FTA will fail; switch to reasonable cause or another ground
- [ ] FTA requested for a penalty type FTA does not cover (accuracy-related, information return, event-based returns such as 706, 709, 3520, 5471, 5472, 8300) → switch grounds
- [ ] 2025-or-later return of an AEP series with a clean history and a penalty assessed → call the notice number first
- [ ] Reasonable-cause reason is only on the IRS "generally does not qualify" list → warn the user
- [ ] Evidence missing for a reasonable-cause claim → warn; ask for documents
- [ ] One set of facts used for two penalties whose time periods differ → warn; split the request
- [ ] Refund deadline within 30 days → tell the user to mail by certified mail today
- [ ] §6404(e) request on employment tax interest → not allowed (i843)
- [ ] Unpaid tax remains → tell the user the failure-to-pay penalty and interest keep accruing

---

## Output format

```markdown
# Form 843 — DRAFT (Rev. December 2024)

## Routing decision
- Channel: Phone (number on notice: ___) | Form 843 by mail | Written statement | Not Form 843 → use ___
- Relief ground: Account correction | §6404(f) written advice | AEP | First Time Abate | Reasonable cause | §6404(e) interest | Net interest zero
- FTA lookback: likely eligible | not eligible because ___ | unknown
- §6511 check (refunds only): return filed __/__/____; 3-year deadline __/__/____; claim date __/__/____; lookback from __/__/____; refundable payments $____

## Reason box (one)
[x] <exact label of the box>

## Identity
Name: ______________________   SSN/ITIN: ___-__-____
Spouse (joint return): ______  SSN: ___-__-____
Address: ____________________  EIN (entities): __-_______
Name/address on return if different: ______
Daytime phone: ______

## Lines
1. Tax period: MM/DD/YYYY to MM/DD/YYYY
2. Amount to be refunded or abated: $____.__
3. Payment dates: a ____ b ____ ... (or "blank: abatement of unpaid amount")
4. Type of tax: [a Employment | b Estate | c Gift | d Excise | e Income | f Fee | g Civil penalty]
5. Type of return: [box letter + form]
6. IRC section: ______ (or "blank: not a penalty request")
7. Reason: [a | b | c | d] (or "blank" with the instruction cited)
8. Explanation:
   <request sentence>
   <ground>
   <facts with dates>
   <compliance history, if FTA>
   <computation of line 2>
   <attachments list>

## Signatures
Taxpayer: ______ Date: ____ IP PIN: (enter only if issued)
Spouse (joint): ______ Date: ____
Paid preparer: (blank unless a paid preparer prepared it)

## Attachments
- [ ] <document, labeled with name and TIN>
- [ ] Form 2848 (if a representative files)

## Validation summary
- Math: all checks passed | <failures>
- Form: all checks passed | <failures>
- Warnings: <list>

## Mailing
Address: <notice return address | service center per i843 | special address>
Method: certified mail, return receipt; keep a copy of everything

## Next steps
- Expect a letter; FTP penalty and interest continue on unpaid tax meanwhile
- If denied (Letter 854C): appeal within the period stated, generally 30 days

## Sources cited in this draft
- Form 843 and Instructions for Form 843 (Rev. December 2024)
- IRM 20.1.1 (11-25-2025), IRM 20.1.1.3.3.2.1 (03-29-2023)
- IRS FTA/AEP page (last reviewed 14-Jul-2026); IRS reasonable cause page (21-Jun-2026)
- IRC §§6404, 6511, 6513(a), 6651 (and the penalty section on line 6)
```

The draft is not the filed form. The user prints, signs, attaches evidence, and mails it, or uses the phone route.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — Every field on Form 843 (Rev. December 2024) with the instruction text behind it
- [`references/penalty-relief-paths.md`](./references/penalty-relief-paths.md) — AEP, First Time Abate criteria from IRM 20.1.1.3.3.2.1, reasonable cause standards and evidence, erroneous written advice, the estimated tax penalty track, denial and appeal
- [`references/refund-and-interest-rules.md`](./references/refund-and-interest-rules.md) — §6511 window and lookback worksheet, §6404(e) interest abatement criteria and computation, net interest rate of zero, §6404(g) and §6404(h)
- [`references/wrong-form-routing.md`](./references/wrong-form-routing.md) — Every "do not use Form 843" case from the instructions with the correct form and sibling skill
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Fifteen failure patterns with fixes and authority
- [`filing.md`](./filing.md) — Channel decision tree, phone script, where to mail (including the special addresses in the instructions), signatures, consent and security rules, appeal

## Examples

- [`examples/fta-refund-paid-penalties.md`](./examples/fta-refund-paid-penalties.md) — Freelancer filed her 2023 return late, paid $1,604.50 of penalties, clean prior history; First Time Abate refund claim with the §6511 check
- [`examples/reasonable-cause-hospitalization.md`](./examples/reasonable-cause-hospitalization.md) — Sole proprietor hospitalized through the 2025 filing deadline, FTA already used in 2022; reasonable-cause abatement of the unpaid failure-to-file penalty only
- [`examples/interest-abatement-irs-delay.md`](./examples/interest-abatement-irs-delay.md) — Married couple whose approved audit transfer sat for 196 days; §6404(e)(1) interest refund estimated with daily compounding, filed under the 2-year-from-payment rule after the 3-year window closed

## Sources

Re-verify each year; the FTA/AEP page and IRM 20.1.1 changed in 2025–2026.

- [Form 843 (Rev. December 2024)](https://www.irs.gov/pub/irs-pdf/f843.pdf) and [Instructions for Form 843 (Rev. December 2024)](https://www.irs.gov/pub/irs-pdf/i843.pdf)
- [About Form 843](https://www.irs.gov/forms-pubs/about-form-843)
- [IRM 20.1.1, Introduction and Penalty Relief](https://www.irs.gov/irm/part20/irm_20-001-001r) (effective 11-25-2025)
- [Penalty relief due to First Time Abate or other administrative waiver](https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver) (AEP section)
- [Penalty relief for reasonable cause](https://www.irs.gov/payments/penalty-relief-for-reasonable-cause)
- [Penalty relief](https://www.irs.gov/payments/penalty-relief)
- [Interest abatement](https://www.irs.gov/payments/interest-abatement)
- [Penalty appeal](https://www.irs.gov/appeals/penalty-appeal); [Publication 5 (Rev. 4-2021)](https://www.irs.gov/pub/irs-pdf/p5.pdf)
- [Failure to file penalty](https://www.irs.gov/payments/failure-to-file-penalty); [Failure to pay penalty](https://www.irs.gov/payments/failure-to-pay-penalty)
- [Quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates)
- [Underpayment of estimated tax by individuals penalty](https://www.irs.gov/payments/underpayment-of-estimated-tax-by-individuals-penalty); [Instructions for Form 2210](https://www.irs.gov/pub/irs-pdf/i2210.pdf)
- IRC §6404 (abatements), §6511 (refund limits), §6513(a) (early returns), §6621(d) (net interest zero), §6622 (daily compounding), §6651 (failure to file or pay), §6656 (failure to deposit), §6665(a) (penalties treated as tax), §6698, §6699
- Treas. Reg. §301.6404-2 (ministerial and managerial acts), §301.6404-3 (erroneous written advice), §1.6664-4, §301.6724-1
- Rev. Proc. 2000-26 (net interest rate of zero)

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, the Internal Revenue Manual, and the Internal Revenue Code. It is not tax advice and does not create a CPA-client relationship. Remind the user that the IRS decides relief on its own records, that a "likely eligible" finding is not an approval, and that trust fund penalties, Tax Court interest reviews, and appeals with large balances warrant a licensed tax professional.
