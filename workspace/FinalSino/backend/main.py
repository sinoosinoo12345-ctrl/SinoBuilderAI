from fastapi import FastAPI


app = FastAPI(
    title="Sino Generated Application"
)


@app.get("/")
def root():

    return {
        "status":"running",
        "engine":"Sino Internal AI"
    }