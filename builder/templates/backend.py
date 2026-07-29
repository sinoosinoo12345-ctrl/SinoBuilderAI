FASTAPI_MAIN = """
from fastapi import FastAPI

app = FastAPI(
    title="{project}",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "project": "{project}",
        "status": "running"
    }
"""
SETTINGS = """
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "{project}"

    VERSION: str = "1.0.0"

    DEBUG: bool = False

    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str

    CORS_ORIGINS: list[str] = [
        "*"
    ]

    class Config:

        env_file = ".env"

        extra = "ignore"


settings = Settings()
"""
ENV_FILE = """
APP_NAME={project}

SECRET_KEY=CHANGE_ME

DATABASE_URL=sqlite:///app.db
"""
LOGGING = """
import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

)

logger = logging.getLogger("SinoBuilder")
"""
DATABASE = """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
"""
HEALTH = """
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")

def health():

    return {

        "status": "healthy"

    }
"""
EXCEPTIONS = """
from fastapi.responses import JSONResponse


def server_error(message):

    return JSONResponse(

        status_code=500,

        content={

            "success": False,

            "message": message,

        },

    )
"""
SECURITY = """
from passlib.context import CryptContext

pwd = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto",

)


def hash_password(password):

    return pwd.hash(password)


def verify_password(password, hashed):

    return pwd.verify(password, hashed)
"""
JWT = """
from datetime import datetime, timedelta

from jose import jwt


def create_access_token(
    data,
    expires_minutes,
    secret_key,
    algorithm,
):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(
            minutes=expires_minutes
        )
    )

    return jwt.encode(
        payload,
        secret_key,
        algorithm=algorithm,
    )
"""
AUTH_ROUTER = """
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
"""
USER_ROUTER = """
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")

def users():

    return []
"""
AI_ROUTER = """
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
"""
MAIN_APP = """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings

from api.auth import router as auth_router
from api.users import router as users_router
from api.ai import router as ai_router
from api.health import router as health_router


app = FastAPI(

    title=settings.APP_NAME,

    version=settings.VERSION,

)

app.add_middleware(

    CORSMiddleware,

    allow_origins=settings.CORS_ORIGINS,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

app.include_router(

    health_router,

    prefix=settings.API_PREFIX,

)

app.include_router(

    auth_router,

    prefix=settings.API_PREFIX,

)

app.include_router(

    users_router,

    prefix=settings.API_PREFIX,

)

app.include_router(

    ai_router,

    prefix=settings.API_PREFIX,

)
"""
PROJECT_STRUCTURE = [

    "backend/main.py",

    "backend/config/settings.py",

    "backend/database.py",

    "backend/security.py",

    "backend/jwt.py",

    "backend/exceptions.py",

    "backend/api/auth.py",

    "backend/api/users.py",

    "backend/api/ai.py",

    "backend/api/health.py",

]
BACKEND_TEMPLATE = {
    "main": MAIN_APP,
    "settings": SETTINGS,
    "database": DATABASE,
    "logging": LOGGING,
    "jwt": JWT,
    "security": SECURITY,
    "exceptions": EXCEPTIONS,
    "health": HEALTH,
    "auth_router": AUTH_ROUTER,
    "users_router": USER_ROUTER,
    "ai_router": AI_ROUTER,
    "env": ENV_FILE,
    "structure": PROJECT_STRUCTURE,
}
