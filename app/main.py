from fastapi import FastAPI

from app.core.config import settings
from app.db.db_config import db
from app.routes.favs import router


def get_app() -> FastAPI:

    app_settings = settings.more_settings.dict()

    app = FastAPI(**app_settings)

    app.add_event_handler("startup", db.initialize_db)
    app.include_router(router)

    return app

app = get_app()