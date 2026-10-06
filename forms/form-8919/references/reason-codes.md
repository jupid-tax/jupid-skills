# Form 8919 Reason Codes — Decision Tree

Lines 1–5, column (c), of Form 8919 take a single-letter reason code explaining why the worker is filing the form. The 2025 Form 8919 lists four codes: A, C, G, and H. Enter only one reason code on each line. Picking a code the facts don't support exposes the worker to the IRS rejecting the employee treatment.

This document is a decision tree for the agent to pick the code with the user. Code text below is quoted from the 2025 Form 8919 (page 1 "Reason codes" and page 2 "Column (c)"); re-check the current revision at https://www.irs.gov/forms-pubs/about-form-8919.

---

## Quick Reference Table

| Code | Form text (2025) | Form SS-8? | Column (d) date |
|------|------------------|------------|-----------------|
| **A** | I filed Form SS-8 and received a determination letter stating that I am an employee of this firm. | Already filed and decided | Date of the determination letter |
| **C** | I received other correspondence from the IRS stating that I am an employee. (Includes a "section 530 employee".) | Not required | Date of the IRS correspondence |
| **G** | I filed Form SS-8 with the IRS and haven't received a reply. Also the fallback when no other code applies. | Must be filed on or before the date the return is filed | Leave blank |
| **H** | I received a Form W-2 and a Form 1099-MISC and/or 1099-NEC from this firm for the year. The 1099 amount should have been included as wages on Form W-2. | **Don't file Form SS-8** | Leave blank |

---

## Decision Tree

```
Did the SAME firm issue the user both a Form W-2 AND a Form 1099-MISC/1099-NEC
for the year, and the 1099 amount was really pay for services as an employee?
├── Yes → CODE H (do not file Form SS-8)
└── No
    │
    Does the user have an IRS determination letter (from Form SS-8) stating
    they are an employee of this firm?
    ├── Yes → CODE A (column (d) = letter date)
    └── No
        │
        Does the user have other IRS correspondence stating they are an employee
        of this firm (including a "section 530 employee" designation)?
        ├── Yes → CODE C (column (d) = correspondence date)
        └── No
            │
            Has the user filed Form SS-8 (or will they file it on or before
            the date they file the return)?
            ├── Yes → CODE G
            └── No  → STOP. Code G requires Form SS-8 filed on or before the
                      return. Offer to prepare SS-8 (references/ss-8-filing.md)
                      or route the income to Schedule C / Schedule SE.
```

---

## Code A: SS-8 Determination Letter on File

**When to use:** The user filed Form SS-8 and the IRS issued a determination letter stating the user is an employee of this firm.

**Required:**
- The determination letter (ask the user for its date; do not guess)
- Determination letter date entered in column (d)

**Example:** Maya filed Form SS-8 in February 2025. The IRS issued a determination letter dated October 15, 2025, stating Maya is an employee of XYZ Marketing. On her 2025 return (filed in 2026), Maya uses code A and enters 10/15/2025 in column (d).

**Scope:** The SS-8 instructions say a determination letter applies only to the worker (or class of workers) requesting it and is binding on the IRS if there is no change in the facts or law that form its basis (Instructions for Form SS-8, Rev. January 2024, "Issuance of determination"). If the work relationship changed materially, ask the user before reusing the letter for a later year.

**Information letter instead of a determination:** In some cases the IRS issues an information letter instead of a formal determination. An information letter is advisory and not binding on the IRS, but the worker may use it in fulfilling their federal tax obligations (same section). Ask the user which kind of letter they have. If it is IRS correspondence stating they are an employee, code C fits.

---

## Code C: Other IRS Correspondence Stating "Employee"

**When to use:** The user received IRS correspondence, other than an SS-8 determination letter, stating that they are an employee of this firm. Also use code C if the user was designated a "section 530 employee": determined by the IRS to be an employee, but the employer was granted relief from employment taxes under section 530 of the Revenue Act of 1978 (2025 Form 8919, page 2, "Column (c)").

**Required:**
- The IRS letter or notice (ask for a copy and its date)
- Date entered in column (d)

**Not code C:** a W-2 plus a 1099 from the same firm (that is code H), or the user's own belief without IRS paper (that is code G with Form SS-8).

---

## Code G: SS-8 Filed, No Reply Yet (and the Fallback Code)

**When to use:**
1. The user filed Form SS-8 with the IRS and hasn't received a reply, or
2. None of the other codes apply but the user believes they should have been treated as an employee. The form then says to enter code G **and file Form SS-8 on or before the date you file your tax return**. Form SS-8 is filed separately; do not attach it to the return.

**Required:**
- Form SS-8 filed (mail or fax) no later than the date the return is filed. Ask for proof: a fax confirmation, certified mail receipt, or the IRS acknowledgment of receipt.
- A documented common-law basis for employee status (`common-law-test.md`)
- Column (d) blank

**Example:** Ana works full-time at ABC Consulting and was paid $72,000 on a 1099-NEC for 2026. She mails Form SS-8 in February 2027 with documentation showing ABC sets her hours, supplies her equipment, and supervises her work. She files her 2026 return in April 2027 with Form 8919, code G, without waiting for the determination (the IRS says a determination may take at least six months).

**Risk (from the form):** If code G is entered, the worker or the firm may be contacted for additional information. Use of the code isn't a guarantee that the IRS will agree. If the IRS doesn't agree that the worker is an employee, the worker may be billed for the additional tax, penalties, and interest resulting from the change to worker status (2025 Form 8919, page 2 caution). Tell the user this before they choose code G.

**Documented basis:** The worker should have evidence of the common-law factors pointing toward employee status. A worker who has multiple clients, sets their own hours, and uses their own equipment does not have that basis.

---

## Code H: W-2 and 1099 From the Same Firm

**When to use:** The user received both a Form W-2 and a Form 1099-MISC and/or 1099-NEC from the same firm for the year, and the 1099 amount should have been included as wages on the W-2 because it was pay for services as an employee (2025 Form 8919, page 2, "Column (c)").

**Do not file Form SS-8** for code H (the form says so twice).

The form lists amounts that are sometimes put on a 1099 by mistake when they should be W-2 wages: employee bonuses, awards, travel expense reimbursements not paid under an accountable plan, scholarships, and signing bonuses.

**Required:**
- The W-2 from the firm
- The 1099-MISC/NEC from the same firm
- The 1099 amount (only the part that was employee pay) in column (f)
- Column (d) blank; column (e) checked (a 1099 was received)

**Example:** Joel is a W-2 graphic designer at Acme Studios ($60,000 on his W-2). Acme paid him another $18,000 for extra hours of the same design work, on Acme's premises and equipment, and reported it on a 1099-NEC. Joel enters Acme Studios with code H and $18,000 in column (f). He does not file Form SS-8.

---

## Codes Not on the Current Form

The 2007 Form 8919 also listed codes B (designated a "section 530 employee" before January 1, 1997), D (previously treated as an employee by the firm in a similar capacity), E (co-workers in similar roles treated as employees), and F (co-workers received SS-8 determinations as employees); D, E, and F had to be paired with G. These codes are not on the 2025 form. Do not enter them. If a user describes one of those situations today, the current form routes it to code G with Form SS-8 (or code C if they hold IRS correspondence).

---

## Multiple Firms, Multiple Codes

Each firm gets its own row and its own code. Common patterns:

- Two firms, both SS-8 pending → two rows, code G on each (a separate Form SS-8 for each firm, per the SS-8 instructions)
- One firm with W-2 + 1099 for employee pay (code H), one firm with SS-8 pending (code G) → two rows with different codes
- One firm with a prior determination letter (code A), one with a new SS-8 (code G) → two rows with different codes

Validation: every row's code must match the user's documents for that firm.

---

## What If No Code Fits?

There is always a fallback: code G with Form SS-8 filed on or before the return. If the user is not willing to file Form SS-8 and none of A, C, or H applies, **the user cannot use Form 8919 for that firm**. The income is reported as self-employment (Schedule C and Schedule SE) unless and until the classification changes.

---

## Sources

- [Form 8919 (2025)](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — reason codes, page 1; column instructions, page 2
- [Form 8919 (2007)](https://www.irs.gov/pub/irs-prior/f8919--2007.pdf) — historical codes B, D, E, F
- [Form SS-8 (Rev. December 2023)](https://www.irs.gov/pub/irs-pdf/fss8.pdf) and [Instructions (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/iss8.pdf)
- [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8)
- [Independent contractor (self-employed) or employee?](https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee) — "at least six months" for an SS-8 determination
- IRC §3121(d) — Definition of "employee"
