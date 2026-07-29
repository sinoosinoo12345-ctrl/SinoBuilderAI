from __future__ import annotations

from dataclasses import dataclass

from ai.prompts.system_prompt import SYSTEM_PROMPT


@dataclass(slots=True)
class PromptResult:
    system_prompt: str
    user_prompt: str
    final_prompt: str


class PromptEngine:
    """
    Production Prompt Builder
    """

    def __init__(self) -> None:
        self.system_prompt = SYSTEM_PROMPT.strip()

    def build(
        self,
        user_prompt: str,
    ) -> PromptResult:

        user_prompt = user_prompt.strip()

        if not user_prompt:
            raise ValueError("Prompt cannot be empty.")

        final_prompt = f"""{self.system_prompt}

==============================
SINO BUILDER AI REQUEST
==============================

USER REQUEST:

{user_prompt}

==============================

Rules:

- Return only the requested result.
- No markdown unless explicitly requested.
- No explanations unless requested.
- Generate production-ready output.
- Follow Clean Architecture.
- Follow SOLID principles.
- Optimize readability and maintainability.
"""

        return PromptResult(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
            final_prompt=final_prompt,
        )
