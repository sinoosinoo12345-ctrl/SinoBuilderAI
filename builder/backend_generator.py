from __future__ import annotations

from pathlib import Path


class BackendGenerator:
    """
    Generates a FastAPI backend structure.
    """

    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def generate(self) -> None:

        backend = self.project_path / "backend"

        (backend / "routers").mkdir(
            parents=True,
            exist_ok=True,
        )

        (backend / "models").mkdir(
            parents=True,
            exist_ok=True,
        )

        (backend / "schemas").mkdir(
            parents=True,
            exist_ok=True,
        )

        (backend / "services").mkdir(
            parents=True,
            exist_ok=True,
        )

        (backend / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        (backend / "main.py").write_text(
            """
from fastapi import FastAPI

app = FastAPI(
    title="Sino Builder AI Backend",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {
        "status": "running"
    }
""".strip(),
            encoding="utf-8",
        )

        (backend / "routers" / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        (backend / "models" / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        (backend / "schemas" / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )

        (backend / "services" / "__init__.py").write_text(
            "",
            encoding="utf-8",
        )
