from __future__ import annotations

import os

from openai import OpenAI

from ai.models.llm_provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    def __init__(self) -> None:

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY not found."
            )

        self.client = OpenAI(
            api_key=api_key,
        )

    def generate(self, prompt: str) -> str:

        response = self.client.responses.create(
            model="gpt-5.5",
            input=prompt,
        )

        return response.output_text
