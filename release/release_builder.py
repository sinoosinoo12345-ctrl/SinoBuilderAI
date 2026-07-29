from __future__ import annotations

import json
from pathlib import Path


class ReleaseBuilder:
    """
    Sino Builder AI
    Release Builder
    Release V1
    """

    def build(
        self,
        project_path: str,
        project_name: str,
    ) -> Path:

        project = Path(
            project_path
        )

        manifest = {

            "name":
                project_name,

            "version":
                "1.0.0",

            "status":
                "ready",

            "path":
                str(project),

        }

        file = (
            project
            / "release.json"
        )

        file.write_text(

            json.dumps(
                manifest,
                indent=4,
                ensure_ascii=False,
            ),

            encoding="utf-8",

        )

        return file
