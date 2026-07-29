from __future__ import annotations

from typing import Dict, List

from plugin_sdk.plugin import Plugin


class PluginRegistry:
    """
    Sino Builder AI
    Plugin Registry
    Release V1
    """

    def __init__(self):

        self._plugins: Dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:

        self._plugins[
            plugin.name.lower()
        ] = plugin

    def unregister(
        self,
        name: str,
    ) -> None:

        self._plugins.pop(
            name.lower(),
            None,
        )

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._plugins
        )

    def get(
        self,
        name: str,
    ) -> Plugin:

        return self._plugins[
            name.lower()
        ]

    def all(
        self,
    ) -> List[Plugin]:

        return list(
            self._plugins.values()
        )

    @property
    def count(
        self,
    ) -> int:

        return len(
            self._plugins
        )
