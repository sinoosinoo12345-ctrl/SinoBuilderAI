from pathlib import Path


class Validator:

    REQUIRED = [
        "frontend",
        "backend",
        "database",
        "config",
        "README.md",
        "requirements.txt",
    ]

    def __init__(self, project_path):

        self.project = Path(project_path)

    def validate(self):

        missing = []

        for item in self.REQUIRED:

            if not (self.project / item).exists():

                missing.append(item)

        return {
            "success": len(missing) == 0,
            "missing": missing,
            "message": (
                "Project structure valid"
                if len(missing) == 0
                else "Missing files detected"
            ),
        }
