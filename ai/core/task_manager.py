from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Task:
    id: str
    agent: str
    action: str
    payload: dict[str, Any] = field(default_factory=dict)
    status: str = "pending"


class TaskManager:
    """
    Central task queue for Sino Builder AI.
    """

    def __init__(self) -> None:
        self._queue: deque[Task] = deque()
        self._history: list[Task] = []

    def add(self, task: Task) -> None:
        self._queue.append(task)

    def next(self) -> Task | None:
        if not self._queue:
            return None

        task = self._queue.popleft()
        task.status = "running"
        return task

    def complete(self, task: Task) -> None:
        task.status = "completed"
        self._history.append(task)

    def fail(self, task: Task) -> None:
        task.status = "failed"
        self._history.append(task)

    def pending_count(self) -> int:
        return len(self._queue)

    def history(self) -> list[Task]:
        return list(self._history)

    def clear(self) -> None:
        self._queue.clear()
        self._history.clear()
