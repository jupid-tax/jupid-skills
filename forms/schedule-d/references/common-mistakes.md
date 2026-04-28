# Common Mistakes — Schedule D

The 10 mistakes filers make most often on Schedule D, ordered roughly by frequency. Each entry follows: **Problem / Impact / Solution / Citation**.

---

## 1. Using the regular tax tables instead of the Qualified Dividends and Capital Gain Tax Worksheet

**Problem:** Filer has long-term capital gain on Schedule D Line 16 but computes Form 1040 Line 16 (tax) directly from the tax tables, treating the entire taxable income as ordinary.

**Impact:** Overpayment of the LTCG-bracket-spread × gain. A $30,000 long-term gain in the 24% ordinary bracket vs the 15% LTCG bracket = $2,700 overpayment.

**Solution:** Whenever Schedule D Line 15 is positive AND Line 16 is positive AND Lines 18, 19 are zero, use the **Qualified Dividends and Capital Gain Tax Worksheet** in the Form 1040 instructions. Tax software handles this automatically; paper filers must run the worksheet manually.

**Citation:** IRC §1(h); Schedule D Line 20 Yes branch; Form 1040 instructions Qualified Dividends and Capital Gain Tax Worksheet.

---

## 2. Missing prior-year capital loss carryover

**Problem:** Filer had a net loss in 2024 that exceeded the $3,000 limit. The unused portion carries forward indefinitely. In 2025, the filer forgets to enter the carryover on Schedule D Line 6 (short-term portion) or Line 14 (long-term portion).

**Impact:** Pays tax on gains that the carryover should have offset. The carryover doesn't lapse, but if it's never claimed, the deduction is permanently lost (absent a 1040-X amendment within 3 years).

**Solution:** Save the prior-year **Capital Loss Carryover Worksheet** every year. If using tax software, the same software year-over-year typically tracks this; if changing software, transcribe the carryover into the new system manually.

**Citation:** IRC §1212(b); Schedule D Lines 6, 14; Capital Loss Carryover Worksheet in Schedule D instructions.

---

## 3. Forgetting to compute NIIT on Form 8960

**Problem:** Single filer with MAGI $250,000 and $40,000 long-term gain pays the 15% LTCG rate and stops there. Misses the 3.8% NIIT on the net investment income above the $200,000 threshold.

**Impact:** Roughly $1,520 underpayment ($40,000 × 3.8%, capped at MAGI excess if smaller). Eventual IRS notice with interest and possibly underpayment penalty.

**Solution:** If MAGI exceeds $200K single / $250K MFJ / $125K MFS, complete Form 8960 alongside Schedule D. The NIIT routes to Schedule 2 → Form 1040 Line 23.

**Citation:** IRC §1411; Form 8960; see [`niit.md`](./niit.md).

---

## 4. Misclassifying a §1231 business property sale

**Problem:** Filer sells a piece of business equipment from their Schedule C operation, classifies it as long-term capital gain, and reports on Form 8949. Actually, business-use property goes on **Form 4797** first; only the net §1231 gain (after recapture as ordinary income) is converted to long-term capital gain and routed to Schedule D Line 11.

**Impact:** Wrong characterization. Depreciation recapture income gets the 0/15/20% capital rate instead of the higher ordinary rate it should have received. The IRS catches this via the Form 4797 / Schedule D crosswalk and issues an underpayment notice.

**Solution:** If the asset was used in a trade or business (Schedule C, rental real estate, farm), it's Form 4797 territory. Investment property held passively (e.g., raw land, REIT shares) is Form 8949 / Schedule D directly.

**Citation:** IRC §1231; Form 4797 instructions; Schedule D Line 11.

---

## 5. Using Qualified Dividends and Capital Gain Tax Worksheet when Schedule D Tax Worksheet is required

**Problem:** Real estate sale with depreciation recapture creates Line 19 (unrecaptured §1250 gain) > 0, but filer uses the simpler Qualified Dividends and Capital Gain Tax Worksheet anyway.

**Impact:** Tax computed at the 15% LTCG rate on the §1250 portion instead of the maximum 25%. Underpayment of (25% − 15%) × Line 19 amount. Schedule D Tax Worksheet has a 25% bucket; the simpler worksheet does not.

**Solution:** Whenever Schedule D Line 18 or Line 19 is greater than zero, use the **Schedule D Tax Worksheet** in the Schedule D instructions (not the Form 1040 instructions worksheet).

**Citation:** Schedule D Line 20; Schedule D Tax Worksheet in i1040sd.pdf.

---

## 6. Missing the §1202 QSBS exclusion

**Problem:** Founder sells C-corp stock held 6+ years that meets the §1202 small-business asset test. Reports the full gain at 20% LTCG + 3.8% NIIT on Schedule D.

**Impact:** Pays $238,000 federal tax on a $1M gain that could have been entirely excluded (subject to the per-issuer cap of $10M or 10× basis).

**Solution:** Before selling stock in a privately-held C-corp, verify QSBS qualification with a tax advisor:
- Stock acquired at original issuance (not from a secondary buyer)
- Issuer was a domestic C-corp with under $50M aggregate gross assets at issuance
- Issuer engaged in qualified active business
- Held more than 5 years

If qualified, report on Form 8949 with code Q (partial) or X (100%); the excluded portion goes in column (g).

**Citation:** IRC §1202; see [`special-rates.md`](./special-rates.md).

---

## 7. Mismatched Form 8949 box totals on Schedule D

**Problem:** Filer enters Form 8949 detail correctly but transcribes wrong totals to Schedule D Lines 1b, 2, 3, 8b, 9, 10. Often a typo or skipped page.

**Impact:** IRS computer reconciles Schedule D Line 1b column (d) against the broker's transmitted 1099-B Box 1d totals. Mismatch → CP2000 notice or rejected e-file.

**Solution:** Run the math check from `SKILL.md` Validation: each Schedule D line equals the sum of the corresponding Form 8949 page totals. Tax software automates this.

**Citation:** Schedule D instructions; IRC §6045(g) (broker reporting).

---

## 8. Wash sale on Form 8949 not adjusting basis on replacement lot

**Problem:** Filer takes a loss, rebuys within 30 days, codes the wash sale correctly on Form 8949 (code W, disallowed loss in column (g)). But forgets to adjust the basis of the replacement lot in their records. A year later, sells the replacement lot using the original purchase price as basis.

**Impact:** Loss claimed twice — once disallowed via wash, once via lower-basis replacement. Audit risk, plus understatement of gain in the year the replacement sells.

**Solution:** When the wash sale is recorded, immediately add the disallowed loss to the basis of the replacement lot in the user's records. Brokers track this within a single account but not across accounts. Cross-account washes are entirely on the user.

**Citation:** IRC §1091; Pub 550 wash sale chapter; see [`forms/form-8949/references/wash-sales.md`](../form-8949/references/wash-sales.md).

---

## 9. Reporting a loss carryover with the wrong character

**Problem:** Filer's prior year had a $20,000 short-term loss that was fully unused (no gains, no $3,000 deduction). Carries forward to current year on Schedule D Line 14 (long-term) instead of Line 6 (short-term).

**Impact:** Subtle but wrong — the carryover, if allocated to long-term, first absorbs current-year long-term gains. Allocated to short-term, it would first absorb short-term gains (which are taxed at higher rates). The error favors the user in some scenarios and the IRS in others, but in either case the form is incorrect.

**Solution:** Character is preserved in carryover under IRC §1212(b). Short-term loss → next year's Schedule D Line 6. Long-term loss → Line 14. The Capital Loss Carryover Worksheet from the prior year specifies which is which.

**Citation:** IRC §1212(b); Capital Loss Carryover Worksheet in Schedule D instructions.

---

## 10. State capital loss carryover ignored

**Problem:** Filer correctly tracks federal capital loss carryover but forgets that state rules differ. Files state return assuming federal carryover transfers automatically.

**Impact:** Varies by state:
- **California** — generally conforms to federal $3,000 limit but uses CA-specific AGI definitions; carryover is allowed but tracked separately
- **New Jersey** — does **not** allow capital loss carryover at all; the loss is permanently lost in the year incurred
- **Other states** — vary widely

**Solution:** When preparing the state return, do not assume federal Schedule D figures transfer cleanly. Each state has its own capital gain schedule. For NJ filers, this means a $20,000 federal carryover has zero state value.

**Citation:** State-specific tax codes; see California FTB Pub 1001 for CA; NJ Division of Taxation rules.

---

## How these mistakes cluster

The most expensive single-error cluster is **#1 + #5** combined: not running any worksheet (just using the tax tables) when one of the preferential-rate worksheets applies. A $50,000 long-term gain at 24% vs 15% = $4,500 overpayment that the IRS will not refund without an amendment.

The most expensive multi-year cluster is **#2 + #9** combined: losing track of carryovers across years. Once the prior-year worksheet is misplaced, the carryover often disappears permanently. For a filer with $50,000 unused loss, that's $7,500–$15,000 of foregone deductions over the next several years.

The most audit-exposed cluster is **#3 + #4 + #5**: filers with NIIT exposure, business property sales, and depreciation recapture all in the same return often understate their tax by missing one of the rate adjustments. The IRS catches at least one of the three through automated crosswalks; a notice is highly likely.

---

## Sources

- [Schedule D Instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf)
- [Form 1040 Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf)
- [Form 8960](https://www.irs.gov/pub/irs-pdf/f8960.pdf) and instructions
- [Form 4797](https://www.irs.gov/pub/irs-pdf/f4797.pdf) and instructions
- [Publication 550](https://www.irs.gov/publications/p550)
- IRC §1(h), §1202, §1211, §1212, §1231, §1250, §1411
