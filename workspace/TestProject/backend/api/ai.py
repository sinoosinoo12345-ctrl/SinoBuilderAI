from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze")
def analyze():
    return {
        "status":"ready"
    }
