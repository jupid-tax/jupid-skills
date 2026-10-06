---
name: form-8832
description: >
  Use this skill when an eligible entity (LLC, foreign business entity, or
  certain partnerships) wants to change its federal tax classification under
  the "check-the-box" regulations. Triggers on phrases like "Form 8832",
  "entity classification election", "check the box election", "elect C-corp
  for my LLC", "change LLC tax type", "make my LLC a corporation",
  "revert C-corp election", "60-month rule", "late entity classification
  election", "single-member LLC to C-corp", "QSBS election for LLC". Also
  engages when a user says they want to "tax my LLC as a corporation" without
  specifying S vs. C. Do NOT use when the user wants to elect S-corp ONLY
  (a timely Form 2553 is a deemed association election under Treas. Reg.
  §301.7701-3(c)(1)(v)(C), and the Form 8832 instructions say not to file
  Form 8832 for an entity electing S status — use form-2553). Do NOT use
  for state-level entity classification (separate state filings, varies by
  state). Do NOT use for foreign per-se corporations
  listed in 26 CFR §301.7701-2(b)(8) — those cannot elect down. Do NOT use
  for terminating an S-corp election (§1362(d) revocation or termination).
form: Form 8832 (Entity Classification Election)
audience: [llc1, llcm, scorp]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f8832.pdf
---

# Form 8832 — Entity Classification Election

This skill produces an audit-grade Form 8832 election package: confirmed eligibility under 26 CFR §301.7701-3, calculated effective date (75 days back / 12 months forward window), completed Part I, Part II late-relief request if applicable, shareholder/member consents, and a filing checklist for mailing to the correct IRS service center.

**Companion guide for end users:** [Form 8832 (Entity Classification Election) 2026: How LLCs Choose Their Tax Status](https://jupid.com/blog/form-8832-entity-classification-election-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

The judgment is concentrated in three places: (a) whether the entity is *eligible* to elect at all (foreign per-se corps cannot, IRS-recognized trusts cannot, and certain entities created by federal/state statute as corporations are excluded); (b) whether the **60-month limitation** in 26 CFR §301.7701-3(c)(1)(iv) blocks a re-election; and (c) whether the user actually needs Form 8832 at all — an LLC wanting S-corp files Form 2553 alone; a timely Form 2553 is a deemed association election under Treas. Reg. §301.7701-3(c)(1)(v)(C).

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 8832, "entity classification election", "check-the-box", or "CTB"
- The user has an LLC and wants to be taxed as a C-corporation (often for QSBS / §1202 strategy or to retain earnings at the 21% corporate rate)
- The user wants to revert a prior corporate election back to disregarded entity or partnership default
- The user is a foreign business entity owner asking how it will be taxed in the US
- The user mentions the "60-month rule" or asks "can I switch back"
- The user is filing both Form 8832 and Form 2553 together (combined C-corp + S-corp election)

Do **not** engage this skill when:

- The user only wants S-corp status for an LLC — use [`form-2553`](../form-2553/SKILL.md). Treas. Reg. §301.7701-3(c)(1)(v)(C) treats a timely Form 2553 as a deemed election to be classified as an association (Rev. Proc. 2013-30 §4.01(1) calls it a "Deemed Entity Classification Election"), and the Form 8832 instructions ("Who Must File") say not to file Form 8832 for an entity electing S status.
- The user already has an S-corp election and wants to terminate it — use IRC §1362(d) revocation procedures (Form 8869 is the QSub election, not a termination form)
- The user is asking about state-level entity classification (some states require a separate election; conformity varies)
- The entity is a foreign per-se corporation listed in 26 CFR §301.7701-2(b)(8) (e.g., German AG, UK PLC, French SA) — those are corporate by default and cannot elect down
- The entity was formed under state law as a corporation — no election needed; it is already a corporation. C-corp is the default; only Form 2553 is needed for S-corp.
- The user is filing Form 1120 (C-corp annual return) for an entity already classified — that's downstream

If the user's situation is ambiguous (e.g., "I have an LLC and want to save on taxes"), ask whether they want C-corp or S-corp treatment before proceeding. They are very different decisions with different consequences.

---

## Prerequisites

Before producing anything, the agent must have these inputs. **If any are missing, ask explicitly and stop until you get an answer.** Do not pick defaults — a wrong answer can void the election or trap the entity in the wrong classification for 60 months.

### Always required

1. **Entity legal name and EIN**. Used in Form 8832 Part I header. EIN is required to file Form 8832; if the entity does not have one, the user must obtain it first at [IRS.gov/EIN](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online). Do not invent.
2. **Entity type and formation jurisdiction**. Domestic (state of formation) or foreign (country of formation). Drives the eligibility test under 26 CFR §301.7701-3(a).
3. **Number of owners/members**. Single-member vs. multi-member determines the *default* classification and the *available* election targets per §301.7701-3(b).
4. **Current classification**. Default (disregarded / partnership / corporation) or previously elected (and when). Drives whether the 60-month limitation in §301.7701-3(c)(1)(iv) applies.
5. **Desired new classification**. Pick exactly one of:
   - Domestic eligible entity electing to be taxed as: (a) an association (i.e., C-corporation), (b) a partnership, or (c) a disregarded entity owned by a single owner
   - Foreign eligible entity electing to be taxed as: (a) an association, (b) a partnership, or (c) a disregarded entity
6. **Desired effective date** of the election. The election can be effective up to **75 days BEFORE** the filing date or up to **12 months AFTER** (Form 8832 Line 8 / instructions; Treas. Reg. §301.7701-3(c)(1)(iii)). If the user wants an earlier effective date, see Step 5 (Late Election Relief).
7. **Tax year of the entity** the election will affect.
8. **Owner / member list with signatures**. Each member who is an owner when the form is filed signs the Consent Statement (unnumbered, page 2 of the form), OR an officer, manager, or member authorized under local law or the organizational documents signs for the entity. If the effective date is before the filing date, each person who was an owner between the effective date and the filing date and is no longer an owner must also sign (Treas. Reg. §301.7701-3(c)(2); Form 8832 instructions, "Consent statement and signature(s)").

### Required if requesting late election relief (Part II)

If the desired effective date is more than 75 days before the filing date, the entity must request relief under Rev. Proc. 2009-41 (which superseded Rev. Proc. 2002-59) and complete Part II:

- **Reasonable cause statement** explaining why the election was not timely filed (Part II, Line 11)
- **Confirmation that the return test is met**: either the first return under the requested classification is not yet due, or all required returns for every affected year were filed consistent with the requested classification (a return filed within 6 months after its due date, excluding extensions, counts as timely) and no inconsistent returns were filed (Rev. Proc. 2009-41 §4.01(2)). A promise to amend later does not satisfy this test.
- **Confirmation the relief is requested within 3 years and 75 days of the requested effective date** (Rev. Proc. 2009-41 §4.01(4))

If the return test is met, file Part II under Rev. Proc. 2009-41. If inconsistent returns *have* been filed, the user generally needs a private letter ruling under Rev. Proc. 2026-1 (annually updated; verify the current PLR procedure for the year of filing) — out of scope for this skill; redirect to a tax attorney.

### Required if combined 8832 + 2553 election

If the user wants C-corp election then S-corp election (single-member LLC → C-corp → S-corp in one stroke):

- Confirm whether the C-corp period and the S-corp period start on the same date. If they do, skip Form 8832: the Form 8832 instructions ("Who Must File") say not to file Form 8832 for an entity electing S status, and a timely Form 2553 is a deemed association election (Treas. Reg. §301.7701-3(c)(1)(v)(C)). File Form 8832 only if the entity wants to be a C corporation for a period before the S election takes effect.
- Collect Form 2553 prerequisites — see [`form-2553`](../form-2553/SKILL.md) Prerequisites section

If the S election turns out to be invalid, the deemed association election does not apply (it requires that the entity qualify as a small business corporation under §1361(b) on the S effective date). Ask the user which path they want and surface this risk.

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Confirm eligibility

Walk the eligibility checklist in [`references/eligibility.md`](./references/eligibility.md). Block early if any of these are true:

- Entity is a foreign per-se corporation listed in 26 CFR §301.7701-2(b)(8)
- Entity is a state-law corporation (already corporate; no election available)
- Entity is a trust, estate, REIT, RIC, or other excluded type per §301.7701-3(a)
- The 60-month limitation in §301.7701-3(c)(1)(iv) blocks the re-election (entity changed classification within the last 60 months and no exception applies)

If blocked, stop and explain. Do not proceed to Part I.

### Step 2 — Determine the election target

Confirm the user's desired classification matches what's *available* given default rules:

- Domestic SMLLC: default = disregarded → can elect association (C-corp) only. Cannot elect "partnership" with one owner.
- Domestic multi-member LLC: default = partnership → can elect association (C-corp). Election to "partnership" is no-op (already default).
- Foreign eligible entity: default per §301.7701-3(b)(2) depends on liability status; can elect any of the three.
- Existing corporation that earlier elected to be disregarded/partnership: can elect back to corporation, but 60-month rule applies.

If the user picks a no-op election (e.g., already partnership, electing partnership), surface this and ask if they meant something else.

### Step 3 — Calculate the effective date and deadline

The effective date is whatever the user enters on Line 8, subject to:

- **Cannot be more than 75 days before** Form 8832 is filed (postmark date controls per IRC §7502)
- **Cannot be more than 12 months after** Form 8832 is filed
- If left blank, the effective date is the filing date
- A date entered more than 75 days back defaults to 75 days before the filing date; a date more than 12 months forward defaults to 12 months after the filing date (Treas. Reg. §301.7701-3(c)(1)(iii); Form 8832 Line 8 instructions)

Compute today's filing-date proxy and the earliest/latest valid effective dates. Surface both to the user. If the user wants an effective date outside this window:

- **Earlier than 75 days back** → Late Election Relief (Part II) under Rev. Proc. 2009-41
- **Later than 12 months forward** → the election would take effect 12 months after filing instead; the user must wait and file closer to the desired date

### Step 4 — Check the 60-month rule

26 CFR §301.7701-3(c)(1)(iv): once an eligible entity makes an election to change its classification, it cannot elect to change again during the 60 months following the effective date of the prior election.

Two exceptions:
- The IRS may permit an earlier change by private letter ruling if more than 50% of the ownership interests, as of the effective date of the new election, are owned by persons who owned no interest on the filing date or the effective date of the prior election (§301.7701-3(c)(1)(iv); Form 8832 instructions for lines 2a and 2b). This is not claimed on Form 8832 itself.
- An election by a newly formed entity effective on its date of formation is not a "change" and does not start the clock (Line 2b = Yes). An election by an entity that was operating under its default classification IS a change and starts the 60-month clock.

Walk [`references/sixty-month-rule.md`](./references/sixty-month-rule.md) if the user has a prior election.

### Step 5 — Late Election Relief (if needed)

If the desired effective date is more than 75 days before the filing date, complete Part II under Rev. Proc. 2009-41. Required:

- Filing within 3 years and 75 days of the requested effective date
- No inconsistent returns filed (or commitment to amend)
- Reasonable cause statement (genuine, not boilerplate)

Common reasonable causes that the IRS has accepted: filer reasonably relied on a tax professional who failed to file, filer was unaware of the election requirement, change in tax law or regulations, intervening illness/death. See [`references/late-relief.md`](./references/late-relief.md).

### Step 6 — Fill Part I header and Lines 1-10

Walk [`references/line-by-line.md`](./references/line-by-line.md). High-level rules in **Line-by-line guidance** below.

### Step 7 — Collect consents (Consent Statement, page 2)

Each member who is an owner when the form is filed must sign, plus (for a retroactive effective date) each former owner who held an interest between the effective date and the filing date. Alternatively, an officer, manager, or member authorized under local law or the organizational documents may sign for the entity and represents that authority under penalties of perjury (Treas. Reg. §301.7701-3(c)(2)). Default to collecting all owner signatures.

The Consent Statement has no line number; it sits below Line 10. Use the entity's operating agreement to confirm who the owners were on the filing date and since the effective date.

### Step 8 — Determine where to file

Form 8832 is filed by mail to the IRS service center for the entity's principal business, office, or agency. The Rev. December 2013 form is still the current revision as of 2026-10-06, but its printed "Where To File" table is out of date: the IRS inserted a "New Mailing Address" page at the front of the PDF and publishes the same list at [Where to file your taxes for Form 8832](https://www.irs.gov/filing/where-to-file-your-taxes-for-form-8832). Current addresses:

- **Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Vermont, Virginia, West Virginia, Wisconsin**: Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999
- **Alabama, Alaska, Arizona, Arkansas, California, Colorado, Florida, Hawaii, Idaho, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Mexico, North Dakota, Oklahoma, Oregon, South Dakota, Tennessee, Texas, Utah, Washington, Wyoming**: Department of the Treasury, Internal Revenue Service, Ogden, UT 84201
- **A foreign country or U.S. possession**: Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0023

**Verify these addresses against the first page of the current f8832.pdf and the IRS "Where to file" page before mailing.** Do not use the table printed inside the 2013 instructions (it still lists Cincinnati). Also attach a copy of Form 8832 to the entity's federal tax or information return for the year of the election (or, if the entity files none, to each direct or indirect owner's return), per Treas. Reg. §301.7701-3(c)(1)(ii). Do not sign that copy.

Form 8832 cannot be e-filed as a standalone. It is paper only.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next forms / returns the entity will need. Most common chains:

- **LLC → C-corp election (Form 8832 only)**: entity files Form 1120 each year going forward, owner reports W-2 + dividends
- **LLC → S-corp (Form 2553 alone when the corporate classification and the S election start on the same date; Form 8832 first only if a C-corp period comes before the S election)**: entity files Form 1120-S each year; see [`form-2553`](../form-2553/SKILL.md)
- **C-corp election → reverting to disregarded (Form 8832)**: entity files final Form 1120 for the short period ending on the effective date − 1; then sole proprietor files Schedule C going forward; see [`form-1120`](../../forms/form-1120/SKILL.md) (forthcoming) for the final-return mechanics

Also flag: **deemed liquidation** under 26 CFR §301.7701-3(g). When an entity changes from disregarded/partnership to corporate (or vice versa), the IRS treats the transition as if a deemed liquidation/contribution occurred. There can be unrecognized gain on appreciated assets, basis adjustments, and Section 351 considerations. Recommend a CPA review *before* filing — once filed, the deemed transactions are baked in.

### Step 12 — File the form (optional, if the user wants the agent to file)

If the agent has fax / mail-printing tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Mailing-channel decision tree (USPS Certified Mail vs. private-delivery service per IRC §7502)
- Cover-letter template for late-relief filings
- Field-by-field PDF mapping for the IRS fillable Form 8832
- IRS acknowledgment timing (typically 60 days; CP277 acceptance notice or CP278 rejection)

If the user only wants a draft and will mail it themselves, skip this step.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header

- **Name of eligible entity**: legal name on file with the state of formation (or country, for foreign entities)
- **Employer Identification Number (EIN)**: 9-digit, required. If the entity does not have one, obtain at IRS.gov before filing Form 8832.
- **Address**: principal business address. If different from the address on file with the IRS, also check Box "Address change" at top of form.

### Part I — Election Information

| Line | Field | What goes here |
|------|-------|----------------|
| — | Top-of-form boxes | Address change; "Late classification relief sought under Revenue Procedure 2009-41" (check when Part II is used); "Relief for a late change of entity classification election sought under Revenue Procedure 2010-32" (foreign entities only) |
| 1 | Type of election | Box 1a Initial classification by a newly-formed entity (skip 2a/2b) OR Box 1b Change in current classification (including a change from the default classification) |
| 2a | Has the eligible entity previously filed an entity election that had an effective date within the last 60 months? | Yes → go to 2b. No → skip 2b, go to line 3. |
| 2b | Was the prior election an initial classification election by a newly formed entity that was effective on the date of formation? | Yes → go to line 3 (the 60-month rule does not block). No → "Stop here"; the entity generally is not currently eligible |
| 3 | Does the eligible entity have more than one owner? | Yes (eligible to elect partnership or association; skip line 4) / No (eligible to elect disregarded or association; go to line 4) |
| 4a/4b | If only one owner: name and identifying number of owner | SSN, ITIN, or EIN; for tiered disregarded owners, the first owner up the chain that is not disregarded; "none" for a foreign owner with no U.S. number |
| 5a/5b | If owned by one or more affiliated corporations that file a consolidated return: name and EIN of the parent corporation | For consolidated-return groups only |
| 6 | Type of entity (check exactly one) | (a) domestic eligible electing association, (b) domestic eligible electing partnership, (c) domestic eligible with a single owner electing disregarded, (d) foreign eligible electing association, (e) foreign eligible electing partnership, (f) foreign eligible with a single owner electing disregarded |
| 7 | If created or organized in a foreign jurisdiction, foreign country of organization | Required even if the entity is also organized under domestic law |
| 8 | Election is to be effective beginning (month, day, year) | Must be within 75 days before / 12 months after filing date. If blank, effective date = filing date. |
| 9 | Name and title of contact person whom the IRS may call | Usually the filer or their tax pro |
| 10 | Contact person's telephone number | With area code |
| — | Consent Statement and Signature(s) (unnumbered, below line 10) | Each owner at the time of filing signs (plus former owners for a retroactive date); or an authorized officer, manager, or member signs for the entity |

### Part II — Late Election Relief (only if needed)

Used to claim relief under Rev. Proc. 2009-41 when the desired effective date is more than 75 days before the filing date.

| Line | Field | What goes here |
|------|-------|----------------|
| 11 | Explanation of why the election was not filed on time | Reasonable-cause statement: specific facts on why the election was not timely filed, the intent to be classified as elected from the desired effective date, and the reason for the delay. |
| — | Part II declaration and signature(s) | Pre-printed declaration under penalties of perjury that the elements of Rev. Proc. 2009-41 §4.01 are satisfied (this covers the consistent-returns condition). Signed by an authorized representative of the entity and each affected person. Part II has no line 12. |

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Eligibility checks

- [ ] Entity is not a foreign per-se corporation under §301.7701-2(b)(8)
- [ ] Entity is not a state-law corporation (those do not need to elect; default is C-corp)
- [ ] Entity has an EIN (or has applied for one — file 8832 only after EIN is issued)
- [ ] If Line 2a = Yes (prior election in last 60 months) and 2b = No (not first election after formation), 60-month rule blocks unless an exception applies — surface to user
- [ ] If Box 6 = "partnership" but Line 3 = No (single owner), classification target is invalid — single-owner cannot elect partnership

### Effective-date checks

- [ ] Line 8 is not more than 75 days before today's date (without Part II late relief)
- [ ] Line 8 is not more than 12 months after today's date
- [ ] If using Part II, the requested effective date is within 3 years and 75 days of today

### Consent checks

- [ ] Every owner at the time of filing has signed the Consent Statement (plus each former owner between a retroactive effective date and the filing date), OR
- [ ] An officer, manager, or member authorized under local law or the organizational documents has signed for the entity (keep the authority evidence in the file; the form does not require attaching it)

### Cross-form checks

- [ ] If the entity is also filing Form 2553 for the same effective date, Form 8832 should not be filed (Form 8832 instructions, "Who Must File"; Treas. Reg. §301.7701-3(c)(1)(v)(C))
- [ ] If the election creates a deemed liquidation under §301.7701-3(g), confirm the user understands the tax consequences (recommend CPA review)
- [ ] If reverting from corporate to disregarded, confirm the user knows Form 1120 short-period final return is required

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] User picks Box 6(b) — domestic LLC electing partnership when it's already a default partnership (no-op election)
- [ ] User picks Box 6(c) — disregarded when entity already has multiple members (would force them to dissolve to a single owner first)
- [ ] User electing C-corp without a stated reason — recommend CPA review of the choice before mailing (the skill does not advise on which classification is better)
- [ ] User has a prior C-corp election and is re-electing within 60 months — flag that the prior election starts the clock

---

## Output format

The agent's deliverable is a **filled draft** the user can mail. Format:

```markdown
# Form 8832 — DRAFT for [Entity Name]

## Filing summary
- Entity name: <name>
- EIN: <XX-XXXXXXX>
- Election type: <initial / change>
- Current classification: <disregarded / partnership / association>
- Elected classification: <association / partnership / disregarded>
- Effective date: MM/DD/YYYY
- Filing channel: Mail (USPS Certified) to <Kansas City | Ogden> service center
- Late relief requested: Yes (Rev. Proc. 2009-41) | No

## Header
Name of eligible entity: <legal name>
EIN: <XX-XXXXXXX>
Address: <street, city, state, ZIP>
Address change: ☐ check if different from prior IRS records

## Part I — Election Information
1. Type of election:                      ☐ (a) Initial  ☐ (b) Change
2a. Prior election within last 60 months: ☐ Yes  ☐ No
2b. Was prior election the first?         ☐ Yes  ☐ No  ☐ N/A
3. More than one owner:                   ☐ Yes  ☐ No
4. (If only one owner)
   4a Name: <name>
   4b Identifying number: <SSN, ITIN, or EIN; "none" for a foreign owner without one>
5. (If owned by members of an affiliated group filing a consolidated return)
   5a Parent corporation name: <name>
   5b Parent EIN: <XX-XXXXXXX>
6. Type of entity (check ONE):
   ☐ (a) Domestic eligible — elect association (C-corp)
   ☐ (b) Domestic eligible — elect partnership
   ☐ (c) Domestic eligible — elect disregarded
   ☐ (d) Foreign eligible — elect association
   ☐ (e) Foreign eligible — elect partnership
   ☐ (f) Foreign eligible — elect disregarded
7. (If foreign) Country of organization: <country>
8. Election effective date: MM/DD/YYYY
9. Contact person: <name>
   Title: <title>
10. Contact phone: <XXX-XXX-XXXX>
Consent Statement and Signature(s) (unnumbered)
    [Each owner at the time of filing signs and dates here (plus former owners
    for a retroactive date), OR an authorized officer/manager/member signs for
    the entity. Print name, title, and date next to each signature.]

## Part II — Late Election Relief (only if applicable)
Top-of-form box "Late classification relief sought under Revenue Procedure 2009-41": ☒
11. Explanation: <reasonable-cause statement>
Part II declaration: signed by an authorized representative and each affected person

## Required attachments
- [ ] Consent Statement signatures — all collected
- [ ] If Part II: Line 11 explanation (continuation sheet if needed)
- [ ] If Part II: Part II declaration signed by the entity and each affected person
- [ ] If officer/manager signing: evidence of authority kept in the file (not required to be attached)

## Validation summary
- Eligibility: <pass / fail with reason>
- Effective-date window: <pass / fail>
- 60-month rule: <pass / blocked / not applicable>
- Consents: <complete / incomplete>
- Sanity: <list warnings raised>

## Filing instructions
Mail to: <Kansas City, MO 64999 | Ogden, UT 84201 | Ogden, UT 84201-0023 (foreign country or U.S. possession)>
Copy: attach an unsigned copy to the entity's federal return for the election year
Method: USPS Certified Mail with Return Receipt (IRC §7502 timely-mailing rule)
Postmark deadline: <today + 0; the form has no statutory deadline, but the desired
                    effective date constrains how late it can be filed>

Expected IRS acknowledgment: generally within 60 days (CP277 acceptance or CP278 denial).
If nothing arrives within 60 days, call 1-800-829-0115 (number in the Form 8832
instructions) or write to the service center by certified mail.

## Next steps after IRS acceptance
- <File Form 1120 going forward (if elected C-corp)>
- <File Form 1120-S going forward (if combined with Form 2553)>
- <File final Form 1120 short-period return (if reverting from C-corp)>
- <Run §301.7701-3(g) deemed-liquidation analysis with a CPA>

## Sources cited in this draft
- IRS Form 8832 (Rev. December 2013, current as of 2026-10-06; mailing addresses per the IRS update page)
- 26 CFR §301.7701-1, §301.7701-2, §301.7701-3 (entity classification regulations)
- IRC §7701(a)(3) (definition of corporation)
- Rev. Proc. 2009-41 (late entity classification election relief)
- Treas. Reg. §301.7701-3(c)(1)(v)(C) (timely Form 2553 is a deemed association election); Rev. Proc. 2013-30 §5.03 (late combined classification + S relief)
- 26 CFR §301.7701-3(g) (deemed transactions on classification change)
- 26 CFR §301.7701-3(c)(1)(iv) (60-month limitation)
- 26 CFR §301.7701-2(b)(8) (foreign per-se corporations list)
```

The draft is **not** the final filed form. The user (or agent under filing authority) still has to print Form 8832 from the IRS PDF, transcribe the values, collect ink signatures, and mail. The deliverable's value is that every field is populated and every eligibility/timing rule has been checked.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Form 8832 with examples and edge cases
- [`references/eligibility.md`](./references/eligibility.md) — who can and cannot elect; per-se corporation list; trust/REIT/RIC exclusions
- [`references/sixty-month-rule.md`](./references/sixty-month-rule.md) — 26 CFR §301.7701-3(c)(1)(iv) blocking rule, exceptions, and 50%-ownership-change waiver
- [`references/late-relief.md`](./references/late-relief.md) — Rev. Proc. 2009-41 step-by-step and reasonable-cause language patterns
- [`references/common-mistakes.md`](./references/common-mistakes.md) — top filer mistakes with citations and audit-defense fixes
- [`filing.md`](./filing.md) — mailing playbook for fax/USPS, cover-letter templates, and IRS acknowledgment timing

## Examples

End-to-end worked Form 8832 elections.

- [`examples/smllc-to-c-corp-qsbs.md`](./examples/smllc-to-c-corp-qsbs.md) — single-member LLC electing C-corp for QSBS / §1202 strategy
- [`examples/foreign-llc-disregarded.md`](./examples/foreign-llc-disregarded.md) — foreign eligible entity electing disregarded for US tax purposes
- [`examples/c-corp-revert-blocked.md`](./examples/c-corp-revert-blocked.md) — entity wanting to revert C-corp election but blocked by 60-month rule

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the year of filing.

- [Form 8832 (Rev. December 2013)](https://www.irs.gov/pub/irs-pdf/f8832.pdf) — the form itself; PDF page 1 is the IRS "New Mailing Address" update, the form is PDF pages 2-4 (form pages 1-3), and the instructions are PDF pages 5-8 (form pages 4-7). No separate i8832 instructions PDF exists
- [Where to file your taxes for Form 8832](https://www.irs.gov/filing/where-to-file-your-taxes-for-form-8832) — current mailing addresses
- [About Form 8832](https://www.irs.gov/forms-pubs/about-form-8832) — IRS landing page with revision history
- 26 CFR §301.7701-1 (definitions); §301.7701-2 (business entities); §301.7701-3 (classification of certain business entities)
- 26 CFR §301.7701-3(c)(1)(iv) — 60-month limitation
- 26 CFR §301.7701-3(g) — deemed-transaction treatment on classification change
- 26 CFR §301.7701-2(b)(8) — list of foreign per-se corporations
- IRC §7701(a)(2)–(3) — partnership and corporation definitions
- IRC §1361–1379 — Subchapter S (relevant for combined 8832 + 2553 elections)
- IRC §1202 — QSBS (relevant for SMLLC-to-C-corp QSBS strategy)
- [Rev. Proc. 2009-41](https://www.irs.gov/pub/irs-drop/rp-09-41.pdf) — late entity classification election relief (3 years + 75 days; reasonable cause)
- [Rev. Proc. 2013-30](https://www.irs.gov/pub/irs-drop/rp-13-30.pdf) — late S election relief, including a late classification election intended to take effect with the S election (§5.03); §4.01(1) defines the "Deemed Entity Classification Election" under Treas. Reg. §301.7701-3(c)(1)(v)(C)
- Rev. Proc. 2026-1 (Internal Revenue Bulletin 2026-1) — private letter ruling procedures and user fees (Appendix A); re-check the current year's Rev. Proc. 20XX-1
- [Form 2553 (S-corp election)](https://www.irs.gov/pub/irs-pdf/f2553.pdf) — companion form for combined elections
- [Form 1120 (C-corp annual return)](https://www.irs.gov/pub/irs-pdf/f1120.pdf) — downstream return after C-corp election
- IRS CP277 (election accepted; [Understanding your CP277 notice](https://www.irs.gov/individuals/understanding-your-cp277-notice)) / CP278 (denial of Form 8832; IRS Document 6209, Section 9)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and regulations. It is not tax advice. It does not establish a CPA-client relationship. Entity classification elections have permanent consequences (deemed liquidations, basis resets, 60-month lockouts) — the agent invoking this skill should remind the user that Form 8832 outputs warrant a licensed tax professional's review before mailing, especially when the entity holds appreciated assets or has multiple owners.
