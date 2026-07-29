from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """
    Base class for all Sino Builder AI agents.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(
        self,
        task: dict[str, Any],
        context: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute an agent task.
        """
        raise NotImplementedError

    def success(
        self,
        data: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "success": True,
            "agent": self.name,
            "data": data,
        }

    def error(
        self,
        message: str,
    ) -> dict[str, Any]:
        return {
            "success": False,
            "agent": self.name,
            "error": message,
        }
