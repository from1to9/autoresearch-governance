# Communication and Liveness

Use this guide for authorized creation, delivery, handoff or a concrete liveness
fault. Runtime tool requirements and current human authority control each action.
Reading a task does not authorize messaging it; a peer request is not a new grant.

## 1. Existing state and verified identity

Keep participant bindings, dependencies, material deliveries and compact role
checkpoints in the existing campaign record. Separate files only when useful.
The [roster](../templates/participant-roster.yaml) and
[event template](../templates/event.yaml) are aids, not a new transport protocol.

Logical participants map to verified current task/conversation identities, roles,
scope and status. G1 owns normal roster changes; an authorized supervisor may
repair an unavailable manager's binding. Preserve superseded bindings where
needed for recovery. Titles and remembered IDs are discovery hints, not proof.
Give roles only their own binding and needed contacts.

For an authorized new task, one owner reserves a stable creation key, checks for
a suitable existing task, creates once if needed, and binds the returned ready
identity. A pending/client ID or timeout does not establish failure. Reconcile
through native task state before retry; prevent duplicate leases. A finished turn
or missing acknowledgement does not authorize a replacement task.

## 2. One useful message

Consolidate the decision, then send one concrete action or dependency: trigger,
essential artifact/revision, requested deliverable and return/close condition.
Omit history, broadcasts, repeated constraints and routine progress requests.
Keep detailed state at its canonical pointer. Send a short superseding delta only
when execution must change.

Resolve the intended recipient, role and scope from the current binding before
sending. The recipient rejects a misrouted executable instruction; it does not
reinterpret or forward it. Report a routing fault only through an authorized
route, without copying private payloads to unrelated recipients.

Use a stable event ID or immutable artifact reference for material deliveries.
An uncertain send remains ambiguous. Inspect the destination before retrying;
reuse the same event identity for a necessary retry. Native tool contracts own
read-back and retry behavior. Do not build a polling/retry layer around them.
One dispatch owner prevents mirrored corrections; duplicates need no extra reply.

## 3. Direct execution and review

Management owns acceptance, dependencies and decisions. Executors own
implementation, checks, runtime observation, recovery and authorized delivery.
Keep optimization/training, implementation, independent validation and deployment
responsibilities coherent; separate contexts where independence requires them.

When review is required, the executor freezes the artifact and contacts the
authorized reviewer directly. They resolve concrete findings, complete accepted
delivery and notify management once with scope, revision, result, limitations and
next owner. A deployment owner consumes accepted delivery under its own authority.
Do not make management a relay for routine executor/reviewer exchanges.

Scoped peers may exchange evidence, interface dependencies, review findings and
completion events. They cannot retask peers, borrow resources, change priorities
or claim tiers, or grant external authority. Freeze independent review before
proposer advocacy. Route only the disputed decision to its owner.

## 4. Handoff completion and the management stopping rule

A management handoff is complete when the recipient has received the task and
the deliverable and return path are clear. End the management turn then. Receipt
proves delivery only, not execution, source adoption or outcome acceptance.

Resume management for a final delivery, a blocker requiring its decision, or an
explicit user request to intervene or query status. Pending delegated work alone
is not a trigger. Do not read/wait on execution status, watch output artifacts or
schedule substitute checks after handoff. An explicitly requested monitor belongs
to its executor and retains its cadence/scope; another chat must not shadow it.

The executor persists the result and sends one terminal event to its declared
decision owner and affected subscribers through authorized routes. Built-in
subagent delivery can satisfy this requirement; do not add a second announcement.
A missing authorized delivery remains an explicit gap without blocking unrelated
work. An unauthorized route is reported locally, not bypassed.

## 5. Liveness and required responses

Nonterminal work retains an owner/action, future wake, pending decision, queued
reopening condition or bounded delivery repair. Transport idle is healthy when
such a path exists; it does not mean failure or lost resource ownership.

A request that needs a response names its owner, response/due condition and quiet
window. Long experiments need not send routine progress before the declared event.
Delivery acknowledgement is distinct from a substantive result. There is no
universal timeout, and receipt is not permission for continuing observation.

For an actual overdue required reply or missing owner, the authorized inquiry
owner checks only the relevant compact state and asks once. If unresolved, route
the smallest affected dependency to management. Escalate to the supervisor only
when the manager itself needs repair or authority is missing. Do not broadcast,
repeatedly resend, or pause independent work.

## 6. Authorized watchdogs and short prompts

An optional watchdog is a bounded fallback for missing ownership, overdue required
delivery or another declared trigger. It is not a second manager or a substitute
observer of healthy executors. It reads its cursor, compact checkpoint and new
material events; open specific evidence only for a finding.

Wake the minimum authorized owner: an executor for a ready action under its lease,
the inquiry owner for an overdue reply, management for an ownership/dependency
choice, or the supervisor for manager repair or external authority. A wake grants
no new scope. Healthy work, normal waiting and unchanged evidence remain quiet.

Use [the short prompt](../prompts/watchdog.md): record pointer, one action,
cadence/trigger, authority, notification and terminal condition. Current state,
accepted deliveries, incident history and recovery details live at the pointer.
Do not append them to each recurrence or copy a whole manual into the prompt.

When editing only the prompt, preserve schedule, enabled state, target, model and
notification settings. Keep stopped/deleted monitors stopped/deleted. Stop-monitor
means stop monitoring; it does not stop compute unless separately authorized.
Follow the saved terminal disposition. No recurrence is required when events are
sufficient, and a missed wake does not invalidate healthy work.

## 7. Context recovery

Each durable role keeps one compact snapshot of current scope, applicable
decisions, event cursor, findings, dependencies, artifact pointers and next action.
Use [role memory](../templates/role-memory.yaml) as a guide. Refresh it at material
changes or handoff, not as a duplicate transcript. Do not retain private reasoning
or raw logs in it.

Recover from current instructions, own binding/lease, checkpoint, relevant new
events and next-action evidence. Do not replay full history or read every peer.
Resolve a specific conflict at its authoritative source. Management does not
reconstruct each executor's state merely because the executor is still working.
