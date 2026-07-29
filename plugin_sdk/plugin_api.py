from __future__ import annotations

from plugin_sdk.plugin_loader import PluginLoader
from plugin_sdk.plugin_manager import PluginManager
from plugin_sdk.plugin_validator import PluginValidator


class PluginAPI:
    """
    Sino Builder AI
    Plugin API
    Release V1
    """

    def __init__(self):

        self.loader = PluginLoader()

        self.manager = PluginManager()

        self.validator = PluginValidator()

    def load(
        self,
        plugin_name: str,
    ):

        plugin = self.loader.load(
            plugin_name
        )

        result = self.validator.validate(
            plugin
        )

        if not result["success"]:

            raise RuntimeError(
                result["errors"]
            )

        self.manager.register(
            plugin
        )

        return plugin

    def enable(
        self,
        plugin_name: str,
    ):

        self.manager.enable(
            plugin_name
        )

    def disable(
        self,
        plugin_name: str,
    ):

        self.manager.disable(
            plugin_name
        )

    def execute(
        self,
        plugin_name: str,
        context: dict,
    ):

        return self.manager.execute(
            plugin_name,
            context,
        )

    def plugins(
        self,
    ):

        return self.manager.registry.all()
