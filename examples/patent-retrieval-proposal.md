# Example: patent retrieval proposal

## Resolution

> Pilot claim-element decomposition for long independent claims, then compare
> it against whole-claim retrieval under a fixed run contract before expanding
> to human evaluation.

## SCQR

- **Situation**: The current system retrieves patent text using dense vectors
  and compares ranked candidates.
- **Complication**: Long claims contain multiple technical limitations, so a
  whole-claim representation may dilute element-level matches; the current
  evidence does not yet establish a causal improvement.
- **Question**: Which controlled change should be tested first, and how should
  quality and resource cost be reported together?
- **Resolution**: Start with a bounded claim-element pilot and preserve a
  whole-claim control.

## Pyramid

### 1. Relevance mechanism

- Claim: element-level matching may reduce semantic dilution in long claims.
- Evidence: `待確認` — requires an ablation by claim length and element type.
- Limitation: improvement may depend on decomposition quality.

### 2. Causal experiment design

- Claim: a fixed candidate set and one major factor per row make the comparison
  interpretable.
- Evidence: experiment design principle, not a measured result.
- Limitation: the pilot does not prove general superiority.

### 3. Evaluation boundary

- Claim: offline IR metrics and failure analysis are Stage 1 evidence; a real
  expert study requires participants, tasks, protocol, and agreement reporting.
- Evidence: protocol requirement; participant evidence is not present here.
- Limitation: offline gains may not translate to user value.

## Logic audit

- Vertical: **partial** — the mechanism is plausible but awaits data.
- Horizontal: **pass** — mechanism, causal design, and evaluation boundary are
  distinct dimensions.
- Overclaim blocked: “全面優於既有方法” is not allowed yet.

