---
name: spreadsheet-logic-builder
description: >
  Use this skill when an accountant, bookkeeper, tax professional, CFO, or
  finance operator needs an agent to design deterministic spreadsheet logic,
  reconciliation rules, Excel formulas, VBA macros, Google Sheets formulas, or
  Python scripts for local spreadsheet work. Triggers on phrases like
  "reconcile this spreadsheet", "build matching logic", "write a macro",
  "create a VBA script", "create spreadsheet automation", "match transactions",
  "clean this ledger", "dedupe rows", "compare two tabs", "40-tab workbook",
  "do not upload client data", or "make AI generate the code, not the answer".
  Do NOT use this skill to guess spreadsheet results directly from raw client
  data; use it to build auditable logic that runs locally.
workflow: Spreadsheet logic builder
audience: [accounting, bookkeeping, tax, finance, cfo, spreadsheet]
last_verified: 2026-06-11
---

# Spreadsheet Logic Builder

This skill turns an agent into a deterministic spreadsheet automation designer
for accountants and finance teams. The agent's job is not to "look at a big
spreadsheet and guess the answer." The job is to help the user define the rules
and produce logic that can run locally: formulas, VBA, Office Scripts, Google
Sheets formulas, SQL, or Python.

Use this for reconciliation, matching, classification, deduplication, exception
reports, workbook cleanup, and repeatable spreadsheet operations.

---

## Use from GitHub

Canonical public link:

```text
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/spreadsheet-logic-builder
```

When a user gives this GitHub link and asks to use or install the skill, first
determine the current runtime:

- If you are running in Codex, treat this as a Codex skill.
- If you are running in Claude Code, treat this as a Claude Code skill.
- If the runtime is unclear, ask one short question: "Are you using Codex or
  Claude Code?"

Do not make the user choose a different GitHub link. The same repository folder
is the source for both runtimes.

For one-off use without installation, read this `SKILL.md`, then load the
reference files only when needed for the user's task.

For repeated local use:

```bash
# Codex
mkdir -p ~/.codex/skills
cp -r workflows/spreadsheet-logic-builder ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -r workflows/spreadsheet-logic-builder ~/.claude/skills/
```

---

## Core rule

Ask for the engine, not the answer.

The agent should not claim it has reconciled a workbook unless the logic has
actually been executed and verified. In normal use, produce:

1. a clear rule spec;
2. deterministic spreadsheet logic;
3. a test plan;
4. expected output columns/tabs;
5. instructions for running locally;
6. verification checks.

Client PII and raw ledgers should remain local whenever possible. If the user
does not need the agent to inspect raw data, ask for column names, sample
headers, and rule descriptions instead of the full dataset.

---

## When to invoke

Engage this skill when the user asks for:

- bank reconciliation logic;
- matching transactions across tabs or files;
- deduplication rules;
- vendor/customer normalization;
- exception reports;
- classification rules;
- multi-tab workbook checks;
- Excel formulas, VBA macros, Office Scripts, Google Sheets formulas, SQL, or
  Python scripts for spreadsheet work;
- a privacy-preserving way to use AI with client spreadsheets.

Do not engage this skill when:

- the user wants a one-off visual chart or formatting edit with no logic;
- the user wants a final tax/legal conclusion;
- the user asks the model to infer missing accounting facts without evidence;
- the task requires direct filing or submission rather than spreadsheet logic.

---

## Required inputs

Before writing code or formulas, collect:

1. Tool target: Excel desktop, Excel Online, Google Sheets, CSV workflow, or
   Python local script.
2. Source structure:
   - sheet/file names;
   - column headers;
   - approximate row counts;
   - key fields such as date, amount, description, invoice number, customer,
     vendor, account, memo, reference id.
3. Desired output:
   - matched rows;
   - unmatched rows;
   - exceptions;
   - duplicate candidates;
   - clean export;
   - audit log.
4. Matching or transformation rules:
   - exact match fields;
   - fuzzy match fields;
   - date tolerance;
   - amount tolerance;
   - one-to-one vs one-to-many;
   - tie-breaking;
   - ignore rules;
   - priority order.
5. Data privacy constraint:
   - can the agent inspect the workbook, or should it work from schema/sample
     rows only?
6. Verification standard:
   - totals that must tie;
   - control counts;
   - known matched examples;
   - known exceptions.

If any of these materially affect the logic, ask before producing code.

For the guided dialogue, load
[`references/dialogue-playbook.md`](./references/dialogue-playbook.md).

---

## Workflow

Execute these steps in order.

### Step 1 - Define the job

State the spreadsheet task in one sentence:

```text
Build deterministic logic to [match/classify/reconcile/dedupe] [source A] to
[source B] and produce [output].
```

If the user describes a vague problem, ask for the target output first.

### Step 2 - Inventory the workbook or schema

If the workbook can be inspected locally, identify sheet names, headers, and
sample row shapes. If not, ask the user to paste:

```text
Sheet/File name:
Columns:
Example row with fake/anonymized values:
Known correct match/example:
```

Do not require PII when fake examples are enough.

### Step 3 - Build the rule spec

Create a rule spec using this format:

```markdown
## Rule Spec
Source A:
Source B:
Primary keys:
Secondary keys:
Date tolerance:
Amount tolerance:
Normalization:
Match priority:
Tie-breakers:
Output tabs/files:
Audit checks:
Open questions:
```

If repository files are available, the user can generate a starter spec with:

```bash
python3 workflows/spreadsheet-logic-builder/scripts/create-rule-spec.py
```

### Step 4 - Choose the execution engine

Pick the simplest reliable engine:

- Excel formulas: best for transparent small/medium workbook logic.
- Power Query: best for repeatable imports, merges, and transformations.
- VBA macro: best for Excel desktop users who want one-click automation.
- Office Script: best for Excel Online / Microsoft 365 automation.
- Google Sheets formulas / Apps Script: best for Google Sheets users.
- Python script: best for large CSV/XLSX files, complex matching, fuzzy logic,
  or audit logs.

Explain the tradeoff briefly and choose one. Do not produce every possible
implementation unless the user asks.

### Step 5 - Write deterministic logic

The code or formulas must:

- avoid hidden assumptions;
- normalize dates, amounts, whitespace, casing, punctuation, and common vendor
  name variants when relevant;
- create explicit match status values;
- produce exception outputs;
- log assumptions and unmatched records;
- preserve original source data;
- avoid destructive edits unless the user explicitly asks.

For matching and reconciliation patterns, load
[`references/rule-patterns.md`](./references/rule-patterns.md).

### Step 6 - Add verification

Every automation should include checks:

- source row counts;
- output row counts;
- matched/unmatched counts;
- total amount tie-out;
- duplicate match warnings;
- changed rows count;
- known example tests.

For larger tasks, produce a test matrix before code.

### Step 7 - Give run instructions

End with clear run instructions:

```markdown
## How to run
1. Save a copy of the workbook.
2. Run [macro/script/formula].
3. Review [output tab/file].
4. Check [control totals].
5. Only then use the result in client workpapers.
```

---

## Output format

Use this structure:

```markdown
## What We Are Building
[One-sentence job.]

## Questions I Need Answered
- [Only if needed.]

## Rule Spec
[Structured rules.]

## Recommended Engine
[Excel formula / VBA / Python / etc., with reason.]

## Logic
[Formulas, macro, script, or pseudocode.]

## Verification
- [Checks.]

## How to Run Locally
- [Steps.]
```

If the user is non-technical, keep code separate from the explanation and make
the run steps simple.

---

## Privacy rules

- Prefer schema, fake examples, and anonymized sample rows over raw client data.
- Do not ask for SSNs, EINs, bank account numbers, full customer ledgers, or
  payroll data unless absolutely necessary.
- If raw files are local and the agent can operate locally, keep outputs local.
- If the user is using a public hosted model or chat app, recommend not uploading
  client PII.
- Say clearly when a workflow is privacy-preserving because the code runs
  locally, not because the AI computed the result.

---

## Examples

- [`examples/reconciliation-request.md`](./examples/reconciliation-request.md)
  - copy-paste request for bank/ledger matching.
- [`examples/example-output.md`](./examples/example-output.md)
  - compact example of a rule spec and output.

