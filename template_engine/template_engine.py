from __future__ import annotations

from template_engine.generator_registry import GeneratorRegistry

from template_engine.flutter_generator import FlutterGenerator
from template_engine.fastapi_generator import FastAPIGenerator
from template_engine.react_generator import ReactGenerator
from template_engine.web_generator import WebGenerator
from template_engine.desktop_generator import DesktopGenerator
from template_engine.docker_generator import DockerGenerator


class TemplateEngine:
    """
    Sino Builder AI
    Template Engine Core
    Release V1
    """

    def __init__(self):

        self.registry = GeneratorRegistry()

        self.register_defaults()

    def register_defaults(self):

        generators = [

            FlutterGenerator(),

            FastAPIGenerator(),

            ReactGenerator(),

            WebGenerator(),

            DesktopGenerator(),

            DockerGenerator(),

        ]

        for generator in generators:

            self.registry.register(
                generator
            )

    def generate(
        self,
        template_type: str,
        project_name: str,
        project_path: str,
        config: dict | None = None,
    ):

        generator = self.registry.get(
            template_type
        )

        return generator.generate(
            project_name,
            project_path,
            config or {},
        )

    def available(self):

        return [
            generator.name
            for generator in self.registry.all()
        ]
