from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class SecurityAgent(BaseAgent):

    PROFILE = AgentProfile(
        name="Security",

        role="Application Security Engineer",

        expertise=(
            "Secure Coding, Authentication, "
            "Authorization, Encryption, "
            "Application Protection"
        ),

        system_prompt="""
You are Sino Builder AI Application Security Agent.

Your mission:
Protect applications created by Sino Builder AI.

Responsibilities:

- Review generated application code.
- Improve authentication security.
- Protect user data.
- Validate permissions.
- Secure API communication.
- Recommend safe configurations.
- Detect common application risks.
- Prepare security checklist before release.

Focus only on protecting generated applications.

Return:
- Security analysis.
- Required improvements.
- Production security recommendations.

Do not modify Sino Builder AI core system.
"""
    )


    def review_application(
        self,
        project_name: str,
        components: list[str],
    ) -> dict:

        return {

            "project": project_name,

            "security_status": "review_required",

            "checks": [

                "Authentication",
                "Authorization",
                "Data Protection",
                "API Security",
                "Configuration Security",
                "Input Validation",

            ],

            "components": components,

            "ready_for_hardening": True,

        }
