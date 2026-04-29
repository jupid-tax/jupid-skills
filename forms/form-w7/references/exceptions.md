# W-7 Exceptions — When the W-7 Can Be Filed Alone

The default rule is that Form W-7 must be filed **with** a federal tax return that requires the ITIN. This makes sense in most cases — the ITIN exists to enable tax filing.

But the IRS recognizes several situations where a person needs an ITIN before filing a return, or where no return is needed at all. These are the **Exceptions** (1-5) listed in Form W-7 instructions. When applying under an exception, the W-7 is filed **alone** with supporting evidence, not with a 1040 / 1040-NR.

The agent's job: identify which exception applies, gather the right supporting evidence, and skip the tax return attachment.

---

## Exception 1 — Passive income (third-party withholding)

**Who**: Nonresident aliens who receive U.S.-source passive income (dividends, royalties, rent, etc.) where the U.S. payer withholds tax under §1441 / §1442 (typical 30% NRA withholding rate). They need an ITIN so the payer can issue Form 1042-S.

Examples:
- Foreign investor receiving U.S. stock dividends through a U.S. broker
- Foreign person receiving royalties from a U.S. licensee
- Foreign owner of U.S. mineral rights receiving royalty payments

**Required evidence**:
- A signed letter on official letterhead from the withholding agent (broker, payer, etc.) identifying the applicant as a payee, including the type and amount of income, and stating that an ITIN is required to facilitate withholding/reporting
- W-8BEN typically also signed and held by the withholding agent

**Reason code**: Box (a) [if treaty benefit claimed] or Box (h) — Other.

---

## Exception 2 — Other income / treaty-exempt scholarship

**Who**: Nonresident aliens with U.S. income that may be treaty-exempt or partially exempt. Common case: foreign scholars, students, or researchers receiving treaty-exempt scholarship/fellowship grants.

Examples:
- Indian student claiming Article 21 of U.S.-India treaty for scholarship income
- French postdoc claiming Article 21 of U.S.-France treaty for fellowship

**Required evidence**:
- Letter from the educational institution / paying party identifying the applicant and the income
- Form 8233 (claim of treaty exemption from withholding on compensation) typically attached
- The treaty article being claimed cited at the top of the W-7

**Reason code**: Box (a) or (f).

---

## Exception 3 — Mortgage interest (§6045)

**Who**: Foreign individuals who are buyers/sellers of U.S. real estate and need an ITIN for mortgage interest reporting under IRC §6045 / Form 1098.

Examples:
- Foreign buyer of U.S. residential property who is paying mortgage interest and needs the lender to issue Form 1098 with their ITIN
- Foreign property owner who refinances a U.S. mortgage

**Required evidence**:
- Letter from the lender stating that an ITIN is needed for Form 1098 reporting
- Mortgage statement or settlement statement showing the applicant as the borrower
- Property address

**Reason code**: Box (h) — Other.

---

## Exception 4 — FIRPTA (§1445)

**Who**: Foreign sellers of U.S. real estate. Under IRC §1445 (FIRPTA), the buyer must withhold up to 15% of the sale price unless an exception applies, and must report withholding to the IRS via Form 8288 / 8288-A. The seller needs an ITIN to be identified on these forms and to file a U.S. return claiming the actual gain (which is usually less than 15% of sale price).

Examples:
- Foreign individual selling a U.S. vacation home
- Foreign person disposing of U.S. partnership interest in a real estate partnership
- Foreign person receiving distributions from a USRPHC (U.S. real property holding corporation)

**Required evidence**:
- Closing/settlement statement (HUD-1 or equivalent) identifying the applicant as the seller
- Form 8288-A (the buyer's withholding statement) if available
- Property address and sale date

**Reason code**: Box (h) — Other; specify "FIRPTA seller / IRC §1445".

**Note**: FIRPTA situations are tax-strategically important because the §1445 withholding (15% of sale price) typically exceeds the actual gain (because the basis offsets most of the proceeds). The seller files Form 1040-NR after closing to claim a refund. The ITIN application happens before that filing — that's why Exception 4 lets the W-7 go alone.

---

## Exception 5 — Foreign-owned U.S. corporation (§6038A)

**Who**: A 25%-or-more foreign owner of a U.S. corporation (CFC reporter), where the corporation must file Form 5472. The foreign owner needs an ITIN to be identified on Form 5472.

Less common; mostly for tax practitioners advising large international corporate structures.

**Required evidence**:
- Form 5472 attached or referenced
- Documentation of the foreign owner's >25% interest

**Reason code**: Box (h) — Other; specify "§6038A reporter / Form 5472".

---

## Exception decision tree

```
Is the applicant filing their own 1040 / 1040-NR?
  YES → No exception; default rule applies (W-7 with return)
  NO  ↓
    Does the applicant have U.S. passive income with third-party withholding?
      YES → Exception 1
      NO  ↓
        Does the applicant have treaty-exempt scholarship / fellowship / other income?
          YES → Exception 2
          NO  ↓
            Is the applicant getting U.S. mortgage interest reported (Form 1098)?
              YES → Exception 3
              NO  ↓
                Is the applicant a foreign seller of U.S. real estate (FIRPTA)?
                  YES → Exception 4
                  NO  ↓
                    Is the applicant a 25%+ foreign owner of a U.S. corporation?
                      YES → Exception 5
                      NO  → No exception applies; W-7 cannot be filed alone
```

---

## When NOT under an exception — the default rule

If no exception applies, the W-7 must be filed with a tax return that requires the ITIN. Common cases:

- Spouse on MFJ return → W-7 attached to the primary filer's 1040 → reason code (e)
- Dependent claimed on someone's 1040 → W-7 attached to the primary filer's 1040 → reason code (d)
- Nonresident alien with U.S. business income → W-7 attached to 1040-NR → reason code (b)
- Resident alien (substantial presence) with U.S. income → W-7 attached to 1040 → reason code (c)

The W-7 is on top of the return packet. The return cannot be e-filed when an ITIN is being applied for; mail to the **IRS Austin ITIN Operation** (different from regular 1040 mailing addresses).

---

## Common mistakes with exceptions

1. **Claiming Exception 4 (FIRPTA) without a closing statement** → IRS rejects; needs HUD-1 or equivalent
2. **Filing W-7 alone hoping to "pre-issue" an ITIN** before having a tax filing obligation → IRS rejects; ITIN is issued only when there's a documented need (filing or exception)
3. **Confusing Exception 2 (treaty-exempt income) with reason code (a) on the form** → Box (a) is the reason code for "claiming treaty benefit"; Exception 2 is the basis for filing without a tax return. Both can apply simultaneously: check (a) and reference Exception 2 in supporting evidence.
4. **Treating Exception 3 (mortgage interest) as automatic for any foreign property buyer** → Exception 3 is specifically for the §6045 information-reporting case where a lender needs the ITIN for Form 1098. If the foreign buyer is also receiving rental income, they likely need a 1040-NR (no exception).

---

## Citation summary

- IRC §1441 / §1442 — NRA withholding (relevant for Exception 1)
- IRC §1445 — FIRPTA (relevant for Exception 4)
- IRC §6038A — Foreign-owned U.S. corporations (relevant for Exception 5)
- IRC §6045 — Information returns / mortgage interest (relevant for Exception 3)
- Form W-7 instructions — Exceptions table
- Form 8288 / 8288-A — FIRPTA withholding forms: <https://www.irs.gov/pub/irs-pdf/f8288.pdf> and <https://www.irs.gov/pub/irs-pdf/f8288b.pdf>
- Form 5472 — Information return of foreign-owned corporations
- Form 1042-S — Foreign person's U.S. source income
- Form 8233 — Compensation treaty exemption
- Form 1098 — Mortgage interest statement
