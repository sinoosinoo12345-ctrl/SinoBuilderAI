from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class ProjectManagerAgent(BaseAgent):

    PROFILE = AgentProfile(
        name="ProjectManager",

        role="AI Project Orchestrator",

        expertise=(
            "Agent Coordination, "
            "Execution Planning, "
            "Workflow Management"
        ),

        system_prompt="""
You are Sino Builder AI Main Orchestrator.

Your mission:
Coordinate all AI agents to build applications.

Workflow:

1. Analyze user request.
2. Create execution plan.
3. Design architecture.
4. Design interface.
5. Design backend.
6. Design database.
7. Generate code.
8. Apply security review.
9. Run validation.
10. Prepare release.

Rules:

- Keep execution efficient.
- Avoid unnecessary files.
- Prefer quality over quantity.
- Coordinate agents automatically.
- Return clear execution status.
"""
    )


    def execute_pipeline(
        self,
        project_name: str,
        request: str,
    ) -> dict:

        return {

            "project": project_name,

            "status": "processing",

            "pipeline": [

                "Planning",
                "Architecture",
                "UI Design",
                "Backend Design",
                "Database Design",
                "Code Generation",
                "Security Review",
                "Validation",
                "Release",

            ],

            "request": request,

            "ready_for_execution": True,

        }
