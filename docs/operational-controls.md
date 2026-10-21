# Operational Controls

Load only the section needed for the current event. Apply the core
[proportionate-design rule](../GOVERNANCE.md#proportionate-design-and-sufficient-verification)
directly; this guide is not an intake checklist or an extra approval gate.

## 1. State and evidence boundaries

Keep portable rules, local task state and authoritative evidence distinct.
Portable guidance contains transferable contracts and procedures. Host/user
identities, resolved paths, credentials, resource assignments and current results
stay local with their scope and date. An old run record grants no new authority.

Use existing task records and storage. One canonical owner holds each rule or
state; other documents link to it. Template fields describe possible needs, not
a requirement to create every record for every task. Campaign-specific numbers
come from user control, statistical design, resource capacity or a real acceptance
contract, not copied examples.

## 2. Goal, experiment, and diagnostic lineage

Bind each research question to the outcome and a decision it can change in the
[campaign](../templates/campaign.yaml) and
[experiment card](../templates/experiment.yaml). Record predecessor, material
novelty and relevant evaluation identity. Diagnostics remain subordinate to the
parent objective; a local metric or convenient component cannot replace it.

When diagnostics could displace outcome work, give their chain a budget and
integration condition. Outcome-bearing negatives and underpowered results count;
pre-outcome infrastructure/invalid-method failures neither count nor reset it.
At the limit, integrate into an outcome comparison, retire the exact path, or
obtain an authorized goal change. Renaming a task does not reset the limit.

Selected outputs are joint consequences of inputs, representation, search,
resource budget and evaluation. Inspect independently sampled inputs before
using selected failures to explain opportunity absence or a search defect. Trace
what the implementation can represent and reach. Separate data/collection bias
from design faults, then make one coordinated causal repair.

## 3. Creation and delivery

[Communication and liveness](communication-liveness.md) owns participant binding,
creation reconciliation, direct delivery and management handoff. Use its existing
records instead of another message protocol. A queued ID or transport timeout is
not proof of creation failure; inspect before retrying. Read access and incoming
messages do not grant sending or task-creation authority.

## 4. Readiness and complete experiments

Review the implementation diff before costly validation. Consolidate checks that
could invalidate the result: input, intervention activation, comparison, outcome
writer, resources and relevant recovery behavior. Reuse passing evidence. Close
concrete findings with focused checks; further review needs new evidence and a
named decision. Routine repairs within the lease proceed autonomously.

A complete experiment is the smallest valid path from authoritative inputs,
through the intended intervention, to analyzable outcomes. Completeness refers
to the causal path, not maximum statistical scale. Freeze a falsifiable hypothesis
and one coordinated change; run, inspect activation, missingness, denominators,
uncertainty, guardrails and cost; then keep, revert, repair, pivot or scale.

Wrong inputs/evaluator, leakage, corruption, unapplied intervention, unrecoverable
outcomes or a concrete safety/resource failure may block their affected scope.
Style, optional refactors, descriptive hashes and reconstructible metadata do not
block by themselves. Required identity/security checks remain binding. Do not
invent provenance or bypass a real cache miss to claim compatibility.

Documentation changes use content, links, portability and applicable hygiene
checks. A new revision or formatting change alone does not justify a campaign.
After a narrow fix, rerun failing and directly affected checks. Preserve unrelated
passing evidence and disclose unresolved failures.

## 5. Recovery and semantic compatibility

Distinguish calculation completion, durable commit, selection/transition and
next-stage dispatch. Find the failed boundary before choosing recovery. A writer
or transition failure with authoritative surviving outputs calls for a boundary
repair; it does not automatically invalidate prior calculations.

Resume through the native contract and preserve completed stages and compatible
partial output. Verify that the new execution consumes restored work and advances
new work. Existing files, a loaded revision or a reset initialization counter
alone proves neither reuse nor loss. Successful continuation before an affected
boundary does not prove that the later boundary has passed.

Reconstruct persisted subjects at the canonical owner. Preserve explicitly
frozen values and distinguish absence of an optional historical field from a
conflicting value. A search projection need not include all immutable subject
fields. Cache validity follows actual computation dependencies; unrelated
scheduling, metadata or downstream presentation changes do not invalidate
upstream results. Judge compatibility by correct usable results, not byte identity.

Only a relevant semantic change invalidates its dependent evidence. Preserve the
rest and state the bridge or limitation for comparisons. Healthy expensive work
continues through reconstructible audit debt. Never repeat valid compute merely
to improve optional metadata, hashes or reporting.

## 6. Measurement and claim boundaries

Separate source acceptance, delivery, deployment, actual runtime adoption,
recovery/new progress, performance and the requested domain outcome. They require
evidence at different boundaries. A successful component, technical exit,
intermediate score or retained candidate does not establish final acceptance.

For performance, separate startup/cold preparation, uncached computation, durable
commit, selection/transition and next dispatch. State work units, cache state,
concurrency, revision, interval and baseline. Reuse throughput is not new-work
throughput. A sub-operation or single-stage gain cannot prove whole-run speedup.
Reuse an adequate baseline; an unavailable comparison limits the claim rather
than authorizing an extra benchmark or restart.

Attribute resource measurements to owner and interval. Distinguish process memory,
shared attribution and swap from host totals, peaks, cumulative counters and
other jobs. Cold allocation or worker turnover is not automatically a leak.
Zero local swap does not prove absence of host pressure. Missing ownership or
measurement stays unknown; do not manufacture zeroes or success.

A domain outcome states its actual sample, denominator, period, costs and relevant
risk basis. Do not combine incomparable samples or promote intermediate selection
into final outcome evidence. Leave the overall objective open while any required
outcome is unmeasured or unresolved.

## 7. Statistical scale and validation

Before an efficacy claim or confirmation-scale allocation, freeze the relevant
claim/tier, population, independent unit, baseline/intervention, metrics,
guardrails, meaningful effect, uncertainty, stopping rule and cost ceiling.
Use the existing [experiment record](../templates/experiment.yaml) when useful;
nonapplicable fields need not become a new framework for engineering checks.

Account for clustering, autocorrelation, repeated observations, shared anchors,
selection and missingness. Rows and execution batches are not automatically
independent replicates. Register sequential looks and pooling rules when needed;
track cumulative exposure across renamed tasks and retries. Underpowered evidence
can inform a narrower decision but cannot claim powered success or impossibility.

Material method changes limit affected pooling; unrelated evidence remains valid.
Invalid/quarantined results retain their reason and cost. Independent review
returns `valid_for_claim`, `valid_for_narrower_claim`, `screen_only`,
`method_revision_required`, `invalid_for_claim` or `unresolved`. A narrower valid
claim does not authorize the original scale-up.

## 8. Progress and intervention

Distinguish experiment/replication results and portfolio decisions from enabling
fixes, audits and blockers. Link a fix to the work it unblocks. Follow relevant
outcomes, costs, invalid work and time to next evidence; do not collect every
possible governance metric.

Intervene when plans, reviews or scaffolding repeatedly displace the requested
outcome, or ready work loses its owner. Correct the smallest affected boundary;
reallocate or replace ownership only within authority. Governance activity is not
scientific progress, but an authorized documentation task completes with its
requested documentation and checks, not an unrelated experiment.

## 9. Lifecycle and resources

Keep a next owner/action/wake for active or queued work. Transport idle does not
mean a task failed. Reuse a coherent conversation; rotate only for a concrete
independence, isolation or recovery need and authorized successor. Transfer one
lease without duplicate writers or full transcript replay.

Bound concurrency by actual user, CPU, memory, storage and I/O limits. Account
for nested workers and numerical threads. Available hardware grants no scope.
Isolate conflicting writers; share immutable inputs and compatible caches through
their established locking contract. Preserve healthy jobs and foreign dirty work.

One human gateway handles campaign decisions without suppressing direct user
instructions or required tool approvals. Ask only for a missing external decision;
prepare what is already reviewable and continue independent work. Silence is not
approval, and a scoped blocker is not a campaign-wide stop.

## 10. Finalization and cleanup

Report the objective, supported result, limits, relevant tested/delivered revision,
remaining work and next owner. Keep implementation, runtime and outcome claims
separate. Report decision-relevant deltas, not concatenated logs.

Preserve raw inputs, models, durable evidence, valid caches, resume state and
foreign/unmerged work. Clean only explicitly authorized disposable targets after
relevant ownership and active-use checks. Ignored, old or merged does not mean
safe to delete. Process control, file deletion and replacement launch are separate
permissions. Do not expand cleanup or recreate intentionally removed state.

Give recurring tasks their saved terminal disposition. Shortening a prompt
preserves schedule, status, target, model and notification settings. A pending
startup dependency does not itself pause a monitor; a historical stopped/deleted
monitor is not recreated. Stopping monitoring does not stop computation unless
also authorized. Use [the short watchdog prompt](../prompts/watchdog.md).
