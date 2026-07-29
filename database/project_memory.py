from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime


class ProjectMemory:
    """
    Stores project history and changes.
    """

    def __init__(self, project_path: str):

        self.project_path = Path(project_path)

        self.memory_file = (
            self.project_path
            / ".sino_memory.json"
        )

    def create(
        self,
        name: str,
        description: str,
    ):

        data = {
            "project": name,
            "description": description,
            "created": datetime.now().isoformat(),
            "changes": [],
        }

        self.save(data)

        return data


    def load(self):

        if not self.memory_file.exists():
            return None

        return json.loads(
            self.memory_file.read_text(
                encoding="utf-8"
            )
        )


    def add_change(
        self,
        change: str,
    ):

        data = self.load()

        if data is None:
            data = {
                "changes": []
            }

        data["changes"].append(
            {
                "change": change,
                "time": datetime.now().isoformat(),
            }
        )

        self.save(data)


    def save(self, data):

        self.memory_file.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
