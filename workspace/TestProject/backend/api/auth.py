from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {
        "token":"demo"
    }

@router.post("/register")
def register():
    return {
        "status":"created"
    }
