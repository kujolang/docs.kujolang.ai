# Verification, conformance and final gate

## Executed verification

This review ran existing tests and a deliberately small executable design model. It did not implement a provider, certify physical isolation, run real-money transactions, or claim complete repository security coverage.

| Check | Result / evidence |
|---|---|
| Ability contract/runtime, cross-language SDK, registry and devkit suite | PASS; [ability-tests.log](evidence/ability-tests.log). The suite uses interpreter paths and includes VM fallback diagnostics in SDK parity; exit 0 does not certify every VM path. |
| Commerce `npm run validate` | PASS, 52 tests plus syntax/security patterns; [commerce-tests.log](evidence/commerce-tests.log). |
| Agents SDK Ability contracts | PASS, 7 tests; [agents-ability.log](evidence/agents-ability.log). |
| Agents SDK approval policy | PASS, 19 tests; [agents-approval.log](evidence/agents-approval.log). |
| Dispatch policy precedence | PASS, 3 tests; [dispatch-policy.log](evidence/dispatch-policy.log). |
| Dispatch SQLite revision/persistence | PASS, 1 test with `DISPATCH_STATE_BACKEND=sqlite`; [dispatch-sqlite-configured.log](evidence/dispatch-sqlite-configured.log). Initial default-filesystem attempt failed; retained diagnostic records explain the correction. |
| Workcell Podman security policy | PASS; [workcell-policy.log](evidence/workcell-policy.log). Uses fake Podman response, **not actual containment or breakout testing**. |
| MCP Ability gateway | PASS with `kujo run tests/test_09_ability_gateway.kujo --interpreter`; [mcp-gateway-corrected.log](evidence/mcp-gateway-corrected.log). Initial test-run command was incorrect for this assertion-script fixture. |
| AI Chat journal | PASS, 7 tests using installed Node 22.17.0; [ai-chat-journal-node22.log](evidence/ai-chat-journal-node22.log). Node 24 attempt failed due to native ABI mismatch; dependencies were not rebuilt or changed. |
| Proposed Ability JSON schemas and request branches | PASS in Kujo VM; [proposed-contracts-corrected.log](evidence/proposed-contracts-corrected.log). First draft used unsupported `not`; changed to closed `oneOf` branches. This is evidence-driven contract simplification, not a runtime modification. |
| Independent SQLite design model | PASS, 9 tests with parameterized crashes/field mutations; [proof-model.log](evidence/proof-model.log). 64 competing claims yield one winner; process death before/after fake charge never permits a second claim. |

The proof model uses Python standard library solely as an independent review fixture. It establishes behavior of its SQLite transaction and modeled state transitions, **not behavior of an unbuilt Kujo Payments implementation**. Sentinel checks exercise its fixed projection only; they do not test every ecosystem log sink. Full fault/isolation/conformance tests below remain implementation acceptance requirements.

Commands can be reproduced from the named repository roots. Proposed fixture checks:

```sh
python3 fixtures/proof_model.py
PAYMENT_REVIEW_ROOT="$PWD" PAYMENT_ABILITY_ROOT="/path/to/ability" kujo run fixtures/validate_contracts.kujo
python3 fixtures/check_package.py /path/to/kujo-repos /path/to/pinned-link-cli
```

The review was produced in an isolated docs repository worktree; existing product source and user changes were preserved. Documentation-site build is unnecessary because no site content/template/build input changed; this package is under release-audits. Package verification checks JSON, coverage, source citations/hashes and local links.

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

The concrete model surface has one function; the SPI has five mandatory methods plus optional cancel, and internal Ability operations remain hidden. [interface-budget.json](evidence/interface-budget.json) records compact UTF-8 byte counts for the proposed tool, two example internal definitions and a status summary. These are reproducible bytes, not provider-exact token billing. No unbuilt-system latency or throughput number is claimed.

Proposed acceptance budgets: model tool schema at most 2 KiB compact JSON; common status summary at most 512 bytes; intake returns within 2 seconds under local fixture load; no invocation waits for human approval. Measure p50/p95 at concurrency 1/16/64, query count and provider request count; make thresholds explicit in Eval. Detailed receipts use authenticated references. A provider operation has a deadline and output limit (suggested 10s/64KiB, configured per route), no unbounded subprocess/stdout capture and no repeated model polling. Cache capabilities to their declared expiry, then revalidate before dispatch. Batch safe observation work; never batch speculative payments to save latency.

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
| 10 | Duplicate financial action protected? | **YES** under durable-store/worker assumptions — pre-send permanent claim, no automatic resend, purchase uniqueness; 64-claim/crash model passes. Not a guarantee against provider fraud. |
| 11 | Ambiguous outcome reconcilable? | **YES** as explicit durable state and evidence workflow. Provider outage may prevent eventual resolution; no guessed result or forced retry. |
| 12 | Provider limits runtime constraints? | **YES** — dated per-profile capability data, separate from action semantics. |
| 13 | Smaller model interface? | **YES** — one measured compact facade instead of SPI, wallet command set and internal execution operations. |
| 14 | CI proves behavior without money? | **YES** for contracts and implemented fixture behavior; proof model and existing offline suites demonstrate the method. Live-provider guarantees need sandbox/live evidence. |
| 15 | No proprietary Kujo service? | **YES** — local fixture, embedded trusted use and self-hosted executor; no mandatory hosted Ability Gateway. |
| 16 | Readiness claims scoped? | **YES** — code facts, proposed controls, fixture tests, provider claims and deployment responsibilities separated. No PCI or production certification. |
| 17 | Simpler than repeated provider integration? | **YES** for multiple consumers/providers, an architectural judgment supported by shared approval/journal/projection logic. For a single trusted script it adds overhead; use fixture phase to measure that cost. |
| 18 | Long-lived primitive? | **YES** with this narrow boundary — payment intent and uncertain financial outcomes survive Link replacement; raw credential brokerage alone would fail this gate. |

Recommendation: **PROCEED WITH ARCHITECTURE CHANGES** through fixture implementation. Link promotion is blocked until actual merchant binding, outcome correlation and deployment isolation evidence pass. That limitation is architecturally resolved by refusing unsupported routes and retaining unknown state, rather than pretending every provider can be made safe by normalization.
