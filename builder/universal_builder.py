from ai.core.memory_manager import MemoryManager
from ai.core.task_scheduler import TaskScheduler
from ai.core.workspace_manager import WorkspaceManager
from ai.core.dependency_manager import DependencyManager
from ai.core.validator import Validator
from ai.core.release_manager import ReleaseManager
from ai.agents.sino_cyber_ai import SinoCyberAI


class UniversalBuilder:

    def __init__(self):

        self.memory = MemoryManager()
        self.scheduler = TaskScheduler()
        self.workspace = WorkspaceManager()
        self.cyber = SinoCyberAI()

    def build(self, project, description):

        self.workspace.create(project)

        self.memory.update(project, "description", description)

        stages = [
            "Planner",
            "Architect",
            "UIDesigner",
            "Backend",
            "Database",
            "Programmer",
            "Dependencies",
            "Validation",
            "CyberSecurity",
            "Release"
        ]

        for stage in stages:
            self.scheduler.add(stage)

        finished = []

        while self.scheduler.pending():

            task = self.scheduler.next()

            name = task["name"]

            if name == "Dependencies":

                DependencyManager(
                    f"workspace/{project}"
                ).write_requirements()

            elif name == "Validation":

                Validator(
                    f"workspace/{project}"
                ).validate()

            elif name == "CyberSecurity":

                self.cyber.scan_project(
                    f"workspace/{project}"
                )

            elif name == "Release":

                ReleaseManager(
                    f"workspace/{project}"
                ).create_release()

            self.memory.append_log(
                project,
                f"{name} Finished"
            )

            finished.append(name)

        return {
            "project": project,
            "status": "completed",
            "finished": finished
        }
