# Top 10 Form 1040 Mistakes

Real mistakes filers make on Form 1040, ranked by how often they trigger IRS notices, refund delays, or audit adjustments. Each entry has the mistake, the consequence, and the fix.

## 1. Wrong filing status (Head of Household trap)

**The mistake**: Single parent or unmarried filer claims HoH without meeting all three rules: (a) unmarried, (b) paid more than half the cost of keeping up a home, (c) qualifying person lived with them more than half the year.

**Why it happens**: HoH gives a larger standard deduction and wider brackets than Single. Filers see the savings and assume they qualify. Common sub-errors:
- Married but living apart, claims HoH (must be "considered unmarried" — strict 6-month test)
- 50/50 custody, both parents try to claim HoH for the same child (only one can)
- Roommate or non-relative dependent — doesn't qualify as HoH person
- Cousin lived in the household — cousins don't satisfy HoH qualifying person test

**Consequence**: IRS reclassifies to Single, sends CP notice with balance due, interest, and 20% accuracy penalty if egregious.

**Fix**: Verify all three tests before filing. Run the qualifying person test from `dependents.md`. If 50/50 custody, only the higher-AGI parent (or by agreement) claims HoH.

---

## 2. SSN / name mismatch with Social Security Administration

**The mistake**: Filer enters their name slightly differently than how it's recorded with the SSA — wrong middle initial, missing hyphen, married name not yet updated, suffix (Jr/Sr) inconsistency.

**Consequence**: IRS e-file system rejects the return (rejection codes R0000-902, R0000-194, F1040-507, etc.). Refund delayed. If the filer doesn't notice the rejection, the return is treated as not filed.

**Fix**: Match the Social Security card exactly. If the name has changed (marriage, divorce), update with SSA *before* filing. Verify dependents' names too — same risk applies.

---

## 3. Forgetting estimated tax payments

**The mistake**: Self-employed filer skips quarterly Form 1040-ES payments because there's no W-2 withholding to keep them on track.

**Consequence**: Underpayment penalty calculated on Form 2210, ~4-8% annualized on the shortfall plus interest. Penalty appears on Line 38.

**Fix**: Pay quarterly via Form 1040-ES (April 15, June 15, September 15, January 15). Safe harbor: pay during the year either 90% of current-year tax OR 100% of prior-year tax (110% if prior-year AGI > $150,000). Either threshold avoids the penalty.

For the agent: when a Schedule C is in the inputs and Line 26 (estimated payments) is $0, surface a sanity warning. The user likely owes Line 38.

---

## 4. Underreporting 1099 income

**The mistake**: Filer adds up 1099-NEC totals and reports that as income, missing:
- Cash payments not on 1099
- Checks for under the $600 1099 threshold
- Gig income reported on 1099-K but mistakenly thought to be excluded
- Crypto sold or used (taxable disposal under digital assets question)

**Consequence**: IRS cross-matches 1099s and bank deposits. Mismatches trigger CP2000 notice ~12 months after filing. Tax + 20% accuracy penalty + interest.

**Fix**: Reconcile bank deposits to invoices before filing. Report ALL business income on Schedule C Line 1, regardless of whether a 1099 was issued. Crypto: answer Yes to digital assets question and report disposals on Form 8949.

---

## 5. Forgetting QBI deduction (Line 13)

**The mistake**: Schedule C / Schedule E passthrough / K-1 filer skips Form 8995 because they don't realize they qualify.

**Consequence**: Leaves 20% of qualified business income deduction on the table. For a $50,000 Schedule C profit at 22% bracket, that's roughly $1,500–$2,000 in unnecessary tax.

**Fix**: Run Form 8995 (simplified) for any Schedule C, Schedule E passthrough, K-1, or qualifying REIT/PTP income below the income threshold ($241,950 single / $383,900 MFJ for 2025). Form 8995-A above the threshold (with SSTB and W-2 wage limits).

QBI is the most under-claimed deduction for solopreneurs.

---

## 6. Wrong dependent claims (residency or shared custody)

**The mistake**: Claiming a child who fails the residency test, or both divorced parents trying to claim the same child without coordinating.

**Consequence**: IRS rejects the second-filed return (e-file error F1040-525). Manual reconciliation required. Penalties if the wrong parent claimed.

**Fix**: Apply IRC §152(c)(4) tiebreaker rules:
1. Parent over non-parent
2. The parent the child lived with longer
3. If equal, higher-AGI parent
4. If non-custodial parent claims, custodial parent must sign Form 8332

Coordinate with the other parent BEFORE filing.

---

## 7. Skipping Schedule SE when self-employment > $400

**The mistake**: Schedule C shows a $25,000 net profit. Filer correctly reports the income on Schedule 1 → 1040 Line 8, but doesn't file Schedule SE and doesn't include SE tax on Line 22.

**Consequence**: IRS notice. Self-employment tax of ~$3,500 plus penalties and interest. Schedule SE is *required* whenever net SE earnings exceed $400 (IRC §1402(a)).

Also misses the half-SE-tax adjustment on Schedule 1 Line 15 — costs the filer additional tax.

**Fix**: If Schedule C Line 31 > $400, Schedule SE is mandatory. Compute SE tax (15.3% × 92.35% × profit, up to SS wage base) and put it on Schedule 2 Line 4 → 1040 Line 22. Half SE tax goes on Schedule 1 Line 15 → 1040 Line 10 (reduces AGI).

---

## 8. Standard deduction taken when itemizing would save more

**The mistake**: Filer with a large mortgage, high state taxes, or major medical expenses defaults to the standard deduction without running Schedule A.

**Consequence**: Pays tax on income the law lets them deduct. Common in high-tax states (CA, NY, NJ, MA) where SALT (capped at $10,000) plus mortgage interest plus property tax plus charitable can exceed the standard deduction.

**Fix**: Run Schedule A whenever the filer has any of:
- Mortgage on a home > $200,000
- Lives in a state with income tax > 5%
- Medical expenses > 7.5% of AGI
- Charitable contributions > $5,000
- Casualty loss in a federally declared disaster area

Compare Schedule A Line 17 to the standard deduction. Take the larger.

For 2025: Single/MFS $15,000, MFJ/QSS $30,000, HoH $22,500.

---

## 9. Wrong digital assets answer

**The mistake**: Filer answers "No" to the digital assets question because they think only "trading" counts. Or answers "Yes" because they hold crypto, even though they didn't sell.

**Consequence**: Wrong "No" can lead to CP2000 notice when crypto exchange 1099 shows up. Wrong "Yes" causes the IRS to expect Form 8949 entries that don't exist.

**Fix**: Answer Yes if during the tax year the filer:
- Sold crypto for fiat
- Exchanged one crypto for another
- Used crypto to pay for goods/services
- Received crypto as payment, mining/staking income, airdrop, or hard fork

Answer No if the filer only:
- Held crypto without selling
- Bought crypto with fiat (purchase only)
- Received as a gift or transferred between own wallets

When Yes, report disposals on Form 8949 → Schedule D → Line 7. Report income (mining, staking, airdrops) as ordinary income on Schedule 1 Line 8v (digital asset income line).

---

## 10. Direct deposit errors (wrong routing/account number)

**The mistake**: Filer enters routing or account number incorrectly on Lines 35b/35d.

**Consequence**: 
- If the routing number is invalid, IRS sends a paper check instead (delay 4–6 weeks).
- If routing is valid but account is invalid, refund is rejected by the bank and IRS reissues by paper check (delay 6–8 weeks).
- If routing and account are valid but belong to someone else, the refund is gone — IRS won't recover it.

**Fix**: Verify routing number against a recent check or the bank's website. Verify account number against a bank statement (NOT a deposit slip — deposit slips often have a different number). For agents: do not auto-fill routing/account; collect at filing time, have the user confirm twice.

---

## Less common but worth flagging

### 11. Combat pay election error

Excluding combat pay reduces taxable income. But for EITC purposes, the filer can ELECT to include nontaxable combat pay (Line 1i) to potentially increase EITC. Many filers don't know about this election. Run both ways.

### 12. Forgetting Schedule B for foreign accounts

Schedule B is required if interest + dividends > $1,500 OR the filer had a foreign bank/financial account at any point during the year. Missing the foreign accounts question on Schedule B Part III triggers FBAR / Form 8938 issues — much more expensive than the tax itself.

### 13. Capital loss > $3,000 not carried forward

A net capital loss is capped at $3,000 ($1,500 MFS) per year on Line 7. Excess carries forward indefinitely (Schedule D Worksheet). Filers who forget the carryforward lose the deduction. Track it year-over-year in tax software or a dedicated worksheet.

### 14. Roth IRA over-contribution

Filer contributes $7,000 to Roth IRA at start of year, then AGI ends up over the phaseout ($165,000–$165,000 single / $246,000–$246,000 MFJ for 2025). Excess contribution triggers 6% excise tax (Form 5329) per year until removed.

**Fix**: Withdraw excess + earnings by October 15 of the following year, or recharacterize as Traditional IRA before October 15.

### 15. Not signing the return

Both spouses must sign on MFJ. Unsigned returns are treated as not filed. IRS will return the form for signature, delaying refund by weeks. E-file PIN substitutes for paper signature — both spouses need their own PIN on MFJ.

### 16. 1099-K below $20,000 threshold mistakenly excluded

For 2025, the 1099-K reporting threshold is $2,500 (verify 2026). Many filers remember the old $20,000 / 200-transactions threshold and exclude smaller amounts. The income is still taxable regardless of whether a 1099-K was issued. Report all gig/marketplace income on Schedule C.

### 17. Putting AGI from wrong year for e-file identity verification

When e-filing, IRS verifies identity with prior-year AGI. Filers sometimes use current-year AGI by mistake, or use AGI from before an amendment, or prior-year AGI from before being audited and adjusted. Use the AGI on the actual 1040 the IRS processed.

If unsure, pull the IRS account transcript at https://www.irs.gov/individuals/get-transcript.

### 18. Forgetting state estimated tax payments

State and federal estimated taxes are separate. A filer who paid $5,000 to the IRS each quarter may owe state too — and the state penalty is independent of the federal one. Most states have 1040-ES equivalents with the same April 15 / June 15 / September 15 / January 15 schedule.

### 19. Incorrect or missing 1095-A reconciliation

If filer received advance Premium Tax Credit (ACA marketplace), Form 8962 must reconcile against actual income. Forgetting this leads to:
- Excess advance PTC repayment if income exceeded projection (Schedule 2 Line 1a)
- Lost net PTC if income was lower than projected (Line 31)

E-file rejection F8962-070 if 1095-A on file but no Form 8962 attached.

### 20. Refund applied to next year, then needed

Line 36 lets a filer apply a refund to next year's estimated taxes. Once filed, this election generally CANNOT be reversed. If the filer needs the cash later, they cannot get it back until they file next year's return and over-pay/refund.

For agents: confirm with the user before populating Line 36.
