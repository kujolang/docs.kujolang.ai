# Triple Win and universal usefulness

## Triple Win

The recommended boundary passes as a design, provided its costs remain visible and live promotion stays gated by evidence. It does not promise that every party gets every preferred workflow.

| Participant | Concrete gain | Tension or cost | Required protection / evidence |
|---|---|---|---|
| Creator/business | One execution record survives agent/framework changes; uncertain charges are visible. | Manual reconciliation costs time and can delay purchases. | Compact status plus explicit next action; never hide unresolved attempts as failures. |
| Developers/teams | One Ability surface and small SPI replace provider-shaped tool collections. | Isolation, storage and adapter conformance are real integration work. | Fixture-first quickstart, pinned versions, explicit dependency boundaries. |
| Merchants | Stable purchase reference and controlled retries reduce duplicate orders and abandonment. | Only registered machine routes initially qualify; no universal browser coverage. | Preserve merchant identity and transaction terms; do not bypass merchant authentication or anti-fraud controls. |
| Payment providers | Adapter respects native authorization and credential handling. | Normalization cannot guarantee identical provider features. | Fail unsupported capability; retain native status privately; no silent fallbacks or misleading parity. |
| Agent/harness developers | Agent receives two small tools and no payment credentials. | Agent cannot repair privileged state through arbitrary shell/browser commands. | Human/operator channel for recovery; no escape hatch that widens agent authority. |
| Open-source consumers | Core and fixture execution can run locally; provider additions need no proprietary Kujo service. | Provider credentials/accounts still require the chosen provider. | Publish schemas, conformance and migration rules under repo license; no hosted approval dependency. |
| End users | Approve identified merchant, exact amount and purpose on a trusted surface. | Approval fatigue and inability to instantly retry uncertain charges. | No prechecked payments or hidden repeat authority; explain why reconciliation blocks a repeat. |
| Infrastructure operators | Separate privileges, quotas and bounded jobs reduce blast radius. | Host/egress/backup/key custody remain operator duties. | Deployment acceptance suite, incident stop control and restore procedure. |
| Broader machine-commerce ecosystem | ACP/UCP/MPP/AP2 fit as integrations without making one vendor the core. | New primitive could fragment standards if it replaces their wire contracts. | Kujo is the application boundary, not a competing network protocol; adapters retain protocol compliance. |

The three wins are: control and portability for creators; less duplicated consequential-action logic for developers; open, adaptable contracts for the wider ecosystem. They fail if an adapter quietly exposes secrets, a consumer is forced onto Kujo cloud, merchant authenticity is guessed from a display name, or ambiguous charges are retried to improve apparent completion rates.

## Five-provider pressure test

A provider here is an **execution adapter**, potentially composing a wallet and merchant protocol. It is not assumed that one vendor both issues credentials and settles the purchase.

| Hypothetical provider | Fit to the same SPI and domain | Provider-specific content kept private | V1 / capability restriction |
|---|---|---|---|
| A: Link wallet + MPP Stripe merchant | Prepare verified merchant challenge; request Link approval; submit SPT once; observe SpendRequest/transaction plus merchant correlation. | SpendRequest ID, network/profile ID, SPT, OAuth session, API revision. | V1 reference candidate for approved machine routes. LPT/PAN unsupported. |
| B: Enterprise corporate-card platform | Prepare transaction; external enterprise policy issues one-use authorization; adapter submits through an API or a separately certified execution service. | Card credential, cost center/provider policy object. | Can fit without core changes if it offers isolated machine execution. Browser-only offering fails V1 capabilities. Preapproved budgets remain later scope. |
| C: Machine-payment protocol wallet | Prepare challenge; authority approves exact action; submit signed payment; observe settlement reference. | Network transaction encoding, signer, method payload, confirmation rule. | Fiat-denominated purchase/settlement adapter can fit V1; raw crypto intent units require a later explicit asset schema, not `USD=USDC`. No sessions/subscriptions. |
| D: Hosted wallet | Prepare route; external page obtains authorization; submit returns pending if user completion initiates funds; observe authoritative result. | Redirect state, provider account/session, signed callback. | Core lifecycle fits. Human page/redirect is the privileged execution surface; a return URL is not success evidence. No new core branch. |
| E: Bank payment | Prepare creditor and payment terms; authorization may require redirect; submit bank instruction once; observe accepted/pending/settled/rejected outcome. | Mandate, bank identifiers, bank transaction reference and rail-specific finality. | One-time purchase fits future adapter; long pending state supported. Standing mandate and transfer intents excluded. |

This is contract reasoning, not five completed integrations. Unsupported providers must be rejected rather than silently translating unsafe behavior. Universality means a stable domain and extension mechanism, not that V1 must execute every rail.

## Abstractions kept and deleted

Keep intent, execution snapshot, durable financial state, provider capabilities and typed observations. They protect boundaries demonstrated by multiple provider shapes. Represent PaymentAuthorization as a projection/reference to Ability approval plus authenticated provider evidence; do not create a second human approval engine.

Delete separate `validate_intent` provider hook (core validates semantics; prepare checks support), `authorization_status` and `inspect_execution` (one stage-aware observe call), provider-owned `sanitize_receipt` (core allowlist controls egress), a global provider registry, and eighteen integration modules. No recurring/refund/transfer flags appear in V1's supported action set.

Keep three execution classes with precise exposure meaning: `machine`, `provider_hosted`, `browser_injection`. Do not rank them as universal security scores. Tokenization and protocol names are orthogonal: both a machine request and DOM insertion can use a token. V1 allows only `machine`; later certified provider-hosted routes use the same state machine. Unknown execution classes fail closed until explicitly versioned and supported.

## Competing architectures and participant tradeoffs

These alternatives were considered against the same participant set. “Mitigation” explains whether the option can be repaired without becoming the recommended architecture. The selected thin boundary is evaluated in the first matrix above.

### Option A: wrap Link CLI/MCP directly in the agent

| Participant | Win | Risk | Mitigation / decision |
|---|---|---|---|
| Authorizing user | Broad web checkout coverage quickly | Issued PAN/SPT/LPT and OAuth authority become reachable to an agent; approval and payment status can be confused | A separate executor and normalized receipt are required, which abandons this option. Reject. |
| Agent developer | Little initial integration code | Vendor-shaped tool proliferation, shell and failure handling per harness | A narrow gateway removes much of the initial shortcut. Reject for a primitive. |
| Merchant | Access to more buyers | Agent retry and checkout mutation can duplicate or misdirect purchase | Stable route binding and financial journal required. |
| Payment provider | Immediate use of supported CLI | Hosted session reachable by arbitrary agent tools; accidental credential disclosure | Privileged adapter custody, not general MCP exposure. |
| Kujo integrator | Familiar shell entrypoint | CLI upgrades change semantics and output | Pin and normalize privately; public wrapper remains the wrong boundary. |
| Open-source ecosystem | Small usable sample | Link lock-in and no portable buyer contract | Keep such a sample explicitly vendor-specific, not Kujo Payments. |
| Infrastructure operator | Few services initially | Same-UID credentials and unauthenticated local service reachability | Physical split is unavoidable under the declared attacker model. |

### Option B: extend Commerce to own payer authority

| Participant | Win | Risk | Mitigation / decision |
|---|---|---|---|
| Authorizing user | One application for shopping and paying | Buyer credentials can be colocated with seller infrastructure and permissions | Split buyer authority into independent boundary; reject combined domain. |
| Agent developer | Reuse existing provider names | Hosted `link` now means both purchase URL and wallet; confusing capability contracts | Separate buyer provider registry required. |
| Merchant | Existing checkout schemas | Seller package takes on buyer execution lifecycle and liabilities | Keep Commerce interoperable through protocols, no buyer vault. |
| Payment provider | Existing seller adapters | Merchant API keys and consumer OAuth become one overloaded provider interface | Distinct roles/account identities; do not reuse adapter contract. |
| Kujo integrator | Fewer repo names | Larger dependency graph and runtime coupling between JS storefronts and Kujo executors | Share exact-money test vectors only; no common package until two strict consumers need it. |
| Open-source ecosystem | One package to discover | Seller-only users inherit payer complexity | Optional external composition gives the benefit without the cost. |
| Infrastructure operator | Potential shared deployment | Seller compromise reaches payer authority | Separate processes/accounts required; bundling does not remove operational work. |

### Option C: new self-contained payment platform

| Participant | Win | Risk | Mitigation / decision |
|---|---|---|---|
| Authorizing user | Integrated policies/history/budgets | More financial data collected, potential lock-in | Remove history, standing budgets and hosted requirement for V1. |
| Agent developer | One vendor-specific all-in-one SDK | New workflow, approval and receipt formats duplicate Ability/Dispatch | Reuse existing contracts instead of parallel machinery. |
| Merchant | Many promised integrations | Generalized carts/order/refund models flatten merchant semantics | Keep payment execution narrow and fulfillment external. |
| Payment provider | Broad capability surface | Lowest-common-denominator semantics or speculative parity claims | Explicit capabilities and unsupported-route outcomes. |
| Kujo integrator | Turnkey-looking feature set | Must maintain financial workflow engine and policy language | Thin state machine plus injected host policy. |
| Open-source ecosystem | Large feature inventory | Fragmentation of Ability and open commerce standards | Do not create a competing network protocol. |
| Infrastructure operator | Central control plane | Mandatory service, retention and accounting burden | Local journal and independently replaceable service components. |

Option C becomes acceptable only after removing those responsibilities; the resulting design is the recommended thin Payments boundary. A fourth option, **do nothing**, is appropriate for a single trusted one-off payment script. It becomes costly when multiple harnesses need the same approval binding, uncertainty handling and credential boundary. Phase 1 must demonstrate those shared obligations before committing to a broad product launch.

## Clarity, Context and Control acceptance

Clarity: an accepted request is distinct from a completed charge; two small tools expose those meanings. Context: a receipt points to the immutable merchant, exact terms and evidence under tenant access checks. Control: a user can deny, expire or cancel before admission, an operator can stop new claims, and no retry silently spends again. Merchant and provider rights to refuse payment remain intact. Tradeoffs—manual reconciliation, limited initial merchant coverage and deployment work—are explicit product costs, not hidden losses transferred to other participants.
