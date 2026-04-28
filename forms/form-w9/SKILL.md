---
name: form-w9
description: >
  Use this skill when a US person (citizen, resident alien, or US-formed business)
  needs to fill out IRS Form W-9 to give to a client, payor, or platform. Triggers
  on phrases like "fill out W-9", "complete W-9 for my client", "send W-9 to
  [company]", "W-9 for LLC", "W-9 for sole proprietor", "what TIN do I put on
  W-9", "W-9 backup withholding", "client requested a W-9". Do NOT use for:
  foreign persons or non-US entities (use forthcoming form-w8ben / form-w8bene
  skill — W-9 is for US persons only); employees onboarding to a new job (that
  is W-4, withholding for wages — different skill); employer issuing W-2 (that is
  the wage statement, also different); a business applying for its own EIN (use
  forthcoming form-ss4 skill).
form: Form W-9
audience: [solo, freelance, llc1, llcm, scorp, employer, individual]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/fw9.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/iw9.pdf
---

# Form W-9 — Request for Taxpayer Identification Number and Certification

This skill walks the agent through producing an audit-grade Form W-9 for a US person to give to a requestor (client, payment platform, bank, real-estate escrow, etc.). The W-9 is **not filed with the IRS** — it is given to the requestor, who keeps it on file and uses it to file information returns (1099-NEC, 1099-K, 1099-MISC, etc.) at year-end.

The form itself takes three minutes. The judgment is in **(a)** picking the right Line 3a tax classification, **(b)** picking the right TIN type for that classification (SSN vs EIN), and **(c)** delivering the completed form securely (it contains the filer's SSN/EIN and full legal name — identity-theft-grade data).

**Companion guide for end users:** [What Is a W-9 Form? Guide for Freelancers and Independent Contractors 2026](https://jupid.com/blog/what-is-a-w9-form-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form W-9, "W-9", or "W9"
- A client, platform (Upwork, Fiverr, Etsy, Stripe, PayPal, Uber, DoorDash, Amazon), bank, broker, or escrow company requested the user's TIN
- The user is starting a contractor / vendor / freelance engagement with a US business and needs to provide tax info
- The user is a US person (citizen, resident alien, US-formed entity)

Do **not** engage this skill when:

- The user is a non-resident alien individual → use the (forthcoming) `form-w8ben` skill
- The user is a non-US (foreign) corporation, partnership, or other entity → use the (forthcoming) `form-w8bene` skill
- The user is a new W-2 employee → that is **Form W-4** (employee withholding certificate), not W-9
- The user is an employer issuing a wage statement → that is **Form W-2**, not W-9
- The user (or their business) is applying for an EIN → use the (forthcoming) `form-ss4` skill (Form SS-4 is the EIN application; W-9 is given to a payor *after* you have a TIN)
- The user is being asked to complete a W-9 by someone they have no business relationship with → suspect phishing; see `references/common-mistakes.md`

If the user's tax residency is ambiguous (e.g., dual-citizen, on a US visa, recent green card holder), ask before proceeding. The wrong form (W-9 vs W-8BEN) leads to over-withholding at 30% (NRA who sent W-9) or backup withholding at 24% (US person who sent W-8BEN).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Filer's full legal name** as it appears on their tax return. Goes on Line 1.
2. **Business name / DBA** (if different from Line 1). Goes on Line 2. Optional.
3. **Federal tax classification** — Line 3a. One of: Individual/sole proprietor, C Corporation, S Corporation, Partnership, Trust/estate, Limited liability company. If the user has an LLC, ask the LLC's tax classification (disregarded entity / S-corp election / C-corp election / partnership). See [`references/tax-classification-decisions.md`](./references/tax-classification-decisions.md).
4. **TIN** — Part I. SSN, ITIN, or EIN, depending on Line 3a. See [`references/tin-selection.md`](./references/tin-selection.md). Do not invent.
5. **Mailing address** — Lines 5 and 6 (street + city/state/ZIP).
6. **Requestor identity** — who asked for the W-9, and how the user verified the request is legitimate. Phishing W-9 requests are a known attack vector.
7. **Delivery channel** the user intends to use (DocuSign / client portal / encrypted email / fax / mail). Drives the security checks in `filing.md`.
8. **Exemption codes** (Line 4) — usually blank for individual/sole-prop/single-member LLC; ask only if the user is a corporation, tax-exempt entity, or financial institution.

For LLCs specifically, also ask:

- Has the LLC filed Form 2553 (S-corp election) or Form 8832 (C-corp election)?
- Is it a single-member LLC (default = disregarded entity, owner files Schedule C) or multi-member (default = partnership, files Form 1065)?
- Does the LLC have its own EIN, or only the owner's SSN?

The single-member LLC case is the most-misfiled W-9 in the wild. If the user has not made a corporate election, **Line 1 is the owner's personal name**, **Line 3a is "Individual/sole proprietor"** (not "Limited liability company"), and **the TIN is the owner's SSN** — even if the LLC has its own EIN. See `examples/single-member-llc-owner.md`.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Verify the requestor

Confirm the W-9 request is legitimate before producing the form. The W-9 contains the filer's full name + SSN/EIN — phishing for it is a well-documented attack.

Ask the user:
- Who requested the W-9? (Person + company)
- How did the request arrive? (Client portal / known-good email / cold email / DM)
- Is there an existing engagement (signed contract, prior invoices, account on a known platform)?

If the request is from a stranger with no existing engagement, advise the user to verify with the company directly via a phone number from the company's official website (not the email signature). Do not produce the W-9 until the user confirms legitimacy.

### Step 2 — Determine US-person status

Confirm the user is a US person:
- US citizen
- US resident alien (green card, substantial presence test)
- US partnership, US corporation, US LLC, US estate or trust
- Domestic estate or trust as defined under §7701(a)(31)

If the user is a non-resident alien individual, redirect to `form-w8ben`. If a foreign entity, redirect to `form-w8bene`. Do not proceed with W-9.

### Step 3 — Determine Line 3a (federal tax classification)

This is the most important judgment in the form. Walk the decision tree in [`references/tax-classification-decisions.md`](./references/tax-classification-decisions.md):

```
Are you an individual / sole proprietor (no formal entity)?           → Individual/sole proprietor
Single-member LLC, no corporate election?                              → Individual/sole proprietor *
Single-member LLC, S-corp election (Form 2553) on file?                → S Corporation **
Single-member LLC, C-corp election (Form 8832) on file?                → C Corporation **
Multi-member LLC, no corporate election?                               → Partnership ***
Multi-member LLC, S-corp election?                                     → S Corporation **
Multi-member LLC, C-corp election?                                     → C Corporation **
Filed Articles of Incorporation as S-corp?                             → S Corporation
Filed Articles of Incorporation as C-corp?                             → C Corporation
General / limited partnership?                                         → Partnership
Trust or estate?                                                       → Trust/estate

* The W-9 form's Line 3a says "Individual/sole proprietor or single-member LLC"
  — they share the same checkbox.
** Line 3a sub-line: check "Limited liability company" and enter the
  classification letter (S or C). Do NOT check the standalone S Corporation
  or C Corporation box if the entity is an LLC.
*** Multi-member LLC taxed as partnership — check "Limited liability
  company" and enter "P".
```

Confirm the user's answer back to them: "You're filling out the W-9 as Individual/sole proprietor, using your SSN. Right?" — get an explicit yes before moving on.

### Step 4 — Determine the TIN to enter

TIN selection follows from Line 3a. Use [`references/tin-selection.md`](./references/tin-selection.md):

| Line 3a classification | TIN to use | Notes |
|------------------------|-----------|-------|
| Individual/sole proprietor | SSN (or ITIN if no SSN) | Even if the sole prop has an EIN, IRS prefers SSN here |
| Single-member LLC (disregarded) | Owner's SSN | LLC's EIN is *not* used; the LLC is invisible to the IRS for this form |
| LLC taxed as S-corp / C-corp | LLC's EIN | The corp election makes the LLC a separate taxpayer |
| Multi-member LLC (partnership) | LLC's EIN | |
| C Corporation / S Corporation | Corporation's EIN | |
| Partnership | Partnership's EIN | |
| Trust/estate | Trust's or estate's EIN | |

If the user does not yet have an EIN but the classification requires one, redirect to `form-ss4` (forthcoming) — they need an EIN before they can complete the W-9.

### Step 5 — Fill Lines 1 through 7 + Part I

Walk every line:

- **Line 1** — filer's legal name. For SMLLC = owner's personal name, NOT the LLC name. For S-corp / C-corp / partnership / trust = entity's legal name.
- **Line 2** — DBA / business name. Optional. For SMLLC, this is where the LLC name goes (if it differs from Line 1).
- **Line 3a** — checkbox + LLC classification letter (if applicable), per Step 3.
- **Line 3b** — new since the March 2024 revision: check this box only if the entity is an LLC owned by a partnership, trust, or estate that is exempt from FATCA reporting under §1471. For most filers, leave blank.
- **Line 4** — Exemption codes (usually blank). See `references/line-by-line.md` for the full list. Sole proprietors and single-member LLC owners always leave blank.
- **Line 5** — Street address.
- **Line 6** — City, state, ZIP.
- **Line 7** — Optional account/list numbers. Most users leave blank unless the requestor specifically asked for an internal account number.
- **Part I — TIN** — the SSN or EIN per Step 4. Format SSN as `XXX-XX-XXXX`, EIN as `XX-XXXXXXX`. Don't strip the dashes.

### Step 6 — Sign Part II (Certification)

Part II is the certification. By signing, the user attests under penalty of perjury that:

1. The TIN entered is correct (or the user is awaiting one).
2. The user is not subject to backup withholding because: (a) they are exempt from BUW, OR (b) the IRS has not notified them they are subject to BUW for failing to report interest/dividends, OR (c) the IRS has notified them they are no longer subject.
3. The user is a US person.
4. Any FATCA code on Line 4 is correct.

Important nuance:
- If the IRS has previously notified the user they ARE currently subject to backup withholding for under-reporting, the user must **strike out item 2** before signing. This is rare but matters.
- Sign + date. Electronic signatures meeting IRS Pub 1345 standards are acceptable (DocuSign, Adobe Sign, Gusto, etc.). Typing a name in a Word doc is **not** sufficient.

### Step 7 — Validate

Run every check in the **Validation** section. Surface any sanity warnings.

### Step 8 — Produce the deliverable

Use the template in **Output format**.

### Step 9 — Hand off to filing

The W-9 is **not filed with the IRS**. It is delivered to the requestor. Hand off to [`filing.md`](./filing.md) which covers:

- Picking a delivery channel (e-signature platform / client portal / encrypted email / fax / mail)
- Field-by-field mapping for DocuSign and Adobe Sign as canonical channels
- Security rules (never email an unencrypted W-9; W-9 contains SSN)

### Step 10 — Set the renewal calendar

W-9s do not expire by IRS rule, but in practice:

- The user should provide a fresh W-9 if their name, address, entity type, or TIN changes
- Many corporate AP departments require a fresh W-9 every fiscal year regardless
- Tell the user to keep a list of every requestor that has their W-9 on file, so they can re-issue when info changes

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header / Identity (Lines 1-2)

- **Line 1** — Name on the user's tax return. For individual / sole prop / SMLLC: personal name. For corporation / partnership: entity name. **Cannot be left blank.**
- **Line 2** — Business / DBA / disregarded-entity name. Optional. Used when the business operates under a name different from Line 1.

### Tax classification (Line 3)

- **Line 3a** — One of seven boxes. See [`references/tax-classification-decisions.md`](./references/tax-classification-decisions.md). The most common error is checking "Limited liability company" for a single-member LLC instead of "Individual/sole proprietor".
- **Line 3b** — New in March 2024 revision: FATCA exemption indicator for LLCs owned by certain pass-through entities. Most filers leave blank.

### Exemptions (Line 4)

Two sub-fields:
- **Exempt payee code** — applies to certain entity types (corporations, banks, tax-exempt orgs, government entities) that are exempt from backup withholding. Sole props and individuals: blank.
- **FATCA reporting code** — applies to entities maintaining accounts outside the US under FATCA. US-only payees: blank.

See `references/line-by-line.md` for the full code list.

### Address (Lines 5-6)

- **Line 5** — Street address (house/apt/suite number + street name)
- **Line 6** — City, state, ZIP

The address is where the requestor will mail the year-end 1099. Use the same address the user files on Form 1040 to avoid mismatches.

### Account number(s) — Line 7

Optional. Used by the requestor for internal vendor / account ID. Most filers leave blank.

### Part I — TIN

Either SSN (or ITIN) or EIN per Step 4. Match the format on the form (boxes for SSN are split XXX-XX-XXXX; EIN is XX-XXXXXXX).

### Part II — Certification

Sign + date. Strike item 2 only if the IRS currently treats the user as subject to backup withholding. Electronic signatures must meet IRS Pub 1345 standards.

---

## Validation

Before declaring the W-9 ready, run these checks. Surface anything that fails — don't silently fix.

### Identity checks

- [ ] Line 1 is non-blank
- [ ] Line 1 matches the name on the user's tax return (the name the IRS will match against the TIN)
- [ ] If Line 3a = Individual/sole proprietor, Line 1 is a personal name (not an entity name)
- [ ] If Line 3a = Corporation / Partnership / Trust, Line 1 is the entity legal name (not a personal name)

### Classification checks

- [ ] Exactly one Line 3a box is checked
- [ ] If "Limited liability company" is checked, the classification letter (C, S, or P) is filled
- [ ] If the user described a single-member LLC with no corporate election, Line 3a = Individual/sole proprietor (not LLC)
- [ ] Line 3b is blank unless the user described a pass-through-owned LLC with a FATCA exemption

### TIN checks

- [ ] If Line 3a = Individual/sole proprietor (incl. SMLLC disregarded), Part I = SSN or ITIN (9 digits, formatted XXX-XX-XXXX)
- [ ] If Line 3a = S-corp / C-corp / Partnership / Trust, Part I = EIN (9 digits, formatted XX-XXXXXXX)
- [ ] TIN length is exactly 9 digits
- [ ] TIN does not start with `9` for SSN field (those are ITIN ranges; allowed only when filer has no SSN)
- [ ] TIN matches the entity on Line 1 — sole prop's SSN with sole prop's name, corporation's EIN with corporation's name

### Certification checks

- [ ] Part II signed
- [ ] Part II dated
- [ ] If the user said they have ever received an IRS BUW notice still in effect, item 2 in Part II is struck through
- [ ] User's signature is on the actual form (not just typed in an email body)

### Sanity checks (warn, don't block)

- [ ] User has an EIN but is filing as Individual/sole proprietor → confirm they understand IRS prefers SSN here
- [ ] User said they "have an LLC" but is filing as Individual/sole proprietor → confirm SMLLC default (disregarded entity); flag if multi-member LLC misfiled
- [ ] User's address on Lines 5-6 differs from the address on their last tax return → confirm intentional
- [ ] Requestor is not from an established business relationship → flag potential phishing
- [ ] Delivery channel is unencrypted email → block and request a secure channel (encrypted email, e-signature platform, or password-protected PDF with separate password channel)

---

## Output format

The deliverable is a **filled draft** the user can transcribe to the IRS PDF or paste into an e-signature platform. Format:

```markdown
# Form W-9 — DRAFT (revision March 2024)

## Identity
1. Name (as shown on income tax return):       <Legal name>
2. Business name / disregarded entity name:    <DBA or blank>

## Tax classification (Line 3)
3a. Federal tax classification:                <one of: Individual/sole proprietor | C Corporation | S Corporation | Partnership | Trust/estate | Limited liability company>
    (If LLC) Tax classification letter:        <C | S | P | blank>
3b. (FATCA pass-through indicator):            <checked | blank>

## Exemptions (Line 4) — usually blank
Exempt payee code:                             <code or blank>
FATCA reporting code:                          <code or blank>

## Address (Lines 5-6)
5. Address (street + apt/suite):               <street>
6. City, state, ZIP:                           <city>, <ST> <ZIP>

## Optional account number(s) (Line 7)
7. List account number(s):                     <blank or vendor ID>

## Part I — Taxpayer Identification Number
TIN (SSN or EIN):                              <XXX-XX-XXXX or XX-XXXXXXX>
TIN type:                                      <SSN | ITIN | EIN>

## Part II — Certification
Signature:                                     ____________________
Date:                                          MM/DD/YYYY
Item 2 struck through?                         <Yes only if IRS BUW notice currently in effect | No>

## Delivery
Channel:                                       <DocuSign | Adobe Sign | client portal | encrypted email | password-protected PDF | fax | mail>
Recipient (requestor):                         <Person + Company>
Verification of requestor legitimacy:          <How user confirmed the request is real>

## Validation summary
- Identity checks: passed
- Classification checks: passed
- TIN checks: passed
- Certification checks: passed
- Sanity warnings: <list any>

## Sources cited in this draft
- IRS Form W-9 (Rev. March 2024)
- IRS Instructions for Form W-9 (Rev. March 2024)
- IRC §6109 (TIN furnishing requirement)
- IRC §3406 (backup withholding)
- IRS Publication 1345 (e-signature standards)
- (any others relied on)
```

The draft is **not** the filed/delivered form. The user (or the agent acting on the user's authorization) must transcribe to the IRS PDF or e-signature platform and send to the requestor through a secure channel — see `filing.md`.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line and box on Form W-9 with examples and edge cases
- [`references/tax-classification-decisions.md`](./references/tax-classification-decisions.md) — Decision tree for Line 3a, including the LLC sub-cases
- [`references/tin-selection.md`](./references/tin-selection.md) — When SSN vs EIN; the SMLLC trap
- [`references/backup-withholding.md`](./references/backup-withholding.md) — IRC §3406 mechanics; when 24% applies; how to stop it
- [`references/w9-vs-w8.md`](./references/w9-vs-w8.md) — Distinguishing W-9 from W-8BEN / W-8BEN-E for borderline cases
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: secure delivery channels, DocuSign / Adobe Sign field mappings, security rules

## Examples

End-to-end worked W-9s. Use these as patterns when the user's situation is similar.

- [`examples/single-member-llc-owner.md`](./examples/single-member-llc-owner.md) — SMLLC, no corporate election, default disregarded entity. Most common pattern.
- [`examples/s-corp-shareholder-employee.md`](./examples/s-corp-shareholder-employee.md) — 100% owner of S-corp providing services as the corp; W-9 in entity name with EIN.
- [`examples/freelance-individual-no-llc.md`](./examples/freelance-individual-no-llc.md) — Individual sole prop with no LLC. Personal name + SSN.

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the current revision — the IRS revises Form W-9 periodically (most recent revision as of last_verified is March 2024).

- [What Is a W-9 Form? Guide for Freelancers and Independent Contractors 2026](https://jupid.com/blog/what-is-a-w9-form-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form W-9 (latest)](https://www.irs.gov/pub/irs-pdf/fw9.pdf) — the form itself (Rev. March 2024)
- [Instructions for Form W-9 (latest)](https://www.irs.gov/pub/irs-pdf/iw9.pdf) — line-by-line IRS guidance
- [About Form W-9](https://www.irs.gov/forms-pubs/about-form-w-9) — IRS landing page with archive of past revisions
- [IRS Topic No. 307 — Backup Withholding](https://www.irs.gov/taxtopics/tc307)
- [Publication 1281 — Backup Withholding for Missing and Incorrect Name/TIN(s)](https://www.irs.gov/pub/irs-pdf/p1281.pdf)
- [Publication 1345 — Handbook for Authorized IRS e-file Providers](https://www.irs.gov/pub/irs-pdf/p1345.pdf) (e-signature standards)
- [Form 1099-NEC](https://www.irs.gov/forms-pubs/about-form-1099-nec) — the year-end information return the W-9 enables
- IRC §3406 (backup withholding requirements, 24% rate)
- IRC §6041 (information return requirements, threshold raised to $2,000 by OBBBA Section 112201 effective 2026)
- IRC §6109 (requirement to furnish TIN; subsection (c) authorizes electronic filings)
- IRC §7701(a)(31) (definition of domestic estate / trust)
- IRC §1471 (FATCA — foreign account tax compliance)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (multi-state residency, dual citizenship, recent entity restructuring) warrant a licensed tax professional's review.
