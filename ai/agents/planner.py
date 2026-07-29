from pathlib import Path
import json


class Planner:

    def run(self, project_path, description):

        project = Path(project_path)

        docs = project / "docs"

        docs.mkdir(parents=True, exist_ok=True)

        plan = {
            "project": project.name,
            "description": description,
            "goals": [
                "Analyze idea",
                "Create architecture",
                "Generate UI",
                "Generate Backend",
                "Generate Database",
                "Generate AI Modules",
                "Security Review",
                "Testing",
                "Release"
            ],
            "status": "planned"
        }

        file = docs / "plan.json"

        file.write_text(
            json.dumps(plan, indent=4),
            encoding="utf-8"
        )

        return plan
