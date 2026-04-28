# §1231 5-Year Lookback Rule

The §1231 5-year lookback (IRC §1231(c)) is the most-missed rule on Form 4797. It exists to prevent taxpayers from gaming the system by alternating ordinary §1231 losses (deducted at full ordinary rates) with §1231 gains (taxed at preferential LTCG rates) across years.

The rule: a current-year net §1231 gain is **recharacterized as ordinary income** to the extent of any non-recaptured net §1231 losses from the prior 5 tax years.

---

## How the lookback works

For each tax year, you have a net §1231 result on Form 4797 Part I Line 7:
- If positive (gain): potentially LTCG
- If negative (loss): ordinary loss

The lookback maintains a "balance" of unrecaptured prior losses:

```
Year   | Line 7 result   | Lookback impact
-------|-----------------|---------------------------
TY-5   | ($20,000) loss  | Adds $20,000 to lookback bucket
TY-4   | $5,000 gain     | First $5,000 is ordinary; bucket → $15,000
TY-3   | $0              | Bucket → $15,000
TY-2   | ($10,000) loss  | Bucket → $25,000 (new loss added)
TY-1   | $30,000 gain    | First $25,000 is ordinary; bucket → $0
TY     | $40,000 gain    | All $40,000 is LTCG (bucket empty)
```

The bucket carries forward 5 years per loss. After 5 years, an unrecaptured §1231 loss is no longer subject to lookback.

---

## Where it appears on Form 4797

**Line 8** — Enter the non-recaptured net §1231 loss from prior 5 years.

**Line 9** — Net §1231 gain after lookback = Line 7 − Line 8 (if Line 7 ≥ Line 8 and both positive). Goes to Schedule D Line 11 as LTCG.

**Part II Line 12** — The recharacterized portion (= min(Line 7, Line 8)) goes here as ordinary.

---

## Worked example

**Setup.** Janet, sole prop with various business equipment dispositions:

| Tax Year | Form 4797 Line 7 | Treatment |
|----------|------------------|-----------|
| 2021 | ($15,000) loss | Ordinary loss; adds to lookback bucket → $15K |
| 2022 | $0 | Bucket → $15K |
| 2023 | $5,000 gain | First $5K ordinary (Line 12); bucket → $10K |
| 2024 | ($8,000) loss | Ordinary loss; bucket → $18K |
| 2025 | $25,000 gain | ??? |

**2025 lookback computation:**

Look at the 5 prior years (2020-2024):
- 2021 loss: $15,000 original; recaptured $5,000 in 2023 → $10,000 unrecaptured
- 2024 loss: $8,000 original; not yet recaptured → $8,000 unrecaptured
- Total non-recaptured §1231 losses in 5-year window: **$18,000**

But wait — the 2021 loss is now **outside the 5-year window** as of 2026 (only 2021-2025 are within 5 years of 2025; the 5-year window for 2025 is 2020-2024 inclusive). So 2021's $10K unrecaptured loss IS still in the 5-year lookback for 2025. For 2026 returns, the 2021 loss falls off.

**2025 entries:**

```
Line 7 (current year net §1231 gain):     $25,000
Line 8 (5-year non-recaptured §1231 loss): $18,000
Line 9 (LTCG to Schedule D Line 11):       $7,000   ← $25,000 − $18,000

Part II Line 12 (recharacterized ordinary): $18,000
```

The $18,000 is taxed at ordinary rates; the $7,000 excess is taxed at LTCG rates.

---

## Tracking the lookback across years

The IRS does NOT compute the lookback for you. You must track:

1. Net §1231 result per year (Form 4797 Line 7)
2. Of any year's loss, how much has already been recharacterized as ordinary in subsequent years
3. The 5-year window — losses age out

A simple tracking spreadsheet:

```
Year | Line 7 | Initial loss for lookback | Recaptured | Remaining | Year falls off
2020 | $X     | $X (if loss)              | $Y         | $X−$Y     | After 2025
2021 | ...    | ...                       | ...        | ...       | After 2026
...
```

When you have a §1231 gain year, you "use up" the oldest unrecaptured loss first.

---

## Common lookback mistakes

### Mistake #1: Filer doesn't pull prior 5 years

The filer just files the current year and ignores history. Net result: §1231 gain reported as 100% LTCG when some portion should be ordinary.

**IRS catches this** by cross-referencing prior-year Form 4797 Line 7 amounts against current-year Line 8. If prior losses exist and current Line 8 is $0, expect a notice.

**Fix:** Always pull the prior 5 years of Form 4797 (or have the user provide prior tax returns). Document the lookback computation in the workpapers.

### Mistake #2: Filer counts a §1231 loss that's already been recaptured

If the user has a §1231 loss in 2021 ($20,000) and a §1231 gain in 2023 ($15,000) that was already partially recaptured ($15,000 of the 2021 loss recharacterized as ordinary in 2023), the remaining unrecaptured loss is $5,000, not $20,000.

**Fix:** Track the recapture history per loss.

### Mistake #3: Filer applies lookback when current Line 7 is a loss

The lookback only applies to current-year §1231 GAINS (Line 7 positive). If Line 7 is a loss, skip Lines 8 and 9 and route the loss to Part II Line 11.

### Mistake #4: Filer uses the wrong 5-year window

The 5-year window is "prior 5 tax years" — for a 2025 return, the window is 2020, 2021, 2022, 2023, 2024 (NOT including 2025 itself, NOT including 2019).

### Mistake #5: Filer applies lookback per asset instead of per year

The lookback works on the year-level NET §1231 result, not per-asset. If 2024 had a $5K gain on one asset and a $10K loss on another, the net is ($5K) loss — that's what enters the lookback bucket.

---

## Lookback and entity types

- **Sole proprietors**: lookback is per individual
- **Partners and S-corp shareholders**: §1231 gains/losses pass through on K-1; lookback is computed at the individual level using the individual's accumulated K-1 §1231 history plus any Form 4797 §1231 amounts at the individual level
- **C-corps**: same lookback rule, but applied at the corporate level

---

## Audit risk

The §1231 lookback is one of the items the IRS specifically reconciles via the "data analytics" function — comparing current-year Line 8 against prior-year Line 7 amounts. A current-year Line 8 of $0 with prior-year ordinary §1231 losses on file is a flag.

The fix is procedural: ALWAYS pull prior 5 years before declaring the lookback complete. This is what audit-grade looks like — the workpapers show the prior-year results, the recapture history, the computation, and the result.
