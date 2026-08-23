---
title: Language basics
description: Learn the small set of Kujo syntax and program shapes needed to read a real file.
custom_url: language-basics
template: docs
section: Learn Kujo
nav_title: Language basics
order: 10
audience: beginner
difficulty: beginner
status: stable
version: current
last_updated: 2026-08-23
next: /learn/runtime/
tags: [language, syntax, beginner]
---


Kujo files are plain text and are meant to stay readable in review. Start with values, bindings, functions, modules, and explicit errors.

## A small program

```kujo
func greet(name) {
  return "hello, " + name
}

message := greet("Kujo")
print(message)
```

## Practice loop

```bash
kujo check hello.kujo
kujo format hello.kujo
kujo run hello.kujo
```

When you need exact syntax or builtin behavior, move to [Reference](/reference/) after understanding the intent of the program.

