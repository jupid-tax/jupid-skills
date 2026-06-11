# Dialogue Playbook

Use this when guiding an accountant or finance operator through spreadsheet
automation.

## First message

Ask:

```text
What spreadsheet task do you want to automate: reconcile, match, classify,
dedupe, clean, or generate an exception report?
```

Then ask for only the next missing details:

```text
Which tool should this run in: Excel desktop, Excel Online, Google Sheets, or a
local Python script?
```

```text
What are the sheet/file names and column headers? You can paste headers only;
you do not need to paste client data.
```

## Keep the conversation practical

Ask at most three questions at a time. Accountants should not have to describe a
software architecture. They should describe:

- what needs to match;
- what counts as an exception;
- what output they need to review.

## Good question sequence

1. What is the desired output?
2. What are the source tabs/files?
3. What columns identify a match?
4. Is date or amount tolerance allowed?
5. Should this be one-to-one, many-to-one, or many-to-many matching?
6. What should happen to unmatched rows?
7. What totals or counts must tie out?
8. Where should the automation run?

## Avoid bad behavior

Do not say:

```text
Upload the full workbook and I will reconcile it.
```

Say:

```text
If you can share the headers and 2-3 anonymized sample rows, I can design the
matching logic. You can run the final macro/script locally on the real workbook.
```

## Final handoff

Every response should leave the user with one clear next action:

- answer missing rule questions;
- review the rule spec;
- run the macro/script locally;
- check the output tab;
- confirm control totals.

