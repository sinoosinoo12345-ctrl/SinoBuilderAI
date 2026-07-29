from __future__ import annotations

import shutil
from pathlib import Path


class Installer:
    """
    Sino Builder AI
    Installer
    Release V1
    """

    def install(
        self,
        project_path: str,
        destination_path: str,
    ) -> Path:

        source = Path(
            project_path
        )

        destination = Path(
            destination_path
        )

        if destination.exists():

            shutil.rmtree(
                destination
            )

        shutil.copytree(
            source,
            destination,
        )

        return destination

    def remove(
        self,
        destination_path: str,
    ) -> None:

        destination = Path(
            destination_path
        )

        if destination.exists():

            shutil.rmtree(
                destination
            )
