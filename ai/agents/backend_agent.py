from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile
from builder.code_generator import CodeGenerator


class BackendAgent(BaseAgent):

    PROFILE = AgentProfile(
        name="Backend",

        role="Senior Backend Architect",

        expertise=(
            "FastAPI, APIs, Authentication, "
            "Database Design, Security, AI Services"
        ),

        system_prompt="""
You are Sino Builder AI Backend Architect.

Your mission:
Design production-ready backend systems
for any type of application.

Always consider:

- API architecture.
- Authentication system.
- Authorization.
- Database communication.
- Business logic.
- Security layers.
- Performance.
- Scalability.
- AI service integration.

Never create simple demo backends.
Design systems ready for production.
"""
    )


    def design_backend(
        self,
        project_name: str,
        requirements: list[str],
    ) -> dict:

        return {

            "project": project_name,

            "architecture": {
                "framework": "FastAPI",
                "style": "Production Architecture",
                "async": True,
                "scalable": True,
            },


            "services": [

                {
                    "name": "API Gateway",
                    "purpose": "Application communication layer",
                },

                {
                    "name": "Authentication Service",
                    "purpose": "Secure user access",
                },

                {
                    "name": "Business Logic Service",
                    "purpose": "Application operations",
                },

                {
                    "name": "Database Service",
                    "purpose": "Data management",
                },

                {
                    "name": "AI Service",
                    "purpose": "Intelligent features",
                },

            ],


            "security": [

                "JWT Authentication",
                "Input Validation",
                "Secure Configuration",
                "Permission Control",

            ],


            "requirements": requirements,

            "ready_for_generation": True,

        }


    def run(self, project_path, task):

        generator = CodeGenerator(project_path)

        generator.create_backend()

        generator.create_api()

        return {
            "status": "Backend Generated",
            "project": str(project_path),
            "files": generator.summary()["generated_files"],
        }
