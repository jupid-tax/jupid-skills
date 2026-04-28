# Top 10 Schedule 1 Mistakes

Real mistakes filers and unsupervised agents make on Schedule 1, ranked by how often they trigger IRS notices, AGI errors, or missed deductions. Each entry has the mistake, the consequence, and the fix.

## 1. Skipping above-the-line deductions when taking the standard deduction

**The mistake**: Filer takes the standard deduction and assumes no other deductions are available. Skips student loan interest (Line 21), HSA (Line 13), SE health insurance (Line 17), SEP-IRA (Line 16), half SE tax (Line 15), educator expenses (Line 11).

**Why it happens**: "Standard vs. itemized" is the visible choice in tax software. Above-the-line deductions sit before that choice and get overlooked.

**Consequence**: AGI overstated by hundreds to thousands of dollars. Missed credit eligibility (premium tax credit, retirement saver's credit, EITC). Pure tax overpayment.

**Fix**: Schedule 1 Part II is **independent** of the standard-vs-itemized choice. Run every Part II line regardless. The four most-missed for solo filers: Line 15 (half SE tax), Line 16 (SEP-IRA), Line 17 (SE health insurance), Line 21 (student loan interest).

---

## 2. Reporting hobby income with expense offsets on Line 8j

**The mistake**: Filer with $5,000 hobby income on Line 8j deducts $4,000 of hobby expenses to net $1,000.

**Why it happens**: Pre-TCJA, hobby expenses were deductible as miscellaneous itemized deductions on Schedule A. TCJA suspended that through 2025 (verify status for 2026). Many filers don't know.

**Consequence**: $4,000 understated income → $880 tax + accuracy penalty on audit at 22% bracket.

**Fix**: Report **gross** hobby income on Line 8j with no offset. If the activity is regular and for-profit (9-factor test under IRC §183), it's a Schedule C business — file Schedule C. If it's truly a hobby, accept the gross-only treatment.

---

## 3. Double-counting Schedule C profit on Line 8

**The mistake**: Filer enters Schedule C net profit on Line 3 ($50,000) AND adds the same amount on Line 8z as "self-employment income."

**Why it happens**: Confusion about which line catches "self-employment" — the form has both Line 3 (Schedule C result) and Line 8 (other income), and "self-employment" sounds like it could go on either.

**Consequence**: $50,000 phantom income, $7,650 phantom SE tax. CP2000 if caught; significant overpayment if uncaught.

**Fix**: Schedule C net profit goes on Line 3 **only**. Line 8 is for income not on a separate schedule. Cross-check: the sum of all 1099-NECs and 1099-Ks should equal Schedule C Line 1, not double-appear on Schedule 1.

---

## 4. Reporting state refund as taxable when it isn't

**The mistake**: Filer who took the standard deduction in 2025 reports a $400 state refund on Line 1 in 2026. Or filer who itemized but had the SALT cap maxed by property tax reports the refund as taxable.

**Why it happens**: Form 1099-G Box 2 looks like income. Filers assume any 1099 amount is reportable.

**Consequence**: Phantom income, ~$88-$120 unnecessary tax depending on bracket.

**Fix**: Run the tax benefit test (see [`state-refund-taxability.md`](./state-refund-taxability.md)). Standard-deduction filers: Line 1 = $0, always. Itemized filers: check whether SALT cap consumed all of the state income tax deduction.

---

## 5. Claiming SE health insurance when employer plan was available

**The mistake**: Filer claims $6,000 SE health insurance on Line 17 for the year, but their spouse had an employer plan available (subsidized) that the family chose not to use.

**Why it happens**: The eligibility test in IRC §162(l)(2)(B) disallows SE health insurance for any month the user **or spouse** was *eligible* for an employer plan — even if they didn't enroll.

**Consequence**: Disallowed deduction in audit. The fix is to apportion the premium by month — eligible months only.

**Fix**: For each month, ask: "Was the user OR their spouse eligible for an employer-subsidized plan?" If yes, that month's premium is **not** deductible on Line 17. Only months where neither had access count.

---

## 6. Forgetting to attach required supporting forms

**The mistake**: Filer claims Line 13 (HSA), Line 14 (Armed Forces moving), Line 15 (SE tax half), or Line 23 (Archer MSA) but doesn't attach the required form (8889, 3903, Schedule SE, 8853).

**Consequence**: Return rejected (e-file) or held up (paper). The IRS asks for the missing form before processing the deduction.

**Fix**: Run the attachment checklist. If Line 13 > 0 → Form 8889 attached. If Line 14 > 0 → Form 3903. If Line 15 > 0 → Schedule SE. If Line 23 > 0 → Form 8853. If Line 12 > 0 → Form 2106. (See [`line-by-line.md`](./line-by-line.md) attachment map.)

---

## 7. Taking student loan interest deduction over the $2,500 cap

**The mistake**: Filer paid $3,200 of student loan interest and reports the full $3,200 on Line 21.

**Why it happens**: The $2,500 cap is statutory (IRC §221) and doesn't change with inflation. Some filers think it's the phaseout, not the cap.

**Consequence**: $700 over-deduction. Caught by IRS automatic 1098-E matching.

**Fix**: Cap Line 21 at $2,500. The phaseout (MAGI-based) further reduces the cap, never raises it. Available with the standard deduction — but capped.

---

## 8. Pre-2019 vs. post-2018 alimony confusion

**The mistake**: Filer with a 2021 divorce decree reports alimony received on Line 2a (or alimony paid on Line 19a). Or filer with a 1998 decree omits it because "alimony isn't taxable anymore."

**Why it happens**: TCJA flipped the alimony rule for decrees executed **after December 31, 2018**. Pre-2019 decrees still follow the old rules (deductible by payer / income to recipient). The cutoff date is the source of confusion.

**Consequence**: Wrong income inclusion or wrong deduction. Both directions get caught — the IRS cross-matches alimony deductions on Line 19a against the recipient's SSN on Line 19b.

**Fix**: Confirm the **original decree date**. Pre-2019: use Lines 2a and 19a. Post-2018: alimony is neither income nor deduction — leave Lines 2a and 19a blank.

---

## 9. Putting digital asset income on the wrong line

**The mistake**: Filer who runs a regular crypto-mining or NFT-creation business reports all crypto income on Line 8v ("Digital assets received as ordinary income") instead of Schedule C.

**Why it happens**: Line 8v is new and prominent on the 2024+ Schedule 1. It feels like the right line for any crypto income.

**Consequence**: Skipping Schedule C means no expense deductions (electricity, equipment, software, professional fees) AND no Schedule SE. Net result: inflated income tax, but missed SE tax (which IRS will assess separately).

**Fix**: If the activity is regular, profit-motive, and would be a trade or business under §162 — it's Schedule C. Line 8v is for **passive** receipt of digital assets (occasional payment, airdrops, small-scale staking, NFT royalties from prior sales). Mining/NFT-creation businesses → Schedule C → Line 3, not 8v.

---

## 10. Treating a 1099-K as Line 8 income when it should be Schedule C (or zero)

**The mistake**: Filer received a 1099-K and reports the gross 1099-K amount on Line 8z, treating it as miscellaneous income.

**Why it happens**: The IRS lowered the 1099-K threshold (now $2,000 for 2026 from the original $20,000). More filers are getting forms they've never seen. They guess Line 8 because it looks like a catchall.

**Consequence**: Overpayment if the activity was personal items sold at a loss (not taxable at all). Underpayment of SE tax if it was actually self-employment that should be Schedule C → Schedule SE.

**Fix**: Three paths:
- **Personal items sold at a loss / 1099-K in error** → enter on the dedicated row above Part I (not on Line 8). Reconciles to zero taxable.
- **Trade or business income** → Schedule C → flows to Line 3. Don't put it on Line 8.
- **Investment income** (rare on 1099-K) → Schedule D / Form 8949.

Never put a 1099-K on Line 8z.

---

## Bonus mistakes (honorable mentions)

### Skipping Line 7 unemployment because "I didn't get the money — it was direct-deposited"

All unemployment compensation is taxable. The 1099-G Box 1 reports it; Line 7 captures it. Pandemic-era exclusions ($10,200 ARPA) are not in effect for 2026.

### Claiming Line 11 (educator expenses) when not a 900-hour K-12 educator

Tutors, college TAs, after-school program staff, and homeschool parents do **not** qualify. The 900-hour K-12 elementary/secondary test is strict.

### Claiming Line 16 (SEP/SIMPLE) without sufficient SE earnings

Owner contribution to a SEP-IRA is capped at ~20% of net SE earnings (after §164(f)). Putting $5,000 into a SEP when net SE earnings is $10,000 means $3,000 is over the cap and creates an excess contribution subject to 6% excise tax (IRC §4973).

### Taking Line 18 (early withdrawal penalty) on a 401(k) distribution

Line 18 is for **savings instruments** (CDs, time deposits) that imposed a penalty for early withdrawal. The 10% additional tax on early 401(k) / IRA distributions before 59½ is a penalty *tax* (Schedule 2), not a Line 18 deduction. Different mechanism, different line.

### Forgetting that Line 22 is always blank

Every year, some filer fills Line 22 with something. It's reserved for future use — leave blank.

---

## Pre-submission validation checklist

Before declaring Schedule 1 ready:

- [ ] Run every Part II line — don't skip just because the user "took the standard deduction"
- [ ] If Line 3 > 0, Schedule SE is in the package and Line 15 has the half-SE-tax amount
- [ ] Line 1 only has an amount if user itemized last year AND deducted state income tax AND had marginal benefit
- [ ] Line 8j hobby income is gross (no expense offset)
- [ ] Line 8 entries don't double-count Schedule C income that's on Line 3
- [ ] Line 17 SE health insurance accounts for any employer-plan-eligible months
- [ ] Line 21 student loan interest is capped at $2,500 and within phaseout
- [ ] Line 19a alimony only if pre-2019 decree, with 19b SSN and 19c date
- [ ] Required attachments listed (8889, 3903, Sch SE, 2106, 8853)
- [ ] Line 22 is blank
- [ ] Line 10 = Lines 1 + 2a + 3 + 4 + 5 + 6 + 7 + 9
- [ ] Line 26 = Lines 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19a + 20 + 21 + 23 + 25

---

## Sources

- IRS Schedule 1 (Form 1040), 2025 revision
- IRC §§61, 111, 162(l), 164(f), 183, 221, 223, 4973
- IRS Publication 525, 535, 969, 970
- TCJA §11051 (alimony), §11041 (miscellaneous itemized deduction suspension)
