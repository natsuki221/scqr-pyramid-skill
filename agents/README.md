# AI 代理適配說明

適配檔刻意維持精簡。完整框架只有一份，位於 [`../core/SCQR_PYRAMID.md`](../core/SCQR_PYRAMID.md)，避免 Codex、Claude Code 與 Gemini／Antigravity 各自演變成不相容版本。

## Codex

可探索的適配檔位於 [`../.agents/skills/scqr-pyramid/SKILL.md`](../.agents/skills/scqr-pyramid/SKILL.md)。

```text
請使用 scqr-pyramid skill，將以下筆記整理成可供決策的提案。
```

## Claude Code

`CLAUDE.md` 會將 Claude Code 導向共用核心：

```text
請遵循此 repository 的 SCQR＋金字塔 Skill，
將下列資料整理成論文發想簡報。
```

## Gemini／Antigravity

`GEMINI.md` 提供專案層級適配：

```text
請套用 SCQR＋金字塔 Skill，依序輸出核心主張、SCQR、
金字塔、證據對照、邏輯稽核與下一步行動。
```

## 建議提供的任務資訊

```yaml
audience: "閱讀或聆聽此內容的人"
artifact: "slides | proposal | memo | paper-idea | chapter-section"
decision_or_action: "閱讀後應做出的決策或行動"
evidence: "筆記、數據、引用來源或未知"
constraints: "時間、篇幅、語言、資源限制"
```
