import settings
from api import router as api_router
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    """
    This is a factory functions which returns FastAppi app with cors middleware configured
    About cors You can read more here: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(DBSessionMiddleware, custom_engine=engine, commit_on_exit=True)
    app.include_router(api_router, prefix="/api")
    return app


def prepare() -> None:
    import adapters.cleanings.tables


app = get_application()
prepare()
