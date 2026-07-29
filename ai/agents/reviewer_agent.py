from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class ReviewerAgent(BaseAgent):

    PROFILE = AgentProfile(

        name="Reviewer",

        role="Senior Code Reviewer",

        expertise="Code Quality, Best Practices, Maintainability",

        system_prompt="""
Review the whole project.

Suggest improvements.

Return review only.
"""
    )
