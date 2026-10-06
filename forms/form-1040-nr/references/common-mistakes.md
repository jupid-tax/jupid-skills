# Common Form 1040-NR Mistakes

Each entry: the mistake, the rule it breaks, how the agent catches it. Sources are the 2025 Form 1040-NR, its instructions (dated Jan 29, 2026), and Pub. 519 (2025) unless noted.

---

### 1. Filing Form 1040 instead of Form 1040-NR (or the reverse)

**Rule:** Form 1040-NR is for nonresident aliens; residents under the green card or substantial presence test file Form 1040. Payroll and consumer software often default students and visitors to Form 1040, which claims a standard deduction and credits a nonresident cannot take.
**Catch:** run the residency tests before anything else and write the result line into the draft. If a Form 1040 was already filed in error, the fix is Form 1040-X with the correct return attached ([`../../form-1040-x/SKILL.md`](../../form-1040-x/SKILL.md)).

### 2. Counting prior-year days at full value, or forgetting the 31-day test

**Rule:** IRC §7701(b)(3): current-year days × 1, first prior year × 1/3, second prior year × 1/6; at least 31 current-year days.
**Catch:** show the formula with the three day counts; check item H matches.

### 3. Excluding student or trainee days without Form 8843

**Rule:** exempt-individual days (other than A/G foreign government-related individuals) and medical-condition days are excluded only with a timely Form 8843.
**Catch:** any excluded days → Form 8843 in the attachment list; no return required → Form 8843 mailed alone to Austin, TX 73301-0215 by the 1040-NR due date.

### 4. Treating an F/J student as exempt forever

**Rule:** a student is not exempt after more than 5 calendar years as an exempt teacher, trainee, or student unless they establish no intent to reside permanently; a teacher or trainee is not exempt if exempt in any part of 2 of the prior 6 years (with a narrow foreign-employer exception).
**Catch:** ask for the visa held in each of the prior six years and count exempt years.

### 5. Claiming the standard deduction

**Rule:** nonresident aliens cannot take the standard deduction; the only exception is students and business apprentices eligible under Article 21(2) of the U.S.–India treaty (Pub. 519 ch. 5).
**Catch:** line 12 must equal Schedule A (Form 1040-NR) line 8 unless the India exception is documented.

### 6. Using MFJ or head of household, or the Single column when married

**Rule:** Form 1040-NR has Single, MFS, QSS, Estate, Trust. Married → MFS unless the five-test Single exception applies to a resident of Canada, Mexico, or South Korea, a U.S. national, or an India Art. 21(2) student or apprentice.
**Catch:** ask marital status on December 31 and residence country; check the Tax Table column used on line 16.

### 7. Putting portfolio dividends or bank interest on page 1

**Rule:** only ECI goes on lines 2b and 3b. U.S.-source dividends that are not ECI go on Schedule NEC line 1a at 30% or the treaty rate; U.S. bank deposit interest is exempt and not reported.
**Catch:** for each Form 1099-INT/1099-DIV/1042-S, ask whether the account is an asset of the U.S. business.

### 8. Taxing capital gains a nonresident doesn't owe tax on

**Rule:** non-ECI U.S.-source capital gains are taxed at 30% only if present 183 days or more in the year (IRC §871(a)(2)); otherwise they are exempt. U.S. real property gains are always ECI.
**Catch:** if days present < 183, Schedule NEC lines 16–18 stay empty for stock sales; real estate goes to Schedule D and line 7a.

### 9. Charging (or skipping) self-employment tax

**Rule:** a nonresident owes SE tax only when a totalization agreement places them in the U.S. social security system.
**Catch:** ask for the certificate of coverage before filling line 23b; never assume either answer.

### 10. Missing Form 1042-S withholding

**Rule:** chapter 3 or 4 withholding in box 10 of Form 1042-S is a payment on line 25g; Forms 8805 and 8288-A go on 25e and 25f; these refunds can take up to 6 months.
**Catch:** reconcile every 1042-S to a line; attach to the front of the return (8805 to the back).

### 11. Reporting treaty-exempt income twice or not at all

**Rule:** treaty-exempt income goes on Schedule OI item L and line 1k only. Leaving it off entirely is not a treaty claim.
**Catch:** item L(1)(e) = line 1k; the same dollars cannot appear on 1a–8 or Schedule NEC (except treaty-exempt interest that was withheld on, which goes on NEC column (d) at 0%).

### 12. Skipping a required Form 8833

**Rule:** treaty-based return positions not waived by Treas. Reg. §301.6114-1(c) require Form 8833; penalty $1,000 per failure for individuals (IRC §6712). Dual-resident tie-breaker claims always require it.
**Catch:** list every treaty position and cite the waiver or mark Form 8833 required ([`treaty-claims.md`](./treaty-claims.md)).

### 13. Filing late and losing all deductions

**Rule:** deductions and credits are allowed only on a timely return: within 16 months of the due date if the prior-year return was filed or this is the first required year (Treas. Reg. §1.874-1(b)). A 2025 return due June 15, 2026 must be filed by October 15, 2027 to keep deductions.
**Catch:** compute and print the 16-month date on every draft; flag any return past it.

### 14. Wrong due date

**Rule:** April 15, 2026 if the user received wages as an employee subject to U.S. income tax withholding; June 15, 2026 otherwise (IRC §6072(c)). Form 4868 extends filing, not payment.
**Catch:** decide from the W-2, not from whether the user "has U.S. income".

### 15. Folding the LLC's filing into the owner's return

**Rule:** a foreign-owned domestic disregarded entity files a pro forma Form 1120 with Form 5472; the owner separately reports ECI on Form 1040-NR (Pub. 519 ch. 7).
**Catch:** whenever an LLC appears, add the Form 5472 handoff ([`../../form-5472/SKILL.md`](../../form-5472/SKILL.md)).

### 16. E-filing a return that must go on paper

**Rule:** returns with a Form W-7 go to the ITIN Operation by mail; a return using an ITIN can't be e-filed in the calendar year the ITIN is assigned (Instructions for Form W-7); dual-status 2025 returns can't be e-filed (Pub. 519).
**Catch:** run the decision tree in [`../filing.md`](../filing.md).

### 17. Claiming credits a nonresident can't take

**Rule:** no EIC (line 27 reserved), no education credits, CTC/ODC/ACTC only for U.S. nationals and residents of Canada or Mexico (limited for South Korea and India).
**Catch:** sanity checks in SKILL.md Validation.

### 18. Paying from a foreign bank by check

**Rule:** a check or money order must be drawn on a U.S. financial institution, with "2025 Form 1040-NR", name, address, phone, and SSN/ITIN, plus Form 1040-V.
**Catch:** if the user has no U.S. account, point to IRS.gov/Individuals/International-Taxpayers/Foreign-Electronic-Payments.
