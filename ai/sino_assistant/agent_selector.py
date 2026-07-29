from __future__ import annotations

from ai.core.architecture_context import ArchitectureContext


class AgentSelector:

    """
    Selects required AI agents according
    to project architecture.
    """

    def select(
        self,
        architecture: ArchitectureContext,
    ) -> list[str]:

        agents = [
            "planner",
            "architect",
        ]

        if "frontend" in architecture.layers:
            agents.append("frontend")

        if "backend" in architecture.layers:
            agents.append("backend")

        if "database" in architecture.layers:
            agents.append("database")

        if "ai" in architecture.layers:
            agents.append("ai")

        agents.extend([
            "validator",
            "integration",
            "release",
        ])

        return list(dict.fromkeys(agents))
