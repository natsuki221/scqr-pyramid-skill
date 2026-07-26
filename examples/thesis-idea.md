# Example: thesis ideation brief

## Resolution

> Frame the thesis as a two-stage evaluation of field-aware patent retrieval:
> first test controlled offline retrieval changes, then test whether experts can
> interpret and use the results in a realistic task.

## SCQR

- **Situation**: Patent retrieval can be evaluated with ranked relevance and
  system resource measures.
- **Complication**: Offline metrics alone do not establish that experts can
  understand, trust, or act on the results.
- **Question**: How can the architecture and evaluation keep retrieval quality,
  resource cost, and human usefulness distinguishable?
- **Resolution**: Use separate Stage 1 and Stage 2 protocols with explicit
  evidence gates.

## Pyramid

1. **Architecture** — separate retriever, reranker, fields, claims granularity,
   and result presentation.
2. **Stage 1** — fixed baselines, controlled ablations, IR metrics, resource
   reporting, and error analysis.
3. **Stage 2** — candidate construction, expert labels, agreement, task timing,
   questionnaire, and realism validation.

## Open questions

- Encoder, ANN configuration, relevance definition, and resource ceiling:
  `待確認`.
- Independent reranker versus same-model rescoring: must remain distinct.
- Participant protocol and sample: `待確認`.

