from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from engine.execution_engine import ExecutionEngine

app = FastAPI(title="Sino Builder AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BuildRequest(BaseModel):
    project_name: str
    requirements: str


@app.get("/")
def root():
    return {
        "status": "running",
        "engine": "Sino Builder AI"
    }


@app.post("/build")
def build(request: BuildRequest):

    engine = ExecutionEngine()

    result = engine.execute(
        request.project_name,
        request.requirements
    )

    return result


@app.get("/projects")
def projects():

    from pathlib import Path

    workspace = Path("workspace")

    if not workspace.exists():
        return []

    return sorted([
        p.name
        for p in workspace.iterdir()
        if p.is_dir()
    ])
