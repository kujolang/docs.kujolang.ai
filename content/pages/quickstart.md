---
title: Five-minute quickstart
description: Create one Kujo file, run it with the VM-first runtime, and check the source.
custom_url: quickstart
template: docs
section: Start here
nav_title: Five-minute quickstart
order: 30
audience: beginner
difficulty: beginner
status: stable
version: current
previous: /install/
next: /choose-a-path/
prerequisites:
  - Kujo CLI on PATH
  - A writable terminal workspace
estimated_time: 5 minutes
tags: [quickstart, cli, runtime]
---

# Five-minute quickstart

Make the smallest useful Kujo program before opening the ecosystem directory.

## Create `hello.kujo`

```kujo
message := "hello from Kujo"
print(message)
```

## Run and check it

```bash
kujo run hello.kujo
kujo check hello.kujo
```

`kujo run` uses the VM-first runtime. The interpreter is available when you need a compatibility or debugging path:

```bash
kujo run --interpreter hello.kujo
```

## Create a project

```bash
kujo init --name hello-kujo
cd hello-kujo
kujo run src/main.kujo
```

The generated project gives you `kujo.toml` and `src/main.kujo`; keep `kujo check`, `kujo format`, and `kujo lint` in the edit loop.

## Next step

Use [Choose a path](/choose-a-path/) when you know what you want to build, or continue with [Language basics](/learn/language-basics/).

