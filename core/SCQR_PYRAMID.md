# Shared operating specification

## 1. Core contract

The skill turns messy material into a decision-ready artifact:

```text
define the decision → write the Resolution → frame SCQR → build the pyramid
→ attach evidence → audit logic → recommend next actions
```

Use the minimum structure that supports the decision. Do not force every
output to have exactly three branches.

## 2. The frameworks

### SCR: compact communication

- **Situation**: the relevant shared context.
- **Complication**: the change, obstacle, risk, or gap.
- **Resolution**: the proposed answer or action.

Use SCR for a short status update, email, meeting intervention, or executive
summary. The listener should understand the issue and requested action quickly.

### SCQR: opening a full argument

- **Situation** establishes the common ground.
- **Complication** creates the tension or meaningful gap.
- **Question** states the decision or research question created by that gap.
- **Resolution** gives the answer, recommendation, or thesis claim.

SCQR is the opening frame. The Resolution must also serve as the top of the
pyramid, so the body proves or qualifies it rather than restarting the story.

### Pyramid Principle

Organize claims from top to bottom:

```text
Resolution
├── Branch A: reason / finding / workstream
│   └── evidence, example, implication
├── Branch B: reason / finding / workstream
│   └── evidence, example, implication
└── Branch C: reason / finding / workstream
    └── evidence, example, implication
```

Every item at a lower level must answer: “Which claim above does this support?”
If it supports none, remove it, move it, or label it as context.

### MECE

MECE is a quality check on a peer group:

- **Mutually exclusive**: avoid double-counting the same cause, claim, or task.
- **Collectively exhaustive**: cover the material dimensions needed for the
  decision, while preserving a deliberate scope boundary.

Do not treat “complete” as “include everything.” Prefer a named dimension such
as feasibility, value, and risk over a mixed list such as cost, Python, and user
dissatisfaction.

### Vertical logic

Check support up and down the tree:

```text
evidence → branch → Resolution
```

Ask whether the evidence actually establishes the branch and whether the
branches jointly support the Resolution. A popular tool, a high benchmark in a
different language, or an attractive anecdote may be relevant context without
being evidence for the stated claim.

### Horizontal logic

Check peer branches for:

- one shared classification dimension;
- comparable level of abstraction;
- no overlap;
- no material omission within the declared scope;
- a useful order: causal, temporal, priority, or decision sequence.

### Six-step problem solving

1. **Define** the problem, constraints, success criteria, and time horizon.
2. **Decompose** it into a logic tree, causal tree, or workstreams.
3. **Prioritize** controllable, high-impact, evidence-accessible levers.
4. **Plan** owners, inputs, tasks, outputs, completion conditions, and risks.
5. **Analyze** quantitative and qualitative evidence, including failure cases.
6. **Synthesize** findings into an appropriately qualified recommendation.

## 3. Evidence discipline

Use these labels when the source material is incomplete:

| Label | Meaning |
|---|---|
| Fact | Directly stated or observed in the supplied material. |
| Inference | Reasoned interpretation; show the bridge. |
| Assumption | Needed for planning but not verified. |
| Recommendation | Proposed action, not a result. |
| Hypothesis | Testable claim awaiting validation. |
| Proposed method | Future design, not completed implementation. |
| `?` / `待確認` | Material detail unavailable or unverified. |

For academic content, never turn an offline proxy into a human study, a
proposed experiment into completed evidence, or a single metric into a general
superiority claim.

## 4. Standard generation procedure

### Step A — decision envelope

Write a small header:

```yaml
audience: "..."
artifact: "slides | proposal | memo | paper-idea | chapter-section"
decision_or_action: "..."
evidence_boundary: "what is supplied and what is not"
constraints: "..."
```

### Step B — Resolution first

Write one sentence containing the action or claim, its scope, and its evidence
qualification. A strong Resolution is specific enough to be challenged.

### Step C — SCQR opening

Use four short paragraphs or bullets. Keep Situation shared and brief;
Complication should explain why action is needed now; Question should create the
decision; Resolution should match the pyramid top.

### Step D — pyramid and evidence map

Choose 2–4 branches. For each branch, include:

```text
claim → evidence → implication → limitation
```

Keep field, method, metric, baseline, resource cost, and user evaluation as
separate dimensions when the topic is technical or academic.

### Step E — audits

Report the audit explicitly:

```text
Vertical: pass / partial / fail — why
Horizontal: pass / partial / fail — why
Open gaps: ...
```

### Step F — next actions

End with 1–5 actions in priority order. Each action should have an output and a
completion condition. Do not hide a major unknown inside an action verb.

## 5. Artifact routing

| Need | Shape |
|---|---|
| Fast update or email | SCR + one recommendation + next action |
| Presentation | SCQR opening + pyramid slide map + evidence/risks |
| Proposal | Resolution + options/criteria + workstreams + decision ask |
| Research idea | Problem + gap + hypothesis + method + evidence boundary |
| Thesis section | Claim hierarchy + citation slots + logic audit + caveats |

