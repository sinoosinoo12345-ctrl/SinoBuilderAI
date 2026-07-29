from fastapi import FastAPI

app = FastAPI(
    title="Sino Builder AI Backend"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "engine": "Sino Builder AI"
    }