from pathlib import Path
import json


class Architect:

    def run(self, project_path):

        project = Path(project_path)

        architecture = {
            "frontend": [
                "assets",
                "components",
                "pages",
                "services"
            ],
            "backend": [
                "api",
                "core",
                "models",
                "services"
            ],
            "database": [
                "models",
                "migrations"
            ],
            "ai": [
                "agents",
                "core"
            ],
            "config": [],
            "docs": []
        }

        for folder, subs in architecture.items():

            root = project / folder

            root.mkdir(parents=True, exist_ok=True)

            for sub in subs:

                (root / sub).mkdir(parents=True, exist_ok=True)

        docs = project / "docs"

        docs.mkdir(exist_ok=True)

        (docs / "architecture.json").write_text(
            json.dumps(architecture, indent=4),
            encoding="utf-8"
        )

        return architecture
