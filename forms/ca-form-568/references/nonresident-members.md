# Nonresident Members — Form 3832 Consent and Form 592 Withholding

When a California LLC has nonresident members (any member who is not a California resident at the end of the year), the LLC has additional obligations: collect Form 3832 consents OR withhold and remit on the member's behalf via Form 592 / 592-A / 592-Q / 592-B.

The agent's job: identify each nonresident member, determine their consent status, and generate the right combination of attachments and withholding deposits.

---

## Why this matters

California taxes nonresidents on California-source income. If a nonresident invests in a California LLC, California wants to collect its share of income tax on the member's distributable California-source income. Two ways:

1. **Member consents** to California jurisdiction (Form 3832) → member files their own California Form 540NR and pays directly. LLC has no withholding obligation.
2. **Member doesn't consent** → LLC withholds 7% of distributable California-source income > $1,500 and remits to FTB. LLC also pays partnership-level tax on Schedule T.

Both: the LLC issues Form 592-B to the member showing withheld amounts, and the member can claim a credit on their 540NR (if they file).

---

## Form 3832 — Nonresident Member Consent

**Purpose**: Each nonresident member signs Form 3832 to consent to California's jurisdiction to tax them on their distributable share. By signing, the member commits to file Form 540NR in California and report the LLC income directly.

**Mechanic**:
1. LLC sends Form 3832 to each nonresident member at the start of the year (or before filing the return)
2. Member signs and returns it
3. LLC attaches all signed Form 3832s to Form 568 when filing
4. LLC has **no withholding obligation** for that member
5. Member is responsible for filing 540NR and paying any California tax on their own

**If the member refuses to sign or doesn't return Form 3832**:
- LLC must withhold 7% of distributable California-source income > $1,500
- LLC must complete Schedule T (568) to compute partnership-level tax on the member's share at 12.3% (individual) or 8.84% (corporate)
- Both withholding **and** Schedule T tax apply — the LLC pays the higher of the two, and the member gets credit for whichever was paid

---

## Form 592 — Withholding Statement (annual)

**Purpose**: Annual reconciliation of all California nonresident withholding the LLC did during the year.

**Filing deadline**: Last day of February (paper) or March 31 (electronic) — but in practice it's filed in conjunction with the Form 568.

**Required when**: any nonresident member did not sign Form 3832 and the LLC withheld during the year.

**Components**:
- Cover page (Form 592) — summary
- Form 592-B — one per nonresident member showing the amount withheld for them
- Underlying deposits — quarterly (Form 592-Q) or per-payment (Form 592-A)

---

## Form 592-A — Foreign Partner / Member Annual Return

**Purpose**: Specifically for **foreign (non-U.S.)** nonresident members. Different from Form 592 (which covers U.S. nonresidents from other states).

**Filing**: by the 15th day of the 4th month after the LLC's tax year-end. Quarterly deposits use Form 592-Q.

> **Out of scope warning**: Foreign members trigger federal §1446 withholding obligations on the LLC for federal partnership purposes, plus California 592-A. These cases are complex; redirect to a CPA.

---

## Form 592-Q — Estimated Quarterly Withholding

**Purpose**: Quarterly deposit voucher for nonresident withholding.

**Due dates** (calendar year):
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: January 15 of following year

The LLC computes 7% × (estimated CA-source distributable income to non-consenting nonresidents) per quarter and deposits via Form 592-Q.

---

## Form 592-B — Member Statement

**Purpose**: Statement to each nonresident member showing the amount withheld for them. Analogous to a federal Schedule K-1 with withholding info.

The member attaches Form 592-B to their California Form 540NR to claim credit for the withheld amount.

---

## Withholding rate and threshold

- **Rate**: 7% of California-source distributable income
- **Threshold**: First $1,500 of California-source distributable income to a single nonresident member is exempt; withhold on the excess
- **Exception**: If the LLC has actual California-source income for the year that's < $1,500 per nonresident member, no withholding required

> Under R&TC §18662(b), withholding is required for nonresident members. Rate is 7% by default; can be reduced via Form 588 (Nonresident Withholding Waiver Request) in narrow circumstances.

---

## Schedule T (568) — Nonconsenting Nonresident Members' Tax

For each member who didn't sign Form 3832:

| Column | What goes here |
|--------|----------------|
| Member name | |
| SSN / ITIN / EIN | |
| Distributable CA-source share (from K-1 568) | |
| Rate: 12.3% (individual) or 8.84% (C-corp member) | |
| Tax = share × rate | |

Sum → Form 568 Line 4 (Nonconsenting nonresident members' tax).

This is paid by the LLC, **in addition to** any 7% withholding via Form 592. The member can take credit on their 540NR for both — but the LLC ends up paying two California amounts on the same income (12.3% + 7%). This is intentional: it creates a strong incentive for the LLC to collect Form 3832 consents.

---

## When NOT to worry about nonresident withholding

If **all** of the following are true, the LLC can skip the entire Form 592 / 592-Q / Schedule T flow:

- Every nonresident member signed Form 3832 (consents on file, attached to Form 568)
- No foreign (non-U.S.) members
- No member's distributable CA-source income exceeds $1,500 (de minimis exemption)

Most well-organized small LLCs collect Form 3832 from every nonresident member at formation and file them with each year's Form 568. This is the operationally simple path.

---

## Common mistakes

1. **Filing Form 568 without attaching Form 3832 for nonresident members**. FTB notice; LLC may be assessed withholding and Schedule T retroactively.
2. **Withholding 7% on member who signed Form 3832**. Refund process is slow; avoid.
3. **Not issuing Form 592-B to members**. Member can't take credit on 540NR; member files complaint with LLC; LLC has to issue retroactively.
4. **Treating a California LLC member who lives in California for part of the year as a resident**. Residency for California tax purposes is fact-specific; consult R&TC §17014 or use FTB Pub 1031.
5. **Treating an out-of-state corporate member as needing Form 3832**. Corporate members typically file California Form 100 or 100S; Form 3832 still useful but withholding mechanics differ. Verify on a case-by-case basis.

---

## Citation summary

- R&TC §18662(a)-(b) — withholding on payments to nonresidents
- R&TC §17014 — California residency for tax purposes
- R&TC §17935 — formation / registration
- R&TC §17942 — LLC fee
- R&TC §17941 — annual LLC tax
- R&TC §19132, §19521 — penalties and interest
- FTB Pub 1017 — Resident and Nonresident Withholding Guidelines
- FTB Pub 1031 — Guidelines for Determining Resident Status
- Form 3832 (2024): <https://www.ftb.ca.gov/forms/2024/2024-3832.pdf>
- Form 592-A (2024): <https://www.ftb.ca.gov/forms/2024/2024-592-a.pdf>
- Form 592-Q (2024): <https://www.ftb.ca.gov/forms/2024/2024-592-q.pdf>

For LLCs with foreign members, complex multi-state nonresident situations, or §1446 federal withholding interactions, redirect to a CPA. This skill produces the routine cases.
