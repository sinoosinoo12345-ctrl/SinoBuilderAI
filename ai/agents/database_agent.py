from __future__ import annotations

from ai.agents.base_agent import BaseAgent
from ai.agents.agent_profile import AgentProfile


class DatabaseAgent(BaseAgent):

    PROFILE = AgentProfile(
        name="Database",

        role="Senior Database Architect",

        expertise=(
            "SQL, PostgreSQL, SQLite, NoSQL, "
            "Data Modeling, ER Design"
        ),

        system_prompt="""
You are Sino Builder AI Database Architect.

Your mission:
Design professional database systems
for any application.

Always define:

- Database type selection.
- Entities.
- Tables.
- Relationships.
- Primary keys.
- Foreign keys.
- Indexes.
- Data validation.
- Performance optimization.

Support:
- Mobile applications.
- Web platforms.
- Enterprise systems.
- AI applications.
- Trading systems.
- E-commerce.
- Any custom software.

Never create random tables.
Always design scalable production databases.
"""
    )


    def design_database(
        self,
        project_name: str,
        requirements: list[str],
    ) -> dict:

        return {

            "project": project_name,

            "database": {
                "primary": "PostgreSQL",
                "development": "SQLite",
                "scalable": True,
            },


            "architecture": {

                "entities": [],

                "relationships": [],

                "indexes": [],

                "constraints": [],

            },


            "features": [

                "Data validation",
                "Secure storage",
                "Migration support",
                "Performance optimization",

            ],


            "requirements": requirements,

            "ready_for_generation": True,

        }

    def run(self, project_path, task):

        from builder.code_generator import CodeGenerator

        generator = CodeGenerator(project_path)

        generator.create_database()

        return {
            "status": "Database Generated",
            "generated": generator.summary(),
    }
