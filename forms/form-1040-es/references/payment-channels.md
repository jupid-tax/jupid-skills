# Payment Channels for Form 1040-ES

Five channels the user (or agent on their behalf) can use to submit each estimated tax installment. Trade-offs and operational steps for each.

---

## 1. IRS Direct Pay (recommended default)

URL: https://www.irs.gov/payments/direct-pay

- **Cost**: free
- **Funding**: ACH from US checking or savings
- **Enrollment**: none — each payment is a fresh session
- **Confirmation**: immediate confirmation number, format `XXXXX-XXXXX-XXXXX-XXXXX`
- **Scheduling**: same-day or up to 365 days in future
- **Limit**: 2 same-day payments per tax form per SSN; can repeat next day if needed
- **Cancellation**: future-dated payments cancellable up to 11:59 PM ET two business days before scheduled date

**Identity verification**: Direct Pay verifies by matching name, SSN, DOB, address against a prior-year return on file. The user must use a prior tax year (any year 2018+) for which they actually filed. If addresses don't match, identity verification fails.

**Use when**: one-off or per-quarter payments, no advance enrollment, simplest channel for a single payment.

**Don't use when**: user wants to schedule all four installments at once at the start of the year (Direct Pay can schedule one at a time, but EFTPS does bulk scheduling more easily); user has had repeated identity verification failures.

For full browser-automation flow, see `filing.md`.

---

## 2. EFTPS (Electronic Federal Tax Payment System)

URL: https://www.eftps.gov

- **Cost**: free
- **Funding**: ACH from US checking or savings
- **Enrollment**: required; PIN mailed within 5–7 business days
- **Confirmation**: immediate EFT acknowledgment number
- **Scheduling**: up to 365 days in future; can schedule all four installments at once
- **Limit**: none practical
- **Cancellation**: scheduled payments cancellable up to 2 business days before settlement

**Identity verification**: tied to PIN + Internet Password set during enrollment; no per-payment identity check.

**Use when**: filer wants to schedule the full year of installments at once (set-and-forget), or filer has had Direct Pay identity-verification issues, or filer makes frequent IRS payments (quarterly + balance-due + amended).

**Don't use when**: it's already past March 31 and the filer hasn't enrolled — they won't receive the PIN in time for the April 15 Q1 payment. Use Direct Pay for Q1, EFTPS for Q2 onward.

**Special note**: EFTPS has a phone option (1-800-555-3453) — same PIN/password, no browser.

---

## 3. Pay by Card (debit or credit)

The IRS authorizes third-party processors to accept card payments. As of early 2026 the authorized processors are listed at https://www.irs.gov/payments/pay-your-taxes-by-debit-or-credit-card. Verify the current list each year — it changes.

| Processor | Debit fee | Credit fee | Notes |
|-----------|-----------|------------|-------|
| Pay1040 | $2.50 flat | 1.75% | Lowest credit fee at time of writing |
| ACI Payments | $2.20 flat | 1.85% | |

(Both fees and processors change. Always verify current values.)

- **Cost**: fee non-refundable, even if IRS later refunds the payment
- **Funding**: any major debit or credit card
- **Enrollment**: none
- **Confirmation**: from processor + IRS within 1–2 business days
- **Scheduling**: same-day only; cannot schedule future date
- **Limit**: 2 same-day payments per tax form per SSN
- **Cancellation**: cannot cancel through processor; must dispute with card issuer

**Use when**: user wants credit card rewards (rewards-rate must beat the ~1.85% fee to be worth it; common for 2× cashback cards on a tax-payment promotion), or user has no checking account access.

**Don't use when**: user is paying for fee minimization (Direct Pay is free).

**Tax-deductibility**: card processing fees on **business** estimated tax payments are deductible on Schedule C as a "business expense" (Line 27a or 17). On personal estimated tax, the fee is not deductible.

---

## 4. Check + Paper Voucher

When all electronic options fail or the user prefers paper:

1. Print the appropriate voucher from page 9–12 of the latest f1040es.pdf
2. Fill in: filer name, SSN, spouse name + SSN if MFJ, address, payment amount
3. Write a check payable to "United States Treasury"
4. Memo line: "2026 Form 1040-ES" + filer's SSN
5. Mail to the IRS address listed on the voucher's instructions (varies by state)

**Mailing addresses**: re-verify each year from the official PDF — the IRS shifts addresses between processing centers. Do NOT hardcode.

**Best practices**:
- USPS Certified Mail with Return Receipt for proof under IRC §7502 (timely mailing = timely filing)
- Postmark **on or before** the installment due date
- Keep a photocopy of the voucher and check
- Allow 4–6 weeks for IRS to credit the payment in the user's account

**Use when**: electronic channels all fail, user has identity-theft concerns about online IRS interaction, or user is overseas without reliable US banking.

**Don't use when**: speed matters (paper is slow) or audit-trail matters (electronic confirmation numbers are stronger evidence).

---

## 5. IRS Online Account

URL: https://www.irs.gov/payments/online-account

After signing in (requires ID.me identity verification), the user can pay directly from their IRS account dashboard. Mechanically routes through Direct Pay; the dashboard saves payment history.

- **Cost**: free
- **Funding**: ACH (same as Direct Pay)
- **Enrollment**: ID.me identity verification (driver's license + selfie + verification call)
- **Use when**: user already has an IRS Online Account and wants centralized payment history

**Browser automation note**: ID.me's identity proofing breaks deterministic agent flows (selfie verification, biometric capture, sometimes a video call). For agent-driven payments, **Direct Pay is the better channel** because it doesn't require ID.me. If the user already has an Online Account session active in their browser, the agent can use it — but the agent should not attempt to enroll in ID.me on the user's behalf.

---

## Channel selection matrix

| User priority | Recommended channel |
|---------------|---------------------|
| Simplest one-time payment, no enrollment | Direct Pay |
| Schedule full year at once | EFTPS |
| Earn card rewards | Card (only if rewards > fee) |
| No US bank account | Card |
| Paper records preferred | Check + voucher |
| Centralized payment history | IRS Online Account |
| Agent-automated | Direct Pay (deterministic flow) |

---

## Common pitfalls across all channels

1. **Wrong "Reason for Payment"**: must select "Estimated Tax" → "1040ES (for 1040, 1040A, 1040EZ)". Selecting "Balance Due" or "Tax Return" puts the money in the wrong bucket and requires manual IRS reallocation (3–6 weeks).

2. **Wrong tax year**: must select the year the estimated payment covers (e.g., 2026 for a 2026-Q1 payment), NOT the calendar year the payment is made (which would be 2026 calendar but Q1 covers Jan–Mar 2026).

3. **Wrong installment quarter**: Direct Pay/EFTPS don't ask about quarter — the IRS allocates based on date received and tax year. As long as the date and year are right, the quarter is correct.

4. **Joint filers**: if MFJ, the payment is associated with the **primary filer's SSN**. The spouse's SSN doesn't appear on Direct Pay. At filing time, the joint return's primary filer SSN matches the payment record.

5. **Foreign filer**: estimated tax for nonresident aliens uses **Form 1040-ES (NR)**, not 1040-ES. Different vouchers, different mailing address. This skill does NOT cover NR filers — redirect.

6. **State estimated tax**: completely separate from federal. The user must also pay state estimated tax to their state DOR (varies by state). Federal Form 1040-ES does not satisfy state obligations.

---

## Confirmation tracking

After every payment, the agent should record (in the user's records, not the agent's logs):

- Channel used
- Date submitted
- Amount
- Tax year covered
- Confirmation number
- Settlement date (when ACH cleared / when IRS posted)

At year-end, the user reconciles: total of all confirmations = Form 1040 Line 26 (total estimated payments). Discrepancies surface at filing time and are usually due to wrong "Reason for Payment" coding (see pitfall #1) or an unposted check.
