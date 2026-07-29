from __future__ import annotations

from template_engine.template_engine import TemplateEngine
from plugin_sdk.plugin_api import PluginAPI
from integration.integration_engine import IntegrationEngine
from release.release_pipeline import ReleasePipeline


class EngineRegistry:
    """
    Sino Builder AI
    Engine Registry
    Release V1
    """

    def __init__(self):

        self.engines = {

            "template":
                TemplateEngine(),

            "plugin":
                PluginAPI(),

            "integration":
                IntegrationEngine(),

            "release":
                ReleasePipeline(),

        }

    def get(
        self,
        name: str,
    ):

        return self.engines.get(
            name
        )

    def all(
        self,
    ) -> list[str]:

        return list(
            self.engines.keys()
        )
