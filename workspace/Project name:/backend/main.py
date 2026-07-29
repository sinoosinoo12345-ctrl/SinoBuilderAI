
from fastapi import FastAPI

app = FastAPI(
    title="Sino Generated API"
)


@app.get("/")
def root():
    return {
        "status": "running"
    }
