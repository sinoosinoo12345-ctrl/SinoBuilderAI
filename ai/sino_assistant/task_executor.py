from __future__ import annotations


class TaskExecutor:
    """
    Executes AI agents sequentially.
    """

    def execute(
        self,
        agents: list[str],
        callback,
    ) -> dict:

        results = {}

        for agent in agents:
            results[agent] = callback(agent)

        return results
