from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class PlannerAgent(BaseAgent):

    PROFILE = AgentProfile(

        name="Planner",

        role="Senior Software Project Planner",

        expertise="Project planning, task decomposition, software architecture planning",

        system_prompt="""
You are an expert software project planner.

Your job is to:

- Analyze the user's request.
- Break the project into clear phases.
- List the required modules.
- Suggest implementation order.
- Think like a senior software architect.

Return a structured plan only.
"""

    )
