from __future__ import annotations

import json
from pathlib import Path


class MemoryManager:

    def __init__(self, workspace="workspace"):

        self.workspace = Path(workspace)

        self.workspace.mkdir(exist_ok=True)

    def _memory_file(self, project):

        return self.workspace / project / ".sino_memory.json"

    def load(self, project):

        file = self._memory_file(project)

        if not file.exists():

            return {}

        try:

            return json.loads(file.read_text())

        except Exception:

            return {}

    def save(self, project, data):

        file = self._memory_file(project)

        file.parent.mkdir(parents=True, exist_ok=True)

        file.write_text(json.dumps(data, indent=4))

    def update(self, project, key, value):

        data = self.load(project)

        data[key] = value

        self.save(project, data)

        return data

    def append_log(self, project, message):

        data = self.load(project)

        logs = data.get("logs", [])

        logs.append(message)

        data["logs"] = logs

        self.save(project, data)

    def clear(self, project):

        self.save(project, {})
