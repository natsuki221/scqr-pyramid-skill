# Agent adapters

The adapters are deliberately thin. The framework lives in one place:
[`../core/SCQR_PYRAMID.md`](../core/SCQR_PYRAMID.md). This prevents Codex,
Claude Code, and Gemini / Antigravity from drifting into three incompatible
versions of the method.

## Codex

The discoverable adapter is
[`../.agents/skills/scqr-pyramid/SKILL.md`](../.agents/skills/scqr-pyramid/SKILL.md).
From a project that has this repository available, ask:

```text
Use the scqr-pyramid skill to turn these notes into a decision-ready proposal.
```

## Claude Code

`CLAUDE.md` points Claude Code to the core contract. A direct invocation is:

```text
Follow the SCQR + Pyramid Skill in this repository and produce a thesis idea
brief from the notes below.
```

## Gemini / Antigravity

`GEMINI.md` provides the project-level adapter. A direct invocation is:

```text
Apply the SCQR + Pyramid Skill. Return the Resolution, SCQR opening, pyramid,
evidence map, logic audit, and next actions.
```

## Suggested context envelope

For consistent results, include:

```yaml
audience: "who will read or hear this"
artifact: "slides | proposal | memo | paper-idea | chapter-section"
decision_or_action: "what should happen after reading"
evidence: "notes, data, citations, or unknown"
constraints: "time, length, language, resources"
```

