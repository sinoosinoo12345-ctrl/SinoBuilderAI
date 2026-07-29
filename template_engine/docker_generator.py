from __future__ import annotations

import shutil
from pathlib import Path

from template_engine.generator_registry import BaseGenerator


class DockerGenerator(BaseGenerator):
    """
    Sino Builder AI
    Docker Generator
    Release V1
    """

    name = "docker"

    def generate(
        self,
        project_name: str,
        project_path: str,
        config: dict,
    ) -> list[str]:

        generated_files = []

        source = Path("templates/docker")
        destination = Path(project_path)

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not source.exists():
            return generated_files

        for file in source.rglob("*"):

            if file.is_file():

                target = (
                    destination /
                    file.relative_to(source)
                )

                target.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                shutil.copy2(
                    file,
                    target,
                )

                generated_files.append(
                    str(target)
                )

        return generated_files
