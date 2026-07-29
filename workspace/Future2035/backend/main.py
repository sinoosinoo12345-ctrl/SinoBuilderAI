from fastapi import FastAPI

app = FastAPI(title="Generated API")

@app.get("/")
def root():
    return {"message":"Backend Ready"}
