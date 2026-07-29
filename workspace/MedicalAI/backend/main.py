from fastapi import FastAPI


app = FastAPI(
    title="Restaurant Management API"
)


@app.get("/")
def root():

    return {
        "status": "running",
        "service": "restaurant"
    }