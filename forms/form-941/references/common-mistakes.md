# Common Form 941 Mistakes

Audit-trip mistakes the agent should surface as warnings during validation. Each entry has the symptom, the IRS authority, and how to fix.

---

## 1. Reporting wages on the wrong quarter (cash basis vs. constructive receipt)

**Symptom**: Wages paid on March 31 reported on Q1; wages paid on April 1 reported on Q1 ("close enough").

**Rule**: Form 941 follows the **constructive receipt** rule. Wages are reported in the quarter the employee was actually paid (received the check or direct deposit), not the pay period. A pay period that ends March 26 but is paid March 30 → Q1. A pay period that ends March 26 but is paid April 4 → Q2.

**Authority**: IRS Reg. §31.3401(a)-1(a)(4); Pub. 15 section 4.

**Fix**: For a check/deposit dated April 1, the wages and FICA go on Q2 941 even though the work was done in March. Reconcile against the bank statement / payroll register, not the timesheet.

---

## 2. Confusing SS wages with FIT wages

**Symptom**: Line 2 = Line 5a col 1 in every case, regardless of pretax 401(k) deferrals.

**Rule**: 401(k) traditional deferrals **reduce Line 2 (FIT wages)** but do **not** reduce Line 5a (SS wages) or Line 5c (Medicare wages). This is the most common payroll-software misconfiguration.

**Authority**: IRC §3401(a)(12) (FIT exclusion for elective deferrals); IRC §3121(v)(1)(A) (FICA inclusion for elective deferrals).

**Fix**: For an employee with $50,000 gross + $5,000 401(k) deferral:
- Line 2 contribution: $45,000
- Line 5a col 1 contribution: $50,000
- Line 5c col 1 contribution: $50,000

Conversely, §125 cafeteria plan (health, dental, FSA, dependent care, transit/parking) reduces **both** FIT and FICA wages.

---

## 3. Missing the Social Security wage base cap

**Symptom**: An executive's SS wages on Line 5a continue to accrue past the wage base.

**Rule**: Once any employee's YTD SS wages reach the annual wage base ($176,100 for 2025; verify 2026), additional wages paid that calendar year are **SS-exempt**. Medicare continues with no cap.

**Authority**: IRC §3121(a)(1); SSA Annual Contribution and Benefit Base.

**Fix**: Track YTD SS wages per employee. Stop SS withholding when an employee crosses the base. Continue Medicare withholding (and Additional Medicare 0.9% if YTD comp > $200K).

Example: Executive earning $250K. By Q3 they cross $176,100 SS base. Q3 partial SS wages = the headroom amount; Q4 SS wages = $0. Medicare wages = full quarterly comp every quarter.

---

## 4. Failing to withhold Additional Medicare 0.9%

**Symptom**: High-earner crosses $200K YTD comp at this employer; Line 5d not populated.

**Rule**: Once an employee's YTD wages from this single employer reach $200,000, withhold 0.9% Additional Medicare on every dollar above $200K. Does not apply to employer share. Threshold is per-employer, not per-employee household.

**Authority**: IRC §3101(b)(2); IRS Reg. §31.3101-1(b).

**Fix**: Track YTD comp per employee. When the threshold crosses mid-quarter, the partial-quarter wages above $200K go on Line 5d.

The 0.9% withheld is not "matched" by the employer. The employee reconciles their actual liability on Form 8959 with their personal Form 1040 (which uses different thresholds for joint vs. single filers — out of scope for the employer).

---

## 5. Reporting 1099 contractor amounts on Form 941

**Symptom**: A "1099 contractor" gets paid through payroll and shows up on Line 2.

**Rule**: 1099 payments do not appear on Form 941 at all. Form 941 is for W-2 employees only. Contractor payments are reported on Form 1099-NEC (or 1099-MISC for some categories) at year-end.

**Authority**: IRC §3401(c) (definition of "employee" for FIT withholding); §3121(d) (employee for FICA); §6041, §6041A (1099 reporting requirements).

**Fix**: Remove the contractor from Form 941. If the worker is genuinely a contractor under the IRS 20-factor / common-law test, file 1099-NEC. If the worker is misclassified and is actually an employee, see [`941-x-corrections.md`](./941-x-corrections.md) for retroactive 941-X with reduced rates under §3509.

---

## 6. Treating S-corp shareholder distributions as wages

**Symptom**: An S-corp shareholder-employee took $100K out of the company; all $100K reported on Line 2.

**Rule**: S-corp shareholder-employees take both **W-2 wages (reasonable compensation)** and **K-1 distributions**. Only the W-2 wage portion goes on 941. Distributions appear on Schedule K-1 (Form 1120-S) and are not subject to FICA.

**Authority**: IRS Rev. Rul. 74-44 (reasonable compensation principle); ongoing IRS audit campaign on under-paid S-corp officers.

**Fix**: Decompose the $100K: based on industry / role / hours, decide reasonable compensation (e.g., $60K W-2 wages, $40K distribution). Run actual payroll for the wage portion (with FICA + FIT). The distribution is just a transfer, no payroll tax. See IRS Fact Sheet 2008-25 and S-corp Audit Technique Guide.

The IRS aggressively challenges $0 reasonable comp where an active S-corp owner takes large distributions.

---

## 7. Schedule B totals don't match Line 12

**Symptom**: Form 941 Line 12 = $25,000; Schedule B daily totals sum to $24,500.

**Rule**: Schedule B grand total **must** equal Form 941 Line 12. The IRS cross-checks automatically.

**Authority**: Schedule B (Form 941) instructions; Form 941 Line 16 instructions.

**Fix**: Recompute Schedule B from the payroll register. Common causes:
- Adjustments on Lines 7–9 not reflected in daily entries
- A pay date assigned to the wrong calendar day
- Employer FICA computed on column 1 instead of column 2

The IRS issues CP207 / CP207L when this fails. Better to catch it pre-filing.

---

## 8. Missing FTD deposits

**Symptom**: Quarter ends with Line 14 = $8,000 due, but no deposits were made during the quarter.

**Rule**: Monthly depositors must deposit by the 15th of the following month. Semi-weekly depositors must deposit per the Wed/Fri rule. Failure triggers Federal Tax Deposit penalty:

| Days late | Penalty |
|-----------|---------|
| 1–5 | 2% |
| 6–15 | 5% |
| 16+ | 10% |
| 10+ days after IRS notice | 15% |

**Authority**: IRC §6656; IRS Reg. §31.6302-1.

**Fix**: Set up EFTPS recurring deposits matched to payroll cadence. Don't wait until the quarter ends. If the user's prior quarter was a Box 1 (de minimis), it may have lulled them into not depositing — but if this quarter exceeds $2,500, deposits are required.

The Trust Fund Recovery Penalty (TFRP) under IRC §6672 can hold individuals personally liable (100% of unpaid trust-fund taxes) for repeated non-deposits.

---

## 9. Filing 941 when an annual Form 944 was assigned

**Symptom**: User filed Q1 941 in April, but the IRS sent a "you are a 944 filer" letter back in February.

**Rule**: The IRS designates very-small employers as **annual** Form 944 filers (annual liability ≤ $1,000). The employer can request to switch to 941 by writing to the IRS or calling 1-800-829-4933 — but the change takes effect the following calendar year, not retroactively.

**Authority**: IRS Reg. §31.6011(a)-1(a)(4); IRS Notice CP540.

**Fix**: If the IRS assigned 944, file 944 once per year (due January 31), not 941 quarterly. Filing 941 when 944 was assigned creates duplicate-filing rejection codes and confused IRS records.

To switch from 944 to 941: write to the IRS or call before April 1 of the year you want 941 to apply. The change applies to that calendar year forward.

---

## 10. Forgetting to file even if no wages were paid

**Symptom**: User had no employees during a quarter, didn't file 941.

**Rule**: Once an employer has filed any 941, they must continue filing **every quarter** even if no wages are paid (Line 1 = 0, Line 2 = 0) — unless they file a final return on Line 17 indicating cessation.

**Authority**: IRS Reg. §31.6011(a)-4(a)(1); Form 941 instructions.

**Fix**: File a "zero" 941 for any quarter with no wages but no final-return indicator. To stop filing permanently, check Line 17 with the last wage-paid date.

If the user has temporarily stopped paying wages (seasonal or pause): use Line 18 (seasonal indicator) to avoid late-filing notices, but still file each quarter wages were paid.

---

## 11. Wrong EIN format

**Symptom**: EIN entered as 123456789 (no hyphen) and IRS rejects.

**Rule**: EIN must be 9 digits formatted XX-XXXXXXX. Software and the IRS may auto-strip the hyphen, but providing it explicitly avoids parsing ambiguity. Cannot be a Social Security number.

**Authority**: IRS Form SS-4 instructions.

**Fix**: Verify against the EIN assignment letter (CP 575) or prior W-2/W-3 transmittal records. If EIN is unknown, retrieve via 1-800-829-4933 (after identity verification) or via Form SS-4 application history.

If the EIN truly doesn't exist for this entity, the user shouldn't be filing 941 at all — they need to apply for an EIN first via Form SS-4.

---

## 12. Mixing FFCRA / ARPA leave credit lines on a current 2026 quarter

**Symptom**: User populates Lines 5a(i), 5a(ii), 11b–11f, or 13b–13z on a 2026 quarter return.

**Rule**: FFCRA / ARPA sick-leave and family-leave credits expired **September 30, 2021**. Any leave wages or credits past that date are not allowed unless retroactively claimed via 941-X for an open tax year (limited window).

**Authority**: ARPA §9641 (sunset date); Notice 2021-24.

**Fix**: For 2026 quarters, default these lines to $0. If the user genuinely has FFCRA-period sick leave wages they want to claim, use 941-X for the appropriate 2020 / 2021 quarter, not the current quarter — and verify the §6511 statute of limitations hasn't expired.

The Employee Retention Credit (ERC) similarly ended Sept 30, 2021 (recovery startup businesses had Q4 2021). The IRS continues to aggressively audit ERC claims; new ERC claims via 941-X face heightened scrutiny.
