# Provider execution boundary

## Exact recommended SPI

This is a typed pseudocode specification, not a runtime implementation. Calls run **inside the privileged executor**. No callable returned by the provider is serialized or dynamically loaded from merchant content. Registry construction is per executor instance and accepts only operator-installed, pinned adapters.

```text
PaymentProvider/v1 {
  describe(Context) -> ProviderCapabilities
  prepare(Intent, OperationContext) -> Preparation
  request_authorization(PreparedRef, OperationContext) -> Observation
  submit(PreparedRef, SubmissionContext) -> Observation
  observe(ExecutionRef, ObservationContext) -> Observation
  cancel(ExecutionRef, OperationContext) -> Observation       // optional
}
```

| Method | Contract and why it exists |
|---|---|
| `describe` | Returns action support and current route/profile constraints. No financial effect. May return unknown/unavailable; absence never means unlimited. Cached to explicit expiry, rechecked at submit. |
| `prepare` | Resolve verified payee/merchant terms and supported route; no money movement or spendable credential issuance. Return normalized immutable terms, expiry and an opaque internal reference. Unsupported routes fail here. |
| `request_authorization` | Start provider approval/credential preparation if needed; return promptly. When provider needs no extra approval, return `authorized` with authenticated policy/provider evidence, never a fabricated human approval. May issue a scoped credential privately, but must not charge. |
| `submit` | One consequential dispatch under already-durable claim, bound to immutable snapshot. May return pending, human action, success, definite no-effect or unknown. Never retries an uncertain dispatch or changes route. |
| `observe` | Retrieve current authorization/financial status without moving money. Consolidates authorization_status, inspect and reconciliation. Can return unknown indefinitely. Required even if only explicit operator reconciliation is possible. |
| `cancel` | Optional best effort revocation before submission. After dispatch, it cannot claim cancellation without authoritative no-effect evidence. No refund, void or compensation is implied. V1 local cancellation works even when provider cancel is unsupported, provided no submit occurred. |

`Context={tenant_id,principal_ref,profile_ref,route_ref,deadline_ms}`. It is executor-owned, authenticated and contains no secret values. `OperationContext` adds `execution_id,operation_id`; operations use different stable IDs for prepare, approval and submit. `SubmissionContext` adds `invocation_id,snapshot_digest,claim_id,provider_idempotency_key`; core constructs it after durable reservation. `ObservationContext` adds `phase=authorization|execution,next_cursor?` and a read-only deadline. All time values are bounded integer milliseconds.

`Preparation={prepared_ref,terms,expires_at_ms,capabilities_digest}` where `terms` supplies fields needed for the immutable execution snapshot: canonical payee, exact charge, request binding, profile versions and selected class/provider. `prepared_ref` and `ExecutionRef={execution_id,prepared_ref}` are executor-local identifiers, never credential values or agent capabilities. Reference access additionally checks tenant, account and route.

`Observation` follows the domain schema. `next_action` is null or `{kind:human_action|operator_review,action_ref}`; `actual_amount` is required for success, null before financial evidence. `evidence_ref` resolves only within the privileged evidence store. `retry_after_ms` is advisory for observation only; it never grants submit permission. Core validates legal phase/outcome combinations, bounded strings and enums and applies state transitions; provider code cannot modify canonical intent.

All adapters receive a restricted HTTP client with explicit destination policy, byte/time limits and no retrying charge requests. Adapter exceptions become fixed error codes before leaving executor. Unknown outcomes fail to reconciliation. A provider-supplied sanitizer does not define what the agent may see: egress is a core allowlist built from validated fields.

## Capabilities and constraints

Stable V1 capabilities: `actions=[purchase]`, supported execution classes, `observation_support={authorization,execution}`, `replay_protection={strategy:provider_key|one_shot,retention_ms:null|integer}`. `provider_key` is advertised only with verified provider behavior; one-shot remains the reference submit policy even when the provider has extra replay protection.

Dynamic `constraints` contains `currencies`, `regions`, `minimum_minor`, `maximum_minor`, `authorization_required`, `credential_expires_at_ms`, `available`, each scoped to profile/route and including observation validity. Amount limits are keyed by currency, not a bare number. Unknown availability or currency prevents selection. Declared adapter capabilities are pinned installation metadata; dynamic responses cannot enable a forbidden execution class.

Resolve intersection of request requirements, host policy, installed adapter support, merchant acceptance and current account constraints. Freeze chosen provider/class/account/merchant in snapshot. A new adapter registers the same SPI and passes fixture/concurrency/egress tests. No `if provider == link` appears in core.

## Link mapping

Source pin: [stripe/link-cli](https://github.com/stripe/link-cli/tree/4aa62ba34eaeb884d00041681f5c7801521c0bf8), CLI package 0.19.1. Read implementation as well as README. This is a proposed mapping, not a tested production integration.

| Link concept | Generic operation | Private location and checks |
|---|---|---|
| SpendRequest | `request_authorization`; later `observe` | Adapter stores ID, immutable terms and provider state. `packages/sdk/src/resources/spend-request.ts:104` sends create; `:156` requests approval; `:176` retrieves. No core SpendRequest type. |
| Human approval | authorization observation + host Ability issuer | Compare returned terms and account against prepared snapshot. `approved` means credential authority, not paid. Wrong or unknown status stops. |
| SPT | `submit` for registered MPP Stripe route | Retrieve only immediately before use, retain in privileged memory; transmit to verified merchant/protocol endpoint. Never receipt, stdout or Dispatch state. |
| LPT | Future `browser_injection` route | Browser-frame account binding stays private. Token stays secret even though it replaces PAN. Entire path excluded from V1. |
| Virtual card | Future browser executor | PAN/CVC/billing details belong exclusively to isolated executor/browser, outside V1. No fallback from failed SPT/LPT. |
| CLI/API | Adapter transport implementation | Prefer Kujo HTTP implementation against pinned documented endpoints; use a fixed CLI/SDK sidecar only if API access cannot be supported. No installing/upgrading at execution time. |
| `payment_status_details`, `link_transaction_id` | `observe` | SDK types at `packages/sdk/src/types/index.ts:123` and `:152` support outcome/correlation fields; require strict runtime validation rather than trusting loose schema. |
| Transactions resource | Operator/executor observation | `packages/sdk/src/resources/transactions.ts:10` defines transaction fields; `:73` lists bounded pages. Never expose purchase history to model; no fuzzy amount/time matching as proof. |
| `--test` | Sandbox adapter mode | Distinct provider environment/account and fixtures; no live fallback. LPT test mode absent in inspected source. |

The current SDK response validator uses a loose object and accepts arbitrary status strings (`resources/spend-request.ts:17`); the Payments adapter must enforce a narrower egress schema. The current `CreateSpendRequestParams` includes `idempotency_key` (`packages/sdk/src/resources/interfaces.ts:27`), and `create` serializes the supplied body. This corrects the September 10 report. Pin and pass the same issuance key, but do not infer its server retention/conflict behavior or merchant-charge semantics from a TypeScript property. `getDuplicateSpendRequest` is correlation evidence, not proof of settlement.

The CLI's `mpp pay` is not a ready-made secure executor. `packages/cli/src/commands/mpp/pay.tsx` refreshes a challenge at a pinned destination and refuses redirects on the paid request. It returns merchant-controlled response data, and the refreshed financial terms must still be compared to the authorized snapshot. That output is merchant-controlled. The reference adapter must bind destination/method/body/challenge, disable redirects and unbounded output, and discard everything except validated evidence. A 2xx response from the initial unauthenticated request must not be reported as a paid execution.

## Minimum Link acceptance proof

Before marking the Link route usable, demonstrate with the exact account/API/merchant revision:

- Wallet account and merchant/network identity are independently resolved and frozen; merchant content cannot substitute a different profile.
- Nonblocking approval is correlated to the same immutable execution. Any account setup or 3DS action remains on the trusted human surface.
- SPT transmission is one-shot, destination-bound and absent from all logs/artifacts. A replacement credential is not issued after unknown charge status.
- A successful payment yields an authenticated, exact transaction reference and amount/currency/payee evidence. If Link omits fields required for that proof, the route remains unresolved or unsupported.
- Crash after charge and before receipt persistence recovers through those references. Provider disappearance leaves a durable unresolved record.

No live acceptance proof was obtained in this review. Source establishes plausible mappings and several critical constraints; it does not establish server finality, exactly-once issuance or complete reconciliation guarantees.

## Execution class semantics

`machine` means a deterministic authenticated protocol/API submission inside the privileged executor, without credential insertion into a browser controlled by the requesting runtime. `provider_hosted` means a trusted provider-controlled human surface completes authorization/payment, with a correlated result independently observed by the executor. `browser_injection` means executor-controlled automation inserts payment credentials into a browser DOM; LPT is in this class even though it is a token. These are exposure classes, not rankings of settlement safety. `bank_redirect` is provider-hosted delivery; `tokenized` describes credential form and is not a fourth class. V1 allows only machine routes; adding a new delivery class requires explicit host support, policy and deployment tests.

## Bounded Link transport contract

Prefer documented HTTPS endpoints from Kujo. Direct API implementation must use the reviewed Link authentication/API contract and a version manifest; access to Stripe's ordinary API SDK does not imply Link API coverage. Use the narrow agent-payment scope and eligibility lookup only where required; do not request financial-insight history/balance scopes.

If a pinned CLI or SDK sidecar is necessary, it belongs entirely inside the executor. Start a fixed absolute executable with a typed argv array; no shell, no runtime package installation, no inherited PATH resolution, no model-supplied executable/subcommand and no provider `_next.pay_command` execution. Validate operation arguments against the chosen route, use an executor-owned nonsymlink cwd, `inherit_env=false` plus an explicit environment allowlist, bounded stdin, a hard deadline and byte cap on both streams. Kujo `spawn_process` supports these controls in `src/interpreter/native_functions/system.rs`. Parent stdout/stderr must contain only normalized safe output; raw credential output is confined to private memory/IPC and never spooled by an outer runner. Reject debug/verbose/output-file overrides from callers.

Defaults proposed for fixture benchmarking are 10 seconds and 64 KiB per call, configurable within deployment ceilings. Kill timed-out processes and descendants using tested platform controls; killing a process does not cancel a request already received by a provider. Classify every exception, nonzero exit, timeout, oversized/truncated output or invalid JSON by operation phase: preparation becomes pending/unknown preparation, post-claim submit becomes reconciliation_required. An exit 0 with a pending SpendRequest is not payment success. Unknown native status maps to unknown, never approval or no-effect.

Native OAuth access/refresh, SPT/LPT and card fields remain in `providers/link/private` and the executor's secret store. `link_pay_token` currently depends on same-frame account markers, uses an execution-method setting rather than a new credential-type enum, and lacks CLI test mode in the pinned source; none of that changes the generic schema. Card and LPT requests are disabled, not fallback strategies. Cleanup cancels/revokes unused native authority where supported; no deletion or local process exit is claimed to revoke remote financial authority.
