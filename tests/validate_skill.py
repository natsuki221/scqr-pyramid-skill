"""不依賴第三方套件的 repository 結構與繁體中文內容驗收器。"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CLAUDE.md",
    "GEMINI.md",
    ".agents/skills/scqr-pyramid/SKILL.md",
    "core/SCQR_PYRAMID.md",
    "agents/README.md",
    "docs/decision-rubric.md",
    "templates/presentation-outline.md",
    "templates/proposal.md",
    "templates/research-idea.md",
    "examples/patent-retrieval-proposal.md",
    "examples/thesis-idea.md",
    "tests/acceptance-cases.yaml",
]

REQUIRED_TERMS = {
    "core/SCQR_PYRAMID.md": [
        "SCR",
        "SCQR",
        "金字塔原理",
        "MECE",
        "垂直邏輯",
        "水平邏輯",
        "六步驟問題解決",
        "證據",
    ],
    "README.md": ["繁體中文", "Codex", "Claude Code", "Gemini", "MIT"],
    "tests/acceptance-cases.yaml": ["language: zh-TW", "待確認"],
}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"缺少必要檔案：{missing}")

    for path, terms in REQUIRED_TERMS.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        absent = [term for term in terms if term not in text]
        if absent:
            raise SystemExit(f"{path} 缺少必要詞彙：{absent}")

    print(f"通過：{len(REQUIRED_FILES)} 個必要檔案與繁體中文核心詞彙均存在")


if __name__ == "__main__":
    main()
