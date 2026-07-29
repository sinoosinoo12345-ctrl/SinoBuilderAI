from __future__ import annotations

from pathlib import Path

from ai.generators.base_generator import BaseGenerator
from ai.models.llm_provider import MockProvider


class PythonGenerator(BaseGenerator):
    """
    Sino Builder AI
    Enterprise Python Generator
    """

    def __init__(self) -> None:

        self.ai = MockProvider()

    def supports(
        self,
        file_path: str,
    ) -> bool:

        return Path(file_path).suffix.lower() == ".py"

    def generate(
        self,
        file_path: str,
        description: str,
        prompt: str,
    ) -> str:

        component = self.detect_component(
            file_path,
            description,
        )

        ai_prompt = self.build_prompt(
            file_path=file_path,
            description=description,
            prompt=prompt,
            component=component,
        )

        result = self.ai.generate(
            ai_prompt
        )

        if result.strip():

            return result

        return self.template(
            description=description,
            component=component,
            file_path=file_path,
        )

    def detect_component(
        self,
        file_path: str,
        description: str,
    ) -> str:

        text = (
            file_path +
            " " +
            description
        ).lower()

        if (
            "fastapi" in text
            or "api" in text
            or "route" in text
            or "router" in text
        ):
            return "fastapi"

        if (
            "django" in text
        ):
            return "django"

        if (
            "flask" in text
        ):
            return "flask"

        if (
            "database" in text
            or "model" in text
            or "sqlite" in text
            or "postgres" in text
        ):
            return "database"

        if (
            "auth" in text
            or "login" in text
            or "jwt" in text
        ):
            return "authentication"

        if (
            "worker" in text
            or "task" in text
        ):
            return "worker"

        if (
            "config" in text
            or "setting" in text
        ):
            return "configuration"

        if (
            "test" in text
        ):
            return "tests"

        if (
            "ai" in text
            or "engine" in text
        ):
            return "ai"

        if (
            "cli" in text
        ):
            return "cli"

        return "module"

    def build_prompt(
        self,
        file_path: str,
        description: str,
        prompt: str,
        component: str,
    ) -> str:

        return f"""
You are Sino Builder AI.

Generate enterprise production Python code.

Project Request:
{prompt}

File:
{file_path}

Purpose:
{description}

Component:
{component}

Rules:

- Return ONLY Python code.
- No markdown.
- No explanations.
- Python 3.13 compatible.
- Production Ready.
- SOLID Architecture.
- Type Hints.
- Logging.
- Error Handling.
- Clean Imports.
- Secure Coding.
- Complete implementation.
"""

    def template(
        self,
        description: str,
        component: str,
        file_path: str,
    ) -> str:

        if component == "fastapi":

            return f'''"""
{description}
"""

from fastapi import FastAPI

app = FastAPI(
    title="Sino Builder AI"
)


@app.get("/")
async def root():

    return {{
        "status": "running",
        "service": "{Path(file_path).stem}"
    }}
'''

        if component == "database":

            return f'''"""
{description}
"""

from sqlalchemy.orm import DeclarativeBase


class Base(
    DeclarativeBase,
):
    pass
'''

        if component == "authentication":

            return f'''"""
{description}
"""

from datetime import datetime


class AuthService:

    def login(
        self,
        username: str,
        password: str,
    ) -> bool:

        return True


    def timestamp(self):

        return datetime.utcnow()
'''
        if component == "worker":

            return f'''"""
{description}
"""

class Worker:

    def execute(self):

        return {{
            "status": "completed"
        }}
'''

        if component == "configuration":

            return f'''"""
{description}
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Settings:

    app_name: str = "Sino Builder AI"

    version: str = "1.0.0"
'''

        if component == "tests":

            return f'''"""
{description}
"""

import unittest


class TestApplication(
    unittest.TestCase,
):

    def test_success(self):

        self.assertTrue(True)


if __name__ == "__main__":

    unittest.main()
'''

        if component == "ai":

            return f'''"""
{description}
"""

class AIEngine:

    def execute(
        self,
        prompt: str,
    ) -> dict:

        return {{
            "success": True,
            "response": prompt,
        }}
'''

        if component == "cli":

            return f'''"""
{description}
"""

import argparse


def main():

    parser = argparse.ArgumentParser()

    parser.parse_args()

    print("CLI Ready")


if __name__ == "__main__":

    main()
'''

        return f'''"""
{description}
"""

from __future__ import annotations


class Service:

    def run(self) -> dict:

        return {{

            "status": "ready",

            "component": "{component}",

        }}


if __name__ == "__main__":

    print(
        Service().run()
    )
'''
