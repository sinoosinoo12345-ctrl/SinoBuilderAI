from pathlib import Path

from ai.core.sino_brain import SinoBrain
from ai.core.task_planner import TaskPlanner
from engine.agent_orchestrator import AgentOrchestrator
from release.release_pipeline import ReleasePipeline


class ExecutionEngine:

    def __init__(self):

        self.brain = SinoBrain()
        self.planner = TaskPlanner()
        self.orchestrator = AgentOrchestrator()
        self.release = ReleasePipeline()

    def execute(self, project_name, description):

        project_path = Path("workspace") / project_name
        project_path.mkdir(parents=True, exist_ok=True)

        brain_result = self.brain.think(description)

        spec = brain_result["spec"]

        tasks = self.planner.build(spec)

        results = []

        for task in tasks:

            result = self.orchestrator.dispatch(
                task,
                str(project_path)
            )

            results.append(result)

        completed = sum(
            1 for r in results
            if r["status"] == "completed"
        )

        failed = sum(
            1 for r in results
            if r["status"] == "failed"
        )

        release_result = self.release.create_release(
            project_path=str(project_path),
            project_name=project_name,
        )

        return {

            "success": failed == 0,

            "project": project_name,

            "project_path": str(project_path),

            "brain": brain_result,

            "tasks": len(tasks),

            "completed": completed,

            "failed": failed,

            "results": results,

            "release": release_result,

        }
