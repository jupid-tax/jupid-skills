# Handling Form 5498 (verification, corrections, archiving)

Form 5498 is **not filed by the recipient**. The IRA custodian files it
with the IRS (by May 31 of the year following the contribution year) and
sends a copy to the account holder. The recipient's job is to verify it
matches their tax return and resolve mismatches before the IRS does.

This file describes:

1. The verification flow an agent runs when the user shares a 5498
2. How to request a corrected 5498 from the custodian if the original is wrong
3. How to amend the user's tax return if the 5498 is right but the return was wrong
4. Archiving and recordkeeping rules

The agent never "files" Form 5498 with the IRS on the user's behalf — that's
the custodian's responsibility.

---

## Section 1 — Verification flow

### Pre-flight

Agent must have:

- The Form 5498 (PDF, photo, or transcribed values box-by-box)
- The user's tax return for the same tax year (Form 1040, Schedule 1,
  Schedule 2, Form 8606 if applicable)
- Any 1099-Rs the user received for the same year
- Any other Forms 5498 if the user has multiple IRAs at different
  custodians

### Browser / data flow

1. **Confirm the tax year.** A 5498 received in May 2026 is for tax year
   2025. The boxes that include "amounts contributed by April 15"
   (Boxes 1, 8, 9, 10) report contributions designated for the prior
   tax year, even if deposited in the current year.

2. **Read Box 7 to determine the IRA type.** This drives which other
   contribution box should be populated.

3. **Walk every populated box** and map it to the relevant return line.
   Use the table in `SKILL.md` Step 3 / Step 4 / Step 5.

4. **Compute the reconciliation status** for each box: Match / Mismatch /
   N/A.

5. **For mismatches**, decide which is wrong:
   - The 5498 (custodian error) → Section 2 below
   - The return (filer error) → Section 3 below
   - Neither (timing or interpretation issue) → document the
     reconciliation and explain to the user why both are correct

6. **For Box 11 (RMD required for next year)**: confirm the user has
   either taken or scheduled the next year's RMD. If not, hand off to
   the `form-5329` skill for missed-RMD handling.

7. **Capture Box 5 (FMV 12/31)** for next year's RMD calculation. If the
   user has multiple IRAs, sum Box 5 across all 5498s for the IRA
   aggregate RMD.

8. **Produce the reconciliation report** per `SKILL.md` Output format.

9. **Archive the 5498** in the user's tax records (see Section 4).

---

## Section 2 — Requesting a corrected 5498 from the custodian

If the 5498 is wrong (rare but happens — most often when the custodian
miscoded a contribution year, or applied a contribution to the wrong
account type), the user must request a corrected 5498.

### When to request

- Box 1 / 8 / 9 / 10 amount is wrong (e.g., custodian recorded $7,000
  but only $5,000 was actually contributed)
- Box 7 IRA type is wrong (custodian miscoded a Roth as a traditional
  or vice versa)
- Box 2 rollover amount is wrong (e.g., shows the gross 401(k)
  distribution but only part was rolled over)
- Box 3 conversion amount is wrong
- Box 11 RMD checkbox is set incorrectly (user is under 73 and a Roth
  IRA owner — Roth IRAs have no lifetime RMD for the original owner)
- Account holder name or SSN is wrong

### How to request

1. **Contact the custodian's tax-form team.** Each custodian has a
   process; common ones:
   - Fidelity: log in → Tax Forms → Request a Correction
   - Vanguard: contact via secure message; reference the specific 5498
   - Schwab: log in → Statements & Tax Forms → "Need a correction?"
2. **Provide documentation** supporting the correct value (deposit
   confirmations, contribution paperwork, account-opening documents).
3. **Wait for the corrected 5498** — typically 4-8 weeks. The custodian
   files a corrected 5498 with the IRS marked "CORRECTED" in the top
   checkbox; the user receives a copy.
4. **Reconcile again** against the return once the corrected 5498
   arrives. If the return matches the corrected 5498, no further action.
   If not, see Section 3.

### What if the custodian refuses?

If the custodian believes the original 5498 is correct and the user
disagrees:

1. Ask for the documentation the custodian relied on
2. If the user still disagrees, the user may attach a statement to their
   return explaining the discrepancy
3. As a last resort, the user can request IRS intervention through the
   CP2000 process — when the IRS sends a notice based on the (incorrect)
   5498, the user replies with documentation and asks for the assessment
   to be reversed

This is rare. Custodians generally correct in good faith when the user
has solid documentation.

---

## Section 3 — Amending the return when the 5498 is correct

If the 5498 is correct and the return underreports or overreports a
contribution / rollover / conversion, the user amends via Form 1040-X.

### Pre-flight for amendment

Agent must have:
- The original return as filed
- The 5498(s) that triggered the discrepancy
- Any 1099-Rs that should also be reconciled
- The user's permission to amend

### Amendment scenarios

#### Scenario A — IRA deduction was claimed but Box 1 is smaller

User claimed $7,000 deduction on Schedule 1 Line 20 but Box 1 = $5,000.
Likely explanation: only $5,000 was actually contributed (the rest was a
withdrawal mistakenly thought to be a contribution; a deposit went to a
different account; etc.).

**Action**: Reduce Schedule 1 Line 20 to $5,000 via Form 1040-X. The
user owes additional tax on the $2,000 difference plus any interest.

#### Scenario B — IRA deduction was *not* claimed but Box 1 has a deductible amount

User contributed $7,000 (Box 1 = $7,000) and is fully deductible-eligible
but didn't claim the deduction on Schedule 1. (Common when filing is
rushed and the contribution was forgotten.)

**Action**: Claim the $7,000 deduction on Schedule 1 Line 20 via Form
1040-X. The user is owed a refund.

#### Scenario C — Roth conversion is on 5498 Box 3 but missing from return

User did a conversion, the 5498 reflects it (Box 3) and the 1099-R reflects
it, but the return failed to include the conversion as taxable income on
Form 1040 Line 4b (and Form 8606 Part II was not completed).

**Action**: Amend to include the conversion on Form 1040 Line 4a/4b and
attach a corrected Form 8606 Part II computing the taxable portion.
Significant tax + interest may be owed.

#### Scenario D — Rollover (Box 2) was reported as taxable on the return

User rolled over a 401(k) to an IRA (Box 2 = $50,000). The 1099-R was
issued with code G (direct rollover). The user mistakenly reported the
$50,000 as taxable on Form 1040 Line 5b.

**Action**: Amend to set Line 5b = $0 (or appropriate non-taxable
amount), with "Rollover" written in the margin or via the appropriate
code. The user is owed a substantial refund.

### Amendment process

1. Use the `form-1040-x` skill (when available) for the actual
   amendment mechanics
2. Attach a copy of the corrected statement explaining the
   reconciliation
3. File electronically (Form 1040-X is e-fileable as of recent years)
   or paper
4. Wait 8-16 weeks for IRS processing

---

## Section 4 — Archiving and recordkeeping

The IRS recommends retaining tax-related documents for 7 years after the
return due date (longer for any year with basis tracking — Form 8606
basis records should be kept indefinitely).

### What to retain related to Form 5498

- The original Form 5498 (PDF or paper)
- Any corrected Form 5498 issued
- Custodian statements showing the contribution / rollover / conversion
  activity that the 5498 reports
- The tax return that the 5498 was reconciled against
- The reconciliation report produced by this skill
- Any Form 1040-X amendments made because of the 5498
- Form 8606 for every year with nondeductible contributions or
  Roth conversions (basis tracking — keep forever)

### Storage

- Digital: encrypted folder on the user's tax records archive
- Physical: folder per tax year, IRA section
- Cloud: encrypted cloud storage with multi-factor authentication

The agent should never store the user's SSN, account numbers, or other
PII in agent logs or transcripts. Pull at verification time, use,
discard.

---

## Section 5 — Common follow-up questions

### "Do I need to file Form 5498 with the IRS?"

No. The custodian files it. The user keeps the copy for records.

### "Why did I get my 5498 in May, after I already filed my return?"

Because Form 5498 is due May 31 of the year following the contribution
year. The IRS designed it this way because contributions for the prior
tax year can be made until April 15 (or extension date), so the 5498
deadline is set after the filing deadline.

If you discover a discrepancy after filing, see Section 3 (amend the
return).

### "I have a Roth IRA — why is Box 11 (RMD) checked?"

It shouldn't be, for the original Roth IRA owner. Roth IRAs have no
RMD requirement during the original owner's lifetime (IRC §408A(c)(5)).
This is likely a custodian error; request a corrected 5498.

Exception: an *inherited* Roth IRA does have RMD requirements for the
beneficiary in some cases (depending on death-year rules). If this is
an inherited account, Box 11 may legitimately be checked.

### "Box 5 (FMV) is much smaller than I expected. Did the custodian make a mistake?"

Possibly. Cross-check against your December 31 statement. Common causes
of legitimate small Box 5:
- Year-end market downturn
- Distributions taken late in the year
- Account closed and rolled out

If neither matches, ask the custodian.

### "Box 1 is $0 but I made an IRA contribution this year."

If you made the contribution before April 15 of the next year and
designated it for the prior tax year, it should appear in Box 1 of the
prior year's 5498 (which arrives by May 31 of the contribution year).

Check: is this the right year's 5498? A 2025-tax-year contribution
made in March 2026 appears on the 2025 5498 (received May 2026), not
the 2026 5498.

If the timing is right and Box 1 is still $0, contact the custodian.

---

## Security and consent rules

These are non-negotiable:

1. **Never store the user's SSN, account numbers, or balances** in agent
   logs or transcripts.
2. **Never request a corrected 5498 without the user's explicit
   authorization** at the moment of request.
3. **Never amend the user's return without explicit authorization** at
   the moment of amendment.
4. **Always show the user the reconciliation report** before
   communicating with the custodian or filing an amendment.
5. **If the user is an inherited-IRA beneficiary**, additional caution:
   the deceased's SSN may also appear on records and is also protected.
