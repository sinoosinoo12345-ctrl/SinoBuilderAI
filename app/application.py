from __future__ import annotations

from app.registry import EngineRegistry


class SinoBuilderApplication:
    """
    Sino Builder AI
    Main Application
    Release V1
    """

    def __init__(self):

        self.registry = EngineRegistry()

        self.version = "1.0.0"

    def status(
        self,
    ) -> dict:

        return {

            "name":
                "Sino Builder AI",

            "version":
                self.version,

            "status":
                "ready",

            "engines":
                self.registry.all(),

        }

    def engine(
        self,
        name: str,
    ):

        return self.registry.get(
            name
        )
