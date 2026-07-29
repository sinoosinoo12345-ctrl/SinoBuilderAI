from __future__ import annotations

from pathlib import Path

from builder.code_generator import CodeGenerator


class GenerationEngine:

    """
    SinoBuilderAI
    Generation Engine

    Responsible for converting
    analyzed architecture into
    a real project.
    """

    def __init__(self):

        self.generator = None

    def initialize(
        self,
        project_path: str | Path,
    ):

        self.generator = CodeGenerator(
            project_path,
        )

    def generate(
        self,
        architecture: dict,
    ):

        if self.generator is None:
            raise RuntimeError(
                "GenerationEngine is not initialized."
        )

        project_type = architecture.get(
            "project_type",
        "generic",
        )

        self.generator.create_project()

        return {
            "success": True,
            "project_type": project_type,
            "generated": self.generator.summary(),
        }
