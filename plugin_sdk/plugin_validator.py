from __future__ import annotations

from plugin_sdk.plugin import Plugin


class PluginValidator:
    """
    Sino Builder AI
    Plugin Validator
    Release V1
    """

    REQUIRED_FIELDS = [
        "name",
        "version",
        "author",
        "description",
    ]

    REQUIRED_METHODS = [
        "install",
        "uninstall",
        "enable",
        "disable",
        "execute",
    ]

    def validate(
        self,
        plugin: Plugin,
    ) -> dict:

        errors = []

        for field in self.REQUIRED_FIELDS:

            if not getattr(plugin, field, None):

                errors.append(
                    f"Missing field: {field}"
                )

        for method in self.REQUIRED_METHODS:

            if not callable(
                getattr(plugin, method, None)
            ):

                errors.append(
                    f"Missing method: {method}"
                )

        return {
            "success": len(errors) == 0,
            "errors": errors,
        }
