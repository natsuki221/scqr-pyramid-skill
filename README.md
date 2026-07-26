# SCQR + Pyramid Skill

A reusable, cross-agent reasoning skill for turning an unclear idea into a
decision-ready brief, proposal, presentation outline, or research direction.

The skill combines:

- **SCR / SCQR** — Situation, Complication, Question, Resolution.
- **Pyramid Principle** — lead with the answer, then support it with grouped
  reasons and evidence.
- **MECE** — make peer-level buckets non-overlapping and collectively complete
  enough for the decision at hand.
- **Vertical and horizontal logic checks** — verify support within a branch and
  comparability across branches.
- **Six-step problem solving** — define, decompose, prioritize, plan, analyze,
  synthesize.

This is a thinking and communication aid, not a claim that McKinsey endorses
this exact package. The framework was distilled from the user-provided video
subtitle/conversation context and is intentionally adapted for AI-assisted
briefing, proposals, and academic ideation.

## Quick start

Give an agent a task and ask it to use the shared skill:

```text
Use the SCQR + Pyramid Skill from this repository.
Task: turn my rough idea into a 7-slide presentation outline.
Audience: my thesis advisor.
Decision or action needed: approve the next experiment.
Evidence available: [paste notes, data, or citations].
Constraints: 10 minutes, Traditional Chinese, do not invent evidence.
```

The agent should return, in order:

1. A one-sentence Resolution.
2. An SCQR opening.
3. A pyramid of 2–4 mutually comparable support branches.
4. Evidence mapped to each branch, with unknowns marked `?` or `待確認`.
5. A vertical/horizontal logic audit.
6. Risks, assumptions, and next actions.

## Supported agents

The repository keeps one shared core and thin adapters:

| Agent | Adapter | Typical discovery |
|---|---|---|
| Codex | `.agents/skills/scqr-pyramid/SKILL.md` | Project skill discovery or explicit path |
| Claude Code | `CLAUDE.md` | Project instructions loaded by Claude Code |
| Gemini / Antigravity | `GEMINI.md` | Project instructions loaded by Gemini tooling |

See [`agents/README.md`](agents/README.md) for invocation examples and the
boundary between shared rules and agent-specific behavior.

### Install as a Claude Code plugin

This repository is also a self-hosting [plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces).
The `plugins/scqr-pyramid/` directory packages the same skill (core spec +
templates) as a standalone Claude Code plugin, so it can be installed without
cloning the whole repo into your project:

```shell
/plugin marketplace add natsuki221/scqr-pyramid-skill
/plugin install scqr-pyramid@scqr-pyramid
/reload-plugins
```

Then invoke it with `/scqr-pyramid:scqr-pyramid`.

## Repository map

```text
.
├── .agents/skills/scqr-pyramid/SKILL.md  # Codex-facing adapter
├── agents/README.md                      # Cross-agent setup and usage
├── core/SCQR_PYRAMID.md                  # Shared operating specification
├── CLAUDE.md                             # Claude Code adapter
├── GEMINI.md                             # Gemini / Antigravity adapter
├── docs/decision-rubric.md               # Quality rubric and anti-patterns
├── templates/                            # Reusable output shapes
├── examples/                             # Worked examples
├── tests/                                # Acceptance cases and validator
├── LICENSE                               # MIT
└── README.md
```

## Design principles

- **Conclusion before exposition.** Do not bury the proposed answer beneath a
  long chronology.
- **Evidence before confidence.** Separate observed facts, inferences,
  assumptions, and proposals.
- **One dimension per peer group.** Do not mix cost, a technology, and a user
  complaint as if they were parallel categories.
- **MECE is decision-relative.** Complete means no material decision gap, not
  that every possible detail is listed.
- **Retrieval is not reranking.** When discussing technical systems, preserve
  distinctions such as field, method, metric, baseline, and resource cost.
- **Academic restraint.** Treat a hypothesis, offline proxy, or proposed study
  as such; never upgrade it into completed evidence.

## License

MIT. See [`LICENSE`](LICENSE).
