# Example — Foreign Real Estate Investor (FIRPTA Withholding)

## Facts

- **Applicant (W-7 subject)**: Lin Wei, Chinese citizen and resident; never lived in the US; non-resident alien for US tax purposes
- **Transaction**: Lin is buying a $1.4 million single-family rental investment property in Miami, FL. Closing scheduled for May 2026.
- **Why an ITIN is needed**:
  - As a foreign buyer, Lin will rent out the property and earn US-source rental income subject to either §871(d) net election (taxed as ECI on Form 1040-NR) or §871(a) gross 30% withholding via Form 1042-S. Either way, Lin needs an ITIN to file 1040-NR or have Form 1042-S issued.
  - More urgent: Lin plans to **resell** the property in 3-5 years. When she does, FIRPTA (IRC §1445) requires the buyer to withhold 15% of the gross sale price on a sale by a foreign person. To **reduce or eliminate** that withholding (because the actual capital gain tax owed will be far less than 15% of gross), Lin can file **Form 8288-B (Application for Withholding Certificate)** at the time of resale — but Form 8288-B requires an ITIN.
  - Lin's CPA recommends getting the ITIN now (during purchase) so that all rental-period reporting (Form 1042-S, 1040-NR) flows through smoothly and so that when resale time comes, Lin can move quickly on the 8288-B without a 7-11 week ITIN delay.
- **Identification documents Lin has**:
  - Chinese passport, valid through 2030
  - Chinese national ID card
  - Chinese household registration ("hukou")
- **No US tax filing yet** — this is Lin's first interaction with the US tax system
- **Lin will not be in the US** during the W-7 application; she's in Shanghai

## Analysis

### Step 1 — SSN ineligibility

Lin is a non-resident alien with no US visa, no US work authorization, and no plans to immigrate. She is not SSN-eligible. ITIN is the appropriate TIN.

### Step 2 — Reason code

This is the key decision for Lin's situation. Several reason codes could apply:

- **(a)** Nonresident alien required to file US tax return — applies if Lin is filing 1040-NR for rental income
- **(h)** Other (specify) — appropriate when applying under an Exception (no current tax return required)

For the **purchase** stage (now), Lin doesn't yet have a 1040-NR to file (no rental income yet). She's applying for the ITIN proactively. This places her under **Exception 3** (mortgage interest reporting under §6045 — if she's financing the purchase with a US mortgage and the lender will issue Form 1098 in her name) OR **Exception 4** (FIRPTA — if she expects withholding events).

If Lin is **paying cash** (no mortgage), Exception 3 doesn't apply. Exception 4 (FIRPTA) is more apt, but technically applies to *sellers* facing §1445 withholding, not buyers.

**Most clean approach**: wait until rental income starts (Lin's first rent check after closing), then file W-7 under reason **(a)** with the first 1040-NR she files.

**Alternative**: if Lin has a US mortgage, file W-7 now under **Exception 3** (mortgage interest §6045 reporting), reason code **(h)** — Other.

For this example: assume Lin is taking a US mortgage to finance the property. Use **Exception 3**, reason code **(h)**.

### Step 3 — Identification documents

Lin's Chinese passport is the cleanest single-document option. It proves both identity and foreign status. No second document needed.

**Submission options**:
1. Mail original passport from China to IRS Austin — risky (3+ months without passport, international mail risk)
2. Mail certified copy from issuing authority — Lin can request a certified copy from the Chinese passport authority or from the Chinese consulate in the US (not directly available to her in Shanghai; may need to use a designated agent)
3. **Use a Certifying Acceptance Agent (CAA)** — many CAAs in the US work with overseas clients via courier. Lin couriers her passport to the CAA, the CAA certifies in person (or accepts notarized scans for some setups; verify CAA's process), and returns the passport.
4. **CAA in China**: there are IRS-approved CAAs operating in major Chinese cities (Hong Kong, Shanghai, Beijing). The IRS Acceptance Agent search tool lists them: https://www.irs.gov/tin/itin/acceptance-agent-program
5. In-person TAC: not feasible — Lin would have to fly to a US TAC

For this example: **Lin uses a CAA in Shanghai**. Cost ~$300-500 (international CAA fees are higher).

### Step 4 — Exception application — no tax return attached

Under Exception 3, Lin's W-7 is **not** attached to a 1040-NR. She files the W-7 alone with supporting evidence:

- **Letter from US lender** (e.g., the bank financing the Miami property purchase) on official letterhead, stating:
  - Lin is the borrower
  - Property address (Miami, FL)
  - Lender will issue Form 1098 for mortgage interest in Lin's name
  - An ITIN is required for §6045 reporting
- Mortgage commitment letter or settlement statement showing Lin as borrower
- Property address and description

### Step 5 — Fill the W-7

Key fields:

- Top of form: check **box (h) — Other**, write "Exception 3: Mortgage interest reporting under §6045"
- Renewal box: **No** (first-time)
- Line 1a: LIN WEI (passport rendering, or "Wei Lin" with surname-first noted on Chinese passport)
- Line 2 (mailing address): the CAA's process determines — typically Lin's address in Shanghai (the IRS will mail the CP-565 internationally)
  - Note: CAA's address is NOT acceptable; must be Lin's actual address
- Line 3: same Shanghai address (no separate foreign address needed)
- Line 4: DOB, place of birth (Shanghai, China)
- Line 5: Female
- Line 6a: China (citizenship)
- Line 6b: Lin's Chinese tax ID (Citizen ID Number) if she has one
- Line 6c: U.S. visa — none (leave blank or "N/A")
- Line 6d: Chinese passport, China, number, expiration 2030
- Line 6e: Date of entry to US — Lin has never been to US (or the date of her first short visit if applicable). This line is for nonresident aliens entering the US; if Lin has never entered, write "N/A" or leave blank with a notation
- Line 6f: Other info — note "First-time ITIN application; non-resident alien purchasing US real estate; Exception 3 — mortgage interest reporting"
- Sign and date

### Step 6 — Supporting evidence

Attach to the W-7:

- Lender letter (per Step 4 above)
- Mortgage commitment letter or HUD-1 / Closing Disclosure
- Property purchase contract showing Lin as buyer

### Step 7 — Submit

Mail to the **ITIN Operation Center**:

```
Internal Revenue Service
ITIN Operation
P.O. Box 149342
Austin, TX 78714-9342
```

For courier (FedEx, UPS, DHL — verify the courier address, different from PO Box):
```
Internal Revenue Service
ITIN Operation
Mail Stop 6090-AUSC
3651 S. Interregional Hwy 35
Austin, TX 78741-0000
```
(Verify against current Pub 1915.)

CAA process: the CAA in Shanghai prepares the package, certifies the passport copy, and sends it via international courier to Austin. CAA also files Form W-7 COA (Certificate of Accuracy). Lin keeps her original passport in Shanghai.

### Step 8 — Wait

Processing: 7-11 weeks. Off-peak (mid-summer): closer to 7. Peak (Jan-April): closer to 11.

Lin should expect the CP-565 by August 2026 if filed in May 2026.

### Step 9 — After ITIN is issued

Lin can now:
- Receive Form 1098 from the US lender with her ITIN
- File Form 1040-NR for the year of the property purchase (and each subsequent year of rental income)
- Make the §871(d) election to treat rental income as ECI (effectively connected income), allowing deduction of mortgage interest, depreciation, property tax, etc.
- When resale time comes (3-5 years), file Form 8288-B to apply for a withholding certificate that reduces FIRPTA withholding from 15% of sale price to a smaller amount tied to actual gain

### Step 10 — When Lin sells the property (future)

This is when the ITIN becomes critical:

- Buyer of the property must withhold 15% of gross sale price under §1445 unless reduced by IRS withholding certificate
- Lin (or her CPA) files Form 8288-B with the IRS BEFORE closing, requesting a reduced withholding amount
- Form 8288-B requires Lin's ITIN
- IRS issues a withholding certificate within ~90 days, allowing buyer to withhold a smaller amount (tied to actual capital gains tax estimated)
- Lin then files 1040-NR for the year of sale, claiming credit for the withheld amount, paying any balance or receiving refund

Without an ITIN obtained in advance, Lin would face full 15% gross withholding ($210,000 on a $1.4M sale), and waiting for ITIN + 8288-B during a closing is a recipe for delay.

## Validation checks

- [x] Reason code (h) "Other — Exception 3 mortgage interest" checked
- [x] Mailing address is Lin's Shanghai address (not CAA's office)
- [x] Passport submitted via CAA-certified copy (originals stay with Lin)
- [x] Lender letter attached on official letterhead
- [x] Property documentation (mortgage commitment, purchase contract) attached
- [x] No 1040-NR attached (Exception 3 path — no tax return required at this stage)
- [x] Mailed to ITIN Operation Austin

## Lessons

1. **Get the ITIN before you need it**: applying during property purchase rather than waiting for resale avoids 7-11 weeks of delay during a time-pressured closing.
2. **FIRPTA 15% gross withholding** can be reduced via Form 8288-B — but only if you have an ITIN. The ITIN is the gating prerequisite for foreign real estate investors.
3. **Reason code (h) + Exception 3** is the right path for foreign buyers with US mortgages. Without a mortgage (cash purchase), the cleanest path is to wait until rental income starts and file W-7 with the first 1040-NR (reason code (a)).
4. **CAA in the foreign country** is the most operationally efficient option — Lin doesn't have to mail her passport internationally.
5. **§871(d) election**: foreign rental property income can be treated as ECI (effectively connected income), enabling deductions. Without the election, gross income is subject to 30% withholding with no deductions. The election is made on the first 1040-NR.
6. **Different ITIN mailing address** vs. regular 1040 address — always send W-7 packets to the Austin ITIN Operation.

## Citations

- IRC §1445 — FIRPTA withholding on sale of US real estate by foreign person
- IRC §871(d) — election to treat real property income as ECI
- IRC §6045 — information returns (mortgage interest reporting on Form 1098)
- IRC §6109 — TIN requirements
- Form 8288-B — Application for Withholding Certificate for Dispositions by Foreign Persons of US Real Property Interests
- Pub. 519 — US Tax Guide for Aliens
- Pub. 1915 — Understanding Your IRS ITIN
- Form W-7 instructions, Exception 3 — mortgage interest reporting
- Form W-7 instructions, Exception 4 — §1445 FIRPTA
- IRS Acceptance Agent Program — international CAA list
