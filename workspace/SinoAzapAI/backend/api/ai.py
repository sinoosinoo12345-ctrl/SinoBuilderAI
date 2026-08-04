from fastapi import APIRouter

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"],
)


@router.get("/status")

def status():

    return {

        "ai": "online"

    }
