from __future__ import annotations

import shutil
from pathlib import Path


class ProjectMerger:
    """
    Sino Builder AI
    Project Merger
    Release V1
    """

    def merge(
        self,
        project_path: Path,
    ) -> dict:

        generated = (
            project_path
            / "generated"
        )

        merged = []

        if not generated.exists():

            return {
                "merged": merged,
                "status": "nothing_to_merge",
            }

        for item in generated.rglob("*"):

            if item.is_file():

                destination = (
                    project_path
                    / item.relative_to(generated)
                )

                destination.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                shutil.copy2(
                    item,
                    destination,
                )

                merged.append(
                    str(destination)
                )

        return {
            "merged": merged,
            "status": "merged",
        }
