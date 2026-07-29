from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class ApkBuilder:
    """
    Sino Builder AI
    Builds a real Release APK.
    """

    def __init__(self, flutter_binary: str = "flutter"):
        self.flutter = flutter_binary

    def build(self, project_path: str) -> Path:
        project = Path(project_path)

        subprocess.run(
            [self.flutter, "clean"],
            cwd=project,
            check=True,
        )

        subprocess.run(
            [self.flutter, "pub", "get"],
            cwd=project,
            check=True,
        )

        subprocess.run(
            [self.flutter, "build", "apk", "--release"],
            cwd=project,
            check=True,
        )

        apk = (
            project
            / "build"
            / "app"
            / "outputs"
            / "flutter-apk"
            / "app-release.apk"
        )

        if not apk.exists():
            raise FileNotFoundError(
                f"APK was not generated: {apk}"
            )

        release_dir = project / "release"
        release_dir.mkdir(exist_ok=True)

        final_apk = release_dir / f"{project.name}.apk"

        shutil.copy2(apk, final_apk)

        return final_apk
