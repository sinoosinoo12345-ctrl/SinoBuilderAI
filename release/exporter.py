from __future__ import annotations

import shutil
from pathlib import Path


class Exporter:
    """
    Sino Builder AI
    Project Exporter
    Release V1
    """

    def export(
        self,
        project_path: str,
        export_path: str,
    ) -> Path:

        source = Path(
            project_path
        )

        destination = Path(
            export_path
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
