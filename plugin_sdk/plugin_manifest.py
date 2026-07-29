from __future__ import annotations

import json
from pathlib import Path


class PluginManifest:
    """
    Sino Builder AI
    Plugin Manifest
    Release V1
    """

    FILE_NAME = "plugin.json"

    def load(
        self,
        plugin_directory: str,
    ) -> dict:

        file = (
            Path(plugin_directory)
            / self.FILE_NAME
        )

        if not file.exists():

            raise FileNotFoundError(
                file
            )

        return json.loads(
            file.read_text(
                encoding="utf-8"
            )
        )

    def save(
        self,
        plugin_directory: str,
        data: dict,
    ) -> None:

        file = (
            Path(plugin_directory)
            / self.FILE_NAME
        )

        file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file.write_text(

            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            ),

            encoding="utf-8",

        )

    def exists(
        self,
        plugin_directory: str,
    ) -> bool:

        return (
            Path(plugin_directory)
            / self.FILE_NAME
        ).exists()
