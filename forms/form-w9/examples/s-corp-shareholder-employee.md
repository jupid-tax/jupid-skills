# Example: S-Corporation Shareholder-Employee (Services Performed Through Corp)

A complete walkthrough of Form W-9 for a 100% owner of an S-corporation who is providing professional services to a client through the corporation. The W-9 is for the **corporation**, not the shareholder personally — Line 1 is the corporate name and Part I is the corporate EIN.

## The filer

- **Filer (entity)**: Patel Consulting Inc.
- **Type**: S Corporation, formed by filing Articles of Incorporation in Delaware in 2022, with a timely Form 2553 (S-corp election) accepted effective January 1, 2023
- **Owner**: Raj Patel — 100% shareholder, also the sole officer and the only employee
- **Business**: Management consulting (operations / supply chain advisory for mid-market manufacturers)
- **Has EIN?**: Yes — corporate EIN obtained at incorporation
- **Tax year**: 2026 (calendar year filer)

## The trigger

Raj's corp signed a Statement of Work with **Northbridge Manufacturing LLC** for a 6-month engagement: $24,000/month invoiced from Patel Consulting Inc. Northbridge's controller, Diane Park, emailed Raj asking for a W-9 from "your company" before processing the first month's invoice. Email came from `dpark@northbridgemfg.com` — a domain Raj recognized from the procurement portal where the SOW was executed. Existing engagement, verified sender → request is legitimate.

## Inputs gathered (Step 1-4 of workflow)

### Step 1 — Verify the requestor

- Requestor: Diane Park, Controller at Northbridge Manufacturing LLC
- Channel: DocuSign envelope sent from Northbridge's procurement system
- Existing engagement: Yes — signed SOW from prior week
- Verdict: Legitimate. Proceed.

### Step 2 — US-person status

Patel Consulting Inc. is a Delaware corporation, formed under US law → US person → W-9 is the correct form.

### Step 3 — Line 3a classification

Decision tree (`references/tax-classification-decisions.md`, Section D.1):

1. Was the entity formed by Articles of Incorporation? **Yes** — Delaware Articles of Incorporation, 2022.
2. Filed Form 2553? **Yes** — election effective 1/1/2023, IRS acceptance letter on file.
3. Therefore: S Corporation, NOT an LLC.

Result: **Line 3a = "S Corporation"** (the standalone S Corporation checkbox, NOT the "Limited liability company" + S combo — Patel Consulting Inc. is not an LLC).

The agent confirms back to Raj: "You're filling this out in the corporation's name, using the corp's EIN — not your personal SSN. Right?" Raj: "Right. The whole point of the S-corp is that the corp is the contracting party, not me."

### Step 4 — TIN selection

Per `references/tin-selection.md`: S Corporation → Corporation's EIN.

- Corporate EIN: `88-XXXXXXX`
- Raj's personal SSN: NOT used on this W-9.

### Step 5 — Line 4 (exemption codes)

**Exempt payee code**: Corporations are generally exempt from backup withholding under IRC §3406(g) and W-9 instructions Code 5. Patel Consulting can enter `5` on the exempt-payee line of Line 4.

**Caveat**: The Code 5 exemption does NOT apply to all payments to corporations. Specifically, payments to corporations for **legal services** (e.g., attorney fees) and **medical/healthcare services** remain 1099-reportable and subject to backup withholding rules. Raj's corp provides management consulting — neither legal nor medical — so Code 5 fully applies.

**FATCA reporting code**: Patel Consulting is a US-only entity with no foreign accounts → blank.

The agent surfaces this to Raj: "Because you're an S-corp, you can mark exempt payee Code 5. This means Northbridge won't apply backup withholding even if there's ever a TIN mismatch, AND in many cases they won't even have to file a 1099 to your corp at year-end — though they often still do as a courtesy. Want to mark Code 5?" Raj: "Yes."

## The completed W-9 draft

```markdown
# Form W-9 — DRAFT (revision March 2024)

## Identity
1. Name (as shown on income tax return):       Patel Consulting Inc.
2. Business name / disregarded entity name:    blank

## Tax classification (Line 3)
3a. Federal tax classification:                S Corporation
    (If LLC) Tax classification letter:        n/a (LLC box NOT checked — entity is a corporation, not an LLC)
3b. (FATCA pass-through indicator):            blank

## Exemptions (Line 4)
Exempt payee code:                             5 (Corporation, exempt from backup withholding)
FATCA reporting code:                          blank

## Address (Lines 5-6)
5. Address (street + apt/suite):               1209 Orange Street, Suite 700
6. City, state, ZIP:                           Wilmington, DE 19801

## Optional account number(s) (Line 7)
7. List account number(s):                     blank (Northbridge did not request a vendor ID)

## Part I — Taxpayer Identification Number
TIN (SSN or EIN):                              88-XXXXXXX
TIN type:                                      EIN

## Part II — Certification
Signature:                                     Raj Patel, President & CEO, Patel Consulting Inc. (electronic via DocuSign)
Date:                                          04/28/2026
Item 2 struck through?                         No

## Delivery
Channel:                                       DocuSign (sent from Northbridge's procurement system)
Recipient (requestor):                         Diane Park, Controller, Northbridge Manufacturing LLC
Verification of requestor legitimacy:          Existing signed SOW; DocuSign envelope from known procurement domain
```

## Why each non-obvious choice

**Why is Line 1 the corporate name and not Raj's personal name?** Because the S-corp is a separate taxpayer for federal income tax. It files Form 1120-S each year using its own EIN. Raj is an employee of his corp (he draws a W-2 salary) and a shareholder (he gets pass-through income on a Schedule K-1) — but the contracting party with Northbridge is the corporation, not Raj. The 1099 (if any) would go to the corp.

**Why is Line 3a the standalone "S Corporation" box and NOT "Limited liability company + S"?** This is a common point of confusion. The "Limited liability company" + S combination is for LLCs that have elected S-corp status — entities formed via Articles of Organization at the state level. Patel Consulting Inc. was formed via Articles of Incorporation — it is and always has been a corporation under state law. The S-corp election (Form 2553) is a federal tax election layered on top of the corporate state form. Line 3a wants the **legal entity form**, then the federal tax election. For a state-formed corp, that's the standalone S Corporation box.

**Why does the Code 5 exemption matter if Raj's corp isn't going to under-report income anyway?** Two reasons. First, it prevents backup withholding from ever starting if there's a name/TIN matching glitch — corps occasionally have address mismatches in IRS records that would trigger BUW for non-exempt payees. Code 5 short-circuits that. Second, it signals to Northbridge's AP system that 1099-NEC reporting may not apply (most non-legal, non-medical payments to corporations are exempt from 1099-NEC reporting under IRC §6041 and Treas. Reg. §1.6041-3(p)). Northbridge can mark the vendor as 1099-exempt in their system.

**Why is Line 2 blank instead of repeating "Patel Consulting Inc."?** When the legal entity name on Line 1 is also the operating name (no separate DBA), Line 2 is left blank per the IRS instructions. Repeating the same name on Line 2 is technically allowed but adds no information.

**Why is the corp's address on Lines 5-6, not Raj's home address?** The address on the W-9 is where the requestor will mail the 1099 (if any) and any IRS-related correspondence. Patel Consulting Inc.'s registered address is its Delaware office of record (the entity's tax-return address on Form 1120-S). Using Raj's home address would create a mismatch with what the IRS has on file for the corporation's EIN.

**Why does Raj sign as "President & CEO" rather than just "Raj Patel"?** When an entity (corp / LLC / partnership / trust) signs a W-9, the signer is acting as an officer of the entity — not as themselves. The signature line should make clear the signer has authority to bind the entity. Raj is the sole officer of Patel Consulting Inc., so he signs as an officer with title. DocuSign handles this through its title field; on a paper form, Raj would write his name + "President & CEO" beneath.

**What if Raj also performs services personally to Northbridge outside the corp?** That would be a separate engagement, with a separate W-9 — under Raj's personal name + SSN, classified as Individual/sole proprietor. Mixing personal and corporate work on one W-9 is not allowed. The IRS treats them as different taxpayers.

## What if Patel Consulting were an LLC instead of a corporation?

Same Raj, same engagement, same federal S-corp tax treatment — but if the entity had been formed by filing **Articles of Organization** in Delaware (an LLC) instead of Articles of Incorporation, the W-9 would be:

| Line | Corp (above) | LLC with S-corp election |
|------|--------------|--------------------------|
| **Line 1** | Patel Consulting Inc. | Patel Consulting LLC |
| **Line 3a** | S Corporation | Limited liability company |
| **LLC letter** | n/a | S |
| **Part I** | Corp's EIN | LLC's EIN |
| **Code 5 on Line 4** | Yes | Yes (LLC taxed as S-corp inherits the corporate exemption) |

The federal tax outcome is identical. The W-9 box selection differs because Line 3a captures the legal-entity form, not just the federal tax election.

## Handoff: what the requestor (Northbridge) does next

Northbridge stores Patel Consulting Inc.'s W-9 in their vendor master with the Code 5 exemption flag. Through 2026, Northbridge tracks the $144,000 in payments under the SOW. At year-end:

- **1099-NEC**: Generally NOT required for payments to a corporation (IRC §6041, Treas. Reg. §1.6041-3(p) general exemption). Northbridge may opt to issue a 1099-NEC anyway as a courtesy or per their internal policy — the corp Code 5 exemption shields it from BUW regardless.
- **No backup withholding**: W-9 on file, valid TIN matching the corporate name, Code 5 exemption certified.
- **State 1099 filing**: Some states (CA, NY, MA, etc.) require 1099 filing thresholds different from federal. Northbridge's state-tax team handles those independently.

Patel Consulting Inc. then files its 2026 Form 1120-S by March 15, 2027 (or with extension by September 15, 2027), reporting the $144,000 as gross receipts. Raj receives:
- A **W-2** from Patel Consulting for his reasonable salary (e.g., $80,000)
- A **Schedule K-1** for the remaining S-corp pass-through profit, taxed on his personal Form 1040

Both flow into Raj's personal return — but neither uses the W-9 with Northbridge as input. The W-9 only governs the corp-to-corp payment relationship.

## Audit-defense documentation the corp keeps

- DocuSign audit trail (signer email, IP, timestamp, tamper-evident seal)
- Copy of the completed W-9 in the corporation's records (encrypted, retained at minimum 4 years per IRS records-retention guidance)
- Form 2553 IRS acceptance letter (proves S-corp election is valid)
- Articles of Incorporation (proves entity is a corporation, not an LLC)
- Corporate resolution authorizing Raj to sign W-9s on behalf of the corp (not strictly required when there's a sole officer, but good practice for audit defense)

## Sources cited in this draft

- IRS Form W-9 (Rev. March 2024)
- IRS Instructions for Form W-9 (Rev. March 2024)
- IRC §3406 (backup withholding; Code 5 corporation exemption per IRC §3406(g))
- IRC §6041 (information return reporting for ordinary payments)
- Treas. Reg. §1.6041-3(p) (general exemption from 1099 reporting for payments to corporations; exceptions for legal services and medical/healthcare services)
- IRC §6109 (TIN furnishing requirement)
- IRC §1361-1378 (S-corporation tax provisions, Subchapter S)
- Form 2553 (Election by a Small Business Corporation)
- Form 1120-S (US Income Tax Return for an S Corporation)
- IRS Publication 1345 (e-signature standards for tax forms)
