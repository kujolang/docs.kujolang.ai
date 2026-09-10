# Contracts and authorization

## Canonical objects

These are proposed V1 contracts. Required fields are listed explicitly; all objects reject unknown fields, including nested objects. No object accepts an untyped provider response or arbitrary metadata bag. Object definitions and invocation machinery come from Ability; the following schemas describe payment domain values.

| Object / version | Purpose and required fields | Owner / persistence | Classification |
|---|---|---|---|
| `kujo.payment-intent/v1` | `schema`, `intent_id`, `purchase_ref`, `principal`, `kind=purchase`, `payee_ref`, `amount`, `purpose`, `expires_at_ms`, `payment_profile`, `correlation_id` | Gateway freezes normalized intent before preparation; immutable durable row. IDs/principal minted or resolved by server. | Tenant-sensitive; selected fields may be agent-visible. |
| `kujo.payment-execution/v1` | `schema`, `execution_id`, `intent_id`, `intent_digest`, `snapshot`, `snapshot_digest`, `state`, `revision`, `created_at_ms`, `updated_at_ms`, `submission_claimed`, `evidence_refs` | Payments owns journal; reference host uses transactional SQLite on local disk. One execution per accepted V1 intent. | Private financial state; agent sees projection only. |
| `kujo.payment-authorization/v1` | `schema`, `authorization_id`, `execution_id`, `snapshot_digest`, `ability_approval_id`, `authority_ref`, `provider_authorization_ref`, `expires_at_ms`, `state` | **Evidence projection**, not new authority token. Private host row links issued Ability approval and provider proof. `provider_authorization_ref` may be null for a route not requiring extra approval. | Private; approval material never accepted from model arguments. |
| `kujo.payment-receipt/v1` | `schema`, `receipt_id`, `execution_id`, `snapshot_digest`, `outcome`, `observed_amount`, `observed_at_ms`, `evidence_ref`, `assurance` | Payments produces immutable outcome evidence from validated observation. Final outcome rows persist independently of Ability receipts. | Tenant-sensitive; bounded safe projection. |
| `kujo.payment-capabilities/v1` | `schema`, `provider_id`, `adapter_version`, `actions`, `execution_classes`, `constraints`, `observed_at_ms`, `valid_until_ms`, `replay_protection`, `observation_support` | Adapter describes; executor validates and caches per tenant/profile/route. Snapshot copies capability digest; no global mutable registry. | Private routing data; optional summary to client. |
| `kujo.payment-observation/v1` | `schema`, `execution_id`, `snapshot_digest`, `phase`, `outcome`, `observed_at_ms`, `evidence_ref`, `actual_amount`, `next_action`, `retry_after_ms` | Provider adapter emits bounded normalized record; core validates and persists. Fields may be null where defined below. | Private until core projection; no raw provider payload. |

`snapshot`, `snapshot_digest` and `capabilities_digest` are null only while an awaiting-authorization row is still preparing terms. No approval or claim is possible until all are populated and validated; thereafter they are immutable. Authorization projection `state` is `requested|granted|consumed|revoked|expired`; only `granted` can advance toward a claim. Receipt `outcome` is `succeeded|failed_no_effect`; unknown/pending outcomes stay in execution observations. Receipt `assurance` is `provider_confirmed|merchant_and_provider_confirmed|operator_verified`, with the underlying evidence required for the selected value; it is never `certified`. IDs are bounded ASCII strings up to 128 characters, hashes are 64 lowercase hex digits, revisions are increasing nonnegative safe integers, timestamps are safe integer milliseconds, and references resolve under tenant authorization. Arrays are bounded to 100 evidence references per response; older evidence is paginated privately.

`principal` uses Ability identity `{type,id,tenant_id}`. Gateway authenticates it independently; model-supplied principal/tenant fields are rejected. Alias resolution for `payment_profile` and `payee_ref` is scoped to that identity, not a global string map. A merchant name or URL from content is a proposal, never a verified payee identity.

`amount = {mode: exact|maximum, minor: integer, currency: uppercase ISO-4217 code}`. `minor` must be positive and at most 9,007,199,254,740,991, with checked arithmetic throughout. Reject floating JSON values, scientific/decimal textual money, unknown currencies, booleans, negative/zero charges and overflow. Validate currencies against a versioned allowlist; never default an unknown exponent. Format money for display after validation. Provider unit conversion is checked and exact; unsupported fractional precision fails. No foreign exchange or dynamic fees beyond the authorized total.

An intent cap is a user constraint, not permission to change a prepared quote. **V1 resolves an exact inclusive amount before approval**; shipping, tax and fees must be included. An `exact` intent must match; a `maximum` intent permits preparation at or below the cap, then approval binds that exact charge. Changed price, currency, merchant, items or shipping profile version invalidates the snapshot. Cancel an unsubmitted intent and obtain new approval; never mutate an approved snapshot.

Optional intent fields: `items` (up to 50 `{sku,quantity}` lines; stable SKU up to 128 ASCII chars, positive integer quantity), `shipping_profile` (opaque alias), `provider_preference` (registered provider ID, advisory before preparation). No free-form per-item HTML, billing address, card brand/last four, redirect URL, auth details or provider credential identifiers. `purpose` is bounded user-facing text (1–500 chars) treated as data. `correlation_id` is a bounded opaque reference; agent journals hold IDs rather than copies. Server may maintain richer purchase context privately, but only immutable version references/hashes enter authorization.

## Execution snapshot

Required immutable `snapshot` fields:

```text
principal                     Ability identity resolved by host
execution_id                  server-minted random ID
intent_digest                 sha256 over canonical normalized intent
payee                         {id, registry_version, display_name, origin}
charge                        {minor, currency}
request_binding               {route_id, route_version, resource_ref, terms_digest}
payment_profile               {alias, version}
shipping_profile              {alias, version} or null
provider                      {id, adapter_version, account_ref}
execution_class               machine | provider_hosted | browser_injection
capabilities_digest           hash of validated provider snapshot
expires_at_ms                 minimum of intent, quote and authorization validity
```

`payee.id` identifies a verified registry entry. Adapter-private mapping pins the actual PSP seller/profile/account, not only a DNS hostname; display and origin must agree with authoritative merchant evidence. `request_binding` binds request method, destination and exact body through an executor-held terms digest. `resource_ref` resolves to that immutable template; the agent cannot provide arbitrary headers/URLs to a credential-bearing fetch. Template changes require a new version and approval. Redirects are disabled for V1 charge requests.

Use SHA-256 with an explicit digest algorithm label, `sha256-canonical-json-v2`, using Ability's explicit v2 canonical JSON helper for payment object hashing. Reject floats and non-interoperable values before hashing. Do not label it unrestricted RFC 8785: cross-runtime ordering/escaping and Unicode vectors must pass; normalize server IDs and schema keys to ASCII. Preserve existing Ability v1 approval/definition digests with its actual helpers. A Payment snapshot digest is a field **inside** the Ability execute input and therefore bound by the existing approval algorithm. Never replace Ability's digest algorithm unilaterally.

## Approval and authenticity

Human approval, provider authorization and policy permission are three separate facts. A provider may approve spending while application policy denies it; policy may allow a request while provider action is pending. Execution requires all applicable facts for the same snapshot.

1. Host authenticates tenant/principal and policy authority; prepares immutable snapshot.
2. Host creates a private `kujo.payments.execution.execute` Ability invocation with server-minted invocation ID and input `{execution_id,snapshot_digest}`. The mapping to the full immutable snapshot is authoritative and cannot be edited.
3. Trusted human surface displays verified merchant, exact charge, original cap, purpose, payment/shipping aliases, expiry and execution class. If Link is the human surface, the adapter must verify returned merchant/amount terms and correlate its SpendRequest to this invocation before issuing an Ability approval.
4. The authenticated issuer stores the actual `kujo.ability.approval/v1` object: `approval_id`, `binding_digest`, `approved_by`, `issued_at_ms`, `expires_at_ms`, `nonce`, bounded `evidence`. Ability binds ability ID/version/definition, input, principal/tenant and invocation ID (`ability/src/contracts.kujo:95`). Digest equality is not issuer authentication: the host consume callback must look up the issued record, verify approver authority and stored binding/expiry/nonce, and consume once.
5. Host rechecks policy, revocation, quote/profile versions and expiry at dispatch. A transaction consumes approval and reserves the one allowed execution. It does not rely on the agent's `approved=true`, Dispatch `--yes`, Leash biometric assertion or a browser redirect.

No cryptographic proof is claimed for a plain hash. Inside a trusted database boundary, authenticated issuer storage and one-use consumption establish authorization. Across services, use authenticated channels plus issuer signature verification or authoritative lookup; public signatures require reviewed key trust/rotation. Future AP2 mandates are evidence verified by a host adapter, not model-authored approval objects.

Expiry prevents starting a financial action; it cannot retract an already submitted payment. A late callback may resolve an old executing record after expiry, but cannot authorize another submission. Revocation before submission stops it; after submission it requests containment/observation, not a refund or a false `cancelled` status.

## Ability surface versus model-visible surface

All definitions use `schema=kujo.ability/v1`, version `1.0.0`, the existing effects enum and explicit idempotency mode.

| Canonical Ability | Input | Effects / idempotency | Exposure |
|---|---|---|---|
| `kujo.payments.intent.request` | Bounded purchase request with `purchase_ref`, payee/profile aliases, money, purpose, expiry duration | write `kujo.payments.intent`; external `kujo.payments.authorization`; keyed | Optional direct API. Returns accepted summary, never blocks for approval. |
| `kujo.payments.execution.inspect` | `{execution_id}` | read `kujo.payments.execution`; intrinsic | Tenant-scoped; reads local authoritative status only. |
| `kujo.payments.execution.execute` | `{execution_id,snapshot_digest}` | external `kujo.payments.purchase`; keyed | **Executor-only**, never listed to model or general MCP client. |
| `kujo.payments.execution.reconcile` | `{execution_id}` | read/external `kujo.payments.evidence`; keyed | Operator/worker only; cannot submit funds. |
| `kujo.payments.intent.cancel` | `{execution_id,expected_revision}` | write `kujo.payments.intent`; keyed | Trusted human/application API; only closes unsubmitted state. |
| `kujo.payments.request` | `{action: request|status, purchase?: bounded request, execution_id?: string}` | write/read `kujo.payments.intent`; external `kujo.payments.authorization`; keyed | Single model-facing facade. Tags conservatively include mutation even for status branch. |

The facade requires exactly one branch, server-dispatches to domain handlers and returns `{execution_id,status,next_action,receipt_ref}`. It does not invoke a second user-visible approval system. Gateway supplies a stable idempotency key on mutating calls; `purchase_ref` also has a tenant/principal uniqueness constraint, so inventing another transport key cannot repeat the same authorized purchase. A new purchase reference still requires independent approval; V1 is not an aggregate spend-control system.

`next_action` is `none|await_authorization|await_provider|operator_review|inspect_receipt`; optional `action_ref` points to an authenticated human UI. Do not pass bearer approval URLs through model context. Agent cannot call cancel/reconcile/execute directly. Capability negotiation and checkout discovery happen server-side using registered routes; model is not shown the provider SPI.

A request Ability receipt may say `succeeded` because the request was persisted, with result status `awaiting_authorization`. It does not claim payment success. On `ability_audit_failed_after_execution`, timeout or connection loss, inspect by purchase/execution ID. Repeating intake with the same key can return the same operation; it never creates another financial attempt.
