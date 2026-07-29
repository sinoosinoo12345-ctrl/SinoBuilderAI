from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class FlutterProjectBuilder:
    """
    Sino Builder AI
    Flutter Production Builder
    """

    def __init__(self, flutter_binary: str = "flutter"):
        self.flutter = flutter_binary

    def create(self, project_path: str) -> Path:

        project = Path(project_path)

        if (project / "pubspec.yaml").exists():
            return project

        if project.exists():
            shutil.rmtree(project)

        project.parent.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            [
                self.flutter,
                "create",
                str(project),
            ],
            check=True,
        )

        return project

    def clean(self, project_path: str):

        subprocess.run(
            [
                self.flutter,
                "clean",
            ],
            cwd=project_path,
            check=True,
        )

    def pub_get(self, project_path: str):

        subprocess.run(
            [
                self.flutter,
                "pub",
                "get",
            ],
            cwd=project_path,
            check=True,
        )

    def build_release(self, project_path: str) -> Path:

        subprocess.run(
            [
                self.flutter,
                "build",
                "apk",
                "--release",
            ],
            cwd=project_path,
            check=True,
        )

        apk = (
            Path(project_path)
            / "build"
            / "app"
            / "outputs"
            / "flutter-apk"
            / "app-release.apk"
        )

        if not apk.exists():
            raise FileNotFoundError(
                "app-release.apk was not generated."
            )

        release = (
            Path(project_path)
            / "release"
        )

        release.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination = (
            release
            / "app-release.apk"
        )

        shutil.copy2(
            apk,
            destination,
        )

        return destination

    def full_build(self, project_path: str) -> Path:

        self.clean(project_path)

        self.pub_get(project_path)

        return self.build_release(project_path)
