# Form W-9 — Line-by-line reference

Every line and box on Form W-9 (Rev. March 2024), checked against the form's own instructions on 2026-10-06, with examples and edge cases. Loaded on demand by the SKILL when the agent needs to map a user input to a specific field.

This reference is self-contained — the agent should be able to fill the form using only this file plus the SKILL workflow.

---

## Header

The form has no header section. The first row is Line 1.

---

## Line 1 — Name (as shown on your income tax return)

**What goes here:** The legal name on the user's federal income tax return.

| Filer type | Line 1 |
|------------|--------|
| Individual / sole proprietor | Personal legal name (e.g., "Jane M. Smith") |
| Single-member LLC (disregarded entity) | **Owner's personal name**, NOT the LLC name |
| Single-member LLC with S-corp or C-corp election | Entity name (e.g., "Smith Design LLC") |
| Multi-member LLC (default partnership) | LLC's legal name |
| Multi-member LLC with corporate election | LLC's legal name |
| C Corporation | Corporation's legal name |
| S Corporation | Corporation's legal name |
| Partnership | Partnership's legal name |
| Trust / estate | Trust's or estate's legal name |

**Cannot be left blank.** This is the name the IRS will match against the TIN entered in Part I. A mismatch triggers a CP2100 / "B" notice to the requestor and can trigger backup withholding.

**Edge cases:**

- **Recently married, name changed?** If the SSA has the new name, use it. If the user changed their last name without telling the SSA, enter first name, the last name shown on the Social Security card, and the new last name (W-9 instructions, Line 1).
- **Operating under a hyphenated last name on tax return but a single last name on driver's license?** Use the tax-return version.
- **Sole proprietor doing business as "ABC Consulting"?** Line 1 = personal name; "ABC Consulting" goes on Line 2.
- **Single-member LLC (Garcia Design LLC) owned by Maya Garcia?** Line 1 = "Maya Garcia"; "Garcia Design LLC" goes on Line 2.
- **Estate of deceased filer?** Line 1 = "Estate of <Decedent's Name>"; entity TIN required.

---

## Line 2 — Business name / disregarded entity name (if different from above)

**What goes here:** The business name, trade name, "doing business as" (DBA), or disregarded entity name if it differs from Line 1.

**Optional** — leave blank if the filer's only operating name is the same as Line 1.

| Filer type | Line 2 typical entry |
|------------|---------------------|
| Sole prop with no DBA | (blank) |
| Sole prop with DBA "Smith Design Studio" | "Smith Design Studio" |
| Single-member LLC (disregarded) | LLC name (e.g., "Smith Design LLC") — the instructions say to enter the disregarded entity's name on line 2 |
| Corporation operating under entity name only | (blank) |
| Corporation with DBA | DBA name |
| Partnership operating under entity name only | (blank) |

**Edge cases:**

- **Sole prop with multiple DBAs?** List the most relevant one (the one the requestor will pay). One per W-9.
- **LLC with the same name on Line 1 (because it's an S-corp election)?** Leave Line 2 blank; line 2 is for a business, trade, DBA, or disregarded entity name that differs from line 1.

---

## Line 3a — Federal tax classification (check ONE box only)

Seven options:

1. **Individual/sole proprietor**
2. **C corporation**
3. **S corporation**
4. **Partnership**
5. **Trust/estate**
6. **LLC** — and if checked, fill the classification letter (C, S, or P)
7. **Other** (rare; see IRS instructions)

A disregarded entity checks the box for its owner's classification (Rev. March 2024 What's New; Line 3a note). The checkbox no longer reads "or single-member LLC".

### When to check each box

| Filer's situation | Check this box | LLC letter (if box 6) |
|-------------------|----------------|------------------------|
| Individual freelancer with no formal entity | Individual/sole proprietor | n/a |
| Sole proprietor with EIN but no LLC | Individual/sole proprietor | n/a |
| Single-member LLC, no Form 2553 / 8832 filed | Individual/sole proprietor | n/a |
| Single-member LLC with Form 2553 (S-corp) on file | Limited liability company | S |
| Single-member LLC with Form 8832 (C-corp) on file | Limited liability company | C |
| Multi-member LLC, no corporate election | Limited liability company | P |
| Multi-member LLC with S-corp election | Limited liability company | S |
| Multi-member LLC with C-corp election | Limited liability company | C |
| Incorporated as S-corp (Articles of Incorp + Form 2553) | S Corporation | n/a |
| Incorporated as C-corp (Articles of Incorp, no S election) | C Corporation | n/a |
| General or limited partnership (not LLC) | Partnership | n/a |
| Trust or estate | Trust/estate | n/a |

**The most common error**: a single-member LLC owner with no corporate election checks "LLC" and writes "S" or nothing. The correct box is the owner's: "Individual/sole proprietor" for an individual owner — the SMLLC default is a disregarded entity treated as the owner for tax purposes.

---

## Line 3b — Foreign partners, owners, or beneficiaries (new in March 2024 revision)

**What this is:** A checkbox added in the March 2024 revision. It applies only if, on line 3a, the filer checked Partnership or Trust/estate, or LLC with "P". Check it if:
- The filer is a partnership (including an LLC taxed as a partnership), trust, or estate, AND
- It is giving this W-9 to a partnership, trust, or estate in which it has an ownership interest, AND
- It has any foreign partners, owners, or beneficiaries (it must check the box if it received a Form W-8 or documentary evidence of foreign status from any of them, or a W-9 with box 3b checked)

The purpose: the receiving flow-through entity may need it for Schedules K-2 and K-3 (Form 1065). **Most filers leave Line 3b blank.** Individuals, sole props, disregarded SMLLCs, and corporations never check it.

---

## Line 4 — Exemptions

Two sub-fields:

### Exempt payee code (1-13)

Applies to entities exempt from backup withholding under IRC §3406. Common codes:

| Code | Applies to |
|------|------------|
| 1 | Organization exempt from tax under §501(a), IRA, custodial account under §403(b)(7) |
| 2 | The United States or any of its agencies / instrumentalities |
| 3 | A state, DC, US commonwealth/possession, or political subdivision |
| 4 | Foreign government, international organization, or any subdivision thereof |
| 5 | Corporation |
| 6 | Dealer in securities or commodities required to register under US/state/territory law |
| 7 | Futures commission merchant registered with CFTC |
| 8 | Real estate investment trust (REIT) |
| 9 | Entity registered at all times during tax year under Investment Company Act of 1940 |
| 10 | Common trust fund operated by bank under §584(a) |
| 11 | Financial institution as defined in §581 |
| 12 | Middleman known in investment community as a nominee or custodian |
| 13 | Trust exempt from tax under §664 or described in §4947 |

**Sole proprietors, individuals, and disregarded single-member LLCs leave this blank** ("Generally, individuals (including sole proprietors) are not exempt from backup withholding"). Corporations (Code 5) are not exempt for card / third-party network settlements, attorneys' fees or gross proceeds, or medical payments reportable on 1099-MISC; S corporations must not enter a code for broker transactions.

### Exemption from FATCA reporting code (A-M)

Applies to certain payees with foreign account exemptions. Codes A through M correspond to specific categories defined in the FATCA regulations.

**For US-only-payee filers, leave blank** — the codes apply only to accounts maintained outside the United States by certain foreign financial institutions; a requester may mark the line "Not Applicable". If the user is being asked for a FATCA code for a foreign account, they need a tax pro — out of scope for this skill.

---

## Line 5 — Address (number, street, and apt. or suite no.)

**What goes here:** The filer's mailing address. The instructions: "This is where the requester of this Form W-9 will mail your information returns." If it differs from what the requester has on file, write "NEW" at the top of the form.

**Formatting:**
- Number + street name + apt/suite designation (e.g., "742 Evergreen Terrace, Suite 4B")
- An address where the user reliably receives mail; matching the tax-return address avoids confusion but is not a W-9 rule
- City, state, and ZIP go on Line 6

**Edge cases:**

- **Filer moves mid-year?** Send a fresh W-9 to every active requestor with the new address.
- **Filer has a separate business address?** Use whichever address the user wants information returns mailed to. Line 2 is for a business name, never an address.
- **Filer is in a different state from the LLC's state of formation?** The LLC's state of formation is not relevant to the W-9 address.

---

## Line 6 — City, state, and ZIP code

Standard. City + 2-letter state code + 5-digit (or 9-digit) ZIP.

---

## Line 7 — List account number(s) here (optional)

**What goes here:** Internal account numbers, vendor IDs, or list designators that the requestor wants for their own recordkeeping.

**Optional.** Most filers leave blank. Fill only if the requestor specifically asks for a vendor ID or account number.

---

## Part I — Taxpayer Identification Number (TIN)

**Boxes for SSN:** Three boxes (3 digits / 2 digits / 4 digits). Format: XXX-XX-XXXX.

**Boxes for EIN:** Two boxes (2 digits / 7 digits). Format: XX-XXXXXXX.

The form has both options. Fill ONLY ONE — leave the other blank.

### Which TIN to enter

| Line 3a classification | TIN |
|------------------------|-----|
| Individual/sole proprietor | SSN (or ITIN if no SSN); a sole prop with an EIN may use either |
| Single-member LLC (disregarded) | Owner's SSN (or the owner's own EIN) |
| LLC taxed as S-corp / C-corp | LLC's EIN |
| Multi-member LLC (partnership) | LLC's EIN |
| C Corporation | Corporation's EIN |
| S Corporation | Corporation's EIN |
| Partnership | Partnership's EIN |
| Trust/estate | Trust's or estate's EIN |

### The SMLLC trap

A single-member LLC is "disregarded" for federal tax purposes — it is treated as the owner. The owner files Schedule C; the LLC does not file its own tax return. Therefore:

- **Line 1 = owner's personal name**
- **Part I = owner's SSN**
- **Line 2 = LLC name** (optional)

Even if the LLC has applied for and received an EIN (for opening a bank account, hiring employees, etc.), the W-9 uses the **owner's SSN** (or the owner's own EIN, if the owner has one) in Part I — never the disregarded LLC's EIN. This is because the IRS matches the 1099-NEC against the name on Line 1 and the TIN in Part I. If Line 1 is the owner's name and the TIN is the LLC's EIN, the matching fails.

The exception is when the SMLLC has filed Form 2553 (S-corp election) or Form 8832 (C-corp election) — then the LLC IS a separate taxpayer, Line 1 = LLC name, Part I = LLC's EIN.

### ITIN vs SSN

If the filer is a US person but ineligible for an SSN (resident alien on a visa that doesn't permit work), they use an ITIN issued via Form W-7. ITINs follow the SSN format (XXX-XX-XXXX) and are entered in the SSN boxes. ITINs always start with `9`.

If the filer's "SSN" starts with `9`, it's actually an ITIN — that's fine for W-9 purposes if the user is otherwise a US person, but flag for the user that some requestors' systems flag ITINs differently.

---

## Part II — Certification

Four numbered statements + a signature + date.

**The certification statements** (paraphrased, see IRS form for exact wording):

1. The number shown on this form is my correct TIN (or I am waiting for one to be issued).
2. I am not subject to backup withholding because: (a) I am exempt from BUW, OR (b) I have not been notified by the IRS that I am subject to BUW for failing to report all interest or dividends, OR (c) the IRS has notified me that I am no longer subject to BUW.
3. I am a US citizen or other US person (defined in instructions).
4. The FATCA code(s) entered on this form (if any) indicating I am exempt from FATCA reporting is correct.

**Strike item 2 ONLY if** the IRS has previously notified the user that they ARE currently subject to backup withholding for under-reporting interest or dividends. This is rare — most filers do not strike anything.

**Signature** — handwritten or electronic. An electronic W-9 is acceptable when the requester's system meets the Instructions for the Requester of Form W-9 (Rev. March 2024), "Electronic Submission of Forms W-9": it makes reasonably certain the submitter is the person on the form, keeps the same information as the paper form, can supply a hard copy, and ends with an electronic signature under penalties of perjury using the paper form's language. E-signature platforms and vendor portals are typical ways requesters meet this.

**When a signature is required** (Form W-9, Part II "Signature requirements"): accounts for interest, dividends, brokers, and barter exchanges opened after 1983 (or backup withholding applies), and real estate transactions. For "other payments" (rents, services by a nonemployee, card / third-party network settlements, medical, attorney gross proceeds, and more), the payee must give the correct TIN but need not sign unless notified of a previously incorrect TIN.

**Date** — the date the user signs. MM/DD/YYYY format.

---

## What's NOT on the form

These are common questions that often confuse first-time filers — none of them appear on Form W-9:

- **Hourly rate or contract value** — not on W-9 (that's in the user's contract with the requestor)
- **Bank account or routing number** — not on W-9 (that's a separate ACH authorization form)
- **Voided check** — not required by W-9; some requestors ask separately for direct-deposit setup
- **Driver's license / passport number** — not on W-9 (some requestors ask separately for I-9 employment verification, but I-9 only applies if the relationship is employee, not contractor)
- **Both SSN and EIN** — fill only one TIN. A sole proprietor with an EIN may enter either; the IRS encourages the SSN (chart note 3)
- **State sales-tax permit number** — not on W-9 (that's state-level, separate)
