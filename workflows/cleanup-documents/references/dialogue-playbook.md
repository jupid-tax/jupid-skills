# Dialogue Playbook

Use this when guiding a business owner or accountant through a document
cleanup. The user is often non-technical: they have a folder full of PDFs,
scans, and photos, and they want it fixed.

Ground rules:

- **Speak the user's language** — all messages below are templates; translate
  them (including folder names in proposals) into whatever language the user
  writes in.
- **Every gate is a menu**: 2–4 numbered options, one marked (recommended).
  In Claude Code use the native question dialog when available; otherwise a
  numbered list. The user answers with a number or free text; "go ahead"
  means "recommended options, continue".
- One decision per message (Gate 3 combines two small settings by design).
- After any file-system change, give the absolute path and say what the user
  will see there.

## Gate 0 — locate the mess

If the folder path was not given:

```text
Which folder should I clean up? Drag it into the chat or paste the path.
```

If the user describes several locations, do one folder per run. Suggest
starting with the messiest.

## Gate 1 — scope

After the fast top-level scan:

```text
I scanned /Users/anna/Documents (nothing was changed): 148 loose files at the
top level, plus 13 existing subfolders (projects, old archives).

What should I organize?

1. Only the 148 loose top-level files (recommended) — existing subfolders
   stay exactly as they are
2. Everything, including subfolders — I'll flatten them into the new
   structure (only pick this if those folders are NOT organized on purpose)
3. One specific subfolder — tell me which

Reply with a number, or just say "go ahead" for option 1.
```

Never scan recursively into workspace/project folders by default; if the
user picks option 2, warn once about any subfolder that looks deliberately
organized before including it.

## Gate 2 — structure

Pick the preset that matches the inventory (see `folder-taxonomy.md`) and
show the actual tree, tailored: drop categories with no matching documents,
renumber contiguously, mention what was dropped.

```text
Based on what I found (mostly business paperwork + some personal documents),
here is the structure I suggest — preset 2 of these options:

1. Business / accounting — 7 flat folders (invoices, receipts, statements,
   tax, payroll, contracts, needs-review)
2. Personal + business (recommended for this folder) — two levels:

   01 Finance & Tax        — Bills & Invoices / Receipts / Bank & Card
                             Statements / Tax Documents
   02 Business & Legal     — Contracts & Agreements / Company & Compliance
   03 Employment & Recruitment — Contracts & Offers / CVs & Candidates /
                             References
   04 Identity, Immigration & Personal — Identity Documents / Immigration /
                             Official Correspondence
   05 Education & Family
   06 Health, Travel & Insurance
   07 Needs Review         — Unreadable / Password-Protected / Ambiguous

3. Multi-client — one folder per client, business taxonomy inside each
4. Custom — describe what you want

You can also just tweak option 2: rename folders, add/remove categories,
split invoices into issued vs received, add year subfolders.
```

Rules for this step:

- Accept the user's names verbatim, including non-English folder names.
- Do not proceed until the user has confirmed. "Looks fine" counts as
  confirmation; silence does not.
- If issued-vs-received invoices matter, ask for the user's business name
  here — once.

## Gate 3 — mode and naming

The one two-part message:

```text
Two quick settings before I start reading the documents:

Mode:
1. Copy (recommended for a first run) — originals stay exactly where they
   are; verified copies go into the new folders; undo deletes only the copies
2. Move — files are relocated into the new folders; undo puts them back
3. Report only — I classify and build the index, but touch nothing

File names:
A. Keep original names (recommended)
B. Standardize to "YYYY-MM-DD Counterparty Type.pdf" (original names stay in
   the index)

Say "go ahead" for 1 + A.
```

## During classification — progress, not questions

For folders over ~30 files, report progress in batches so the user is not
staring at silence:

```text
Read 60 of 148… so far: 22 invoices, 15 receipts, 9 statements, 3 for review.
```

Do not ask questions mid-classification unless a genuinely blocking ambiguity
appears.

## Gate 4 — the plan, misfits, approval

```text
All 148 files read. Here's the plan (nothing is applied yet):

| Folder | Files |
|--------|-------|
| 01 Finance & Tax | 52 |
| 02 Business & Legal | 24 |
| ... | ... |
| 07 Needs Review | 7 |

Needs Review: 3 unreadable scans, 2 password-protected PDFs, 2 ambiguous.

I also found 3 documents that fit none of the approved folders — two concert
tickets and a magazine article. Options:

1. Add "08 Events & Tickets" and "09 Articles" for them (recommended)
2. Leave them in 07 Needs Review/Ambiguous
3. Decide file by file

4 exact duplicates found — I'll file them together and flag them, not delete.

Approve the plan? (I'll copy the files — originals stay untouched.)
```

Wait for confirmation, run the dry-run silently, then execute.

Immediately after applying, anchor the user in the file system:

```text
Done. The folders are at /Users/anna/Documents (01–07, next to your existing
folders). Originals are still in place; the new folders hold verified copies.
[clickable path/link when the runtime supports it]
```

If the structure was created before files were applied (avoid this when
possible), say explicitly: "the folders exist but are EMPTY until you approve
the plan — that's why you don't see files in them yet."

## Gate 5 — the deliverable

```text
Folders are done. What do you want as the record?

1. Excel index (recommended) — one row per document: category, date, amount,
   counterparty, where it was filed, and why
2. CSV index — same, opens anywhere
3. Both
4. None — folders are enough

I can also add an audit log — a short Markdown report of this run (what was
scanned, what you approved, counts, undo command). Want it?
```

The index and audit log are written in the user's language (`--lang ru` for
Russian headers; other languages get English headers — rename afterwards if
asked).

## Closing

Use the Output format from `SKILL.md`: counts table, absolute path, Needs
Review list with reasons, index location, undo command. One screen, no fluff.

## Avoid bad behavior

Do not say:

```text
I've organized your documents using advanced AI classification.
```

Say:

```text
52 invoices filed. Every row in the index shows why a file was classified the
way it was — spot-check a few before you rely on it.
```

Do not:

- touch a single file before scope, structure, mode, and plan are all
  confirmed;
- create the folder structure "to show it" before the plan is approved — the
  user sees empty folders and thinks the cleanup failed;
- hide the Needs Review pile at the bottom of a long message — it is the one
  part the user must act on;
- ask open-ended questions where a menu with a recommended default works;
- transcribe passport numbers, SSNs, or medical details into chat, manifest,
  index, or audit log.
