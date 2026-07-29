from __future__ import annotations

from pathlib import Path
import json


class ProjectStatus:
    """
    Shows project health information.
    """

    def analyze(
        self,
        project_path: str,
    ):

        path = Path(project_path)

        memory_file = (
            path
            / ".sino_memory.json"
        )

        versions = (
            path
            / ".versions"
        )

        files = 0

        for item in path.rglob("*"):

            if item.is_file() and ".versions" not in str(item):

                files += 1


        data = {}

        if memory_file.exists():

            data = json.loads(
                memory_file.read_text(
                    encoding="utf-8"
                )
            )


        return {
            "files": files,
            "changes": len(
                data.get(
                    "changes",
                    []
                )
            ),
            "backups": len(
                list(versions.iterdir())
            ) if versions.exists() else 0,
        }
