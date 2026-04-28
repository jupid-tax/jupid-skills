# Common Mistakes on Form 8949

The IRS computer cross-references every Box A and Box D entry against broker 1099-B totals. The eight most common mistakes below all produce CP2000 notices, audit triggers, or overpayment of tax. The skill encodes checks for each one.

---

## Mistake 1 — Not reporting crypto-to-crypto swaps as taxable

**The problem**: filer swaps ETH for BTC inside Coinbase and assumes "I didn't touch USD, so no tax." Wrong — under Notice 2014-21, that's a disposition of ETH at FMV. The swap produces a gain or loss on the ETH side that must be reported on 8949.

**Impact**: Unreported gain. The IRS receives exchange data and Form 1099-DA proceeds (starting tax year 2025). When totals don't match, a CP2000 notice arrives 9–18 months after filing.

**How the skill avoids it**: in Step 2, the agent treats every CSV row from a crypto exchange as a potential disposition. Swaps appear as paired transactions (sell of one asset + buy of another) and are reported as a single 8949 row on the sell side.

---

## Mistake 2 — Wrong holding period (off-by-one error)

**The problem**: filer buys on Jan 15, 2025, sells on Jan 15, 2026, and reports as long-term. That's **exactly** one year — short-term. Long-term requires more than one year (Jan 16, 2026 or later).

**Impact**: If the broker correctly reports it as short-term and the filer claims long-term, mismatch triggers a CP2000. If both sides agree on the wrong treatment, the filer overpays or underpays depending on which way the error went.

**How the skill avoids it**: in Step 3, holding period is computed as (sold date) − (acquired date + 1) > 365. Boundary cases (exactly 365 days) are flagged and re-confirmed.

---

## Mistake 3 — Not adjusting basis for wash sale disallowed losses

**The problem**: filer takes a loss, rebuys within 30 days, files the loss on 8949 without code "W". A year later, sells the replacement lot using only the rebuy price as basis — claiming the deferred loss a second time.

**Impact**: Loss claimed twice. If the IRS audits or 1099-B data flags it, owe tax + penalties + interest.

**How the skill avoids it**: in Step 4, every loss row is checked for replacement purchases within 61 days across all of the user's accounts (and spouse's). Code "W" + adjustment in (g) is applied. The replacement lot's adjusted basis is recorded for next year's tracking.

---

## Mistake 4 — Forgetting a 1099-B

**The problem**: filer misses a 1099-B from a closed account, a small DRIP account, or a transferred-out lot. The IRS gets a copy from the broker; the filer's return doesn't include it.

**Impact**: Automatic CP2000 notice 9–18 months later. The IRS treats unreported proceeds as if basis = $0, so the proposed tax is enormous relative to the actual gain. The filer then has to respond with the actual basis records, which they may not have because they forgot the account existed.

**How the skill avoids it**: in Step 2, the agent asks the user to list every brokerage and account used during the year, including any closed during the year. The agent confirms the list against W-8 / W-9 filings, recurring deposits, and prior-year returns when possible.

---

## Mistake 5 — Wrong box (A vs B vs C, or D vs E vs F)

**The problem**: filer puts a covered share sale in Box C ("no 1099-B received") instead of Box A. The 1099-B exists; the IRS computer expects Box A totals to match it; mismatch flags the return.

**Impact**: CP2000 or slow-walked refund. May also flag the return for desk audit.

**How the skill avoids it**: in Step 3, the agent reads each 1099-B's "basis reported to IRS" / "basis not reported to IRS" / "non-1099-B" labeling and assigns the correct box. Sanity check in Step 8 confirms that Box A/D entries have a 1099-B and Box C/F entries don't.

---

## Mistake 6 — Defaulting to $0 basis when records are missing

**The problem**: filer doesn't have basis records for a 5-year-old crypto purchase or a transferred-in stock lot. They enter $0 basis on 8949 to "be safe", figuring overpaying is better than under-reporting.

**Impact**: They overpay massively. A $20,000 sale of crypto with actual basis of $15,000 reported as $0 basis means $20,000 reported gain instead of $5,000 — at 32% federal that's a $4,800 over-payment. Then when the user later finds the actual records, they have to file Form 1040-X to recover, and the IRS may ask why the original was wrong.

**How the skill avoids it**: in Prerequisite step and Step 2, the agent **requires** basis records before producing a draft. If the user can't produce them, the agent stops and asks rather than defaulting to $0.

For crypto specifically: the agent guides the user through CSV exports from exchanges (which usually contain historical basis), wallet history reconstruction (Etherscan, BTCScan), and prior-year tax returns (which may have already established basis for surviving lots).

---

## Mistake 7 — Cross-account / spousal / IRA wash sales missed

**The problem**: filer sells AAPL at a loss in their Schwab account on Dec 15. The same week, they buy AAPL in their Fidelity Roth IRA. Schwab's 1099-B doesn't flag a wash because Schwab can't see Fidelity. The filer reports the loss; later the IRS reconciles with broker data and notices the Fidelity purchase.

**Impact**: For the cross-broker case, a CP2000 with disallowed loss. For the Roth IRA case, a CP2000 with a **permanent** loss disallowance — the loss can never be recovered because the IRA has no taxable basis to absorb it.

**How the skill avoids it**: in Step 4, the agent explicitly asks: "Did you (or your spouse) buy the same security in any other account, including IRAs, within 30 days of any loss sale this year?" This catches the cross-account and IRA cases that broker reporting can't.

---

## Mistake 8 — Schedule D total doesn't tie to 8949 totals

**The problem**: filer enters 8949 transactions correctly but transposes a digit when totaling them onto Schedule D. Or they forget to include Box C totals in Line 3. Or they miscount.

**Impact**: Mismatch between 8949 page totals and Schedule D box-line entries triggers an internal-consistency error in IRS processing. Might be auto-corrected; might not.

**How the skill avoids it**: in Step 6 and Step 8 (Validation), the agent computes box totals from the row-level data, then computes Schedule D line entries from the box totals. The Validation step explicitly checks that 8949 box totals = Schedule D line entries.

---

## Mistake 9 — Net loss > $3,000 not properly carried forward

**The problem**: filer has a $20,000 net capital loss. They use $3,000 against ordinary income but don't track the $17,000 carryforward. Next year, they don't claim the carryforward — losing the deduction.

**Impact**: Permanent loss of the $17,000 carryforward (or part of it). Can be recovered via amended return within 3 years.

**How the skill avoids it**: in Step 7 and the Output, when net loss exceeds $3,000 the agent computes the Capital Loss Carryover Worksheet result and saves it explicitly for next year. The deliverable lists separate short-term and long-term carryforward amounts (carryover retains its character per §1212).

---

## Mistake 10 — Treating §121 home-sale exclusion incorrectly

**The problem**: filer sells primary residence with $400,000 gain, qualifies for the $250,000 §121 exclusion (single filer), and either:
- Doesn't report at all (wrong if any gain exceeds the exclusion or 1099-S was issued), or
- Reports the full $400,000 gain (wrong — should report net $150,000 with code "H" and the excluded portion as adjustment in (g))

**Impact**: Either CP2000 notice (under-reporting) or overpayment ($250,000 × 15% = $37,500 lost).

**How the skill avoids it**: when the user mentions selling a primary residence, the agent walks through §121 qualification (owned + used 2 of past 5 years), computes qualifying exclusion, and applies code "H" with the exclusion as adjustment when partial gain remains. If gain is fully excluded AND no 1099-S was issued, no 8949 entry needed.

---

## Mistake 11 — Forgetting NIIT (Form 8960)

**The problem**: filer has $50,000 net long-term capital gain and $250,000 W-2 income. They report Schedule D correctly but don't file Form 8960 for the 3.8% NIIT under §1411.

**Impact**: Owe an additional $50,000 × 3.8% = $1,900 in NIIT. Eventually catches up via IRS notice or in a later audit.

**How the skill avoids it**: in Step 8 and Step 10, the agent checks MAGI against the NIIT threshold ($200K single / $250K MFJ) and surfaces Form 8960 as a required attachment whenever the threshold is exceeded.

---

## Mistake 12 — Using wrong cost basis method on partial sale

**The problem**: filer has 200 shares AAPL across two lots — 150 long-term low-basis and 50 short-term high-basis. They sell 50 shares and let the broker default to FIFO, selling 50 of the long-term low-basis shares. They could have used specific-ID to sell the short-term high-basis lot and produce a much smaller gain.

**Impact**: Overpayment of tax by the difference between the two scenarios. Cannot be retroactively changed once the trade settles.

**How the skill avoids it**: this is an **advisory** check rather than a filing fix. The agent surfaces specific-ID savings opportunities when the user is contemplating a sale. Once the trade has occurred and the broker has applied the default method, the basis is locked unless specific-ID was elected at trade time.

---

## Cross-checking against the digital asset question

The Form 1040 digital asset question reads: "At any time during [year], did you (a) receive (as a reward, award, or payment for property or services); or (b) sell, exchange, or otherwise dispose of a digital asset (or a financial interest in a digital asset)?"

If the user answers "Yes" but has no Box C/F entries on 8949 and no 1099-MISC entries on Schedule 1: the agent should reconcile. The "Yes" answer is correct in many cases (receiving a small airdrop, getting paid in crypto, etc.) but each "Yes" should produce **some** corresponding tax entry somewhere. A "Yes" with nothing else is a flag.

If the user answers "No" but has crypto activity in their records: the agent must correct the answer. False "No" answers are perjury (the form is signed under penalty of perjury) and trigger major penalties.

---

## Summary checklist

Before declaring an 8949 draft ready, verify:

- [ ] Every crypto swap in the user's CSVs is reported on 8949
- [ ] Holding period is computed as (sold − acquired − 1) > 365 for long-term
- [ ] Every loss is checked for wash sale across all accounts
- [ ] Every 1099-B issued to the user is represented on the form
- [ ] Each transaction is in the correct box based on 1099-B labeling
- [ ] No row has $0 basis when actual basis is positive
- [ ] Cross-account, spousal, and IRA wash sales are surfaced
- [ ] 8949 box totals tie to Schedule D box-line entries
- [ ] If net loss > $3,000, carryforward is computed and saved
- [ ] §121 home sale is handled with code "H" if partial exclusion applies
- [ ] Form 8960 (NIIT) is on the to-do list if MAGI > threshold
- [ ] Form 1040 digital asset question is consistent with reported activity
