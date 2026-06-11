# Example Output

```markdown
## What We Are Building
Build deterministic logic to match bank transactions to ledger rows and produce
matched, unmatched, and ambiguous-match tabs.

## Questions I Need Answered
- Is the amount tolerance exactly $0.00 or should we allow $0.01 rounding?
- Should bank settlement dates match ledger dates within 0, 1, or 3 days?
- Is one bank transaction allowed to match multiple ledger rows?

## Rule Spec
Source A: `Bank` tab
Source B: `Ledger` tab
Primary keys: exact amount + normalized reference when available
Secondary keys: date within tolerance + normalized vendor text
Date tolerance: user to confirm
Amount tolerance: user to confirm
Normalization: lowercase, trim, remove punctuation, approved vendor alias table
Match priority: exact reference first, then amount/date/vendor score
Tie-breakers: mark as ambiguous when top two scores are within 10 points
Output tabs: `Matched`, `Unmatched Bank`, `Unmatched Ledger`, `Ambiguous`
Audit checks: row counts, total amounts, matched amount tie-out

## Recommended Engine
Use a local Python script because the matching requires candidate scoring,
one-to-one matching, and an audit log. Excel formulas would be harder to audit
and easier to break in a 40-tab workbook.

## Logic
[Provide the script or formulas here.]

## Verification
- Bank source row count equals matched + unmatched bank + ambiguous bank rows.
- Ledger source row count equals matched + unmatched ledger + ambiguous ledger rows.
- Matched bank amount total equals matched ledger amount total within tolerance.
- Duplicate candidate matches are flagged, not silently accepted.

## How to Run Locally
1. Save a copy of the workbook.
2. Run the script against the copied workbook.
3. Review the exception tabs first.
4. Check the audit log totals.
5. Only then use the matched output in the workpaper.
```

