---
title: Evidence and run history
description: Preserve the receipt, failure bundle, usage, and handoff that explain what happened.
custom_url: review/evidence-and-run-history
template: docs
section: Keep work reviewable
nav_title: Evidence and run history
order: 30
audience: developer
difficulty: intermediate
status: launch scope
version: current
previous: /review/tests-and-evaluation/
next: /review/quality-and-release-gates/
tags: [evidence, casefile, runledger]
---

# Evidence and run history

- [RunLedger](/tools/runledger/) records run metadata, usage, cost, verdicts, and follow-ups.
- [CaseFile](/tools/casefile/) captures a failure as a reproducible evidence bundle.
- [PatchBrief](/tools/patchbrief/) turns a diff into a reviewable summary and handoff.
- [ChangeBucket](/tools/changebucket/) measures change footprint and blast radius.

```bash
runledger start --name local-check
casefile capture --from-log build.log
```

Use these artifacts to make a handoff legible. Do not treat a receipt as automatic billing capture or a signed security attestation.

