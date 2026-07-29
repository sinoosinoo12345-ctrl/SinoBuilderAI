from __future__ import annotations


from ai.agents.planner import Planner
from ai.agents.architect import Architect
from ai.agents.ui_designer import UIDesigner
from ai.agents.backend_agent import BackendAgent
from ai.agents.database_agent import DatabaseAgent
from ai.agents.programmer import ProgrammerAgent
from ai.agents.sino_cyber_ai import SinoCyberAI
from ai.agents.release_agent import ReleaseAgent


class AgentOrchestrator:

    def __init__(self):

        self.agents = {
            "Planner": Planner(),
            "Architect": Architect(),
            "UIDesigner": UIDesigner(),
            "Backend": BackendAgent(),
            "Database": DatabaseAgent(),
            "AI": ProgrammerAgent(),
            "Cyber": SinoCyberAI(),
            "Release": ReleaseAgent(),
        }

    def register(self, name, agent):
        self.agents[name] = agent

    def has_agent(self, name):
        return name in self.agents

    def dispatch(self, task, project_path):

        agent_name = task.get("agent")

        agent = self.agents.get(agent_name)

        if agent is None:
            return {
                "agent": agent_name,
                "status": "missing",
                "result": None,
            }

        try:

            if hasattr(agent, "run"):
                result = agent.run(project_path, task)

            elif hasattr(agent, "execute"):
                result = agent.execute(project_path, task)

            elif hasattr(agent, "generate"):
                result = agent.generate(project_path, task)

            else:
                raise Exception(
                    f"{agent_name} has no executable method."
                )

            return {
                "agent": agent_name,
                "status": "completed",
                "result": result,
            }

        except Exception as e:

            return {
                "agent": agent_name,
                "status": "failed",
                "error": str(e),
            }

    def dispatch_all(self, tasks, project_path):

        results = []

        for task in tasks:
            results.append(
                self.dispatch(
                    task,
                    project_path,
                )
            )

        return results
