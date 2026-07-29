from __future__ import annotations

from pathlib import Path

from ai.core.ai_engine import AIEngine
from ai.core.agent_context import AgentContext
from ai.generators.generator_router import GeneratorRouter


class CodeGenerationEngine:
    """
    Sino Builder AI
    Universal Production Code Engine.
    """

    def __init__(self):

        self.ai = AIEngine()
        self.router = GeneratorRouter()


    def analyze_project_type(
        self,
        description: str,
    ) -> str:

        text = description.lower()

        if any(
            x in text
            for x in [
                "mobile",
                "flutter",
                "android",
                "ios",
            ]
        ):
            return "mobile"

        if any(
            x in text
            for x in [
                "website",
                "web",
                "dashboard",
            ]
        ):
            return "web"

        if any(
            x in text
            for x in [
                "api",
                "backend",
                "server",
            ]
        ):
            return "backend"

        return "universal"


    def _build_prompt(
        self,
        file_path: str,
        description: str,
        context: AgentContext | None,
    ) -> str:


        project = ""
        decisions = ""
        generated = ""


        if context:

            project = context.project

            decisions = "\n".join(
                context.decisions
            )

            generated = "\n".join(
                context.generated_files
            )


        app_type = self.analyze_project_type(
            description
        )


        language = {
            ".py": "Python",
            ".dart": "Flutter Dart",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".html": "HTML",
            ".css": "CSS",
            ".json": "JSON",

        }.get(
            Path(file_path).suffix,
            "Source Code",
        )


        return f"""
You are Sino Builder AI Senior Developer.

Build a production application.

Application Type:
{app_type}

Project:
{project}

Language:
{language}

File:
{file_path}

Purpose:
{description}

Previous Decisions:
{decisions}

Generated Files:
{generated}

Requirements:

- Professional 2035 quality.
- Modern architecture.
- Clean code.
- Secure implementation.
- Responsive design.
- Complete working code.
- No explanations.
- Return only source code.
"""


    def generate_code(
        self,
        file_path: str,
        description: str,
        context: AgentContext | None = None,
    ) -> str:


        prompt = self._build_prompt(
            file_path,
            description,
            context,
        )


        try:

            return self.router.generate(
                file_path=file_path,
                description=description,
                prompt=prompt,
            )


        except ValueError:

            return self.ai.generate(
                prompt
            )


    def save_file(
        self,
        project_path: str,
        file_path: str,
        code: str,
    ) -> str:


        full_path = (
            Path(project_path)
            / file_path
        )


        full_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


        full_path.write_text(
            code,
            encoding="utf-8",
        )


        return str(full_path)


    def generate_and_save(
        self,
        project_path: str,
        file_path: str,
        description: str,
        context: AgentContext | None = None,
    ) -> str:


        code = self.generate_code(
            file_path,
            description,
            context,
        )


        return self.save_file(
            project_path,
            file_path,
            code,
        )
