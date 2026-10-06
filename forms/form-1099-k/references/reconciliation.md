# Reconciling 1099-K to Schedule C / Schedule 1 / Schedule E / Form 8949

The reconciliation worksheet is the audit-defense artifact for any 1099-K reconciled return. This file covers how to build it.

---

## Why reconciliation matters

The IRS receives the PSE's copy of every 1099-K. Document matching runs against the recipient's return:

- IRS sees: Box 1a from the 1099-K
- IRS expects: an amount equal to or greater than Box 1a accounted for on the recipient's return (across Schedule C Line 1, Schedule E Line 3, Schedule 1 Line 8j, Form 8949, and the 1099-K entry space at the top of Schedule 1 for amounts included in error or personal items sold at a loss)

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
- Transactions reported: <Payment card | Third party network>
- Box 1b (CNP; blank on third party network forms): $<amount>
- Box 3 (Transactions): <count>
- Box 4 (Federal tax withheld): $<amount>

## Activity classification
| Portion | Amount | Classification | Destination |
|---------|--------|----------------|-------------|
| <Description> | $<amount> | Trade or business | Schedule C Line 1 |
| <Description> | $<amount> | Personal payment | Schedule 1 entry space (top of form) |
| <Description> | $<amount> | Personal-item loss | Schedule 1 entry space (top of form) |
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
| Schedule 1 entry space (top of form) | $<amount> | Personal payments + personal items sold at a loss |
| Schedule 1 Line 8j | $<amount> | Hobby portion (if any) |
| Form 8949 Part I/II | $<amount> | Personal-item gains (if any) |
| Form 1040 Line 25b | $<Box 4> | Backup withholding credit |

## Validation
- Sum of classified portions equals Box 1a: <yes/no>
- Personal portion entered once in the Schedule 1 entry space, not inside Schedule C: <yes/no>
- All trade-or-business portion appears in Schedule C Line 1 or Schedule E Line 3: <yes/no>
- Box 4 amount appears on Form 1040 Line 25b: <yes/no>
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

Boxes 5a through 5l (monthly gross) should add up to Box 1a. Bank deposits from the platform usually won't match Box 1a exactly because:

- Settlement-date vs deposit-date timing (December 2026 settlement deposited January 2, 2027 still 2026 gross)
- Platform fees deducted before deposit (if the user gets net deposits, those won't equal gross)
- ACH return-fail-redo cycles

For most users, the bank-deposit cross-check is informational, not definitive. The platform's settlement records win.

### Step 5 — Cross-check against other 1099s (double-reporting)

If a client paid the user $5,000 through PayPal and the client (mistakenly or correctly) also issued a 1099-NEC for the same $5,000, the user has overlapping 1099s.

The income is taxable **once**. Two ways to handle:

1. **Report on Schedule C Line 1 once**, keep records showing the overlap. If the IRS sends a CP2000, respond with the reconciliation worksheet showing the overlap.
2. **Ask the issuing client to correct the 1099-NEC** (rescind it because the payment was via a third-party network and the 1099-K already reports it). Some clients will, some won't.

The general rule (Instructions for Forms 1099-MISC and 1099-NEC): payments made with a payment card or through a third party network are reported on Form 1099-K by the PSE, and the client should NOT issue a 1099-NEC for those same payments. But many clients issue 1099-NECs anyway. Document the overlap; report once. If Forms 1099-NEC box 1 total more than Schedule C line 1, attach a statement explaining the difference (2025 Schedule C instructions, line 1).

### Step 6 — Build the ledger

For each portion, identify the destination (Schedule C / Schedule 1 / Schedule E / Form 8949 / Schedule 1 entry space) and the specific line. Note the amount. The total of destinations equals Box 1a.

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

If the deadline approaches without a corrected form, don't wait (FS-2025-08, What to do Q4):

- File using the user's own records and enter the amount included in error in the entry space at the top of Schedule 1, with records showing why
- Or file Form 4868 for an extension of time to file (until October 15); it does not extend time to pay

Never report the wrong Box 1a amount as income just because it's on the form, and never drop the overstated amount from the return without the entry-space entry.

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
| Reporting only the business portion as Schedule C | Return doesn't show where the personal portion went | Enter the personal portion in the entry space at the top of Schedule 1 |
| Reporting personal payments as Schedule C income | Pays unnecessary SE tax and income tax | Move them to the entry space at the top of Schedule 1 |
| Reporting Etsy sales as hobby when it's actually trade/business | Loses Schedule C deductions | Apply the §183 9-factor test; profit motive + regularity = business |
| Excluding sub-threshold cash sales from Schedule C | All income is taxable | Add cash sales to Schedule C Line 1 alongside 1099-K portion |
| Mixing two PSEs' Box 1a into one entry | Loses traceability for CP2000 defense | Reconcile each 1099-K independently |
| Forgetting Box 4 federal withholding | Misses a refundable credit | Claim on Form 1040 Line 25b |

---

## Sources

- IRC §6050W (1099-K reporting)
- IRC §61 (gross income)
- IRC §162 (trade or business expenses)
- IRC §165 (losses; personal-use property losses not deductible)
- IRC §1221 (capital asset definition)
- [IRS Fact Sheet FS-2025-08, Form 1099-K FAQs](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) (Oct. 23, 2025)
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf), Schedule 1 "Form(s) 1099-K"
- [Instructions for Forms 1099-MISC and 1099-NEC](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf)
- [IRS CP2000 notice information](https://www.irs.gov/individuals/understanding-your-cp2000-notice)
- [Schedule C (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-c-form-1040)
- [Schedule E (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-e-form-1040)
- [Schedule 1 (Form 1040)](https://www.irs.gov/forms-pubs/about-schedule-1-form-1040)
- [Form 8949](https://www.irs.gov/forms-pubs/about-form-8949)
