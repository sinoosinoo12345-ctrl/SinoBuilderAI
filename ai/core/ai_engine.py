from __future__ import annotations

from ai.core.prompt_engine import PromptEngine
from ai.models.router import ModelRouter


class AIEngine:
    """
    Sino Builder AI
    Cyber AI Generation Engine
    """

    def __init__(
        self,
        provider: str = "sino"
    ) -> None:

        self.router = ModelRouter.default()

        self.provider = self.router.get(
            provider
        )

        self.prompt_engine = PromptEngine()

    def generate(

        self,

        request: str,

        system_prompt: str = "",

    ) -> str:

        prompt = self.build_prompt(

            request=request,

            system_prompt=system_prompt,

        )

        response = self.provider.generate(
            prompt
        )

        return response.strip()

    def build_prompt(

        self,

        request: str,

        system_prompt: str,

    ) -> str:

        request = request.strip()

        system_prompt = system_prompt.strip()

        if system_prompt:

            request = (
                system_prompt
                + "\n\n"
                + request
            )

        final = self.prompt_engine.build(
            request
        )

        return final.final_prompt
    def generate_code(
        self,
        prompt: str,
    ) -> str:

        return self.generate(
            request=prompt,
            system_prompt=self.code_system_prompt(),
        )

    def generate_architecture(
        self,
        prompt: str,
    ) -> str:

        return self.generate(
            request=prompt,
            system_prompt=self.architecture_system_prompt(),
        )

    def generate_security(
        self,
        prompt: str,
    ) -> str:

        return self.generate(
            request=prompt,
            system_prompt=self.security_system_prompt(),
        )

    def improve_code(
        self,
        code: str,
    ) -> str:

        return self.generate(
            request=code,
            system_prompt="""
Improve the following source code.

Rules:
- Production Ready.
- SOLID.
- Clean Architecture.
- Optimize Performance.
- Secure Coding.
- Keep functionality unchanged.
Return code only.
""",
        )
    @staticmethod
    def code_system_prompt() -> str:

        return """
You are Sino Builder AI.

Generate production-ready source code.

Rules:

- Return ONLY source code.
- No markdown.
- No explanations.
- Python 3.13 compatible.
- Clean Architecture.
- SOLID principles.
- Enterprise quality.
- Include imports.
- Include type hints.
- Include error handling.
- Generate complete implementations.
"""

    @staticmethod
    def architecture_system_prompt() -> str:

        return """
You are the Chief Software Architect of Sino Builder AI.

Design scalable enterprise software architecture.

Rules:

- Modern Architecture.
- Modular.
- Production Ready.
- Security First.
- High Performance.
"""

    @staticmethod
    def security_system_prompt() -> str:

        return """
You are the Cyber Security Chief of Sino Builder AI.

Analyze software from a cyber-security perspective.

Rules:

- Authentication.
- Authorization.
- Secure Storage.
- Input Validation.
- Encryption.
- OWASP Top 10.
- Return only actionable recommendations.
"""
