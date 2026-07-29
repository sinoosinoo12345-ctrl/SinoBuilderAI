from __future__ import annotations


class AgentFactory:
    """
    Production Agent Factory
    """

    _agents: dict[str, type] = {}

    @classmethod
    def register(
        cls,
        name: str,
        agent_class: type,
    ) -> None:

        cls._agents[name.lower()] = agent_class

    @classmethod
    def create(
        cls,
        name: str,
    ):

        key = name.lower()

        if key not in cls._agents:

            raise ValueError(
                f"Unknown agent: {name}"
            )

        return cls._agents[key]()

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:

        return name.lower() in cls._agents

    @classmethod
    def available(
        cls,
    ) -> list[str]:

        return sorted(
            cls._agents.keys()
        )

    @classmethod
    def clear(
        cls,
    ) -> None:

        cls._agents.clear()
