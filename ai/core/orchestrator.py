from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass(slots=True)
class AgentTask:
    name: str
    payload: dict
    status: str = "pending"


class Orchestrator:
    """
    Coordinates execution between AI agents.
    """

    def __init__(self) -> None:
        self._agents: dict[str, Callable[[dict], dict]] = {}

    def register_agent(
        self,
        name: str,
        handler: Callable[[dict], dict],
    ) -> None:
        if name in self._agents:
            raise ValueError(f"Agent '{name}' already registered.")

        self._agents[name] = handler

    def unregister_agent(self, name: str) -> None:
        self._agents.pop(name, None)

    def has_agent(self, name: str) -> bool:
        return name in self._agents

    def available_agents(self) -> list[str]:
        return sorted(self._agents.keys())

    def execute(self, task: AgentTask) -> dict:
        if task.name not in self._agents:
            raise RuntimeError(
                f"Agent '{task.name}' not found."
            )

        task.status = "running"

        result = self._agents[task.name](task.payload)

        task.status = "completed"

        return result
