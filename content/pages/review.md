---
title: Keep work reviewable
description: Define work, focus context, run checks, capture proof, and gate release decisions.
custom_url: review
template: docs
section: Keep work reviewable
nav_title: Keep work reviewable
order: 60
audience: developer
difficulty: intermediate
status: stable
version: current
next: /review/context-and-task-contracts/
tags: [review, evidence, quality]
---

# Keep work reviewable

The review loop is a sequence of small, inspectable artifacts:

```text
Define the work → Spec
Focus the context → Scout + Scent
Prepare execution → PackWrite + Muzzle
Run the work → Kujo + Dispatch
Check the result → Eval + repository tests
Inspect the change → PatchBrief + ChangeBucket + Concord
Capture the proof → RunLedger + CaseFile
Gate the release → ShipCheck + Fence + Lens + Redact
```

## Start small

- Define a task contract with [Spec](/review/context-and-task-contracts/).
- Package only the context needed for that task.
- Run deterministic checks with [Eval](/review/tests-and-evaluation/).
- Leave a receipt or evidence bundle for the next person.

The tools are local-first. A receipt or report is evidence of a run in a specific workspace, not a blanket claim that a project is enterprise-ready.

