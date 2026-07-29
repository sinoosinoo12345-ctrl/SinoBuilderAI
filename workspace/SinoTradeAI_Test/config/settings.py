from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
def login(data: dict):

    return {
        "success": True,
        "user": data
    }