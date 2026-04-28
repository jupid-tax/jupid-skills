# Form 8919 Reason Codes — Decision Tree

Form 8919 Line 1 column (c) requires a single-letter reason code explaining why the worker is using Form 8919 instead of Schedule SE. The valid codes are A, C, G, and H. Picking the wrong code invalidates the filing.

This document is a decision tree for the agent to pick the correct code with the user.

---

## Quick Reference Table

| Code | Trigger | SS-8 Required? | Typical Use |
|------|---------|----------------|-------------|
| **A** | IRS already determined worker = employee | Yes (already filed) | After a successful SS-8 |
| **C** | Same firm issued W-2 + 1099 for same job | No | Employer split your pay between W-2 and 1099 wrongly |
| **G** | SS-8 filed, awaiting determination | Yes (just filed or about to file) | **Most common** for misclassified workers |
| **H** | Same firm issued W-2 + 1099, then W-2c that didn't fix it | Optional | Employer corrected the W-2 but didn't include the 1099 amount |

---

## Decision Tree

```
Did the user file Form SS-8 with the IRS?
├── No
│   │
│   Did the SAME firm issue both a W-2 AND a 1099 for the SAME work?
│   ├── Yes
│   │   │
│   │   Did the firm later issue a W-2c that did NOT add the 1099 amount as wages?
│   │   ├── Yes  → CODE H
│   │   └── No   → CODE C
│   │
│   └── No → STOP. The user must file Form SS-8 first to use codes A or G.
│            (Or, if they have W-2 + 1099 from same firm without SS-8, use code C/H.)
│
└── Yes
    │
    Has the IRS issued a determination letter ruling worker = employee?
    ├── Yes → CODE A
    └── No (still pending) → CODE G
```

---

## Code A: IRS Determination Letter on File

**When to use:** The user filed Form SS-8 in a prior year, and the IRS issued a determination letter ruling that the user is an employee of the firm.

**Required:**
- Form SS-8 filed (the user has proof — typically a copy of the SS-8 they mailed and the IRS determination letter)
- IRS determination letter ruling worker = employee
- Determination letter date entered in Form 8919 column (d)
- SS-8 box checked in column (e)

**Example:** Maya filed SS-8 for tax year 2024 in February 2025. The IRS issued a determination letter dated October 15, 2025, ruling Maya was an employee of XYZ Marketing. For her 2025 1040 (filed April 2026), Maya uses code A on Form 8919, enters 10/15/2025 in column (d), and checks the SS-8 box.

**Audit defense:** The determination letter is conclusive for Maya's specific situation with XYZ Marketing. The IRS has already ruled. Form 8919 with code A is rarely challenged at audit because the underlying classification has been adjudicated.

**Subsequent years:** If the work relationship continues unchanged, Maya can use code A in subsequent years too (referencing the same determination date) until the relationship ends or materially changes.

---

## Code C: Same Firm, W-2 + 1099, Same Job

**When to use:** The same firm issued the user both a W-2 and a 1099-MISC/NEC for the same work in the same year, and the 1099 portion should have been reported as wages on the W-2.

**No SS-8 required** — the misclassification is self-evident from the firm's own filings (issuing two forms for one job).

**Required:**
- W-2 from the firm (with some wages reported)
- 1099-MISC or 1099-NEC from the SAME firm
- Both forms are for the same work / same job
- 1099 amount entered in Form 8919 column (f)
- SS-8 box left unchecked
- Date column (d) typically blank

**Example:** Joel works as an in-house designer at Acme Studios. Acme runs payroll on him for 40 hours/week ($60,000 W-2). For "extra projects" outside the 40 hours, Acme paid Joel an additional $18,000 reported on a 1099-NEC. The "extra projects" were the same kind of design work, on Acme's premises, with Acme's tools — they should have been wages.

For tax year 2026, Joel files Form 8919 with code C, listing Acme Studios with $18,000 in column (f). The W-2 portion remains separately reported on Form 1040 Line 1a.

**Audit defense:** Code C cases are usually clear-cut. The agent should ensure the user has documentation that the 1099 work was the same as the W-2 work (same role, same supervision, same location).

---

## Code G: SS-8 Filed, Determination Pending

**When to use:** The user filed Form SS-8 (or is filing it now), reasonably believes they are an employee, and is filing Form 8919 with the 1040 before the IRS has issued a determination.

**This is the most common code** for proactive misclassified workers.

**Required:**
- Form SS-8 filed with the IRS (proof of mailing recommended)
- User has a reasonable basis to believe they are an employee (common-law test result)
- SS-8 box checked in column (e)
- Date column (d) typically blank (or date of any IRS correspondence acknowledging receipt of SS-8)

**Example:** Ana works full-time at ABC Consulting and was paid $72,000 on a 1099-NEC. She files SS-8 in February 2027 with documentation showing ABC sets her hours, supplies her equipment, and supervises her work. By April 15, 2027, the IRS has acknowledged receipt of SS-8 but has not yet issued a determination.

Ana files Form 1040 with Form 8919 attached, code G, on April 15. She mails the SS-8 in February with certified mail return receipt; she keeps the green card as proof of filing.

**Risk:** If the IRS later rules **against** Ana (rules her a contractor), she will need to amend her 1040 to file Schedule SE instead. The amendment will assess the difference (full SE tax minus the FICA she already paid) plus interest. There is no penalty for a good-faith filing — the IRS recognizes that SS-8 determinations can take 6-12 months and workers shouldn't have to wait to file their 1040.

**Reasonable basis:** "Reasonable basis" means the user has documented evidence of the common-law test factors pointing toward employee status. It is a low bar but not zero — a worker who has multiple clients, sets their own hours, and uses their own equipment cannot reasonably claim employee status.

---

## Code H: W-2 + 1099 + W-2c That Didn't Fix It

**When to use:** The user got a W-2 and a 1099 from the same firm (like code C), then the firm issued a Form W-2c (corrected W-2). The W-2c, however, did **not** add the 1099 amount to wages — it left the misclassification unresolved.

**Required:**
- W-2 from the firm
- 1099-MISC or 1099-NEC from the same firm
- W-2c subsequently issued by the firm
- The W-2c does **not** reclassify the 1099 amount as wages
- 1099 amount entered in Form 8919 column (f)

**Example:** Continuing the Joel/Acme case, suppose Acme was audited for unrelated reasons and issued Joel a W-2c correcting his W-2 wages by +$2,000 (a withholding error). The W-2c left the $18,000 1099 amount alone. Joel uses code H instead of code C because the firm acted but didn't fix the misclassification.

**Audit defense:** Like code C, code H is usually clear-cut. The W-2c is documentary evidence that the firm reconsidered the W-2 reporting but chose not to correct the misclassification.

---

## Why Other Codes Don't Apply

The form historically had codes B, D, E, and F for various employer remediation scenarios. Most are now retired or apply to extremely narrow situations. **Workers should not use B, D, E, or F.** If your situation seems to fit one of those, it almost certainly fits A, C, G, or H instead — re-run the decision tree.

---

## Multiple Firms, Multiple Codes

If the user has misclassified income from multiple firms, each row on Line 1 has its own code. Common patterns:

- Two firms, both code G (filed SS-8 for both, both pending) → two rows, code G on each
- One firm code C (W-2 + 1099 same job), one firm code G (SS-8 pending) → two rows with different codes
- One firm code A (prior determination), one firm code G (new SS-8) → two rows with different codes

Each row stands on its own. The validation: every row's reason code must match the user's documentation for that specific firm.

---

## What If the Reason Doesn't Fit Any Code?

If the user genuinely believes they are misclassified but the situation doesn't fit codes A, C, G, or H — for example, no SS-8 has been filed and there's no W-2 from the same firm — **the user cannot use Form 8919 yet**.

The path forward:

1. File Form SS-8 immediately (mail to Holtsville, NY 11742-0631)
2. Wait for the SS-8 mailing to be acknowledged by the IRS (or for proof of certified mail)
3. File Form 1040 with Form 8919, code G, citing the SS-8 filing

Without an SS-8 filing, code G is invalid. Without a W-2 from the same firm, codes C and H are invalid. Without a determination letter, code A is invalid. SS-8 is the gating step for the majority of misclassification cases.

---

## Sources

- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf) — current revision
- [Form SS-8](https://www.irs.gov/pub/irs-pdf/fss8.pdf)
- [About Form SS-8](https://www.irs.gov/forms-pubs/about-form-ss-8)
- IRC §7436 — Judicial review of employment status determinations
- IRC §3121(d) — Definition of "employee"
