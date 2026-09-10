# V1 specification and implementation blueprint

## Frozen V1

Implement a buyer-side one-time purchase primitive with one verified merchant, an exact inclusive charge resolved within the requested maximum, one fiat currency, explicit one-use authorization, one immutable route and one submission claim. Support fixture operation without external services. Add Link SPT/MPP only for routes that meet the published conformance gates. No credential-bearing agent interface.

Use Kujo modules for core, gateway and provider logic where supported. The review's Python proof is a repository-maintenance model exercising SQLite interleavings; it is not a Python Payments implementation or a production bridge. A provider SDK sidecar is a documented exception only if direct Kujo integration cannot reasonably satisfy the protocol; freeze its version and isolate its output.

Excluded: browser injection (PAN and LPT), card/account management, transaction-history tools, subscriptions, recurring/standing budgets, autonomous refunds, transfers, FX, split/partial payments, crypto intent units, portfolio/financial advice, seller acquiring, full cart/order/fulfillment management, multi-region stores, proprietary Kujo SaaS and arbitrary provider installation. Deferred capabilities are not advertised as supported.

## Repository and package layout

```text
payments/
  kujo.toml
  kennel.toml + kennel.lock             only if Kennel is selected for distribution
  README.md  SECURITY.md  CHANGELOG.md
  contracts/
    intent.schema.json  execution.schema.json  receipt.schema.json
    authorization.schema.json  observation.schema.json  capabilities.schema.json
    abilities/*.json
  src/
    domain/                            pure validation, snapshots, lifecycle, projections
    application/                       use cases, Ability hooks, injected policy/store/SPI
    storage/                           durable reference SQLite implementation
    providers/contract.kujo             SPI validation only
    providers/fixture/                 fake adapter, never installed in live registry
    providers/link/                    private API mapping; no model-facing CLI
    executor/                          trusted composition root, worker, credential access
    gateway/                           authenticated request/status boundary
    client/                            credential-free request/status client
  examples/
    local-fixture/
    agents-sdk/
    dispatch/
    workcell-agent/
  tests/
    unit/ contract/ fixtures/ security/ fault/ sandbox/
  docs/
    architecture.md security.md provider-authoring.md operations.md
  fence.toml
```

Dependency direction: client → published contracts and gateway transport; gateway → application; application → domain, Ability and injected ports; storage/adapters → domain and port contracts; executor → application/storage/adapters at the only privileged composition root. Domain cannot import provider implementations, storage, AI SDK or executor. Commerce has no dependency in either direction. Optional integrations are examples/configuration rather than empty modules for every ecosystem tool.

Only executor reads secret store handles; provider code receives needed privileged handles via construction inside executor, never by importing agent config. Public package entrypoints exclude provider/executor modules. Package split may follow if distribution tooling cannot enforce this export boundary; do not add a generic plugin host.

## Machine-enforced fences

Use Fence v1 TOML syntax with distinct zones: client, gateway, application, domain, storage, provider_contract, provider_implementations and executor. Declare `unknown_dependency_policy="deny"`, error severity and fail-on error. Explicit cannot-depend-on rules prohibit client/gateway/domain importing executor or provider implementations. Domain imports only domain; application may import domain/provider_contract/Ability. Executor is the permitted composition root.

Fence's external-import fallback allows unlisted third-party modules, and same-zone imports are always allowed. Therefore add a separate locked-dependency inventory check and privileged-builtin usage check: `env`, `reveal`, filesystem/secret/process/network consumers outside approved executor/provider/storage boundaries fail. Static checks cover direct code/imports only; reject dynamic module loading and user-specified shell in product code. Mutation tests deliberately add forbidden imports, undeclared external packages and secret API calls and must fail. A passing Fence scan never substitutes for runtime isolation testing.

## Phased plan

Each phase is independently reviewable. Phase 0 accepts the architecture; later phases implement the specified proof rather than adding speculative features. Do not move real money to finish an offline gate.

| Phase | Goal and files/repos | Required tests | Exit evidence and principal risk |
|---|---|---|---|
| 0 — Contract review | Proposed payments repo: architecture, schema drafts, decision record, threat model and conformance cases. This review resides in docs repo until implementation begins. | Schema examples, golden digest vectors, provider pressure tests, boundary review. | All final architecture questions resolved; explicit conditional live gates. Risk: mistaking a paper decision for runtime proof. |
| 1 — Durable fixture core | payments `src/domain`, `src/storage`, fixture provider, schema files. | Money edges, state transitions, SQLite CAS/concurrent workers, kill/reopen at claim and evidence boundaries, retained key tombstones. | No financial retry after any unknown outcome; same purchase cannot gain a second claim. Risk: API/store durability semantics differ from proof model. |
| 2 — Ability and gateway | payments `src/application`, `src/gateway`, `src/client`, Ability definitions. Existing Ability/SDK/MCP unchanged. | Definition validation in actual Kujo runtime, approval issuer/nonce tests, wrong tenant/principal, async intake, result/receipt separation, post-effect audit failures. | Minimal agent facade; privileged execute hidden and inaccessible; no schema system duplication. Risk: treating hashed approval as authenticated approval. |
| 3 — Physical boundary | payments executor deployment and Workcell example; operator egress config. No Workcell core changes assumed. | Separate-principal runtime breakout, mount/env/process/socket/browser checks, malicious merchant input, egress redirects/DNS/IP policy. | Exact supported host profile documented and tested. Risk: platform/engine configuration or host network exposes credentials. |
| 4 — Link machine adapter | payments `providers/link`, pinned API/optional sidecar and synthetic provider fixtures. | SpendRequest create ambiguity, approval/expiry/revocation, SPT sentinel, full MPP challenge binding, status mapping, missing correlation and unknown enums. | Offline conformance passes; no raw output; API revision and unsupported routes explicit. Risk: provider idempotency/finality not guaranteed by SDK source. |
| 5 — Sandbox validation | payments sandbox tests, exact test account/merchant revision recorded. | Provider success→connection loss→reconcile; test-mode environment separation; amount/merchant/body mutations; pending human step-up. | Independently correlated sandbox financial outcome; no implicit promotion or live fallback. Risk: sandbox differs from real account/rail. |
| 6 — Optional ecosystem composition | payments examples for Dispatch, Agents SDK/MCP, Workcell and sanitized telemetry. | Paused request resumes by inspecting ID; no `--yes` bypass; tool schema/payload budgets; all selected evidence sinks scanned. | No upstream code changes, no duplicate journal or policy ownership. Risk: integration retries or transcript capture reintroduce leakage. |
| 7 — Release security gauntlet | payments security/fault/conformance tests, Fence, Spec/Eval/ShipCheck and pinned packages. | All threat rows; worker concurrency, kill matrix, disk full, restoration freeze, provider disappearance, terminal contradiction, redaction canaries. | Published scoped test evidence and honest supported environments; no blanket safety/PCI claims. Risk: broad readiness language exceeds tested deployment. |
| 8 — Explicit live acceptance | payments operator runbook and controlled live receipt, only under separately explicit transaction authorization. | Small exact approved transaction, bank/provider follow-up, redacted evidence, emergency stop and recovery drill. | Exact account, merchant, amount, policy and operator approval recorded. If evidence is missing, keep Link experimental. No automatic real-money CI. |

## Operations and recovery

Local usefulness: validate contracts, run fixture provider and inspect existing receipts with no network. Embedded mode is suitable for trusted application code and fixtures; embedding executor in an untrusted agent process is unsupported. Self-hosting can run a separate service on the same machine under a distinct principal or on a remote host. Hosted identity/notification/storage are options, not Kujo requirements.

Operators own service identity, tenant mapping, key custody/rotation, provider credentials, database backups, egress, retention and incident response. Introduce an execution stop switch that blocks new claims but leaves observation and evidence export working. Never erase an unresolved claim to resume traffic. Restores start in observation-only mode until journal/provider state is reconciled.

Provider disappearance leaves evidence and unknown state intact. Another provider can serve **new** explicitly authorized purchases; it cannot take over an ambiguous old one. Adding a provider means implementing six-or-fewer SPI methods, capability declarations and the common conformance cases, with private native mappings and no core special case.

Human approval lives in an authenticated UI/provider surface. Financial status comes from executor observation. Cancellation stops an unsubmitted request; submitted funds require explicit later provider/operator processes, outside V1. Receipt retention follows deployment policy and applicable obligations; this review specifies no jurisdiction-independent legal retention period.
