from __future__ import annotations

from release.release_builder import ReleaseBuilder
from release.exporter import Exporter
from release.installer import Installer


class ReleasePipeline:
    """
    Sino Builder AI
    Release Pipeline
    Release V1
    """

    def __init__(self):

        self.builder = ReleaseBuilder()

        self.exporter = Exporter()

        self.installer = Installer()

    def create_release(
        self,
        project_path: str,
        project_name: str,
        export_path: str | None = None,
    ) -> dict:

        release_file = (
            self.builder.build(
                project_path,
                project_name,
            )
        )

        result = {

            "release_file":
                str(release_file),

            "status":
                "built",

        }

        if export_path:

            exported = (
                self.exporter.export(
                    project_path,
                    export_path,
                )
            )

            result["exported"] = str(
                exported
            )

        return result
