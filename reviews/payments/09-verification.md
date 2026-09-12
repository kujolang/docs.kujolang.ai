# Verification, conformance and final gate

## Executed verification

This revision re-ran source-backed offline suites and review fixtures. It did not implement Payments or access payment credentials. [Verification manifest](evidence/verification.json) records exact commands, runtime binary hash, test scope and logs. Initial `kujo run` invocations of Agents SDK/Dispatch test-block files exited zero without executing those tests; they were corrected to `test-run`, with the original non-test outputs retained. A tool exit code alone was not accepted as test evidence.

| Check | Current result and scope |
|---|---|
| Ability full repository test script | PASS — contracts/runtime, SDK cross-language, registry trust and devkit; [log](evidence/ability-tests.log) |
| Commerce validation | PASS — 52 tests plus syntax/security patterns; [log](evidence/commerce-tests.log) |
| Agents SDK Ability projection/gateway | PASS — 7 executed tests; [log](evidence/agents-tests.log) |
| MCP Ability gateway | PASS — entrypoint assertions; [log](evidence/mcp-tests.log) |
| Dispatch SQLite revisions | PASS — 1 executed test with SQLite configuration; [log](evidence/dispatch-state-tests.log) |
| Dispatch process lock contention | PASS — one winner, three timeouts; [log](evidence/dispatch-lock-tests.log) |
| Workcell schema compatibility | PASS — schema fixture only; [log](evidence/workcell-tests.log) |
| Lens bridge | PASS — 51 tests; [log](evidence/lens-tests.log). Does not establish a credential-safe browser. |
| Proposed contracts and field framing | PASS — five Ability definitions, seven domain schemas and six Python/Kujo UTF-8 binding vectors; [log](evidence/contracts-tests.log) |
| SQLite review model | PASS — 12 tests including 64 claims, 8 competing processes, cancellation, crashes and one-shot recovery; [log](evidence/proof-tests.log) |

The independent model's fake processor intentionally permits duplicate charges: a uniqueness constraint at the fake processor cannot conceal a replay bug. This proves the modeled admission rules under SQLite transaction assumptions, not the unbuilt payment executor. The sentinel test checks only the model's projection; the full security/sink matrix remains an implementation requirement. No hardware power-cut, filesystem durability or malicious host isolation proof is claimed.

Reproduce review checks from this package root:

```sh
python3 fixtures/proof_model.py
PAYMENT_REVIEW_ROOT="$PWD" PAYMENT_ABILITY_ROOT="/path/to/ability" /path/to/kujo run fixtures/validate_contracts.kujo
python3 fixtures/check_package.py /path/to/kujo-repos /path/to/pinned-link-cli
```

The documentation-site build is not applicable: these files live in `reviews/`, outside site content/templates. The package checker validates local links, source line references, JSON syntax, source hashes, document coverage and measured interface budgets. Historical September 10 results remain in the old package and are not represented as tests executed today.

## Required implementation test matrix

| Level | Cases and decisive assertions | Execution environment |
|---|---|---|
| Unit | Positive safe integers; reject float/bool/overflow/unknown currency; zero/three-decimal currency vectors; canonical digests; exact vs maximum; every legal/illegal transition. | Pure offline. |
| Contract | Each Ability definition validates against actual pinned runtime; strict unknown-field rejection; output shapes; unsupported schema versions/enums; approval authenticity and binding. | Offline Kujo + cross-language vectors. |
| Provider fixture | Link approved is not paid; missing token/status/correlation; duplicate-create response; unsupported LPT/PAN; all five provider shapes with supported/unsupported capability combinations. | Synthetic fixtures only. |
| Integration | Request persists then returns; duplicate request same ID; tenant-scoped inspect; Dispatch pauses/resumes by ID; SDK gateway callback and MCP projection; cancellation CAS. | Isolated local fixture service. |
| Security / approval | Wrong amount, merchant, currency, intent, principal, tenant, execution, provider/class, expiry, nonce and modified input; forged issuer; replay; revoke before claim. Every case stops before fake provider counter increments. | Offline hostile-input harness. |
| Concurrency | 64+ callers, multiple processes, duplicate keys with changed inputs, new keys for same purchase_ref, same nonce across executions, crash/stale lease competing workers. At most one charge-bearing submission. | Actual selected store and Kujo executor; not just Python model. |
| Fault injection | Kill before/after journal commit, before/after provider charge, before receipt, audit/write/disk-full failure, network loss, 5xx, timeout, malformed body, provider outage. Unknown never resubmits. | Separate fake processor persistence; externally controlled kill points. |
| Reconciliation | Exact ID matching, delayed/provider-missing evidence, wrong amount, partial outcome, conflicting/duplicate callbacks, retained tombstone, provider disappearance, restored stale DB. | Offline fixture provider; sandbox confirmation separately. |
| TOCTOU | Mutate merchant/domain/account, amount/currency, body/cart, quote version and shipping profile between approval and dispatch. Reject or obtain fresh authorization. | Offline adversarial merchant. |
| Secret leakage | Unique fake PAN/CVC/SPT/LPT/OAuth/refresh/API-secret canaries in success, denial, timeout, malformed response and thrown error. Search raw, escaped, URL/base64 and split-field representations across every produced artifact. Zero leaked canaries outside executor. | Closed fixture filesystem; no real credentials. |
| Runtime breakout | Agent attempts Link-state/env/process-env/temp/profile reads; privileged CLI, traversal/symlink/hardlink, mounts, loopback/internal services, engine sockets, DevTools and network escapes. All fail for supported deployment. | Actual Linux/OCI or selected OS-principal deployment. No simulation-based certification. |
| Logging/evidence | Ability, SDK, MCP, Dispatch, Watchdog, RunLedger, CaseFile, Workcell, Lens, stdout/stderr, exception/debug bundles and optional telemetry enabled/disabled. Test fields and bytes, not only regex names. | Synthetic sentinels plus all selected integrations. |
| Fence/supply chain | Forbidden cross-zone import, undeclared package, dynamic loading and privileged builtin are rejected; exact adapter checksum/version; installed test provider cannot register in live mode. | CI mutation tests. |
| E2E sandbox | Test-mode Link approval→SPT→registered test merchant→authoritative transaction observation; crash/timeout reconciliation; test credentials never cross boundary. | Provider sandbox, separately opt-in; normal CI need not access it. |
| Manual live | One exact authorized transaction and authoritative follow-up; operator stop/recovery; account/region/merchant/API versions recorded. | Separate explicit transaction authorization; never normal CI. |

## Performance and token footprint

The concrete model surface has two functions; the SPI has five mandatory methods plus optional cancel, and internal Ability operations remain hidden. [interface-budget.json](evidence/interface-budget.json) records compact UTF-8 byte counts for both proposed tools and a status summary. The combined schema is 1,361 UTF-8 bytes and the sample summary is 114 bytes. These are reproducible bytes, not provider-exact token billing. No unbuilt-system latency or throughput number is claimed.

Proposed acceptance budgets: combined model tool schemas at most 4 KiB compact JSON; common status summary at most 512 bytes; intake returns within 2 seconds under local fixture load; no invocation waits for human approval. Measure p50/p95 at concurrency 1/16/64, query count and provider request count; make thresholds explicit in Eval. Detailed receipts use authenticated references. A provider operation has a deadline and output limit (suggested 10s/64KiB, configured per route), no unbounded subprocess/stdout capture and no repeated model polling. Cache capabilities to their declared expiry, then revalidate before dispatch. Batch safe observation work; never batch speculative payments to save latency.

## Final review gate

YES below evaluates the **specified architecture**, with evidence and limits shown. It does not mean the corresponding production implementation exists. Important runtime gaps remain hard phase-exit gates; they are not waived by a YES. No architecture question remains unresolved before starting the bounded fixture implementation.

| # | Question | Answer and evidence |
|---|---|---|
| 1 | Triple Win? | **YES** — participant gains, costs and protections in [assessment](03-assessment.md); no gain depends on sacrificing another party's credentials or agency. |
| 2 | Useful beyond Link? | **YES** — five distinct provider mappings; credential issuance and execution are separated. |
| 3 | Another provider without core changes? | **YES** within supported semantics — SPI and capability intersection; incompatible currencies/classes fail explicitly until a versioned extension. |
| 4 | Reuses Ability? | **YES** — concrete definitions and existing approval/receipt hooks; schema checks pass. |
| 5 | Avoids workflow engine? | **YES** — domain state only; Dispatch optionally owns pause/resume and application workflow. |
| 6 | Avoids policy engine? | **YES** — injected host decision and issuer verification; no new policy language, standing budget or delegated authority engine. |
| 7 | Preserves Commerce seller side? | **YES** — existing hosted `link` and seller provider registry retained; no dependency cycle. |
| 8 | Agent operates without credentials? | **YES** by interface design — aliases and status only; all native tokens stay in executor. Full sink tests remain mandatory. |
| 9 | Physically enforceable isolation? | **YES**, conditional on separate principal/guest/service and enforced egress. Same-process or same-UID designs explicitly unsupported. Actual target breakout testing is not yet done. |
| 10 | Duplicate financial action protected? | **YES** under durable-store/worker assumptions — pre-send permanent claim, no automatic resend, purchase uniqueness; 64-claim/8-process/crash model passes. Not a guarantee against provider fraud. |
| 11 | Ambiguous outcome reconcilable? | **YES** as explicit durable state and evidence workflow. Provider outage may prevent eventual resolution; no guessed result or forced retry. |
| 12 | Provider limits runtime constraints? | **YES** — dated per-profile capability data, separate from action semantics. |
| 13 | Smaller model interface? | **YES** — two measured narrow tools instead of SPI, wallet command set and internal execution operations. |
| 14 | CI proves behavior without money? | **YES** for contracts and implemented fixture behavior; proof model and existing offline suites demonstrate the method. Live-provider guarantees need sandbox/live evidence. |
| 15 | No proprietary Kujo service? | **YES** — local fixture, embedded trusted use and self-hosted executor; no mandatory hosted Ability Gateway. |
| 16 | Readiness claims scoped? | **YES** — code facts, proposed controls, fixture tests, provider claims and deployment responsibilities separated. No PCI or production certification. |
| 17 | Simpler than repeated provider integration? | **YES** for multiple consumers/providers, an architectural judgment supported by shared approval/journal/projection logic. For a single trusted script it adds overhead; use fixture phase to measure that cost. |
| 18 | Long-lived primitive? | **YES** with this narrow boundary — payment intent and uncertain financial outcomes survive Link replacement; raw credential brokerage alone would fail this gate. |

Recommendation: **PROCEED WITH ARCHITECTURE CHANGES** through fixture implementation. Link promotion is blocked until actual merchant binding, outcome correlation and deployment isolation evidence pass. That limitation is architecturally resolved by refusing unsupported routes and retaining unknown state, rather than pretending every provider can be made safe by normalization.
