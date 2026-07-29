from pathlib import Path

class DependencyManager:

    def __init__(self, project_path):
        self.project = Path(project_path)

    def requirements(self):
        return [
            "fastapi",
            "uvicorn",
            "pydantic",
            "sqlalchemy",
            "python-dotenv",
        ]

    def write_requirements(self):
        self.project.mkdir(parents=True, exist_ok=True)

        req = self.project / "requirements.txt"

        req.write_text(
            "\n".join(self.requirements()),
            encoding="utf-8"
        )

        return req

    def exists(self):
        return (self.project / "requirements.txt").exists()
