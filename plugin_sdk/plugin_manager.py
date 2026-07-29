from __future__ import annotations

from typing import Dict

from plugin_sdk.plugin import Plugin
from plugin_sdk.plugin_registry import PluginRegistry


class PluginManager:
    """
    Sino Builder AI
    Plugin Manager
    Release V1
    """

    def __init__(self):

        self.registry = PluginRegistry()

        self.enabled: Dict[str, bool] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:

        self.registry.register(
            plugin
        )

        self.enabled[
            plugin.name.lower()
        ] = False

    def install(
        self,
        name: str,
    ) -> None:

        plugin = self.registry.get(
            name
        )

        plugin.install()

    def uninstall(
        self,
        name: str,
    ) -> None:

        plugin = self.registry.get(
            name
        )

        plugin.uninstall()

        self.registry.unregister(
            name
        )

        self.enabled.pop(
            name.lower(),
            None,
        )

    def enable(
        self,
        name: str,
    ) -> None:

        plugin = self.registry.get(
            name
        )

        plugin.enable()

        self.enabled[
            name.lower()
        ] = True

    def disable(
        self,
        name: str,
    ) -> None:

        plugin = self.registry.get(
            name
        )

        plugin.disable()

        self.enabled[
            name.lower()
        ] = False

    def execute(
        self,
        name: str,
        context: dict,
    ):

        if not self.enabled.get(
            name.lower(),
            False,
        ):

            raise RuntimeError(
                "Plugin is disabled"
            )

        plugin = self.registry.get(
            name
        )

        return plugin.execute(
            context
        )
