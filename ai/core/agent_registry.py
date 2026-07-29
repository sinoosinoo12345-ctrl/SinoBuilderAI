from __future__ import annotations

from ai.core.agent_factory import AgentFactory

from ai.agents.planner_agent import PlannerAgent
from ai.agents.architect_agent import ArchitectAgent
from ai.agents.backend_agent import BackendAgent
from ai.agents.frontend_agent import FrontendAgent
from ai.agents.database_agent import DatabaseAgent
from ai.agents.testing_agent import TestingAgent
from ai.agents.security_agent import SecurityAgent
from ai.agents.refactor_agent import RefactorAgent
from ai.agents.documentation_agent import DocumentationAgent
from ai.agents.deployment_agent import DeploymentAgent
from ai.agents.reviewer_agent import ReviewerAgent
from ai.agents.debug_agent import DebugAgent
from ai.agents.memory_agent import MemoryAgent
from ai.agents.devops_agent import DevOpsAgent
from ai.agents.project_manager_agent import ProjectManagerAgent


def register_all() -> None:

    AgentFactory.clear()

    agents = {

        "Planner": PlannerAgent,

        "ProjectManager": ProjectManagerAgent,

        "Architect": ArchitectAgent,

        "Backend": BackendAgent,

        "Frontend": FrontendAgent,

        "Database": DatabaseAgent,

        "Testing": TestingAgent,

        "Security": SecurityAgent,

        "Refactor": RefactorAgent,

        "Reviewer": ReviewerAgent,

        "Documentation": DocumentationAgent,

        "Deployment": DeploymentAgent,

        "Memory": MemoryAgent,

        "DevOps": DevOpsAgent,

        "Debug": DebugAgent,

    }

    for name, agent in agents.items():

        AgentFactory.register(
            name,
            agent,
        )
