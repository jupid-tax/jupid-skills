# Form 4797 — Common Mistakes

The audit-trip mistakes on Form 4797 — what filers and even some preparers get wrong, why it matters, and how to fix it.

---

## #1: Reporting a business asset sale on Form 8949 instead of Form 4797

**What happens:** Filer sells equipment used in their Schedule C business (or a rental property) and lists it on Form 8949 alongside personal stocks and crypto.

**Why it's wrong:** Form 8949 is for personal capital assets and investment property only. Business-use property goes on Form 4797. The character of the gain (and the recapture treatment) is completely different.

**Audit catch:** The IRS cross-references the filer's prior-year Form 4562 depreciation schedule. An asset that was depreciated for years and then disappears from the depreciation schedule but doesn't show up on Form 4797 raises a flag.

**Fix:** Move the disposition to Form 4797. Compute §1245 / §1250 recapture in Part III. Roll up correctly to Part I and Part II.

---

## #2: Forgetting "depreciation allowed or allowable"

**What happens:** Filer never claimed depreciation on a rental property or claimed less than the full amount, and assumes there's nothing to recapture.

**Why it's wrong:** IRC §1016(a)(2) requires the filer to reduce basis by depreciation "allowed or allowable" — meaning what they should have claimed under the applicable method, not what they actually claimed. The IRS computes recapture on the should-have-claimed amount.

**Audit catch:** Comparison of Form 4797 depreciation line vs. years-of-ownership × straight-line MACRS schedule. If they don't reconcile, the IRS proposes adjustment using "allowable".

**Fix:** File Form 3115 (Application for Change in Accounting Method) BEFORE filing Form 4797. This produces a §481(a) catch-up adjustment that recovers the lost deductions in the current year. Then file Form 4797 with the correct accumulated depreciation.

---

## #3: Skipping the §1231 5-year lookback

**What happens:** Current year has a §1231 gain. Filer reports it all as long-term capital gain on Schedule D. Doesn't check prior 5 years for unrecaptured §1231 losses.

**Why it's wrong:** IRC §1231(c) requires recharacterization of current-year §1231 gain as ordinary income up to the amount of non-recaptured net §1231 losses from the prior 5 years.

**Audit catch:** IRS data-analytics tools flag returns where prior-year Form 4797 Line 7 was negative and current-year Line 8 is zero.

**Fix:** Always pull the prior 5 years of Form 4797. Track each year's net §1231 result and how much has already been recharacterized in intervening years. Enter the unrecaptured balance on Line 8.

See [`references/1231-lookback.md`](./1231-lookback.md) for the full mechanics.

---

## #4: Treating cost-segregated rental components as pure §1250

**What happens:** Filer used cost segregation to accelerate depreciation on a rental property, reclassifying $400K of components into 5/7/15-year MACRS lives. At sale, treats the entire gain as §1250 with 25% cap.

**Why it's wrong:** Components reclassified to short MACRS lives become §1245 property (per IRC §1245(a)(3)(B)). At sale, those components recapture at full ordinary rates, not the 25% cap.

**Audit catch:** Comparison of prior-year Form 4562 (which lists the cost-segregated components by class life) against the current-year Form 4797. If §1245 property was on the depreciation schedule but doesn't show up in Part III §1245 recapture, the IRS proposes adjustment.

**Fix:** When selling a cost-segregated rental, allocate the sales price across asset classes. Apply §1245 recapture to the segregated components. Apply §1250 / unrecaptured §1250 gain treatment to the building shell.

---

## #5: Missing §179 / §280F recapture when business use drops

**What happens:** Filer took §179 on a $40K truck in year 1 (100% business). Business use drops to 40% in year 3. Filer reports nothing on Form 4797 because the truck wasn't sold.

**Why it's wrong:** IRC §179(d)(10) and §280F(b)(2) trigger recapture when business use drops to ≤50% before the recovery period ends, even without a sale.

**Audit catch:** Comparison of Form 4562 business-use percentages across years. A drop from 100% to 40% with no Part IV recapture on Form 4797 is a clear flag.

**Fix:** Complete Part IV. Compute recomputed MACRS depreciation through year of drop (Line 34). Recapture amount (Line 35) goes to Schedule C Line 6 as Other Income. Add the recaptured amount back to basis for future depreciation.

---

## #6: Forgetting unrecaptured §1250 gain when statutory recapture is $0

**What happens:** Filer sells a rental, sees Line 26g = $0 (because MACRS post-1986 is straight-line), and reports the entire gain as regular long-term capital gain at 0/15/20%.

**Why it's wrong:** Even when statutory §1250 recapture is $0, the depreciation portion of the gain is taxed as **unrecaptured §1250 gain** at a 25% federal cap (IRC §1(h)(1)(E)). The 25%-capped portion does NOT use the 0/15/20% LTCG rate.

**Audit catch:** Schedule D Line 19 (Unrecaptured §1250 Gain Worksheet result) being zero when prior-year Form 4562 shows depreciation on rental real estate.

**Fix:** Complete the Unrecaptured §1250 Gain Worksheet in the Schedule D instructions. Enter the depreciation portion of the §1231 gain on Schedule D Line 19. The Schedule D Tax Worksheet then applies the 25% cap correctly.

---

## #7: Land/building allocation drift between purchase and sale

**What happens:** Filer allocated 20% of purchase price to land at acquisition (so 80% was depreciable building). At sale, claims 50% allocation to land to reduce the recapture portion of the gain.

**Why it's wrong:** Allocation should be consistent and supported by reasonable evidence (county property tax assessor split, appraisal, etc.). Inconsistent allocation between purchase and sale is the kind of facts-and-circumstances issue that loses on audit.

**Audit catch:** Manual review during real estate audit; comparison of Form 4562 (which shows the depreciable base, implying the building % at purchase) against Form 4797 sales price allocation.

**Fix:** Use the same land/building ratio at sale as at purchase, unless there's documented evidence of a substantial relative-value shift (e.g., the building burned down and was rebuilt, or the land value dramatically appreciated relative to the building). Keep the documentation.

---

## #8: Incorrectly handling installment sales

**What happens:** Filer sells equipment for $100K with $20K down and $80K in seller financing over 4 years. Reports the full gain on Form 4797 in year 1.

**Why it's wrong:** Installment method (IRC §453) defers recognition of gain to the years payments are received — but **§1245 and §1250 recapture is recognized in full in the year of sale**, even if cash hasn't been received. Only the residual §1231 gain spreads over the installment period.

**Audit catch:** Form 6252 (Installment Sale Income) reconciliation against Form 4797.

**Fix:** Recognize ALL §1245 / §1250 / §1252 / §1254 / §1255 recapture in year 1 on Form 4797 Part II (via Part III Line 32). Spread only the residual §1231 gain across years using Form 6252. The §1231 portion that's deferred shows up on Form 4797 Line 3 in subsequent years.

---

## #9: Treating a like-kind exchange as a Form 4797 sale

**What happens:** Filer trades a rental property for another rental property in a §1031 like-kind exchange. Reports the disposition of the old property on Form 4797.

**Why it's wrong:** Pure §1031 like-kind exchanges (real property only post-TCJA) defer gain — they go on **Form 8824**, not Form 4797. Form 4797 only enters the picture if the exchange has "boot" (cash received, debt relief, or non-like-kind property received), in which case the boot portion is recognized.

**Audit catch:** Form 8824 mismatched against Form 4797 lines.

**Fix:** Use Form 8824 for like-kind exchange disclosure. If boot was received, the recognized gain (limited to boot) flows to Form 4797 Line 5 (or Line 16 for ordinary).

---

## #10: Misclassifying §197 goodwill recapture

**What happens:** Filer sells their service business including $50K of purchased goodwill. Treats the goodwill sale as pure long-term capital gain.

**Why it's wrong:** Purchased goodwill is a §197 amortizable intangible — and §197 intangibles are §1245 property. Amortization taken (15-year SL under §197) recaptures as ordinary at sale.

**Audit catch:** Form 4562 prior-year amortization on §197 intangibles + Form 8594 (asset acquisition allocation) reconciliation.

**Fix:** On Form 4797 Part III, list each §197 intangible with its amortization. Compute §1245 recapture on each. Self-created goodwill (not amortized) is a different story — it's pure §1231 with no recapture.

---

## #11 (Bonus): Forgetting that Form 4797 gains are NOT self-employment income

**What happens:** Filer sells equipment from their Schedule C business, computes the gain on Form 4797, then includes the gain in their Schedule SE self-employment tax computation.

**Why it's wrong:** IRS Reg. §1.1402(a)-6 specifically excludes Form 4797 gains from net earnings from self-employment. SE tax does NOT apply to gains on the sale of business property.

**Impact:** Overpays SE tax (15.3% on the gain).

**Fix:** Form 4797 gains flow to Schedule 1 / Form 1040 directly. Schedule SE is computed only from Schedule C net profit (Line 31), NOT from Form 4797 amounts.

---

## #12 (Bonus): Forgetting depreciation recapture on a former rental that became a personal residence

**What happens:** Filer rented out their property from 2010 to 2018, took depreciation, then moved back in as their primary residence from 2018 to 2025. Sells in 2025 and claims full §121 exclusion ($250K single / $500K MFJ).

**Why it's wrong:** Per IRC §121(d)(6), §121 exclusion does NOT shelter depreciation taken on the property after May 6, 1997. That depreciation portion is unrecaptured §1250 gain at 25%, recognized on Form 4797.

**Audit catch:** Manual audit review for personal-residence sales of formerly-rental properties. The IRS specifically asks about prior depreciation in audit interviews.

**Fix:** On Form 4797 Part III, report the depreciation portion of the gain as unrecaptured §1250 gain. The §121 exclusion still applies to the appreciation portion (above original basis) up to the dollar cap, but the depreciation portion is taxed at 25%.
