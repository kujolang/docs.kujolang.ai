# Contracts and authorization

## Canonical objects

These are proposed V1 contracts. Required fields are listed explicitly; all objects reject unknown fields, including nested objects. No object accepts an untyped provider response or arbitrary metadata bag. Object definitions and invocation machinery come from Ability; the following schemas describe payment domain values.

| Object / version | Purpose and required fields | Owner / persistence | Classification |
|---|---|---|---|
| `kujo.payment-intent/v1` | `schema`, `intent_id`, `purchase_ref`, `principal`, `kind=purchase`, `payee_ref`, `amount`, `purpose`, `expires_at_ms`, `payment_profile`, `correlation_id` | Gateway freezes normalized intent before preparation; immutable durable row. IDs/principal minted or resolved by server. | Tenant-sensitive; selected fields may be agent-visible. |
| `kujo.payment-execution/v1` | `schema`, `execution_id`, `intent_id`, `intent_digest`, `snapshot`, `snapshot_digest`, `state`, `revision`, `created_at_ms`, `updated_at_ms`, `submission_claimed`, `evidence_refs`, `closed_reason`, `next_action` | Payments owns journal; reference host uses transactional SQLite on local disk. One execution per accepted V1 intent. | Private financial state; agent sees projection only. |
| `kujo.payment-authorization/v1` | `schema`, `authorization_id`, `execution_id`, `snapshot_digest`, `ability_approval_id`, `authority_ref`, `provider_authorization_ref`, `expires_at_ms`, `state` | **Evidence projection**, not new authority token. Private host row links issued Ability approval and provider proof. `provider_authorization_ref` may be null for a route not requiring extra approval. | Private; approval material never accepted from model arguments. |
| `kujo.payment-receipt/v1` | `schema`, `receipt_id`, `execution_id`, `snapshot_digest`, `outcome`, `observed_amount`, `observed_at_ms`, `evidence_ref`, `confirmation_rule_ref`, `assurance` | Payments produces immutable outcome evidence from validated observation. Final outcome rows persist independently of Ability receipts. | Tenant-sensitive; bounded safe projection. |
| `kujo.payment-capabilities/v1` | `schema`, `provider_id`, `adapter_version`, `actions`, `execution_classes`, `constraints`, `observed_at_ms`, `valid_until_ms`, `replay_protection`, `observation_support` | Adapter describes; executor validates and caches per tenant/profile/route. Snapshot copies capability digest; no global mutable registry. | Private routing data; optional summary to client. |
| `kujo.payment-observation/v1` | `schema`, `execution_id`, `snapshot_digest`, `phase`, `outcome`, `observed_at_ms`, `evidence_ref`, `actual_amount`, `next_action`, `retry_after_ms` | Provider adapter emits bounded normalized record; core validates and persists. Fields may be null where defined below. | Private until core projection; no raw provider payload. |

`snapshot` and `snapshot_digest` are null only while an awaiting-authorization row is still preparing terms. No approval or claim is possible until both and the nested capability digest are populated and validated; thereafter they are immutable. Authorization projection `state` is `requested|granted|consumed|revoked|expired`; only `granted` can advance toward a claim. Receipt `outcome` is `succeeded|failed_no_effect`; unknown/pending outcomes stay in execution observations. Receipt `assurance` is `provider_confirmed|merchant_and_provider_confirmed|operator_verified`, with the underlying evidence required for the selected value; it is never `certified`. IDs are bounded ASCII strings up to 128 characters, hashes are 64 lowercase hex digits, revisions are increasing nonnegative safe integers, timestamps are safe integer milliseconds, and references resolve under tenant authorization. Arrays are bounded to 100 evidence references per response; older evidence is paginated privately.

`principal` uses Ability identity `{type,id,tenant_id}`. Gateway authenticates it independently; model-supplied principal/tenant fields are rejected. Alias resolution for `payment_profile` and `payee_ref` is scoped to that identity, not a global string map. A merchant name or URL from content is a proposal, never a verified payee identity.

`amount = {mode: exact|maximum, minor: integer, currency: uppercase ISO-4217 code}`. `minor` must be positive and at most 9,007,199,254,740,991, with checked arithmetic throughout. Reject floating JSON values, scientific/decimal textual money, unknown currencies, booleans, negative/zero charges and overflow. Validate currencies against a versioned allowlist; never default an unknown exponent. Format money for display after validation. Provider unit conversion is checked and exact; unsupported fractional precision fails. No foreign exchange or dynamic fees beyond the authorized total.

An intent cap is a user constraint, not permission to change a prepared quote. **V1 resolves an exact inclusive amount before approval**; shipping, tax and fees must be included. An `exact` intent must match; a `maximum` intent permits preparation at or below the cap, then approval binds that exact charge. Changed price, currency, merchant, items or shipping profile version invalidates the snapshot. Cancel an unsubmitted intent and obtain new approval; never mutate an approved snapshot.

The gateway resolves optional item lines from the immutable purchase resource; the model request need not transmit them. Optional intent fields: `items` (up to 50 `{sku,quantity}` lines; stable SKU up to 128 ASCII chars, positive integer quantity), `shipping_profile` (opaque alias), `provider_preference` (registered provider ID, advisory before preparation). No free-form per-item HTML, billing address, card brand/last four, redirect URL, auth details or provider credential identifiers. `purpose` is bounded user-facing text (1–500 chars) treated as data. `correlation_id` is a bounded opaque reference; agent journals hold IDs rather than copies. Server may maintain richer purchase context privately, but only immutable version references/hashes enter authorization.

## Execution snapshot

Required immutable `snapshot` fields:

```text
principal                     Ability identity resolved by host
execution_id                  server-minted random ID
intent_digest                 sha256 over canonical normalized intent
payee                         {id, registry_version, display_name, origin}
charge                        {minor, currency}
currency_table_version        reviewed fiat unit table revision
request_binding               {route_id, route_version, resource_ref, terms_digest}
payment_profile               {alias, version}
shipping_profile              {alias, version} or null
provider                      {id, adapter_version, account_ref}
execution_class               machine | provider_hosted | browser_injection
capabilities_digest           hash of validated provider snapshot
expires_at_ms                 minimum of intent, quote and authorization validity
```

`payee.id` identifies a verified registry entry. Adapter-private mapping pins the actual PSP seller/profile/account, not only a DNS hostname; display and origin must agree with authoritative merchant evidence. `request_binding` binds request method, destination and exact body through an executor-held terms digest. `resource_ref` resolves to that immutable template; the agent cannot provide arbitrary headers/URLs to a credential-bearing fetch. Template changes require a new version and approval. Redirects are disabled for V1 charge requests.

Use the versioned payment-specific encoding in [Contract details](10-contract-details.md) for payment object digests. Do not import `ability/src/internal.kujo`: the public Ability API exports definition digests and approval binding, not a general canonical-JSON utility. Keep Ability v1 definition/approval digests unchanged and execute their helpers in the trusted Kujo host. A Payment snapshot digest is a scalar **inside** the Ability execute input and is bound by its existing approval algorithm. Cross-service clients refer to the host-issued approval; they do not recompute v1 approval bindings independently.

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
| `kujo.payments.execution.reconcile` | `{execution_id}` | external `kujo.payments.evidence`, write `kujo.payments.execution`; keyed | Operator/worker only; cannot submit funds. |
| `kujo.payments.intent.cancel` | `{execution_id,expected_revision}` | write `kujo.payments.intent`; keyed | Trusted human/application API; only closes unsubmitted state. |

**Agent-visible projection:** expose only `purchase_request` for `kujo.payments.intent.request` (keyed) and `purchase_status` for `kujo.payments.execution.inspect` (intrinsic). Do not ship a separate multiplexed Ability. The full internal surface remains the five operations above. Human/application cancellation is retained; it need not consume model schema tokens.

Intake persists the request and returns `{execution_id,status,next_action,receipt_ref}` promptly. Identity, correlation, idempotency key and durable purchase reference come from authenticated host context. Repeated request with the same business purchase reference returns the existing execution or a conflict; a new transport key cannot reset it. A new business reference needs fresh authorization. Status reads local authoritative state on every call and never returns an Ability idempotency-cache snapshot.

`next_action` is `none|await_authorization|await_provider|operator_review|inspect_receipt`; a host-only optional `action_ref` refers to the application's trusted human UI. No bearer URL enters model context. Capability negotiation, approval, execute and reconcile are hidden from model discovery and denied by transport authorization, not merely omitted from a tool list.

A request Ability receipt says `succeeded` when intake persisted successfully, even if result status is `awaiting_authorization`. It does not claim payment success. After a timeout or failed operation receipt, query the same business reference/execution; never manufacture a new purchase to retry. An exact transport key replay may legitimately return the original intake receipt: follow it with fresh `purchase_status`.

The request definition conservatively declares external purchase authority as well as journal mutation because accepting a request can schedule a consequential action after approval. Automatic tool execution permission does not substitute for the private, one-use execute approval.
