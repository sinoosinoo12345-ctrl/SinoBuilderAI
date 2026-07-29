from __future__ import annotations

from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    """
    Base class for all source code generators.
    """

    @abstractmethod
    def supports(self, file_path: str) -> bool:
        """
        Return True if this generator supports the file.
        """
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        file_path: str,
        description: str,
        prompt: str,
    ) -> str:
        """
        Generate production-ready source code.
        """
        raise NotImplementedError
