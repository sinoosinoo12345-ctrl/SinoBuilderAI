from __future__ import annotations

import shutil
from pathlib import Path
from datetime import datetime


class VersionManager:
    """
    Creates backups before modifications.
    """

    def __init__(self, project_path: str):

        self.project_path = Path(project_path)

        self.backup_path = (
            self.project_path
            / ".versions"
        )


    def create_backup(self):

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )

        destination = (
            self.backup_path
            / timestamp
        )

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        for item in self.project_path.iterdir():

            if item.name == ".versions":
                continue

            target = destination / item.name

            if item.is_dir():

                shutil.copytree(
                    item,
                    target,
                )

            else:

                shutil.copy2(
                    item,
                    target,
                )

        return str(destination)
