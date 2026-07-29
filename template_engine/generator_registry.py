from __future__ import annotations

from typing import Dict
from typing import List


class BaseGenerator:
    """
    Sino Builder AI
    Base Generator Interface
    Release V1
    """

    name = "base"

    def generate(
        self,
        project_name: str,
        project_path: str,
        config: dict,
    ) -> list[str]:
        raise NotImplementedError


class GeneratorRegistry:
    """
    Sino Builder AI
    Generator Registry
    Release V1
    """

    def __init__(self):

        self._generators: Dict[str, BaseGenerator] = {}

    def register(
        self,
        generator: BaseGenerator,
    ):

        self._generators[
            generator.name.lower()
        ] = generator

    def unregister(
        self,
        name: str,
    ):

        self._generators.pop(
            name.lower(),
            None,
        )

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._generators
        )

    def get(
        self,
        name: str,
    ) -> BaseGenerator:

        return self._generators[
            name.lower()
        ]

    def all(
        self,
    ) -> List[BaseGenerator]:

        return list(
            self._generators.values()
        )

    def clear(
        self,
    ):

        self._generators.clear()
