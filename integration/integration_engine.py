from __future__ import annotations

from pathlib import Path

from integration.dependency_manager import DependencyManager
from integration.project_merger import ProjectMerger
from integration.final_validator import FinalValidator


class IntegrationEngine:
    """
    Sino Builder AI
    Integration Engine
    Release V1
    """

    def __init__(self):

        self.dependencies = DependencyManager()

        self.merger = ProjectMerger()

        self.validator = FinalValidator()

    def integrate(
        self,
        project_path: str,
    ) -> dict:

        project = Path(
            project_path
        )

        dependency_result = (
            self.dependencies.resolve(
                project
            )
        )

        merge_result = (
            self.merger.merge(
                project
            )
        )

        validation = (
            self.validator.validate(
                project
            )
        )

        return {

            "dependencies":
                dependency_result,

            "merge":
                merge_result,

            "validation":
                validation,

            "success":
                validation["success"],

        }
