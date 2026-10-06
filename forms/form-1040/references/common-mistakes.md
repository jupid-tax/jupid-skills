# Top 10 Form 1040 Mistakes

Real mistakes filers make on Form 1040. Each entry has the mistake, the consequence, and the fix. Line numbers and amounts verified 2026-10-06 against the 2025 Form 1040 and its instructions (filed in 2026); re-check them on the next revision.

## 1. Wrong filing status (Head of Household trap)

**The mistake**: Single parent or unmarried filer claims HoH without meeting all three rules: (a) unmarried, (b) paid more than half the cost of keeping up a home, (c) qualifying person lived with them more than half the year.

**Why it happens**: HoH gives a larger standard deduction and wider brackets than Single. Filers see the savings and assume they qualify. Common sub-errors:
- Married but living apart, claims HoH (must be "considered unmarried" — strict 6-month test)
- 50/50 custody, both parents try to claim HoH for the same child (only one can)
- Roommate or non-relative dependent — doesn't qualify as HoH person
- Cousin lived in the household — cousins don't satisfy HoH qualifying person test

**Consequence**: IRS reclassifies to Single, sends a notice with the balance due and interest, plus the 20% accuracy-related penalty (IRC §6662) when the error comes from negligence or produces a substantial understatement.

**Fix**: Verify all three tests before filing. Run the qualifying person test from `dependents.md`. If 50/50 custody, only the higher-AGI parent (or by agreement) claims HoH.

---

## 2. SSN / name mismatch with Social Security Administration

**The mistake**: Filer enters their name slightly differently than how it's recorded with the SSA — wrong middle initial, missing hyphen, married name not yet updated, suffix (Jr/Sr) inconsistency.

**Consequence**: IRS e-file rejects the return (name/SSN mismatch business rules). Refund delayed. If the filer doesn't notice the rejection, the return is not filed.

**Fix**: Match the Social Security card exactly. If the name has changed (marriage, divorce), update with SSA *before* filing. Verify dependents' names too — same risk applies.

---

## 3. Forgetting estimated tax payments

**The mistake**: Self-employed filer skips quarterly Form 1040-ES payments because there's no W-2 withholding to keep them on track.

**Consequence**: Underpayment penalty calculated on Form 2210 at the IRC §6621 underpayment interest rate, applied to each late or short installment for the time it was late. Penalty appears on Line 38 and is added to Line 37.

**Fix**: Pay quarterly via Form 1040-ES (for 2026: April 15, June 15, September 15, 2026 and January 15, 2027). Safe harbor: pay during the year either 90% of current-year tax OR 100% of prior-year tax (110% if prior-year AGI > $150,000, $75,000 MFS); no penalty if Line 37 is under $1,000 (i1040gi 2025, Line 38).

For the agent: when a Schedule C is in the inputs and Line 26 (estimated payments) is $0, surface a sanity warning. The user likely owes Line 38.

---

## 4. Underreporting 1099 income

**The mistake**: Filer adds up 1099-NEC totals and reports that as income, missing:
- Cash payments not on 1099
- Payments under the 1099-NEC filing threshold ($600 for payments in 2025; $2,000 for payments after 2025 under P.L. 119-21)
- Gig income reported on 1099-K but mistakenly thought to be excluded
- Crypto sold, exchanged, or received as payment (digital assets question; 1099-DA starts with 2025 sales)

**Consequence**: IRS matches information returns (1099s) to the return. Mismatches trigger a CP2000 notice months after filing. Tax + interest, and possibly the 20% accuracy-related penalty.

**Fix**: Reconcile bank deposits to invoices before filing. Report ALL business income on Schedule C, regardless of whether a 1099 was issued. Crypto: answer Yes to the digital assets question and report disposals on Form 8949.

---

## 5. Forgetting QBI deduction (Line 13a)

**The mistake**: Schedule C / Schedule E passthrough / K-1 filer skips Form 8995 because they don't realize they qualify.

**Consequence**: Leaves 20% of qualified business income deduction on the table. For a $50,000 Schedule C profit in the 22% bracket: QBI = $50,000 − $3,532 (half of SE tax) = $46,468; deduction $9,294; about $2,045 of unnecessary tax.

**Fix**: Run Form 8995 (simplified) for any Schedule C, Schedule E passthrough, K-1, or qualifying REIT/PTP income when taxable income before the QBI deduction is at or below $197,300 ($394,600 MFJ) for 2025 ($201,750 / $403,500 for 2026, Rev. Proc. 2025-32 §4.26). Form 8995-A above the threshold (with SSTB and W-2 wage limits). The deduction goes on Line 13a.

QBI is the most under-claimed deduction for solopreneurs.

---

## 6. Wrong dependent claims (residency or shared custody)

**The mistake**: Claiming a child who fails the residency test, or both divorced parents trying to claim the same child without coordinating.

**Consequence**: E-file rejects the second-filed return because the dependent's SSN was already used; the second filer must paper-file and the IRS sorts out the claim. Tax, interest, and possible penalties for the parent who wasn't entitled.

**Fix**: Apply IRC §152(c)(4) tiebreaker rules:
1. Parent over non-parent
2. The parent the child lived with longer
3. If equal, higher-AGI parent
4. If non-custodial parent claims, custodial parent must sign Form 8332

Coordinate with the other parent BEFORE filing.

---

## 7. Skipping Schedule SE when self-employment earnings are $400 or more

**The mistake**: Schedule C shows a $25,000 net profit. Filer correctly reports the income on Schedule 1 → 1040 Line 8, but doesn't file Schedule SE and doesn't include SE tax on Line 23.

**Consequence**: IRS notice. Self-employment tax of $3,532 ($25,000 × 0.9235 × 15.3%) plus penalties and interest. Schedule SE is *required* when net earnings from self-employment are $400 or more (IRC §6017; Schedule SE line 4c test).

Also misses the half-SE-tax adjustment on Schedule 1 Line 15 — costs the filer additional tax.

**Fix**: If 92.35% of Schedule C Line 31 (Schedule SE line 4c) is $400 or more, Schedule SE is mandatory. Compute SE tax (12.4% up to the $176,100 2025 wage base plus 2.9% on all, on 92.35% of profit) and put it on Schedule 2 Line 4 → Schedule 2 Line 21 → 1040 Line 23. Half SE tax goes on Schedule 1 Line 15 → 1040 Line 10 (reduces AGI).

---

## 8. Standard deduction taken when itemizing would save more

**The mistake**: Filer with a large mortgage, high state taxes, or major medical expenses defaults to the standard deduction without running Schedule A.

**Consequence**: Pays tax on income the law lets them deduct. Common in high-tax states (CA, NY, NJ, MA) where SALT (for 2025 capped at $40,000, $20,000 MFS, reduced when MAGI exceeds $500,000, $250,000 MFS, but not below $10,000 / $5,000; Schedule A line 5e) plus mortgage interest plus charitable can exceed the standard deduction.

**Fix**: Run Schedule A whenever the filer has any of:
- Mortgage on a home > $200,000
- Lives in a state with income tax > 5%
- Medical expenses > 7.5% of AGI
- Charitable contributions > $5,000
- Casualty loss in a federally declared disaster area

Compare Schedule A Line 17 to the standard deduction. Take the larger.

For 2025: Single/MFS $15,750, MFJ/QSS $31,500, HoH $23,625 (i1040gi 2025, What's New). Schedule 1-A deductions (Line 13b) are available either way.

---

## 9. Wrong digital assets answer

**The mistake**: Filer answers "No" to the digital assets question because they think only "trading" counts. Or answers "Yes" because they hold crypto, even though they didn't sell.

**Consequence**: Wrong "No" can lead to CP2000 notice when crypto exchange 1099 shows up. Wrong "Yes" causes the IRS to expect Form 8949 entries that don't exist.

**Fix**: Answer Yes if during the tax year the filer (2025 question text: "(a) receive (as a reward, award, or payment for property or services); or (b) sell, exchange, or otherwise dispose of a digital asset"):
- Sold crypto for fiat
- Exchanged one crypto for another
- Used crypto to pay for goods/services
- Received crypto as a reward, award, or payment (including mining/staking rewards, airdrops, hard forks)

Answer No if the filer only (i1040gi 2025, Digital Assets):
- Held crypto in a wallet or account
- Transferred crypto between wallets or accounts they own or control
- Bought crypto with U.S. or other real currency

If unsure about another situation (e.g., receiving crypto as a bona fide gift), check the Digital Assets section of the instructions and ask. A gift the filer *made* can require Form 709.

When Yes, report disposals on Form 8949 → Schedule D → Line 7a. Report digital assets received as ordinary income and not reported elsewhere on Schedule 1 Line 8v.

---

## 10. Direct deposit errors (wrong routing/account number)

**The mistake**: Filer enters routing or account number incorrectly on Lines 35b/35d.

**Consequence** (i1040gi 2025, Lines 35a–35d):
- A rejected direct deposit delays the refund. Starting in October 2025 the IRS generally stopped issuing paper refund checks unless an exception applies, so a bad account number is no longer a simple switch to a check.
- "The IRS isn't responsible for a lost refund if you enter the wrong account information." If the numbers are valid but belong to someone else, the refund may be gone.
- Other rejection reasons: joint refund to an individual account the bank won't accept, name mismatch the bank won't accept, or three refunds already deposited to the same account.

**Fix**: Routing number is nine digits starting 01–12 or 21–32; account number up to 17 characters. Verify against a check or the bank (a deposit slip's routing number can differ). The account must be in the filer's name. For agents: do not auto-fill routing/account; collect at filing time, have the user confirm twice.

---

## Less common but worth flagging

### 11. Combat pay election error

Excluding combat pay reduces taxable income. But for EITC purposes, the filer can ELECT to include nontaxable combat pay (Line 1i) to potentially increase EITC. Many filers don't know about this election. Run both ways.

### 12. Forgetting Schedule B for foreign accounts

Schedule B is required if taxable interest is over $1,500, OR ordinary dividends are over $1,500, OR the filer had a financial interest in or signature authority over a foreign account, or a foreign trust (i1040gi 2025, Lines 2b, 3b). Missing the foreign accounts question on Schedule B Part III triggers FBAR / Form 8938 issues — much more expensive than the tax itself.

### 13. Capital loss > $3,000 not carried forward

A net capital loss is capped at $3,000 ($1,500 MFS) per year on Line 7a. Excess carries forward indefinitely (Schedule D Worksheet). Filers who forget the carryforward lose the deduction. Track it year-over-year in tax software or a dedicated worksheet.

### 14. Roth IRA over-contribution

Filer contributes $7,000 to Roth IRA at start of year, then modified AGI ends up in or over the phaseout ($150,000–$165,000 single / $236,000–$246,000 MFJ for 2025, Pub. 590-A). Excess contribution triggers 6% excise tax (Form 5329) per year until removed.

**Fix**: Withdraw excess + earnings by October 15 of the following year, or recharacterize as Traditional IRA before October 15.

### 15. Not signing the return

Both spouses must sign on MFJ. Unsigned returns are treated as not filed. IRS will return the form for signature, delaying refund by weeks. E-file PIN substitutes for paper signature — both spouses need their own PIN on MFJ.

### 16. Marketplace income without a 1099-K mistakenly excluded

P.L. 119-21 restored the Form 1099-K reporting threshold: payment apps and marketplaces send a 1099-K only if business transactions are more than $20,000 AND more than 200 transactions (i1040gi 2025, What's New). Many sellers below that line get no form and assume the income isn't taxable. It still is. Report all gig/marketplace business income on Schedule C.

### 17. Putting AGI from wrong year for e-file identity verification

When e-filing, IRS verifies identity with prior-year AGI. Filers sometimes use current-year AGI by mistake, or use AGI from before an amendment, or prior-year AGI from before being audited and adjusted. Use the AGI on the actual 1040 the IRS processed.

If unsure, pull the IRS account transcript at https://www.irs.gov/individuals/get-transcript.

### 18. Forgetting state estimated tax payments

State and federal estimated taxes are separate. A filer who paid $5,000 to the IRS each quarter may owe state too — and the state penalty is independent of the federal one. Many states follow the federal April / June / September / January schedule; check the state's own due dates.

### 19. Incorrect or missing 1095-A reconciliation

If filer received advance Premium Tax Credit (ACA marketplace), Form 8962 must reconcile against actual income. Forgetting this leads to:
- Excess advance PTC repayment if income exceeded projection (Schedule 2 Line 1a → Line 17)
- Lost net PTC if income was lower than projected (Schedule 3 Line 9 → Line 31)

Leaving Form 8962 off holds up processing; the 2025 instructions say anyone enrolled with advance payments "must file a 2025 return and attach Form 8962".

### 20. Refund applied to next year, then needed

Line 36 lets a filer apply a refund to next year's estimated taxes. The election "can't be changed later" (i1040gi 2025, Line 36). If the filer needs the cash later, they cannot get it back until they file next year's return and over-pay/refund.

For agents: confirm with the user before populating Line 36.
