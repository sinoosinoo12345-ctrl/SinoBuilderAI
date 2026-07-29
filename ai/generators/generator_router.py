from __future__ import annotations

from pathlib import Path

from ai.generators.python_generator import PythonGenerator
from ai.generators.flutter_generator import FlutterGenerator
from ai.generators.config_generator import ConfigGenerator


class GeneratorRouter:
    """
    Sino Builder AI
    Universal Intelligent Generator Router
    """

    def __init__(self) -> None:

        self.generators = []

        self.register(PythonGenerator())
        self.register(FlutterGenerator())
        self.register(ConfigGenerator())

    def register(self, generator) -> None:
        self.generators.append(generator)

    def generate(
        self,
        file_path: str,
        description: str,
        prompt: str,
    ) -> str:

        extension = Path(file_path).suffix.lower()

        for generator in self.generators:

            if generator.supports(file_path):

                return generator.generate(
                    file_path=file_path,
                    description=description,
                    prompt=prompt,
                )

        raise RuntimeError(
            f"No generator available for extension: {extension}"
        )

    def supported_extensions(self):

        extensions = []

        for generator in self.generators:

            if hasattr(generator, "supports"):

                extensions.append(generator.__class__.__name__)

        return extensions
