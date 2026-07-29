from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from ai.core.context import ProjectContext


class ProjectManager:
    """
    Sino Builder AI
    Project Manager
    """

    def __init__(
        self,
        workspace: str | Path,
    ) -> None:

        self.workspace = Path(workspace)
        self.workspace.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create_project(
        self,
        project_name: str,
        description: str = "",
    ) -> ProjectContext:

        project_name = project_name.strip()

        if not project_name:
            raise ValueError(
                "Project name cannot be empty."
            )

        project_path = (
            self.workspace / project_name
        )

        project_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        folders = [

            "frontend",

            "backend",

            "database",

            "ai",

            "assets",

            "docs",

            "tests",

            "release",

            "logs",

        ]

        for folder in folders:

            (
                project_path / folder
            ).mkdir(
                parents=True,
                exist_ok=True,
            )

        return ProjectContext(

            project_id=str(uuid4()),

            project_name=project_name,

            workspace=self.workspace,

            description=description,

        )

    def open_project(
        self,
        project_name: str,
    ) -> ProjectContext:

        project_path = (
            self.workspace / project_name
        )

        if not project_path.exists():

            raise FileNotFoundError(
                project_name
            )

        return ProjectContext(

            project_id="existing",

            project_name=project_name,

            workspace=self.workspace,

        )

    def exists(
        self,
        project_name: str,
    ) -> bool:

        return (
            self.workspace / project_name
        ).exists()

    def list_projects(
        self,
    ) -> list[str]:

        return sorted(

            p.name

            for p in self.workspace.iterdir()

            if p.is_dir()

        )
