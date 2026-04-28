# Reconciling 1099-K to Schedule C / Schedule 1 / Schedule E / Form 8949

The reconciliation worksheet is the audit-defense artifact for any 1099-K reconciled return. This file covers how to build it.

---

## Why reconciliation matters

The IRS receives the PSE's copy of every 1099-K. Document matching runs against the recipient's return:

- IRS sees: Box 1a from the 1099-K
- IRS expects: an amount equal to or greater than Box 1a appearing on the recipient's return (across Schedule C Line 1, Schedule E Line 3, Schedule 1 Line 8j, Schedule 1 Line 8z, Form 8949)

If the IRS can't see at least Box 1a worth of income on the return, the system generates a CP2000 notice proposing additional tax + interest + penalties.

The reconciliation worksheet is the artifact that:

1. Proves Box 1a was fully reported (split across multiple destinations is fine)
2. Documents the classification of each portion
3. Defends against a CP2000 by showing the work

Keep it for at least 6 years with the rest of the return.

---

## The reconciliation worksheet structure

```markdown
# 1099-K Reconciliation — <Tax Year>

## Source 1099-K
- PSE: <Name + EIN>
- Recipient: <Name + TIN>
- Box 1a (Gross): $<amount>
- Box 1b (CNP): $<amount>
- Box 2 (Transactions): <count>
- Box 4 (Federal tax withheld): $<amount>

## Activity classification
| Portion | Amount | Classification | Destination |
|---------|--------|----------------|-------------|
| <Description> | $<amount> | Trade or business | Schedule C Line 1 |
| <Description> | $<amount> | Personal payment | Schedule 1 Line 8z + Line 24z (net $0) |
| <Description> | $<amount> | Personal-item loss | Schedule 1 Line 8z + Line 24z (net $0) |
| <Description> | $<amount> | Personal-item gain | Form 8949 |
| **Total** | **$<should equal Box 1a>** | | |

## Reconciliation to platform records
| Source | Amount | Match? |
|--------|--------|--------|
| 1099-K Box 1a | $<amount> | — |
| Platform year-end gross report | $<amount> | <yes/no, with explanation if no> |
| Sum of monthly bank deposits | $<amount> | <yes/no, with timing notes> |

## Other 1099s for same income (double-reporting check)
| Other form | Issuer | Amount | Resolution |
|------------|--------|--------|-----------|
| 1099-NEC | <Client> | $<amount> | Already counted in Schedule C Line 1 — same payment, reported once |

## Ledger of return entries
| Form / line | Amount | Cross-reference |
|-------------|--------|-----------------|
| Schedule C Line 1 | $<amount> | Trade portion + non-1099 cash sales |
| Schedule C Line 2 (Returns) | $<amount> | Refunds + chargebacks |
| Schedule C Line 10 (Commissions and fees) | $<amount> | Platform processing fees |
| Schedule 1 Line 8z | $<amount> | Personal portion |
| Schedule 1 Line 24z | $<amount> | Offset of personal portion |
| Schedule 1 Line 8j | $<amount> | Hobby portion (if any) |
| Form 8949 Part I/II | $<amount> | Personal-item gains (if any) |
| Form 1040 Line 25c | $<Box 4> | Backup withholding credit |

## Validation
- Sum of classified portions equals Box 1a: <yes/no>
- Personal portion offset on Line 24z matches Line 8z: <yes/no>
- All trade-or-business portion appears in Schedule C Line 1 or Schedule E Line 3: <yes/no>
- Box 4 amount appears on Form 1040 Line 25c: <yes/no>
```

---

## Step-by-step reconciliation

### Step 1 — Pull source records

- The 1099-K(s) for the year (paper or PDF download from the platform)
- The platform's year-end gross-payments report (most platforms expose this in tax-time settings)
- The user's bank statements showing deposits from the platform
- Any other 1099s the user received (1099-NEC, 1099-MISC, 1099-DA)
- The user's own bookkeeping for the year (cash sales, expense receipts, mileage log)

### Step 2 — Classify each transaction

Using `personal-vs-business.md`, group transactions by classification. For mixed-use accounts (a single Venmo or PayPal used for both freelance and personal), the user has to look at the actual transactions, not just the summary.

A useful technique: export the platform's transaction CSV, add a "Classification" column, and tag each row. Sum by classification at the end. The sum should equal Box 1a (within a few cents of rounding).

### Step 3 — Cross-check against platform records

The 1099-K Box 1a should match the platform's own year-end gross-payments report. If they differ:

- **By a few dollars** — rounding, FX timing, settlement-date differences. Note and proceed.
- **By tens or hundreds** — investigate. Common causes: chargebacks reversed across year boundaries, multiple linked accounts, currency conversion timing.
- **By thousands** — likely a real error. Request a corrected 1099-K from the PSE before filing.

### Step 4 — Cross-check against bank deposits

Sum of monthly bank deposits from the platform (Box 5a + 5b + ... + 5l) should match Box 1a. They might not match the bank-deposit total exactly because:

- Settlement-date vs deposit-date timing (December 2026 settlement deposited January 2, 2027 still 2026 gross)
- Platform fees deducted before deposit (if the user gets net deposits, those won't equal gross)
- ACH return-fail-redo cycles

For most users, the bank-deposit cross-check is informational, not definitive. The platform's settlement records win.

### Step 5 — Cross-check against other 1099s (double-reporting)

If a client paid the user $5,000 through PayPal and the client (mistakenly or correctly) also issued a 1099-NEC for the same $5,000, the user has overlapping 1099s.

The income is taxable **once**. Two ways to handle:

1. **Report on Schedule C Line 1 once**, keep records showing the overlap. If the IRS sends a CP2000, respond with the reconciliation worksheet showing the overlap.
2. **Ask the issuing client to correct the 1099-NEC** (rescind it because the payment was via a third-party network and the 1099-K already reports it). Some clients will, some won't.

The general rule (per IRS Form 1099-K FAQs): when payments flow through a third-party network, the network is the responsible reporter and the client should NOT issue a 1099-NEC for those same payments. But many clients issue 1099-NECs anyway. Document the overlap; report once.

### Step 6 — Build the ledger

For each portion, identify the destination (Schedule C / Schedule 1 / Schedule E / Form 8949) and the specific line. Note the amount. The total of destinations equals Box 1a.

### Step 7 — Validate

Run all the validation checks in `SKILL.md` Validation section.

### Step 8 — Save

Save the worksheet as a PDF along with the 1099-K(s) and other 1099s in the user's tax records folder for the year. Keep at least 6 years.

---

## Corrected 1099-K workflow

If the user determines the 1099-K is wrong:

1. Document the discrepancy with screenshots from the platform
2. Contact the PSE's tax support — most platforms have a "Request 1099-K correction" workflow in their help center
3. Provide the corrected information needed
4. Wait 4-6 weeks for a corrected form (Form 1099-K with the "CORRECTED" box checked)
5. File using the corrected form

If the deadline approaches without a corrected form:

- File Form 4868 for an extension (until October 15)
- Or file using the user's own records and attach a written explanation

Never file with a known-wrong 1099-K and "fix it later" — that creates an automatic CP2000 mismatch.

---

## CP2000 response workflow

If the IRS sends a CP2000 alleging under-reported 1099-K income:

1. Read the notice carefully. It identifies the discrepancy.
2. Check the user's reconciliation worksheet for the year in question
3. If the user reported correctly, respond by mail (address on the CP2000) with:
   - The signed CP2000 response page indicating disagreement
   - The reconciliation worksheet
   - A brief cover letter explaining where each portion of Box 1a appears on the return
   - Copies of all 1099s and supporting documents
4. Mail by the deadline (usually 30 days from notice date) via certified mail with return receipt
5. Do NOT amend the original return — CP2000 is its own resolution channel

The reconciliation worksheet is designed to be the response artifact. Submit it as-is with the cover letter.

---

## Common reconciliation pitfalls

| Pitfall | Why it's wrong | Fix |
|---------|----------------|-----|
| Subtracting platform fees from Box 1a before reporting Line 1 | Creates IRS document-mismatch | Report gross on Line 1, deduct fees on Line 10 |
| Reporting only the business portion as Schedule C | IRS can't see where personal portion went | Report full Box 1a across destinations; offset personal on Line 24z |
| Reporting personal payments as Schedule C income | Pays unnecessary 15.3% SE tax | Reroute to Schedule 1 Line 8z + Line 24z |
| Reporting Etsy sales as hobby when it's actually trade/business | Loses Schedule C deductions | Apply the §183 9-factor test; profit motive + regularity = business |
| Excluding sub-threshold cash sales from Schedule C | All income is taxable | Add cash sales to Schedule C Line 1 alongside 1099-K portion |
| Mixing two PSEs' Box 1a into one entry | Loses traceability for CP2000 defense | Reconcile each 1099-K independently |
| Forgetting Box 4 federal withholding | Misses a refundable credit | Claim on Form 1040 Line 25c |

---

## Sources

- IRC §6050W (1099-K reporting)
- IRC §61 (gross income)
- IRC §162 (trade or business expenses)
- IRC §165 (losses; personal-use property losses not deductible)
- IRC §1221 (capital asset definition)
- [IRS Form 1099-K FAQs](https://www.irs.gov/newsroom/form-1099-k-faqs)
- [IRS CP2000 notice information](https://www.irs.gov/individuals/understanding-your-cp2000-notice)
- IRS Notice 2023-74 (personal-item resale guidance)
- [Schedule C (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-c-form-1040)
- [Schedule E (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-e-form-1040)
- [Schedule 1 (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-1-form-1040)
- [Form 8949](https://www.irs.gov/forms-pubs/about-form-8949)
