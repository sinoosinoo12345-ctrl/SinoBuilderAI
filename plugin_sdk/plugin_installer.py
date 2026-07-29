from __future__ import annotations

import shutil
from pathlib import Path

from plugin_sdk.plugin_manifest import PluginManifest


class PluginInstaller:
    """
    Sino Builder AI
    Plugin Installer
    Release V1
    """

    def __init__(
        self,
        plugins_directory: str = "plugins",
    ):

        self.plugins_directory = Path(
            plugins_directory
        )

        self.manifest = PluginManifest()

    def install(
        self,
        source_directory: str,
    ) -> Path:

        source = Path(
            source_directory
        )

        if not source.exists():

            raise FileNotFoundError(
                source
            )

        data = self.manifest.load(
            str(source)
        )

        plugin_name = data["name"]

        destination = (
            self.plugins_directory
            / plugin_name
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

    def uninstall(
        self,
        plugin_name: str,
    ) -> None:

        destination = (
            self.plugins_directory
            / plugin_name
        )

        if destination.exists():

            shutil.rmtree(
                destination
            )

    def installed_plugins(
        self,
    ) -> list[str]:

        if not self.plugins_directory.exists():

            return []

        return sorted(

            item.name

            for item in self.plugins_directory.iterdir()

            if item.is_dir()

        )
