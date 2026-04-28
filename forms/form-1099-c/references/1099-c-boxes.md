# Form 1099-C — Box-by-Box Reference

Complete lookup for every box on Form 1099-C (Cancellation of Debt). The 1099-C is an information return — the **creditor** prepares it and sends one copy to the IRS and one to the borrower. The borrower (the agent's user) does **not** file the 1099-C itself; they use it as the input to their reporting decision on the 1040.

Form revision in scope: 2024-revision used for tax years 2024 and forward. Verify against the [current PDF](https://www.irs.gov/pub/irs-pdf/f1099c.pdf) before using for a specific tax year.

---

## Header (creditor and borrower identity)

| Field | What it contains | What the agent does with it |
|-------|------------------|------------------------------|
| Creditor's name, address, telephone | The lender or other party who canceled the debt | Record for the reporting plan; ask user to confirm the creditor matches a debt they recognize |
| Creditor's TIN | EIN of the creditor | Informational only |
| Debtor's name | The user's legal name | Must match the user's 1040 name; flag mismatch |
| Debtor's TIN | The user's SSN or ITIN | Must match the user's 1040 TIN; flag mismatch |
| Account number | Creditor's internal reference | Useful when the user has multiple accounts with the same creditor |

If the form is addressed to a different person (deceased relative, business entity, ex-spouse), redirect — see SKILL.md Step 1.

---

## Box 1 — Date of identifiable event

The date the creditor decided the debt was uncollectable or otherwise canceled it. **This date determines the tax year of reporting.**

- A 1099-C with Box 1 = 2025-08-15 is reported on the **2025** tax return (filed in 2026).
- If the creditor backdates or the date crosses a year boundary, trust Box 1 unless the user has documentation that a different date applies.
- For Box 6 = H (36-month nonpayment testing period), Box 1 is the date the testing period ended, **not** the date of the original default.

**Edge case:** If the user disputes that the debt was actually canceled on Box 1's date (e.g., they made a payment that month), they can request the creditor correct the form. Until corrected, report based on what's on the form and document the dispute.

---

## Box 2 — Amount of debt discharged

The dollar amount of debt the creditor canceled, in U.S. dollars. **This is the income figure** — either reportable as income on the 1040 or excludable via Form 982.

Includes principal + capitalized fees + (per Box 3) interest if the creditor included it.

The creditor reports a 1099-C only if Box 2 is **$600 or more** (Treas. Reg. §1.6050P-1). Below that threshold the creditor is not required to issue the form, but the cancellation may still be income to the borrower.

**Sanity check:** Box 2 should match the borrower's recollection of the canceled balance. Common mismatches:

- Creditor included accrued interest the borrower didn't expect → see Box 3
- Creditor canceled less than the full balance because the borrower paid part → Box 2 = forgiven portion only, not original balance
- Creditor wrote off statute-of-limitations debt the borrower thought was already gone → still reportable

---

## Box 3 — Interest, if included in Box 2

The portion of Box 2 that represents accrued unpaid interest the creditor canceled.

**Why this matters:** Cash-method individual taxpayers generally do **not** have a basis in unpaid interest (because they never paid it and never deducted it). For a personal-use debt, the interest portion in Box 3 is still includable as canceled debt income. The Box 3 amount is informational — it does **not** reduce Box 2 for reporting purposes.

For business debt where the borrower previously deducted accrued interest on their books (rare for cash-method solos), an offsetting deduction may be available — out of scope for the typical consumer situation; consult Pub 4681 Chapter 1.

---

## Box 4 — Debt description

A short text description of what the debt was for. Examples seen on actual 1099-Cs:

- "Credit card"
- "Mortgage"
- "Home equity loan"
- "Auto loan deficiency"
- "Personal loan"
- "Federal Direct Loan" (student)
- "Business credit line"
- "Vendor account"
- "Medical services"

**The agent uses Box 4 to classify personal vs. business** in SKILL.md Step 3. If Box 4 is ambiguous (e.g., "Credit card" but the user used the card for business expenses), ask the user how they used the proceeds — that determines the routing target.

---

## Box 5 — Was the borrower personally liable for repayment?

A Yes/No checkbox.

- **Yes** = recourse debt. The borrower was personally on the hook. If foreclosure / repo, the deficiency cancellation is what's in Box 2.
- **No** = nonrecourse debt. The lender's only remedy was the collateral. Different tax mechanics — the cancellation in Box 2 may not fully apply; instead, the bid price at foreclosure is treated as the amount realized, and any "phantom" cancellation may not exist for income purposes.

**For the typical consumer 1099-C (credit card, personal loan), Box 5 is Yes.** For mortgage cancellations in foreclosure or short sale, check the deed and loan documents — purchase-money mortgages in some states are nonrecourse, others are recourse. See [Pub 4681 Chapter 2](https://www.irs.gov/publications/p4681) for the foreclosure/abandonment analysis.

---

## Box 6 — Identifiable event code

A single letter A through I describing **why** the creditor canceled the debt. This drives the agent's initial exclusion analysis.

| Code | Meaning | Agent's first move |
|------|---------|---------------------|
| **A** | Bankruptcy (Title 11 case — Chapter 7, 11, 12, 13) | Confirm Title 11 discharge order; default to §108(a)(1)(A) full exclusion via Form 982 Box 1a |
| **B** | Other judicial debt relief — receivership, foreclosure, or similar federal/state court proceeding | Likely cancellation; analyze under foreclosure rules + insolvency |
| **C** | Statute of limitations or expiration of deficiency period | Treat as discharged; test exclusions normally |
| **D** | Foreclosure election under §1604(g)(2) of FDIC Improvement Act | Rare; FDIC-related; analyze under foreclosure rules |
| **E** | Debt relief from a probate proceeding | Decedent-related; out of scope for individual reporting — redirect to estate return |
| **F** | By agreement (negotiated settlement) | Most common consumer code; test all exclusions |
| **G** | Decision or policy of the creditor to discontinue collection | Common for charge-offs; test all exclusions |
| **H** | Expiration of nonpayment testing period (36-month rule) | Common for charge-offs after 36 months of nonpayment; test all exclusions; **Box 1 date = end of testing period, not original default** |
| **I** | Other identifiable event | Catch-all; test all exclusions; ask user for context |

**Codes F and G cover the bulk of consumer 1099-Cs.** Code A is the only code that auto-flags a clean exclusion path; everything else requires testing insolvency and the situation-specific exclusions.

**Important:** Box 6 = A does **not** automatically grant the exclusion — the user must have an actual Title 11 discharge order. If the bankruptcy is pending or was dismissed, the exclusion does not apply.

---

## Box 7 — Fair market value of property

If the cancellation accompanied a foreclosure or repossession, the FMV of the property at the time of the foreclosure/repossession.

**Used for:** the foreclosure gain/loss analysis under Pub 4681 Chapter 2. The borrower may have **two** taxable events from a single foreclosure:

1. **Sale or other disposition of the property** (gain or loss) — uses Box 7 as amount realized for nonrecourse, or the lower of Box 7 / outstanding debt for recourse
2. **Cancellation of debt income** — Box 2 (if recourse and Box 5 = Yes)

For nonrecourse debt (Box 5 = No), the entire deficiency is folded into the sale analysis; there is no separate cancellation-of-debt income.

For recourse debt (Box 5 = Yes), the sale uses Box 7 as the amount realized, and the difference between Box 7 and the outstanding loan balance is the cancellation amount in Box 2.

If the user received a 1099-A in the same year (Acquisition or Abandonment of Secured Property), the foreclosure analysis layers on top of the cancellation analysis. See [Pub 4681 Chapter 2](https://www.irs.gov/publications/p4681).

---

## What's NOT on the form

The 1099-C does **not** include:

- Any indication of whether an exclusion applies — the creditor doesn't analyze the borrower's situation
- The borrower's basis in the debt or related property
- The borrower's insolvency position
- Whether the debt is personal or business — the agent infers from Box 4 and asks the user

The agent must collect these inputs from the user (see SKILL.md Prerequisites).

---

## Common box-reading mistakes

1. **Treating Box 2 as a tax bill** — it's the income amount, not the tax. At a 22% marginal bracket, $13,000 in Box 2 = roughly $2,860 of federal tax. And exclusions can wipe it to zero.
2. **Ignoring Box 3** — agents sometimes subtract Box 3 from Box 2 because "interest is different." It's not. Box 3 is informational; Box 2 is the income figure.
3. **Reading Box 6 = E as relevant to a living debtor** — Code E is probate-only and almost always means the form was sent to the wrong person or the wrong address.
4. **Skipping Box 5 on a foreclosure 1099-C** — the recourse vs. nonrecourse distinction changes the entire analysis.
5. **Assuming Box 6 = A means the exclusion is automatic** — confirm the bankruptcy discharge order exists.

---

## Sources

- [Form 1099-C (PDF)](https://www.irs.gov/pub/irs-pdf/f1099c.pdf) — current revision
- [Instructions for Forms 1099-A and 1099-C (PDF)](https://www.irs.gov/pub/irs-pdf/i1099ac.pdf) — IRS line-by-line guidance for creditors (useful for understanding what Box 6 codes mean to the issuer)
- [Publication 4681](https://www.irs.gov/publications/p4681) — Canceled Debts, Foreclosures, Repossessions, and Abandonments (the canonical reference for borrowers)
- Treas. Reg. §1.6050P-1 — creditor reporting requirements
