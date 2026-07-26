"""Small dependency-free acceptance validator for repository structure."""

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
        "Pyramid Principle",
        "MECE",
        "Vertical logic",
        "Horizontal logic",
        "Six-step problem solving",
        "evidence",
    ],
    "README.md": ["Codex", "Claude Code", "Gemini", "MIT"],
}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing required files: {missing}")

    for path, terms in REQUIRED_TERMS.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        absent = [term for term in terms if term not in text]
        if absent:
            raise SystemExit(f"{path} missing terms: {absent}")

    print(f"OK: {len(REQUIRED_FILES)} required files and all core terms present")


if __name__ == "__main__":
    main()

