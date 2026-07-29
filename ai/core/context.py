from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ProjectContext:
    """
    Holds the active project state shared across all AI agents.
    """

    project_id: str
    project_name: str
    workspace: Path

    description: str = ""
    target_platforms: list[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self) -> None:
        self.updated_at = datetime.utcnow()

    def set_description(self, description: str) -> None:
        self.description = description.strip()
        self.update()

    def add_platform(self, platform: str) -> None:
        platform = platform.strip().lower()

        if platform and platform not in self.target_platforms:
            self.target_platforms.append(platform)
            self.update()

    def set_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value
        self.update()

    def get_metadata(self, key: str, default: Any = None) -> Any:
        return self.metadata.get(key, default)

    @property
    def project_path(self) -> Path:
        return self.workspace / self.project_name
