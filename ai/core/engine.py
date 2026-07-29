from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai.core.context import ProjectContext


@dataclass(slots=True)
class EngineResult:
    success: bool
    message: str
    data: dict[str, Any] = field(default_factory=dict)


class SinoCoreEngine:
    """
    Main execution engine for Sino Builder AI.
    Responsible for receiving user requests,
    validating them, and starting execution.
    """

    VERSION = "1.0.0"

    def __init__(self) -> None:
        self._active_context: ProjectContext | None = None

    @property
    def context(self) -> ProjectContext | None:
        return self._active_context

    def load_project(self, context: ProjectContext) -> None:
        self._active_context = context

    def unload_project(self) -> None:
        self._active_context = None

    def is_project_loaded(self) -> bool:
        return self._active_context is not None

    def execute(self, request: str) -> EngineResult:
        request = request.strip()

        if not request:
            return EngineResult(
                success=False,
                message="Empty request."
            )

        if self._active_context is None:
            return EngineResult(
                success=False,
                message="No project loaded."
            )

        return EngineResult(
            success=True,
            message="Request accepted.",
            data={
                "request": request,
                "project": self._active_context.project_name,
                "project_id": self._active_context.project_id,
                "status": "queued"
            }
        )
