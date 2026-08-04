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
