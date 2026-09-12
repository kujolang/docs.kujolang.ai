# Kujo Payments architecture review

Review revision: **2026-09-12**. This revision supersedes the September 10 recommendation where it differs; the [historical package](../../release-audits/payments-2026-09-10/README.md) remains intact. Source observations are dated, proposed contracts are pre-release, and no Payments implementation has begun.

**Verdict: PROCEED WITH ARCHITECTURE CHANGES.** Proceed with the bounded implementation plan, not live financial execution. The smallest defensible primitive is a buyer-side, authorized payment execution journal with provider adapters, exposed through Ability. No payment implementation or live transaction was created by this review.

## Executive summary

Kujo Payments deserves a separate domain because none of the inspected components combines payer intent, verified payment authorization, an immutable execution attempt, and evidence-driven reconciliation. Ability already supplies operation identity, schemas, invocation, approval binding and execution receipts. Dispatch supplies workflow control. Workcell supplies a configurable containment harness. Reimplementing any of those would make Payments larger and less trustworthy.

Keep **`payments`**. `purchases` would imply inventory, carts, fulfillment and returns; `transactions` would ambiguously include database transactions; `spend` suggests budgeting and financial management. Define Payments as the execution of a specifically authorized financial action, initially one purchase. It does not acquire payments for merchants, hold a balance, store raw card details for agents, manage orders, or provide a policy engine. Commerce remains seller-side checkout infrastructure; the buyer/seller distinction is real, although both sides participate in checkout and have idempotency concerns.

The original proposal needs these material corrections:

1. **Credential issuance is not payment execution.** Link approval can issue a card or token without a merchant charge. The adapter must complete a merchant/protocol transaction and independently observe its outcome. An approved SpendRequest is never a successful PaymentReceipt.
2. **Local idempotency is not universal exactly-once settlement.** Ability delegates durable stores; Dispatch caches completed tool output. Payments must persist a submission claim before any charge request and never automatically resubmit an uncertain attempt. A provider must support verifiable replay protection or the adapter must accept loss of liveness through a one-shot submission rule.
3. **Separate operation receipts from financial evidence.** Ability can report a failed audit or timeout after a handler executes. A failed tool invocation does not establish that no money moved. Preserve the authoritative PaymentExecution and inspect it after any transport or receipt failure.
4. **Server-owned tooling is a logical boundary until deployed separately.** `register_ability_gateway_tool` accepts an invocation callback. It does not create a separate principal, container, authenticated transport, or secret store. Workcell intentionally passes declared secrets into workloads. Payment credentials must never be declared as agent workload secrets.
5. **Remove browser credential injection from V1, including LPT.** Tokens inserted in browser DOM remain credentials. Disabling screenshots alone does not remove DOM, network, session, extension or DevTools exposure. A future privileged browser requires its own disposable profile and exclusive process boundary; it must never be handed back to the agent.

6. **Keep request and status as separate small tools.** A keyed multiplexed tool can replay an old pending status; read status must be intrinsic and fresh. Two narrow tools earn their extra schema by keeping effects and caching honest. Cancellation remains a human/application operation.
7. **Bind the merchant route, not just the wallet.** A backend must compose credential authority with a registered merchant protocol and its authoritative evidence. No arbitrary URL, HTTP body or shell command is accepted from the model.

A Link-first reference adapter is sound **only for an explicitly supported machine purchase route**, initially Link SPT plus a registered MPP Stripe merchant route. The current CLI source (0.19.1) includes LPT, transaction-status fields and a SpendRequest creation idempotency key. Issuance idempotency does not prove merchant-charge idempotency. Those details remain adapter-local. A Link-only credential retrieval wrapper would not deserve a new primitive.

V1: one-time purchase, one verified merchant, an exact resolved charge within a user-supplied cap, one ISO fiat currency, explicit one-use authorization, one immutable route, one consequential submission, compact tenant-scoped status, durable evidence and an unresolved-outcome queue. Use a fixture provider first. Link live promotion requires merchant correlation, bounded I/O and reconciliation evidence. If a route cannot provide those, it stays unsupported; there is no virtual-card fallback.

This design benefits business owners through control and recovery, developers through a reusable contract, and the ecosystem through provider neutrality and self-hostability. Its cost is deliberate: uncertain outcomes can require operator attention, and broad browser compatibility is sacrificed to preserve the credential boundary. These costs must be stated to adopters rather than hidden behind automatic retries.

## Review package

| Deliverables | Document |
|---|---|
| 1 Executive summary | This page |
| 2 Ecosystem findings; 11 integration matrix | [Ecosystem and integration ownership](01-ecosystem.md) |
| 3 External standards findings | [Standards and current provider behavior](02-standards.md) |
| 4 Triple Win; 5 universal usefulness | [Product and provider pressure tests](03-assessment.md) |
| 6 Domain model; 12 Ability surface | [Contracts and authorization](04-contracts.md) |
| 7 State machine | [Durability and reconciliation](05-lifecycle.md) |
| 8 SPI; 9 Link mapping | [Provider boundary](06-providers.md) |
| 10 Security architecture; 14 threat model | [Security and deployment boundaries](07-security.md) |
| 13 package layout; 16 V1 specification; 17 phases | [Implementation blueprint](08-implementation.md) |
| Exact contract details and corrections | [Contract details](10-contract-details.md) |
| 15 tests; all 18 final questions | [Verification and final gate](09-verification.md) |

Evidence dates, source hashes, checkout heads and test logs are in [evidence](evidence/). Proposed contracts and proof fixtures are in [fixtures](fixtures/). These artifacts describe a design; they are not a payment SDK, a compliance assessment, or a deployment certification.
