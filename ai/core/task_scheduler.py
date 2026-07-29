from __future__ import annotations

from collections import deque


class TaskScheduler:

    def __init__(self):

        self.tasks = deque()

    def add(self, name: str, payload=None):

        self.tasks.append({
            "name": name,
            "payload": payload,
            "status": "waiting"
        })

    def next(self):

        if not self.tasks:
            return None

        task = self.tasks.popleft()
        task["status"] = "running"
        return task

    def complete(self, task):

        task["status"] = "done"
        return task

    def pending(self):

        return len(self.tasks)

    def clear(self):

        self.tasks.clear()

    def all(self):

        return list(self.tasks)
