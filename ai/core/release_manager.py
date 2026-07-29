from __future__ import annotations

import json
from pathlib import Path


class ReleaseManager:

    def __init__(self, project_path):

        self.project = Path(project_path)

    def create_release(self):

        self.project.mkdir(parents=True, exist_ok=True)

        release = {
            "engine": "Sino Builder AI",
            "version": "7.0",
            "status": "ready",
            "targets": [
                "Android APK",
                "Web",
                "Windows",
                "Linux",
                "macOS"
            ]
        }

        file = self.project / "release.json"

        file.write_text(
            json.dumps(release, indent=4),
            encoding="utf-8"
        )

        return file

    def exists(self):

        return (self.project / "release.json").exists()
