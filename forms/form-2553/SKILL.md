---
name: form-2553
description: >
  Use this skill when an LLC owner, corporation, or small-business founder wants
  to elect S-corporation tax status. Triggers on phrases like "elect S-corp",
  "file Form 2553", "S-corp election deadline", "make S-corp election for my LLC",
  "should my LLC be an S-corp", "late S-corp election", "Rev. Proc. 2013-30",
  "missed S-corp deadline", "convert LLC to S-corp". Also engages when the user
  asks "is S-corp worth it for me" and provides profit figures. Do NOT use for
  revoking or terminating an existing S-corp election (revocation statement
  under IRC §1362(d) and Reg. §1.1362-6(a)(3); Form 8869 is the QSub election), changing
  the tax year of an already-elected S-corp (Form 1128), or filing the annual
  return for an entity that already elected S-corp (use form-1120-s). Do NOT use
  for entity formation itself — that's a state filing, not federal.
form: Form 2553 (Election by a Small Business Corporation)
audience: [scorp, llc1, llcm]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f2553.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2553.pdf
---

# Form 2553 — Election by a Small Business Corporation

This skill produces an audit-grade Form 2553 election package: confirmed eligibility, calculated deadline, completed Part I (entity info + shareholder consents), Part II / III / IV as needed, and a filing checklist for fax or mail submission to the IRS service center.

The math is mostly date arithmetic and a yes/no eligibility checklist. The judgment is in (a) whether the user actually wants to elect — there's a real break-even threshold below which it's not worth the compliance overhead — and (b) catching late filings early so the user can use Rev. Proc. 2013-30 relief instead of losing a year.

**Form revision:** the line map in this skill was verified on 2026-10-06 against Form 2553 (Rev. December 2017) and the Instructions for Form 2553 (Rev. December 2020), which are still the current revisions. The election is not annual, so there is no 2025 or 2026 edition. Before each use, check https://www.irs.gov/forms-pubs/about-form-2553 for a newer revision; a new revision can re-letter the items.

**Companion guide for end users:** [Form 2553 + AI Agent Skill: S-Corp Election Guide 2026](https://jupid.com/blog/form-2553-s-corp-election-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2553, "S-corp election", "elect S-corp", or "Subchapter S"
- The user has formed (or is forming) an LLC or corporation and asks about tax structure choice
- The user is a sole proprietor / single-member LLC owner with profit ≥$40K asking about SE tax savings
- The user mentions missing a deadline and asks about late S-corp election or Rev. Proc. 2013-30
- The user describes wanting to "be paid as W-2 from my own company"

Do **not** engage this skill when:

- The user already has an S-corp and is filing the annual return → use [`form-1120-s`](../form-1120-s/SKILL.md)
- The user wants to **revoke** an existing S-corp election → a revocation statement with consent of shareholders holding more than half the shares, filed with the Form 2553 service center (IRC §1362(d)(1); Reg. §1.1362-6(a)(3); Form 1120-S instructions, "Termination of Election"), not Form 2553. Form 8869 is the QSub election and does not revoke anything
- The user wants to change the tax year of an existing S-corp → Form 1128
- The user is a multi-member LLC that does NOT want to elect S-corp → file Form 1065 (partnership return); use [`form-1065`](../form-1065/SKILL.md)
- The user is asking about C-corp election → that's the default for any corporation; no election needed (use Form 1120)
- The user wants entity *formation* (Articles of Organization, etc.) → that's a state filing; redirect to the secretary-of-state filing process

If the user's situation is ambiguous (e.g., "I formed an LLC but I don't know what type of taxation I'm under"), ask before proceeding. Default LLC taxation is sole prop (single-member) or partnership (multi-member). S-corp requires an affirmative election via this form.

---

## Prerequisites

Before producing anything, the agent must have these inputs. **If any are missing, ask explicitly and stop until you get an answer.** Do not pick defaults for these — wrong answers void the election or trigger a year of incorrect tax returns.

### Always required

1. **Tax year** the election is to take effect (2025, 2026, etc.)
2. **Entity name** — exactly as registered with the state and on IRS records
3. **Entity type** — corporation (Inc., Corp.) or LLC. If LLC, confirm whether Form 8832 has been filed; if not, a timely Form 2553 alone also makes the entity a corporation (deemed classification election, Reg. §301.7701-3(c)(1)(v)(C); Form 2553 instructions, "Purpose of Form"). A late Form 2553 from an LLC needs the Part IV representations as well
4. **Date of formation** — date articles of incorporation/organization were accepted by the state
5. **State of formation**
6. **EIN** — if the entity doesn't have one, ASK the user to apply at IRS.gov/EIN before proceeding. If the EIN has been applied for but not received by the time the election is due, the instructions allow "Applied For" plus the application date in item A (Instructions for Form 2553, "Item A")
7. **Date entity began doing business** OR **date shareholders first owned stock** OR **date entity acquired assets** — whichever was earliest. Used to compute the deadline for new entities.
8. **Desired effective date of election** (item E)
9. **Tax year choice** — calendar year (default; almost always the right answer for small entities) or fiscal year (Part II required if non-calendar)
10. **Complete shareholder list**: each shareholder's full legal name, address, SSN/ITIN/EIN, number of shares (or LLC ownership %), date acquired, and whether they consent
11. **For shareholders in community-property states (AZ, CA, ID, LA, NV, NM, TX, WA, WI)**: name of the spouse who holds a community interest and confirmation that they will sign the consent in column K (Reg. §1.1362-6(b)(2)(i))

### Required if filing late (Rev. Proc. 2013-30)

12. **Reasonable cause statement** — why was the election filed late, and what did the entity do once it found out? Rev. Proc. 2013-30 §4.03(1) requires both the reasonable cause and the diligent actions to correct the mistake; the statement goes on line I or an attachment and carries the penalties-of-perjury declaration (§4.03(3)). The agent helps the user state the facts in 2-4 sentences. "We wanted to wait and see how the year went" is not reasonable cause
13. **Returns already filed since the intended effective date** — ASK for every federal return and information return filed for the entity (or, for a single-member LLC, the owner's Schedule C) for each year from the intended effective date. For an LLC that needs the deemed classification election (no timely Form 8832), Part IV representation 5 requires either (a) all required returns timely filed consistent with S status and no inconsistent returns, or (b) no return filed for the first year because its due date has not passed (Rev. Proc. 2013-30 §5.03(5)). If a Schedule C or Form 1065 was already filed for an intended S year, or the first year's Form 1120-S due date passed with no return filed, representation 5 cannot be made as written: stop and refer the user to a CPA (a letter ruling may be the only route). A corporation (not an LLC) instead needs every shareholder's statement that they reported consistently with S status (§5.02)

### Optional but strongly recommended

14. **Reasonable salary analysis** — what salary will the shareholder-employee be paid? The agent should ask for the user's industry, role, geographic market, and hours worked, then point to BLS OES (Occupational Employment Statistics) data for the right NAICS code. **Do NOT pick a default salary** — under-salary triggers IRS reclassification (*David E. Watson, P.C. v. United States*, 668 F.3d 1008 (8th Cir. 2012)). This is a "ask, don't guess" point.
15. **Profit projection for the election year** — if not provided, ask. Used to calculate break-even (whether the election is worth the compliance overhead) and to validate that the proposed reasonable salary is plausible.

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Confirm eligibility

Walk through the IRC §1361(b) eligibility checklist with the user. Surface failures immediately — there is no point completing the form if the entity is ineligible.

```
Eligibility checklist (all must be YES):
□ Domestic corporation OR domestic LLC (formed under U.S. state law)
□ Not a bank using the reserve method, insurance company under Subchapter L,
  IRC §936 possessions corporation, or DISC
□ ≤100 shareholders (spouses count as one; six-generation family election available)
□ All shareholders are individuals (U.S. citizens or resident aliens),
  qualifying trusts, estates, or qualifying tax-exempt orgs
□ No shareholders are: C-corps, partnerships, multi-member LLCs,
  non-resident aliens, most foreign trusts, or IRAs
□ One class of stock (voting/non-voting OK; no preferred, no debt-recharacterized-as-stock)
```

For LLCs: check the operating agreement for waterfall distributions, preferred returns, or other clauses that violate the one-class-of-stock rule. If found, the operating agreement must be amended to pro-rata economic rights before filing 2553.

### Step 2 — Compute the deadline

Use [`references/timing-rules.md`](./references/timing-rules.md). Decision tree:

```
Is the election meant to start with the entity's FIRST tax year in existence?

NO → Existing-entity case.
  Window = any time during the preceding tax year, or no later than
  2 months 15 days after the start of the tax year the election is for.
  Calendar-year entity → March 15 of the intended year.
  Fiscal-year entity → 2 months 15 days from start of fiscal year.

YES → New-entity case.
  The first tax year starts on the EARLIEST of:
    (a) date entity first had shareholders/members
    (b) date entity first had assets
    (c) date entity began doing business
  Deadline = 2 months 15 days after that date. An election filed before
  that date is not valid (no prior tax year).
```

Date arithmetic (instructions, "When To Make the Election"): the 2-month period ends the day before the numerically corresponding day of the second following month; then add 15 days. January 7 → March 21; January 1 → March 15; March 1 → May 15. If the last day is a Saturday, Sunday, or legal holiday, IRC §7503 moves it to the next business day (March 15, 2026 is a Sunday, so a calendar-2026 election was due March 16, 2026).

State the computed deadline back to the user explicitly. Compare with today's date:

- **Today is on or before the deadline** → timely election, no late-relief statements
- **Today is after the deadline but within 3 years 75 days of the item E date** → late election under Rev. Proc. 2013-30: header, line I reasonable-cause statement, all-period shareholder consents, and Part IV if the entity is an LLC relying on the deemed classification election (Step 6)
- **Today is more than 3 years 75 days after the item E date** → Rev. Proc. 2013-30 is unavailable, except for a corporation that filed every return as an S corporation (§5.04 conditions; instructions, requirement 6). Otherwise the route is a letter ruling under §1362(b)(5) (Rev. Proc. 2026-1, Appendix A: $14,500 user fee, reduced to $3,450 or $9,775 for gross income under $400,000 or $10 million). Beyond this skill's scope; redirect to a CPA

### Step 3 — Run the break-even check (advisory)

If the user hasn't yet committed to the election, surface the economic case:

```
Estimated annual SE tax savings ≈ (Net profit − reasonable salary) × 0.9235 × 15.3%
  [12.4% part only up to the SS wage base: $176,100 for 2025, $184,500 for 2026,
   https://www.ssa.gov/oact/cola/cbb.html]

Overhead figures below are rough market estimates, not IRS numbers.
Ask the user for actual quotes before relying on them.

Estimated annual compliance overhead:
  Payroll software:        $400-$800
  State unemployment tax:  $100-$700 (varies by state and wage base)
  Bookkeeping increment:   $1,000-$2,000
  Form 1120-S preparation: $800-$2,000

Break-even: net profit roughly $40,000-$60,000 depending on state.
```

If projected net profit is below $40K and the user hasn't yet made the election, ASK whether they still want to proceed. Don't decide for them — but make the trade-off visible. If above $80K, the math is decisively in favor.

### Step 4 — Collect shareholder consent data

Build the shareholder consent table:

```
| # | Name | Address | SSN/ITIN | Shares (or LLC %) | Date acquired | Spouse consent? |
|---|------|---------|----------|-------------------|---------------|-----------------|
| 1 | ...  | ...     | ...      | ...               | ...           | ...             |
```

For each shareholder, confirm they will sign and date in column K. For community-property states, confirm the spouse with a community interest will also sign (Reg. §1.1362-6(b)(2)(i)).

Who must consent depends on timing (instructions, "Column K"): if the election is filed before the item E date, only shareholders who own stock on the day the election is made; if filed on or after the item E date (including every late election), every shareholder or former shareholder who owned stock at any time from the item E date to the filing date. Former shareholders enter -0- shares in column L.

If any shareholder is in an ineligible category (C-corp, non-resident alien, partnership, multi-member LLC), STOP — entity is ineligible.

### Step 5 — Determine tax year (Part II?)

Default: calendar year (item F, box (1)). For small entities, this is almost always correct.

If the user wants a fiscal year, ask why. Acceptable reasons:
- Natural business year (≥25% of gross receipts in last 2 months for last 3 years; Rev. Proc. 2006-46)
- Ownership tax year (matching majority shareholders)
- Documented business purpose
- §444 election (required-payment buy-in)

Complete Part II only if item F box (2) or (4) is checked (box (3), a 52-53-week year ending with reference to December, does not need Part II). A business-purpose request (box Q1) carries a user fee of $5,750 under Rev. Proc. 2026-1, Appendix A (A)(3)(a)(ii) (reduced to $3,450 for gross income under $400,000); the IRS bills it later, do not send it with the form. Most small filers should not use Part II.

### Step 6 — Late election package (Rev. Proc. 2013-30)

If Step 2 identified a late election, the package is (Rev. Proc. 2013-30 §§4.03, 5.01-5.03; Instructions for Form 2553, "Relief for Late Elections"):

1. Write "FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1
2. Line I: explain the reasonable cause for the late filing and the diligent actions taken once the mistake was found (or attach a statement with the penalties-of-perjury declaration from §4.03(3)), signed by the officer
3. Column K: consents from everyone who was a shareholder at any time from the item E date to the filing date; their signature also declares they reported income consistently with S status for every affected year (§5.02)
4. Part IV: required only when the entity is an eligible entity (typically an LLC) that also missed the corporate classification election, i.e. it has no timely Form 8832 and relies on Form 2553 for the deemed classification. Part IV has five representations (1, 2, 3, 4, and 5a or 5b); none are optional, and 5a/5b must be true (see Prerequisite 13)
5. If the form is attached to a Form 1120-S, write "INCLUDES LATE ELECTION(S) FILED PURSUANT TO REV. PROC. 2013-30" at the top of the 1120-S page 1

A corporation (Inc./Corp.) filing late does not complete Part IV; lines 1-4 above are the whole package.

### Step 7 — Determine if Part III needed (QSST)

Only needed if a Qualified Subchapter S Trust is among the shareholders. Most LLCs and small corporations have no trust shareholders. If applicable, see Form 2553 instructions page 5 for QSST election content; Part III can be used only if the stock was transferred to the trust on or before the date the S election is made, and Form 2553 cannot be filed with only Part III completed. Otherwise skip.

### Step 8 — Run validation checks

See **Validation** below. Run every check.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off to filing

If the user authorizes the agent to file, follow [`filing.md`](./filing.md). Otherwise, produce the printable PDF and instruct the user to fax or mail per [`filing.md`](./filing.md), plus inform them of state-level S-corp election requirements (see [`references/state-conformity.md`](./references/state-conformity.md)).

### Step 11 — Set follow-up reminders

- 60 days from filing: check for the CP261 acceptance notice; if neither acceptance nor nonacceptance has arrived within 2 months (5 months if box Q1 was checked), call 800-829-4933 (Instructions for Form 2553, "Where To File")
- 30 days from acknowledgment: confirm payroll provider is set up
- Quarterly: Form 941 deadlines (Apr 30, Jul 31, Oct 31, Jan 31)
- Annual: Form 940 (Jan 31), W-2 (Jan 31), Form 1120-S (Mar 15), state returns

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Election Information (page 1)

Item letters below are from Form 2553 (Rev. December 2017). The name and address lines carry no letter.

- **Name** — the true name from the charter or other formation document, matching the EIN record; enter "C/O" and a person's name if the mailing address is someone else's
- **Address** — number, street, suite; a P.O. box only if the Post Office does not deliver to the street address
- **A. Employer identification number** — required; "Applied For" plus the application date is allowed if the EIN has not arrived by the due date
- **B. Date incorporated** — the date the state accepted the formation filing
- **C. State of incorporation** — state (or country) of formation
- **D. Name or address changed** — check if the entity changed its name or address after applying for the EIN
- **E. Effective date of election** — the SINGLE most important field. A new entity enters the earliest of first shareholders, first assets, or start of business; an existing entity enters the first day of the tax year the election is for. Drives the 2-month-15-day deadline
- **F. Selected tax year** — check exactly one: (1) calendar year; (2) fiscal year ending (month and day); (3) 52-53-week year ending with reference to December; (4) 52-53-week year ending with reference to another month. Box (2) or (4) requires Part II
- **G. More than 100 shareholders** — check only if column J lists more than 100 and treating family members as one shareholder brings the count to 100 or fewer
- **H. Contact** — name and title of the officer or legal representative the IRS may call, and telephone number
- **I. Late election explanation** — blank for a timely election; for a late election, the reasonable cause and diligent actions (Step 6)
- **Signature** — officer signature, title, date below item I. Officers listed in the instructions: president, vice president, treasurer, assistant treasurer, chief accounting officer, or another officer authorized to sign. An unsigned Form 2553 is not timely filed

### Shareholder consent (page 2, columns J-N)

For each shareholder or former shareholder required to consent:
- **J. Name and address** — for a disregarded single-member LLC shareholder, the owner's name and address; for a nominee, guardian, custodian, or agent, the person for whom the stock is held
- **K. Shareholder's consent statement** — signature and date. Use handwritten signatures: Form 2553 is not on the IRS list of forms that accept electronic or digital signatures (IRM 10.10.1, Exhibit 10.10.1-2)
- **L. Stock owned or percentage of ownership** — number of shares (or percentage for an entity without stock, such as an LLC) and date(s) acquired; -0- for former shareholders
- **M. Social security number or EIN** — SSN for individuals; EIN for an estate, qualified trust, or exempt organization
- **N. Shareholder's tax year ends** — month and day (12/31 for most individuals)

Each spouse with a community interest in the stock signs column K (Reg. §1.1362-6(b)(2)(i)). A continuation sheet or separate consent statement must carry the entity's name, address, EIN, and columns J-N.

### Part II — Selection of Fiscal Tax Year (page 3)

Skip unless item F box (2) or (4) is checked. Item O (new / existing retaining / existing changing) plus one of: P1 natural business year or P2 ownership tax year (Rev. Proc. 2006-46 automatic approval), Q1 business purpose (Rev. Proc. 2002-39; user fee) with optional Q2 back-up §444 election and Q3 calendar-year fallback, or R1 §444 election (Form 8716) with optional R2 fallback. Most small filers leave this blank.

### Part III — Qualified Subchapter S Trust (QSST) Election (page 4)

Only if a QSST is a shareholder and the stock was transferred to the trust on or before the date the S election is made. The income beneficiary (or legal representative) makes the §1361(d)(2) election here; the deemed owner of the QSST must also consent in column K.

### Part IV — Late Corporate Classification Election Representations (page 4)

Only for a late election by an eligible entity (typically an LLC) whose corporate classification election is also late. Five representations, all required: (1) eligible entity under Reg. §301.7701-3(a); (2) intended corporate classification as of the S effective date; (3) fails to be a corporation solely because Form 8832 was not timely filed or deemed filed; (4) fails to be an S corporation solely because Form 2553 was late; (5a) all required returns timely filed consistent with S status and no inconsistent returns, or (5b) no return filed for the first year because its due date has not passed. A corporation filing late leaves Part IV blank.

---

## Validation

Run all checks before declaring ready.

### Eligibility checks

- [ ] Entity is a domestic corp or LLC formed under U.S. state law
- [ ] All shareholders are eligible (no C-corps, no partnerships, no multi-member LLCs, no non-resident aliens, no IRAs)
- [ ] Shareholder count ≤100 (with spouses/family aggregations)
- [ ] One class of stock confirmed (operating agreement reviewed for LLCs)
- [ ] EIN obtained and matches IRS records
- [ ] Entity is not in an ineligible class (bank reserve method, insurance, possessions, DISC)

### Date checks

- [ ] For a new entity, item E equals the earliest of first shareholders, first assets, or start of business, and is not before item B
- [ ] Election effective date is the start of a tax year (e.g., Jan 1 for calendar year filers continuing from prior year)
- [ ] Today's date is computed against the deadline; on-time vs late status surfaced
- [ ] If late, today is within 3 years 75 days of effective date (Rev. Proc. 2013-30 window)

### Shareholder consent checks

- [ ] Every shareholder named on the form
- [ ] Every required shareholder (and former shareholder, for a late or retroactive election) has signed and dated column K, by hand
- [ ] Every shareholder has an SSN/ITIN/EIN in column M and a tax year end in column N
- [ ] Current ownership in column L sums to 100% (or to total issued shares); former shareholders show -0-
- [ ] In community-property states, each spouse with a community interest has signed

### Form completeness checks

- [ ] Name, address, and items A-F and H completed; G checked only if the family-aggregation test applies
- [ ] Item F has exactly one box checked
- [ ] If item F box (2) or (4), Part II is completed (box (3) does not need it)
- [ ] If late: header written, item I explanation (or signed statement) present, and Part IV completed only if the entity is an LLC/eligible entity relying on the deemed classification election
- [ ] Officer signature, title, and date present below item I
- [ ] If QSST shareholder, Part III is completed for that trust

### Sanity warnings (do not block)

- [ ] Effective date is more than 1 year in the past → unusual; verify the user wants this
- [ ] Reasonable salary projected to be <30% of net profit → flag risk of IRS reclassification (*David E. Watson, P.C. v. United States*). The 30% trigger is a heuristic, not an IRS threshold
- [ ] Reasonable salary projected to be >100% of net profit → mathematically impossible to draw distributions; question whether election makes sense
- [ ] Single shareholder is a non-resident alien → ineligible; STOP
- [ ] Operating agreement contains "preferred return" or "waterfall" language → potential one-class-of-stock violation; require operating agreement review

### Cross-form checks

- [ ] User informed about Form 1120-S annual filing requirement
- [ ] User informed about Form 941 quarterly payroll filings
- [ ] User informed about Form 940 annual FUTA
- [ ] User informed about W-2 issuance to shareholder-employee
- [ ] User informed about state-level S-corp election (if state requires separate)
- [ ] User has chosen a payroll provider before the election effective date

---

## Output format

The agent's deliverable is a filled draft + filing instructions:

```markdown
# Form 2553 — DRAFT Election by a Small Business Corporation

## Header (top margin of page 1)
FILED PURSUANT TO REV. PROC. 2013-30  [only if late]

## Part I — Election Information (Form 2553, Rev. December 2017)

Name:                                  <name exactly as on EIN record>
Address:                               <street, suite, city, state, ZIP>
A. Employer identification number:     <EIN or "Applied For MM/DD/YYYY">
B. Date incorporated:                  MM/DD/YYYY
C. State of incorporation:             <state>
D. Name/address changed after EIN:     [ ] name  [ ] address
E. Election effective for tax year
   beginning:                          MM/DD/YYYY
F. Selected tax year:
   [X] (1) Calendar year
   [ ] (2) Fiscal year ending MM/DD           (Part II required)
   [ ] (3) 52-53-week year, December
   [ ] (4) 52-53-week year, month: ___        (Part II required)
G. >100 shareholders, family test:     [ ] (blank unless applicable)
H. Contact name and title:             <name, title>   Phone: <number>
I. Late election explanation:          <blank if timely | reasonable cause +
                                        diligent actions, or "See attached statement">
Signature of officer: <name>   Title: <title>   Date: MM/DD/YYYY

## Page 2 — Shareholders' consents (columns J-N)

| # | J. Name & address | K. Signature / date | L. Shares or % / date(s) acquired | M. SSN or EIN | N. Tax year ends |
|---|-------------------|---------------------|-----------------------------------|---------------|------------------|
| 1 | ...               | ... / MM/DD/YYYY    | ...                               | XXX-XX-1234   | 12/31            |

(Add rows for spouses with a community interest and, for late or retroactive
elections, for former shareholders with -0- shares.)

## Part II — Selection of Fiscal Tax Year (only if F box 2 or 4)

O: <1 new | 2 existing retaining | 3 existing changing>
P / Q / R: <P1 natural business year | P2 ownership tax year | Q1 business purpose
            (+Q2/Q3) | R1 §444 election with Form 8716 (+R2)>
Attachments: <47-month gross receipts schedule | business-purpose statement | Form 8716>

## Part III — QSST Election (if applicable)

Income beneficiary name, address, SSN: <...>
Trust name, address, EIN: <...>
Date stock transferred to trust: MM/DD/YYYY
Signature of income beneficiary or legal representative, date

## Part IV — Late Corporate Classification Election Representations
## (only an eligible entity/LLC filing late without a timely Form 8832)

Representations 1-4 apply; 5: [ ] 5a returns timely filed consistent with S status
                              [ ] 5b first-year return not yet due

## Filing instructions

- Service center: <Kansas City, MO 64999 / fax 855-887-7734 | Ogden, UT 84201 / fax 855-214-7520>
  (state split on Instructions for Form 2553 page 3 and
   https://www.irs.gov/filing/where-to-file-your-taxes-for-form-2553)
- Method: fax OR mail (certified or registered mail receipt is on the instructions' list of acceptable proof of filing)
- Filing date: MM/DD/YYYY
- Expected response: CP261 acceptance notice, generally within 60 days (CP264 = election denied)
- If nothing within 2 months (5 if Q1 checked): call 800-829-4933

## Required follow-up filings

- [ ] State-level S-corp election (see references/state-conformity.md)
- [ ] Set up payroll provider before election effective date
- [ ] Form 941 quarterly (Apr 30, Jul 31, Oct 31, Jan 31)
- [ ] Form 940 annual (Jan 31)
- [ ] W-2 to shareholder-employee (Jan 31)
- [ ] Form 1120-S annual (March 15, or Sep 15 with extension)

## Validation summary

- Eligibility: <pass | list failures>
- Timing: on-time | late under Rev. Proc. 2013-30 | beyond 3-year 75-day window
- Consents: <N of N collected>
- Math: <pass | list issues>
- Sanity warnings: <list>

## Sources cited in this draft

- IRS Form 2553 (Rev. December 2017)
- IRS Instructions for Form 2553 (Rev. December 2020)
- IRC §1361(b), §1362(a), §1362(b)
- Reg. §1.1361-1(l), §1.1362-6
- Rev. Proc. 2013-30 (if late filing); Reg. §301.7701-3(c)(1)(v)(C) (if LLC)
- Rev. Proc. 2006-46 (if natural business year claimed in Part II)
```

The draft is **not** the final filed form — the user (or agent under explicit consent in `filing.md`) must transcribe to the IRS PDF and fax or mail.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every item on Form 2553 (Rev. December 2017), Parts I-IV, from the PDF text
- [`references/eligibility.md`](./references/eligibility.md) — IRC §1361 eligibility detailed: shareholder types, one-class-of-stock rule, ineligible corporation classes
- [`references/timing-rules.md`](./references/timing-rules.md) — When the 2-month-15-day clock starts; Rev. Proc. 2013-30 late relief mechanics
- [`references/reasonable-salary.md`](./references/reasonable-salary.md) — IRS factors test (*David E. Watson, P.C. v. United States*, Rev. Rul. 74-44); BLS OES wage data approach
- [`references/state-conformity.md`](./references/state-conformity.md) — State follow-up after the federal election (NY CT-6, AR AR1103, NJ registration and consent under P.L. 2022, c. 133) and entity-level taxes
- [`references/common-mistakes.md`](./references/common-mistakes.md) — 15 mistakes that void elections or trigger reclassification
- [`filing.md`](./filing.md) — Browser-automation playbook: fax vs mail decision tree, CP261 follow-up, state filings

## Examples

End-to-end worked elections.

- [`examples/consulting-llc-on-time.md`](./examples/consulting-llc-on-time.md) — Single-member LLC, $150K profit, on-time election, $80K reasonable salary
- [`examples/late-election-with-relief.md`](./examples/late-election-with-relief.md) — Single-member LLC wanting S status from 01/01/2025, found the missed deadline in February 2026 before any 2025 return was due; Rev. Proc. 2013-30 with Part IV
- [`examples/multi-member-llc-electing-scorp.md`](./examples/multi-member-llc-electing-scorp.md) — 2-member LLC (50/50) electing S-corp, both members consent, operating agreement amended for one-class-of-stock

## Sources

Authoritative sources used by this skill. Re-verify each year — the IRS revises Form 2553 and instructions periodically.

- [Form 2553 (latest)](https://www.irs.gov/pub/irs-pdf/f2553.pdf) — the form itself
- [Instructions for Form 2553 (latest)](https://www.irs.gov/pub/irs-pdf/i2553.pdf) — Rev. December 2020; line-by-line IRS guidance, service center addresses and fax numbers page 3
- [Where to file Form 2553](https://www.irs.gov/filing/where-to-file-your-taxes-for-form-2553) — current Kansas City / Ogden split (checked 2026-10-06)
- [CP261](https://www.irs.gov/individuals/understanding-your-cp261-notice) (election accepted), [CP264](https://www.irs.gov/individuals/understanding-your-cp264-notice) (Form 2553 denied), [CP262](https://www.irs.gov/individuals/understanding-your-cp262-notice) (S election revoked)
- [About Form 2553](https://www.irs.gov/forms-pubs/about-form-2553) — IRS landing page
- [Form 1120-S](https://www.irs.gov/pub/irs-pdf/f1120s.pdf) — annual S-corp return (downstream)
- [Publication 542](https://www.irs.gov/publications/p542) — Corporations
- [Publication 15 (Circular E)](https://www.irs.gov/publications/p15) — Employer's Tax Guide
- IRC §1361 (S-corp eligibility)
- IRC §1362 (election, revocation, termination)
- IRC §3121 (FICA tax definitions)
- Reg. §1.1361-1(l) — One-class-of-stock rule
- Reg. §1.1362-6 — Election filing requirements
- Reg. §1.1362-6(b)(2)(i) — community-property spouses must consent; §1.1362-6(b)(3)(iii) — late shareholder consents
- Reg. §301.7701-3(c)(1)(v)(C) — timely Form 2553 is a deemed corporate classification election for an eligible entity
- IRC §1362(b)(5) and Reg. §301.9100-3 — letter-ruling relief outside Rev. Proc. 2013-30
- Rev. Proc. 2013-30, 2013-36 I.R.B. 173 — Late S-corp election relief (§§4.02, 4.03, 5.01-5.04)
- Rev. Proc. 2026-1, Appendix A — user fees ($5,750 Part II business purpose; $14,500 §1362(b)(5)/§301.9100-3 relief; reduced fees $3,450 / $9,775)
- IRM 10.10.1, Exhibit 10.10.1-2 — forms that accept electronic or digital signatures (Form 2553 is not listed)
- Rev. Proc. 2006-46 — Natural business year procedure
- Rev. Rul. 74-44 — Reasonable compensation framework
- *David E. Watson, P.C. v. United States*, 668 F.3d 1008 (8th Cir. 2012) — reasonable-salary case law
- [S corporation compensation and medical insurance issues](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues) — IRS reasonable-compensation factors
- [SSA contribution and benefit base](https://www.ssa.gov/oact/cola/cbb.html) — $176,100 (2025), $184,500 (2026)
- Bureau of Labor Statistics OES — wage data for reasonable-salary analysis (https://www.bls.gov/oes/)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and case law. It is not tax or legal advice. S-corp election has consequences across federal tax, state tax, payroll compliance, and shareholder estate planning. The agent invoking this skill should remind the user that the output is a starting point and that complex situations (multi-state operations, shareholder buy-sell agreements, anticipated changes in ownership) warrant a licensed CPA or tax attorney's review.
