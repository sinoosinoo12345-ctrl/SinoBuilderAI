from __future__ import annotations

import json
from pathlib import Path


class ProjectManager:
    """
    Manages created Sino Builder AI projects.
    """

    def __init__(
        self,
        workspace: str = "workspace",
    ):

        self.workspace = Path(
            workspace
        )

        self.workspace.mkdir(
            parents=True,
            exist_ok=True,
        )


    def list_projects(self) -> list[dict]:

        projects = []

        for item in self.workspace.iterdir():

            if not item.is_dir():
                continue

            memory = (
                item
                / ".sino_memory.json"
            )

            # Only Sino Builder AI projects
            if not memory.exists():
                continue

            project = {
                "name": item.name,
                "path": str(item),
            }

            data = json.loads(
                memory.read_text(
                    encoding="utf-8"
                )
            )

            project.update(
                {
                    "description": data.get(
                        "description",
                        ""
                    ),
                    "changes": len(
                        data.get(
                            "changes",
                            []
                        )
                    ),
                }
            )

            projects.append(
                project
            )

        return projects


    def get_project(
        self,
        name: str,
    ):

        path = (
            self.workspace
            / name
        )

        memory = (
            path
            / ".sino_memory.json"
        )

        if not memory.exists():

            return None

        return {
            "name": name,
            "path": str(path),
        }
