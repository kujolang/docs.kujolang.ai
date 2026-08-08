---
title: Context and task contracts
description: Turn an open-ended request into a structured contract with scope, acceptance, and evidence.
custom_url: context-and-task-contracts
template: docs
section: Keep work reviewable
nav_title: Context and task contracts
order: 10
audience: developer
difficulty: intermediate
status: launch scope
version: current
next: /ecosystem/
tags: [spec, context, contracts]
---


Start with [Spec](/tools/spec/) when the work needs a name, objective, acceptance criteria, constraints, and a clear completion state.

```bash
kujo run spec.kujo validate task.spec.yml
```

Then use [Scout](/tools/scout/) to map the repository and [Scent](/tools/scent/) to package the narrow context that the task actually needs. The artifact is a contract and a focused context pack, not a giant transcript.
