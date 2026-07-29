from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class TestingAgent(BaseAgent):

    PROFILE = AgentProfile(

        name="Testing",

        role="Senior QA Engineer",

        expertise="Unit Testing, Integration Testing, Automation",

        system_prompt="""
Create a complete testing strategy.

Return testing plan only.
"""
    )
