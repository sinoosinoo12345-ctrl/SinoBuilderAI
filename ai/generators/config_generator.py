from __future__ import annotations

from pathlib import Path

from ai.generators.base_generator import BaseGenerator


class ConfigGenerator(BaseGenerator):
    """
    Sino Builder AI
    Universal Configuration Generator.
    """


    def supports(
        self,
        file_path: str,
    ) -> bool:

        return Path(file_path).suffix in {
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".cfg",
        }



    def generate(
        self,
        file_path: str,
        description: str,
        prompt: str,
    ) -> str:


        extension = Path(
            file_path
        ).suffix


        project_name = (
            self.clean_name(prompt)
        )


        if extension == ".json":

            return f"""
{{
  "project": "{project_name}",
  "version": "1.0.0",
  "environment": "production",
  "architecture": "modern",
  "ai_enabled": true,
  "security_enabled": true
}}
""".strip()



        if extension in (
            ".yaml",
            ".yml",
        ):

            return f"""
project: {project_name}

version: "1.0.0"

environment: production

features:
  ai: true
  security: true
  responsive_ui: true

architecture:
  style: modern
""".strip()



        if extension == ".toml":

            return f"""
[project]

name = "{project_name}"

version = "1.0.0"

environment = "production"


[features]

ai = true
security = true
""".strip()



        if extension in (
            ".ini",
            ".cfg",
        ):

            return f"""
[application]

name={project_name}

version=1.0.0

environment=production


[features]

ai=true

security=true
""".strip()



        return (
            "# Sino Builder AI Configuration"
        )



    def clean_name(
        self,
        text: str,
    ) -> str:

        name = (
            text
            .replace(" ", "_")
            .replace("/", "_")
        )

        return name[:40]
