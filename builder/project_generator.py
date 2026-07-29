from __future__ import annotations

from pathlib import Path

from ai.agents.planner import PlannerAgent
from builder.code_generator import CodeGenerator
from release.release_pipeline import ReleasePipeline


class ProjectGenerator:
    """
    Sino Builder AI
    Full Project Generator V3
    Internal Generation Engine
    """

    def __init__(
        self,
        workspace: str = "workspace",
    ):

        self.workspace = Path(workspace)
        self.workspace.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.planner = PlannerAgent()
        self.release = ReleasePipeline()


    def generate(
        self,
        project_name: str,
        prompt: str,
    ):

        project_path = (
            self.workspace / project_name
        )

        project_path.mkdir(
            parents=True,
            exist_ok=True,
        )


        plan = self.planner.create_plan(
            prompt
        )


        generator = CodeGenerator(
            project_path
        )


        generator.create_backend()
        generator.create_frontend()


        release = self.release.create_release(
            str(project_path),
            project_name,
        )


        return {
            "project": project_name,
            "path": str(project_path),
            "plan": plan.tasks,
            "release": release,
            "status": "generated",
        }
