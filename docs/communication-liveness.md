# Communication and Liveness

Load this guide only when creating or rotating a participant, sending across
tasks, completing bounded work, recovering context, or auditing campaign
liveness. It prevents stale task IDs, wrong-destination instructions, silent
completion, manager relay bottlenecks, and all-idle deadlock.

## 1. Minimal state

Keep four small durable objects in existing campaign state:

- a G1-owned versioned participant roster;
- a dependency and event-subscription map;
- an append-only event/delivery stream;
- one role-owned memory snapshot per durable participant.

Ordinary files are sufficient. Do not build a broker, presence service,
database, or scheduler merely to implement these records.

## 2. Participant roster

A stable logical `participant_id` is identity. A task or conversation ID is a
verified transport binding, never an identity remembered from prose. The
human-facing G0 supervisor initializes its own and the verified G1 binding; G1
is the normal writer thereafter. The G0 supervisor may append one superseding
repair version if G1 is unreachable or misbound.

Use [the roster template](../templates/participant-roster.yaml). Each entry
records:

- governance level and function;
- functional contribution role, professional lens, and bounded decision scope;
- current task/conversation IDs and binding/scope epochs;
- owned scope, status, capabilities, and contact topics;
- checkpoint, role-memory, inbox-cursor, and binding-readback refs.

Rules:

1. After creating or reusing a task, read product/task state back and verify the
   creation key, logical role, scope epoch, and transport IDs before binding it.
2. Append a new roster version for creation, rotation, replacement, retirement,
   or correction. Do not rewrite an old binding.
3. Revoke or supersede a stale binding before sending new executable work.
4. Persist the roster outside G1 conversation context.
5. Give G0 and G2 only their own binding plus contacts required by current
   dependencies, review, or discussion. G1 retains the full roster.
6. A participant that observes a mismatch reports it and rejects affected work;
   it does not guess the intended identity.

## 3. Resolve before send; verify before act

Every cross-task message uses [the event template](../templates/event.yaml) and
binds:

- stable message/event ID, campaign, sender, and logical recipients;
- destination transport IDs resolved from one roster version;
- scope epoch, event kind, content hash, and evidence refs;
- action or decision needed, response owner, subscribers, and close condition;
- whether a reply is required, its due condition, and the declared inquiry
  owner/route if that reply is not observed;
- delivery state.

Resolve recipients from the latest roster immediately before sending. Do not
copy an ID from an old transcript, checkpoint narrative, or peer message.

The receiver compares the logical recipient, destination ID, campaign, and scope
with its durable self-binding. On mismatch it MUST NOT execute, reinterpret, or
forward the payload. It records `rejected_wrong_destination` and sends one
routing-error event to the sender and roster owner without the sensitive
payload.

An ambiguous send requires destination read-back for the identical ID, scope,
and hash. A policy-permitted retry reuses the same tuple only after absence is
shown. Never send a blind third copy. An event seen at the wrong destination is
not absence.

## 4. Direct role communication

G1 owns goal control, directory state, portfolio, and leases; it is not the
mandatory transport for every message. Participants MAY communicate directly
when the subject is already inside both scopes:

- evidence or artifact availability;
- dependency readiness, invalidation, or blocker state;
- reproduction, critique, challenge, or bounded discussion;
- an implementation or experiment interface;
- handoff, resource release, or terminal contribution result;
- a routing or identity fault.

Direct communication cannot retask a peer, change its priority or lease, borrow
resources, alter model assignment or claim tier, or grant decision authority.
Send those effects to the declared decision owner. Copy G1 only when portfolio,
lease, resource, roster, validation, route, arbitration, or completion state
changes.

Use subscriptions instead of all-to-all broadcast. Independence still applies:
a blind reviewer does not receive proposer advocacy before its first-pass freeze.

## 5. Dependencies and terminal notification

Every lease or commission declares:

```yaml
dependencies:
  requires_event_ids: ["<event-id>"]
  produces_event_kinds: ["<kind>"]
subscribers:
  - participant_id: "<logical-id>"
    notify_on: "<completed | invalid | blocked | artifact_ready | resource_released>"
    reason: "<decision or dependency>"
completion_owner: "<participant-id>"
```

Before bounded work becomes idle, its owner MUST:

1. persist the result or bounded artifact;
2. classify outcome and resource state;
3. refresh role memory or the terminal output record;
4. send one terminal event to the commissioner, decision owner, and every
   subscriber whose condition fired;
5. include evidence refs, next owner/action, and wake condition;
6. record required deliveries as observed or explicitly ambiguous.

The event may go directly to dependent peers. It does not wait for G1 relay.
Receipt-only chatter is unnecessary for informational events. An event that
declares `response_required: true` follows the bounded response protocol below;
delivery read-back alone is not a substantive reply.

Work is computation-terminal but communication-incomplete while a required
terminal event is neither observed nor reconciled. This does not block unrelated
work, but the watchdog can repair it.

## 6. Liveness invariant

Every nonterminal campaign MUST retain at least one durable liveness edge:

- an active participant owns an authorized next action;
- an external or compute condition has a due/wake condition and target;
- a decision has one owner and close condition;
- a queued lane has a precise reopening event and subscriber;
- a required delivery is in bounded reconciliation.

Transport `idle` is healthy when such an edge exists. It is a fault when all
relevant tasks are idle and durable state has no executable owner, future wake,
pending condition, or terminal completion. It is also a fault when upstream work
completed but declared subscribers were not informed, or when a blocking
response obligation is overdue without an acknowledgement, progress, blocker,
or terminal event.

G2 checks its lane before ending a turn. G1 checks the campaign after each event
batch. A periodic G0 watchdog is an independent fallback, not a second manager.

## 7. Required replies and silence recovery

Questions, decisions, handoffs, and executable requests that cannot safely be
left unanswered set `response_required: true`. The sender also declares:

- an acknowledgement or first-response due condition proportional to the work;
- the next evidence/wake condition for intentionally quiet long work;
- one `inquiry_owner`, normally the commissioner, coordination group, or
  relevant functional/professional group owner;
- a compact escalation route drawn from the current roster.

A valid active response is an acknowledgement with current state and next
evidence condition, a progress/result event, a blocker or bounded decline, or a
routing rejection. Transport delivery, an idle status, or an old heartbeat is
not a response. There is no universal timeout: do not interrupt healthy work
inside its declared evidence window.

When a required response becomes overdue, the watchdog MUST NOT blindly resend
the original instruction or halt the campaign. It:

1. verifies the recipient binding, event cursor, declared quiet window, and any
   observable active work;
2. wakes the declared inquiry owner to ask the silent participant directly with
   one idempotent `inquiry_request` and a close condition;
3. wakes G1 if the inquiry owner is absent/unreachable, the response blocks
   several lanes, or one bounded inquiry also goes unanswered, so G1 can assign
   another coordinator, reroute, rotate, or replan the smallest affected edge;
4. wakes G0 only when G1 itself does not respond or requires repair/replacement.

The inquiry owner may be a manager, coordination group, or the corresponding
product, engineering, algorithm, data, mathematics, review, or other functional
group named in the roster. Only the dependent edge waits; unrelated authorized
work continues. Inquiry and escalation events contain no new task authority.

## 8. Watchdog wake routing

Each recurrence reads only its cursor, current roster identity/hash, compact G1
checkpoint, due/wake and required-response indexes, unobserved required
completions, and checkpoints for participants implicated by a trigger. It does
not poll full transcripts.

Choose the minimum sufficient target:

- wake **G2** when a registered dependency or due condition is satisfied and its
  existing lease already authorizes the next action;
- wake the declared **inquiry owner** when a required reply is overdue, so that
  the commissioner, coordination group, or functional owner actively asks the
  silent participant;
- wake **G1** for missing ownership, roster/routing repair, portfolio choice,
  resource reallocation, retry/pivot, repeated silence, missing inquiry owner,
  or completion-event reconciliation;
- wake **G0** for unreachable or repeatedly misbound G1, charter/authority
  change, manager repair or replacement, completion, or a true human decision;
- wake several participants only for independent already-owned actions or the
  declared subscribers of one event.

Do not wake anyone for healthy long work, correctly queued state, unchanged
evidence, or reassurance. A wake binds current roster identity, a stable wake ID
and hash, exact trigger, smallest action, evidence refs, and close condition. It
grants no new authority.

Cadence follows the tolerable silent gap, expected evidence windows, and cost of
stranded resources. A scheduler may run more often than work is due; unchanged
runs remain silent. Missing one recurrence does not invalidate healthy work.

Use [the watchdog prompt](../prompts/watchdog.md). If recurrence is unavailable,
run the same audit manually or on material events.

## 9. Role-owned memory and compaction

Every durable G0, G1, G2, reviewer, or long-lived contributor maintains
[one compact memory snapshot](../templates/role-memory.yaml). The role writes its
own snapshot; G1 does not reconstruct every role from transcripts.

Store identities and hashes, event cursor, applicable decisions, durable
findings and negative results, open questions, dependencies, contact slice,
commitments, artifact refs, next action, wake condition, and context-health
flags. Do not store private chain-of-thought, raw logs, or a transcript copy.

Role emphasis:

- G0: charter/authority versions, G1 audit and completion gaps;
- G1: roster, dependency map, portfolio decisions, and resources;
- G2: hypothesis/attempt map, evidence, experiment state, and dependencies;
- reviewer: frozen packet, examined evidence, objections, and disposition;
- bounded subagent: one returned artifact and terminal event, with no separate
  durable memory unless promoted to a G2 conversation.

Refresh at lease acceptance, around long external work, material results or
decisions, direct dependency messages, nonterminal turn end, and before expected
compaction or handoff. After restart, read only the self-binding/contact slice,
role memory, campaign digest, lease, checkpoint, post-cursor deltas, and
next-action artifacts. Full transcript replay requires one named conflict.

## 10. Failure repair table

| Failure | Minimum repair |
| --- | --- |
| wrong task/conversation ID in roster | quarantine binding, read product state, append corrected version, notify affected roles |
| instruction sent to wrong task | reject without action; resolve logical recipient and verified binding before one correct send |
| small task completes silently | persist result; send terminal event directly to commissioner, decision owner, and fired subscribers |
| required reply is overdue | verify binding/quiet window; wake the declared manager, coordination group, or functional inquiry owner to ask directly; escalate only the affected edge if silence persists |
| all tasks idle before terminal state | reconcile liveness edges; wake minimum authorized G2/G1/G0 set |
| G1 becomes a relay bottleneck | restore scoped direct subscriptions; send G1 only management deltas |
| peer message changes scope | reject scope change, route it to decision owner, retain valid evidence exchange |
| long context loses state | recover from role memory, checkpoint, cursor, and refs |
| roster is too large for runtime roles | keep full roster at G1; distribute versioned contact slices |

Repairs preserve autonomy and direct cooperation. They do not add a standing
approval layer.
