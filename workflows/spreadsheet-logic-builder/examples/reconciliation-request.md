# Reconciliation Request

Paste this into Codex or Claude Code:

```text
Use this skill from GitHub:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/spreadsheet-logic-builder

I need to build deterministic spreadsheet logic for a reconciliation.

Tool target:
[Excel desktop / Excel Online / Google Sheets / local Python]

Source A:
[sheet/file name and column headers]

Source B:
[sheet/file name and column headers]

Matching rules:
[exact keys, amount tolerance, date tolerance, description/vendor rules]

Desired output:
[matched rows / unmatched rows / exception report / cleaned export]

Privacy constraint:
[work from headers and fake examples only / can inspect local workbook / can use anonymized sample rows]

Verification:
[totals that must tie, known examples, row counts, exception checks]

Please ask any missing questions first, then produce:
1. a rule spec;
2. the recommended engine;
3. the formulas/macro/script;
4. verification checks;
5. local run instructions.
```

