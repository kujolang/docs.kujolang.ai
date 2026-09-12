# Contract details and review corrections

This document completes the implementation contract where a diagram or object inventory leaves choices open. Everything here is a proposed Payments requirement, not shipped runtime behavior. The machine-readable shapes in [fixtures](fixtures/) must remain consistent with these rules; relational constraints require executable domain validation as well as JSON Schema.

## Responsibilities at the last boundary

A PaymentProvider is a **payment execution backend**. A wallet that only issues a credential is insufficient. Link is composed with a registered MPP merchant route inside its backend. The backend owns native credential exchange, merchant protocol submission and observation, while core owns canonical terms, claim admission and state changes. No separate extensible merchant-workflow engine is needed for V1: install a small operator-reviewed route table with explicit protocol revision and request-template version.

A route record contains `route_id`, `version`, verified payee identity, merchant origin, protocol name/revision, provider acceptance identity, request-template digest, confirmation rule and evidence lookup strategy. The private record may contain endpoint paths and processor account identifiers. Only its opaque ID/version and binding digest are portable. Arbitrary merchant URLs supplied by an agent cannot become credential-bearing routes. Adding a new backend can add its own route resolver; core sees the same normalized snapshot.

The submitted request must refer to an immutable resource/order/challenge or use a conditional version enforced by the merchant. Re-fetching a mutable cart immediately before payment leaves a race; it is insufficient if the merchant can change the recipient or total between check and charge. A route without enforceable exact terms, credential scoping and reliable binding is unsupported. Core cannot repair a merchant that declines to honor its own transaction contract.

## Money and canonical binding

V1 is one fiat-denominated purchase. A currency's minor-unit exponent is validated against a versioned currency table; record `currency_table_version` in the snapshot. Provider-specific unit exceptions are exact adapter conversions, not changes to currency meaning. Unknown or obsolete codes require an explicit reviewed table update. Examples: USD 5500 = USD 55.00, JPY 55 = JPY 55, KWD 55000 = KWD 55.000. Never equate USD and USDC. Refunds, FX, asset denominations and recurring authorizations require a later versioned contract.

All monetary JSON numbers must decode to exact integers in `[1,9007199254740991]`. Reject boolean values and fractional values. JSON Schema's `integer` describes a mathematical integer and some parsers accept `5500.0` or exponent notation as that integer; **lexical rejection requires an ingress parser check**, not merely the schema. The canonical host serializer emits ordinary base-10 integers. Conformance must test parser and serialization behavior independently of schema validation.

Payment binding uses SHA-256 over a fixed-order **field vector**, not a new operation-contract protocol. Each vector starts with an ASCII domain/version string. Encode every element as decimal UTF-8 byte length, a colon, then those exact bytes, concatenated; empty string encodes `0:`. Integers are canonical base-10 strings, boolean flags are `0` or `1`, optional values use a presence flag followed by their fields when present. Never concatenate raw fields with an ambiguous delimiter. UTF-8 is used without Unicode normalization, which would otherwise silently change user text. IDs and schema keys are ASCII. This simple payment-specific encoding avoids importing private Ability canonicalization helpers or changing existing Ability approval digests.

Intent vector order:

```text
kujo.payment-intent-binding/v1
intent_id, purchase_ref, principal.type, principal.id, principal.tenant_id,
kind, payee_ref, amount.mode, amount.minor, amount.currency,
purpose, expires_at_ms, payment_profile, correlation_id,
shipping_profile-present, [shipping_profile],
provider_preference-present, [provider_preference],
items-count, [sku, quantity] repeated in supplied order
```

Snapshot vector order:

```text
kujo.payment-snapshot-binding/v1
principal.type, principal.id, principal.tenant_id,
execution_id, intent_digest,
payee.id, payee.registry_version, payee.display_name, payee.origin,
charge.minor, charge.currency, currency_table_version,
request_binding.route_id, request_binding.route_version,
request_binding.resource_ref, request_binding.terms_digest,
payment_profile.alias, payment_profile.version,
shipping_profile-present, [shipping_profile.alias, shipping_profile.version],
provider.id, provider.adapter_version, provider.account_ref,
execution_class, capabilities_digest, expires_at_ms
```

The `terms_digest` binds a route-specific, versioned canonical request template including destination, method, body, purchase/order identity, item quantities, fulfillment version and final exact all-in total. The backend publishes test vectors for that protocol encoding. It is never a hash of untrusted prose describing an action. Capability digest uses the same field-vector framing over `schema,provider_id,adapter_version`, sorted action/class sets, observation/replay fields, observed/valid-until timestamps and constraints ordered by currency/region. Include every declared constraint and distinguish unknown from empty. New fields or changed encoding require a new binding version; an adapter cannot silently change the vector. Golden vectors in two runtimes are a phase-0 gate.

An authorization binds an execution snapshot, not a broad amount cap. No post-approval edit to the payee, currency, quote, shipping profile, provider account, execution class or request payload is permitted, even if the new amount remains below the original cap. Prepare a new request and obtain a new approval after safely closing the old unsubmitted intent. Intent IDs and submission history are never reused.

## Authorization and execution handoff

There is one policy decision callback in the host. It receives authenticated identity plus the immutable snapshot and returns the existing Ability policy-decision envelope. Domain invariants cannot be overridden by an `allow` result. No callback supplied by the model can execute in the privileged runtime.

For human-authorized V1, the private execute operation's host policy requires approval. Do not mint a grant from provider `approved` alone unless the registered trusted issuer has independently verified the approving account, approval event and exact terms. Link's UI may serve as the human presentation channel only where its signed/authenticated observation and local account association meet this requirement. Otherwise collect a separate trusted application approval; avoiding duplicate UX is secondary to verified authority. Future enterprise grants can use the same Ability approval issuer interface without claiming to be human actions.

Approval storage fields are the existing Ability approval object plus issuer trust/version, subject/tenant and immutable execution association. A hash match is not authentication. The consume callback compares the stored issued object (including nonce, expiry and approver), verifies issuer authority and policy version, and atomically reserves the corresponding execution. A forged identical-looking approval object is rejected if no issued record exists. Nonces are unique within an issuer namespace; IDs are unique across the reference service.

Reference sequence:

1. Gateway records intent, request-key mapping and a durable work item; returns accepted ID. No provider call is needed for intake to finish.
2. A bounded worker prepares and requests native approval. Preparation has its own durable operation record to detect uncertain issuance and avoid duplicate notifications.
3. Trusted authorization issuer records the exact execute invocation and grant. Optional Dispatch/Leash notifications only carry opaque IDs.
4. Worker invokes the private Ability execute operation. Its durable `begin_idempotency` hook owns the invocation. Its `consume_approval` callback uses `BEGIN IMMEDIATE` to consume grant and compare-and-set execution from ready to executing with the permanent financial claim.
5. Only this callback's **successful in-memory return in the same worker invocation** grants a one-use dispatch permit. A stored claim ID, outbox item, duplicate callback, recovered process or resumed workflow cannot reconstruct a permit. The handler consumes that permit once and makes one charge-bearing dispatch with retries disabled.
6. Observation/outcome persistence follows. If killed anywhere after the claim, recovery only observes. A crash before the actual send may leave zero charges and unresolved state; liveness is intentionally sacrificed.

Outbox rows schedule bounded nonfinancial jobs and sanitized evidence delivery. **A generic at-least-once outbox consumer must never send a payment simply because a submission row exists.** Financial dispatch requires winning the claim in this invocation. A lease release, timeout or worker restart cannot restore permission. When making a final no-effect determination, ensure the original worker is dead or its outbound authority has been revoked; otherwise a delayed original request could still arrive.

Policy revocation and cancellation serialize with the claim. If cancellation wins, no submit; if claim wins, the UI reports in-flight. Pre-send expiry and provider-enforced expiry are both checked. There is inevitably a boundary between local admission and remote processing; native scoped controls must enforce amount, recipient and deadline at the processor where available. No wording claims local revocation retroactively undoes an admitted financial action.

## Observation, reconciliation and receipts

`Observation.phase` is `authorization|execution`. Legal outcomes are:

| Phase | Allowed outcomes | Required evidence / implication |
|---|---|---|
| authorization | pending, authorized, denied, expired, unknown | Correlated provider authorization observation, or explicit not-required status under the trusted policy. Never a payment receipt. |
| execution | pending, succeeded, failed_no_effect, unknown | After claim only. Success/no-effect require authoritative transaction/recipient correlation; unknown stays unresolved. |

`next_action` is null or `{kind:human_action|operator_review,action_ref}`. No raw provider action URL, HTML, reason string, credential or response body may escape. `actual_amount` is required for `succeeded`, and must equal the exact approved charge. `evidence_ref` is required for every conclusive outcome. A `failed_no_effect` observation must also establish no remaining processor/worker authority capable of later charging. A missing transaction, expired token, cancelled SpendRequest or empty history page alone cannot establish that.

Define V1 `succeeded` as **provider-confirmed completed purchase charge according to the installed route's confirmation rule**, not token issuance, an authorization hold, mere bank acceptance or irreversible settlement. Pending captures and accepted bank instructions stay executing. Financial success does not assert goods delivered, fulfilled or beyond dispute. Receipt evidence records the confirmation rule and evidence version. A later refund/chargeback is an independent annotation, not a reversal to ready. Providers that cannot support this conclusion are not enabled for live V1.

Reconciliation cannot promise eventual resolution if a provider disappears. It provides a stable execution ID, bounded observations, retained evidence and operator escalation. Manual reconciliation may annotate an unresolved case; only authenticated evidence satisfying the same route rule can close it conclusively. Amount/time fuzzy matching and a human checkbox are not settlement proof. No reconciliation action can mint a replacement credential or reset the claim.

Provider idempotency retention is separate from local tombstone retention. Reference V1 retains execution IDs, business purchase-reference digests and submission claims indefinitely unless an operator performs an explicit export/migration preserving replay protection. Financial PII retention is configurable and can be removed while these minimal identities remain. Restored databases enter observe-only mode; a stale backup must never recreate live authority.

## Data classifications and bounded data

| Class | Fields/examples | Default recipients and retention |
|---|---|---|
| Public operational | Schema/version, supported action names, generic error enum, static adapter version | Documentation or operator-approved public capability summary. No account eligibility/limits by default. |
| Tenant-sensitive | Amount, payee, SKU, order history, aliases, purchase/execution IDs, account eligibility, evidence | Authenticated task owner and narrowly scoped operator. Default application policy; no global telemetry. |
| Private personal | Email, shipping/billing address, payment brand/last four, provider payment-method IDs | Trusted application/provider only. Omit from agent schema and generic receipts. |
| Secret | PAN/CVC, OAuth access/refresh, SPT/LPT, signing keys, bank credentials, usable redirect/session tokens | Privileged executor or trusted human provider surface only; no generic state/log/snapshot. |

Core returns server-generated identifiers, fixed enums and approved normalized amounts; it does not pass arbitrary provider strings through just because they fit a string schema. Provider evidence references are mapped to fresh local opaque IDs. Authorization/receipt objects are private even where their schema is public. Human intent purpose is bound but not echoed into diagnostics. Detailed evidence is fetched through an authenticated operator endpoint with explicit authorization, not a bearer file URL.

Object limits: IDs 1–128 ASCII characters, adapter IDs 1–64, purpose 1–500 UTF-8 characters with an additional 2 KiB byte limit, 50 item rows, positive integer quantities ≤1,000,000, 100 evidence refs per page, 32 KiB request body, 64 KiB normalized provider response, 1 MiB bounded private evidence page only when a route explicitly requires it. Unknown fields and enum values fail closed. Page cursors are bounded authenticated references. These are initial configurable implementation resource limits, not provider financial limits; changing a stable wire maximum requires explicit compatibility review.

## Corrections to the September 10 review

| Prior assumption | Current correction | Architectural result |
|---|---|---|
| Link creation has no general idempotency-key field | Current source `CreateSpendRequestParams.idempotency_key` and serialized create body exist. | Use stable issuance key; still require server retention/conflict proof and a separate financial claim. |
| One keyed request/status facade is the minimum | Reusing a keyed status call can cache pending state and declares read as write. | Two small tools, keyed request and intrinsic status; no model-visible executor or approval objects. |
| Payments can use Ability's canonical v2 helper as a public utility | Generic canonical helpers are in private `src/internal.kujo`. | Keep public Ability approval semantics unchanged; use explicit domain field-vector hashes and golden vectors. |
| Local pre-execution check alone prevents checkout races | Merchant terms can mutate after that read. | Require immutable resource/conditional version plus native financial constraints; reject unsupported routes. |
| A durable claim/outbox alone grants send authority | Recovered outbox consumers can resend if they treat stored claims as permits. | One winner obtains an ephemeral one-use dispatch permit; no permit reconstruction after crash. |
| Exit zero from `kujo run` means test blocks ran | Test-block files require `test-run`. | Record corrected tests with actual test counts; entrypoint assertion scripts still use `run`. |

None of these corrections requires starting a Payments implementation or modifying existing ecosystem primitives.

## Gateway replay identity

Agents SDK checks returned receipt invocation identity (`agents-sdk/src/agents/abilities/contract.kujo:76`), whereas Ability keyed replay returns the original stored receipt (`ability/src/runtime.kujo:203`). The gateway must assign and durably reuse a server-minted invocation ID for each authenticated `(principal type, principal ID, tenant, operation, idempotency key)` before calling Ability. A changed payload with the same key conflicts. Concurrent request intake resolves to that same record. Never invent a new receipt identity after replay. Status uses a fresh intrinsic read invocation and does not replay the original pending request summary. Add a gateway replay fixture before exposing the tools; no SDK change is required.

Capability vector is frozen in this order (booleans use `true`/`false`, null uses a presence field `0`; present uses `1` then value; counted arrays use a decimal count followed by elements):

```text
kujo.payment-capabilities-binding/v1,
schema, provider_id, adapter_version,
actions-count, [actions sorted], classes-count, [execution_classes sorted],
observed_at_ms, valid_until_ms,
observation_support.authorization, observation_support.execution,
replay_protection.strategy, retention-present, [retention_ms],
currencies-present, [count, sorted currencies],
regions-present, [count, sorted regions],
amount_limits-count, [currency, minimum-present, [minimum_minor], maximum-present, [maximum_minor]] sorted by currency,
authorization_required-present, [authorization_required],
credential_expiry-present, [credential_expires_at_ms],
available-present, [available]
```

Reject duplicate set members and duplicate currency-limit entries before encoding. Unknown availability or unsupported currency/region prevents execution; unknown replay retention never grants permission to retry. The review's cross-runtime vectors prove the framing primitive; full intent, snapshot and capability object vectors remain a phase-0 implementation gate.
