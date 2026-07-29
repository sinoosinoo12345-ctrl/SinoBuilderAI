from fastapi import FastAPI

app = FastAPI(
    title="Sino Builder AI Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "engine": "Sino Builder AI"
    }
