from __future__ import annotations

from pathlib import Path
import shutil


class WorkspaceManager:

    def __init__(self, workspace="workspace"):
        self.workspace = Path(workspace)
        self.workspace.mkdir(exist_ok=True)

    def create(self, project_name: str):
        project = self.workspace / project_name
        project.mkdir(parents=True, exist_ok=True)
        return project

    def exists(self, project_name: str):
        return (self.workspace / project_name).exists()

    def delete(self, project_name: str):
        project = self.workspace / project_name

        if project.exists():
            shutil.rmtree(project)
            return True

        return False

    def list_projects(self):

        projects = []

        for p in self.workspace.iterdir():

            if not p.is_dir():
                continue

            if (p / ".sino_memory.json").exists() or (p / "release.json").exists():
                projects.append(p.name)

        return sorted(projects)

    def path(self, project_name: str):
        return self.workspace / project_name
