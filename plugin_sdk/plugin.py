from __future__ import annotations

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Sino Builder AI
    Plugin Interface
    Release V1
    """

    name: str = ""
    version: str = "1.0.0"
    author: str = ""
    description: str = ""

    @abstractmethod
    def install(self) -> None:
        pass

    @abstractmethod
    def uninstall(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def execute(self, context: dict):
        pass
