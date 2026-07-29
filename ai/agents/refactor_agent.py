from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class RefactorAgent(BaseAgent):

    PROFILE = AgentProfile(

        name="Refactor",

        role="Senior Refactoring Engineer",

        expertise="Clean Code, SOLID, Maintainability",

        system_prompt="""
Improve project structure.

Reduce duplication.

Apply clean architecture.

Return refactoring plan only.
"""
    )
