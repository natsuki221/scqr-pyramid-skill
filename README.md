# SCQR＋金字塔 Skill（繁體中文版）

一套可跨 AI 代理重複使用的思考技能，協助你將模糊想法整理成可供決策的簡報大綱、提案、決策備忘錄、研究方向或論文章節。

本技能整合：

- **SCR／SCQR**：情境（Situation）、複雜情況（Complication）、問題（Question）、解決方案（Resolution）。
- **金字塔原理（Pyramid Principle）**：先講答案，再用分組論點與證據支持。
- **MECE**：同層分類互不重疊，並在決策範圍內涵蓋重要面向。
- **垂直與水平邏輯檢查**：驗證證據是否支持上層論點，以及同層論點是否可比較。
- **六步驟問題解決**：定義、拆解、排序、規劃、分析、綜合。

這是一套思考與溝通工具，不代表 McKinsey 對本套件的認可。本版本根據使用者提供的影片字幕與對話內容蒸餾，並針對 AI 輔助簡報、提案與學術發想調整。

## 快速開始

將任務交給 AI，並要求它使用此技能：

```text
請使用此 repository 的 SCQR＋金字塔 Skill。
任務：將我的零散筆記整理成 7 頁簡報大綱。
受眾：論文指導教授。
需要的決策或行動：同意下一個實驗。
現有證據：[貼上筆記、數據或引用來源]
限制：10 分鐘、繁體中文、不可虛構證據。
```

AI 應依序輸出：

1. 一句話的解決方案／核心主張。
2. SCQR 開場。
3. 由 2～4 個可比較分支組成的金字塔。
4. 每個分支對應的證據；未知項目標示為 `?` 或 `待確認`。
5. 垂直與水平邏輯稽核。
6. 風險、假設與下一步行動。

## 支援的 AI 代理

本 repository 採用一份共用核心與三個薄型適配檔：

| 代理 | 適配檔 | 一般載入方式 |
|---|---|---|
| Codex | `.agents/skills/scqr-pyramid/SKILL.md` | 專案 Skill 探索或明確指定路徑 |
| Claude Code | `CLAUDE.md` | Claude Code 專案指令 |
| Gemini／Antigravity | `GEMINI.md` | Gemini 專案指令 |

各代理的呼叫方式請參閱 [`agents/README.md`](agents/README.md)。

### 安裝為 Claude Code Plugin

本 repository 同時也是一個自帶的 [plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)。
`plugins/scqr-pyramid/` 目錄將同一份 skill（核心規格＋模板）封裝成獨立的 Claude Code
plugin，不需要 clone 整個 repository 即可安裝：

```shell
/plugin marketplace add natsuki221/scqr-pyramid-skill
/plugin install scqr-pyramid@natsuki221-skills
/reload-plugins
```

安裝完成後以 `/scqr-pyramid:scqr-pyramid` 呼叫。

## Repository 結構

```text
.
├── .agents/skills/scqr-pyramid/SKILL.md  # Codex 適配檔
├── agents/README.md                      # 跨代理設定與使用方式
├── core/SCQR_PYRAMID.md                  # 共用核心規格
├── CLAUDE.md                             # Claude Code 適配檔
├── GEMINI.md                             # Gemini／Antigravity 適配檔
├── docs/decision-rubric.md               # 品質評分與反模式
├── templates/                            # 可重複使用的輸出模板
├── examples/                             # 完整範例
├── tests/                                # 驗收案例與驗證器
├── LICENSE                               # MIT
└── README.md
```

## 設計原則

- **結論先於鋪陳**：不要將建議埋在冗長時間線或實作細節後面。
- **證據先於信心**：分開標示已知事實、推論、假設與提案。
- **同層只用一種分類維度**：不要把成本、技術名稱與使用者抱怨當成平行類別。
- **MECE 與決策範圍相依**：「完整」是沒有重大決策缺口，不是列出所有細節。
- **檢索與重新排序不同**：討論技術系統時，分開處理欄位、方法、指標、基線與資源成本。
- **維持學術克制**：假設、離線代理指標與規劃中的研究，不得描述成已完成的證據。

## 授權

採用 MIT License，詳見 [`LICENSE`](LICENSE)。
