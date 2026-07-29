from __future__ import annotations

import importlib.util
from pathlib import Path

from plugin_sdk.plugin import Plugin


class PluginLoader:
    """
    Sino Builder AI
    Plugin Loader
    Release V1
    """

    def __init__(
        self,
        plugins_directory: str = "plugins",
    ):

        self.plugins_directory = Path(
            plugins_directory
        )

    def load(
        self,
        plugin_name: str,
    ) -> Plugin:

        plugin_file = (
            self.plugins_directory
            / plugin_name
            / "plugin.py"
        )

        if not plugin_file.exists():

            raise FileNotFoundError(
                plugin_file
            )

        spec = importlib.util.spec_from_file_location(
            plugin_name,
            plugin_file,
        )

        if spec is None or spec.loader is None:

            raise RuntimeError(
                "Cannot load plugin"
            )

        module = importlib.util.module_from_spec(
            spec
        )

        spec.loader.exec_module(
            module
        )

        if not hasattr(
            module,
            "PluginImplementation",
        ):

            raise RuntimeError(
                "PluginImplementation not found"
            )

        plugin = module.PluginImplementation()

        if not isinstance(
            plugin,
            Plugin,
        ):

            raise TypeError(
                "Invalid plugin"
            )

        return plugin

    def discover(
        self,
    ) -> list[str]:

        if not self.plugins_directory.exists():

            return []

        return sorted(

            item.name

            for item in self.plugins_directory.iterdir()

            if item.is_dir()

        )
