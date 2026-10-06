# Form W-9 — Tax classification decision tree (Line 3a)

Decision tree for picking the correct Line 3a checkbox (Form W-9, Rev. March 2024: "Check the appropriate box on line 3a for the U.S. federal tax classification of the person whose name is entered on line 1"). The most-misfiled section of W-9 is Line 3a for LLC owners — this file is the canonical reference.

---

## Top-level question: what's the legal form of the filer?

```
Q: Are you filing as an individual (no formal entity) OR with a single-member LLC OR with a multi-member entity OR as a corporation OR as a trust/estate?

  Individual / sole prop (no LLC)        → Section A
  Single-member LLC (SMLLC)              → Section B
  Multi-member LLC                       → Section C
  Corporation (formed as such)           → Section D
  Partnership (formed as such, not LLC)  → Section E
  Trust or estate                        → Section F
```

---

## Section A — Individual / sole proprietor (no LLC)

The filer operates as themselves, filing Schedule C with their Form 1040. May or may not have an EIN.

- **Line 3a checkbox:** `Individual/sole proprietor`
- **LLC classification letter:** n/a (do not check the LLC box)
- **TIN (Part I):** SSN (or ITIN if applicable). A sole proprietor who has an EIN may enter either the SSN or the EIN; the IRS encourages the SSN.

Examples:
- Freelance graphic designer with no LLC → Individual/sole proprietor + SSN
- Uber driver with no entity → Individual/sole proprietor + SSN
- Consultant operating under a DBA, no LLC → Individual/sole proprietor + SSN; DBA goes on Line 2

---

## Section B — Single-member LLC (SMLLC)

The single biggest source of W-9 errors. The answer depends entirely on whether the SMLLC has made a tax election.

### Section B.1 — SMLLC, no corporate election (default = disregarded entity)

This is the default for an SMLLC unless the owner has filed Form 2553 or Form 8832. The IRS treats the LLC as if it doesn't exist for federal income tax — the owner files Schedule C just like a sole proprietor.

- **Line 1:** Owner's personal legal name
- **Line 2:** LLC name (e.g., "Garcia Design LLC")
- **Line 3a checkbox:** `Individual/sole proprietor`
- **LLC classification letter:** n/a (do NOT check the LLC box)
- **TIN (Part I):** Owner's SSN, or the owner's own EIN if the owner has one (NOT the LLC's EIN, even if the LLC has one)

Rev. March 2024 What's New: "An LLC that is a disregarded entity should check the appropriate box for the tax classification of its owner." For an individual owner that is "Individual/sole proprietor" (the box no longer says "or single-member LLC"). If the owner is a foreign person, the owner gives a Form W-8 instead of a W-9.

**The trap:** owners check "Limited liability company" on Line 3a, write "S" or nothing for the classification, and put the LLC's EIN in Part I. The IRS then can't match the 1099 to the owner's SSN, sends a "B" notice to the requestor, and the requestor applies 24% backup withholding.

### Section B.2 — SMLLC with S-corp election (Form 2553 filed)

The owner has filed Form 2553 to elect S-corporation taxation for the LLC. The LLC is now treated as a separate taxpayer for federal income tax.

- **Line 1:** LLC's legal name
- **Line 2:** Blank (or DBA, if any)
- **Line 3a checkbox:** `LLC`
- **LLC classification letter:** `S`
- **TIN (Part I):** LLC's EIN (NOT the owner's SSN)

### Section B.3 — SMLLC with C-corp election (Form 8832 filed)

The owner has filed Form 8832 to elect C-corporation taxation for the LLC. Rare but possible.

- **Line 1:** LLC's legal name
- **Line 2:** Blank (or DBA, if any)
- **Line 3a checkbox:** `LLC`
- **LLC classification letter:** `C`
- **TIN (Part I):** LLC's EIN

---

## Section C — Multi-member LLC

Default is partnership taxation; can elect S-corp or C-corp.

### Section C.1 — Multi-member LLC, no corporate election (default = partnership)

- **Line 1:** LLC's legal name
- **Line 2:** Blank (or DBA, if any)
- **Line 3a checkbox:** `LLC`
- **LLC classification letter:** `P`
- **Line 3b:** check only if the LLC has foreign partners and is giving the W-9 to a partnership, trust, or estate it owns an interest in
- **TIN (Part I):** LLC's EIN

### Section C.2 — Multi-member LLC with S-corp election

- **Line 1:** LLC's legal name
- **Line 3a checkbox:** `LLC`
- **LLC classification letter:** `S`
- **TIN (Part I):** LLC's EIN

### Section C.3 — Multi-member LLC with C-corp election

- **Line 1:** LLC's legal name
- **Line 3a checkbox:** `LLC`
- **LLC classification letter:** `C`
- **TIN (Part I):** LLC's EIN

---

## Section D — Corporation (S-corp or C-corp formed as such)

The entity was formed by filing Articles of Incorporation (not Articles of Organization, which is for LLCs).

### Section D.1 — S Corporation

Filed Articles of Incorporation + Form 2553 to elect S-corp status.

- **Line 1:** Corporation's legal name
- **Line 3a checkbox:** `S Corporation` (NOT the LLC box)
- **TIN (Part I):** Corporation's EIN

### Section D.2 — C Corporation

Filed Articles of Incorporation; no S-corp election.

- **Line 1:** Corporation's legal name
- **Line 3a checkbox:** `C Corporation`
- **TIN (Part I):** Corporation's EIN

**Note for corporations:** Most payments to a C-corp or S-corp are exempt from 1099-NEC reporting (the requestor doesn't have to file a 1099 at year-end). Exceptions: payments to attorneys (fees and gross proceeds, regardless of entity type) and medical/health-care payments (Reg. §1.6041-3(p)(1)).

---

## Section E — Partnership (general or limited, not an LLC)

Formed by partnership agreement; files Form 1065.

- **Line 1:** Partnership's legal name
- **Line 3a checkbox:** `Partnership`
- **TIN (Part I):** Partnership's EIN

---

## Section F — Trust or estate

Trust formed by trust instrument; estate of a deceased person.

- **Line 1:** Trust's or estate's legal name (e.g., "John Doe Revocable Trust" or "Estate of John Doe")
- **Line 3a checkbox:** `Trust/estate`
- **TIN (Part I):** Trust's or estate's EIN

Grantor trusts depend on the account and filing method (W-9 "What Name and Number To Give the Requester" chart): a revocable trust where the grantor is also trustee, or a grantor trust using Optional Filing Method 1, gives the grantor's name and SSN (Line 3a then follows the grantor, e.g., Individual/sole proprietor); a grantor trust filing Form 1041 or using Optional Filing Method 2 gives the trust's name and EIN. Ask which applies.

---

## Quick lookup table

| Filer described as... | Line 3a | LLC letter | Line 1 | TIN |
|-----------------------|---------|-----------|--------|-----|
| Freelancer, no LLC | Individual/sole prop | n/a | Personal name | SSN |
| Sole prop with EIN, no LLC | Individual/sole prop | n/a | Personal name | SSN or own EIN (IRS encourages SSN) |
| SMLLC, default (disregarded) | Individual/sole prop (owner's box) | n/a | Owner's personal name | Owner's SSN (or owner's own EIN) |
| SMLLC, S-corp election | LLC | S | LLC name | LLC's EIN |
| SMLLC, C-corp election | LLC | C | LLC name | LLC's EIN |
| Multi-member LLC, partnership default | LLC | P | LLC name | LLC's EIN |
| Multi-member LLC, S-corp | LLC | S | LLC name | LLC's EIN |
| Multi-member LLC, C-corp | LLC | C | LLC name | LLC's EIN |
| S-corp (Articles of Incorporation) | S Corporation | n/a | Corp name | Corp's EIN |
| C-corp (Articles of Incorporation) | C Corporation | n/a | Corp name | Corp's EIN |
| Partnership (not LLC) | Partnership | n/a | Partnership name | Partnership's EIN |
| Trust or estate | Trust/estate | n/a | Trust/estate name | Trust/estate's EIN |
| Grantor trust, Optional Filing Method 1 or revocable trust with grantor as trustee | Grantor's box (e.g., Individual/sole prop) | n/a | Grantor's name | Grantor's SSN |

---

## How to verify the user's tax classification

If the user isn't sure which box to check:

1. **"Did you form an LLC by filing Articles of Organization with the state?"**
   - Yes → it's an LLC; ask Q2
   - No, formed as a corporation → check S Corp or C Corp per Q3
   - No, no formal entity → Individual/sole prop

2. **"Have you filed Form 2553 (S-corp election) or Form 8832 (C-corp election) for the LLC?"**
   - Yes, Form 2553 → LLC + S
   - Yes, Form 8832 → LLC + C
   - No → ask Q4

3. **"Did you file Form 2553 for the corporation?"**
   - Yes → S Corporation
   - No → C Corporation

4. **"Is the LLC owned by one person or multiple?"**
   - One → Individual/sole proprietor (default disregarded)
   - Multiple → LLC + P (default partnership)

If the user can't answer Q2 or Q3 confidently, advise them to check with their CPA or check IRS records before completing the W-9. The wrong classification leads to TIN-matching failures and backup withholding that's hard to unwind.
