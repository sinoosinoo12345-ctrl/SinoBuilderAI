from pathlib import Path


class ProgrammerAI:

    def run(self, project_path):

        project = Path(project_path)

        frontend = project / "frontend"
        backend = project / "backend"

        # واجهة رئيسية

        (frontend / "pages" / "home.html").write_text(
"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Home</title>
</head>
<body>

<h2>Welcome To Sino Builder AI</h2>

<button onclick="build()">
Build Project
</button>

<script src="../app.js"></script>

</body>
</html>
""",
            encoding="utf-8"
        )

        # API

        (backend / "api" / "routes.py").write_text(
'''from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():

    return {
        "status":"ok"
    }
''',
            encoding="utf-8"
        )

        # Service

        (backend / "services" / "builder.py").write_text(
'''class BuilderService:

    def build(self):

        return "Project Generated"
''',
            encoding="utf-8"
        )

        return {
            "status": "Programming Finished"
        }
