# Rule Patterns

Use these patterns to design deterministic spreadsheet automation.

## Exact match

Use when both sides share a stable key.

Examples:

- invoice number;
- transaction id;
- payment reference;
- customer id;
- normalized email.

Rule:

```text
Match if normalized_key_A = normalized_key_B.
```

Verification:

- no key maps to more than one row unless many-to-one is expected;
- all matched rows preserve source row ids.

## Amount and date tolerance match

Use when bank and ledger descriptions differ but dates and amounts should line
up.

Rule:

```text
Match if abs(amount_A - amount_B) <= amount_tolerance
and abs(date_A - date_B) <= date_tolerance_days.
```

Recommended defaults:

- amount tolerance: exact or 0.01 unless the user confirms otherwise;
- date tolerance: 0-3 days depending on bank settlement timing.

Do not assume tolerance silently.

## Description normalization

Normalize only to improve matching; preserve original text.

Common transformations:

- trim whitespace;
- lowercase;
- remove repeated spaces;
- remove punctuation;
- strip bank prefixes such as `POS`, `ACH`, `CARD`, `PAYMENT`;
- map known vendor aliases from a user-approved lookup table.

Never overwrite the original description.

## Priority scoring

When no single exact key exists, use a scoring model and expose the score.

Example:

```text
+50 exact amount
+30 date within 1 day
+20 normalized vendor contains candidate vendor
+10 reference number overlap
```

Output should include:

- best candidate;
- score;
- reason codes;
- ambiguity warning when multiple candidates are close.

## One-to-one matching

Once a row is matched, remove it from the candidate pool unless the user allows
many-to-one matching. This prevents one bank transaction from matching multiple
ledger rows by accident.

## Exception report

Always produce exception outputs:

- unmatched in source A;
- unmatched in source B;
- duplicate keys;
- ambiguous candidate matches;
- amount/date outside tolerance;
- missing required fields.

## Audit log

For client workpapers, produce a log with:

- run timestamp;
- source file names;
- row counts;
- total amounts;
- match rules;
- matched count;
- unmatched count;
- exceptions count;
- code/script version if available.

