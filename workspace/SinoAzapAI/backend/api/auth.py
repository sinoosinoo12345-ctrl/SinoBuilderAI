from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")

def login():

    return {

        "success": True

    }


@router.post("/register")

def register():

    return {

        "success": True

    }
