from __future__ import annotations

import os

from ai.models.llm_provider import (
    BaseLLMProvider,
    MockProvider,
)

from ai.models.sino_provider import SinoProvider


class ModelRouter:
    """
    Sino Builder AI
    Universal Model Router
    """

    def __init__(self) -> None:

        self.providers: dict[str, BaseLLMProvider] = {}

    def register(
        self,
        name: str,
        provider: BaseLLMProvider,
    ) -> None:

        self.providers[name.lower()] = provider

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self.providers

    def get(
        self,
        name: str,
    ) -> BaseLLMProvider:

        name = name.lower()

        if name not in self.providers:

            raise ValueError(
                f"AI Provider '{name}' is not registered."
            )

        return self.providers[name]

    def available(self) -> list[str]:

        return sorted(
            self.providers.keys()
        )

    @classmethod
    def default(cls):

        router = cls()

        router.register(
            "sino",
            SinoProvider(),
        )

        router.register(
            "local",
            MockProvider(),
        )

        openai_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if openai_key:

            from ai.models.openai_provider import OpenAIProvider

            router.register(
                "openai",
                OpenAIProvider(),
            )

        return router
