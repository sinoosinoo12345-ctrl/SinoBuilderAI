from pathlib import Path


class BackendEngineer:

    def run(self, project_path):

        project = Path(project_path)

        backend = project / "backend"

        (backend / "main.py").write_text(
'''from fastapi import FastAPI

app = FastAPI(title="Generated API")

@app.get("/")
def root():
    return {"message":"Backend Ready"}
''',
            encoding="utf-8"
        )

        (backend / "api" / "__init__.py").write_text("", encoding="utf-8")
        (backend / "core" / "__init__.py").write_text("", encoding="utf-8")
        (backend / "models" / "__init__.py").write_text("", encoding="utf-8")
        (backend / "services" / "__init__.py").write_text("", encoding="utf-8")

        return {
            "status": "Backend Generated"
        }
